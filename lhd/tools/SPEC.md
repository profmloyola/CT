> **Actualización v01 (Fase 0).** Esta copia es la especificación original con un cambio de estado: la base técnica (sección 3) está construida y probada. Las decisiones de la sección 15 se tomaron con los valores recomendados (ver `PROJECT.md`). La Fase 1 (Modernismo) espera la aprobación de las listas propuestas; los datos de `src-data/` son provisionales (de prueba) hasta entonces. Cambios de implementación respecto del texto: (1) el build agrega el campo `track` a cada enlace de contexto en `data/<época>.json`; (2) la época por defecto al abrir el sitio es `CFG.defaultEra` (por defecto `modernism`); (3) los filtros son multiselección con todo activado de inicio (un clic desactiva); (4) las imágenes de la API de Wikipedia solo se muestran si el archivo está en Wikimedia Commons; (5) alcance regional reducido a Europa, Norteamérica, América Latina y global (se eliminaron Asia, África y Medio Oriente y Oceanía, y sus elementos de ejemplo en la sección 10); (6) **v04, decisiones de la persona responsable:** listas del Modernismo aprobadas; se saca el texto de Benjamin; Chile deja de ser categoría y chip (queda dentro de América Latina, y no se fuerzan obras chilenas); la fila «Producción» pasa a llamarse **«Productivo»** (en inglés «Productive»; nombre provisional, el identificador interno sigue siendo `production`); se confirman las decisiones 1 a 4, 7 y 8 de la sección 15 y el alcance regional; (8) **v07:** nombres cortos por sí solos (la explicación va en el texto), «Estado actual» con mayúscula inicial, imagen de ficha como enlace a su fuente, «Efecto en el diseño» sin fondo especial, barras de sección más claras, la línea de vida del diseñador no tapa las obras; (7) **v06:** se elimina la lente de contexto (4.6); la ficha de época muestra siempre los resúmenes de contexto y los cambios clave; Disciplinas y Regiones pasan a la fila de Contexto; las barras CONTEXTO y DISEÑO son más oscuras.

> **Actualización del 4 oct 2026 (puntos 71 y 72, plan v8):** el alcance de contenido ya no es solo el de la sección 10: la etapa 6 del plan (`PLAN-CIERRE.md`, sección 9b) lo amplía a ≥ 500 obras. El nivel `normal` se mostrará como «Completo» (solo etiqueta; el valor de los datos no cambia).

> **Actualización del 3 oct 2026 (punto 44, manda sobre lo anterior):** campo nuevo `refs` `[{label, url, checks, date}]` en todos los elementos y en los enlaces de contexto, con marcas `[n]` en los textos EN y ES.
> - **v30 (punto 59, manda):** las marcas se muestran como superíndices también en el sitio público; cada ficha termina con la sección colapsable «Fuentes (n)» (advertencia «no revisada» si no hay fuentes). «Revisión» pasó a «Observaciones» (solo texto) y el resumen de `?editar` tiene tres bloques. Antes de v30 las marcas se quitaban en el sitio público y se veían solo en `?editar`.
> - Detalle y validaciones: `MANUAL-CONTENIDO.md`, sección 7.1.
>
> **Actualización v20 (manda sobre lo anterior):**
> - **Contenido:** las reglas están en `tools/MANUAL-CONTENIDO.md`.
> - **v24 (puntos 48–50):** dos niveles; contexto colapsado al abrir; macromovimientos dentro de la fila «Movimientos», con el mismo comportamiento que los demás movimientos.
> - **Niveles:** campo `level` (`essential|normal`; desde v24 solo dos niveles, punto 48) en movimientos, instituciones, teoría, diseñadores y obras; `star` lo calcula el build (= `essential`).
> - **Épocas:** no se muestran. Los macromovimientos (`macro: true`, `parts`, `context_summary`, `shifts`) dan el panorama.
> - **Diseñadores:** todo diseñador necesita al menos una obra de su nivel o de uno más básico.
> - **Fichas:** «Saber más» usa `where` (sin Wikipedia); `wiki` solo sirve para la imagen.
>
> **Actualización v19:**
> - **Color de los diseñadores:** la línea de vida va en el color de sus disciplinas (campo `disciplines`); las de varias disciplinas van en rayas.
> - **Selección:** lo elegido queda en tinta; lo relacionado y las curvas conservan su color.
> - **Escala:** «Visual» (antes «Por densidad») y «Cronológica» (antes «Lineal»).
> - **Navegación:** botones ⟷ (línea completa) y |⟷| (ajustar a lo que se muestra), y una sola flecha doble por sección.
> - Ver los puntos 23 a 30 de `tools/CAMBIOS-PENDIENTES.md`.
>
> **Actualización v18:**
> - **La teoría (56-theory.json) es una categoría de DISEÑO**, no de contexto: no hay fila ni foco «Teórico». Los enlaces de contexto (`80-context-links.json`) pueden apuntar a textos teóricos.
> - **Organizar** tiene cuatro vistas, todas con grupos plegables: «Por categoría», «Por fecha» (sin diseñadores), «Por disciplina» (la teoría va según su género) y «Por región».
> - **Navegación del tiempo:** minimapa con corchetes, arrastre sobre los años, flechas en los extremos y «De … a … Todo». Ver los puntos 17 a 22 de `tools/CAMBIOS-PENDIENTES.md`.
>
> **Actualización v15:** ver los puntos 5 a 10 de `tools/CAMBIOS-PENDIENTES.md`. En particular, el diseño ya no tiene subfranjas: se organiza con «Organizar» (cronológica, por disciplina con Interdisciplinario para 2 o más disciplinas, o por región con zonas culturales estables según el primer país de `countries`, que debe ser el de la actividad principal). Se eliminó el filtro de regiones (el campo `regions` se mantiene). `CFG.defaultEra` ya no se usa: sin selección, la ficha queda vacía.
>
> **Actualización v14:** ver los puntos 1 a 4 de `tools/CAMBIOS-PENDIENTES.md` (flechas dobles en CONTEXTO y DISEÑO; el foco restaura el estado anterior al quitarlo; destacado en tinta, sin naranja; el nombre de la subcategoría activa el foco en todo el sitio).
>
> **Actualización v13 (el foco como eje; manda sobre v11 y v12):** (1) los chips de Contexto ya no muestran u ocultan filas: son los botones **Foco:** (en inglés **Lens:**), uno por subcategoría (político, económico, social, cultural, tecnológico, productivo, teórico); el activo se pinta con el color de su fila; otro clic lo quita; uno a la vez. (2) Con un foco activo quedan en la línea los hechos de esa fila y solo los movimientos, instituciones, diseñadores y obras conectados con ellos; un diseñador se muestra solo si él mismo está conectado (si solo lo está una obra suya, se muestra la obra suelta); se abren las partes de diseño que tienen elementos conectados y se cierran las demás filas de contexto. (3) La ficha muestra **«Foco: …»**: el diseño desde ese contexto (texto general), la síntesis de cada época para esa fila, sus hechos y el diseño conectado; la ✕ quita el foco. (4) El foco se activa desde la barra de filtros, el nombre de la fila de contexto en la línea (la flechita sigue abriendo y cerrando la fila), la ficha de época, la sección Contexto de las fichas y la ficha de un hecho, de productivo o de teoría. (5) Junto a los botones de foco hay un solo botón **Conexiones** (todas las curvas); al activar un foco se enciende y al quitarlo vuelve a su estado anterior. Con un foco activo, las curvas y el resaltado hacia el contexto solo van a hechos de ese foco.
>
> **Actualización v12 (correcciones a v11; manda sobre v11):** (1) la barra de épocas es la primera fila de la subfranja Movimientos, no un botón del eje: clic = ficha de época, sin zoom automático (el zoom queda en el botón de lupa de la ficha); (2) el diseño tiene tres subfranjas: Movimientos · Instituciones · Diseñadores y obras (las obras sin diseñador visible van en esta última); (3) con «Diseñadores» solo: líneas de vida; con «Obras» solo: todas las obras como marcadores, agrupadas por disciplina (gráfico, producto, moda, arquitectura), y cada disciplina puede compartir su primera fila con la última de la anterior para usar menos filas; con ambos: obras sobre la línea de su diseñador, sin etiquetas; (4) las instituciones son barras de color propio (`--c-inst`, un neutro algo más azul) sin ícono, que terminan en punta de flecha; (5) las fichas de obra, diseñador, movimiento e institución tienen un botón de filtro «Ver solo sus conexiones»: esconde todo menos el elemento y todas sus relaciones directas (las curvas siguen si están encendidas); (6) el foco de contexto también esconde (ya no atenúa) el diseño no conectado; un diseñador se mantiene si tiene una obra conectada.
>
> **Actualización v11 (interfaz continua). Manda sobre el resto del documento donde lo contradiga.**
> 1. **Una sola línea continua de 1750 a hoy.** Se elimina «Antes de 1750» (época, carpeta y datos de prueba). Las épocas siguen existiendo como carpetas de datos, como fichas de panorama y como **barra de épocas** sobre el eje de años (clic: ficha de época + zoom a sus años); ya no hay botones de época ni flechas laterales.
> 2. **Cada elemento aparece una sola vez**, en la carpeta de la época donde **empieza** (inicio ≥ inicio de la época y < inicio de la siguiente; la última llega a hoy). Su fin puede caer en otra época: se dibuja entero. Ya no se exige `cont: true` para pasar el fin de la época; `cont: true` con `end` significa «sigue después de ese año» (flecha corta) y sin `end`, «sigue hasta hoy». No hay columna previa ni `pre`.
> 3. **La flecha de las barras largas es solo visual:** una barra de más de 30 años, o que ocuparía más del 75 % del ancho visible, se dibuja como punto + etiqueta + flecha; al elegirla se dibuja completa y lo que sigue en su fila baja. No aplica a los diseñadores (su línea de vida queda como está, por revisar).
> 4. **Sin carriles por disciplina (se reabre y revierte la decisión de la sección 2):** el diseño es un solo espacio con subfranjas plegables por tipo: Movimientos · Instituciones · Diseñadores y obras · Obras sin diseñador. La disciplina solo se ve en el marcador de la obra (forma y color); movimientos, instituciones y diseñadores van en tonos neutros. Se quitaron `lanes` y `lane` de los datos. Filtro de disciplinas: un diseñador se ve si alguna de sus disciplinas está activa o si tiene una obra visible, y en su línea solo se dibujan las obras de disciplinas activas; movimientos e instituciones se filtran por sus `disciplines`.
> 5. **Escala:** dos modos, lineal y «por densidad» (cada década mide 10 × max(1, √(n/2)) unidades, n = elementos que empiezan en ella; marcas en el eje donde cambia). Vista inicial: la línea completa. **Nivel de detalle según el zoom:** de lejos, épocas, movimientos y obras imprescindibles; las etiquetas aparecen solo cuando se leen bien. Las filas se reutilizan siempre, contando el ancho de la etiqueta.
> 6. **Sin dibujo del período de fabricación** (4.4): el dato queda solo en la ficha de la obra.
> 7. **Conexiones:** al elegir un elemento, curvas hacia sus relaciones directas, con tres botones (contexto, obras, otras); las de contexto en el color de su fila; nota al pasar el cursor; flecha si terminan en una sección cerrada o salen de la vista; vista tenue al pasar el cursor.
> 8. **Foco por fila de contexto** (complementa 4.6): botón junto al nombre de la fila y en la síntesis de la ficha de época; chip «Foco: … ✕»; uno a la vez; se combina con «Ver solo este movimiento».
> 9. **Modo `?editar`** (3.1): `editar.php` en el servidor con contraseña provisional en ese archivo; imagen por URL, revisión de fichas (revisada / observada), resumen y exportación. Ver `PROJECT.md`.
> 10. **Datos generados:** un solo `data/all.json` (sección 3.3). **Etiquetas muy breves:** el build avisa desde 22 caracteres; los diseñadores también pueden llevar `short` (sin traducción).
>
> **Actualización v10 (Fase 1).** El Modernismo está redactado con contenido real (245 elementos). Se eliminaron los enlaces con la LHA (sección 12). Un diseñador puede estar en el carril Interdisciplinario con dos disciplinas cuando así lo aprobó la persona responsable (el build avisa con WARN; se acepta y se explica).

# Línea de Historia del Diseño (LHD): especificación completa para construirla

> **Para quién es este documento.** Está escrito para Claude, en una sesión futura, como instrucción completa para construir un sitio nuevo: una línea de tiempo interactiva de la historia del diseño. Está en español para que la persona responsable del proyecto (docente universitaria/o en Chile) pueda leerlo y editarlo. Si al comenzar se adjunta el proyecto **LHA** (Línea de Historia del Arte, `LHA-completo-vNN.zip`), hay que reutilizar su código; si no, este documento basta para construir el sitio desde cero.
>
> **Cómo usarlo.** Adjunta este archivo (y, si lo tienes, el zip de LHA) y pega el mensaje de la sección 16.

---

## 1. Propósito y tesis

La LHD es una línea de tiempo bilingüe (español/inglés), estática y sin dependencias, para un curso universitario de historia del diseño.

**Tesis:** el diseño se entiende como respuesta a su contexto. Por eso la línea no es una galería de objetos célebres. Cada obra, diseñador, movimiento e institución se presenta enlazado a los hechos políticos, económicos, sociales, culturales y tecnológicos que la explican, y cada hecho de contexto existe en la línea solo porque afectó al diseño.

Criterios generales (heredados de LHA, decididos por la persona responsable):
- **Conciso, preciso, pertinente.** Mejor menos elementos y más fuertes que una lista exhaustiva.
- **Limpieza visual.** Etiquetas cortas, secciones colapsadas al entrar, sin decoración innecesaria.
- **Rigor.** Cada fecha y atribución verificada; ante la duda, se deja fuera. Fuentes abiertas y legales.

---

## 2. Decisiones ya tomadas (no reabrir)

| Tema | Decisión |
|---|---|
| Épocas | 5, en una sola línea continua (v11): Revolución Industrial (1750–1851) · Reforma (1851–1914) · Modernismo (1914–1945) · Posguerra (1945–1975) · Posmoderno (1975–hoy). «Antes de 1750» se eliminó |
| Filas de diseño | ~~Por disciplina~~ **Reabierta y revertida en v11:** un solo espacio de diseño con subfranjas por tipo (movimientos, instituciones, diseñadores y obras, obras sin diseñador); la disciplina solo en el marcador de la obra |
| Regiones | No son filas: son un **filtro** |
| Contexto | Bloque principal y muy visible, dividido en subcategorías: **Político, Económico, Social, Cultural, Tecnológico**; además **Producción** (materiales, procesos y herramientas del diseño) y **Teórico** (textos del diseño) |
| Ambiental | No es fila propia: se reparte entre **Social** y **Económico** |
| Tecnología | **Separada en dos**: Tecnológico (tecnología general: energía, transporte, comunicaciones, computación) y Producción (con qué y cómo se diseña y fabrica) |
| Instituciones | **No son contexto**: van en la línea de diseño, junto con diseñadores y obras (escuelas, empresas, estudios, exposiciones, asociaciones, museos, revistas) |
| Regla obligatoria | **Todo elemento de contexto debe enlazar con al menos un elemento de diseño**, con una nota que explique el vínculo. El build falla si no se cumple |
| Autoría | Cada obra distingue **diseñador o estudio** y **fabricante o cliente**; se admiten obras anónimas o corporativas |
| Fechas | Cada obra distingue **año de diseño** y **período de fabricación** cuando corresponde |
| Dónde verla | Colecciones de diseño (MoMA, V&A, Cooper Hewitt, Vitra Design Museum, Design Museum de Londres, Die Neue Sammlung…) y estado actual (en producción, en uso, demolida…) |
| Imágenes | Se acepta que serán más escasas que en arte (derechos de autor); se compensa con enlaces a colecciones |

Disciplinas: el **mobiliario** va en Producto; el **textil** en Moda; **interiores** en Arquitectura; **interfaces y diseño digital** en Gráfico.

---

## 3. Base técnica

### 3.1 Si se dispone del proyecto LHA (recomendado)

LHA es un sitio estático (`index.html`, `app.js`, `style.css`) sin librerías. Sus datos se escriben a mano en `src-data/<época>/*.json` y `tools/build_data.py` los combina en `data/<época>.json` y `data/index.json` (índice global para búsqueda y estadísticas). Leer primero `PROJECT.md`, `tools/ERA-SPEC.md` y `tools/GUIDE-TECH-THEORY.md` de LHA.

Qué se reutiliza tal cual o casi:
- Navegación por épocas (botones arriba; flechas de época anterior/siguiente en los bordes).
- Escala lineal por época, zoom (Ctrl + rueda, teclas + y −), carriles colapsables, botones expandir/colapsar todo.
- **Todas las secciones y subsecciones colapsadas al entrar a una época**; quien navega las abre.
- Panel lateral de fichas redimensionable, con X para cerrar y Esc.
- **Ficha general** con botón (i) a la derecha del botón de idioma; **se abre cada vez que se carga la página**, salvo que la dirección apunte a un elemento (`#id`).
- Búsqueda global entre épocas, enlaces directos `#id`, tema claro/oscuro, aviso "solo computador".
- Bilingüe: textos de interfaz en un diccionario `UI.en / UI.es`; datos con campos en inglés y su traducción en `es: {…}`.
- Fichas con secciones, chips de elementos relacionados, conexiones (`from`, `to`, `note`), conceptos.
- Imágenes desde la API de Wikipedia (imagen de la página), con alternativa en Wikimedia Commons.
- Etiquetas de Teoría = **solo el apellido del autor**.

Qué se cambia (ver secciones 4 y 5):
- `ERAS`: las 6 épocas de la LHD.
- El bloque de contexto pasa de 1 fila de hechos a 5 filas temáticas + Productivo (antes «Producción») + Teórico.
- `MEDIA` (pintura/escultura/arquitectura/artes decorativas) pasa a `DISCIPLINES` (gráfico/producto/moda/arquitectura).
- Nuevo tipo de elemento: **institución**.
- Nuevo tipo de relación: **enlace de contexto** (contexto → diseño, con nota).
- Nuevos campos de obra: autoría múltiple, fabricante, período de fabricación, colecciones.
- Filtros: subcategorías de contexto, disciplinas, regiones (varias), tipo de elemento, imprescindibles (sin lente de contexto, ver 4.6).
- No copiar el modo de edición de imágenes de LHA (`imagenes.php`) tal como está: tenía la contraseña escrita en el código. Si se quiere un modo de edición, la clave debe vivir fuera del código publicado.

### 3.2 Si no se dispone de LHA

Construir el mismo modelo: sitio estático en HTML/CSS/JS sin dependencias, datos en JSON, un script de build en Python que valida y combina, y un servidor estático simple para probar (`python3 -m http.server`). Seguir este documento como especificación funcional.

### 3.3 Estructura de carpetas

```
lhd/
  index.html  app.js  style.css
  data/                      ← generado por el build (no editar a mano)
    all.json                 ← v11: toda la línea (épocas, elementos con su campo era, enlaces,
                               conexiones, índice de búsqueda y estadísticas por época)
  src-data/<era>/            ← datos escritos a mano
    01-structure.json        ← época, filas de contexto, resumen de contexto (sin carriles desde v11)
    02-movements.json
    03-institutions.json
    10-…19 designers-and-works-<disciplina>.json
    40-context-political.json   41-context-economic.json   42-context-social.json
    43-context-cultural.json    44-context-technological.json
    50-production-materials.json  51-production-processes.json  52-production-tools.json
    56-theory.json
    60-concepts.json
    80-context-links.json    ← enlaces contexto → diseño (obligatorios)
    85-connections.json      ← conexiones generales (influencias, respuestas)
  tools/build_data.py
  PROJECT.md                 ← decisiones y bitácora de avances
  tools/SPEC.md              ← este documento, actualizado
```

---

## 4. Estructura visual de la línea

### 4.1 Épocas

| id | Español | English | Inicio | Fin | Eje de la época |
|---|---|---|---|---|---|
| `industrial` | Revolución Industrial | Industrial Revolution | 1750 | 1851 | Mecanización y división del trabajo: quien diseña se separa de quien fabrica |
| `reform` | Reforma | Reform | 1851 | 1914 | Reacción contra la mala calidad industrial; nacen la marca, la publicidad y la profesión |
| `modernism` | Modernismo | Modernism | 1914 | 1945 | La máquina como modelo; vanguardias; estandarización; diseño, política y crisis |
| `postwar` | Posguerra | Post-war | 1945 | 1975 | Reconstrucción, consumo y Guerra Fría; buen diseño, identidad corporativa, método; diseño y desarrollo en el Sur |
| `postmodern` | Posmoderno | Postmodern | 1975 | hoy (año actual) | Crisis del funcionalismo; globalización y marca; revolución digital; sostenibilidad; interacción y servicios |

\* *(Obsoleto desde v11: no hay época anterior a 1750 ni columna previa.)* **Recomendación original para la primera época:** que la escala empiece en 1450 (imprenta de tipos móviles) y que los antecedentes anteriores (escritura, alfabeto, papel, xilografía, tipos móviles; los de Asia solo como antecedente y con región `global`) se muestren en la **columna previa** de la época, con flecha a la izquierda, como hace LHA con las tecnologías que vienen de antes. Así 3.000 años de antecedentes no aplastan los 300 años centrales. Confirmar con la persona responsable (sección 15).

Reglas de pertenencia a una época:
- Un elemento pertenece a la época en que **empieza** (el build lo exige: inicio ≥ inicio de la época y < inicio de la siguiente). Para los diseñadores, la época de su actividad principal.
- Las barras que pasan el fin de la época se dibujan enteras en la línea continua (v11); si son largas, se abrevian en pantalla con una flecha que es solo visual.
- Si un elemento importante sigue vigente en la época siguiente, se crea una ficha nueva con **id distinto** centrada en lo que cambió (los ids son únicos en todo el sitio).

### 4.2 Bloques y filas

```
CONTEXTO
  Político          guerras, revoluciones, regímenes, políticas de Estado, leyes
  Económico         industrialización, mercados, crisis, consumo, comercio, globalización, recursos
  Social            urbanización, trabajo, género, vida doméstica, migraciones, salud, medio ambiente
  Cultural          movimientos artísticos, medios (prensa, cine, radio, TV, internet), ideas, ocio
  Tecnológico       energía, transporte, comunicaciones, computación (tecnología general)
  Productivo        ▸ Materiales  ▸ Procesos  ▸ Herramientas   (con qué y cómo se diseña y fabrica)
  Teórico           textos del diseño: manifiestos, tratados, libros, programas de escuelas
DISEÑO (v11: un solo espacio, sin carriles por disciplina)
  Movimientos           barras de borde difuso, tono neutro
  Instituciones         barras de borde marcado con ícono, tono neutro
  Diseñadores y obras   líneas de vida con sus obras encima (forma y color por disciplina)
  Obras sin diseñador   anónimas, o cuyo diseñador está oculto por un filtro
```

*Texto anterior a v11 (carriles Interdisciplinario, Gráfico, Producto, Moda, Arquitectura): se conserva abajo solo como registro.*

- **Etiquetas de las filas de contexto:** usar adjetivos paralelos (Político, Económico, Social, Cultural, Tecnológico) y los sustantivos Producción y Teórico, que corresponden a los dos tipos de ficha existentes ("tecnología" y "teoría"). En inglés: Political, Economic, Social, Cultural, Technological, Production, Theoretical.
- **Interdisciplinario** cumple el papel del carril "Paneuropeo" de LHA. Allí van Arts and Crafts, art nouveau, Werkbund, Bauhaus, Ulm, Memphis, el Good Design y los diseñadores que trabajan en tres o más disciplinas (p. ej., Peter Behrens).
- **Dentro de cada carril de diseño**, de arriba abajo:
  1. Movimientos y estilos (barras con borde difuso, como los periodos de LHA).
  2. Instituciones (barras de otro estilo: borde marcado, sin relleno o con trama suave, y un ícono pequeño según el tipo: escuela, empresa, estudio, exposición, asociación, museo, revista).
  3. Diseñadores (líneas de vida, con sus obras como marcadores sobre la línea).
  4. Obras sin diseñador en la época (anónimas, corporativas o de diseñadores de otra época) como marcadores sueltos.
- **Arquitectura** se limita a lo que la historia del diseño necesita: vivienda y construcción industrializada, edificios-manifiesto, interiores y ciudad. Las grandes obras ya presentes en LHA se enlazan (sección 12), no se repiten con largos textos.

### 4.3 Marcadores, formas y colores

- **Forma por disciplina** (como los medios en LHA): Gráfico = círculo · Producto = rombo · Moda = triángulo · Arquitectura = cuadrado.
- **Color por disciplina** en los marcadores de obra (4 colores suaves y accesibles en tema claro y oscuro).
- **Color por subcategoría de contexto:** a diferencia de LHA (contexto gris), aquí cada fila de contexto tiene un tono propio, apagado, que se usa en sus marcadores, en el título de sus fichas y en la sección "Contexto" de las obras: Político (rojo óxido), Económico (ocre), Social (verde), Cultural (violeta), Tecnológico (azul pizarra), Producción (gris acero), Teórico (tinta). Validar contraste en ambos temas.
- **Imprescindibles:** estrella, como en LHA.

### 4.4 Período de fabricación

*v11: ya no se dibuja en la línea; el dato queda solo en la ficha de la obra.*

Una obra de diseño tiene un **año de diseño** (marcador) y, si se fabricó en serie, un **período de fabricación**: se dibuja una línea fina desde el marcador hasta el fin de la producción, o hasta el borde de la época con flecha si sigue fabricándose (p. ej., silla Thonet n.º 14, 1859 → hoy). Esto deja ver de un vistazo qué perduró y qué fue efímero. Agregar un interruptor "Período de fabricación" para ocultar estas líneas si la vista se carga.

### 4.5 Filtros (chips)

Fila de chips, como en LHA:
1. **Contexto:** Político · Económico · Social · Cultural · Tecnológico · Productivo · Teórico.
2. **Disciplinas:** Gráfico · Producto · Moda · Arquitectura (con su forma).
3. **Regiones** (selección múltiple): Europa · Norteamérica · América Latina. Los elementos `global` se ven siempre. **Alcance:** la LHD solo cubre Europa, Norteamérica y América Latina (más lo `global`); no hay regiones de Asia, África y Medio Oriente ni Oceanía, y no se incluyen elementos propios de ellas. No hay chip de Chile (queda dentro de América Latina).
4. **Tipo de elemento:** Movimientos · Instituciones · Diseñadores · Obras.
5. **Imprescindibles.**

### 4.6 Contexto en la ficha de la época (reemplaza a la lente)

Se descartó el selector «Ver el diseño desde» (lente). En su lugar, la ficha de la época reúne siempre, en este orden: idea central, *Cambios clave* (`shifts`) y *El contexto en síntesis* con las cinco subcategorías (`context_summary`, ver 5.1), aunque la ficha quede larga. Para leer la época desde un solo tipo de contexto se usan los chips de *Contexto* (muestran u ocultan filas) y el resaltado contexto ↔ diseño al seleccionar un hecho.

### 4.7 Interacción y fichas

- Al seleccionar un elemento de contexto se **iluminan** los elementos de diseño que explica; al seleccionar una obra se iluminan sus elementos de contexto. LHA ya resalta relaciones; hay que alimentar el índice con los enlaces de contexto.
- **Ficha de obra:** tipo (disciplina · tipo de objeto), título, autoría y año, imagen, *Idea clave*, **Contexto** (alto en la ficha, agrupado por subcategoría, cada enlace con su nota), *Análisis*, *Diseño y producción* (diseñador/estudio, fabricante/cliente, materiales y procesos con enlaces a Producción, período de fabricación), *Movimiento e institución*, *Conexiones*, *Estado actual* (sección propia, como Análisis o Diseño y producción), *Dónde verla* (colecciones), *Ver en la línea de arte* (si existe), *Saber más*.
- **Ficha de contexto:** subcategoría, nombre, fecha, *Qué pasó*, **Efecto en el diseño** (obligatorio), **Diseño relacionado** (lista de elementos con la nota de cada enlace), *Conexiones*, *Saber más*.
- **Ficha de diseñador:** fechas, disciplinas, *Biografía*, obras, movimientos, instituciones, contexto (derivado de sus obras).
- **Ficha de institución:** tipo, fechas, lugar, *Idea clave*, *Historia*, personas, obras, contexto.
- **Ficha de movimiento:** como el periodo en LHA: idea clave, cómo reconocerlo, contexto, el cambio, artistas y obras clave. Lleva un **botón de filtro** («Ver solo este movimiento», como el filtro por estilo de LHA): deja en la línea solo el movimiento, sus diseñadores, obras e instituciones y los hechos de contexto, producción y teoría vinculados con ellos; aparece un chip «Solo: nombre ✕» en los filtros para volver a ver todo. Se desactiva al cambiar de época o al elegir algo fuera del conjunto.
- **Colores de la ficha:** el título, el sobretítulo y los encabezados van en tonos neutros; el color de la disciplina o del contexto solo aparece en marcadores pequeños (cuadrados y puntos), no en el texto.
- **Ficha de Producción y de Teoría:** como las de tecnología y teoría de LHA (sección 5).
- **Panorama de la época** (sin nada seleccionado): visión general, cambios clave, **el contexto en síntesis** (una frase por subcategoría), estadísticas y conceptos.
- **Ficha general (i):**
  - presentación de la línea y su tesis;
  - las secciones con una descripción muy breve de cada una (Político, Económico, Social, Cultural, Tecnológico, Producción, Teórico; Interdisciplinario, Gráfico, Producto, Moda, Arquitectura; movimientos, instituciones, diseñadores, obras, conceptos, conexiones);
  - datos generales: totales, obras por disciplina, contexto por subcategoría, tabla por época con enlace a cada una, y el porcentaje de obras con enlace de contexto.

---

## 5. Modelo de datos

Convenciones (de LHA):
- Ids en minúsculas con guiones, **únicos en todo el sitio**. Prefijos: `th-` para teoría; `ctx-` para contexto (recomendado); `inst-` para instituciones (recomendado).
- Años como enteros (negativo = a. C.); `date` es texto para mostrar ("c. 1925", "1925–26", "desde 1859").
- Campos de texto en inglés y su traducción completa en `es: {…}`.
- `wiki`: solo un título de Wikipedia en inglés que se haya comprobado que existe (de ahí sale la imagen).

### 5.1 Estructura de época (`01-structure.json`)

```json
{
 "era": { "id": "modernism", "start": 1914, "end": 1945,
   "name": "Modernism", "intro": "…", "shifts": ["…", "…"],
   "context_summary": { "political": "…", "economic": "…", "social": "…", "cultural": "…", "technological": "…" },
   "es": { "name": "Modernismo", "intro": "…", "shifts": ["…"], "context_summary": { "political": "…", "economic": "…", "social": "…", "cultural": "…", "technological": "…" } } },
 "tracks": [
   { "id": "political", "label": "Political", "es": { "label": "Político" } },
   { "id": "economic", "label": "Economic", "es": { "label": "Económico" } },
   { "id": "social", "label": "Social", "es": { "label": "Social" } },
   { "id": "cultural", "label": "Cultural", "es": { "label": "Cultural" } },
   { "id": "technological", "label": "Technological", "es": { "label": "Tecnológico" } }
 ]
}
```

*v11: ya no hay lista `lanes` (la clave se rechaza).*

### 5.2 Movimiento (`02-movements.json`)

```json
{ "id": "bauhaus-movement", "disciplines": ["graphic","product","architecture"],
  "start": 1919, "end": 1933, "fadeIn": 2, "fadeOut": 3, "regions": ["europe"], "countries": ["DE"],
  "name": "…", "short": "…", "key": "…", "traits": ["…"], "context": "…", "shift": "…", "wiki": "…",
  "es": { "name": "…", "short": "…", "key": "…", "traits": ["…"], "context": "…", "shift": "…" } }
```

### 5.3 Institución (`03-institutions.json`)

```json
{ "id": "inst-bauhaus", "kind": "school", "disciplines": ["graphic","product","architecture"],
  "start": 1919, "end": 1933, "place": "Weimar, Dessau, Berlin", "regions": ["europe"], "countries": ["DE"],
  "name": "Bauhaus", "short": "Bauhaus", "key": "…", "more": "…", "wiki": "Bauhaus",
  "links": { "designers": ["gropius", "…"], "works": ["…"] },
  "es": { "name": "Bauhaus", "short": "Bauhaus", "key": "…", "more": "…", "place": "Weimar, Dessau, Berlín" } }
```

Valores de `kind`: `school` (escuela), `company` (empresa o fabricante), `studio` (estudio o agencia), `exhibition` (exposición o feria), `association` (asociación, grupo, premio), `museum` (museo o colección), `publication` (revista o editorial). `end: null` = sigue activa.

### 5.4 Diseñador

```json
{ "id": "schutte-lihotzky", "kind": "person", "disciplines": ["architecture","product"],
  "born": 1897, "died": 2000, "dates": "1897–2000", "countries": ["AT"], "regions": ["europe"],
  "name": "Margarete Schütte-Lihotzky", "movements": ["…"], "institutions": ["inst-neues-frankfurt"],
  "key": "…", "more": "…", "wiki": "Margarete_Schütte-Lihotzky",
  "es": { "key": "…", "more": "…", "dates": "1897–2000" } }
```

`kind`: `person`, `duo` (p. ej., Charles y Ray Eames), `collective`. Los estudios y empresas son **instituciones**, no diseñadores. Desde v11 no hay carril (`lane`); `disciplines` decide el filtro. Un `short` opcional (sin traducción, p. ej. «Moholy-Nagy») acorta el nombre en la línea.

### 5.5 Obra

```json
{ "id": "frankfurt-kitchen", "discipline": "architecture", "type": "interior",
  "title": "Frankfurt Kitchen", "designers": ["schutte-lihotzky"], "maker": "inst-neues-frankfurt", "client": null,
  "year": 1926, "date": "1926", "production": { "from": 1926, "to": 1930, "note": "about 10,000 installed" },
  "regions": ["europe"], "countries": ["DE"], "star": true,
  "materials": "…", "tech": ["fitted-kitchen-process"],
  "key": "…", "more": "…",
  "where": [ { "label": "MAK, Vienna", "url": "https://…" } ], "status": "reconstructions in museums",
  "wiki": "Frankfurt_kitchen",
  "es": { "title": "Cocina de Frankfurt", "date": "1926", "materials": "…", "key": "…", "more": "…", "status": "…",
          "production": { "note": "unas 10.000 instaladas" } } }
```

- `type`: lista abierta por disciplina. Gráfico: cartel, tipografía, libro, revista, identidad, logotipo, señalética, mapa o gráfico de información, sello o billete, envase, interfaz. Producto: mueble, lámpara, utensilio, aparato, máquina, vehículo, juguete. Moda: prenda, colección, accesorio, textil, calzado. Arquitectura: edificio, vivienda, interior, conjunto, ciudad.
- `designers` puede estar vacío (obra anónima o corporativa); en ese caso `maker` o `client` deben indicar quién la produjo.
- `production`: omitir en obras únicas (un cartel, un edificio). `to: null` = sigue en producción.
- Las cifras de `production.note` son textos cortos y solo si se verificaron.
- `posthumous: true` (v46, etapa 7): obra terminada o publicada después de la muerte de su autor (p. ej. el *Manuale tipografico* de Bodoni, 1818). El build no comprueba entonces que `year` caiga dentro de la vida del diseñador; `date` y el texto deben explicarlo.

### 5.6 Elemento de contexto (`40-…44-context-*.json`)

```json
{ "id": "ctx-weimar-housing", "track": "social", "start": 1919, "end": 1933, "date": "1919–1933",
  "regions": ["europe"], "countries": ["DE"],
  "name": "Housing shortage and social housing in Weimar Germany", "short": "Housing shortage",
  "key": "…", "happened": "…", "effect": "…", "wiki": "…",
  "es": { "name": "…", "short": "Falta de vivienda", "date": "1919–1933", "key": "…", "happened": "…", "effect": "…" } }
```

- `track`: `political`, `economic`, `social`, `cultural`, `technological`.
- `effect` (Efecto en el diseño) es **obligatorio**: una a tres frases sobre cómo este hecho cambió el diseño.
- Los hechos puntuales tienen solo `start`; los procesos tienen `start` y `end` y se dibujan como barra.

### 5.7 Producción (`50-…52-production-*.json`)

Mismo formato que las tecnologías de LHA:

```json
{ "id": "tubular-steel", "sub": "materials", "start": 1925, "end": 1945, "cont": true, "regions": ["europe"],
  "wiki": "…", "date": "1925 →", "name": "…", "short": "…",
  "key": "…", "origin": "…", "enabled": "…", "change": "…", "economy": "…", "relations": "…",
  "links": { "movements": [], "institutions": [], "designers": [], "works": [] },
  "es": { "name": "…", "short": "…", "date": "1925 →", "key": "…", "origin": "…", "enabled": "…", "change": "…", "economy": "…", "relations": "…" } }
```

`sub`: `materials`, `processes`, `tools`. Las secciones de la ficha son: qué es, origen, qué permitió, **cómo cambió el diseño**, economía (opcional) y relación con el diseño.

### 5.8 Teoría (`56-theory.json`)

Mismo formato que las teorías de LHA: `id` (`th-…`), `year`, `date`, `regions`, `genre`, `author`, `name`, **`short` = solo el apellido**, `key`, `ideas` (3–5), `impact`, `links`, `sources` (`[{label, es, url}]`, al menos un enlace https), `wiki`, `es`.

Géneros (`genre`): `manifesto` (manifiestos y programas), `criticism` (crítica), `history` (historia del diseño), `method` (métodos y práctica del diseño), `pedagogy` (programas de escuelas), `typography` (tipografía y diseño gráfico), `architecture`, `society` (diseño, sociedad y ética).

### 5.9 Enlace de contexto (`80-context-links.json`)

```json
{ "links": [
  { "ctx": "ctx-weimar-housing", "item": "frankfurt-kitchen",
    "note": "Built for the social housing estates of Neues Frankfurt, where small, standardised flats needed an efficient kitchen.",
    "es": { "note": "Hecha para los conjuntos de vivienda social del Nuevo Frankfurt, donde departamentos pequeños y estandarizados necesitaban una cocina eficiente." } }
] }
```

- `ctx` = elemento de contexto (político, económico, social, cultural o tecnológico). `item` = obra, diseñador, movimiento o institución.
- La nota explica **el porqué** del vínculo en una o dos frases (máximo ~200 caracteres).
- Se admiten enlaces **entre épocas** (p. ej., el taylorismo de 1911 explica la cocina de 1926). Desde v11 todo va en un solo `data/all.json`, así que no hay que duplicar nada.

### 5.10 Conexiones y conceptos

- Conexiones (`85-connections.json`): `{from, to, note, es:{note}}` entre cualquier par de elementos (influencias, respuestas, continuidades). Pueden cruzar épocas.
- Conceptos (`60-concepts.json`): `{id, name, terms, key, wiki, es}`. Por ejemplo: la forma sigue a la función, estandarización, obra de arte total, Good Design, aerodinámica (streamlining), obsolescencia planificada, identidad corporativa, retícula, ergonomía, diseño centrado en el usuario, sostenibilidad, diseño universal, diseño participativo, *branding*.

---

## 6. Reglas de validación del build

El build debe imprimir `PROBLEM` (y no dar por terminada la época) si:
1. Un id se repite en el sitio.
2. **Un elemento de contexto no tiene al menos un enlace de contexto**, o le falta `effect`.
3. Un enlace de contexto apunta a ids inexistentes, o su `ctx` no es contexto, o su `item` no es de diseño.
4. Un elemento de Producción o Teoría no tiene ningún enlace; una teoría no tiene fuente https.
5. Falta cualquier campo de texto en `es`, o un `es` tiene campos distintos a los del inglés.
6. Una obra no tiene `designers` ni `maker` ni `client`.
7. El año de inicio cae fuera de la época de su carpeta (v11: inicio ≥ inicio de la época y < inicio de la siguiente; el fin puede caer en otra época), o un fin es anterior al inicio o posterior a hoy.
8. Una `track`, `discipline`, `genre`, `kind` o región no está en la lista permitida (`europe`, `north-america`, `latin-america`, `global`).

Y debe imprimir `WARN` (sin bloquear) si:
- una obra **imprescindible** no tiene enlaces de contexto (la meta es que todas tengan al menos uno);
- una subcategoría de contexto tiene menos de 4 elementos en la época;
- una ficha supera los largos recomendados;
- una etiqueta de la línea (`short`, o el nombre si no hay `short`) pasa de 22 caracteres (v11).

Además, el build calcula estadísticas por época (para el panorama y la ficha general): elementos por tipo, obras por disciplina, contexto por subcategoría, imprescindibles y porcentaje de obras con contexto.

---

## 7. Estilo de redacción

- El inglés es el texto principal; `es` es una traducción completa y natural, en **español de Chile/neutro** ("costo", no "coste"; "computador"; "departamento"; "auto").
- Largos como en LHA: `key` = una oración (~130–160 caracteres); los demás campos, una a tres oraciones; `effect`, una a tres; notas de enlace, una o dos.
- **Sin paréntesis** en `name`, `title`, `short`, `date`, `author` ni etiquetas de fuentes: usar «:» para precisar (p. ej., «Silla Wassily: modelo B3», «1931: publicada en 1933») o «·» para separar. El build avisa (`WARN`).
- **Nombres cortos por sí solos:** `name` y `title` son el nombre breve y reconocible («Nuevo Frankfurt», no «Nuevo Frankfurt: programa municipal de construcción»); lo que el elemento *es* va en `key` y `more`. Evitar «:» con explicación y pasar de ~40 caracteres (el build avisa). Los textos corridos, incluido `status`, empiezan con mayúscula.
- **Etiquetas de la línea de tiempo breves:** lo que se dibuja es `short` (si no existe, `name` o `title`); aspirar a 28 caracteres o menos y a dos o tres palabras. Las obras también pueden llevar `short` (con su `es.short`). La información larga va en la ficha.
- Apóstrofo tipográfico (’) y raya corta para rangos (–). En español: "a. C.", miles con punto (45.000), "→" para "continúa".
- Hechos concretos (nombres, fechas, lugares, obras); nada de relleno.
- **Siempre mostrar el vínculo con el contexto**: en `context` de los movimientos, en `more` de las obras y en todas las notas. Evitar el determinismo simple: usar "influencia, no causa estricta" cuando corresponda, como en LHA.
- Incluir a las mujeres diseñadoras y a quienes trabajaban en colectivos o empresas (a menudo invisibilizados), y obras anónimas cuando son importantes.

---

## 8. Fuentes, imágenes y verificación

- **Verificar cada fecha, atribución y cifra.** Ante la duda, dejarla fuera e informarlo.
- Fuentes de consulta: Wikipedia (como punto de partida, no como única fuente), colecciones de museos (MoMA, V&A, Cooper Hewitt, Vitra Design Museum, Design Museum, Die Neue Sammlung, Museum für Gestaltung Zürich, Bauhaus-Archiv), Britannica, archivos de escuelas y empresas, ICAA (documentos de arte latinoamericano), Memoria Chilena (Biblioteca Nacional de Chile).
- **Teoría:** enlazar digitalizaciones abiertas y legales (Internet Archive en acceso libre —no "Borrow"—, Project Gutenberg, Wikisource, Gallica, HathiTrust, Biblioteca Digital Hispánica, Memoria Chilena, ICAA, sitios oficiales de fundaciones y museos). Si el texto tiene derechos vigentes, enlazar una página informativa oficial o de Wikipedia ("Sobre el texto"). Nunca sitios piratas.
- **Imágenes:** las da la API de Wikipedia (`wiki`) o Wikimedia Commons; no copiar imágenes con derechos al repositorio. Para obras sin imagen libre, la ficha muestra "Ver en la colección" con enlace al museo.
- **Herramientas:** la web se consulta con las herramientas de búsqueda y lectura de la sesión, de a pocas páginas por vez, porque hay límites de peticiones. Para archive.org, verificar ediciones con `https://archive.org/metadata/<id>/metadata`.
- Al final de cada entrega, listar en español qué no se pudo verificar.

---

## 9. Tamaños objetivo por época

Orientativos; la calidad manda. Las primeras épocas son más pequeñas.

| Época | Contexto (por subcategoría) | Producción | Teoría | Movimientos | Instituciones | Diseñadores | Obras |
|---|---|---|---|---|---|---|---|
| ~~Antes de 1750~~ (eliminada) | 4–6 | 10–15 | 5–8 | 4–6 | 6–10 | 10–20 | 30–50 |
| Revolución Industrial | 5–8 | 12–18 | 6–10 | 6–8 | 8–12 | 15–25 | 40–60 |
| Reforma | 6–10 | 15–20 | 8–12 | 8–12 | 12–18 | 30–45 | 60–90 |
| Modernismo | 6–10 | 15–20 | 12–18 | 10–14 | 15–20 | 45–70 | 90–130 |
| Posguerra | 6–10 | 15–20 | 12–18 | 12–16 | 18–25 | 50–80 | 100–150 |
| Posmoderno | 6–10 | 15–20 | 12–18 | 10–14 | 15–22 | 45–70 | 90–140 |

Equilibrio deseado: unas **4 disciplinas con presencia real** en cada época desde 1750; **América Latina presente** en todas las épocas, sin forzar (sección 10.7). La meta anterior de 20–30 % fuera de Europa y EE. UU. se retira, porque el alcance regional ya no incluye Asia, África ni Oceanía; la proporción de América Latina se fija con la persona responsable.

---

## 10. Contenido inicial por época

Las listas siguientes son **puntos de partida para proponer, no listas finales**: hay que verificarlas, recortarlas y mostrarlas a la persona responsable antes de redactar. Las marcadas *(verificar)* son dudosas.

### 10.1 Antes de 1750 (eliminada en v11; se conserva como registro, no se redacta)

- **Antecedentes:** escritura cuneiforme (c. 3200 a. C.), alfabeto fenicio (c. 1050 a. C.), capitales romanas de la Columna de Trajano (113), papel en China (tradición: 105), Sutra del Diamante impreso (868), tipos móviles de Bi Sheng (c. 1040) y de Corea (Jikji, 1377), quipus andinos como registro de información. (Los antecedentes de Asia —papel, Sutra del Diamante, tipos móviles de Bi Sheng y de Corea— solo se incluyen si explican la imprenta europea, con región `global`.)
- **Político:** Reforma protestante (1517) e imprenta como propaganda; Contrarreforma; conquista de América y primeras imprentas coloniales (México 1539, Lima 1584); privilegios reales de impresión; monarquías absolutas y manufacturas reales.
- **Económico:** gremios y aprendizaje; Compañías de las Indias (1600, 1602) y llegada de porcelana china y telas indias (chintz) que cambian el gusto europeo; mercantilismo (Colbert, Gobelinos 1662).
- **Social:** alfabetización creciente; vida urbana y cortesana; leyes suntuarias sobre el vestido.
- **Cultural:** humanismo (de la letra humanística a la romana), Renacimiento, Barroco; ciencia ilustrada (Vesalio, 1543).
- **Tecnológico:** relojería y mecánica, navegación, óptica, energía hidráulica y eólica.
- **Producción:** tipos móviles, fundición de tipos y prensa; xilografía; grabado en cobre; papel de trapo; telar de tiro; estampado de telas con tacos; ebanistería y torno; cartografía.
- **Teórico:** Durero, *Underweysung der Messung* (1525, construcción de letras); Geofroy Tory, *Champ fleury* (1529); Comenius, *Orbis pictus* (1658, libro ilustrado para niños: diseño de información); Moxon, *Mechanick Exercises… of Printing* (1683–84); Vecellio, libro de trajes (1590).
- **Instituciones:** taller de Gutenberg (Maguncia); imprenta aldina (Venecia, 1494); Plantin (Amberes, 1555); Imprimerie royale (1640); Gobelinos (1662).
- **Diseñadores:** Gutenberg, Nicolas Jenson, Aldo Manucio y Francesco Griffo, Claude Garamond, Robert Granjon, Christophe Plantin, Philippe Grandjean, William Caslon, André-Charles Boulle.
- **Obras:** Biblia de 42 líneas (c. 1455); romana de Jenson (1470); *Hypnerotomachia Poliphili* (1499); Virgilio en cursiva (1501); mapa de Mercator (1569); *Orbis pictus* (1658); Romain du Roi (desde 1692); muestrario de Caslon (1734); mobiliario de Boulle; *robe à la française* (moda, siglo XVIII).

### 10.2 Revolución Industrial (1750–1851)

- **Político:** revoluciones de EE. UU. (1776) y Francia (1789) y sus símbolos; sistema métrico (1795); Imperio napoleónico; independencias latinoamericanas (1810–1825): banderas, escudos, prensa patriota.
- **Económico:** división del trabajo (Adam Smith, 1776); sistema de fábrica; algodón y comercio colonial; patentes y registro de diseños (leyes británicas de 1839 y 1842 *(verificar)*); consumo de clase media.
- **Social:** urbanización y clase obrera; trabajo infantil; tiempo de reloj; ludismo (1811–1816).
- **Cultural:** Ilustración y *Encyclopédie*; neoclasicismo (Pompeya); romanticismo y neogótico; prensa periódica.
- **Tecnológico:** máquina de vapor de Watt; ferrocarril (1825, 1830); telégrafo (1837, 1844); fotografía (1839).
- **Producción:** loza y porcelana industrial (Wedgwood); hierro fundido; estampado textil con cilindros (1783); telar Jacquard con tarjetas perforadas (1804); máquina de papel continuo (c. 1803); prensa de hierro (Stanhope) y prensa a vapor (1814); litografía (1796); grabado en madera de testa (Bewick); tipos gruesos, egipcios y de palo seco (1816); piezas intercambiables.
- **Teórico:** Chippendale, *The Gentleman and Cabinet-Maker’s Director* (1754); láminas de oficios de la *Encyclopédie* (1751–1772); Hepplewhite (1788) y Sheraton (1791–1794); Pugin, *True Principles* (1841); *Journal of Design and Manufactures* (1849–1852).
- **Movimientos:** neoclasicismo; estilo Imperio y Regencia; Biedermeier; neogótico; diseño shaker.
- **Instituciones:** Wedgwood (Etruria, 1769); Soho Manufactory de Boulton (1766); Sèvres y Meissen; Stamperia de Bodoni (Parma, 1768); Conservatoire des arts et métiers (1794); Government School of Design (Londres, 1837); Thonet (1819); *Ackermann’s Repository* (1809–1828).
- **Diseñadores:** Josiah Wedgwood, Matthew Boulton, Thomas Chippendale, Robert Adam, John Baskerville, Giambattista Bodoni, Firmin Didot, Thomas Bewick, Percier y Fontaine, Karl Friedrich Schinkel, A. W. N. Pugin, Michael Thonet, Rose Bertin (moda).
- **Obras:** Virgilio de Baskerville (1757); *Manuale tipografico* de Bodoni (1818); loza Queen’s ware; silla Windsor y silla shaker; tarjetas Jacquard; Penny Black, primer sello adhesivo (1840); grabados de moda en revistas; silueta Imperio; Crystal Palace (1851, enlazar a LHA).
- **América Latina y Chile:** *La Aurora de Chile* (1812), primera imprenta y periódico del país; *Gaceta de Buenos Aires* (1810); símbolos patrios.

### 10.3 Reforma (1851–1914)

- **Político:** exposiciones universales como escaparate imperial (1851, 1867, 1889, 1900); unificaciones de Italia y Alemania.
- **Económico:** segunda revolución industrial; marcas registradas (ley británica de 1875; el triángulo de Bass, 1876); grandes almacenes (Bon Marché, 1852); venta por catálogo; publicidad; taylorismo (1911); cadena de montaje de Ford (1913).
- **Social:** vivienda obrera y movimiento obrero; mujeres en oficinas (máquina de escribir); hogar burgués e higiene; ocio urbano.
- **Cultural:** japonismo; esteticismo; prensa ilustrada; fotografía popular (Kodak, 1888); cine (1895).
- **Tecnológico:** electricidad y luz eléctrica (1879); teléfono (1876); automóvil (1886); bicicleta de seguridad (1885); máquina de escribir (1874).
- **Producción:** madera curvada; cromolitografía y cartel; linotipia (1886) y monotipia (1887); fotograbado de medio tono (década de 1880); máquina de coser (Singer, 1851); aluminio (1886); celuloide (1870); patrones de papel (Butterick, 1863); vidrio artístico; acero y hormigón armado.
- **Teórico:** Owen Jones, *The Grammar of Ornament* (1856); Semper; Ruskin; Morris; Christopher Dresser, *Principles of Decorative Design* (1873); Sullivan (1896); Loos (1910); debate del Werkbund entre Muthesius (tipificación) y Van de Velde (1914).
- **Movimientos:** Arts and Crafts; esteticismo; art nouveau, Jugendstil y modernisme; Escuela de Glasgow; Secesión de Viena; cartel ilustrado; Prairie School.
- **Instituciones:** Morris & Co. (1861); South Kensington Museum, hoy V&A (1852); Liberty (1875); Kelmscott Press (1891); Wiener Werkstätte (1903); Deutscher Werkbund (1907); AEG con Behrens (1907); Singer; Ford (1903).
- **Diseñadores:** William Morris, Christopher Dresser, Philip Webb, Charles Rennie Mackintosh, Margaret Macdonald, Josef Hoffmann, Koloman Moser, Henry van de Velde, Victor Horta, Hector Guimard, Antoni Gaudí, Louis Comfort Tiffany, Émile Gallé, René Lalique, Jules Chéret, Alfons Mucha, Peter Behrens, Charles Frederick Worth, Paul Poiret, Mariano Fortuny, Frank Lloyd Wright.
- **Obras:** silla n.º 14 de Thonet (1859); *Strawberry Thief* y *Kelmscott Chaucer* (enlazar a LHA); logotipo de Coca-Cola (1887); silla de Hill House (1902–1903); Sitzmaschine (1905); Sanatorio de Purkersdorf (1904); hervidor y lámparas de la AEG (1908–1909); Ford T (1908); vestido Delphos (1907); entradas del metro de Guimard; carteles de Chéret, Lautrec y Mucha (enlazar a LHA).
- **América Latina y Chile:** Lira Popular (pliegos de poesía popular con grabados, c. 1860–1920); revista *Zig-Zag* (1905); los grabados de José Guadalupe Posada (México, enlazar a LHA); el auge del salitre y la arquitectura de Valparaíso como contexto.

### 10.4 Modernismo (1914–1945): **época piloto recomendada**

Es la época con vínculos contexto–diseño más claros y abundantes; conviene construirla primero para probar el modelo.

- **Político:** Primera Guerra Mundial y cartel de propaganda; Revolución rusa (1917); República de Weimar (1919–1933); fascismo italiano (1922); nazismo (1933), cierre de la Bauhaus y exilio a EE. UU.; Guerra Civil Española; New Deal (1933); Segunda Guerra Mundial (Utility Furniture británico, 1942).
- **Económico:** fordismo y taylorismo; consumo masivo y crédito; crac de 1929 y Gran Depresión: el diseño industrial como herramienta de venta; propuesta de obsolescencia planificada (Bernard London, 1932); racionamiento.
- **Social:** voto y trabajo de las mujeres; vivienda social (Nuevo Frankfurt, 1925–1930); higienismo; electrificación del hogar; ocio y deporte.
- **Cultural:** vanguardias (cubismo, futurismo, De Stijl, constructivismo, dadá, surrealismo); cine sonoro y radio; jazz; Exposición de Artes Decorativas de París (1925); MoMA (1929) y las exposiciones "Estilo Internacional" (1932) y *Machine Art* (1934).
- **Tecnológico:** automóvil masivo, aviación, radio, cine sonoro (1927), primeras transmisiones de televisión; aerodinámica.
- **Producción:** tubo de acero (1925); contrachapado moldeado; baquelita y primeros plásticos; acero inoxidable; offset y fotografía impresa; fotomontaje; cremallera; nailon (1935/1939); prensado de chapa; cadena de montaje.
- **Teórico:** manifiesto De Stijl (1918); programa de la Bauhaus (1919); Le Corbusier, *Vers une architecture* (1923); El Lisitski, "Topografía de la tipografía" (1923); Moholy-Nagy, *Malerei, Fotografie, Film* (1925); Tschichold, "Elementare Typographie" (1925) y *Die neue Typographie* (1928); Beatrice Warde, "The Crystal Goblet" (1930/1932); Bel Geddes, *Horizons* (1932); Herbert Read, *Art and Industry* (1934); Pevsner, *Pioneers of the Modern Movement* (1936); Neurath, *International Picture Language* (1936).
- **Movimientos:** De Stijl; constructivismo; Bauhaus; art déco; nueva tipografía; Streamline Moderne; Estilo Internacional.
- **Instituciones:** Bauhaus (1919–1933); VKhUTEMAS (1920–1930); Werkbund y Weissenhof (1927); Nuevo Frankfurt; London Transport con Frank Pick; Penguin Books (1935); MoMA; Olivetti; Container Corporation of America; Cranbrook (1932); Black Mountain College (1933); New Bauhaus de Chicago (1937); Taller de Gráfica Popular (México, 1937); casas de moda de Chanel y Schiaparelli.
- **Diseñadores:** Gerrit Rietveld, Theo van Doesburg, Aleksandr Ródchenko, Varvara Stepánova, Liubov Popova, El Lisitski, Walter Gropius, László Moholy-Nagy, Marcel Breuer, Marianne Brandt, Wilhelm Wagenfeld, Herbert Bayer, Anni Albers, Gunta Stölzl, Ludwig Mies van der Rohe, Lilly Reich, Le Corbusier, Charlotte Perriand, Eileen Gray, Alvar y Aino Aalto, Margarete Schütte-Lihotzky, Jan Tschichold, Paul Renner, A. M. Cassandre, Edward McKnight Kauffer, Edward Johnston, Harry Beck, Eric Gill, Stanley Morison, Raymond Loewy, Norman Bel Geddes, Henry Dreyfuss, Coco Chanel, Elsa Schiaparelli, Madeleine Vionnet, Sonia Delaunay, Leopoldo Méndez.
- **Obras:** tipografía Johnston (1916); silla Roja y Azul y casa Schröder (enlazar a LHA); lámpara Wagenfeld (1924); infusor de Brandt (enlazar a LHA); silla Wassily (1925); cocina de Frankfurt (1926); Futura (1927); Gill Sans (1928); silla Barcelona y Villa Savoye (enlazar a LHA); Times New Roman (1932); mapa del metro de Londres (1933); portadas de Penguin (1935); cartel *Normandie* de Cassandre (1935); carteles de Ródchenko y El Lisitski (enlazar a LHA); Chanel n.º 5 (1921) y el "pequeño vestido negro" (1926); vestido langosta de Schiaparelli y Dalí (1937); duplicadora Gestetner (1929) y refrigerador Coldspot (1934) de Loewy; Chrysler Airflow (1934); Dymaxion (1933); Volkswagen (1938); silla Paimio (enlazar a LHA) y jarrón Aalto (1936); gráficos Isotype; Jeep (1941); Utility Furniture (1942).
- **América Latina y Chile:** Taller de Gráfica Popular (1937); Semana de Arte Moderno de São Paulo (1922) y su gráfica; muralismo mexicano (enlazar a LHA); CORFO (1939) y el inicio de la industrialización chilena; revistas ilustradas chilenas (*Zig-Zag*, *El Peneca* con Coré) *(verificar fechas)*.

### 10.5 Posguerra (1945–1975)

- **Político:** Guerra Fría (1947–1991) y diseño como propaganda de modos de vida; Plan Marshall (1948); Revolución cubana (1959); Mayo de 1968; **Unidad Popular (1970–1973) y golpe de Estado (1973)**.
- **Económico:** "milagros" alemán e italiano; sociedad de consumo y crédito; publicidad televisiva; industrialización por sustitución de importaciones en América Latina (CEPAL, 1948); contenedor (1956); crisis del petróleo (1973).
- **Social:** baby boom y suburbios; juventud y contracultura; feminismo de segunda ola; derechos civiles; conciencia ecológica (*Silent Spring*, 1962; Club de Roma, 1972).
- **Cultural:** televisión, rock y pop; arte pop (enlazar a LHA); Juegos Olímpicos como proyectos de diseño total (México 1968, Múnich 1972); Expo 67; carrera espacial y llegada a la Luna (1969).
- **Tecnológico:** transistor (1947), computador (desde 1946; IBM 360, 1964), circuito integrado (1958–1959), avión a reacción, satélites.
- **Producción:** moldeo por inyección de plásticos (ABS, polipropileno); fibra de vidrio y contrachapado moldeado (Eames); espuma de poliuretano; fotocomposición; Letraset (1961); serigrafía; muebles para armar en caja plana (IKEA, 1956); fibras sintéticas en moda (poliéster, elastano, 1958).
- **Teórico:** Paul Rand, *Thoughts on Design* (1947); Max Bill, "Die gute Form" (1949); Dreyfuss, *Designing for People* (1955); Packard, *The Hidden Persuaders* (1957) y *The Waste Makers* (1960); revista *Neue Grafik* (1958); manifiesto "First Things First" (1964); Christopher Alexander, *Notes on the Synthesis of Form* (1964); McLuhan, *Understanding Media* (1964); Rudofsky, *Architecture Without Architects* (1964); Venturi (1966, enlazar a LHA); Papanek, *Design for the Real World* (1971); Venturi, Scott Brown e Izenour, *Learning from Las Vegas* (1972); Bonsiepe, textos de la experiencia chilena (1974 *(verificar)*); los textos de Maldonado en Ulm.
- **Movimientos:** Good Design; diseño escandinavo; diseño italiano; funcionalismo de Ulm; estilo tipográfico internacional (suizo); identidad corporativa; diseño pop y psicodélico; diseño radical (Archizoom, Superstudio); brutalismo y metabolismo; prêt-à-porter y moda de la era espacial.
- **Instituciones:** HfG Ulm (1953–1968); Braun (departamento de diseño, 1955–1956); Olivetti; Herman Miller y Knoll; Vitra; Marimekko (1951); IKEA; Compasso d’Oro (1954); ICSID (1957); Push Pin Studios (1954); Pentagram (1972); **ESDI, Río de Janeiro (1963)**; **CIDI, Buenos Aires (1962)**; **INTEC/CORFO en Chile (1970–1973)**; DICAP (sello discográfico, Chile) *(verificar fecha de fundación)*.
- **Diseñadores:** Charles y Ray Eames, George Nelson, Eero Saarinen, Florence Knoll, Arne Jacobsen, Hans Wegner, Verner Panton, Dieter Rams, Hans Gugelot, Otl Aicher, Max Bill, Tomás Maldonado, Gui Bonsiepe, Marcello Nizzoli, Ettore Sottsass, Achille Castiglioni, Joe Colombo, Gio Ponti, Paul Rand, Saul Bass, Massimo Vignelli, Milton Glaser, Josef Müller-Brockmann, Adrian Frutiger, Max Miedinger, Wim Crouwel, Christian Dior, Cristóbal Balenciaga, Mary Quant, Yves Saint Laurent, Pierre Cardin, André Courrèges, Maija Isola, Lina Bo Bardi, Sergio Rodrigues, Aloísio Magalhães, Lance Wyman, Vicente y Antonio Larrea.
- **Obras:** silla LCW (1945) y Lounge (1956) de los Eames; silla Tulip (1956); Ant (1952) y Egg (1958); Wishbone (1949); silla Panton (producida desde 1967); taburete Ulm (1954); Braun SK 4 (1956); Olivetti Lettera 22 (1950); Vespa (1946); Fiat 500 (1957); taburete Butterfly (1954); Helvetica y Univers (1957); logotipo de IBM (1956, rayas en 1972); identidad de Lufthansa (1962); pictogramas de Múnich 1972; identidad de México 68; cartel de *Vértigo* (1958); New Look de Dior (1947); traje de Chanel (1954); minifalda de Quant (c. 1965); vestido Mondrian (1965) y Le Smoking (1966) de Saint Laurent; Unikko de Marimekko (1964); sillón Mole (1957); sala de operaciones de **Cybersyn** (1972–1973); carátulas de la Nueva Canción Chilena (Larrea); murales de la Brigada Ramona Parra.
- **América Latina y Chile:** ESDI, CIDI, México 68, Brasilia (enlazar a LHA), Cybersyn e INTEC (equipo de Bonsiepe), gráfica de la Unidad Popular, productos de consumo masivo de INTEC (p. ej., la cuchara dosificadora de leche *(verificar)*), el golpe de 1973 como corte.

### 10.6 Posmoderno (1975–hoy)

- **Político:** neoliberalismo (Thatcher, Reagan; **Chile como laboratorio desde 1975**); dictaduras y transiciones en América Latina (**plebiscito chileno de 1988**); caída del Muro de Berlín (1989); 11 de septiembre (2001); Primavera Árabe; populismos.
- **Económico:** globalización y deslocalización (China como "fábrica del mundo"; OMC, 2001); marcas globales y *branding*; *fast fashion*; crisis de 2008; economía de plataformas.
- **Social:** diversidad y feminismos; crisis climática (Kioto, 1997; París, 2015); envejecimiento; migraciones; pandemia de COVID-19 (2020).
- **Cultural:** posmodernidad; punk (1976); MTV (1981); hip hop y cultura de club; cultura de internet y redes sociales.
- **Tecnológico:** computador personal (Apple II, 1977; IBM PC, 1981; Macintosh, 1984); web (1991); teléfono móvil y smartphone (iPhone, 2007); IA generativa (2022).
- **Producción:** autoedición y PostScript (1984–1985); fuentes digitales; CAD/CAM; impresión 3D y corte láser; prototipado rápido; materiales reciclados y biomateriales; impresión digital; fabricación deslocalizada.
- **Teórico:** los diez principios de Dieter Rams (c. 1980); Müller-Brockmann, *Grid Systems* (1981); Norman, *The Design of Everyday Things* (1988, como *The Psychology of Everyday Things*); Bruce Mau, *Incomplete Manifesto* (1998); "First Things First 2000" (1999); Naomi Klein, *No Logo* (1999); McDonough y Braungart, *Cradle to Cradle* (2002); Tim Brown, "Design Thinking" (2008); Dunne y Raby, *Speculative Everything* (2013); Arturo Escobar, *Designs for the Pluriverse* (2018); Bonsiepe, textos sobre diseño y periferia *(verificar títulos y años)*.
- **Movimientos:** Memphis (1981) y Alchimia; posmodernismo; deconstructivismo (enlazar a LHA); New Wave y tipografía experimental (Weingart, Emigre, Carson); Droog (1993); diseño crítico y especulativo; diseño sostenible; diseño de interacción, de experiencia y de servicios.
- **Instituciones:** Memphis; Apple; frog design; IDEO (1991); *Emigre* (1984); Droog; Alessi; Zara (1975) y H&M; Vitra Design Museum (1989); Design Museum de Londres (1989); Elemental (Chile, 2001 *(verificar)*).
- **Diseñadores:** Ettore Sottsass, Michele De Lucchi, Philippe Starck, Ron Arad, Marc Newson, Jasper Morrison, Jonathan Ive, Hartmut Esslinger, Susan Kare, Zuzana Licko, Wolfgang Weingart, April Greiman, David Carson, Neville Brody, Paula Scher, Stefan Sagmeister, Vivienne Westwood, Martin Margiela, Alexander McQueen, Hella Jongerius, Fernando y Humberto Campana, Alejandro Aravena (Elemental).
- **Obras:** I ♥ NY (1977); librero Carlton (1981); Macintosh e íconos de Susan Kare (1984); revista *Emigre* (1984); Swatch (1983); exprimidor Juicy Salif (1990); utensilios OXO Good Grips (1990); *Ray Gun* (1992); aspiradora Dyson DC01 (1993); iMac (1998); iPod (2001); iPhone (2007); ropa punk de Westwood (1976); cartel *Hope* (2008); Quinta Monroy de Elemental (2004).
- **América Latina y Chile:** **arpilleras** chilenas desde 1974 (textil como testimonio bajo la dictadura); **franja y logotipo del NO** en el plebiscito de 1988; Elemental y la vivienda incremental; los hermanos Campana (Brasil); el diseño en la economía de mercado chilena.

### 10.7 Presencia de América Latina

- **América Latina** en todas las épocas (ver cada sección). Chile no es una categoría ni un chip: está dentro de América Latina. El campo `countries` (códigos ISO: CL, AR, BR, MX…) es solo informativo. Los elementos chilenos de la sección 10 son sugerencias: se incluyen solo si fueron relevantes para la historia del diseño, sin forzar.
- **Alcance regional:** solo Europa, Norteamérica y América Latina (más lo `global`). Asia, África y Medio Oriente y Oceanía quedan fuera: no se crean regiones ni elementos propios de ellas, **salvo (punto 61, 4 oct 2026) los que tengan influencia demostrable en el diseño occidental** (p. ej., japonismo, metabolismo, Muji, Kawakubo, Yamamoto): **v31 (paso 0.10):** `REGION_ZONES.global = ['beyond']` y `ZONE_OF` con los códigos de Asia, África, Medio Oriente y Oceanía: en «Organizar por región» el grupo «Global» se subdivide en la zona «Más allá de Occidente» solo si hay algún elemento con país de esa zona (hoy ninguno); el filtro de región no los oculta. Van con `regions: ["global"]`, su país en `countries` y una línea de mecanismo que explique la influencia (orientativo 6 a 10 en toda la línea; ver `PLAN-CIERRE.md`, C5 y paso 0.10). Si un hecho de esas regiones explica directamente el diseño europeo, norteamericano o latinoamericano (p. ej., la porcelana china y el chintz indio que cambian el gusto europeo), se incluye en la región que afecta, no en la de origen.
- Buscar el equilibrio sin forzar: incluir lo que realmente fue influyente, con fuentes.

---

## 11. Ejemplo completo del modelo (para calibrar estilo y densidad)

**Obra:** Cocina de Frankfurt (Margarete Schütte-Lihotzky, 1926). Disciplina: Arquitectura (interior). Fabricante: oficina municipal del Nuevo Frankfurt. Producción: 1926–1930, unas 10.000 instaladas *(verificar)*.
- *Idea clave:* Una cocina pequeña y completamente equipada, diseñada como un laboratorio para ahorrar pasos y tiempo, instalada en serie en la vivienda social de Frankfurt.
- *Contexto* (enlaces con nota):
  - **Social** · Falta de vivienda en la Alemania de Weimar → "Hecha para departamentos pequeños y estandarizados de vivienda social."
  - **Económico** · Taylorismo y racionalización → "Aplica el estudio de tiempos y movimientos al trabajo doméstico."
  - **Social** · Nuevo papel de la mujer → "Pensada para liberar tiempo a mujeres que también trabajaban fuera de casa."
  - **Tecnológico** · Electrificación del hogar → "Integra cocina eléctrica o a gas y luz artificial en un espacio mínimo."
- *Dónde verla:* reconstrucciones en el MAK de Viena y el MoMA *(verificar)*.

**Contexto:** Taylorismo y racionalización (Económico, 1911 →).
- *Qué pasó:* Frederick Taylor publicó *The Principles of Scientific Management* (1911): medir y dividir el trabajo para aumentar la productividad.
- *Efecto en el diseño:* La eficiencia se volvió un valor estético y social: cocinas laboratorio, muebles estandarizados, cadenas de montaje y señalética racional.
- *Diseño relacionado:* cocina de Frankfurt, Ford T, Bauhaus, Utility Furniture…

---

## 12. Sin enlaces con la Línea de Historia del Arte (v10)

- Decisión de la persona responsable (v10): **la LHD no enlaza con la LHA.** Se eliminaron el campo `lha` de los datos, el botón «Ver en la línea de arte», la constante `LHA_URL` y la opción `lhaUrl` de `app.js`. Las menciones «(enlazar a LHA)» de las listas de la sección 10 ya no aplican: esas obras se redactan en la LHD como cualquier otra, con el texto enfocado en el diseño y su contexto.

---

## 13. Procedimiento de trabajo

La persona responsable prefiere que se le pregunte antes de empezar trabajos grandes, que se le muestren listas para aprobar y que cada entrega venga con un resumen corto en español.

**Fase 0: base (una sesión)**
1. Leer este documento y, si está, `PROJECT.md` y el código de LHA.
2. Copiar LHA a `lhd/` y adaptar:
   - configuración de épocas;
   - filas de contexto con colores;
   - disciplinas con formas;
   - instituciones;
   - enlaces de contexto;
   - período de fabricación;
   - filtros;
   - fichas nuevas;
   - ficha general;
   - validaciones del build.
3. Crear datos mínimos de prueba (2–3 elementos de cada tipo) y comprobar en el navegador (Playwright con Chromium, servidor `python3 -m http.server`).
4. Crear `PROJECT.md` (decisiones y bitácora) y `tools/SPEC.md` (este documento).
5. Entregar `LHD-vNN.zip` con capturas.

**Fase 1: época piloto (Modernismo)**
1. Proponer las listas (contexto por subcategoría, producción, teoría, movimientos, instituciones, diseñadores, obras por disciplina) con cantidades y **esperar aprobación**.
2. Redactar en inglés y español; crear los enlaces de contexto (cada contexto con al menos uno; cada obra imprescindible con al menos uno; meta: dos o tres por obra imprescindible).
3. Verificar datos y fuentes; anotar lo no verificado.
4. Build sin `PROBLEM`; revisar los `WARN`.
5. Revisar en el navegador: carriles, fichas, resaltado contexto ↔ diseño, filtros, ficha general, tema oscuro e inglés.
6. Actualizar `PROJECT.md` y entregar el zip con un resumen en español: qué se agregó, qué revisar, qué no se pudo verificar y las fuentes.
7. Pedir retroalimentación sobre el modelo antes de seguir.

**Fases 2 a 5:** una época por sesión, en este orden: Posguerra → Reforma → Posmoderno → Revolución Industrial (v11: «Antes de 1750» se eliminó). Mismo procedimiento; cada elemento va en la carpeta de la época donde empieza.

**Fase 7: integración.** Enlaces con LHA, revisión de equilibrio regional y de disciplinas, búsqueda global, estadísticas y una revisión final de errores con un agente independiente que no haya escrito el contenido.

---

## 14. Errores que evitar (aprendidos en LHA)

- Estilos tratados como tecnologías, o estructuras (bóvedas, el marco de acero como sistema) tratadas como materiales: el material va en Producción y la estructura la explican las obras.
- Fechas de Wikipedia sin contrastar; atribuciones dudosas presentadas como seguras.
- Conexiones entre épocas visibles solo en una época (aquí el build debe resolverlo).
- Ids repetidos entre épocas (p. ej., una obra y una tecnología con el mismo id).
- Etiquetas largas en las filas de contexto y teoría, que multiplican las filas: usar `short` breve (apellido en teoría; dos o tres palabras en contexto).
- Contraseñas u otros secretos escritos en archivos publicados.
- Filosofía pura en la fila Teórico: la persona responsable prefirió dejar fuera textos filosóficos generales (Platón, Kant, Burke) y quedarse con textos sobre el arte o el diseño. Las obras de pensamiento social se aceptan si tratan directamente del diseño o de la cultura material (Packard, Papanek, Klein).

---

## 15. Decisiones abiertas (confirmar al comenzar)

1. **Nombre del sitio:** "Línea de Historia del Diseño" (LHD) u otro.
2. **Idiomas:** bilingüe español/inglés como LHA (recomendado), o solo español.
3. **Inicio de la primera época:** escala desde 1450 con antecedentes en la columna previa (recomendado), o desde la escritura.
4. **Carril Interdisciplinario:** confirmar que se agrega a las cuatro disciplinas.
5. **Nombre de la fila Producción** (materiales, procesos y herramientas del diseño): **resuelto en v04:** «Productivo» (provisional; la persona responsable consideró también «Industrial»).
6. **Chip "Chile":** **resuelto en v04:** eliminado; Chile queda dentro de América Latina.
7. **URL de LHA** para los enlaces cruzados, y si se agregan los enlaces inversos en LHA.
8. **Época piloto:** Modernismo (recomendado) u otra.

---

## 16. Mensaje para iniciar la sesión futura

> Adjunto el documento `LHD-especificacion.md` y el proyecto de la Línea de Historia del Arte (`LHA-completo-vNN.zip`). Quiero construir la Línea de Historia del Diseño siguiendo el documento. Empieza por confirmar conmigo las decisiones abiertas (sección 15) y luego haz la fase 0 (base técnica). No redactes contenidos de ninguna época sin mostrarme antes las listas propuestas.
