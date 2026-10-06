"""v24: two detail levels (point 48), context collapsed on load (49), macro-movements inside Movements (50)."""
import subprocess, time, os
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(os.environ.get('LHD_SHOTS', '/tmp'), 'lhd-shots'); os.makedirs(OUT, exist_ok=True)
EXE = os.environ.get('CHROMIUM', '/opt/pw-browsers/chromium')
srv = subprocess.Popen(['python3', '-m', 'http.server', '8768', '-d', ROOT], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(0.8)
ok = True
def check(cond, msg):
    global ok
    print(('PASS ' if cond else 'FAIL ') + msg); ok = ok and cond
try:
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=EXE)
        pg = b.new_context(viewport={'width': 1440, 'height': 900}).new_page()
        errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        for pat in ('**/fonts.googleapis.com/**', '**/fonts.gstatic.com/**'): pg.route(pat, lambda r: r.abort())
        pg.route('**/en.wikipedia.org/**', lambda r: r.fulfill(status=200, content_type='application/json', body='{"query":{"pages":{}}}'))
        pg.add_init_script("try{localStorage.clear();localStorage.setItem('lhd-lang','es');localStorage.setItem('lhd-level','complete')}catch(e){}")
        pg.goto('http://127.0.0.1:8768/index.html'); pg.wait_for_timeout(1000)
        check(pg.locator('[data-level]').count() == 2, 'only two level buttons')
        check(pg.evaluate("LHD.state.level") == 'normal', 'stored «complete» falls back to normal')
        check(pg.evaluate("LHD.state.data.works.every(w=>w.level==='essential'||w.level==='normal')"), 'all works are essential or normal')
        check(pg.locator('#content .it.ctx, #content .it.prod').count() == 0, 'context and productive rows collapsed on load')
        check(pg.evaluate("['political','economic','social','cultural','technological','production'].every(k=>LHD.state.collapsed.has('trk:'+k))"), 'all context keys collapsed')
        pg.screenshot(path=f'{OUT}/v24-load.png')
        check(pg.locator('.it.movement[data-id="macro-modernism"]').count() == 1 and pg.locator('.it.macro').count() == 0, 'macro drawn as a movement')
        pg.click('[data-type="movements"]') if pg.locator('[data-type="movements"]').count() else pg.evaluate("LHD.state.types.delete('movements')")
        pg.wait_for_timeout(300)
        check(pg.locator('.it.movement[data-id="macro-modernism"]').count() == 0, 'hiding movements hides the macro too')
        check(not errs, 'no page errors ' + ' '.join(errs[:2]))
        b.close()
finally:
    srv.terminate()
print('RESULT:', 'PASS' if ok else 'FAIL')
