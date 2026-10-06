#!/usr/bin/env python3
"""R2: incidencias de la verificación de fuentes, como DATOS (tools/r2_incidencias.json) y como documento (tools/R2-INCIDENCIAS.md).

Uso:  python3 tools/pipeline/r2_incidencias.py [--dry]
Reúne los `issues` de todas las salidas aplicadas (lote*.json y out_*.json de r2_work) y los `drop` propuestos, los AGREGA a
tools/r2_incidencias.json (clave = sha1 de elemento + texto: lo ya registrado no se vuelve a crear ni se pisa) y reescribe el .md.
Después del primer registro, el JSON es la fuente de verdad: se puede borrar r2_work sin perder incidencias.

Cada incidencia: id (INC-0001…), clave, elemento (id, ctx~item o from>to), tipo, campo, actual, propuesta, cambios (opcional: lista de
{id, campo, idioma en|es|-, de, a} que un paso posterior de la R2.6 puede aplicar), fuentes [{label,url}],
clase (A|B|C|D|E), clase_origen (auto|manual), recomendacion, texto, origen, estado (abierta|decidida|aplicada|cerrada),
bloque (n.º de la hoja .xlsx en que se envió), decision (Aceptar|Rechazar|Otro), valor_final, nota.

Clases (PLAN-V1, R2.6; la E es una ampliación para las propuestas de quitar):
  A  dato de la ficha contradicho por 2 o más fuentes de calidad: la hoja llega con la corrección aceptada por defecto
  B  fuentes en desacuerdo entre sí: se propone «c.», un rango o mantener
  C  texto que el agente ya quitó o suavizó: informativa; se cierra en bloque salvo que se marque alguna
  D  campo de ficha dudoso o sin verificar (designers, maker, materials, status, fechas…): propuesta con fuente
  E  propuesta de quitar un enlace de contexto o una conexión (`drop`): no se borra sin decisión
La clase automática (clase_origen auto) es un primer filtro por palabras clave: se corrige a mano en el JSON (clase_origen manual).
"""
import glob
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r2lib import ROOT, WORK, load_all, record_key, registry

JSON_PATH = ROOT + '/tools/r2_incidencias.json'
MD_PATH = ROOT + '/tools/R2-INCIDENCIAS.md'
CLASES = ('A', 'B', 'D', 'E', 'C')       # orden de revisión: lo que más pesa primero
ESTADOS = ('abierta', 'decidida', 'aplicada', 'cerrada')
TIPOS = {'works': 'obra', 'designers': 'diseñador', 'movements': 'movimiento', 'institutions': 'institución', 'theories': 'teoría',
         'contexts': 'contexto', 'production': 'productivo', 'concepts': 'concepto'}
# campos de ficha que las incidencias nombran (en `código` o como «campo x»); (regex, nombre del campo)
CAMPOS = [(re.compile(p, re.I), n) for p, n in (
    (r'\bstatus\b', 'status'), (r'\bmaterials?\b', 'materials'), (r'\btech\b', 'tech'), (r'\bdesigners\b', 'designers'),
    (r'\bmaker\b', 'maker'), (r'\bclient\b', 'client'), (r'\bcountries\b', 'countries'), (r'\bplace\b', 'place'),
    (r'\bdates\b', 'dates'), (r'(?:campo|field|`)\s*(?:year|date)\b|\byear/date\b|\bdate\b|\byear\b', 'year/date'),
    (r'\bstart\b|\bend\b', 'start/end'))]
NO_TOCADO = re.compile(r'no se (tocó|tocan|cambia|cambian|cambió|modificó|modifican|alteró|corrigió|corrige|añadió)|sin tocar|queda(?:n)? sin tocar|no (lo |la )?toqué|no (lo |la )?cambié|no se ha tocado|'
                       r'se mantiene|se mantuvo|conservé|mantuve|dejé el campo|queda(?:n)? sin|no se modific|pendiente de verificar|revisar\b|sin cambio|se conserv\w+ por la ficha', re.I)
FICHA = re.compile(r'\bficha\b|ERROR DE LA FICHA|DATO DE LA FICHA', re.I)
FICHA_ERROR = re.compile(r'ERROR DE LA FICHA|DATO DE LA FICHA|DESACTUALIZADO')
REC_AUTO = {'C': 'Informativa: el agente ya quitó o suavizó el texto. Se cierra en bloque salvo que marques alguna.'}
CONTRADICE = re.compile(r'contradic|corrección de fondo|erróne|equivocad|falleci|fallec|murió|nació|nacimiento|no es .{0,40} sino|atribuy\w+ (el )?(invento|diseño)', re.I)
DESACUERDO = re.compile(r'difier|discrep|desacuerdo|disienten|divergen|no coinciden|contradictori|distintas fechas|\bvs\.?\b|según .{3,60} según|mientras que|\d{3,4} ?/ ?\d{3,4}', re.I)


def clave(elemento, texto):
    return hashlib.sha1((elemento + '|' + texto).encode('utf-8')).hexdigest()[:12]


def campos_de(texto):
    out = []
    for rx, n in CAMPOS:
        if rx.search(texto) and n not in out:
            out.append(n)
    return out


def clasificar(texto, drop=False):
    """(clase, campo) automáticos."""
    if drop:
        return 'E', ''
    campos = campos_de(texto)
    if DESACUERDO.search(texto) and (campos or NO_TOCADO.search(texto) or re.search(r'dice|dan |da ', texto)):
        return 'B', ', '.join(campos)
    if FICHA_ERROR.search(texto):
        return 'A', ', '.join(campos)
    if (campos or FICHA.search(texto)) and NO_TOCADO.search(texto):
        return ('A' if CONTRADICE.search(texto) else 'D'), ', '.join(campos)
    return 'C', ''


def tipo_de(el, reg):
    if '~' in el:
        return 'enlace'
    if '>' in el:
        return 'conexión'
    if el in reg:
        return TIPOS.get(reg[el][0], reg[el][0])
    return 'ensayo' if el.startswith(('lens-', 'disc-')) else '?'


def valor_actual(reg, elemento, campo):
    """Valor actual de los campos de ficha en data/all.json (texto), para la hoja."""
    if elemento not in reg or not campo:
        return ''
    x = reg[elemento][1]
    out = []
    varios = len(campo.split(', ')) > 1
    for c in campo.split(', '):
        names = {'year/date': ('year', 'date'), 'start/end': ('start', 'end')}.get(c, (c,))
        for n in names:
            v = x.get(n)
            if v in (None, '', []):
                continue
            if isinstance(v, (list, dict)):
                v = json.dumps(v, ensure_ascii=False)
            out.append(f'{n}: {v}' if varios or len(names) > 1 else str(v))
    return '\n'.join(out)


def cargar():
    if os.path.exists(JSON_PATH):
        return json.load(open(JSON_PATH, encoding='utf-8'))
    return {'version': 1, 'nota': 'Generado por tools/pipeline/r2_incidencias.py; después del primer registro es la fuente de verdad (ver el docstring del script).', 'incidencias': []}


def recolectar():
    """[(elemento, texto, drop, fuentes, origen)] de las salidas que hay en r2_work."""
    files = sorted(glob.glob(WORK + '/lote*.json')) + sorted(glob.glob(WORK + '/out_*.json'))
    rows = []
    for f in files:
        for e in json.load(open(f, encoding='utf-8')):
            el = record_key(e)
            fuentes = [{'label': r.get('label', ''), 'url': r.get('url', '')} for r in (e.get('refs') or [])]
            for s in e.get('issues') or []:
                rows.append((el, s, bool(e.get('drop')), fuentes, os.path.basename(f)))
    return rows


def merge(data, rows, reg):
    known = {i['clave'] for i in data['incidencias']}
    n = max([int(i['id'][4:]) for i in data['incidencias']] + [0])
    nuevas = 0
    for el, texto, drop, fuentes, origen in rows:
        k = clave(el, texto)
        if k in known:
            continue
        known.add(k)
        n += 1
        clase, campo = clasificar(texto, drop)
        data['incidencias'].append({
            'id': f'INC-{n:04d}', 'clave': k, 'elemento': el, 'tipo': tipo_de(el, reg), 'campo': campo, 'actual': valor_actual(reg, el, campo),
            'propuesta': '', 'cambios': [], 'fuentes': fuentes, 'clase': clase, 'clase_origen': 'auto', 'recomendacion': REC_AUTO.get(clase, ''), 'texto': texto, 'origen': origen,
            'estado': 'abierta', 'bloque': None, 'decision': '', 'valor_final': '', 'nota': ''})
        nuevas += 1
    return nuevas


def escribir_md(data):
    L = ['# R2: incidencias de la verificación de fuentes', '',
         'Generado por `tools/pipeline/r2_incidencias.py` desde `tools/r2_incidencias.json` (la fuente de verdad). Por elemento: lo que se quitó, suavizó o corrigió y '
         'los datos de la ficha que las fuentes ponen en duda y **no se tocaron**. Clases: A dato contradicho · B fuentes en desacuerdo · C texto ya corregido · '
         'D campo de ficha dudoso · E propuesta de quitar un enlace o conexión. Se deciden en la hoja `.xlsx` (`incidencias_xlsx.py`).', '']
    por = {}
    for i in data['incidencias']:
        por.setdefault(i['elemento'], []).append(i)
    for el, lst in por.items():
        L.append(f'## `{el}`')
        L += [f"- **{i['clase']}** · {i['estado']} · {i['id']}: {i['texto']}" for i in lst]
        L.append('')
    open(MD_PATH, 'w', encoding='utf-8').write('\n'.join(L))
    return len(por)


def main(argv):
    d = load_all()
    reg = registry(d)
    data = cargar()
    nuevas = merge(data, recolectar(), reg)
    if '--dry' not in argv:
        json.dump(data, open(JSON_PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        n_el = escribir_md(data)
    else:
        n_el = len({i['elemento'] for i in data['incidencias']})
    por_clase = {c: sum(1 for i in data['incidencias'] if i['clase'] == c) for c in 'ABCDE'}
    print(f"{len(data['incidencias'])} incidencias ({nuevas} nuevas) de {n_el} elementos; por clase {por_clase} → tools/r2_incidencias.json y tools/R2-INCIDENCIAS.md")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
