# -*- coding: utf-8 -*-
"""Etapa 7: regenera los anexos (tablas A a F) de tools/REVISION-EDITORIAL-ETAPA7.md a partir de REVISION-ETAPA7.json y REVISION-ETAPA7-AJUSTES.json.
Uso: python3 tools/pipeline/etapa7_anexos.py [SALIDA.md]   (sin argumento, imprime en pantalla). Útil después del V4 para dejar las tablas al día."""
import json, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
R = json.load(open(os.path.join(BASE, 'tools', 'REVISION-ETAPA7.json'), encoding='utf-8'))
A = json.load(open(os.path.join(BASE, 'tools', 'REVISION-ETAPA7-AJUSTES.json'), encoding='utf-8'))
d = json.load(open(os.path.join(BASE, 'data', 'all.json'), encoding='utf-8'))
NAME = {}
for k in ['works', 'designers', 'movements', 'institutions', 'theories', 'contexts', 'production']:
    for x in d[k]:
        NAME[x['id']] = (x.get('es') or {}).get('title') or (x.get('es') or {}).get('name') or x.get('title') or x.get('name')
for r in R:
    NAME[r['id']] = r.get('title_es') or r.get('name_es') or r.get('title') or r.get('name')
ERA = {'industrial': 'Industrial', 'reform': 'Reforma', 'modernism': 'Modernismo', 'postwar': 'Posguerra', 'postmodern': 'Posmoderno'}
DISC = {'graphic': 'Gráfico', 'product': 'Producto', 'fashion': 'Moda', 'architecture': 'Arquitectura'}
LV = {'essential': '★', 'normal': 'C'}
out = []
w = out.append


def cnt(t):
    rs = [r for r in R if r['rtype'] == t]
    c = {p: sum(1 for r in rs if r['prioridad'] == p) for p in 'ABC'}
    return f"{len(rs)}: {c['A']} A, {c['B']} B, {c['C']} C (Parte III)"


def links_txt(r):
    parts = []
    for l in r.get('links') or []:
        if l['tipo'] == 'directo':
            parts.append(f"`{l['ctx']}`")
        else:
            parts.append(f"↳ `{l['via']}`")
    return ', '.join(parts)


w('## Anexo A. Elementos nuevos (fichas por crear)\n')
w('Todos están en `tools/REVISION-ETAPA7.json` con el formato de `PROPUESTA-ETAPA6.json` (campos `rtype`, `id`, nombres EN/ES, años, disciplina, región, `level`, `prioridad`, `curso`, `links` con su línea de mecanismo; `duda` cuando hay un dato por verificar; `reserva_origen` cuando se repone desde la reserva). '
  'Nivel: ★ imprescindible, C Completo. Prioridad: **A** falta grave del canon; **B** recomendable para un relato completo; **C** opcional. En «Conexiones», `ctx-…` es un enlace de contexto directo y ↳ una conexión secundaria.\n')

w(f'### A.1 Obras ({cnt("work")})\n')
for era in ['industrial', 'reform', 'modernism', 'postwar', 'postmodern']:
    rows = [r for r in R if r['rtype'] == 'work' and r['era'] == era]
    if not rows: continue
    w(f'**{ERA[era]}**\n')
    w('| Prio. | id | Obra | Año | Disciplina | Autor | Nivel | Por qué | Conexiones |')
    w('|---|---|---|---|---|---|---|---|---|')
    for r in sorted(rows, key=lambda r: (r['prioridad'], r['discipline'], r['year'])):
        aut = ', '.join(f'`{x}`' for x in r['designers']) or (r.get('maker') or '')
        extra = (' ⚠ ' + r['duda']) if r.get('duda') else ''
        rep = ' (repuesta desde la reserva)' if r.get('reserva_origen') else ''
        w(f"| {r['prioridad']} | `{r['id']}` | {r['title_es']} | {r.get('date') or r['year']} | {DISC[r['discipline']]} | {aut} | {LV[r['level']]} | {r['curso']}{rep}{extra} | {links_txt(r)} |")
    w('')

w(f'### A.2 Diseñadores ({cnt("designer")})\n')
w('| Prio. | id | Nombre | Fechas | Disciplinas | País | Nivel | Por qué | Conexiones |')
w('|---|---|---|---|---|---|---|---|---|')
for r in sorted([r for r in R if r['rtype'] == 'designer'], key=lambda r: (r['prioridad'], r['born'] or 0)):
    f = f"{r['born']}–{r['died'] or ''}" if r['kind'] == 'person' else f"desde {r['born']}" if not r['died'] else f"{r['born']}–{r['died']}"
    extra = (' ⚠ ' + r['duda']) if r.get('duda') else ''
    rep = ' (repuesto desde la reserva)' if r.get('reserva_origen') else ''
    w(f"| {r['prioridad']} | `{r['id']}` | {r['name']} | {f} | {', '.join(DISC[x] for x in r['disciplines'])} | {', '.join(r['countries'])} | {LV[r['level']]} | {r['curso']}{rep}{extra} | {links_txt(r)} |")
w('')

w(f'### A.3 Movimientos ({cnt("movement")})\n')
w('| Prio. | id | Nombre | Años | Nivel | Por qué | Miembros propuestos |')
w('|---|---|---|---|---|---|---|')
for r in [r for r in R if r['rtype'] == 'movement']:
    w(f"| {r['prioridad']} | `{r['id']}` | {r['name_es']} | {r['start']}–{r['end'] or ''} | {LV[r['level']]} | {r['curso']}{(' Nota: ' + r['nota']) if r.get('nota') else ''} | {', '.join('`'+x+'`' for x in r['miembros'])} |")
w('')

w(f'### A.4 Instituciones ({cnt("institution")})\n')
w('| Prio. | id | Nombre | Tipo | Años | Lugar | Por qué | Conexiones |')
w('|---|---|---|---|---|---|---|---|')
for r in [r for r in R if r['rtype'] == 'institution']:
    extra = (' ⚠ ' + r['duda']) if r.get('duda') else ''
    w(f"| {r['prioridad']} | `{r['id']}` | {r['name_es']} | {r['kind']} | {r['start']}–{r['end'] or ''} | {r['place']} | {r['curso']}{extra} | {links_txt(r)} |")
w('')

w(f'### A.5 Teoría ({cnt("theory")})\n')
w('| Prio. | id | Obra | Autor | Año | Nivel | Por qué | Conexiones |')
w('|---|---|---|---|---|---|---|---|')
for r in sorted([r for r in R if r['rtype'] == 'theory'], key=lambda r: (r['prioridad'], r['year'])):
    extra = (' ⚠ ' + r['duda']) if r.get('duda') else ''
    w(f"| {r['prioridad']} | `{r['id']}` | *{r['name_es']}* | {r['author']} | {r['year']} | {LV[r['level']]} | {r['curso']}{extra} | {links_txt(r)} |")
w('')

w(f'### A.6 Hechos de contexto ({cnt("context")})\n')
w('| Prio. | id | Hecho | Fecha | Subcategoría | Por qué | Explica a |')
w('|---|---|---|---|---|---|---|')
TR = {'political': 'Político', 'economic': 'Económico', 'social': 'Social', 'cultural': 'Cultural', 'technological': 'Tecnológico'}
for r in [r for r in R if r['rtype'] == 'context']:
    ex = ', '.join('`' + e['id'] + '`' for e in r['explica']) or '—'
    extra = (' **' + r['nota'] + '**') if r.get('nota') else ''
    rep = ' (repuesto desde la reserva)' if r.get('reserva_origen') else ''
    w(f"| {r['prioridad']} | `{r['id']}` | {r['name_es']} | {r['date']} | {TR[r['track']]} | {r['curso']}{rep}{extra} | {ex} |")
w('')

w(f'### A.7 Productivo ({cnt("production")})\n')
w('| Prio. | id | Nombre | Desde | Tipo | Por qué | Obras que lo llevan en `tech` |')
w('|---|---|---|---|---|---|---|')
for r in [r for r in R if r['rtype'] == 'production']:
    w(f"| {r['prioridad']} | `{r['id']}` | {r['name_es']} | {r['start']} | {r['sub']} | {r['curso']}{(' ' + r['nota']) if r.get('nota') else ''} | {', '.join('`'+x+'`' for x in r['anclas']) or '—'} |")
w('')

w('## Anexo B. Cambios de nivel\n')
w('Validados contra v44: cada id existe y está hoy en el nivel «de». Un diseñador que sube a ★ necesita una obra ★ (regla dura del build): la columna «Requiere» lo indica.\n')
for key, title in [('niveles_obras_sube', 'B.1 Obras que suben a ★ (33)'), ('niveles_obras_baja', 'B.2 Obras que bajan a Completo (20)'),
                   ('niveles_disenadores_sube', 'B.3 Diseñadores que suben a ★ (23)'), ('niveles_disenadores_baja', 'B.4 Diseñadores que bajan a Completo (7)'),
                   ('niveles_movimientos', 'B.5 Movimientos (6 suben, 6 bajan)'), ('niveles_instituciones', 'B.6 Instituciones (2 suben, 3 bajan)'),
                   ('niveles_teoria', 'B.7 Teoría (2 bajan; suben las nuevas de Morris y Hitchcock-Johnson)')]:
    w(f'### {title}\n')
    w('| id | Nombre | De → a | Motivo | Requiere |')
    w('|---|---|---|---|---|')
    for r in A[key]:
        w(f"| `{r['id']}` | {NAME.get(r['id'], '')} | {LV[r['de']]} → {LV[r['a']]} | {r['motivo']} | {r.get('requiere', '')} |")
    w('')

w('## Anexo C. Fusiones, renombres y retiros\n')
w('| Acción | Elementos | Detalle |')
w('|---|---|---|')
for r in A['fusiones_y_renombres']:
    ids = r.get('ids') or [r.get('id')]
    det = r['motivo']
    for k in ['queda', 'nuevo_nombre', 'start', 'track']:
        if k in r: det = f"**{k}:** {r[k]}. " + det
    w(f"| {r['accion']} | {', '.join('`'+i+'`' for i in ids)} | {det} |")
w('')

w('## Anexo D. Pertenencias que faltan (sin redacción nueva)\n')
w(A['pertenencia_movimientos']['_como'] + '\n')
w('| Movimiento | Agregar como miembros |')
w('|---|---|')
for k, v in A['pertenencia_movimientos'].items():
    if k.startswith('_'): continue
    w(f"| `{k}` | {', '.join(('`'+x+'`') if not x.startswith(('—', '(')) and ' ' not in x else x for x in v)} |")
w('')
w(A['pertenencia_instituciones']['_como'] + '\n')
w('| Institución | Agregar a `links` |')
w('|---|---|')
for k, v in A['pertenencia_instituciones'].items():
    if k.startswith('_'): continue
    w(f"| `{k}` | {', '.join(('`'+x+'`') if not x.startswith(('—', '(')) and ' ' not in x else x for x in v)} |")
w('')

w('## Anexo E. Correcciones de datos\n')
w('| id | Campo | Hoy | Propuesto | Motivo |')
w('|---|---|---|---|---|')
for r in A['correcciones']:
    w(f"| `{r['id']}` | {r['campo']} | {r['actual']} | {r['propuesto']} | {r['motivo']} |")
w('')
w('## Anexo F. A la reserva (aprobado en el V4, decisión D7)\n')
w('| id | Nombre | Motivo |')
w('|---|---|---|')
for r in A['candidatos_reserva_aprobados_V4']:
    w(f"| `{r['id']}` | {NAME.get(r['id'], '')} | {r['motivo']} |")
w('')
w('## Anexo G. Enlaces de contexto para las ★ (decisión D3)\n')
w(A['enlaces_estrella']['_como'] + '\n')
w('| id | Obra | Enlaces directos hoy | Tipo | Propuesta / nota |')
w('|---|---|---|---|---|')
for r in A['enlaces_estrella']['lista']:
    prop = '; '.join(f"`{p['ctx']}`: {p['mecanismo']}" for p in r.get('propuesta', []))
    nota = (' ' + r['nota']) if r.get('nota') else ''
    w(f"| `{r['id']}` | {NAME.get(r['id'], '')} | {', '.join(r['hoy'])} | {r['tipo']} | {prop}{nota} |")
w('')
import sys; (open(sys.argv[1], 'w', encoding='utf-8').write('\n'.join(out)) if len(sys.argv) > 1 else print('\n'.join(out)))
print(len(out), 'líneas')
