"""Etapa 1b (v34): vista previa de las listas (preview_listas.py). Sin tocar src-data/ ni data/. Incluye una carga en el navegador."""
import hashlib, glob, json, os, subprocess, sys, tempfile, shutil, threading, http.server, functools
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ok = True
def check(c, m):
    global ok
    print(('PASS ' if c else 'FAIL ') + m); ok = ok and c
def digest():
    h = hashlib.md5()
    for f in sorted(glob.glob(ROOT + '/src-data/*/*.json')) + [ROOT + '/data/all.json', ROOT + '/index.html']:
        h.update(open(f, 'rb').read())
    return h.hexdigest()
d0 = digest()
out = os.path.join(tempfile.mkdtemp(), 'vp')
r = subprocess.run([sys.executable, ROOT + '/tools/pipeline/preview_listas.py', '--out', out], capture_output=True, text=True)
check(r.returncode == 0 and 'OK: no PROBLEM' in r.stdout, 'la vista previa se construye sin PROBLEM')
for f in ('index.html', 'app.js', 'style.css', 'data/all.json', 'LEEME-VISTA-PREVIA.md', 'INFORME-VISTA-PREVIA.md'):
    check(os.path.exists(os.path.join(out, f)), f'existe {f}')
d = json.load(open(out + '/data/all.json', encoding='utf-8'))
real = json.load(open(ROOT + '/data/all.json', encoding='utf-8'))
check(len(d['works']) >= 500, f"obras: {len(d['works'])} (etapa 6: mínimo 500; V3 = 585)")
check(sum(1 for w in d['works'] if w.get('level') == 'essential') in range(140, 190), 'obras ★ entre 140 y 189 (etapa 6: ~165)')
check(len(d['items']) >= len(real['items']), f"al menos tantos elementos que el sitio real ({len(d['items'])} vs {len(real['items'])})")
check(all(w['id'] in {x['id'] for x in d['works']} for w in real['works']), 'toda obra del sitio real está en la vista previa')
check({'ctx-corfo', 'ctx-early-television'} <= {c['id'] for c in d['contexts']}, 'ctx-corfo y ctx-early-television reintegrados')
mm = next(m for m in d['movements'] if m['id'] == 'macro-modernism')
check({'good-design', 'ulm-functionalism', 'international-typographic-style', 'corporate-identity-design'} <= set(mm['parts']), 'macro-modernism suma los movimientos de Posguerra')
extra = {i[0] for i in d['items']} - {i[0] for i in real['items']}
retirados = open(ROOT + '/tools/RESERVA-FASE-B.json', encoding='utf-8').read()
check((any(c.get('draft') for c in d['contexts']) or all('"' + x + '"' in retirados for x in extra)) and not any(w.get('draft') for w in real['works']), 'las fichas nuevas llevan draft (si queda alguna sin escribir); las reales no')
check('previewBadge' in open(out + '/index.html', encoding='utf-8').read(), 'etiqueta VISTA PREVIA en index.html')
check(digest() == d0, 'el proyecto real (src-data, data, index.html) quedó intacto')
# navegador
try:
    from playwright.sync_api import sync_playwright
    H = functools.partial(http.server.SimpleHTTPRequestHandler, directory=out)
    H.log_message = lambda *a, **k: None
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), H); port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get('CHROMIUM', '/opt/pw-browsers/chromium')); pg = b.new_page(viewport={'width': 1400, 'height': 900})
        errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.goto(f'http://127.0.0.1:{port}/index.html'); pg.wait_for_timeout(1800)
        check(not errs, 'sin errores de JavaScript: ' + str(errs[:2]))
        check(pg.evaluate("LHD.state.data.works.length") == len(d['works']), 'el sitio carga todas las obras')
        pg.evaluate("LHD.go('i-love-ny-1977')"); pg.wait_for_timeout(500)
        t = pg.locator('#panel').inner_text()
        check('Ficha en desarrollo' in t and 'quiebra' in t.lower() or 'fiscal' in t.lower(), 'la ficha de «I ♥ NY» (Posmoderno, aún en desarrollo) muestra «en desarrollo» y su contexto con mecanismo')
        b.close()
    srv.shutdown()
except ImportError:
    print('SKIP navegador (sin playwright)')
shutil.rmtree(os.path.dirname(out), ignore_errors=True)
print('RESULT', 'OK' if ok else 'FALLA'); sys.exit(0 if ok else 1)
