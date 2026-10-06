"""v21 (point 44), updated in v30 (point 59): numbered sources. Public site AND edit mode show superscripts and a numbered Sources list (inside a collapsed section)."""
import subprocess, time, os, re
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(os.environ.get('LHD_SHOTS', '/tmp'), 'lhd-shots'); os.makedirs(OUT, exist_ok=True)
EXE = os.environ.get('CHROMIUM', '/opt/pw-browsers/chromium')
srv = subprocess.Popen(['php', '-S', '127.0.0.1:8766', '-t', ROOT], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(0.8)
ok = True
def check(cond, msg):
    global ok
    print(('PASS ' if cond else 'FAIL ') + msg)
    ok = ok and cond
try:
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=EXE)
        ctx = b.new_context(viewport={'width': 1440, 'height': 900})
        pg = ctx.new_page()
        errs = []
        pg.on('pageerror', lambda e: errs.append('PAGEERROR: ' + str(e)))
        for pat in ('**/fonts.googleapis.com/**', '**/fonts.gstatic.com/**'): pg.route(pat, lambda r: r.abort())
        pg.route('**/en.wikipedia.org/**', lambda r: r.fulfill(status=200, content_type='application/json', body='{"query":{"pages":{}}}'))
        pg.add_init_script("try{localStorage.setItem('lhd-lang','es')}catch(e){}")
        CL = os.environ.get('LHD_CLAVE', 'uai2026')
        # public site: same information as edit mode
        for iid in ('ctx-red-vienna', 'frankfurt-kitchen', 'inst-neues-frankfurt'):
            pg.goto(f'http://127.0.0.1:8766/index.html#{iid}'); pg.wait_for_timeout(900)
            txt = pg.locator('#panel').inner_text()
            check(not re.search(r'\[\d{1,2}\]|⟦', txt), f'public card {iid} without raw markers')
            check(pg.locator('#panel sup.rf').count() >= 1, f'public card {iid} shows superscripts')
            check(pg.locator('#panel details.sources .rf-list li').count() >= 1, f'public card {iid} lists its sources')
        pg.fill('#q', 'Viena Roja'); pg.wait_for_timeout(400)
        check(pg.locator('#results button').count() > 0, 'search finds the new fact')
        check(not re.search(r'\[\d|⟦', pg.locator('#results').inner_text()), 'search results without markers')
        # edit mode
        pg.goto('http://127.0.0.1:8766/index.html?editar#ctx-red-vienna'); pg.wait_for_timeout(900)
        pg.locator('#panel details.sources > summary').click(); pg.wait_for_timeout(200)
        n_sup = pg.locator('#panel sup.rf').count(); n_src = pg.locator('#panel .rf-list li').count()
        check(n_sup >= 3, f'edit card shows superscripts ({n_sup})')
        check(n_src >= 2, f'edit card lists its sources ({n_src})')
        txt = pg.locator('#panel').inner_text()
        check('⟦' not in txt and not re.search(r'\[\d{1,2}\]', txt), 'no raw tokens or markers in edit mode')
        pg.screenshot(path=f'{OUT}/v21-sources-context.png')
        pg.locator('#panel sup.rf a').first.click(); pg.wait_for_timeout(900)
        check(pg.locator('#panel .rf-list li.rf-hi').count() == 1, 'clicking a superscript highlights its source')
        pg.goto('http://127.0.0.1:8766/index.html?editar#frankfurt-kitchen'); pg.wait_for_timeout(1200)
        pg.locator('#panel details.sources > summary').click(); pg.wait_for_timeout(200)
        n_sup = pg.locator('#panel sup.rf').count(); n_src = pg.locator('#panel .rf-list li').count()
        check(n_sup >= 3 and n_src >= 3, f'work card numbers the sources of its links ({n_sup} sup, {n_src} sources)')
        nums = [int(x) for x in pg.locator('#panel .rf-list .rf-n').all_inner_texts()]
        check(nums == list(range(1, len(nums) + 1)), f'sources numbered 1..n without gaps {nums}')
        pg.locator('#panel details.sources').scroll_into_view_if_needed()
        pg.screenshot(path=f'{OUT}/v21-sources-work.png')
        import json as _j
        _d = _j.load(open(os.path.join(ROOT, 'data/all.json')))
        _L = {l['item'] for l in _d['ctxLinks'] if l.get('refs')} | {l['ctx'] for l in _d['ctxLinks'] if l.get('refs')}
        _C = {c[k] for c in _d['connections'] if c.get('refs') for k in ('from', 'to')}
        _none = next((x['id'] for k in ('theories', 'institutions', 'designers', 'contexts') for x in _d[k] if not x.get('refs') and x['id'] not in _L and x['id'] not in _C), None)
        pg.goto(f'http://127.0.0.1:8766/index.html?editar#{_none}'); pg.wait_for_timeout(1000)
        check(pg.locator('#panel details.sources .rf-none').count() == 1, 'card without sources says so')
        check(not errs, 'no page errors ' + ' | '.join(errs[:3]))
        b.close()
finally:
    srv.terminate()
print('RESULT:', 'PASS' if ok else 'FAIL')
