"""Etapa 1 (v32): listas_check.py sobre LISTAS-CIERRE.md y la lista real de recorte (--prueba). Sin navegador; no escribe nada real."""
import hashlib, glob, json, os, subprocess, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, 'tools', 'pipeline')
ok = True
def check(c, m):
    global ok
    print(('PASS ' if c else 'FAIL ') + m); ok = ok and c
def digest():
    h = hashlib.md5()
    for f in sorted(glob.glob(ROOT + '/src-data/*/*.json')) + [ROOT + '/tools/RESERVA-FASE-B.json']:
        h.update(open(f, 'rb').read())
    return h.hexdigest()
d0 = digest()
r = subprocess.run([sys.executable, P + '/listas_check.py'], capture_output=True, text=True)
check(r.returncode == 0 and r.stdout.strip().splitlines()[-1].startswith('0 error(es)'), 'LISTAS-CIERRE.md pasa el verificador')
for t in ('industrial', 'reform', 'postwar', 'postmodern'):
    check(any(l.startswith(t + ':') for l in r.stdout.splitlines()), f'hay sección de {t}')
# el verificador detecta errores
bad = '''## Tramo: postwar
### Contextos
| id | nombre | sub | años | regiones | nivel | relaciona |
|---|---|---|---|---|---|---|
| `ctx-x` | X | political | 1950 | europe | ★ | `no-existe-zz` |
| `ctx-x` | X otra vez | political | 1950 | europe | N | |
### Obras
| id | título | disciplina | año | nivel | diseñadores | tech | regiones | contextos |
|---|---|---|---|---|---|---|---|---|
| `obra-x` | O | product | 1950 | ★ | | | europe | `ctx-x`: corto |
'''
tmp = tempfile.mkdtemp(); f = os.path.join(tmp, 'mala.md'); open(f, 'w').write(bad)
r = subprocess.run([sys.executable, P + '/listas_check.py', f, '--tramo', 'postwar'], capture_output=True, text=True)
check(r.returncode == 1, 'una lista mala falla')
for frag in ('id repetido', 'no existe', 'mecanismo demasiado corto', '★ necesita', 'objetivo'):
    check(frag in r.stdout, f'detecta: {frag}')
# recorte real (aplicado en v33): las listas quitadas ya no están en src-data y sí en la reserva
sel = json.load(open(ROOT + '/tools/RECORTE-MODERNISMO.json'))
check((len(sel['works']), len(sel['designers']), len(sel['contexts'])) == (18, 8, 3), 'el recorte es 18 obras, 8 diseñadores y 3 contextos')
sys.path.insert(0, P)
import recorte_lib as R
m = R.Model(); ids = m.all_ids()
REPUESTOS = {'claire-mccardell', 'adrian',  # repuestos a propósito en la etapa 6 (V3 aprobado, v44)
             'faaborg-chair', 'anglepoise-lamp', 'baby-brownie', 'maison-de-verre', 'karl-marx-hof', 'gres-draped-gowns',
             'kaare-klint', 'carwardine', 'walter-dorwin-teague', 'chareau', 'madame-gres'}  # repuestos en la etapa 7 (paso 7.4, v47)
check(not any(i in ids for k in sel for i in sel[k] if i not in REPUESTOS), 'lo recortado ya no está en src-data (salvo lo repuesto en la etapa 6)')
res = json.load(open(ROOT + '/tools/RESERVA-FASE-B.json', encoding='utf-8')).get('recorte_modernismo', {})
check(sorted(w['id'] for w in res.get('works', [])) == sorted(i for i in sel['works'] if i not in REPUESTOS), 'las obras recortadas (menos las repuestas) están en la reserva')
check(not R.orphans(m), 'sin huérfanos')
for keep in ('stool-60', 'maison-du-peuple-clichy', 'lacoste-polo', 'jean-prouve', 'lacoste'):
    check(keep in ids, f'V1 (punto 66): se mantiene {keep}')
check(digest() == d0, 'la prueba no escribió nada')
print('RESULT', 'OK' if ok else 'FALLA'); sys.exit(0 if ok else 1)
