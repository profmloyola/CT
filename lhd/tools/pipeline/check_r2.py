#!/usr/bin/env python3
"""R2: revisa las salidas de los agentes (formato apply2.py) ANTES de aplicarlas.

Uso: python3 tools/pipeline/check_r2.py [--con-fuentes] r2_work/out_t01_1.json [...]
Código de salida: 0 sin ERROR; 1 con ERROR (los AVISO no cuentan). --con-fuentes permite registros que ya tienen fuentes (refuerzo, R2.5).

Registros que entiende (se reconocen por sus claves):
  elemento   {id, en:{key,…}, es:{…}, refs, other, issues}   obras, diseñadores, movimientos, instituciones, teorías, contextos, productivos
  ensayo     {id, en:{paras}, es:{paras}, refs, issues}       id de src-essays/essays.json
  enlace     {ctx, item, en:{note}, es:{note}, refs, issues}  enlace de contexto existente (ctxLinks)
  conexión   {from, to, en:{note}, es:{note}, refs, issues}   conexión existente
  propuesta de quitar  {ctx, item | from, to, drop: true, issues}   el enlace o la conexión NO se borra al aplicar: va a incidencias

Comprueba: el registro existe y no tiene fuentes aún; campos permitidos y obligatorios del tipo; marcas [n] con fuente, mismas marcas
en EN y ES (por campo; por párrafo en los ensayos); toda fuente citada; URL https, sin Wikipedia/wikis, sin puerto raro ni repetidas;
label, checks y fecha AAAA-MM-DD; largos; en los ensayos, los enlaces [[id|texto]] bien formados, con id existente, iguales en EN y ES
y sin marcas dentro; registros sin repetir entre las salidas."""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r2lib import ESS_LINK, FIELDS, MARK, OTHER_OK, load_all, load_essays, marks_of, record_key, record_kind, registry

BAD = ('wikipedia.org', 'wikiwand', 'grokipedia', 'wikimedia.org', 'wikidata', 'fandom.com', 'wikia.', 'wikihow', 'miraheze', 'everybodywiki', 'dbpedia')
SOFT = ('blogspot.', 'wordpress.com', 'medium.com', 'tumblr.com', 'substack.com', 'pinterest.', 'amazon.', 'ebay.', 'etsy.', 'aliexpress', 'facebook.com', 'instagram.com', 'twitter.com')
LISTS = ('traits', 'ideas')
OPTIONAL = ('dates', 'economy', 'relations')
DATE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
LEN_KEY, LEN_NOTE = 230, 240


def refs_errors(refs, L, W):
    urls = set()
    for n, r in enumerate(refs, 1):
        u = r.get('url') or ''
        if not u.startswith('https://'):
            L.append(f'refs[{n}] url no https')
        if any(b in u for b in BAD):
            L.append(f'refs[{n}] fuente no válida: {u}')
        elif any(b in u for b in SOFT):
            W.append(f'refs[{n}] blog, tienda o red social: {u}')
        if re.match(r'https://[^/]+:\d+', u):
            L.append(f'refs[{n}] url con puerto: {u}')
        if ' ' in u:
            L.append(f'refs[{n}] url con espacios')
        if u in urls:
            L.append(f'refs[{n}] url repetida')
        urls.add(u)
        if not r.get('label') or not r.get('checks') or not r.get('date'):
            L.append(f'refs[{n}] falta label/checks/date')
        elif not DATE.match(r['date']):
            L.append(f'refs[{n}] date no es AAAA-MM-DD: {r["date"]}')


def marks_vs_refs(en, es, refs, L, W, per_field=True):
    """Marcas válidas, iguales en EN y ES (por campo) y fuentes citadas."""
    n_refs = len(refs)
    used = set()
    for lang, src in (('en', en), ('es', es)):
        for f, v in src.items():
            ms = marks_of(v)
            for m in ms:
                if m < 1 or m > n_refs:
                    L.append(f'{lang}.{f}: marca [{m}] sin fuente')
            used |= ms
    if per_field:
        for f in en:
            if f in es and marks_of(en[f]) != marks_of(es[f]):
                L.append(f'marcas distintas en «{f}»: EN {sorted(marks_of(en[f]))} vs ES {sorted(marks_of(es[f]))}')
            if isinstance(en.get(f), list) and isinstance(es.get(f), list):
                for i, (a, b) in enumerate(zip(en[f], es[f])):
                    if marks_of(a) != marks_of(b):
                        L.append(f'marcas distintas en «{f}»[{i + 1}]: EN {sorted(marks_of(a))} vs ES {sorted(marks_of(b))}')
    for n in range(1, n_refs + 1):
        if n not in used:
            W.append(f'refs[{n}] sin citar')
    if not used:
        L.append('ninguna marca [n] en el texto')


def check_element(e, kind, x, L, W, con_fuentes):
    en, es = e.get('en') or {}, e.get('es') or {}
    allowed = FIELDS[kind]
    if set(en) != set(es):
        L.append(f'EN y ES con campos distintos: {sorted(en)} vs {sorted(es)}')
    for f in en:
        if f not in allowed:
            L.append(f'campo «{f}» no permitido para {kind}: {list(allowed)}')
    for f in allowed:
        if f not in OPTIONAL and f not in en:
            L.append(f'falta el campo «{f}» en en/es')
    for lang, src in (('en', en), ('es', es)):
        for f, v in src.items():
            if f in LISTS:
                if not isinstance(v, list) or not v or not all(isinstance(s, str) and s.strip() for s in v):
                    L.append(f'{lang}.{f} debe ser una lista de textos no vacía')
            elif not isinstance(v, str) or not v.strip():
                L.append(f'{lang}.{f} debe ser un texto no vacío')
        k = src.get('key')
        if isinstance(k, str) and len(MARK.sub('', k)) > (LEN_KEY if lang == 'en' else LEN_KEY + 30):
            W.append(f'{lang}: key de {len(MARK.sub("", k))} caracteres')
        if kind == 'contexts' and isinstance(src.get('effect'), str) and len(MARK.sub('', src['effect'])) > 480:
            W.append(f'{lang}: effect de {len(MARK.sub("", src["effect"]))} caracteres (máximo recomendado 480)')
    for f in LISTS:
        if isinstance(en.get(f), list) and isinstance(es.get(f), list) and len(en[f]) != len(es[f]):
            L.append(f'«{f}»: EN tiene {len(en[f])} elementos y ES {len(es[f])}')
    for f in (e.get('other') or {}):
        if f not in OTHER_OK:
            W.append(f'other.{f}: campo que no se espera cambiar (anótalo en issues)')
    if x.get('refs') and not con_fuentes:
        L.append('ya tiene fuentes (¿repetido?)')
    marks_vs_refs(en, es, e.get('refs') or [], L, W)


def check_note(e, x, L, W, con_fuentes):
    en, es = e.get('en') or {}, e.get('es') or {}
    if set(en) != {'note'} or set(es) != {'note'}:
        L.append(f'en y es deben llevar solo «note»: {sorted(en)} vs {sorted(es)}')
    for lang, src in (('en', en), ('es', es)):
        v = src.get('note')
        if not isinstance(v, str) or not v.strip():
            L.append(f'{lang}.note vacío')
        elif len(MARK.sub('', v)) > LEN_NOTE:
            W.append(f'{lang}: note de {len(MARK.sub("", v))} caracteres (recomendado ≤ {LEN_NOTE})')
    if x.get('refs') and not con_fuentes:
        L.append('ya tiene fuentes (¿repetido?)')
    marks_vs_refs(en, es, e.get('refs') or [], L, W)


def link_ids(p):
    return sorted(m.group(1) for m in ESS_LINK.finditer(p))


def check_essay(e, orig, reg, L, W, con_fuentes):
    en, es = e.get('en') or {}, e.get('es') or {}
    if set(en) != {'paras'} or set(es) != {'paras'}:
        L.append(f'en y es deben llevar solo «paras»: {sorted(en)} vs {sorted(es)}')
        return
    pe, ps = en['paras'], es['paras']
    if not (isinstance(pe, list) and isinstance(ps, list) and pe and ps and all(isinstance(p, str) and p.strip() for p in pe + ps)):
        L.append('paras debe ser una lista de textos no vacía (EN y ES)')
        return
    if len(pe) != len(ps):
        L.append(f'EN tiene {len(pe)} párrafos y ES {len(ps)}')
    for lang, paras in (('en', pe), ('es', ps)):
        for i, p in enumerate(paras, 1):
            if '[[' in ESS_LINK.sub('', p) or ']]' in ESS_LINK.sub('', p):
                L.append(f'{lang} párrafo {i}: corchetes dobles mal formados')
            for m in ESS_LINK.finditer(p):
                if m.group(1) not in reg:
                    L.append(f'{lang} párrafo {i}: id inexistente en [[{m.group(1)}]]')
                if m.group(2) and '[' in m.group(2):
                    L.append(f'{lang} párrafo {i}: marca o corchete dentro del texto del enlace [[{m.group(1)}|…]]')
            if re.search(r'\[\[[^\]]*\[\d', p):
                L.append(f'{lang} párrafo {i}: marca [n] dentro de un enlace [[id|texto]]')
            if not MARK.search(p):
                W.append(f'{lang} párrafo {i}: sin ninguna marca [n]')
    for i, (a, b) in enumerate(zip(pe, ps), 1):
        if link_ids(a) != link_ids(b):
            L.append(f'párrafo {i}: enlaces [[id]] distintos en EN y ES: {link_ids(a)} vs {link_ids(b)}')
        if marks_of(a) != marks_of(b):
            L.append(f'párrafo {i}: marcas distintas en EN {sorted(marks_of(a))} y ES {sorted(marks_of(b))}')
    if len(pe) != len(orig['paras']):
        W.append(f'el ensayo tenía {len(orig["paras"])} párrafos y ahora {len(pe)}')
    else:
        for i, (a, o) in enumerate(zip(pe, orig['paras']), 1):
            if link_ids(a) != link_ids(o):
                W.append(f'párrafo {i}: los enlaces [[id]] difieren del original')
    if orig.get('refs') and not con_fuentes:
        L.append('ya tiene fuentes (¿repetido?)')
    marks_vs_refs({'paras': pe}, {'paras': ps}, e.get('refs') or [], L, W, per_field=False)


def check_records(records, d, reg, essays, con_fuentes, seen):
    links = {r['ctx'] + '~' + r['item']: r for r in d['ctxLinks']}
    conns = {r['from'] + '>' + r['to']: r for r in d['connections']}
    err = warn = 0
    for e in records:
        L, W = [], []
        rk, kind = record_key(e), record_kind(e)
        if rk in seen:
            L.append('registro repetido')
        seen.add(rk)
        refs = e.get('refs') or []
        x = None
        if kind == 'enlaces':
            x = links.get(rk)
        elif kind == 'conexiones':
            x = conns.get(rk)
        elif e.get('id') in essays:
            x, kind = essays[e['id']], 'ensayos'
        elif e.get('id') in reg:
            kind, x = reg[e['id']]
        if x is None:
            L.append({'enlaces': 'enlace inexistente', 'conexiones': 'conexión inexistente'}.get(kind, 'id inexistente'))
        elif e.get('drop'):
            if kind not in ('enlaces', 'conexiones'):
                L.append('`drop` solo se admite en enlaces y conexiones')
            if not e.get('issues'):
                L.append('`drop` sin issues: explica el motivo y las fuentes consultadas')
            if e.get('en') or e.get('es') or refs:
                W.append('`drop` con texto o refs: se ignoran')
        else:
            if not refs:
                L.append('sin refs')
            refs_errors(refs, L, W)
            if kind == 'ensayos':
                check_essay(e, x, reg, L, W, con_fuentes)
            elif kind in ('enlaces', 'conexiones'):
                check_note(e, x, L, W, con_fuentes)
            else:
                check_element(e, kind, x, L, W, con_fuentes)
        for s in L:
            print('ERROR', rk, s)
            err += 1
        for s in W:
            print('AVISO', rk, s)
            warn += 1
    return err, warn


def main(argv):
    con = '--con-fuentes' in argv
    files = [a for a in argv if not a.startswith('--')]
    if not files:
        print(__doc__)
        return 2
    d = load_all()
    reg = registry(d)
    essays = {e['id']: e for e in load_essays()}
    seen = set()
    err = warn = 0
    for fn in files:
        a, b = check_records(json.load(open(fn, encoding='utf-8')), d, reg, essays, con, seen)
        err += a
        warn += b
    print(f'{len(seen)} registros; {err} ERROR; {warn} AVISO')
    return 1 if err else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
