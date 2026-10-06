# Brief: lista maestra de un tramo (etapa 1, pasos 1.2–1.4)

Eres un agente de Sonnet. Escribes la **lista de qué entra y cómo se conecta** de UN tramo del proyecto LHD (línea de historia del diseño, ES-CL). No escribes el contenido final de las fichas: solo id, nombre, datos mínimos y la **línea de mecanismo** de cada enlace. Habla en español de Chile.

## Qué leer primero
1. `tools/PLAN-CIERRE.md` secciones 1 a 3, 7 (etapa 1) y las reglas C1–C8 (en especial C4, C4b, C5). Los tamaños de tu tramo están en la sección 3.
2. `tools/SPEC.md` sección 10 (la subsección de tu tramo y 10.7 América Latina) y sección 5 (modelo).
3. `tools/MANUAL-CONTENIDO.md` secciones 3–5 y 11 (elementos de fuera de Occidente).
4. La lista de ids existentes (se genera con un script corto que recorre `src-data/*/*.json`; ya se usó en la etapa 1 y no se guarda): **todos los ids que ya existen**; no los repitas como nuevos y úsalos para enlazar (hay muchos de Modernismo).
5. `tools/pipeline/EJEMPLOS.md` para ver cómo son los registros (solo para calibrar nombres e ids; no los generas).

## Archivo que debes escribir: `tools/LISTAS-CIERRE.md` (una sección por tramo)
Empieza con `## Tramo: <tramo>` y luego estas subsecciones (`###`), cada una con una tabla Markdown. La primera columna es siempre el `id` entre acentos graves. Ids en minúsculas con guiones, en inglés o nombre propio como los existentes (p. ej. `eames-lcw`, `ctx-cold-war`; los contextos empiezan con `ctx-`; los movimientos de tramo no usan `macro-`).

- `### Contextos`: `id` | nombre | sub (political, economic, social, cultural, technological) | años | regiones (europe, north-america, latin-america, global; separadas por coma) | nivel (★ o N) | relaciona (ids opcionales, entre acentos graves)
- `### Productivo`: `id` | nombre | sub (materials, processes, tools) | años | nivel | relaciona
- `### Teoría`: `id` | nombre | años | nivel | relaciona
- `### Movimientos`: `id` | nombre | años | nivel | relaciona
- `### Instituciones`: `id` | nombre | años | nivel | relaciona
- `### Diseñadores`: `id` | nombre | años | disciplinas | nivel | obras | relaciona (movimientos/instituciones)
- `### Obras`: `id` | título | disciplina (graphic, product, fashion, architecture) | año | nivel | diseñadores | tech | regiones | contextos
- `### Conexiones`: `from` | `to` | línea (influencias entre elementos; ≥ 8 por tramo; una frase de 12 a 200 caracteres)
- `### Reserva`: `id` | tipo | nombre | motivo (≈15 % extra por tipo, elementos que quedan fuera pero que se podrían meter si falta; no cuentan).

Reglas de la columna **contextos** de las obras: `` `ctx-id`: mecanismo; `ctx-id2`: mecanismo2 `` — separados por «; » (punto y coma + espacio) y cada mecanismo es una frase concreta de 12–200 caracteres que diga **por qué ese hecho explica esa obra**. **Si no puedes escribir la línea, no hay enlace.** Toda obra ≥ 1 contexto; toda obra ★ ≥ 2 contextos de subcategorías distintas. Los contextos pueden ser de otro tramo (p. ej. un ctx de Modernismo) pero deben existir (en tu lista o en `_ids_existentes.tsv`; también puedes usar `ctx-corfo` y `ctx-early-television`, que están en la reserva de Modernismo y se reintegrarán).
En `diseñadores`, `tech` y `relaciona` se escriben ids entre acentos graves, separados por coma. Cada contexto debe quedar con ≥ 2 enlaces (obras que lo citan, o `relaciona`); cada diseñador con ≥ 1 obra y ≥ 1 enlace; cada institución, movimiento, teoría y productivo con ≥ 1 enlace (aparecer en la columna de otro elemento, o en su propia `relaciona`).

## Cantidades y proporciones (el verificador las exige)
Cantidades por tipo = las de la sección 3 del plan para tu tramo (±2; obras ±3), **contando también los elementos que ya existen en `src-data/<tramo>/`**, que debes incluir en las tablas (con su mismo id). ★ de obras entre 25 % y 35 % (el objetivo exacto está en la sección 3). Se eligen primero los ★ (lo que explica el cambio de época), luego Normal. Reparte disciplinas (gráfica, producto, moda, arquitectura) con criterio de la sección 3 y cuida C5 (América Latina ≥ 15 % de las obras en Posguerra y Posmoderno, ≥ 2 elementos en Reforma e Industrial; Chile ≤ 6 elementos en 1970–73; elementos de fuera de Occidente solo con influencia demostrable, `regions: global`).
Parte de SPEC 10.x y complétala con lo más conocido del tramo, sin forzar y sin inventar hechos: si dudas de una fecha o atribución, deja fuera el elemento o ponlo en la reserva. No copies textos largos.

## Verificación obligatoria
Corre `python3 tools/pipeline/listas_check.py tools/listas/<tramo>.md --tramo <tramo>` hasta que dé **0 errores** (los AVISO se pueden dejar, pero léelos). Escribe el archivo por secciones (primero contextos, productivo, teoría, movimientos, instituciones, diseñadores; luego obras, conexiones, reserva) para no perder trabajo.
No toques `src-data/`, `app.js` ni otros archivos. Al terminar responde en ≤ 10 líneas: cantidades finales, las 3 decisiones más discutibles de tu lista y cualquier aviso restante.
