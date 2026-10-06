# Stage 8: scope by discipline, essays on focus/discipline cards, header warning, unified filter bar
import threading, functools, http.server, socketserver, json, os
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EXE = os.environ.get('CHROMIUM', '/opt/pw-browsers/chromium')
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
srv = socketserver.TCPServer(('127.0.0.1', 0), functools.partial(Q, directory=ROOT)); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
U = f'http://127.0.0.1:{port}/index.html'
ok = lambda name, cond, extra='': print(('PASS ' if cond else 'FAIL ') + name, extra)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=EXE)
    def page(lang='es', theme='light'):
        ctx = b.new_context(viewport={'width': 1440, 'height': 900}, color_scheme=theme)
        pg = ctx.new_page(); pg.errs = []
        pg.on('pageerror', lambda e: pg.errs.append(str(e)))
        for pat in ('**/fonts.googleapis.com/**', '**/fonts.gstatic.com/**'): pg.route(pat, lambda r: r.abort())
        pg.route('**/wikipedia.org/**', lambda r: r.fulfill(status=200, content_type='application/json', body='{"query":{"pages":{}}}'))
        pg.add_init_script(f"try{{localStorage.setItem('lhd-lang','{lang}');localStorage.setItem('lhd-theme','{theme}')}}catch(e){{}}")
        return pg
    pg = page(); pg.goto(U); pg.wait_for_timeout(900)
    # filter bar order: Foco | Disciplinas | Conexiones | Detalle
    order = pg.evaluate("[...document.querySelectorAll('#filters .frow:first-child > *')].map(e => e.className.includes('lens-l') ? 'L:' + e.textContent : e.className.includes('conn') ? 'CONN' : '').filter(Boolean)")
    ok('bar order', order == ['L:Foco', 'L:Disciplinas', 'CONN', 'L:Detalle'], str(order))
    ok('scope chips share the style', pg.locator('#filters .chip.scope').count() == 10)
    pg.evaluate("LHD.state.info && document.getElementById('infoBtn').click()"); pg.wait_for_timeout(200)
    # scope: one at a time, only works of the discipline
    pg.click('[data-disc="fashion"]'); pg.wait_for_timeout(900)
    r = pg.evaluate("""(() => { const S = LHD.state, d = S.data;
      const ids = [...document.querySelectorAll('#content .it.work')].map(e => e.dataset.id);
      return { scope: S.scope, n: ids.length, bad: ids.filter(i => d.works.find(w => w.id === i).discipline !== 'fashion'), disc: [...S.disc] }; })()""")
    ok('scope fashion: only fashion works', r['scope'] == 'fashion' and r['n'] > 0 and not r['bad'] and r['disc'] == ['fashion'], json.dumps(r))
    ok('discipline card with essay', 'DISCIPLINA' in pg.inner_text('#panel .kicker').upper() and pg.locator('#panel .essay p').count() >= 8)
    ok('essay links are buttons with data-go', pg.locator('#panel .essay .el-link[data-go]').count() >= 15)
    ok('meta line', 'min de lectura' in pg.inner_text('#panel .p-meta') and 'obras' in pg.inner_text('#panel .p-meta'))
    ok('essay not reviewed warning', pg.locator('#panel .unrev-note').count() == 1)
    ctxn = pg.evaluate("document.querySelectorAll('#content .it.context').length")
    pg.click('[data-disc="graphic"]'); pg.wait_for_timeout(500)
    ok('switching scope: one at a time', pg.evaluate("LHD.state.scope") == 'graphic' and pg.locator('#filters .chip.disc[aria-pressed="true"]').count() == 1)
    # essay link opens a card and keeps the scope
    first = pg.locator('#panel .essay .el-link').first.get_attribute('data-go')
    pg.locator('#panel .essay .el-link').first.click(); pg.wait_for_timeout(500)
    ok('opening a card keeps the scope', pg.evaluate("LHD.state.scope") == 'graphic' and pg.evaluate("LHD.state.sel") == first)
    # focus combined with scope: the card shows the last one turned on
    pg.click('[data-focus="political"]'); pg.wait_for_timeout(800)
    ok('focus + scope together', pg.evaluate("LHD.state.scope === 'graphic' && LHD.state.focus === 'political'") and 'FOCO' in pg.inner_text('#panel .kicker').upper())
    ok('lens essay', pg.locator('#panel .essay p').count() >= 6)
    pg.click('[data-disc="graphic"]'); pg.wait_for_timeout(500)
    ok('scope off keeps focus', pg.evaluate("LHD.state.scope === null && LHD.state.focus === 'political'"))
    pg.click('[data-focus="political"]'); pg.wait_for_timeout(500)
    ok('everything off: all disciplines', pg.evaluate("LHD.state.scope === null && LHD.state.focus === null && LHD.state.disc.size === 4"))
    # EN
    pg2 = page('en', 'dark'); pg2.goto(U); pg2.wait_for_timeout(900)
    pg2.evaluate("LHD.setScope('architecture')"); pg2.wait_for_timeout(900)
    ok('EN essay', 'DISCIPLINE' in pg2.inner_text('#panel .kicker').upper() and 'min read' in pg2.inner_text('#panel .p-meta'))
    # header warning on element cards without sources
    r = pg.evaluate("""(() => { const d = LHD.state.data; const ids = d.works.map(w => w.id); const out = {};
      for (const id of ids.slice(0, 400)) { LHD.select(id, {reveal: false}); const has = !!document.querySelector('#panel .p-head .unrev-note'); const src = document.querySelector('#panel details.sources'); const unrev = src && src.classList.contains('unrev'); if (has !== !!unrev) return {bad: id, has, unrev}; }
      return {bad: null}; })()""")
    ok('header warning matches the Sources section', r['bad'] is None, json.dumps(r))
    ok('no page errors', not pg.errs and not pg2.errs, str(pg.errs + pg2.errs))
    b.close()
