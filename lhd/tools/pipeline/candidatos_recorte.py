#!/usr/bin/env python3
"""Candidatos al recorte del Modernismo (plan 3.0 y paso 0.7a). Solo LEE src-data/modernism; no cambia nada.

Uso: python3 tools/pipeline/candidatos_recorte.py [--json]
Imprime, por disciplina, las obras Normal recortables (sin ninguna protección de 3.0) de la más a la menos «prescindible»
(menos enlaces de contexto primero; después las repetidas del mismo diseñador, tipo o movimiento), con sus enlaces y diseñadores;
los diseñadores recortables (no ★, y todas sus obras recortables) y los hechos de contexto con su número de enlaces.
Con --json imprime lo mismo como JSON.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import recorte_lib as R


def analyse(m):
    pw, pd_, pc = R.protections(m)
    n = R.link_counts(m)
    works = list(m.items('works'))
    designers = {x['id']: x for x in m.items('designers')}
    free = [w for w in works if w['id'] not in pw and w.get('level') == 'normal']
    freeids = {w['id'] for w in free}
    by_des, by_type = {}, {}
    for w in works:
        for d in w.get('designers') or []:
            by_des[d] = by_des.get(d, 0) + 1
        by_type[w.get('type')] = by_type.get(w.get('type'), 0) + 1
    def repeat(w):   # cuántas otras obras comparten su diseñador o su tipo (más = más repetida)
        a = max([by_des.get(d, 1) - 1 for d in w.get('designers') or []] or [0])
        return a + by_type.get(w.get('type'), 1) - 1
    cand = {}
    for w in free:
        cand.setdefault(w['discipline'], []).append({
            'id': w['id'], 'title': w['title'], 'year': w['year'], 'type': w.get('type'), 'links': n.get(w['id'], 0),
            'designers': w.get('designers') or [], 'repeat': repeat(w)})
    for lst in cand.values():
        lst.sort(key=lambda x: (x['links'], -x['repeat'], x['id']))
    dcand = []
    for did, d in designers.items():
        if did in pd_:
            continue
        mine = [w for w in works if did in (w.get('designers') or [])]
        if all(w['id'] in freeids for w in mine):
            dcand.append({'id': did, 'name': d['name'], 'works': [w['id'] for w in mine], 'links': n.get(did, 0)})
    dcand.sort(key=lambda x: (len(x['works']), x['links'], x['id']))
    ccand = sorted(({'id': c['id'], 'name': c['name'], 'links': n.get(c['id'], 0), 'protected': c['id'] in pc,
                     'links_to_free_works': sum(1 for l in m.links() if l['ctx'] == c['id'] and l['item'] in freeids)}
                    for c in m.items('contexts')), key=lambda x: (x['protected'], x['links'], x['id']))
    return cand, dcand, ccand, (pw, pd_, pc)


def main(argv):
    m = R.Model()
    cand, dcand, ccand, (pw, pd_, pc) = analyse(m)
    if '--json' in argv:
        print(json.dumps({'works': cand, 'designers': dcand, 'contexts': ccand}, ensure_ascii=False, indent=1)); return 0
    total = sum(len(v) for v in cand.values())
    print(f'Obras del Modernismo: {len(list(m.items("works")))} · protegidas: {len(pw)} · recortables (Normal sin protección): {total}')
    for disc in ('graphic', 'product', 'architecture', 'fashion'):
        print(f'\n== {disc}: {len(cand.get(disc, []))} recortables (más prescindibles primero)')
        for x in cand.get(disc, []):
            print(f"  {x['id']:34} {x['year']}  enlaces={x['links']}  repetida={x['repeat']:2}  {x['type'] or '':10} {', '.join(x['designers']) or '-'}  · {x['title']}")
    print(f'\n== Diseñadores recortables (no ★ y todas sus obras recortables): {len(dcand)}')
    for x in dcand:
        print(f"  {x['id']:24} obras={len(x['works'])} enlaces={x['links']}  {x['name']}  [{', '.join(x['works'])}]")
    print('\n== Hechos de contexto por enlaces (los protegidos van al final)')
    for x in ccand:
        print(f"  {x['id']:34} enlaces={x['links']:2} (a obras recortables: {x['links_to_free_works']}){'  PROTEGIDO' if x['protected'] else ''}  {x['name']}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
