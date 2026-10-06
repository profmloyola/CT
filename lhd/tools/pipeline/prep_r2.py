#!/usr/bin/env python3
"""R2: arma los lotes de fuentes.

Uso:
  python3 tools/pipeline/prep_r2.py TIPO TANDA [--n 8] [--lotes 3] [--dry]
  python3 tools/pipeline/prep_r2.py --plantillas        # imprime las plantillas de prompt en Markdown
  python3 tools/pipeline/prep_r2.py --doc               # las escribe en CONTINUAR-R2.md (entre sus marcas)
TIPO: obras | diseñadores | movimientos | instituciones | teorias | contextos | productivos | ensayos | enlaces | conexiones

Toma de data/all.json (y de src-essays/essays.json para los ensayos) los registros SIN fuentes dentro del alcance de la R2:
fichas ★ (obras, diseñadores, movimientos, instituciones, teorías), todos los hechos de contexto y productivos, los ensayos,
y los enlaces de contexto y las conexiones que tocan una ficha ★. Salta los que ya están en lotes anteriores (r2_work/in_*.json)
y escribe in_TANDA_k.json (el registro completo, más contexto de ayuda para el agente) y prompt_TANDA_k.txt (el prompt del tipo).
--n: registros por agente (8; enlaces y conexiones 15; ensayos 2). --lotes: agentes en paralelo (3). --dry: solo cuenta y lista.
"""
import datetime
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r2lib import (DEFAULT_N, ESS_LINK, KEY, KINDS, WORK, brief, conn_key, link_key, load_all, load_essays, record_key,
                   registry, sort_key, star_ids)

DOC_INI, DOC_FIN = '<!-- PLANTILLAS:INICIO (generado por prep_r2.py --doc; no editar a mano) -->', '<!-- PLANTILLAS:FIN -->'
PLANT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plantillas_r2.json')


def plantillas():
    return json.load(open(PLANT, encoding='utf-8'))


def fill(s, sub):
    """Reemplaza {tanda}, {k}... sin usar str.format (los textos llevan llaves JSON)."""
    for kk, v in sub.items():
        s = s.replace('{' + kk + '}', str(v))
    return s


def prompt(tipo, tanda, k, n, fecha=None):
    P = plantillas()
    c, t = P['comun'], P['tipos'][tipo]
    sub = dict(tanda=tanda, k=k, n=n, unidad=t['unidad'], fecha=fecha or datetime.date.today().isoformat(), tarea=t['tarea'])
    out = [fill(c['apertura'], sub), '', 'Formato de salida: ' + t['salida'], '', 'Reglas:']
    out += [f'{i}. ' + fill(r, sub) for i, r in enumerate(c['reglas'], 1)]
    return '\n'.join(out) + '\n'


def plantillas_md():
    L = []
    for tipo in KINDS:
        L += [f'### Plantilla: `{tipo}`', '', '```', prompt(tipo, '<tanda>', '<k>', '<n>', '<AAAA-MM-DD>').rstrip(), '```', '']
    return '\n'.join(L)


def pending(tipo, d):
    """Registros del alcance que aún no tienen fuentes, en el orden de la línea de tiempo: [(clave, registro_para_el_agente)]."""
    reg = registry(d)
    if tipo in KEY:
        rows = [x for x in d[KEY[tipo]] if not x.get('refs') and (tipo in ('contextos', 'productivos') or x.get('star'))]
        rows.sort(key=lambda x: sort_key(d, x))
        return [(x['id'], {kk: v for kk, v in x.items() if kk not in ('images', 'star')}) for x in rows]
    if tipo == 'ensayos':
        out = []
        for e in load_essays():
            if e.get('refs'):
                continue
            ids = []
            for p in e['paras']:
                for m in ESS_LINK.finditer(p):
                    if m.group(1) not in ids:
                        ids.append(m.group(1))
            r = {kk: v for kk, v in e.items() if kk != 'images'}
            r['elementos_citados'] = {i: brief(reg, i) for i in ids}
            out.append((e['id'], r))
        return out
    star = star_ids(d)
    if tipo == 'enlaces':
        rows = [l for l in d['ctxLinks'] if l['item'] in star and not l.get('refs')]
        rows.sort(key=lambda l: sort_key(d, reg[l['item']][1]) + (l['ctx'],))
        return [(link_key(l), {'ctx': l['ctx'], 'item': l['item'], 'note': l['note'], 'es': l['es'], 'track': l.get('track'),
                               'ctx_info': brief(reg, l['ctx']), 'item_info': brief(reg, l['item'])}) for l in rows]
    if tipo == 'conexiones':
        rows = [c for c in d['connections'] if (c['from'] in star or c['to'] in star) and not c.get('refs')]
        rows.sort(key=lambda c: sort_key(d, reg[c['from'] if c['from'] in star else c['to']][1]) + (c['from'], c['to']))
        return [(conn_key(c), {'from': c['from'], 'to': c['to'], 'note': c['note'], 'es': c['es'],
                               'from_info': brief(reg, c['from']), 'to_info': brief(reg, c['to'])}) for c in rows]
    raise SystemExit('tipo desconocido: ' + tipo)


def assigned():
    done = set()
    for f in glob.glob(WORK + '/in_*.json'):
        done |= {record_key(x) for x in json.load(open(f, encoding='utf-8'))}
    return done


def main(argv):
    if '--plantillas' in argv:
        print(plantillas_md())
        return 0
    if '--doc' in argv:                       # reescribe la sección de plantillas de CONTINUAR-R2.md (entre las marcas)
        p = os.path.join(os.path.dirname(WORK), '..', '..', 'CONTINUAR-R2.md')
        p = os.path.normpath(p)
        t = open(p, encoding='utf-8').read()
        i, j = t.index(DOC_INI) + len(DOC_INI), t.index(DOC_FIN)
        open(p, 'w', encoding='utf-8').write(t[:i] + '\n\n' + plantillas_md().rstrip() + '\n\n' + t[j:])
        print('Plantillas escritas en CONTINUAR-R2.md')
        return 0
    if len(argv) < 2 or argv[0] not in KINDS:
        print(__doc__)
        return 2
    tipo, tanda = argv[0], argv[1]
    n = int(argv[argv.index('--n') + 1]) if '--n' in argv else DEFAULT_N.get(tipo, 8)
    lotes = int(argv[argv.index('--lotes') + 1]) if '--lotes' in argv else 3
    done = assigned()
    todo = [(k, r) for k, r in pending(tipo, load_all()) if k not in done]
    print(f'{tipo}: {len(todo)} sin fuentes pendientes de asignar')
    for k in range(lotes):
        chunk = todo[k * n:(k + 1) * n]
        if not chunk:
            break
        if '--dry' not in argv:
            json.dump([c[1] for c in chunk], open(f'{WORK}/in_{tanda}_{k + 1}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
            open(f'{WORK}/prompt_{tanda}_{k + 1}.txt', 'w', encoding='utf-8').write(prompt(tipo, tanda, k + 1, len(chunk)))
        print(f'in_{tanda}_{k + 1}.json ({len(chunk)}):', ', '.join(c[0] for c in chunk))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
