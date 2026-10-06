"""R1 (Parte II): la auditoría corre, no tiene ERROR sin anotar, el build no avisa etiquetas largas y la limpieza es idempotente.
Sin navegador. No modifica nada (r1_limpieza.py se prueba con --dry)."""
import json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ok = True
def check(cond, msg):
    global ok
    print(('PASS ' if cond else 'FAIL ') + msg)
    ok = ok and cond
def run(*a):
    return subprocess.run([sys.executable] + list(a), cwd=ROOT, capture_output=True, text=True)

b = run('tools/build_data.py', '-v')
check('OK: no PROBLEM' in b.stdout, 'build sin PROBLEM')
check('timeline label is long' not in b.stdout, 'ninguna etiqueta de la línea de tiempo supera 22 caracteres')
a = run('tools/pipeline/auditoria.py', '--strict', '--json', os.path.join(ROOT, 'tools', 'pipeline', '.auditoria-test.json'))
check(a.returncode == 0, 'auditoría --strict: 0 ERROR sin anotar')
check('AUDITORÍA LHD' in a.stdout and 'Hallazgos' in a.stdout, 'la auditoría imprime su informe')
p = os.path.join(ROOT, 'tools', 'pipeline', '.auditoria-test.json')
f = json.load(open(p, encoding='utf-8')); os.remove(p)
check(not [x for x in f if x['sev'] == 'ERROR' and '[anotada]' not in x['msg']], 'sin ERROR sin anotar en el JSON')
check(not [x for x in f if x['cat'] in ('id inexistente', 'marca [n] sin fuente', 'enlace de contexto repetido', 'conexión repetida')], 'sin ids rotos, marcas sin fuente ni duplicados')
d = run('tools/pipeline/r1_limpieza.py', '--dry')
check('shorts agregados: 0; enlaces repetidos quitados: 0; enlaces nuevos: 0' in d.stdout, 'r1_limpieza.py es idempotente (nada que hacer)')
print('RESULT: ' + ('PASS' if ok else 'FAIL'))
sys.exit(0 if ok else 1)
