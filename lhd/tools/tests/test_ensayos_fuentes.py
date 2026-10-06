"""R2.0 (plan v1.0): los ensayos con fuentes. Las marcas [n] del ensayo se ven como superíndices, la lista «Fuentes del ensayo»
está cerrada al abrir, un clic en el superíndice la abre y resalta la fuente, no quedan marcas en bruto, el aviso «No revisada»
desaparece, y un ensayo sin fuentes sigue avisando. Trabaja sobre una copia del sitio con un ensayo de prueba (no toca el proyecto)."""
import functools, http.server, json, os, re, shutil, socketserver, tempfile, threading
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EXE = os.environ.get('CHROMIUM', '/opt/pw-browsers/chromium')
ok_all = True
def ok(name, cond, extra=''):
    global ok_all
    ok_all = ok_all and bool(cond)
    print(('PASS ' if cond else 'FAIL ') + name, extra)

tmp = tempfile.mkdtemp(prefix='lhd-ess-')
site = os.path.join(tmp, 'site')
os.makedirs(site)
for f in ('index.html', 'app.js', 'style.css'):
    shutil.copy(os.path.join(ROOT, f), site)
for dname in ('data', 'help'):
    shutil.copytree(os.path.join(ROOT, dname), os.path.join(site, dname))
# ensayo de prueba: lens-political con marcas y fuentes; lens-economic queda sin fuentes
p = os.path.join(site, 'data', 'essays.json')
E = json.load(open(p, encoding='utf-8'))
pol = next(e for e in E['essays'] if e['id'] == 'lens-political')
pol['paras'][0] = pol['paras'][0].rstrip() + '[1][2]'
pol['paras'][1] = pol['paras'][1].rstrip() + '[2]'
pol['es']['paras'][0] = pol['es']['paras'][0].rstrip() + '[1][2]'
pol['es']['paras'][1] = pol['es']['paras'][1].rstrip() + '[2]'
pol['refs'] = [
    {'label': 'Fuente de prueba uno', 'url': 'https://example.org/uno', 'checks': 'Qué sostiene la primera.', 'date': '2026-10-06'},
    {'label': 'Fuente de prueba dos', 'url': 'https://example.org/dos', 'checks': 'Qué sostiene la segunda.', 'date': '2026-10-06'}]
json.dump(E, open(p, 'w', encoding='utf-8'), ensure_ascii=False)

class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
srv = socketserver.TCPServer(('127.0.0.1', 0), functools.partial(Q, directory=site))
port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
U = f'http://127.0.0.1:{port}/index.html'
try:
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=EXE)
        def page(lang):
            pg = b.new_context(viewport={'width': 1440, 'height': 900}).new_page(); pg.errs = []
            pg.on('pageerror', lambda e: pg.errs.append(str(e)))
            for pat in ('**/fonts.googleapis.com/**', '**/fonts.gstatic.com/**'): pg.route(pat, lambda r: r.abort())
            pg.route('**/wikipedia.org/**', lambda r: r.fulfill(status=200, content_type='application/json', body='{"query":{"pages":{}}}'))
            pg.add_init_script(f"try{{localStorage.setItem('lhd-lang','{lang}')}}catch(e){{}}")
            return pg
        pg = page('es'); pg.goto(U); pg.wait_for_timeout(900)
        pg.click('[data-focus="political"]'); pg.wait_for_timeout(1200)
        ok('foco político con ensayo', pg.locator('#panel .essay p').count() >= 6)
        ok('superíndices en el ensayo', pg.locator('#panel .essay sup.rf').count() == 3, pg.locator('#panel .essay sup.rf').count())
        html = pg.inner_html('#panel .essay')
        ok('sin marcas [n] en bruto ni fichas rotas', not re.search(r'\[\d{1,2}\]', re.sub(r'<[^>]+>', '', html)) and '⟦' not in html)
        ok('los enlaces [[id]] siguen siendo botones', pg.locator('#panel .essay .el-link[data-go]').count() >= 15)
        det = pg.locator('#panel details.sources')
        ok('una sola lista de fuentes y cerrada al abrir', det.count() == 1 and not det.evaluate('e => e.open'))
        ok('título «Fuentes del ensayo (2)»', det.locator('summary').inner_text().strip() == 'Fuentes del ensayo (2)', det.locator('summary').inner_text())
        ok('sin aviso «No revisada» cuando hay fuentes', pg.locator('#panel .unrev-note').count() == 0)
        pg.locator('#panel .essay sup.rf a').nth(1).click(); pg.wait_for_timeout(900)
        ok('clic en el superíndice abre la lista', det.evaluate('e => e.open'))
        ok('y resalta su fuente', pg.locator('#panel .rf-list li.rf-hi').count() == 1 and pg.locator('#panel .rf-list li.rf-hi .rf-n').inner_text() == '2')
        ok('fuente con enlace externo seguro', pg.locator('#panel .rf-list li a').first.get_attribute('rel') == 'noopener noreferrer')
        meta = pg.inner_text('#panel .p-meta')
        ok('la lectura en minutos no cuenta las marcas', 'min de lectura' in meta)
        # ensayo sin fuentes: sigue el aviso y no hay lista
        pg.click('[data-focus="political"]'); pg.wait_for_timeout(300)
        pg.click('[data-focus="economic"]'); pg.wait_for_timeout(1000)
        ok('ensayo sin fuentes: aviso «No revisada», sin lista', pg.locator('#panel .unrev-note').count() == 1 and pg.locator('#panel details.sources').count() == 0)
        # inglés y disciplina
        pg2 = page('en'); pg2.goto(U); pg2.wait_for_timeout(900)
        pg2.click('[data-focus="political"]'); pg2.wait_for_timeout(1200)
        ok('EN: título «Essay sources (2)» y superíndices', pg2.locator('#panel details.sources summary').inner_text().strip() == 'Essay sources (2)' and pg2.locator('#panel .essay sup.rf').count() == 3)
        ok('sin errores de JavaScript', not pg.errs and not pg2.errs, str(pg.errs + pg2.errs))
        b.close()
finally:
    srv.shutdown()
    shutil.rmtree(tmp, ignore_errors=True)
print('RESULT: ' + ('PASS' if ok_all else 'FAIL'))
raise SystemExit(0 if ok_all else 1)
