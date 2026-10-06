#!/usr/bin/env python3
"""Etapa 7 (pasos 7.4, 7.5 y 7.7): aplica de forma mecánica los ajustes aprobados en el V4 (tools/REVISION-ETAPA7-AJUSTES.json).

Uso (desde la carpeta lhd):
  python3 tools/pipeline/ajustes_etapa7.py estructura --prueba    # ensayo en una copia temporal + build; NO toca src-data/
  python3 tools/pipeline/ajustes_etapa7.py estructura --aplicar   # paso 7.4: escribe en src-data/ y en tools/RESERVA-FASE-B.json
  python3 tools/pipeline/ajustes_etapa7.py relaciones --aplicar   # paso 7.5, después de aplicar cada tanda de fichas nuevas (idempotente)
  python3 tools/pipeline/ajustes_etapa7.py niveles --prueba       # paso 7.7 (cuando ya existen las fichas nuevas)
  python3 tools/pipeline/ajustes_etapa7.py niveles --aplicar

Fase «estructura» (sin redactar texto):
  1. pertenencias de movimientos e instituciones (Anexo D), y las 5 pertenencias que se quitan;
  2. fusiones, retiros, renombres de metadatos (name/short), fechas, pistas y cambio de carpeta;
  3. correcciones de datos (Anexo E);
  4. retiro a la reserva de los 4 elementos de la decisión D7 (y de los diseñadores que quedan sin obra);
  5. reposición desde la reserva de 11 fichas del recorte del Modernismo (con sus enlaces guardados).
Fase «relaciones»: miembros de los movimientos nuevos, obras de las instituciones nuevas, `movements`/`tech`/`institutions` propuestos y
las pertenencias del Anexo D que esperaban una ficha nueva (idempotente).
Fase «niveles»: cambios de nivel del Anexo B (solo cuando ya existen las obras ★ nuevas que exige la regla dura del build).

Lo que exige redactar (textos de los renombrados, Bodoni 1818, ctx-photography, etc.) NO lo hace este script: lo informa al final
como «pendientes de texto» para la redacción (paso 7.5). Todo lo retirado se guarda en RESERVA-FASE-B.json → `etapa7_retirados`.
"""
import copy, glob, json, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ERAS = [('industrial', 0, 1850), ('reform', 1851, 1913), ('modernism', 1914, 1944), ('postwar', 1945, 1974), ('postmodern', 1975, 9999)]
LIST_KIND = {'works': 'work', 'designers': 'designer', 'movements': 'movement', 'institutions': 'institution', 'theories': 'theory',
             'contexts': 'context', 'production': 'production', 'concepts': 'concept'}


def era_of(y):
    for k, a, b in ERAS:
        if a <= y <= b:
            return k
    return 'postmodern'


class Repo:
    def __init__(self, base):
        self.base = base
        self.files = {}      # path -> dict
        self.dirty = set()
        for f in sorted(glob.glob(os.path.join(base, 'src-data', '*', '*.json'))):
            self.files[f] = json.load(open(f, encoding='utf-8'))
        self.resfile = os.path.join(base, 'tools', 'RESERVA-FASE-B.json')
        self.res = json.load(open(self.resfile, encoding='utf-8'))
        self.log, self.todo = [], []
        self.reindex()

    def reindex(self):
        self.idx = {}
        for f, d in self.files.items():
            for k, v in d.items():
                if k in LIST_KIND and isinstance(v, list):
                    for r in v:
                        if isinstance(r, dict) and 'id' in r:
                            self.idx[r['id']] = (f, k, r)

    def get(self, i):
        return self.idx.get(i, (None, None, None))[2]

    def kind(self, i):
        x = self.idx.get(i)
        return LIST_KIND[x[1]] if x else None

    def touch(self, f):
        self.dirty.add(f)

    def file_of(self, i):
        return self.idx[i][0]

    def all_links(self):
        for f, d in self.files.items():
            for l in d.get('links', []) if isinstance(d.get('links'), list) else []:
                yield f, l

    # ---------- primitivas
    def add_to_list(self, rec, field, val, f):
        lst = rec.get(field)
        if lst is None:
            rec[field] = lst = []
        if val not in lst:
            lst.append(val)
            self.touch(f)
            return True
        return False

    def add_link_field(self, rec, field, val, f):
        lk = rec.get('links')
        if not isinstance(lk, dict):
            rec['links'] = lk = {}
        return self.add_to_list(lk, field, val, f)

    def remove_everywhere(self, i, replace=None, skip_fields=()):
        """Quita (o reemplaza) el id i en todas las listas de ids de todos los registros, enlaces y conexiones."""
        n = 0
        for f, d in self.files.items():
            for k, v in d.items():
                if not isinstance(v, list):
                    continue
                for r in v:
                    if not isinstance(r, dict):
                        continue
                    if k == 'links' and 'ctx' in r:
                        continue
                    if k == 'connections':
                        continue
                    for fld, val in list(r.items()):
                        if fld in skip_fields:
                            continue
                        if isinstance(val, list) and i in val:
                            new = [x for x in val if x != i]
                            if replace and replace not in new:
                                new.append(replace)
                            r[fld] = new; n += 1; self.touch(f)
                        elif isinstance(val, dict) and fld in ('links',):
                            for kk, vv in val.items():
                                if isinstance(vv, list) and i in vv:
                                    new = [x for x in vv if x != i]
                                    if replace and replace not in new:
                                        new.append(replace)
                                    val[kk] = new; n += 1; self.touch(f)
        return n

    def stash(self, key, what):
        self.res.setdefault('etapa7_retirados', {}).setdefault(key, []).append(what)

    def retire(self, i, motivo, key):
        f, k, rec = self.idx[i]
        self.files[f][k] = [r for r in self.files[f][k] if r.get('id') != i]
        self.touch(f)
        links, conns = [], []
        for ff, d in self.files.items():
            if isinstance(d.get('links'), list):
                keep = []
                for l in d['links']:
                    if l.get('ctx') == i or l.get('item') == i:
                        links.append(l); self.touch(ff)
                    else:
                        keep.append(l)
                d['links'] = keep
            if isinstance(d.get('connections'), list):
                keep = []
                for c in d['connections']:
                    if c.get('from') == i or c.get('to') == i:
                        conns.append(c); self.touch(ff)
                    else:
                        keep.append(c)
                d['connections'] = keep
        refs = self.remove_everywhere(i)
        self.stash(key, {'motivo': motivo, 'tipo': LIST_KIND[k], 'registro': rec, 'links': links, 'connections': conns})
        self.reindex()
        self.log.append(f'retirado {i} ({motivo}): {len(links)} enlaces, {len(conns)} conexiones, {refs} referencias')

    def repoint(self, old, new):
        """Reemplaza old por new en enlaces y conexiones (sin duplicar)."""
        n = 0
        for f, d in self.files.items():
            if isinstance(d.get('links'), list):
                for l in d['links']:
                    if l.get('item') == old:
                        l['item'] = new; n += 1; self.touch(f)
            if isinstance(d.get('connections'), list):
                for c in d['connections']:
                    for e in ('from', 'to'):
                        if c.get(e) == old:
                            c[e] = new; n += 1; self.touch(f)
        return n

    def move(self, i, era):
        f, k, rec = self.idx[i]
        dest = os.path.join(self.base, 'src-data', era, os.path.basename(f))
        if dest == f:
            return
        self.files[f][k] = [r for r in self.files[f][k] if r.get('id') != i]
        if dest not in self.files:
            self.files[dest] = {k: []}
        self.files[dest].setdefault(k, []).append(rec)
        self.touch(f); self.touch(dest)
        self.reindex()
        self.log.append(f'movido {i} → src-data/{era}/{os.path.basename(f)}')

    def move_file(self, i, basename):
        f, k, rec = self.idx[i]
        dest = os.path.join(os.path.dirname(f), basename)
        if dest == f:
            return
        self.files[f][k] = [r for r in self.files[f][k] if r.get('id') != i]
        if dest not in self.files:
            self.files[dest] = {k: []}
        self.files[dest].setdefault(k, []).append(rec)
        self.touch(f); self.touch(dest)
        self.reindex()

    def save(self):
        for f in sorted(self.dirty):
            os.makedirs(os.path.dirname(f), exist_ok=True)
            with open(f, 'w', encoding='utf-8') as fh:
                json.dump(self.files[f], fh, ensure_ascii=False, indent=1)
                fh.write('\n')
        with open(self.resfile, 'w', encoding='utf-8') as fh:
            json.dump(self.res, fh, ensure_ascii=False, indent=1)
            fh.write('\n')


def clean_id(x):
    return x.split(' ')[0]


def pertenencias(R, A):
    """Anexo D: agrega las pertenencias que faltan (idempotente: se puede correr de nuevo cuando existan las fichas nuevas)."""
    pend = []
    for m, lst in A['pertenencia_movimientos'].items():
        if m.startswith('_'):
            continue
        if not R.get(m):
            pend.append(f'{m} (movimiento nuevo: sus miembros se fijan al crearlo en 7.5)')
            continue
        for x in lst:
            if x.startswith('—'):
                continue
            i = clean_id(x)
            k = R.kind(i)
            if not k:
                pend.append(f'{m} ← {i} (ficha nueva: el campo `movements` va en su registro de 7.5)')
                continue
            rec, f = R.get(i), R.file_of(i)
            if k in ('work', 'designer'):
                if R.add_to_list(rec, 'movements', m, f):
                    R.log.append(f'pertenencia: {i} → {m}')
            elif k == 'institution':
                if R.add_link_field(R.get(m), 'institutions', i, R.file_of(m)):
                    R.log.append(f'pertenencia: {m}.links.institutions ← {i}')
            elif k == 'theory':
                if R.add_link_field(rec, 'movements', m, f):
                    R.log.append(f'pertenencia: {i}.links.movements ← {m}')
    gray = R.get('eileen-gray')
    if gray and R.add_to_list(gray, 'movements', 'international-style', R.file_of('eileen-gray')):
        R.log.append('pertenencia: eileen-gray → international-style')
    # 1b. pertenencias de instituciones
    for inst, lst in A['pertenencia_instituciones'].items():
        if inst.startswith('_'):
            continue
        irec = R.get(inst)
        if not irec:
            pend.append(f'{inst} (institución nueva)')
            continue
        for x in lst:
            if x.startswith('(') or x.startswith('—'):
                continue
            i = clean_id(x)
            k = R.kind(i)
            if not k:
                pend.append(f'{inst} ← {i} (ficha nueva: agregar al crearla)')
                continue
            if k == 'work':
                if R.add_link_field(irec, 'works', i, R.file_of(inst)):
                    R.log.append(f'institución: {inst}.links.works ← {i}')
            elif k == 'designer':
                if R.add_to_list(R.get(i), 'institutions', inst, R.file_of(i)):
                    R.log.append(f'institución: {i}.institutions ← {inst}')
            elif k == 'theory':
                if R.add_link_field(R.get(i), 'institutions', inst, R.file_of(i)):
                    R.log.append(f'institución: {i}.links.institutions ← {inst}')

    return pend


def fase_estructura(R, A):
    # 1. pertenencias de movimientos ------------------------------------------------------------
    quitar = [('illustrated-poster', 'hokusai-great-wave-1831'), ('international-typographic-style', 'windows-phone-metro-2010'),
              ('brutalism-metabolism', 'lina-bo-bardi'), ('brutalism-metabolism', 'kurokawa'), ('brutalism-metabolism', 'nakagin-capsule-tower'),
              ('art-deco', 'eileen-gray')]
    for m, i in quitar:
        rec = R.get(i)
        if not rec:
            continue
        f = R.file_of(i)
        if m in (rec.get('movements') or []):
            rec['movements'] = [x for x in rec['movements'] if x != m]; R.touch(f)
            R.log.append(f'pertenencia quitada: {i} ✕ {m}')
        mv = R.get(m)
        if mv and isinstance(mv.get('links'), dict):
            for kk in ('works', 'designers'):
                if i in (mv['links'].get(kk) or []):
                    mv['links'][kk] = [x for x in mv['links'][kk] if x != i]; R.touch(R.file_of(m))
                    R.log.append(f'pertenencia quitada: {m}.links.{kk} ✕ {i}')
    pend = pertenencias(R, A)

    # 2. fusiones, retiros, renombres, fechas, pistas -----------------------------------------------
    if R.get('social-architecture'):
        n = R.repoint('social-architecture', 'participatory-social-architecture')
        R.remove_everywhere('social-architecture', replace='participatory-social-architecture')
        R.retire('social-architecture', 'fusionado con participatory-social-architecture', 'fusiones')
        R.log.append(f'fusión social-architecture → participatory-social-architecture ({n} enlaces/conexiones repuntados)')
    if R.get('iconic-architecture'):
        R.retire('iconic-architecture', 'duplica ctx-star-architecture', 'retiros')
    if R.get('droog-design'):
        R.add_link_field(R.get('inst-droog'), 'works', 'rag-chair-1991', R.file_of('inst-droog'))
        R.remove_everywhere('droog-design')
        R.retire('droog-design', 'duplica inst-droog', 'retiros')
    if R.get('inst-archigram'):
        n = R.repoint('inst-archigram', 'archigram')
        R.remove_everywhere('inst-archigram')
        R.retire('inst-archigram', 'duplica el diseñador colectivo archigram', 'retiros')
        R.log.append(f'inst-archigram → archigram ({n} enlaces/conexiones repuntados)')
    if R.get('bentwood'):
        R.remove_everywhere('bentwood', replace='steam-bentwood')
        n = R.repoint('bentwood', 'steam-bentwood')
        R.retire('bentwood', 'duplica steam-bentwood', 'fusiones')
    ren = {
        'brutalism-metabolism': ('Brutalism', 'Brutalism', 'Brutalismo', 'Brutalismo'),
        'futurism-typography': ('Futurism', 'Futurism', 'Futurismo', 'Futurismo'),
        'punk-fashion': ('Punk', 'Punk', 'Punk', 'Punk'),
        'ctx-gothic-revival': ('Romantic medievalism and religious revival', 'Romantic medievalism', 'Medievalismo romántico y renovación religiosa', 'Medievalismo romántico'),
        'prestressed-concrete': ('Prestressed concrete and thin shells', 'Prestressed concrete', 'Hormigón pretensado y cáscaras delgadas', 'Hormigón pretensado'),
    }
    for i, (n_en, s_en, n_es, s_es) in ren.items():
        rec = R.get(i)
        if not rec:
            continue
        rec['name'], rec['short'] = n_en, s_en
        rec.setdefault('es', {})
        rec['es']['name'], rec['es']['short'] = n_es, s_es
        R.touch(R.file_of(i)); R.log.append(f'renombrado {i} → {n_es}')
    fut = R.get('futurism-typography')
    if fut:
        fut['start'] = 1909
        for x in ('architecture', 'fashion', 'product'):
            if x not in fut['disciplines']:
                fut['disciplines'].append(x)
        R.touch(R.file_of('futurism-typography'))
        R.move('futurism-typography', 'reform')
    punk = R.get('punk-fashion')
    if punk and 'graphic' not in punk['disciplines']:
        punk['disciplines'].append('graphic'); R.touch(R.file_of('punk-fashion'))
    for i, st in (('international-style', 1925), ('postmodern-architecture', 1964), ('landscape-urbanism', 1982)):
        rec = R.get(i)
        if rec and rec.get('start') != st:
            rec['start'] = st; R.touch(R.file_of(i)); R.log.append(f'fecha: {i}.start = {st}')
            if era_of(st) != os.path.basename(os.path.dirname(R.file_of(i))):
                R.move(i, era_of(st))
    for i in ('ctx-great-exhibition', 'ctx-paris-1900'):
        rec = R.get(i)
        if rec and rec.get('track') != 'cultural':
            rec['track'] = 'cultural'; R.touch(R.file_of(i))
            R.move_file(i, '43-context-cultural.json'); R.log.append(f'pista: {i} → cultural')
    th = R.get('th-speculative-everything')
    if th and R.get('critical-speculative-design'):
        if R.add_link_field(th, 'movements', 'critical-speculative-design', R.file_of('th-speculative-everything')):
            R.log.append('th-speculative-everything.links.movements ← critical-speculative-design')

    # 3. correcciones de datos -------------------------------------------------------------------
    def setf(i, **kv):
        rec = R.get(i)
        if not rec:
            return None
        for k, v in kv.items():
            if k.startswith('es_'):
                rec.setdefault('es', {})[k[3:]] = v
            else:
                rec[k] = v
        R.touch(R.file_of(i)); R.log.append(f'corrección {i}: {", ".join(kv)}')
        return rec
    setf('bodoni-manuale-1788', year=1818, date='1818', title='Bodoni’s Manuale tipografico (1818)', es_title='Manuale tipografico de Bodoni (1818)', es_date='1818', posthumous=True)   # requiere el ajuste del build del paso 7.3 (campo `posthumous`)
    if setf('werkbund-cologne-1914', year=1914, date='1914', es_date='1914'):
        R.move('werkbund-cologne-1914', 'modernism')
    if setf('th-werkbund-debate', year=1914, date='1914', es_date='1914'):
        R.move('th-werkbund-debate', 'modernism')
    t14 = R.get('thonet-chair-14')
    if t14 and 'michael-thonet' not in (t14.get('designers') or []):
        setf('thonet-chair-14', designers=['michael-thonet'] + (t14.get('designers') or []))
    if setf('jatiya-sangsad-dhaka-1982', designers=['louis-kahn'], year=1962, date='1962–1982', es_date='1962–1982'):
        R.move('jatiya-sangsad-dhaka-1982', 'postwar')
    setf('seattle-library-2004', maker='OMA (Rem Koolhaas and Joshua Prince-Ramus) with LMN Architects')
    setf('brasilia-cathedral', maker='Oscar Niemeyer; structure by Joaquim Cardozo')
    setf('museo-antropologia-mexico', maker='Pedro Ramírez Vázquez with Rafael Mijares and Jorge Campuzano')
    pz = R.get('prozodezhda-1922')
    if pz and 'SU' in (pz.get('countries') or []):
        setf('prozodezhda-1922', countries=['RU' if c == 'SU' else c for c in pz['countries']])

    # 4. D7: a la reserva (y diseñadores que quedan sin obra) -----------------------------------
    d7 = [r['id'] for r in A['candidatos_reserva_aprobados_V4']]
    huerfanos = set()
    for i in d7:
        rec = R.get(i)
        if not rec:
            continue
        huerfanos |= set(rec.get('designers') or [])
        R.retire(i, 'decisión D7 del V4', 'reserva_D7')
    for dz in sorted(huerfanos):
        if R.get(dz) and not any(dz in (w.get('designers') or []) for f, d in R.files.items() for w in d.get('works', []) if isinstance(w, dict)):
            R.retire(dz, 'diseñador sin obras tras la decisión D7', 'reserva_D7')

    # 5. reposiciones desde la reserva -----------------------------------------------------------
    rm = R.res.get('recorte_modernismo', {})
    want = set(A['reposiciones']['recorte_modernismo'])
    disc_file = {'graphic': '20-works-graphic.json', 'product': '21-works-product.json', 'fashion': '22-works-fashion.json', 'architecture': '23-works-architecture.json'}
    repuestos = []
    for k in ('designers', 'works'):
        keep = []
        for rec in rm.get(k, []):
            if rec.get('id') in want and not R.get(rec['id']):
                rec = copy.deepcopy(rec)
                rec.pop('_file', None)
                era = 'modernism'
                fn = disc_file[rec['discipline']] if k == 'works' else '10-designers.json'
                dest = os.path.join(R.base, 'src-data', era, fn)
                R.files.setdefault(dest, {k: []}).setdefault(k, []).append(rec)
                R.touch(dest); repuestos.append(rec['id'])
            else:
                keep.append(rec)
        rm[k] = keep
    R.reindex()
    # enlaces guardados del recorte
    keepl = []
    linkfile = os.path.join(R.base, 'src-data', 'modernism', '80-context-links.json')
    for l in rm.get('links', []):
        if l.get('item') in repuestos and R.get(l['ctx']):
            R.files[linkfile]['links'].append(l); R.touch(linkfile)
        else:
            keepl.append(l)
    rm['links'] = keepl
    keepi = []
    for e in rm.get('ids_in_links', []):
        ids = [x for x in e['ids'] if x in repuestos]
        own = R.get(e['owner'])
        if ids and own:
            for x in ids:
                if e['field'] in ('works', 'designers', 'movements', 'institutions') and isinstance(own.get('links'), dict):
                    R.add_link_field(own, e['field'], x, R.file_of(e['owner']))
                else:
                    R.add_to_list(own, e['field'], x, R.file_of(e['owner']))
            rest = [x for x in e['ids'] if x not in repuestos]
            if rest:
                keepi.append({**e, 'ids': rest})
        else:
            keepi.append(e)
    rm['ids_in_links'] = keepi
    R.res['recorte_modernismo'] = rm
    R.log.append(f'repuestos desde la reserva: {", ".join(repuestos)}')
    return pend


def fase_relaciones(R, A):
    """Paso 7.5 (después de aplicar las fichas nuevas): fija las relaciones que los agentes no escriben en otros registros:
    miembros de los movimientos nuevos, obras de las instituciones nuevas, `movements`/`tech`/`institutions` propuestos en
    REVISION-ETAPA7.json y las pertenencias del Anexo D que quedaron pendientes por falta de la ficha."""
    REV = [r for r in json.load(open(os.path.join(R.base, 'tools', 'REVISION-ETAPA7.json'), encoding='utf-8')) if r.get('estado') == 'aprobado-V4']
    pend = []
    for r in REV:
        if not R.get(r['id']):
            pend.append(f"{r['id']} (aún no existe: falta redactarla o se descartó)")
            continue
        rec, f = R.get(r['id']), R.file_of(r['id'])
        if r['rtype'] == 'movement':
            for i in r.get('miembros', []):
                k = R.kind(i)
                if k in ('work', 'designer'):
                    if R.add_to_list(R.get(i), 'movements', r['id'], R.file_of(i)):
                        R.log.append(f"miembro: {i} → {r['id']}")
                elif k == 'institution':
                    R.add_link_field(rec, 'institutions', i, f)
                elif k == 'theory':
                    R.add_link_field(R.get(i), 'movements', r['id'], R.file_of(i))
                elif not k:
                    pend.append(f"{r['id']} ← {i} (no existe)")
        if r['rtype'] == 'institution':
            for i in r.get('obras', []):
                if R.kind(i) == 'work' and R.add_link_field(rec, 'works', i, f):
                    R.log.append(f"institución nueva: {r['id']}.links.works ← {i}")
        if r['rtype'] in ('work', 'designer'):
            for fld in ('movements', 'tech', 'institutions'):
                for i in r.get(fld, []) or []:
                    if R.get(i) and R.add_to_list(rec, fld, i, f):
                        R.log.append(f"{r['id']}.{fld} ← {i}")
        if r['rtype'] == 'production':
            for i in r.get('anclas', []):
                if R.kind(i) == 'work' and R.add_to_list(R.get(i), 'tech', r['id'], R.file_of(i)):
                    R.log.append(f"{i}.tech ← {r['id']}")
                if R.kind(i) == 'work' and R.add_link_field(rec, 'works', i, f):   # v48: el build exige que el productivo ligue una obra
                    R.log.append(f"productivo nuevo: {r['id']}.links.works ← {i}")
    pend += pertenencias(R, A)
    return pend


def fase_niveles(R, A):
    pend = []
    for key in ('niveles_obras_sube', 'niveles_obras_baja', 'niveles_disenadores_sube', 'niveles_disenadores_baja',
                'niveles_movimientos', 'niveles_instituciones', 'niveles_teoria'):
        for r in A[key]:
            rec = R.get(r['id'])
            if not rec:
                pend.append(f"{r['id']} (no existe)")
                continue
            if rec.get('level') != r['a']:
                rec['level'] = r['a']; R.touch(R.file_of(r['id'])); R.log.append(f"nivel {r['id']}: {r['de']} → {r['a']}")
    return pend


def build(base):
    p = subprocess.run([sys.executable, os.path.join(base, 'tools', 'build_data.py')], cwd=base, capture_output=True, text=True)
    out = p.stdout + p.stderr
    probs = [l for l in out.splitlines() if 'PROBLEM' in l and not l.startswith('OK')]
    return out.strip().splitlines()[-1] if out.strip() else '', probs


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ('estructura', 'relaciones', 'niveles') or sys.argv[2] not in ('--prueba', '--aplicar'):
        print(__doc__); sys.exit(2)
    fase, modo = sys.argv[1], sys.argv[2]
    A = json.load(open(os.path.join(HERE, 'tools', 'REVISION-ETAPA7-AJUSTES.json'), encoding='utf-8'))
    base = HERE
    if modo == '--prueba':
        tmp = tempfile.mkdtemp(prefix='lhd-etapa7-')
        base = os.path.join(tmp, 'lhd')
        shutil.copytree(HERE, base, ignore=shutil.ignore_patterns('__pycache__', '*.pyc', 'ediciones'))
        os.makedirs(os.path.join(base, 'ediciones'), exist_ok=True)
    R = Repo(base)
    pend = {'estructura': fase_estructura, 'relaciones': fase_relaciones, 'niveles': fase_niveles}[fase](R, A)
    R.save()
    last, probs = build(base)
    print(f'== {fase} {modo}: {len(R.log)} cambios; {len(R.dirty)} archivos')
    for l in R.log:
        print('  ' + l)
    if pend:
        print(f'== pendientes para la redacción (7.5) o para después ({len(pend)}):')
        for p in pend:
            print('  - ' + p)
    if fase == 'estructura':
        print('== pendientes de TEXTO (los redacta un agente en 7.5; ver GUIA-EJECUCION-ETAPA7.md, sección 4.3):')
        for t in ['bodoni-manuale-1788: título y textos a la edición de 1818', 'brutalism-metabolism → Brutalismo: key, traits, context, shift sin el metabolismo',
                  'futurism-typography → Futurismo: key, traits, context, shift ampliados a arquitectura, moda y objeto (conservar las marcas [n] existentes)',
                  'punk-fashion → Punk: key y traits con la gráfica', 'ctx-gothic-revival: key acorde al nuevo nombre',
                  'jatiya-sangsad-dhaka-1982: revisar el texto con Kahn como autor', 'werkbund-cologne-1914 y th-werkbund-debate: revisar que el texto diga 1914',
                  'international-style / postmodern-architecture / landscape-urbanism: revisar fechas en los textos']:
            print('  - ' + t)
    print('== build:', last)
    for p in probs[:30]:
        print('  ' + p)
    if modo == '--prueba':
        print(f'(ensayo en {base}; src-data/ real sin cambios)')
    sys.exit(1 if probs else 0)


if __name__ == '__main__':
    main()
