# Tarea: redactar los elementos aprobados de la etapa 7 (Parte I: sin fuentes)

Proyecto: Línea de Historia del Diseño (LHD). **Lee primero `tools/pipeline/briefs/BRIEF-ETAPA6-REDACCION.md`: todas sus reglas valen igual** (y, a través de él, `BRIEF-CONTENIDO.md` y `EJEMPLOS.md`). Esta tarea cambia solo lo que se indica abajo. Los elementos vienen de la revisión editorial externa (`tools/REVISION-EDITORIAL-ETAPA7.md`) aprobada por Mauricio en el V4.

## Hay tres tipos de lote

### 1. Lotes de fichas nuevas (`<tramo>_w<n>`, `_d<n>`, `_m<n>`, `_c<n>`)
Igual que en la etapa 6. Diferencias:
- **No copies a la salida** estos campos de la propuesta (además de los que ya excluye el brief de la etapa 6): `prioridad`, `estado`, `era`, `miembros`, `obras`, `anclas`, `nota`. Las pertenencias (`miembros` de un movimiento, `obras` de una institución, `anclas` de un productivo) las fija después un script; tú no tocas otras fichas.
- **`duda`:** el dato marcado no se afirma si no lo conoces con certeza. Escribe la frase sin él (por ejemplo, sin el año exacto o sin el nombre de un coautor).
- **Contexto `ctx-photography`:** no es nuevo; se repone desde la reserva. Copia su registro de `tools/RESERVA-FASE-B.json` (clave `industrial_etapa5` → `contexts`), cambia `end` a `null` y `date` a «1839 →» (EN y ES), agrega al final de `effect` una frase sobre su efecto posterior (prensa ilustrada, Nueva Visión, fotomontaje) y escribe los enlaces de `escribir_links`.
- **Las líneas de mecanismo son propuestas.** Mejóralas si hace falta; si al redactar un enlace no puedes sostener el mecanismo sin inventar, devuelve `sin_enlace` con el motivo (como en la etapa 6).
- **Obras ★ nuevas** (`level: essential`): Wainwright, Farnsworth y *God Save the Queen*. Intenta que cada una quede con dos enlaces directos de subcategorías distintas; si no es posible sin forzar, deja uno y avísalo en tu respuesta (se anota como excepción C4c).

### 2. Lotes de enlaces para obras ★ existentes (`<tramo>_e<n>`, decisión D3)
El archivo trae `escribir_links`: pares `ctx` → `item` (la obra ya existe) con una línea de mecanismo, el `tipo` («enlace» o «contexto nuevo») y una `nota`. Por cada par escribe un registro `link` como en la etapa 6 (`note` en inglés y `es.note`, ≤ 200 caracteres, `refs: []`). **Regla D3: no forzar.** Si el mecanismo no se sostiene, devuelve `{"rtype":"link","ctx":"...","item":"...","sin_enlace":true,"motivo":"..."}`; esa obra quedará como excepción C4c. Antes de escribir, lee la ficha de la obra en `src-data/` para no contradecirla.

### 3. Lote de reescritura de fichas existentes (`textos_1`)
Cada entrada trae `id` e `instruccion`. Lee el registro actual en `src-data/` y devuelve, en el **formato de `apply2.py`**, solo los campos de texto que cambian:
`{"id": "...", "en": {"key": "...", "more": "..."}, "es": {"key": "...", "more": "..."}, "refs": <COPIA EXACTA de los refs actuales del registro>, "issues": ["qué cambiaste"]}`
- **`refs` debe ser la copia exacta de los `refs` que ya tiene el registro** (`apply2.py` los reemplaza: si pones `[]` se pierden las fuentes de los elementos del Modernismo). Si el registro no tiene fuentes, `[]`.
- **No borres frases que tengan marcas `[n]`**; puedes agregar frases nuevas sin marcas.
- No cambies `id`, nivel, años ni relaciones (eso ya lo hizo `ajustes_etapa7.py`). Los movimientos usan `key`, `traits`, `context` y `shift`; los contextos, `key`, `happened` y `effect`; las obras, `key`, `more` y `status`.
- **No uses `validate_out.py` en este lote** (no admite este formato). Comprueba tú mismo: `en` y `es` con los mismos campos, `key` de una frase (≤ 200 caracteres), `more` de 2 a 4 frases, `refs` copiados sin cambios y las marcas `[n]` iguales en EN y ES. La sesión que orquesta lo aplica con `apply2.py` y corre el build.

## Salida
Como en la etapa 6: un JSON por lote (`<lote>_out.json`), escrito con un script Python (`json.dump(..., ensure_ascii=False, indent=1)`), validado con `validate_out.py` hasta que diga OK (salvo el lote `textos_1`, ver arriba). No edites archivos del proyecto. Responde con 5 líneas: hechos, descartados, `sin_enlace`, ★ que quedaron con un solo enlace directo y dudas.
