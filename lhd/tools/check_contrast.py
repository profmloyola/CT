"""Check WCAG contrast of the colour tokens in style.css (light and dark).
Text tokens (--t-*) must reach 4.5:1 on the surface and on the tinted context row; marker tokens (--c-*) 3:1."""
import re, sys, os
css = open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'style.css'), encoding='utf-8').read()

def blocks():
    light = re.search(r':root \{(.*?)\n\}', css, re.S).group(1)
    dark = re.search(r':root\[data-theme="dark"\] \{(.*?)\n\}', css, re.S).group(1)
    return light, dark
def tokens(block):
    d = {}
    for m in re.finditer(r'--([a-z0-9-]+):\s*([^;]+);', block):
        d[m.group(1)] = m.group(2).strip()
    return d
def hexrgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def trip(s): return tuple(int(x) for x in s.split(','))
def lum(c):
    def f(v):
        v /= 255; return v/12.92 if v <= 0.03928 else ((v+0.055)/1.055) ** 2.4
    r, g, b = map(f, c); return 0.2126*r + 0.7152*g + 0.0722*b
def cr(a, b):
    la, lb = lum(a), lum(b); hi, lo = max(la, lb), min(la, lb); return (hi+0.05)/(lo+0.05)
def mix(a, b, p): return tuple(round(a[i]*p + b[i]*(1-p)) for i in range(3))
light, dark = blocks()
Lt, Dt = tokens(light), dict(tokens(light)); Dt.update(tokens(dark))
bad = 0
for name, T in (('light', Lt), ('dark', Dt)):
    surface, lane, ctx = hexrgb(T['surface']), hexrgb(T['lane-a']), hexrgb(T['ctx-bg'])
    tint = int(T['tint'].rstrip('%')) / 100
    print(f'== {name}')
    for k in sorted(T):
        if k.startswith('t-'):
            col = hexrgb(T[k]); base = k[2:]
            row = mix(trip(T['c-' + base]), ctx, tint) if base in ('political','economic','social','cultural','technological','production','theory') else surface
            c1, c2 = cr(col, surface), cr(col, row)
            ok = c1 >= 4.5 and c2 >= 4.5; bad += not ok
            print(f"  text   {k:16} {T[k]}  on surface {c1:4.1f}  on row {c2:4.1f}  {'ok' if ok else 'LOW'}")
        if k.startswith('c-') and k[2:] != 'neutral':
            col = trip(T[k]); c1 = cr(col, lane); c2 = cr(col, ctx)
            ok = c1 >= 3 and c2 >= 3; bad += not ok
            print(f"  marker {k:16} rgb({T[k]})  on lane {c1:4.1f}  on ctx {c2:4.1f}  {'ok' if ok else 'LOW'}")
    for k in ('ink-2', 'muted'):
        c = cr(hexrgb(T[k]), surface); ok = c >= 4.5; bad += not ok
        print(f"  text   {k:16} {T[k]}  on surface {c:4.1f}  {'ok' if ok else 'LOW'}")
# v30: warning colour of the "Sources" section (text on --warn-bg and on the surface), 4.5:1
import re as _re
_css = css
_light = _re.search(r':root \{ --warn: (#[0-9A-Fa-f]{6}); --warn-bg: (#[0-9A-Fa-f]{6}); \}', _css)
_dark = _re.search(r':root\[data-theme="dark"\] \{ --warn: (#[0-9A-Fa-f]{6}); --warn-bg: (#[0-9A-Fa-f]{6}); \}', _css)
for _n, _m, _s in (('light', _light, Lt['surface']), ('dark', _dark, Dt['surface'])):
    _w, _b = hexrgb(_m.group(1)), hexrgb(_m.group(2))
    _c1, _c2 = cr(_w, hexrgb(_s)), cr(_w, _b)
    _ok = _c1 >= 4.5 and _c2 >= 4.5; bad += not _ok
    print(f"  warn {_n:5} {_m.group(1)} on surface {_c1:4.1f}  on warn-bg {_c2:4.1f}  {'ok' if _ok else 'LOW'}")

print('LOW values:', bad)
sys.exit(1 if bad else 0)
