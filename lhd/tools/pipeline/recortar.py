#!/usr/bin/env python3
"""Aplica el recorte del Modernismo (plan 3.0 y paso 0.7b).

Uso: python3 tools/pipeline/recortar.py <lista.json> [--prueba] [--base DIR]
  lista.json = {"works": [ids], "designers": [ids], "contexts": [ids]}   (la que escribe la etapa 1, paso 1.6: tools/RECORTE-MODERNISMO.json)
  --base DIR carpeta del proyecto alternativa (pruebas con una copia)
  --prueba   trabaja sobre una COPIA de src-data en un directorio temporal: no toca el proyecto ni la reserva; muestra lo que haría.

Se NIEGA (sin tocar nada) si:
  - una obra, un diseñador o un hecho de contexto está protegido (3.0: obra ★, citada en una conexión / concepto / macromovimiento, de
    América Latina o única de un movimiento o institución; diseñador ★; hecho de contexto citado en el macromovimiento);
  - un diseñador de la lista tiene una obra que se queda;
  - tras el recorte quedan ids huérfanos o el build da PROBLEM (se prueba antes en la copia).
Al aplicar: quita los registros, sus enlaces de contexto, sus conexiones y sus ids en `links` de otros elementos; guarda lo quitado en
tools/RESERVA-FASE-B.json (clave recorte_modernismo) y corre el build.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import recorte_lib as R


def build_in(project_dir):
    out = subprocess.run([sys.executable, os.path.join(project_dir, 'tools', 'build_data.py')], capture_output=True, text=True)
    lines = (out.stdout + out.stderr).splitlines()
    return [l for l in lines if l.startswith('PROBLEM')], lines[-1] if lines else ''


def plan_cut(m, sel):
    """Valida la lista contra las protecciones. -> lista de errores (vacía si se puede)."""
    pw, pd_, pc = R.protections(m)
    works = {x['id']: x for x in m.items('works')}
    designers = {x['id']: x for x in m.items('designers')}
    contexts = {x['id']: x for x in m.items('contexts')}
    cw, cd, cc = set(sel.get('works', [])), set(sel.get('designers', [])), set(sel.get('contexts', []))
    errs = []
    for i in sorted(cw):
        if i not in works: errs.append(f'obra {i}: no existe')
        elif i in pw: errs.append(f'obra {i}: PROTEGIDA ({"; ".join(pw[i])})')
        elif works[i].get('level') != 'normal': errs.append(f'obra {i}: no es Normal')
    for i in sorted(cd):
        if i not in designers: errs.append(f'diseñador {i}: no existe')
        elif i in pd_: errs.append(f'diseñador {i}: PROTEGIDO ({"; ".join(pd_[i])})')
        else:
            keep = [w['id'] for w in works.values() if i in (w.get('designers') or []) and w['id'] not in cw]
            if keep: errs.append(f'diseñador {i}: tiene obras que se quedan ({", ".join(keep)})')
    for i in sorted(cc):
        if i not in contexts: errs.append(f'contexto {i}: no existe')
        elif i in pc: errs.append(f'contexto {i}: PROTEGIDO ({"; ".join(pc[i])})')
    # lo que quedaría sin nada: diseñadores sin obra y hechos de contexto sin enlaces
    for did, d in designers.items():
        if did in cd: continue
        mine = [w['id'] for w in works.values() if did in (w.get('designers') or [])]
        if mine and all(i in cw for i in mine):
            errs.append(f'diseñador {did}: se quedaría sin obras; agrégalo a "designers" (si no es ★) o conserva alguna de sus obras ({", ".join(mine)})')
    gone = cw | cd | cc
    by_ctx = {}
    for l in m.items('links'):
        by_ctx.setdefault(l['ctx'], []).append(l['item'])
    for cid, items in by_ctx.items():
        if cid in cc or cid not in contexts: continue
        if items and all(i in gone for i in items):
            errs.append(f'contexto {cid}: se quedaría sin enlaces (todos van a lo recortado); agrégalo a "contexts" o conserva alguno')
    return errs


def cut(m, sel):
    """Aplica el recorte en memoria. -> dict de lo quitado."""
    cw, cd, cc = set(sel.get('works', [])), set(sel.get('designers', [])), set(sel.get('contexts', []))
    gone = cw | cd | cc
    saved = {'works': [], 'designers': [], 'contexts': [], 'links': [], 'connections': [], 'ids_in_links': []}
    for key, S, bucket in (('works', cw, 'works'), ('designers', cd, 'designers'), ('contexts', cc, 'contexts')):
        for f, d in m.files.items():
            keep = []
            for x in d.get(key, []) or []:
                (saved[bucket] if x.get('id') in S else keep).append(x)
            if key in d: d[key] = keep
    for f, d in m.files.items():
        if 'links' in d and isinstance(d['links'], list) and d['links'] and 'ctx' in d['links'][0]:
            keep = []
            for l in d['links']:
                (saved['links'] if l['ctx'] in gone or l['item'] in gone else keep).append(l)
            d['links'] = keep
        if 'connections' in d:
            keep = []
            for c in d['connections']:
                (saved['connections'] if c['from'] in gone or c['to'] in gone else keep).append(c)
            d['connections'] = keep
        for key in R.KEYS:
            for x in d.get(key, []) or []:
                lk = x.get('links')
                if isinstance(lk, dict):
                    for fld in ('works', 'designers', 'movements', 'institutions'):
                        if fld in lk:
                            rm = [i for i in lk[fld] if i in gone]
                            if rm:
                                saved['ids_in_links'].append({'owner': x['id'], 'field': fld, 'ids': rm})
                                lk[fld] = [i for i in lk[fld] if i not in gone]
    return saved


def main(argv):
    test = '--prueba' in argv
    if '--base' in argv:   # carpeta del proyecto alternativa (solo para pruebas con una copia)
        R.BASE = os.path.abspath(argv[argv.index('--base') + 1])
        argv = [a for i, a in enumerate(argv) if a != '--base' and (i == 0 or argv[i - 1] != '--base')]
    args = [a for a in argv if not a.startswith('--')]
    if len(args) != 1:
        print(__doc__); return 2
    sel = json.load(open(args[0], encoding='utf-8'))
    m = R.Model()
    errs = plan_cut(m, sel)
    if errs:
        print('NO SE APLICÓ NADA. Motivos:')
        for e in errs: print('  ' + e)
        return 1
    n_before = {k: len(list(m.items(k))) for k in ('works', 'designers', 'contexts')}
    # 1. ensayo en una copia del proyecto (src-data + build_data.py)
    tmp = tempfile.mkdtemp()
    os.makedirs(os.path.join(tmp, 'tools'))
    shutil.copy(os.path.join(R.BASE, 'tools', 'build_data.py'), os.path.join(tmp, 'tools'))
    shutil.copytree(os.path.join(R.BASE, 'src-data'), os.path.join(tmp, 'src-data'))
    trial = R.Model(os.path.join(tmp, 'src-data'))
    saved = cut(trial, sel)
    orph = R.orphans(trial)
    trial.save()
    probs, last = build_in(tmp)
    if orph or probs:
        print('NO SE APLICÓ NADA. El recorte dejaría problemas:')
        for o in orph: print('  huérfano: ' + o)
        for p in probs[:15]: print('  ' + p)
        shutil.rmtree(tmp); return 1
    n_after = {k: len(list(trial.items(k))) for k in ('works', 'designers', 'contexts')}
    print(f"{'PRUEBA' if test else 'RECORTE'}: obras {n_before['works']} -> {n_after['works']}, diseñadores {n_before['designers']} -> {n_after['designers']}, "
          f"hechos de contexto {n_before['contexts']} -> {n_after['contexts']}; enlaces quitados {len(saved['links'])}, conexiones {len(saved['connections'])}, "
          f"ids quitados de `links` {sum(len(x['ids']) for x in saved['ids_in_links'])}; sin huérfanos; build: {last}")
    shutil.rmtree(tmp)
    if test:
        return 0
    # 2. aplicar de verdad
    saved = cut(m, sel)
    m.save()
    rp = os.path.join(R.BASE, 'tools', 'RESERVA-FASE-B.json')
    res = json.load(open(rp, encoding='utf-8'))
    bucket = res.setdefault('recorte_modernismo', {})
    for k, v in saved.items():
        bucket.setdefault(k, []).extend(v)
    with open(rp, 'w', encoding='utf-8') as fh:
        json.dump(res, fh, ensure_ascii=False, indent=1); fh.write('\n')
    probs, last = build_in(R.BASE)
    print('build real:', last)
    return 1 if probs else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
