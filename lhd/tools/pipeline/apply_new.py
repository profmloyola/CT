#!/usr/bin/env python3
"""Agrega elementos NUEVOS (Parte I) a src-data/<tramo>/ (plan, paso 0.4).

Uso:
  python3 tools/pipeline/apply_new.py <tramo> salida1.json [salida2.json ...]
  python3 tools/pipeline/apply_new.py <tramo> --links-from-lists            # solo rellena relaciones desde LISTAS-CIERRE.md
Opciones:
  --root DIR         carpeta src-data alternativa (pruebas: trabajar en una COPIA)
  --pendientes FILE  archivo donde anotar los descartes (por omisión tools/PENDIENTES-FUENTES.md)
  --listas FILE      LISTAS-CIERRE.md alternativa
  --no-validate      no correr validate_out.py antes (no se recomienda)

Cada registro lleva `rtype` = context | production | theory | movement | institution | designer | work | link | connection.
Archivo de destino (nombres del Modernismo):
  context  -> 40-context-political / 41-economic / 42-social / 43-cultural / 44-technological  (por `track`)
  production -> 50-production-materials / 51-production-processes / 52-production-tools          (por `sub`)
  theory -> 56-theory.json · movement -> 02-movements.json · institution -> 03-institutions.json · designer -> 10-designers.json
  work -> 20-works-graphic / 21-works-product / 22-works-fashion / 23-works-architecture          (por `discipline`)
  link -> 80-context-links.json · connection -> 85-connections.json
Se rechaza (sin tocar nada) si la validación falla o si un id ya existe. Los registros {"descartado": true} y {"sin_enlace": true}
no se agregan: se anotan en PENDIENTES-FUENTES.md. `refs` queda [] (Parte I).

--links-from-lists: lee las columnas «relaciona» de las tablas de LISTAS-CIERRE.md (primera columna = `id`; la columna «relaciona» trae ids
entre acentos graves) y rellena, solo con ids que existan en src-data/: `links` (movements, institutions, designers, works) de productivo, teoría,
instituciones y movimientos, y `movements` / `institutions` de los diseñadores. No duplica ni inventa ids.
"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import validate_out as V  # noqa: E402

BASE = V.BASE
TRACK_FILE = {'political': '40-context-political', 'economic': '41-context-economic', 'social': '42-context-social',
              'cultural': '43-context-cultural', 'technological': '44-context-technological'}
SUB_FILE = {'materials': '50-production-materials', 'processes': '51-production-processes', 'tools': '52-production-tools'}
DISC_FILE = {'graphic': '20-works-graphic', 'product': '21-works-product', 'fashion': '22-works-fashion', 'architecture': '23-works-architecture'}
LISTKEY = {'context': 'contexts', 'production': 'production', 'theory': 'theories', 'movement': 'movements',
           'institution': 'institutions', 'designer': 'designers', 'work': 'works', 'link': 'links', 'connection': 'connections'}
KIND_LINK_FIELD = {'movement': 'movements', 'institution': 'institutions', 'designer': 'designers', 'work': 'works'}


def target(rec):
    t = rec['rtype']
    if t == 'context':
        return TRACK_FILE[rec['track']]
    if t == 'production':
        return SUB_FILE[rec['sub']]
    if t == 'work':
        return DISC_FILE[rec['discipline']]
    return {'theory': '56-theory', 'movement': '02-movements', 'institution': '03-institutions', 'designer': '10-designers',
            'link': '80-context-links', 'connection': '85-connections'}[t]


def load(path, key):
    if os.path.exists(path):
        return json.load(open(path, encoding='utf-8'))
    return {key: []}


def dump(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write('\n')


def note_pending(pend, tramo, items):
    if not items:
        return
    text = open(pend, encoding='utf-8').read() if os.path.exists(pend) else '# Pendientes de fuentes y descartes\n'
    head = '## Parte I: descartes a la reserva'
    if head not in text:
        text = text.rstrip('\n') + f'\n\n{head}\n'
    add = ''.join(f'- `{i}` · {tramo}: {m}\n' for i, m in items)
    open(pend, 'w', encoding='utf-8').write(text.rstrip('\n') + '\n' + add)


def apply_files(tramo, files, root, pend, validate=True):
    folder = os.path.join(root, tramo)
    if not os.path.isdir(folder):
        sys.exit(f'No existe la carpeta {folder}')
    if validate:
        bad = 0
        for f in files:
            errs = V.validate(f, False, tramo, root)
            if errs:
                bad += len(errs)
                print(f'{f}: {len(errs)} error(es)')
                for e in errs:
                    print('  ' + e)
        if bad:
            sys.exit('No se aplicó nada: corrige los errores de arriba (o devuélvelos al agente).')
    kinds, _ = V.known_ids(root)
    pending, added, files_touched = [], {}, {}
    for f in files:
        for rec in json.load(open(f, encoding='utf-8')):
            t = rec.get('rtype')
            if rec.get('descartado'):
                pending.append((rec['id'], rec.get('motivo', '')))
                continue
            if rec.get('sin_enlace'):
                pending.append((f"{rec.get('ctx') or rec.get('from')}~{rec.get('item') or rec.get('to')}", 'sin enlace: ' + rec.get('motivo', '')))
                continue
            name = target(rec)
            path = os.path.join(folder, name + '.json')
            data = files_touched.get(path) or load(path, LISTKEY[t])
            lst = data.setdefault(LISTKEY[t], [])
            out = {k: v for k, v in rec.items() if k != 'rtype'}
            out.setdefault('refs', [])
            if t == 'link':
                if any(x.get('ctx') == out['ctx'] and x.get('item') == out['item'] for g in glob.glob(os.path.join(root, '*', '80-context-links.json'))
                       for x in json.load(open(g, encoding='utf-8')).get('links', [])):
                    sys.exit(f"El enlace {out['ctx']} -> {out['item']} ya existe; no se aplicó nada más.")
            elif t == 'connection':
                if any(x.get('from') == out['from'] and x.get('to') == out['to'] for x in lst):
                    sys.exit(f"La conexión {out['from']} -> {out['to']} ya existe.")
            else:
                if out['id'] in kinds or out['id'] in added:
                    sys.exit(f"El id {out['id']} ya existe; no se aplicó nada más.")
                added[out['id']] = t
            lst.append(out)
            files_touched[path] = data
    for path, data in files_touched.items():
        dump(path, data)
    note_pending(pend, tramo, pending)
    return added, pending, files_touched


def parse_listas(listas):
    """-> {id: [ids relacionados]} de todas las tablas con columna «relaciona»."""
    rel = {}
    if not os.path.exists(listas):
        return rel
    col = None
    for line in open(listas, encoding='utf-8'):
        s = line.strip()
        if not s.startswith('|'):
            col = None
            continue
        cells = [c.strip() for c in s.strip('|').split('|')]
        if all(re.fullmatch(r':?-{2,}:?', c) for c in cells if c):
            continue
        low = [c.lower() for c in cells]
        if any(c.startswith('relaciona') for c in low):
            col = next(i for i, c in enumerate(low) if c.startswith('relaciona'))
            continue
        if col is None or col >= len(cells):
            continue
        m = re.match(r'`([a-z0-9]+(?:-[a-z0-9]+)*)`', cells[0])
        if m:
            rel.setdefault(m.group(1), [])
            rel[m.group(1)] += [x for x in re.findall(r'`([a-z0-9]+(?:-[a-z0-9]+)*)`', cells[col]) if x not in rel[m.group(1)]]
    return rel


def links_from_lists(tramo, root, listas):
    rel = parse_listas(listas)
    kinds, _ = V.known_ids(root)
    folder = os.path.join(root, tramo)
    n = 0
    for path in sorted(glob.glob(os.path.join(folder, '*.json'))):
        data = json.load(open(path, encoding='utf-8'))
        changed = False
        for key, kind in (('production', 'production'), ('theories', 'theory'), ('institutions', 'institution'), ('movements', 'movement'), ('designers', 'designer')):
            for it in data.get(key, []) or []:
                for r in rel.get(it['id'], []):
                    if r not in kinds or r == it['id']:
                        continue
                    rk = kinds[r]
                    if kind == 'designer':
                        field = {'movement': 'movements', 'institution': 'institutions'}.get(rk)
                        if field and r not in it.setdefault(field, []):
                            it[field].append(r); changed = True; n += 1
                    else:
                        field = KIND_LINK_FIELD.get(rk)
                        if field:
                            lk = it.setdefault('links', {})
                            if r not in lk.setdefault(field, []):
                                lk[field].append(r); changed = True; n += 1
        if changed:
            dump(path, data)
    return n


def main(argv):
    root, pend, listas, validate = V.SRC, os.path.join(BASE, 'tools', 'PENDIENTES-FUENTES.md'), V.LISTAS, True
    args, files, links = [], [], False
    it = iter(argv)
    for a in it:
        if a == '--root': root = os.path.abspath(next(it))
        elif a == '--pendientes': pend = os.path.abspath(next(it))
        elif a == '--listas': listas = os.path.abspath(next(it))
        elif a == '--no-validate': validate = False
        elif a == '--links-from-lists': links = True
        else: args.append(a)
    if not args:
        print(__doc__); return 2
    tramo, files = args[0], args[1:]
    if tramo not in V.TRAMOS:
        print(f'tramo desconocido: {tramo} (uno de {V.TRAMOS})'); return 2
    os.environ['LHD_SRC'] = root
    if files:
        added, pending, touched = apply_files(tramo, files, root, pend, validate)
        by = {}
        for t in added.values():
            by[t] = by.get(t, 0) + 1
        print('agregados:', ', '.join(f'{v} {k}' for k, v in sorted(by.items())) or 'ninguno', '| a la reserva:', len(pending))
        for p in sorted(touched):
            print('  escrito', os.path.relpath(p, root))
    if links:
        print('relaciones rellenadas desde LISTAS-CIERRE.md:', links_from_lists(tramo, root, listas))
    elif not files:
        print('nada que hacer: da archivos o --links-from-lists')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
