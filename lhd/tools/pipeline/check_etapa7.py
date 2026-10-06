#!/usr/bin/env python3
"""Etapa 7 (paso 7.7, v46): verificación de cierre sobre data/all.json (correr después de `python3 tools/build_data.py`).

Uso: python3 tools/pipeline/check_etapa7.py [--estricto]
Informa:
  1. elementos aprobados en el V4 (REVISION-ETAPA7.json, estado aprobado-V4) que no existen en la línea (descartados o pendientes);
  2. movimientos ★ sin ninguna obra ★ visible en su ficha (misma regla que app.js: obras con el movimiento, links.works del
     movimiento y obras de sus diseñadores dentro de las fechas del movimiento);
  3. movimientos e instituciones sin ninguna obra visible;
  4. obras ★ con menos de dos enlaces directos de subcategorías distintas (lista para anotar excepciones C4c, decisión D3);
  5. diseñadores ★ sin obra ★ (lo exige también el build).
Con --estricto termina con código 1 si hay casos en 2 o 5 (los demás son informativos).
"""
import collections, json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
d = json.load(open(os.path.join(BASE, 'data', 'all.json'), encoding='utf-8'))
rev = json.load(open(os.path.join(BASE, 'tools', 'REVISION-ETAPA7.json'), encoding='utf-8'))
ids = {x['id'] for k in ('works', 'designers', 'movements', 'institutions', 'theories', 'contexts', 'production') for x in d[k]}
W = {w['id']: w for w in d['works']}
wbd = collections.defaultdict(list)
for w in d['works']:
    for x in w.get('designers') or []:
        wbd[x].append(w)
NOW = 2026


def members(rec, field_of_designer):
    lk = rec.get('links') or {}
    out = set(lk.get('works') or [])
    if field_of_designer == 'movements':
        out |= {w['id'] for w in d['works'] if rec['id'] in (w.get('movements') or [])}
    if field_of_designer == 'institutions':
        out |= {w['id'] for w in d['works'] if w.get('maker') == rec['id'] or w.get('client') == rec['id']}
    des = set(lk.get('designers') or []) | {a['id'] for a in d['designers'] if rec['id'] in (a.get(field_of_designer) or [])}
    end = rec.get('end') if rec.get('end') is not None else NOW
    for a in des:
        for w in wbd[a]:
            if (rec.get('start') or 0) <= w['year'] <= end:
                out.add(w['id'])
    return {x for x in out if x in W}


bad = 0
falt = [r['id'] for r in rev if r.get('estado') == 'aprobado-V4' and r['id'] not in ids]
print(f'1. Aprobados en el V4 que no están en la línea: {len(falt)}')
for x in falt:
    print('   -', x)
print('2. Movimientos ★ sin obra ★ visible:')
n2 = 0
for m in d['movements']:
    if m.get('macro') or m.get('level') != 'essential':
        continue
    ws = members(m, 'movements')
    if not any(W[w]['level'] == 'essential' for w in ws):
        n2 += 1; print(f"   - {m['id']} ({len(ws)} obras visibles)")
print(f'   total: {n2}')
print('3. Movimientos e instituciones sin obras visibles:')
for k, fld in (('movements', 'movements'), ('institutions', 'institutions')):
    for r in d[k]:
        if r.get('macro'):
            continue
        if not members(r, fld):
            print(f"   - {r['id']}")
ctx = {c['id']: c['track'] for c in d['contexts']}
tr = collections.defaultdict(set)
for l in d['ctxLinks']:
    if l['ctx'] in ctx:
        tr[l['item']].add(ctx[l['ctx']])
falta = [w['id'] for w in d['works'] if w['level'] == 'essential' and len(tr[w['id']]) < 2]
print(f'4. Obras ★ con menos de 2 enlaces directos de subcategorías distintas (anotar como excepción C4c si no hay enlace cierto): {len(falta)}')
for x in falta:
    print(f"   - {x}: {sorted(tr[x]) or 'ninguno'}")
print('5. Diseñadores ★ sin obra ★:')
n5 = 0
for a in d['designers']:
    if a.get('level') == 'essential' and not any(w['level'] == 'essential' for w in wbd[a['id']]):
        n5 += 1; print('   -', a['id'])
print(f'   total: {n5}')
if '--estricto' in sys.argv and (n2 or n5):
    sys.exit(1)
