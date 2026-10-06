#!/usr/bin/env python3
"""R1.3: correcciones mecánicas de la Parte II (idempotente; se puede correr más de una vez).

Uso (desde la carpeta lhd):   python3 tools/pipeline/r1_limpieza.py [--dry]

1. Etiquetas largas: agrega `short` (EN y ES, máx. 22 caracteres) a los elementos cuya etiqueta de la línea de tiempo
   pasaba de 22 caracteres (lista en tools/pipeline/r1_shorts.py). No toca elementos que ya tienen `short`.
2. Enlaces de contexto repetidos: deja uno solo (el que lleva fuentes o, si empatan, el más específico).
3. Elementos desconectados con enlace seguro (ver ENLACES_NUEVOS).
Escribe src-data/ con el mismo formato de siempre (indent=1, UTF-8). Después corre build_data.py.
"""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
from r1_shorts import SHORTS  # noqa: E402

DRY = '--dry' in sys.argv
LISTS = ('movements', 'institutions', 'designers', 'works', 'contexts', 'production', 'theories', 'concepts')

# (era, ctx, item, nota EN, nota ES). Solo enlaces que el propio texto del proyecto respalda.
ENLACES_NUEVOS = [
    ('postmodern', 'ctx-design-museums', 'inst-design-museum-london',
     'As design became a collectable culture, Terence Conran opened a museum in London in 1989 to show industrial, graphic, fashion and architectural design to a wide public.',
     'Al volverse el diseño una cultura coleccionable, Terence Conran abrió en Londres en 1989 un museo para mostrar a un público amplio el diseño industrial, gráfico, de moda y de arquitectura.'),
]
# enlaces repetidos: (ctx, item) -> índice (0 = primero, 1 = segundo, ...) de la copia que se conserva, entre las que están
# en 80-context-links.json de la era; si una copia está en otro archivo (p. ej. 90-test-*) se conserva esa.
REPETIDOS = {('ctx-urban-informality', 'participatory-social-architecture'): 'ultimo',
             ('ctx-personal-computer', 'macintosh-icons-1984'): 'otro-archivo'}


def load_all():
    files = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'src-data', '*', '*.json'))):
        files[f] = json.load(open(f, encoding='utf-8'))
    return files


def save(files, changed):
    for f in changed:
        if not DRY:
            open(f, 'w', encoding='utf-8').write(json.dumps(files[f], ensure_ascii=False, indent=1) + '\n')


def main():
    files = load_all()
    changed = set()
    # 1. shorts
    n_short = 0
    for f, d in files.items():
        for k in LISTS:
            for x in d.get(k, []):
                if x['id'] in SHORTS and not x.get('short'):
                    en, es = SHORTS[x['id']]
                    x['short'] = en
                    if k != 'designers':   # el nombre de un diseñador no se traduce: un solo `short`
                        x.setdefault('es', {})['short'] = es
                    n_short += 1
                    changed.add(f)
    # 2. enlaces repetidos
    n_dup = 0
    for (c, i), regla in REPETIDOS.items():
        found = [(f, l) for f, d in files.items() for l in d.get('links', []) if l.get('ctx') == c and l.get('item') == i]
        if len(found) < 2:
            continue
        if regla == 'ultimo':
            drop = found[:-1]
        else:   # 'otro-archivo': se conserva la copia que no está en 80-context-links.json
            drop = [t for t in found if os.path.basename(t[0]).startswith('80-')][:len(found) - 1]
        for f, l in drop:
            files[f]['links'].remove(l)
            changed.add(f)
            n_dup += 1
    # 3. enlaces nuevos
    n_new = 0
    for era, c, i, en, es in ENLACES_NUEVOS:
        p = os.path.join(ROOT, 'src-data', era, '80-context-links.json')
        if any(l.get('ctx') == c and l.get('item') == i for d in files.values() for l in d.get('links', [])):
            continue
        files[p]['links'].append({'ctx': c, 'item': i, 'note': en, 'es': {'note': es}, 'refs': []})
        changed.add(p)
        n_new += 1
    save(files, changed)
    print(f"shorts agregados: {n_short}; enlaces repetidos quitados: {n_dup}; enlaces nuevos: {n_new}; archivos tocados: {len(changed)}{' (DRY)' if DRY else ''}")


if __name__ == '__main__':
    main()
