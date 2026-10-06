# Aplica fuentes y textos corregidos a elementos, enlaces, conexiones y ensayos YA existentes (Parte II).
# Uso: python3 tools/pipeline/apply2.py [--dry] salida1.json [salida2.json ...]
# Antes: python3 tools/pipeline/check_r2.py salida.json (sin ERROR). Después: python3 tools/build_data.py.
# Todo o nada: si un registro no se encuentra, no se escribe nada. --dry comprueba y cuenta sin escribir.
# `drop: true` (enlaces y conexiones) NO borra: se registra como DROP-PROPUESTO y va a las incidencias (se decide en la hoja .xlsx, R2.6).
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
from lib import _load, _files
from r2lib import ESSAYS, record_key, record_kind

NORM = re.compile(r'\s*((?:\[\d{1,2}\])+)\s*([.,;:])')


def norm(s):
    if isinstance(s, list): return [norm(x) for x in s]
    s = NORM.sub(r'\2\1', s)
    return re.sub(r'\s+((?:\[\d{1,2}\])+)', r'\1', s)


def conn(a, b):
    for p in _files():
        d = _load(p)
        for l in d.get('connections', []) if isinstance(d.get('connections'), list) else []:
            if l['from'] == a and l['to'] == b: return l
    raise KeyError((a, b))


def linkany(c, i):
    for p in _files():
        d = _load(p)
        for l in d.get('links', []) if isinstance(d.get('links'), list) else []:
            if l.get('ctx') == c and l.get('item') == i: return l
    raise KeyError((c, i))


def essay(i):
    for x in _load(ESSAYS)['essays']:
        if x['id'] == i: return x
    raise KeyError(i)


def find(e):
    k = record_kind(e)
    if k == 'enlaces': return linkany(e['ctx'], e['item'])
    if k == 'conexiones': return conn(e['from'], e['to'])
    try: return get(e['id'])
    except KeyError: return essay(e['id'])


def main(argv):
    dry = '--dry' in argv
    files = [a for a in argv if not a.startswith('--')]
    if not files:
        print(__doc__ if __doc__ else 'Uso: apply2.py [--dry] salida.json ...'); return 2
    log = []
    for fn in files:
        for e in json.load(open(fn, encoding='utf-8')):
            x = find(e); lab = record_key(e)
            if e.get('drop'):
                log.append((lab, 'DROP-PROPUESTO', e.get('issues', []))); continue
            x['refs'] = e['refs']
            for k, v in (e.get('en') or {}).items(): x[k] = norm(v)
            for k, v in (e.get('es') or {}).items(): x.setdefault('es', {})[k] = norm(v)
            for k, v in (e.get('other') or {}).items():
                if v is not None: x[k] = v
            log.append((lab, 'ok', e.get('issues', [])))
    if not dry:
        save()
        json.dump(log, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'r2_work', 'log2_' + '_'.join(os.path.basename(f).split('.')[0] for f in files) + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(('(dry) ' if dry else '') + 'applied', sum(1 for l in log if l[1] == 'ok'), '; drop propuestos', sum(1 for l in log if l[1] != 'ok'))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
