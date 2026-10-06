#!/usr/bin/env python3
"""Correcciones puntuales posteriores a apply_new (etapa 6): enlaces de teorías, kinds, autores, fechas."""
import json, glob
def walk():
    for f in glob.glob('src-data/*/*.json'):
        d = json.load(open(f, encoding='utf-8'))
        key = next((k for k, v in d.items() if isinstance(v, list)), None) if isinstance(d, dict) else None
        yield f, d, (d[key] if key else d)
TH = {
 'th-laugier-essai-1753': {'movements': ['neoclassicism'], 'designers': ['soufflot']},
 'th-winckelmann-history-1764': {'movements': ['neoclassicism']},
 'th-ruskin-seven-lamps-1849': {'movements': ['arts-and-crafts'], 'designers': ['pugin']},
 'th-garden-cities-of-tomorrow': {'movements': ['garden-city-movement'], 'designers': ['raymond-unwin']},
 'th-veblen-leisure-class': {'designers': ['charles-frederick-worth']},
 'th-work-of-art-mechanical': {'movements': ['new-vision']},
 'th-theory-design-machine-age': {'movements': ['international-style']},
 'th-death-life-great-american-cities': {'movements': ['new-urbanism']},
 'th-complexity-contradiction': {'designers': ['robert-venturi'], 'movements': ['postmodern-architecture']},
 'th-barthes-fashion-system': {'designers': ['christian-dior'], 'institutions': ['inst-vogue']},
}
KIND = {'publisher': 'publication', 'firm': 'studio', 'award': 'association', 'society': 'association'}
MAKER = {
 'paisley-shawl-1820': 'Paisley weavers, Scotland', 'caras-y-caretas-1898': 'Caras y Caretas magazine, Buenos Aires',
 'crinoline-cage-1856': 'Crinoline manufacturers', 'shirtwaist-blouse-1895': 'Ready-to-wear blouse makers, USA',
 'kahlo-tehuana-1930': 'Frida Kahlo', 'miranda-baiana-1939': 'Carmen Miranda and Hollywood and Rio costume makers',
 'zoot-suit-1940': 'Harlem and Los Angeles tailors and wearers', 'recycling-symbol-1970': 'Gary Anderson',
 'nasa-worm-logo-1975': 'Danne & Blackburn', 'museo-memoria-santiago-2010': 'Estudio América',
 'jatiya-sangsad-dhaka-1982': 'Louis Kahn (completed by his office)'}
DROP = {'recycling-symbol-1970': ['gary-anderson'], 'nasa-worm-logo-1975': ['danne-blackburn'],
        'museo-memoria-santiago-2010': ['estudio-america'], 'jatiya-sangsad-dhaka-1982': ['louis-kahn']}
YEAR = {'pantheon-paris-1790': 1764, 'la-moneda-1805': 1784}
DKIND = {'sanaa': 'collective', 'pezo-von-ellrichshausen': 'collective', 'beggarstaffs': 'collective',
         'bresciani-valdes-castillo-huidobro': 'collective'}
for f, d, lst in walk():
    ch = False
    for r in lst:
        if not isinstance(r, dict): continue
        i = r.get('id')
        if i in TH:
            L = r.setdefault('links', {'movements': [], 'institutions': [], 'designers': [], 'works': []})
            for k, v in TH[i].items():
                L.setdefault(k, [])
                for x in v:
                    if x not in L[k]: L[k].append(x); ch = True
        if r.get('kind') in KIND and f.endswith('03-institutions.json'): r['kind'] = KIND[r['kind']]; ch = True
        if i in DKIND and f.endswith('10-designers.json'): r['kind'] = DKIND[i]; ch = True
        if i in MAKER and 'designers' in r:
            if i in DROP: r['designers'] = [x for x in r['designers'] if x not in DROP[i]]
            r['maker'] = MAKER[i]; ch = True
        if i in YEAR: r['year'] = YEAR[i]; ch = True
    if ch:
        json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1); print('fix', f)
