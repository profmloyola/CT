# Línea de Historia del Diseño (LHD): decisiones y bitácora

Sitio estático (HTML, CSS y JS sin librerías) basado en el código de la Línea de Historia del Arte (LHA v28). Especificación completa en `tools/SPEC.md`.

## Estado

> **Para retomar en una sesión nueva:** leer `INICIO-SESION-NUEVA.md` (raíz). Plan de lo que falta: `tools/PLAN-CIERRE.md` (único plan vigente). Reglas de contenido: `tools/MANUAL-CONTENIDO.md`. Decisiones y pendientes: `tools/CAMBIOS-PENDIENTES.md`. *Los registros de verificación, revisión y fuentes de las fases anteriores (`VERIFICACION-*`, `REVISION-*`, `A6-LOTE*`, `LISTAS-*`, `PLAN-FASES`, `GUIA-REDACCION-FASE1`, etc.) se retiraron del paquete en v29; las menciones a ellos más abajo son históricas.*

- **v37 (4 oct 2026): etapa 4, Posmoderno (pasos 4.1 a 4.4; punto 69).** Contenido nuevo en `src-data/postmodern/` (sin fuentes, `refs: []`; para lo posterior a 2010 solo hechos de certeza, C1), con el método de las etapas 2 y 3 (9 lotes de núcleo, 9 de obras más 1 suelto, 9 de enlaces, 1 de conexiones y 1 de relleno, todos con agentes Sonnet): **73 obras (21 ★), 35 diseñadores, 30 hechos de contexto (con `ctx-personal-computer`), 14 productivos, 9 teorías, 8 movimientos (con `macro-postmodernism`), 12 instituciones, 112 enlaces de contexto y 14 conexiones**; América Latina 13 obras (18 %). `macro-postmodernism` suma a `parts` Memphis, Alchimia, deconstructivismo y New Wave (junto con diseño pop y radical, de la etapa 2). Los hechos que empiezan antes de 1975 llevan `start` 1975 y el año real en `date`; `arpilleras-1974` se escribió con `year` 1976 (fecha «c. 1974–1990») porque 1974 cae fuera del tramo. Desviaciones de la lista (en `LISTAS-CIERRE.md` y `PENDIENTES-FUENTES.md`): `ctx-fall-berlin-wall` y `ctx-fast-fashion` a la reserva (sin elemento al que enlazarlos con mecanismo cierto); 39 enlaces `sin_enlace`; `carlton-bookcase-1981`, `dyson-dc01-1993`, `westwood-punk-1976`, `sesc-pompeia-1986` y `portland-building-1982` bajaron de ★ a Normal (C4) y `kettle-9093-1985`, `mtv-logo-1981` y `gaultier-cone-bra-1990` subieron a ★ (tenían 2 enlaces directos de subcategorías distintas), con lo que el ★ queda en 28,8 %; `vivienne-westwood`, `michael-graves`, `alexander-mcqueen` y `zaha-hadid` bajaron a Normal como diseñadores (sin obra ★ propia). Bajo la meta de 2 enlaces: `ctx-crisis-2008`, `ctx-platform-economy`, `ctx-feminisms`, `ctx-ageing-accessibility` y `ctx-digital-music`; sin enlace directo: `well-tempered-chair-1986`, `lockheed-lounge-1986`, `air-chair-1999`, `macbook-air-2008`, `torres-siamesas-2005`, `mube-1988`, `mestizo-restaurant-2007` y `vitra-fire-station-1993`. Pruebas ajustadas (C6): `test_preview` (rango de ★ más amplio). Todo lo nuevo lleva «contenido no revisado» hasta la Parte II. `?v=37`.
- **v36 (4 oct 2026): etapa 3, Reforma (pasos 3.1 a 3.3; punto 68).** Contenido nuevo en `src-data/reform/` (sin fuentes, `refs: []`), con el método de la etapa 2 (8 lotes de núcleo, 8 de obras, 8 de enlaces, 1 de conexiones y 1 de relleno, todos con agentes Sonnet; `validate_out.py` y `apply_new.py`): **60 obras (18 ★), 28 diseñadores, 30 hechos de contexto (con `ctx-taylorism`), 11 productivos, 6 teorías, 6 movimientos (con `macro-modernism`), 9 instituciones, 103 enlaces de contexto y 18 conexiones**; América Latina 4 obras (7 %). Los hechos, movimientos o instituciones que empiezan antes de 1851 (Gothic Revival, ferrocarril, cromolitografía, Glasgow School of Art…) llevan `start` 1851 en el campo y su año real en `date` y en el texto; la obra `werkbund-cologne-1914` lleva `year` 1913 (fecha 1913–1914) y `th-werkbund-debate` también 1913, porque el build corta el tramo en 1913. Desviaciones de la lista (en `LISTAS-CIERRE.md`, reserva, y `PENDIENTES-FUENTES.md`): `ctx-telephone` y `aluminium` a la reserva (sin elemento al que enlazarlos con mecanismo cierto); 20 enlaces quedaron `sin_enlace`. Bajo la meta de 2 enlaces: `ctx-department-stores`, `ctx-nitrate-boom`, `ctx-classical-archaeology`, `ctx-safety-bicycle` y `ctx-snapshot-photography` (1 cada uno); sin enlace directo: `worth-haute-couture` y `levis-riveted-jeans`. Todas las ★ cumplen 2 enlaces de subcategorías distintas. Pruebas ajustadas (C6): `test_preview` (la vista previa debe tener al menos tantos elementos como el sitio real). Todo lo nuevo lleva «contenido no revisado» hasta la Parte II. `?v=36`.
- **v35 (4 oct 2026): etapa 2, Posguerra (pasos 2.1 a 2.4; punto 67).** Contenido nuevo en `src-data/postwar/`, escrito sin fuentes (`refs: []`) por agentes Sonnet en paralelo (12 lotes de núcleo, 11 de obras, 11 de enlaces, 1 de conexiones, 1 de relleno, 1 de etiquetas cortas) y validado con `validate_out.py` / aplicado con `apply_new.py`: **90 obras (24 ★), 44 diseñadores, 36 hechos de contexto, 15 productivos, 11 teorías, 11 movimientos (con `macro-postmodernism`), 15 instituciones, 142 enlaces de contexto y 16 conexiones**; América Latina 17 obras (19 %). `ctx-corfo` y `ctx-early-television` volvieron de la reserva a `src-data/modernism/` (Modernismo: 41 hechos de contexto, 237 enlaces). `macro-modernism` suma a `parts` Good Design, funcionalismo de Ulm, estilo tipográfico internacional e identidad corporativa; `macro-postmodernism` suma diseño pop y diseño radical. Desviaciones de la lista (todas en `LISTAS-CIERRE.md` y `PENDIENTES-FUENTES.md`): `larrea-hermanos` y `xerox-914` a la reserva (sin datos ciertos / sin enlace con mecanismo); 23 enlaces quedaron `sin_enlace` por fechas o mecanismo dudoso; `eames-lounge`, `ulm-stool`, `hfg-ulm-building` y `max-bill` bajaron de ★ a Normal (C4: una ★ necesita 2 enlaces directos de subcategorías distintas y no se pudo escribir el segundo con certeza; ★ queda en 26,7 %); `ctx-marshall-plan`, `ctx-corfo` y `ctx-second-wave-feminism` quedan con 1 enlace y `ctx-early-television` con 1 débil (meta: 2). 4 obras sin enlace directo (`vertigo-titles`, `iv-centenario-rio-symbol`, `balenciaga-sack-dress`, `casa-curutchet`); 37 obras con `short` agregado. Cambios de código: `build_data.py` no exige 12 años de «edad» a los colectivos (`kind: collective`) al comprobar el año de sus obras (Archizoom, Superstudio); `tools/LISTAS-CIERRE.md` al día con lo anterior. Pruebas ajustadas (C6): `test_general` (la ficha del macromovimiento Posmodernismo ya no trae el aviso «en desarrollo» al estar Posguerra lista) y `test_preview` (ahora usa «I ♥ NY», de Posmoderno). Todo el contenido nuevo lleva la advertencia «contenido no revisado» hasta la Parte II. `?v=35`.
- **v34 (4 oct 2026): etapa 1b, vista previa de toda la línea.** `tools/pipeline/preview_listas.py`: copia el sitio y `src-data/` a una carpeta temporal, agrega una ficha «en desarrollo» por cada fila de `LISTAS-CIERRE.md` que aún no existe (nombre ES también en EN, años, nivel, disciplina, región derivada de obras relacionadas, enlaces de contexto con su línea de mecanismo, conexiones, `parts` de los macromovimientos, `ctx-corfo` y `ctx-early-television` desde la reserva), corre `build_data.py` (mismas reglas) y deja el sitio con etiqueta «VISTA PREVIA», `LEEME-VISTA-PREVIA.md` e `INFORME-VISTA-PREVIA.md`. Rellenos para pasar las reglas del build: un diseñador ★ sin obra ★ figura Normal; contextos, teorías y productivos sin enlace a un elemento de diseño se enlazan al vecino más cercano (todo listado en el informe). Resultado: 373 obras (114 ★), 186 diseñadores, 165 contextos, 657 enlaces. No cambia el sitio real ni `src-data/`. Prueba nueva `test_preview`. `?v=34`.
- **v33 (4 oct 2026): V1 aprobado con cambios (punto 66) y recorte del Modernismo aplicado (paso 1.7).** `RECORTE-MODERNISMO.json`: 18 obras, 8 diseñadores, 3 hechos; se mantienen Stool 60, Maison du Peuple, Lacoste (camisa y diseñador) y Prouvé, y se repusieron Letty Lynton/Adrian, EKCO AD65/Wells Coates y Zonnestraal (Fuller/Dymaxion se descartó porque Posguerra lo usa). Resultado: 120 obras (37 ★), 64 diseñadores, 39 hechos de contexto; lo quitado está en `tools/RESERVA-FASE-B.json` (`recorte_modernismo`). Pruebas ajustadas (C6): `test_recorte` (conteos relativos), `test_etapa1` (verifica lo aplicado), `test_v20`, `test_v22`, `ejemplos_ok.json`; `EJEMPLOS.md` regenerado. `?v=33`.
- **v32 (4 oct 2026): etapa 1 (pasos 1.1–1.6), pendiente de V1.** Nuevos: `tools/LISTAS-CIERRE.md` (listas maestras de Industrial 30 obras, Reforma 60, Posguerra 90, Posmoderno 73, con ids, nivel, contextos con línea de mecanismo, conexiones ≥ 8 y reserva; las escribieron agentes Sonnet por tramo con `tools/pipeline/briefs/BRIEF-LISTAS.md` y se unificaron resolviendo ids repetidos entre tramos), `tools/pipeline/listas_check.py` (paso 1.5: ids únicos y sin choques, referencias existentes, cantidades ±2/±3, ★ 25–35 %, contexto ≥ 2 enlaces, obra ≥ 1 contexto, ★ ≥ 2 subcategorías, conexiones ≥ 8, mecanismos de 12–200 caracteres), `tools/RECORTE-MODERNISMO.md/.json` (18 obras, 8 diseñadores, 3 contextos; ensayo con `recortar.py --prueba` sin huérfanos; **no aplicado**), `tools/RESUMEN-V1.md` y `tools/tests/test_etapa1.py`. Sin cambios de código ni de datos (`?v=32`).
- **v31 (4 oct 2026): estado actual. Etapa 0 ejecutada (punto 64).** Herramientas de la Parte I: `tools/build_data.py` (teoría sin enlace de fuente: WARN; `refs: []` cuenta como «sin fuentes todavía»); `tools/pipeline/validate_out.py` (valida la salida de un agente: ids, es completo, marcas, largos, nivel, año del tramo, regiones; `--refs` para la Parte II); `apply_new.py` (agrega elementos a `src-data/<tramo>/`, descartes a `PENDIENTES-FUENTES.md`, `--links-from-lists`); `EJEMPLOS.md` generado por `make_ejemplos.py`; `candidatos_recorte.py`, `recortar.py` (`--prueba`; ensaya en una copia con build y huérfanos antes de aplicar) y `recorte_lib.py`; `tools/empaquetar.sh NN`; plantillas de `ESTADO-ACTUAL` y `LEEME` en `tools/plantillas/`. El tipo de registro de los agentes se llama **`rtype`** (en las obras `type` ya es el tipo de obra). Elementos orientales (paso 0.10): `REGION_ZONES.global = ['beyond']` y `ZONE_OF` con Asia, África, Medio Oriente y Oceanía; zona «Más allá de Occidente» solo si existe alguno. Pruebas nuevas: `test_etapa0`, `test_recorte`, `test_empaquetar` (sin navegador) y `test_v31`. Datos sin cambios (`?v=31`).
- **v30 (4 oct 2026): Etapa P ejecutada (puntos 59 y 62).** Las fuentes son públicas: cada ficha (movimiento, institución, diseñador, obra, contexto, productivo, teoría, concepto) termina con la sección «Fuentes (n)», un `<details class="sources">` cerrado al abrir; sin fuentes, un triángulo de advertencia en el título cerrado y el mensaje «no ha sido revisada». Los superíndices `[n]` salen para todos y el clic abre la sección y resalta la fuente. Las ficha de época, foco, información y ayuda no la llevan. Técnica: `renderPanel` enciende `rfMode(true)` solo mientras arma la ficha y lo apaga (`finally`), así el buscador, los tooltips y las etiquetas nunca ven marcas; `srcCount(id)` cuenta las fuentes propias y las de sus enlaces. «Revisión» pasa a «Observaciones» (solo texto; sin casilla «Revisada»); `editar.php` ya no guarda `revisada` y limpia los registros viejos; clave `lhd2026` (punto 60; no se cambia). El resumen de revisión (`?editar`) tiene tres bloques: revisión por IA (con fuentes / sin fuentes, por tipo y por época, con lista filtrable), observaciones pendientes (la ficha sale al vaciar el texto) e imágenes cambiadas a mano; la exportación `.md` suma las imágenes y la cuenta sin fuentes. Pruebas: `test_v21` y `test_editar` ajustadas, nueva `test_v30`; `check_contrast.py` revisa el color de advertencia (`--warn`); imágenes de la ayuda regeneradas. `?v=30`. Datos sin cambios.
- **v29r (4 oct 2026):** Solo documentos: plan v7 (punto 61): 375 obras (Industrial 30, Reforma 60, Modernismo 120, Posguerra 90, Posmoderno 75), recorte del Modernismo de solo 18 obras, 8 diseñadores y 3 hechos de contexto, elementos orientales con influencia en Occidente permitidos (paso 0.10), ~32 a 33 sesiones.
- **v29q (4 oct 2026):** solo documentos: `tools/PLAN-CIERRE.md` v6 (etapa previa P, sección 5A: fuentes públicas, «Observaciones», clave `lhd2026`; modelos con Sonnet; ZIP único de continuidad, sección 5B). Puntos 59 y 60. Nuevos: `ESTADO-ACTUAL.md` y `LEEME-PROBAR-EN-WEB.md`.
- **v29 (4 oct 2026):** Solo documentos: `tools/PLAN-CIERRE.md` v4 (línea equilibrada: 380 obras en total, Modernismo recortado de 138 a 100 en lo no esencial, Posguerra 100, Posmoderno 95, Reforma 55, Industrial 30; V0 aprobado; punto 58). Paquete limpio: se retiraron los registros de fases anteriores y el punto de retorno de la prueba por fecha; `tools/pipeline/` con `lib.py`, `apply2.py` y `apply3.py`; `tools/PENDIENTES-FUENTES.md`. Código y datos iguales a v27.
- **v28 (4 oct 2026):** solo documentos: `tools/PLAN-CIERRE.md` v1 a v3 (puntos 55 a 57).
- **v27 (4 oct 2026):** A6, lote 4 (130 elementos) y A2 (23 enlaces nuevos; diseñadores con enlace propio 59/72). Punto 54, `tools/A6-LOTE4-FUENTES.md`. Pendientes por límite de búsquedas: Cranbrook, Revolución Industrial, Posmodernismo.
- **v26 (4 oct 2026):** A6, lote 3: los 56 diseñadores sin fuentes quedan con `refs` y fechas de vida verificadas (punto 53, `tools/A6-LOTE3-FUENTES.md`). Esperan visto bueno.
- **v25 (4 oct 2026):** A6, lote 2: las 62 obras Normal con fuentes; las 138 obras del Modernismo quedan trazadas (163 de 310 elementos). Correcciones aplicadas, esperan visto bueno (punto 52).
- **v24 (4 oct 2026).** Solo dos niveles (★ y Normal), contexto colapsado al abrir, macromovimientos dentro de «Movimientos», contraseña «lhd» (puntos 48–51); plan replanificado.
- **v23 (4 oct 2026).** A6, lote 1: las 30 obras ★ sin fuentes ya tienen `refs` y marcas (101 de 310 elementos del Modernismo). Correcciones de contenido aplicadas, a la espera del visto bueno (punto 47).
- **v22 (3 oct 2026).** Correcciones de la revisión independiente (punto 46) y conceptos en la ficha del macromovimiento (punto 45). Modernismo: 138 obras (37 ★), 72 diseñadores, 42 hechos de contexto, 232 enlaces (225 con fuentes), 71 de 310 elementos con `refs`. Sigue: A6 (fuentes de las fichas existentes) y el resto de A2.
- **v21 (3 oct 2026).** Fase A en curso: fuentes numeradas en `?editar` (A0), revisión de enlaces (A1), 8 hechos nuevos (A3), 43 obras y 13 diseñadores nuevos (A4) y primeros enlaces propios (A2). Modernismo: 138 obras (37 ★). Falta: A6 (fuentes de las fichas existentes), completar A2 y la revisión independiente.
- **v20 (3 oct 2026).** Niveles de detalle, macromovimientos en vez de épocas, conexiones indirectas, 96 obras en el Modernismo (32 ★). Lo que sigue: fase A del plan (ampliación del Modernismo).
- **Fase 0 (base técnica): hecha.** Versión v01.
- **Interfaz v11: hecha.** Una sola línea continua 1750–hoy, sin carriles por disciplina, con curvas de conexión, foco por fila de contexto y modo `?editar`. Detalle y decisiones técnicas en `tools/PROGRESO-INTERFAZ-V11.md`; reglas nuevas al comienzo de `tools/SPEC.md`.
- **Fase 1 (Modernismo): redactada (v10).** 245 elementos con contenido real en inglés y español: 38 hechos de contexto, 16 de Productivo, 14 textos de teoría, 11 movimientos, 17 instituciones, 58 diseñadores, 91 obras (28 imprescindibles), 147 enlaces de contexto, 19 conexiones y 8 conceptos. La época está marcada `"complete": true`. Verificación en `tools/VERIFICACION-MODERNISMO.md`, revisión independiente en `tools/REVISION-INDEPENDIENTE-MODERNISMO.md`, matriz de enlaces en `tools/PLAN-ENLACES-MODERNISMO.md`, plan de ids en `tools/PLAN-IDS-MODERNISMO.md` y progreso en `tools/PROGRESO-FASE1.md`.
- **Datos de prueba:** ya no quedan en el Modernismo. Siguen los archivos `90-test-*.json` de Reforma y Posmoderno (Antes de 1750 se eliminó en v11) (el taylorismo de Reforma explica la Cocina de Frankfurt como enlace entre épocas: al borrar ese archivo, redactar el taylorismo real con el mismo id `ctx-taylorism` o quitar ese enlace).

## Cómo probar

```
cd lhd
python3 tools/build_data.py        # valida y genera data/all.json (PROBLEM = error; WARN = aviso)
python3 tools/check_contrast.py    # contraste de colores en tema claro y oscuro
sh tools/tests/run_all.sh          # pruebas de navegador (v20); ver INICIO-SESION-NUEVA.md
python3 -m http.server 8000        # abrir http://localhost:8000
php -S 127.0.0.1:8000              # en lugar del anterior, para probar el modo ?editar (http://127.0.0.1:8000/?editar)
```

Pruebas en navegador con Playwright y Chromium (carriles, fichas, resaltado contexto ↔ diseño, filtros, columna previa, año final de Posmoderno, ficha general, tema oscuro, inglés, búsqueda entre épocas, zoom, imágenes simuladas): pasaron todas en v01. Las capturas están en `screenshots/`.

## Estructura

- `index.html`, `app.js`, `style.css`: el sitio. Los colores son variables al comienzo de `style.css` (tema claro, `prefers-color-scheme` y `data-theme`).
- `src-data/<época>/*.json`: datos escritos a mano (ver sección 3.3 y 5 de la especificación).
- `data/all.json`: generado por `build_data.py` (toda la línea en un archivo); no editar a mano.
- `editar.php` y `ediciones/`: modo `?editar` (ver Seguridad). `ediciones/imagenes.json` es público; `ediciones/revision.json` y `ediciones/copias/` están bloqueados por `.htaccess`. La carpeta `ediciones/` debe poder escribirla PHP en el hosting.
- `tools/build_data.py`: valida (secciones 6 y 14 de la especificación) y combina todo en `data/all.json`; exige que cada elemento empiece en la época de su carpeta; calcula estadísticas por época; resuelve `end: "now"` al año actual; borra los `data/*.json` antiguos.
- `tools/check_contrast.py`: revisa los tokens de color.

## Configuración (`window.LHD_CONFIG`, antes de cargar `app.js`)

- `defaultEra`: época cuya ficha de panorama se muestra por defecto (por defecto `modernism`).

## Decisiones tomadas (sección 15 de la especificación)

Las decisiones 1 a 4, 7 y 8 quedaron **confirmadas** por la persona responsable (v04); la 5 y la 6 cambiaron:

1. Nombre: «Línea de Historia del Diseño».
2. Bilingüe español/inglés (`UI.en` / `UI.es`; datos con `es: {…}`).
3. ~~Primera época desde 1450, antecedentes en la columna previa~~ **(v11: se eliminó «Antes de 1750»; la línea empieza en 1750).**
4. ~~Carril «Interdisciplinario» agregado a las cuatro disciplinas~~ **(v11: no hay carriles por disciplina; ver SPEC).**
5. Fila **«Productivo»** (antes «Producción»; materiales, procesos, herramientas). Nombre provisional; también se consideró «Industrial». Se cambia en `UI.<idioma>` (`tr_production`, `k_production`, `production`, `n_production`) y en el texto de ayuda; el identificador interno sigue siendo `production`.
6. **Sin chip «Chile»** ni categoría Chile: Chile queda dentro de América Latina; el campo `countries` es solo informativo. No se fuerzan obras chilenas.
7. **Sin enlaces con la LHA (v10):** se quitaron del código, los datos y la documentación.
8. Época piloto: Modernismo.

Otras decisiones de implementación:

- v11: todas las secciones empiezan abiertas (la vista lejana ya es liviana gracias al nivel de detalle); la ficha general (i) se abre en cada carga salvo que la dirección traiga `#id`.
- Los chips de filtro son multiselección con todo activado; un clic desactiva.
- Obras sin diseñador visible (anónimas o con el diseñador filtrado) van en la subfranja «Obras sin diseñador»; las demás, sobre la línea de vida de su primer diseñador visible.
- Imágenes: API de Wikipedia (imagen de la página); solo se muestra si el archivo está en Wikimedia Commons (si no, podría ser no libre). Si no hay imagen libre: «Ver en la colección» (primer enlace de `where`) y búsqueda en Commons.
- Sin lente (v06): la ficha de época muestra siempre el resumen de las cinco subcategorías de contexto (`context_summary`) y los cambios clave. Disciplinas y regiones están en la fila superior junto a Contexto.

- **Alcance regional (v02):** la LHD solo tiene las regiones `europe`, `north-america` y `latin-america`, más `global` (siempre visible). Se eliminaron Asia, África y Medio Oriente y Oceanía (filtro, textos, validación del build y ejemplos de la especificación). El chip «Chile» se mantiene. Los antecedentes de Asia que explican la imprenta europea, si se incluyen, van como `global`. Se retiró la meta de 20–30 % fuera de Europa y EE. UU.

- **Textos y alcance (v04):** listas del Modernismo aprobadas (245 elementos, sin el texto de Benjamin). Ver el resto de cambios en la bitácora.
- **Ayuda (v03):** botón «?» junto al de información; abre una ventana sobre la línea (se cierra con la ✕, el botón, `Esc`, un clic fuera, al elegir un elemento o al cambiar de época). Textos en `UI.<idioma>.help` de `app.js`. La leyenda se dibuja en código con las mismas formas y colores del sitio, así que no queda desactualizada. Solo la imagen numerada es una captura (`help/overview-es.webp` y `-en.webp`): se regenera con `python3 tools/make_help_images.py [id-de-obra]` cuando cambie la interfaz o el contenido de la época piloto (hoy muestra datos de prueba). No incluye recorridos guiados, ni compartir ni citar (decisión de la persona responsable).
- **Solo en computador:** bajo 900 px de ancho el sitio muestra un aviso en lugar de la línea (igual que LHA).

- **Etiquetas y fichas (v05):** la línea de tiempo dibuja etiquetas breves (`short`, también en obras) y quita cualquier paréntesis como respaldo (`plain()` en `app.js`); en las fichas se usa «:» en lugar de paréntesis. El build avisa cuando un nombre, título, `short` o fecha lleva paréntesis o una etiqueta pasa de 28 caracteres. «Estado actual» es una sección propia de la ficha de obra. Títulos y encabezados de la ficha van en tonos neutros. Los movimientos tienen botón de filtro «Ver solo este movimiento» y un chip «Solo: …» en los filtros.

## Seguridad

- **Modo `?editar` (v11), provisional por decisión de la persona responsable:** la contraseña está escrita en `editar.php` (constante `CLAVE`, hoy `lhd` desde v24, punto 51), no en `app.js` ni en los datos. Desde v60 vale `uai2026` (punto 83; antes `lhd2026`); no publicar `editar.php` en un repositorio público. El navegador la pide al primer intento de editar, una vez por sesión (`sessionStorage`). El PHP valida ids y URLs, bloquea la carpeta al escribir y guarda una copia antes de cada cambio.
- Si el hosting no es Apache, hay que bloquear a mano `ediciones/revision.json` y `ediciones/copias/` (el `.htaccess` no aplica).
- Ningún archivo publicado contiene claves ni datos personales.
- Las fuentes de teoría exigen enlace https (el build lo valida).

## Bitácora

- **v01 (Fase 0):** base técnica completa; build con todas las validaciones (probadas con casos negativos); contraste validado (0 valores bajos); pruebas de navegador en claro, oscuro e inglés. Propuesta de listas del Modernismo entregada como documento aparte (256 elementos).

- **v02:** cambio de alcance regional (ver decisiones). Cambios en `app.js`, `tools/build_data.py`, `tools/SPEC.md`, `PROJECT.md`; el build exige ahora región en `europe`, `north-america`, `latin-america` o `global`.

- **v03:** ayuda con leyenda (ver decisiones). Carpeta nueva `help/` que hay que subir junto con el sitio. `app.js?v=2`, `style.css?v=3`.

- **v04:** se quita el chip y la lógica «Chile» (`app.js`); la fila «Producción» pasa a llamarse «Productivo»; ayuda e imagen regeneradas; `SPEC.md` y propuesta actualizadas. `app.js?v=3`, `style.css?v=3`.

- **v05:** ajustes menores pedidos (Estado actual, etiquetas breves, fichas neutras, filtro de movimiento). `app.js?v=4`, `style.css?v=4`. Datos de prueba corregidos.

## Pendiente y notas

- v11, por revisar con la persona responsable: la línea de vida de los diseñadores (quedó igual, como se pidió); edición de textos en el modo `?editar` (en pausa); umbrales de barras largas (30 años / 75 % del ancho) y de nivel de detalle (4 y 12 px por año), en las constantes al comienzo de `app.js`.
- Al redactar Posguerra y las demás épocas: cada elemento en la carpeta de la época donde empieza; no duplicar elementos.

- Siguiente: Posguerra, con la misma guía.
- Revisar con la persona responsable: obras imprescindibles, enlaces débiles de CORFO y televisión, 8 diseñadores en Interdisciplinario con dos disciplinas (WARN aceptado).
- Decidir más adelante, al llegar a «Antes de 1750», si los antecedentes asiáticos de la imprenta (papel, tipos móviles de Bi Sheng y de Corea) se mantienen como `global`.
- Confirmar el nombre definitivo de la fila «Productivo».
- Luego: redactar Modernismo en inglés y español, con enlaces de contexto, verificación y `WARN` revisados; borrar los datos de prueba de ese carril.
- Los totales de las fichas usan plural fijo («1 obras»); mejorar si molesta.
- Pendiente de la Fase 7: revisión de equilibrio y revisión final con un agente independiente.
- **v06:** se elimina el lente «Ver el diseño desde» (decisión del usuario); su texto y los cambios clave quedan en la ficha de época. Disciplinas y Regiones suben a la barra superior junto a Contexto. Barras CONTEXTO y DISEÑO más oscuras (`--head-bg`, claro `#A9B0BC`, oscuro `#4A505B`). `app.js?v=5`, `style.css?v=5`. Imágenes de ayuda regeneradas.
- **v07:** (1) los nombres de elementos son cortos por sí solos: nada de «Nombre: explicación» (la explicación va en el texto); el build avisa si un nombre/título lleva «:» o pasa de 40 caracteres; `short` ya no es obligatorio (solo cuando el nombre sigue largo para la línea de tiempo). (2) «Estado actual» empieza con mayúscula (la ficha la fuerza y el build avisa si un texto corrido empieza en minúscula). (3) La imagen de la ficha es un enlace a su fuente en Commons (se quitan «Ver fuente» y el crédito; queda como tooltip). (4) «Efecto en el diseño» sin fondo especial. (5) Barras CONTEXTO y DISEÑO más claras: `--head-bg` claro `#CBD0D8`, oscuro `#394049`. (6) La línea de vida del diseñador (hover o selección) queda bajo los marcadores de obra y sus etiquetas. `app.js?v=6`, `style.css?v=6`.
- **v08:** barra superior con separación uniforme de 8 px entre búsqueda, tema, idioma, información y ayuda. El chip «Vida en producción» pasa a llamarse «Período de fabricación» (EN «Manufacturing span»); cambia en el chip, la ficha de obra, la ayuda y la especificación. `app.js?v=7`. `style.css?v=7`.
- **v10 (Fase 1):** Modernismo redactado (ver Estado). Investigación con cinco agentes en paralelo y revisión independiente de un sexto agente sobre 50 elementos; correcciones aplicadas. Código: se eliminan los enlaces con la LHA (`app.js?v=8`). Decisiones de la persona responsable: se mantienen CORFO y la primera televisión con enlaces débiles declarados; el traje de tweed pasa a «Tweed en Chanel» (uso desde c. 1924; el traje de museo es de 1954). Decisiones por defecto (anotadas en `PROGRESO-FASE1.md`): fechas de constructivismo (1921–1932), Nueva Objetividad (1924–1933), programa constructivista (1921), Olivetti (desde 1931), Chanel (desde 1914), Zig-Zag (desde 1919); autores sin ficha (Leete, Flagg, Holden, Bialetti…) en `maker`. Imágenes de ayuda regeneradas con la Cocina de Frankfurt.
- **v09b:** sin cambios de código. Se agregan `tools/GUIA-REDACCION-FASE1.md` (guía detallada para redactar el Modernismo en una sesión futura, con el anexo de listas aprobadas) y `tools/LISTAS-MODERNISMO.md` (las 245 listas aprobadas, guardadas en el proyecto). Siguiente paso: la Fase 1 con esa guía.
- **v11 (interfaz):** (A) una sola línea continua 1750–hoy con escala lineal o por densidad, barra de épocas en la línea (clic: ficha + zoom), vista inicial completa, filas reutilizadas, nivel de detalle según el zoom, barras largas como punto + etiqueta + flecha, sin dibujo del período de fabricación; (B) diseño sin carriles por disciplina (subfranjas por tipo, tonos neutros, disciplina solo en la obra); (C) curvas de conexión con tres botones y foco por fila de contexto; (D) modo `?editar` con `editar.php` (imagen por URL, revisión de fichas, resumen, marcas en la línea, exportar observaciones); (E) `data/all.json`, reglas nuevas en SPEC y build, etiquetas `short` más breves (55 elementos; el contenido del Modernismo no cambia), ficha general, ayuda e imágenes de ayuda rehechas. Se eliminó `src-data/before-1750/`. `app.js?v=11`, `style.css?v=11`.
- **v12 (correcciones a v11):** barra de épocas como primera fila de Movimientos (clic: ficha, sin zoom); tres subfranjas de diseño (se suma «Obras sin diseñador» a «Diseñadores y obras»); modos Diseñadores / Obras / ambos (obras agrupadas por disciplina con pocas filas; sin etiquetas cuando van sobre las líneas); instituciones como barras de color propio con punta de flecha; botón «Ver solo sus conexiones» en las fichas de obra, diseñador, movimiento e institución; el foco esconde lo no conectado. `app.js?v=12`, `style.css?v=12`.
- **v13 (el foco como eje):** los chips de Contexto pasan a ser botones «Foco:» («Lens:» en inglés), que esconden todo lo no conectado (un diseñador solo si está conectado él mismo), abren las partes de diseño con elementos conectados y muestran la ficha «Foco: …» (el diseño desde ese contexto, por época, con hechos y diseño conectado; textos generales en `UI.<idioma>.lens_*`). El foco se activa desde la barra, el nombre de la fila de contexto, la ficha de época, la sección Contexto de las fichas y las fichas de hechos, productivo y teoría. Un solo botón Conexiones (el foco lo enciende y al quitarlo vuelve a su estado); con foco, las curvas al contexto solo van a hechos de ese foco. Ya no se pueden ocultar filas de contexto con chips (se pliegan con la flechita). `app.js?v=13`, `style.css?v=13`.
- **v14 (puntos 1–4 de `tools/CAMBIOS-PENDIENTES.md`):** (1) flechas dobles de desplegar y plegar todo en las barras CONTEXTO y DISEÑO; se quitan los botones de la esquina del eje (con foco, CONTEXTO solo actúa sobre la fila del foco). (2) Al quitar el foco todo vuelve a la «foto» tomada al activarlo: filas, Conexiones, ficha abierta y desplazamiento (al salir del foco eligiendo otro hecho, solo filas y Conexiones). (3) El destacado deja el naranja: tinta (negro / blanco en oscuro) y negrita; relacionado en negrita con línea fina; marca «Observada» neutra; números de la ayuda en tinta. (4) El nombre de la subcategoría es el activador del foco en todo el sitio (barra, línea, ficha de época, sección Contexto, sobretítulo de fichas de hecho, productivo y teoría); se quitan los botones «Foco». `app.js?v=14`, `style.css?v=14`.
- **v15 (puntos 5–10 de `tools/CAMBIOS-PENDIENTES.md`):**
  - (5) Flechas dobles a la izquierda de CONTEXTO; DISEÑO ya no las tiene.
  - (6) «Disciplinas» en negrita y sus chips activos más oscuros.
  - (7) DISEÑO sin subfranjas plegables. La barra de épocas es la primera fila de DISEÑO. Nuevo control «Organizar»: cronológica, por disciplina (Interdisciplinario = 2 o más disciplinas) y por región (Europa, Norteamérica, América Latina, Varias regiones, Global). Se quita el filtro Regiones.
  - (8) La ficha de época se cierra; sin selección, la ficha muestra un mensaje.
  - (9) En la vista por región, las regiones se dividen en zonas culturales estables (tabla país → zona en `app.js`). Se reordenó el país principal (primero de `countries`) de 9 diseñadores; es un cambio de datos, no de contenido.
  - (10) Instituciones en el mismo gris que los movimientos; los movimientos, algo más oscuros.
  - Los nombres de grupo y de zona siguen la vista al desplazarse. `app.js?v=15`, `style.css?v=15`.
- **v16 (puntos 11–13):**
  - (11) En las vistas cronológica y por disciplina, línea punteada tenue y nombre chico gris entre los bloques Movimientos, Instituciones y Diseñadores y obras. Los nombres siguen la vista al desplazarse.
  - (12) Instituciones como barras blancas con contorno gris y punta de flecha.
  - (13) Doble clic en un elemento: lo elige y activa «Ver solo sus conexiones»; otro doble clic lo quita. Doble clic en una época: acerca la vista. Las fichas de hechos, productivo y teoría también tienen el botón de filtro.
  - `app.js?v=16`, `style.css?v=16`.
- **v17 (prueba por fecha, hoy parte del sitio):**
  - «Organizar» tiene ahora «Por categoría» (la vista anterior) y una nueva vista **«Por fecha»**: una fila por elemento, ordenada por año de inicio, con divisiones por década.
  - Contorno de 1 px en las instituciones.
  - `app.js?v=17`, `style.css?v=17`.
- **v18 (puntos 17–22):**
  - (17) En «Por fecha» se ocultan los diseñadores; al elegir uno aparece su línea en la fila de su primera obra.
  - (18) Minimapa del tiempo con corchetes sobre los años, y arrastre sobre los años para acercarse a un tramo.
  - (19) Flechas ‹ › en los extremos del eje: suman un 25 % de años por ese lado; mantener apretado repite.
  - (20) «De [año] a [año] Todo» en la esquina del eje; se quitan los botones − y +.
  - (21) La teoría pasa a DISEÑO: bloque «Teoría», chip en Mostrar, sin foco «Teórico». Su disciplina sale del género. Los hechos de contexto pueden enlazar con textos teóricos (`DESIGN_KINDS` del build).
  - (22) Grupos plegables en todas las vistas de Organizar, y flechas dobles (⌄⌄ / ››) en CONTEXTO y DISEÑO, dibujadas como las flechitas simples.
  - `app.js?v=18`, `style.css?v=18`.
- **v19 (puntos 23–30):**
  - (23) Una sola flecha doble por sección (CONTEXTO, DISEÑO) que alterna como las flechitas: ⌄⌄ si hay algo abierto (pliega todo), ›› si todo está plegado (despliega). Se dibuja al final de `build()` (`secFill`), cuando ya se sabe el estado.
  - (24) Al arrastrar sobre los años, el tramo se sombrea en toda la altura de la línea (`#vsel`).
  - (25) Botones de ícono ⟷ (línea completa) y |⟷| (ajustar a lo que se muestra, `visibleSpan()`): del inicio más temprano al más tardío de lo visible, con el fin de las barras cortas y un 4 % de margen. No cuentan los grupos de diseño plegados ni el nivel de zoom. Cada botón se atenúa si ya está en ese estado.
  - (26) Las líneas de vida de los diseñadores van en el color de sus disciplinas (`disciplines`): una disciplina va en color sólido y varias, en rayas alternas de 10 px (`desBar`, variables `--dbg`/`--dbf`).
  - (27) Lo elegido queda en tinta; lo relacionado conserva su color: hechos en el color de su fila, obras con etiqueta y anillo de su disciplina, diseñadores con la línea a color pleno. Las curvas van en el color de lo que alcanzan (`curveCol`).
  - (28) La escala pasa de «Por densidad / Lineal» a «Visual / Cronológica» (en inglés, Visual / Chronological).
  - (29) Se quitan los dos puntos de «Foco» y «Organizar».
  - (30) El chip «✕ Solo: …» va invertido en tinta.
  - `app.js?v=19`, `style.css?v=19`.
- **v19.1 (puntos 31–32):**
  - (31) Productivo pasa de gris a petróleo: tema claro `28, 128, 150` con texto `#155F70`; tema oscuro `86, 178, 196` con texto `#8CCAD8`.
  - (32) Los botones de Disciplinas llevan su color:
    - encendidos, borde y texto del color con un fondo apenas teñido;
    - apagados, el mismo color desteñido.
  - `?v=19.1`.
- **v19.2 (punto 33):**
  - El filtro «Solo» de un movimiento o de una institución también deja las obras que sus diseñadores hicieron mientras existió; una institución sin cierre cuenta hasta hoy (`makeIso`).
  - Esas obras van sobre la línea del diseñador, sin curva propia.
  - `?v=19.2`.
- **v19.3 (punto 34):**
  - La esquina del eje queda como «[1750] – [2026] Todo Ajustar» (en inglés «All» y «Fit»). Se quitan los íconos ⟷ y |⟷|, que se confundían.
  - La esquina mide lo mismo que la columna de nombres (190 px) y el eje queda alineado.
  - `?v=19.3`.
- **v20 (puntos 35–42, primera ronda de contenido):**
  - **Niveles de detalle:** campo `level` (imprescindible ★ / normal / completo) y control «Detalle» (Normal por defecto). Al navegar a un elemento de un nivel mayor, el detalle sube solo.
  - **Épocas:** se eliminan de la interfaz. Se reemplazan por los macromovimientos Modernismo y Posmodernismo, con ficha especial; la Revolución Industrial pasa a ser un hecho de contexto. Las carpetas por época quedan solo como orden de los archivos.
  - **Obras nuevas:** cuatro obras verificadas (Moholy-Nagy, Zwart, Meyer, Bel Geddes). Ningún diseñador queda sin obra; el build lo exige.
  - **Fichas:** «Acerca de» reescrita; «Saber más» con fuentes y sin Wikipedia; sin «Buscar en» ni «Dónde verla».
  - **Conexiones:** las indirectas se dibujan con línea fina y entran en «Solo».
  - **Manual:** nuevo `tools/MANUAL-CONTENIDO.md`. Los pendientes quedan al final de `tools/CAMBIOS-PENDIENTES.md`.
  - `?v=20`.
- **v21 (puntos 43–44, fase A):**
  - **Fuentes numeradas (A0):**
    - campo `refs` en fichas, enlaces y conexiones;
    - marcas `[n]` en los textos;
    - el sitio público las borra (también de la búsqueda);
    - en `?editar` son superíndices que llevan a «Revisión → Fuentes», con las fuentes de la ficha y de sus enlaces numeradas en una sola serie;
    - el build valida marcas, URL https, EN = ES, fuentes sin citar y Wikipedia, y cuenta las fichas sin fuentes;
    - prueba nueva `tools/tests/test_v21.py`.
  - **Revisión de enlaces (A1, `tools/REVISION-ENLACES-MODERNISMO.md`):**
    - se eliminan 16, se reescriben 14 y se trasladan 3;
    - todos los que siguen tienen `refs`;
    - CORFO y Primeras transmisiones de televisión pasan a `tools/RESERVA-FASE-B.json`.
  - **Correcciones:** cartel *Power* 1930; *El Peneca* 180.000 ejemplares hacia 1940; Stölzl; Chanel en Deauville en 1912; Nuevo Frankfurt con 12.000 a 15.000 viviendas; «Saber más» del vestido langosta.
  - **Contenido nuevo:**
    - 8 hechos de contexto (Revolución mexicana, en `reform`; Viena Roja, Era Vargas, Auge de la publicidad, NEP, Campañas de alfabetización, Revistas de moda, Teléfono automático);
    - 13 diseñadores;
    - 43 obras (la de Zwart quedó en reserva por falta de fuente sobre su contenido);
    - 4 conexiones;
    - unos 90 enlaces nuevos, todos con fuentes.
  - **Pruebas:** `test_v20` se ajustó a los datos nuevos (el pequeño vestido negro pasó del fordismo a las revistas de moda).
  - `?v=21`.
- **v22 (puntos 45–46, fase A):**
  - **Conceptos en el macromovimiento (punto 45):** la ficha del macromovimiento muestra los conceptos de las épocas que abarca (función `macroConceptsHtml` en `app.js`). El Modernismo muestra los 8; el Posmodernismo, ninguno todavía.
  - **Revisión independiente aplicada (punto 46):** detalle en la sección 5 de `tools/REVISION-INDEPENDIENTE-FASE-A.md`.
    - 11 errores corregidos (Adrian, marajoara, Vogue 1937, WPA, Frye, Kubus, Popover, REA, Brodovitch, Breuer, Campari).
    - Dudosos y estilo aplicados con fuentes nuevas abiertas en la web (Cooper Hewitt, AAA, ICP, FIT, MoMA, Werkbundarchiv, The Henry Ford, London Transport Museum, Memoria Chilena, PBS, Docomomo Ibérico, Itaú Cultural, La Tempestad).
    - 9 enlaces suspendidos y el hecho «Cine sonoro» pasan a `tools/RESERVA-FASE-B.json` (`suspended_links`, `contexts`).
    - Nuevo diseñador `lucio-costa`; 11 enlaces nuevos (9 propios de diseñadores, Guerra Civil → BKF y uno más).
    - Fechas corregidas: logotipo del metro 1916, Clichy 1935–1938, dispensario 1933–1938; «Metros y transporte eléctrico» desde 1916; «Teléfono automático» solo EE. UU. hasta tener fuente europea.
  - **Manual 7.1:** la `key` de los hechos de contexto resume lo marcado; marcar solo lo que la fuente dice; atribuir lo que dicen fabricantes o blogs.
  - **Pruebas:** nueva `tools/tests/test_v22.py`; `test_v20` ajustada (Chanel ya no tiene enlace tecnológico).
  - `?v=22`.
- **v23 (punto 47, A6 lote 1):**
  - 30 obras ★ trazadas con fuentes (5 revisiones paralelas; un revisor independiente contrastó 8 de 12 correcciones clave).
  - Registro: `tools/A6-LOTE1-FUENTES.md`.
  - Correcciones de contenido aplicadas (KdF-Wagen, Johnston, mapa del metro, Narkomfin, Utility, Chanel, vestido langosta, Adolf, Kitchener, medias de nailon y otras); esperan el visto bueno.
  - `?v=23`.
- **v24 (puntos 48–51):**
  - **Dos niveles:** `LEVELS = ['essential', 'normal']` en `app.js` y el build; 48 elementos de `complete` pasaron a `normal`; un nivel guardado «complete» cae en «normal».
  - **Contexto colapsado al abrir:** todas las filas, incluido «Productivo».
  - **Macromovimientos:** sin fila propia; se dibujan primero en la fila «Movimientos» con `drawMv` (filas propias arriba), se ocultan con «Movimientos», entran en «Solo», foco y niveles. Su etiqueta se desliza (`stickyNames`) para seguir visible mientras su tramo está en pantalla. «Ajustar» sigue sin contarlos.
  - **Contraseña** de `?editar`: `lhd`.
  - **Documentación:** manual (niveles), `PLAN-FASES.md` replanificado (A4 cerrada; tamaños B–E reducidos), `SPEC.md`, `PROPUESTA-NIVELES.md`, `LISTAS-FASE-A.md`, `INICIO-SESION-NUEVA.md`. Imágenes de ayuda regeneradas.
  - **Pruebas:** nueva `test_v24.py`; `test_general`, `test_v19` y `test_v20` ajustadas.
  - `?v=24`.
- **v25 (punto 52, A6 lote 2):**
  - 62 obras Normal trazadas (8 revisiones paralelas; revisor independiente sobre 12 correcciones clave).
  - Registro: `tools/A6-LOTE2-FUENTES.md`. Notas de producción sin cifras sin fuente; materiales y fechas corregidos.
  - `?v=25`.


## v38 (4 de octubre de 2026) — punto 70
Los movimientos y macromovimientos se dibujan siempre sobre su extensión temporal real (antes, los de más de 30 años o 75 % del ancho se acortaban a punto + etiqueta + flecha). La etiqueta (`.mt`) se desliza dentro de la barra para quedar a la vista. Cambios: `app.js` (`drawMv` y el manejador de etiquetas pegajosas), `style.css`, `?v=38`. Instituciones y hechos de contexto largos siguen acortados. Tests OK.

## v39 (4 de octubre de 2026) — puntos 71 a 73 (solo documentos)

- Sin cambios en el sitio ni en los datos (`app.js`, `style.css` y `src-data/` iguales a v38; `index.html` solo sube `?v=39`).
- `tools/PLAN-CIERRE.md` pasa a **v8**: nueva **etapa 6** (sección 9b, pasos 6.1 a 6.8) entre la etapa 5 y la Parte II: levantamiento transversal y complemento hasta **≥ 500 obras** (todos los diseñadores y obras razonables para un curso universitario de historia del diseño: gráfico, producto, moda y arquitectura; movimientos arquitectónicos de las últimas cuatro décadas; instituciones y documentos como el Premio Pritzker); propuesta **V3** con conexiones y crecimiento por período; redacción completa tras el V3; **V2 movido al final de la etapa 6**; regla **C4c** (enlaces directos relajados solo en casos excepcionales y anotados; nadie desconectado; se pueden agregar hechos de contexto); Parte II recalculada (R2 a R4 de 12 a ~16 a 18 sesiones).
- Punto 72: la etiqueta visible del nivel «Normal» pasa a «Completo» en el paso 6.7 (valor interno `normal` sin cambio); deseable D5 reformulado.
- Documentos ajustados: `MANUAL-CONTENIDO.md`, `PROPUESTA-NIVELES.md`, `LISTAS-CIERRE.md`, `SPEC.md`, `INICIO-SESION-NUEVA.md`, `ESTADO-ACTUAL.md`, `CAMBIOS-PENDIENTES.md`.
- La etapa 5 sigue sin iniciar.

## v40 (4 de octubre de 2026) — punto 74 (solo documentos)

- Aprobados los puntos 54, 67, 68 y 69; cerrados el 41, los 1 a 6 y 9 de «Pendientes para recordar». Punto 65 decidido (contar contexto directo / indirecto / ninguno en el build y la auditoría R1), aún sin implementar (se hará con «implementa», propuesta: paso 6.7 del plan). `index.html` sube a `?v=40`; sitio y datos sin cambios.
- Mauricio confirmó el punto 65 en el paso 6.7; incorporado al plan (6.7 c, 6.2 y R1.1).

## v41 (4 de octubre de 2026) — solo documentos

- Punto 65 confirmado en el paso 6.7 e incorporado al plan v8 (6.7 c, 6.2, R1.1). Sitio y datos sin cambios; `index.html` sube a `?v=41`.

## v42 (4 de octubre de 2026) — punto 75: etapa 5 (Industrial)

- Contenido: tramo `industrial` completo según `LISTAS-CIERRE.md`, escrito con agentes Sonnet en 9 lotes en paralelo (contexto, productivo, teoría, movimientos, instituciones, diseñadores, 30 obras) más 5 lotes de enlaces, conexiones y relleno; todo sin fuentes (`refs: []`, ficha «no revisada»). Cifras: 30 obras (9 ★; gráfica 10, producto 9, arquitectura 7, moda 4; América Latina 3), 14 diseñadores, 23 hechos de contexto, 9 productivos, 5 teorías, 5 movimientos, 6 instituciones, 63 enlaces, 16 conexiones.
- Desviaciones: ver punto 75 y `PENDIENTES-FUENTES.md` (reserva de telégrafo, fotografía y estampado con cilindros; Bodoni 1788; niveles).
- Pruebas: build sin PROBLEM; `listas_check.py` 0 errores; `run_all.sh` todo PASS. Se ajustó `test_preview.py` (la vista previa ya no tiene fichas nuevas sin escribir) y `LISTAS-CIERRE.md` (filas movidas a la reserva, Bodoni).
- Rendimiento: `all.json` 2,8 MB; carga de la página 0,45 s; sin errores de página. Captura de la línea completa revisada.
- Sitio: sin cambios de código; `index.html` sube a `?v=42`.

## v43 (4 de octubre de 2026) — punto 76: etapa 6, pasos 6.1 y 6.2 (hasta el V3)

- Sin cambios en el sitio ni en los datos (`src-data/` igual a v42; `index.html` sube a `?v=43`).
- Nuevo: `tools/LEVANTAMIENTO-ETAPA6.md`, `tools/PROPUESTA-ETAPA6.md` y `.json`, `tools/pipeline/briefs/BRIEF-ETAPA6.md`, `tools/pipeline/propuesta_etapa6.py` (+ `propuesta_etapa6_nota.md`). Seis agentes Sonnet propusieron faltantes por disciplina; se fusionaron (7 ids repetidos y 7 alias unificados), se quitaron 2 diseñadores sin obra, se bajaron 4 diseñadores ★ a Normal y se pidió un segundo enlace directo para 26 obras ★ (8 conseguidos).
- Resultado de la propuesta: 585 obras, 342 diseñadores, 76 movimientos, 94 instituciones, 80 teorías y 183 hechos de contexto si se aprueba todo.
- La etapa 6 queda detenida en el paso 6.3 (V3) a la espera de la persona responsable.

## v44 (5 de octubre de 2026) — punto 77: V3 aprobado; etapa 6, pasos 6.4 a 6.8
- **Datos:** 373 → **585 obras** (+212; ★ 109 → 165), diseñadores 185 → 339, movimientos 76, instituciones 94, teorías 78, productivos 65, contextos 183, enlaces 1.118, conexiones 107. Por tramo (obras): Industrial 53, Reforma 94, Modernismo 155, Posguerra 143, Posmoderno 140. América Latina 12 % de las obras (Posguerra 20 %). Sin fuentes (`refs: []`).
- **Método:** `tools/pipeline/prep_etapa6.py` arma 56 lotes desde `PROPUESTA-ETAPA6.json`; agentes Sonnet con `briefs/BRIEF-ETAPA6-REDACCION.md`; `validate_out.py` (conoce los ids de la propuesta); `apply_new.py` por tramo; `fix_etapa6.py` (enlaces de teorías, `kind`, `maker`, años); lote de relleno de contexto (22 `sin_enlace`).
- **Interfaz:** `lv_normal`/`lvTip_normal` ahora «Completo»/«Complete» (valor interno `normal`); ayuda actualizada. `?v=44`.
- **Build:** conteo del punto 65 (`ctx_coverage`: directo / solo indirecto / ninguno; guarda `ctxDirect`, `ctxIndirect`, `ctxNone` en `stats`). Hoy 540 / 25 / 20.
- **Rendimiento:** `all.json` 3,9 MB; carga local 0,45 s con 585 obras. Capturas verificadas (línea ES clara, EN oscuro, ficha del Guggenheim Bilbao, móvil 390 px).
- **Pruebas:** `test_preview` y `test_etapa1` ajustadas (≥ 500 obras; `claire-mccardell` y `adrian` repuestos a propósito).
- Pendiente: V2 de Mauricio. Parte II no iniciada.

## v45 (5 de octubre de 2026) — punto 78: revisión editorial externa (etapa 7, paso 7.1; solo documentos)
- **Sin cambios en el sitio ni en los datos** (`app.js`, `style.css`, `src-data/` iguales a v44); `index.html` sube a `?v=45`.
- **Nuevo:** `tools/REVISION-EDITORIAL-ETAPA7.md` (revisión editorial independiente en tono académico: dictamen, canon de contraste, diagnóstico de movimientos, instituciones, teoría, diseñadores, obras, contexto y productivo, revisión de los ★, correcciones de datos, decisiones D1 a D8 para el V4, instrucciones y anexos A a F), `tools/REVISION-ETAPA7.json` (193 elementos nuevos, formato de `PROPUESTA-ETAPA6.json` más `prioridad` A/B/C), `tools/REVISION-ETAPA7-AJUSTES.json` (niveles, fusiones, pertenencias, correcciones, reserva) y `tools/pipeline/etapa7_anexos.py` (regenera los anexos desde los JSON).
- **Plan v9:** etapa 7 (sección 9c, pasos 7.1 a 7.8) entre la etapa 6 y la Parte II; nuevo visto bueno V4; se propone mover el V2 (6.8) a 7.8. Ajustados el resumen, el mapa de etapas, la estimación de sesiones y el seguimiento.
- Documentos ajustados: `PLAN-CIERRE.md`, `CAMBIOS-PENDIENTES.md` (punto 78), `ESTADO-ACTUAL.md`, `INICIO-SESION-NUEVA.md`.
- Pendiente: V4 de Mauricio. La etapa 7 no avanza (7.3 en adelante) sin su visto bueno.

## v46 (5 de octubre de 2026) — punto 79: V4, preparación de la etapa 7 (paso 7.3), etapa 8 y Parte III (plan v10)
- **Sin cambios en el sitio ni en los datos** (`app.js`, `style.css`, `src-data/` iguales a v45); `index.html` sube a `?v=46`.
- **V4:** A y B aprobados (171 registros), C a la Parte III (26); decisiones D1 a D8 en `REVISION-ETAPA7-AJUSTES.json` → `decisiones_V4` y en el recuadro de `REVISION-EDITORIAL-ETAPA7.md`.
- **Nuevo:** `tools/GUIA-EJECUCION-ETAPA7.md` (guía para Sonnet), `tools/ESPEC-ETAPA8.md`, `tools/pipeline/ajustes_etapa7.py`, `prep_etapa7.py`, `check_etapa7.py`, `briefs/BRIEF-ETAPA7-REDACCION.md`.
- **Código de herramientas:** `tools/build_data.py` acepta `posthumous: true` en obras (no comprueba la vida del diseñador; SPEC 5.5); `tools/pipeline/validate_out.py` cuenta como planificados los ids `aprobado-V4` de `REVISION-ETAPA7.json`; `etapa7_anexos.py` con cifras dinámicas y Anexo G.
- **Ensayo:** `ajustes_etapa7.py estructura` sobre una copia → 225 cambios, 45 archivos, build «OK: no PROBLEM» (587 obras, 341 diseñadores, 73 movimientos, 93 instituciones, 64 productivos); `niveles` sobre esa copia solo falla por `louis-sullivan` (espera el Wainwright ★ de 7.5), como se esperaba.
- Documentos: `PLAN-CIERRE.md` v10 (7.2 y 7.3 marcados, regla C4d, sección 9d, Parte III), `MANUAL-CONTENIDO.md` (D3 y D2), `SPEC.md` 5.5, `CAMBIOS-PENDIENTES.md` (punto 79), `ESTADO-ACTUAL.md`, `INICIO-SESION-NUEVA.md`.

## v47 (5 de octubre de 2026) — punto 80: etapa 7, paso 7.4 (ajustes estructurales)
- `ajustes_etapa7.py estructura --aplicar`: 225 cambios en 45 archivos de `src-data/`; 587 obras, 341 diseñadores, 73 movimientos, 93 instituciones, 64 productivos; build «OK: no PROBLEM». Retiros y reserva D7 en `RESERVA-FASE-B.json` → `etapa7_retirados`; 11 fichas repuestas del recorte del Modernismo.
- Código del sitio (`app.js`, `style.css`) sin cambios; `index.html` sube a `?v=47`. Pruebas ajustadas por conteo (C6): `test_etapa1`, `test_preview`, `test_v31` (esta última rota en silencio antes de 7.4), y `listas_check.py` (ids movidos de carpeta).

## v48 a v51 (5 de octubre de 2026) — punto 85: etapa 7, pasos 7.5 y 7.6 (en tandas)
- **7.5 en tres tandas por período** (v48 Industrial+Reforma+Modernismo, v49 Posguerra, v50 Posmoderno): 160 fichas nuevas redactadas por agentes Sonnet desde `tools/pipeline/e7_work/` (lotes y salidas), validadas con `validate_out.py` y aplicadas con `apply_new.py`; `ajustes_etapa7.py relaciones` aplicado por tanda. Cifras tras 7.5: 652 obras, 385 diseñadores, 80 movimientos, 100 instituciones, 68 productivos, 194 contextos, 100 teorías.
- **7.6 (v51):** 5 lotes de enlaces D3 (13 aplicados; 7 `sin_enlace` o ya existentes) y 9 reescrituras con `apply2.py`; excepciones C4c anotadas una por una en `PENDIENTES-FUENTES.md`.
- **Herramientas:** `ajustes_etapa7.py relaciones` ahora liga también `links.works` de los productivos nuevos con sus anclas (el build lo exige); `listas_check.py` acepta los dos ids de Werkbund movidos a `modernism`; pruebas ajustadas por conteo (C6): `test_etapa1`, `test_preview`, `test_v31` (esta última estaba rota en silencio desde antes). Ajustes a mano de datos aprobados por Mauricio: enlaces de las teorías de Smith, Forty, Simmel, Giedion y Lynch; Prada como diseñadora de su mochila; tres estilos nuevos en `macro-modernism`.
- Código del sitio sin cambios (solo `index.html` `?v`).

## v52 (5 de octubre de 2026) — punto 85: etapa 7, pasos 7.7 y 7.8
- **7.7:** `ajustes_etapa7.py niveles --aplicar` (102 cambios de nivel, 35 archivos): 181 obras ★ (27,8 %), 102 diseñadores ★, 35 movimientos ★. **«Acerca de» (D8):** sección «Fundamento conceptual y bibliográfico» (dos párrafos y la bibliografía base en cinco grupos, ES y EN) con `BASIS` y `basisList()` en `app.js` y la regla `.basis` en `style.css`; `index.html` sube a `?v=52`. Contraste sin valores bajos; carga local ≈ 1,2 s; capturas ES claro y EN oscuro sin errores de página.
- **7.8:** ZIP `LHD-v52.zip`. Pendiente de Mauricio: 4 movimientos ★ sin obra ★ visible (`PENDIENTES-FUENTES.md`, «paso 7.7»).

## v53 (5 de octubre de 2026) — punto 87: movimientos ★ sin obra ★
- Decisión de Mauricio: suben a ★ `opera-garnier-1875`, `merz-magazine-1923` y `ciudad-abierta-1970`; diseño sostenible queda como está. 184 obras ★ (28,2 %). Solo datos; `index.html` `?v=53`.

## v54 (5 de octubre de 2026) — punto 88: etapa 8, pasos 8.1 a 8.5
- `app.js`: `makeScope/applyScope/setScope` (alcance por disciplina), `cardKind()`, `discCard()`, `lensCard()` con ensayo, `essayOf()` (carga perezosa de `data/essays.json`), `head()` con advertencia «No revisada», barra de filtros reordenada. `style.css`: `.chip.scope`, `.essay`, `.el-link`, `.pdf-btn`, `.unrev-note`.
- `tools/build_data.py`: lee y valida `src-essays/essays.json`; escribe `data/essays.json`. `tools/pipeline/briefs/BRIEF-ENSAYOS.md`, `tools/pipeline/validate_essay.py`, `tools/pipeline/e8_work/` (salidas de los agentes y catálogo de ids).
- Pruebas: `tools/tests/test_etapa8.py` (en `run_all.sh`); `test_general.py` adaptado. `index.html` `?v=54`.

## v55 (5 de octubre de 2026) — punto 89: etapa 8, paso 8.5b
Imágenes de las fichas (`src-images/images.json` → campo `images`), galería con carrusel (`imgGallery`), galerías de movimientos desde obras ★, portada de teorías. 816 de 1.237 elementos con imagen; segunda pasada pendiente. Prueba nueva: `test_imagenes.py`.

## v56 (5 de octubre de 2026) — punto 90: sin PDF de ensayos; aviso «no revisada» en rojo claro
Se eliminan `make_essays_pdf.py`, `ensayos/`, el botón «Descargar PDF» y `pdfs` en `essays.json`. `--warn`/`--warn-bg` en rojo claro.

## v57 (5 de octubre de 2026) — punto 91: subtítulos en negro y texto de presentación
`style.css` (`.sect h3`, `.essay-sub` en `--ink`); `infoCard()` y textos `info*` de `app.js` reescritos; `cell()` acepta texto (arreglo del NaN).

## v58 (5 de octubre de 2026) — punto 92: subtítulos de bibliografía en gris
`.info-sub.basis-h` en `style.css`; clase agregada en `basisList()`.

## v59 (5 de octubre de 2026) — punto 96: 8.5b, segunda pasada de imágenes
Se añadieron 286 imágenes libres de Commons (1.102 de 1.237 fichas con imagen, 89 %). Informe con cobertura por tipo y era y las 135 excepciones: `audit/INFORME-IMAGENES.md`. Picks en `tools/pipeline/e8_img/res/011.json`.

## v60 (5 de octubre de 2026) — punto 97: 8.5c, modo edición, resumen y épocas por años
Contraseña `uai2026` pedida al editar (cuadro emergente; la acción continúa sola); resumen con cifras y listado de imágenes y tres listados colapsables cerrados al abrir; épocas nombradas por años con `eraName(e)`. Pruebas: `test_editar.py` reescrita.

## v61 (5 de octubre de 2026) — punto 98: 8.6, pruebas e integración
Foco con diseñadores de obras conectadas (`.ind`), «Por disciplina» sin «Interdisciplinario» (`discGroups`, copias de diseñador por disciplina), imágenes con pie solo en carruseles, enlace a la fuente y línea «Imagen:» en «Fuentes» (`imgRefHtml`, `S.imgRefs`). Prueba nueva: `test_etapa86.py`.

## v62 (5 de octubre de 2026) — punto 99: 8.7, V2 dado
Mauricio da su OK al sitio completo; **Parte I cerrada**. Solo documentos y `?v=62`; datos y código iguales a v61. Sigue la Parte II (R1).

## v63 (5 de octubre de 2026) — punto 100: Parte II, R1
Auditoría automática (`tools/pipeline/auditoria.py`, informe en `audit/INFORME-R1.md`), interruptor `STRICT_THEORY_SOURCES`, limpieza mecánica (`r1_limpieza.py`: 209 `short`, 2 enlaces repetidos quitados, 1 enlace nuevo) y prueba `test_r1.py`. Datos: 1.310 enlaces (antes 1.311); el código del sitio no cambió.

## v64 (5 de octubre de 2026) — punto 101: Parte II, R2, lote 01
Primer lote de fuentes (4 obras ★ industriales: Baskerville, Bodoni, Penny Black, Encyclopédie). Solo cambian esos 4 elementos y la versión de caché.

## v76 (6 de octubre de 2026) — punto 103: R2.0, herramientas de la R2 ampliada
`prep_r2.py`, `check_r2.py` y `apply2.py` cubren los diez tipos del plan (más `r2lib.py` y `plantillas_r2.json`); `auditoria.py --v1`; incidencias como datos (`tools/r2_incidencias.json`, `r2_incidencias.py`) y `incidencias_xlsx.py`. Sitio: los ensayos muestran las marcas `[n]` como superíndices y una sección «Fuentes del ensayo» (`essaySources`, `rfRow` compartida con las fichas); el build valida las marcas de los ensayos. Pruebas nuevas: `test_ensayos_fuentes`, `test_r2_tools`, `test_r2_incidencias`, `test_r2_auditoria`; `test_preview` usa `$CHROMIUM`. Datos de contenido sin cambios.

