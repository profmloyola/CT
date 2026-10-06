"""v22: concepts on the macromovement card (point 45) and corrections of the independent review (point 46)."""
import subprocess, time, os, re, json
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(os.environ.get('LHD_SHOTS', '/tmp'), 'lhd-shots'); os.makedirs(OUT, exist_ok=True)
EXE = os.environ.get('CHROMIUM', '/opt/pw-browsers/chromium')
srv = subprocess.Popen(['python3', '-m', 'http.server', '8767', '-d', ROOT], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(0.8)
ok = True
def check(cond, msg):
    global ok
    print(('PASS ' if cond else 'FAIL ') + msg)
    ok = ok and cond
try:
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=EXE)
        pg = b.new_context(viewport={'width': 1440, 'height': 900}).new_page()
        errs = []
        pg.on('pageerror', lambda e: errs.append('PAGEERROR: ' + str(e)))
        for pat in ('**/fonts.googleapis.com/**', '**/fonts.gstatic.com/**'): pg.route(pat, lambda r: r.abort())
        pg.route('**/en.wikipedia.org/**', lambda r: r.fulfill(status=200, content_type='application/json', body='{"query":{"pages":{}}}'))
        pg.add_init_script("try{localStorage.setItem('lhd-lang','es')}catch(e){}")
        pg.goto('http://127.0.0.1:8767/index.html#macro-modernism'); pg.wait_for_timeout(1000)
        txt = pg.locator('#panel').inner_text()
        check('Conceptos' in txt or 'CONCEPTOS' in txt, 'macro card has a Concepts section')
        n = pg.evaluate("[...document.querySelectorAll('#panel h3, #panel h4')].filter(h=>/concept/i.test(h.textContent)).length")
        chips = pg.evaluate("(()=>{const h=[...document.querySelectorAll('#panel h3, #panel h4')].find(h=>/concept/i.test(h.textContent)); return h? h.parentElement.querySelectorAll('.chip, button').length : 0})()")
        check(chips >= 8, f'macro card lists the 8 Modernism concepts ({chips})')
        pg.screenshot(path=f'{OUT}/v22-macro-concepts.png')
        pg.goto('http://127.0.0.1:8767/index.html#macro-postmodernism'); pg.wait_for_timeout(800)
        check('Conceptos' not in pg.locator('#panel').inner_text(), 'postmodern macro card without concepts (none written yet)')
        pg.goto('http://127.0.0.1:8767/index.html#coco-chanel'); pg.wait_for_timeout(800)
        txt = pg.locator('#panel').inner_text()
        check('Gabrielle' in txt, 'Chanel birth name present (v33: Adrian was cut)')
        pg.goto('http://127.0.0.1:8767/index.html#ministry-education-rio'); pg.wait_for_timeout(800)
        check('Lúcio Costa' in pg.locator('#panel').inner_text(), 'Ministry card credits Lúcio Costa')
        check(not errs, 'no page errors ' + ' '.join(errs))
        b.close()
finally:
    srv.terminate()
d = json.load(open(os.path.join(ROOT, 'data/all.json')))
labels = [r['label'] for x in d['ctxLinks'] for r in x.get('refs', [])]
check(not any('Frye' in l for l in labels), 'no context link relies on the Frye catalogue record')
print('RESULT:', 'PASS' if ok else 'FAIL')
