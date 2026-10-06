# LHD: cómo retomar el proyecto en una sesión nueva

*Estado al 6 de octubre de 2026: versión **v76** (R2.0 hecha; ver `ESTADO-ACTUAL.md`). Antes: **v64** (Parte I cerrada; R1 hecha; **R2 empezada**, lote 01). Antes: **v62** (V2 dado). Antes: **v61** (etapa 8: pasos 8.1 a 8.6). Antes: **v46** (V4 dado; etapa 7 preparada, con guía para Sonnet; etapa 8 y Parte III en el plan). Antes: v45 (revisión editorial externa), v44 (etapa 6 redactada). Antes: **v38** (etapas P, 0, 1, 2, 3 y 4 ejecutadas; V1 aprobado, recorte del Modernismo aplicado, Posguerra, Reforma y Posmoderno escritas). **Lo que cambia en cada entrega está en `ESTADO-ACTUAL.md`** (siguiente paso, decisiones pendientes, cifras y mensaje para pegar).*

## 1. Qué es

La **Línea de Historia del Diseño (LHD)** es un sitio estático, bilingüe (español de Chile e inglés), que apoya un curso universitario de historia del diseño.
- **Una sola línea continua de 1750 a hoy.** Arriba va el CONTEXTO (político, económico, social, cultural, tecnológico y productivo); abajo, el DISEÑO (macromovimientos, movimientos, instituciones, teoría, diseñadores y obras).
- **Tesis:** el diseño es una respuesta a su contexto. Lo central son las **conexiones**.
- **Contenido real:** el Modernismo (1914–1945, recortado): 120 obras (37 ★), 64 diseñadores, 41 hechos de contexto, 236 enlaces, con fuentes; y, **sin fuentes todavía** (Parte II): la **Posguerra (v35)**, 90 obras (24 ★), 44 diseñadores, 36 hechos de contexto, 142 enlaces; la **Reforma (v36)**, 60 obras (18 ★), 28 diseñadores, 30 hechos de contexto, 103 enlaces; y el **Posmoderno (v38)**, 73 obras (21 ★), 35 diseñadores, 30 hechos de contexto, 112 enlaces. y el **Industrial (v42)**, 30 obras (9 ★), 14 diseñadores, 23 hechos de contexto, 63 enlaces (también sin fuentes). Con eso la línea tiene 373 obras.
- **Qué se está haciendo:** completar la línea con una cantidad de contenido **equilibrada según la importancia histórica de cada época** (meta hasta la etapa 5: **375 obras**; el Modernismo se recorta a 120 en lo no esencial; punto 61). **Desde el plan v8 (puntos 71 y 72) hay una etapa 6 que lleva la línea a ≥ 500 obras**, con todos los diseñadores y obras que un curso universitario de historia del diseño esperaría (gráfico, producto, moda y arquitectura), arquitectura reciente e instituciones relevantes (p. ej. Premio Pritzker). Primero **contenido y conexiones**; las **fuentes y la revisión** van aparte (Parte II del plan).

## 2. Qué leer, en este orden

1. **Este archivo y `ESTADO-ACTUAL.md`** (la hoja de estado, que cambia en cada entrega; trae el siguiente paso).
   - `LEEME-PROBAR-EN-WEB.md`: cómo probar el sitio en local y subirlo a un hosting.
2. **`tools/PLAN-CIERRE.md` (v10): qué falta hacer, etapa por etapa. Para la etapa 7, leer además `tools/GUIA-EJECUCION-ETAPA7.md`; para la etapa 8, `tools/ESPEC-ETAPA8.md`. Es el único plan vigente: ejecutar el siguiente paso sin marcar (casilla `[ ]`).** Trae las reglas (sección 1), los tamaños (sección 3), el recorte del Modernismo (3.0), qué modelo usar en cada paso (sección 2) y los textos de los briefs (anexos A y B).
3. `tools/MANUAL-CONTENIDO.md`: reglas de contenido vigentes (niveles, inclusión, conexiones, prueba de tres preguntas, fuentes). **Manda sobre todo lo demás en contenido.**
4. **`tools/CAMBIOS-PENDIENTES.md`:** registro numerado de cada decisión de la persona responsable (consultar el final: puntos 53 a 79 y «PENDIENTES PARA RECORDAR»). El próximo punto es el **104**.
5. `PROJECT.md`: bitácora por versión (v01–v44) y decisiones técnicas. Los documentos de verificación y revisión de las fases anteriores se retiraron del paquete: las menciones a ellos son históricas.
6. Según la tarea:
   - `tools/SPEC.md`: especificación técnica y listas iniciales de cada tramo, sección 10. Las notas de actualización al comienzo mandan sobre el texto original.
   - `tools/PROPUESTA-NIVELES.md`: nivel de cada elemento actual (sirve para no recortar ★ del Modernismo).
   - `tools/RESERVA-FASE-B.json`: hechos de contexto retirados (`ctx-corfo`, `ctx-early-television`, que se reintegran en la etapa 1) y enlaces suspendidos.
   - `tools/PENDIENTES-FUENTES.md`: lo que falta de fuentes y los descartes.
   - `tools/pipeline/`: scripts y briefs para trabajar con agentes en paralelo.

## 3. Cómo trabajar con la persona responsable (acordado)

- **Idioma y forma:**
  - Hablar en **español de Chile** («computador», «auto», «departamento»).
  - Respuestas breves y claras.
  - Cada entrega lleva un resumen corto: qué cambió, qué revisar, qué no se pudo verificar.
- **Protocolo de comentarios:**
  - La persona escribe observaciones mientras revisa el sitio. **No se implementan de inmediato**: se registran como puntos numerados en `tools/CAMBIOS-PENDIENTES.md` (el próximo es el **104**).
  - Junto con cada punto se le avisa de los posibles problemas y se le pregunta lo necesario.
  - **Solo se implementa cuando dice «implementa».**
- **Decisiones visuales:** cuando duda, mostrar maquetas (capturas con la opción aplicada por inyección de CSS o JS, sin tocar el sitio) y recomendar una.
- **Contenido:**
  - Las **listas maestras** se proponen y se aprueban una vez (V1) antes de redactar; después se trabaja con pocas aprobaciones (plan, sección 0).
  - **Parte I del plan (contenido nuevo): sin fuentes** (`refs: []`, sin marcas `[n]`, sin buscar en la web; regla C1 a C3 del plan). **Parte II (fuentes y revisión):** `refs` con enlace directo y marcas `[n]` (manual, 7.1), solo URL encontradas, sin Wikipedia.
  - No forzar elementos (tampoco chilenos).
- **Entregas:**
  - Zip `LHD-vNN.zip` de la carpeta `lhd` completa, más capturas clave.
  - Subir la versión en `index.html` (`app.js?v=NN`, `style.css?v=NN`).
  - Actualizar `PROJECT.md` y `CAMBIOS-PENDIENTES.md`.

## 4. Cómo correrlo y probarlo

```
cd lhd
python3 tools/build_data.py        # valida src-data/ y genera data/all.json (PROBLEM = error, WARN = aviso)
python3 -m http.server 8000        # ver el sitio: http://localhost:8000
php -S 127.0.0.1:8000              # en vez del anterior, para el modo ?editar
sh tools/tests/run_all.sh          # todas las pruebas de navegador (Playwright + Chromium)
python3 tools/make_help_images.py  # regenera las imágenes de la ayuda (help/overview-es|en.webp)
python3 tools/check_contrast.py    # contraste de colores
python3 tools/pipeline/auditoria.py   # auditoría R1 (-v ids, --md F informe, --strict falla con ERROR sin anotar)
python3 tools/pipeline/auditoria.py --v1   # definición de terminado de la R2 (pendientes; código 1 mientras quede alguno)
```

- **Pruebas** (`tools/tests/`):
  - `test_general` (búsqueda, fichas, filtros, foco, macromovimientos);
  - `test_eje` (navegación del tiempo);
  - `test_v19` (flechas dobles, sombreado, Todo/Ajustar, colores);
  - `test_v20` (niveles, macromovimientos, conexiones indirectas, fichas);
  - `test_v21` (fuentes numeradas: superíndices y lista en el sitio público y en `?editar`);
  - `test_v31` (zona «Más allá de Occidente» para elementos orientales);
  - `test_preview` (vista previa de las listas, etapa 1b, con carga en el navegador);
  - `test_etapa1` (verificador de listas y ensayo del recorte real, sin navegador);
  - `test_r1` (auditoría sin ERROR, sin etiquetas largas, limpieza idempotente; sin navegador);
  - `test_r2_tools`, `test_r2_incidencias`, `test_r2_auditoria` (herramientas de la R2: lotes, validación, aplicación, incidencias, hoja .xlsx y `auditoria.py --v1`; sin navegador, sobre copias) y `test_ensayos_fuentes` (superíndices y «Fuentes del ensayo»);
  - `test_etapa0`, `test_recorte`, `test_empaquetar` (sin navegador: validación, aplicación, recorte y empaquetado, siempre sobre copias);
  - `test_v30` (fuentes públicas: superíndices, «Fuentes» cerrada, advertencia, clic en superíndice, sin marcas en búsqueda ni tooltips);
  - `test_v22` (conceptos en el macromovimiento y correcciones de la revisión independiente);
  - `test_v24` (dos niveles, contexto colapsado, macromovimientos en «Movimientos»);
  - `test_editar` (modo edición; necesita PHP y deja `ediciones/` limpio al terminar).
  - Se espera que todas digan PASS.
  - Las capturas van a `/tmp/lhd-shots`, o a `$LHD_SHOTS/lhd-shots`.
  - Chromium se busca en `/opt/pw-browsers/chromium`, o en `$CHROMIUM`.
- **Cuidado:**
  - No usar `pkill -f "php -S"` (cerró la terminal en sesiones anteriores); terminar el servidor desde el propio script.
  - Antes de entregar, `ediciones/` debe quedar con `imagenes.json` = `{}`, sin `revision.json` y sin `copias/*.json`.

## 5. Mapa técnico rápido

- **Archivos del sitio:**
  - `index.html`, `app.js` (~2.300 líneas, sin librerías), `style.css` (colores como variables al comienzo, tema claro y oscuro).
  - `data/all.json` lo genera el build: no se edita.
- **Datos:**
  - Se escriben a mano en `src-data/<carpeta>/*.json`. Las carpetas `industrial`, `reform`, `modernism`, `postwar` y `postmodern` solo ordenan por año de inicio.
  - Campos por tipo: `MANUAL-CONTENIDO.md` y `SPEC.md` sección 5.
  - Novedades de v20: `level` (desde v24 solo `essential` o `normal`), y los macromovimientos (`macro`, `parts`, `context_summary`, `shifts`).
  - v24: la página abre con todo el contexto colapsado; los macromovimientos se dibujan primero dentro de la fila «Movimientos» (ya no tienen fila propia).
- **Build** (`tools/build_data.py`): valida
  - niveles (`star` ya no va en las fuentes);
  - diseñadores sin obras o con un nivel mayor que el de sus obras;
  - macromovimientos;
  - fechas dentro de la carpeta;
  - textos en español;
  - enlaces.
- **Partes de `app.js`:**
  - Escala: `buildScale`, `U`, `xOf`, `lp`; niveles de detalle por zoom `LOD_MID` y `LOD_NEAR`.
  - Filas: `build()`, que arma contexto, macromovimientos y diseño según «Organizar».
  - Relaciones: `relations(id)`, que incluye las indirectas con `via`.
  - Curvas: `drawCurves`, `curveCol`.
  - Filtro «Solo»: `makeIso`, `setIso`.
  - Foco: `makeFocus`, `applyFocus`, `setFocus`.
  - Visibilidad: `levelOk`, `workShown`, `designerVisible`, `movementVisible`, `macroVisible`.
  - Rango visible: `setRangeU`, `visibleSpan` (Ajustar), `wireRange`.
  - Fichas: `workCard`, `designerCard`, `movementCard` / `macroCard`, `contextCard`, `lensCard`, `infoCard`, `learnHtml`.
  - Modo edición: `makeEditor`.
  - Textos de la interfaz en `UI.es` y `UI.en`, al comienzo.
- **Modo `?editar`:**
  - Sirve para revisar fichas y reemplazar imágenes.
  - `editar.php` guarda en `ediciones/`. La contraseña está en la constante `CLAVE` de `editar.php`.
  - La contraseña es **`uai2026`** (desde v60, punto 83; antes `lhd2026`). Se pide al editar, no al abrir `?editar`. Es insegura pero el sitio es personal. No ponerla en `app.js`.

## 6. Próximo paso

**Las etapas P (v30), 0 (v31), 1 (v32–v33), 1b (v34), 2 (v35), 3 (v36), 4 (v38) y 5 (v42) ya están hechas.** La **etapa 6 está hecha en v44** (585 obras). **Etapa 7 (punto 78, plan sección 9c): la revisión editorial externa (7.1) está hecha en v45** — `tools/REVISION-EDITORIAL-ETAPA7.md`, `tools/REVISION-ETAPA7.json` (elementos nuevos, prioridad A/B/C) y `tools/REVISION-ETAPA7-AJUSTES.json` (niveles, fusiones, pertenencias, correcciones). **V4 dado y paso 7.3 hecho en v46** (punto 79). **Etapa 7 cerrada en v52** (puntos 80 a 86) con `tools/GUIA-EJECUCION-ETAPA7.md`, luego la **etapa 8** (`tools/ESPEC-ETAPA8.md`; el **V2** va al final de ella) y solo después la Parte II. La prioridad C de la revisión queda para la **Parte III** (sección 17 del plan). Nada se inicia sin el «implementa» de Mauricio. Método de la etapa 6 (referencia): (≥ 500 obras, todos los diseñadores y obras razonables para un curso universitario; conexiones directas o secundarias, regla C4c; rótulo «Completo» y conteo de contexto del punto 65 en 6.7). **No se inicia sin el «implementa» de Mauricio.** Método probado en las etapas 2 a 5: lotes con agentes Sonnet en paralelo (≤12 elementos, ≤10 obras, ≤15 enlaces; prompt corto que apunta a un archivo con los ids), `validate_out.py`, `apply_new.py`, `--links-from-lists`, un lote de relleno y `sin_enlace` en vez de inventar. Herramientas: `validate_out.py`, `apply_new.py`, `listas_check.py`, `recortar.py`, `preview_listas.py`, `EJEMPLOS.md`, `empaquetar.sh` (el tipo de registro de los agentes es `rtype`; los textos en inglés van en el nivel superior y el español en `es`).

**Modelos (todo con Sonnet, punto 60):** pasos `[A]` Sonnet esfuerzo medio (Opus medio solo si hay fallas graves y con aviso previo); pasos `[B]` Sonnet esfuerzo medio (agentes `general-purpose`, `model: "sonnet"`); pasos `[C]` Sonnet esfuerzo bajo. Si un paso falla dos veces, sube de nivel (plan, sección 2).

**Rutina de cada sesión:** plan, sección 5 (build y pruebas al empezar y al terminar, `?v=NN`, punto en `CAMBIOS-PENDIENTES.md`, entrada en `PROJECT.md`, casilla marcada, **ZIP único de continuidad según la sección 5B del plan** y resumen de 6 líneas).

## 7. Mensaje sugerido para abrir la sesión nueva

> Adjunto el zip completo de la Línea de Historia del Diseño (LHD v61). Descomprímelo, lee `INICIO-SESION-NUEVA.md`, `ESTADO-ACTUAL.md` y `tools/GUIA-EJECUCION-ETAPA7.md`, y ejecuta el siguiente paso sin marcar de `tools/PLAN-CIERRE.md` (etapa 8, paso 8.7 (V2); no se avanza sin mi «implementa»). Usa el mismo protocolo: registra mis comentarios en `tools/CAMBIOS-PENDIENTES.md` (el próximo punto es el 99) y no implementes cosas nuevas hasta que diga «implementa». Todo el plan se hace con Sonnet; si algo sale con fallas graves, avísame antes de usar Opus.

Para continuar R2 en una sesión nueva: leer CONTINUAR-R2.md (ciclo de tanda, reglas, plantilla de agente).

**Desde v74 (punto 102): el plan vigente es `tools/PLAN-V1.md` (cierre de la versión pública LHD v1.0).** Leer después de `ESTADO-ACTUAL.md` y antes de `CONTINUAR-R2.md`. **R2.0 (herramientas) está hecha en v76; la sesión nueva sigue en R2.1, solo cuando Mauricio lo diga** (mensaje para pegar al final de `ESTADO-ACTUAL.md`).
