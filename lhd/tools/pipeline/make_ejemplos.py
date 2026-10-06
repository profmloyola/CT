#!/usr/bin/env python3
"""Genera tools/pipeline/EJEMPLOS.md (y tools/tests/ejemplos_ok.json) con un registro REAL por tipo copiado del Modernismo,
mostrado como se escribirá la Parte I: sin refs, sin marcas [n], sin where, sin wiki ni sources. Uso: python3 tools/pipeline/make_ejemplos.py"""
import copy, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import get, link, BASE, _load, ROOT  # noqa: E402

MARK = re.compile(r'\s?(?:\[\d{1,2}\])+')
DROP = ('refs', 'where', 'wiki', 'sources')

def clean(o):
    if isinstance(o, str):
        return re.sub(r'\s+([.,;:])', r'\1', MARK.sub('', o)).strip()
    if isinstance(o, list):
        return [clean(x) for x in o]
    if isinstance(o, dict):
        return {k: clean(v) for k, v in o.items() if k not in DROP}
    return o

def rec(t, x):
    out = {'rtype': t}
    out.update(clean(copy.deepcopy(x)))
    out['refs'] = []
    return out

PICK = [('context', 'ctx-fordism'), ('production', 'tubular-steel'), ('theory', 'th-vers-une-architecture'),
        ('movement', 'de-stijl'), ('institution', 'inst-bauhaus'), ('designer', 'gropius'),
        ('work', 'barcelona-chair'), ('work', 'kitchener-poster')]
recs = [rec(t, get(i)) for t, i in PICK]
l = link('ctx-first-world-war', 'kitchener-poster')
recs.append(rec('link', {k: v for k, v in l.items()}))
c = next(x for x in _load(ROOT + '/modernism/85-connections.json')['connections'] if x['from'] == 'kitchener-poster' and x['to'] == 'i-want-you-poster')
recs.append(rec('connection', c))

NOTES = {
    'ctx-fordism': 'Hecho de contexto. `happened` cuenta qué pasó; `effect` explica el efecto sobre el diseño (el mecanismo). Va en `src-data/<tramo>/4x-context-<track>.json`.',
    'tubular-steel': 'Productivo (material, proceso o herramienta). Necesita `links` a algún movimiento, institución, diseñador u obra. Va en `5x-production-*.json` según `sub`.',
    'th-vers-une-architecture': 'Teoría (el id empieza con `th-`). `ideas` lleva 3 a 5 elementos y `short` es solo el apellido. En la Parte I no lleva `sources` (el build lo avisa como WARN; se agregan en la Parte II).',
    'de-stijl': 'Movimiento. `traits` y la traducción `es.traits` deben tener la misma cantidad de elementos.',
    'inst-bauhaus': 'Institución (el id empieza con `inst-`). `end` es obligatorio (año, o `null` si sigue activa).',
    'gropius': 'Diseñador. Años y lugares de nacimiento y muerte solo si se conocen con certeza (si no, solo años).',
    'barcelona-chair': 'Obra ★ (`level: essential`). Debe tener `designers`, `maker` o `client`; las ★ llevan al menos 2 enlaces de contexto de subcategorías distintas (se definen en LISTAS-CIERRE.md).',
    'kitchener-poster': 'Obra Normal en el modelo de datos del Modernismo (aquí aparece con el nivel que tiene hoy). Sin `designers` pero con `maker`.',
}
lines = ['# Ejemplos de registros (Parte I: sin fuentes)', '',
         '*Generado por `python3 tools/pipeline/make_ejemplos.py` a partir de registros reales del Modernismo. Se muestran como se escribirá la Parte I: `refs: []`, sin marcas `[n]`, sin `where`, sin `wiki` y sin `sources`. Copia SUS campos, su orden y sus largos. Cada registro lleva `rtype` (el tipo de registro; en las obras `type` ya es el tipo de obra: chair, poster...).*', '',
         'Reglas que no se ven en los ejemplos: ids en minúsculas con guiones y fijos (los da `LISTAS-CIERRE.md`); `level` solo `essential` o `normal`; `key` una frase (≤ 200 caracteres); `short` ≤ 22; nota de enlace ≤ 220 y explica el MECANISMO; español de Chile completo en `es`; sin citas textuales ni cifras dudosas.', '']
for r in recs:
    key = r.get('id') or f"{r.get('ctx') or r.get('from')} → {r.get('item') or r.get('to')}"
    note = NOTES.get(r.get('id'), 'Enlace de contexto: `ctx` (hecho) → `item` (elemento de diseño); la nota explica el mecanismo en 1 o 2 frases.' if r['rtype'] == 'link'
                     else 'Conexión entre dos elementos de diseño (influencia, continuidad); la nota aclara si es influencia o causa.')
    lines += [f"## {r['rtype']} · `{key}`", '', note, '', '```json', json.dumps(r, ensure_ascii=False, indent=1), '```', '']
open(os.path.join(BASE, 'tools/pipeline/EJEMPLOS.md'), 'w', encoding='utf-8').write('\n'.join(lines))
json.dump(recs, open(os.path.join(BASE, 'tools/tests/ejemplos_ok.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('EJEMPLOS.md:', len(recs), 'registros')
