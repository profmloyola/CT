# CONTINUAR — instrucciones para una sesión nueva (v77)

> **Plan vigente: `tools/PLAN-V1.md`** (cierre de la versión pública «LHD v1.0»; reemplaza las secciones 11 a 14 de `PLAN-CIERRE.md`). **R2.0 (herramientas) está hecha en v76. Lo siguiente es R2.1 (19 movimientos, 18 instituciones y 28 teorías ★), pero solo cuando Mauricio diga explícitamente «implementa» / «sigue con R2.1».** El ciclo de tanda, las reglas y las plantillas de abajo valen para toda la R2.

## Estado (6 oct 2026, v76)
- Parte I cerrada; R1 hecha; R2.0 hecha; R2.1 en adelante sin empezar.
- Pendientes de la R2 (medidos con `python3 tools/pipeline/auditoria.py --v1`, que da 0 cuando la R2 está terminada): movimientos ★ 19, instituciones ★ 18, teorías ★ 28, contextos 152, productivos 52, ensayos 10, enlaces de fichas ★ 359, conexiones de fichas ★ 72, obras ★ con una sola fuente 7 (no son las 7 de «fuentes débiles» de la R2.5: ver abajo), incidencias abiertas 717.
- **Calendario de incidencias (decisión de Mauricio, 6 oct): las revisa todas en la R2.6.** No enviar hojas en los checkpoints de R2.1 a R2.5 salvo que las pida; solo acumular con `r2_incidencias.py`.
- Hoja de incidencias: el bloque 1 (40 filas: 4 de clase A, 24 de B, 12 de D) está curado y enviado a Mauricio; **nada está decidido ni aprobado**. Solo la clase A trae «Aceptar» por defecto (y solo con una corrección concreta).
- Límite semanal de la cuenta: se reinicia el 8 oct, 22:00 (America/Santiago). Si los agentes devuelven "limit reached", NO inventar: reencolar.
- Checkpoint con ZIP **cada 2 tandas** (`?v=NN`, `ESTADO-ACTUAL.md`, `CAMBIOS-PENDIENTES.md`, `empaquetar.sh`, SendUserFile). Próximo punto de `CAMBIOS-PENDIENTES.md`: 104.

## Herramientas (R2.0)
| Herramienta | Qué hace |
|---|---|
| `prep_r2.py TIPO TANDA [--n] [--lotes] [--dry]` | Arma los lotes `in_TANDA_k.json` y su `prompt_TANDA_k.txt`. Tipos: `obras`, `diseñadores`, `movimientos`, `instituciones`, `teorias`, `contextos`, `productivos`, `ensayos`, `enlaces`, `conexiones`. Salta lo ya asignado. Por omisión 8 por agente (enlaces y conexiones 15; ensayos 2). `--plantillas` imprime las plantillas; `--doc` las escribe aquí. |
| `check_r2.py [--con-fuentes] salida.json …` | Valida las salidas de los agentes antes de aplicarlas (todos los tipos; ver su docstring). Código 1 si hay ERROR. |
| `apply2.py [--dry] salida.json …` | Aplica a `src-data/` y `src-essays/`. Todo o nada. `drop` en un enlace o conexión **no borra**: queda como DROP-PROPUESTO y va a incidencias. |
| `auditoria.py --v1 [-v] [--json F]` | La definición de terminado de la R2 (14 categorías); código 1 mientras quede algo. |
| `r2_incidencias.py` | Reúne los `issues` de las salidas en `tools/r2_incidencias.json` (fuente de verdad; clases A a E) y regenera `tools/R2-INCIDENCIAS.md`. Idempotente: no pisa la curaduría. |
| `incidencias_xlsx.py export\|import\|cerrar\|resumen` | Hoja `.xlsx` por bloques (`export OUT.xlsx --siguiente --n 40`), lectura de las decisiones de Mauricio (`import`) y cierre en bloque de una clase (`cerrar C`, solo con su visto bueno). `import` no aplica nada a los datos: eso es la R2.6. |

Sitio: los ensayos ya muestran las marcas `[n]` como superíndices y una sección «Fuentes del ensayo (n)» cerrada al abrir (`test_ensayos_fuentes.py`); el build exige marcas con fuente, iguales en EN y ES y fuera de los `[[id|texto]]`.

## Ciclo de una tanda (desde la carpeta `lhd` del proyecto descomprimido)
1. `python3 tools/pipeline/prep_r2.py TIPO tNN [--n 8] [--lotes 3]` (crea `in_tNN_k.json` y `prompt_tNN_k.txt` en `tools/pipeline/r2_work/`).
2. Lanzar 3 agentes Sonnet (`general-purpose`, `model: "sonnet"`), uno por lote, con el contenido de su `prompt_tNN_k.txt`; cada uno escribe su `out_tNN_k.json` (nombre único).
3. `python3 tools/pipeline/check_r2.py tools/pipeline/r2_work/out_tNN_*.json`; corregir los ERROR (a mano o devolviendo el lote al agente).
4. `python3 tools/pipeline/apply2.py [--dry] tools/pipeline/r2_work/out_tNN_*.json` (primero `--dry`, después sin él).
5. `python3 tools/build_data.py` → «OK: no PROBLEM».
6. `python3 tools/pipeline/r2_incidencias.py` (agrega las incidencias nuevas al JSON y al `.md`).
7. Borrar `r2_work/in_tNN_*.json` y `prompt_tNN_*.txt` (también tras tandas fallidas, para reencolar).
8. Cada 2 tandas, checkpoint: `python3 tools/pipeline/auditoria.py --v1`, anotar en `tools/CAMBIOS-PENDIENTES.md`, actualizar `ESTADO-ACTUAL.md`, subir versión (`?v=NN`) y `OUT=/mnt/user-data/outputs sh tools/empaquetar.sh NN`, SendUserFile.

Hoja de incidencias (R2.6, por bloques): `python3 tools/pipeline/incidencias_xlsx.py export SALIDA.xlsx --siguiente --n 40` → Mauricio decide en la hoja → `incidencias_xlsx.py import ENTRADA.xlsx` → (R2.6) aplicar los cambios, build y estado `aplicada`. La clase automática de una incidencia es un filtro por palabras clave: **hay que revisarla a mano antes de enviar cada bloque** (propuesta y recomendación salen del texto de la incidencia y de lo que dicen las fuentes; si no hay base para cambiar, la propuesta es «Mantener»).

## Reglas
1. Máximo 3 agentes en paralelo (Sonnet, `general-purpose`), 8 fichas por agente (15 enlaces o conexiones; 2 ensayos). Avanzar por tandas.
2. Sin Wikipedia ni wikis, blogs o tiendas como fuente. Sin URL inventadas ni con «:443» ni con espacios. Cada marca [n] tiene su ref; EN y ES llevan las mismas marcas. Fuente de fabricante o revista: marcada con ⚠.
3. No cambiar datos de ficha dudosos: anotarlos en `issues` (van a `tools/r2_incidencias.json` y a la hoja `.xlsx`).
4. Diseñadores: `short` y `name` no se traducen (en `es` solo `key`, `more`, `dates`). Obras y demás tipos sí llevan `es`.
5. Fecha en refs: la de hoy (AAAA-MM-DD).
6. No usar `validate_out.py` en R2. Control = `check_r2.py` + `apply2.py` + build sin PROBLEM + `r2_incidencias.py`.
7. Nada se marca como aprobado sin el visto bueno de Mauricio; si se alcanza un límite, se aplica lo que salió bien, se entrega el ZIP y lo pendiente se reencola.

## Plantillas de prompt por tipo
Se rellenan solas en `prompt_tNN_k.txt` (el agente recibe ese archivo). Fuente única: `tools/pipeline/plantillas_r2.json`; esta sección se regenera con `python3 tools/pipeline/prep_r2.py --doc` y una prueba comprueba que coincide.

<!-- PLANTILLAS:INICIO (generado por prep_r2.py --doc; no editar a mano) -->

### Plantilla: `obras`

```
Eres investigador del proyecto LHD (Línea de Historia del Diseño). Lee tools/pipeline/r2_work/in_<tanda>_<k>.json (<n> obras ★). Para cada obra verifica con fuentes la ficha (fechas, autoría, lugar, técnica, hechos del texto) y reescribe `key` y `more` con marcas [n]; 2 a 3 fuentes por obra, una al menos institucional.

Formato de salida: Lista de objetos {"id","en":{"key","more"},"es":{"key","more"},"refs":[…],"other":{},"issues":[]} (sin `rtype`). `key` ≤ 230 caracteres sin contar las marcas.

Reglas:
1. Busca en la web fuentes primarias o de alta calidad (museos, archivos, universidades, editoriales académicas, Britannica, fundaciones, instituciones oficiales). NO uses Wikipedia, wikis (Fandom, Wikiwand, Grokipedia…), blogs ni tiendas. Una fuente de fabricante o de revista se acepta solo si no hay otra y se marca con ⚠ al comienzo de `checks`.
2. Usa únicamente URL que hayas abierto tú y que sustenten la afirmación: nunca adivinadas, sin «:443» ni espacios. Fecha de cada fuente: la de hoy (<AAAA-MM-DD>, formato AAAA-MM-DD).
3. Cada marca [n] del texto corresponde a refs[n-1]; EN y ES llevan exactamente las mismas marcas; toda fuente de `refs` se cita al menos una vez. La marca va después del signo de puntuación (…texto.[1]) y fuera de los corchetes dobles [[id|texto]].
4. Cada ref es {"label","url","checks","date"}: `label` = institución y título de la página; `checks` = qué afirmaciones concretas sostiene (cifras, fechas, nombres).
5. Lo que ninguna fuente abierta sostenga se quita o se suaviza, y lo anotas en `issues` (una línea por cambio). Nunca inventes datos ni fuentes.
6. Si un dato de la ficha parece erróneo o dudoso (fechas, autoría, material, cliente, estado, país…) NO lo cambies: descríbelo en `issues` con las fuentes que lo contradicen o lo dudan y su valor corregido, si lo hay. `other` queda vacío salvo instrucción expresa.
7. Si se agotan las búsquedas o el límite de la sesión, deja fuera el registro que no alcances a completar y dilo al final; no lo rellenes con datos sin fuente.
8. Escribe el resultado en tools/pipeline/r2_work/out_<tanda>_<k>.json (nombre único; nunca reutilices el de otra salida) y, si puedes, corre `cd tools/pipeline && python3 check_r2.py r2_work/out_<tanda>_<k>.json` y corrige los ERROR. No uses validate_out.py. Al final informa cuántos registros completaste y cuáles quedaron fuera.
```

### Plantilla: `diseñadores`

```
Eres investigador del proyecto LHD (Línea de Historia del Diseño). Lee tools/pipeline/r2_work/in_<tanda>_<k>.json (<n> diseñadores ★). Para cada diseñador confirma fechas de vida, país y obra principal y reescribe `key` y `more` con marcas [n]; 2 a 3 fuentes, una al menos institucional o enciclopédica de calidad (Britannica, museo, fundación).

Formato de salida: Lista de objetos {"id","en":{"key","more"[,"dates"]},"es":{mismos campos},"refs":[…],"other":{},"issues":[]}. `name` y `short` no se traducen ni se tocan; `dates` solo si una fuente corrige las fechas de vida y se anota en `issues`.

Reglas:
1. Busca en la web fuentes primarias o de alta calidad (museos, archivos, universidades, editoriales académicas, Britannica, fundaciones, instituciones oficiales). NO uses Wikipedia, wikis (Fandom, Wikiwand, Grokipedia…), blogs ni tiendas. Una fuente de fabricante o de revista se acepta solo si no hay otra y se marca con ⚠ al comienzo de `checks`.
2. Usa únicamente URL que hayas abierto tú y que sustenten la afirmación: nunca adivinadas, sin «:443» ni espacios. Fecha de cada fuente: la de hoy (<AAAA-MM-DD>, formato AAAA-MM-DD).
3. Cada marca [n] del texto corresponde a refs[n-1]; EN y ES llevan exactamente las mismas marcas; toda fuente de `refs` se cita al menos una vez. La marca va después del signo de puntuación (…texto.[1]) y fuera de los corchetes dobles [[id|texto]].
4. Cada ref es {"label","url","checks","date"}: `label` = institución y título de la página; `checks` = qué afirmaciones concretas sostiene (cifras, fechas, nombres).
5. Lo que ninguna fuente abierta sostenga se quita o se suaviza, y lo anotas en `issues` (una línea por cambio). Nunca inventes datos ni fuentes.
6. Si un dato de la ficha parece erróneo o dudoso (fechas, autoría, material, cliente, estado, país…) NO lo cambies: descríbelo en `issues` con las fuentes que lo contradicen o lo dudan y su valor corregido, si lo hay. `other` queda vacío salvo instrucción expresa.
7. Si se agotan las búsquedas o el límite de la sesión, deja fuera el registro que no alcances a completar y dilo al final; no lo rellenes con datos sin fuente.
8. Escribe el resultado en tools/pipeline/r2_work/out_<tanda>_<k>.json (nombre único; nunca reutilices el de otra salida) y, si puedes, corre `cd tools/pipeline && python3 check_r2.py r2_work/out_<tanda>_<k>.json` y corrige los ERROR. No uses validate_out.py. Al final informa cuántos registros completaste y cuáles quedaron fuera.
```

### Plantilla: `movimientos`

```
Eres investigador del proyecto LHD (Línea de Historia del Diseño). Lee tools/pipeline/r2_work/in_<tanda>_<k>.json (<n> movimientos ★). Para cada movimiento verifica con fuentes sus rasgos, su contexto y el cambio que introdujo, y reescribe `key`, `traits`, `context` y `shift` con marcas [n]; 3 a 4 fuentes (al menos una académica o de museo). Modelo de formato: `macro-modernism` en data/all.json.

Formato de salida: Lista de objetos {"id","en":{"key","traits":[…],"context","shift"},"es":{mismos campos},"refs":[…],"other":{},"issues":[]}. `traits` es una lista; cada elemento puede llevar marcas. No incluyas `name` ni `short`.

Reglas:
1. Busca en la web fuentes primarias o de alta calidad (museos, archivos, universidades, editoriales académicas, Britannica, fundaciones, instituciones oficiales). NO uses Wikipedia, wikis (Fandom, Wikiwand, Grokipedia…), blogs ni tiendas. Una fuente de fabricante o de revista se acepta solo si no hay otra y se marca con ⚠ al comienzo de `checks`.
2. Usa únicamente URL que hayas abierto tú y que sustenten la afirmación: nunca adivinadas, sin «:443» ni espacios. Fecha de cada fuente: la de hoy (<AAAA-MM-DD>, formato AAAA-MM-DD).
3. Cada marca [n] del texto corresponde a refs[n-1]; EN y ES llevan exactamente las mismas marcas; toda fuente de `refs` se cita al menos una vez. La marca va después del signo de puntuación (…texto.[1]) y fuera de los corchetes dobles [[id|texto]].
4. Cada ref es {"label","url","checks","date"}: `label` = institución y título de la página; `checks` = qué afirmaciones concretas sostiene (cifras, fechas, nombres).
5. Lo que ninguna fuente abierta sostenga se quita o se suaviza, y lo anotas en `issues` (una línea por cambio). Nunca inventes datos ni fuentes.
6. Si un dato de la ficha parece erróneo o dudoso (fechas, autoría, material, cliente, estado, país…) NO lo cambies: descríbelo en `issues` con las fuentes que lo contradicen o lo dudan y su valor corregido, si lo hay. `other` queda vacío salvo instrucción expresa.
7. Si se agotan las búsquedas o el límite de la sesión, deja fuera el registro que no alcances a completar y dilo al final; no lo rellenes con datos sin fuente.
8. Escribe el resultado en tools/pipeline/r2_work/out_<tanda>_<k>.json (nombre único; nunca reutilices el de otra salida) y, si puedes, corre `cd tools/pipeline && python3 check_r2.py r2_work/out_<tanda>_<k>.json` y corrige los ERROR. No uses validate_out.py. Al final informa cuántos registros completaste y cuáles quedaron fuera.
```

### Plantilla: `instituciones`

```
Eres investigador del proyecto LHD (Línea de Historia del Diseño). Lee tools/pipeline/r2_work/in_<tanda>_<k>.json (<n> instituciones ★). Para cada institución verifica fundación, lugar, fundadores y papel en la historia del diseño (sitio oficial o archivo propio sirve para fechas y datos internos; para su importancia usa una fuente externa), y reescribe `key` y `more` con marcas [n]; 2 a 3 fuentes.

Formato de salida: Lista de objetos {"id","en":{"key","more"},"es":{"key","more"},"refs":[…],"other":{},"issues":[]}.

Reglas:
1. Busca en la web fuentes primarias o de alta calidad (museos, archivos, universidades, editoriales académicas, Britannica, fundaciones, instituciones oficiales). NO uses Wikipedia, wikis (Fandom, Wikiwand, Grokipedia…), blogs ni tiendas. Una fuente de fabricante o de revista se acepta solo si no hay otra y se marca con ⚠ al comienzo de `checks`.
2. Usa únicamente URL que hayas abierto tú y que sustenten la afirmación: nunca adivinadas, sin «:443» ni espacios. Fecha de cada fuente: la de hoy (<AAAA-MM-DD>, formato AAAA-MM-DD).
3. Cada marca [n] del texto corresponde a refs[n-1]; EN y ES llevan exactamente las mismas marcas; toda fuente de `refs` se cita al menos una vez. La marca va después del signo de puntuación (…texto.[1]) y fuera de los corchetes dobles [[id|texto]].
4. Cada ref es {"label","url","checks","date"}: `label` = institución y título de la página; `checks` = qué afirmaciones concretas sostiene (cifras, fechas, nombres).
5. Lo que ninguna fuente abierta sostenga se quita o se suaviza, y lo anotas en `issues` (una línea por cambio). Nunca inventes datos ni fuentes.
6. Si un dato de la ficha parece erróneo o dudoso (fechas, autoría, material, cliente, estado, país…) NO lo cambies: descríbelo en `issues` con las fuentes que lo contradicen o lo dudan y su valor corregido, si lo hay. `other` queda vacío salvo instrucción expresa.
7. Si se agotan las búsquedas o el límite de la sesión, deja fuera el registro que no alcances a completar y dilo al final; no lo rellenes con datos sin fuente.
8. Escribe el resultado en tools/pipeline/r2_work/out_<tanda>_<k>.json (nombre único; nunca reutilices el de otra salida) y, si puedes, corre `cd tools/pipeline && python3 check_r2.py r2_work/out_<tanda>_<k>.json` y corrige los ERROR. No uses validate_out.py. Al final informa cuántos registros completaste y cuáles quedaron fuera.
```

### Plantilla: `teorias`

```
Eres investigador del proyecto LHD (Línea de Historia del Diseño). Lee tools/pipeline/r2_work/in_<tanda>_<k>.json (<n> teorías ★ (textos teóricos)). Para cada teoría verifica autor, fecha, lugar y contenido: si existe el texto original digitalizado (archivo, biblioteca digital, Internet Archive de una institución, Project Gutenberg), úsalo como una de las fuentes y contrasta `ideas` y `impact` con él. Reescribe `key`, `ideas` y `impact` con marcas [n]; 2 a 3 fuentes.

Formato de salida: Lista de objetos {"id","en":{"key","ideas":[…],"impact"},"es":{mismos campos},"refs":[…],"other":{},"issues":[]}. `ideas` es una lista (4 a 6 ideas); no incluyas `name`, `short` ni `author`.

Reglas:
1. Busca en la web fuentes primarias o de alta calidad (museos, archivos, universidades, editoriales académicas, Britannica, fundaciones, instituciones oficiales). NO uses Wikipedia, wikis (Fandom, Wikiwand, Grokipedia…), blogs ni tiendas. Una fuente de fabricante o de revista se acepta solo si no hay otra y se marca con ⚠ al comienzo de `checks`.
2. Usa únicamente URL que hayas abierto tú y que sustenten la afirmación: nunca adivinadas, sin «:443» ni espacios. Fecha de cada fuente: la de hoy (<AAAA-MM-DD>, formato AAAA-MM-DD).
3. Cada marca [n] del texto corresponde a refs[n-1]; EN y ES llevan exactamente las mismas marcas; toda fuente de `refs` se cita al menos una vez. La marca va después del signo de puntuación (…texto.[1]) y fuera de los corchetes dobles [[id|texto]].
4. Cada ref es {"label","url","checks","date"}: `label` = institución y título de la página; `checks` = qué afirmaciones concretas sostiene (cifras, fechas, nombres).
5. Lo que ninguna fuente abierta sostenga se quita o se suaviza, y lo anotas en `issues` (una línea por cambio). Nunca inventes datos ni fuentes.
6. Si un dato de la ficha parece erróneo o dudoso (fechas, autoría, material, cliente, estado, país…) NO lo cambies: descríbelo en `issues` con las fuentes que lo contradicen o lo dudan y su valor corregido, si lo hay. `other` queda vacío salvo instrucción expresa.
7. Si se agotan las búsquedas o el límite de la sesión, deja fuera el registro que no alcances a completar y dilo al final; no lo rellenes con datos sin fuente.
8. Escribe el resultado en tools/pipeline/r2_work/out_<tanda>_<k>.json (nombre único; nunca reutilices el de otra salida) y, si puedes, corre `cd tools/pipeline && python3 check_r2.py r2_work/out_<tanda>_<k>.json` y corrige los ERROR. No uses validate_out.py. Al final informa cuántos registros completaste y cuáles quedaron fuera.
```

### Plantilla: `contextos`

```
Eres investigador del proyecto LHD (Línea de Historia del Diseño). Lee tools/pipeline/r2_work/in_<tanda>_<k>.json (<n> hechos de contexto). Para cada hecho de contexto verifica cifras, fechas, nombres y lugares, y reescribe `key`, `happened` y `effect` con marcas [n] en cada cifra, fecha o nombre; 2 a 3 fuentes. `effect` explica qué cambió para el diseño y no pasa de 480 caracteres.

Formato de salida: Lista de objetos {"id","en":{"key","happened","effect"},"es":{mismos campos},"refs":[…],"other":{},"issues":[]}.

Reglas:
1. Busca en la web fuentes primarias o de alta calidad (museos, archivos, universidades, editoriales académicas, Britannica, fundaciones, instituciones oficiales). NO uses Wikipedia, wikis (Fandom, Wikiwand, Grokipedia…), blogs ni tiendas. Una fuente de fabricante o de revista se acepta solo si no hay otra y se marca con ⚠ al comienzo de `checks`.
2. Usa únicamente URL que hayas abierto tú y que sustenten la afirmación: nunca adivinadas, sin «:443» ni espacios. Fecha de cada fuente: la de hoy (<AAAA-MM-DD>, formato AAAA-MM-DD).
3. Cada marca [n] del texto corresponde a refs[n-1]; EN y ES llevan exactamente las mismas marcas; toda fuente de `refs` se cita al menos una vez. La marca va después del signo de puntuación (…texto.[1]) y fuera de los corchetes dobles [[id|texto]].
4. Cada ref es {"label","url","checks","date"}: `label` = institución y título de la página; `checks` = qué afirmaciones concretas sostiene (cifras, fechas, nombres).
5. Lo que ninguna fuente abierta sostenga se quita o se suaviza, y lo anotas en `issues` (una línea por cambio). Nunca inventes datos ni fuentes.
6. Si un dato de la ficha parece erróneo o dudoso (fechas, autoría, material, cliente, estado, país…) NO lo cambies: descríbelo en `issues` con las fuentes que lo contradicen o lo dudan y su valor corregido, si lo hay. `other` queda vacío salvo instrucción expresa.
7. Si se agotan las búsquedas o el límite de la sesión, deja fuera el registro que no alcances a completar y dilo al final; no lo rellenes con datos sin fuente.
8. Escribe el resultado en tools/pipeline/r2_work/out_<tanda>_<k>.json (nombre único; nunca reutilices el de otra salida) y, si puedes, corre `cd tools/pipeline && python3 check_r2.py r2_work/out_<tanda>_<k>.json` y corrige los ERROR. No uses validate_out.py. Al final informa cuántos registros completaste y cuáles quedaron fuera.
```

### Plantilla: `productivos`

```
Eres investigador del proyecto LHD (Línea de Historia del Diseño). Lee tools/pipeline/r2_work/in_<tanda>_<k>.json (<n> elementos productivos (materiales, procesos, herramientas)). Para cada elemento productivo verifica origen, fechas, inventores, lugares y cifras, y reescribe `key`, `origin`, `enabled`, `change` (y `economy` y `relations` si existen) con marcas [n]; 2 a 3 fuentes.

Formato de salida: Lista de objetos {"id","en":{"key","origin","enabled","change"[,"economy","relations"]},"es":{mismos campos},"refs":[…],"other":{},"issues":[]}. Incluye `economy` y `relations` solo si el elemento los tiene.

Reglas:
1. Busca en la web fuentes primarias o de alta calidad (museos, archivos, universidades, editoriales académicas, Britannica, fundaciones, instituciones oficiales). NO uses Wikipedia, wikis (Fandom, Wikiwand, Grokipedia…), blogs ni tiendas. Una fuente de fabricante o de revista se acepta solo si no hay otra y se marca con ⚠ al comienzo de `checks`.
2. Usa únicamente URL que hayas abierto tú y que sustenten la afirmación: nunca adivinadas, sin «:443» ni espacios. Fecha de cada fuente: la de hoy (<AAAA-MM-DD>, formato AAAA-MM-DD).
3. Cada marca [n] del texto corresponde a refs[n-1]; EN y ES llevan exactamente las mismas marcas; toda fuente de `refs` se cita al menos una vez. La marca va después del signo de puntuación (…texto.[1]) y fuera de los corchetes dobles [[id|texto]].
4. Cada ref es {"label","url","checks","date"}: `label` = institución y título de la página; `checks` = qué afirmaciones concretas sostiene (cifras, fechas, nombres).
5. Lo que ninguna fuente abierta sostenga se quita o se suaviza, y lo anotas en `issues` (una línea por cambio). Nunca inventes datos ni fuentes.
6. Si un dato de la ficha parece erróneo o dudoso (fechas, autoría, material, cliente, estado, país…) NO lo cambies: descríbelo en `issues` con las fuentes que lo contradicen o lo dudan y su valor corregido, si lo hay. `other` queda vacío salvo instrucción expresa.
7. Si se agotan las búsquedas o el límite de la sesión, deja fuera el registro que no alcances a completar y dilo al final; no lo rellenes con datos sin fuente.
8. Escribe el resultado en tools/pipeline/r2_work/out_<tanda>_<k>.json (nombre único; nunca reutilices el de otra salida) y, si puedes, corre `cd tools/pipeline && python3 check_r2.py r2_work/out_<tanda>_<k>.json` y corrige los ERROR. No uses validate_out.py. Al final informa cuántos registros completaste y cuáles quedaron fuera.
```

### Plantilla: `ensayos`

```
Eres investigador del proyecto LHD (Línea de Historia del Diseño). Lee tools/pipeline/r2_work/in_<tanda>_<k>.json (<n> ensayos). Verifica cada afirmación de hecho que el propio ensayo hace (fechas, nombres, cifras, causas, atribuciones) y pon marcas [n] con su lista `refs`. NO revises las fichas que el ensayo cita con [[id|texto]]: eso no es parte de esta tarea. Lo que no se sostenga se quita o se suaviza y se anota en `issues`; no agregues afirmaciones nuevas sin fuente. El texto del ensayo es un conjunto de párrafos independientes.

Formato de salida: Lista de objetos {"id","en":{"paras":[…]},"es":{"paras":[…]},"refs":[…],"issues":[]}. `paras` conserva el orden y el número de párrafos del original (EN y ES igual número); los enlaces [[id|texto]] y [[id]] se conservan idénticos en EN y ES (mismo id en el mismo párrafo) y las marcas [n] van fuera de ellos. Un solo `refs` por ensayo, numerado de corrido en todo el texto. No cambies `title` ni `subtitle`.

Reglas:
1. Busca en la web fuentes primarias o de alta calidad (museos, archivos, universidades, editoriales académicas, Britannica, fundaciones, instituciones oficiales). NO uses Wikipedia, wikis (Fandom, Wikiwand, Grokipedia…), blogs ni tiendas. Una fuente de fabricante o de revista se acepta solo si no hay otra y se marca con ⚠ al comienzo de `checks`.
2. Usa únicamente URL que hayas abierto tú y que sustenten la afirmación: nunca adivinadas, sin «:443» ni espacios. Fecha de cada fuente: la de hoy (<AAAA-MM-DD>, formato AAAA-MM-DD).
3. Cada marca [n] del texto corresponde a refs[n-1]; EN y ES llevan exactamente las mismas marcas; toda fuente de `refs` se cita al menos una vez. La marca va después del signo de puntuación (…texto.[1]) y fuera de los corchetes dobles [[id|texto]].
4. Cada ref es {"label","url","checks","date"}: `label` = institución y título de la página; `checks` = qué afirmaciones concretas sostiene (cifras, fechas, nombres).
5. Lo que ninguna fuente abierta sostenga se quita o se suaviza, y lo anotas en `issues` (una línea por cambio). Nunca inventes datos ni fuentes.
6. Si un dato de la ficha parece erróneo o dudoso (fechas, autoría, material, cliente, estado, país…) NO lo cambies: descríbelo en `issues` con las fuentes que lo contradicen o lo dudan y su valor corregido, si lo hay. `other` queda vacío salvo instrucción expresa.
7. Si se agotan las búsquedas o el límite de la sesión, deja fuera el registro que no alcances a completar y dilo al final; no lo rellenes con datos sin fuente.
8. Escribe el resultado en tools/pipeline/r2_work/out_<tanda>_<k>.json (nombre único; nunca reutilices el de otra salida) y, si puedes, corre `cd tools/pipeline && python3 check_r2.py r2_work/out_<tanda>_<k>.json` y corrige los ERROR. No uses validate_out.py. Al final informa cuántos registros completaste y cuáles quedaron fuera.
```

### Plantilla: `enlaces`

```
Eres investigador del proyecto LHD (Línea de Historia del Diseño). Lee tools/pipeline/r2_work/in_<tanda>_<k>.json (<n> enlaces de contexto de fichas ★). Cada enlace dice que un hecho de contexto (`ctx`) llevó a una decisión o rasgo de una ficha de diseño (`item`) y da el mecanismo en `note`. Encuentra una fuente que sostenga EL MECANISMO (qué cambió en el contexto → qué cambió en el diseño), no solo cada extremo por separado. Reescribe `note` con marcas [n] (≤ 240 caracteres sin marcas).

Formato de salida: Lista de objetos {"ctx","item","en":{"note"},"es":{"note"},"refs":[…],"issues":[]}. Si ninguna fuente sostiene el mecanismo ni siquiera de forma suavizada, usa en cambio {"ctx","item","drop":true,"issues":["motivo y qué fuentes consultaste"]}: el enlace NO se borra, solo se propone quitarlo en la hoja de incidencias. Los campos `ctx_*` e `item_*` del lote son solo contexto para ti: no los devuelvas.

Reglas:
1. Busca en la web fuentes primarias o de alta calidad (museos, archivos, universidades, editoriales académicas, Britannica, fundaciones, instituciones oficiales). NO uses Wikipedia, wikis (Fandom, Wikiwand, Grokipedia…), blogs ni tiendas. Una fuente de fabricante o de revista se acepta solo si no hay otra y se marca con ⚠ al comienzo de `checks`.
2. Usa únicamente URL que hayas abierto tú y que sustenten la afirmación: nunca adivinadas, sin «:443» ni espacios. Fecha de cada fuente: la de hoy (<AAAA-MM-DD>, formato AAAA-MM-DD).
3. Cada marca [n] del texto corresponde a refs[n-1]; EN y ES llevan exactamente las mismas marcas; toda fuente de `refs` se cita al menos una vez. La marca va después del signo de puntuación (…texto.[1]) y fuera de los corchetes dobles [[id|texto]].
4. Cada ref es {"label","url","checks","date"}: `label` = institución y título de la página; `checks` = qué afirmaciones concretas sostiene (cifras, fechas, nombres).
5. Lo que ninguna fuente abierta sostenga se quita o se suaviza, y lo anotas en `issues` (una línea por cambio). Nunca inventes datos ni fuentes.
6. Si un dato de la ficha parece erróneo o dudoso (fechas, autoría, material, cliente, estado, país…) NO lo cambies: descríbelo en `issues` con las fuentes que lo contradicen o lo dudan y su valor corregido, si lo hay. `other` queda vacío salvo instrucción expresa.
7. Si se agotan las búsquedas o el límite de la sesión, deja fuera el registro que no alcances a completar y dilo al final; no lo rellenes con datos sin fuente.
8. Escribe el resultado en tools/pipeline/r2_work/out_<tanda>_<k>.json (nombre único; nunca reutilices el de otra salida) y, si puedes, corre `cd tools/pipeline && python3 check_r2.py r2_work/out_<tanda>_<k>.json` y corrige los ERROR. No uses validate_out.py. Al final informa cuántos registros completaste y cuáles quedaron fuera.
```

### Plantilla: `conexiones`

```
Eres investigador del proyecto LHD (Línea de Historia del Diseño). Lee tools/pipeline/r2_work/in_<tanda>_<k>.json (<n> conexiones de fichas ★). Cada conexión dice que el elemento `from` influyó en el elemento `to` y da el mecanismo en `note`. Encuentra una fuente que sostenga EL MECANISMO (la influencia o la transmisión, no solo cada extremo por separado). Reescribe `note` con marcas [n] (≤ 240 caracteres sin marcas).

Formato de salida: Lista de objetos {"from","to","en":{"note"},"es":{"note"},"refs":[…],"issues":[]}. Si ninguna fuente sostiene la conexión ni siquiera suavizada, usa {"from","to","drop":true,"issues":["motivo y qué fuentes consultaste"]}: la conexión NO se borra, solo se propone quitarla en la hoja de incidencias. Los campos `from_*` y `to_*` del lote son solo contexto: no los devuelvas.

Reglas:
1. Busca en la web fuentes primarias o de alta calidad (museos, archivos, universidades, editoriales académicas, Britannica, fundaciones, instituciones oficiales). NO uses Wikipedia, wikis (Fandom, Wikiwand, Grokipedia…), blogs ni tiendas. Una fuente de fabricante o de revista se acepta solo si no hay otra y se marca con ⚠ al comienzo de `checks`.
2. Usa únicamente URL que hayas abierto tú y que sustenten la afirmación: nunca adivinadas, sin «:443» ni espacios. Fecha de cada fuente: la de hoy (<AAAA-MM-DD>, formato AAAA-MM-DD).
3. Cada marca [n] del texto corresponde a refs[n-1]; EN y ES llevan exactamente las mismas marcas; toda fuente de `refs` se cita al menos una vez. La marca va después del signo de puntuación (…texto.[1]) y fuera de los corchetes dobles [[id|texto]].
4. Cada ref es {"label","url","checks","date"}: `label` = institución y título de la página; `checks` = qué afirmaciones concretas sostiene (cifras, fechas, nombres).
5. Lo que ninguna fuente abierta sostenga se quita o se suaviza, y lo anotas en `issues` (una línea por cambio). Nunca inventes datos ni fuentes.
6. Si un dato de la ficha parece erróneo o dudoso (fechas, autoría, material, cliente, estado, país…) NO lo cambies: descríbelo en `issues` con las fuentes que lo contradicen o lo dudan y su valor corregido, si lo hay. `other` queda vacío salvo instrucción expresa.
7. Si se agotan las búsquedas o el límite de la sesión, deja fuera el registro que no alcances a completar y dilo al final; no lo rellenes con datos sin fuente.
8. Escribe el resultado en tools/pipeline/r2_work/out_<tanda>_<k>.json (nombre único; nunca reutilices el de otra salida) y, si puedes, corre `cd tools/pipeline && python3 check_r2.py r2_work/out_<tanda>_<k>.json` y corrige los ERROR. No uses validate_out.py. Al final informa cuántos registros completaste y cuáles quedaron fuera.
```

<!-- PLANTILLAS:FIN -->

## Pendientes conocidos
- R2.5 (refuerzo de fuentes débiles): `seagram-building`, `think-small`, `cadillac-eldorado-1959`, `i-love-ny-1977`, `dvf-wrap-dress-1974`, `air-jordan-1-1985`, `beethoven-poster-1955`. Aparte, `auditoria.py --v1` lista 7 obras ★ con **una sola** fuente (otras): se refuerzan en R2.5 también.
- `levis-riveted-jeans` desconectado; `ctx-latam-centenaries-1910` con 1 enlace sin anotar; largos de `key` de conceptos y ref no citada de `streamlining` (R3, v1.1).
- Datos de ficha dudosos: `tools/r2_incidencias.json`; los de fichas ★ nombrados por el plan (R2.6): `dresser-teapot`, `citroen-2cv-1948`, `lc2-armchair-1928`, Pugin, Paxton, Etruria, tipografía de Múnich 72, `cadillac-eldorado-1959`, Guggenheim Bilbao (todos están en el bloque 1).
- Entorno: Playwright (Python) necesita `pip install playwright`; Chromium está en `/opt/pw-browsers/chromium` (variable `CHROMIUM` si cambia). No usar `pkill` (cierra la terminal).
