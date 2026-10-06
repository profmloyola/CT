"""Etapa 0 (v31): pruebas de candidatos_recorte.py y recortar.py (sin navegador). Todo lo que escribe va a copias."""
import hashlib, glob, json, os, shutil, subprocess, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, 'tools', 'pipeline'); sys.path.insert(0, P)
import recorte_lib as R, candidatos_recorte as C
ok = True
def check(cond, msg):
    global ok
    print(('PASS ' if cond else 'FAIL ') + msg); ok = ok and cond
def digest(base=ROOT):
    h = hashlib.md5()
    for f in sorted(glob.glob(base + '/src-data/*/*.json')) + [base + '/tools/RESERVA-FASE-B.json', base + '/data/all.json']:
        h.update(open(f, 'rb').read())
    return h.hexdigest()
def run(sel, *extra, base=None):
    tmp = tempfile.mkdtemp(); p = os.path.join(tmp, 'sel.json'); json.dump(sel, open(p, 'w'))
    cmd = [sys.executable, P + '/recortar.py', p] + list(extra) + (['--base', base] if base else [])
    out = subprocess.run(cmd, capture_output=True, text=True); shutil.rmtree(tmp); return out
before = digest()
N0 = len(list(R.Model().items('works')))
m = R.Model(); cand, dcand, ccand, (pw, pd_, pc) = C.analyse(m)
works = {w['id']: w for w in m.items('works')}
cids = {x['id'] for v in cand.values() for x in v}
check(sum(len(v) for v in cand.values()) >= 18 + 10, f'hay candidatos de sobra ({sum(len(v) for v in cand.values())}) para quitar 18')
check(all(works[i]['level'] == 'normal' and i not in pw for i in cids), 'ningún candidato es ★ ni está protegido')
check(not (cids & {w['id'] for w in works.values() if 'latin-america' in w['regions']}), 'ningún candidato es de América Latina')
check(all(x['links'] <= y['links'] for v in cand.values() for x, y in zip(v, v[1:])), 'orden: menos enlaces primero')
out = subprocess.run([sys.executable, P + '/candidatos_recorte.py'], capture_output=True, text=True)
check(out.returncode == 0 and '== graphic' in out.stdout and 'Hechos de contexto' in out.stdout, 'candidatos_recorte.py imprime obras, diseñadores y contexto')
# selección de 3 obras que no dejan diseñadores sin obra
def free(sel):
    for did in {d for i in sel for d in works[i].get('designers') or []}:
        if all(i in sel for i in [w['id'] for w in works.values() if did in (w.get('designers') or [])]): return False
    return True
sel = []
for disc in ('graphic', 'product', 'architecture'):
    for x in cand[disc]:
        if x['links'] >= 0 and free(sel + [x['id']]): sel.append(x['id']); break
withlink = next(x['id'] for v in cand.values() for x in v if x['links'] >= 1 and free(sel + [x['id']]))
sel.append(withlink)
out = run({'works': sel, 'designers': [], 'contexts': []}, '--prueba')
check(out.returncode == 0 and 'PRUEBA' in out.stdout and 'sin huérfanos' in out.stdout and 'no PROBLEM' in out.stdout, '--prueba quita 4 obras sin huérfanos ni PROBLEM: ' + out.stdout.strip()[:200])
check(f'obras {N0} -> {N0 - 4}' in out.stdout, f'--prueba cuenta {N0} -> {N0 - 4} obras')
check(digest() == before, '--prueba no toca el proyecto')
# se niega
refusals = [
    ('obra ★', {'works': ['barcelona-chair']}, 'es ★'),
    ('obra citada en una conexión', {'works': [next(w for w in m.items('works') if w['level'] == 'normal' and any(c['from'] == w['id'] or c['to'] == w['id'] for c in m.items('connections')))['id']]}, 'conexión'),
    ('obra latinoamericana', {'works': [next(w['id'] for w in m.items('works') if 'latin-america' in w['regions'] and w['level'] == 'normal')]}, 'América Latina'),
    ('diseñador ★', {'designers': ['gropius']}, 'PROTEGIDO'),
    ('diseñador con obras que se quedan', {'designers': [next(d['id'] for d in m.items('designers') if d['level'] == 'normal' and sum(d['id'] in (w.get('designers') or []) for w in works.values()) >= 1)]}, 'obras que se quedan'),
    ('obra que deja sin obras a un diseñador', {'works': [next(w['id'] for w in works.values() if w['level'] == 'normal' and w['id'] not in pw and not free([w['id']]))]}, 'se quedaría sin obras'),
    ('id inexistente', {'works': ['no-existe']}, 'no existe'),
]
for name, s_, frag in refusals:
    s_.setdefault('works', []); s_.setdefault('designers', []); s_.setdefault('contexts', [])
    o = run(s_, '--prueba')
    check(o.returncode == 1 and frag in o.stdout, f'se niega: {name} ({frag})')
# aplicación real sobre una COPIA del proyecto
tmp = tempfile.mkdtemp()
shutil.copytree(ROOT + '/src-data', tmp + '/src-data'); os.makedirs(tmp + '/tools'); shutil.copy(ROOT + '/tools/build_data.py', tmp + '/tools')
_r = json.load(open(ROOT + '/tools/RESERVA-FASE-B.json', encoding='utf-8')); _r.pop('recorte_modernismo', None); json.dump(_r, open(tmp + '/tools/RESERVA-FASE-B.json', 'w', encoding='utf-8'))
o = run({'works': sel, 'designers': [], 'contexts': []}, base=tmp)
check(o.returncode == 0 and 'RECORTE' in o.stdout and 'build real: OK' in o.stdout, 'aplicación real (en una copia): ' + o.stdout.strip()[-160:])
m2 = R.Model(tmp + '/src-data')
check(len(list(m2.items('works'))) == N0 - 4 and not R.orphans(m2) and not set(sel) & set(m2.by_id('works')), 'copia: N0-4 obras, sin huérfanos, obras quitadas')
res = json.load(open(tmp + '/tools/RESERVA-FASE-B.json', encoding='utf-8'))
check(sorted(w['id'] for w in res['recorte_modernismo']['works']) == sorted(sel), 'las obras quitadas quedan en RESERVA-FASE-B.json (recorte_modernismo)')
check(os.path.exists(tmp + '/data/all.json'), 'el build real generó data/all.json en la copia')
shutil.rmtree(tmp)
check(digest() == before, 'el proyecto real quedó intacto')
print('RESULT:', 'PASS' if ok else 'FAIL')
