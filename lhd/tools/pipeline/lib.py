import json,glob,os,datetime
BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))   # carpeta del proyecto
ROOT=BASE+'/src-data'
D=datetime.date.today().isoformat()
_cache={}
def _files():
    return sorted(glob.glob(ROOT+'/*/*.json'))
def _load(p):
    if p not in _cache: _cache[p]=json.load(open(p,encoding='utf-8'))
    return _cache[p]
def get(i):
    for p in _files():
        d=_load(p)
        for k,v in d.items():
            if isinstance(v,list):
                for x in v:
                    if isinstance(x,dict) and x.get('id')==i: return x
    raise KeyError(i)
def R(label,url,checks):
    return {'label':label,'checks':checks,'date':D,'url':url}
def rep(i,field,old,new,lang='en'):
    x=get(i); t=x if lang=='en' else x['es']
    assert old in t[field], (i,field,lang,old,t[field])
    t[field]=t[field].replace(old,new)
def setf(i,field,en=None,es=None):
    x=get(i)
    if en is not None: x[field]=en
    if es is not None: x.setdefault('es',{})[field]=es
def LP(): return ROOT+'/modernism/80-context-links.json'
def link(ctx,item):
    for l in _load(LP())['links']:
        if l['ctx']==ctx and l['item']==item: return l
    raise KeyError((ctx,item))
def setlink(ctx,item,en,es,refs=None,newctx=None):
    l=link(ctx,item); l['note']=en; l['es']['note']=es
    if refs is not None: l['refs']=refs
    if newctx: l['ctx']=newctx
RESERVE=[]
def droplink(ctx,item,why):
    d=_load(LP()); l=link(ctx,item); d['links'].remove(l); l['_motivo']=why; RESERVE.append(l)
def addlink(ctx,item,en,es,refs):
    d=_load(LP())
    assert not any(l['ctx']==ctx and l['item']==item for l in d['links']),(ctx,item)
    d['links'].append({'ctx':ctx,'item':item,'note':en,'es':{'note':es},'refs':refs})
def save():
    for p,d in _cache.items():
        with open(p,'w',encoding='utf-8') as f:
            json.dump(d,f,ensure_ascii=False,indent=1); f.write('\n')
    rp=BASE+'/tools/RESERVA-FASE-B.json'
    r=json.load(open(rp,encoding='utf-8'))
    r.setdefault('suspended_links',[]).extend(RESERVE)
    r['note_v22']='suspended_links: enlaces suspendidos en v22 por la revisión independiente (sin fuente suficiente). Recuperar solo con fuente.'
    with open(rp,'w',encoding='utf-8') as f:
        json.dump(r,f,ensure_ascii=False,indent=1); f.write('\n')
