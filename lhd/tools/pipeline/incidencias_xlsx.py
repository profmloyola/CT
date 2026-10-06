#!/usr/bin/env python3
"""R2: hoja de cálculo de incidencias (PLAN-V1, R2.6). Lee y escribe tools/r2_incidencias.json (ver r2_incidencias.py).

Uso:
  python3 tools/pipeline/incidencias_xlsx.py export SALIDA.xlsx --siguiente [--n 40]   # arma el bloque siguiente (A, B, D, E y C, en ese orden) y le asigna número
  python3 tools/pipeline/incidencias_xlsx.py export SALIDA.xlsx --bloque N             # vuelve a escribir un bloque ya asignado
  python3 tools/pipeline/incidencias_xlsx.py import ENTRADA.xlsx [--dry]               # lee decision, valor final y nota; no aplica nada a los datos
  python3 tools/pipeline/incidencias_xlsx.py cerrar CLASE [--dry]                      # cierra en bloque las abiertas de una clase (p. ej. C), solo con el visto bueno de Mauricio
  python3 tools/pipeline/incidencias_xlsx.py resumen                                   # conteo por clase y estado

Columnas de la hoja: n° · id · tipo · campo · incidencia · valor actual · propuesta · fuentes · clase · recomendación · decisión · valor final · nota.
Las columnas hasta «recomendación» son de lectura; Mauricio completa «decisión» (Aceptar / Rechazar / Otro), «valor final» (obligatorio con «Otro») y «nota».
`import` rechaza todo el archivo si hay un error (n.º desconocido, id cambiado, decisión inválida, «Otro» sin valor final), para no dejar decisiones a medias.
La clase A de la hoja trae «Aceptar» por defecto solo cuando tiene una corrección concreta (`cambios`); el resto sale en blanco.
Estados: abierta → decidida (al importar una decisión) → aplicada (R2.6, al aplicar los cambios y pasar el build) · cerrada (informativas)."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r2_incidencias import CLASES, ESTADOS, JSON_PATH, cargar

HEAD = ['n°', 'id', 'tipo', 'campo', 'incidencia', 'valor actual', 'propuesta', 'fuentes', 'clase', 'recomendación', 'decisión', 'valor final', 'nota']
WIDTH = [9, 24, 11, 18, 62, 30, 36, 54, 7, 48, 13, 30, 30]
DECISIONES = ('Aceptar', 'Rechazar', 'Otro')
LEGEND = [
    ('Qué es esto', 'Las incidencias son los datos de ficha dudosos y los textos corregidos que salieron de la revisión de fuentes de las fichas ★. Nada de esto se cambió en los datos: espera tu decisión.'),
    ('Cómo decidir', 'En la columna «decisión» elige Aceptar (adoptar la propuesta; si la propuesta dice «Mantener», significa dejar la ficha como está), Rechazar (no hacer nada con esta incidencia) u Otro (escribe en «valor final» lo que debe quedar). La «nota» es libre.'),
    ('Clase A', 'Dato de la ficha contradicho por dos o más fuentes de calidad. Viene con «Aceptar» marcado cuando hay una corrección concreta; cámbialo si no estás de acuerdo.'),
    ('Clase B', 'Fuentes en desacuerdo entre sí. La propuesta es mantener, usar «c.» o un rango.'),
    ('Clase C', 'Texto que el agente ya quitó o suavizó. Informativa: se cierra en bloque salvo que marques alguna.'),
    ('Clase D', 'Campo de ficha dudoso o sin verificar (designers, maker, materials, status, fechas…): propuesta con fuente.'),
    ('Clase E', 'Propuesta de quitar un enlace de contexto o una conexión: no se borra sin tu decisión.'),
    ('Columnas de lectura', 'n°, id, tipo, campo, incidencia, valor actual, propuesta, fuentes, clase y recomendación no se leen al importar (salvo n° e id, que se comprueban). Si ves una clase mal puesta, anótalo en «nota».'),
    ('Fuentes', 'Son las fuentes que abrió el agente para esa ficha (etiqueta y enlace). La incidencia dice cuál sostiene cada cosa.'),
]


def fuentes_txt(i):
    return '\n'.join(f"{f['label']} — {f['url']}" for f in i.get('fuentes', []))


def orden(i):
    return (CLASES.index(i['clase']) if i['clase'] in CLASES else 99, i['id'])


def seleccion(data, n, bloque, siguiente):
    inc = data['incidencias']
    if bloque is not None:
        rows = sorted([i for i in inc if i.get('bloque') == bloque], key=orden)
        if not rows:
            raise SystemExit(f'El bloque {bloque} no existe (aún no se asignó).')
        return rows, bloque
    libres = sorted([i for i in inc if i.get('bloque') is None and i['estado'] == 'abierta'], key=orden)
    if not libres:
        raise SystemExit('No quedan incidencias abiertas sin bloque.')
    nuevo = max([i.get('bloque') or 0 for i in inc] + [0]) + 1
    rows = libres[:n]
    for i in rows:
        i['bloque'] = nuevo
    return rows, nuevo


def export_xlsx(rows, bloque, path):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
    from openpyxl.worksheet.datavalidation import DataValidation
    from openpyxl.worksheet.properties import PageSetupProperties
    wb = Workbook()
    ws = wb.active
    ws.title = f'Bloque {bloque}'
    ws.append(HEAD)
    thin = Side(style='thin', color='BBBBBB')
    fill = {'A': 'F8D7DA', 'B': 'FFF3CD', 'C': 'E9ECEF', 'D': 'D6E9F8', 'E': 'E2D9F3'}
    for c in ws[1]:
        c.font = Font(bold=True, color='FFFFFF')
        c.fill = PatternFill('solid', fgColor='1F3A5F')
        c.alignment = Alignment(vertical='center', wrap_text=True)
    for r, i in enumerate(rows, 2):
        ws.append([i['id'], i['elemento'], i['tipo'], i['campo'], i['texto'], i['actual'], i['propuesta'], fuentes_txt(i), i['clase'], i['recomendacion'],
                   i.get('decision') or '', i.get('valor_final') or '', i.get('nota') or ''])
        lines = 1
        for col, w in zip(ws[r], WIDTH):
            col.alignment = Alignment(vertical='top', wrap_text=True)
            col.border = Border(top=thin, bottom=thin, left=thin, right=thin)
            v = str(col.value or '')
            lines = max(lines, sum(max(1, -(-len(p) // max(1, int(w * 1.05)))) for p in v.split('\n')))
        ws.row_dimensions[r].height = min(15 * lines, 330)
        ws.cell(r, 9).fill = PatternFill('solid', fgColor=fill.get(i['clase'], 'FFFFFF'))
        ws.cell(r, 9).font = Font(bold=True)
        for c in (11, 12, 13):
            ws.cell(r, c).fill = PatternFill('solid', fgColor='FFFFE0')
    for k, w in enumerate(WIDTH, 1):
        ws.column_dimensions[ws.cell(1, k).column_letter].width = w
    ws.row_dimensions[1].height = 24
    ws.freeze_panes = 'C2'
    ws.page_setup.orientation = 'landscape'
    ws.page_setup.paperSize = ws.PAPERSIZE_A3
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
    ws.print_title_rows = '1:1'
    ws.auto_filter.ref = f'A1:{ws.cell(1, len(HEAD)).column_letter}{len(rows) + 1}'
    dv = DataValidation(type='list', formula1='"' + ','.join(DECISIONES) + '"', allow_blank=True, showErrorMessage=True,
                        errorTitle='Decisión', error='Elige Aceptar, Rechazar u Otro (o deja en blanco).')
    ws.add_data_validation(dv)
    dv.add(f'K2:K{len(rows) + 1}')
    ws2 = wb.create_sheet('Instrucciones')
    ws2.column_dimensions['A'].width = 22
    ws2.column_dimensions['B'].width = 120
    ws2.append(['Hoja de incidencias · LHD', f'Bloque {bloque}: {len(rows)} filas, ordenadas de la clase A a la C.'])
    for k, v in LEGEND:
        ws2.append([k, v])
    for row in ws2.iter_rows():
        row[0].font = Font(bold=True)
        for c in row:
            c.alignment = Alignment(vertical='top', wrap_text=True)
    wb.save(path)


def import_xlsx(path, data):
    """Devuelve (cambios, errores). cambios = [(incidencia, decision, valor_final, nota)]."""
    from openpyxl import load_workbook
    wb = load_workbook(path, data_only=True)
    ws = next((s for s in wb.worksheets if [str(c.value or '').strip() for c in s[1]][:len(HEAD)] == HEAD), None)
    if ws is None:
        return [], ['No encuentro una hoja con las columnas esperadas: ' + ' · '.join(HEAD)]
    por_id = {i['id']: i for i in data['incidencias']}
    cambios, errores = [], []
    for n, row in enumerate(ws.iter_rows(min_row=2, values_only=True), 2):
        if not row or not row[0]:
            continue
        inc = str(row[0]).strip()
        i = por_id.get(inc)
        if not i:
            errores.append(f'fila {n}: n.º desconocido «{inc}»')
            continue
        if str(row[1] or '').strip() != i['elemento']:
            errores.append(f'fila {n}: el id «{row[1]}» no coincide con {inc} («{i["elemento"]}»): ¿se movieron filas?')
            continue
        dec = str(row[10] or '').strip()
        dec = next((d for d in DECISIONES if d.lower() == dec.lower()), dec) if dec else ''
        if dec and dec not in DECISIONES:
            errores.append(f'fila {n} ({inc}): decisión inválida «{dec}» (Aceptar, Rechazar u Otro)')
            continue
        final = str(row[11] if row[11] is not None else '').strip()
        nota = str(row[12] if row[12] is not None else '').strip()
        if dec == 'Otro' and not final:
            errores.append(f'fila {n} ({inc}): «Otro» necesita «valor final»')
            continue
        cambios.append((i, dec, final, nota))
    return cambios, errores


def aplicar_import(cambios):
    n_dec = n_borr = 0
    for i, dec, final, nota in cambios:
        if i['estado'] in ('aplicada', 'cerrada'):
            continue                      # lo ya aplicado o cerrado no se reabre desde la hoja
        i['decision'], i['valor_final'], i['nota'] = dec, final, nota
        if dec:
            i['estado'] = 'decidida'
            n_dec += 1
        else:
            i['estado'] = 'abierta'
            n_borr += 1
    return n_dec, n_borr


def resumen(data):
    inc = data['incidencias']
    L = [f'{len(inc)} incidencias', '  clase  ' + '  '.join(f'{e:>9}' for e in ESTADOS) + '    total']
    for c in 'ABCDE':
        f = [sum(1 for i in inc if i['clase'] == c and i['estado'] == e) for e in ESTADOS]
        L.append(f'  {c:<5}  ' + '  '.join(f'{x:>9}' for x in f) + f'    {sum(f):>5}')
    bl = sorted({i['bloque'] for i in inc if i.get('bloque')})
    L.append('  bloques asignados: ' + (', '.join(f'{b} ({sum(1 for i in inc if i.get("bloque") == b)})' for b in bl) or 'ninguno'))
    return '\n'.join(L)


def main(argv):
    if not argv or argv[0] not in ('export', 'import', 'cerrar', 'resumen'):
        print(__doc__)
        return 2
    cmd, args = argv[0], argv[1:]
    dry = '--dry' in args
    pos, skip = [], False
    for a in args:
        if skip:
            skip = False
        elif a in ('--n', '--bloque'):
            skip = True
        elif not a.startswith('--'):
            pos.append(a)
    data = cargar()
    if cmd == 'resumen':
        print(resumen(data))
        return 0
    if cmd == 'cerrar':
        clase = pos[0] if pos else ''
        if clase not in tuple('ABCDE'):
            print('Indica la clase (A a E).')
            return 2
        n = 0
        for i in data['incidencias']:
            if i['clase'] == clase and i['estado'] == 'abierta':
                i['estado'] = 'cerrada'
                n += 1
        if not dry:
            json.dump(data, open(JSON_PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(('(dry) ' if dry else '') + f'{n} incidencias de clase {clase} cerradas')
        return 0
    if not pos:
        print(__doc__)
        return 2
    if cmd == 'export':
        n = int(args[args.index('--n') + 1]) if '--n' in args else 40
        bloque = int(args[args.index('--bloque') + 1]) if '--bloque' in args else None
        if bloque is None and '--siguiente' not in args:
            print('Indica --siguiente o --bloque N.')
            return 2
        rows, b = seleccion(data, n, bloque, '--siguiente' in args)
        export_xlsx(rows, b, pos[0])
        if bloque is None and not dry:
            json.dump(data, open(JSON_PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        por = {c: sum(1 for i in rows if i['clase'] == c) for c in 'ABCDE' if any(i['clase'] == c for i in rows)}
        print(f'Bloque {b}: {len(rows)} filas {por} → {pos[0]}')
        return 0
    cambios, errores = import_xlsx(pos[0], data)
    if errores:
        print('NO SE IMPORTÓ NADA:')
        for e in errores:
            print('  ' + e)
        return 1
    n_dec, n_borr = aplicar_import(cambios)
    if not dry:
        json.dump(data, open(JSON_PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(('(dry) ' if dry else '') + f'{len(cambios)} filas leídas: {n_dec} decididas, {n_borr} sin decisión')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
