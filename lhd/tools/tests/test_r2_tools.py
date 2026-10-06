"""R2.0 (plan v1.0): prep_r2.py, check_r2.py y apply2.py para todos los tipos (teorías, contextos, productivos, ensayos, enlaces, conexiones).
Sin navegador. Trabaja siempre sobre una COPIA del proyecto (nada del original cambia). Las fuentes de las salidas de prueba son example.org:
son datos de prueba de una copia desechable, no contenido del proyecto."""
import copy, hashlib, json, os, shutil, subprocess, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ok_all = True
def check(cond, msg, extra=''):
    global ok_all
    ok_all = ok_all and bool(cond)
    print(('PASS ' if cond else 'FAIL ') + msg, extra if not cond else '')

tmp = tempfile.mkdtemp(prefix='lhd-r2-')
C = os.path.join(tmp, 'lhd')
shutil.copytree(ROOT, C, ignore=shutil.ignore_patterns('__pycache__', '.git', 'e8_img', 'e7_work', 'e8_work'))
W = os.path.join(C, 'tools', 'pipeline', 'r2_work')
def run(*a):
    return subprocess.run([sys.executable] + list(a), cwd=C, capture_output=True, text=True)
def tree_hash():
    h = hashlib.sha1()
    for base in ('src-data', 'src-essays'):
        for dp, dn, fn in sorted(os.walk(os.path.join(C, base))):
            for f in sorted(fn):
                h.update(open(os.path.join(dp, f), 'rb').read())
    return h.hexdigest()
def jl(p): return json.load(open(p, encoding='utf-8'))
def dump(o, name):
    p = os.path.join(W, name)
    json.dump(o, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return p
def chk(*files, extra=()):
    r = run('tools/pipeline/check_r2.py', *extra, *files)
    return r.returncode, r.stdout
def expect_error(o, name, needle, extra=()):
    code, out = chk(dump(o, name), extra=extra)
    check(code == 1 and needle in out, f'check_r2 rechaza: {needle}', out.strip()[-300:])

try:
    b = run('tools/build_data.py')
    check('OK: no PROBLEM' in b.stdout, 'build de la copia sin PROBLEM')
    REF = {'label': 'Fuente de prueba', 'url': 'https://example.org/prueba', 'checks': 'Qué sostiene.', 'date': '2026-10-06'}

    # ---------- prep_r2.py: todos los tipos ----------
    TIPOS = {'movimientos': 2, 'instituciones': 2, 'teorias': 2, 'contextos': 2, 'productivos': 2, 'ensayos': 2, 'enlaces': 2, 'conexiones': 2}
    prep = {}
    for t, n in TIPOS.items():
        r = run('tools/pipeline/prep_r2.py', t, 'tA', '--n', str(n), '--lotes', '1')
        p = os.path.join(W, 'in_tA_1.json')
        ok = r.returncode == 0 and os.path.exists(p) and len(jl(p)) == n
        check(ok, f'prep_r2 {t}: arma un lote de {n}', r.stdout + r.stderr)
        if not ok: continue
        prep[t] = jl(p)
        pr = open(os.path.join(W, 'prompt_tA_1.txt'), encoding='utf-8').read()
        check('in_tA_1.json' in pr and 'out_tA_1.json' in pr and '{' + 'tanda}' not in pr and '{k}' not in pr, f'prompt de {t} sin marcas sin rellenar')
        r2 = run('tools/pipeline/prep_r2.py', t, 'tB', '--n', str(n), '--lotes', '1')
        p2 = os.path.join(W, 'in_tB_1.json')
        a, bb = {json.dumps(x, sort_keys=True) for x in prep[t]}, {json.dumps(x, sort_keys=True) for x in jl(p2)}
        check(not (a & bb), f'prep_r2 {t}: la tanda siguiente no repite lo asignado')
        os.remove(p); os.remove(p2)
        for f in ('prompt_tA_1.txt', 'prompt_tB_1.txt'):
            os.remove(os.path.join(W, f))
    for t in ('obras', 'diseñadores'):
        r = run('tools/pipeline/prep_r2.py', t, 'tZ')
        check('0 sin fuentes pendientes' in r.stdout and not os.path.exists(os.path.join(W, 'in_tZ_1.json')), f'prep_r2 {t}: nada pendiente (todas con fuentes)', r.stdout)
    check(run('tools/pipeline/prep_r2.py', 'rarezas', 'tZ').returncode != 0, 'prep_r2 rechaza un tipo desconocido')
    check(all(k in run('tools/pipeline/prep_r2.py', '--plantillas').stdout for k in ('`teorias`', '`ensayos`', '`enlaces`', '`conexiones`')), 'prep_r2 --plantillas lista todos los tipos')
    # CONTINUAR-R2.md lleva las plantillas tal como las genera prep_r2.py --doc (fuente única: plantillas_r2.json)
    doc = open(os.path.join(ROOT, 'CONTINUAR-R2.md'), encoding='utf-8').read()
    plant = run('tools/pipeline/prep_r2.py', '--plantillas').stdout.strip()
    check(plant in doc and all(f'### Plantilla: `{t}`' in doc for t in ('obras', 'diseñadores', 'movimientos', 'instituciones', 'teorias', 'contextos', 'productivos', 'ensayos', 'enlaces', 'conexiones')), 'CONTINUAR-R2.md trae las plantillas de los 10 tipos, iguales a las de prep_r2.py (regenerar con --doc)')
    # contexto de ayuda para el agente
    e = prep.get('enlaces', [{}])[0]
    check({'ctx_info', 'item_info', 'note', 'es'} <= set(e), 'enlaces: el lote lleva el contexto de ambos extremos')
    check({'elementos_citados'} <= set(prep.get('ensayos', [{}])[0]), 'ensayos: el lote lleva los elementos citados')

    # ---------- salidas buenas de cada tipo ----------
    FIELDS = {'movimientos': ('key', 'traits', 'context', 'shift'), 'instituciones': ('key', 'more'), 'teorias': ('key', 'ideas', 'impact'),
              'contextos': ('key', 'happened', 'effect'), 'productivos': ('key', 'origin', 'enabled', 'change', 'economy', 'relations')}
    def mk(v, lang_marks='[1]'):
        return [s.rstrip() + lang_marks for s in v] if isinstance(v, list) else v.rstrip() + lang_marks
    def good(t, rec):
        if t in FIELDS:
            f = [x for x in FIELDS[t] if x in rec]
            return {'id': rec['id'], 'en': {x: mk(rec[x]) for x in f}, 'es': {x: mk(rec['es'][x]) for x in f}, 'refs': [REF], 'other': {}, 'issues': ['Nota de prueba (incidencia).']}
        if t == 'ensayos':
            return {'id': rec['id'], 'en': {'paras': mk(rec['paras'])}, 'es': {'paras': mk(rec['es']['paras'])}, 'refs': [REF], 'issues': []}
        if t == 'enlaces':
            return {'ctx': rec['ctx'], 'item': rec['item'], 'en': {'note': mk(rec['note'])}, 'es': {'note': mk(rec['es']['note'])}, 'refs': [REF], 'issues': []}
        return {'from': rec['from'], 'to': rec['to'], 'en': {'note': mk(rec['note'])}, 'es': {'note': mk(rec['es']['note'])}, 'refs': [REF], 'issues': []}
    outs = {}
    for t in prep:
        outs[t] = dump([good(t, r) for r in prep[t]], f'out_tA_{t}.json')
        code, out = chk(outs[t])
        check(code == 0 and '0 ERROR' in out, f'check_r2 acepta una salida buena de {t}', out)
    old = os.path.join(W, 'out_t01_1.json')
    code, out = chk(old, extra=('--con-fuentes',))
    check(code == 0, 'check_r2 --con-fuentes acepta una salida real anterior (obras)', out[-200:])
    code, out = chk(old)
    check(code == 1 and 'ya tiene fuentes' in out, 'sin --con-fuentes rechaza lo que ya tiene fuentes')

    # ---------- salidas malas ----------
    el = good('contextos', prep['contextos'][0])
    m = copy.deepcopy(el); m['en']['key'] += '[2]'; m['es']['key'] += '[2]'
    expect_error([m], 'bad1.json', 'sin fuente')
    m = copy.deepcopy(el); m['es']['key'] = m['es']['key'].replace('[1]', '')
    expect_error([m], 'bad2.json', 'marcas distintas')
    m = copy.deepcopy(el); m['refs'][0]['url'] = 'https://es.wikipedia.org/wiki/Algo'
    expect_error([m], 'bad3.json', 'fuente no válida')
    m = copy.deepcopy(el); m['refs'][0]['url'] = 'https://example.org:443/x'
    expect_error([m], 'bad4.json', 'puerto')
    m = copy.deepcopy(el); m['refs'][0]['date'] = '6-10-2026'
    expect_error([m], 'bad5.json', 'AAAA-MM-DD')
    m = copy.deepcopy(el); m['refs'] = []
    expect_error([m], 'bad6.json', 'sin refs')
    m = copy.deepcopy(el); m['id'] = 'no-existe'
    expect_error([m], 'bad7.json', 'id inexistente')
    m = copy.deepcopy(el); m['en']['shift'] = 'x[1]'; m['es']['shift'] = 'x[1]'
    expect_error([m], 'bad8.json', 'no permitido')
    m = copy.deepcopy(el); del m['en']['effect']; del m['es']['effect']
    expect_error([m], 'bad9.json', 'falta el campo')
    th = good('teorias', prep['teorias'][0]); th['es']['ideas'] = th['es']['ideas'][:-1]
    expect_error([th], 'bad10.json', 'EN tiene')
    expect_error([el, copy.deepcopy(el)], 'bad11.json', 'registro repetido')
    # enlaces y conexiones
    ln = good('enlaces', prep['enlaces'][0]); ln['en']['key'] = 'x[1]'; ln['es']['key'] = 'x[1]'
    expect_error([ln], 'bad12.json', 'solo «note»')
    ln = good('enlaces', prep['enlaces'][0]); ln['item'] = 'no-existe'
    expect_error([ln], 'bad13.json', 'enlace inexistente')
    cn = good('conexiones', prep['conexiones'][0]); cn['to'] = 'no-existe'
    expect_error([cn], 'bad14.json', 'conexión inexistente')
    dr = {'ctx': prep['enlaces'][1]['ctx'], 'item': prep['enlaces'][1]['item'], 'drop': True}
    expect_error([dr], 'bad15.json', 'sin issues')
    dr['issues'] = ['Ninguna fuente sostiene el mecanismo (se consultaron X e Y).']
    code, out = chk(dump([dr], 'drop_ok.json'))
    check(code == 0, 'check_r2 acepta una propuesta de quitar con sus issues', out)
    dre = {'id': prep['contextos'][0]['id'], 'drop': True, 'issues': ['x']}
    expect_error([dre], 'bad16.json', 'solo se admite en enlaces y conexiones')
    # ensayos
    es0 = good('ensayos', prep['ensayos'][0])
    m = copy.deepcopy(es0); m['en']['paras'][0] += ' [[no-existe-id|texto]][1]'; m['es']['paras'][0] += ' [[no-existe-id|texto]][1]'
    expect_error([m], 'bad17.json', 'id inexistente')
    m = copy.deepcopy(es0); m['en']['paras'][0] += ' [[ctx-enlightenment|texto'
    expect_error([m], 'bad18.json', 'mal formados')
    m = copy.deepcopy(es0); m['en']['paras'][0] += ' [[ctx-enlightenment|texto[1]]]'; m['es']['paras'][0] += ' [[ctx-enlightenment|texto[1]]]'
    expect_error([m], 'bad19.json', 'dentro del texto del enlace')
    m = copy.deepcopy(es0); m['en']['paras'][0] += ' [[ctx-enlightenment|texto]][1]'
    expect_error([m], 'bad20.json', 'enlaces [[id]] distintos')
    m = copy.deepcopy(es0); m['es']['paras'] = m['es']['paras'][:-1]
    expect_error([m], 'bad21.json', 'párrafos')
    m = copy.deepcopy(es0); m['en']['paras'][1] = m['en']['paras'][1].replace('[1]', '[1][2]'); m['es']['paras'][1] = m['es']['paras'][1].replace('[1]', '[1][2]')
    expect_error([m], 'bad22.json', 'sin fuente')
    m = copy.deepcopy(es0); m['en']['title'] = 'Otro título'; m['es']['title'] = 'Otro título'
    expect_error([m], 'bad23.json', 'solo «paras»')
    for f in [f for f in os.listdir(W) if f.startswith(('bad', 'drop_ok'))]:
        os.remove(os.path.join(W, f))

    # ---------- apply2.py ----------
    sem = {t: json.load(open(outs[t], encoding='utf-8')) for t in outs}
    h0 = tree_hash()
    allouts = list(outs.values())
    r = run('tools/pipeline/apply2.py', '--dry', *allouts)
    check(r.returncode == 0 and tree_hash() == h0 and 'applied 16' in r.stdout, 'apply2 --dry no escribe nada', r.stdout + r.stderr)
    # una propuesta de quitar un enlace: no lo borra
    drop_link = {'ctx': prep['enlaces'][1]['ctx'], 'item': prep['enlaces'][1]['item'], 'drop': True, 'issues': ['Ninguna fuente sostiene el mecanismo.']}
    # (el segundo enlace del lote entra aquí solo como propuesta de quitar; no se aplica el texto)
    lk = jl(outs['enlaces']); lk = [x for x in lk if (x['ctx'], x['item']) != (drop_link['ctx'], drop_link['item'])]
    dump(lk, 'out_tA_enlaces.json'); outs['enlaces'] = os.path.join(W, 'out_tA_enlaces.json')
    dump([drop_link], 'out_tA_drop.json')
    r = run('tools/pipeline/apply2.py', *outs.values(), os.path.join(W, 'out_tA_drop.json'))
    check(r.returncode == 0, 'apply2 aplica todos los tipos', r.stdout + r.stderr)
    check('drop propuestos 1' in r.stdout, 'apply2 cuenta la propuesta de quitar sin aplicarla', r.stdout)
    b2 = run('tools/build_data.py')
    check('OK: no PROBLEM' in b2.stdout, 'build sin PROBLEM después de aplicar', b2.stdout[-300:])
    d = jl(os.path.join(C, 'data', 'all.json'))
    ess = jl(os.path.join(C, 'data', 'essays.json'))['essays']
    reg = {x['id']: x for k in ('movements', 'institutions', 'theories', 'contexts', 'production') for x in d[k]}
    for t in FIELDS:
        for rec in sem[t]:
            x = reg[rec['id']]
            check(x.get('refs') == [REF] and x['key'].endswith('[1]'), f'{t}: {rec["id"]} quedó con su fuente y su marca')
    for rec in sem['ensayos']:
        x = next(e for e in ess if e['id'] == rec['id'])
        check(x['refs'] == [REF] and all(p.endswith('[1]') for p in x['paras']) and all(p.endswith('[1]') for p in x['es']['paras']), f'ensayo {rec["id"]} con fuentes y marcas (EN y ES)')
        check(len(x['paras']) == len(rec['en']['paras']), f'ensayo {rec["id"]}: mismo número de párrafos')
    links = {(l['ctx'], l['item']): l for l in d['ctxLinks']}
    for rec in sem['enlaces']:
        l = links[(rec['ctx'], rec['item'])]
        if (rec['ctx'], rec['item']) == (drop_link['ctx'], drop_link['item']): continue
        check(l['refs'] == [REF] and l['note'].endswith('[1]'), f'enlace {rec["ctx"]}~{rec["item"]} aplicado')
    check((drop_link['ctx'], drop_link['item']) in links and not links[(drop_link['ctx'], drop_link['item'])].get('refs'), 'el enlace propuesto para quitar sigue en los datos, sin fuentes')
    conns = {(c['from'], c['to']): c for c in d['connections']}
    for rec in sem['conexiones']:
        c = conns[(rec['from'], rec['to'])]
        check(c['refs'] == [REF] and c['note'].endswith('[1]'), f'conexión {rec["from"]}>{rec["to"]} aplicada (fuera del Modernismo)')
    logs = [f for f in os.listdir(W) if f.startswith('log2_')]
    check(any('DROP-PROPUESTO' in open(os.path.join(W, f), encoding='utf-8').read() for f in logs), 'el log registra DROP-PROPUESTO')
    # después de aplicar, prep ya no vuelve a ofrecer lo aplicado
    for t, n in (('teorias', 2), ('contextos', 2), ('conexiones', 2)):
        before = int(run('tools/pipeline/prep_r2.py', t, 'tQ', '--dry').stdout.split(':')[1].split()[0])
        check(before > 0, f'prep_r2 {t}: sigue habiendo pendientes distintos de lo aplicado ({before})')
    check(int(run('tools/pipeline/prep_r2.py', 'ensayos', 'tQ', '--dry').stdout.split(':')[1].split()[0]) == 8, 'prep_r2 ensayos: quedan 8 de 10 tras aplicar 2')
    # el control del plan: pendientes bajan en auditoria --v1
    a = run('tools/pipeline/auditoria.py', '--v1', '-v', '--json', os.path.join(tmp, 'v1.json'))
    P = jl(os.path.join(tmp, 'v1.json'))
    check(len(P['essays']) == 8 and len(P['links']) == 358 and len(P['connections']) == 70 and len(P['contexts']) == 150 and len(P['theories']) == 26, 'auditoria --v1 refleja lo aplicado (8 ensayos, 358 enlaces, 70 conexiones, 150 contextos, 26 teorías)', {k: len(v) for k, v in P.items()})
    check(not P['orphan_marks'] and not P['uncited_refs'], 'sin marcas huérfanas ni fuentes sin citar tras aplicar')
finally:
    shutil.rmtree(tmp, ignore_errors=True)
print('RESULT: ' + ('PASS' if ok_all else 'FAIL'))
sys.exit(0 if ok_all else 1)
