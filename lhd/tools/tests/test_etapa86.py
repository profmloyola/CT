# Step 8.6: point 93 (designers with works inside a focus), point 94 (by discipline: four groups, designer copies),
# point 95 (minimal caption, image as a link, "Imagen:" line inside Fuentes)
import threading, functools, http.server, socketserver, json, os, re
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EXE = os.environ.get('CHROMIUM', '/opt/pw-browsers/chromium')
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
srv = socketserver.TCPServer(('127.0.0.1', 0), functools.partial(Q, directory=ROOT)); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
U = f'http://127.0.0.1:{port}/index.html'
ok = lambda name, cond, extra='': print(('PASS ' if cond else 'FAIL ') + name, extra)
D = json.load(open(os.path.join(ROOT, 'data/all.json')))
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=EXE)
    def page(theme='light', w=1440):
        ctx = b.new_context(viewport={'width': w, 'height': 900}, color_scheme=theme)
        pg = ctx.new_page(); pg.errs = []
        pg.on('pageerror', lambda e: pg.errs.append(str(e)))
        for pat in ('**/fonts.googleapis.com/**', '**/fonts.gstatic.com/**'): pg.route(pat, lambda r: r.abort())
        pg.route('**/wikipedia.org/**', lambda r: r.fulfill(status=200, content_type='application/json', body='{"query":{"pages":{}}}'))
        pg.route('**/commons.wikimedia.org/**', lambda r: r.abort())
        pg.add_init_script(f"try{{localStorage.setItem('lhd-lang','es');localStorage.setItem('lhd-theme','{theme}')}}catch(e){{}}")
        return pg
    pg = page(); pg.goto(U); pg.wait_for_timeout(900)
    pg.evaluate("LHD.state.info && document.getElementById('infoBtn').click()"); pg.wait_for_timeout(200)
    # ---- 93: focus Productivo
    pg.click('[data-focus="production"]'); pg.wait_for_timeout(1000)
    r = pg.evaluate("""(() => { const d = LHD.state.data;
      const dsIds = new Set([...document.querySelectorAll('#content .it.designer')].map(e => e.dataset.id));
      const works = [...document.querySelectorAll('#content .it.work')].map(e => d.works.find(w => w.id === e.dataset.id)).filter(Boolean);
      const orphan = works.filter(w => (w.designers || []).length && !(w.designers || []).some(x => dsIds.has(x)));
      return { ind: document.querySelectorAll('#content .it.designer.ind').length, ds: dsIds.size, works: works.length, orphan: orphan.map(w => w.id).slice(0, 5), nOrphan: orphan.length }; })()""")
    ok('93: with a focus, designers entering only through a work are drawn faint (.ind)', r['ind'] > 0 and r['ds'] > r['ind'], json.dumps(r))
    ok('93: no work is left without its designer line', r['works'] > 0 and r['nOrphan'] == 0, json.dumps(r))
    bar = pg.evaluate("(() => { const e = document.querySelector('#content .it.designer.ind .nm'); return e ? getComputedStyle(e).fontWeight : null })()")
    ok('93: faint designer has a normal-weight grey name', bar in ('400', 'normal'), str(bar))
    pg.click('[data-focus="production"]'); pg.wait_for_timeout(500)
    ok('93: focus off removes .ind', pg.locator('#content .it.designer.ind').count() == 0)
    # ---- 94: by discipline
    pg.click('[data-arrange="disc"]'); pg.wait_for_timeout(900)
    labs = pg.evaluate("[...document.querySelectorAll('#labelsInner .grp-label')].map(e => e.textContent.trim())")
    ok('94: exactly four discipline groups, no Interdisciplinario', len(labs) == 4 and not any('nterdisc' in x for x in labs), str(labs))
    r = pg.evaluate("""(() => { const m = {}; document.querySelectorAll('#content .it.designer').forEach(e => { m[e.dataset.id] = (m[e.dataset.id] || 0) + 1; });
      const dup = Object.keys(m).filter(k => m[k] > 1); return { dup: dup.length, ex: dup.slice(0, 3), total: Object.keys(m).length }; })()""")
    ok('94: a designer with works in several disciplines is drawn once per discipline', r['dup'] >= 5, json.dumps(r))
    r = pg.evaluate("""(() => { const d = LHD.state.data, bad = [];
      document.querySelectorAll('#content .it.designer').forEach(e => { /* every copy keeps all stripes: the bar style is set on the element */ if (!e.getAttribute('style') && !e.querySelector('.bar')) bad.push(e.dataset.id); });
      return bad.length; })()""")
    ok('94: copies keep their life line', r == 0)
    cnt = pg.evaluate("LHD.state.data.designers.length > 0")
    # selecting a duplicated designer highlights every copy
    dup = pg.evaluate("(() => { const m = {}; document.querySelectorAll('#content .it.designer').forEach(e => { m[e.dataset.id] = (m[e.dataset.id] || 0) + 1; }); return Object.keys(m).find(k => m[k] > 1); })()")
    pg.evaluate(f"LHD.select && LHD.select('{dup}')"); pg.wait_for_timeout(600)
    ok('94: selection marks every copy', pg.locator(f'#content .it.designer.sel[data-id="{dup}"]').count() >= 2, dup)
    pg.keyboard.press('Escape'); pg.wait_for_timeout(200)
    pg.click('[data-disc="fashion"]'); pg.wait_for_timeout(800)
    m = pg.evaluate("(() => { const m = {}; document.querySelectorAll('#content .it.designer').forEach(e => { m[e.dataset.id] = (m[e.dataset.id] || 0) + 1; }); return Object.values(m).filter(x => x > 1).length; })()")
    ok('94: with a discipline scope there is a single group and no copies', m == 0, str(m))
    pg.click('[data-disc="fashion"]'); pg.wait_for_timeout(300)
    pg.click('[data-arrange="chrono"]'); pg.wait_for_timeout(300)
    ok('94: no page errors', not pg.errs, ' | '.join(pg.errs[:3]))
    # ---- 95: images
    movs = [m['id'] for m in D['movements'] if not m.get('macro')][:80]
    seen_cap = 0; bad = []; marks = set()
    for mid in movs:
        pg.goto(U + '#' + mid); pg.wait_for_timeout(250)
        caps = pg.locator('#panel .gal-s figcaption').all_inner_texts()
        for c in caps:
            seen_cap += 1
            if re.search(r'Public|CC BY|CC0|Fuente|Source|Créditos|Credits', c): bad.append((mid, c))
            for mk in re.findall(r'\((?:C|CC)\)', c): marks.add(mk)
    ok('95: carousel captions say what the photo is, without licence texts', seen_cap > 20 and not bad, f'{seen_cap} captions; bad={bad[:2]}')
    ok('95: (C)/(CC) marks appear only as marks', marks <= {'(C)', '(CC)'} and len(marks) >= 1, str(marks))
    work = next(w['id'] for w in D['works'] if w.get('images') and not any(i.get('r') for i in w['images']))
    pg.goto(U + '#' + work); pg.wait_for_timeout(500)
    ok('95: single image: no caption', pg.locator('#panel .gal.one figcaption').count() == 0)
    ok('95: the image is a link to its source', pg.locator('#panel .gal.one a[target="_blank"] img').count() == 1 and 'Abrir la fuente' in (pg.locator('#panel .gal.one a').get_attribute('aria-label') or ''))
    pg.locator('#panel details.sources > summary').click(); pg.wait_for_timeout(150)
    order = pg.evaluate("(() => { const s = document.querySelector('#panel details.sources'); const k = [...s.children].map(e => e.className || e.tagName); return k; })()")
    ok('95: Fuentes starts with the "Imagen:" line, before the text sources', 'rf-imgs' in order and (('rf-list' not in order) or order.index('rf-imgs') < order.index('rf-list')), str(order))
    ok('95: the line says "Imagen:"', pg.locator('#panel .rf-imgs li').first.inner_text().startswith('Imagen'))
    pg.goto(U + '#frankfurt-kitchen'); pg.wait_for_timeout(500)
    pg.locator('#panel details.sources > summary').click(); pg.wait_for_timeout(150)
    order = pg.evaluate("[...document.querySelector('#panel details.sources').children].map(e => e.className || e.tagName)")
    ok('95: with text sources, the image line comes first', 'rf-imgs' in order and 'rf-list' in order and order.index('rf-imgs') < order.index('rf-list'), str(order))
    # a card with an image but no text sources keeps the warning
    found = None
    for w in D['works']:
        if not w.get('images'): continue
        pg.goto(U + '#' + w['id']); pg.wait_for_timeout(150)
        if pg.locator('#panel details.sources.unrev').count():
            found = w['id']; break
    ok('95: a card with only the image reference is still "No revisada"', found is not None and pg.locator('#panel .unrev-note').count() == 1 and pg.locator('#panel .rf-imgs li').count() >= 1, str(found))
    n = pg.evaluate("document.querySelector('#panel details.sources .rf-t').textContent")
    ok('95: the image line is not counted as a source', '(0)' in n, n)
    # a designer without a portrait that shows a work: no caption either
    pg.set_viewport_size({'width': 390, 'height': 800}); pg.goto(U + '#' + movs[0]); pg.wait_for_timeout(500)
    ok('95: 390 px: the panel does not overflow', pg.evaluate("(() => { const p = document.getElementById('panel'); return p.scrollWidth <= p.clientWidth + 1; })()"))
    ok('95: no page errors', not pg.errs, ' | '.join(pg.errs[:3]))
    # dark theme
    pgd = page('dark'); pgd.goto(U + '#' + work); pgd.wait_for_timeout(500)
    ok('95: dark theme renders the card', pgd.locator('#panel .gal.one').count() == 1 and not pgd.errs)
    b.close()
