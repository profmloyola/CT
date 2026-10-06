#!/usr/bin/env python3
"""Validate one essay file in e8_work/out against ids of data/all.json (same rules as build_data)."""
import json, re, sys, os
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
d = json.load(open(R + '/data/all.json'))
kind = {i[0]: i[2] for i in d['items']}; era = {i[0]: i[1] for i in d['items']}
disc = {w['id']: w['discipline'] for w in d['works']}; wiki = {w['id']: bool(w.get('wiki')) for w in d['works']}
LR = re.compile(r'\[\[([a-z0-9_.\-]+)(?:\|[^\]]*)?\]\]')
for eid in sys.argv[1:]:
    e = json.load(open(f'{R}/tools/pipeline/e8_work/out/{eid}.json')); P = []
    n = len(e['paras']); lo, hi = (6, 10) if e['kind'] == 'lens' else (8, 12)
    if not lo <= n <= hi: P.append(f'{n} paras')
    if len(e['es']['paras']) != n: P.append('es paras count')
    for l, ps in (('en', e['paras']), ('es', e['es']['paras'])):
        for i, p in enumerate(ps):
            if len(p) > 1100: P.append(f'{l} para {i+1}: {len(p)} chars')
    a = [m for p in e['paras'] for m in LR.findall(p)]; b = [m for p in e['es']['paras'] for m in LR.findall(p)]
    if sorted(a) != sorted(b): P.append('ids differ en/es: ' + str(set(a) ^ set(b)))
    for m in set(a) | set(b):
        if m not in kind: P.append('unknown id ' + m)
    ds = set(a); ks = {kind.get(m) for m in ds}
    if len(ds) < 15: P.append(f'{len(ds)} distinct ids')
    if 'context' not in ks or not ks & {'movement', 'work'} or not ks & {'designer', 'institution'}: P.append('kinds ' + str(ks))
    if len({era.get(m) for m in ds}) < 4: P.append('eras')
    if not 4 <= len(e['images']) <= 8: P.append('images count')
    for im in e['images']:
        if kind.get(im) != 'work': P.append('image not work ' + im)
        elif not wiki[im]: print('WARN image without wiki', im)
    if e['kind'] == 'discipline':
        off = [m for m in ds if kind.get(m) == 'work' and disc.get(m) != e['target']]
        if off: P.append('works of other disciplines: ' + ', '.join(off))
    print(eid, 'ids', len(ds), 'kinds', sorted(ks))
    print('\n'.join('PROBLEM: ' + p for p in P) or 'OK')
