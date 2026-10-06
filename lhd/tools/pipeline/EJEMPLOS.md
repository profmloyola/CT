# Ejemplos de registros (Parte I: sin fuentes)

*Generado por `python3 tools/pipeline/make_ejemplos.py` a partir de registros reales del Modernismo. Se muestran como se escribirá la Parte I: `refs: []`, sin marcas `[n]`, sin `where`, sin `wiki` y sin `sources`. Copia SUS campos, su orden y sus largos. Cada registro lleva `rtype` (el tipo de registro; en las obras `type` ya es el tipo de obra: chair, poster...).*

Reglas que no se ven en los ejemplos: ids en minúsculas con guiones y fijos (los da `LISTAS-CIERRE.md`); `level` solo `essential` o `normal`; `key` una frase (≤ 200 caracteres); `short` ≤ 22; nota de enlace ≤ 220 y explica el MECANISMO; español de Chile completo en `es`; sin citas textuales ni cifras dudosas.

## context · `ctx-fordism`

Hecho de contexto. `happened` cuenta qué pasó; `effect` explica el efecto sobre el diseño (el mecanismo). Va en `src-data/<tramo>/4x-context-<track>.json`.

```json
{
 "rtype": "context",
 "id": "ctx-fordism",
 "track": "economic",
 "start": 1914,
 "end": 1945,
 "cont": true,
 "date": "1914 →",
 "regions": [
  "north-america"
 ],
 "countries": [
  "US"
 ],
 "name": "Fordism",
 "short": "Fordism",
 "key": "Henry Ford’s model of a moving assembly line, standard products and high wages, which made mass production the model for the century.",
 "happened": "Ford introduced the moving assembly line at Highland Park in 1913 and the five-dollar day in January 1914. The price of the Model T fell from 850 dollars to as little as 260 over its production run, and more than 15 million were built between 1908 and 1927.",
 "effect": "Mass production became the declared model of modern design: Le Corbusier conceived his Citrohan house (1920–22) as a ‘machine for living in’ by analogy with industrial production, and named it after Citroën cars. In Germany, where Ford’s book appeared in translation in 1923, employers, unions and conservatives each found something to admire in Fordism, and the Nazi ‘people’s car’ project of the 1930s took Ford’s Dearborn factory and the Model T as its model.",
 "es": {
  "name": "Fordismo",
  "short": "Fordismo",
  "date": "1914 →",
  "key": "El modelo de Henry Ford de cadena de montaje móvil, productos estándar y salarios altos, que hizo de la producción en masa el modelo del siglo.",
  "happened": "Ford introdujo la cadena de montaje móvil en Highland Park en 1913 y el salario de cinco dólares diarios en enero de 1914. El precio del Model T bajó de 850 dólares a hasta 260 durante su producción, y entre 1908 y 1927 se fabricaron más de 15 millones.",
  "effect": "La producción en masa se volvió el modelo declarado del diseño moderno: Le Corbusier concibió su casa Citrohan (1920–22) como una «máquina de habitar», por analogía con la producción industrial, y la bautizó en homenaje a los autos Citroën. En Alemania, donde el libro de Ford apareció traducido en 1923, empresarios, sindicatos y conservadores encontraron cada uno algo que admirar en el fordismo, y el proyecto nazi del auto «del pueblo» de los años treinta tomó como modelo la fábrica de Dearborn y el Model T."
 },
 "refs": []
}
```

## production · `tubular-steel`

Productivo (material, proceso o herramienta). Necesita `links` a algún movimiento, institución, diseñador u obra. Va en `5x-production-*.json` según `sub`.

```json
{
 "rtype": "production",
 "id": "tubular-steel",
 "sub": "materials",
 "start": 1925,
 "end": 1945,
 "cont": true,
 "date": "1925 →",
 "regions": [
  "europe"
 ],
 "countries": [
  "DE"
 ],
 "name": "Tubular steel",
 "short": "Tubular steel",
 "key": "Bent steel tube, light, strong and plated with nickel or chrome, became the material of modern furniture from the mid-1920s.",
 "origin": "Seamless steel tube had been improved by the Mannesmann process of 1886, and tubular steel was already used in bicycle handlebars. At the Bauhaus in Dessau, Marcel Breuer made his first tubular-steel chair in 1925, inspired, by his own account, by the handlebars and frame of his Adler bicycle.",
 "enabled": "Thin, strong frames of bent tube, including chairs without back legs that rest on a cantilever, and frames bolted together from a few lengths of tube that could be taken apart. Standard-Möbel, founded in Berlin in 1926 to make them, aimed at series production, although in practice most tubular-steel chairs were still made by hand in small batches.",
 "change": "Furniture could now look light and open: Breuer argued that metal furniture belonged to a more modern room, one of airy elements that neither hinder movement nor the view through the room, and its smooth, cleanable surface fitted the ideas of hygiene of the time.",
 "economy": "Thonet, the great maker of bentwood chairs, signed with Breuer in 1928 and bought his firm Standard-Möbel in 1929; according to Thonet itself, it was the largest manufacturer of tubular-steel furniture in the world in the 1930s.",
 "relations": "The cantilever chair was developed by several designers at once: Mart Stam made a chair without back legs from ten pieces of gas pipe in 1926, Mies van der Rohe turned the idea into a curved, flexible model in Stuttgart in 1927, and Breuer designed his Cesca chair in 1928, in a race that the Design Museum says Stam won.",
 "links": {
  "movements": [
   "bauhaus-movement",
   "new-objectivity"
  ],
  "institutions": [
   "inst-bauhaus",
   "inst-weissenhof"
  ],
  "designers": [
   "breuer",
   "mies-van-der-rohe",
   "lilly-reich",
   "perriand",
   "eileen-gray"
  ],
  "works": [
   "wassily-chair",
   "mr10-chair",
   "cesca-chair",
   "lc4-chaise-longue",
   "e1027-table"
  ]
 },
 "es": {
  "name": "Tubo de acero",
  "short": "Tubo de acero",
  "date": "1925 →",
  "key": "El tubo de acero doblado, liviano, resistente y niquelado o cromado, se volvió el material del mueble moderno desde mediados de la década de 1920.",
  "origin": "El tubo de acero sin costura se había perfeccionado con el proceso Mannesmann de 1886, y el tubo de acero ya se usaba en los manubrios de bicicleta. En la Bauhaus de Dessau, Marcel Breuer hizo su primera silla de tubo de acero en 1925, inspirado, según él mismo, en el manubrio y el cuadro de su bicicleta Adler.",
  "enabled": "Estructuras delgadas y resistentes de tubo doblado, incluidas sillas sin patas traseras que se apoyan en voladizo, y armazones atornillados a partir de unos pocos tramos de tubo, que podían desarmarse. Standard-Möbel, fundada en Berlín en 1926 para fabricarlas, apuntaba a la producción en serie, aunque en la práctica la mayoría de las sillas de tubo de acero se seguían haciendo a mano, en tandas pequeñas.",
  "change": "El mueble pudo verse ahora liviano y abierto: Breuer sostenía que el mueble metálico pertenecía a una habitación más moderna, hecha de elementos aéreos que no estorban el movimiento ni la vista a través del espacio, y su superficie lisa y fácil de limpiar encajaba con las ideas de higiene de la época.",
  "economy": "Thonet, el gran fabricante de sillas de madera curvada, firmó con Breuer en 1928 y compró su empresa Standard-Möbel en 1929; según la propia Thonet, en los años treinta era el mayor fabricante de muebles de tubo de acero del mundo.",
  "relations": "La silla en voladizo la desarrollaron varios diseñadores a la vez: Mart Stam hizo en 1926 una silla sin patas traseras con diez piezas de tubo de gas, Mies van der Rohe convirtió la idea en un modelo curvo y flexible en Stuttgart en 1927, y Breuer diseñó su silla Cesca en 1928, en una carrera que, según el Design Museum, ganó Stam."
 },
 "refs": []
}
```

## theory · `th-vers-une-architecture`

Teoría (el id empieza con `th-`). `ideas` lleva 3 a 5 elementos y `short` es solo el apellido. En la Parte I no lleva `sources` (el build lo avisa como WARN; se agregan en la Parte II).

```json
{
 "rtype": "theory",
 "id": "th-vers-une-architecture",
 "level": "essential",
 "year": 1923,
 "date": "1923",
 "regions": [
  "europe"
 ],
 "countries": [
  "FR"
 ],
 "genre": "architecture",
 "author": "Le Corbusier",
 "name": "Towards an Architecture",
 "short": "Le Corbusier",
 "key": "Le Corbusier’s polemical book of 1923, which held up ships, aeroplanes and cars as models for a new architecture.",
 "ideas": [
  "The engineer’s aesthetic is in full bloom while architecture declines; the engineer, inspired by the law of economy and guided by calculation, works in accord with the laws of the universe.",
  "Architecture works with three elements, volume, surface and plan, ordered by regulating lines.",
  "The house should be mass-produced: ‘a machine for living in’.",
  "Ships, aeroplanes and cars show what industry achieves by selection and standards; the aeroplane is ‘a product of high selection’.",
  "The choice is ‘architecture or revolution’."
 ],
 "impact": "Gathered from the articles Le Corbusier signed in L’Esprit Nouveau, the review he founded with Amédée Ozenfant and Paul Dermée, it was published by Crès in Paris in 1923, in the collection ‘L’Esprit Nouveau’, and appeared in English in 1927. It met with ‘dazzling success’.",
 "links": {
  "movements": [
   "international-style"
  ],
  "institutions": [],
  "designers": [
   "le-corbusier"
  ],
  "works": [
   "esprit-nouveau-pavilion",
   "villa-savoye"
  ]
 },
 "es": {
  "author": "Le Corbusier",
  "name": "Hacia una arquitectura",
  "short": "Le Corbusier",
  "date": "1923",
  "key": "El libro polémico de Le Corbusier de 1923, que propuso barcos, aviones y autos como modelos de una nueva arquitectura.",
  "ideas": [
   "La estética del ingeniero está en pleno florecimiento mientras la arquitectura retrocede; el ingeniero, inspirado por la ley de economía y guiado por el cálculo, actúa de acuerdo con las leyes del universo.",
   "La arquitectura trabaja con tres elementos, volumen, superficie y planta, ordenados por trazados reguladores.",
   "La casa debe producirse en serie: «una máquina para habitar».",
   "Barcos, aviones y autos muestran lo que logra la industria con selección y estándares; el avión es «un producto de alta selección».",
   "La elección es «arquitectura o revolución»."
  ],
  "impact": "Reunido a partir de los artículos que Le Corbusier firmó en L’Esprit Nouveau, la revista que fundó con Amédée Ozenfant y Paul Dermée, lo publicó Crès en París en 1923, en la colección «L’Esprit Nouveau», y apareció en inglés en 1927. Tuvo un «éxito deslumbrante»."
 },
 "refs": []
}
```

## movement · `de-stijl`

Movimiento. `traits` y la traducción `es.traits` deben tener la misma cantidad de elementos.

```json
{
 "rtype": "movement",
 "id": "de-stijl",
 "level": "essential",
 "disciplines": [
  "graphic",
  "product",
  "architecture"
 ],
 "start": 1917,
 "end": 1931,
 "fadeIn": 1,
 "fadeOut": 2,
 "regions": [
  "europe"
 ],
 "countries": [
  "NL"
 ],
 "name": "De Stijl",
 "short": "De Stijl",
 "key": "A Dutch group that reduced form to straight lines, right angles and primary colours, and applied it to painting, furniture, typography and architecture.",
 "traits": [
  "Horizontal and vertical lines only",
  "Red, yellow and blue with black, white and grey",
  "Asymmetric balance of rectangular planes",
  "Furniture and buildings made of rectilinear planes",
  "One language for painting, design and architecture"
 ],
 "context": "It formed in the Netherlands, neutral during the First World War, around the magazine De Stijl founded by Theo van Doesburg, whose first issue appeared in October 1917. Its 1918 manifesto saw the war as the destruction of the old, individualist world and called for the universal and for an international unity in life, art and culture. The group ended with Van Doesburg’s death in March 1931.",
 "shift": "From decoration to a system of elementary forms that could be applied to any object or building. Van Doesburg moved to Weimar in 1921 and gave his own De Stijl course there, close to the Bauhaus, which carried the group’s ideas to its students.",
 "es": {
  "name": "De Stijl",
  "short": "De Stijl",
  "key": "Un grupo neerlandés que redujo la forma a líneas rectas, ángulos rectos y colores primarios, y la aplicó a la pintura, el mobiliario, la tipografía y la arquitectura.",
  "traits": [
   "Solo líneas horizontales y verticales",
   "Rojo, amarillo y azul con negro, blanco y gris",
   "Equilibrio asimétrico de planos rectangulares",
   "Muebles y edificios hechos de planos rectilíneos",
   "Un mismo lenguaje para pintura, diseño y arquitectura"
  ],
  "context": "Se formó en los Países Bajos, neutrales en la Primera Guerra Mundial, en torno a la revista De Stijl, que fundó Theo van Doesburg y cuyo primer número salió en octubre de 1917. Su manifiesto de 1918 vio en la guerra la destrucción del viejo mundo individualista y pidió lo universal y una unidad internacional en la vida, el arte y la cultura. El grupo terminó con la muerte de Van Doesburg en marzo de 1931.",
  "shift": "De la decoración a un sistema de formas elementales aplicable a cualquier objeto o edificio. Van Doesburg se instaló en Weimar en 1921 y dio allí su propio curso De Stijl, cerca de la Bauhaus, que llevó las ideas del grupo a sus estudiantes."
 },
 "refs": []
}
```

## institution · `inst-bauhaus`

Institución (el id empieza con `inst-`). `end` es obligatorio (año, o `null` si sigue activa).

```json
{
 "rtype": "institution",
 "id": "inst-bauhaus",
 "level": "essential",
 "kind": "school",
 "disciplines": [
  "graphic",
  "product",
  "fashion",
  "architecture"
 ],
 "start": 1919,
 "end": 1933,
 "place": "Weimar, Dessau, Berlin",
 "regions": [
  "europe"
 ],
 "countries": [
  "DE"
 ],
 "name": "Bauhaus",
 "short": "Bauhaus",
 "key": "The German school of art, craft and design founded by Walter Gropius in Weimar in 1919, whose teaching spread across the world when its teachers and students emigrated after the Nazis forced it to close.",
 "more": "Founded on 1 April 1919 in Weimar by merging the art academy and the school of arts and crafts, it moved to Dessau in 1925 after the new conservative government of Thuringia cut its funds, into a building designed by Gropius and opened in 1926. Its directors were Gropius (1919–28), Hannes Meyer (1928–30) and Mies van der Rohe (1930–33). Dessau’s Nazi-dominated council voted in August 1932 to close it; it reopened privately in Berlin in October, was raided and sealed by the police in April 1933 and was dissolved by its teachers that July. Women were admitted but often steered to the weaving workshop, which Gunta Stölzl led from 1927.",
 "links": {
  "designers": [
   "gropius",
   "hannes-meyer",
   "mies-van-der-rohe",
   "moholy-nagy",
   "breuer",
   "bayer",
   "marianne-brandt",
   "wagenfeld",
   "gunta-stolzl",
   "anni-albers",
   "lilly-reich"
  ],
  "works": [
   "bauhaus-dessau-building",
   "wagenfeld-lamp",
   "brandt-tea-infuser",
   "kandem-lamp",
   "wassily-chair",
   "stolzl-tapestry",
   "albers-wall-hanging",
   "torten-estate"
  ]
 },
 "es": {
  "name": "Bauhaus",
  "short": "Bauhaus",
  "place": "Weimar, Dessau, Berlín",
  "key": "La escuela alemana de arte, oficio y diseño fundada por Walter Gropius en Weimar en 1919, cuya enseñanza se difundió por el mundo cuando sus profesores y estudiantes emigraron tras su cierre forzado por los nazis.",
  "more": "Fundada el 1 de abril de 1919 en Weimar al fusionar la academia de arte y la escuela de artes y oficios, se trasladó a Dessau en 1925, después de que el nuevo gobierno conservador de Turingia le recortara los fondos, a un edificio diseñado por Gropius e inaugurado en 1926. Sus directores fueron Gropius (1919–28), Hannes Meyer (1928–30) y Mies van der Rohe (1930–33). El concejo de Dessau, de mayoría nazi, votó en agosto de 1932 cerrarla; reabrió como escuela privada en Berlín en octubre, fue allanada y sellada por la policía en abril de 1933 y sus profesores la disolvieron en julio. Admitió mujeres, pero a menudo las encaminó al taller de tejido, que Gunta Stölzl dirigió desde 1927."
 },
 "refs": []
}
```

## designer · `gropius`

Diseñador. Años y lugares de nacimiento y muerte solo si se conocen con certeza (si no, solo años).

```json
{
 "rtype": "designer",
 "id": "gropius",
 "level": "essential",
 "kind": "person",
 "disciplines": [
  "architecture",
  "product"
 ],
 "born": 1883,
 "died": 1969,
 "dates": "1883–1969",
 "countries": [
  "DE",
  "GB",
  "US"
 ],
 "regions": [
  "europe",
  "north-america"
 ],
 "name": "Walter Gropius",
 "movements": [
  "bauhaus-movement",
  "new-objectivity",
  "international-style"
 ],
 "institutions": [
  "inst-bauhaus",
  "inst-weissenhof"
 ],
 "key": "German architect who founded the Bauhaus in 1919 and directed it until 1928, joining art, craft and industry in one school.",
 "more": "After serving in the First World War he founded the Bauhaus in Weimar in 1919 and designed its new building and the masters’ houses in Dessau in 1925–26, as well as the Törten housing estate. He left the directorship in 1928 to work in Berlin. Under Nazism he emigrated to London in 1934 and in 1937 to Harvard, where he taught a generation of American architects. Born in Berlin in 1883, he died in Boston in 1969.",
 "es": {
  "dates": "1883–1969",
  "key": "Arquitecto alemán que fundó la Bauhaus en 1919 y la dirigió hasta 1928, uniendo arte, oficio e industria en una sola escuela.",
  "more": "Tras servir en la Primera Guerra Mundial fundó la Bauhaus en Weimar en 1919 y diseñó su nuevo edificio y las casas de los maestros en Dessau en 1925–26, además del conjunto de viviendas de Törten. Dejó la dirección en 1928 para trabajar en Berlín. Bajo el nazismo emigró a Londres en 1934 y en 1937 a Harvard, donde formó a una generación de arquitectos estadounidenses. Nació en Berlín en 1883 y murió en Boston en 1969."
 },
 "refs": []
}
```

## work · `barcelona-chair`

Obra ★ (`level: essential`). Debe tener `designers`, `maker` o `client`; las ★ llevan al menos 2 enlaces de contexto de subcategorías distintas (se definen en LISTAS-CIERRE.md).

```json
{
 "rtype": "work",
 "id": "barcelona-chair",
 "level": "essential",
 "discipline": "product",
 "type": "chair",
 "title": "Barcelona chair",
 "designers": [
  "mies-van-der-rohe",
  "lilly-reich"
 ],
 "maker": "Berliner Metallgewerbe Josef Müller",
 "client": "German Reich",
 "year": 1929,
 "date": "1929",
 "production": {
  "from": 1929,
  "to": null,
  "note": "made in small numbers in Germany until the mid-1930s; by Knoll after the Second World War"
 },
 "regions": [
  "europe"
 ],
 "countries": [
  "DE",
  "ES"
 ],
 "materials": "Chrome-plated flat steel bars, leather cushions",
 "tech": [
  "chrome-plating"
 ],
 "key": "The stately armless chair of crossed steel bars and leather designed by Mies van der Rohe and Lilly Reich for the German pavilion in Barcelona.",
 "more": "Made for the 1929 Barcelona exhibition as a ‘monumental’ seat for the opening presided over by the King and Queen of Spain, it had an X-shaped frame of flat steel bars, at first bolted and chromed, with leather cushions; only two were placed in the pavilion. Reich, artistic director of the German section, shared in its design. Made by hand despite its machine look, it went into series production after the war at Knoll, which welds the frame and, since 1964, makes it in stainless steel.",
 "status": "Still in production by Knoll.",
 "es": {
  "title": "Silla Barcelona",
  "date": "1929",
  "materials": "Pletinas de acero cromado, cojines de cuero",
  "key": "La señorial silla sin brazos de pletinas de acero cruzadas y cuero que Mies van der Rohe y Lilly Reich diseñaron para el pabellón alemán de Barcelona.",
  "more": "Hecha para la exposición de Barcelona de 1929 como asiento «monumental» para la inauguración presidida por los reyes de España, tenía una estructura en X de pletinas de acero, al principio atornilladas y cromadas, con cojines de cuero; en el pabellón se pusieron solo dos. Reich, directora artística de la sección alemana, participó en su diseño. Hecha a mano pese a su aspecto de máquina, después de la guerra pasó a producirse en serie en Knoll, que suelda la estructura y, desde 1964, la hace en acero inoxidable.",
  "status": "Sigue en producción por Knoll.",
  "production": {
   "note": "fabricada en pequeñas cantidades en Alemania hasta mediados de los años treinta; por Knoll desde la posguerra"
  }
 },
 "refs": []
}
```

## work · `kitchener-poster`

Obra Normal en el modelo de datos del Modernismo (aquí aparece con el nivel que tiene hoy). Sin `designers` pero con `maker`.

```json
{
 "rtype": "work",
 "id": "kitchener-poster",
 "level": "essential",
 "discipline": "graphic",
 "type": "poster",
 "title": "Lord Kitchener Wants You",
 "short": "Kitchener",
 "designers": [],
 "maker": "Alfred Leete",
 "client": "London Opinion",
 "year": 1914,
 "date": "1914",
 "regions": [
  "europe"
 ],
 "countries": [
  "GB"
 ],
 "materials": "Lithograph and letterpress on paper",
 "tech": [],
 "key": "Alfred Leete’s image of Lord Kitchener pointing at the viewer, first a magazine cover in September 1914 and then a recruiting poster.",
 "more": "Leete drew it for the cover of the magazine London Opinion in September 1914. The design was then turned into a poster reading ‘Britons, [Kitchener] wants you. Join your country’s army!’, printed with London Opinion’s credit, and the Parliamentary Recruiting Committee took it up for its campaign. It is often remembered as the ‘Your country needs you’ poster, although those words are not on the ‘Britons’ version. Britain relied on volunteers until conscription was introduced in January 1916, and the direct gaze and pointing finger turned the poster into a personal appeal. The image appeared after the first great rush of volunteers: by the end of August 1914 some 30,000 men a day were already enlisting.",
 "status": "A few original prints survive in museums; the image is endlessly reproduced and parodied.",
 "es": {
  "title": "Lord Kitchener te quiere",
  "short": "Kitchener",
  "date": "1914",
  "materials": "Litografía y tipografía sobre papel",
  "key": "La imagen de Alfred Leete de Lord Kitchener señalando a quien mira, primero portada de revista en septiembre de 1914 y luego cartel de reclutamiento.",
  "more": "Leete la dibujó para la portada de la revista London Opinion de septiembre de 1914. El diseño se convirtió luego en un cartel que decía «Británicos, [Kitchener] los quiere. ¡Únanse al ejército de su país!», impreso con el crédito de London Opinion, y el Comité Parlamentario de Reclutamiento lo adoptó para su campaña. Se le suele recordar como el cartel de «Tu país te necesita», aunque esas palabras no están en la versión «Británicos». Gran Bretaña dependió de voluntarios hasta que la conscripción se impuso en enero de 1916, y la mirada directa y el dedo que apunta hicieron del cartel un llamado personal. La imagen apareció después de la primera gran oleada de voluntarios: a fines de agosto de 1914 ya se alistaban unos 30.000 hombres por día.",
  "status": "Se conservan pocos ejemplares originales en museos; la imagen se reproduce y parodia sin fin."
 },
 "refs": []
}
```

## link · `ctx-first-world-war → kitchener-poster`

Enlace de contexto: `ctx` (hecho) → `item` (elemento de diseño); la nota explica el mecanismo en 1 o 2 frases.

```json
{
 "rtype": "link",
 "ctx": "ctx-first-world-war",
 "item": "kitchener-poster",
 "note": "Britain relied on volunteers until 1916, so the state needed images that spoke to each man; Leete’s pointing Kitchener became the model recruiting appeal.",
 "es": {
  "note": "Gran Bretaña dependió de voluntarios hasta 1916, así que el Estado necesitó imágenes que hablaran a cada hombre; el Kitchener que señala de Leete se volvió el modelo del llamado a enlistarse."
 },
 "refs": []
}
```

## connection · `kitchener-poster → i-want-you-poster`

Conexión entre dos elementos de diseño (influencia, continuidad); la nota aclara si es influencia o causa.

```json
{
 "rtype": "connection",
 "from": "kitchener-poster",
 "to": "i-want-you-poster",
 "note": "Flagg’s Uncle Sam adapted the pointing finger of Alfred Leete’s 1914 British recruiting poster, an image of Kitchener pointing at the viewer that was copied for other posters.",
 "es": {
  "note": "El Tío Sam de Flagg adaptó el dedo que señala del cartel británico de reclutamiento de Alfred Leete de 1914, una imagen de Kitchener que apunta al espectador y que fue copiada en otros carteles."
 },
 "refs": []
}
```
