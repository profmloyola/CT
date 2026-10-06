# Tarea: redactar los elementos aprobados de la etapa 6 (Parte I: sin fuentes)

Proyecto: Línea de Historia del Diseño (LHD). **Lee primero `tools/pipeline/briefs/BRIEF-CONTENIDO.md` (todas sus reglas valen: C1 no inventar, sin web, `refs: []`, sin marcas `[n]`, `rtype`, 5 líneas de respuesta) y `tools/pipeline/EJEMPLOS.md` (copia los campos, el orden y los largos del registro modelo de cada tipo; en las obras revisa también `type` y los campos de producción).** Esta tarea cambia solo la entrada:

## Entrada
Un archivo JSON con una lista de **registros de propuesta** (ya aprobados por Mauricio; los ids, años, niveles, diseñadores y regiones están FIJOS y no se cambian). Cada uno trae `rtype`, `id`, nombres (`name`/`title` en inglés y `name_es`/`title_es`), `curso` (por qué entra), `links` (propuesta de conexiones), y además:
- `campos`: relaciones que **el propio registro debe llevar** (p. ej. `designers`, `movements`, `tech`, `institutions`, `links.works`, `links.designers`…). Ponlas tal cual, en el lugar que muestra EJEMPLOS.md (los registros de movimiento, institución, teoría y productivo llevan un objeto `links` con listas `movements`, `institutions`, `designers`, `works`). Para una obra, `designers` viene también del registro (campo `designers`).
- `escribir_links`: pares `ctx` → `item` con una línea de mecanismo. **Debes redactar cada par como un registro `link`** (ver abajo).
- `escribir_conexiones`: pares `from` → `to`. Redáctalos como registros `connection`.

## Qué escribir
Un archivo de salida con una lista que contenga, por cada registro de entrada:
1. **El registro completo del elemento** (mismo `rtype` y `id`), con todos los campos del ejemplo de su tipo, textos en inglés al nivel superior y en español de Chile dentro de `es`. Copia sin cambios `id`, `level`, `year`/`start`/`end`/`born`/`died`, `discipline`/`disciplines`, `designers`, `regions`, `countries`. `title_es`/`name_es` van como `es.title`/`es.name`. **No copies** los campos de la propuesta: `curso`, `links` (la lista de propuesta), `explica`, `duda`, `excepcion_C4c`, `reserva_origen`, `escribir_links`, `escribir_conexiones`, `campos`, `_src`. Si el registro lleva `duda`, escribe solo lo que sea seguro (usa «c.», o deja fuera la frase).
2. **Un registro `link` por cada par de `escribir_links`:** `{"rtype":"link","ctx":"...","item":"...","note":"(inglés, ≤ 200 caracteres)","es":{"note":"(español, ≤ 200 caracteres)"},"refs":[]}`. La nota explica el MECANISMO (qué cambió en el contexto → qué decisión de diseño cambió) en 1 o 2 frases, a partir de la línea de mecanismo dada. Si no puedes sostenerla sin inventar: `{"rtype":"link","ctx":"...","item":"...","sin_enlace":true,"motivo":"..."}`.
3. **Un registro `connection` por cada par de `escribir_conexiones`:** `{"rtype":"connection","from":"...","to":"...","note":"...","es":{"note":"..."},"refs":[]}` (nota ≤ 200 caracteres, mecanismo o influencia concreta).
4. Si no conoces bien un elemento: `{"id":"...","descartado":true,"motivo":"..."}` en vez de rellenarlo.

## Reglas específicas
- **Nombres propios y datos:** solo lo que conozcas con alta certeza. Obras de arquitectura: ciudad, año de terminación aproximado («c.» si dudas), arquitecto. Nada de cifras dudosas.
- **Elementos fuera de Occidente** (`regions: ["global"]`): incluye en `more` o en la nota del enlace la línea de mecanismo que explica su influencia en el diseño occidental.
- **Obras**: `key` una frase (≤ 200 caracteres), `more` 2 a 4 frases, `materials`, `status` (estado actual: existe, se conserva, destruida…), `tech` solo con ids de productivo existentes en `src-data/` (si no hay certeza, `[]`), `date` como texto. Diseñadores nuevos: `kind`, `dates`, `born`, `died` (o null si vive; solo si lo conoces con certeza; si no, omite el dato dudoso pero mantén `born` si el registro lo trae), `key` (1 frase) y `more` (1 a 3 frases).
- **Instituciones/premios**: `kind` (school, firm, museum, award, society, publisher…, como en EJEMPLOS), `place`, `start`, `end` (o sin `end` si sigue). **Teorías/documentos**: `author`, `year`, `ideas`, `impact` como en el ejemplo. **Movimientos**: `traits`, `context`, `shift`. **Contextos**: `happened` y `effect` (el mecanismo hacia el diseño).
- Ids de los campos de relación: solo existentes en `src-data/` o presentes en `tools/PROPUESTA-ETAPA6.json`.

## Salida y validación
Escribe el JSON (script Python con `json.dump(..., ensure_ascii=False, indent=1)`) en la ruta indicada; el nombre empieza con el tramo (p. ej. `postwar_d1_out.json`). Corre `python3 tools/pipeline/validate_out.py <archivo>` y arregla todo lo que marque hasta que diga OK. No edites archivos del proyecto. Responde con 5 líneas: elementos hechos, descartados (y por qué), enlaces sin_enlace y dudas.
