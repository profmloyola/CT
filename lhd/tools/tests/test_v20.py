import threading, functools, http.server, socketserver, json
from playwright.sync_api import sync_playwright
import os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))   # the lhd folder
OUT = os.path.join(os.environ.get('LHD_SHOTS', '/tmp'), 'lhd-shots'); os.makedirs(OUT, exist_ok=True)
EXE = os.environ.get('CHROMIUM', '/opt/pw-browsers/chromium')
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
srv=socketserver.TCPServer(('127.0.0.1',0),functools.partial(Q,directory=ROOT)); port=srv.server_address[1]
threading.Thread(target=srv.serve_forever,daemon=True).start()
U=f'http://127.0.0.1:{port}/index.html'
ok=lambda n,c,e='': print(('PASS ' if c else 'FAIL ')+n, e)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=EXE)
    def page(lang='es',theme='light'):
        ctx=b.new_context(viewport={'width':1440,'height':900},color_scheme=theme); pg=ctx.new_page(); pg.errs=[]
        pg.on('pageerror',lambda e: pg.errs.append(str(e)))
        for pat in ('**/fonts.googleapis.com/**','**/fonts.gstatic.com/**'): pg.route(pat,lambda r:r.abort())
        pg.route('**/en.wikipedia.org/**', lambda r: r.fulfill(status=200, content_type='application/json', body='{"query":{"pages":{}}}'))
        pg.add_init_script(f"try{{localStorage.clear();localStorage.setItem('lhd-lang','{lang}');localStorage.setItem('lhd-theme','{theme}')}}catch(e){{}}")
        return pg
    pg=page(); pg.goto(U); pg.wait_for_timeout(900)
    ok('default level normal', pg.evaluate("LHD.state.level")=='normal' and pg.locator('[data-level=normal][aria-pressed=true]').count()==1)
    ok('no era bar', pg.locator('.it.era').count()==0)
    ok('macro in movements row (v24)', pg.locator('.it.movement[data-id="macro-modernism"]').count()==1)
    cnt=lambda: pg.evaluate("document.querySelectorAll('#content .it.work').length")
    n_norm=pg.evaluate("LHD.state.data.works.filter(w=>w.level!=='complete').length")
    pg.click('[data-level=essential]'); pg.wait_for_timeout(200)
    vis_e=pg.evaluate("[...document.querySelectorAll('#content .it.work')].map(e=>e.dataset.id).filter(id=>LHD.state.data.works.find(w=>w.id===id).level!=='essential').length")
    ok('essential hides others', vis_e==0)
    des_e=pg.evaluate("[...document.querySelectorAll('#content .it.designer')].map(e=>e.dataset.id).filter(id=>LHD.state.data.designers.find(w=>w.id===id).level!=='essential').length")
    ok('essential designers only', des_e==0)
    pg.evaluate("LHD.go('stool-60')"); pg.wait_for_timeout(400)
    ok('auto raise to normal (v24: two levels)', pg.evaluate("LHD.state.level")=='normal')
    ok('toast shown', pg.locator('#toast.on').count()==1, pg.locator('#toast').inner_text() if pg.locator('#toast').count() else '')
    pg.click('[data-level=normal]'); pg.wait_for_timeout(200)
    # macro card
    pg.evaluate("LHD.go('macro-modernism')"); pg.wait_for_timeout(400)
    txt=pg.locator('#panel').inner_text()
    ok('macro card', 'Macromovimiento' in txt.replace('MACROMOVIMIENTO','Macromovimiento') and 'factor por factor' in txt.lower(), txt[:120].replace('\n',' | '))
    pg.screenshot(path=OUT + '/v20_macro.png')
    # chanel indirect
    pg.evaluate("LHD.select('coco-chanel')"); pg.wait_for_timeout(300)
    rel=pg.evaluate("LHD.relations('coco-chanel').filter(r=>r.type==='ctx').map(r=>r.tone)")
    ok('chanel ctx tracks (v22: sound-film link moved to cinema)', set(rel)>={'political','social','cultural'}, json.dumps(sorted(set(rel))))
    pg.click('#isoBtn'); pg.wait_for_timeout(300)
    vis=pg.evaluate("['ctx-fashion-magazines','ctx-cinema','ctx-womens-vote-work'].map(id=>!!document.querySelector('#content .it[data-id=\"'+id+'\"]'))")
    ok('chanel Solo shows indirect ctx', all(vis), json.dumps(vis))
    thin=pg.evaluate("[...document.querySelectorAll('#curves path[stroke-width=\"0.8\"]')].length")
    ok('thin curves drawn', thin>0, str(thin))
    pg.screenshot(path=OUT + '/v20_chanel.png')
    pg.click('.chip.iso'); pg.wait_for_timeout(200)
    pg.evaluate("LHD.select('chanel-little-black-dress')"); pg.wait_for_timeout(300)
    ok('dress->art deco relation', pg.evaluate("LHD.relations('chanel-little-black-dress').some(r=>r.other==='art-deco')"))
    t2=pg.locator('#panel').inner_text()
    ok('no Buscar en / Donde verla', 'Buscar en' not in t2 and 'Dónde verla' not in t2 and 'Wikipedia' not in t2)
    ok('saber mas has where links', pg.locator('#panel ul.learn a').count()>=1)
    # info card
    pg.click('#infoBtn'); pg.wait_for_timeout(300)
    t3=pg.locator('#panel').inner_text()
    ok('info card new', 'Cómo usar la línea del tiempo' in t3 and 'proyecto en desarrollo' in t3 and 'Por época' not in t3)
    pg.screenshot(path=OUT + '/v20_info.png')
    pg.click('[data-help]'); pg.wait_for_timeout(300)
    ok('help opens from info', not pg.locator('#help').is_hidden())
    pg.keyboard.press('Escape')
    # lens card
    pg.evaluate("LHD.select(null); LHD.setFocus('economic')"); pg.wait_for_timeout(300)
    t4=pg.locator('#panel').inner_text()
    ok('lens by macro', 'por macromovimiento' in t4.lower() and 'modernismo' in t4.lower())
    pg.evaluate("LHD.setFocus('economic')"); pg.wait_for_timeout(200)
    pg.screenshot(path=OUT + '/v20_line.png')
    print('errors', pg.errs or 'none')
    pg2=page('en','dark'); pg2.goto(U+'#bauhaus-movement'); pg2.wait_for_timeout(800)
    pg2.screenshot(path=OUT + '/v20_dark.png'); print('errors2', pg2.errs or 'none')
    b.close()
srv.shutdown()
