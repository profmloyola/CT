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
