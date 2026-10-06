# PLAN-V1 — Cierre de la primera versión pública «LHD v1.0»

*Punto 102 de `CAMBIOS-PENDIENTES.md`. Escrito el 6 de octubre de 2026 (v74). **Reemplaza las secciones 11 a 14 de `PLAN-CIERRE.md`** (R2 a R5 antiguas). La Parte I y la R1 siguen hechas tal como constan allí. Ninguna etapa se inicia ni se da por aprobada sin el «implementa» y el visto bueno de Mauricio.*

## 0. Objetivo y decisiones tomadas

**Objetivo:** publicar la LHD v1.0 con **todas las fichas ★ revisadas** (fuentes, datos y enlaces), un proyecto limpio y coherente, una documentación nueva sin historial y un `ROADMAP.md` para las versiones siguientes.

Decisiones de Mauricio (6 oct 2026):

| # | Tema | Decisión |
|---|---|---|
| D1 | Ensayos | Se revisan **las fuentes del propio ensayo** (lo que el ensayo afirma). Las fichas no ★ que cita no entran en la v1.0. |
| D2 | Enlaces | Solo los enlaces de contexto y las conexiones **de las fichas ★**. |
| D3 | Vista pública | El sitio **abre en «★ Imprescindible»** por defecto. Lo demás sigue accesible con su aviso «No revisada». |
| D4 | Modo edición | Se mantiene, con una **contraseña nueva y segura** generada por Claude, que **vive en `editar.php`** (constante `CLAVE`). Se entrega solo por el chat; no se escribe en ningún documento. |
| D5 | Renombres | Se renombra **todo lo interno inconsistente** (épocas, niveles, `lens`, archivos, campos, clases, claves de interfaz). **Los ids de los elementos no se tocan**, salvo errores evidentes aprobados. Todo renombre se hace por script y con prueba de equivalencia. |
| D6 | Licencia | **Sin licencia** del contenido. Se mantienen los créditos de las imágenes, que exigen sus fuentes. |
| D7 | Incidencias | Se deciden en una **hoja de cálculo editable** (`.xlsx`), por bloques. |
| D8 | Idioma de la documentación | `README.md` bilingüe (EN y ES); el resto en español de Chile. **Los nombres de archivo de la documentación van en inglés** (`CONTENT.md`, `DATA.md`, `SOURCES.md`, `INTERFACE.md`…); solo el nombre, no el contenido. |
| D9 | Versiones | v74, v75… durante el trabajo; el paquete final se llama **LHD v1.0** y el proyecto limpio parte en 1.0 (`?v=1.0.0`). |

## 1. Alcance medido (v73)

| Elemento | Total | Sin fuentes |
|---|---|---|
| Obras ★ | 184 | 0 |
| Diseñadores ★ | 102 | 0 |
| Movimientos ★ | 35 | 19 |
| Instituciones ★ | 22 | 18 |
| Teorías ★ | 31 | 28 |
| Hechos de contexto (todos) | 194 | 152 |
| Productivos (fila de contexto «Productivo»; todos) | 68 | 52 |
| Ensayos | 10 | 10 |
| Enlaces de contexto de fichas ★ | 475 | 359 |
| Conexiones de fichas ★ | 91 | 72 |
| Obras ★ con fuentes débiles (refuerzo) | 7 | — |
| Elementos con incidencias (`R2-INCIDENCIAS.md`) | 224 | — |

**Estimación:** unas 27 tandas de 3 agentes (≈ 13 checkpoints), más la revisión de incidencias, la limpieza y la documentación.

## 2. Reglas que valen en todo el plan

1. Máximo **3 agentes en paralelo** (Sonnet, `general-purpose`); hasta 8 fichas o unos 15 enlaces por agente. Checkpoint con ZIP **cada 2 tandas** (`ESTADO-ACTUAL.md`, `CAMBIOS-PENDIENTES.md`, `?v=NN`, `empaquetar.sh`, SendUserFile).
2. **Sin Wikipedia** ni wikis, blogs o tiendas. Solo URL abiertas por el agente; nunca adivinadas. Fuentes de fabricante o revista se marcan con ⚠.
3. Cada marca `[n]` tiene su fuente; EN y ES llevan las mismas marcas.
4. **Los datos de ficha dudosos no se cambian en la tanda:** van como incidencia y se deciden en la R2.6.
5. Si se alcanza el límite de búsquedas o de sesión: se aplica lo que salió bien, se entrega el ZIP y lo pendiente se reencola. Nunca se inventa.
6. Nada se marca como aprobado sin el visto bueno de Mauricio.
7. Control de cada salida: `check_r2.py` → `apply2.py` → `build_data.py` («OK: no PROBLEM») → `r2_incidencias.py`.

## 3. Vistos buenos (puertas)

| Puerta | Cuándo | Qué aprueba Mauricio |
|---|---|---|
| **V-R2** | Fin de la R2 | Contenido ★ revisado, incidencias resueltas y revisión independiente |
| **V-nombres** | R2b.1 | La tabla de renombres (glosario canónico) |
| **V-limpieza** | Fin de la R2b | Sitio limpio: capturas y pruebas, sin cambios de contenido |
| **V-docs** | Fin de la R2c | Documentación nueva y `ROADMAP.md` |
| **V-1.0** | R2e | Los tres ZIP; recién entonces se publica |

---

## 4. R2 — Revisión completa de las fichas ★ `[B]`

**Definición de terminado (la comprueba un script, no la impresión):** `python3 tools/pipeline/auditoria.py --v1` da **0** en todo esto: fichas ★ sin fuentes; contextos y productivos sin fuentes; ensayos sin fuentes; enlaces y conexiones de fichas ★ sin fuentes; marcas `[n]` huérfanas o fuentes sin citar en el alcance; incidencias abiertas; obras ★ con una sola fuente.

### R2.0 Herramientas (1 sesión, sin agentes) — hecha en v76 (punto 103); falta el visto bueno de Mauricio
- [x] `prep_r2.py`: agregar los tipos `teorias`, `contextos`, `ensayos`, `enlaces` (de fichas ★) y `conexiones` (de fichas ★).
- [x] `check_r2.py`: validar enlaces (`ctx`/`item`, campo `note`), conexiones (`from`/`to`) y ensayos (`paras` con marcas; mismas marcas en EN y ES; sin romper los `[[id|texto]]`).
- [x] `apply2.py`: aplicar ensayos a `src-essays/essays.json`.
- [x] Sitio: comprobar que las marcas `[n]` de los ensayos se ven como superíndices y que la lista «Fuentes» del ensayo funciona; si no, implementarlo con su prueba.
- [x] `auditoria.py --v1`: la definición de terminado de arriba, con listado de pendientes.
- [x] **Incidencias como datos:** `tools/r2_incidencias.json` (id, tipo, campo, valor actual, propuesta, fuentes, clase, estado `abierta|decidida|aplicada|cerrada`) generado desde los `out_*.json`; `tools/pipeline/incidencias_xlsx.py export|import` (exporta la hoja y lee de vuelta las decisiones).
- [x] Plantillas de prompt para cada tipo nuevo en `CONTINUAR-R2.md`.

### R2.1 Fichas ★ restantes (≈ 3 tandas)
- [ ] 19 movimientos ★ (modelo: `macro-modernism`; campos `key`, `traits`, `context`, `shift`).
- [ ] 18 instituciones ★.
- [ ] 28 teorías ★, con el texto original digitalizado cuando exista.

### R2.2 Elementos de contexto (≈ 9 tandas)
- [ ] Los 152 hechos de contexto y los 52 productivos (materiales, procesos y herramientas) sin fuentes; 2 a 3 fuentes cada uno, con marcas en cifras, fechas y nombres.

### R2.3 Ensayos (≈ 2 tandas; 2 ensayos por agente)
- [ ] Los 10 ensayos (6 de foco y 4 de disciplina): verificar cada afirmación de hecho del ensayo, poner marcas `[n]` y su lista `refs`. Lo que no se sostenga se quita o se suaviza (`issues`). **No se revisan las fichas citadas** (D1).

### R2.4 Enlaces y conexiones de fichas ★ (≈ 10 tandas)
- [ ] 359 enlaces de contexto y 72 conexiones sin fuentes. La fuente debe sostener **el mecanismo** (qué cambió en el contexto → qué decisión de diseño cambió). Si no se puede: se reescribe a lo que consta o se propone `drop` (va a la hoja de incidencias; no se borra sin decisión).
- [ ] Revisar de paso los 116 enlaces ★ que ya tienen fuentes, pero solo si el agente detecta un problema evidente.

### R2.5 Refuerzo de fuentes débiles (≈ media tanda)
- [ ] `seagram-building`, `think-small`, `cadillac-eldorado-1959`, `i-love-ny-1977`, `dvf-wrap-dress-1974`, `air-jordan-1-1985`, `beethoven-poster-1955`: al menos 2 fuentes de calidad cada una.
- [ ] Fichas ★ cuya única fuente de un dato sea de fabricante o revista (⚠): buscar una fuente institucional.

### R2.6 Incidencias, datos dudosos y correcciones pendientes (por bloques)
- [ ] Clasificar todas las incidencias (las 224 actuales más las que salgan en R2.1–R2.5):
  - **Clase A — dato contradicho** por 2 o más fuentes de calidad (p. ej. muerte de Gehry, nacimiento de Philip Johnson en Cleveland, Fernando Campana fallecido): la hoja llega con la corrección **aceptada por defecto**.
  - **Clase B — fuentes en desacuerdo** entre sí (p. ej. Posada 1851/1852, Bazaar 1955/1957): se propone «c.», un rango o mantener, según el caso.
  - **Clase C — texto ya quitado o suavizado** por el agente: informativa; se cierra en bloque salvo que Mauricio marque alguna.
  - **Clase D — campos de ficha** (`designers`, `maker`, `materials`, fechas de inicio y fin de movimientos): propuesta con fuente.
- [ ] Incluir los pendientes ★ anteriores: `dresser-teapot` (`maker`), `citroen-2cv` (`designers`), `lc2-armchair` (`maker` vacío), Pugin, Paxton 1803/1801, Etruria, tipografía de Múnich 72, `cadillac-eldorado-1959` (Earl o Mitchell), Guggenheim Bilbao.
- [ ] Entregar la hoja `.xlsx` en bloques de ~40 filas: columnas id · tipo · campo · valor actual · propuesta · fuentes · clase · recomendación · **decisión** (Aceptar / Rechazar / Otro) · **valor final** · nota.
- [ ] Aplicar las decisiones con `incidencias_xlsx.py import` → build → estado `aplicada`.

### R2.7 Revisión independiente de lo ★ (1 a 2 tandas)
- [ ] 3 agentes que no redactaron contrastan una **muestra estratificada de 40 afirmaciones**: obras, diseñadores, movimientos/instituciones/teorías, contextos, ensayos, enlaces; repartidas por época. Responden CONFIRMADA / REFUTADA / NO CONCLUYENTE, con la cita.
- [ ] **Regla de escalada:** si en un estrato hay 2 o más REFUTADAS, ese estrato se amplía con otra muestra de 40.
- [ ] Resultado en `tools/REVISION-INDEPENDIENTE-V1.md`; solo lo REFUTADO se corrige (pasa por la hoja de incidencias).

### R2.8 Cierre de la R2
- [ ] `auditoria.py --v1` en 0; build sin PROBLEM; todas las pruebas PASS.
- [ ] **V-R2**: visto bueno de Mauricio al contenido.

---

## 5. R2b — Proyecto limpio y coherente (sin cambios de contenido) `[A/B]`

**Regla de oro:** la R2b **no cambia ningún texto ni dato**. Lo garantiza una prueba de equivalencia: el `all.json` de antes y el de después son idénticos una vez aplicada la tabla de renombres.

- [ ] **R2b.0 Respaldo:** `LHD-respaldo-vNN.zip` con el proyecto completo tal cual (historia incluida), entregado **antes** de tocar nada.
- [ ] **R2b.1 Inventario y glosario:** script `tools/inventario_nombres.py` que lista ids de época, valores de nivel, campos de datos, nombres de archivos, claves de interfaz (`UI.es`/`UI.en`), clases CSS, funciones y comentarios con marca de versión («v24:», etc.). Propuesta de **tabla de renombres** (`tools/renombres.json`), por ejemplo:

  | Hoy | v1.0 |
  |---|---|
  | épocas `industrial`, `reform`, `modernism`, `postwar`, `postmodern` | `1750-1850`, `1851-1913`, `1914-1944`, `1945-1974`, `1975-hoy` (carpetas de `src-data/` con el mismo nombre) |
  | niveles `normal` / `essential` y bandera `star` | `complete` / `essential` (una sola forma) |
  | `lens` (código, CSS, ids de ensayo `lens-*`) | `focus` |
  | `90-test-content.json` y otros nombres de archivo provisorios | nombres según su contenido |

  La auditoría lista además los **ids de elementos inconsistentes** (p. ej. obras sin año en el id) para que Mauricio decida caso a caso; por defecto no se tocan. → **V-nombres**.
- [ ] **R2b.2 Línea base:** guardar el `all.json` normalizado, los resultados de todas las pruebas y capturas de 8 vistas clave (inicio, foco, disciplina, ficha de obra, de diseñador, de ensayo, modo edición, tema oscuro).
- [ ] **R2b.3 Renombres por script** (`tools/renombrar.py renombres.json`): datos, `build_data.py`, `app.js`, `style.css`, `editar.php`, pruebas y herramientas. Solo por script, nunca a mano.
- [ ] **R2b.4 Eliminar restos:**
  - código y CSS sin uso (cobertura de Chromium para JS y CSS; revisión de cada candidato);
  - comentarios con marcas de versión o de etapas; los 11 TODO (se resuelven o pasan al `ROADMAP.md`);
  - campos de datos que el sitio no lee; restos de funciones descartadas (PDF de ensayos, contraseña antigua, niveles antiguos, `posthumous` si ya no aplica, etc.);
  - scripts de etapas cerradas (`prep_etapa6/7`, `ajustes_etapa7`, `recortar`, `listas_check`, `validate_out`, `apply_new`, etc.) y carpetas de trabajo (`e7_work`, `e8_work`, `e8_img`, `r2_work`);
  - pruebas de etapas cerradas, que se fusionan en pruebas por función (`test_sitio`, `test_fichas`, `test_fuentes`, `test_editar`, `test_datos`).
- [ ] **R2b.5 Cambios de comportamiento acordados:**
  - abrir en «★ Imprescindible» por defecto (D3), con su prueba;
  - **contraseña nueva** (≥ 20 caracteres aleatorios) en la constante `CLAVE` de `editar.php` (D4), entregada a Mauricio solo por el chat; `empaquetar.sh` deja de buscar una clave escrita y solo comprueba que `CLAVE` no esté vacía ni sea una clave antigua;
  - herramientas que quedan, generalizadas: `build_data.py`, `auditoria.py`, `prep_fuentes.py` / `check_fuentes.py` / `apply_fuentes.py` (el ciclo de fuentes para cualquier tipo), `incidencias_xlsx.py`, `empaquetar.sh` (con modos `proyecto`, `web` y `respaldo`), `check_contrast.py`, `make_help_images.py`.
- [ ] **R2b.6 Auditoría de no ruptura:**
  - prueba de equivalencia de `all.json` (antes = después con la tabla aplicada);
  - todas las pruebas PASS;
  - `tools/tests/test_limpieza.py`: ningún nombre antiguo de la tabla aparece en ningún archivo; ningún archivo sin referencia; ninguna clave de interfaz sin uso; sin errores de consola en las 8 vistas;
  - capturas de las 8 vistas comparadas con la línea base (solo debe cambiar la vista inicial por D3).
- [ ] **V-limpieza.**

---

## 6. R2c — Documentación nueva («fresh start») `[A]`

Describe **solo el estado actual**: sin historial, sin puntos numerados, sin «antes era…».

| Archivo | Contenido |
|---|---|
| `README.md` (EN y ES) | Qué es; cómo correrlo y probarlo; estructura de carpetas; cómo publicar; dónde está cada documento |
| `BRIEF.md` | Propósito, tesis («el diseño como respuesta a su contexto»), público, alcance temporal y disciplinar, épocas, cifras de la v1.0, qué está revisado y qué no |
| `CLAUDE.md` | Instrucciones para agentes: comandos, reglas de contenido y fuentes, convenciones de nombres, flujo de trabajo, lo que no se hace (Wikipedia, inventar URL, tocar datos dudosos, `pkill`), cómo entregar |
| `docs/CONTENT.md` | Manual editorial: tipos de elemento, niveles, criterios de inclusión, conexiones y prueba de tres preguntas, estilo bilingüe (español de Chile), largos, imágenes y créditos, **glosario canónico** |
| `docs/DATA.md` + `schema/*.json` | Modelo de datos por tipo, archivos de `src-data/`, ids; **JSON Schema** que el build usa para validar |
| `docs/SOURCES.md` | Método de fuentes y revisión, ciclo con agentes y plantillas de prompt, hoja de incidencias, revisión independiente |
| `docs/INTERFACE.md` | Diseño e interacción: filas, foco, disciplinas, niveles, organizar, fichas, colores y temas, accesibilidad, modo edición; mapa de `app.js` |
| `ROADMAP.md` | Etapas futuras (sección 7) |
| `CHANGELOG.md` | Una sola entrada: «1.0» |

- [ ] Redactar los archivos.
- [ ] **Prueba de la documentación:** un agente nuevo recibe **solo** el ZIP limpio y una tarea real (agregar una ficha con fuentes, aplicarla, pasar el build y las pruebas, empaquetar). Lo que no logre hacer sin preguntar es un vacío de la documentación y se corrige.
- [ ] **V-docs.**

---

## 7. R2d — `ROADMAP.md` (contenido previsto)

Cifras recalculadas al cerrar la R2 con `auditoria.py`.

1. **v1.1 — Revisión de las fichas no ★:** obras (382), diseñadores (242), movimientos (41), instituciones (66) y teorías (58) sin fuentes (cifras de v73); con la misma regla de incidencias.
2. **v1.1 — Enlaces y conexiones restantes:** 710 enlaces de contexto y 19 conexiones sin fuentes (v73) que no son de fichas ★; enlaces que no sostengan su mecanismo se reescriben o se quitan.
3. **v1.1 — Revisión independiente global** (muestra estratificada con escalada sobre toda la línea) y activar `STRICT_THEORY_SOURCES`.
4. **Pendientes de datos:** `levis-riveted-jeans` desconectado; contextos con un solo enlace; 135 fichas sin imagen; conceptos del Modernismo (marcas en `key`, recuento en el sitio).
5. **v1.2 — Contenido nuevo (prioridad C de la revisión editorial):** 15 obras, 4 diseñadores, 2 instituciones, 4 teorías, 1 productivo y una obra para el diseño crítico y especulativo (Dunne & Raby).
6. **Deseables:** segunda obra para los diseñadores con una sola; conceptos para todas las épocas; recuperar los enlaces suspendidos; reemplazar fuentes débiles por primarias; tercer nivel de detalle; revisión del inglés por una persona nativa; pruebas de accesibilidad (teclado, contraste, lector de pantalla); revisión visual por época.
7. **Técnico:** contraseña con *hash* y fuera del código; los TODO que no se resolvieron en la R2b.

- [ ] Redactar `ROADMAP.md` (va dentro del V-docs).

---

## 8. R2e — Los tres paquetes `[C]`

| ZIP | Contenido | Prueba |
|---|---|---|
| `LHD-respaldo-vNN.zip` | El proyecto completo con su historia (el de R2b.0; se rehace al final si hubo cambios) | Descomprimir y build |
| `LHD-v1.0-web.zip` | Solo lo que se publica: `index.html`, `app.js`, `style.css`, `data/all.json`, `data/essays.json`, `editar.php`, `ediciones/` (con `.htaccess` e `imagenes.json` = `{}`), `help/*.webp` | Carpeta vacía + servidor PHP + pruebas generales; sin `tools/` ni `src-data/` |
| `LHD-v1.0.zip` | Proyecto limpio: sitio, `src-*`, `tools/` vigentes, `schema/`, `docs/` y los documentos nuevos | Carpeta vacía: build, todas las pruebas, `auditoria.py --v1` en 0 |

- [ ] Armar y probar los tres (`empaquetar.sh respaldo|web|proyecto`).
- [ ] Entregar con SendUserFile, más la contraseña nueva por el chat y una lista corta de dudas ⚠ (máximo 25, ordenadas por riesgo).
- [ ] **V-1.0.** Solo después se publica.

## 9. Orden y ritmo

R2.0 → R2.1 → R2.2 → R2.3 → R2.4 → R2.5 → R2.6 (a medida que se acumulan bloques) → R2.7 → **V-R2** → R2b.0 → R2b.1 → **V-nombres** → R2b.2 a R2b.6 → **V-limpieza** → R2c y R2d → **V-docs** → R2e → **V-1.0**.

Riesgos y cómo se mitigan:
- **Límites de la cuenta:** tandas pequeñas, checkpoint cada 2 tandas y reencolar; el límite semanal se reinicia el 8 de octubre, 22:00 (America/Santiago).
- **Que la limpieza rompa algo:** congelamiento del contenido, línea base, renombres solo por script, prueba de equivalencia y capturas.
- **Documentación incompleta:** prueba con un agente que solo tenga el ZIP limpio.
- **Errores de fuentes que no detecta el control de forma:** revisión independiente con escalada.
