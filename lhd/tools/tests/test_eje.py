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
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=EXE)
    pg=b.new_page(viewport={'width':1440,'height':900}); errs=[]
    pg.on('pageerror',lambda e: errs.append(str(e)))
    for pat in ('**/fonts.googleapis.com/**','**/fonts.gstatic.com/**'): pg.route(pat,lambda r:r.abort())
    pg.route('**/en.wikipedia.org/**',lambda r:r.fulfill(status=200,content_type='application/json',body='{"query":{"pages":{}}}'))
    pg.goto(f'http://127.0.0.1:{port}/index.html'); pg.wait_for_timeout(700)
    rng=lambda: [pg.input_value('#yFrom'), pg.input_value('#yTo')]
    print('start', rng(), 'fit disabled', pg.is_disabled('#zoomFit'))
    # drag on axis
    clip=pg.locator('#axisClip').bounding_box()
    y=clip['y']+28
    pg.mouse.move(clip['x']+380,y); pg.mouse.down(); pg.mouse.move(clip['x']+600,y,steps=5)
    print('sel visible', pg.is_visible('#axsel'), pg.inner_text('#axsel').replace('\n',' '))
    pg.mouse.up(); pg.wait_for_timeout(300); print('after drag', rng())
    # inputs
    pg.fill('#yFrom','1920'); pg.press('#yFrom','Tab'); pg.fill('#yTo','1930'); pg.press('#yTo','Enter'); pg.wait_for_timeout(300); print('typed 1920-1930 ->', rng(), '(a short span widens to the maximum zoom)')
    pg.fill('#yFrom','1960'); pg.press('#yFrom','Enter'); pg.wait_for_timeout(1200); pg.locator('body').click(position={'x': 5, 'y': 5}); pg.wait_for_timeout(200); print('bad input (from > to) keeps the range ->', rng())
    # edge left click
    pg.mouse.move(clip['x']+20,y); pg.wait_for_timeout(100)
    pg.click('#edgeL'); pg.wait_for_timeout(300); print('edge left ->', rng())
    # minimap: drag right bracket
    br=pg.locator('#tmapWin .br').bounding_box()
    pg.mouse.move(br['x']+2,br['y']+5); pg.mouse.down(); pg.mouse.move(br['x']+80,br['y']+5,steps=4); pg.mouse.up(); pg.wait_for_timeout(300); print('bracket ->', rng())
    w=pg.locator('#tmapWin').bounding_box()
    pg.mouse.move(w['x']+w['width']/2,w['y']+5); pg.mouse.down(); pg.mouse.move(w['x']+w['width']/2-60,w['y']+5,steps=4); pg.mouse.up(); pg.wait_for_timeout(300); print('pan ->', rng())
    pg.screenshot(path=f'{OUT}/u3.png')
    pg.click('#zoomFit'); pg.wait_for_timeout(300); print('all ->', rng())
    print('errors', errs or 'none')
    b.close()
srv.shutdown()
