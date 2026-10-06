"""Etapa 0 (v31): pruebas de validate_out.py y apply_new.py (sin navegador). Trabaja siempre sobre COPIAS de src-data."""
import contextlib, copy, hashlib, glob, json, os, shutil, subprocess, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'pipeline'))
import validate_out as V
import apply_new as A

ok = True
def check(cond, msg):
    global ok
    print(('PASS ' if cond else 'FAIL ') + msg)
    ok = ok and cond

def digest():
    h = hashlib.md5()
    for f in sorted(glob.glob(ROOT + '/src-data/*/*.json')) + [ROOT + '/tools/PENDIENTES-FUENTES.md', ROOT + '/tools/RESERVA-FASE-B.json']:
        h.update(open(f, 'rb').read())
    return h.hexdigest()
before = digest()

orig = json.load(open(ROOT + '/tools/tests/ejemplos_ok.json', encoding='utf-8'))
ren = {r['id'] for r in orig if 'id' in r}
def fix(x):
    if isinstance(x, dict): return {k: fix(v) for k, v in x.items()}
    if isinstance(x, list): return [fix(v) for v in x]
    return x + '-t' if isinstance(x, str) and x in ren else x
good = [fix(r) for r in orig]
tmp = tempfile.mkdtemp()
def write(name, data):
    p = os.path.join(tmp, name); json.dump(data, open(p, 'w', encoding='utf-8'), ensure_ascii=False); return p
def errs(data, refs=False, tramo='modernism', name='modernism_a.json'):
    return V.validate(write(name, data), refs, tramo)
def mut(fn, idx=0):
    d = copy.deepcopy(good); fn(d[idx]); return d

# ---- validate_out
check(errs(good) == [], 'archivo bueno: sin errores ' + str(errs(good)[:2]))
check(any('YA existe' in e for e in errs(orig)), '(a) id existente detectado')
check(any('no existe' in e for e in errs(mut(lambda r: r.update(designers=['no-such-designer']), 6))), '(b) id referenciado inexistente detectado')
check(any('es.key falta' in e for e in errs(mut(lambda r: r['es'].pop('key')))), '(c) falta es.key detectado')
check(any('no se traduce' in e for e in errs(mut(lambda r: r['es'].update(inventado='x')))), '(c) campo de más en es detectado')
check(any('misma cantidad' in e for e in errs(mut(lambda r: r['es']['traits'].pop(), 3))), '(c) traits con distinto largo detectado')
check(any('marca [n]' in e for e in errs(mut(lambda r: r.update(key=r['key'] + '[1]')))), '(d) marca [n] en la Parte I detectada')
check(any('refs: []' in e for e in errs(mut(lambda r: r.update(refs=[{'label': 'x'}])))), '(d) refs no vacío en la Parte I detectado')
check(any('máximo ~200' in e for e in errs(mut(lambda r: r.update(key='x' * 300)))), '(e) key larga detectada')
check(any('short de' in e for e in errs(mut(lambda r: r.update(short='y' * 30), 3))), '(e) short largo detectado')
check(any('note de' in e for e in errs(mut(lambda r: r.update(note='z' * 300), 9))), '(e) nota de enlace larga detectada')
check(any('level' in e for e in errs(mut(lambda r: r.update(level='star'), 3))), '(f) level inválido detectado')
check(any('fuera del tramo' in e for e in errs(mut(lambda r: r.update(start=1700), 3))), '(g) año fuera del tramo detectado')
check(any('rtype' in e for e in errs(mut(lambda r: r.pop('rtype')))), 'falta rtype detectado')
check(any('fuera de Occidente' in e for e in errs(mut(lambda r: r.update(countries=['JP']), 7))), 'C5: país oriental sin regions global detectado')
check(errs(mut(lambda r: r.update(countries=['JP'], regions=['global']), 7)) == [], 'C5: país oriental con regions global se acepta')
check(any('regions' in e for e in errs(mut(lambda r: r.update(regions=['asia']), 7))), 'región inválida detectada')
dis = [{'rtype': 'work', 'id': 'x-t', 'descartado': True, 'motivo': 'no lo conozco bien'}]
check(errs(dis) == [], 'registro descartado con motivo se acepta')
check(errs([{'rtype': 'work', 'id': 'x-t', 'descartado': True}]) != [], 'descartado sin motivo se rechaza')
# --refs (Parte II)
r2 = copy.deepcopy(orig[8])  # enlace (ids originales: existen en src-data)
r2['note'] = r2['note'] + '[1]'; r2['es']['note'] = r2['es']['note'] + '[1]'
r2['refs'] = [{'label': 'IWM', 'url': 'https://www.iwm.org.uk/x', 'checks': 'x', 'date': '2026-10-04'}]
check(errs([r2], refs=True) == [], '--refs: enlace con marca y fuente: OK ' + str(errs([r2], refs=True)))
b = copy.deepcopy(r2); b['refs'] = []
check(any('al menos una fuente' in e for e in errs([b], refs=True)), '--refs: sin fuentes detectado')
b = copy.deepcopy(r2); b['es']['note'] = b['es']['note'].replace('[1]', '')
check(any('mismas marcas' in e for e in errs([b], refs=True)), '--refs: EN y ES con distintas marcas detectado')
b = copy.deepcopy(r2); b['refs'][0]['url'] = 'https://en.wikipedia.org/wiki/X'
check(any('Wikipedia' in e for e in errs([b], refs=True)), '--refs: Wikipedia rechazada')
b = copy.deepcopy(r2); b['refs'].append(dict(b['refs'][0]))
check(any('no se cita' in e for e in errs([b], refs=True)), '--refs: fuente sin citar detectada')
# línea de comandos
p = write('modernism_cli.json', mut(lambda r: r['es'].pop('key')))
out = subprocess.run([sys.executable, ROOT + '/tools/pipeline/validate_out.py', p], capture_output=True, text=True)
check(out.returncode == 1 and 'es.key falta' in out.stdout, 'línea de comandos: código 1 y mensaje')
out = subprocess.run([sys.executable, ROOT + '/tools/pipeline/validate_out.py', write('modernism_ok.json', good)], capture_output=True, text=True)
check(out.returncode == 0 and out.stdout.strip().endswith('OK'), 'línea de comandos: archivo bueno imprime OK')

# ---- apply_new sobre una copia
root = os.path.join(tmp, 'src-data'); shutil.copytree(ROOT + '/src-data', root)
pend = os.path.join(tmp, 'pend.md'); shutil.copy(ROOT + '/tools/PENDIENTES-FUENTES.md', pend)
gp = write('modernism_good.json', good + [{'rtype': 'work', 'id': 'obra-dudosa', 'descartado': True, 'motivo': 'atribución dudosa'}])
added, pending, touched = A.apply_files('modernism', [gp], root, pend)
check(len(added) == 8 and set(added.values()) >= {'context', 'production', 'theory', 'movement', 'institution', 'designer', 'work'}, f'apply_new agrega 8 elementos ({len(added)})')
check(pending == [('obra-dudosa', 'atribución dudosa')] and 'obra-dudosa' in open(pend, encoding='utf-8').read(), 'el descarte queda en PENDIENTES-FUENTES.md')
def has(file, key, i):
    d = json.load(open(os.path.join(root, 'modernism', file + '.json'), encoding='utf-8')); return any(x.get('id') == i for x in d[key])
check(has('41-context-economic', 'contexts', 'ctx-fordism-t') and has('50-production-materials', 'production', 'tubular-steel-t') and has('56-theory', 'theories', 'th-vers-une-architecture-t'), 'contexto, productivo y teoría en su archivo')
check(has('21-works-product', 'works', 'barcelona-chair-t') and has('20-works-graphic', 'works', 'kitchener-poster-t') and has('10-designers', 'designers', 'gropius-t'), 'obras por disciplina y diseñador en su archivo')
lk = json.load(open(os.path.join(root, 'modernism', '80-context-links.json'), encoding='utf-8'))['links']
check(any(l['item'] == 'kitchener-poster-t' for l in lk), 'enlace agregado a 80-context-links.json')
cn = json.load(open(os.path.join(root, 'modernism', '85-connections.json'), encoding='utf-8'))['connections']
check(any(c['from'] == 'kitchener-poster-t' for c in cn), 'conexión agregada a 85-connections.json')
check(all('rtype' not in x for x in json.load(open(os.path.join(root, 'modernism', '56-theory.json'), encoding='utf-8'))['theories']), 'rtype no se guarda en los datos')
try:
    with contextlib.redirect_stdout(open(os.devnull, 'w')):
        A.apply_files('modernism', [gp], root, pend)
    dup = False
except SystemExit as e:
    dup = True
check(dup, 'un segundo apply del mismo archivo se rechaza (ids repetidos)')
# tramo vacío: crea los archivos que faltan
tgood = [fix(r) for r in orig if r['rtype'] in ('context', 'production')]
for r in tgood:
    r['id'] += '2'
    r['start'] = 1800 if r['rtype'] == 'context' else 1800
tp = write('industrial_a.json', tgood)
try:
    added2, _, touched2 = A.apply_files('industrial', [tp], root, pend)
    check(len(added2) == 2 and any(p.endswith('50-production-materials.json') for p in touched2), 'tramo industrial: crea el archivo de productivo que faltaba')
except SystemExit as e:
    check(False, 'tramo industrial: ' + str(e))
# --links-from-lists
listas = os.path.join(tmp, 'LISTAS.md')
open(listas, 'w', encoding='utf-8').write('| id | nombre | relaciona |\n|---|---|---|\n| `tubular-steel-t` | Acero tubular | `bauhaus-movement`, `breuer`, `no-existe` |\n| `gropius-t` | Gropius | `de-stijl`, `inst-bauhaus` |\n')
n = A.links_from_lists('modernism', root, listas)
ts = next(x for x in json.load(open(os.path.join(root, 'modernism', '50-production-materials.json'), encoding='utf-8'))['production'] if x['id'] == 'tubular-steel-t')
gr = next(x for x in json.load(open(os.path.join(root, 'modernism', '10-designers.json'), encoding='utf-8'))['designers'] if x['id'] == 'gropius-t')
check('breuer' in ts['links']['designers'] and 'bauhaus-movement' in ts['links']['movements'] and 'no-existe' not in json.dumps(ts['links']), '--links-from-lists rellena links de productivo (solo ids existentes)')
check('inst-bauhaus' in gr['institutions'] and gr['movements'].count('de-stijl') == 1, '--links-from-lists rellena movements/institutions del diseñador')
check(A.links_from_lists('modernism', root, listas) == 0, '--links-from-lists no duplica')

check(digest() == before, 'src-data, PENDIENTES y RESERVA reales quedaron intactos')
shutil.rmtree(tmp)
print('RESULT:', 'PASS' if ok else 'FAIL')
