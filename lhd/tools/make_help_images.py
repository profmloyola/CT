#!/usr/bin/env python3
"""Regenerates help/overview-es.webp and help/overview-en.webp (screenshot with numbered callouts).
Run it again whenever the interface or the content of the pilot era changes noticeably:
    python3 tools/make_help_images.py [work-id]
Needs: playwright (with Chromium) and Pillow. It starts its own local server; fonts load from Google if online."""
import http.server, socketserver, threading, os, sys, io, functools
from playwright.sync_api import sync_playwright
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'help')
WORK = sys.argv[1] if len(sys.argv) > 1 else 'frankfurt-kitchen'
os.makedirs(OUT, exist_ok=True)

class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
handler = functools.partial(Quiet, directory=ROOT)
srv = socketserver.TCPServer(('127.0.0.1', 0), handler); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()

# where each numbered callout goes: (selector, anchor) -> circle centre computed in the page
JS = """
(workId) => {
  const R = (sel) => document.querySelector(sel).getBoundingClientRect();
  const pts = [];
  const s = R('#q'); pts.push([s.left - 26, s.top + s.height / 2]);
  const f = R('#filters'); pts.push([f.right - 30, f.top + 58]);
  const a = R('.axis-clip'); pts.push([a.right - 16, a.top + a.height / 2]);
  const z = R('#axisCorner'); pts.push([z.right - 4, z.top + 6]);
  const l = document.querySelector('#labelsInner .lens-row .lname').getBoundingClientRect(); pts.push([l.right + 12, l.top + l.height / 2]);
  const p = R('#panel'); pts.push([p.left, p.top + p.height * 0.42]);
  pts.forEach(([x, y], i) => {
    const d = document.createElement('div');
    d.textContent = String(i + 1);
    d.style.cssText = `position:fixed;z-index:9999;left:${x - 12}px;top:${y - 12}px;width:24px;height:24px;border-radius:50%;background:#17191E;color:#fff;font:700 13px/24px system-ui,sans-serif;text-align:center;box-shadow:0 0 0 2px #fff,0 2px 6px rgba(0,0,0,.3)`;
    document.body.appendChild(d);
  });
}
"""

with sync_playwright() as p:
    exe = os.environ.get('CHROMIUM', '/opt/pw-browsers/chromium')
    b = p.chromium.launch(executable_path=exe) if os.path.exists(exe) else p.chromium.launch()
    for lang in ('es', 'en'):
        ctx = b.new_context(viewport={'width': 1440, 'height': 900}, device_scale_factor=1.25, color_scheme='light')
        pg = ctx.new_page()
        pg.route('**/en.wikipedia.org/**', lambda r: r.abort())
        pg.add_init_script(f"try{{localStorage.setItem('lhd-lang','{lang}');localStorage.setItem('lhd-theme','light')}}catch(e){{}}")
        pg.goto(f'http://127.0.0.1:{port}/index.html#{WORK}')
        pg.wait_for_timeout(400); pg.evaluate("(w) => { LHD.setEraView('modernism'); LHD.select(w); document.getElementById('viewport').scrollTop = 0; }", WORK)
        pg.wait_for_selector('#labelsInner [data-k]'); pg.wait_for_timeout(500)
        pg.mouse.move(5, 5); pg.wait_for_timeout(300)
        pg.evaluate(JS, WORK); pg.wait_for_timeout(100)
        png = pg.screenshot()
        im = Image.open(io.BytesIO(png)).convert('RGB')
        im.save(os.path.join(OUT, f'overview-{lang}.webp'), 'WEBP', quality=82, method=6)
        print('ok', lang, im.size)
        ctx.close()
    b.close()
srv.shutdown()
