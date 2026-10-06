#!/usr/bin/env python3
"""Verificación estructural de tools/LISTAS-CIERRE.md (plan, paso 1.5).

Uso: python3 tools/pipeline/listas_check.py [archivo.md ...] [--tramo postwar] [--root DIR]
Lee las secciones «## Tramo: <tramo>» con subsecciones «### Contextos|Productivo|Teoría|Movimientos|Instituciones|Diseñadores|Obras|Conexiones|Reserva».
Primera columna = `id` entre acentos graves. Columnas (por nombre de encabezado, sin importar el orden):
  Contextos: id | nombre | sub | años | regiones | nivel | relaciona
  Productivo: id | nombre | sub | años | nivel | relaciona        Teoría/Movimientos/Instituciones: id | nombre | años | nivel | relaciona
  Diseñadores: id | nombre | años | disciplinas | nivel | obras | relaciona
  Obras: id | título | disciplina | año | nivel | diseñadores | tech | regiones | contextos   («contextos» = `ctx-id`: mecanismo; `ctx-id2`: mecanismo)
  Conexiones: from | to | línea           Reserva: id | tipo | nombre | motivo
Los elementos que ya existen en src-data/<tramo>/ se listan también (cuentan para las cantidades).
Sale con código 1 si hay ERROR; los AVISO no fallan.
"""
import glob, json, os, re, sys
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TRAMOS = ['industrial', 'reform', 'modernism', 'postwar', 'postmodern']
SECC = {'contextos': 'contexts', 'productivo': 'production', 'teoría': 'theories', 'teoria': 'theories', 'movimientos': 'movements',
        'instituciones': 'institutions', 'diseñadores': 'designers', 'disenadores': 'designers', 'obras': 'works',
        'conexiones': 'connections', 'reserva': 'reserve'}
# tamaños objetivo (plan, sección 3): ctx, prod, teoría, mov, inst, dis, obras, ★obras
TARGET = {'industrial': (25, 10, 5, 5, 6, 14, 30, 9), 'reform': (30, 12, 6, 6, 10, 28, 60, 18),
          'modernism': (39, 16, 14, 11, 17, 64, 120, 37), 'postwar': (36, 16, 11, 10, 14, 43, 90, 27),
          'postmodern': (32, 15, 9, 8, 12, 36, 75, 22)}
KEYS = ['contexts', 'production', 'theories', 'movements', 'institutions', 'designers', 'works']
ID = r'[a-z0-9]+(?:-[a-z0-9]+)*'
DISC = {'graphic', 'product', 'fashion', 'architecture'}
SUBC = {'political', 'economic', 'social', 'cultural', 'technological'}
REG = {'europe', 'north-america', 'latin-america', 'global'}


CTXSUB = {}


MOVIDOS_ETAPA7 = {'th-werkbund-debate', 'werkbund-cologne-1914'}  # pasan a la carpeta modernism en 7.4 (v47): la lista de reform queda como histórica

def ids_src(root):
    out = {}
    for f in glob.glob(os.path.join(root, '*', '*.json')):
        t = os.path.basename(os.path.dirname(f))
        d = json.load(open(f, encoding='utf-8'))
        for k in ('movements', 'institutions', 'designers', 'works', 'contexts', 'production', 'theories', 'concepts'):
            for x in d.get(k, []) or []:
                if isinstance(x, dict) and 'id' in x:
                    out[x['id']] = (k, t)
                    if k == 'contexts': CTXSUB[x['id']] = x.get('track')
    return out


def parse(files):
    """-> {tramo: {sec: [fila dict]}} con '_line' y '_file'."""
    data = {}
    for fn in files:
        tramo = sec = None; hdr = None
        for n, line in enumerate(open(fn, encoding='utf-8'), 1):
            s = line.strip()
            m = re.match(r'##\s+Tramo:\s*(\w+)', s)
            if m:
                tramo = m.group(1); sec = hdr = None; data.setdefault(tramo, {}); continue
            m = re.match(r'###\s+(\S+)', s)
            if m:
                sec = SECC.get(m.group(1).lower()); hdr = None
                if tramo and sec: data[tramo].setdefault(sec, [])
                continue
            if not s.startswith('|') or not tramo or not sec:
                if not s.startswith('|'): hdr = None
                continue
            cells = [c.strip() for c in s.strip('|').split('|')]
            if all(re.fullmatch(r':?-{2,}:?', c) for c in cells if c): continue
            if hdr is None:
                hdr = [c.lower().strip('` ') for c in cells]; continue
            row = {hdr[i]: cells[i] for i in range(min(len(hdr), len(cells)))}
            row['_line'] = n; row['_file'] = os.path.basename(fn); row['_cells'] = cells
            data[tramo][sec].append(row)
    return data


def idof(cell):
    m = re.match(r'`(' + ID + r')`', cell or '')
    return m.group(1) if m else None


def refs(cell):
    return re.findall(r'`(' + ID + r')`', cell or '')


def col(row, *names):
    for k in row:
        for nm in names:
            if k.startswith(nm): return row[k]
    return ''


def main(argv):
    root = os.path.join(BASE, 'src-data'); files = []; only = None
    it = iter(argv)
    for a in it:
        if a == '--root': root = next(it)
        elif a == '--tramo': only = next(it)
        else: files.append(a)
    if not files: files = [os.path.join(BASE, 'tools', 'LISTAS-CIERRE.md')]
    data = parse(files)
    src = ids_src(root)
    res = os.path.join(BASE, 'tools', 'RESERVA-FASE-B.json')
    reserve_ctx = {x['id'] for x in json.load(open(res, encoding='utf-8')).get('contexts', [])} if os.path.exists(res) else set()
    err, warn = [], []
    E = lambda r, m: err.append(f"{r['_file']}:{r['_line']}: {m}")
    W = lambda r, m: warn.append(f"{r['_file']}:{r['_line']}: {m}")
    kind_of, tramo_of, row_of = {}, {}, {}
    for t, secs in data.items():
        for sec in KEYS + ['reserve']:
            for r in secs.get(sec, []):
                i = idof(r['_cells'][0])
                if not i:
                    E(r, f'primera columna sin `id` ({r["_cells"][0][:30]})'); continue
                if sec == 'reserve':
                    kind_of.setdefault('res:' + i, 'reserve'); continue
                if i in kind_of:
                    E(r, f'id repetido: {i}'); continue
                kind_of[i] = sec; tramo_of[i] = t; row_of[i] = r
                if i in src:
                    k, st = src[i]
                    if st != t and not (t == 'modernism' and i in reserve_ctx) and i not in MOVIDOS_ETAPA7:
                        E(r, f'{i} ya existe en src-data/{st} (esta lista lo pone en {t})')
                    if k != sec and not (k == 'concepts'):
                        E(r, f'{i} existe en src-data como {k}, aquí está como {sec}')
    # ids de contexto de la reserva permitidos como referencia
    def known(i):
        return i in kind_of or i in src or i in reserve_ctx
    def kind(i):
        if i in kind_of: return kind_of[i]
        if i in src: return src[i][0]
        return 'contexts' if i in reserve_ctx else None
    # enlaces existentes en src-data (ctx -> item)
    deg = {}
    for f in glob.glob(os.path.join(root, '*', '80-context-links.json')):
        for l in json.load(open(f, encoding='utf-8')).get('links', []):
            deg[l['ctx']] = deg.get(l['ctx'], 0) + 1; deg[l['item']] = deg.get(l['item'], 0) + 1
    ctx_dir = {}   # ctx -> {obra: sub}
    work_ctx = {}
    for t, secs in data.items():
        if only and t != only: continue
        # --- filas
        for sec in KEYS:
            for r in secs.get(sec, []):
                i = idof(r['_cells'][0])
                if not i: continue
                nivel = col(r, 'nivel')
                if nivel not in ('★', 'N', '*'): E(r, f'{i}: nivel debe ser ★ o N (hay «{nivel}»)')
                for x in refs(col(r, 'relaciona')):
                    if not known(x): E(r, f'{i}: relaciona con {x}, que no existe')
                    elif x == i: E(r, f'{i}: se relaciona consigo mismo')
                    else:
                        deg[i] = deg.get(i, 0) + 1; deg[x] = deg.get(x, 0) + 1
                if sec == 'contexts':
                    if col(r, 'sub') not in SUBC: E(r, f'{i}: sub inválida «{col(r, "sub")}»')
                    for g in re.split(r'[,; ]+', col(r, 'regiones')):
                        if g and g not in REG: E(r, f'{i}: región inválida «{g}»')
                    if not col(r, 'regiones'): E(r, f'{i}: faltan regiones')
                if sec == 'production' and col(r, 'sub') not in ('materials', 'processes', 'tools'): E(r, f'{i}: sub de productivo inválida')
                if sec == 'designers':
                    for x in refs(col(r, 'obras')):
                        if not known(x): E(r, f'{i}: obra {x} no existe')
                        else: deg[i] = deg.get(i, 0) + 1
                if sec == 'works':
                    if col(r, 'disciplina') not in DISC: E(r, f'{i}: disciplina inválida «{col(r, "disciplina")}»')
                    for g in re.split(r'[,; ]+', col(r, 'regiones')):
                        if g and g not in REG: E(r, f'{i}: región inválida «{g}»')
                    for x in refs(col(r, 'diseñadores', 'disenadores')) + refs(col(r, 'tech')):
                        if not known(x): E(r, f'{i}: {x} no existe')
                        else: deg[x] = deg.get(x, 0) + 1
                    cs = col(r, 'contextos')
                    parts = [p.strip() for p in re.split(r';\s*(?=`)', cs) if p.strip()]
                    work_ctx[i] = []
                    for p in parts:
                        m = re.match(r'`(' + ID + r')`\s*:\s*(.+)$', p)
                        if not m: E(r, f'{i}: contexto sin mecanismo «{p[:40]}»'); continue
                        c, mech = m.group(1), m.group(2)
                        if not known(c) or kind(c) != 'contexts': E(r, f'{i}: {c} no es un contexto existente'); continue
                        if len(mech) < 12: E(r, f'{i}: mecanismo demasiado corto para {c}')
                        if len(mech) > 200: W(r, f'{i}: mecanismo largo en {c} ({len(mech)})')
                        work_ctx[i].append(c); deg[c] = deg.get(c, 0) + 1; deg[i] = deg.get(i, 0) + 1
                        ctx_dir.setdefault(c, set()).add(i)
                    if not work_ctx[i]: E(r, f'{i}: obra sin contexto (C4/C4b)')
                    elif nivel == '★':
                        subs = set()
                        for c in work_ctx[i]:
                            rr = row_of.get(c)
                            subs.add(col(rr, 'sub') if rr else CTXSUB.get(c) or ('?' + c))
                        if len(work_ctx[i]) < 2 or len(subs) < 2: E(r, f'{i}: ★ necesita ≥2 contextos de subcategorías distintas')
        # --- conexiones
        nconn = 0
        for r in secs.get('connections', []):
            a, b = idof(r['_cells'][0]), idof(r['_cells'][1]) if len(r['_cells']) > 1 else None
            if not a or not b: E(r, 'conexión sin from/to'); continue
            for x in (a, b):
                if not known(x): E(r, f'conexión: {x} no existe')
            if len(col(r, 'línea', 'linea')) < 12: E(r, f'conexión {a}->{b} sin línea')
            nconn += 1
            deg[a] = deg.get(a, 0) + 1; deg[b] = deg.get(b, 0) + 1
        if secs.get('connections') is not None and nconn < 8:
            err.append(f'{t}: solo {nconn} conexiones (mínimo 8)')
    # --- cantidades, ★, grado
    summary = []
    for t, secs in data.items():
        if only and t != only: continue
        cnt = [len(secs.get(k, [])) for k in KEYS]
        tg = TARGET[t]
        works = secs.get('works', [])
        stars = sum(1 for r in works if col(r, 'nivel') in ('★', '*'))
        for n, (k, c, g) in enumerate(zip(KEYS, cnt, tg)):
            tol = 3 if k == 'works' else 2
            if abs(c - g) > tol: err.append(f'{t}: {k} = {c}, objetivo {g} (±{tol})')
        if works:
            p = stars / len(works)
            if not 0.25 <= p <= 0.35: err.append(f'{t}: ★ de obras = {stars}/{len(works)} = {p:.0%} (debe estar entre 25 % y 35 %)')
        # grado mínimo
        for sec in KEYS:
            for r in secs.get(sec, []):
                i = idof(r['_cells'][0])
                if not i: continue
                need = 2 if sec == 'contexts' else 1
                if sec == 'works': continue
                if deg.get(i, 0) < need: E(r, f'{i}: {deg.get(i, 0)} enlaces (mínimo {need})')
        # disciplinas y regiones
        disc = {}
        la = 0
        for r in works:
            d = col(r, 'disciplina'); disc[d] = disc.get(d, 0) + 1
            if 'latin-america' in col(r, 'regiones'): la += 1
        summary.append(f"{t}: " + ' '.join(f'{k}={c}/{g}' for k, c, g in zip(KEYS, cnt, tg)) + f" | ★obras {stars} | disc {disc} | LatAm obras {la} ({(la / len(works) if works else 0):.0%}) | conexiones {len(secs.get('connections', []))} | reserva {len(secs.get('reserve', []))}")
    # --- chequeos de enlaces de contexto: ≥2
    print('\n'.join(summary))
    for w in warn: print('AVISO', w)
    for e in err: print('ERROR', e)
    print(f'{len(err)} error(es), {len(warn)} aviso(s)')
    return 1 if err else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
