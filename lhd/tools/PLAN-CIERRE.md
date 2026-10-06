# Plan de cierre de la LHD (versión 10, 5 de octubre de 2026; etapas P y 0 a 6 ejecutadas; etapa 7 en curso; etapa 8 y Parte III agregadas en v46)

> **Este es el único plan vigente.** Para reglas de contenido sigue mandando `tools/MANUAL-CONTENIDO.md`, **salvo** lo que cambia aquí: **primero se escribe el contenido y las conexiones, sin trabajo de fuentes**; las fuentes y la revisión van en la **Parte II**, separada.
> **Estado de partida: v31** (etapa P ejecutada; datos iguales a v27). Modernismo terminado y con fuentes (138 obras, 72 diseñadores, 42 hechos de contexto, 255 enlaces; tras el recorte de la sección 3.0 quedan 120, 64, 39 y ~245). Los otros tramos casi no tienen contenido (solo `ctx-taylorism`, `ctx-industrial-revolution`, `ctx-personal-computer`, Susan Kare, íconos del Macintosh y los macromovimientos vacíos).
> **Decisiones de la persona responsable (puntos 56 a 58):** lo más importante es **contenido y conexiones**; revisión y fuentes son secundarias y separadas; **línea equilibrada según la importancia histórica de cada época**, para lo cual se **recorta el Modernismo solo en lo no esencial** y se ajustan las épocas. **Punto 61 (4 de octubre de 2026):** se aprueba la propuesta de proporciones: **375 obras** (Industrial 30, Reforma 60, Modernismo 120, Posguerra 90, Posmoderno 75), recorte del Modernismo reducido a 18 obras Normal, 8 diseñadores y 3 hechos de contexto, y se permiten elementos orientales con influencia en Occidente. **V0 (este plan) está aprobado**; V1 ya dado (v33).
> **Punto 78 (5 de octubre de 2026, plan v9):** se agrega la **etapa 7** (sección 9c): **revisión editorial externa** de todo el listado contra el canon de un curso universitario y complemento de lo que falte. Su paso 7.1 (la revisión) está hecho en v45. **Punto 79 (plan v10):** V4 dado (A y B aprobados; C a la Parte III), preparación 7.3 hecha en v46 con la guía `tools/GUIA-EJECUCION-ETAPA7.md`; nueva **etapa 8** (sección 9d: ensayos de foco y de disciplina, alcance por disciplina, barra unificada y advertencia de revisión en la cabecera de las fichas), al final de la cual va el **V2**; nueva **Parte III** (sección 17: desarrollo futuro). La Parte II empieza después de la etapa 8.
> **Puntos 71 y 72 (4 de octubre de 2026, plan v8):** se agrega la **etapa 6** (sección 9b), entre la etapa 5 y la Parte II: levantamiento transversal y complemento de obras y diseñadores, para que estén **todos los diseñadores y obras que sería razonable encontrar en un curso universitario de historia del diseño** (gráfico, producto, moda y arquitectura), con **mínimo 500 obras** en total (la meta de 375 pasa a ser el piso de la etapa 5, no el techo), buena cobertura de la arquitectura de las últimas cuatro décadas e instituciones y premios relevantes (p. ej. Premio Pritzker). Se relaja un poco la exigencia de enlaces directos solo en casos excepcionales (regla C4c). **El V2 se mueve al final de la etapa 6**; nuevo **V3** (aprobación de la lista de la etapa 6) antes de redactar. En la etapa 6 el nivel visible «Normal» pasa a llamarse **«Completo»** (solo la etiqueta; el valor interno sigue siendo `normal`).

## 0. Resumen

0. **Etapa previa P (nueva, punto 59): fuentes visibles en el sitio público**, sección «Fuentes» al final de cada ficha, «Observaciones» en vez de «Revisión» y resumen de revisión renovado (sección 5A). **Ejecutada en v30 (punto 62).**
1. **Parte I (contenido y conexiones), etapas 0 a 8:** ~17 sesiones hasta la etapa 5 (más ~12 a 16 de la etapa 6, sección 9b). Se recorta el Modernismo (etapa 1) y se escriben ~400 elementos de contexto y diseño, **255 obras nuevas** y ~440 enlaces de contexto, **sin buscar fuentes**. Al cierre de la etapa 5 la línea tiene **375 obras** repartidas según la importancia de cada época (sección 3); la **etapa 6** la completa hasta **≥ 500 obras** con lo que un curso universitario de historia del diseño esperaría encontrar (sección 9b), la **etapa 7** la somete a una revisión editorial externa y agrega lo que falte (sección 9c), y la **etapa 8** agrega los ensayos de foco y de disciplina, el alcance por disciplina y la advertencia de revisión (sección 9d). Los agentes escriben desde su conocimiento, con reglas para no inventar (sección 1).
2. **Parte II (fuentes y revisión), etapas R1 a R5:** separada, por lotes, en el orden de riesgo. Se puede hacer después, a ratos, o no hacer todo. **Solo R1 (automática) y el empaquetado de R5 son obligatorias antes de publicar.** La Parte II **no empieza hasta cerrar la etapa 6** (punto 71), **la etapa 7** (punto 78) **y la etapa 8 con su V2** (punto 79): con ≥ 500 obras crece (R2 a R4 pasan de 12 a ~16 a 18 sesiones; ver sección 4; con la etapa 7, unas 65 a 170 fichas más según el alcance aprobado en el V4). La contraseña de `?editar` **no se cambia antes de publicar** (queda `lhd2026`, fijada en la etapa P; punto 60).
3. Todo lo que se escribe en la Parte I queda con `refs: []` (el build lo cuenta como «sin fuentes todavía»: es un aviso, no un error). Esa cuenta es la lista de trabajo de la Parte II.
4. **Tus vistos buenos:** V0 (este plan; **ya dado**), V1 (listas maestras y lista de recorte del Modernismo; **ya dado**), V3 (propuesta de la etapa 6; **ya dado**), V4 (revisión editorial externa de la etapa 7; **ya dado**, punto 79) y **V2** (el sitio completo, **al final de la etapa 8**, paso 8.7). La Parte II no pide vistos buenos.
5. Cada paso tiene casilla `[ ]`, qué leer, qué hacer, qué entregar y cómo comprobarlo, para que lo ejecute Sonnet con esfuerzo bajo o medio. **Todo el plan se hace con Sonnet** (punto 60, para ahorrar recursos); Opus queda solo como respaldo si V1 muestra fallas graves.
6. Si se agota el uso o el contexto (error 429): parar, aplicar lo validado y seguir en la sesión siguiente.
7. **Parte III (desarrollo futuro, sección 17):** lo que queda para después de la Parte II: los elementos de prioridad C de la revisión editorial y los deseables.

## 1. Reglas (aprobadas con V0; el modelo no pregunta por ellas)

- **C1. Qué se escribe sin fuentes y cómo no inventar.** Cada elemento se escribe solo con lo que el modelo conoce con **alta certeza**: nombres, años, atribuciones y relaciones famosas. Sin citas textuales, sin cifras dudosas (usar «c.», rangos o «unos»), sin títulos ni cargos inventados, sin detalles de procedencia o precio. Ante la duda, **omitir la frase**, no adivinar. Los textos son tan largos como los del Modernismo (`key` una frase; `more` 2 a 4 frases).
- **C2. Nada de `[n]` ni `refs` en la Parte I.** `refs: []` y sin marcas. Tampoco se busca en la web (más rápido y barato). `where` («Saber más») se deja vacío; se llena en la Parte II.
- **C3. Manda `LISTAS-CIERRE.md`.** Dentro de ella un elemento dudoso se cambia por uno de la reserva (15 %); se anota en `tools/PENDIENTES-FUENTES.md`.
- **C4. Conexiones: lo más importante.** Prueba de las tres preguntas (manual 9.1) en una línea, con el **mecanismo** («la crisis del petróleo de 1973 encarece los plásticos → el diseño vuelve a la madera y al reciclado»). Una coincidencia de fechas **no** es un enlace. Metas por tramo: todo hecho de contexto con ≥ 2 enlaces; toda obra con ≥ 1 enlace de contexto **(directo de preferencia; punto 65: por ahora basta con uno indirecto, ver C4b)** y las ★ con ≥ 2 de subcategorías distintas (directos); todo diseñador, institución, movimiento, teoría y productivo con ≥ 1 enlace propio; ≥ 8 «conexiones» entre elementos (influencias, continuidades) por tramo.
- **C4b. «Con contexto» (punto 65, 4 oct 2026).** La meta «toda obra con ≥ 1 enlace de contexto» **puede cumplirse con enlaces indirectos**, aunque se prefiere el directo (`80-context-links.json`). Cuenta como indirecto, para una obra: un productivo en `tech` (el sitio lo muestra como relación de contexto), un enlace de contexto de alguno de sus diseñadores, o uno de los movimientos o instituciones de sus diseñadores; para un diseñador: un enlace de contexto de alguna de sus obras. Las obras ★ siguen necesitando ≥ 2 enlaces directos de subcategorías distintas. En el Modernismo de hoy (v31): 102 obras con enlace directo, 32 solo indirecto y 5 sin ninguno (`bauhaus-exhibition-poster`, `gill-sans`, `times-new-roman`, `faaborg-chair`, `coca-cola-bottle`); 13 diseñadores sin enlace directo, 6 de ellos también sin indirecto (`eric-gill`, `stanley-morison`, `perriand`, `kaare-klint`, `chareau`, `jean-prouve`). Para las obras nuevas, las listas de la etapa 1 deben traer al menos un contexto por obra siempre que se pueda.
- **C4d. Las ★ y la conectividad (punto 79, decisión D3 del V4).** El nivel ★ se decide por importancia historiográfica. A toda obra ★ se le buscan dos enlaces directos de subcategorías distintas **sin forzarlos** (se pueden agregar hechos de contexto); si no hay un enlace cierto, se anota como excepción C4c con su motivo. **Nunca se baja una ★ por falta de enlaces.** Vale para toda la línea desde la etapa 7.
- **C4c. Etapa 6: exigencia de conexión relajada (punto 71).** Para los elementos que agrega la etapa 6 vale: (a) todo elemento queda con **al menos una conexión**, directa o secundaria (C4b amplía «secundaria» a cualquier enlace de contexto o conexión de un elemento ligado: obra → diseñador, movimiento, institución o productivo; diseñador → obras; etc.); **nadie queda totalmente desconectado**; (b) puede tener **solo conexiones secundarias**; (c) las obras ★ nuevas deberían tener 2 enlaces directos de subcategorías distintas, pero se admiten **excepciones** (1 directo más secundarios, o solo secundarios) **en casos excepcionales y siempre anotadas una por una en la propuesta V3 con su motivo**; (d) si hace falta, la etapa 6 **agrega hechos de contexto nuevos** para enriquecer el mapa; (e) lo icónico que no logre ninguna conexión sin inventar va a la reserva y se avisa en el V3. La prueba de las tres preguntas y la regla «una coincidencia de fechas no es un enlace» siguen vigentes.
- **C5. Decisiones editoriales ya tomadas:** Chile pesa poco (≤ 6 elementos en 1970–1973: INTEC/CORFO, Cybersyn, gráfica de la Unidad Popular, carátulas de Larrea y un solo hecho político «Unidad Popular y golpe de Estado, 1970–1973»); en Posguerra, un tercio escandinavo, un tercio italiano, un tercio estadounidense dentro de lo europeo/norteamericano; **América Latina ≥ 15 % de las obras** en Posguerra y Posmoderno y ≥ 2 elementos en Reforma e Industrial; **Asia, África, Medio Oriente y Oceanía:** sin elementos propios, **salvo los que tengan influencia demostrable en el diseño occidental** (punto 61: japonismo, metabolismo, Muji, Kawakubo, Yamamoto y similares); cada uno lleva una línea de mecanismo que explica esa influencia en su enlace o su ficha, se marca `regions: ["global"]` con su país en `countries`, y no son más de unos 6 a 10 en toda la línea (orientativo, no es tope); África, Medio Oriente y Oceanía quedan igual sin elementos propios salvo que cumplan lo mismo; niveles: ★ ≈ 30 % de las obras, el resto Normal (desde la etapa 6, la etiqueta visible de este nivel es «Completo»; punto 72; el valor interno sigue siendo `normal`).
- **C6. Pruebas.** Si una prueba falla por un conteo de datos, se ajusta la prueba. Si falla por error de página, se corrige el código y se anota en `PROJECT.md`.
- **C7. Lo único que se te pregunta en medio:** nada, salvo contradicción grave con el manual o algo irreversible fuera de este plan.
- **C8. Honestidad del sitio (cambia con la etapa P, punto 59).** Las fuentes y los superíndices son **públicos**: cada ficha tiene al final la sección «Fuentes», y la que no tiene fuentes muestra una advertencia «contenido no revisado» (también con la sección cerrada). Mientras la Parte II no se haga, **todo lo nuevo de la Parte I se verá con esa advertencia en el sitio público**. Antes de publicar, R2 y R3 son el mínimo de verificación recomendado, pero la decisión es tuya (sección 15).

## 2. Modelos y esfuerzo

| Tipo | Modelo y esfuerzo | Para qué | Pasos |
|---|---|---|---|
| **A** | **Sonnet, esfuerzo medio** (antes Opus alto; punto 60) | Decidir qué entra y cómo se conecta. La red de seguridad es V1 (tú), la verificación automática 1.5 y la reserva del 15 %; Opus solo si V1 encuentra fallas graves en un tramo (se rehace ese tramo) | 1.1–1.6 |
| **B** | **Sonnet, esfuerzo medio** | Redactar elementos y enlaces con agentes en paralelo; en la Parte II, buscar fuentes y revisar | pasos `[B]` |
| **C** | **Sonnet, esfuerzo bajo** | Ejecutar scripts, build, pruebas, aplicar JSON, documentos, zips | pasos `[C]` |

La sesión que orquesta puede ser Sonnet de esfuerzo bajo; los agentes se lanzan con `general-purpose` y `model: "sonnet"`. **Subir de nivel:** un paso `[C]` que falla dos veces por algo que no es un tipeo pasa a `[B]`; un `[B]` que falla dos veces pasa a `[A]` solo para esa decisión; un `[A]` que falla dos veces, o cuyo V1 sale con fallas graves, pasa a Opus de esfuerzo medio solo para esa decisión.

## 3. Tamaños (Parte I)

Todo con nivel `essential` (★) o `normal` (la etiqueta visible «Normal» pasa a «Completo» en la etapa 6, paso 6.7; punto 72). **Esta sección describe el alcance de las etapas 0 a 5 (375 obras); la etapa 6 lo amplía a ≥ 500 (sección 9b) y sus cifras definitivas salen del V3.** **Criterio de equilibrio:** el Modernismo es el núcleo (~32 % de las obras), seguido de la Posguerra (~24 %) y el Posmoderno (~20 %); Reforma ~16 % e Industrial ~8 % (tramos largos, con menos producción documentada; los hechos de contexto llevan el peso en Industrial). Ajustado en el punto 61 (ver 3.2).

| Tramo (carpeta) | Años | Contexto (5 subcat.) | Productivo | Teoría | Movimientos | Institu-ciones | Diseña-dores | **Obras (★)** | Enlaces de contexto |
|---|---|---|---|---|---|---|---|---|---|
| Industrial 1750–1850 (`industrial`) | ~100 | 25 (5 c/u) | 10 | 5 | 5 | 6 | 14 | **30 (9)** | ~60 |
| Reforma 1851–1913 (`reform`) | ~63 | 30 (6 c/u) | 12 | 6 | 6 | 10 | 28 | **60 (18)** | ~110 |
| **Modernismo 1914–1944 (`modernism`), tras el recorte** | 31 | **39** (de 42) | 16 | 14 | 11 | 17 | **64** (de 72) | **120 (37)** (de 138) | ~245 (de 255) |
| Posguerra 1945–1974 (`postwar`) | 30 | 36 | 16 | 11 | 10 | 14 | 43 | **90 (27)** | ~150 |
| Posmoderno 1975–hoy (`postmodern`) | ~51 | 32 | 15 | 9 | 8 | 12 | 36 | **75 (22)** | ~120 |
| **Total nuevo (sin Modernismo)** | | 123 | 53 | 31 | 29 | 42 | 121 | **255 (76)** | ~440 |
| **Total de la línea** | | 162 | 69 | 45 | 40 | 59 | 185 | **375 (113)** | ~685 |

**Obras por año:** Industrial 0,3 · Reforma 1,0 · Modernismo 3,9 · Posguerra 3,0 · Posmoderno 1,5. El ★ queda en ~30 % de las obras.
Las 255 obras nuevas incluyen los **íconos del Macintosh** (ya existen), así que se redactan 254. Más **reserva del 15 %** por tipo (solo ids y nombres).
**Ya existe y se conserva** (entra en las listas): `ctx-taylorism` (reform), `ctx-personal-computer`, `susan-kare`, `macintosh-icons-1984` (postmodern), `ctx-industrial-revolution` (industrial), `macro-modernism` (reform) y `macro-postmodernism` (postwar).
**Lo que valida el build como PROBLEM:** hecho de contexto con `effect` y ≥ 1 enlace; productivo y teoría con ≥ 1 enlace; obra con `designers`, `maker` o `client`; `es` completo; ids únicos. (Diseñador con ≥ 1 obra: el build lo avisa.)

### 3.0 Recorte del Modernismo (decidido en el punto 58)
El Modernismo baja de 138 a 120 obras (punto 61). **Se recortan solo cosas no esenciales; no se toca nada ★.** Cantidades: **18 obras Normal** (gráfica 5, producto 5, arquitectura 5, moda 3; quedan 34 / 34 / 33 / 19), **8 diseñadores** y **3 hechos de contexto**. Reglas de selección (las aplica la etapa 1, paso 1.6):
- **Nunca** se recorta: una obra ★; una obra citada en una conexión (`85-connections.json`), en un concepto o en el texto de un macromovimiento; una obra de América Latina; la única obra de un movimiento o institución; un diseñador ★ o con una obra que se queda; un hecho de contexto citado en `context_summary` o `shifts` del macromovimiento.
- **Se recortan primero:** obras con menos enlaces de contexto y repetidas del mismo diseñador, tipo o movimiento (por ejemplo, varias sillas o carteles de una misma escuela); después, los diseñadores que se quedan sin obra y los hechos de contexto con menos enlaces una vez recortadas las obras (hoy los más bajos son `ctx-automatic-telephone`, `ctx-planned-obsolescence`, `ctx-aviation`, `ctx-consumer-credit`, `ctx-jazz-age`, `ctx-paris-1937` y `ctx-semana-arte-moderna`; el criterio manda sobre esta lista).
- **Por qué alcanza el margen:** hoy hay 79 obras Normal sin ninguna de las protecciones (21 de gráfica, 21 de producto, 21 de arquitectura y 16 de moda), muchas más que las 18 que se recortan; 42 diseñadores tienen solo obras Normal.
- Lo recortado **se guarda** en `tools/RESERVA-FASE-B.json` (clave `recorte_modernismo`) por si se quiere recuperar; no queda en el sitio. Se quitan también los enlaces, conexiones y marcas que dependían de lo recortado.

### 3.2 Proporciones por época (**aprobadas en el punto 61**)
Se revisó el reparto frente a lo que suele enseñar un curso universitario de historia del diseño (Revolución Industrial y reforma del siglo XIX como origen de la disciplina; Modernismo y Bauhaus como núcleo; posguerra con estilo suizo, diseño italiano y escandinavo e identidades corporativas; y una última parte posmoderna y digital, más temática que canónica).

| Tramo | Curso típico | Antes | **Aprobado** |
|---|---|---|---|
| Industrial 1750–1850 | 7–10 % | 30 (8 %) | **30** (8 %) |
| Reforma 1851–1913 | 18–22 % | 55 (14 %) | **60** (16 %) |
| Modernismo 1914–1944 | 28–32 % | 100 (26 %) | **120** (32 %), recortando solo 18 |
| Posguerra 1945–1974 | 20–25 % | 100 (26 %) | **90** (24 %) |
| Posmoderno 1975–hoy | 15–20 % | 95 (25 %) | **75** (20 %) |
| **Total** | | 380 | **375** (nuevas: 255 en vez de 280) |

Razones: (1) la Reforma quedaba corta (exposiciones universales, Arts and Crafts, Art Nouveau, Secesión, Werkbund y Behrens son siempre una unidad grande); (2) el Posmoderno pesaba demasiado y es el más riesgoso (lo posterior a 2010 no tiene canon asentado y choca con la regla C1); (3) recortar 38 obras del Modernismo habría descartado trabajo ya verificado.
- **Elementos orientales (decisión del punto 61):** se permiten cuando tengan influencia demostrable en el diseño occidental (ver C5). Verificación técnica en la etapa 0 (paso 0.10): cómo se ven en el filtro y en «Organizar por región», que hoy solo conoce Europa, Norteamérica, América Latina y `global`.
- **Efecto:** −25 obras nuevas y −20 recortes frente al plan v6: unas 3 a 4 sesiones menos en total.

### 3.1 Ajuste del build para la Parte I `[C]` (primer paso de la etapa 0)
Hoy el build da **PROBLEM** si una teoría no tiene fuente https. Como la Parte I no lleva fuentes, en la etapa 0 ese chequeo pasa a **WARN** (en `tools/build_data.py`, regla 4 del SPEC 6); se anota en `tools/SPEC.md` y `PROJECT.md`. En la Parte II (R1) vuelve a **PROBLEM**.

## 4. Mapa de etapas

| Etapa | Qué | Sesiones | Tipo |
|---|---|---|---|
| **Etapa previa: diseño del sitio** | | | |
| **P** | **Fuentes visibles en el sitio, «Observaciones» y resumen de revisión (sección 5A)** | 1–2 | B (código) y C |
| **Parte I: contenido y conexiones** | | | |
| 0 | Preparación (scripts, briefs, ajuste del build) | 1 | C |
| 1 | Listas maestras y matriz de conexiones de los 4 tramos + lista de recorte del Modernismo (**V1**), y aplicación del recorte | 2 | **A** (decide) y C (aplica) |
| 2 | Posguerra (90 obras) | 4 | B y C |
| 3 | Reforma | 3 | B y C |
| 4 | Posmoderno (75 obras) | 4 | B y C |
| 5 | Industrial (30 obras) + integración de la Parte I (sin V2; el V2 pasó al final de la etapa 6) | 3 | B y C |
| 6 | Levantamiento transversal y complemento (≥ 500 obras): propuesta (V3), redacción de todo lo nuevo, rótulo «Completo» e integración (**hecha en v44**; su V2 pasa a 7.8) | ~12 a 16 | A, B y C |
| 7 | Revisión editorial externa (7.1, v45), V4 (dado) y complemento: ajustes estructurales, redacción de lo aprobado, niveles e integración (guía: `GUIA-EJECUCION-ETAPA7.md`) | ~5 a 7 | A (revisión), B y C |
| **8** | **Ensayos de foco y de disciplina, alcance por disciplina, barra unificada, advertencia de revisión en la cabecera; V2** | **~4 a 6** | B y C |
| **Parte II: fuentes y revisión (separada)** | | | |
| R1 | Auditoría automática y limpieza | 1 | C |
| R2 | Fuentes: ★ nuevas, fechas de vida, movimientos e instituciones | 4 → ~5 (se recalcula con el V3) | B |
| R3 | Fuentes: contexto, productivo, teoría, enlaces | 5 → ~6 | B |
| R4 | Fuentes del resto, pendientes del Modernismo y revisión independiente | 3 → ~5 | B |
| R5 | Seguridad y paquete para publicar | 1 | C |

Orden de los tramos: Posguerra (continúa el Modernismo y completa el macromovimiento) → Reforma → Posmoderno → Industrial (el más chico, al final). **Etapa previa P: 1 a 2 sesiones; Parte I: ~17 hasta la etapa 5, ~12 a 16 de la etapa 6, ~5 a 7 de la etapa 7 y ~4 a 6 de la etapa 8; Parte II: ~18 a 20 tras la etapa 7 (más las referencias de los 10 ensayos). Parte III: sin estimación (desarrollo futuro).** Con «sesión» se entiende una sesión de trabajo de Claude hasta agotar contexto o uso, con su ZIP de continuidad (sección 5B).

## 5. Antes y después de cada sesión (lista fija)

**Al empezar:** (1) leer `INICIO-SESION-NUEVA.md` y la sección de este plan que toca; (2) `python3 tools/build_data.py 2>&1 | tail -5`: en la Parte I no debe haber PROBLEM, salvo los esperados de cada paso; (3) mirar `tools/PENDIENTES-FUENTES.md`.
**Al terminar:** (1) build sin PROBLEM (o los esperados); (2) `sh tools/tests/run_all.sh 2>&1 | grep -E "FAIL|Error|Timeout"` sin salida; (3) `ediciones/imagenes.json` = `{}` y `ediciones/copias/` vacía; (4) subir `?v=NN` en `index.html`; (5) un punto nuevo en `tools/CAMBIOS-PENDIENTES.md` y una entrada en `PROJECT.md`; (6) marcar la casilla del paso aquí; (7) **ZIP único de continuidad (sección 5B):** `sh tools/empaquetar.sh NN` genera, prueba y entrega `LHD-vNN.zip`, con un resumen de 6 líneas (no hay que aprobarlo para seguir); (8) **nunca** `pkill -f "php -S"`.

## 5B. ZIP único de continuidad (punto 60)

Al terminar **cada paso o sesión del plan** se guarda **un solo ZIP con todo el proyecto**, listo para (a) probarlo en la web antes de publicar y (b) continuar en otra sesión de Claude sin perder nada. Solo vale el último: cada entrega nuevo lo reemplaza (`LHD-vNN.zip`, con NN la versión de `index.html`); los anteriores quedan obsoletos.

**Qué lleva (todo el contenido de `lhd/`):** el sitio completo (`index.html`, `app.js`, `style.css`, `data/all.json`, `help/`, `editar.php`, `ediciones/` limpia con su `.htaccess`), `src-data/`, `tools/` (plan, manual, scripts, pruebas, briefs), `PROJECT.md`, `INICIO-SESION-NUEVA.md` y los dos archivos nuevos de abajo. No lleva `__pycache__`, `*.pyc`, capturas ni copias de `ediciones/copias/`.

**Archivos que garantizan que la sesión nueva parta sin problemas:**
- **`ESTADO-ACTUAL.md` (en la raíz de `lhd/`, se actualiza en cada entrega):** versión; qué etapa y paso se terminó y cuál es **el siguiente sin marcar**; decisiones pendientes tuyas; cifras actuales (obras, diseñadores, contexto, enlaces; con y sin fuentes); resultado del build y de las pruebas; y el **mensaje exacto para pegar** en la sesión nueva («Lee `INICIO-SESION-NUEVA.md` y `ESTADO-ACTUAL.md` y ejecuta el siguiente paso sin marcar de `tools/PLAN-CIERRE.md`»).
- **`LEEME-PROBAR-EN-WEB.md`:** cómo subir el sitio a un hosting (con PHP para `?editar`; sin PHP el sitio público funciona igual), permisos de `ediciones/` (escritura), la contraseña de `?editar` (`lhd2026` desde la etapa P) y cómo probar en local (`python3 -m http.server`).
- `INICIO-SESION-NUEVA.md` sigue siendo la guía estable (qué es el proyecto, cómo trabajar, mapa técnico); `ESTADO-ACTUAL.md` es la hoja que cambia.

**`tools/empaquetar.sh NN` (se escribe en la etapa 0, paso 0.9; hasta entonces se hace a mano con la misma lista):**
1. Verifica que `ediciones/imagenes.json` sea `{}` y que no haya `revision.json` ni `copias/*.json` (en la etapa P, que `editar.php` tenga la clave acordada).
2. Corre el build (sin PROBLEM) y comprueba que `ESTADO-ACTUAL.md` mencione la versión NN y que `index.html` use `?v=NN`.
3. Arma `LHD-vNN.zip` desde la carpeta que contiene `lhd`: `zip -qr LHD-vNN.zip lhd -x "*/__pycache__/*" "*.pyc" "lhd/ediciones/copias/*.json"`.
4. **Prueba el ZIP:** lo descomprime en una carpeta limpia, corre el build allí, levanta `python3 -m http.server` y comprueba que `index.html`, `app.js`, `style.css` y `data/all.json` respondan (HTTP 200) y que `all.json` sea JSON válido.
5. Lo entrega con `SendUserFile` y, si hay carpeta conectada, lo guarda también ahí.

---

# PARTE I. CONTENIDO Y CONEXIONES

## 5A. Etapa previa P: fuentes visibles en el sitio público `[B]` y `[C]` (1 a 2 sesiones; punto 59)

**Estado: EJECUTADA en v30 (4 de octubre de 2026, punto 62), tras la orden «implementa».** *Nota de implementación: en vez de dejar `rfMode` siempre encendido, `renderPanel` lo enciende solo mientras arma la ficha y lo apaga al terminar; el efecto público es el mismo y el buscador, los tooltips y las etiquetas nunca ven marcas.* Es un ajuste de diseño y de código (`app.js`, `style.css`, `editar.php`, ayuda, pruebas y documentos); no toca los datos. Se hace **antes de la etapa 0** para que todo lo que se escriba después ya se vea con su sección «Fuentes».

### 5A.1 Qué se quiere (decisiones de la persona responsable)
1. **Transparencia:** las fuentes de información dejan de ser exclusivas del modo `?editar` y se ven en el sitio real, con la misma información que hoy muestra `?editar`: las afirmaciones llevan **superíndice** y las fuentes van **numeradas**.
2. **Sección «Fuentes» al final de cada ficha** (última sección; en inglés «Sources»), **colapsable y colapsada por defecto**.
3. **Ficha sin fuentes = no revisada:** en el título de la sección «Fuentes» aparece un **ícono de advertencia** (visible aun con la sección colapsada) y, dentro, un mensaje de que **el contenido no ha sido revisado**.
4. **En `?editar` también se ven** (es contenido del sitio real). Se **conserva** la función de cambiar la imagen con otro enlace (lápiz sobre la foto).
5. **La sección «Revisión» pasa a llamarse «Observaciones»** y queda **solo el campo de texto** de comentarios; se elimina la casilla «Revisada».
6. **El resumen de revisión** (menú de la barra superior en `?editar`) se ajusta para mostrar: (a) el **avance de la revisión por IA**; (b) las **fichas con comentarios humanos pendientes** (si a una ficha se le borra el texto de observación, sale de la lista); (c) el **listado de fichas con la imagen cambiada manualmente**.

### 5A.2 Definiciones (confirmadas por la persona responsable, punto 60)
- **«Revisada por IA» = la ficha tiene al menos una fuente en `refs`** (propia o de un enlace de contexto que la toca). **«No revisada» = no tiene ninguna.** Es el único criterio; no hay casilla manual. (Hoy faltan fuentes en solo 3 elementos del Modernismo y en 1 enlace; los demás ya las tienen, así que el sitio actual casi no mostrará advertencias.)
- **Qué fichas llevan la sección:** las de movimiento, institución, diseñador, obra, hecho de contexto, productivo, teoría y concepto. **No** la llevan la ficha de época/macromovimiento global, la del foco (lente), la de ayuda ni la vacía.
- **«Observación pendiente» = la ficha tiene texto en Observaciones.** Si el texto queda vacío, la ficha sale de la lista y del contador. «Resolver» sigue guardando el texto en «Observaciones resueltas» (historial) y vaciando el campo.
- **«Imagen cambiada manualmente» = la ficha tiene una entrada en `ediciones/imagenes.json`.**

### 5A.3 Diseño de la ficha (sitio público)
- **Sin nota sobre IA:** la sección no lleva ninguna línea sobre cómo se redacta o verifica el contenido; solo la lista de fuentes o la advertencia (decisión del punto 60).
- **Orden de secciones:** como hoy, y **«Fuentes» siempre la última**. En `?editar`, «Observaciones» va justo antes de «Fuentes» (así «Fuentes» sigue siendo la última). El lápiz de la imagen no cambia.
- **Control:** `<details class="sect sources">` nativo (teclado y lector de pantalla gratis), **cerrado al abrir cada ficha**; el estado no se recuerda entre fichas. El título es «Fuentes (n)» con la cuenta de fuentes.
- **Con fuentes:** lista numerada igual a la de hoy: etiqueta con enlace (`target="_blank" rel="noopener noreferrer"`), dominio, qué sostiene (`checks`, con los ⚠ visibles) y fecha de consulta. Las fuentes de los enlaces de contexto siguen a las propias y llevan «Enlace: A → B»; las de conexiones, «Conexión».
- **Sin fuentes:** ícono de advertencia (triángulo en SVG, con `aria-label` y `title`) en el título; al abrir, el mensaje: *«Esta ficha aún no ha sido revisada: no tiene fuentes registradas, así que su contenido podría contener errores.»* / *“This card has not been reviewed yet: it has no recorded sources, so its content may contain errors.”* Color de advertencia con contraste suficiente en tema claro y oscuro (`check_contrast.py`).
- **Superíndices:** cada marca `[n]` del texto se ve como `<sup>` con enlace a su fuente. **Clic en un superíndice → abre «Fuentes», desplaza hasta esa fuente y la resalta** (hoy solo desplaza). Una ficha sin fuentes no tiene superíndices.
- **«Saber más» (`where`) se mantiene** como lecturas recomendadas; «Fuentes» es la verificación. Los dos nombres deben distinguirse en la ayuda.

### 5A.4 Cambios técnicos
- **`app.js`:**
  - `rfMode` queda siempre encendido: ya no depende de `ED.on && ED.key`; los superíndices salen para todos.
  - **Auditar todo lugar donde un texto sale fuera de la ficha** y debe seguir sin marcas: búsqueda, tooltips, notas de las curvas, ficha de foco y de época, listas del resumen, etiquetas `aria-label`, título de la pestaña, exportación. Allí se usa `rfPlain` (o se quita el token); la búsqueda no debe indexar las marcas.
  - `rfList` pasa a envolver todo en `<details>`; mensaje de advertencia en vez del texto actual de la tarea A6; se agrega «abrir al hacer clic en superíndice».
  - `renderPanel`: la sección «Fuentes» se agrega para todos (no solo `ED.on`); `ED.reviewHtml` deja de incluir `⟦FUENTES⟧` y se coloca antes de ella.
  - `E.reviewHtml`: título «Observaciones», sin casilla ni insignia «Revisada/Observada»; queda `textarea`, Guardar, Resolver, fecha del último cambio e historial.
  - `E.state`: queda solo «con observación» / «sin observación»; se eliminan `STL.ok` y los chips «Revisada».
  - `E.summaryCard` y `exportNotes`: ver 5A.5.
  - Textos EN/ES: ayuda («En el modo edición tiene además el resumen de revisión», `rv_btn`, partes de la ayuda sobre fuentes y revisión) y «Acerca de».
- **`style.css`:** estilos de la sección colapsable, del ícono de advertencia y del resaltado de la fuente; los de `.rv-sources` y `.rf-list` se reutilizan.
- **`editar.php`:** la acción `revision` guarda solo `obs` (y `historial`, `fecha`); ya no guarda ni lee `revisada`. Los registros viejos con `revisada: true` y sin texto se ignoran (no cuentan) y se limpian al próximo guardado. `ediciones/revision.json` sigue **privado** (`.htaccess`): las observaciones humanas no son públicas. `ediciones/imagenes.json` sigue público.
- **Datos y build:** sin cambios en `src-data/`. El aviso del build «N elementos sin refs» sigue siendo la lista de trabajo de la Parte II y ahora coincide con las fichas que muestran la advertencia.

### 5A.5 Resumen de revisión (menú de la barra superior, solo `?editar`)
Pasa a tener tres bloques:
1. **Revisión por IA.** Cuenta global «con fuentes / sin fuentes» con barra de avance, y el mismo cuadro por tipo (obras, diseñadores, contexto, etc.) y por época. Chips para filtrar la lista: «Sin fuentes» (por defecto) y «Con fuentes». La lista muestra nombre, tipo, época y la cantidad de fuentes.
2. **Observaciones pendientes.** Lista de las fichas con comentario humano, con el texto y la fecha; clic abre la ficha. Contador en la cabecera. Al borrar el texto, la ficha sale de la lista y del contador. Filtro por época.
3. **Imágenes cambiadas manualmente.** Lista de las fichas con imagen reemplazada: nombre, miniatura, dominio de la URL y la URL completa; clic abre la ficha (donde está el lápiz para cambiarla o quitarla).
- **Exportar `.md`:** incluye observaciones abiertas y resueltas y, nuevo, la lista de imágenes cambiadas y la cuenta de fichas sin fuentes.
- Se quitan las insignias «Revisada/Observada/Sin revisar» y el filtro por estado antiguo.

### 5A.6 Pasos
- [x] **P.1 `[B]` Fuentes públicas:** `rfMode` siempre encendido, auditoría de textos fuera de la ficha, sección «Fuentes» colapsable con advertencia y clic en superíndice, estilos, textos EN/ES. Probar a mano con una ficha con fuentes, una sin fuentes y una con fuentes de enlaces.
- [x] **P.2 `[B]` Observaciones y resumen:** renombrar y simplificar la sección, `editar.php`, resumen de tres bloques, exportación. Mantener el lápiz de imagen.
- [x] **P.3 `[C]` Pruebas y documentos:**
  - Pasar `test_v21` (hoy comprueba que el sitio público no muestra marcas) a comprobar lo contrario.
  - Ajustar `test_editar` (sin casilla, lista de observaciones, lista de imágenes, borrar el texto saca la ficha).
  - Escribir `test_v30`: público con superíndices; «Fuentes» cerrada al abrir; advertencia en una ficha sin fuentes (con la sección cerrada); clic en superíndice abre y desplaza; búsqueda y tooltips sin marcas; ficha de época y foco sin sección.
  - Revisar contraste (`check_contrast.py`) y regenerar las imágenes de ayuda (`make_help_images.py`) si cambian la barra o la ficha.
  - Actualizar `MANUAL-CONTENIDO.md` 7.1 (puntos 2 y 5: las fuentes dejan de ser internas), `SPEC.md` (actualización v30), `PROJECT.md`, `INICIO-SESION-NUEVA.md` y las secciones 1 (C8) y 15 de este plan; subir `?v=30`.
- [x] **P.2b `[C]` Contraseña:** poner `CLAVE = 'lhd2026'` en `editar.php`; en `test_editar.py` y `test_v21.py` leerla de `LHD_CLAVE` (por omisión `lhd2026`); actualizar `PROJECT.md` (puntos sobre la contraseña) y `INICIO-SESION-NUEVA.md`. **Queda así para siempre:** es insegura, pero el sitio es personal y no se difundirá masivamente (decisión del punto 60); **no se pide ni se cambia más.**
- [x] **P.4 `[C]` Cierre:** rutina de la sección 5; capturas (ficha con fuentes cerrada y abierta, ficha sin fuentes, resumen, ancho de teléfono 390 px); `ediciones/` limpia; zip `LHD-v30.zip`.
- **Listo cuando:** en el sitio público una ficha con fuentes muestra superíndices y «Fuentes (n)» cerrada; una sin fuentes muestra el triángulo de advertencia en el título cerrado y el mensaje al abrir; `?editar` muestra lo mismo más «Observaciones» y el resumen nuevo; todas las pruebas dicen PASS.

### 5A.7 Efectos sobre el resto del plan
- **La Parte I deja el contenido nuevo a la vista sin fuentes:** las ~255 obras y ~400 elementos nuevos se verán con la advertencia hasta que se haga la Parte II. Es la transparencia buscada, pero sube el peso de R2 y R3 antes de publicar (ver sección 15, palanca 4).
- **Tramos con contenido de prueba** (taylorismo, Kare, íconos del Macintosh, etc.) también mostrarán la advertencia si no tienen fuentes.
- **Ya no hay «Revisada» manual:** el avance de revisión sale de las fuentes registradas, y la Parte II lo hace subir solo.

## 6. Etapa 0: preparación `[C]` (1 sesión) — **EJECUTADA en v31 (punto 64)**

*Notas de implementación: el tipo de registro de los agentes se llama `rtype` (no `type`, que en las obras es el tipo de obra); `refs: []` también cuenta como «sin fuentes» en el aviso del build; `recortar.py` ensaya el recorte en una copia (build y huérfanos) antes de tocar nada; hay pruebas nuevas `test_etapa0`, `test_recorte`, `test_empaquetar` (sin navegador) y `test_v31` (zona «Más allá de Occidente»).*

- [x] **0.1 Ajustar el build** como en 3.1 (teoría sin fuente: WARN). Correr el build y las pruebas: sin PROBLEM nuevo.
- [x] **0.2 Revisar `tools/pipeline/`.** Ya contiene `lib.py` (`get`, `rep`, `setf`, `link`, `addlink`, `droplink`, `save`; rutas relativas a la carpeta del proyecto), `apply2.py` (aplica `refs`, textos y correcciones a elementos, enlaces y conexiones ya existentes) y `apply3.py` (agrega enlaces nuevos con `refs`); los usa sobre todo la Parte II. Comprobar que corren (`python3 -c "import sys;sys.path.insert(0,'tools/pipeline');import lib;print(lib.get('gropius')['id'])"`). `save()` agrega a `RESERVA-FASE-B.json` los enlaces que se descarten: no ensuciar esa reserva con pruebas.
- [x] **0.3 Escribir `tools/pipeline/validate_out.py`.** Entrada: un JSON de agente (lista de registros). **Falla con mensaje claro** si: (a) un id ya existe en `src-data/`; (b) un id referenciado (`designers`, `movements`, `institutions`, `tech`, `ctx`, `item`, `from`, `to`, `parts`) no existe en `src-data/` ni en `tools/LISTAS-CIERRE.md`; (c) falta un campo de texto en `es` o `es` trae campos distintos; (d) un texto tiene marcas `[n]` (no corresponden a la Parte I; la opción `--refs` las exige en la Parte II y comprueba que cada marca tenga fuente, que cada fuente se cite, que EN y ES tengan las mismas marcas y que las URL sean https y no de Wikipedia); (e) `key` supera ~200 caracteres, `short` supera 22, una nota de enlace supera 220; (f) `level` no es `essential` o `normal`; (g) año fuera del tramo. Imprime `OK` o la lista de errores. Probar con un archivo bueno y uno con un error puesto a propósito.
- [x] **0.4 Escribir `tools/pipeline/apply_new.py`.** Entrada: carpeta del tramo y uno o más JSON de elementos nuevos (cada uno con `rtype` = `context|production|theory|movement|institution|designer|work|link|connection`). Los agrega al archivo que corresponde en `src-data/<tramo>/`, con los nombres del Modernismo: contexto `40-context-political.json`, `41-context-economic.json`, `42-context-social.json`, `43-context-cultural.json`, `44-context-technological.json` (por `track`); productivo `50-production-materials.json`, `51-production-processes.json`, `52-production-tools.json` (por `sub`); `56-theory.json`; `02-movements.json`; `03-institutions.json`; `10-designers.json`; obras `20-works-graphic.json`, `21-works-product.json`, `22-works-fashion.json`, `23-works-architecture.json` (por `discipline`); enlaces `80-context-links.json`; conexiones `85-connections.json`. Rechaza ids repetidos; `json.dump(..., ensure_ascii=False, indent=1)`. Opción `--links-from-lists`: lee las columnas «relaciona» de `tools/LISTAS-CIERRE.md` y rellena `links` de productivo, teoría, instituciones y movimientos y `movements`/`institutions` de los diseñadores, solo con ids que existan. Los registros con `"descartado": true` se omiten y se anotan en `tools/PENDIENTES-FUENTES.md`. Probar en **una copia** de `src-data/`.
- [x] **0.5 `tools/pipeline/EJEMPLOS.md`:** un registro real por tipo copiado del Modernismo (`ctx-fordism`, `tubular-steel`, `th-vers-une-architecture`, `de-stijl`, `inst-bauhaus`, `gropius`, obra ★ `barcelona-chair`, obra Normal `kitchener-poster`, un enlace y una conexión), **mostrándolos sin `refs` ni marcas `[n]`** (así se escribirá la Parte I).
- [x] **0.6 Briefs.** Ya están guardados en `tools/pipeline/briefs/` (`BRIEF-CONTENIDO.md` = Anexo A; `BRIEF-FUENTES.md` = Anexo B, para la Parte II). Revisarlos contra los scripts nuevos (`validate_out.py`, `apply_new.py`) y corregir ambos lugares si algo cambia. `tools/PENDIENTES-FUENTES.md` ya existe (pendientes de fuentes del Modernismo y encabezado «id · motivo» para lo que se descarte); se va completando.
- [x] **0.7 Scripts del recorte (3.0).** (a) `tools/pipeline/candidatos_recorte.py`: lee `src-data/modernism/`, aplica las protecciones de 3.0 y escribe en pantalla, por disciplina, las obras Normal recortables ordenadas de más a menos «prescindible» (menos enlaces de contexto primero; repetidas del mismo diseñador o tipo primero), con sus enlaces y diseñadores, y los hechos de contexto con su número de enlaces. (b) `tools/pipeline/recortar.py <lista.json>`: la lista trae `works`, `designers` y `contexts` por quitar; el script **se niega** si alguno está protegido (3.0), los quita de `src-data/modernism/`, quita sus enlaces de `80-context-links.json`, sus conexiones, sus ids en `works` de diseñadores, `parts` y conceptos, los guarda en `RESERVA-FASE-B.json` bajo `recorte_modernismo` y corre el build; debe quedar sin PROBLEM nuevo. Probar con `--prueba` (trabaja sobre una copia de `src-data/` en un directorio temporal).
- [x] **0.9 `tools/empaquetar.sh`** como en 5B, más plantillas de `ESTADO-ACTUAL.md` y `LEEME-PROBAR-EN-WEB.md` (el primer ZIP de este tipo se arma hoy, `LHD-v29q.zip`, con los archivos escritos a mano). Probar el script con una copia.
- [x] **0.10 Elementos de influencia oriental (punto 61).** Probar con un elemento de prueba (`regions: ["global"]`, `countries: ["JP"]`) cómo se ve en los filtros y en «Organizar por región» (hoy `REGION_ZONES` y `ZONE_OF` solo conocen Europa, Norteamérica y América Latina). Si cae en un grupo confuso, agregar lo mínimo (por ejemplo, la zona «Otras» o una zona «Asia, por influencia»), con prueba y nota en `PROJECT.md`; actualizar `SPEC.md` (sección 10.7 y alcance regional) y `MANUAL-CONTENIDO.md` con la regla de C5.
- [x] **0.8** `INICIO-SESION-NUEVA.md`: orden de lectura con este plan; mensaje inicial «Lee `INICIO-SESION-NUEVA.md` y ejecuta el siguiente paso sin marcar de `tools/PLAN-CIERRE.md`».
- **Listo cuando:** `validate_out.py` detecta el error de prueba, `apply_new.py` agrega un elemento a la copia y `recortar.py --prueba` quita 3 obras de prueba sin dejar ids huérfanos.

## 7. Etapa 1: listas maestras, matriz de conexiones y recorte `[A]` (2 sesiones, **V1**) — **EJECUTADA: pasos 1.1–1.6 en v32; V1 aprobado y paso 1.7 en v33**

Con **Sonnet de esfuerzo medio** (punto 60; si V1 muestra fallas graves en un tramo, ese tramo se rehace con Opus de esfuerzo medio). Para compensar el menor esfuerzo: se trabaja un tramo por vez, se escribe primero la línea de mecanismo de las ★ y los enlaces de cada contexto, y se corre 1.5 antes de mostrar nada. Primera sesión: **recorte del Modernismo (1.6)** y listas de Posguerra y Posmoderno. Segunda: Reforma e Industrial, verificación y V1; la aplicación del recorte (1.7) es un paso `[C]` después de V1. No se escribe el contenido final: se decide **qué entra y cómo se conecta**.

- [x] **1.1 Leer** `SPEC.md` secciones 5, 9, 10 y 10.7, `MANUAL-CONTENIDO.md` (secciones 3 a 5 y 9.1), `tools/PROPUESTA-NIVELES.md` y las secciones 1 y 3 de este plan.
- [x] **1.2 Crear `tools/LISTAS-CIERRE.md`**, una sección por tramo, con una tabla por tipo (una fila por elemento, con estas columnas):
  - **Contexto:** `id`, nombre ES, subcategoría, inicio–fin, regiones, **qué explica** (ids de obras o diseñadores y una línea de mecanismo por cada uno).
  - **Productivo / Teoría / Movimientos / Instituciones:** `id`, nombre ES, años, nivel, ids relacionados.
  - **Diseñadores:** `id`, nombre, años, disciplinas, nivel, ids de sus obras.
  - **Obras:** `id`, título ES, disciplina, tipo, año, nivel, ids de diseñadores, ids de productivo (`tech`), **ids de los contextos que la explican con la línea de mecanismo** (≥ 1; las ★ ≥ 2 de subcategorías distintas).
  - **Conexiones** (influencias entre elementos, ≥ 8 por tramo): `from`, `to` y una línea.
  - **Reserva (15 %)** al final de cada tipo.
  Parte de SPEC 10.x (`SPEC.md` y `MANUAL-CONTENIDO.md` sección 10) **ampliada** hasta los tamaños de la sección 3 (esas listas traen entre 40 y 70 por tramo; se completa con lo más conocido del tramo, sin forzar). Se eligen primero las ★ (lo que explica el cambio de época), luego Normal. Se cuidan disciplinas (gráfica, producto, moda, arquitectura), regiones y C5.
- [x] **1.3 Reglas de conexión (C4):** la columna «qué explica» de cada contexto y «contextos» de cada obra llevan la línea de mecanismo. Si no se puede escribir la línea, **no hay enlace**. Cada contexto con ≥ 2 enlaces; cada diseñador, institución, movimiento, teoría y productivo con ≥ 1 enlace propio (a un contexto o a otro elemento).
- [x] **1.4 Reglas por tramo** (incluir en la lista):
  - **Posguerra:** `macro-modernism` suma a `parts` los movimientos de 1945–1970 que le pertenecen (Good Design, funcionalismo de Ulm, estilo tipográfico internacional, identidad corporativa); `macro-postmodernism` suma los de los años sesenta que anuncian el posmodernismo (diseño pop, diseño radical); reintegrar `ctx-corfo` y `ctx-early-television` desde `tools/RESERVA-FASE-B.json` (van a `src-data/modernism/`; enlazan con obras de Posguerra); un hecho «Unidad Popular y golpe de Estado, 1970–1973» (C5).
  - **Reforma:** `ctx-taylorism` se conserva; el Werkbund (1907) como institución y el debate Muthesius–Van de Velde como teoría; no hay macromovimiento propio.
  - **Posmoderno:** se conservan Kare, íconos del Macintosh y computador personal; `macro-postmodernism` suma a `parts` Memphis, Alchimia, deconstructivismo y New Wave; no hay tercer macromovimiento.
  - **Industrial:** sin macromovimiento; neoclasicismo e historicismos como movimientos; `ctx-industrial-revolution` → `macro-modernism` ya existe.
- [x] **1.5 Verificación estructural de la lista** (script corto en Python que lee `LISTAS-CIERRE.md`): ids únicos y en minúsculas con guiones, sin choques con `src-data/`, ids referenciados existentes, cantidades por tipo igual a la sección 3 (±2; obras ±3), ★ entre 25 % y 35 %, contexto con ≥ 2 enlaces, obra con ≥ 1 contexto.
- [x] **1.6 Lista de recorte del Modernismo `[A]`.** Correr `python3 tools/pipeline/candidatos_recorte.py` y elegir **18 obras, 8 diseñadores y 3 hechos de contexto** según 3.0 (gráfica 5, producto 5, arquitectura 5, moda 3). Guardar `tools/RECORTE-MODERNISMO.md` (tabla con id, nombre y motivo de cada uno) y `tools/RECORTE-MODERNISMO.json` (la lista que lee `recortar.py`). Al elegir, tener en cuenta las listas de los otros tramos: no quitar un hecho de contexto o una obra que el Modernismo comparta como antecedente directo de una obra de Posguerra (enlaces entre épocas).
- [x] **1.7 Aplicar el recorte `[C]`, después de V1.** `python3 tools/pipeline/recortar.py tools/RECORTE-MODERNISMO.json`; comprobar: 120 obras, 64 diseñadores, 39 hechos de contexto, 37 ★ (hoy 38 en el archivo: una es de prueba), build sin PROBLEM; «con contexto» se mide con la regla C4b (directo o indirecto); build sin PROBLEM; `run_all.sh` limpio (ajustar los conteos de las pruebas si hace falta, C6). Actualizar `PROJECT.md`.
- **Entrega y V1:** `LISTAS-CIERRE.md`, `RECORTE-MODERNISMO.md` y un resumen de una página (cantidades por tipo y disciplina, % América Latina, las 5 decisiones más discutibles, lo que se recorta). **Aquí pides V1** en un solo mensaje.

## 7b. Etapa 1b: vista previa de toda la línea `[C]` — **EJECUTADA en v34** (pedida por Mauricio tras V1)
- [x] 1b.1 `tools/pipeline/preview_listas.py`: sitio de vista previa aparte (fichas «en desarrollo») a partir de `LISTAS-CIERRE.md`, sin tocar `src-data/` ni `data/`.
- [x] 1b.2 Prueba `test_preview` y entrega en un ZIP distinto (`LHD-vista-previa-1b.zip`) con `INFORME-VISTA-PREVIA.md`.
- La vista previa se regenera cuando cambien las listas; no es parte de la publicación. Después sigue la etapa 2.

## 8. Plantilla de tramo (etapas 2 a 5)

Para el tramo `X` (carpeta `src-data/X/`) se usa su sección de `LISTAS-CIERRE.md`. **Sesiones:** S1 = 8.1 y 8.2 (núcleo); S2 = 8.3 (obras); S3 = 8.4 a 8.6 (enlaces, integración y cierre). Industrial (chico) hace S1 y S2 juntas. Reforma: S1, S2, S3.

### 8.1 Contexto, productivo, teoría `[B]`
- [ ] Armar lotes de **hasta 12 elementos** (un agente por lote; natural: una subcategoría de contexto, o productivo + teoría). Sin web: los agentes escriben más rápido y se pueden lanzar hasta ~10 a la vez.
- [ ] Lanzar los agentes en paralelo (una sola llamada). Prompt de cada agente (copiarlo y completar):
  `Lee y sigue exactamente tools/pipeline/briefs/BRIEF-CONTENIDO.md. Tramo: <carpeta>. Tipo: <context|production|theory>. Ids de tu lote (tools/LISTAS-CIERRE.md, sección <tramo>): <ids>. Resultado: <carpeta de trabajo>/<tramo>_<lote>.json`
- [ ] Validar cada salida con `python3 tools/pipeline/validate_out.py <archivo>`. Si falla: devolver el mensaje exacto al mismo agente con `SendMessage` (una vez); si falla otra vez, arreglar a mano si es trivial o pasar el elemento a la reserva (C3).
- [ ] Aplicar con `python3 tools/pipeline/apply_new.py <tramo> <archivos>`.

### 8.2 Movimientos, instituciones, diseñadores `[B]`
Igual que 8.1 (tipo `movement|institution|designer`). Los diseñadores llevan 1 a 3 frases y años y lugares de nacimiento y muerte **solo si se conocen con certeza** (si no, solo años). Aplicar.
- **Cierre de S1:** `python3 tools/build_data.py`. **Son esperables PROBLEM por ids de obras o enlaces que aún no existen.** Cualquier otro PROBLEM se arregla ahora.

### 8.3 Obras `[B]`
- [ ] Lotes de **hasta 10 obras** por agente (agrupadas por diseñador o disciplina). Mismo prompt con `Tipo: work`. En Posguerra y Posmoderno (90 y 75 obras) S2 se parte en dos sesiones (S2a y S2b, de ~45 y ~38 obras).
- [ ] Cada obra sigue el ejemplo de `EJEMPLOS.md`: `key` (1 frase), `more` (2 a 4 frases), `materials`, `tech`, `status`, `level`, `year`, `designers`. Sin `where` y sin `wiki` salvo que el agente conozca con certeza el título exacto de la página de Wikipedia en inglés.
- [ ] Validar y aplicar como en 8.1.

### 8.4 Enlaces de contexto y conexiones `[B]`
- [ ] Lotes de **hasta 15 enlaces** por agente, con los pares `ctx` → `item` y la línea de mecanismo **ya definidos** en `LISTAS-CIERRE.md`. El agente redacta cada nota (1 a 2 frases, ≤ 200 caracteres, EN y ES, sin marcas). Si no puede expresar el mecanismo sin inventar, devuelve `"sin_enlace": true`.
- [ ] Lo mismo con las conexiones (`from`, `to`, nota).
- [ ] Si por un `sin_enlace` un contexto queda con < 1 enlace o una obra ★ sin contexto: un agente más con ese caso. Si tampoco, bajar la obra a Normal o pasar el contexto a la reserva.
- [ ] Validar y aplicar con `apply_new.py`. Después `python3 tools/pipeline/apply_new.py <tramo> --links-from-lists`.

### 8.5 Integración `[C]`
- [ ] `python3 tools/build_data.py 2>&1 | grep PROBLEM` vacío. Arreglar WARN mecánicos: `es` incompleto, `short` > 22 caracteres, año fuera del tramo (mover el elemento a la carpeta correcta). WARN permitidos: sin `refs` (esperado), textos largos.
- [ ] Macromovimientos: completar `parts` y enlaces propios según 1.4 (Posguerra, Reforma, Posmoderno).
- [ ] Proporciones: contar en `data/all.json` por tipo y nivel; ★ entre 25 % y 35 % de las obras; si no, reclasificar los más dudosos.
- [ ] Contar **enlaces por contexto, obra, diseñador, etc.** contra las metas de C4 (y C4b para «toda obra con ≥ 1 enlace»: directo o indirecto) con una línea de Python; los que quedan bajo la meta se anotan en `PENDIENTES-FUENTES.md` y se cubren con un lote extra de 8.4.

### 8.6 Pruebas y cierre `[C]`
- [ ] `sh tools/tests/run_all.sh` sin FAIL (C6). Sin capturas ni revisión por tramo.
- [ ] Sección «Tramo X» en `PROJECT.md` con cantidades finales y los ids a reserva. Rutina de la sección 5. Marcar casillas. Entregar zip.

---

## 9. Etapas 2 a 5: parámetros por tramo

### Etapa 2: Posguerra (`postwar`, 1945–1974) · 4 sesiones (S2 en dos) · 90 obras (24 ★ finales; 27 en la lista)
- [x] 2.1 S1 · [x] 2.2 S2a · [x] 2.3 S2b · [x] 2.4 S3. **EJECUTADA en v35 (punto 67).**
- **Contexto:** Guerra Fría; Plan Marshall; Unidad Popular y golpe (C5); «milagros» alemán e italiano; sociedad de consumo y crédito; industrialización por sustitución de importaciones (CEPAL); baby boom y suburbios; reconstrucción de la vivienda y los grandes conjuntos; Revolución Cubana; descolonización; plásticos y petroquímica; aeropuertos y turismo de masas; contracultura; feminismo de segunda ola; televisión y arte pop; Juegos Olímpicos (México 68, Múnich 72); Expo 67; transistor; circuito integrado; carrera espacial; crisis del petróleo.
- **Movimientos:** Good Design; diseño escandinavo; diseño italiano; funcionalismo de Ulm; estilo suizo; identidad corporativa; diseño pop; diseño radical; brutalismo/metabolismo; moda de la era espacial.
- **Obras (90):** SPEC 10.5 más lo más conocido de cada disciplina (sillas Eames, Tulip, Ant, Wishbone; Braun SK 4; Lettera 22; Vespa; Fiat 500; Helvetica y Univers; identidades de IBM y Lufthansa; pictogramas de Múnich 72; New Look de Dior; Le Smoking; minifalda; Unikko; Cybersyn; Larrea; Brigada Ramona Parra; ESDI; Brasilia…).

### Etapa 3: Reforma (`reform`, 1851–1913) · 3 sesiones · 60 obras (18 ★)
- [x] 3.1 S1 · [x] 3.2 S2 · [x] 3.3 S3. **EJECUTADA en v36 (punto 68).**
- **Contexto:** exposiciones universales; segunda revolución industrial; marcas y publicidad; grandes almacenes; vivienda obrera; mujeres en oficinas; japonismo; prensa ilustrada; Kodak; electricidad; teléfono; automóvil y bicicleta; taylorismo (ya existe); Ford 1913.
- **Teoría:** Owen Jones, Ruskin, Morris, Dresser, Sullivan, Loos y debate del Werkbund. **Obras:** SPEC 10.3 más silla n.º 14 de Thonet, carteles de Chéret, Lautrec y Mucha, vidrios de Tiffany y Gallé, edificios de Mackintosh y Hoffmann, AEG de Behrens, vestido Delphos, Lira Popular, *Zig-Zag*, Posada.

### Etapa 4: Posmoderno (`postmodern`, 1975–hoy) · 4 sesiones (S2 en dos) · 75 obras (22 ★)
- [x] 4.1 S1 · [x] 4.2 S2a · [x] 4.3 S2b · [x] 4.4 S3. **EJECUTADA en v37 (punto 69).**
- **Contexto (32):** neoliberalismo; plebiscito de 1988; caída del Muro y fin de la Guerra Fría; globalización y marcas globales; deslocalización de la manufactura; *fast fashion*; computador personal (ya existe); web; teléfono inteligente; autoedición; videojuegos y cultura *pop* global; diseño de interacción y experiencia de usuario; crisis climática y diseño sostenible; pandemia; redes sociales.
- **Obras (75):** SPEC 10.6 más Apple II/iMac/iPod/iPhone, Memphis, Swatch, Juicy Salif, OXO, *Ray Gun*, *Emigre*, I ♥ NY, Westwood, cartel *Hope*, arpilleras, franja del NO, Quinta Monroy, Campana, Muji, IKEA, Nike, Benetton, Absolut, MTV, Mac OS y Windows, Google, Ive, Starck, Rams en retrospectiva, Zaha Hadid, Gehry, Koolhaas, Yamamoto, Kawakubo, McQueen, Margiela, Paula Scher, Sagmeister, Fairey, Wikipedia y *Wired*. **Para lo posterior a 2010, solo hechos de los que haya certeza; ante la duda, omitir** (C1).

### Etapa 5: Industrial (`industrial`, 1750–1850) + integración de la Parte I · 3 sesiones · 30 obras (9 ★)
- [x] 5.1 S1+S2 (8.1 a 8.3) · [x] 5.2 S3 (8.4 a 8.6) · [x] 5.3 integración de la Parte I (abajo; **sin V2**: el V2 pasó al final de la etapa 6, punto 71). **EJECUTADA en v42 (punto 75).** Resultado: 30 obras (9 ★), 14 diseñadores, 23 hechos de contexto, 9 productivos, 5 teorías, 5 movimientos, 6 instituciones, 63 enlaces y 16 conexiones; reserva: telégrafo, fotografía y estampado con cilindros.
- **Contexto (5 por subcategoría):** revoluciones de EE. UU. y Francia, sistema métrico, independencias latinoamericanas, división del trabajo, sistema de fábrica, urbanización, ludismo, Ilustración, neoclasicismo, romanticismo, vapor, ferrocarril, telégrafo, fotografía. **Obras:** Wedgwood, Baskerville, Bodoni, Chippendale, Windsor, shaker, Penny Black, Jacquard, Bewick, Crystal Palace, Percier y Fontaine, Schinkel, *La Aurora de Chile*, símbolos patrios, láminas de la *Encyclopédie*…

### 5.3 Integración de la Parte I `[C]` (cierre de la etapa 5; el V2 pasó al final de la etapa 6)
- [ ] Build sin PROBLEM; `run_all.sh` limpio; **4 capturas** (línea completa en español claro; un tramo nuevo en inglés oscuro; una ficha con enlaces; ancho de teléfono 390 px); mirarlas y arreglar fallas graves (la página no carga, etiquetas ilegibles).
- [ ] **Rendimiento:** medir el tiempo de carga con Playwright (el `all.json` rondará 3 MB). Si pasa de 3 s en equipo normal, aplicar la mitigación más simple y registrarla.
- [ ] Revisar y actualizar el texto de ayuda y de «Acerca de» con las cifras finales; contar enlaces por tipo contra C4; ajustar con un lote extra de enlaces si hay faltas.
- [ ] **Entrega:** zip y resumen (cantidades, % de América Latina, lo que quedó bajo la meta de conexiones). **No se pide V2 aquí** (punto 71): con 375 obras la línea queda completa según el plan original, pero la etapa 6 la amplía; la Parte I se cierra con el V2 de la etapa 6. Si quieres mirar el sitio en este punto, puedes comentar igual (se registra como punto numerado).


## 9b. Etapa 6: levantamiento transversal y complemento (≥ 500 obras) · ~12 a 16 sesiones (puntos 71 y 72)

**Para qué.** Asegurar que estén **todos los diseñadores y obras que sería razonable encontrar en un curso universitario de historia del diseño** (gráfico + producto + moda + arquitectura, de 1750 a hoy), con la inmensa mayoría de las obras más icónicas del diseño y la arquitectura de todas las épocas, y una **buena cobertura de los movimientos arquitectónicos de las últimas cuatro décadas** (desde ~1985: p. ej. deconstructivismo, high-tech, regionalismo crítico, minimalismo, parametricismo, arquitectura sostenible y otros que proponga el levantamiento). Se suman **instituciones y documentos relevantes** (p. ej. Premio Pritzker, bienales, premios, escuelas, museos, manifiestos y cartas). Un premio entra como **institución**; un manifiesto o carta, como **teoría**; no se crea un tipo nuevo salvo que Mauricio lo pida.

**Metas.** **Mínimo 500 obras en total** (hoy 343 y 375 al cerrar la etapa 5), más si el canon lo exige; la cifra final sale del V3. **Criterio de inclusión:** «¿se esperaría ver este elemento en un curso universitario de historia del diseño?». Se cuida que ninguna época quede muy desbalanceada (tabla de crecimiento por período en el V3; el reparto del punto 61 deja de ser techo y pasa a ser referencia). Reglas de conexión: **C4c** (relajadas en casos excepcionales; nadie desconectado). Regla C1 intacta: sin fuentes y sin inventar (**Parte I**); para lo posterior a 2010, solo hechos de los que haya certeza.

**Pasos:**
- [x] **6.1 Levantamiento `[A]` (1 sesión). HECHO en v43 (punto 76).** Auditoría transversal de la línea (obras, diseñadores, movimientos, instituciones, teoría y contexto por época, disciplina, región y nivel) contra un canon de lo que un curso universitario de historia del diseño enseña (se apoya en lo ya aprobado en las listas, en la reserva `RESERVA-FASE-B.json` y en `LISTAS-CIERRE.md`). Resultado: lista de faltantes icónicos por época y disciplina, y lista de movimientos arquitectónicos desde ~1985. Entregable: `tools/LEVANTAMIENTO-ETAPA6.md`.
- [x] **6.2 Propuesta `[A]` (1 a 2 sesiones). HECHO en v43 (punto 76): 585 obras en total (+212), 157 diseñadores, 35 movimientos, 35 instituciones, 35 teorías y 23 contextos nuevos; ver `tools/PROPUESTA-ETAPA6.md`.** Documento `tools/PROPUESTA-ETAPA6.md` (y `.json` con ids): para cada elemento nuevo (obra, diseñador, movimiento, institución, teoría o hecho de contexto): id, nombre, año, disciplina, región, nivel (★ o Completo), **los enlaces de contexto y conexiones que tendría** (directos y secundarios, con la línea de mecanismo), y las **excepciones a C4c** una por una con su motivo. Con una **tabla de crecimiento por período** (antes → después, por tipo y total, y % de América Latina). Lo que no logre conexión va a la reserva. Verificación automática con `listas_check.py` (ajustado a C4c) y con el conteo directo / indirecto / sin contexto del punto 65 (el código se escribe en 6.7; en 6.2 se calcula con un script provisional sobre la propuesta).
- [x] **6.3 Visto bueno V3 (Mauricio). APROBADO el 5 de octubre de 2026 (punto 77): «Apruebo la lista completa».**
- [x] **6.4 S1 `[B]` HECHO en v44:**** contexto nuevo, productivo, teoría, movimientos e instituciones (plantilla 8.1 y 8.2).
- [x] **6.5 S2 `[B]` HECHO en v44:** (varias sesiones, por época y disciplina):** diseñadores y obras (plantilla 8.2 y 8.3; lotes de ≤ 10 obras).
- [x] **6.6 S3 `[B]` HECHO en v44 (22 `sin_enlace`; 20 obras sin ningún contexto, anotadas como excepción C4c):**** enlaces de contexto y conexiones (plantilla 8.4; `sin_enlace` permitido; lote de relleno).
- [x] **6.7 Integración y rótulo «Completo» `[C]` HECHO en v44 (rótulo cambiado; conteo del punto 65 en `build_data.py`; carga 0,45 s con 585 obras; 4 capturas):** (a) **punto 72:** la etiqueta visible del nivel «Normal» pasa a **«Completo»** (EN «Complete») en `UI.es` y `UI.en` (`lv_normal`, `lvTip_normal`; tooltip: «Todos los elementos: imprescindibles y el resto»), en la ayuda, la ficha general (i), `MANUAL-CONTENIDO.md`, `PROPUESTA-NIVELES.md`, `LISTAS-CIERRE.md`, los briefs y las pruebas; **el valor interno `level: "normal"` no cambia** (datos, build y agentes), y el rótulo del deseable D5 se actualiza; (b) build sin PROBLEM, `run_all.sh` limpio, **rendimiento** con ≥ 500 obras (carga, densidad y niveles por zoom; mitigación más simple si pasa de 3 s) y 4 capturas; (c) **punto 65 (confirmado el 4 de octubre de 2026): conteo de contexto.** `tools/build_data.py` cuenta y muestra, para obras y diseñadores, cuántos tienen **contexto directo / solo indirecto / sin contexto** (definición de C4b; hoy solo cuenta lo directo con `worksWithContext`), por tramo y total, y lista los que quedan **sin contexto**; el aviso es WARN (no PROBLEM) y las excepciones de C4c deben figurar en el V3. La futura auditoría R1 (`auditoria.py`, paso R1.1) reutiliza esa misma función. Se ajustan las pruebas de datos y se anotan en `PROJECT.md` las cifras de antes y después; (d) ayuda y «Acerca de» con las cifras finales; contar enlaces por tipo contra C4 y C4c.
- [x] **6.8 Entrega (ZIP v44). El V2 se trasladó al final de la etapa 8 (paso 8.7; punto 79, decisión D6).** ZIP y resumen: cantidades por período, % de América Latina, excepciones a C4c, lo que quedó en la reserva. Tú miras el sitio completo y dices «ok» o qué cambiar. **Con el ok, la Parte I está cerrada** y se puede empezar la Parte II.

**Modelos:** 6.1 y 6.2 son tipo A (Sonnet, esfuerzo medio); 6.4 a 6.6 tipo B; 6.3 y 6.8 son tuyos; 6.7 tipo C. Si 6.1 o 6.2 salen con fallas graves, aviso antes de usar Opus.

> **Punto 78 (5 de octubre de 2026):** antes de dar el V2 y pasar a la Parte II, Mauricio pidió una **revisión editorial externa** de todo el listado. Se registró como **etapa 7** (sección 9c). **Punto 79 (V4):** el V2 del paso 6.8 se traslada al **final de la etapa 8** (sección 9d), antes de la Parte II.

## 9c. Etapa 7: revisión editorial externa y complemento · ~5 a 7 sesiones (puntos 78 y 79)

**Para qué.** Contrastar la línea completa (v44) con el canon de un curso universitario general de historia del diseño —movimientos, instituciones, teoría, diseñadores, obras y contexto, en general y en gráfico, producto, moda y arquitectura— y revisar que los imprescindibles (★) sean los que todo estudiante debe conocer, sin faltantes ni sobrantes. La revisión es independiente de las decisiones anteriores de la bitácora y puede contradecirlas.

**Documentos de la etapa:**
- `tools/REVISION-EDITORIAL-ETAPA7.md`: la revisión (dictamen, criterios, diagnóstico por tipo, imprescindibles, correcciones, decisiones D1 a D8 y su resultado en el V4) con sus anexos A a G.
- `tools/REVISION-ETAPA7.json`: **197 registros nuevos** con el formato de `PROPUESTA-ETAPA6.json` más `prioridad` (A/B/C) y **`estado`**: **171 `aprobado-V4`** (A 56, B 115: 71 obras, 49 diseñadores, 7 movimientos, 7 instituciones, 22 teorías, 11 hechos de contexto, 4 productivos; 12 se reponen desde la reserva) y **26 `parte-III`** (la prioridad C, sección 17).
- `tools/REVISION-ETAPA7-AJUSTES.json`: cambios sobre lo existente (niveles, fusiones, pertenencias, correcciones, reserva D7, reposiciones, enlaces D3 de las ★ y decisiones del V4).
- **`tools/GUIA-EJECUCION-ETAPA7.md`: guía paso a paso para ejecutar 7.4 a 7.8 con Sonnet** (comandos, resultados esperados, prompts de los agentes, problemas previsibles y lista de cierre). **Es lo primero que se lee al retomar la etapa.**
- Herramientas: `tools/pipeline/ajustes_etapa7.py` (fases `estructura`, `relaciones` y `niveles`, con `--prueba`), `prep_etapa7.py`, `check_etapa7.py`, `etapa7_anexos.py` y `briefs/BRIEF-ETAPA7-REDACCION.md`.

**Reglas.** Valen C1 a C4c y el manual, con la **regla D3** del V4: **la ★ se decide por importancia historiográfica; a toda obra ★ se le buscan enlaces de contexto sin forzarlos (se pueden agregar hechos de contexto); lo que no se pueda enlazar con certeza se anota como excepción C4c, nunca se baja el nivel.** Lo marcado ⚠ (`duda`) no se afirma sin certeza; las líneas de mecanismo de los JSON son propuestas, no textos finales. Lo `parte-III` no se toca.

**Pasos:**
- [x] **7.1 Revisión editorial externa `[A]` HECHA en v45 (punto 78).** Sin cambios en el sitio ni en los datos.
- [x] **7.2 Visto bueno V4 (Mauricio). DADO el 5 de octubre de 2026 (punto 79):** D1 se aprueban A y B, la C pasa a la Parte III; D2 se mantiene «Moda» (se entiende «moda y textil»; lo explicará la ficha de disciplina de la etapa 8); D3 la ★ por importancia, con enlaces de contexto sin forzar; D4 ★ chilenos aprobados; D5 contextos de COVID-19 e IA generativa (con anclas); D6 V2 al final de la etapa 8; D7 los cuatro candidatos a la reserva; D8 subsección de fundamento conceptual y bibliográfico en «Acerca de».
- [x] **7.3 Preparación `[C]` HECHA en v46 (punto 79).** `prep_etapa7.py` (lotes desde `REVISION-ETAPA7.json`, solo `aprobado-V4`, más lotes de enlaces D3 y de reescrituras), `ajustes_etapa7.py` (probado en una copia: fase `estructura` con 225 cambios en 45 archivos y build sin PROBLEM), `check_etapa7.py`, `BRIEF-ETAPA7-REDACCION.md`; `validate_out.py` reconoce los ids aprobados; `build_data.py` acepta `posthumous: true` (SPEC 5.5).
- [x] **7.4 Ajustes estructurales `[C]` HECHO en v47 (punto 80).** `ajustes_etapa7.py estructura --prueba` y luego `--aplicar` (guía, sección 4): pertenencias del Anexo D, fusiones y retiros, renombres de metadatos, fechas, pistas, correcciones de datos, reserva D7 y reposición de 11 fichas del recorte del Modernismo con sus fuentes. Cifras esperadas: 587 obras, 341 diseñadores, 73 movimientos, 93 instituciones, 64 productivos. Build sin PROBLEM; pruebas (C6 si fallan por conteo).
- [x] **7.5 Redacción `[B]` HECHA en v50 (punto 85, en tres tandas por período).** `prep_etapa7.py`; agentes por lotes (contexto, productivo, teoría, movimientos e instituciones; luego diseñadores; luego obras); `validate_out.py`; `apply_new.py` por tramo; `ajustes_etapa7.py relaciones --aplicar`. 160 fichas (las 11 repuestas ya están). Guía, sección 5.
- [x] **7.6 Enlaces D3, reescrituras y relleno `[B]` HECHA en v51 (punto 85).** Lotes `_e` (enlaces para 59 obras ★; 25 propuestas de enlace, 2 con contexto nuevo, 4 enlaces suspendidos que esperan fuente y 28 excepciones previstas), lote `textos_1` (Bodoni 1818, Brutalismo, Futurismo, Punk, medievalismo romántico, Jatiya Sangsad, Werkbund, fechas de tres movimientos) con `apply2.py`, lote de relleno y excepciones C4c anotadas una por una. Guía, sección 6.
- [x] **7.7 Niveles e integración `[C]` HECHA en v52 (punto 86).** `ajustes_etapa7.py niveles` (Anexo B); `check_etapa7.py --estricto` (todo movimiento ★ con obra ★ visible; todo diseñador ★ con obra ★); **«Acerca de» con la subsección «Fundamento conceptual y bibliográfico» (D8)**, con los textos y el código de la guía, sección 7.3; build, `run_all.sh`, contraste, rendimiento y 4 capturas.
- [x] **7.8 Entrega `[C]` (sin V2) HECHA en v52 (punto 86): etapa 7 cerrada.** ZIP y resumen: cifras por período y disciplina, ★, % de América Latina, excepciones C4c, descartes y reserva. Sigue la etapa 8.

**Modelos:** 7.1 tipo A (hecha); 7.3, 7.4, 7.7 y 7.8 tipo C; 7.5 y 7.6 tipo B; 7.2 fue tuyo. **Sesiones:** ~1 para 7.4, ~3 a 4 para 7.5–7.6 y ~1 para 7.7–7.8.

## 9d. Etapa 8: ensayos de foco y de disciplina, barra de filtros y advertencia de revisión · ~4 a 6 sesiones (punto 79)

**Para qué.** Que la línea, además de mostrar elementos y conexiones, **enseñe a leerlos**: (1) cada **foco de contexto** (político, económico, social, cultural, tecnológico y productivo) tiene una ficha con un **ensayo breve** —«La historia del diseño desde lo político», etc.— de varios párrafos, con eventos, movimientos y obras como ejemplos enlazados a sus fichas; (2) los botones de **disciplina** pasan de mostrar/ocultar a ser **botones de alcance**: filtran la línea a lo relevante para esa disciplina y abren una ficha-ensayo «La historia del diseño gráfico» (etc.), panorama de 1750 a hoy; (3) los botones de foco y de disciplina tienen la **misma apariencia** y la barra queda en el orden **Foco | Disciplinas | [Conexiones] | Detalle**; (4) las fichas sin fuentes muestran el **ícono de advertencia también arriba**, bajo el título y los años (junto a «Imprescindible» cuando corresponde). **El V2 se hace al final de esta etapa**, antes de la Parte II.

**Especificación completa:** `tools/ESPEC-ETAPA8.md` (comportamiento, formato de datos de los ensayos, estilos, textos de la interfaz, pruebas y brief de redacción). Manda sobre este resumen.

**Pasos:**
- [x] **8.1 Maquetas `[C]`.** Capturas de la barra nueva (foco y disciplinas con la misma apariencia, en el orden pedido; claro y oscuro), de una ficha-ensayo de foco y de una de disciplina, y de la advertencia en la cabecera de una ficha, con CSS/JS inyectado sin tocar el sitio. Se muestran a Mauricio; si no objeta, se sigue (las observaciones se registran como puntos).
- [x] **8.2 Datos y build `[C]`.** Archivo `src-essays/essays.json` (formato en la especificación), lectura y validación en `build_data.py` (ids de los vínculos, imágenes, largo, `es` completo), salida `data/essays.json`.
- [x] **8.3 Redacción de los 10 ensayos `[B]`** (6 de foco y 4 de disciplina, en español y en inglés), con `briefs/BRIEF-ENSAYOS.md` (en la especificación). Sin web (C1); sin fuentes hasta la Parte II (`refs: []`). Revisión de coherencia contra la línea (todo vínculo existe y dice lo que su ficha dice).
- [x] **8.4 Interfaz `[B]` y `[C]`.** (a) Alcance por disciplina (estado `S.scope`, filtrado del diseño y del contexto, combinación con el foco, ficha de disciplina, regreso al estado anterior); (b) ficha de foco con el ensayo al comienzo y las listas actuales debajo; (c) vínculos del ensayo que abren fichas; (d) apariencia común de los botones (etiqueta, ícono de color, borde del color, sombra muy suave) y nuevo orden de la barra; (e) **advertencia «no revisada» en la cabecera** de toda ficha sin fuentes (y de los ensayos); (f) ayuda, «Acerca de» y textos de la interfaz en ES y EN.
- [x] ~~**8.5 PDF `[C]`.** `tools/make_essays_pdf.py`: genera `ensayos/<id>-<es|en>.pdf` con Chromium (Playwright, ya instalado para las pruebas), con imágenes libres de Wikimedia Commons de las obras citadas (con crédito y licencia), la advertencia «contenido no revisado» y un apartado de referencias que se llena en la Parte II. Enlace «Descargar PDF» al final de cada ficha-ensayo.~~ **(anulado en el punto 90: no hay PDF)**
- [x] **8.5b Imágenes (v55: galería; v59: segunda pasada hecha, 1.102 de 1.237 con imagen y 135 excepciones en `audit/INFORME-IMAGENES.md`) — de todas las fichas y galería de estilos `[B]` y `[C]` (punto 81; ESPEC sección 11).** Antes del V2: (1) auditoría de cobertura real de imágenes (obras, diseñadores, movimientos, instituciones y teorías) (hoy `wiki` en solo 75 de 587 obras y 75 de 341 diseñadores); (2) búsqueda por lotes de una imagen libre para **cada obra y cada diseñador** (primero ★), en Commons y en las fuentes de la sección 11.4 (Smithsonian/Cooper Hewitt, The Met, Art Institute of Chicago, Library of Congress, Europeana, Internet Archive, Flickr Commons/Openverse, Memoria Chilena, etc.), con sucedáneos (11.5) y excepciones anotadas una por una; (3) campo `images` con autor, licencia, origen y alt, y aviso del build «N sin imagen» (meta 0); (4) componente de **galería con puntitos** para toda ficha, y **3 a 5 imágenes en movimientos y macromovimientos** (por defecto, las obras ★ del propio estilo);  Decisiones D-IMG1 a D-IMG3 **resueltas en el punto 82** (se acepta una imagen con derechos reservados de un sitio legítimo, con un enlace «Créditos»; los diseñadores sin retrato muestran una obra suya; instituciones con imagen y teorías con su portada). Es el único paso de la Parte I que usa la web (las imágenes no son contenido redactado).
- [x] **8.5c (v60, hecho) Modo edición y resumen de revisión `[B]` y `[C]` (punto 83; ESPEC sección 12).** (1) La contraseña se pide **al editar algo**, no al abrir `?editar`; (2) contraseña **`uai2026`** (reemplaza `lhd2026`; punto 60); (3) el resumen suma **cifras de imágenes** (con/sin, libre, derechos reservados, sucedánea; por tipo y época) y un **listado de fichas por imagen** como el de fuentes; (4) listados de **fuentes, imágenes y observaciones** colapsables y **cerrados al abrir**; (5) épocas por **años** en **todo el sitio** («1750–1850 · 1851–1913 · 1914–1944 · 1945–1974 · 1975–hoy»), no por etiqueta; Modernismo y Posmodernismo quedan como macromovimientos (punto 84). Va después de 8.5b porque usa su campo `images`.
- [x] **8.6 (v61, hecho) Pruebas e integración `[C]`** (incluye el punto 93: diseñadores con obras dentro del foco, opción B; el punto 94: «Por disciplina» sin grupo «Interdisciplinario»; y el punto 95: pie de foto mínimo, imagen como enlace y referencia en «Fuentes»). Prueba nueva de navegador (alcance, ensayos, vínculos, orden de la barra, advertencia en la cabecera); `run_all.sh`; contraste; rendimiento; imágenes de la ayuda; 6 capturas.
- [x] **8.7 (v62, hecho) Entrega y V2 (Mauricio): «OK» dado el 5 de octubre de 2026 (punto 99). PARTE I CERRADA.** ZIP y resumen. Mauricio mira el sitio completo (contenido de las etapas 6 y 7, ensayos, barra y advertencias) y dice «ok» o qué cambiar. **Con el ok, la Parte I queda cerrada** y empieza la Parte II.

**Modelos:** 8.1, 8.2, 8.5 y 8.6 tipo C; 8.5b tipo B (búsqueda de imágenes y código de la galería) con apoyo C; 8.5c tipo B (código del modo edición) con apoyo C; 8.3 tipo B (si los ensayos salen débiles, se avisa antes de usar Opus para reescribirlos); 8.4 tipo B (código) con apoyo C; 8.7 es tuyo.

---

# PARTE II. FUENTES Y REVISIÓN (separada; se hace después de la etapa 8 y su V2)

Se trabaja por **lotes de hasta 6 a 8 elementos por agente**, con web, usando `BRIEF-FUENTES.md`. En todos los lotes valen: las correcciones por falta de fuente se aplican sin consultar (se quita, se suaviza o se atribuye); no se usa Wikipedia; solo URL encontradas o ya en el proyecto; el resultado se valida con `tools/pipeline/validate_out.py --refs` y se aplica con `apply2.py` (elementos) o `apply3.py` (enlaces). **Cada lote es independiente y puede hacerse en cualquier momento.** El avance se mide con el aviso del build «N elementos sin refs».

## 10. R1: auditoría automática y limpieza `[C]` (1 sesión; obligatoria antes de publicar)
- [x] **R1.1 (v63, hecho)** Escribir `tools/pipeline/auditoria.py`: elementos por tramo y tipo; obras por disciplina, región y nivel; % con `refs`; obras y diseñadores con contexto directo / solo indirecto / sin contexto (punto 65, función ya hecha en el paso 6.7); diseñadores sin obra; contextos sin enlace; ids de `parts` inexistentes; textos con `[n]` sin cerrar; metas de C4 (enlaces por tipo).
- [x] **R1.2 (v63, hecho: interruptor `STRICT_THEORY_SOURCES` en `build_data.py`, hoy `False`; ponerlo en `True` cuando R3 termine las teorías)** Volver la falta de fuente https en una teoría a **PROBLEM** solo cuando R3 termine las teorías (hasta entonces, WARN).
- [x] **R1.3 (v63, hecho: `tools/pipeline/r1_limpieza.py`)** Corregir lo mecánico: etiquetas largas, fichas largas, textos duplicados, ids huérfanos.

> **Desde v74 (punto 102), las secciones 11 a 14 quedan reemplazadas por `tools/PLAN-V1.md`** (cierre de la versión pública LHD v1.0). Se conservan abajo solo como referencia.

## 11. R2: fuentes de lo más importante `[B]` (4 sesiones)
Orden (las cifras de 375 obras se recalculan con el V3 de la etapa 6): (1) las **76 obras ★ nuevas** (más las ★ de la etapa 6); (2) **fechas de vida** de los 121 diseñadores nuevos (como el lote 3 del Modernismo: nacimiento y muerte con lugar y año); (3) los 29 movimientos y 42 instituciones nuevos. Por cada elemento: 1 a 2 fuentes (2 a 3 las ★), marcas `[n]` en cifras, fechas y atribuciones, corrección de lo que no se sostenga.

## 12. R3: fuentes de contexto y enlaces `[B]` (5 sesiones)
Orden: (0) **referencias de los 10 ensayos de la etapa 8** (campo `refs` de `src-essays/essays.json`; aparecen en la ficha); (1) hechos de contexto (123) y productivo (53) **y los 8 conceptos del Modernismo (punto 63: antes hay que sumar los conceptos a `rfPrepare` y `srcCount` en `app.js`, y acortar sus `key` al agregar marcas)**; (2) teoría (31, con texto primario); (3) los enlaces de las obras ★ y de los contextos; (4) el resto de los enlaces. **Un enlace cuyo mecanismo no se pueda respaldar se quita o se reescribe a lo que sí consta** (tercera pregunta de la prueba).

## 13. R4: el resto y revisión independiente `[B]` (3 sesiones)
- [ ] Fuentes de las obras Normal/Completo (179 nuevas más las de la etapa 6) y de las conexiones.
- [ ] **Pendientes del Modernismo** (todos opcionales): `inst-cranbrook`; frases sin marca de Leica, rayón y cromado; `ctx-industrial-revolution` y su enlace con `macro-modernism`; `macro-postmodernism` (fechas y Memphis); ficha de museo del afiche *Books*; 5 efectos de contexto largos; segundo enlace de 13 obras ★; teorías sin enlace.
- [ ] **Revisión independiente global:** 3 agentes que no hayan redactado contrastan **40 afirmaciones** (obras ★, cifras, fechas de vida) y responden CONFIRMADA / REFUTADA / NO CONCLUYENTE con la cita. Resultado en `tools/REVISION-INDEPENDIENTE-FINAL.md`; solo lo REFUTADO se corrige.

## 14. R5: paquete para publicar `[C]` (1 sesión; obligatoria antes de publicar)
- [x] **Contraseña:** desde 8.5c (v60) es `uai2026` (punto 83); no se te pide nada sobre ella.
- [ ] Armar `LHD-publicar.zip` con solo lo necesario (`index.html`, `app.js`, `style.css`, `data/all.json`, `data/essays.json`, `editar.php`, `ediciones/` con su `.htaccess`, imágenes de ayuda), sin `src-data/`, `tools/`, `PROJECT.md` ni notas. Probar abriéndolo en una carpeta limpia con las pruebas generales. Es distinto del ZIP de continuidad de la sección 5B, que sí lleva todo el proyecto.
- [ ] Entregar el zip y una **lista corta de dudas ⚠** (máximo 25, ordenadas por riesgo).


---

## 15. Cómo ahorrar sin bajar las obras

Palancas, de menor a mayor daño, que se activan editando solo `LISTAS-CIERRE.md` o saltando un paso: (1) instituciones, productivo y teoría al 75 %; (2) menos enlaces propios de diseñadores; (3) saltar R4 y publicar tras R2 y R3; (4) saltar R2 a R4 por completo (el sitio sale con contenido sin fuentes; desde la etapa P cada ficha lo declara con la advertencia «no revisado» en el sitio público).

## 16. Deseables (Parte III, sección 17)

| # | Qué | Tipo |
|---|---|---|
| D1 | Segunda obra para los 34 diseñadores del Modernismo con una sola | B |
| D2 | Conceptos nuevos por tramo (hoy 8, solo del Modernismo) | B |
| D3 | Recuperar los enlaces suspendidos de `RESERVA-FASE-B.json` con fuentes | B |
| D4 | Sustituir fuentes débiles (divulgación, blogs) por primarias | B |
| D5 | Nivel de alto detalle (tercer nivel; ya no puede llamarse «Completo», que desde el punto 72 es la etiqueta de `normal`; nombre a definir) | A+B |
| D6 | Revisión del inglés por una persona nativa | externa |
| D7 | Pruebas de accesibilidad (teclado, contraste, lector de pantalla) | B |
| D8 | Capturas y revisión visual por tramo | B |

---

# PARTE III. DESARROLLO FUTURO (después de la Parte II; punto 79)

## 17. Parte III: lo que queda para una etapa futura

No se inicia sin el «implementa» de Mauricio. Mismas reglas que la Parte I (contenido y conexiones) y, si se hace después de la Parte II, cada ficha nueva entra con fuentes (método de `BRIEF-FUENTES.md`).

- [ ] **III.1 Elementos de prioridad C de la revisión editorial (26).** En `tools/REVISION-ETAPA7.json` con `estado: "parte-III"`: 15 obras (Casa de las Palmeras de Kew, Biblia de la Doves Press, radio EKCO AD65, Sanatorio Zonnestraal, bolígrafo Bic Cristal, lazo rojo, logo de Nike, *The Dark Side of the Moon*, XO de One Laptop per Child, 30 St Mary Axe, Mjøstårnet, vestido Four-Leaf Clover de Charles James, vestido de Ultrasuede de Halston, Tom Ford en Gucci, *Afterwords* de Chalayan), 4 diseñadores (Wells Coates, Brinkman & Van der Vlugt, William Van Alen, Chermayeff & Geismar), 2 instituciones (Total Design, Central School of Arts and Crafts), 4 teorías (Durand, Eastlake, Baudrillard, Meggs) y 1 productivo (madera masiva). Además: una obra para el movimiento de diseño crítico y especulativo (Dunne & Raby, *Technological Dreams Series: No. 1, Robots*, 2007), que hoy no tiene obras. Para prepararlos: cambiar su `estado` a `aprobado-V4` (o crear un `estado` nuevo y ajustar `prep_etapa7.py`) y seguir el método de la etapa 7.
- [ ] **III.2 Deseables** de la sección 16 (D1 a D8).

## Anexo A. `tools/pipeline/briefs/BRIEF-CONTENIDO.md` (Parte I)

```
# Tarea: redactar elementos NUEVOS de la LHD (sin fuentes; Parte I del plan)

Proyecto: Línea de Historia del Diseño. Lee primero tools/MANUAL-CONTENIDO.md (secciones 3, 7 y 9.1), tools/SPEC.md sección 5 (el tipo que te toca)
y tools/pipeline/EJEMPLOS.md (registro modelo del tipo: copia SUS campos, orden y largos; en esta parte no llevan refs ni marcas [n]).
Tu lista de ids está en tools/LISTAS-CIERRE.md (nombre, nivel, año, relaciones, líneas de mecanismo). Los ids están FIJOS: no los cambies ni inventes otros.
En campos que apuntan a otros elementos usa solo ids de LISTAS-CIERRE.md o de src-data/.

Reglas:
1. Español de Chile e inglés, texto completo en `es`. Sin web: escribe desde lo que sabes. SOLO hechos que conozcas con alta certeza (nombres, años, atribuciones, relaciones conocidas).
   Sin citas textuales, sin cifras dudosas (usa «c.», rangos o «unos»), sin títulos ni cargos inventados, sin precios ni procedencias. Ante la duda, omite la frase.
2. `refs`: [] y SIN marcas [n]. No llenes `where`. No pongas `wiki` salvo que conozcas con certeza el título exacto de la página en inglés.
3. `level`: el de la lista. `key` una frase (≤ 200 caracteres); `more` 2 a 4 frases; en enlaces, la nota explica el MECANISMO (qué cambió en el contexto → qué decisión de diseño cambió) en 1 o 2 frases (≤ 200 caracteres).
   Una coincidencia de fechas NO es un enlace. Si no puedes expresar el mecanismo sin inventar, devuelve {"ctx": "...", "item": "...", "sin_enlace": true, "motivo": "..."}.
4. Si no conoces bien un elemento, devuélvelo así: {"id": "...", "descartado": true, "motivo": "..."} (pasa a la reserva). No lo rellenes.
5. Máximo 12 elementos por agente (10 si son obras). No edites archivos del proyecto: escribe un JSON con una lista de registros (script Python con json.dump y ensure_ascii=False)
   en la ruta indicada; cada registro lleva "rtype" (context|production|theory|movement|institution|designer|work|link|connection). Ojo: es "rtype", no "type", porque en las obras "type" ya es el tipo de obra (chair, poster…).
6. Antes de terminar corre: python3 tools/pipeline/validate_out.py <tu archivo> (el nombre del archivo empieza con el tramo, por ejemplo postwar_lote3.json, o agrega --tramo postwar) y arregla lo que marque. Tu archivo no se aplica hasta que diga OK.
7. Responde con 5 líneas: elementos hechos, descartados (y por qué) y cualquier duda.
```

## Anexo B. `tools/pipeline/briefs/BRIEF-FUENTES.md` (Parte II)

```
# Tarea: fuentes de elementos YA escritos de la LHD (Parte II del plan)

Lee tools/MANUAL-CONTENIDO.md secciones 7, 7.1 y 9.1 y mira un elemento del Modernismo ya con refs (por ejemplo `gropius`).
Para cada id de tu lista (máximo 8): lee su ficha y busca 1 a 2 fuentes (2 a 3 para ★, contexto, teoría y productivo) con WebSearch y WebFetch:
museo, archivo, catálogo, enciclopedia académica (Britannica…), bibliografía académica, sitio patrimonial u oficial, texto primario digitalizado. NO Wikipedia, NO blogs de empresas ni tiendas.
SOLO URL que encontraste en búsquedas o que ya están en el proyecto; NUNCA adivines una URL. Si un WebFetch falla, no reintentes variantes: busca otra fuente.
Devuelve la ficha con marcas [n] pegadas después de la puntuación (mismos números en EN y ES; toda fuente citada y toda marca con fuente), `refs` con {label, url, checks (en español; ⚠ lo no confirmado), date (hoy)}.
Si una afirmación no aparece en ninguna fuente: quítala o suavízala y dilo en `issues`. Si una fuente contradice el texto: corrígelo y explícalo. Si algo lo dice solo una marca o un blog, atribúyelo («según…»).
Corrige también datos (año, fechas de vida) con `other` si la fuente los contradice. Para enlaces: la fuente debe sostener el mecanismo; si no, `"drop": true`.
Formato de salida: un JSON con una lista de registros; no edites el proyecto (escríbelo con un script Python, json.dump y ensure_ascii=False). Un registro por elemento:
  {"id": "...", "en": {"key": "...[1]", "more": "...[1][2]"}, "es": {"key": "...", "more": "..."}, "refs": [{"label": "Institución, documento", "url": "https://...", "checks": "qué sostiene (⚠ lo no confirmado)", "date": "<hoy>"}], "other": {"date": "1928"}, "issues": ["lo que quitaste o suavizaste y por qué"]}
  (`en` y `es` solo con los campos que cambian; `other` solo si una fuente corrige un dato; se aplica con apply2.py.)
  Enlace: {"ctx": "ctx-...", "item": "id", "en": {"note": "...[1]"}, "es": {"note": "...[1]"}, "refs": [...], "issues": []}, o {"ctx": "...", "item": "...", "drop": true, "issues": ["motivo"]} para quitarlo.
  Conexión: igual que el enlace, con "from" y "to" en vez de "ctx" e "item".
Valida con validate_out.py --refs.
Responde con 6 líneas. Si la web o el uso se agotan (429, «200 búsquedas»): no inventes; escribe lo terminado y lista los pendientes.
```

## Anexo C. Seguimiento

- Etapa previa: [x] P (fuentes visibles, Observaciones y resumen; sección 5A; v30)
- Parte I: [x] Etapa 0 (v31) · [x] Etapa 1 (listas + recorte) + **V1** (v33) · [x] Etapa 2 Posguerra (v35) · [x] Etapa 3 Reforma (v36) · [x] Etapa 4 Posmoderno (v37) · [x] Etapa 5 Industrial (v42, sin V2) · [x] Etapa 6 (≥ 500 obras: [x] 6.1 · [x] 6.2 (v43) · [x] 6.3 V3 · [x] 6.4–6.6 · [x] 6.7 (v44) · [x] 6.8 entrega; su V2 pasó a 8.7)
- **Etapa 7** (revisión editorial externa, puntos 78 y 79): [x] 7.1 revisión (v45) · [x] 7.2 **V4** · [x] 7.3 preparación (v46) · [x] 7.4 ajustes estructurales (v47) · [x] 7.5 redacción (v50) · [x] 7.6 enlaces D3 y textos (v51) · [x] 7.7 niveles, «Acerca de» e integración (v52) · [x] 7.8 entrega (v52)
- **Etapa 8** (punto 79; 8.5b agregado en el punto 81 y 8.5c en el 83): [ ] 8.1 maquetas · [ ] 8.2 datos y build · [ ] 8.3 ensayos · [ ] 8.4 interfaz · ~~8.5 PDF~~ (anulado, punto 90) · [x] 8.5b imágenes y galería · [x] 8.5c modo edición, resumen y épocas por años · [x] 8.6 pruebas · [x] 8.7 **V2 (OK, v62)**
- Parte I: **CERRADA con el V2 (punto 99, v62).**
- Parte II: [x] R1 (v63) · [ ] R2 · [ ] R3 · [ ] R4 · [ ] R5
- Parte III: [ ] III.1 elementos C de la revisión · [ ] III.2 deseables
