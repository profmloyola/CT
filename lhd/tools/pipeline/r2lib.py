"""R2: utilidades comunes de prep_r2.py, check_r2.py, auditoria.py --v1 y r2_incidencias.py.

Tipos de lote (el primer argumento de prep_r2.py): obras, diseñadores, movimientos, instituciones, teorias, contextos, productivos
(elementos con `id`), ensayos (registros de src-essays/essays.json), enlaces (ctxLinks de fichas ★) y conexiones (de fichas ★).
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORK = ROOT + '/tools/pipeline/r2_work'
ESSAYS = ROOT + '/src-essays/essays.json'
MARK = re.compile(r'\[(\d{1,2})\]')
ESS_LINK = re.compile(r'\[\[([^\]|]+)(?:\|([^\]]*))?\]\]')

# tipo de lote -> clave de all.json
KEY = {'obras': 'works', 'diseñadores': 'designers', 'movimientos': 'movements', 'instituciones': 'institutions',
       'teorias': 'theories', 'contextos': 'contexts', 'productivos': 'production'}
# todos los tipos con `refs` y `id`
ELEMENT_KEYS = ('works', 'designers', 'movements', 'institutions', 'theories', 'contexts', 'production', 'concepts')
# fichas de diseño: las que pueden ser ★ (alcance de enlaces y conexiones)
STAR_KEYS = ('works', 'designers', 'movements', 'institutions', 'theories')
# tipos de lote con lote por defecto de 8 fichas; los demás
DEFAULT_N = {'enlaces': 15, 'conexiones': 15, 'ensayos': 2}
KINDS = tuple(KEY) + ('ensayos', 'enlaces', 'conexiones')

# campos que el agente puede escribir en en/es, por tipo de elemento (clave de all.json)
FIELDS = {
    'works': ('key', 'more'),
    'designers': ('key', 'more', 'dates'),
    'movements': ('key', 'traits', 'context', 'shift'),
    'institutions': ('key', 'more'),
    'theories': ('key', 'ideas', 'impact'),
    'contexts': ('key', 'happened', 'effect'),
    'production': ('key', 'origin', 'enabled', 'change', 'economy', 'relations'),
    'concepts': ('key', 'more'),
}
# campos de nivel superior que el agente puede cambiar con `other` (solo cuando una fuente lo exige y se anota en issues)
OTHER_OK = ('materials', 'status', 'date', 'year', 'dates', 'maker', 'client', 'designers', 'tech', 'place', 'countries')


def load_all():
    p = ROOT + '/data/all.json'
    if not os.path.exists(p):
        raise SystemExit('No existe data/all.json: corre antes python3 tools/build_data.py')
    return json.load(open(p, encoding='utf-8'))


def load_essays():
    return json.load(open(ESSAYS, encoding='utf-8'))['essays']


def registry(d):
    """id -> (clave de all.json, ficha)."""
    return {x['id']: (k, x) for k in ELEMENT_KEYS for x in d.get(k, [])}


def star_ids(d):
    return {x['id'] for k in STAR_KEYS for x in d[k] if x.get('star')}


def year_of(x):
    for f in ('year', 'start', 'born'):
        if isinstance(x.get(f), int):
            return x[f]
    return 0


def sort_key(d, x):
    order = {e['id']: i for i, e in enumerate(d['eras'])}
    return (order.get(x.get('era'), 99), year_of(x))


def link_key(l):
    return l['ctx'] + '~' + l['item']


def conn_key(c):
    return c['from'] + '>' + c['to']


def record_key(r):
    """Clave estable de un registro de lote o de salida: id, ctx~item o from>to."""
    if 'ctx' in r and 'item' in r:
        return link_key(r)
    if 'from' in r and 'to' in r:
        return conn_key(r)
    return r.get('id')


def record_kind(r):
    if 'ctx' in r and 'item' in r:
        return 'enlaces'
    if 'from' in r and 'to' in r:
        return 'conexiones'
    return 'id'


def marks_of(v):
    """Números de marca [n] que aparecen en un texto, lista de textos o diccionario."""
    return {int(m) for m in MARK.findall(v if isinstance(v, str) else json.dumps(v, ensure_ascii=False))}


def label(reg, i):
    """Nombre corto de un elemento para mostrarlo al agente."""
    if i not in reg:
        return i
    x = reg[i][1]
    return x.get('name') or x.get('title') or i


def brief(reg, i):
    """{name, date, key} de un elemento (contexto breve para el agente en enlaces, conexiones y ensayos)."""
    if i not in reg:
        return {'name': i}
    x = reg[i][1]
    return {k: v for k, v in (('name', x.get('name')), ('date', x.get('date') or x.get('year')), ('key', MARK.sub('', x.get('key') or ''))) if v}
