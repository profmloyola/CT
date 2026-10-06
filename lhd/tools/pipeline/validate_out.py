#!/usr/bin/env python3
"""Valida la salida JSON de un agente (lista de registros) ANTES de aplicarla (plan, paso 0.3).

Uso:
  python3 tools/pipeline/validate_out.py [--refs] [--tramo industrial|reform|modernism|postwar|postmodern] salida.json [...]

- Parte I (por omisión): sin `refs` ni marcas [n].
- Parte II (`--refs`): exige marcas [n] con fuente, fuentes citadas, mismas marcas en EN y ES, URL https y no de Wikipedia.
- El tramo se toma de `--tramo` o del prefijo del nombre del archivo (`postwar_lote3.json` -> postwar). Sin tramo no se revisan los años.
- Imprime `OK` o la lista de errores (código de salida 1 si hay errores).

Qué comprueba (plan 0.3): (a) id ya existente en src-data/; (b) ids referenciados que no existen en src-data/, en el mismo archivo ni en
tools/LISTAS-CIERRE.md; (c) falta un campo de texto en `es`, o `es` trae campos distintos; (d) marcas [n] / refs fuera de lugar;
(e) largos (key ~200 en inglés y 230 en español, short 22, nota de enlace 220 en inglés y 240 en español); (f) level distinto de essential/normal; (g) año fuera del tramo.
Cada registro lleva `rtype` (no `type`, que en las obras es el tipo de obra). Los registros {"id": ..., "descartado": true} y {"ctx"/"item"..., "sin_enlace": true} se aceptan sin más (van a la reserva).
"""
import glob
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(BASE, 'src-data')
LISTAS = os.path.join(BASE, 'tools', 'LISTAS-CIERRE.md')
NOW = 2026
TYPES = ('context', 'production', 'theory', 'movement', 'institution', 'designer', 'work', 'link', 'connection')
KIND_OF_TYPE = {'context': 'context', 'production': 'production', 'theory': 'theory', 'movement': 'movement',
                'institution': 'institution', 'designer': 'designer', 'work': 'work'}
KEY_OF_KIND = {'movements': 'movement', 'institutions': 'institution', 'designers': 'designer', 'works': 'work',
               'contexts': 'context', 'production': 'production', 'theories': 'theory', 'concepts': 'concept'}
# campos de texto que llevan traducción (igual que FIELDS de build_data.py)
TEXT = {
    'movement': ['name', 'short', 'key', 'context', 'shift', 'traits', 'more'],
    'institution': ['name', 'short', 'key', 'more', 'place'],
    'designer': ['key', 'more', 'dates'],
    'work': ['title', 'short', 'key', 'more', 'materials', 'date', 'status', 'production'],
    'context': ['name', 'short', 'key', 'happened', 'effect', 'date'],
    'production': ['name', 'short', 'key', 'origin', 'enabled', 'change', 'economy', 'relations', 'date'],
    'theory': ['name', 'short', 'author', 'key', 'ideas', 'impact', 'date'],
    'link': ['note'], 'connection': ['note'],
}
REQUIRED = {  # campos que deben existir en inglés (como el build)
    'movement': ['id', 'name', 'key', 'disciplines', 'start'],
    'institution': ['id', 'name', 'key', 'kind', 'disciplines', 'start', 'end'],
    'designer': ['id', 'name', 'key', 'kind', 'disciplines', 'born'],
    'work': ['id', 'title', 'key', 'discipline', 'type', 'year'],
    'context': ['id', 'name', 'key', 'happened', 'effect', 'track', 'start'],
    'production': ['id', 'name', 'key', 'sub', 'start'],
    'theory': ['id', 'name', 'author', 'key', 'ideas', 'impact', 'genre', 'year'],
    'link': ['ctx', 'item', 'note'], 'connection': ['from', 'to', 'note'],
}
HAS_LEVEL = ('movement', 'institution', 'designer', 'work', 'theory')
REF_FIELDS = {  # campos que apuntan a ids -> tipo(s) esperado(s) cuando el id está en src-data
    'designers': ('designer',), 'movements': ('movement',), 'institutions': ('institution',), 'tech': ('production',),
    'parts': ('movement',), 'ctx': ('context',), 'item': None, 'from': None, 'to': None,
}
LINK_FIELDS = {'movements': ('movement',), 'institutions': ('institution',), 'designers': ('designer',), 'works': ('work',)}
SKIP_MARK = {'refs', 'where', 'sources', 'links', 'id', 'wiki', 'img', 'designers', 'movements', 'institutions', 'tech', 'parts',
             'regions', 'countries', 'disciplines', 'terms', 'maker', 'client', 'ctx', 'item', 'from', 'to', 'track', 'type', 'rtype', 'es'}
MARK = re.compile(r'\[(\d{1,2})\]')
ID_RE = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
REGIONS = ('europe', 'north-america', 'latin-america', 'global')
BEYOND = set('JP CN KR TW HK IN LK TH VN ID MY SG PH PK BD NP MN IR IQ TR SA IL EG MA NG GH ET ZA KE SN AU NZ'.split())   # = zona «Más allá de Occidente» de app.js
TRAMOS = ('industrial', 'reform', 'modernism', 'postwar', 'postmodern')


def era_range(tramo, src=SRC):
    d = json.load(open(os.path.join(src, tramo, '01-structure.json'), encoding='utf-8'))['era']
    end = NOW if d['end'] == 'now' else d['end'] - 1
    return d['start'], end


def known_ids(src=SRC):
    """id -> tipo (de src-data); y los ids sin tipo que figuran en LISTAS-CIERRE.md."""
    kinds = {}
    for f in glob.glob(os.path.join(src, '*', '*.json')):
        d = json.load(open(f, encoding='utf-8'))
        for k, v in d.items():
            if k in KEY_OF_KIND and isinstance(v, list):
                for x in v:
                    if isinstance(x, dict) and 'id' in x:
                        kinds[x['id']] = KEY_OF_KIND[k]
    planned = set()
    if os.path.exists(LISTAS):
        for line in open(LISTAS, encoding='utf-8'):
            if line.lstrip().startswith('|'):
                planned.update(re.findall(r'`([a-z0-9]+(?:-[a-z0-9]+)*)`', line))
    prop = os.path.join(BASE, 'tools', 'PROPUESTA-ETAPA6.json')   # etapa 6: los ids aprobados en el V3 cuentan como planificados
    if os.path.exists(prop):
        try:
            planned.update(r['id'] for r in json.load(open(prop, encoding='utf-8')) if isinstance(r, dict) and 'id' in r)
        except Exception:
            pass
    rev = os.path.join(BASE, 'tools', 'REVISION-ETAPA7.json')   # etapa 7 (v46): los ids aprobados en el V4 cuentan como planificados
    if os.path.exists(rev):
        try:
            planned.update(r['id'] for r in json.load(open(rev, encoding='utf-8')) if isinstance(r, dict) and r.get('estado') == 'aprobado-V4')
        except Exception:
            pass
    return kinds, planned


def texts(o, path=''):
    """Recorre las cadenas de un registro (sin los campos que no son prosa)."""
    if isinstance(o, dict):
        for k, v in o.items():
            if k in SKIP_MARK:
                continue
            yield from texts(v, path + '.' + k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from texts(v, f'{path}[{i}]')
    elif isinstance(o, str):
        yield path, o


def marks_of(rec, lang):
    src = rec if lang == 'en' else rec.get('es') or {}
    found = set()
    for k, v in src.items():
        if k in SKIP_MARK:
            continue
        for _, s in texts({k: v}):
            found.update(int(n) for n in MARK.findall(s))
    return found


def label(rec, t):
    return rec.get('id') or f"{rec.get('ctx') or rec.get('from')}~{rec.get('item') or rec.get('to')}"


def validate(path, use_refs, tramo, src=SRC):
    errs = []
    try:
        data = json.load(open(path, encoding='utf-8'))
    except Exception as ex:  # noqa: BLE001
        return [f'{path}: JSON no válido ({ex})']
    if not isinstance(data, list):
        return [f'{path}: debe ser una lista de registros']
    kinds, planned = known_ids(src)
    in_file = {r['id'] for r in data if isinstance(r, dict) and 'id' in r}
    rng = era_range(tramo, src) if tramo else None
    seen = set()

    def err(rec, msg):
        errs.append(f'[{label(rec, rec.get("rtype"))}] {msg}')

    def exists(i):
        return i in kinds or i in in_file or i in planned

    for rec in data:
        if not isinstance(rec, dict):
            errs.append('un registro no es un objeto'); continue
        t = rec.get('rtype')
        if t not in TYPES:
            err(rec, f'rtype debe ser uno de {TYPES} (vino {t!r}); ojo: `type` es el tipo de obra (chair, poster...), no el tipo de registro'); continue
        if rec.get('descartado') or rec.get('sin_enlace'):
            if not rec.get('motivo'):
                err(rec, 'un registro descartado / sin_enlace necesita "motivo"')
            continue
        # (a) ids
        if t in KIND_OF_TYPE:
            i = rec.get('id', '')
            if not ID_RE.match(i):
                err(rec, 'id debe ir en minúsculas con guiones')
            if i in kinds:
                err(rec, 'el id YA existe en src-data/ (a)')
            if i in seen:
                err(rec, 'id repetido en el archivo')
            seen.add(i)
            if t == 'context' and not i.startswith('ctx-'): err(rec, 'id de contexto debe empezar con ctx-')
            if t == 'theory' and not i.startswith('th-'): err(rec, 'id de teoría debe empezar con th-')
            if t == 'institution' and not i.startswith('inst-'): err(rec, 'id de institución debe empezar con inst-')
        # campos obligatorios en inglés
        for f in REQUIRED[t]:
            if rec.get(f) in (None, '', []) and not (f == 'end' and f in rec):
                err(rec, f'falta el campo {f}')
        # regiones y países (plan C5 / punto 61): lo de fuera de Occidente va como global + su país, con influencia demostrable
        regs, ctry = rec.get('regions'), rec.get('countries') or []
        if t != 'link' and t != 'connection':
            for r in regs or []:
                if r not in REGIONS: err(rec, f'regions: {r} no es una de {REGIONS}')
            if any(c in BEYOND for c in ctry) and regs != ['global']:
                err(rec, 'elemento de fuera de Occidente (C5): debe llevar regions: ["global"], su país en countries y una línea de mecanismo de su influencia')
        # (b) ids referenciados
        for f, exp in REF_FIELDS.items():
            v = rec.get(f)
            for i in ([v] if isinstance(v, str) else v if isinstance(v, list) else []):
                if not isinstance(i, str):
                    continue
                if not exists(i):
                    err(rec, f'{f}: el id {i} no existe en src-data/, en el archivo ni en LISTAS-CIERRE.md (b)')
                elif exp and i in kinds and kinds[i] not in exp:
                    err(rec, f'{f}: {i} es {kinds[i]}, se esperaba {"/".join(exp)}')
        for f, exp in LINK_FIELDS.items():
            for i in (rec.get('links') or {}).get(f, []) or []:
                if not exists(i):
                    err(rec, f'links.{f}: el id {i} no existe (b)')
                elif i in kinds and kinds[i] not in exp:
                    err(rec, f'links.{f}: {i} es {kinds[i]}, se esperaba {"/".join(exp)}')
        # (c) español completo y sin campos de más
        es = rec.get('es')
        if not isinstance(es, dict):
            err(rec, 'falta es (c)')
            es = {}
        for f in TEXT[t]:
            if f in rec and rec[f] not in (None, '', []):
                if es.get(f) in (None, '', []):
                    err(rec, f'es.{f} falta (c)')
                elif isinstance(rec[f], list) and (not isinstance(es[f], list) or len(es[f]) != len(rec[f])):
                    err(rec, f'es.{f} debe tener la misma cantidad de elementos que en inglés ({len(rec[f])}) (c)')
        for f in es:
            if f not in TEXT[t]:
                err(rec, f'es trae el campo {f}, que no se traduce (c)')
        # (d) marcas y refs
        if use_refs:
            refs = rec.get('refs')
            if not isinstance(refs, list) or not refs:
                err(rec, 'con --refs hace falta refs con al menos una fuente')
                refs = []
            for n, r in enumerate(refs, 1):
                if not (r.get('label') and r.get('checks') and r.get('url') and r.get('date')):
                    err(rec, f'refs[{n}] necesita label, url, checks y date')
                u = str(r.get('url', ''))
                if not u.startswith('https://'): err(rec, f'refs[{n}]: la URL debe ser https')
                if 'wikipedia.org' in u: err(rec, f'refs[{n}]: Wikipedia no vale como fuente')
                if r.get('date') and not re.match(r'^\d{4}-\d{2}-\d{2}$', str(r['date'])): err(rec, f'refs[{n}]: date AAAA-MM-DD')
            en_m, es_m = marks_of(rec, 'en'), marks_of(rec, 'es')
            if en_m != es_m: err(rec, f'EN y ES deben tener las mismas marcas (EN {sorted(en_m)}, ES {sorted(es_m)})')
            for n in sorted(en_m | es_m):
                if n < 1 or n > len(refs): err(rec, f'la marca [{n}] no tiene fuente (refs trae {len(refs)})')
            for n in range(1, len(refs) + 1):
                if n not in en_m: err(rec, f'la fuente {n} no se cita en el texto')
        else:
            if rec.get('refs'):
                err(rec, 'la Parte I va con refs: [] (d)')
            for lang, src in (('en', rec), ('es', es)):
                for p, s in texts(src):
                    if MARK.search(s):
                        err(rec, f'marca [n] en {lang}{p}: no corresponde en la Parte I (d)')
            if rec.get('where'):
                err(rec, 'where se deja vacío en la Parte I')
        # (e) largos
        if len(str(rec.get('key', ''))) > 210: err(rec, f'key de {len(rec["key"])} caracteres (máximo ~200, tolerancia 210) (e)')
        if len(str(es.get('key', ''))) > 230: err(rec, f'es.key de {len(es["key"])} caracteres (máximo 230) (e)')
        for f, v in (('short', rec.get('short')), ('es.short', es.get('short'))):
            if v and len(v) > 22: err(rec, f'{f} de {len(v)} caracteres (máximo 22) (e)')
        for f, v, mx in (('note', rec.get('note'), 220), ('es.note', es.get('note'), 240)):
            if v and len(v) > mx: err(rec, f'{f} de {len(v)} caracteres (máximo {mx}) (e)')
        # (f) nivel
        if t in HAS_LEVEL and rec.get('level') not in ('essential', 'normal'):
            err(rec, f'level debe ser essential o normal (vino {rec.get("level")!r}) (f)')
        if t not in HAS_LEVEL and 'level' in rec:
            err(rec, 'este tipo no lleva level')
        # (g) año dentro del tramo
        if rng:
            for f in ('start', 'year'):
                y = rec.get(f)
                if isinstance(y, int) and not (rng[0] <= y <= rng[1]):
                    err(rec, f'{f} {y} fuera del tramo {tramo} ({rng[0]}–{rng[1]}) (g)')
            for f in ('start', 'year', 'born'):
                if f in rec and not isinstance(rec[f], int):
                    err(rec, f'{f} debe ser un entero')
    return errs


def main(argv):
    use_refs = '--refs' in argv
    tramo = None
    files = []
    it = iter(argv)
    for a in it:
        if a == '--tramo':
            tramo = next(it, None)
        elif not a.startswith('--'):
            files.append(a)
    if not files:
        print(__doc__); return 2
    bad = 0
    for f in files:
        t = tramo
        if not t:
            pre = os.path.basename(f).split('_')[0]
            t = pre if pre in TRAMOS else None
        if t and t not in TRAMOS:
            print(f'tramo desconocido: {t}'); return 2
        errs = validate(f, use_refs, t, os.environ.get('LHD_SRC') or SRC)
        if errs:
            bad += len(errs)
            print(f'{f}: {len(errs)} error(es)')
            for e in errs:
                print('  ' + e)
        else:
            print(f'{f}: OK')
    if not bad:
        print('OK')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
