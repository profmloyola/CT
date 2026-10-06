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
