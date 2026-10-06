# Recorte del Modernismo (propuesta para V1)
Lista que lee `tools/pipeline/recortar.py` (`RECORTE-MODERNISMO.json`). **No está aplicada**: se aplica en el paso 1.7, solo después del visto bueno V1.
Ensayo (`--prueba`): obras 139 → 121, diseñadores 73 → 65, hechos de contexto 46 → 43 (cifras que incluyen los elementos de prueba de otros tramos; en el Modernismo quedan 120 obras, 64 diseñadores y 39 hechos); sin huérfanos; build sin PROBLEM.
Ninguna obra ★, de América Latina, citada en conexiones/conceptos/macromovimiento ni única de un movimiento o institución. Reparto: gráfica 5, producto 5, arquitectura 5, moda 3. **V1 (punto 66):** se mantienen Stool 60, Maison du Peuple, camisa Lacoste, Jean Prouvé y René Lacoste; se repusieron con Letty Lynton (Adrian), EKCO AD65 (Wells Coates) y Zonnestraal para seguir en 18 / 8 / 3. Fuller/Dymaxion se descartó como reposición: Posguerra lo usa (cúpula geodésica, Expo 67).

## 18 obras

| id | obra | disciplina | año | motivo |
|---|---|---|---|---|
| `soaring-to-success` | Soaring to Success | graphic | 1918 | Cartel de McKnight Kauffer; otro cartel suyo (Power) queda; repetido en gráfica comercial. |
| `bauhaus-exhibition-poster` | Bauhaus exhibition poster | graphic | 1923 | Sin enlaces; la Bauhaus ya se explica con Bayer, Moholy-Nagy y las portadas. |
| `pro-eto` | Pro Eto | graphic | 1923 | Libro de Ródchenko/Lisitski sin enlaces; Lisitski y Ródchenko siguen con otras obras. |
| `universal-alphabet` | Universal alphabet | graphic | 1925 | Experimento de Bayer sin enlaces; Bayer queda con otras obras. |
| `intransigeant-poster` | L’Intransigeant poster | graphic | 1925 | Cassandre queda con Normandie y otras obras. |

| `faaborg-chair` | Faaborg chair | product | 1914 | Diseño escandinavo previo; 0 enlaces; el diseño escandinavo se cubre en Posguerra. |
| `anglepoise-lamp` | Anglepoise lamp | product | 1932 | Lámpara de oficina de un solo diseñador; Wagenfeld y Brandt cubren la lámpara. |
| `baby-brownie` | Baby Brownie | product | 1934 | Estilismo de cámara; Teague sin otra obra; el estilismo lo cubren Loewy y Bel Geddes. |
| `john-deere-model-a` | Styled John Deere Model B | product | 1938 | Estilismo de maquinaria agrícola; Dreyfuss queda con otras obras. |
| `maison-de-verre` | Maison de Verre | architecture | 1928 | Casa-vitrina, 0 enlaces; arquitectura moderna ya bien representada. |
| `villa-mairea` | Villa Mairea | architecture | 1938 | Casa de Aalto, 0 enlaces; Aalto queda con otras obras. |
| `co-op-interieur` | Co-op Interieur | architecture | 1926 | Instalación de Hannes Meyer; el diseñador queda con ADGB. |
| `karl-marx-hof` | Karl-Marx-Hof | architecture | 1927 | Vivienda social vienesa; el Nuevo Frankfurt cubre el tema. |
| `gres-draped-gowns` | Alix draped gown | fashion | 1937 | Moda de alta costura sin enlaces; la moda queda con Chanel, Vionnet y Schiaparelli. |
| `popover-dress` | Popover dress | fashion | 1942 | Moda funcional estadounidense con 0 enlaces. |
| `zonnestraal` | Zonnestraal Sanatorium | architecture | 1926 | Sanatorio con 1 enlace; ya hay arquitectura sanitaria y obrera en el tramo. |
| `ekco-ad65` | EKCO AD65 radio | product | 1932 | Radio de baquelita con 1 enlace; Wells Coates sin otra obra. |
| `letty-lynton-dress` | Letty Lynton dress | fashion | 1932 | Vestido de cine con 1 enlace; Adrian sin otra obra. |

## 8 diseñadores (quedan sin obras)

| id | nombre | motivo |
|---|---|---|
| `kaare-klint` | Kaare Klint | Solo su silla Faaborg (recortada). |
| `carwardine` | George Carwardine | Solo la lámpara Anglepoise. |
| `walter-dorwin-teague` | Walter Dorwin Teague | Solo Baby Brownie. |
| `chareau` | Pierre Chareau | Solo Maison de Verre. |
| `madame-gres` | Madame Grès | Solo los vestidos drapeados. |
| `claire-mccardell` | Claire McCardell | Solo el Popover dress. |
| `adrian` | Adrian | Solo el vestido Letty Lynton. |
| `wells-coates` | Wells Coates | Solo la radio EKCO AD65. |

## 3 hechos de contexto

| id | nombre | motivo |
|---|---|---|
| `ctx-automatic-telephone` | Automatic telephone | 1 enlace; efecto menor en el diseño de la época. |
| `ctx-jazz-age` | Jazz Age | Redundante con ocio, cine sonoro y art déco. |
| `ctx-metropolitan-life` | Metropolitan life | Se solapa con ocio y metros; sus obras tienen otros contextos. |

Lo recortado se guarda en `tools/RESERVA-FASE-B.json` (clave `recorte_modernismo`) para recuperarlo en la fase B.
