"""v30 (point 59): public sources. Superscripts for everyone; 'Fuentes' is the last section of a card, closed on opening;
a card without sources shows a warning (also closed); clicking a superscript opens and highlights its source;
no markers in search, tooltips or labels; era, lens and info cards have no section."""
import subprocess, time, os, re, json
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(os.environ.get('LHD_SHOTS', '/tmp'), 'lhd-shots'); os.makedirs(OUT, exist_ok=True)
EXE = os.environ.get('CHROMIUM', '/opt/pw-browsers/chromium')
PORT = 8767
srv = subprocess.Popen(['python3', '-m', 'http.server', str(PORT), '-d', ROOT], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(0.8)
ok = True
def check(cond, msg):
    global ok
    print(('PASS ' if cond else 'FAIL ') + msg)
    ok = ok and cond
d = json.load(open(os.path.join(ROOT, 'data/all.json')))
linked = {l[k] for l in d['ctxLinks'] if l.get('refs') for k in ('ctx', 'item')}
none_id = next((x['id'] for k in ('theories', 'institutions', 'designers', 'contexts', 'movements') for x in d[k] if not x.get('refs') and x['id'] not in linked and not x.get('macro')), None)
URL = f'http://127.0.0.1:{PORT}/index.html'
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
        # a card with sources: public, section closed, superscripts, last section
        pg.goto(URL + '#ctx-red-vienna'); pg.wait_for_timeout(1000)
        det = pg.locator('#panel details.sources')
        check(det.count() == 1, 'Fuentes section present in the public card')
        check(not det.evaluate('e => e.open'), 'Fuentes closed on opening the card')
        check(re.match(r'Fuentes \(\d+\)', det.locator('summary').inner_text().strip()) is not None, 'title is "Fuentes (n)"')
        check(det.locator('svg.rf-warn').count() == 0, 'no warning when the card has sources')
        check(pg.evaluate("() => { const k = [...document.querySelector('#panel').children]; return k[k.length - 1].matches('details.sources'); }"), 'Fuentes is the last section')
        check(pg.locator('#panel sup.rf').count() >= 3, 'public card has superscripts')
        # click on a superscript while closed: opens and highlights
        pg.locator('#panel sup.rf a').first.click(); pg.wait_for_timeout(900)
        check(det.evaluate('e => e.open'), 'clicking a superscript opens Fuentes')
        check(pg.locator('#panel .rf-list li.rf-hi').count() == 1, 'clicking a superscript highlights its source')
        pg.screenshot(path=f'{OUT}/v30-fuentes-abierta.png')
        # stays open on re-render of the same card, closed on another card
        pg.evaluate("() => LHD.select('ctx-red-vienna')"); pg.wait_for_timeout(300)
        check(pg.locator('#panel details.sources').evaluate('e => e.open'), 'same card keeps its section open when it is drawn again')
        pg.evaluate("() => LHD.select('frankfurt-kitchen')"); pg.wait_for_timeout(600)
        check(not pg.locator('#panel details.sources').evaluate('e => e.open'), 'another card opens with Fuentes closed')
        pg.screenshot(path=f'{OUT}/v30-fuentes-cerrada.png')
        # markers never leak
        html = pg.evaluate('() => document.body.innerHTML')
        check('⟦' not in html and not re.search(r'>[^<]*\[\d{1,2}\][^<]*<', html), 'no tokens or [n] markers anywhere in the page')
        pg.fill('#q', 'Viena'); pg.wait_for_timeout(300)
        check(not re.search(r'\[\d|⟦', pg.locator('#results').inner_text()), 'search results without markers')
        pg.fill('#q', ''); pg.keyboard.press('Escape')
        pg.locator('#content .it.work').first.hover(force=True); pg.wait_for_timeout(300)
        check(not re.search(r'\[\d|⟦', pg.locator('#tip').inner_text()), 'tooltip without markers')
        # card without sources: warning visible with the section closed
        check(none_id is not None, 'there is a card without sources to test (' + str(none_id) + ')')
        pg.evaluate(f"() => LHD.select('{none_id}')"); pg.wait_for_timeout(700)
        det = pg.locator('#panel details.sources')
        check(det.count() == 1 and not det.evaluate('e => e.open'), 'card without sources: section closed')
        check(det.locator('summary svg.rf-warn').is_visible(), 'warning triangle visible in the closed title')
        check(pg.locator('#panel sup.rf').count() == 0, 'no superscripts without sources')
        det.locator('summary').click(); pg.wait_for_timeout(200)
        check('no ha sido revisada' in det.inner_text(), 'message says the card has not been reviewed')
        pg.screenshot(path=f'{OUT}/v30-sin-fuentes.png')
        # English
        pg.click('#langBtn'); pg.wait_for_timeout(600)
        check('has not been reviewed' in pg.locator('#panel details.sources').inner_text() or pg.locator('#panel details.sources').evaluate('e => e.open'), 'English message')
        pg.click('#langBtn'); pg.wait_for_timeout(300)
        # concept card has the section too
        if d.get('concepts'):
            pg.evaluate(f"() => LHD.select('{d['concepts'][0]['id']}')"); pg.wait_for_timeout(500)
            check(pg.locator('#panel details.sources').count() == 1, 'concept card has the section')
        # no section in era, lens or info cards
        pg.evaluate("() => LHD.select(null)"); pg.evaluate("() => LHD.showEra('modernism')"); pg.wait_for_timeout(500)
        check(pg.locator('#panel details.sources').count() == 0 and pg.locator('#panel sup.rf').count() == 0, 'era card without section')
        pg.evaluate("() => LHD.setFocus('political')"); pg.wait_for_timeout(500)
        check(pg.locator('#panel details.sources').count() == 0 and pg.locator('#panel sup.rf').count() == 0, 'lens card without section')
        pg.evaluate("() => LHD.setFocus(null)"); pg.click('#infoBtn'); pg.wait_for_timeout(400)
        check(pg.locator('#panel details.sources').count() == 0, 'info card without section')
        # phone width screenshot (the site is desktop-only; just must not break)
        pg2 = ctx.new_page(); pg2.set_viewport_size({'width': 390, 'height': 800})
        for pat in ('**/fonts.googleapis.com/**', '**/fonts.gstatic.com/**'): pg2.route(pat, lambda r: r.abort())
        pg2.goto(URL + '#frankfurt-kitchen'); pg2.wait_for_timeout(800); pg2.screenshot(path=f'{OUT}/v30-390.png')
        check(not errs, 'no page errors ' + ' | '.join(errs[:3]))
        b.close()
finally:
    srv.terminate()
print('RESULT:', 'PASS' if ok else 'FAIL')
