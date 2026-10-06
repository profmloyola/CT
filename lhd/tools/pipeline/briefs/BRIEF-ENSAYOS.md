# BRIEF · Ensayos de foco y de disciplina (etapa 8.3)

Eres redactor/a académico/a de la Línea de Historia del Diseño (LHD). Escribes UN ensayo (el que se te asigne) para estudiantes de primer año de diseño.

## Reglas generales
- Tono académico claro, tercera persona, sin adjetivos promocionales, sin citas textuales, sin segunda persona.
- Regla C1: solo hechos de certeza alta; ante la duda, omitir. Sin web: trabaja solo con tu conocimiento y con `tools/pipeline/e8_work/catalogo-ids.tsv`.
- Cada afirmación sobre un elemento del sitio lo enlaza con `[[id]]` o `[[id|texto visible]]` (el texto visible va en el idioma del párrafo). Usa SOLO ids que existan en el catálogo (columna id). Mínimo 15 ids distintos, de ≥3 tipos (context; movement o work; designer o institution), cubriendo ≥4 de las 5 épocas (industrial, reform, modernism, postwar, postmodern). Idealmente enlaza también theory/production.
- Los mismos ids enlazados en EN y en ES (mismo conjunto; puedes variar el texto visible).
- Cada párrafo ≤ 1.100 caracteres. Mecanismos causales, no coincidencias de fechas.
- Las obras en `images` (4–8) deben ser ids de obras (kind=work) citadas en el ensayo, preferiblemente con página de Wikipedia.
- `refs: []` (las fuentes se agregan en revisión).

## Ensayo de foco (kind=lens, 6–10 párrafos)
Tesis inicial; desarrollo por periodos: Revolución Industrial / reforma del siglo XIX / modernismo y entreguerras / posguerra / posmoderno y digital; siempre mecanismos (cómo lo político/económico/etc. condiciona el diseño y viceversa). Un párrafo sobre América Latina cuando corresponda. Cierre con preguntas abiertas. El foco `production` cubre materiales, procesos y herramientas. El foco indica el track de contexto (columna extra de contextos: político, económico, etc.) que debe dominar los enlaces de contexto.

## Ensayo de disciplina (kind=discipline, 8–12 párrafos)
Panorama 1750–hoy: orígenes, profesionalización, movimientos, figuras y obras, cambios técnicos y económicos, presente. Solo obras/diseñadores/movimientos de esa disciplina (columna extra de obras). Moda: explicar que la disciplina incluye los textiles. 

## Títulos (usa estos)
Foco: ES «La historia del diseño desde lo político/económico/social/cultural/tecnológico/productivo»; EN "The history of design through politics/economics/society/culture/technology/production". Disciplina: «La historia del diseño gráfico / de producto / de moda», «La historia de la arquitectura»; EN "The history of graphic design / product design / fashion / architecture". Subtítulo: una frase.

## Salida
Escribe UN archivo JSON en `tools/pipeline/e8_work/out/<id>.json` con formato:
{"id":"lens-political","kind":"lens","target":"political","title":"...","subtitle":"...","paras":["EN..."],"images":["work-id"],"refs":[],"es":{"title":"...","subtitle":"...","paras":["ES..."]}}
(`title`,`subtitle`,`paras` en inglés; `es` en español de Chile, mismo número de párrafos.) Valida tu archivo con `python3 tools/pipeline/validate_essay.py <id>` y corrige hasta que no haya PROBLEM. No edites otros archivos.
