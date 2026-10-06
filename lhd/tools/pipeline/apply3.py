# Agrega enlaces de contexto NUEVOS con refs (Parte II / A2). Uso: python3 tools/pipeline/apply3.py salida.json
import json,sys
from lib import *
from lib import _load
n=0
for fn in sys.argv[1:]:
    for e in json.load(open(fn)):
        if e.get('sin_enlace'): continue
        addlink(e['ctx'],e['item'],e['en']['note'],e['es']['note'],e['refs']); n+=1
save(); print('links added',n)
