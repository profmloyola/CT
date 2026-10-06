"""Etapa 0 (v31): prueba de tools/empaquetar.sh sobre una COPIA del proyecto (nunca toca el real)."""
import os, shutil, subprocess, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ok = True
def check(cond, msg):
    global ok
    print(('PASS ' if cond else 'FAIL ') + msg); ok = ok and cond
tmp = tempfile.mkdtemp(); proj = os.path.join(tmp, 'lhd'); out = os.path.join(tmp, 'out')
shutil.copytree(ROOT, proj, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
# la copia simula la versión 77 (el estado real puede ir en otra versión)
idx = open(proj + '/index.html', encoding='utf-8').read(); import re
open(proj + '/index.html', 'w', encoding='utf-8').write(re.sub(r'\?v=\d+', '?v=77', idx))
open(proj + '/ESTADO-ACTUAL.md', 'a', encoding='utf-8').write('\n(prueba) v77\n')
def run(nn, **env):
    e = dict(os.environ, OUT=out, **env)
    return subprocess.run(['sh', proj + '/tools/empaquetar.sh', nn], capture_output=True, text=True, env=e, cwd=tmp)
r = run('77')
check(r.returncode == 0 and 'ZIP listo y probado' in r.stdout and os.path.exists(out + '/LHD-v77.zip'), 'arma y prueba el ZIP en una carpeta limpia: ' + r.stdout.strip()[-120:])
r = run('78'); check(r.returncode == 1 and 'no menciona v78' in r.stdout, 'se niega si ESTADO-ACTUAL.md no menciona la versión')
open(proj + '/ediciones/imagenes.json', 'w').write('{"a": "https://x"}')
r = run('77'); check(r.returncode == 1 and 'imagenes.json' in r.stdout, 'se niega si ediciones/imagenes.json tiene datos')
open(proj + '/ediciones/imagenes.json', 'w').write('{}\n')
open(proj + '/ediciones/revision.json', 'w').write('{}')
r = run('77'); check(r.returncode == 1 and 'revision.json' in r.stdout, 'se niega si hay revision.json')
os.remove(proj + '/ediciones/revision.json')
s = open(proj + '/editar.php', encoding='utf-8').read(); open(proj + '/editar.php', 'w', encoding='utf-8').write(s.replace("'uai2026'", "'otra'"))
r = run('77'); check(r.returncode == 1 and 'clave' in r.stdout, 'se niega si editar.php no tiene la clave acordada')
r = run('abc'); check(r.returncode == 2, 'versión no numérica: código 2')
shutil.rmtree(tmp)
print('RESULT:', 'PASS' if ok else 'FAIL')
