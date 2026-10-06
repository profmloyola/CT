#!/usr/bin/env python3
"""Etapa 7 (pasos 7.5 y 7.6; v46): arma los lotes de redacción a partir de tools/REVISION-ETAPA7.json (solo `estado: aprobado-V4`)
y de tools/REVISION-ETAPA7-AJUSTES.json (enlaces de las ★ de la decisión D3 y textos de elementos existentes que hay que reescribir).
Copia adaptada de prep_etapa6.py (misma lógica de lotes, enlaces y campos).

Uso: python3 tools/pipeline/prep_etapa7.py OUTDIR
Escribe OUTDIR/<tramo>_<grupo><n>.json (fichas nuevas), OUTDIR/<tramo>_e<n>.json (enlaces D3 de obras ★ existentes),
OUTDIR/textos_<n>.json (reescrituras de fichas existentes) y OUTDIR/INDICE.txt. No toca src-data/.
No incluye lo que repone ajustes_etapa7.py desde la reserva (`reserva_origen`), salvo el contexto ctx-photography, que se redacta con sus enlaces.
Cada registro de entrada trae: la propuesta + `escribir_links` (pares ctx -> elemento que el agente debe redactar como registros `link`),
`escribir_conexiones` (pares elemento -> elemento que el agente redacta como `connection`) y `campos` (relaciones que el propio registro debe llevar).
Las demás relaciones (miembros de movimientos, obras de instituciones, pertenencias) las fija después
`ajustes_etapa7.py relaciones --aplicar` (sin agentes).
"""
import collections, glob, json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(BASE, 'tools', 'pipeline'))
import validate_out as V  # noqa: E402

ERAS = [('industrial', 0, 1850), ('reform', 1851, 1913), ('modernism', 1914, 1944), ('postwar', 1945, 1974), ('postmodern', 1975, 9999)]
FIELD_OF = {  # (tipo del elemento, tipo de la vía) -> campo del propio elemento
    ('work', 'designer'): 'designers', ('work', 'movement'): 'movements', ('work', 'production'): 'tech',
    ('designer', 'movement'): 'movements', ('designer', 'institution'): 'institutions',
}
LINKS_OF = {'designer': 'designers', 'work': 'works', 'movement': 'movements', 'institution': 'institutions'}


def era_of(y):
    for k, a, b in ERAS:
        if a <= y <= b:
            return k
    return 'postmodern'


def main():
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    recs = [r for r in json.load(open(os.path.join(BASE, 'tools', 'REVISION-ETAPA7.json'), encoding='utf-8'))
            if r.get('estado') == 'aprobado-V4' and (not r.get('reserva_origen') or r['rtype'] == 'context')]
    kinds, _ = V.known_ids()
    kind = dict(kinds)
    for r in recs:
        kind[r['id']] = r['rtype']
    by = {r['id']: r for r in recs}
    wy = collections.defaultdict(list)
    for r in recs:
        if r['rtype'] == 'work':
            for d in r.get('designers') or []:
                wy[d].append(r['year'])
    # año de cada registro
    def yr(r):
        t = r['rtype']
        if t == 'work': return r['year']
        if t == 'designer': return min(wy[r['id']]) if wy.get(r['id']) else (r.get('born') or 1900) + 30
        return r.get('start') or r.get('year') or 1900
    # pares de enlace de contexto, cada uno asignado a un solo registro
    pares = {}   # (ctx, item) -> registro responsable
    for r in recs:
        if r['rtype'] == 'context':
            continue
        for l in r.get('links') or []:
            if l.get('tipo') == 'directo' or (l.get('via') or '').startswith('ctx-'):
                c = l.get('ctx') or l.get('via')
                pares.setdefault((c, r['id']), (r['id'], l['mecanismo']))
    for r in recs:
        if r['rtype'] == 'context':
            for e in r.get('explica') or []:
                if (r['id'], e['id']) not in pares:
                    pares[(r['id'], e['id'])] = (r['id'], e['mecanismo'])
    # asignar a cada elemento los pares que debe escribir: el propio elemento si es el `item`; si no, el contexto (cuando el item ya existe)
    escribir = collections.defaultdict(list)
    for (c, i), (resp, mec) in pares.items():
        owner = resp
        escribir[owner].append({'ctx': c, 'item': i, 'mecanismo': mec})
    out_recs = []
    for r in recs:
        r = dict(r)
        r['escribir_links'] = escribir.get(r['id'], [])
        r['escribir_conexiones'] = []
        r['campos'] = collections.defaultdict(list)
        if r['rtype'] != 'context':
            for l in r.get('links') or []:
                if l.get('tipo') != 'secundario':
                    continue
                via = l['via']
                if via.startswith('ctx-'):
                    continue
                vk, ik = kind.get(via), r['rtype']
                if (ik, vk) in FIELD_OF:
                    r['campos'][FIELD_OF[(ik, vk)]].append(via)
                elif ik in ('movement', 'institution', 'theory', 'production') and vk in LINKS_OF:
                    r['campos']['links.' + LINKS_OF[vk]].append(via)
                elif vk in ('institution', 'movement', 'theory', 'production') and ik in LINKS_OF:
                    pass   # lo fija rel_etapa6.py en la vía
                elif ik == 'designer' and vk == 'work':
                    pass   # lo da work.designers de esa obra (rel_etapa6.py lo comprueba)
                else:
                    r['escribir_conexiones'].append({'from': r['id'], 'to': via, 'mecanismo': l['mecanismo']})
        r['campos'] = dict(r['campos'])
        out_recs.append(r)
    # lotes
    groups = collections.defaultdict(list)
    for r in out_recs:
        t = r['rtype']
        g = {'work': 'w', 'designer': 'd', 'context': 'c'}.get(t, 'm')   # m = movimientos, instituciones y teoría
        groups[(era_of(yr(r)), g)].append(r)
    index = []
    for (era, g), lst in sorted(groups.items()):
        lst.sort(key=lambda r: (r.get('discipline') or (r.get('disciplines') or [''])[0] or '', r['rtype'], yr(r)))
        size = 10 if g == 'w' else 12
        n = 0
        for i in range(0, len(lst), size):
            n += 1
            name = f'{era}_{g}{n}'
            json.dump(lst[i:i + size], open(os.path.join(out, name + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
            index.append(f'{name}\t{len(lst[i:i+size])}\t' + ','.join(sorted({r["rtype"] for r in lst[i:i+size]})))
    # D3: enlaces de contexto para obras ★ existentes (tipo «enlace» o «contexto nuevo»), agrupados por tramo de la obra
    A = json.load(open(os.path.join(BASE, 'tools', 'REVISION-ETAPA7-AJUSTES.json'), encoding='utf-8'))
    yr_exist = {}
    for f in glob.glob(os.path.join(BASE, 'src-data', '*', '2*-works-*.json')):
        for w in json.load(open(f, encoding='utf-8')).get('works', []):
            yr_exist[w['id']] = w['year']
    estrella = collections.defaultdict(list)
    for e in A['enlaces_estrella']['lista']:
        for p in e.get('propuesta', []):
            if e['id'] in yr_exist:
                estrella[era_of(yr_exist[e['id']])].append({'ctx': p['ctx'], 'item': e['id'], 'mecanismo': p['mecanismo'], 'tipo': e['tipo'], 'nota': e.get('nota', '')})
    for era, lst in sorted(estrella.items()):
        for i in range(0, len(lst), 12):
            name = f'{era}_e{i // 12 + 1}'
            json.dump({'escribir_links': lst[i:i + 12]}, open(os.path.join(out, name + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
            index.append(f'{name}\t{len(lst[i:i+12])}\tlink (D3)')
    # textos de elementos existentes que cambian (renombres, correcciones): salida en formato de apply2.py
    TEXTOS = [
        ('bodoni-manuale-1788', 'La obra pasa a ser la edición de 1818 (2 vols., publicada por la viuda; `posthumous: true`). Reescribir key, more y status para esa edición; mencionar que la primera muestra es de 1788.'),
        ('brutalism-metabolism', 'Pasa a llamarse Brutalismo (el metabolismo es un movimiento aparte). Reescribir key, traits, context y shift solo para el brutalismo (Le Corbusier, los Smithson, Banham, Brasil).'),
        ('futurism-typography', 'Pasa a llamarse Futurismo (desde 1909): ampliar key, traits, context y shift a arquitectura (Sant’Elia), moda (TuTa), objeto (Depero) y manifiesto. CONSERVAR las frases que ya tienen marcas [n] y sus refs.'),
        ('punk-fashion', 'Pasa a llamarse Punk (moda y gráfica): ampliar key y traits con la gráfica (Jamie Reid, fanzines, fotocopia).'),
        ('ctx-gothic-revival', 'Pasa a llamarse «Medievalismo romántico y renovación religiosa»: ajustar key, happened y effect para que el contexto no se confunda con el nuevo movimiento gothic-revival.'),
        ('jatiya-sangsad-dhaka-1982', 'Ahora tiene designers [louis-kahn], year 1962 y date «1962–1982»: revisar que key y more sean coherentes (proyecto de 1962, terminado en 1982).'),
        ('werkbund-cologne-1914', 'Ahora year 1914: revisar que el texto no diga 1913.'),
        ('international-style', 'start 1925: revisar key y context (el nombre es de 1932, pero el movimiento abarca desde mediados de los años veinte).'),
        ('postmodern-architecture', 'start 1964: incluir la Casa Vanna Venturi como obra fundadora en key o context si corresponde.'),
        ('landscape-urbanism', 'start 1982: mencionar el concurso del Parc de la Villette como origen.'),
        ('critical-speculative-design', 'Sin cambios de texto; solo verificar que la ficha no prometa obras que la línea no tiene.'),
    ]
    json.dump([{'id': i, 'instruccion': t} for i, t in TEXTOS], open(os.path.join(out, 'textos_1.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    index.append(f'textos_1\t{len(TEXTOS)}\treescritura (apply2.py)')
    open(os.path.join(out, 'INDICE.txt'), 'w').write('\n'.join(index) + '\n')
    print(len(index), 'lotes;', sum(len(v) for v in escribir.values()), 'enlaces; ',
          sum(len(r['escribir_conexiones']) for r in out_recs), 'conexiones')


main()
