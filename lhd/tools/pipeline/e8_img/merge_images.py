#!/usr/bin/env python3
"""Merge res/*.json (tandas) into src-images/images.json  {id: [{file, credit, license}]}.
Cleans credits; keeps existing manual entries (key 'manual': true) untouched."""
import json, glob, os, re, html
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
OUT = os.path.join(ROOT, 'src-images', 'images.json')
old = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
def clean_credit(a):
    a = html.unescape(a or '')
    a = re.sub(r'Unknown author.*|AnonymousUnknown.*|No machine-readable.*', '', a).strip()
    return a[:60]
def lic(l):
    l = (l or '').replace('Creative Commons ', 'CC ').strip()
    return {'No restrictions': 'No known restrictions', 'FAL': 'Free Art License', 'Attribution': 'Attribution'}.get(l, l)
out = {}
for f in sorted(glob.glob(os.path.join(HERE, 'res', '*.json'))):
    for r in json.load(open(f, encoding='utf-8'))['picked']:
        iid, file, lc, art = r[:4]
        out[iid] = [{'file': file, 'credit': clean_credit(art), 'license': lic(lc)}]
for iid, lst in old.items():           # manual additions (extra images) survive
    if any(x.get('manual') for x in lst):
        out[iid] = out.get(iid, [])[:1] + [x for x in lst if x.get('manual')]
json.dump(dict(sorted(out.items())), open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print('images.json:', len(out), 'items with image')
