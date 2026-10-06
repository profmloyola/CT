"""Build the LHD data (Línea de Historia del Diseño).

Usage: python3 tools/build_data.py [-v] [era-id ...]

Reads every folder src-data/<era-id>/*.json, merges the lists, validates them against the rules of
tools/SPEC.md (section 6) and writes ONE file, data/all.json: the whole continuous line 1750–today
(eras, every element, context links, connections, search index and statistics per era).

Continuous model (v11): each element appears once, in the folder of the era where its start year falls
(start >= era.start and start < era.end; the last era runs to today). Its end may lie in a later era:
the timeline draws it whole (long bars are shortened on screen to point + label + arrow, which is only
visual). There are no discipline lanes: the discipline lives in the work (and in the "disciplines" list
of movements, institutions and designers).

List keys in the source files: tracks, movements, institutions, designers, works, contexts,
production, theories, concepts, links (context links), connections. The key "era" is a single object.

Output lines:
  PROBLEM  blocks the era (exit code 1).
  WARN     does not block; review it.
"""
import datetime
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ERA_ORDER = ['industrial', 'reform', 'modernism', 'postwar', 'postmodern']
NOW = datetime.date.today().year

TRACKS = ['political', 'economic', 'social', 'cultural', 'technological']
DISCIPLINES = ['graphic', 'product', 'fashion', 'architecture']
REGIONS = ['europe', 'north-america', 'latin-america', 'global']
PROD_SUBS = ['materials', 'processes', 'tools']
INST_KINDS = ['school', 'company', 'studio', 'exhibition', 'association', 'museum', 'publication']
DESIGNER_KINDS = ['person', 'duo', 'collective']
GENRES = ['manifesto', 'criticism', 'history', 'method', 'pedagogy', 'typography', 'architecture', 'society']
WORK_TYPES = {
    'graphic': ['poster', 'typeface', 'book', 'magazine', 'identity', 'logo', 'signage', 'infographic', 'map', 'stamp', 'banknote',
                'package', 'interface', 'cartel', 'tipografia', 'libro', 'revista', 'identidad', 'logotipo', 'senaletica', 'mapa',
                'sello', 'envase', 'typography', 'icon', 'cover', 'illustration', 'print', 'album', 'pictogram'],
    'product': ['furniture', 'chair', 'lamp', 'utensil', 'appliance', 'device', 'machine', 'vehicle', 'toy', 'tool', 'object', 'instrument',
                'mueble', 'lampara', 'utensilio', 'aparato', 'maquina', 'vehiculo', 'juguete', 'kitchenware', 'tableware', 'watch', 'bottle', 'ceramics'],
    'fashion': ['garment', 'collection', 'accessory', 'textile', 'footwear', 'prenda', 'coleccion', 'accesorio', 'calzado', 'dress', 'fragrance', 'costume'],
    'architecture': ['building', 'housing', 'interior', 'complex', 'city', 'edificio', 'vivienda', 'conjunto', 'ciudad', 'pavilion', 'estate', 'infrastructure'],
}
LEVELS = ['essential', 'normal']   # v24: two detail levels (essential = ★); «complete» was merged into normal
LEVEL_RANK = {k: i for i, k in enumerate(LEVELS)}
THEORY_TEXT = ('name', 'short', 'author', 'key', 'impact')

# text fields that need a Spanish translation (inside "es")
FIELDS = {
    'movement': ['name', 'short', 'key', 'context', 'shift', 'traits', 'more', 'shifts', 'context_summary'],
    'institution': ['name', 'short', 'key', 'more', 'place'],
    'designer': ['key', 'more', 'dates'],
    'work': ['title', 'short', 'key', 'more', 'materials', 'date', 'status', 'production'],
    'context': ['name', 'short', 'key', 'happened', 'effect', 'date'],
    'production': ['name', 'short', 'key', 'origin', 'enabled', 'change', 'economy', 'relations', 'date'],
    'theory': ['name', 'short', 'author', 'key', 'ideas', 'impact', 'date'],
    'concept': ['name', 'key'],
}
# fields that must exist in English (PROBLEM when missing); the rest give a WARN when missing
REQUIRED = {
    'movement': ['name', 'key'],
    'institution': ['name', 'key'],
    'designer': ['name', 'key'],
    'work': ['title', 'key'],
    'context': ['name', 'key', 'happened', 'effect'],
    'production': ['name', 'key'],
    'theory': ['name', 'author', 'key', 'ideas', 'impact'],
    'concept': ['name', 'key'],
}
RECOMMENDED = {
    'movement': ['traits', 'context', 'shift'],
    'institution': ['more'],
    'designer': ['more'],
    'work': ['more'],
    'production': ['origin', 'enabled', 'change', 'relations'],
}
KEYS = {  # source key -> kind
    'movements': 'movement', 'institutions': 'institution', 'designers': 'designer', 'works': 'work',
    'contexts': 'context', 'production': 'production', 'theories': 'theory', 'concepts': 'concept',
}
DESIGN_KINDS = ('movement', 'institution', 'designer', 'work', 'theory')  # v18: theory is design
LIST_KEYS = list(KEYS) + ['tracks', 'links', 'connections']
# recommended maximum lengths (WARN)
LEN_KEY, LEN_NOTE, LEN_EFFECT, LEN_LONG = 230, 240, 480, 1100
# R1.2 (Parte II): while R3 has not finished the theories, a theory without a source link is only a WARN.
# When R3 ends, set this to True: it becomes a PROBLEM again (as it was before v31).
STRICT_THEORY_SOURCES = False
LEN_NAME = 40  # names and titles (cards, chips)
LEN_LABEL = 22  # timeline labels (short, or name/title when there is no short): very short (v11)

verbose = '-v' in sys.argv
only = [a for a in sys.argv[1:] if not a.startswith('-')]


def load_era(folder):
    out = {k: [] for k in LIST_KEYS}
    out['era'] = None
    problems = []
    for f in sorted(glob.glob(os.path.join(folder, '*.json'))):
        try:
            part = json.load(open(f, encoding='utf-8'))
        except Exception as ex:  # noqa: BLE001
            problems.append(f"{os.path.basename(f)}: invalid JSON ({ex})")
            continue
        for k, v in part.items():
            if k == 'era':
                out['era'] = v
            elif k in LIST_KEYS and isinstance(v, list):
                for it in v:
                    if isinstance(it, dict):
                        it['_file'] = os.path.basename(f)
                out[k].extend(v)
            else:
                problems.append(f"{os.path.basename(f)}: unknown key {k}")
    return out, problems


eras, all_problems, all_warns = {}, [], []
for eid in ERA_ORDER:
    folder = os.path.join(ROOT, 'src-data', eid)
    if not os.path.isdir(folder):
        all_problems.append(f"[{eid}] missing folder src-data/{eid}")
        continue
    data, probs = load_era(folder)
    eras[eid] = data
    all_problems += [f"[{eid}] {p}" for p in probs]
for d in glob.glob(os.path.join(ROOT, 'src-data', '*')):
    if os.path.isdir(d) and os.path.basename(d) not in ERA_ORDER:
        all_problems.append(f"unknown era folder {os.path.basename(d)}")

# ---------- global registry ----------
reg = {}  # id -> (era, kind)
for eid, d in eras.items():
    if not d['era']:
        all_problems.append(f"[{eid}] missing 'era' in 01-structure.json")
        d['era'] = {'id': eid, 'start': 0, 'end': 0}
    if d['era'].get('end') == 'now':
        d['era']['end'] = NOW
    if d['era'].get('id') != eid:
        all_problems.append(f"[{eid}] era.id must be {eid}")
    seen_local = set()
    for key, kind in KEYS.items():
        for it in d[key]:
            iid = it.get('id')
            if not iid or not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', iid):
                all_problems.append(f"[{eid}] {kind} has a bad id: {iid!r} (lower-case ascii, hyphens)")
                continue
            if iid in reg:
                where = reg[iid][0]
                all_problems.append(f"[{eid}] duplicate id {iid}" + ('' if where == eid else f" (also in era {where})"))
            reg[iid] = (eid, kind)
            seen_local.add(iid)


def kind_of(i):
    return reg[i][1] if i in reg else None


def era_of(i):
    return reg[i][0] if i in reg else None


def txt(v):
    return v if isinstance(v, str) and v.strip() else None


def check_es(eid, kind, it, probs, warns):
    label = f"{kind} {it.get('id')}"
    if kind != 'concept':
        check_refs(eid, label, it, probs, warns)
    es = it.get('es')
    if not isinstance(es, dict):
        probs.append(f"{label}: missing 'es'")
        return
    allowed = FIELDS[kind]
    for f in REQUIRED[kind]:
        if not it.get(f):
            probs.append(f"{label}: missing {f}")
    for f in RECOMMENDED.get(kind, []):
        if not it.get(f):
            warns.append(f"{label}: no {f}")
    for f in allowed:
        if f == 'production':
            en = (it.get('production') or {}).get('note')
            es_v = (es.get('production') or {}).get('note') if isinstance(es.get('production'), dict) else None
            if en and not es_v:
                probs.append(f"{label}: missing es.production.note")
            if es_v and not en:
                probs.append(f"{label}: es.production.note without English note")
            continue
        en, es_v = it.get(f), es.get(f)
        if isinstance(en, dict) or isinstance(es_v, dict):   # e.g. context_summary of a macro-movement (checked there)
            continue
        if isinstance(en, list) or isinstance(es_v, list):
            if (en or []) and not es_v:
                probs.append(f"{label}: missing es.{f}")
            elif len(en or []) != len(es_v or []):
                probs.append(f"{label}: es.{f} has a different number of items than the English one")
            continue
        if en and not txt(es_v):
            probs.append(f"{label}: missing es.{f}")
        if es_v and not en:
            probs.append(f"{label}: es.{f} has no English counterpart")
    for f in es:
        if f not in allowed:
            probs.append(f"{label}: es.{f} is not a translatable field")
    # names, titles, short labels and dates: no parentheses (use ':' or '·'); timeline labels stay short
    for f in ('name', 'title', 'short', 'date', 'author', 'dates'):
        for v, lang in ((it.get(f), 'en'), (es.get(f), 'es')):
            if isinstance(v, str) and '(' in v:
                warns.append(f"{label}: {lang} {f} has parentheses ({v[:40]!r}); use ':' or '·' instead")
    # running text starts with a capital letter
    for f in ('key', 'more', 'happened', 'effect', 'status', 'context', 'shift', 'impact', 'origin', 'enabled', 'change', 'economy', 'relations'):
        for v, lang in ((it.get(f), 'en'), (es.get(f), 'es')):
            if isinstance(v, str) and v.strip() and v.strip()[0].isalpha() and v.strip()[0].islower():
                warns.append(f"{label}: {lang} {f} starts with a lowercase letter ({v[:30]!r})")
    # names are short by themselves: no ':' with an explanation (it goes in the text), and not long
    for f in ('name', 'title'):
        for v, lang in ((it.get(f), 'en'), (es.get(f), 'es')):
            if isinstance(v, str) and kind != 'concept':
                if ':' in v:
                    warns.append(f"{label}: {lang} {f} has an explanation after ':' ({v[:40]!r}); keep the name short and put the explanation in the text")
                elif len(v) > LEN_NAME:
                    warns.append(f"{label}: {lang} {f} is long ({len(v)} chars); shorten it and move the detail to the text")
    for v, lang in ((it.get('short') or it.get('title') or it.get('name') or '', 'en'),
                    (es.get('short') or es.get('title') or es.get('name') or '', 'es')):
        if kind != 'concept' and len(v) > LEN_LABEL:
            warns.append(f"{label}: {lang} timeline label is long ({len(v)} chars); add a 'short' of a few words")
    # lengths
    k = MARK_RE.sub('', it.get('key') or '')
    if len(k) > LEN_KEY:
        warns.append(f"{label}: key is long ({len(k)} chars; aim for ~130–160)")
    if len(MARK_RE.sub('', es.get('key') or '')) > LEN_KEY + 30:
        warns.append(f"{label}: es.key is long ({len(MARK_RE.sub('', es['key']))} chars)")
    if kind == 'context' and len(it.get('effect') or '') > LEN_EFFECT:
        warns.append(f"{label}: effect is long ({len(it['effect'])} chars; 1–3 sentences)")
    for f in ('more', 'happened', 'origin', 'enabled', 'change', 'impact', 'context', 'shift', 'economy', 'relations'):
        if len(MARK_RE.sub('', it.get(f) or '')) > LEN_LONG:
            warns.append(f"{label}: {f} is long ({len(MARK_RE.sub('', it[f]))} chars)")


def check_geo(label, it, probs, need_regions=True):
    regs = it.get('regions')
    if need_regions and (not isinstance(regs, list) or not regs):
        probs.append(f"{label}: needs regions")
    for r in regs or []:
        if r not in REGIONS:
            probs.append(f"{label}: bad region {r}")
    for c in it.get('countries', []) or []:
        if not re.fullmatch(r'[A-Z]{2}', str(c)):
            probs.append(f"{label}: bad country code {c}")
    w = it.get('wiki')
    if w and (' ' in w or w.startswith('http')):
        probs.append(f"{label}: wiki must be an English Wikipedia page title with underscores")


def era_end(era):
    """Last start year allowed in an era: the year before the next era starts; the last era runs to today."""
    i = ERA_ORDER.index(era['id']) if era.get('id') in ERA_ORDER else -1
    return NOW if i == len(ERA_ORDER) - 1 else era['end'] - 1


def in_era(era, it, label, probs, field='start'):
    """The start year decides the era (start >= era.start and start < era.end). The end may be later."""
    y = it.get(field)
    if not isinstance(y, int):
        probs.append(f"{label}: needs an integer {field}")
        return
    if y < era['start'] or y > era_end(era):
        probs.append(f"{label}: {field} {y} is outside the era {era['start']}–{era_end(era)}; move it to the folder of the era where it starts")
    e = it.get('end')
    if e is not None:
        if not isinstance(e, int):
            probs.append(f"{label}: end must be an integer or null")
        elif e < y:
            probs.append(f"{label}: end before start")
        elif e > NOW:
            probs.append(f"{label}: end {e} is in the future")


def valid_refs(label, ids, kinds, probs):
    for i in ids or []:
        if i not in reg:
            probs.append(f"{label}: unknown id {i}")
        elif kinds and reg[i][1] not in kinds:
            probs.append(f"{label}: {i} is a {reg[i][1]}, expected {'/'.join(kinds)}")


# ---------- sources (v21, point 44): numbered refs and [n] markers ----------
MARK_RE = re.compile(r'\[(\d{1,2})\]')
NO_MARK_FIELDS = ('id', 'name', 'title', 'short', 'wiki', 'img', 'url', 'label')
SKIP_FIELDS = ('refs', 'where', 'sources', 'links', 'designers', 'movements', 'institutions', 'tech', 'parts',
               'regions', 'countries', 'disciplines', 'terms', 'maker', 'client', '_file')
refs_missing = {}  # era -> number of elements without refs


def collect_marks(o, out, path=''):
    """Every [n] marker in the text fields of an element (EN and ES)."""
    if isinstance(o, str):
        out.extend((int(m), path) for m in MARK_RE.findall(o))
    elif isinstance(o, list):
        for x in o:
            collect_marks(x, out, path)
    elif isinstance(o, dict):
        for k, v in o.items():
            if k in SKIP_FIELDS:
                continue
            collect_marks(v, out, f"{path}.{k}" if path else k)


def check_refs(eid, label, it, probs, warns, count_missing=True):
    refs = it.get('refs')
    if refs is None or refs == []:   # v31: refs: [] (Part I) also counts as «no sources yet»
        if count_missing:
            refs_missing[eid] = refs_missing.get(eid, 0) + 1
        refs = []
    if not isinstance(refs, list):
        probs.append(f"{label}: refs must be a list")
        return
    for n, r in enumerate(refs, 1):
        if not isinstance(r, dict) or not r.get('label') or not r.get('checks'):
            probs.append(f"{label}: refs[{n}] needs label and checks")
            continue
        u = r.get('url')
        if u is not None and not str(u).startswith('https://'):
            probs.append(f"{label}: refs[{n}] url must be https ({u})")
        if u and 'wikipedia.org' in u:
            warns.append(f"{label}: refs[{n}] is Wikipedia (not a verification source)")
        if r.get('date') and not re.fullmatch(r'\d{4}-\d{2}-\d{2}', str(r['date'])):
            probs.append(f"{label}: refs[{n}] date must be YYYY-MM-DD")
    marks = []
    collect_marks(it, marks)
    used = set()
    for n, path in marks:
        if n < 1 or n > len(refs):
            probs.append(f"{label}: marker [{n}] in {path} has no source (refs has {len(refs)})")
        used.add(n)
    for f in NO_MARK_FIELDS:
        for v in (it.get(f), (it.get('es') or {}).get(f)):
            if isinstance(v, str) and MARK_RE.search(v):
                probs.append(f"{label}: {f} must not carry [n] markers")
    # the same markers in EN and ES
    en_m, es_m = [], []
    collect_marks({k: v for k, v in it.items() if k != 'es'}, en_m)
    collect_marks(it.get('es') or {}, es_m)
    if sorted(set(n for n, _ in en_m)) != sorted(set(n for n, _ in es_m)):
        warns.append(f"{label}: EN and ES cite different sources ({sorted(set(n for n, _ in en_m))} vs {sorted(set(n for n, _ in es_m))})")
    for n in range(1, len(refs) + 1):
        if n not in used:
            warns.append(f"{label}: refs[{n}] is not cited in the text")


# ---------- validation per era ----------
link_count = {}      # ctx id -> number of links
item_links = {}      # design item id -> number of links
valid_links = []     # (era declared, link)
for eid, d in eras.items():
    probs, warns = [], []
    for ln in d['links']:
        c, i = ln.get('ctx'), ln.get('item')
        lbl = f"link {c}>{i}"
        if c not in reg:
            probs.append(f"{lbl}: unknown ctx {c}")
        elif reg[c][1] != 'context':
            probs.append(f"{lbl}: ctx {c} is a {reg[c][1]}, not a context element")
        if i not in reg:
            probs.append(f"{lbl}: unknown item {i}")
        elif reg[i][1] not in DESIGN_KINDS:
            probs.append(f"{lbl}: item {i} is a {reg[i][1]}, not a design element")
        if c in reg and i in reg and reg[c][1] == 'context' and reg[i][1] in DESIGN_KINDS:
            link_count[c] = link_count.get(c, 0) + 1
            item_links[i] = item_links.get(i, 0) + 1
            valid_links.append((eid, ln))
        n = ln.get('note') or ''
        if not n:
            probs.append(f"{lbl}: missing note")
        elif len(MARK_RE.sub('', n)) > LEN_NOTE:
            warns.append(f"{lbl}: note is long ({len(MARK_RE.sub('', n))} chars; ~200 max)")
        if not (ln.get('es') or {}).get('note'):
            probs.append(f"{lbl}: missing es.note")
        check_refs(eid, lbl, ln, probs, warns)
    all_problems += [f"[{eid}] {p}" for p in probs]
    all_warns += [f"[{eid}] {p}" for p in warns]

for eid, d in eras.items():
    if only and eid not in only:
        continue
    era = d['era']
    probs, warns = [], []
    ready = any(d[k] for k in KEYS)
    d['_ready'] = ready
    for t in d['tracks']:
        if t.get('id') not in TRACKS:
            probs.append(f"track {t.get('id')}: not in {TRACKS}")
        if not (t.get('es') or {}).get('label'):
            probs.append(f"track {t.get('id')}: missing es.label")
    tracks = {t['id'] for t in d['tracks']}
    if not isinstance(era.get('start'), int) or not isinstance(era.get('end'), int):
        probs.append('era: start and end must be integers (end may be "now")')
    if not (era.get('es') or {}).get('intro') or not era.get('intro'):
        probs.append('era: needs intro and es.intro')
    if not (era.get('es') or {}).get('name'):
        probs.append('era: needs es.name')
    # v20: the eras are only folders (they are not shown); their overview texts moved to the macro-movements.
    # --- detail level (v20): every design element has one
    for key in ('movements', 'institutions', 'designers', 'works', 'theories'):
        for it in d[key]:
            if it.get('level') not in LEVELS:
                probs.append(f"{key[:-1]} {it['id']}: level must be one of {LEVELS} (got {it.get('level')!r})")
            if 'star' in it:
                probs.append(f"{key[:-1]} {it['id']}: 'star' is replaced by level: essential")

    # --- movements
    for it in d['movements']:
        lbl = f"movement {it['id']}"
        if it.get('macro'):
            # macro-movement (v20): an umbrella over several movements, with an overview of its context by factor
            valid_refs(lbl, it.get('parts'), ('movement',), probs)
            cs, ces = it.get('context_summary') or {}, (it.get('es') or {}).get('context_summary') or {}
            miss = [t for t in TRACKS if not cs.get(t) or not ces.get(t)]
            if miss:
                probs.append(f"{lbl}: macro-movement needs context_summary in EN and ES for {', '.join(miss)}")
            if len(it.get('shifts') or []) != len((it.get('es') or {}).get('shifts') or []) or not it.get('shifts'):
                probs.append(f"{lbl}: macro-movement needs shifts in EN and ES (same number)")
        for x in it.get('disciplines') or []:
            if x not in DISCIPLINES:
                probs.append(f"{lbl}: bad discipline {x}")
        if not it.get('disciplines'):
            probs.append(f"{lbl}: needs disciplines")
        in_era(era, it, lbl, probs)
        check_geo(lbl, it, probs)
        check_es(eid, 'movement', it, probs, warns)
    # --- institutions
    for it in d['institutions']:
        lbl = f"institution {it['id']}"
        if it.get('kind') not in INST_KINDS:
            probs.append(f"{lbl}: bad kind {it.get('kind')}")
        if not it.get('disciplines'):
            probs.append(f"{lbl}: needs disciplines")
        for x in it.get('disciplines') or []:
            if x not in DISCIPLINES:
                probs.append(f"{lbl}: bad discipline {x}")
        if 'end' not in it:
            probs.append(f"{lbl}: needs end (a year, or null if still active)")
        if it.get('end') is None:
            it['cont'] = True
        in_era(era, it, lbl, probs)
        lk = it.get('links') or {}
        valid_refs(lbl, lk.get('designers'), ('designer',), probs)
        valid_refs(lbl, lk.get('works'), ('work',), probs)
        check_geo(lbl, it, probs)
        check_es(eid, 'institution', it, probs, warns)
    # --- designers
    for it in d['designers']:
        lbl = f"designer {it['id']}"
        if it.get('kind') not in DESIGNER_KINDS:
            probs.append(f"{lbl}: bad kind {it.get('kind')} (studios and companies are institutions)")
        ds = it.get('disciplines') or []
        if not ds:
            probs.append(f"{lbl}: needs disciplines")
        for x in ds:
            if x not in DISCIPLINES:
                probs.append(f"{lbl}: bad discipline {x}")
        b, dd = it.get('born'), it.get('died')
        if not isinstance(b, int):
            probs.append(f"{lbl}: needs an integer born")
        else:
            end = dd if isinstance(dd, int) else NOW
            if b > era['end'] or end < era['start']:
                probs.append(f"{lbl}: life {b}–{dd} does not overlap the era")
            if dd is not None and not isinstance(dd, int):
                probs.append(f"{lbl}: died must be an integer or null")
        valid_refs(lbl, it.get('movements'), ('movement',), probs)
        valid_refs(lbl, it.get('institutions'), ('institution',), probs)
        check_geo(lbl, it, probs)
        check_es(eid, 'designer', it, probs, warns)
    # --- works
    des = {x['id']: x for x in d['designers']}
    for it in d['works']:
        lbl = f"work {it['id']}"
        disc = it.get('discipline')
        if disc not in DISCIPLINES:
            probs.append(f"{lbl}: bad discipline {disc}")
        elif it.get('type') and it['type'] not in WORK_TYPES[disc]:
            warns.append(f"{lbl}: type '{it['type']}' is not in the usual list for {disc}")
        if not (it.get('designers') or it.get('maker') or it.get('client')):
            probs.append(f"{lbl}: needs designers, maker or client")
        valid_refs(lbl, it.get('designers'), ('designer',), probs)
        for f in ('maker', 'client'):
            v = it.get(f)
            if isinstance(v, str) and v.startswith('inst-'):
                valid_refs(lbl, [v], ('institution',), probs)
        valid_refs(lbl, it.get('tech'), ('production',), probs)
        valid_refs(lbl, it.get('movements'), ('movement',), probs)
        y = it.get('year')
        if not isinstance(y, int):
            probs.append(f"{lbl}: needs an integer year")
        else:
            if y < era['start'] or y > era_end(era):
                probs.append(f"{lbl}: year {y} is outside the era {era['start']}–{era_end(era)}; move it to the folder of the era where it starts")
            for dn in it.get('designers') or []:
                dsg = des.get(dn) or None
                if dsg is None and dn in reg:
                    # a designer of another era: look it up there
                    dsg = next((x for x in eras[reg[dn][0]]['designers'] if x['id'] == dn), None)
                if dsg and isinstance(dsg.get('born'), int):
                    top = dsg['died'] + 1 if isinstance(dsg.get('died'), int) else NOW
                    gap = 0 if dsg.get('kind') in ('collective', 'studio', 'firm') else 12  # un colectivo no «nace»: su primer año ya cuenta
                    if not (dsg['born'] + gap <= y <= top) and not it.get('posthumous'):   # v46 (etapa 7): `posthumous: true` = obra terminada o publicada tras la muerte del autor
                        probs.append(f"{lbl}: year {y} outside the life of {dn} ({dsg['born']}–{dsg.get('died')})")
        pr = it.get('production')
        if pr is not None:
            if not isinstance(pr.get('from'), int):
                probs.append(f"{lbl}: production.from must be an integer")
            elif isinstance(y, int) and pr['from'] < y - 1:
                warns.append(f"{lbl}: production starts before the design year")
            if pr.get('to') is not None and (not isinstance(pr['to'], int) or pr['to'] < pr.get('from', 0)):
                probs.append(f"{lbl}: bad production.to")
        for w in it.get('where') or []:
            if not str(w.get('url', '')).startswith('https://') or not w.get('label'):
                probs.append(f"{lbl}: 'where' entries need label and https url")
        check_geo(lbl, it, probs)
        check_es(eid, 'work', it, probs, warns)
        if it.get('level') == 'essential' and not item_links.get(it['id']):
            warns.append(f"{lbl}: must-know work without context links")
    # --- contexts
    for it in d['contexts']:
        lbl = f"context {it['id']}"
        if it.get('track') not in tracks:
            probs.append(f"{lbl}: bad track {it.get('track')}")
        in_era(era, it, lbl, probs)
        check_geo(lbl, it, probs)
        check_es(eid, 'context', it, probs, warns)
        if not link_count.get(it['id']):
            probs.append(f"{lbl}: has no context link (every context element must explain at least one design element)")
    # --- production
    for it in d['production']:
        lbl = f"production {it['id']}"
        if it.get('sub') not in PROD_SUBS:
            probs.append(f"{lbl}: bad sub {it.get('sub')}")
        in_era(era, it, lbl, probs)
        lk = it.get('links') or {}
        n = 0
        for f, kinds in (('movements', ('movement',)), ('institutions', ('institution',)), ('designers', ('designer',)), ('works', ('work',))):
            valid_refs(lbl, lk.get(f), kinds, probs)
            n += len(lk.get(f) or [])
        if n == 0:
            probs.append(f"{lbl}: must link to at least one movement, institution, designer or work")
        check_geo(lbl, it, probs)
        check_es(eid, 'production', it, probs, warns)
    # --- theories
    for it in d['theories']:
        lbl = f"theory {it['id']}"
        if not it['id'].startswith('th-'):
            probs.append(f"{lbl}: id must start with th-")
        if it.get('genre') not in GENRES:
            probs.append(f"{lbl}: bad genre {it.get('genre')}")
        in_era(era, {'start': it.get('year')}, lbl, probs)
        if not it.get('sources'):
            # v31 (plan 3.1): Part I writes theories without source links; Part II (R1) turns this back into a PROBLEM
            (probs if STRICT_THEORY_SOURCES else warns).append(f"{lbl}: no source link yet (STRICT_THEORY_SOURCES; R1.2: PROBLEM when R3 ends the theories)")
        for s in it.get('sources') or []:
            if not str(s.get('url', '')).startswith('https://'):
                probs.append(f"{lbl}: bad source url")
            if not s.get('label') or not s.get('es'):
                probs.append(f"{lbl}: sources need label and es")
        lk = it.get('links') or {}
        n = 0
        for f, kinds in (('movements', ('movement',)), ('institutions', ('institution',)), ('designers', ('designer',)), ('works', ('work',))):
            valid_refs(lbl, lk.get(f), kinds, probs)
            n += len(lk.get(f) or [])
        if n == 0:
            probs.append(f"{lbl}: must link to at least one movement, institution, designer or work")
        if len(it.get('ideas') or []) < 3 or len(it.get('ideas') or []) > 5:
            warns.append(f"{lbl}: ideas should be 3–5")
        if len(it.get('short') or '') > 22:
            warns.append(f"{lbl}: short should be only the author's surname")
        check_geo(lbl, it, probs)
        check_es(eid, 'theory', it, probs, warns)
    # --- concepts
    for it in d['concepts']:
        check_es(eid, 'concept', it, probs, warns)
    # --- connections
    for c in d['connections']:
        lbl = f"connection {c.get('from')}>{c.get('to')}"
        for e in ('from', 'to'):
            if c.get(e) not in reg:
                probs.append(f"{lbl}: unknown {c.get(e)}")
        if not (c.get('es') or {}).get('note') or not c.get('note'):
            probs.append(f"{lbl}: needs note and es.note")
        check_refs(eid, lbl, c, probs, warns, count_missing=False)
    # --- balance warnings
    if ready:
        short = [f"{t} {sum(1 for x in d['contexts'] if x['track'] == t)}" for t in TRACKS if sum(1 for x in d['contexts'] if x['track'] == t) < 4]
        if short:
            warns.append('era: context subcategories with fewer than 4 elements: ' + ', '.join(short))
    all_problems += [f"[{eid}] {p}" for p in probs]
    all_warns += [f"[{eid}] {p}" for p in warns]


# ---------- sources summary (v21) ----------
for eid2, n in refs_missing.items():
    if n:
        all_warns.append(f"[{eid2}] {n} elements or links have no refs yet (sources: manual 7.1; plan A6)")

# ---------- global checks (v20) ----------
works_by_designer = {}
for e in eras.values():
    for w in e['works']:
        for x in w.get('designers') or []:
            works_by_designer.setdefault(x, []).append(w)
for eid, d in eras.items():
    for a in d['designers']:
        ws = works_by_designer.get(a['id'], [])
        if not ws:
            all_problems.append(f"[{eid}] designer {a['id']}: has no works (every designer on the line needs at least one)")
        elif a.get('level') in LEVEL_RANK and min(LEVEL_RANK.get(w.get('level'), 9) for w in ws) > LEVEL_RANK[a['level']]:
            all_problems.append(f"[{eid}] designer {a['id']}: level {a['level']} but no work at that level or a more basic one (its life line would be empty)")


# ---------- essays (stage 8.2) ----------
LENS_TARGETS = ['political', 'economic', 'social', 'cultural', 'technological', 'production']
DISC_TARGETS = ['graphic', 'product', 'fashion', 'architecture']
ESSAY_SRC = os.path.join(ROOT, 'src-essays', 'essays.json')
essays_out = {'essays': []}
_ess_ids = set()
if os.path.exists(ESSAY_SRC):
    _raw = json.load(open(ESSAY_SRC, encoding='utf-8')).get('essays', [])
    _wdisc = {w['id']: w.get('discipline') for e in eras.values() for w in e['works']}
    _link_re = re.compile(r'\[\[([a-z0-9_.\-]+)(?:\|[^\]]*)?\]\]')
    for es_ in _raw:
        eid_ = es_.get('id', '?')
        tag = f"[essay {eid_}]"
        kind_ = es_.get('kind')
        if eid_ in _ess_ids:
            all_problems.append(f"{tag} duplicate id")
        _ess_ids.add(eid_)
        tg = es_.get('target')
        if kind_ not in ('lens', 'discipline') or eid_ != ('lens-' if kind_ == 'lens' else 'disc-') + str(tg) \
                or tg not in (LENS_TARGETS if kind_ == 'lens' else DISC_TARGETS):
            all_problems.append(f"{tag} invalid kind/target/id")
            continue
        for k in ('title', 'subtitle'):
            if not txt(es_.get(k)):
                all_problems.append(f"{tag} missing {k}")
        paras = es_.get('paras') or []
        lo, hi = (6, 10) if kind_ == 'lens' else (8, 12)
        if not lo <= len(paras) <= hi:
            all_problems.append(f"{tag} has {len(paras)} paragraphs (expected {lo}-{hi})")
        es_es = es_.get('es') or {}
        for k in ('title', 'subtitle'):
            if not txt(es_es.get(k)):
                all_problems.append(f"{tag} es.{k} missing")
        pes = es_es.get('paras') or []
        if len(pes) != len(paras):
            all_problems.append(f"{tag} es.paras has {len(pes)} paragraphs, EN has {len(paras)}")
        for lang, pl in (('en', paras), ('es', pes)):
            for i, ptxt in enumerate(pl):
                if not txt(ptxt):
                    all_problems.append(f"{tag} empty paragraph {i + 1} ({lang})")
                elif len(MARK_RE.sub('', ptxt)) > 1100:
                    all_problems.append(f"{tag} paragraph {i + 1} ({lang}) has {len(MARK_RE.sub('', ptxt))} chars (max 1100)")
        ids_en = [m for ptxt in paras for m in _link_re.findall(ptxt)]
        ids_es = [m for ptxt in pes for m in _link_re.findall(ptxt)]
        if sorted(ids_en) != sorted(ids_es):
            all_problems.append(f"{tag} linked ids differ between EN and ES")
        for m in set(ids_en) | set(ids_es):
            if m not in reg:
                all_problems.append(f"{tag} link to unknown id {m}")
        dist = set(ids_en)
        kinds_ = {kind_of(m) for m in dist if m in reg}
        if len(dist) < 15:
            all_problems.append(f"{tag} only {len(dist)} distinct linked ids (min 15)")
        if 'context' not in kinds_ or not kinds_ & {'movement', 'work'} or not kinds_ & {'designer', 'institution'}:
            all_problems.append(f"{tag} needs links of >=3 kinds (context, movement or work, designer or institution)")
        eras_hit = {era_of(m) for m in dist if m in reg}
        if len(eras_hit & set(ERA_ORDER)) < 4:
            all_problems.append(f"{tag} links cover only {len(eras_hit)} eras (min 4)")
        imgs = es_.get('images') or []
        if not 4 <= len(imgs) <= 8:
            all_problems.append(f"{tag} has {len(imgs)} images (expected 4-8)")
        _wk = {w['id']: w for e in eras.values() for w in e['works']}
        nfree = 0
        for im in imgs:
            if im not in _wk:
                all_problems.append(f"{tag} image {im} is not a work")
            elif _wk[im].get('wiki'):
                nfree += 1
        if imgs and not nfree:
            all_warns.append(f"{tag} no image has a wiki page")
        if not isinstance(es_.get('refs'), list):
            all_problems.append(f"{tag} refs must be a list")
        elif not es_['refs']:
            all_warns.append(f"{tag} not reviewed: no refs yet")
        # [n] marks of the text (R2.3): each one needs its source, the same marks in EN and ES paragraph by paragraph, none inside [[id|text]]
        _nref = len(es_['refs']) if isinstance(es_.get('refs'), list) else 0
        for _lang, _pl in (('en', paras), ('es', pes)):
            for i, ptxt in enumerate(_pl):
                for _m in MARK_RE.findall(ptxt):
                    if not 1 <= int(_m) <= _nref:
                        all_problems.append(f"{tag} paragraph {i + 1} ({_lang}) has mark [{_m}] without a source")
                if re.search(r'\[\[[^\]]*\[\d', ptxt):
                    all_problems.append(f"{tag} paragraph {i + 1} ({_lang}) has a mark inside a [[id|text]] link")
        for i, (pa, pb) in enumerate(zip(paras, pes)):
            if sorted(MARK_RE.findall(pa)) != sorted(MARK_RE.findall(pb)):
                all_problems.append(f"{tag} paragraph {i + 1}: [n] marks differ between EN and ES")
        essays_out['essays'].append(es_)
    _missing = [x for x in ['lens-' + t for t in LENS_TARGETS] + ['disc-' + t for t in DISC_TARGETS] if x not in _ess_ids]
    if _missing:
        all_warns.append("essays missing: " + ', '.join(_missing))


# ---------- output ----------
def strip(o):
    if isinstance(o, dict):
        return {k: strip(v) for k, v in o.items() if not k.startswith('_')}
    if isinstance(o, list):
        return [strip(x) for x in o]
    return o


os.makedirs(os.path.join(ROOT, 'data'), exist_ok=True)
ctx_track = {x['id']: x.get('track') for e2 in eras.values() for x in e2['contexts']}
design_by_id = {x['id']: x for e in eras.values() for x in e['designers']}
out = {'eras': [], 'tracks': None, 'ctxLinks': [], 'connections': [], 'items': [], 'stats': {}}
for key in KEYS:
    out[key] = []
seen = set()
_imgp = os.path.join(ROOT, 'src-images', 'images.json')
IMGS = json.load(open(_imgp, encoding='utf-8')) if os.path.exists(_imgp) else {}
_allids = {x['id'] for e in eras.values() for k in KEYS for x in e[k]}
for _iid, _l in IMGS.items():
    if _iid not in _allids:
        all_problems.append(f"images.json: unknown item {_iid}")
    for _im in _l:
        if not _im.get('file') or not _im.get('license'):
            all_problems.append(f"images.json: {_iid} image without file/license")
_nimg = {'work': [0, 0], 'designer': [0, 0]}
for eid in ERA_ORDER:
    if eid not in eras:
        continue
    d = eras[eid]
    era = dict(d['era'])
    ready = any(d[k] for k in KEYS)
    era['ready'] = ready
    out['eras'].append(era)
    if out['tracks'] is None and d['tracks']:
        out['tracks'] = d['tracks']
    for key, kind in KEYS.items():
        for it in d[key]:
            it = dict(it, era=eid)
            if kind in DESIGN_KINDS:
                it['star'] = it.get('level') == 'essential'   # the ★ marks every essential element
            if IMGS.get(it['id']):
                it['images'] = [{k2: v2 for k2, v2 in {'f': i['file'], 'c': i.get('credit', ''), 'l': i['license'],
                                'r': 1 if i.get('rights') == 'reserved' else 0}.items() if v2 != '' and v2 != 0}
                                for i in IMGS[it['id']]]
            if kind in _nimg:
                _nimg[kind][0] += 1
                _nimg[kind][1] += 1 if it.get('images') else 0
            out[key].append(it)
            name = it.get('title') or it.get('name') or ''
            es = it.get('es') or {}
            name_es = es.get('title') or es.get('name') or name
            year = it.get('year', it.get('start', it.get('born', '')))
            by = ''
            if kind == 'work' and it.get('designers'):
                by = ', '.join(design_by_id[x]['name'] for x in it['designers'] if x in design_by_id)
            if kind == 'theory':
                by = it.get('author', '')
            out['items'].append([it['id'], eid, kind, name, name_es, year, by, 1 if it.get('star') else 0])
    for c in d['connections']:
        k = (c.get('from'), c.get('to'))
        if k not in seen:
            seen.add(k)
            out['connections'].append(c)
    works = d['works']
    with_ctx = sum(1 for w in works if item_links.get(w['id']))
    nlinks = sum(1 for (e2, ln) in valid_links if e2 == eid)
    out['stats'][eid] = {
        'movements': len(d['movements']), 'institutions': len(d['institutions']), 'designers': len(d['designers']),
        'works': len(works), 'stars': sum(1 for w in works if w.get('level') == 'essential'),
        'contexts': len(d['contexts']), 'production': len(d['production']), 'theories': len(d['theories']),
        'concepts': len(d['concepts']), 'connections': len(d['connections']), 'links': nlinks,
        'byDiscipline': {x: sum(1 for w in works if w.get('discipline') == x) for x in DISCIPLINES},
        'byTrack': {x: sum(1 for c in d['contexts'] if c.get('track') == x) for x in TRACKS},
        'worksWithContext': with_ctx,
    }
    s = out['stats'][eid]
    print(f"{eid}: ready={ready} movements={s['movements']} institutions={s['institutions']} designers={s['designers']} works={s['works']} "
          f"(stars {s['stars']}, with context {with_ctx}) contexts={s['contexts']} production={s['production']} theories={s['theories']} "
          f"concepts={s['concepts']} links={s['links']} connections={s['connections']}")
# ---------- point 65 (rule C4b): works with direct context / only indirect / none ----------
def ctx_coverage(w):
    if item_links.get(w['id']):
        return 'direct'
    rel = list(w.get('designers') or []) + list(w.get('movements') or [])
    if any(item_links.get(x) for x in rel):
        return 'indirect'
    return 'none'
_tot = {'direct': 0, 'indirect': 0, 'none': 0}
_none = []
for eid, d in eras.items():
    cnt = {'direct': 0, 'indirect': 0, 'none': 0}
    for w in d['works']:
        c = ctx_coverage(w)
        cnt[c] += 1
        if c == 'none':
            _none.append(f"[{eid}] {w['id']}")
    out['stats'][eid]['ctxDirect'], out['stats'][eid]['ctxIndirect'], out['stats'][eid]['ctxNone'] = cnt['direct'], cnt['indirect'], cnt['none']
    for k in _tot:
        _tot[k] += cnt[k]
    print(f"  context coverage {eid}: direct {cnt['direct']} / only indirect {cnt['indirect']} / none {cnt['none']}")
print(f"  context coverage TOTAL: direct {_tot['direct']} / only indirect {_tot['indirect']} / none {_tot['none']}")
if _none:
    all_warns.append(f"works without any context (neither direct nor indirect), {len(_none)}: " + ', '.join(_none))
out['ctxLinks'] = [dict(ln, track=ctx_track.get(ln['ctx'])) for (_, ln) in valid_links]
out['generated'] = datetime.date.today().isoformat()
out = strip(out)
json.dump(out, open(os.path.join(ROOT, 'data', 'all.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
for old in glob.glob(os.path.join(ROOT, 'data', '*.json')):
    if os.path.basename(old) not in ('all.json', 'essays.json'):
        os.remove(old)  # per-era files of v10 and earlier
json.dump(essays_out, open(os.path.join(ROOT, 'data', 'essays.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('essays.json:', len(essays_out['essays']), 'essays')
print('all.json:', len(out['items']), 'items in', len(out['eras']), 'eras')

if only:
    keep = tuple(f"[{e}]" for e in only)
    all_problems = [p for p in all_problems if p.startswith(keep) or not p.startswith('[')]
    all_warns = [p for p in all_warns if p.startswith(keep)]
for _k, _lab in (('work', 'obras'), ('designer', 'diseñadores')):
    if _nimg[_k][0] - _nimg[_k][1]:
        all_warns.append(f"images: {_nimg[_k][0] - _nimg[_k][1]} {_lab} sin imagen de {_nimg[_k][0]}")
if all_warns:
    print('\n'.join('WARN: ' + w for w in (all_warns if verbose else all_warns[:25])))
    if not verbose and len(all_warns) > 25:
        print(f"... {len(all_warns) - 25} more WARN lines (use -v)")
if all_problems:
    print('\n'.join('PROBLEM: ' + p for p in all_problems))
    sys.exit(1)
print('OK: no PROBLEM')
