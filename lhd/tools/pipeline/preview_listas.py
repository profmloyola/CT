#!/usr/bin/env python3
"""Etapa 1b: VISTA PREVIA de toda la línea a partir de tools/LISTAS-CIERRE.md (sin tocar src-data/ ni data/).

Uso: python3 tools/pipeline/preview_listas.py [--out DIR] [--listas FILE] [--keep]
  --out DIR     carpeta donde queda el sitio de vista previa (por omisión /tmp/lhd-vista-previa)
  --listas FILE LISTAS-CIERRE.md alternativa (pruebas)
  --zip FILE    además arma un ZIP de la carpeta de salida
  --keep        no borra la carpeta de trabajo temporal

Qué hace: copia el sitio y `src-data/` a una carpeta temporal; agrega, por cada fila de las listas que aún no existe en src-data,
una ficha «en desarrollo» (nombre, años, nivel, regiones, disciplina, enlaces con su línea de mecanismo y conexiones; textos de relleno
iguales en ES y EN, y los nombres en español también en EN); reintegra `ctx-corfo` y `ctx-early-television` desde la reserva; suma a los
macromovimientos (`parts`) los movimientos que la lista les asigna; corre `build_data.py` en esa copia (mismas reglas de validación) y deja
index.html, app.js, style.css, help/ y data/all.json en --out, con una etiqueta fija «VISTA PREVIA». El proyecto real queda intacto.
"""
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import listas_check as LC  # noqa: E402

BASE = LC.BASE
ERAS = [('industrial', 1750, 1851), ('reform', 1851, 1914), ('modernism', 1914, 1945), ('postwar', 1945, 1975), ('postmodern', 1975, 9999)]
NOW = __import__('datetime').date.today().year
PH_ES = 'Ficha en desarrollo: esta vista previa muestra solo la estructura de la línea. El texto de esta ficha aún no está escrito.'
PH_EN = 'Card in development: this preview shows only the structure of the timeline. The text of this card is not written yet.'
DEFAULT_TYPE = {'graphic': 'poster', 'product': 'object', 'fashion': 'garment', 'architecture': 'building'}
SEC_KEY = {'contexts': 'contexts', 'production': 'production', 'theories': 'theories', 'movements': 'movements',
           'institutions': 'institutions', 'designers': 'designers', 'works': 'works'}


def era_of(year):
    for e, a, b in ERAS:
        if a <= year < b:
            return e
    return 'industrial' if year < 1750 else 'postmodern'


def years(cell):
    return [int(x) for x in re.findall(r'\d{4}', cell or '')]


def short_of(name):
    s = re.sub(r'[«»“”"*]', '', name).strip()
    s = re.sub(r'\s*\([^)]*\)', '', s).strip()
    if len(s) <= 22:
        return s
    cut = s[:22].rsplit(' ', 1)[0]
    return cut if len(cut) >= 8 else s[:22]


def disc_list(cell):
    return [x.strip() for x in re.split(r'[,; ]+', cell or '') if x.strip() in LC.DISC]


def build(listas, out_dir, keep=False):
    data = LC.parse([listas])
    work = tempfile.mkdtemp(prefix='lhd-prev-')
    for f in ('index.html', 'app.js', 'style.css'):
        shutil.copy(os.path.join(BASE, f), work)
    if os.path.isdir(os.path.join(BASE, 'help')):
        shutil.copytree(os.path.join(BASE, 'help'), os.path.join(work, 'help'))
    os.makedirs(os.path.join(work, 'tools'))
    shutil.copy(os.path.join(BASE, 'tools', 'build_data.py'), os.path.join(work, 'tools'))
    shutil.copytree(os.path.join(BASE, 'src-data'), os.path.join(work, 'src-data'))
    sd = os.path.join(work, 'src-data')
    exist = LC.ids_src(sd)                    # id -> (clave, tramo)
    notes = []

    # ---- reserva: se reintegran al Modernismo
    res = json.load(open(os.path.join(BASE, 'tools', 'RESERVA-FASE-B.json'), encoding='utf-8'))
    reint = [x for x in res.get('contexts', []) if x['id'] in ('ctx-corfo', 'ctx-early-television') and x['id'] not in exist]
    if reint:
        p = os.path.join(sd, 'modernism', '44-context-technological.json')
        for x in reint:
            f = os.path.join(sd, 'modernism', {'economic': '41-context-economic.json', 'technological': '44-context-technological.json'}[x['track']])
            d = json.load(open(f, encoding='utf-8'))
            d['contexts'].append(x)
            json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
            exist[x['id']] = ('contexts', 'modernism')

    # ---- filas nuevas, por tipo
    rows, kind_of = {}, {}   # id -> fila / clave
    for t, secs in data.items():
        for sec in SEC_KEY:
            for r in secs.get(sec, []):
                i = LC.idof(r['_cells'][0])
                if i:
                    kind_of[i] = sec
                    if i not in exist:
                        rows[i] = (sec, r)
    for i, (k, t) in exist.items():
        kind_of.setdefault(i, k)
    kmap = {'movements': 'movements', 'institutions': 'institutions', 'designers': 'designers', 'works': 'works'}

    lvl = lambda r: 'essential' if LC.col(r, 'nivel') in ('★', '*') else 'normal'
    # obras: primero, para derivar regiones y años de los demás
    works = {i: r for i, (s, r) in rows.items() if s == 'works'}
    by_designer, by_tech = {}, {}
    for i, r in works.items():
        for d in LC.refs(LC.col(r, 'diseñadores', 'disenadores')):
            by_designer.setdefault(d, []).append(i)
        for t in LC.refs(LC.col(r, 'tech')):
            by_tech.setdefault(t, []).append(i)
    work_year = {i: (years(LC.col(r, 'año')) or [1900])[0] for i, r in works.items()}
    work_reg = {i: [g for g in re.split(r'[,; ]+', LC.col(r, 'regiones')) if g in LC.REG] or ['europe'] for i, r in works.items()}

    related = {}   # id -> ids relacionados (de su fila y inversos)
    for i, (s, r) in rows.items():
        for x in LC.refs(LC.col(r, 'relaciona')):
            related.setdefault(i, set()).add(x); related.setdefault(x, set()).add(i)
    for i, r in works.items():
        for x in LC.refs(LC.col(r, 'diseñadores', 'disenadores')) + LC.refs(LC.col(r, 'tech')):
            related.setdefault(x, set()).add(i)
    conn_nb = {}
    for t, secs in data.items():
        for r in secs.get('connections', []):
            a, b = LC.idof(r['_cells'][0]), LC.idof(r['_cells'][1])
            if a and b:
                conn_nb.setdefault(a, set()).add(b); conn_nb.setdefault(b, set()).add(a)

    def regions_of(i, default=('europe',)):
        c = Counter()
        for w in by_designer.get(i, []) + by_tech.get(i, []):
            c.update(work_reg[w])
        for x in related.get(i, ()):
            if x in works:
                c.update(work_reg[x])
        if c:
            top = [g for g, n in c.most_common() if n >= max(1, c.most_common(1)[0][1] // 2)]
            return top[:2]
        return list(default)

    def disc_of(i):
        c = Counter()
        for w in by_designer.get(i, []) + by_tech.get(i, []):
            c[LC.col(works[w], 'disciplina')] += 1
        for x in related.get(i, ()):
            if x in works:
                c[LC.col(works[x], 'disciplina')] += 1
        return [d for d, n in c.most_common(2)] or ['product']

    def typed_links(i):
        lk = {}
        for x in sorted(related.get(i, ())):
            k = kind_of.get(x)
            if k in kmap and x != i:
                lk.setdefault(kmap[k], []).append(x)
        if not lk:
            for x in sorted(conn_nb.get(i, ())):
                k = kind_of.get(x)
                if k in kmap and x != i:
                    lk.setdefault(kmap[k], []).append(x)
        return lk

    def base(i, sec, r, name):
        o = {'id': i, 'name': name, 'short': short_of(name), 'key': PH_EN, 'draft': True,
             'es': {'name': name, 'short': short_of(name), 'key': PH_ES}}
        if sec == 'designers':
            o['es'] = {'key': PH_ES}
        if sec in ('movements', 'institutions', 'designers', 'works', 'theories'):
            o['level'] = lvl(r)
        return o

    new = {e: {k: [] for k in ('contexts', 'production', 'theories', 'movements', 'institutions', 'designers', 'works', 'links', 'connections')} for e, _, _ in ERAS}
    warn = []
    for i, (sec, r) in rows.items():
        cell = r['_cells']
        name = LC.col(r, 'nombre', 'título', 'titulo') or i
        yy = years(LC.col(r, 'años', 'año'))
        trailing = bool(re.search(r'(–|hoy)\s*$', LC.col(r, 'años', 'año')))
        if sec == 'contexts':
            st = max(yy[0], 1750) if yy else 1900
            o = base(i, sec, r, name)
            o.update(track=LC.col(r, 'sub'), start=st, date=LC.col(r, 'años'),
                     regions=[g for g in re.split(r'[,; ]+', LC.col(r, 'regiones')) if g in LC.REG] or ['global'], countries=[])
            if len(yy) > 1 and not re.search(r'hoy', LC.col(r, 'años')):
                o['end'] = yy[1]
            elif trailing or len(yy) == 1 and 'hoy' in LC.col(r, 'años'):
                o['cont'] = True
            o.update(happened=PH_EN, effect=PH_EN)
            o['es'].update(date=o['date'], happened=PH_ES, effect=PH_ES)
            new[era_of(st)]['contexts'].append(o)
        elif sec == 'production':
            st = max(yy[0], 1750) if yy else 1900
            o = base(i, sec, r, name)
            o.update(sub=LC.col(r, 'sub'), start=st, date=LC.col(r, 'años'), regions=regions_of(i), countries=[], links=typed_links(i))
            if len(yy) > 1 and 'hoy' not in LC.col(r, 'años'):
                o['end'] = yy[1]
            else:
                o['cont'] = True
            for f in ('origin', 'enabled', 'change', 'economy', 'relations'):
                o[f] = PH_EN; o['es'][f] = PH_ES
            o['es']['date'] = o['date']
            new[era_of(st)]['production'].append(o)
        elif sec == 'theories':
            y = yy[0] if yy else 1900
            o = base(i, sec, r, name)
            o.update(year=max(y, 1750), date=str(y), genre='criticism', author='Por definir', regions=regions_of(i), countries=[],
                     links=typed_links(i), ideas=[PH_EN], impact=PH_EN)
            o['es'].update(author='Por definir', date=str(y), ideas=[PH_ES], impact=PH_ES)
            new[era_of(max(y, 1750))]['theories'].append(o)
        elif sec == 'movements':
            st = max(yy[0], 1750) if yy else 1900
            o = base(i, sec, r, name)
            o.update(disciplines=disc_of(i), start=st, fadeIn=1, fadeOut=1, regions=regions_of(i), countries=[], traits=[PH_EN], context=PH_EN, shift=PH_EN)
            if len(yy) > 1 and 'hoy' not in LC.col(r, 'años'):
                o['end'] = yy[1]
            o['es'].update(traits=[PH_ES], context=PH_ES, shift=PH_ES)
            new[era_of(st)]['movements'].append(o)
        elif sec == 'institutions':
            st = max(yy[0], 1750) if yy else 1900
            o = base(i, sec, r, name)
            o.update(kind='company', disciplines=disc_of(i), start=st, end=(yy[1] if len(yy) > 1 and 'hoy' not in LC.col(r, 'años') else None),
                     place='Por definir', regions=regions_of(i), countries=[], more=PH_EN, links=typed_links(i))
            o['es'].update(place='Por definir', more=PH_ES)
            new[era_of(st)]['institutions'].append(o)
        elif sec == 'designers':
            raw = LC.col(r, 'años')
            born = yy[0] if yy else None
            died = yy[1] if len(yy) > 1 and not raw.startswith('n') and ('–' in raw) and not raw.rstrip().endswith('–') else None
            wy = [work_year[w] for w in by_designer.get(i, [])]
            if born is None:
                born = (min(wy) - 25) if wy else 1900
                warn.append(f'{i}: sin años de nacimiento en la lista (se usa {born})')
            if raw.startswith('n') or raw.rstrip().endswith('–'):
                died = None
            if wy:
                if born + 12 > min(wy):
                    born = min(wy) - 14
                if died is not None and died + 1 < max(wy):
                    died = max(wy)
            o = base(i, sec, r, name)
            o.update(kind='duo' if '/' in raw or ' y ' in name else 'person', disciplines=disc_list(LC.col(r, 'disciplinas')) or disc_of(i),
                     born=born, died=died, dates=raw, countries=[], regions=regions_of(i), movements=[], institutions=[], more=PH_EN)
            o['es'].update(dates=raw, more=PH_ES)
            lk = typed_links(i)
            o['movements'] = lk.get('movements', []); o['institutions'] = lk.get('institutions', [])
            anchor = (min(wy) if wy else born + 30)
            new[era_of(min(max(anchor, 1750), NOW))]['designers'].append(o)
        elif sec == 'works':
            y = (yy or [1900])[0]
            disc = LC.col(r, 'disciplina')
            o = base(i, sec, r, name)
            o['title'] = name; o['es']['title'] = name
            del o['name']; del o['es']['name']
            allds = LC.refs(LC.col(r, 'diseñadores', 'disenadores'))
            ds = [x for x in allds if kind_of.get(x) == 'designers']
            insts = [x for x in allds if kind_of.get(x) == 'institutions']
            o.update(discipline=disc, type=DEFAULT_TYPE.get(disc, 'object'), designers=ds, year=y, date=str(y),
                     regions=work_reg[i], countries=[], tech=[x for x in LC.refs(LC.col(r, 'tech'))], more=PH_EN, where=[])
            if insts:
                o['maker'] = insts[0]
            elif not ds:
                o['client'] = 'Por definir'
            o['es'].update(date=str(y), more=PH_ES)
            new[era_of(max(y, 1750))]['works'].append(o)
            # enlaces de contexto
            for m in re.finditer(r'`(' + LC.ID + r')`\s*:\s*([^;]+?)(?=;\s*`|$)', LC.col(r, 'contextos')):
                note = m.group(2).strip().rstrip('.')
                lk = {'ctx': m.group(1), 'item': i, 'note': note + '.', 'refs': [], 'es': {'note': note + '.'}}
                new[era_of(max(y, 1750))]['links'].append(lk)
    # conexiones
    for t, secs in data.items():
        for r in secs.get('connections', []):
            a, b = LC.idof(r['_cells'][0]), LC.idof(r['_cells'][1])
            note = LC.col(r, 'línea', 'linea').strip()
            if a and b:
                new[t]['connections'].append({'from': a, 'to': b, 'note': note, 'refs': [], 'es': {'note': note}})

    # ---- contextos sin ninguna obra que los cite: se enlazan a algún elemento de diseño relacionado (nota de relleno)
    design_kinds = ('movements', 'institutions', 'designers', 'works', 'theories')
    linked_ctx = {l['ctx'] for e in new.values() for l in e['links']}
    for l in glob.glob(os.path.join(sd, '*', '80-context-links.json')):
        linked_ctx |= {x['ctx'] for x in json.load(open(l, encoding='utf-8')).get('links', [])}
    for i, (sec, r) in rows.items():
        if sec != 'contexts' or i in linked_ctx:
            continue
        cands = [x for x in sorted(related.get(i, set()) | conn_nb.get(i, set())) if kind_of.get(x) in design_kinds]
        if not cands:
            for x in sorted(related.get(i, ())):
                if kind_of.get(x) == 'production':
                    cands += [w for w in by_tech.get(x, [])][:1]
        if not cands:
            gg = {}
            for a, bs in list(related.items()) + list(conn_nb.items()):
                for b in bs:
                    gg.setdefault(a, set()).add(b); gg.setdefault(b, set()).add(a)
            seen, front = {i}, [i]
            for _ in range(3):
                nxt = []
                for x in front:
                    for y in sorted(gg.get(x, ())):
                        if y not in seen:
                            seen.add(y); nxt.append(y)
                            if kind_of.get(y) in design_kinds and not cands:
                                cands.append(y)
                front = nxt
        if cands:
            e = next(e for e in new if any(c['id'] == i for c in new[e]['contexts']))
            note = 'Relación indicada en la lista de cierre; la línea de mecanismo se escribe con la ficha.'
            new[e]['links'].append({'ctx': i, 'item': cands[0], 'note': note, 'refs': [], 'es': {'note': note}})
            linked_ctx.add(i)
            notes.append(f'{i}: contexto sin obras; enlazado a {cands[0]} (relleno)')
        else:
            warn.append(f'{i}: contexto sin ningún elemento de diseño relacionado')
    # ---- teorías y productivos sin ningún elemento de diseño enlazado (solo relacionados con contextos u otros): vecino más cercano
    graph = {}
    def edge(a, b):
        graph.setdefault(a, set()).add(b); graph.setdefault(b, set()).add(a)
    for a, bs in list(related.items()) + list(conn_nb.items()):
        for b in bs:
            edge(a, b)
    for e in new.values():
        for l in e['links']:
            edge(l['ctx'], l['item'])
    def nearest(i, kinds, hops=3):
        seen, front = {i}, [i]
        for _ in range(hops):
            nxt = []
            for x in front:
                for y in sorted(graph.get(x, ())):
                    if y in seen:
                        continue
                    seen.add(y); nxt.append(y)
                    if kind_of.get(y) in kinds:
                        return y
            front = nxt
        return None
    dk = ('movements', 'institutions', 'designers', 'works')
    for e in new.values():
        for sec in ('theories', 'production'):
            for it in e[sec]:
                lk = it.get('links') or {}
                if not any(lk.get(f) for f in ('movements', 'institutions', 'designers', 'works')):
                    y = nearest(it['id'], dk)
                    if y:
                        it['links'] = {kmap[kind_of[y]]: [y]}
                        notes.append(f"{it['id']}: sin elemento de diseño enlazado en la lista; relleno con {y}")
    # ---- diseñadores ★ sin obra ★: se bajan a Normal en la vista previa (y se avisa)
    star_works = {w for w, r in works.items() if lvl(r) == 'essential'}
    for e in new.values():
        for dsg in e['designers']:
            if dsg['level'] == 'essential' and not any(w in star_works for w in by_designer.get(dsg['id'], [])):
                dsg['level'] = 'normal'
                warn.append(f"{dsg['id']}: diseñador ★ sin ninguna obra ★ en la lista (en la vista previa figura como Normal)")

    # ---- macromovimientos: parts
    macros = {m: [i for i, (s, r) in rows.items() if s == 'movements' and m in LC.refs(LC.col(r, 'relaciona'))]
              for m in ('macro-modernism', 'macro-postmodernism')}
    for f in glob.glob(os.path.join(sd, '*', '*.json')):
        d = json.load(open(f, encoding='utf-8'))
        ch = False
        for mv in d.get('movements', []) or []:
            if mv.get('id') in macros:
                for x in macros[mv['id']]:
                    if x not in mv.setdefault('parts', []):
                        mv['parts'].append(x); ch = True
        if ch:
            json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    # ---- escribir fichas nuevas
    for e, d in new.items():
        d = {k: v for k, v in d.items() if v}
        if d:
            json.dump(d, open(os.path.join(sd, e, '95-vista-previa.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    # ---- construir y copiar
    r = subprocess.run([sys.executable, os.path.join(work, 'tools', 'build_data.py')], capture_output=True, text=True)
    log = (r.stdout + r.stderr).splitlines()
    probs = [l for l in log if l.startswith('PROBLEM')]
    if probs:
        if not keep:
            pass
        print('\n'.join(probs[:60]))
        print(f'{len(probs)} PROBLEM; carpeta de trabajo: {work}')
        return 1, work, log, warn
    os.makedirs(out_dir, exist_ok=True)
    for f in ('index.html', 'app.js', 'style.css'):
        shutil.copy(os.path.join(work, f), out_dir)
    if os.path.isdir(os.path.join(work, 'help')):
        shutil.rmtree(os.path.join(out_dir, 'help'), ignore_errors=True)
        shutil.copytree(os.path.join(work, 'help'), os.path.join(out_dir, 'help'))
    os.makedirs(os.path.join(out_dir, 'data'), exist_ok=True)
    shutil.copy(os.path.join(work, 'data', 'all.json'), os.path.join(out_dir, 'data', 'all.json'))
    # etiqueta fija
    ix = open(os.path.join(out_dir, 'index.html'), encoding='utf-8').read()
    badge = ('<div id="previewBadge" style="position:fixed;left:8px;bottom:8px;z-index:99999;background:#7a1f1f;color:#fff;font:600 12px/1.3 system-ui,sans-serif;'
             'padding:6px 10px;border-radius:6px;box-shadow:0 1px 6px rgba(0,0,0,.35);max-width:70vw;pointer-events:none">'
             'VISTA PREVIA · solo estructura: las fichas nuevas no tienen texto y los nombres están en español también en EN</div>')
    if 'previewBadge' not in ix:
        ix = ix.replace('</body>', badge + '\n</body>')
        ix = ix.replace('<title>', '<title>[Vista previa] ', 1)
    open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8').write(ix)
    d = json.load(open(os.path.join(out_dir, 'data', 'all.json'), encoding='utf-8'))
    st = d['stats']
    L = ['# Informe de la vista previa (etapa 1b)', '',
         'Generado desde `tools/LISTAS-CIERRE.md` + el Modernismo ya recortado. Cada elemento aparece en la época donde **empieza** (año de inicio), '
         'así que las cifras por época pueden diferir en 1 o 2 de las listas por tramo.', '',
         '| Época | Contextos | Productivo | Teoría | Mov. | Inst. | Diseñadores | Obras (★) | Enlaces | Conexiones |', '|---|---|---|---|---|---|---|---|---|---|']
    for e, a, b in ERAS:
        x = st.get(e, {})
        L.append(f"| {e} | {x.get('contexts')} | {x.get('production')} | {x.get('theories')} | {x.get('movements')} | {x.get('institutions')} | "
                 f"{x.get('designers')} | {x.get('works')} ({x.get('stars')}) | {x.get('links')} | {x.get('connections')} |")
    L += ['', f"Total de obras: {len(d['works'])} ({sum(1 for w in d['works'] if w.get('level') == 'essential')} ★) · diseñadores {len(d['designers'])} · contextos {len(d['contexts'])} · "
          f"enlaces de contexto {len(d['ctxLinks'])} · conexiones {len(d['connections'])}.", '',
          '## Cosas que la vista previa dejó a la vista (para revisar en las listas)', '']
    L += [f'- {w}' for w in (warn + notes)] or ['- Ninguna.']
    L += ['', 'Los «relleno» son enlaces o relaciones que la lista no traía hacia un elemento de diseño y que la vista previa completó con el vecino más cercano '
          'para que el sitio construya; en el contenido final se reemplazan por enlaces reales con su línea de mecanismo.', '']
    open(os.path.join(out_dir, 'INFORME-VISTA-PREVIA.md'), 'w', encoding='utf-8').write('\n'.join(L))
    open(os.path.join(out_dir, 'LEEME-VISTA-PREVIA.md'), 'w', encoding='utf-8').write('''# Vista previa de la LHD (etapa 1b)

Es el mismo sitio, con **todos los elementos de las cinco épocas** (contextos, productivo, teoría, movimientos, instituciones, diseñadores y obras)
según `LISTAS-CIERRE.md`. Las fichas nuevas están **en desarrollo**: tienen nombre, años, nivel, disciplina, región y sus enlaces con la línea
de mecanismo, pero no tienen texto; los nombres están en español también en EN. El Modernismo ya recortado conserva sus fichas completas.

Para verla (el navegador necesita un servidor, no abre bien con doble clic): desde esta carpeta, `python3 -m http.server 8000` y abre
http://localhost:8000. No sirve para publicar. Lee `INFORME-VISTA-PREVIA.md` para las cifras y lo que la vista previa tuvo que completar.
''')
    if not keep:
        shutil.rmtree(work, ignore_errors=True)
    return 0, work, log, warn + notes


def main(argv):
    out, listas, keep, zipto = '/tmp/lhd-vista-previa', os.path.join(BASE, 'tools', 'LISTAS-CIERRE.md'), False, None
    it = iter(argv)
    for a in it:
        if a == '--out': out = os.path.abspath(next(it))
        elif a == '--listas': listas = os.path.abspath(next(it))
        elif a == '--keep': keep = True
        elif a == '--zip': zipto = os.path.abspath(next(it))
        else:
            print(__doc__); return 2
    code, work, log, warn = build(listas, out, keep)
    for w in warn:
        print('AVISO', w)
    print('\n'.join(l for l in log if l.startswith(('industrial', 'reform', 'modernism', 'postwar', 'postmodern', 'all.json', 'OK'))))
    if code == 0:
        print('Vista previa lista en', out)
        if zipto:
            if os.path.exists(zipto):
                os.remove(zipto)
            root = os.path.dirname(out)
            subprocess.run(['zip', '-qr', zipto, os.path.basename(out)], cwd=root, check=True)
            print('ZIP:', zipto)
    return code


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
