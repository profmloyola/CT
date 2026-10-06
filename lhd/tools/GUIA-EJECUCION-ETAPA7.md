# Guía de ejecución de la etapa 7 (pasos 7.4 a 7.8)

*Preparada en v46 (5 de octubre de 2026, punto 79) para que una sesión nueva con **Sonnet** ejecute, sin decisiones nuevas, todas las correcciones aprobadas por Mauricio en el **V4** sobre la revisión editorial externa (`tools/REVISION-EDITORIAL-ETAPA7.md`). Léela completa antes de empezar. Si algo no calza con lo que dice aquí, **detente y avisa**: no improvises.*

---

## 0. Qué está decidido y qué ya está hecho

### 0.1 Decisiones del V4 (no se vuelven a preguntar)
| | Decisión | Consecuencia para esta etapa |
|---|---|---|
| D1 | Se aprueban las prioridades **A y B**; la **C** pasa a la **Parte III** (desarrollo futuro). | Solo se trabaja lo que en `REVISION-ETAPA7.json` tiene `estado: "aprobado-V4"` (171 registros). Lo `parte-III` (26) **no se toca**. |
| D2 | La disciplina se sigue llamando **«Moda»**; internamente es «moda y textil». | No se cambia ningún rótulo. Lo explicará la ficha de disciplina de la **etapa 8**. |
| D3 | La ★ se decide por **importancia**. A toda obra ★ se le buscan enlaces de contexto **sin forzarlos**; se pueden agregar hechos de contexto. | Lotes `_e` de enlaces para 59 obras ★; lo que no se pueda enlazar con certeza se anota como **excepción C4c**. Nunca se baja una ★ por falta de enlaces. |
| D4 | Aprobados los cuatro ★ chilenos (Cybersyn, Quinta Monroy, arpilleras, franja del NO); La Aurora de Chile pasa a Completo. | Incluido en el Anexo B. |
| D5 | Se agregan los contextos de **COVID-19** e **IA generativa**. | Ya están en el JSON como B, con sus anclas (ilustración del SARS-CoV-2 de los CDC; portada de *Cosmopolitan* hecha con DALL·E 2; productivo «modelos generativos de texto a imagen»). |
| D6 | El **V2** pasa al final de la **etapa 8**, antes de la Parte II. | El paso 7.8 es solo una entrega (ZIP y resumen), sin V2. |
| D7 | Los cuatro candidatos pasan a la **reserva**. | Lo hace `ajustes_etapa7.py estructura` (Monumento a la Independencia, Torres Siamesas, *Where the Wild Things Are*, Puente del Alamillo, y los diseñadores que quedan sin obra: Rivas Mercado, Sendak, Calatrava). |
| D8 | «Acerca de» con una subsección nueva sobre el **fundamento conceptual y bibliográfico** (Forty y el canon de la sección 1.1 de la revisión). | Paso 7.7, con los textos de la sección 7.3 de esta guía. |

Se entiende aprobado también todo `REVISION-ETAPA7-AJUSTES.json` (pertenencias, fusiones, renombres, correcciones), que no lleva prioridad.

### 0.2 Hecho en v46 (no repetir)
- **7.1** revisión; **7.2** V4; **7.3** herramientas listas y probadas:
  - `tools/pipeline/ajustes_etapa7.py` — aplica lo mecánico (fases `estructura`, `relaciones`, `niveles`; modo `--prueba` en una copia y `--aplicar`).
  - `tools/pipeline/prep_etapa7.py` — arma los lotes para los agentes.
  - `tools/pipeline/briefs/BRIEF-ETAPA7-REDACCION.md` — instrucciones de los agentes.
  - `tools/pipeline/check_etapa7.py` — verificación de cierre.
  - `tools/pipeline/validate_out.py` reconoce los ids aprobados de `REVISION-ETAPA7.json`.
  - `tools/build_data.py` acepta `posthumous: true` en una obra (Bodoni, 1818); documentado en `SPEC.md` 5.5.
- Ensayo completo de la fase `estructura` sobre una copia: **225 cambios en 45 archivos y build «OK: no PROBLEM»**. La fase `niveles` sobre esa copia solo falla por `louis-sullivan` (necesita el Wainwright ★, que se crea en 7.5): es lo esperado.

---

## 1. Antes de empezar (cada sesión)
1. Leer `INICIO-SESION-NUEVA.md`, `ESTADO-ACTUAL.md` y la sección 9c de `tools/PLAN-CIERRE.md`.
2. `python3 tools/build_data.py 2>&1 | tail -3` → debe decir `OK: no PROBLEM`.
3. `sh tools/tests/run_all.sh 2>&1 | grep -E "FAIL|Error|Timeout"` → sin salida.
4. Mirar `tools/PENDIENTES-FUENTES.md` (al final se anotan descartes y excepciones de esta etapa).
5. **Nunca** `pkill -f "php -S"`. `ediciones/` debe quedar limpia al entregar.
6. Modelos: la sesión que orquesta puede ser Sonnet; los agentes, `general-purpose` con `model: "sonnet"` (punto 60). Si un paso falla dos veces, avisar antes de subir de modelo.

---

## 2. Mapa de archivos

| Archivo | Para qué |
|---|---|
| `tools/REVISION-EDITORIAL-ETAPA7.md` | La revisión (criterios, diagnóstico, anexos A a G). Se consulta, no se edita. |
| `tools/REVISION-ETAPA7.json` | 197 registros nuevos en formato de propuesta. **Usar solo `estado: "aprobado-V4"`.** Campos útiles: `links` (enlaces propuestos con su línea de mecanismo), `duda`, `reserva_origen`, `miembros` (movimientos), `obras` (instituciones), `anclas` (productivo). |
| `tools/REVISION-ETAPA7-AJUSTES.json` | Cambios sobre lo existente: `niveles_*`, `fusiones_y_renombres`, `pertenencia_movimientos`, `pertenencia_instituciones`, `correcciones`, `candidatos_reserva_aprobados_V4`, `reposiciones`, `enlaces_estrella` (D3) y `decisiones_V4`. |
| `tools/pipeline/ajustes_etapa7.py` | Aplica lo mecánico. Todo lo que retira lo guarda en `RESERVA-FASE-B.json` → `etapa7_retirados`. |
| `tools/pipeline/prep_etapa7.py OUTDIR` | Crea los lotes: `<tramo>_w/_d/_m/_c<n>.json` (fichas nuevas), `<tramo>_e<n>.json` (enlaces D3) y `textos_1.json` (reescrituras). |
| `tools/pipeline/validate_out.py`, `apply_new.py`, `apply2.py` | Validar y aplicar la salida de los agentes (como en la etapa 6). |
| `tools/pipeline/check_etapa7.py` | Verificación final (paso 7.7). |
| `tools/pipeline/etapa7_anexos.py [SALIDA]` | Regenera las tablas de los anexos si cambian los JSON. |

---

## 3. Orden de trabajo (resumen)

```
7.4  ajustes_etapa7.py estructura --prueba → --aplicar → build → pruebas
7.5  prep_etapa7.py → agentes (lotes c, m, d, w) → validate_out → apply_new (por tramo)
     → ajustes_etapa7.py relaciones --aplicar → build
7.6  agentes (lotes _e y textos_1) → apply_new (enlaces) y apply2 (textos) → lote de relleno → build
     → excepciones C4c anotadas
7.7  ajustes_etapa7.py niveles --prueba → --aplicar → «Acerca de» (D8) → check_etapa7.py → build, pruebas, capturas
7.8  ZIP y resumen (sin V2; el V2 es al final de la etapa 8)
```

Cada paso termina con la rutina de la sección 5 del plan (build, pruebas, `?v=NN`, punto en `CAMBIOS-PENDIENTES.md`, entrada en `PROJECT.md`, casilla marcada, `ESTADO-ACTUAL.md` y ZIP con `sh tools/empaquetar.sh NN`). Si la sesión se corta, el ZIP permite seguir desde el último paso marcado.

---

## 4. Paso 7.4 — Ajustes estructurales `[C]`

### 4.1 Ejecutar
```
cd lhd
python3 tools/pipeline/ajustes_etapa7.py estructura --prueba    # ensayo: no toca src-data/
```
Resultado esperado: `== estructura --prueba: 225 cambios; 45 archivos`, 57 pendientes «para la redacción» (normales: son pertenencias de fichas que aún no existen) y `== build: OK: no PROBLEM`. Si el número difiere poco, revisar la lista; si el build da PROBLEM, **no aplicar** y avisar.
```
python3 tools/pipeline/ajustes_etapa7.py estructura --aplicar
python3 tools/build_data.py 2>&1 | tail -3
```

### 4.2 Qué hace (para entender el informe)
1. **Pertenencias** (Anexo D de la revisión): agrega `movements` a obras y diseñadores, `links.institutions` a movimientos, `links.movements` a teorías, `links.works` a instituciones e `institutions` a diseñadores. Quita 6 pertenencias erróneas: Hokusai del cartel ilustrado; Windows Phone del estilo tipográfico internacional; Lina Bo Bardi, Kurokawa y la Nakagin del brutalismo (el metabolismo se crea en 7.5); Eileen Gray del art déco (pasa al estilo internacional).
2. **Fusiones y retiros:** `social-architecture` → `participatory-social-architecture`; retira `iconic-architecture`, `droog-design` (su obra pasa a `inst-droog`), `inst-archigram` (queda el diseñador `archigram`) y `bentwood` (queda `steam-bentwood`).
3. **Renombres de metadatos** (`name`/`short` EN y ES): Brutalismo, Futurismo (con `start` 1909 y carpeta `reform`), Punk (con `graphic`), «Medievalismo romántico y renovación religiosa» (`ctx-gothic-revival`) y «Hormigón pretensado y cáscaras delgadas». **Fechas:** estilo internacional 1925, arquitectura posmoderna 1964, urbanismo del paisaje 1982. **Pista:** `ctx-great-exhibition` y `ctx-paris-1900` pasan a «cultural» (archivo `43-context-cultural.json`). `th-speculative-everything` se liga a `critical-speculative-design`.
4. **Correcciones:** Bodoni 1818 con `posthumous: true`; Werkbund de Colonia y debate de 1914 (a la carpeta `modernism`); silla n.º 14 con `michael-thonet`; Jatiya Sangsad con `louis-kahn`, `year` 1962 y `date` «1962–1982» (a la carpeta `postwar`); `maker` de Seattle, Catedral de Brasilia y Museo de Antropología; `prozodezhda-1922` con país RU.
5. **D7:** pasan a la reserva las 4 obras y los 3 diseñadores que quedan sin obra, con sus enlaces.
6. **Reposiciones** desde `recorte_modernismo`: Maison de Verre y Chareau, Karl-Marx-Hof, Baby Brownie y Teague, vestidos de Alix y Madame Grès, Anglepoise y Carwardine, silla Faaborg y Kaare Klint, **con sus fuentes y enlaces originales**.

### 4.3 Después de aplicar
- Cifras esperadas en `data/all.json`: **587 obras, 341 diseñadores, 73 movimientos, 93 instituciones, 64 productivos**.
- `sh tools/tests/run_all.sh`: si alguna prueba falla **solo por un conteo** (obras por tramo, etc.), se ajusta la prueba (regla C6) y se anota en `PROJECT.md`. Si falla por un error de página, se corrige el código.
- Anotar en `PENDIENTES-FUENTES.md` (sección «Etapa 7»): lo retirado (D7 y fusiones) y que los textos de los renombrados quedan para 7.6.
- Los **textos** de los elementos renombrados o corregidos todavía no están al día: los reescribe el lote `textos_1` en 7.6. No es un error.

---

## 5. Paso 7.5 — Redacción de las fichas nuevas `[B]`

### 5.1 Preparar los lotes
```
python3 tools/pipeline/prep_etapa7.py /tmp/e7
cat /tmp/e7/INDICE.txt
```
Esperado: 24 lotes de fichas nuevas (160 registros: 65 obras, 44 diseñadores, 22 teorías, 11 contextos, 7 instituciones, 7 movimientos, 4 productivos), 5 lotes `_e` (D3) y `textos_1`. Las 11 fichas repuestas en 7.4 no aparecen (ya están); `ctx-photography` sí aparece, porque se redacta con sus enlaces.

### 5.2 Lanzar los agentes
- Orden: primero los lotes `_c` y `_m` (contexto, productivo, teoría, movimientos, instituciones), luego `_d` (diseñadores) y al final `_w` (obras). Se pueden lanzar en paralelo dentro de cada grupo (hasta 8 a la vez).
- Prompt de cada agente (copiar y cambiar solo las rutas):

> Proyecto LHD en `<ruta>/lhd`. Lee `tools/pipeline/briefs/BRIEF-ETAPA7-REDACCION.md` y síguelo al pie de la letra. Tu lote es `/tmp/e7/<lote>.json`. Escribe tu salida en `/tmp/e7/out/<lote>_out.json` y valida con `python3 tools/pipeline/validate_out.py /tmp/e7/out/<lote>_out.json --tramo <tramo>` hasta que diga OK. No edites archivos del proyecto. Responde en 5 líneas.

### 5.3 Aplicar
Por tramo, en el orden del punto anterior:
```
python3 tools/pipeline/apply_new.py <tramo> /tmp/e7/out/<tramo>_c1_out.json /tmp/e7/out/<tramo>_m1_out.json ...
```
- `apply_new.py` rechaza todo el archivo si la validación falla o si un id ya existe: corregir y volver a aplicar.
- Los `descartado` y `sin_enlace` se anotan solos en `PENDIENTES-FUENTES.md`.
- Un contexto cuyos enlaces apuntan a obras que aún no se aplican puede dar PROBLEM en el build («item desconocido»): **aplicar todos los lotes del paso antes de correr el build**. Si al final un enlace apunta a una ficha descartada, quitar ese enlace (anotarlo).

Después de aplicar todo:
```
python3 tools/pipeline/ajustes_etapa7.py relaciones --aplicar
python3 tools/build_data.py 2>&1 | tail -3
```
`relaciones` fija lo que los agentes no escriben en otras fichas: miembros de los movimientos nuevos (`miembros`), obras de las instituciones nuevas (`obras`), `tech` de las obras ancla de los productivos nuevos (`anclas`) y las pertenencias del Anexo D que esperaban una ficha nueva. Es idempotente: se puede correr de nuevo sin duplicar.

### 5.4 Puntos que requieren cuidado
- **Movimientos nuevos y macromovimientos:** agregar a `parts` de `macro-modernism` los movimientos `suprematism`, `plakatstil` (si se acepta como precursor) y `new-york-school-graphic`, y a `macro-postmodernism` ninguno nuevo. `gothic-revival` y `design-methods` no van en ningún macro. Hacerlo a mano en `src-data/reform/02-movements.json` (macro-modernism) y anotarlo.
- **Metabolismo:** al crearse, `relaciones` le pone la Nakagin, Kurokawa, Tange y la Yoyogi como miembros.
- **Obras con `duda`:** si el agente omitió el dato dudoso, está bien. Si lo afirmó, revisar.
- **Anclas de D5** (`cdc-sars-cov-2-illustration-2020`, `cosmopolitan-ai-cover-2022`): si un agente las descarta por falta de certeza, el contexto correspondiente se queda con un solo enlace (o ninguno): en ese caso, **no aplicar el contexto** sin enlaces y avisar en la entrega.

---

## 6. Paso 7.6 — Enlaces D3, textos y relleno `[B]`

### 6.1 Enlaces de las ★ existentes (lotes `_e`)
Mismo prompt del 5.2 con el lote `_e`. Aplicar con `apply_new.py <tramo> <salida>` (solo trae registros `link`). Regla D3: un `sin_enlace` no es un fracaso; la obra queda como excepción.

### 6.2 Reescrituras (`textos_1`)
Mismo prompt con `textos_1`. La salida está en formato de `apply2.py` (no pasa por `validate_out.py`). Revisarla a mano (EN y ES con los mismos campos; `refs` idénticos a los actuales; marcas `[n]` intactas) y aplicar:
```
python3 tools/pipeline/apply2.py /tmp/e7/out/textos_1_out.json
python3 tools/build_data.py 2>&1 | tail -3
```

### 6.3 Lote de relleno y excepciones
- Correr `python3 tools/pipeline/check_etapa7.py` y mirar el punto 4 (obras ★ con menos de dos enlaces directos de subcategorías distintas). Para cada una que no tenga enlace cierto, **anotar la excepción C4c** en `PENDIENTES-FUENTES.md` con el motivo (la columna «nota» de `enlaces_estrella` ya trae el motivo de las 28 excepciones previstas y de los 4 enlaces suspendidos que esperan fuente).
- Hechos de contexto nuevos con menos de 2 enlaces (meta C4): `ctx-suez-crisis-1956` tendrá 1 (aceptado); si otro queda en 0, no se aplica.
- Un lote de relleno (como en la etapa 6) para contextos nuevos con un solo enlace solo si hay mecanismos ciertos.

---

## 7. Paso 7.7 — Niveles, «Acerca de» e integración `[C]`

### 7.1 Niveles
```
python3 tools/pipeline/ajustes_etapa7.py niveles --prueba
python3 tools/pipeline/ajustes_etapa7.py niveles --aplicar
```
Debe dar build sin PROBLEM. Si da «designer X: level essential but no work at that level», es que la obra ★ que lo sostiene se descartó en 7.5: dejar ese diseñador en Completo (editar su `level` a `normal`) y anotarlo.

### 7.2 Verificación
```
python3 tools/build_data.py 2>&1 | tail -3
python3 tools/pipeline/check_etapa7.py --estricto
```
- Punto 1: los aprobados que faltan deben ser solo descartes anotados.
- Punto 2 (movimientos ★ sin obra ★ visible) y punto 5 (diseñadores ★ sin obra ★) deben quedar en 0. Si un movimiento ★ no tiene obra ★, revisar sus pertenencias (Anexo D) antes de tocar niveles.
- Punto 3: los que queden sin obras deben anotarse (se espera que solo queden algunos premios, museos y el diseño crítico y especulativo, cuya obra pasó a la Parte III).

### 7.3 «Acerca de» (D8)
En `app.js`, función `infoCard()`, agregar una sección **después** de `sect(t('infoAbout'), paras(t('infoIntro')))`:
```js
sect(t('infoBasis'), paras(t('infoBasisText')) + basisList()) +
```
y, junto a `infoCard`, la función:
```js
// v4x (D8, etapa 7): fundamento conceptual y bibliográfico de la línea
const BASIS = [
  ['Adrian Forty', 'Objects of Desire: Design and Society since 1750', 1986, 'base'],
  ['Nikolaus Pevsner', 'Pioneers of the Modern Movement', 1936, 'gen'], ['Sigfried Giedion', 'Mechanization Takes Command', 1948, 'gen'],
  ['Reyner Banham', 'Theory and Design in the First Machine Age', 1960, 'gen'], ['John Heskett', 'Industrial Design', 1980, 'gen'],
  ['Penny Sparke', 'An Introduction to Design and Culture', 1986, 'gen'], ['Jonathan Woodham', 'Twentieth-Century Design', 1997, 'gen'],
  ['David Raizman', 'History of Modern Design', 2003, 'gen'], ['Victor Margolin', 'World History of Design', 2015, 'gen'],
  ['Philip B. Meggs y Alston W. Purvis', "Meggs' History of Graphic Design", 1983, 'graphic'], ['Stephen Eskilson', 'Graphic Design: A New History', 2007, 'graphic'],
  ['Kenneth Frampton', 'Modern Architecture: A Critical History', 1980, 'architecture'], ['William J. R. Curtis', 'Modern Architecture since 1900', 1982, 'architecture'],
  ['Christopher Breward', 'The Culture of Fashion', 1995, 'fashion'], ['Valerie Steele', 'Fifty Years of Fashion: New Look to Now', 1997, 'fashion'],
  ['Silvia Fernández y Gui Bonsiepe (coords.)', 'Historia del diseño en América Latina y el Caribe', 2008, 'latam'],
];
function basisList() {
  const groups = ['gen', 'graphic', 'architecture', 'fashion', 'latam'];
  return groups.map((g) => `<div class="info-sub">${esc(t('basis_' + g))}</div><ul class="basis">` +
    BASIS.filter((b) => b[3] === g).map((b) => `<li>${esc(b[0])}, <i>${esc(b[1])}</i> (${b[2]})</li>`).join('') + '</ul>').join('');
}
```
(En inglés, «y» → «and» y «coords.» → «eds.»: usar `S.lang` dentro de `basisList` o duplicar los autores en dos listas.)

Textos para `UI.es` (y su traducción en `UI.en`):
- `infoBasis`: «Fundamento conceptual y bibliográfico» / «Conceptual and bibliographic basis».
- `basis_gen`: «Historia general del diseño» / «General design history»; `basis_graphic`: «Diseño gráfico» / «Graphic design»; `basis_architecture`: «Arquitectura» / «Architecture»; `basis_fashion`: «Moda» / «Fashion»; `basis_latam`: «América Latina» / «Latin America».
- `infoBasisText` (dos párrafos separados por una línea en blanco):

> La línea se apoya en la historia social del diseño. Su base conceptual es *Objects of Desire: Design and Society since 1750* (1986), de Adrian Forty, que estudia el diseño desde 1750 no como una sucesión de estilos o de autores, sino como la forma material que toman las ideas, las necesidades y los conflictos de cada sociedad: la división del trabajo en la fábrica, la organización del hogar y de la oficina, el consumo, la higiene o la imagen de las empresas. De ese enfoque vienen la tesis de la línea —el diseño como respuesta a su contexto— y su fecha de inicio.
>
> La selección de movimientos, instituciones, textos, diseñadores y obras sigue el canon de las historias generales que se usan en la enseñanza universitaria del diseño y de sus cuatro disciplinas. Ninguna de ellas es por sí sola el canon: lo que aparece en casi todas orienta el nivel imprescindible (★), y el resto, el nivel completo. Las fuentes de cada ficha se citan al final de ella; las fichas que aún no tienen fuentes muestran una advertencia.

> The timeline rests on the social history of design. Its conceptual basis is Adrian Forty’s *Objects of Desire: Design and Society since 1750* (1986), which studies design since 1750 not as a sequence of styles or authors but as the material form taken by the ideas, needs and conflicts of each society: the division of labour in the factory, the organisation of the home and the office, consumption, hygiene or the image of companies. From that approach come the thesis of the timeline—design as a response to its context—and its starting date.
>
> The choice of movements, institutions, texts, designers and works follows the canon of the general histories used in university teaching of design and its four disciplines. None of them is the canon on its own: what appears in almost all of them guides the must-know level (★), and the rest, the complete level. The sources of each card are cited at its end; cards that do not yet have sources show a warning.

(Los títulos de libros van en cursiva con `<i>` construido en `basisList`; en `paras` el texto se escapa, así que en `infoBasisText` los títulos van sin asteriscos.) Agregar en `style.css` una regla mínima para `.basis` (lista sin viñetas o con viñeta discreta, mismo tamaño que `.sum-tip`) y comprobar el contraste con `python3 tools/check_contrast.py`.

### 7.4 Cierre técnico
- Actualizar en «Acerca de» y en la ayuda las cifras que estén escritas a mano (las de `stats` se calculan solas).
- `sh tools/tests/run_all.sh` (ajustar pruebas de conteo, C6), `python3 tools/check_contrast.py`, `python3 tools/make_help_images.py` si cambió la ficha de información.
- Rendimiento: carga local con Playwright (< 3 s) y 4 capturas: línea completa ES claro; un tramo EN oscuro; la ficha «Acerca de» con la sección nueva; ancho 390 px.

---

## 8. Paso 7.8 — Entrega `[C]`
ZIP (`sh tools/empaquetar.sh NN`) y resumen de 6 líneas: cifras por período y disciplina, ★ (total y %), % de América Latina, excepciones C4c, descartes y lo que pasó a la reserva. **No hay V2 aquí**: el V2 es al final de la etapa 8 (D6). El siguiente paso es la etapa 8 (sección 9d del plan), que no se inicia sin el «implementa» de Mauricio.

---

## 9. Reglas que no se pueden romper
- **No inventar** (C1): solo hechos de alta certeza; ante la duda, omitir. **Sin web** en la Parte I. `refs: []` en lo nuevo.
- **No cambiar ids** existentes ni los ids de `REVISION-ETAPA7.json`.
- **No borrar fuentes**: al reescribir un elemento con `refs`, se copian sus `refs` y se conservan sus marcas `[n]`.
- **No bajar una ★ por falta de enlaces** (D3): se anota la excepción.
- **No tocar lo `parte-III`.**
- Todo lo retirado va a `RESERVA-FASE-B.json`, nunca se borra sin dejar copia.
- Registrar cada desviación en `PENDIENTES-FUENTES.md` y en el punto de `CAMBIOS-PENDIENTES.md` de la entrega.

## 10. Problemas previsibles
| Síntoma | Causa probable | Qué hacer |
|---|---|---|
| `apply_new.py` rechaza un archivo | Validación fallida o id repetido | Correr `validate_out.py` sobre ese archivo y corregir; un id repetido suele ser una ficha que ya repuso `ajustes_etapa7.py`. |
| Build: «link … unknown item» | Se aplicó un contexto antes que sus obras, o la obra se descartó | Aplicar todos los lotes del paso; si se descartó, quitar el enlace y anotarlo. |
| Build: «year … outside the life of …» | Obra posterior a la muerte del diseñador | Si es una obra póstuma real, `posthumous: true` y explicarlo en el texto; si no, revisar el año. |
| Build: «designer … level essential but no work …» | La obra ★ que lo sostenía no existe | Ver 7.1: dejar el diseñador en Completo y anotarlo. |
| Una prueba falla por un número | Cambió el conteo | Ajustar la prueba (C6) y anotarlo en `PROJECT.md`. |
| `ajustes_etapa7.py` da cifras distintas a las esperadas | Alguien editó `src-data/` antes | Revisar el informe línea por línea; si hay dudas, no aplicar y avisar. |

## 11. Lista de cierre de la etapa 7
- [x] 7.4 aplicado (v47); build OK; pruebas OK; retiros anotados.
- [x] 7.5 fichas nuevas aplicadas (v50); `relaciones` aplicado; descartes anotados.
- [x] 7.6 enlaces D3 y textos aplicados (v51); excepciones C4c anotadas una por una.
- [x] 7.7 niveles aplicados (v52; queda 4 movimientos ★ sin obra ★, decisión pendiente); `check_etapa7.py --estricto` sin casos en 2 y 5; «Acerca de» con la subsección D8; pruebas, contraste, capturas y rendimiento.
- [x] 7.8 ZIP (v52), resumen, `ESTADO-ACTUAL.md`, `PROJECT.md`, `CAMBIOS-PENDIENTES.md`; casillas marcadas en el plan.
