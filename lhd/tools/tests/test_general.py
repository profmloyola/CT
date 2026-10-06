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
        pg.add_init_script(f"try{{localStorage.setItem('lhd-lang','{lang}');localStorage.setItem('lhd-theme','{theme}')}}catch(e){{}}")
        return pg
    pg = page()
    pg.goto(U); pg.wait_for_timeout(700)
    ok('info card on load', pg.locator('#panel .thesis').count() == 1)
    ok('macro drawn in the movements row (v24)', pg.locator('.it.movement[data-id="macro-modernism"]').count() == 1 and pg.locator('.it.macro').count() == 0)
    # search
    pg.fill('#q', 'barcelona'); pg.wait_for_timeout(200)
    ok('search results', pg.locator('#results button').count() > 0, pg.locator('#results button').first.inner_text().replace('\n', ' '))
    pg.press('#q', 'Enter'); pg.wait_for_timeout(400)
    ok('search opens card', 'Barcelona' in pg.locator('#panel .p-title').inner_text())
    ok('selected visible in line', pg.locator('#content .it.sel').count() >= 1)
    # long bar expand
    pg.evaluate("LHD.select('ctx-fordism')"); pg.wait_for_timeout(200)
    ok('long fact expands when selected', pg.locator('#content .it.expanded[data-id="ctx-fordism"]').count() == 1)
    pg.evaluate("LHD.select(null)"); pg.wait_for_timeout(200)
    ok('long fact shortened again', pg.locator('#content .it.lng[data-id="ctx-fordism"]').count() == 1)
    # discipline filter rule
    r = pg.evaluate("""(() => { document.querySelector('[data-disc=product]').click();
      const S = LHD.state; const ids = [...document.querySelectorAll('#content .it.work')].map(e => e.dataset.id);
      const d = S.data; const bad = ids.filter(id => d.works.find(w => w.id === id).discipline !== 'product');
      const des = [...document.querySelectorAll('#content .it.designer')].map(e => e.dataset.id);
      const wrong = des.filter(id => { const a = d.designers.find(x => x.id === id); const hasW = d.works.some(w => (w.designers||[]).includes(id) && w.discipline === 'product'); return !(a.disciplines.includes('product') || hasW); });
      return { works: ids.length, bad, designers: des.length, wrong }; })()""")
    ok('discipline filter (product only)', not r['bad'] and not r['wrong'], json.dumps(r))
    pg.evaluate("document.querySelector('[data-disc=product]').click();")   # stage 8: the scope goes off with a second click
    ok('scope off restores all disciplines', pg.evaluate("LHD.state.scope === null && LHD.state.disc.size === 4"))
    # focus + iso
    pg.evaluate("LHD.go('bauhaus-movement')"); pg.wait_for_timeout(200)
    pg.click('#isoBtn'); pg.wait_for_timeout(200)
    pg.evaluate("LHD.setFocus('economic')"); pg.wait_for_timeout(200)
    ok('iso chip + focus chip', pg.locator('.chip.iso').count() == 1 and pg.locator('.chip.lens[aria-pressed="true"]').count() == 1)
    ok('other context rows closed in focus', pg.locator('[data-k="trk:political"][aria-expanded="false"]').count() == 1 and pg.locator('[data-k="trk:economic"][aria-expanded="true"]').count() == 1)
    pg.screenshot(path=f'{OUT}/t_focus_iso.png')
    pg.click('.chip.lens[data-focus=economic]'); pg.wait_for_timeout(150); pg.click('.chip.iso'); pg.wait_for_timeout(150)
    ok('chips cleared', pg.locator('.chip.lens[aria-pressed="true"], .chip.iso').count() == 0)
    # connection toggles
    pg.evaluate("LHD.go('frankfurt-kitchen')"); pg.wait_for_timeout(200)
    n1 = pg.evaluate("LHD.state.curves.length")
    pg.click('[data-connall]'); pg.wait_for_timeout(150)
    n2 = pg.evaluate("LHD.state.curves.length")
    ok('context curves toggle', n1 > n2, f'{n1} -> {n2}')
    pg.click('[data-connall]'); pg.wait_for_timeout(150)
    # hover preview
    pg.evaluate("LHD.go('ctx-weimar-housing')"); pg.wait_for_timeout(200)   # the row opens (context starts collapsed since v25)
    pg.evaluate("LHD.select(null)"); pg.wait_for_timeout(150)
    el = pg.locator('#content .it[data-id="ctx-weimar-housing"]')
    el.scroll_into_view_if_needed(); el.hover(); pg.wait_for_timeout(150)
    ok('faint preview on hover', pg.evaluate("LHD.state.curves.length > 0 && LHD.state.curves.every(c => c.faint)"))
    # curve note tooltip
    pg.evaluate("LHD.select('ctx-weimar-housing')"); pg.wait_for_timeout(200)
    hit = pg.locator('#curves .hit').first
    box = pg.evaluate("(() => { const p = document.querySelector('#curves .hit'); const l = p.getTotalLength(); const pt = p.getPointAtLength(l * 0.5); const r = document.getElementById('curves').getBoundingClientRect(); return [r.left + pt.x, r.top + pt.y]; })()")
    pg.mouse.move(box[0], box[1]); pg.wait_for_timeout(150)
    ok('curve note on hover', len(pg.locator('#tip').inner_text().strip()) > 0, pg.locator('#tip').inner_text()[:90].replace('\n', ' | '))
    # era bar click and not-ready era
    pg.evaluate("LHD.go('macro-postmodernism')"); pg.wait_for_timeout(300)
    ok('postmodern macro card', 'Posmodernismo' in pg.locator('#panel .p-title').inner_text())  # v35: Posguerra ya tiene contenido; la ficha ya no trae el aviso de «en desarrollo»
    # scale switch keeps working
    pg.click('[data-scale=linear]'); pg.wait_for_timeout(200)
    ok('linear scale', pg.evaluate("LHD.state.scale") == 'linear' and pg.locator('.scm').count() == 0)
    pg.click('[data-scale=uneven]'); pg.wait_for_timeout(200)
    ok('uneven scale marks', pg.locator('.scm').count() > 0)
    # info card pivot -> era
    pg.click('#infoBtn'); pg.wait_for_timeout(200)
    ok('info card disclaimer', pg.locator('#panel .disclaimer').count() == 1)
    # collapse all / expand all
    pg.evaluate("document.querySelector('[data-secall=\"ctx:close\"]').click();"); pg.wait_for_timeout(150)
    ok('collapse all', pg.locator('#labelsInner [data-k^="trk:"][aria-expanded="true"], #labelsInner [data-k^="psub:"][aria-expanded="true"]').count() == 0)
    pg.evaluate("document.querySelector('[data-secall=\"ctx:open\"]').click();"); pg.wait_for_timeout(150)
    pg.evaluate("const b = document.querySelector('[data-secall=\"des:open\"]'); if (b) b.click();"); pg.wait_for_timeout(150)
    ok('expand all', pg.locator('#labelsInner [aria-expanded="false"]').count() == 0)
    # help
    pg.click('#helpBtn'); pg.wait_for_timeout(300)
    ok('help open', not pg.locator('#help').is_hidden() and pg.locator('.hparts li').count() == 6)
    pg.screenshot(path=f'{OUT}/t_help.png')
    pg.keyboard.press('Escape')
    print('page errors:', pg.errs or 'none')
    # hash load, dark, English
    pg2 = page('en', 'dark')
    pg2.goto(U + '#bauhaus-movement'); pg2.wait_for_timeout(800)
    ok('hash load (EN)', pg2.locator('#panel .p-title').inner_text() == 'Bauhaus', pg2.locator('#panel .kicker').inner_text())
    pg2.screenshot(path=f'{OUT}/t_dark_en.png')
    pg2.evaluate("LHD.setEraView('modernism')"); pg2.wait_for_timeout(300)
    pg2.screenshot(path=f'{OUT}/t_dark_era.png')
    print('page errors 2:', pg2.errs or 'none')
    # small screen
    pg3 = page(w=760, h=900); pg3.goto(U); pg3.wait_for_timeout(500)
    ok('mobile notice', pg3.locator('.mobile-notice').is_visible())
    pg3.screenshot(path=f'{OUT}/t_mobile.png')
    # light era view full
    pg4 = page(); pg4.goto(U); pg4.wait_for_timeout(600); pg4.evaluate("LHD.setEraView('modernism')"); pg4.wait_for_timeout(300)
    pg4.evaluate("document.getElementById('viewport').scrollTop = 1250"); pg4.wait_for_timeout(200)
    pg4.screenshot(path=f'{OUT}/t_design.png')
    b.close()
srv.shutdown()
