# Auditoría LHD (R1.1)
Datos: data/all.json generado el 2026-10-05.
## 1. Elementos por tramo
| tramo | obras | ★ | diseñ. | mov. | inst. | teor. | ctx | prod. | conc. |
|---|---|---|---|---|---|---|---|---|---|
| industrial 1750–1850 | 53 | 14 | 34 | 9 | 12 | 10 | 27 | 10 | 0 |
| reform 1851–1913 | 99 | 33 | 59 | 14 | 15 | 14 | 37 | 11 | 0 |
| modernism 1914–1944 | 172 | 47 | 89 | 16 | 24 | 21 | 43 | 16 | 8 |
| postwar 1945–1974 | 166 | 51 | 103 | 21 | 31 | 32 | 43 | 16 | 0 |
| postmodern 1975–hoy | 162 | 39 | 100 | 20 | 18 | 23 | 44 | 15 | 0 |
| TOTAL | 652 | 184 | 385 | 80 | 100 | 100 | 194 | 68 | 8 |

## 2. Obras por disciplina y región (una obra puede tener varias regiones)
| tramo | graphic | product | fashion | architecture | europe | north-america | latin-america | global |
|---|---|---|---|---|---|---|---|---|
| industrial | 17 | 13 | 7 | 16 | 45 | 3 | 4 | 2 |
| reform | 26 | 23 | 14 | 36 | 70 | 24 | 6 | 0 |
| modernism | 47 | 47 | 31 | 47 | 132 | 28 | 14 | 0 |
| postwar | 38 | 54 | 23 | 51 | 81 | 47 | 33 | 8 |
| postmodern | 43 | 36 | 24 | 59 | 66 | 59 | 16 | 41 |
| TOTAL | 171 | 173 | 99 | 209 | 394 | 161 | 73 | 51 |

América Latina: 73 de 652 obras (11.2 %).  ★: 184 (28.2 %).
## 3. Fuentes (refs)
| tipo | con fuentes | total | % | ★ con fuentes | ★ total |
|---|---|---|---|---|---|
| work | 127 | 652 | 19 | 41 | 184 |
| designer | 70 | 385 | 18 | 29 | 102 |
| movement | 12 | 80 | 15 | 8 | 35 |
| institution | 16 | 100 | 16 | 4 | 22 |
| theory | 14 | 100 | 14 | 3 | 31 |
| context | 42 | 194 | 22 | 0 | 0 |
| production | 16 | 68 | 24 | 0 | 0 |
| concept | 8 | 8 | 100 | 0 | 0 |

Enlaces de contexto con fuentes: 241 de 1310.  Conexiones con fuentes: 23 de 114.
## 4. Contexto de obras y diseñadores (C4b)
| tramo | directo | solo indirecto | ninguno |
|---|---|---|---|
| industrial | 53 | 0 | 0 |
| reform | 97 | 1 | 1 |
| modernism | 142 | 26 | 4 |
| postwar | 152 | 7 | 7 |
| postmodern | 158 | 2 | 2 |
| TOTAL obras | 602 | 36 | 14 |
| TOTAL diseñadores | 128 | 243 | 14 |

Enlaces por tipo: 1310 de contexto → diseño; 114 conexiones.
Contextos según su número de enlaces: 1: 14, 2: 23, 3: 28, 4: 18, 5: 18, 6: 11, 7: 16, 8: 9, 9: 7, 10: 12, 11: 8, 12: 6, 13: 5, 14: 8, 15: 1, 16: 3, 17: 1, 19: 1, 20: 2, 31: 1, 32: 2
Elementos sin enlace propio por tipo: work 1, movement 2
## 5. Hallazgos
| gravedad | categoría | casos |
|---|---|---|
| ERROR | elemento totalmente desconectado | 1 |
| META | contexto con 1 solo enlace (meta: ≥ 2) | 14 |
| META | diseñador sin contexto (ni directo ni por sus obras) | 14 |
| META | movement sin enlace propio (solo lo citan otros) | 2 |
| META | obra sin ningún contexto (ni directo ni indirecto) | 14 |
| META | obra ★ sin 2 enlaces directos de subcategorías distintas (excepción C4c a anotar) | 41 |
| AVISO | diseñadores sin imagen (ver audit/INFORME-IMAGENES.md) | 1 |
| AVISO | fuente sin citar en el texto | 1 |
| AVISO | instituciones sin imagen (ver audit/INFORME-IMAGENES.md) | 1 |
| AVISO | key largo | 10 |
| AVISO | obras sin imagen (ver audit/INFORME-IMAGENES.md) | 1 |
| AVISO | teoría sin fuente https (pasa a ERROR cuando R3 termine las teorías, R1.2) | 86 |
| AVISO | teorías sin imagen (ver audit/INFORME-IMAGENES.md) | 1 |

TOTAL: 0 ERROR sin anotar · 1 ERROR anotados · 85 META · 101 AVISO

### ERROR: elemento totalmente desconectado (1)
- `levis-riveted-jeans` · work [anotada]

### META: contexto con 1 solo enlace (meta: ≥ 2) (14)
- `ctx-penny-post` · 1 enlace(s) [anotada]
- `ctx-registered-designs` · 1 enlace(s) [anotada]
- `ctx-luddism` · 1 enlace(s) [anotada]
- `ctx-latam-centenaries-1910` · 1 enlace(s)
- `ctx-snapshot-photography` · 1 enlace(s) [anotada]
- `ctx-planned-obsolescence` · 1 enlace(s) [anotada]
- `ctx-corfo` · 1 enlace(s) [anotada]
- `ctx-early-television` · 1 enlace(s) [anotada]
- `ctx-marshall-plan` · 1 enlace(s) [anotada]
- `ctx-suez-crisis-1956` · 1 enlace(s) [anotada]
- `ctx-crisis-2008` · 1 enlace(s) [anotada]
- `ctx-platform-economy` · 1 enlace(s) [anotada]
- `ctx-aids-crisis` · 1 enlace(s) [anotada]
- `ctx-digital-music` · 1 enlace(s) [anotada]

### META: diseñador sin contexto (ni directo ni por sus obras) (14)
- `erich-mendelsohn` · modernism
- `kaare-klint` · modernism [anotada]
- `chareau` · modernism [anotada]
- `alvin-lustig` · modernism
- `jean-prouve` · modernism [anotada]
- `aloisio-magalhaes` · postwar [anotada]
- `clorindo-testa` · postwar
- `hubert-de-givenchy` · postwar
- `zuzu-angel` · postwar
- `armin-hofmann` · postwar
- `ron-arad` · postmodern [anotada]
- `paulo-mendes-da-rocha` · postmodern [anotada]
- `smiljan-radic` · postmodern [anotada]
- `naoto-fukasawa` · postmodern [anotada]

### META: movement sin enlace propio (solo lo citan otros) (2)
- `critical-speculative-design` · [anotada]
- `sustainable-design` · [anotada]

### META: obra sin ningún contexto (ni directo ni indirecto) (14)
- `levis-riveted-jeans` · reform [anotada]
- `times-new-roman` · modernism [anotada]
- `bar-sous-le-toit` · modernism [anotada]
- `faaborg-chair` · modernism [anotada]
- `maison-de-verre` · modernism [anotada]
- `vertigo-titles` · postwar [anotada]
- `iv-centenario-rio-symbol` · postwar [anotada]
- `beethoven-poster-1955` · postwar [anotada]
- `giselle-poster-1959` · postwar [anotada]
- `givenchy-breakfast-1961` · postwar [anotada]
- `zuzu-angel-collection-1971` · postwar [anotada]
- `banco-de-londres-1966` · postwar [anotada]
- `well-tempered-chair-1986` · postmodern [anotada]
- `mestizo-restaurant-2007` · postmodern [anotada]

### META: obra ★ sin 2 enlaces directos de subcategorías distintas (excepción C4c a anotar) (41)
- `cenotaph-newton-1784` · 1 enlace(s), subcategorías: cultural [anotada]
- `akzidenz-grotesk-1896` · 1 enlace(s), subcategorías: economic [anotada]
- `priester-matches-1905` · 1 enlace(s), subcategorías: economic [anotada]
- `poiret-high-waist` · 1 enlace(s), subcategorías: social [anotada]
- `fagus-factory` · 1 enlace(s), subcategorías: economic [anotada]
- `looshaus` · 1 enlace(s), subcategorías: cultural [anotada]
- `wainwright-building-1891` · 1 enlace(s), subcategorías: economic [anotada]
- `johnston-typeface` · 1 enlace(s), subcategorías: technological [anotada]
- `books-poster` · 1 enlace(s), subcategorías: economic [anotada]
- `normandie-poster` · 1 enlace(s), subcategorías: social [anotada]
- `tube-map-1933` · 1 enlace(s), subcategorías: technological [anotada]
- `zang-tumb-tuuum-1914` · 1 enlace(s), subcategorías: cultural [anotada]
- `merz-magazine-1923` · 1 enlace(s), subcategorías: cultural [anotada]
- `red-blue-chair` · 1 enlace(s), subcategorías: cultural [anotada]
- `coca-cola-bottle` · 1 enlace(s), subcategorías: economic [anotada]
- `barcelona-chair` · 1 enlace(s), subcategorías: political [anotada]
- `paimio-chair` · 1 enlace(s), subcategorías: social [anotada]
- `moka-express` · 0 enlace(s), subcategorías: — [anotada]
- `bkf-chair` · 1 enlace(s), subcategorías: political [anotada]
- `vionnet-bias-dress` · 1 enlace(s), subcategorías: social [anotada]
- `lobster-dress` · 2 enlace(s), subcategorías: cultural [anotada]
- `nylon-stockings` · 1 enlace(s), subcategorías: economic [anotada]
- `casa-del-fascio-como` · 1 enlace(s), subcategorías: political [anotada]
- `fallingwater-1937` · 1 enlace(s), subcategorías: social [anotada]
- `beethoven-poster-1955` · 0 enlace(s), subcategorías: — [anotada]
- `citroen-2cv-1948` · 1 enlace(s), subcategorías: economic [anotada]
- `balenciaga-sack-dress` · 1 enlace(s), subcategorías: economic [anotada]
- `ronchamp-chapel` · 1 enlace(s), subcategorías: political [anotada]
- `seagram-building` · 1 enlace(s), subcategorías: economic [anotada]
- `chandigarh-1951` · 1 enlace(s), subcategorías: political [anotada]
- `guggenheim-new-york-1959` · 0 enlace(s), subcategorías: — [anotada]
- `salk-institute-1965` · 0 enlace(s), subcategorías: — [anotada]
- `ciudad-abierta-1970` · 1 enlace(s), subcategorías: social [anotada]
- `sydney-opera-house-1973` · 1 enlace(s), subcategorías: technological [anotada]
- `farnsworth-house-1951` · 0 enlace(s), subcategorías: — [anotada]
- `carlton-bookcase-1981` · 2 enlace(s), subcategorías: cultural [anotada]
- `westwood-punk-1976` · 2 enlace(s), subcategorías: cultural [anotada]
- `portland-building-1982` · 2 enlace(s), subcategorías: cultural [anotada]
- `seattle-library-2004` · 1 enlace(s), subcategorías: cultural [anotada]
- `church-of-the-light-1989` · 1 enlace(s), subcategorías: economic [anotada]
- `gando-school-2001` · 1 enlace(s), subcategorías: social [anotada]

### AVISO: diseñadores sin imagen (ver audit/INFORME-IMAGENES.md) (1)
- `22 de 385`

### AVISO: fuente sin citar en el texto (1)
- `streamlining` · refs[2]

### AVISO: instituciones sin imagen (ver audit/INFORME-IMAGENES.md) (1)
- `13 de 100`

### AVISO: key largo (10)
- `functionalism` · en: 270 caracteres
- `functionalism` · es: 269 caracteres
- `gesamtkunstwerk` · en: 263 caracteres
- `gesamtkunstwerk` · es: 289 caracteres
- `streamlining` · en: 239 caracteres
- `streamlining` · es: 252 caracteres
- `corporate-identity` · en: 337 caracteres
- `corporate-identity` · es: 372 caracteres
- `minimum-dwelling` · en: 310 caracteres
- `minimum-dwelling` · es: 347 caracteres

### AVISO: obras sin imagen (ver audit/INFORME-IMAGENES.md) (1)
- `90 de 652`

### AVISO: teoría sin fuente https (pasa a ERROR cuando R3 termine las teorías, R1.2) (86)
- `th-chippendale-director`
- `th-hepplewhite-guide`
- `th-sheraton-drawing-book`
- `th-pugin-true-principles`
- `th-journal-of-design`
- `th-laugier-essai-1753`
- `th-winckelmann-history-1764`
- `th-ruskin-seven-lamps-1849`
- `th-smith-wealth-of-nations-1776`
- `th-pugin-contrasts-1836`
- `th-grammar-of-ornament`
- `th-nature-of-gothic`
- `th-dresser-principles`
- `th-sullivan-function`
- `th-loos-ornament-and-crime`
- `th-semper-der-stil`
- `th-viollet-le-duc-entretiens`
- `th-moderne-architektur`
- `th-garden-cities-of-tomorrow`
- `th-veblen-leisure-class`
- `th-futurist-manifesto`
- `th-morris-hopes-fears-1882`
- `th-wright-art-craft-machine-1901`
- `th-simmel-fashion-1904`
- `th-flugel-psychology-clothes`
- `th-work-of-art-mechanical`
- `th-charter-of-athens`
- `th-werkbund-debate`
- `th-sant-elia-manifesto-1914`
- `th-international-style-1932`
- `th-kepes-language-of-vision-1944`
- `th-rand-thoughts-on-design`
- `th-gute-form`
- `th-designing-for-people`
- `th-hidden-persuaders`
- `th-waste-makers`
- `th-neue-grafik`
- `th-first-things-first`
- `th-notes-synthesis-form`
- `th-understanding-media`
- `th-design-for-the-real-world`
- `th-learning-from-las-vegas`
- `th-never-leave-well-enough-alone`
- `th-new-brutalism-banham`
- `th-measure-of-man-1960`
- `th-metabolism-1960`
- `th-theory-design-machine-age`
- `th-death-life-great-american-cities`
- `th-architecture-without-architects`
- `th-complexity-contradiction`
- `th-architettura-della-citta`
- `th-barthes-fashion-system`
- `th-life-between-buildings`
- `th-giedion-mechanization-1948`
- `th-barthes-mythologies-1957`
- `th-lynch-image-city-1960`
- `th-albers-interaction-color-1963`
- `th-munari-arte-come-mestiere-1966`
- `th-ruder-typographie-1967`
- `th-simon-sciences-artificial-1969`
- `th-maldonado-speranza-1970`
- `th-rittel-webber-1973`
- `th-mari-autoprogettazione-1974`
- `th-rams-ten-principles`
- `th-grid-systems`
- `th-design-everyday-things`
- `th-incomplete-manifesto`
- `th-first-things-first-2000`
- `th-no-logo`
- `th-cradle-to-cradle`
- `th-design-thinking-brown`
- `th-speculative-everything`
- `th-language-postmodern-architecture`
- `th-pattern-language`
- `th-delirious-new-york`
- `th-visual-display-quantitative-information`
- `th-towards-critical-regionalism`
- `th-deconstructivist-architecture`
- `th-sml-xl`
- `th-charter-new-urbanism`
- `th-eyes-of-the-skin`
- `th-parametricism-manifesto`
- `th-bonsiepe-dependencia-1978`
- `th-hebdige-subculture-1979`
- `th-forty-objects-desire-1986`
- `th-brundtland-1987`

### AVISO: teorías sin imagen (ver audit/INFORME-IMAGENES.md) (1)
- `10 de 100`
