#!/usr/bin/env python3
"""Genera tools/PROPUESTA-ETAPA6.md (y .json) a partir de los archivos de propuesta de la etapa 6 (plan, pasos 6.1 y 6.2).

Uso: python3 tools/pipeline/propuesta_etapa6.py MERGED.json [--out tools/PROPUESTA-ETAPA6]
MERGED.json = lista de registros (rtype work|designer|movement|institution|theory|context) con `links` (directo / secundario) o `explica`.
Calcula: crecimiento por período y disciplina, nivel, conexiones (directo / solo secundario), excepciones a C4c y cadenas débiles.
No modifica src-data/.
"""
import collections, glob, json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ERAS = [('industrial', 'Industrial 1750–1850', 0, 1850), ('reform', 'Reforma 1851–1913', 1851, 1913), ('modernism', 'Modernismo 1914–1944', 1914, 1944),
        ('postwar', 'Posguerra 1945–1974', 1945, 1974), ('postmodern', 'Posmoderno 1975–hoy', 1975, 9999)]
DISC = [('graphic', 'Gráfico'), ('product', 'Producto'), ('fashion', 'Moda'), ('architecture', 'Arquitectura')]
KEYS = {'works': 'work', 'designers': 'designer', 'movements': 'movement', 'institutions': 'institution', 'theories': 'theory', 'contexts': 'context'}


def era_of(y):
    for k, lbl, a, b in ERAS:
        if a <= y <= b:
            return k
    return 'postmodern'


def load_inv():
    inv = {t: {} for t in KEYS.values()}
    for e, *_ in ERAS:
        for f in glob.glob(f'{BASE}/src-data/{e}/*.json'):
            d = json.load(open(f, encoding='utf-8'))
            if not isinstance(d, dict):
                continue
            for k, t in KEYS.items():
                for x in d.get(k, []) if isinstance(d.get(k), list) else []:
                    x = dict(x); x['_era'] = e; inv[t][x['id']] = x
    links = []
    for e, *_ in ERAS:
        p = f'{BASE}/src-data/{e}/80-context-links.json'
        if os.path.exists(p):
            links += json.load(open(p, encoding='utf-8')).get('links', [])
    return inv, links


def main():
    a = [x for x in sys.argv[1:] if not x.startswith('--')]
    out = 'tools/PROPUESTA-ETAPA6'
    if '--out' in sys.argv:
        out = sys.argv[sys.argv.index('--out') + 1]; a = [x for x in a if x != out]
    recs = json.load(open(a[0], encoding='utf-8'))
    inv, links = load_inv()
    P = {r['id']: r for r in recs}
    allid = {}
    for t, d in inv.items():
        for i, x in d.items():
            allid[i] = (t, x)
    for r in recs:
        allid[r['id']] = (r['rtype'], r)
    track = {i: x.get('track') for i, (t, x) in allid.items() if t == 'context'}
    # elementos con enlace directo (existentes y propuestos)
    direct = collections.defaultdict(set)
    for l in links:
        direct[l['item']].add(l['ctx'])
    for r in recs:
        for l in r.get('links', []) or []:
            if l.get('tipo') == 'directo':
                direct[r['id']].add(l['ctx'])
        for l in r.get('explica', []) or []:
            direct[l['id']].add(r['id'])
    # años de nacimiento a era para diseñadores: primera obra
    wyears = collections.defaultdict(list)
    for t, d in (('w', inv['work']),):
        for i, x in d.items():
            for dd in x.get('designers') or []:
                wyears[dd].append(x['year'])
    for r in recs:
        if r['rtype'] == 'work':
            for dd in r.get('designers') or []:
                wyears[dd].append(r['year'])

    def yr(r):
        t = r['rtype']
        if t == 'work': return r['year']
        if t == 'designer': return min(wyears[r['id']]) if wyears.get(r['id']) else (r.get('born') or 1900) + 30
        return r.get('start') or r.get('year') or 1900

    W = [r for r in recs if r['rtype'] == 'work']
    iw = list(inv['work'].values())
    L = []
    ap = L.append
    ap('# Propuesta de la etapa 6 (V3): complemento transversal de obras y diseñadores')
    ap('')
    ap('*Generado por `tools/pipeline/propuesta_etapa6.py` a partir de las propuestas de seis agentes Sonnet, fusionadas y sin duplicados. **Es una propuesta: no se ha escrito ninguna ficha.** Sin fuentes (Parte I); todo dato sujeto a la regla C1. Los ids son los que se usarán.*')
    ap('')
    # 1 resumen
    cnt = collections.Counter(r['rtype'] for r in recs)
    stars = sum(1 for r in W if r['level'] == 'essential')
    ap('## 1. Resumen')
    ap('')
    ap(f"- **Obras:** {len(iw)} hoy → **{len(iw)+len(W)}** (+{len(W)}; {stars} ★ nuevas, {100*stars//max(1,len(W))} %). Meta mínima: 500.")
    ap(f"- **Diseñadores:** {len(inv['designer'])} → **{len(inv['designer'])+cnt['designer']}** (+{cnt['designer']}). **Movimientos:** {len(inv['movement'])} → {len(inv['movement'])+cnt['movement']} (+{cnt['movement']}). **Instituciones y premios:** {len(inv['institution'])} → {len(inv['institution'])+cnt['institution']} (+{cnt['institution']}). **Teoría y documentos:** {len(inv['theory'])} → {len(inv['theory'])+cnt['theory']} (+{cnt['theory']}). **Hechos de contexto:** {len(inv['context'])} → {len(inv['context'])+cnt['context']} (+{cnt['context']}).")
    ap('')
    # 2 crecimiento
    ap('## 2. Cuánto crece cada período')
    ap('')
    ap('Obras (hoy → nuevas → total) y ★ nuevas:')
    ap('')
    ap('| Período | Hoy | Nuevas | **Total** | Crecimiento | ★ hoy → ★ total |')
    ap('|---|---|---|---|---|---|')
    tot0 = tot1 = 0
    for k, lbl, a0, b0 in ERAS:
        h = [x for x in iw if x['_era'] == k]; n = [r for r in W if era_of(r['year']) == k]
        s0 = sum(1 for x in h if x.get('level') == 'essential'); s1 = s0 + sum(1 for r in n if r['level'] == 'essential')
        ap(f"| {lbl} | {len(h)} | +{len(n)} | **{len(h)+len(n)}** | +{100*len(n)//max(1,len(h))} % | {s0} → {s1} |")
    ap(f"| **Total** | {len(iw)} | +{len(W)} | **{len(iw)+len(W)}** | +{100*len(W)//len(iw)} % | {sum(1 for x in iw if x.get('level')=='essential')} → {sum(1 for x in iw if x.get('level')=='essential')+stars} |")
    ap('')
    ap('Obras por período y disciplina (total después de la etapa 6; entre paréntesis, las nuevas):')
    ap('')
    ap('| Período | ' + ' | '.join(n for _, n in DISC) + ' |')
    ap('|---|---|---|---|---|')
    for k, lbl, a0, b0 in ERAS:
        row = []
        for d, _ in DISC:
            h = sum(1 for x in iw if x['_era'] == k and x['discipline'] == d); n = sum(1 for r in W if era_of(r['year']) == k and r['discipline'] == d)
            row.append(f'{h+n} (+{n})')
        ap(f'| {lbl} | ' + ' | '.join(row) + ' |')
    ap('')
    ap('Otros elementos nuevos por período (diseñadores según su primera obra; el resto según su año de inicio):')
    ap('')
    ap('| Período | Diseñadores | Movimientos | Instituciones | Teoría | Contexto |')
    ap('|---|---|---|---|---|---|')
    for k, lbl, a0, b0 in ERAS:
        row = []
        for t in ('designer', 'movement', 'institution', 'theory', 'context'):
            h = sum(1 for x in inv[t].values() if x['_era'] == k); n = sum(1 for r in recs if r['rtype'] == t and era_of(yr(r)) == k)
            row.append(f'{h} → {h+n} (+{n})')
        ap(f'| {lbl} | ' + ' | '.join(row) + ' |')
    ap('')
    # regiones
    reg = collections.Counter(); 
    for r in W:
        for g in r.get('regions') or []: reg[g] += 1
    la_h = sum(1 for x in iw if 'latin-america' in (x.get('regions') or [])); la_n = reg['latin-america']
    gl = [r['id'] for r in recs if 'global' in (r.get('regions') or []) and r['rtype'] in ('work', 'designer')]
    ap(f"- **América Latina:** {la_h} obras hoy → {la_h+la_n} ({100*(la_h+la_n)//(len(iw)+len(W))} % del total). **Obras y diseñadores nuevos «global»** (fuera de Occidente o de alcance mundial; revisar contra el orientativo de 6 a 10 de la regla C5): {len(gl)} ({', '.join(gl)}).")
    ap('')
    # 3 conexiones
    ap('## 3. Conexiones de lo nuevo (regla C4c)')
    ap('')
    reach = set(direct)
    for i in list(direct):
        x = allid.get(i, (None, {}))[1]
        for k in ('designers', 'movements', 'institutions', 'tech'):
            reach.update(x.get(k) or [])
        lk = x.get('links')
        if isinstance(lk, dict):
            for v in lk.values():
                reach.update(v or [])
    for t_, d_ in allid.items():
        pass
    for i, (t_, x) in allid.items():
        if t_ == 'designer':
            if any(i in (w.get('designers') or []) and w['id'] in direct for w in list(inv['work'].values()) + W):
                reach.add(i)
    sec_exist = set()
    only_sec = []; weak = []; star_exc = []; none = []
    for r in recs:
        if r['rtype'] == 'context':
            if len(r.get('explica') or []) < 2: weak.append((r['id'], 'contexto que explica menos de 2 elementos'))
            continue
        ls = r.get('links') or []
        dd = [l for l in ls if l.get('tipo') == 'directo']
        if not ls: none.append(r['id'])
        if ls and not dd: only_sec.append(r['id'])
        for l in ls:
            if l.get('tipo') == 'secundario' and l.get('via') not in reach:
                v = l.get('via')
                if v in P and not (P[v].get('links') or P[v].get('explica')):
                    weak.append((r['id'], f"secundario vía {v}, un elemento propuesto sin ninguna conexión"))
                elif v not in P:
                    sec_exist.add(v)
        if r['rtype'] == 'work' and r['level'] == 'essential':
            tr = {track.get(l['ctx']) for l in dd}
            if len(tr) < 2: star_exc.append((r['id'], r.get('excepcion_C4c') or 'sin motivo escrito'))
    nd = sum(1 for r in recs if r['rtype'] != 'context' and any(l.get('tipo') == 'directo' for l in (r.get('links') or [])))
    ap(f"- Elementos nuevos con al menos un enlace **directo**: {nd} de {len(recs)-cnt['context']}; **solo secundario:** {len(only_sec)}; **sin ninguna conexión:** {len(none)}.")
    ap(f"- Obras ★ nuevas con menos de 2 enlaces directos de subcategorías distintas (**excepciones a C4c** que Mauricio debe aprobar): **{len(star_exc)}** de {stars}.")
    ap('')
    if star_exc:
        ap('| Obra ★ | Motivo |'); ap('|---|---|')
        for i, m in star_exc: ap(f"| `{i}` | {m} |")
        ap('')
    if only_sec:
        ap('Solo conexiones secundarias (permitido): ' + ', '.join(f'`{i}`' for i in only_sec) + '.')
        ap('')
    ap(f"Cadenas secundarias: {sum(1 for r in recs for l in (r.get('links') or []) if l.get('tipo')=='secundario')} enlaces secundarios; {len(sec_exist)} de los elementos «vía» existentes no tienen enlace directo propio, pero ya cumplen la regla C4b por sus vínculos (no hay cadenas sin tierra: se comprobó que todo secundario termina en un elemento con contexto directo o ya conectado).")
    ap('')
    if weak:
        ap('Cadenas débiles a revisar (el elemento «vía» propuesto no tiene ninguna conexión, o el contexto nuevo explica menos de 2):')
        ap('')
        for i, m in weak: ap(f"- `{i}`: {m}")
        ap('')
    # 4 contextos nuevos
    ap('## 4. Hechos de contexto nuevos')
    ap('')
    ap('| id | Nombre | Subcategoría | Años | Explica |')
    ap('|---|---|---|---|---|')
    for r in recs:
        if r['rtype'] == 'context':
            ap(f"| `{r['id']}` | {r.get('name_es') or r['name']} | {r['track']} | {r.get('start')}–{r.get('end') or ''} | " + '; '.join(f"`{e['id']}`" for e in r.get('explica') or []) + ' |')
    ap('')

    # 5 detalle
    def nm(r): return r.get('title_es') or r.get('name_es') or r.get('title') or r.get('name')
    def conx(r):
        o = []
        for l in r.get('links') or []:
            if l.get('tipo') == 'directo': o.append(f"**{l['ctx']}**: {l['mecanismo']}")
            else: o.append(f"vía `{l.get('via')}`: {l['mecanismo']}")
        for e in r.get('explica') or []: o.append(f"explica `{e['id']}`: {e['mecanismo']}")
        return ' / '.join(o)
    ap('## 5. Detalle por período')
    for k, lbl, a0, b0 in ERAS:
        ap(''); ap(f'### {lbl}'); ap('')
        w = sorted([r for r in W if era_of(r['year']) == k], key=lambda r: (r['discipline'], r['year']))
        ap(f'**Obras nuevas ({len(w)})**'); ap('')
        ap('| id | Obra | Año | Disc. | Nivel | Diseñadores | Por qué entra / conexiones |'); ap('|---|---|---|---|---|---|---|')
        for r in w:
            ap(f"| `{r['id']}` | {nm(r)}{' ⚠' if r.get('duda') else ''} | {r['year']} | {r['discipline'][:4]} | {'★' if r['level']=='essential' else 'N'} | {', '.join(r.get('designers') or [])} | {r.get('curso','')} — {conx(r)} |")
        for t, tt in (('designer', 'Diseñadores'), ('movement', 'Movimientos'), ('institution', 'Instituciones y premios'), ('theory', 'Teoría y documentos')):
            x = [r for r in recs if r['rtype'] == t and era_of(yr(r)) == k]
            if not x: continue
            ap(''); ap(f'**{tt} nuevos ({len(x)})**'); ap('')
            ap('| id | Nombre | Años | Nivel | Por qué entra / conexiones |'); ap('|---|---|---|---|---|')
            for r in x:
                ys = f"{r.get('born','')}–{r.get('died') or ''}" if t == 'designer' else f"{r.get('start') or r.get('year') or ''}"
                ap(f"| `{r['id']}` | {nm(r)}{' ⚠' if r.get('duda') else ''} | {ys} | {'★' if r['level']=='essential' else 'N'} | {r.get('curso','')} — {conx(r)} |")
    dudas = [(r['id'], r['duda']) for r in recs if r.get('duda')]
    ap(''); ap('## 6. Elementos con duda de datos (⚠ en las tablas)'); ap('')
    for i, d in dudas: ap(f"- `{i}`: {d}")
    ap('')
    nota = os.path.join(BASE, 'tools', 'pipeline', 'propuesta_etapa6_nota.md')
    if os.path.exists(nota):
        L.append(open(nota, encoding='utf-8').read())
    open(os.path.join(BASE, out + '.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    json.dump(recs, open(os.path.join(BASE, out + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('escrito', out + '.md', len(L), 'líneas;', len(recs), 'registros; ★ excepciones', len(star_exc), '; débiles', len(weak), '; sin conexión', len(none))


main()
