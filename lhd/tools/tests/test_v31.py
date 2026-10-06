"""v31 (paso 0.10 del plan, punto 61): elementos de influencia oriental (regions: ["global"], countries: ["JP"]).
Con 'Organizar por región' caen en el grupo «Global», subdividido en la zona «Más allá de Occidente (por su influencia)».
Con los datos actuales (desde la etapa 6) el grupo aparece."""
import subprocess, time, os, json
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(os.environ.get('LHD_SHOTS', '/tmp'), 'lhd-shots'); os.makedirs(OUT, exist_ok=True)
EXE = os.environ.get('CHROMIUM', '/opt/pw-browsers/chromium')
PORT = 8768
srv = subprocess.Popen(['python3', '-m', 'http.server', str(PORT), '-d', ROOT, '--bind', '127.0.0.1'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(0.8)
ok = True
def check(cond, msg):
    global ok
    print(('PASS ' if cond else 'FAIL ') + msg); ok = ok and cond
raw = json.load(open(os.path.join(ROOT, 'data/all.json'), encoding='utf-8'))
inj = json.loads(json.dumps(raw))
for k in ('movements', 'designers'):
    x = next(a for a in inj[k] if a['id'] in ('de-stijl', 'kaare-klint'))
    x['regions'] = ['global']; x['countries'] = ['JP']
try:
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=EXE)
        def page(data):
            ctx = b.new_context(viewport={'width': 1440, 'height': 900}); pg = ctx.new_page(); errs = []
            pg.on('pageerror', lambda e: errs.append(str(e)))
            for pat in ('**/fonts.googleapis.com/**', '**/fonts.gstatic.com/**'): pg.route(pat, lambda r: r.abort())
            pg.route('**/en.wikipedia.org/**', lambda r: r.fulfill(status=200, content_type='application/json', body='{"query":{"pages":{}}}'))
            if data is not None: pg.route('**/data/all.json', lambda r: r.fulfill(status=200, content_type='application/json', body=json.dumps(data)))
            pg.add_init_script("try{localStorage.setItem('lhd-lang','es');localStorage.setItem('lhd-arrange','region')}catch(e){}")
            return pg, errs
        pg, errs = page(None)
        pg.goto(f'http://127.0.0.1:{PORT}/index.html'); pg.wait_for_timeout(1200)
        labs0 = pg.evaluate("() => [...document.querySelectorAll('.grp-label, .zone-label')].map(e => e.textContent.trim())")
        # desde la etapa 6 los datos reales sí traen elementos orientales (95 con regions: global): el grupo y la zona aparecen (v47, C6)
        check(any(l.startswith('Global') for l in labs0) and any(l.startswith('Más allá de Occidente') for l in labs0), 'datos actuales: aparece el grupo Global con la zona Más allá de Occidente')
        check(not errs, 'datos actuales: sin errores de página')
        pg2, errs2 = page(inj)
        pg2.goto(f'http://127.0.0.1:{PORT}/index.html#de-stijl'); pg2.wait_for_timeout(1500)
        labs = pg2.evaluate("() => [...document.querySelectorAll('.grp-label, .zone-label')].map(e => e.textContent.trim())")
        check(any(l.startswith('Global') for l in labs) and any(l.startswith('Más allá de Occidente') for l in labs), 'con elementos orientales: grupo «Global» con la zona «Más allá de Occidente» ' + str(labs))
        check(pg2.locator('#content .it[data-id="de-stijl"]').count() == 1, 'el movimiento de prueba (JP) se dibuja')
        check(any(l.startswith('Europa') for l in labs) and any(l.startswith('América Latina') for l in labs), 'los demás grupos (Europa, América Latina) siguen apareciendo')
        pg2.screenshot(path=f'{OUT}/v31-region-global.png')
        check('de-stijl' in (pg2.evaluate('() => LHD.state.sel') or ''), 'su ficha abre sin errores')
        check(not errs2, 'con elementos orientales: sin errores de página ' + ' | '.join(errs2[:2]))
        b.close()
finally:
    srv.terminate()
print('RESULT:', 'PASS' if ok else 'FAIL')
