"""Funciones comunes de candidatos_recorte.py y recortar.py (plan, 3.0 y paso 0.7): carga de src-data/, protecciones y huérfanos."""
import glob
import json
import os
import re
import unicodedata

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TRAMO = 'modernism'
KEYS = {'movements': 'movement', 'institutions': 'institution', 'designers': 'designer', 'works': 'work', 'contexts': 'context',
        'production': 'production', 'theories': 'theory', 'concepts': 'concept'}


def norm(s):
    s = unicodedata.normalize('NFD', str(s).lower())
    return re.sub(r'[^a-z0-9 ]+', ' ', ''.join(c for c in s if not unicodedata.combining(c))).strip()


class Model:
    """Todos los JSON de src-data/ en memoria (path -> datos). Se puede guardar sobre otra raíz."""

    def __init__(self, root=None):
        self.root = root or os.path.join(BASE, 'src-data')
        self.files = {}
        for f in sorted(glob.glob(os.path.join(self.root, '*', '*.json'))):
            self.files[f] = json.load(open(f, encoding='utf-8'))

    def items(self, key):
        for f, d in self.files.items():
            for x in d.get(key, []) or []:
                if isinstance(x, dict):
                    yield x

    def by_id(self, key):
        return {x['id']: x for x in self.items(key)}

    def all_ids(self):
        ids = {}
        for k, kind in KEYS.items():
            for x in self.items(k):
                ids[x['id']] = kind
        return ids

    def links(self):
        return [l for l in self.items('links')]

    def save(self, root=None):
        root = root or self.root
        for f, d in self.files.items():
            out = os.path.join(root, os.path.relpath(f, self.root))
            os.makedirs(os.path.dirname(out), exist_ok=True)
            with open(out, 'w', encoding='utf-8') as fh:
                json.dump(d, fh, ensure_ascii=False, indent=1)
                fh.write('\n')


def texts_of(o):
    if isinstance(o, dict):
        for v in o.values():
            yield from texts_of(v)
    elif isinstance(o, list):
        for v in o:
            yield from texts_of(v)
    elif isinstance(o, str):
        yield o


def names_of(x):
    out = {x['id']}
    for k in ('title', 'name', 'short'):
        for src in (x, x.get('es') or {}):
            if src.get(k):
                out.add(src[k])
    return {n for n in out if n}


def mentioned(x, haystack):
    """¿Aparece el id o un nombre (≥ 5 letras) del elemento en el texto normalizado?"""
    for n in names_of(x):
        nn = norm(n)
        if x['id'] == n and n in haystack[1]:
            return True
        if len(nn) >= 5 and (' ' + nn + ' ') in haystack[0]:
            return True
    return False


def haystack(m):
    """(texto normalizado, texto crudo) de los macromovimientos y los conceptos."""
    raw = ' '.join(s for k in ('movements', 'concepts') for x in m.items(k) if k == 'concepts' or x.get('macro') for s in texts_of(x))
    return ' ' + norm(raw) + ' ', raw


def protections(m):
    """-> (works, designers, contexts): {id: [motivos]} de lo que NO se puede recortar (plan 3.0)."""
    hay = haystack(m)
    works = {x['id']: x for x in m.items('works')}
    designers = {x['id']: x for x in m.items('designers')}
    contexts = {x['id']: x for x in m.items('contexts')}
    conn_ids = set()
    for c in m.items('connections'):
        conn_ids.update([c['from'], c['to']])
    # obras asociadas a cada movimiento / institución (por sus diseñadores, por links.works y por maker)
    assoc = {}
    for w in works.values():
        for d in w.get('designers') or []:
            for mv in (designers.get(d) or {}).get('movements') or []:
                assoc.setdefault(mv, set()).add(w['id'])
            for ins in (designers.get(d) or {}).get('institutions') or []:
                assoc.setdefault(ins, set()).add(w['id'])
        if w.get('maker') in (m.by_id('institutions')):
            assoc.setdefault(w['maker'], set()).add(w['id'])
    for ins in m.items('institutions'):
        for wid in (ins.get('links') or {}).get('works', []) or []:
            assoc.setdefault(ins['id'], set()).add(wid)
    for mv in m.items('movements'):
        for wid in (mv.get('links') or {}).get('works', []) or []:
            assoc.setdefault(mv['id'], set()).add(wid)
    pw = {}
    for wid, w in works.items():
        why = []
        if w.get('level') == 'essential': why.append('es ★')
        if wid in conn_ids: why.append('citada en una conexión')
        if mentioned(w, hay): why.append('citada en un concepto o macromovimiento')
        if 'latin-america' in (w.get('regions') or []): why.append('de América Latina')
        for k, s in assoc.items():
            if s == {wid}: why.append(f'única obra de {k}')
        if why: pw[wid] = why
    pd_ = {}
    for did, d in designers.items():
        why = []
        if d.get('level') == 'essential': why.append('es ★')
        if why: pd_[did] = why
    pc = {}
    for cid, c in contexts.items():
        if mentioned(c, hay): pc[cid] = ['citado en context_summary / shifts de un macromovimiento']
    return pw, pd_, pc


def link_counts(m):
    n = {}
    for l in m.links():
        n[l['ctx']] = n.get(l['ctx'], 0) + 1
        n[l['item']] = n.get(l['item'], 0) + 1
    return n


def orphans(m):
    """Ids referenciados que ya no existen (lista de textos). Revisa todos los campos que apuntan a ids."""
    ids = set(m.all_ids())
    bad = []
    def chk(owner, field, v):
        for i in ([v] if isinstance(v, str) else v or []):
            if isinstance(i, str) and i not in ids:
                bad.append(f'{owner}.{field} -> {i}')
    for k in KEYS:
        for x in m.items(k):
            for f in ('designers', 'movements', 'institutions', 'tech', 'parts'):
                chk(x['id'], f, x.get(f))
            for f, v in (x.get('links') or {}).items():
                if f in ('movements', 'institutions', 'designers', 'works'):
                    chk(x['id'], 'links.' + f, v)
    for l in m.links():
        chk(f"link {l['ctx']}~{l['item']}", 'ctx', l['ctx']); chk(f"link {l['ctx']}~{l['item']}", 'item', l['item'])
    for c in m.items('connections'):
        chk(f"conn {c['from']}~{c['to']}", 'from', c['from']); chk(f"conn {c['from']}~{c['to']}", 'to', c['to'])
    return bad
