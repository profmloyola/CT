"""R2.0 (plan v1.0): `auditoria.py --v1`, la definición de terminado de la R2. Sin navegador. Trabaja sobre una copia: llena a mano `data/all.json` y
`data/essays.json` de la copia con fuentes de prueba y comprueba que da 0 (código 0, «R2 TERMINADA») y que cada categoría detecta su caso."""
import copy, json, os, shutil, subprocess, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ok_all = True
def check(cond, msg, extra=''):
    global ok_all
    ok_all = ok_all and bool(cond)
    print(('PASS ' if cond else 'FAIL ') + msg, extra if not cond else '')
def jl(p): return json.load(open(p, encoding='utf-8'))

tmp = tempfile.mkdtemp(prefix='lhd-v1-')
C = os.path.join(tmp, 'lhd')
shutil.copytree(ROOT, C, ignore=shutil.ignore_patterns('__pycache__', '.git', 'e8_img', 'e7_work', 'e8_work'))
def run(*a):
    return subprocess.run([sys.executable] + list(a), cwd=C, capture_output=True, text=True)
REF = {'label': 'Prueba', 'url': 'https://example.org/p', 'checks': 'x', 'date': '2026-10-06'}
AP, EP, IP = (os.path.join(C, 'data', 'all.json'), os.path.join(C, 'data', 'essays.json'), os.path.join(C, 'tools', 'r2_incidencias.json'))
try:
    run('tools/build_data.py')
    r = run('tools/pipeline/auditoria.py', '--v1', '-v', '--json', os.path.join(tmp, 'a.json'))
    P = jl(os.path.join(tmp, 'a.json'))
    check(r.returncode == 1 and 'R2 NO terminada' in r.stdout, 'con pendientes, auditoria --v1 sale con código 1 y lo dice')
    check(list(P) == ['works', 'designers', 'movements', 'institutions', 'theories', 'contexts', 'production', 'essays', 'links', 'connections', 'orphan_marks', 'uncited_refs', 'open_incidents', 'single_source_works'], 'las 14 categorías de la definición de terminado', list(P))
    d = jl(AP)
    star = {x['id'] for k in ('works', 'designers', 'movements', 'institutions', 'theories') for x in d[k] if x.get('star')}
    check(len(P['links']) == sum(1 for l in d['ctxLinks'] if l['item'] in star and not l.get('refs')), 'enlaces pendientes = enlaces de fichas ★ sin fuentes')
    check(len(P['connections']) == sum(1 for c in d['connections'] if (c['from'] in star or c['to'] in star) and not c.get('refs')), 'conexiones pendientes = conexiones de fichas ★ sin fuentes')
    check(len(P['contexts']) == sum(1 for x in d['contexts'] if not x.get('refs')) and len(P['production']) == sum(1 for x in d['production'] if not x.get('refs')), 'contextos y productivos sin fuentes (todos, no solo ★)')
    check(P['single_source_works'] == [w['id'] for w in d['works'] if w.get('star') and len(w.get('refs') or []) == 1], 'obras ★ con una sola fuente')

    # ---- llenar la copia: todo con fuentes y marcas ----
    def tag(o, fields, n=1):
        for f in fields:
            if isinstance(o.get(f), list): o[f][0] = o[f][0] + f'[{n}]'
            elif f in o: o[f] = o[f] + f'[{n}]'
    def fill(x, fields, with_es=True):
        x['refs'] = [REF]
        tag(x, fields)
        if with_es and 'es' in x: tag(x['es'], fields)
    for k, fields in (('works', ('key',)), ('designers', ('key',)), ('movements', ('key',)), ('institutions', ('key',)), ('theories', ('key',)), ('contexts', ('key',)), ('production', ('key',))):
        for x in d[k]:
            if (x.get('star') or k in ('contexts', 'production')) and not x.get('refs'): fill(x, fields)
    for l in d['ctxLinks']:
        if l['item'] in star and not l.get('refs'): fill(l, ('note',))
    for c in d['connections']:
        if (c['from'] in star or c['to'] in star) and not c.get('refs'): fill(c, ('note',))
    for w in d['works']:
        if w.get('star') and len(w.get('refs') or []) == 1:
            w['refs'] = w['refs'] + [REF | {'url': 'https://example.org/q'}]
            w['key'] += '[2]'; w['es']['key'] += '[2]'
    json.dump(d, open(AP, 'w', encoding='utf-8'), ensure_ascii=False)
    E = jl(EP)
    for e in E['essays']:
        e['refs'] = [REF]; e['paras'][0] += '[1]'; e['es']['paras'][0] += '[1]'
    json.dump(E, open(EP, 'w', encoding='utf-8'), ensure_ascii=False)
    inc = jl(IP)
    for i in inc['incidencias']: i['estado'] = 'cerrada'
    json.dump(inc, open(IP, 'w', encoding='utf-8'), ensure_ascii=False)
    r = run('tools/pipeline/auditoria.py', '--v1')
    check(r.returncode == 0 and 'TOTAL pendientes: 0' in r.stdout and 'R2 TERMINADA' in r.stdout, 'todo con fuentes y las incidencias cerradas: 0 pendientes, código 0', r.stdout[-600:])

    # ---- cada categoría detecta su caso ----
    def verdict(mut, key, needle=None):
        dd = copy.deepcopy(d); ee = copy.deepcopy(E); ii = copy.deepcopy(inc)
        mut(dd, ee, ii)
        json.dump(dd, open(AP, 'w', encoding='utf-8'), ensure_ascii=False); json.dump(ee, open(EP, 'w', encoding='utf-8'), ensure_ascii=False); json.dump(ii, open(IP, 'w', encoding='utf-8'), ensure_ascii=False)
        r = run('tools/pipeline/auditoria.py', '--v1', '--json', os.path.join(tmp, 'm.json'))
        P2 = jl(os.path.join(tmp, 'm.json'))
        return r.returncode, P2
    star_work = next(w for w in d['works'] if w.get('star'))
    code, P2 = verdict(lambda dd, ee, ii: next(w for w in dd['works'] if w['id'] == star_work['id']).update(refs=[]), 'works')
    check(code == 1 and star_work['id'] in P2['works'], 'detecta una obra ★ sin fuentes')
    code, P2 = verdict(lambda dd, ee, ii: next(x for x in dd['contexts']).update(refs=[]), 'contexts')
    check(code == 1 and len(P2['contexts']) == 1, 'detecta un contexto sin fuentes')
    code, P2 = verdict(lambda dd, ee, ii: ee['essays'][0].update(refs=[]), 'essays')
    check(code == 1 and P2['essays'] == [E['essays'][0]['id']], 'detecta un ensayo sin fuentes')
    lk = next(l for l in d['ctxLinks'] if l['item'] in star)
    code, P2 = verdict(lambda dd, ee, ii: next(l for l in dd['ctxLinks'] if (l['ctx'], l['item']) == (lk['ctx'], lk['item'])).update(refs=[]), 'links')
    check(code == 1 and P2['links'] == [lk['ctx'] + '~' + lk['item']], 'detecta un enlace ★ sin fuentes')
    cn = next(c for c in d['connections'] if c['from'] in star or c['to'] in star)
    code, P2 = verdict(lambda dd, ee, ii: next(c for c in dd['connections'] if (c['from'], c['to']) == (cn['from'], cn['to'])).update(refs=[]), 'connections')
    check(code == 1 and P2['connections'] == [cn['from'] + '>' + cn['to']], 'detecta una conexión ★ sin fuentes')
    code, P2 = verdict(lambda dd, ee, ii: next(x for x in dd['theories'] if x.get('star')).update(key=next(x for x in dd['theories'] if x.get('star'))['key'] + '[7]'), 'orphan')
    check(code == 1 and len(P2['orphan_marks']) == 1 and '[7]' in P2['orphan_marks'][0], 'detecta una marca [n] sin fuente', P2['orphan_marks'])
    code, P2 = verdict(lambda dd, ee, ii: (lambda x: x.update(refs=x['refs'] + [REF | {'url': 'https://example.org/z'}]))(next(x for x in dd['institutions'] if x.get('star'))), 'uncited')
    check(code == 1 and len(P2['uncited_refs']) == 1, 'detecta una fuente sin citar', P2['uncited_refs'])
    code, P2 = verdict(lambda dd, ee, ii: ee['essays'][0].update(paras=ee['essays'][0]['paras'] + ['Texto [3].']), 'orphan')
    check(code == 1 and len(P2['orphan_marks']) == 1, 'detecta una marca huérfana en un ensayo')
    code, P2 = verdict(lambda dd, ee, ii: ii['incidencias'][0].update(estado='decidida'), 'inc')
    check(code == 1 and len(P2['open_incidents']) == 1, 'una incidencia decidida pero no aplicada sigue pendiente')
    code, P2 = verdict(lambda dd, ee, ii: ii['incidencias'][0].update(estado='aplicada'), 'inc')
    check(code == 0, 'aplicada o cerrada no cuenta')
    wk = next(w for w in d['works'] if w.get('star'))
    code, P2 = verdict(lambda dd, ee, ii: next(w for w in dd['works'] if w['id'] == wk['id']).update(refs=[REF], key=wk['key'].replace('[2]', '').replace('[1]', '') + '[1]'), 'single')
    check(code == 1 and wk['id'] in P2['single_source_works'], 'detecta una obra ★ con una sola fuente')
finally:
    shutil.rmtree(tmp, ignore_errors=True)
print('RESULT: ' + ('PASS' if ok_all else 'FAIL'))
sys.exit(0 if ok_all else 1)
