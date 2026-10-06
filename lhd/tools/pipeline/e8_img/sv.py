#!/usr/bin/env python3
"""sv.py NNN  < lines 'id¦file¦license¦artist'  -> res/NNN.json (formato de las tandas: {"picked":[[id,file,lic,artist]]})"""
import sys,json,os
n=sys.argv[1]; rows=[l.rstrip('\n').split('¦') for l in sys.stdin if l.strip()]
bad=[r for r in rows if len(r)!=4]; assert not bad,bad
p=os.path.join(os.path.dirname(os.path.abspath(__file__)),'res',f'{n}.json')
old=json.load(open(p))['picked'] if os.path.exists(p) else []
d={r[0]:r for r in old}; d.update({r[0]:r for r in rows})
json.dump({'picked':list(d.values())},open(p,'w'),ensure_ascii=False)
print(n,len(d),'picks')
