import threading, functools, http.server, socketserver, json
from playwright.sync_api import sync_playwright
import os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))   # the lhd folder
OUT = os.path.join(os.environ.get('LHD_SHOTS', '/tmp'), 'lhd-shots'); os.makedirs(OUT, exist_ok=True)
EXE = os.environ.get('CHROMIUM', '/opt/pw-browsers/chromium')
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
srv = socketserver.TCPServer(('127.0.0.1', 0), functools.partial(Q, directory=ROOT)); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
U = f'http://127.0.0.1:{port}/index.html'
ok = lambda name, cond, extra='': print(('PASS ' if cond else 'FAIL ') + name, extra)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=EXE)
    def page(lang='es', theme='light', w=1440, h=900):
        ctx = b.new_context(viewport={'width': w, 'height': h}, color_scheme=theme)
        pg = ctx.new_page(); pg.errs = []
        pg.on('pageerror', lambda e: pg.errs.append(str(e)))
        for pat in ('**/fonts.googleapis.com/**', '**/fonts.gstatic.com/**'): pg.route(pat, lambda r: r.abort())
        pg.route('**/en.wikipedia.org/**', lambda r: r.fulfill(status=200, content_type='application/json', body='{"query":{"pages":{}}}'))
        pg.add_init_script(f"try{{localStorage.clear();localStorage.setItem('lhd-lang','{lang}');localStorage.setItem('lhd-theme','{theme}')}}catch(e){{}}")
        return pg
    pg = page(); pg.goto(U); pg.wait_for_timeout(800)
    # 23
    sb = lambda s: pg.locator(f'[data-secall^="{s}:"]')
    ok('23 one arrow per section', sb('ctx').count() == 1 and sb('des').count() == 1)
    ok('23 ctx starts folded (v24) -> open arrow', sb('ctx').get_attribute('data-secall') == 'ctx:open' and pg.locator('#labelsInner [data-k^="trk:"][aria-expanded="true"]').count() == 0)
    pg.evaluate("document.querySelector('[data-secall^=\"ctx:\"]').click()"); pg.wait_for_timeout(150)
    ok('23 ctx opened -> close arrow', sb('ctx').get_attribute('data-secall') == 'ctx:close' and pg.locator('#labelsInner [data-k^="trk:"][aria-expanded="false"]').count() == 0)
    pg.evaluate("document.querySelector('[data-secall^=\"ctx:\"]').click()"); pg.wait_for_timeout(150)
    ok('23 ctx folded again', sb('ctx').get_attribute('data-secall') == 'ctx:open')
    pg.evaluate("document.querySelector('[data-secall^=\"ctx:\"]').click()"); pg.wait_for_timeout(150)
    ok('23 ctx reopened', sb('ctx').get_attribute('data-secall') == 'ctx:close' and pg.locator('#labelsInner [data-k^="trk:"][aria-expanded="false"]').count() == 0)
    pg.evaluate("document.querySelector('[data-secall^=\"des:\"]').click()"); pg.wait_for_timeout(150)
    ok('23 des folded', sb('des').get_attribute('data-secall') == 'des:open')
    pg.evaluate("document.querySelector('[data-secall^=\"des:\"]').click()"); pg.wait_for_timeout(150)
    ok('23 des reopened', sb('des').get_attribute('data-secall') == 'des:close')
    # 24
    ax = pg.locator('#axisClip').bounding_box()
    pg.mouse.move(ax['x'] + 300, ax['y'] + 30); pg.mouse.down(); pg.mouse.move(ax['x'] + 500, ax['y'] + 30, steps=5)
    vs = pg.evaluate("(() => { const v = document.getElementById('vsel'); const r = v.getBoundingClientRect(); return {hidden: v.hidden, h: r.height, x: r.left}; })()")
    ok('24 shade down the line', not vs['hidden'] and vs['h'] > 500 and abs(vs['x'] - (ax['x'] + 300)) < 3, json.dumps(vs))
    pg.screenshot(path=f'{OUT}/v19_drag.png')
    pg.mouse.up(); pg.wait_for_timeout(200)
    ok('24 shade gone + zoomed', pg.evaluate("document.getElementById('vsel').hidden && LHD.state.zoomed"))
    # 25
    ok('25 whole-line enabled when zoomed', not pg.locator('#zoomFit').is_disabled())
    pg.click('#zoomFit'); pg.wait_for_timeout(200)
    ok('25 whole line -> disabled', pg.locator('#zoomFit').is_disabled())
    ok('25 fit enabled w/o filter (content is narrower than the whole line)', not pg.locator('#zoomVis').is_disabled())
    pg.evaluate("LHD.go('bauhaus-movement')"); pg.wait_for_timeout(200); pg.click('#isoBtn'); pg.wait_for_timeout(200)
    ok('25 fit enabled with Only', not pg.locator('#zoomVis').is_disabled())
    pg.click('#zoomVis'); pg.wait_for_timeout(300)
    r = pg.evaluate("[document.getElementById('yFrom').value, document.getElementById('yTo').value]")
    ok('25 fit applied, then disabled', pg.locator('#zoomVis').is_disabled(), json.dumps(r))
    pg.screenshot(path=f'{OUT}/v19_fit_iso.png')
    # 30
    bg = pg.evaluate("getComputedStyle(document.querySelector('.chip.iso')).backgroundColor")
    ok('30 Only chip dark', bg in ('rgb(23, 25, 30)',), bg)
    pg.click('.chip.iso'); pg.wait_for_timeout(200)
    # 26/27
    pg.click('#zoomFit'); pg.wait_for_timeout(200)
    st = pg.evaluate("(() => { const b = document.querySelector('.it.designer[data-id=\"breuer\"] .bar') || document.querySelector('.it.designer .bar'); return b ? getComputedStyle(b).backgroundImage + ' | ' + getComputedStyle(b).backgroundColor : 'none'; })()")
    ok('26 designer bar coloured', 'rgba(' in st and '128, 128' not in st, st[:160])
    pg.evaluate("LHD.select('frankfurt-kitchen')"); pg.wait_for_timeout(300)
    cols = pg.evaluate("[...new Set([...document.querySelectorAll('#curves path[stroke]')].map(p => p.getAttribute('stroke')))]")
    ok('27 curves coloured', any('--c-architecture' in c or '--c-product' in c or '--c-graphic' in c for c in cols) or len(cols) > 1, json.dumps(cols))
    rl = pg.evaluate("(() => { const e = document.querySelector('#content .it.rel[data-t] .t'); return e ? getComputedStyle(e).color : null; })()")
    ok('27 related fact text in row colour', rl and rl != 'rgb(23, 25, 30)', str(rl))
    pg.screenshot(path=f'{OUT}/v19_sel.png')
    # 28/29
    txt = pg.locator('#filters').inner_text()
    ok('28 scale names', 'Visual' in txt and 'Cronológica' in txt and 'densidad' not in txt)
    ok('29 no colons', 'Foco:' not in txt and 'Organizar:' not in txt, txt[:80].replace('\n', ' '))
    print('page errors:', pg.errs or 'none')
    pg2 = page('en', 'dark'); pg2.goto(U + '#breuer'); pg2.wait_for_timeout(800)
    pg2.click('#isoBtn'); pg2.wait_for_timeout(200)
    pg2.screenshot(path=f'{OUT}/v19_dark.png')
    t2 = pg2.locator('#filters').inner_text()
    ok('EN names', 'Chronological' in t2 and 'Lens:' not in t2)
    print('page errors 2:', pg2.errs or 'none')
    b.close()
srv.shutdown()
