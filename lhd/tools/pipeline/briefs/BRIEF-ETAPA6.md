# Tarea: levantamiento y propuesta de la etapa 6 (complemento transversal; Parte I, sin fuentes)

Proyecto: Línea de Historia del Diseño (LHD), sitio bilingüe sobre historia del diseño de 1750 a hoy. Lee primero `tools/MANUAL-CONTENIDO.md` (secciones 3, 7 y 9.1) y la regla C4c de `tools/PLAN-CIERRE.md` (sección 1) y la sección 9b (etapa 6).

## Qué se busca
La línea tiene hoy 373 obras (gráfico, producto, moda, arquitectura) y debe llegar a **≥ 500 obras** con **todos los diseñadores y obras que sería razonable encontrar en un curso universitario de historia del diseño** (gráfico + producto + moda + arquitectura), de 1750 a hoy, más una **buena cobertura de los movimientos arquitectónicos de las últimas cuatro décadas** (desde ~1985) e instituciones/documentos relevantes (premios como el Pritzker, bienales, escuelas, museos, manifiestos, libros clave).
Tu tarea es **proponer solo lo que FALTA** en tu parte (no escribas las fichas completas todavía: es una propuesta para que Mauricio la apruebe).

## Qué ya existe (NO lo repitas ni cambies sus ids)
En `/tmp/claude-0/-home-claude/214f9bc1-c67a-5fde-964f-0f6f6a9a671e/scratchpad/e6/`: `inv_works.txt` (era|disciplina|id|título|año|nivel|diseñadores|región), `inv_designers.txt`, `inv_movement.txt`, `inv_institution.txt`, `inv_theory.txt`, `inv_context.txt`, `inv_production.txt`, `inv_concept.txt` (era|id|nombre|años|pista|nivel) y `reserva.txt` (candidatos ya pensados: parte de ahí cuando calcen). Antes de proponer algo, **búscalo ahí por nombre** (con grep; un mismo objeto puede estar con otro título). Obras por época hoy (gráfica/producto/moda/arquitectura): Industrial 10/9/4/7 · Reforma 14/17/8/21 · Modernismo 34/34/19/33 · Posguerra 24/30/12/24 · Posmoderno (1975–hoy) 21/22/13/17.

## Criterio de inclusión
«¿Se esperaría ver este elemento en un curso universitario de historia del diseño (o de arquitectura/moda) de nivel general?». Lo icónico y canónico primero; después lo que da cuerpo (otras regiones, mujeres, América Latina y Chile, ejemplos claros de un contexto que cambió el diseño). Reparte entre épocas según la importancia histórica; si una época está muy corta frente a su canon, dilo en `curso`. Elementos orientales solo con influencia demostrable en el diseño occidental (región `global`).
Sin web: escribe desde lo que sabes con **alta certeza** (C1): nombres, años y atribuciones famosas; si dudas de un dato, omite el elemento o márcalo `"duda": "..."`. Para lo posterior a 2010, solo hechos de los que haya certeza.

## Conexiones (regla C4c, relajada)
Todo elemento propuesto debe tener **al menos una conexión**, y ninguno puede quedar desconectado:
- `directo`: un enlace de contexto (`ctx` = id de un hecho de contexto existente en `inv_context.txt`, o uno NUEVO que tú propones) con el **mecanismo** en una línea (qué cambió en el contexto → qué decisión de diseño cambió). Una coincidencia de fechas NO es un enlace.
- `secundario`: el elemento se conecta por otro elemento que ya tiene enlace directo (`via` = id de su diseñador, movimiento, institución, productivo, o de otra obra), con una línea que lo explica. Puede tener solo secundarios.
- Las obras ★ deberían tener 2 directos de subcategorías distintas; si no, marca `"excepcion_C4c": "motivo"`.
- Puedes proponer **hechos de contexto nuevos** (rtype `context`) cuando enriquezcan el mapa (p. ej. algo que explique varias obras nuevas); deben explicar al menos 2 elementos.

## Formato de salida
Un archivo JSON (lista de registros; escríbelo con un script Python, `json.dump(..., ensure_ascii=False, indent=1)`), con estos campos. Ids únicos en minúsculas, en inglés, con año al final para obras (`slug-1927`); revisa que no existan en los `inv_*`.
- `{"rtype":"work","id","title" (en),"title_es","year","discipline":"graphic|product|fashion|architecture","designers":[ids existentes o nuevos],"regions":[...],"countries":["ISO"],"level":"essential|normal","curso":"por qué un curso lo incluye (1 línea, es)","links":[{"tipo":"directo","ctx":"...","mecanismo":"..."},{"tipo":"secundario","via":"...","mecanismo":"..."}], "reserva_origen":opcional,"duda":opcional,"excepcion_C4c":opcional}`
- `{"rtype":"designer","id","name","born","died" (o null),"disciplines":[...],"countries","regions","level","curso","links":[...]}`
- `{"rtype":"movement","id","name","name_es","start","end","disciplines","regions","level","curso","links":[...]}`
- `{"rtype":"institution","id","name","name_es","start","end","level","curso","links":[...]}` (los premios, bienales, escuelas y museos son instituciones)
- `{"rtype":"theory","id":"th-...","name","name_es","author","year","level","curso","links":[...]}` (manifiestos, cartas, libros clave)
- `{"rtype":"context","id":"ctx-...","name","name_es","track":"political|economic|social|cultural|technological","start","end","regions","level","curso","explica":[{"id":"...","mecanismo":"..."}]}`
Los niveles son `essential` (★, lo que un curso introductorio no puede omitir; ≈ 30 % de lo que propongas) o `normal`.
Los ids de diseñadores que uses en `designers` deben existir en `inv_designers.txt` o estar propuestos en tu mismo archivo.

## Al terminar
No edites archivos del proyecto. Responde con 6 líneas: cuántos elementos propones por tipo y época, cuáles te dejaron dudas y qué quedó fuera por falta de certeza.
