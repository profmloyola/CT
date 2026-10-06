# 8.5b: image gallery (1 image, several, movement gallery, credit visible, no image, 390 px viewport)
import threading, functools, http.server, socketserver, json, os, base64
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EXE = os.environ.get('CHROMIUM', '/opt/pw-browsers/chromium')
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
srv = socketserver.TCPServer(('127.0.0.1', 0), functools.partial(Q, directory=ROOT)); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
U = f'http://127.0.0.1:{port}/index.html'
ok = lambda name, cond, extra='': print(('PASS ' if cond else 'FAIL ') + name, extra)
PNG = base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==')
d = json.load(open(os.path.join(ROOT, 'data', 'all.json')))
withimg = [w for w in d['works'] if w.get('images')]
noimg = [w for w in d['works'] if not w.get('images') and not w.get('wiki')]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=EXE)
    def page(w=1440, lang='es'):
        ctx = b.new_context(viewport={'width': w, 'height': 900}); pg = ctx.new_page(); pg.errs = []
        pg.on('pageerror', lambda e: pg.errs.append(str(e)))
        for pat in ('**/fonts.googleapis.com/**', '**/fonts.gstatic.com/**'): pg.route(pat, lambda r: r.abort())
        pg.route('**/wikipedia.org/**', lambda r: r.fulfill(status=200, content_type='application/json', body='{"query":{"pages":{}}}'))
        pg.route('**/commons.wikimedia.org/**', lambda r: r.fulfill(status=200, content_type='image/png', body=PNG))
        pg.add_init_script(f"try{{localStorage.setItem('lhd-lang','{lang}')}}catch(e){{}}")
        return pg
    pg = page(); pg.goto(U); pg.wait_for_timeout(900)
    ok('data has images', len(withimg) > 400, str(len(withimg)))
    w = withimg[0]
    pg.evaluate(f"LHD.select('{w['id']}', {{reveal:false}})"); pg.wait_for_timeout(400)
    ok('work: 1 image linked to its source, no caption', pg.locator('#panel .p-img.gal.one img').count() == 1 and pg.locator('#panel .p-img figcaption').count() == 0 and 'commons.wikimedia.org/wiki/File:' in pg.locator('#panel .p-img.gal.one a').first.get_attribute('href'))
    ok('licence goes to the Imagen line in Fuentes', pg.locator('#panel .rf-imgs li').count() >= 1)
    # movement gallery
    mv = [m for m in d['movements'] if not m.get('macro')]
    got = None
    for m in mv:
        pg.evaluate(f"LHD.select('{m['id']}', {{reveal:false}})")
        if pg.locator('#panel .gal-track .gal-s').count() >= 2: got = m['id']; break
    ok('movement gallery 2-4 slides + dots', got is not None and pg.locator('#panel .gal-dot').count() == pg.locator('#panel .gal-s').count() <= 4, str(got))
    if got:
        pg.locator('#panel .gal-dot').nth(1).click(); pg.wait_for_timeout(700)
        ok('dot moves carousel', pg.locator('#panel .gal-dot.on').get_attribute('data-gi') == '1')
        pg.locator('#panel .gal').focus(); pg.keyboard.press('ArrowLeft'); pg.wait_for_timeout(700)
        ok('arrow key moves carousel', pg.locator('#panel .gal-dot.on').get_attribute('data-gi') == '0')
        ok('slide caption links to work', pg.locator('#panel .gal-s .pchip-lnk[data-go]').count() >= 2)
    macros = [m for m in d['movements'] if m.get('macro')]
    gm = 0
    for m in macros:
        pg.evaluate(f"LHD.select('{m['id']}', {{reveal:false}})")
        if pg.locator('#panel .gal-s').count() >= 2: gm += 1
    ok('macro movements with gallery', gm >= 1, f'{gm}/{len(macros)}')
    # designer without portrait shows a work
    des = [a for a in d['designers'] if a.get('images')]
    pg.evaluate(f"LHD.select('{des[0]['id']}', {{reveal:false}})")
    ok('designer with image', pg.locator('#panel .p-img img').count() >= 1)
    # theory cover
    th = [x for x in d['theories'] if x.get('images')]
    pg.evaluate(f"LHD.select('{th[0]['id']}', {{reveal:false}})")
    ok('theory cover', pg.locator('#panel .p-img img').count() == 1)
    # no image: no errors, no box
    if noimg:
        pg.evaluate(f"LHD.select('{noimg[0]['id']}', {{reveal:false}})"); pg.wait_for_timeout(300)
        ok('no image: no box', pg.locator('#panel .p-img').count() == 0)
    ok('no JS errors', not pg.errs, str(pg.errs[:2]))
    # 390 px
    pm = page(390, 'en'); pm.goto(U); pm.wait_for_timeout(900)
    pm.evaluate(f"LHD.select('{withimg[0]['id']}', {{reveal:false}})"); pm.wait_for_timeout(400)
    ok('mobile: no horizontal overflow', pm.evaluate("document.documentElement.scrollWidth <= 400"))
    ok('mobile EN: image is a link, no caption', pm.locator('#panel .p-img a img').count() >= 1 and pm.locator('#panel .p-img figcaption').count() == 0)
    ok('mobile no JS errors', not pm.errs, str(pm.errs[:2]))
