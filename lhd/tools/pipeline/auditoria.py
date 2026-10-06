#!/usr/bin/env python3
"""R1.1: auditoría automática de la LHD (Parte II, sección 10 del plan).

Uso (desde la carpeta lhd):
    python3 tools/pipeline/auditoria.py            # informe en pantalla (resumen + hallazgos por categoría)
    python3 tools/pipeline/auditoria.py -v         # además, la lista completa de ids de cada hallazgo
    python3 tools/pipeline/auditoria.py --md F.md  # escribe el informe completo en un archivo Markdown
    python3 tools/pipeline/auditoria.py --json F   # escribe los hallazgos en JSON
    python3 tools/pipeline/auditoria.py --strict   # código de salida 1 si hay hallazgos de gravedad ERROR
    python3 tools/pipeline/auditoria.py --v1       # definición de terminado de la R2 (PLAN-V1, sección 4): pendientes por categoría;
                                                   # código de salida 1 mientras quede algún pendiente (-v: todos los ids; --json F: a un archivo)

Lee data/all.json (corre antes `python3 tools/build_data.py`). Solo lee; no modifica nada.

Gravedad: ERROR = dato roto (id inexistente, marca [n] sin fuente, elemento desconectado);
          META  = no cumple una meta de C4 (plan, sección 1) y debe anotarse o cubrirse;
          AVISO = a revisar (texto duplicado, ficha larga, etc.).
"""
import argparse
import collections
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ERA_ORDER = ['industrial', 'reform', 'modernism', 'postwar', 'postmodern']
ERA_YEARS = {'industrial': '1750–1850', 'reform': '1851–1913', 'modernism': '1914–1944', 'postwar': '1945–1974', 'postmodern': '1975–hoy'}
DISC = ['graphic', 'product', 'fashion', 'architecture']
REGIONS = ['europe', 'north-america', 'latin-america', 'global']
KINDS = [('works', 'work'), ('designers', 'designer'), ('movements', 'movement'), ('institutions', 'institution'),
         ('theories', 'theory'), ('contexts', 'context'), ('production', 'production'), ('concepts', 'concept')]
DESIGN = ('work', 'designer', 'movement', 'institution', 'theory')
MARK_RE = re.compile(r'\[(\d{1,2})\]')
SKIP = ('refs', 'where', 'sources', 'links', 'designers', 'movements', 'institutions', 'tech', 'parts', 'regions',
        'countries', 'disciplines', 'terms', 'maker', 'client', 'images', 'production')
LEN_KEY, LEN_MORE = 230, 1100      # mismos topes que build_data.py
LEN_LABEL = 22


def load():
    p = os.path.join(ROOT, 'data', 'all.json')
    if not os.path.exists(p):
        sys.exit('No existe data/all.json: corre antes python3 tools/build_data.py')
    return json.load(open(p, encoding='utf-8'))


def texts(o, path=''):
    """(ruta, texto) de todos los textos visibles de un elemento (EN y ES)."""
    if isinstance(o, str):
        yield path, o
    elif isinstance(o, list):
        for x in o:
            yield from texts(x, path)
    elif isinstance(o, dict):
        for k, v in o.items():
            if k in SKIP:
                continue
            yield from texts(v, f'{path}.{k}' if path else k)


class Report:
    def __init__(self):
        self.items = []   # (severity, category, id, message)

    noted = set()

    def add(self, sev, cat, ident, msg=''):
        if sev in ('META', 'ERROR') and ident in self.noted:
            msg = (msg + ' ' if msg else '') + '[anotada]'
        self.items.append((sev, cat, ident, msg))

    def by_cat(self):
        out = collections.OrderedDict()
        for sev, cat, ident, msg in self.items:
            out.setdefault((sev, cat), []).append((ident, msg))
        return out


def annotated():
    """ids citados (entre acentos graves) en los documentos donde se anotan las excepciones C4c."""
    ids = set()
    for f in ('PENDIENTES-FUENTES.md', 'CAMBIOS-PENDIENTES.md', 'LISTAS-CIERRE.md'):
        p = os.path.join(ROOT, 'tools', f)
        if os.path.exists(p):
            for tok in re.findall(r'`([a-z0-9][a-z0-9\-~]+)`', open(p, encoding='utf-8').read()):
                ids.update(tok.split('~'))   # `ctx~obra` (enlaces sin_enlace) anota a los dos
    return ids


def audit(d):
    R = Report()
    NOTED = annotated()
    R.noted = NOTED
    reg = {}                      # id -> (kind, element)
    for key, kind in KINDS:
        for x in d[key]:
            if x['id'] in reg:
                R.add('ERROR', 'id duplicado', x['id'], f'{kind} y {reg[x["id"]][0]}')
            reg[x['id']] = (kind, x)
    era_of = {i: x.get('era') for i, (k, x) in reg.items()}

    # ---------- 1. conteos ----------
    S = collections.OrderedDict()
    for eid in ERA_ORDER:
        row = {}
        for key, kind in KINDS:
            row[kind] = sum(1 for x in d[key] if x.get('era') == eid)
        ws = [w for w in d['works'] if w.get('era') == eid]
        row['stars'] = sum(1 for w in ws if w.get('star'))
        row['disc'] = {x: sum(1 for w in ws if w.get('discipline') == x) for x in DISC}
        row['reg'] = {x: sum(1 for w in ws if x in (w.get('regions') or [])) for x in REGIONS}
        S[eid] = row

    # ---------- 2. fuentes (refs) ----------
    refs = {}
    for key, kind in KINDS:
        tot = len(d[key])
        con = sum(1 for x in d[key] if x.get('refs'))
        st = [x for x in d[key] if x.get('star')]
        refs[kind] = (con, tot, sum(1 for x in st if x.get('refs')), len(st))
    # urls repetidas, que no sean https o de Wikipedia
    for _, (kind, x) in reg.items():
        for n, r in enumerate(x.get('refs') or [], 1):
            u = r.get('url') or ''
            if u and not u.startswith('https://'):
                R.add('ERROR', 'fuente sin https', x['id'], f'refs[{n}] {u}')
            if 'wikipedia.org' in u:
                R.add('AVISO', 'fuente de Wikipedia', x['id'], f'refs[{n}]')
    # R1.2: la fuente de una teoría va en `sources` (texto primario); falta = AVISO hasta que R3 termine las teorías
    # (interruptor STRICT_THEORY_SOURCES en tools/build_data.py).
    for t in d['theories']:
        if not any((r.get('url') or '').startswith('https://') for r in (t.get('sources') or []) + (t.get('refs') or [])):
            R.add('AVISO', 'teoría sin fuente https (pasa a ERROR cuando R3 termine las teorías, R1.2)', t['id'])

    # ---------- 3. ids que no existen ----------
    def chk(owner, field, ids, kinds=None):
        for i in ids or []:
            if i not in reg:
                R.add('ERROR', 'id inexistente', owner, f'{field} → {i}')
            elif kinds and reg[i][0] not in kinds:
                R.add('ERROR', 'id de tipo equivocado', owner, f'{field} → {i} es {reg[i][0]}')
    for w in d['works']:
        chk(w['id'], 'designers', w.get('designers'), ('designer',))
        chk(w['id'], 'movements', w.get('movements'), ('movement',))
        chk(w['id'], 'tech', w.get('tech'), ('production',))
    for x in d['designers']:
        chk(x['id'], 'movements', x.get('movements'), ('movement',))
        chk(x['id'], 'institutions', x.get('institutions'), ('institution',))
    for m in d['movements']:
        chk(m['id'], 'parts', m.get('parts'), ('movement',))
        for k, v in (m.get('links') or {}).items():
            chk(m['id'], f'links.{k}', v)
    for key in ('institutions', 'production', 'theories'):
        for x in d[key]:
            lk = x.get('links') or {}
            for k, v in lk.items():
                chk(x['id'], f'links.{k}', v)
    for c in d['connections']:
        chk(f"conexión {c.get('from')}→{c.get('to')}", 'from/to', [c.get('from'), c.get('to')])
    for ln in d['ctxLinks']:
        chk(f"enlace {ln.get('ctx')}→{ln.get('item')}", 'ctx/item', [ln.get('ctx')], ('context',))
        chk(f"enlace {ln.get('ctx')}→{ln.get('item')}", 'item', [ln.get('item')], DESIGN)

    # ---------- 4. marcas [n] sin cerrar y fuentes sin citar ----------
    for _, (kind, x) in reg.items():
        nref = len(x.get('refs') or [])
        used = set()
        for path, t in texts(x):
            for m in MARK_RE.findall(t):
                n = int(m)
                used.add(n)
                if n < 1 or n > nref:
                    R.add('ERROR', 'marca [n] sin fuente', x['id'], f'[{n}] en {path} (refs tiene {nref})')
            opens = t.count('[') - t.count(']')
            if opens:
                R.add('ERROR', 'corchete sin cerrar', x['id'], f'en {path}')
        for n in range(1, nref + 1):
            if n not in used:
                R.add('AVISO', 'fuente sin citar en el texto', x['id'], f'refs[{n}]')
    for ln in d['ctxLinks']:
        nref = len(ln.get('refs') or [])
        for path, t in texts(ln):
            for m in MARK_RE.findall(t):
                if not 1 <= int(m) <= nref:
                    R.add('ERROR', 'marca [n] sin fuente', f"enlace {ln['ctx']}→{ln['item']}", f'[{m}] en {path}')

    # ---------- 5. conectividad (C4, C4b, C4c) ----------
    ctx_links = collections.defaultdict(list)    # item id -> enlaces de contexto
    ctx_of = collections.defaultdict(list)       # ctx id -> enlaces
    for ln in d['ctxLinks']:
        ctx_links[ln['item']].append(ln)
        ctx_of[ln['ctx']].append(ln)
    conn = collections.defaultdict(int)
    for c in d['connections']:
        conn[c['from']] += 1
        conn[c['to']] += 1
    referenced = collections.defaultdict(int)   # veces que otro elemento lo cita
    for w in d['works']:
        for f in ('designers', 'movements', 'tech'):
            for i in w.get(f) or []:
                referenced[i] += 1
    for x in d['designers']:
        for f in ('movements', 'institutions'):
            for i in x.get(f) or []:
                referenced[i] += 1
    for m in d['movements']:
        for i in m.get('parts') or []:
            referenced[i] += 1
    for key in ('movements', 'institutions', 'production', 'theories'):
        for x in d[key]:
            for v in (x.get('links') or {}).values():
                for i in v or []:
                    referenced[i] += 1

    # 5a. todo hecho de contexto con >= 2 enlaces
    ctx_few = {}
    for c in d['contexts']:
        n = len(ctx_of.get(c['id'], []))
        if n < 2:
            ctx_few[c['id']] = n
            R.add('ERROR' if n == 0 else 'META', 'contexto sin enlaces' if n == 0 else 'contexto con 1 solo enlace (meta: ≥ 2)', c['id'], f'{n} enlace(s)')

    # 5b. obras: directo / indirecto / ninguno (C4b) y ★ con 2 enlaces directos de subcategorías distintas
    track_of = {c['id']: c.get('track') for c in d['contexts']}
    cov = {'direct': 0, 'indirect': 0, 'none': 0}
    cov_era = {e: {'direct': 0, 'indirect': 0, 'none': 0} for e in ERA_ORDER}
    for w in d['works']:
        if ctx_links.get(w['id']):
            k = 'direct'
        else:
            rel = list(w.get('designers') or []) + list(w.get('movements') or []) + list(w.get('tech') or [])
            k = 'indirect' if any(ctx_links.get(i) for i in rel) or w.get('tech') else 'none'
        cov[k] += 1
        cov_era[w['era']][k] += 1
        if k == 'none':
            R.add('META', 'obra sin ningún contexto (ni directo ni indirecto)', w['id'], w['era'])
        if w.get('star'):
            tr = {track_of.get(l['ctx']) for l in ctx_links.get(w['id'], [])}
            if len(ctx_links.get(w['id'], [])) < 2 or len(tr) < 2:
                R.add('META', 'obra ★ sin 2 enlaces directos de subcategorías distintas (excepción C4c a anotar)', w['id'],
                      f"{len(ctx_links.get(w['id'], []))} enlace(s), subcategorías: {', '.join(sorted(t for t in tr if t)) or '—'}")

    # 5c. diseñadores: obras propias, contexto directo/indirecto
    works_of = collections.defaultdict(list)
    for w in d['works']:
        for i in w.get('designers') or []:
            works_of[i].append(w['id'])
    dcov = {'direct': 0, 'indirect': 0, 'none': 0}
    for x in d['designers']:
        if not works_of.get(x['id']):
            R.add('META', 'diseñador sin ninguna obra', x['id'], x['era'])
        if ctx_links.get(x['id']):
            dcov['direct'] += 1
        elif any(ctx_links.get(w) for w in works_of.get(x['id'], [])):
            dcov['indirect'] += 1
        else:
            dcov['none'] += 1
            R.add('META', 'diseñador sin contexto (ni directo ni por sus obras)', x['id'], x['era'])

    # 5d. todo elemento de diseño y productivo con >= 1 enlace propio; nadie desconectado
    own_missing = collections.Counter()
    isolated = []
    for key, kind in KINDS:
        if kind in ('context', 'concept'):
            continue
        for x in d[key]:
            i = x['id']
            own = len(ctx_links.get(i, [])) + conn.get(i, 0) + sum(len(v or []) for v in (x.get('links') or {}).values())
            if kind == 'work':   # C4c: obra → diseñador, movimiento o productivo cuenta como conexión
                own += len(x.get('designers') or []) + len(x.get('movements') or []) + len(x.get('tech') or [])
            if kind == 'designer':
                own += len(works_of.get(i, []))
            if own == 0:
                own_missing[kind] += 1
                if not referenced.get(i):
                    isolated.append(i)
                    R.add('ERROR', 'elemento totalmente desconectado', i, kind)
                elif kind != 'work':
                    R.add('META', f'{kind} sin enlace propio (solo lo citan otros)', i)
    # conceptos: solo una cuenta (no llevan enlaces por diseño)

    # 5e. obras sin diseñador citado que exista, y diseñadores huérfanos de obra ya cubiertos arriba
    # ---------- 6. mecánica del texto (R1.3) ----------
    for _, (kind, x) in reg.items():
        nm = x.get('short') or x.get('title') or x.get('name') or ''
        es = x.get('es') or {}
        nm_es = es.get('short') or es.get('title') or es.get('name') or nm
        if kind in DESIGN or kind in ('context', 'production'):
            for lang, t in (('en', nm), ('es', nm_es)):
                if len(t) > LEN_LABEL and not x.get('short'):
                    R.add('AVISO', 'etiqueta larga sin «short»', x['id'], f'{lang}: {t!r} ({len(t)})')
        for lang, src in (('en', x), ('es', es)):
            k = src.get('key') or ''
            if len(MARK_RE.sub('', k)) > LEN_KEY:
                R.add('AVISO', 'key largo', x['id'], f'{lang}: {len(MARK_RE.sub("", k))} caracteres')
            m = src.get('more') or ''
            if len(MARK_RE.sub('', m)) > LEN_MORE:
                R.add('AVISO', 'ficha larga («more»)', x['id'], f'{lang}: {len(MARK_RE.sub("", m))} caracteres')
        # EN y ES iguales (traducción olvidada)
        for f in ('key', 'more'):
            a, b = (x.get(f) or '').strip(), (es.get(f) or '').strip()
            if a and a == b and len(a) > 40:
                R.add('AVISO', 'texto igual en EN y ES (¿sin traducir?)', x['id'], f)
        if x.get('key') and x.get('more') and x['key'].strip() == x['more'].strip():
            R.add('AVISO', 'key y more idénticos', x['id'])

    # textos duplicados entre elementos distintos
    seen = collections.defaultdict(list)
    for _, (kind, x) in reg.items():
        for f in ('key', 'more', 'happened', 'effect'):
            t = re.sub(r'\s+', ' ', (x.get(f) or '').strip().lower())
            if len(t) > 60:
                seen[t].append(x['id'])
    for t, ids in seen.items():
        if len(ids) > 1:
            R.add('AVISO', 'texto duplicado entre elementos', ids[0], 'también: ' + ', '.join(ids[1:]))
    nl = collections.defaultdict(list)
    for ln in d['ctxLinks']:
        t = re.sub(r'\s+', ' ', (ln.get('note') or '').strip().lower())
        if t:
            nl[t].append(f"{ln['ctx']}→{ln['item']}")
    for t, ids in nl.items():
        if len(ids) > 1:
            R.add('AVISO', 'nota de enlace duplicada', ids[0], 'también: ' + ', '.join(ids[1:]))
    # enlaces y conexiones repetidos
    pairs = collections.Counter((l['ctx'], l['item']) for l in d['ctxLinks'])
    for p, n in pairs.items():
        if n > 1:
            R.add('ERROR', 'enlace de contexto repetido', f'{p[0]}→{p[1]}', f'{n} veces')
    cp = collections.Counter(frozenset((c['from'], c['to'])) for c in d['connections'])
    for p, n in cp.items():
        if n > 1:
            R.add('ERROR', 'conexión repetida', '↔'.join(sorted(p)), f'{n} veces')

    # ---------- 7. imágenes ----------
    for key, kind in (('works', 'obras'), ('designers', 'diseñadores'), ('institutions', 'instituciones'), ('theories', 'teorías')):
        sin = [x['id'] for x in d[key] if not x.get('images')]
        if sin:
            R.add('AVISO', f'{kind} sin imagen (ver audit/INFORME-IMAGENES.md)', f'{len(sin)} de {len(d[key])}')

    return R, S, refs, cov, cov_era, dcov, own_missing


def render(d, R, S, refs, cov, cov_era, dcov, own_missing, verbose, md=False):
    L = []
    h = (lambda s: f'## {s}') if md else (lambda s: f'\n=== {s} ===')
    L.append('# Auditoría LHD (R1.1)' if md else 'AUDITORÍA LHD (R1.1)')
    L.append(f"Datos: data/all.json generado el {d.get('generated')}.")
    L.append(h('1. Elementos por tramo'))
    hdr = ['tramo', 'obras', '★', 'diseñ.', 'mov.', 'inst.', 'teor.', 'ctx', 'prod.', 'conc.']
    rows = [hdr]
    tot = collections.Counter()
    for eid, r in S.items():
        row = [f'{eid} {ERA_YEARS[eid]}', r['work'], r['stars'], r['designer'], r['movement'], r['institution'], r['theory'], r['context'], r['production'], r['concept']]
        rows.append(row)
        for h_, v in zip(hdr[1:], row[1:]):
            tot[h_] += v
    rows.append(['TOTAL'] + [tot[h_] for h_ in hdr[1:]])
    L += table(rows, md)
    L.append(h('2. Obras por disciplina y región (una obra puede tener varias regiones)'))
    rows = [['tramo'] + DISC + REGIONS]
    for eid, r in S.items():
        rows.append([eid] + [r['disc'][x] for x in DISC] + [r['reg'][x] for x in REGIONS])
    rows.append(['TOTAL'] + [sum(r['disc'][x] for r in S.values()) for x in DISC] + [sum(r['reg'][x] for r in S.values()) for x in REGIONS])
    L += table(rows, md)
    nw = len(d['works'])
    la = sum(1 for w in d['works'] if 'latin-america' in (w.get('regions') or []))
    L.append(f'América Latina: {la} de {nw} obras ({100 * la / nw:.1f} %).  ★: {sum(1 for w in d["works"] if w.get("star"))} ({100 * sum(1 for w in d["works"] if w.get("star")) / nw:.1f} %).')
    L.append(h('3. Fuentes (refs)'))
    rows = [['tipo', 'con fuentes', 'total', '%', '★ con fuentes', '★ total']]
    for kind, (c, t, cs, ts) in refs.items():
        rows.append([kind, c, t, f'{100 * c / t:.0f}' if t else '–', cs, ts])
    L += table(rows, md)
    nlinks = sum(1 for l in d['ctxLinks'] if l.get('refs'))
    L.append(f"Enlaces de contexto con fuentes: {nlinks} de {len(d['ctxLinks'])}.  Conexiones con fuentes: {sum(1 for c in d['connections'] if c.get('refs'))} de {len(d['connections'])}.")
    L.append(h('4. Contexto de obras y diseñadores (C4b)'))
    rows = [['tramo', 'directo', 'solo indirecto', 'ninguno']]
    for e, c in cov_era.items():
        rows.append([e, c['direct'], c['indirect'], c['none']])
    rows.append(['TOTAL obras', cov['direct'], cov['indirect'], cov['none']])
    rows.append(['TOTAL diseñadores', dcov['direct'], dcov['indirect'], dcov['none']])
    L += table(rows, md)
    L.append(f"Enlaces por tipo: {len(d['ctxLinks'])} de contexto → diseño; {len(d['connections'])} conexiones.")
    ln = collections.Counter(len([1 for l in d['ctxLinks'] if l['ctx'] == c['id']]) for c in d['contexts'])
    L.append('Contextos según su número de enlaces: ' + ', '.join(f'{k}: {v}' for k, v in sorted(ln.items())))
    if own_missing:
        L.append('Elementos sin enlace propio por tipo: ' + ', '.join(f'{k} {v}' for k, v in own_missing.items()))
    L.append(h('5. Hallazgos'))
    cats = R.by_cat()
    order = {'ERROR': 0, 'META': 1, 'AVISO': 2}
    summary = [['gravedad', 'categoría', 'casos']]
    for (sev, cat), v in sorted(cats.items(), key=lambda kv: (order[kv[0][0]], kv[0][1])):
        summary.append([sev, cat, len(v)])
    nerr = sum(1 for (s, _), v in cats.items() if s == 'ERROR' for _i, m in v if '[anotada]' not in m)
    nmeta = sum(len(v) for (s, _), v in cats.items() if s == 'META')
    nav = sum(len(v) for (s, _), v in cats.items() if s == 'AVISO')
    if len(summary) > 1:
        L += table(summary, md)
    L.append(f'TOTAL: {nerr} ERROR sin anotar · {sum(len(v) for (s_, _), v in cats.items() if s_ == "ERROR") - nerr} ERROR anotados · {nmeta} META · {nav} AVISO')
    if verbose or md:
        for (sev, cat), v in sorted(cats.items(), key=lambda kv: (order[kv[0][0]], kv[0][1])):
            L.append(f'\n### {sev}: {cat} ({len(v)})' if md else f'\n[{sev}] {cat} ({len(v)})')
            for ident, msg in v:
                L.append(f'- `{ident}`' + (f' · {msg}' if msg else '') if md else f'  {ident}' + (f'  {msg}' if msg else ''))
    return '\n'.join(L), (nerr, nmeta, nav)


# ---------- --v1: definición de terminado de la R2 (PLAN-V1, sección 4) ----------
V1_TITLES = [
    ('works', 'obras ★ sin fuentes'), ('designers', 'diseñadores ★ sin fuentes'), ('movements', 'movimientos ★ sin fuentes'),
    ('institutions', 'instituciones ★ sin fuentes'), ('theories', 'teorías ★ sin fuentes'),
    ('contexts', 'hechos de contexto sin fuentes'), ('production', 'productivos sin fuentes'), ('essays', 'ensayos sin fuentes'),
    ('links', 'enlaces de contexto de fichas ★ sin fuentes'), ('connections', 'conexiones de fichas ★ sin fuentes'),
    ('orphan_marks', 'marcas [n] sin fuente (en el alcance)'), ('uncited_refs', 'fuentes sin citar en su texto (en el alcance)'),
    ('open_incidents', 'incidencias abiertas (abierta o decidida sin aplicar)'), ('single_source_works', 'obras ★ con una sola fuente'),
]


def v1_marks(o, refs):
    """(marcas sin fuente, fuentes sin citar) de un registro: las marcas de todos sus textos (EN y ES) contra sus refs."""
    used = {int(m) for _, t in texts(o) for m in MARK_RE.findall(t)}
    n = len(refs or [])
    return sorted(m for m in used if m < 1 or m > n), [k for k in range(1, n + 1) if k not in used]


def v1(d, essays, incidents):
    """Pendientes de la definición de terminado: {clave: [ids]}. `incidents` es la lista de tools/r2_incidencias.json (o None)."""
    star = {x['id'] for k in ('works', 'designers', 'movements', 'institutions', 'theories') for x in d[k] if x.get('star')}
    P = collections.OrderedDict((k, []) for k, _ in V1_TITLES)
    for k in ('works', 'designers', 'movements', 'institutions', 'theories'):
        P[k] = [x['id'] for x in d[k] if x.get('star') and not x.get('refs')]
    P['contexts'] = [x['id'] for x in d['contexts'] if not x.get('refs')]
    P['production'] = [x['id'] for x in d['production'] if not x.get('refs')]
    P['essays'] = [e['id'] for e in essays if not e.get('refs')]
    links = [l for l in d['ctxLinks'] if l['item'] in star]
    conns = [c for c in d['connections'] if c['from'] in star or c['to'] in star]
    P['links'] = [l['ctx'] + '~' + l['item'] for l in links if not l.get('refs')]
    P['connections'] = [c['from'] + '>' + c['to'] for c in conns if not c.get('refs')]
    scope = ([(x['id'], x) for k in ('works', 'designers', 'movements', 'institutions', 'theories') for x in d[k] if x.get('star')]
             + [(x['id'], x) for k in ('contexts', 'production') for x in d[k]] + [(e['id'], e) for e in essays]
             + [(l['ctx'] + '~' + l['item'], l) for l in links] + [(c['from'] + '>' + c['to'], c) for c in conns])
    for ident, o in scope:
        bad, unused = v1_marks({k: v for k, v in o.items() if k != 'refs'}, o.get('refs'))
        if bad:
            P['orphan_marks'].append(f'{ident} [{",".join(map(str, bad))}]')
        if unused:
            P['uncited_refs'].append(f'{ident} refs {",".join(map(str, unused))}')
    if incidents is None:
        P['open_incidents'] = ['(falta tools/r2_incidencias.json: córrelo con r2_incidencias.py)']
    else:
        P['open_incidents'] = [i['id'] + ' ' + i.get('elemento', '') for i in incidents if i.get('estado') in ('abierta', 'decidida')]
    P['single_source_works'] = [x['id'] for x in d['works'] if x.get('star') and len(x.get('refs') or []) == 1]
    return P


def v1_text(P, verbose=False):
    titles = dict(V1_TITLES)
    L = ['LHD v1.0 · definición de terminado de la R2 (pendientes; todo debe quedar en 0)', '']
    for k, ids in P.items():
        L.append(f'  {len(ids):>4}  {titles[k]}')
        if ids and (verbose or len(ids) <= 3):
            L.append('        ' + ', '.join(ids))
        elif ids:
            L.append('        ' + ', '.join(ids[:3]) + f', … (+{len(ids) - 3}; -v para la lista completa)')
    total = sum(len(v) for v in P.values())
    L += ['', f'TOTAL pendientes: {total}  →  ' + ('R2 TERMINADA' if not total else 'R2 NO terminada')]
    return '\n'.join(L), total


def table(rows, md):
    if md:
        out = ['| ' + ' | '.join(str(c) for c in rows[0]) + ' |', '|' + '---|' * len(rows[0])]
        out += ['| ' + ' | '.join(str(c) for c in r) + ' |' for r in rows[1:]]
        return out + ['']
    w = [max(len(str(r[i])) for r in rows) for i in range(len(rows[0]))]
    return ['  ' + '  '.join(str(c).ljust(w[i]) if i == 0 or not str(c).replace('.', '').isdigit() else str(c).rjust(w[i]) for i, c in enumerate(r)) for r in rows]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-v', action='store_true')
    ap.add_argument('--md')
    ap.add_argument('--json')
    ap.add_argument('--strict', action='store_true')
    ap.add_argument('--v1', action='store_true')
    a = ap.parse_args()
    d = load()
    if a.v1:
        pe = os.path.join(ROOT, 'data', 'essays.json')
        essays = json.load(open(pe, encoding='utf-8')).get('essays', []) if os.path.exists(pe) else []
        pi = os.path.join(ROOT, 'tools', 'r2_incidencias.json')
        incidents = json.load(open(pi, encoding='utf-8')).get('incidencias') if os.path.exists(pi) else None
        P = v1(d, essays, incidents)
        text, total = v1_text(P, a.v)
        print(text)
        if a.json:
            json.dump(P, open(a.json, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        sys.exit(1 if total else 0)
    R, S, refs, cov, cov_era, dcov, own_missing = audit(d)
    text, (nerr, nmeta, nav) = render(d, R, S, refs, cov, cov_era, dcov, own_missing, a.v)
    print(text)
    if a.md:
        open(a.md, 'w', encoding='utf-8').write(render(d, R, S, refs, cov, cov_era, dcov, own_missing, True, md=True)[0] + '\n')
        print(f'\nInforme escrito en {a.md}')
    if a.json:
        json.dump([{'sev': s, 'cat': c, 'id': i, 'msg': m} for s, c, i, m in R.items], open(a.json, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    sys.exit(1 if (a.strict and nerr) else 0)


if __name__ == '__main__':
    main()
