# Especificación de la etapa 8: ensayos de foco y de disciplina, barra de filtros y advertencia de revisión

*v46, 5 de octubre de 2026 (punto 79). Pedido de Mauricio; resumen y pasos en `PLAN-CIERRE.md`, sección 9d. Esta especificación manda sobre el resumen. No se implementa sin el «implementa» de Mauricio. Al final de la etapa va el **V2** (sitio completo) y, con su ok, empieza la Parte II.*

---

## 1. Lo que pidió Mauricio (en sus palabras, resumido)

1. **Fichas de foco contextual** (político, económico, social, cultural, tecnológico y productivo) con un **análisis más completo**: un texto de varios párrafos que explique cómo entender el diseño desde ese foco, con **eventos, movimientos y obras como ejemplos enlazados a sus fichas**, que se lea como un **breve ensayo de introducción** («La historia del diseño desde lo político / lo económico / …»), con las **referencias** al final (estas se agregan en la Parte II).
2. **Fichas de disciplina:** los botones de disciplina dejan de ser mostrar/ocultar y pasan a ser **botones de alcance**, como los de foco: al presionarlos, la línea muestra **solo lo relevante para esa disciplina** (contexto, movimientos, instituciones, diseñadores y obras) y la ficha presenta **«La historia del diseño XXXX»**: un panorama de 1750 a hoy, con los principales eventos de contexto que determinaron su evolución y ejemplos de obras y diseñadores.
3. **Apariencia equivalente** de los botones de foco y de disciplina: **etiqueta, ícono de color, borde del botón en una línea del mismo color y sombreado muy suave**. El botón de **Conexiones** se mueve a la derecha: **Foco | Disciplinas | [Conexiones] | Detalle**.
4. **V2 al final de la etapa 8**, antes de la Parte II.
5. **Advertencia en la cabecera:** en las fichas no revisadas (sin fuentes) aparece el **ícono de advertencia** (el que hoy está en «Fuentes») también **arriba, bajo el título y los años, al lado de «Imprescindible»** cuando corresponde.
6. (Decisión D2 del V4) La disciplina se sigue llamando «Moda», pero se entiende como **moda y textil**; su ficha de disciplina lo explica.

---

## 2. Barra de filtros

### 2.1 Orden
Primera fila de `renderFilters()` (hoy: Foco · Conexiones | Disciplinas | Detalle) pasa a:

**Foco** (6 botones) │ **Disciplinas** (4 botones) │ **Conexiones** │ **Detalle** (★ / Completo)

(separadores `<span class="sep"></span>` entre grupos; el botón de Conexiones conserva su ícono de curva y su función). La segunda fila (Mostrar, Organizar, Escala, chip «Solo:») no cambia.

### 2.2 Apariencia común (foco y disciplina)
Una sola regla de estilo para `.chip.lens` y `.chip.disc` (por ejemplo, una clase común `.chip.scope`), con el color del botón en una variable (`--sc`: `--c-<track>` para el foco, `--c-<disc>` para la disciplina):
- **Apagado:** etiqueta en `var(--ink-2)`; **ícono de color** (el punto del foco; el glifo de la disciplina) a opacidad plena; **borde de 1 px del color** (`rgba(var(--sc), .55)`); fondo transparente; **sombra muy suave** (`0 1px 2px rgba(0,0,0,.06)` en claro; `0 1px 2px rgba(0,0,0,.35)` en oscuro). **Las disciplinas apagadas ya no se ven deshabilitadas** (se quita la opacidad .55 actual).
- **Hover:** borde del color a opacidad plena.
- **Encendido:** fondo `rgba(var(--sc), .14)`, borde de 1,5 px del color, etiqueta `var(--ink)` en 600, sombra `0 1px 3px rgba(var(--sc), .25)`. (El foco hoy se enciende con fondo sólido de color: se reemplaza por este estilo, para que ambos grupos sean iguales.)
- Contraste comprobado con `python3 tools/check_contrast.py` en claro y oscuro.

### 2.3 Maqueta (paso 8.1)
Antes de tocar el sitio: capturas con CSS/JS inyectado (método habitual) de la barra en claro y oscuro, de una ficha-ensayo de foco, de una de disciplina y de una cabecera con la advertencia. Se muestran a Mauricio; si no objeta, se sigue.

---

## 3. Alcance por disciplina (comportamiento)

- **Estado:** `S.scope ∈ {null, 'graphic', 'product', 'fashion', 'architecture'}`; **uno a la vez**. Clic en una disciplina apagada → la enciende (y apaga otra que estuviera encendida); clic en la encendida → la apaga; la ✕ de su ficha también la apaga. Desaparece el modo mostrar/ocultar (`S.disc` pasa a derivarse: `S.scope ? new Set([S.scope]) : new Set(DISCS)`; la preferencia guardada, si existe, se ignora).
- **Fotografía y regreso**, como el foco (`applyFocus`): al encender el primer alcance se guarda el estado (secciones abiertas, Conexiones, ficha, posición) y al apagarlo se restituye.
- **Qué se ve con el alcance encendido** (función `makeScope(disc)`, análoga a `makeFocus`):
  - obras: solo las de esa disciplina (`workShown` ya usa `S.disc`);
  - diseñadores: los que tienen esa disciplina o una obra visible de ella (`designerVisible` ya lo hace);
  - movimientos e instituciones: los que incluyen la disciplina en `disciplines` **o** tienen una obra visible de ella;
  - teoría: la ligada (por `links`) a algún elemento visible;
  - **contexto:** solo los hechos con al menos un enlace (directo, en `ctxLinks`) a un elemento de diseño visible; productivo: solo los ligados por `tech` a obras visibles. Se agrega esa condición a `ctxVisible` y `prodVisible` (`!S.SC || S.SC.facts.has(id)`).
- **Con un foco encendido a la vez:** se pueden combinar (el foco limita el contexto y el diseño conectado; el alcance, la disciplina): se ve la intersección. La ficha muestra la del **último** que se encendió; si se apaga ese, se muestra la del otro.
- «Ajustar» (`visibleSpan`) y «Organizar» respetan el alcance. El chip «Solo:» sigue funcionando encima.
- **Ficha de disciplina** (`discCard()`), al encender el alcance y cuando no hay otra ficha seleccionada:
  - cabecera: rótulo «Disciplina», título **«La historia del diseño gráfico»** (ver títulos en 5.3), meta «Ensayo · N min de lectura · X obras · Y diseñadores», advertencia de no revisada (sección 7) mientras el ensayo no tenga fuentes;
  - el **ensayo** (sección 4) ;
  - debajo, listas en chips: movimientos, instituciones, diseñadores ★ y obras ★ de la disciplina (con «ver todo» si el nivel es Completo) y «Hechos de contexto más conectados» (los 12 con más enlaces a elementos de la disciplina).

## 4. Ficha de foco (`lensCard()`)

Nuevo orden: cabecera (rótulo «Foco», título **«La historia del diseño desde lo político»**, meta «Ensayo · N min de lectura · X hechos · Y elementos conectados», advertencia de no revisada mientras no tenga fuentes) → **ensayo** → las secciones actuales («Por macromovimiento», «Hechos de esta fila», «Diseño conectado») → consejo final. El texto breve actual `lens_<k>` queda como respaldo si falta el ensayo.

**Vínculos del ensayo:** cada `[[id]]` se dibuja como un vínculo en línea (botón con `data-go="<id>"`, estilo de texto subrayado discreto con el color de su tipo) que abre la ficha del elemento, igual que los chips. Al abrir una ficha desde el ensayo, el foco o el alcance siguen encendidos.

---

## 5. Datos de los ensayos

### 5.1 Archivo y build
- Archivo nuevo **`src-essays/essays.json`** (fuera de `src-data/`, que solo admite carpetas de época). `tools/build_data.py` lo lee, lo valida y escribe **`data/essays.json`**; `app.js` lo carga al abrir por primera vez una ficha de foco o de disciplina (no se mete en `all.json`, para no aumentar la carga inicial).
- Formato:
```json
{ "essays": [
  { "id": "lens-political", "kind": "lens", "target": "political",
    "title": "The history of design through politics",
    "subtitle": "How states, parties and movements have used and contested design since 1750",
    "paras": ["… the [[ctx-russian-revolution]] … [[constructivism|Constructivism]] … [[red-wedge-poster]] …", "…"],
    "images": ["red-wedge-poster", "kitchener-poster", "munich72-pictograms", "franja-del-no-1988"],
    "refs": [],
    "es": { "title": "La historia del diseño desde lo político",
            "subtitle": "Cómo los Estados, los partidos y los movimientos han usado y disputado el diseño desde 1750",
            "paras": ["… la [[ctx-russian-revolution]] … [[constructivism|el constructivismo]] …", "…"] } } ] }
```
- `kind`: `lens` (con `target` = `political`, `economic`, `social`, `cultural`, `technological` o `production`) o `discipline` (con `target` = `graphic`, `product`, `fashion` o `architecture`). Ids: `lens-<target>` y `disc-<target>`. **10 ensayos.**
- Vínculos: `[[id]]` muestra el nombre del elemento en el idioma de la vista; `[[id|texto]]` muestra el texto dado.
- **Validación del build** (PROBLEM salvo indicación): ids de vínculos e imágenes existentes; mismos ids enlazados en EN y ES (el orden puede variar); `es` completo; **6 a 10 párrafos** en los de foco y **8 a 12** en los de disciplina; cada párrafo ≤ 1.100 caracteres; **≥ 15 ids distintos enlazados** por ensayo, de al menos tres tipos (contexto, movimiento u obra, y diseñador o institución) y de al menos cuatro de los cinco tramos; `images` con 4 a 8 obras (WARN si alguna no tiene imagen libre disponible: sin `wiki` ni imagen elegida en `?editar`).
- `refs` sigue la forma de las fichas (`label`, `url`, `checks`, `date`) y se llena en la Parte II (R3). Sin `refs`, la ficha lleva la advertencia de «no revisado».

### 5.2 Imágenes
Solo 72 de las 585 obras tienen hoy `wiki` (de donde la ficha toma la imagen libre de Wikimedia Commons). Para cada obra de `images` sin `wiki`, el redactor del paso 8.3 propone el título exacto del artículo de Wikipedia en inglés **solo si lo conoce con certeza** (si no, se elige otra obra con imagen). La comprobación de que la imagen existe y es libre (repositorio `shared` de Commons) la hace `make_essays_pdf.py`.

### 5.3 Títulos
| id | ES | EN |
|---|---|---|
| lens-political | La historia del diseño desde lo político | The history of design through politics |
| lens-economic | La historia del diseño desde lo económico | The history of design through economics |
| lens-social | La historia del diseño desde lo social | The history of design through society |
| lens-cultural | La historia del diseño desde lo cultural | The history of design through culture |
| lens-technological | La historia del diseño desde lo tecnológico | The history of design through technology |
| lens-production | La historia del diseño desde lo productivo | The history of design through production |
| disc-graphic | La historia del diseño gráfico | The history of graphic design |
| disc-product | La historia del diseño de producto | The history of product design |
| disc-fashion | La historia del diseño de moda | The history of fashion design |
| disc-architecture | La historia de la arquitectura | The history of architecture |

(Para arquitectura se propone «La historia de la arquitectura»; la alternativa literal, «La historia del diseño arquitectónico», se muestra en la maqueta 8.1 para que Mauricio elija.)

---

## 6. (Sin PDF)

El PDF de los ensayos se **anuló en el punto 90 (v56)**: no hay generador, ni carpeta `ensayos/`, ni botón de descarga. Los ensayos solo se leen en la ficha.

## 7. Advertencia de «no revisada» en la cabecera

- `head()` recibe un indicador más (`unrev`). Cuando es verdadero, bajo el título y la meta, en la misma línea que el sello «Imprescindible» (si lo hay), aparece **el mismo ícono triangular de «Fuentes»** (`rf-warn`, color `var(--warn)`) con el texto **«No revisada»** (EN «Not reviewed») y el `title`/`aria-label` «Ficha no revisada: aún no tiene fuentes» / «Card not reviewed: it has no sources yet». Un clic en ella abre la sección «Fuentes» y la lleva a la vista.
- Se calcula con `srcCount(id) === 0` (misma regla que la sección «Fuentes») en todas las fichas de elementos (obra, diseñador, movimiento, institución, hecho de contexto, productivo, teoría, concepto) y con `refs` vacío en los ensayos. No aparece en las fichas de información, ayuda ni revisión.
- La advertencia de la sección «Fuentes» se mantiene igual.

---

## 8. Brief de redacción de los ensayos (`tools/pipeline/briefs/BRIEF-ENSAYOS.md`, se crea en 8.3)

Contenido mínimo del brief:
- **Tarea:** escribir un ensayo (ES de Chile e inglés) con el formato de la sección 5.1. Uno por agente.
- **Tono:** académico y claro, para estudiantes de primer año; tercera persona; sin adjetivos de promoción; sin citas textuales.
- **Estructura de un ensayo de foco:** (1) tesis: qué permite ver ese foco del diseño; (2) desarrollo por grandes períodos (Revolución Industrial; reforma del siglo XIX; modernismo y entreguerras; posguerra; posmodernidad y era digital), siempre con **mecanismos** (qué cambió en el contexto → qué decisión de diseño cambió), nunca coincidencias de fechas; (3) un párrafo sobre América Latina cuando el foco lo permita; (4) cierre: preguntas o claves para seguir mirando la línea con ese foco.
- **Estructura de un ensayo de disciplina:** panorama de 1750 a hoy: orígenes del oficio, profesionalización, grandes movimientos, figuras y obras, cambios técnicos y económicos que la transformaron, y estado actual. El de **moda explica que la disciplina incluye el textil** (decisión D2). El de **productivo** (foco) trata materiales, procesos y herramientas.
- **Vínculos:** solo ids que existan en la línea (`data/all.json`), con `[[id]]` o `[[id|texto]]`; ≥ 15 distintos; lo que se diga de un elemento debe coincidir con su ficha.
- **Hechos:** regla C1 (solo lo que se sabe con alta certeza; ante la duda, omitir); sin web; `refs: []`.
- **Imágenes:** 4 a 8 obras citadas en el texto, de preferencia con `wiki`.
- **Validación:** el build (sección 5.1) y una lectura de Mauricio en el V2.

---

## 9. Textos de la interfaz y ayuda
- Nuevos en `UI.es`/`UI.en`: rótulo «Disciplina» del kicker, «Ensayo», «min de lectura», «No revisada», «Hechos de contexto más conectados», títulos de la tabla 5.3, tooltips de los botones de disciplina («Ver la historia del diseño gráfico» / «Quitar el alcance»).
- Ayuda: reescribir los párrafos de «Filtros» (Disciplinas ahora es alcance, uno a la vez; nuevo orden de la barra) y de «Fichas» (ensayos, advertencia en la cabecera). Regenerar las imágenes de la ayuda (`python3 tools/make_help_images.py`).
- «Acerca de»: una línea que anuncie los ensayos de foco y de disciplina.

## 10. Pruebas (paso 8.6; las de imágenes y galería, en la sección 11)
- Prueba nueva `tools/tests/test_v4x_etapa8.py` (Playwright): orden de la barra (Foco, Disciplinas, Conexiones, Detalle); los botones de foco y disciplina tienen borde del color y sombra; un clic en «Gráfico» deja solo obras gráficas y muestra «La historia del diseño gráfico»; un segundo clic restituye el estado; alcance + foco a la vez; un vínculo del ensayo abre su ficha; la advertencia de cabecera aparece en una ficha sin fuentes y no en una con fuentes (por ejemplo, una obra del Modernismo con `refs`); sin errores de página; ES y EN.
- Ajustar `tools/tests/test_general.py`, que hoy usa los botones de disciplina como mostrar/ocultar (C6).
- `run_all.sh`, `check_contrast.py`, rendimiento (< 3 s) y 6 capturas (barra claro y oscuro; ficha de foco; ficha de disciplina; cabecera con advertencia; 390 px).


---

## 11. Imágenes en todas las fichas de obra y de diseñador, y galería en las fichas de estilos (paso 8.5b; punto 81)

**Lo que pidió Mauricio:** antes de su revisión final (V2), asegurar que **todas las fichas de obra y de diseñador tengan imagen**; sugerirle fuentes de imágenes para cuando Wikimedia no tenga; y que las **fichas de estilos** (movimientos y macromovimientos) lleven **una o varias imágenes**, con puntitos abajo para pasar de una a otra.

### 11.1 Punto de partida (v47)
- Hoy la imagen sale de `wiki` (título de Wikipedia en inglés) consultando la API en el navegador (`fetchImage`, `app.js`), y solo se muestra si el archivo está en **Wikimedia Commons** (repositorio `shared`). Además `ediciones/imagenes.json` permite reemplazar a mano la imagen de una ficha con una URL (modo `?editar`).
- Cobertura: `wiki` existe en **75 de 587 obras** y **75 de 341 diseñadores** (faltan ~512 y ~266); en las ★, 32 de 165 obras y 28 de 86 diseñadores. Tener `wiki` tampoco garantiza imagen: muchas obras posteriores a 1950 tienen su foto en Wikipedia como «uso legítimo» (no en Commons) y hoy no se muestran.
- Solo hay **una** imagen por ficha, y movimientos e instituciones casi no tienen (13 de 73 y 18 de 93 con `wiki`).

### 11.2 Qué se hace
1. **Auditoría `[C]`:** `tools/pipeline/imagenes_etapa8.py audit` consulta Commons y entrega, por elemento, si la ficha **hoy muestra imagen real** (no solo si tiene `wiki`). Informe en `tools/INFORME-IMAGENES.md` (cobertura por tipo, nivel y época; lista de faltantes). Es la única parte de la Parte I que usa la web: las imágenes **no** son contenido redactado, así que no rompe la regla C2.
2. **Búsqueda `[B]`:** agentes Sonnet por lotes (≤ 12 elementos), **primero ★ y después el resto**. Para cada ficha sin imagen, buscar un archivo **de licencia libre** en este orden: (a) Commons por búsqueda directa y por categoría (no solo la imagen principal del artículo; el artículo de Wikidata, propiedad P18, ayuda); (b) las fuentes de la lista 11.4; (c) si no existe, un sucedáneo (11.5). Cada elegida se guarda con **archivo, autor, licencia, URL de origen y alt** (texto alternativo). Sin inventar: si no hay certeza de que la imagen muestre la obra o a la persona, no se pone y se anota.
3. **Datos y build `[C]`:** campo nuevo `images: [{ "file": "File:Nombre.jpg" | "url": "https://…", "credit": "…", "license": "CC BY-SA 4.0", "source": "https://…", "alt": {en, es}, "caption": {en, es}? }]` en obras, diseñadores, movimientos, instituciones y teorías (la primera es la principal; `rights`: `free` o `reserved`). `build_data.py` valida (HTTPS, licencia no vacía, alt en ES y EN) y avisa **«N obras / N diseñadores sin imagen»** igual que el aviso de fuentes; **meta: 0**, con excepciones anotadas una por una con su motivo. `wiki` sigue valiendo como respaldo.
4. **Galería `[B]` código:** componente único `imgGallery(it, kind)` que reemplaza a `imgBox` para todos los tipos: 1 imagen → como hoy; 2 a 6 → carrusel con **puntitos abajo** (botones accesibles con `aria-label`, flechas del teclado, deslizar en el celular, imagen cargada solo al verse), pie con **crédito y licencia** y enlace a la fuente; el lápiz del modo edición y las imágenes cambiadas a mano siguen funcionando (la imagen de `imagenes.json` pasa a ser la primera). Tema claro y oscuro; contraste (`check_contrast.py`).
5. **Fichas de estilos:** movimientos y macromovimientos muestran **de 3 a 5 imágenes**. Por defecto se arman **solas con las obras ★ del propio movimiento** que ya tienen imagen (pie: nombre de la obra, año y vínculo a su ficha), de modo que no hace falta buscar licencias nuevas; se pueden agregar o fijar imágenes propias con `images` (p. ej. una página de manifiesto, un cartel de la exposición). Un movimiento sin obras con imagen queda con la que se elija a mano o, si no hay, sin imagen y anotado. Las **instituciones** (galería) y las **teorías** (portada) también llevan imagen, por D-IMG3.
7. **Tamaño:** las imágenes de Commons se enlazan (miniatura de la API, no se descargan). Lo que venga de otras fuentes (libre o de derechos reservados) se guarda en `img/` redimensionado a 720 px de ancho en WebP (≈ 40 KB); `empaquetar.sh` y R5 deben incluir `img/` y el ZIP no debe pasar de unos 40 MB (si pasa, se avisa).

### 11.3 Cierre del paso
- El aviso del build en 0 (o excepciones anotadas) para obras y diseñadores; informe final con cobertura por tipo y época, y la lista de excepciones con su motivo.
- Prueba nueva en `test_v4x_etapa8.py` o aparte: una obra con 1 imagen, una con varias, un movimiento con galería (puntitos, flechas, teclado), crédito visible, ficha sin imagen sin errores de página, 390 px.
- **Revisión visual de Mauricio** (parte del V2): muestra de ~30 fichas (10 obras, 10 diseñadores, 10 estilos).

### 11.4 Dónde buscar cuando Wikimedia Commons no tiene la imagen (sugerencias a Mauricio)
**Colecciones de museos y archivos con imágenes libres (CC0 o dominio público), las más útiles para historia del diseño:**
- **Smithsonian Open Access** (incluye el **Cooper Hewitt**, museo nacional de diseño: producto, gráfica y textil): CC0.
- **The Metropolitan Museum of Art (Open Access)**, **Art Institute of Chicago**, **Cleveland Museum of Art**, **National Gallery of Art**, **Rijksmuseum**: CC0 o dominio público; buenos para muebles, vidrio, cerámica, moda y estampas anteriores a 1950.
- **Library of Congress** (Prints & Photographs; en arquitectura, **HABS/HAER**) y **NYPL Digital Collections**: muchas imágenes sin restricciones conocidas; revisar la nota de derechos de cada una.
- **Europeana**, **Gallica (BnF)**, **Deutsche Digitale Bibliothek**, **Digitale Collectie / Het Nieuwe Instituut** y **Nationalmuseum (Suecia)**: filtrar por «dominio público» o CC0.
- **Internet Archive** y **HathiTrust / Google Books** (libros y revistas anteriores a 1929: portadas, carteles, anuncios, tipografías, planos).
- **Flickr Commons** y búsquedas de Flickr/Openverse filtradas por licencia **CC BY o CC BY-SA** (fotos de edificios, objetos y exhibiciones hechas por aficionados).
- **Openverse** (buscador de CC de WordPress), **Geograph** (edificios del Reino Unido), **Wellcome Collection** (CC BY; textiles y objetos).
- **Para Chile y América Latina:** **Memoria Chilena** y **Biblioteca Nacional Digital** (BNCh), Archivo Patrimonial de la Universidad de Chile, **Museo Histórico Nacional**, **Biblioteca Digital Hispánica**, **Brasiliana** y **Acervo Digital** de Brasil. Muchas piezas tienen restricciones: se revisa caso a caso.
- **Retratos de diseñadores:** Commons y los archivos de las universidades (ETH, Bauhaus-Archiv cuando es PD), **Bundesarchiv** (en Commons), Library of Congress, Smithsonian Archives. Para diseñadores vivos casi siempre solo hay retratos CC de eventos o del propio estudio.

**Cuando la imagen es de derechos reservados (D-IMG1, decidida por Mauricio en el punto 82):** el sitio es **privado e interno, no se publica**, así que se acepta una imagen con derechos reservados **si viene de un sitio legítimo y confiable** (museo, archivo, biblioteca, fundación del diseñador, fabricante o editorial, prensa reconocida; no de blogs, tiendas de terceros, Pinterest ni buscadores de imágenes). Se prefiere siempre la libre (Commons y la lista de arriba) y los sucedáneos 11.5; la de derechos reservados es el siguiente recurso. Esas imágenes se marcan `"rights": "reserved"` en `images` y la galería muestra junto a ellas un pequeño enlace **«Créditos» («Credits»)** que despliega autor o titular, fuente y enlace a la página de origen (las libres ya muestran crédito y licencia en el pie). **Guardar copia local** en `img/` (redimensionada, WebP) para las de derechos reservados, porque los sitios de origen suelen bloquear el enlace directo desde otras páginas y las URL cambian. **Si algún día el sitio se hace público**, todas las marcadas `reserved` deben revisarse o reemplazarse (el build las lista con `--imagenes-reservadas`). Esto no es asesoría legal.

### 11.5 Sucedáneos cuando no hay imagen libre de la obra (en este orden)
1. Otra foto (libre o, por D-IMG1, de un sitio legítimo con derechos reservados) de la **misma obra** (de otro autor, de un museo o de una exposición).
2. Una foto libre de **una réplica, un ejemplar de museo o una vista parcial** (marcada así en el pie).
3. Un anuncio, una página de catálogo, una patente o un plano **antiguo** (dominio público) de la misma obra.
4. Una imagen de **otra obra del mismo diseñador** (para fichas de diseñador, la obra más conocida con imagen libre), con el pie «Obra más conocida: …».
5. Sin imagen, solo si ninguna de las anteriores existe: **excepción anotada** (lo esperable son algunos diseñadores vivos y obras muy recientes).

### 11.6 Decisiones de Mauricio (punto 82, resueltas)
- **D-IMG1:** no hace falta que la imagen sea libre: el sitio es privado, y se acepta una imagen con derechos reservados de un sitio legítimo y confiable. Cuando ocurra, la ficha muestra un pequeño enlace **«Créditos»** (ver 11.4). Se sigue prefiriendo la libre.
- **D-IMG2:** diseñadores (vivos o no) sin retrato disponible: se muestra **una obra suya** (opción 4 de 11.5, con el pie «Obra más conocida: …»).
- **D-IMG3:** las **instituciones** llevan imagen y galería (edificio, sede o pieza emblemática) y las **teorías** llevan su **portada** (del libro, manifiesto o revista), con el mismo criterio de D-IMG1.


---

## 12. Modo edición y resumen de revisión (paso 8.5c; punto 83)

**Lo que pidió Mauricio:** (1) el modo edición hoy pide la contraseña apenas se abre; debe pedirla **al editar algo**; (2) la contraseña será **`uai2026`**; (3) el resumen de edición debe mostrar también datos de las **imágenes** (con y sin imagen, con imagen libre, con imagen con derechos reservados, etc.) y un **listado de fichas por imagen**, parecido al de fuentes; y un listado de **fichas con comentarios**; (4) los listados de **fuentes, imágenes y observaciones** son **colapsables y parten colapsados**; (5) las **épocas se nombran por sus años** («1914–1944»), no por etiquetas («Modernismo»), **en todo el sitio** (punto 84).

### 12.1 Contraseña al editar, no al abrir
- Con `?editar` en la dirección, la página abre **sin pedir nada**: se ve la etiqueta «Modo edición», el botón del resumen y los controles de edición (lápiz sobre la foto, sección «Observaciones»).
- La contraseña se pide **la primera vez que se intenta una acción de edición**: tocar el lápiz de la imagen, escribir o guardar una observación, marcarla como resuelta, cambiar o restaurar una imagen, o abrir en el resumen la parte que lee observaciones del servidor. Se muestra como un cuadro pequeño (diálogo con foco en el campo, `Esc` cancela, mensaje claro si es incorrecta); al acertar, la acción pedida **sigue sola**, sin repetir el gesto. Se guarda solo en `sessionStorage` (como hoy), así que no se vuelve a pedir en esa sesión del navegador.
- El **resumen** se abre sin contraseña y calcula desde los datos del sitio todo lo que no es privado (fuentes, imágenes, épocas, imágenes cambiadas a mano, que ya son públicas en `imagenes.json`). Solo la lista de **observaciones** (`revision.json`, privada) pide la contraseña: en su lugar aparece un botón «Ingresar contraseña para ver las observaciones».
- **Cambio de contraseña a `uai2026`:** en `editar.php` (constante `CLAVE`), `tools/tests/test_editar.py`, `test_v21.py`, `test_empaquetar.py`, `tools/empaquetar.sh` (la verificación de la clave), `LEEME-PROBAR-EN-WEB.md` y su plantilla, `INICIO-SESION-NUEVA.md`, `ESTADO-ACTUAL.md` y `PROJECT.md`. **Reemplaza la decisión del punto 60** (la clave `lhd2026` no se cambiaba). Sigue sin ir en `app.js`. Es una clave simple en un archivo del servidor, aceptable para un sitio privado.

### 12.2 Resumen ampliado
Orden de las secciones: **Revisión por IA (fuentes)** · **Imágenes** · **Observaciones** · **Imágenes cambiadas a mano** (dentro de «Imágenes») · exportar.
- **Cifras de fuentes** (como hoy): total con fuentes, por tipo y por época.
- **Cifras de imágenes (nuevas):** sobre las fichas que llevan imagen (obras, diseñadores, movimientos, instituciones y teorías): **con imagen / sin imagen**, y dentro de las con imagen **libre**, **con derechos reservados (con «Créditos»)** y **sucedánea** (obra suya en un diseñador, réplica, etc.); por tipo y por época, con barras como las de fuentes; y cuántas se cambiaron a mano. Se calculan con el campo `images` del paso 8.5b (`rights`, `file`/`url`); mientras ese campo no exista, con `wiki` y las imágenes cambiadas a mano.
- **Listados (los tres colapsables):** cada uno es una sección con título, **cuenta** y flecha (`<details>` o botón con `aria-expanded`), **cerrada al abrir el resumen** (y se vuelve a cerrar al reabrirlo). Contenido:
  1. **Fuentes:** como hoy (filtros «Sin fuentes/Con fuentes» y época; filas que abren la ficha).
  2. **Imágenes (nuevo):** filtros «Sin imagen», «Libre», «Derechos reservados», «Sucedánea» y época; fila con miniatura, nombre, tipo, época y origen; clic abre la ficha. Debajo, «Imágenes cambiadas a mano».
  3. **Observaciones (fichas con comentarios):** como hoy («Observaciones pendientes»); se agrega el contador de resueltas si existen.
- Tope de 150 filas por listado, con aviso de filtrar por época (como hoy).

### 12.3 Épocas por años en todo el sitio (decidido en el punto 84)
- **Nombre de cada época:** solo sus años, sin etiqueta: **1750–1850 · 1851–1913 · 1914–1944 · 1945–1974 · 1975–hoy** (en inglés, «1975–today»). Sin años repetidos: el año de término que se muestra es el inicio de la siguiente época menos uno (Mauricio eligió **1914–1944** para la tercera). Se calcula desde `start`/`end` de cada época con un asistente único `eraName(e)` (no se escribe a mano).
- **Dónde:** en **todo el sitio**: la franja o selector de épocas, el título y la meta de la ficha de época (hoy `tx(e, 'name')` más el rango), el buscador y los tooltips que citan una época, el resumen de revisión (chips, tablas, filas), la exportación .md, la ayuda y «Acerca de», las imágenes de la ayuda (`make_help_images.py`) y los textos de los ensayos de la etapa 8 (por ejemplo «Época 1914–1944»). El **texto introductorio** de cada época (`intro`) se conserva; solo cambia el rótulo. En los datos, el `name` de las épocas puede quedar como nombre interno, pero ya no se muestra.
- **Macromovimientos:** **Modernismo** y **Posmodernismo** siguen existiendo como macromovimientos (`macro-modernism`, `macro-postmodernism`), con su ficha y su lugar en la fila «Movimientos». Así se evita la confusión actual entre la época «Modernismo» (1914–1945) y el macromovimiento del mismo nombre (1907–1970). Hoy las demás épocas (Industrial, Reforma, Posguerra) **no** tienen macromovimiento: Mauricio **evaluará más adelante** si se agrega otro (queda registrado como decisión futura; no se hace en esta etapa).
- **Advertencia para el código:** ningún texto, prueba ni documento debe asumir que las épocas se llaman «Modernismo», «Posguerra», etc.; las pruebas que buscan esas etiquetas se ajustan (C6) y los textos que dicen «la época Modernista» se cambian a «la época 1914–1944» o al macromovimiento, según el caso. Los documentos internos (plan, bitácora) pueden seguir usando los nombres históricos de los tramos.

### 12.4 Pruebas (8.6)
`test_editar.py`: abrir `?editar` no muestra ningún campo de contraseña; el primer intento de editar la pide, rechaza una incorrecta, acepta `uai2026` y completa la acción; el resumen abre con los tres listados cerrados, se abren y cierran, y muestra las cifras de imágenes; las épocas aparecen como años en toda la interfaz (franja de épocas, ficha de época, buscador, chips, tablas, filas, exportación) y ninguna muestra «Modernismo», «Posguerra», etc. como época; los macromovimientos Modernismo y Posmodernismo siguen apareciendo en «Movimientos»; 390 px; contraste. `test_v21.py` y `test_empaquetar.py` con la clave nueva; `ediciones/` limpia al terminar.

## Nota (v61, punto 95): leyendas de imágenes
Desde 8.6 el enlace «Créditos» y el pie con licencia se reemplazan por: pie solo en carruseles (nombre de la foto y marca «(C)» o «(CC)» si no es dominio público), imagen como enlace a su fuente y una línea «Imagen: …» al inicio de «Fuentes» (no cuenta como fuente). Ver `CAMBIOS-PENDIENTES.md`, punto 95 y 98.
