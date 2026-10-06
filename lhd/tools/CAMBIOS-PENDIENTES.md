# Cambios pendientes (registro de revisión, después de v13)

**Puntos 1 a 4: implementados en v14. Puntos 5 a 10: implementados en v15. Puntos 11 a 13: implementados en v16. Puntos 14 y 16: v17 (prueba). Puntos 17 a 22: v18.**

Se anotan aquí las observaciones de la persona responsable mientras revisa el sitio. **No se implementan hasta que lo pida.** Cada punto lleva las dudas o los riesgos detectados.

## 1. ✅ Flecha doble en las barras CONTEXTO y DISEÑO

- La barra de categoría **CONTEXTO** lleva una flecha doble para plegar o desplegar todas sus filas, igual que la flechita de cada subcategoría, pero doble. Lo mismo en **DISEÑO**.
- Se eliminan los botones «Expandir todo» y «Colapsar todo» de la esquina del eje.
- Notas técnicas:
  - En la esquina del eje quedan −, + y ↔ (línea completa).
  - Cada flecha doble actúa solo sobre su categoría.
  - Hay que actualizar la ayuda (parte «Zoom y secciones»), la imagen numerada y las pruebas.
- **Decidido:**
  - Cada barra (CONTEXTO y DISEÑO) lleva **dos botones**: doble flecha hacia abajo (desplegar todo) y doble flecha hacia arriba (plegar todo). Así no importa si hay filas abiertas y cerradas a la vez.
  - Van a la derecha del nombre de la barra, en la columna de nombres.
  - Cada botón lleva su tooltip («Desplegar todo el contexto», «Plegar todo el diseño», etc.).
  - Se usan los mismos íconos que tenían los botones que se eliminan.
  - **La vista del foco prima.** Con un foco activo, los botones de CONTEXTO solo pliegan o despliegan la fila del foco (y las subfilas de Productivo, si el foco es Productivo); no quitan el foco ni abren otras filas.
  - Los botones de DISEÑO funcionan igual con o sin foco: muestran o esconden las subfranjas, pero lo no conectado sigue oculto.

## 2. ✅ Al quitar un foco, todo vuelve al estado anterior

- Al activar un foco se guarda una «foto» del estado. Al quitarlo, se restaura esa foto.
- Ejemplo: si una subcategoría estaba cerrada y se activó su foco, al quitar el foco vuelve a quedar cerrada.
- Hoy solo se restauran las Conexiones (v13). Las secciones quedan como las dejó el foco.
- Notas técnicas:
  - **Qué guarda la foto:** las filas y subfranjas abiertas o cerradas (`S.collapsed`) y el botón Conexiones (ya se hace).
  - **Cambio directo de un foco a otro** (Político → Económico): se conserva la foto original, la de antes del primer foco. Al quitar el último foco se vuelve a ese estado inicial.
  - **Cambios hechos durante el foco** (por ejemplo, plegar Instituciones): se descartan al quitar el foco, porque se vuelve a la foto.
  - **Salir del foco de manera indirecta** también restaura la foto. Ocurre al elegir un hecho de otra fila o al usar la flechita de otra fila de contexto.
- **Decidido:** la foto incluye también la ficha que estaba abierta y la posición de desplazamiento (horizontal y vertical).
  - La ficha puede ser el elemento elegido (y su resaltado), la ficha de época, la ficha general (i) o el resumen de revisión.
  - El zoom no se guarda: el foco no lo cambia, así que queda como esté.
  - Si el elemento que estaba elegido quedó oculto por un filtro cambiado durante el foco, se restaura igual (`select` ya reabre lo necesario).

## 3. ✅ El color de destacado deja de ser naranja: negro y negrita (blanco en tema oscuro)

- **Motivo:** los colores tienen significado en la LHD. El naranja de selección (`--accent`, #C2410C claro / #F07A45 oscuro) se confunde con Político (rojo óxido).
- **Cambio:** el destacado pasa a tinta, con negrita.
  - Tema claro: negro, `--ink` #17191E.
  - Tema oscuro: blanco, `--ink` #E8E9EC.
  - Los tokens `--accent*` pasan a valores neutros; ningún color de categoría se usa para destacar.
- **Dónde se aplica** (son unas 28 reglas en `style.css`):
  - elemento seleccionado: texto en negrita y anillo de la obra;
  - barra del movimiento o institución seleccionada;
  - línea de vida resaltada;
  - punto del hecho seleccionado;
  - texto al pasar el cursor por la línea;
  - borde de foco del teclado;
  - enlaces del panel (el panel ya usa neutros).
- **Riesgos y decisiones propuestas:**
  - **Distinguir «elegido» de «relacionado»:** hoy se distinguen por la intensidad del naranja. Propuesta:
    - elegido = relleno negro (blanco en oscuro) con texto invertido, o anillo negro grueso en las obras;
    - relacionado = solo texto en negrita negra y barra con contorno negro, sin relleno.
  - **Líneas de vida largas relacionadas:** quedarían negras y gruesas, muy pesadas a la vista. Propuesta: barra negra más fina o con 60 % de opacidad.
  - **Marca roja de «Observada»** del modo editar (#D92D20): también se parece a Político. Propuesta: cambiarla por un ícono neutro (un «!» negro sobre blanco con borde), o dejarla roja porque solo se ve en el modo editar.
  - **Números de la ayuda** (`.hb`, círculos naranjas) y la imagen numerada (#C2410C): pasan a negro con número blanco, y la imagen se regenera.
  - Hay que volver a revisar el contraste en ambos temas (`check_contrast.py`).
- **Decidido** (la persona responsable delega el detalle, con el negro como base, destacado sin que quede pesado ni feo):
  - **Elegido:**
    - movimientos e instituciones: relleno de tinta con texto invertido;
    - hechos: barra de tinta y texto en negrita;
    - obras: anillo de tinta de 2 px;
    - diseñadores: nombre en negrita y línea de vida en tinta de 3 px, sin engrosar.
  - **Relacionado:**
    - nombre o etiqueta en negrita de tinta;
    - movimientos e instituciones: contorno de tinta de 1,5 px sobre su color de siempre, sin relleno nuevo;
    - hechos: barra en tinta al 70 %;
    - líneas de vida: tinta al 55 % y del mismo grosor (no más pesadas).
  - **Al pasar el cursor:** el texto pasa a tinta y subrayado (no cambia de color).
  - **Marca de «Observada»** (modo editar): círculo blanco con borde de tinta y un «!» en tinta. Ya no es rojo; el rojo queda solo como fondo de la etiqueta «Modo edición».
  - **Números de la ayuda:** círculo de tinta con número invertido; se regenera la imagen numerada.
  - Al implementarlo, revisar con capturas en tema claro y oscuro que el resultado no quede pesado, y ajustar opacidades si hace falta.

## 4. ✅ El foco se activa igual en todo el sitio: haciendo clic en el nombre de la subcategoría

- **Pedido:**
  - En las fichas, el nombre de la subcategoría de contexto («Político», «Económico»…) se vuelve el activador del foco, igual que en la línea, donde se hace clic en el nombre de la fila.
  - Se eliminan los botones «Foco» que hoy están al lado.
  - Debe funcionar en las fichas de movimientos, instituciones, obras y diseñadores.
- **Estado actual (v13):** las cuatro fichas ya tienen la sección «Contexto» con un botón «Foco» por subcategoría (la de diseñador la arma con los enlaces de sus obras). Quizá no se notaba porque la sección solo aparece cuando hay enlaces de contexto.
- **Se aplica igual en:**
  - el encabezado de cada grupo de la sección Contexto de las fichas de movimiento, institución, obra y diseñador (también producción y teoría, que tienen esa sección);
  - la «Síntesis del contexto» de la ficha de época (el nombre de cada subcategoría);
  - el sobretítulo de las fichas de hecho, productivo y teoría: hoy dice «Contexto · Político» y tiene un botón Foco en el encabezado. Solo la palabra de la subcategoría se vuelve activable y se quita el botón;
  - los botones de la barra de filtros siguen como están (son la entrada principal).
- **Aspecto del nombre activable:** el mismo en todas partes, igual que en la línea.
  - Normal: texto con el cuadradito de color y un subrayado punteado discreto.
  - Al pasar el cursor: borde en el color de la subcategoría y tooltip «Foco: Político» (o «Quitar el foco»).
  - Activo: relleno con el color de la subcategoría y texto invertido.
  - Es un `<button>` para el teclado y los lectores de pantalla (`aria-pressed`).
- **Decidido:** al activar el foco desde una ficha, se muestra la ficha del foco. Su ✕ quita el foco y devuelve exactamente a donde se estaba (la ficha de origen, su resaltado, las secciones y el desplazamiento), según el punto 2.

## 5. ✅ Flechas dobles a la izquierda de CONTEXTO y DISEÑO

- **Pedido:** las flechas dobles de desplegar y plegar van a la izquierda del nombre, en la misma posición que la flechita simple de las filas.
  - Hoy (v14) están a la derecha, alineadas al borde de la columna de nombres.
- **Notas técnicas:**
  - Las dos flechas van seguidas, a la izquierda del nombre: ⇊ ⇈ CONTEXTO.
  - La columna de nombres mide 190 px; caben sin cortar «CONTEXTO» ni «DISEÑO».
  - El nombre se corre unos 30 px a la derecha. La flechita simple de las filas queda en el borde izquierdo y el texto de las filas no se mueve, así que las columnas no quedan alineadas exactamente: las flechas dobles ocupan más ancho que la simple.
  - Se regenera la imagen numerada de la ayuda.

## 6. ✅ Etiqueta «Disciplinas» en negrita y chips activos de disciplina un poco más oscuros

- **Etiqueta:** en la primera fila de la barra de filtros, «Disciplinas» usa el mismo estilo que «Foco:» (negrita, en tinta, 11,5 px).
  - Hoy es gris claro y normal.
- **Chips activos de disciplina:** el fondo pasa a ser un poco más oscuro.
  - Hoy usan `--chip-on`: #E8EBF1 en tema claro, #232830 en oscuro.
  - Propuesta: #DCE1E9 en tema claro y #2B313B en oscuro, con borde `--ink-2`, sin tocar el ícono de color.
  - Se revisa el contraste del texto.
- **Decidido:** solo los chips de Disciplinas. Regiones, Mostrar y Escala quedan como están.

## 7. ✅ (En planificación) DISEÑO sin subcategorías + «Organizar por»

- **Idea de la persona responsable:**
  - Se eliminan las subfranjas plegables Movimientos / Instituciones / Diseñadores y obras. Todo se sigue mostrando.
  - Lo que se ve u oculta se controla con la barra **Mostrar**: la segunda fila empieza con «Mostrar: Movimientos | Instituciones | Diseñadores | Obras | Imprescindibles».
  - Nuevo control **«Organizar»** (o «Ver por») con tres opciones: cronológica, por disciplina, por región.
- **Preguntas abiertas** (ver la conversación):
  1. **Cronológica:**
     - **Opción A:** los tipos siguen apilados en orden (movimientos arriba, luego instituciones, luego diseñadores y obras), pero sin encabezados ni pliegue.
     - **Opción B:** todo mezclado en filas comunes solo por fecha.
  2. **Por disciplina, elementos con varias disciplinas** (Bauhaus, De Stijl, Gropius…). Hay tres formas:
     - repetirlos en cada grupo, marcados como repetidos;
     - ponerlos en un grupo «Varias disciplinas»;
     - ponerlos solo en su disciplina principal.
     
     Lo mismo pasa con las regiones (exilios: Bauhaus → Norteamérica).
  3. ¿Los grupos (Gráfico, Producto…; Europa, Norteamérica…) llevan nombre en la columna izquierda? ¿Se pueden plegar?
  4. **Posición de la barra de épocas:** primera fila de DISEÑO, fija arriba en todas las vistas.
  5. **Regiones:** si la segunda fila empieza con Mostrar, el filtro Regiones se mueve a otro lugar, a la primera fila tras Disciplinas o al final de la segunda.
  6. **Flechas dobles de DISEÑO** (puntos 1 y 5): sin subfranjas, dejan de tener sentido. En DISEÑO podrían plegar o desplegar los grupos de la vista por disciplina o región, o desaparecer.
  7. **Curvas con elementos repetidos:** si un elemento aparece en dos grupos, la curva va a la copia más cercana o a la primera.
- **Decidido (respuestas de la persona responsable):**
  1. **Cronológica = opción A:**
     - los tipos van apilados en orden: movimientos, instituciones, diseñadores y obras;
     - sin encabezados ni pliegue.
  2. **Por disciplina:** se vuelve a probar un grupo **«Interdisciplinario»**, que existe solo en esta vista. Ni la vista cronológica ni la vista por región lo tienen.
  3. Los grupos llevan nombre en la columna izquierda. No se pliegan (coherente con quitar los pliegues).
  4. **Se elimina el filtro Regiones** de la barra. El dato `regions` sigue en los datos y sirve para organizar por región.
  5. **Se eliminan las flechas dobles de DISEÑO**; quedan solo las de CONTEXTO. El punto 5 aplica solo a CONTEXTO.
  6. El control se llama **«Organizar:»** (en inglés «Arrange:»).
  - **Barra de épocas:** no se respondió. Se aplica la propuesta: primera fila de DISEÑO, fija en las tres vistas.
  - **Barra de filtros resultante:**
    - Fila 1: Foco: … | Conexiones | Disciplinas: …
    - Fila 2: Mostrar: Movimientos | Instituciones | Diseñadores | Obras | Imprescindibles | Organizar: Cronológica | Por disciplina | Por región | Escala: … | chip «Solo: …»
- **Pendiente de respuesta:**
  - **a)** Criterio de «Interdisciplinario». Propuesta:
    - movimientos, instituciones y diseñadores con **2 o más** disciplinas;
    - las obras van en el grupo de su diseñador (sobre su línea), o en el de su disciplina si no tienen diseñador visible.
    - Alternativa: 3 o más, como la regla antigua.
  - **b)** Por región, elementos con varias regiones (p. ej. `europe` + `north-america`). Opciones:
    - un grupo análogo «Varias regiones»;
    - meterlos en «Global»;
    - repetirlos.
  - **c)** Orden de los grupos. Propuesta:
    - por disciplina: Interdisciplinario, Gráfico, Producto, Moda, Arquitectura;
    - por región: Europa, Norteamérica, América Latina, (Varias regiones), Global.

## 8. ✅ La ficha de época se cierra; sin selección, la ficha queda vacía con un mensaje

- **Pedido:**
  - Las fichas de época (Modernismo, etc.) también tienen ✕ y se pueden cerrar. Hoy la ✕ no hace nada visible, porque sin selección se vuelve a mostrar la ficha de época.
  - Si no hay nada seleccionado, la zona de la ficha aparece en blanco con un mensaje como «Selecciona un elemento para ver su contenido».
- **Notas técnicas y propuesta:**
  - **Prioridad del panel:**
    - ficha general (i);
    - resumen de revisión (modo editar);
    - elemento elegido;
    - ficha de época (solo si se pidió: clic en la barra de épocas, en la tabla de la ficha general o en «Ficha de época» de la ficha del foco);
    - ficha del foco;
    - **vacío con mensaje**.
  - La ficha de época ya no se muestra por defecto. `CFG.defaultEra` deja de usarse y se documenta.
  - **Mensaje:** centrado, gris y breve, en ES y EN.
    - ES: «Selecciona un elemento de la línea para ver su ficha.»
    - EN: «Select an item on the line to see its card.»
    - Debajo, dos ayudas en letra pequeña:
      - «Haz clic en una época de la barra de épocas para leer su panorama»;
      - «El botón (i) abre la presentación».
  - **Barra de épocas:** el tramo se marca como activo solo mientras su ficha está abierta.
  - **Al cargar el sitio:** se sigue abriendo la ficha general (i); al cerrarla queda el mensaje.
  - **Foco:** con un foco activo, cerrar la ficha de un elemento sigue llevando a la ficha del foco. La ✕ del foco lo quita y restaura la foto (punto 2). Si la foto no tenía ficha, queda el mensaje.

## 9. ✅ (En evaluación) Subdivisiones geográficas dentro de cada región en «Organizar por región»

- **Idea:** dentro de Europa, Norteamérica y América Latina aparecen divisiones más tenues por país o zona.
- **Datos disponibles hoy:**
  - Cada elemento de diseño tiene `countries` con códigos ISO actuales.
  - En el Modernismo hay 179 elementos de diseño en 27 países: DE 53, FR 38, US 36, GB 29, RU 19, NL 13… y muchos con 1 a 3.
  - 48 elementos tienen más de un país (exilios, obras internacionales).
- **Problemas detectados:**
  1. **Fronteras que cambian entre 1750 y hoy.** Alemania se unifica en 1871; Italia, en 1861. Están Austria-Hungría, el Imperio ruso, la URSS, Checoslovaquia y Yugoslavia. Las colonias y virreinatos de América Latina se independizan entre 1810 y 1825 aprox.; Irlanda, en 1922. Los códigos ISO son anacrónicos para gran parte de la línea.
  2. **Elementos con varios países:** habría que elegir un país principal. Hoy el primero de la lista no está pensado para eso.
  3. **Demasiadas filas:** con 27 países, muchos con 1 a 3 elementos, la vista se alarga y se vuelve rala.
- **Opciones:**
  - **A. Países actuales**, con la nota «territorio actual». Es simple pero anacrónica y genera muchas filas pequeñas.
  - **B. Zonas culturales estables**, que no son países y no cambian con los años. Propuesta:
    - Europa: Islas Británicas; Francia y Benelux; Mundo germánico (DE, AT, CH); Europa central y del este (CZ, HU, PL…); Rusia y espacio soviético; Nórdicos; Mediterráneo (IT, ES, PT).
    - Norteamérica: EE. UU.; Canadá.
    - América Latina: México y Centroamérica; Caribe; Andes; Brasil; Cono Sur.
    - Es estable, con pocas filas, y evita discutir fronteras. La tabla país → zona es fija y vive en el código o en un archivo de datos.
  - **C. Etiquetas que cambian según los años visibles.** La fila sigue siendo la misma zona o territorio, pero su nombre cambia según el año en el centro de la vista; por ejemplo: Prusia y estados alemanes → Imperio alemán → República de Weimar → Alemania. Otra variante muestra los nombres históricos como rótulos tenues dentro de la franja, en los años en que cambian.
    - Requiere una tabla de nombres por período para unas 15 zonas, investigada y verificada como el resto del contenido.
    - Exige más cuidado en casos que se reparten entre varias filas, como Austria-Hungría.
- **Recomendación:** B ahora (zonas estables, divisiones tenues con su nombre a la izquierda y en letra más chica). C, en su variante de rótulos tenues dentro de la franja, como mejora posterior cuando haya contenido en otras épocas.
  - Para B haría falta un país principal por elemento. Propuesta: el primero de `countries`, que es el lugar de la actividad principal; revisar los 48 casos con varios países.
- **Decidido:** opción **B**, zonas culturales estables, con las zonas propuestas.
  - **Cómo se ven:** son divisiones tenues dentro de cada región, con el nombre de la zona a la izquierda en letra más chica.
  - **Zona de cada elemento:** sale de su país principal, el primero de `countries`. Antes de implementar hay que revisar los 48 elementos con varios países y reordenarlos si hace falta. Ese reordenamiento es un cambio de datos, no de contenido.
  - **Zonas sin elementos visibles:** no se muestran.
  - **Países fuera de las tres regiones** (JP, TR, KE…): no tienen zona. Van sin subdivisión dentro de «Global» o del grupo que corresponda según 7b.
  - **Mapa país → zona**, fijo en el código:
    - Islas Británicas: GB, IE.
    - Francia y Benelux: FR, BE, NL, LU.
    - Mundo germánico: DE, AT, CH.
    - Europa central y del este: CZ, SK, HU, PL, RO, BG, las de la ex-Yugoslavia y los países bálticos.
    - Rusia y espacio soviético: RU, UA, BY, GE, AM…
    - Nórdicos: DK, NO, SE, FI, IS.
    - Mediterráneo: IT, ES, PT, GR.
    - EE. UU.: US.
    - Canadá: CA.
    - México y Centroamérica: MX, GT, CR, PA…
    - Caribe: CU, DO, PR…
    - Andes: CO, VE, EC, PE, BO.
    - Brasil: BR.
    - Cono Sur: CL, AR, UY, PY.
  - **Opción C** (rótulos históricos tenues) queda como mejora posterior, cuando haya contenido en otras épocas.

### Punto 7: respuestas a las preguntas a, b y c («aplica lo propuesto»)
- **a)** Interdisciplinario: movimientos, instituciones y diseñadores con **2 o más** disciplinas.
  - Las obras van sobre la línea de su diseñador, aunque esté en Interdisciplinario.
  - Las obras sin diseñador visible van al grupo de su disciplina.
- **b)** Elementos con varias regiones: van a un grupo **«Varias regiones»**, sin subdivisiones por zona.
  - Las obras de un diseñador van sobre su línea, en el grupo del diseñador.
  - Las obras sueltas van en el grupo de su propia región.
- **c)** Orden de los grupos:
  - por disciplina: Interdisciplinario, Gráfico, Producto, Moda, Arquitectura;
  - por región: Europa, Norteamérica, América Latina, Varias regiones, Global.

**Estado:**
- Punto 7: definido.
- Puntos 5, 6, 7, 8 y 9: listos para implementar cuando se pida.
- Punto 5: solo CONTEXTO, porque DISEÑO pierde las flechas dobles.

## 10. ✅ Instituciones y movimientos en el mismo gris; movimientos un poco más oscuros

- **Pedido:** quitar el tono azulado de las instituciones (`--c-inst` 86,108,160). Movimientos e instituciones usan el mismo gris neutro, y los movimientos quedan algo más destacados por ser más oscuros.
- **Propuesta:**
  - **Mismo tono:** `--c-inst` = `--c-neutral` (104,116,138 en claro; 149,158,173 en oscuro).
  - **Instituciones:** opacidad de relleno algo menor, 0,22 en claro.
  - **Movimientos:** un poco más oscuros. La opacidad del relleno sube de `--p-alpha` 0,18 a 0,26 en claro y de 0,26 a 0,34 en oscuro, y el texto pasa de `--t-neutral` a `--ink-2`.
  - **Se distinguen por la forma, no por el color:** el movimiento tiene borde difuso y la institución termina en punta de flecha.
  - Revisar con capturas en ambos temas que el texto de las barras siga legible y que lo elegido o relacionado (punto 3) se siga distinguiendo.

## 11. ✅ Divisiones tenues entre movimientos, instituciones y diseñadores (vistas cronológica y por disciplina)

- **Pedido:** en las vistas cronológica y por disciplina, una línea tenue separa los bloques de movimientos, instituciones y diseñadores y obras, equivalente a las zonas de la vista por región.
- **Propuesta:**
  - Línea punteada tenue (la misma `zone-line`) entre bloques.
  - Nombre del bloque en letra chica y gris en la columna izquierda: «Movimientos», «Instituciones», «Diseñadores y obras». Va bajo el nombre del grupo en la vista por disciplina, y sigue la vista al desplazarse como las zonas.
  - En la vista por región no se agregan, porque las zonas ya dividen. Hacerlo dejaría dos niveles de líneas dentro de cada zona.
  - Un bloque vacío (por ejemplo, sin instituciones en Moda) no muestra línea ni nombre.
  - Las obras sin diseñador visible van dentro de «Diseñadores y obras», al final del bloque.
- Pendiente de respuesta: ¿con nombre en la columna izquierda o solo la línea?

## 12. ✅ Nuevo aspecto para las instituciones (se confunden con los movimientos)

- **Problema (v15):** en el mismo gris, las instituciones se confunden con los movimientos aunque terminen en punta de flecha.
- **Opciones:**
  - **A. Blanca con contorno.** Relleno blanco (en tema oscuro, el color de la superficie) con un contorno gris de 1,5 px y la punta de flecha. Se distingue del movimiento, que es una barra gris rellena y difusa, y sigue siendo neutra.
    - Técnica: dos capas con la misma forma recortada, una gris de fondo y una blanca encima, 1,5 px más chica.
  - **B. Solo contorno:** borde gris sin relleno, con punta de flecha. Es parecida a A, pero el fondo de la fila se ve a través.
  - **C. Línea fina con flecha:** una línea de 3 px con la punta y el nombre encima, como un hecho de contexto con duración. Es la más liviana, pero se puede confundir con las barras de contexto y con las líneas de vida.
  - **D. Trama:** relleno de rayas diagonales grises.
- **Recomendación:** A.
  - Elegida: relleno de tinta, igual que hoy.
  - Relacionada: contorno de tinta y nombre en negrita.
  - Con foco: contorno y fondo tenue del color de la fila.
- **Decidido (punto 12):** opción **A**: relleno blanco (color de la superficie en tema oscuro), contorno gris de 1,5 px y punta de flecha. Elegida, relacionada y con foco quedan como en la recomendación. La leyenda de la ayuda se actualiza.
- **Decidido (punto 11):** línea punteada tenue y nombre del bloque en letra chica gris en la columna izquierda.

## 13. ✅ Doble clic = seleccionar + filtro «Ver solo sus conexiones»

- **Pedido:** hacer doble clic en un elemento de la línea equivale a seleccionarlo y activar su filtro (el botón de embudo de la ficha).
- **Notas técnicas:**
  - El primer clic ya selecciona, y el doble clic agrega el filtro, así que el comportamiento es natural.
  - El contenido de la línea ya no permite seleccionar texto, así que el doble clic no marca palabras.
  - Doble clic sobre el elemento que ya tiene el filtro activo: quita el filtro (igual que el botón).
  - La etiqueta de una obra (fuera del marcador) responde igual que el marcador.
- **Propuesta para otros elementos:**
  - **Movimientos, instituciones, diseñadores y obras:** filtro «Ver solo sus conexiones», como se pidió.
  - **Hechos de contexto, productivo y teoría:** hoy su ficha no tiene botón de filtro, pero el filtro funciona con cualquier elemento. Propuesta: el doble clic también filtra (queda el hecho y el diseño conectado), y se agrega el botón de embudo a esas fichas para que sea coherente.
    - Alternativa: que el doble clic sobre un hecho active el foco de su fila.
  - **Barra de épocas:** el doble clic acerca la vista a la época (como la lupa de su ficha). Un clic abre la ficha sin mover la vista.
  - **Nombres de filas y grupos:** el doble clic no hace nada especial.
- **Ayuda:** agregar «Doble clic» en Atajos y en la sección de fichas.
- Pendiente de respuesta: qué hace el doble clic en hechos de contexto y en la barra de épocas.
- **Decidido (punto 13):**
  - **Hechos de contexto, productivo y teoría:** el doble clic también activa «Ver solo sus conexiones», y sus fichas reciben el botón de embudo.
  - **Barra de épocas:** el doble clic acerca la vista a la época; un clic abre la ficha sin mover la vista.

**Estado:** puntos 11, 12 y 13 definidos, listos para implementar cuando se pida.

## 14. ✅ Contorno de las instituciones más delgado

- **Pedido:** la línea de contorno de las instituciones es un poco más delgada.
- **Propuesta:** bajar de 1,5 px a 1 px.
  - Se cambia el recorte de la capa blanca (`.inst .ib::after`): left, top y bottom pasan a 1 px y right a 1,5 px. La punta de la flecha se ajusta para que el contorno se vea parejo.
  - Se revisa en ambos temas que el contorno no desaparezca sobre el fondo de la fila, sobre todo en tema oscuro.
  - La leyenda de la ayuda pasa a `stroke-width="1"`.

## 15. ✅ (reemplazado por el 16) Renombrar «Cronológica» en Organizar

- **Pedido:** que empiece con «Por», como «Por disciplina» y «Por región».
- **Candidatas:**
  - «Por cronología» (EN «By chronology»).
  - «Por fecha» (EN «By date»).
  - «Por año» (EN «By year»).
  - «Por tiempo» (EN «By time»).
  - Se evita «Por época» porque sugiere agruparlo por épocas, y esta vista no agrupa.
- **Recomendación:** «Por fecha» / «By date». Es corto, claro y dice exactamente lo que hace: todo en un bloque, ordenado solo por fecha.
- Hay que actualizar el chip, la ayuda y la ficha (i).
- Pendiente de respuesta: cuál de las candidatas.
- **Decidido:** «Por fecha» (EN «By date»). El identificador interno sigue siendo `chrono`, así que la preferencia guardada en el navegador no se pierde.

## 16. ✅ PRUEBA (v17): «Por categoría» + nuevo «Por fecha»

- **Pedido:**
  - La antigua vista «Por fecha» (bloques Movimientos / Instituciones / Diseñadores y obras) pasa a llamarse **«Por categoría»** (EN «By category»; id interno `chrono`).
  - Nueva vista **«Por fecha»** (EN «By date»; id `date`): una fila por cada movimiento, institución, diseñador (con sus obras) y obra sin diseñador, ordenada por año de inicio. Forma una línea de tiempo larga hacia abajo.
- **Implementación:**
  - Año de inicio: `start` en movimientos e instituciones, `born` en diseñadores y `year` en obras. Si hay empate, el orden es movimiento, institución, diseñador, obra, y luego por nombre.
  - Una línea tenue y la década («1920–1929») a la izquierda en cada década nueva; la etiqueta sigue la vista.
  - Las obras sueltas llevan etiqueta.
  - El nivel de detalle se mantiene (lo oculto por zoom no ocupa fila).
  - En el Modernismo, la vista mide unos 3.600 px de alto.
- **Observación:** los diseñadores se ordenan por nacimiento, así que quedan arriba, antes de los movimientos (1860–1900). Alternativa: ordenarlos por su primera obra.
- **Vuelta atrás:**
  - El código está aislado en un bloque marcado «TEST (v17)» en `build()`, más la entrada `date` del chip y los textos.
  - Además se guardó la versión anterior completa como `LHD-v16-antes-de-prueba-por-fecha.zip`.
- También se implementó el punto 14: contorno de 1 px en las instituciones.

## 17. ✅ En «Por fecha», los diseñadores se esconden

- **Pedido:** en la vista «Por fecha» no se muestran los diseñadores. Su año de nacimiento desordena la línea, porque quedan todos arriba (1860–1900).
- **Consecuencias y propuesta:**
  - **Obras:** todas pasan a ser obras sueltas, una fila por obra según su año, con etiqueta. La línea queda formada por movimientos, instituciones y obras.
  - **Chip «Diseñadores» en Mostrar:** en esta vista queda deshabilitado (atenuado), con el tooltip «En la vista por fecha no se muestran los diseñadores». Al volver a otra vista recupera su estado.
  - **Elegir un diseñador** desde la búsqueda, un chip de ficha o una curva: se abre su ficha, pero no tiene lugar en la línea. Propuesta:
    - las obras del diseñador se resaltan (como relacionadas) y la vista va a la primera;
    - no se cambia de vista automáticamente.
  - **Filtro «Ver solo sus conexiones» o doble clic** sobre un diseñador desde su ficha: quedan sus obras y lo conectado, sin la línea de vida.
  - **Curvas:** las relaciones diseñador ↔ obra no se dibujan, porque el diseñador no está en la línea; las demás, sí.
- Pendiente de respuesta: confirmar la propuesta para elegir un diseñador en esta vista.
- **Respuesta:** al elegir un diseñador, aparece su línea de vida.
- **Propuesta concreta:**
  - **Posición:** la línea del diseñador elegido aparece en el lugar de su **primera obra**, no en el de su nacimiento, para no saltar a la década de 1860.
  - **Obras:** sus obras se mueven a esa línea y dejan de verse sueltas mientras está elegido.
  - **Al quitar la selección:** la línea desaparece y las obras vuelven a sus filas.
  - **Con «Ver solo sus conexiones»** sobre un diseñador: igual, con la línea visible mientras dure el filtro.
- Pendiente de respuesta:
  - ¿Solo la línea del diseñador elegido?
  - ¿O también la de los diseñadores de una obra elegida (por ejemplo, al elegir la Silla Barcelona, aparecen Mies y Lilly Reich)?
- **Decidido (delegado):** la línea aparece **solo al elegir un diseñador**, no al elegir una obra.
  - Motivo: si cada clic en una obra hiciera aparecer líneas y mover obras a ellas, la línea se reacomodaría a cada clic y se perdería el lugar.
  - Al elegir una obra, su diseñador sigue conectado por una curva hacia su ficha. Sin línea en la vista, la curva no tiene destino, así que la relación se ve en la ficha.

**Estado:** punto 17 definido, listo para implementar cuando se pida.

## 18. ✅ Elegir en el eje de años el tramo al que se hace zoom

- **Pedido:** seleccionar en la línea de años el tramo que se quiere ver, haciendo clic y arrastrando, o con dos corchetes que se puedan mover (o ambos).
- **Propuesta A: arrastrar en el eje.**
  - Al apretar y arrastrar sobre los años aparece un tramo sombreado, con los años de inicio y fin escritos.
  - Una franja muy tenue sombrea el mismo tramo en toda la línea.
  - Al soltar, la vista se ajusta a ese tramo, con el zoom máximo como límite.
  - Un clic sin arrastre o `Esc` cancela.
  - El cursor sobre el eje es una cruz o I de selección, para que se note que se puede.
- **Propuesta B: corchetes.**
  - Sobre el eje solo se ven los años visibles, así que unos corchetes en sus bordes no tendrían recorrido.
  - Para que sirvan hace falta una tira delgada de 1750–hoy (8–10 px) sobre los años, con dos corchetes que marcan el tramo visible. Al mover un corchete cambia el zoom; al arrastrar el tramo entre ellos, la vista se desplaza.
  - Es un «minimapa» solo de tiempo. Antes se decidió no tener minimapa; habría que reabrir esa decisión.
- **Recomendación:** A ahora; B solo si después se quiere ver siempre dónde está uno dentro de 1750–hoy.
- Pendiente de respuesta: A, B o ambos.

## 19. ✅ Flechas en los extremos del eje para ampliar el período visible

- **Pedido:** al llevar el mouse a los extremos del eje de años, el cursor se convierte en flecha y el período mostrado se agranda.
- **Dudas:**
  - **Qué significa «se agranda»:**
    - **(a)** alejar el zoom por ese lado: se suman años a la izquierda o la derecha y el otro borde queda fijo;
    - **(b)** desplazarse en esa dirección sin cambiar el zoom.
  - **Cuándo actúa:**
    - solo con pasar el mouse, que es incómodo porque se mueve sin querer;
    - con clic, que amplía un 25 % por clic;
    - mantener apretado, que amplía de forma continua.
- **Propuesta:** (a) con clic o con el botón apretado.
  - Al acercarse a 40 px del borde del eje aparece una flecha ‹ o › y el cursor cambia.
  - Cada clic suma un 25 % de años por ese lado, con el borde opuesto fijo.
  - Mantener apretado repite.
  - En el extremo de 1750 o de hoy la flecha no aparece.

## 20. ✅ Botón «Toda la línea»

- **Pedido:** el botón de ajuste (↔) pasa a tener texto, para que se vea más.
- **Propuesta:**
  - Texto «Toda la línea» (EN «Whole line»), con el ícono ↔ delante, en la esquina del eje junto a − y +.
  - Cabe en los 190 px de la columna.
  - Mientras ya se ve toda la línea, el botón queda atenuado.
- **Decidido (punto 19):** opción (a): ampliar por ese lado, con el borde opuesto fijo. Actúa con clic (+25 %) o manteniendo apretado, no con solo pasar el mouse. En 1750 y en hoy no hay flecha.

### Punto 20 reemplazado: «Desde ____ Hasta ____» + «Todo» en la esquina del eje
- **Pedido:** en lugar de los botones −, + y ↔, la esquina del eje muestra «Desde [año] Hasta [año]», con campos donde se escribe el año, y un botón **«Todo»** (toda la línea).
- **Notas técnicas y propuesta:**
  - **Valores:** los campos muestran siempre los años visibles (inicio y fin) y se actualizan al desplazarse y al hacer zoom.
  - **Aplicar:** al escribir un año y apretar Enter (o al salir del campo), la vista se ajusta a ese tramo. Valores fuera de 1750–hoy se ajustan al límite. Si «Desde» es mayor o igual que «Hasta», o el tramo es más corto que el zoom máximo, el campo vuelve al valor anterior con un aviso breve.
  - **Zoom:** quedan la rueda con Ctrl/⌘, las teclas + y −, el arrastre en el eje (punto 18) y las flechas de los bordes (punto 19). Se pierden los botones − y +.
  - **Espacio:** «Desde [1914] Hasta [1945] Todo» necesita unos 215 px y la columna mide 190 px. Hay tres soluciones:
    - **(1)** textos más cortos: «De [1914] a [1945] Todo», que cabe;
    - **(2)** ensanchar la columna de nombres a 220 px para todas las filas;
    - **(3)** poner los campos sobre el eje, a la izquierda de los años.
    
    Propuesta: (1).
  - En inglés: «From [ ] To [ ] All» (cabe).
- Pendiente de respuesta:
  - (1), (2) o (3) para el espacio.
  - Si el punto 18 (arrastrar en el eje) se mantiene además de los campos.
- **Decidido (punto 20):** opción (1): «De [año] a [año] Todo» (EN «From [ ] To [ ] All») en la esquina del eje.
- **Decidido (punto 18):** se hacen **A y B**.
  - **A.** Arrastrar sobre los años del eje para elegir un tramo.
  - **B.** **Minimapa del tiempo:** una tira delgada (unos 10 px) sobre los años, con toda la línea de 1750 a hoy.
    - Usa la misma escala que la línea (por densidad o lineal).
    - Muestra las épocas como tramos tenues, sin textos para no recargar; el nombre va en el tooltip.
    - Dos corchetes `[ ]` marcan el tramo visible.
    - Arrastrar un corchete cambia el inicio o el fin, es decir, el zoom.
    - Arrastrar el tramo entre los corchetes desplaza la vista sin cambiar el zoom.
    - Clic fuera del tramo centra la vista ahí.
    - Se actualiza al desplazarse y al hacer zoom.
  - Esto reabre la decisión de «sin minimapa» (punto 5 de la lista de v11) solo para el tiempo; no hay minimapa de las filas.
  - El eje pasa de 26 a unos 38 px de alto.

**Estado:** puntos 17, 18, 19 y 20 definidos, listos para implementar cuando se pida.

## 21. ✅ La teoría pasa de CONTEXTO a DISEÑO (obras de teoría del diseño)

- **Pedido:**
  - La fila «Teórico» deja de ser contexto y se vuelve una categoría de DISEÑO.
  - Se mantienen las conexiones, el ícono de libro y la ficha, pero se organiza distinto.
  - Hay un chip «Teoría» en Mostrar.
- **Datos actuales:**
  - 14 textos en el Modernismo, en `56-theory.json`.
  - Campos: `genre`, `regions`, `countries`, enlaces a movimientos, instituciones, diseñadores y obras.
  - El `short` es el apellido del autor (Gropius, Le Corbusier, Tschichold…).
  - No tienen `disciplines`.
- **Cambios que implica:**
  1. **CONTEXTO:** desaparecen la fila «Teórico» y su contador.
     - Productivo sigue siendo contexto.
     - La ficha (i) y la ayuda pasan la teoría a la parte de Diseño.
  2. **Foco:** se quita «Teórico» de los botones de foco, porque el foco es solo para contexto, y con él su ficha de foco.
     - La palabra «Teoría» en el sobretítulo de su ficha deja de activar un foco.
  3. **DISEÑO:**
     - Nuevo bloque «Teoría» con el ícono de libro.
     - **Por categoría:** el bloque va después de «Instituciones» y antes de «Diseñadores y obras» (propuesta), porque los textos suelen explicar movimientos y escuelas.
     - **Por fecha:** una fila por texto, según su año.
     - **Por región:** según `regions` y el país principal, como el resto.
     - **Por disciplina:** no tienen `disciplines`. Propuesta: derivarlo del `genre`. Tipografía → Gráfico; arquitectura → Arquitectura; manifiestos, pedagogía, método, crítica, historia y sociedad → Interdisciplinario. Alternativa: agregar `disciplines` a cada texto en los datos.
  4. **Mostrar:** chip «Teoría» después de «Obras».
  5. **Conexiones:**
     - Las curvas entre teoría y diseño dejan de ser «de contexto» (hoy van en el tono del Teórico) y pasan a ser relaciones de diseño, en gris neutro como las demás.
     - Con un foco activo, la teoría se muestra solo si está conectada con hechos de ese foco, como el resto del diseño.
  6. **Enlaces de contexto:** hoy un hecho de contexto no puede enlazar con un texto teórico, porque el build solo acepta movimientos, instituciones, diseñadores y obras.
     - Se permite (`DESIGN_KINDS` + `theory`), para que un texto pueda tener sus hechos de contexto como cualquier obra.
     - Se actualizan SPEC y build.
  7. **Etiquetas:** hoy el `short` es el apellido del autor. En DISEÑO se confunde con las líneas de vida (por ejemplo, «Gropius» como texto y como diseñador). Propuesta:
     - en la línea mostrar el título corto del texto, con el ícono de libro y el apellido en el tooltip: «Vers une architecture», «Die neue Typographie», «Horizons»;
     - requiere un `short` nuevo por texto, en EN y ES, y cambiar la regla del build que pide «solo el apellido».
  8. **Estadísticas y ficha (i):** «Productivo + teoría» pasa a «Productivo» en contexto y «Teoría» en diseño.
  9. **Ayuda:** la leyenda mueve el ícono de libro a Diseño, y se regeneran las imágenes.
- Pendiente de respuesta:
  - **2.** ¿Se quita Teórico del foco?
  - **3.** Ubicación del bloque en «Por categoría» y regla para «Por disciplina».
  - **7.** Etiquetas con título corto.
- **Decidido:**
  - **2.** Se quita «Teórico» del foco. El foco queda para las 6 filas de contexto: político, económico, social, cultural, tecnológico y productivo.
  - **3.** En «Por categoría», el bloque «Teoría» va después de Instituciones: Movimientos, Instituciones, Teoría, Diseñadores y obras.
  - **3.** En «Por disciplina», la disciplina se deriva del género del texto:
    - tipografía → Gráfico;
    - arquitectura → Arquitectura;
    - manifiesto, pedagogía, método, crítica, historia y sociedad → Interdisciplinario.
  - **7.** Sin preferencia; se aplica la propuesta. En la línea va el título corto del texto (nuevo `short` en EN y ES para los 14 textos), con el autor en el tooltip. La regla del build pasa de «solo el apellido» a «título corto» (máximo 22 caracteres). El `short` de los textos es un cambio de presentación; el resto del contenido no cambia.

**Estado:** puntos 17 a 21 definidos, listos para implementar cuando se pida.
- **Cambio de decisión (punto 21.7):** se mantiene el **apellido del autor** como etiqueta de los textos en la línea, como hoy. No se escriben `short` nuevos ni cambia la regla del build.
  - El ícono de libro y el bloque propio «Teoría» bastan para distinguir el texto de la línea de vida del diseñador.
  - El título completo va en el tooltip y en la ficha.

## 22. ✅ Grupos plegables en las vistas de «Organizar»

- **Pedido:** los grupos se pliegan con la flechita.
  - **Por fecha:** las décadas.
  - **Por disciplina:** cada disciplina, y dentro de ella sus categorías (Movimientos, Instituciones, Teoría, Diseñadores y obras).
  - **Por región:** cada región y sus zonas.
  - En todos los casos se mantiene la tipografía y la jerarquía actual: grupo en negrita, subdivisión en gris claro y chico, cada uno con su flechita a la izquierda.
- **Reabre** la decisión del punto 7.3 («los grupos no se pliegan»).
- **Notas técnicas y propuesta:**
  - **Flechitas:**
    - las de grupo son iguales a las de las filas de contexto;
    - las de subdivisión son más chicas y grises, junto al nombre gris.
  - **Grupo plegado:** queda una franja baja con el nombre, el número de elementos y una nota en cursiva («12 elementos»), como hoy en contexto.
    - Las curvas hacia elementos de un grupo plegado terminan en flecha sobre esa franja (mecanismo actual).
  - **Estado:** cada vista recuerda lo que se plegó en ella; por ejemplo, plegar «Moda» no pliega nada en la vista por región.
    - Al elegir un elemento que está dentro de un grupo plegado, se abre ese grupo.
    - La «foto» del foco (punto 2) incluye estos pliegues.
  - **Flechas dobles en DISEÑO:** con grupos plegables vuelven a tener sentido.
    - Propuesta: recuperar «⇊ ⇈» a la izquierda de DISEÑO, igual que en CONTEXTO, para plegar o desplegar todos los grupos y subdivisiones de la vista actual.
    - Esto revierte en parte el punto 7.5.
  - **Por fecha:** puede tener unas 20 décadas cuando haya contenido en todas las épocas; el plegado por décadas ayuda a recorrerla.
  - Los nombres siguen la vista al desplazarse, como hoy.
- Pendiente de respuesta:
  - **a)** ¿También se pliegan las categorías en «Por categoría» (Movimientos, Instituciones, Teoría, Diseñadores y obras)?
  - **b)** ¿Se recuperan las flechas dobles de DISEÑO?
- **Decidido (22.b):** CONTEXTO y DISEÑO llevan flechas dobles de «desplegar todo» y «plegar todo». Las de DISEÑO actúan sobre los grupos de la vista actual.
- **Nuevo aspecto de las flechas dobles** (la persona responsable no quiere las actuales ⇊ ⇈ con borde):
  - Se dibujan como las flechitas simples de las filas: mismo trazo de 1,5 px, mismo gris, sin borde ni fondo, del tamaño de la flechita simple.
  - **Desplegar todo:** dos chevrones hacia abajo, uno sobre otro (como la flechita de «abierto», doble).
  - **Plegar todo:** dos chevrones hacia la derecha, uno junto al otro, «››» (como la flechita de «cerrado», doble).
  - Así cada flecha doble se lee como «todas abiertas» o «todas cerradas», con el mismo código visual que las filas.
  - Al pasar el mouse se oscurecen, igual que las simples; cada una lleva su tooltip.
  - Van a la izquierda del nombre (CONTEXTO, DISEÑO).
- Pendiente de respuesta (22.a): ¿también se pliegan las categorías en «Por categoría»? Si no hay respuesta, se aplica la propuesta (sí, por coherencia).

### Notas de la implementación v18
- **Zoom máximo:** 60 px por año en la década más densa. Un tramo escrito en «De … a …» más corto que lo que permite ese zoom se amplía solo; por ejemplo, 1920–1930 queda en 1920–1935.
- **Claves de pliegue del diseño:**
  - `g:<vista>:<grupo>` para los grupos;
  - `b:<vista>:<grupo>:<bloque>` para las categorías;
  - `z:region:<región>:<zona>` para las zonas.
  
  Al activar un foco se abren todas (la foto del punto 2 las restaura al quitarlo).
- **Teoría en «Por fecha»:** una fila por texto. Los diseñadores ocultos no se cuentan en el aviso «Acerca para ver más».

## 23. ✅ Una sola flecha doble que alterna (como las flechas simples)

- **Pedido:** en CONTEXTO y DISEÑO no se ven las dos flechas dobles a la vez. Se ve una sola, que cambia entre «⌄⌄» y «››» como la flechita simple de abrir o cerrar.
- **Propuesta (misma lógica que la flechita simple, que muestra el estado actual):**
  - Si hay al menos una fila o grupo abierto en esa sección, se ve **⌄⌄** («abierto»); un clic pliega todo y la flecha pasa a **››**.
  - Si todo está plegado, se ve **››**; un clic despliega todo y pasa a **⌄⌄**.
  - El tooltip dice lo que hará el clic: «Plegar todo el contexto» o «Desplegar todo el contexto».
  - **Con un foco activo:** la flecha de CONTEXTO refleja y cambia solo la fila del foco (y sus subfilas).
  - **En DISEÑO:** cuenta los grupos y subdivisiones de la vista actual de Organizar.

## 24. ✅ El tramo que se arrastra sobre los años se sombrea en toda la línea

- **Pedido:** al arrastrar sobre los años, el tramo sombreado baja por toda la línea, para ver claramente qué queda dentro y fuera.
- **Propuesta:**
  - El sombreado va del eje hasta el borde inferior de la vista, sobre las filas y bajo la columna de nombres y la ficha.
  - Tono gris tenue, con bordes de tinta de 1,5 px a cada lado y los años de inicio y fin arriba, como ahora.
  - No bloquea el mouse.
  - Desaparece al soltar o con `Esc`.

## 25. ✅ Botón «Ajustar a lo visible»

- **Pedido:** además de «Todo» (1750–hoy, con todas las épocas aunque estén vacías), un botón que ajuste la vista a lo que se está mostrando, sin considerar las épocas.
- **Qué cuenta como «lo visible»** (propuesta):
  - Los elementos que quedan en la línea después de filtros, foco y «Ver solo sus conexiones»: hechos, productivos, movimientos, instituciones, teoría, obras y diseñadores dibujados.
  - El tramo va desde el **año de inicio más temprano** hasta el **año de inicio más tardío**, con un margen del 4 % a cada lado.
  - No cuentan los finales de barras largas o abiertas (Chanel, MoMA siguen «hasta hoy»), porque estirarían la vista hasta hoy.
  - Sí cuenta el final de las barras cortas.
  - **Ejemplo:** con el Modernismo como único contenido, ajusta a unos 1908–1948; con un foco o un filtro activo, al tramo de lo que quedó.
- **Dónde ponerlo:**
  - **(a)** En la esquina del eje, como ícono al lado de «Todo»: «De [ ] a [ ] Todo ⤢». Cabe achicando un poco los campos de año. Tooltip «Ajustar a lo que se muestra».
  - **(b)** Como texto: «Todo | Ajustar». No cabe en 190 px sin ensanchar la columna o quitar «De» y «a».
  - **(c)** En el minimapa del tiempo, doble clic para ajustar a lo visible. Es poco descubrible.
  - **(d)** En la barra de filtros, junto a «Escala».
- **Recomendación:**
  - (a), como ícono junto a «Todo», con tooltip.
  - Además, que al activar un foco o «Ver solo sus conexiones» no se ajuste solo: el usuario decide con el botón.
- Pendiente de respuesta: ubicación, y si el ajuste es automático al activar un foco o un filtro.
- **Decidido (punto 25):** en la esquina del eje, «Todo» se reemplaza por un botón de ícono **⟷** (flecha doble, «Toda la línea») y se agrega un botón **|⟷|** (flecha entre topes, «Ajustar a lo que se muestra»): «De [ ] a [ ] ⟷ |⟷|».
  - Íconos SVG con el mismo trazo que el resto, tooltip y `aria-label` en ES y EN.
  - El botón ⟷ queda atenuado cuando ya se ve toda la línea; |⟷| queda atenuado cuando la vista ya coincide con lo visible.
  - El ajuste no es automático al activar un foco o un filtro (decisión por defecto; el usuario usa el botón).
  - Se actualizan la ayuda («Años visibles») y la imagen numerada.

## 26. ✅ Líneas de vida de los diseñadores con color de disciplina

- **Idea:** la barra del diseñador toma el color de su disciplina. El problema son los que tienen más de una.
- **Datos:**
  - Cada diseñador tiene `disciplines` en los datos (ej.: Breuer = producto + arquitectura).
  - Sus obras también tienen disciplina, y no siempre coinciden con la lista: puede haber disciplinas sin obras en la línea.
- **Opciones para quien tiene varias disciplinas:**
  - **(a) Rayas:** la línea alterna tramos cortos de cada color (por ejemplo, 6 px azul y 6 px naranja). Se lee «varias disciplinas» sin elegir una.
  - **(b) Disciplina principal:** un solo color, el de la disciplina con más obras en la línea (o la primera de `disciplines` si no tiene obras). Es simple, pero esconde la otra.
  - **(c) Tramos en el tiempo:** la línea se colorea por la disciplina de sus obras en cada período (Breuer: producto en los años 20 y arquitectura después). Es lo más informativo, pero es ambiguo entre obras y fuera de ellas.
  - **(d) Gris neutro para los de varias disciplinas,** color solo para los de una (equivalente a «Interdisciplinario»).
- **Fuente del color:** propuesta `disciplines` del diseñador (dato curado), no las obras visibles. Así el color no cambia al filtrar.
- **Riesgo:** líneas de color fuerte compiten con los marcadores de obra, que usan los mismos colores. Propuesta:
  - línea al 45 % de opacidad;
  - el marcador de la obra mantiene su borde blanco para separarse de la línea.
- **Decidido (punto 26):** opción **(a) rayas**.
  - **Una disciplina:** la línea va en su color al 55 %.
  - **Varias disciplinas:** tramos alternos de 10 px de cada color al 60 %, en el orden de `disciplines`.
  - **Fuente:** el campo `disciplines` del diseñador, no sus obras, así que el color no cambia al filtrar.
  - **Estados:**
    - elegido: línea en tinta, como hoy (falta confirmar en el punto 27);
    - relacionado: los colores de su línea al 100 %;
    - con foco: el color del foco.
  - La leyenda de la ayuda agrega «Diseñador de varias disciplinas (rayas)».
  - Se mostraron maquetas de (a) y (d) antes de decidir.

## 27. ✅ Los destacados y las curvas conservan su color (no negro)

- **Pedido:** al seleccionar algo o activar el filtro, las curvas y los destacados siguen su color original:
  - en contexto, curvas y texto en el color de su subcategoría;
  - las curvas hacia obras, en el color de su disciplina.
- **Propuesta:**
  - **Curvas:**
    - hacia un hecho de contexto o productivo: color de su fila (ya es así);
    - hacia una obra: color de la disciplina de la obra (hoy, gris);
    - hacia un diseñador: color de su línea, según el punto 26;
    - hacia movimientos, instituciones y teoría: gris neutro, que es su color.
  - **Relacionados:**
    - hechos: texto en negrita en el color de la fila (`--t-<fila>`) y barra en ese color al 100 %;
    - obras: etiqueta en negrita en el color de su disciplina y un anillo fino de ese color;
    - movimientos e instituciones: tinta y negrita (su color es neutro);
    - diseñadores: nombre en negrita y línea en su color al 100 %.
  - **El elegido:** se mantiene en tinta (negro o blanco) para distinguir «el elegido» de «los relacionados». Esto revisa en parte el punto 3.
  - **Con foco:** los elementos conectados ya usan el color del foco; no cambia.
- **Decidido:** el elemento elegido queda en tinta (negro, o blanco en tema oscuro); los relacionados van en sus colores.

## 28. ✅ Nombres de la escala: «Visual» y «Cronológica»

- **Pedido:** «Por densidad» pasa a ser «Visual» y «Lineal» pasa a ser «Cronológica».
- **Inglés:** «Visual» y «Chronological».
- **Ayudas que se actualizan:** los textos de ayuda (barra de filtros y eje: «en la escala “por densidad”…») y los tooltips de los botones.
  - Los tooltips se mantienen y explican la diferencia: «Visual: las décadas con más elementos son más anchas» / «Cronológica: todos los años miden lo mismo».
- **Sin conflicto:** «Cronológica» ya no se usa en Organizar, porque se reemplazó por «Por fecha» en el punto 16.
- **Lo que no cambia:** la clave guardada en el navegador (`lhd-scale`: uneven / linear), así que se conserva la preferencia de cada visitante.

## 29. ✅ «Foco» sin dos puntos

- **Pedido:** la etiqueta de la barra de filtros pasa de «Foco:» a «Foco».
- **Inglés:** «Lens:» pasa a «Lens».
- **Lo que no cambia:**
  - la etiqueta sigue en negrita, igual que «Disciplinas» (punto 6);
  - en la ayuda, «<b>Foco:</b>» funciona como título de párrafo y se mantiene.
- **Coherencia:** revisar que las otras etiquetas de la barra (Disciplinas, Organizar, Mostrar, Escala) tampoco lleven dos puntos.

## 30. ✅ El chip «✕ Solo: ___» más visible

- **Pedido:** cuando el filtro de una ficha está activo, el chip «✕ Solo: …» debe destacar para que se note y se quite fácil.
- **Propuesta:** chip invertido en tinta:
  - fondo negro, texto blanco en negrita y ✕ blanca;
  - en tema oscuro, fondo blanco y texto oscuro;
  - al pasar el cursor, un poco más claro.
- **Por qué funciona:** hoy los botones activos (focos, disciplinas) usan un gris claro, así que un chip negro se distingue de inmediato y se lee como «filtro encendido».
- **Riesgo:** si el foco también está activo, hay dos cosas marcadas a la vez. Se distinguen porque el foco es gris claro y «Solo» es negro.
- **Opcional:** un aviso breve la primera vez no es necesario; el color basta.


## 31. ✅ Productivo con un color propio (no gris)

- **Pedido:** «Productivo» deja de ser gris y pasa a tener un color propio.
- **Problema:** el gris actual se confunde con el neutro de movimientos, instituciones y curvas.
- **Qué hay que evitar:** los colores ya ocupados.
  - **Contexto:** político ladrillo, económico mostaza, social verde, cultural violeta, tecnológico azul.
  - **Disciplinas:** gráfico azul, producto naranja, moda rosa, arquitectura verde azulado.
- **Candidatos** (se mostraron maquetas sin tocar el sitio):
  - **(a) Café:** tono de taller y materiales. Es el más distinto de los demás, pero queda cerca del ladrillo y la mostaza si se mira rápido.
  - **(b) Petróleo:** azul verdoso profundo, de industria. Es vivo y se distingue, pero es vecino del azul de tecnológico y del verde azulado de arquitectura.
  - **(c) Oliva:** tono de máquina y de uniforme de trabajo. Es distinto de todos, pero es el menos vivo.
- **Lo que cambia:** el color del chip del foco, de la fila, de sus hechos y de sus curvas, y su versión para el tema oscuro (un tono más claro). El nombre interno `production` no cambia.
- **Decidido: (b) petróleo.**
  - Tema claro: `28, 128, 150` / texto `#155F70`.
  - Tema oscuro: un tono más claro (propuesta `86, 178, 196` / texto `#8CCAD8`).

## 32. ✅ Botones de Disciplinas con su color más visible

- **Pedido:** solo los botones de la barra (no la línea) muestran mejor el color de su disciplina, para que el color se lea como una dimensión de información.
- Se mostraron maquetas con tres variantes, en tema claro y oscuro, con «Moda» apagado para ver el estado inactivo:
  - **(A) Borde:** borde y texto del color de la disciplina, con un fondo muy suave.
  - **(B) Relleno:** fondo del color de la disciplina con texto blanco (oscuro en el tema oscuro).
  - **(C) Tinte:** fondo tenue del color y texto del color, en negrita, sin borde de color.
- **Apagado (las tres):** borde gris, texto gris y marcador desteñido, para que se note el contraste encendido/apagado.
- **Decidido: (A) borde.** Además, todas las disciplinas llevan su color también apagadas (Moda en rosa): borde tenue y texto del color, todo desteñido. Así se distingue encendido de apagado sin perder el color.


## 33. ✅ Al filtrar un movimiento (o una institución) se ven sus diseñadores, pero no sus obras

- **Qué pasa hoy:** el filtro «Solo» deja el elemento y sus relaciones directas.
  - Un movimiento se relaciona directamente con sus diseñadores, a través del campo `movements` del diseñador.
  - Las obras no tienen campo `movements`, así que para un movimiento son de segundo grado y se esconden.
  - Resultado: las líneas de vida aparecen vacías.
  - Ejemplo, Bauhaus: 11 diseñadores y 15 obras de ellos, todas entre 1919 y 1933, sin que se vea ninguna.
- **Por qué es un problema:** sin obras, el filtro de un movimiento no muestra lo que el movimiento produjo.
- **Propuesta:** al filtrar un movimiento, se muestran también las obras de sus diseñadores hechas durante el movimiento (entre su inicio y su fin).
  - Ejemplo: de Breuer se ven las obras de Bauhaus, pero no sus edificios de los años 60.
  - Esas obras van sobre la línea del diseñador, sin curva propia, porque su relación es a través del diseñador.
  - La curva sigue yendo del movimiento al diseñador.
- **Lo mismo para instituciones:**
  - las obras de los diseñadores ligados a la institución, mientras existió;
  - las obras que la institución produjo (`maker`), que ya se ven.
- **Alternativa B:** todas las obras de esos diseñadores, sin límite de fechas. Es más simple, pero mezcla etapas.
- **Alternativa C:** agregar `movements` a las obras en los datos. Es lo más preciso, pero requiere curaduría obra por obra.
- **Foco:** sin cambios. Con un foco activo, una obra se ve solo si ella misma está conectada.
- **Decidido: A, por período**, para movimientos e instituciones. Una institución sin fecha de cierre cuenta hasta hoy.

## 34. ✅ Botones ⟷ y |⟷| demasiado parecidos

- **Pedido:** los dos botones del eje (línea completa y ajustar a lo que se muestra) se confunden. Se buscan alternativas.
- Se mostraron maquetas de cuatro variantes:
  - **(A) Palabras:** «Todo» y «Ajustar».
  - **(B) Íconos distintos:** |—| para la línea completa y [•] (corchetes alrededor de un punto) para lo que se muestra. Mismo ancho que hoy.
  - **(C) Ícono + palabra:** «⟷ Todo» y «embudo Visible». El embudo se asocia con el botón de filtro de las fichas, que es justamente lo que reduce lo visible.
  - **(D) Segmentado:** «Todo | Ajustado» como un interruptor de dos posiciones; la opción activa queda en negro.
- **Riesgo con A, C y D:** el texto ensancha la esquina del eje y la descalza de la columna de nombres.
  - Arreglo posible 1: acortar «De … a …» a solo los dos años con un guion («1750 – 2026»).
  - Arreglo posible 2: pasar los botones a una segunda línea bajo los años.
- **Notas sobre las variantes:**
  - D aclara el estado: se ve si la línea está completa o ajustada.
  - Con D, «Ajustado» deja de estar activo apenas uno mueve el zoom, porque entonces no es ni una cosa ni la otra.
- **Decidido: (A) palabras «Todo» y «Ajustar»**, con el rango acortado a «[1750] – [2026]» (se quitan «De» y «a»).
  - En inglés: «All» y «Fit».
  - Se mantienen los tooltips: «Ver la línea completa» y «Ajustar a lo que se muestra».
  - El eje debe quedar alineado con la columna de nombres.
  - Se actualizan la ayuda y su imagen.

---
# Observaciones de contenido (ronda 1, 3 oct 2026): en conversación, no implementar todavía

Las definiciones que se acuerden aquí deben quedar en los manuales de creación de contenido, para las fases siguientes (ver punto 42).

## 35. ✅ Tres niveles de detalle: Imprescindible, Normal, Completo

- **Pedido:**
  - Todos los elementos de diseño (movimientos, instituciones, teoría, diseñadores, obras) llevan un nivel.
  - Los imprescindibles se marcan con ★.
  - El contexto es siempre visible en todos los niveles.
  - Junto a Disciplinas va «Detalle» con tres botones.
  - Las fichas siempre están completas, con todas sus conexiones. Al ir a un elemento de otro nivel, cambia el modo de detalle.
- **Propuesta:**
  - Campo `level` en los datos (`essential` / `normal` / `complete`). `star` se reemplaza por `level: essential`.
  - Los niveles son acumulativos: Normal muestra imprescindible + normal, y Completo muestra todo.
  - El chip «Imprescindibles» de Mostrar se quita: lo reemplaza Detalle.
  - Al navegar a un elemento de un nivel mayor, el detalle sube a ese nivel y se avisa con un mensaje breve. Nunca baja solo.
  - Nivel por defecto: Normal.
  - Clasificación inicial: las 29 obras ★ quedan como imprescindibles. Para el resto se propone una lista para revisión. Completo queda casi vacío hasta que se agregue contenido nuevo.
- Pendiente de respuesta: nivel por defecto; reglas de cuándo un diseñador o un movimiento es imprescindible; si el nivel de un diseñador depende del de sus obras.

## 36. ✅ ¿Eliminar las épocas? → macromovimientos

- **Pedido:** eliminar las épocas. Modernismo y Posmodernismo pasan a ser macromovimientos con ficha especial (más contexto, en todos los factores). La Revolución Industrial pasa a ser un hecho de contexto.
- **Propuesta:** ver la conversación.
- **Puntos a resolver:**
  - qué pasa con «Reforma» (1851–1914) y «Posguerra» (1945–1975);
  - dónde va el contenido de las fichas de época (resúmenes por factor, cambios clave);
  - el minimapa del tiempo, que hoy colorea por época;
  - la organización interna de `src-data/<época>/`, que puede quedar igual.
- Pendiente de respuesta.

## 37. ✅ (en parte) Todo diseñador tiene obras; más obras en general

- **Hoy:** 59 diseñadores y 92 obras. Hay 4 diseñadores sin obras: Moholy-Nagy, Piet Zwart, Norman Bel Geddes y Hannes Meyer. Los cuatro son importantes, así que se les agrega al menos una obra cada uno.
- **Regla para el manual:** un diseñador entra a la línea solo con al menos una obra relevante y verificada; sin obra, no entra.
- **Propuesta de meta:** al menos dos obras por diseñador importante, y llevar el Modernismo de 92 a unas 130 a 150 obras.
- Pendiente de respuesta: meta.

## 38. ✅ Ficha «Acerca de la línea de tiempo»

- **Estructura:**
  1. Presentación y propuesta conceptual.
  2. Secciones.
  3. Qué es cada tipo de elemento.
  4. Datos generales y cuantitativos.
  5. Enlace «Cómo se usa», que abre la ayuda.
  6. Aviso final: «Proyecto en desarrollo; puede contener errores».
- **Se quitan:** las instrucciones de uso.

## 39. ✅ Fichas: quitar «Buscar en» y «Dónde verla»; «Saber más» con fuentes

- **«Saber más»:**
  - los enlaces a la fuente, que hoy están en «Dónde verla»;
  - páginas relevantes de empresas, museos, archivos y fundaciones;
  - sin Wikipedia.
- Pendiente de respuesta: ¿se mantiene el enlace «Ver imágenes en Wikimedia Commons» y la imagen que se obtiene por la API? No es Wikipedia, pero es del mismo ecosistema.

## 40. ✅ Las conexiones que muestra la ficha deben verse todas en la línea (error)

- **Causa:** la ficha muestra conexiones heredadas, que el filtro y las curvas no usan.
  - La ficha de un diseñador junta el contexto propio y el de sus obras («Vía: obra»). Las curvas y «Solo» usan solo los enlaces directos.
  - Ejemplo, Chanel: tiene enlaces directos a político, social y tecnológico; a económico y cultural llega solo a través del vestido negro.
  - Ejemplo, el pequeño vestido negro: la ficha muestra Art déco a través de su diseñadora, pero la obra no tiene enlace propio a Art déco, así que no hay curva.
- **Propuesta:**
  - Toda conexión que muestra una ficha se dibuja y entra en «Solo».
  - Las heredadas («vía …») se marcan en la nota de la curva.
  - Pendiente de respuesta: si también van con un trazo distinto (más fino o punteado).

## 41. ✅ (CERRADO el 4 de octubre de 2026 por Mauricio; lo cubren el plan de cierre y la etapa 6) El contexto como centro del análisis

- **Hoy:**
  - obras: 61 de 92 tienen algún enlace de contexto;
  - diseñadores: 16 de 59;
  - movimientos: 9 de 11;
  - instituciones: 7 de 17;
  - teoría: 0 de 14;
  - hechos de contexto: 40.
- **Meta:** que cada obra, diseñador, movimiento, institución y texto tenga enlaces de contexto donde haya una relación verificable, sin forzarlos. Agregar hechos de contexto donde falten.
- **Base:** ver las lecciones de la literatura en la conversación (por ejemplo, la mediación).

## 42. ✅ Manuales de contenido

- Las definiciones de los puntos 35 a 41 se escriben en un manual general de contenido, `tools/MANUAL-CONTENIDO.md`, que sirva para todas las fases.
- **Contenido del manual:** niveles, reglas de inclusión, tipos de ficha, método de enlaces de contexto y fuentes permitidas.
- `GUIA-REDACCION-FASE1.md` queda como antecedente histórico.

### Decisiones de la persona responsable (3 oct 2026) sobre los puntos 35 a 42

- **35. Niveles de detalle:** sí.
  - Por defecto, Normal.
  - El nivel de un diseñador depende de sus obras y de su importancia histórica.
  - Las 29 obras ★ se mantienen. El resto se reparte en Normal (60–70 %) y Completo (30–40 %).
  - Propuesta para revisión en `tools/PROPUESTA-NIVELES.md`, con una regla: un diseñador tiene al menos una obra de su nivel o de uno más básico.
  - Falta decidir el caso de Rodchenko y Tschichold.
- **36. Épocas:** se eliminan.
  - Modernismo y Posmodernismo pasan a ser macromovimientos con ficha especial.
  - Reforma y Posguerra se eliminan.
  - La Revolución Industrial pasa a ser un hecho de contexto.
- **37. Diseñadores sin obras:** sí, con la meta propuesta (al menos dos obras por diseñador importante; 130–150 obras en el Modernismo). Se agregan obras a Moholy-Nagy, Zwart, Bel Geddes y Meyer.
- **38. Ficha «Acerca de»:** sí.
- **39. Fichas:**
  - Se mantiene la imagen.
  - Se quitan el enlace y el texto visibles de Wikimedia Commons; al hacer clic en la imagen se abre su fuente.
  - Se quitan «Buscar en» y «Dónde verla»; «Saber más» queda sin Wikipedia.
- **40. Conexiones indirectas:** todas se dibujan, con una línea más fina, y entran en «Solo».
- **41. Contexto:** primero se ajusta el manual; después se hace la revisión y ampliación del contenido.
- **Lecciones de la literatura:** se incorpora solo la 1 (manual, sección 9.1); las demás no se incorporan.

### Implementación v20 (3 oct 2026)

- **35. Niveles de detalle:**
  - Campo `level` en los datos; `star` ya no se escribe a mano (el build lo calcula).
  - Botones «Detalle» junto a Disciplinas; Normal por defecto.
  - Al ir a un elemento de un nivel mayor, el detalle sube solo y aparece un aviso.
  - Desaparece el chip «Imprescindibles» de Mostrar.
  - La ★ aparece junto al nombre de todo lo imprescindible en la línea y en las fichas.
  - Obras ★: 32 (las 29 de antes, más «Libros» de Rodchenko, *Die neue Typographie* y los Libros de la Bauhaus de Moholy-Nagy).
- **36. Épocas:**
  - Se quitan la barra de épocas, la ficha de época, las líneas verticales de época y los colores de época del minimapa (ahora lleva marcas por siglo).
  - Primera fila de DISEÑO: «Macromovimientos», con Modernismo (1907–1970) y Posmodernismo (1966–1995), cada uno con ficha especial: contexto factor por factor, cambios clave, rasgos y movimientos que reúne.
  - La ficha de foco resume «Por macromovimiento».
  - Nuevo hecho de contexto: «Revolución Industrial» (económico, c. 1760–1840).
- **37. Obras nuevas (verificadas con fuentes):**
  - Libros de la Bauhaus (Moholy-Nagy, 1925–1930, ★);
  - Catálogo de NKF (Piet Zwart, 1927–1928);
  - Escuela sindical de la ADGB en Bernau (Hannes Meyer, 1928–1930);
  - Futurama (Bel Geddes, 1939).
  - Todas con enlaces de contexto. El build da `PROBLEM` si un diseñador no tiene obras.
- **38. Ficha «Acerca de»:** presentación conceptual, secciones, qué es cada elemento, datos, botón «Cómo se usa» (abre la ayuda) y aviso de proyecto en desarrollo.
- **39. Fichas:**
  - Sin «Buscar en» ni «Dónde verla».
  - «Saber más» lista las fuentes (`where`), sin Wikipedia.
  - Sin imagen libre no se muestra imagen ni texto.
  - La imagen enlaza a su página de origen.
- **40. Conexiones indirectas:** se dibujan con línea fina y entran en «Solo».
  - Un diseñador hereda el contexto de sus obras.
  - Una obra hereda los movimientos e instituciones de su diseñador.
  - Un movimiento o una institución incluye las obras de sus diseñadores durante su período.
  - La nota de la curva dice «Vía: …».
- **42. Manual:** `tools/MANUAL-CONTENIDO.md`.

## 43. ✅ Fase A: listas de ampliación del Modernismo (implementado en v21; quedan A6, parte de A2 y la revisión independiente)

- **Propuesta:** `tools/LISTAS-FASE-A.md` (3 oct 2026), sobre los datos de v20.
- **Decisión de la persona responsable (3 oct 2026): aprobadas todas las propuestas recomendadas (R)**, incluidas estas recomendaciones:
  1. **H6, alfabetización:** un solo hecho social para la URSS (*likbez*), México (SEP) y España.
  2. **H3, Era Vargas:** entra, aunque el contexto político quede con 11 hechos, uno sobre la meta de 6 a 10.
  3. **Diseñadores:** se aceptan 71 en el tramo, uno sobre el rango de 45 a 70 de `SPEC.md`.
  4. **Sin segunda obra forzada** para Renner, Vionnet, Schütte-Lihotzky (salvo que se confirmen las escuelas en Turquía), Ginzburg ni Porsche.
     - La Biblioteca Central de la UNAM de O’Gorman pasa a la fase B.
     - El Volkswagen en serie también pasa a la fase B.
  5. **No entran:** GOELRO, «Arte degenerado», la crisis del salitre ni los grandes almacenes.
  6. **Opcionales** (sección 2.4 y teoría T1–T3): quedan en reserva. Solo entran si alguna obra recomendada no se puede verificar.
- **Alcance aprobado:**
  - 8 hechos de contexto (H1–H8);
  - 44 obras (139 en el tramo, 37 ★);
  - 13 diseñadores nuevos;
  - el plan de enlaces A2.
- **Verificación hecha (3 oct 2026):** en `tools/VERIFICACION-FASE-A.md`.
  - Se ajustan fechas y matices; América Latina queda con 10 obras.
  - Quedan dos preguntas: O1 (Moholy-Nagy) y O10 (Méndez).
- **A1 en curso (3 oct 2026):** `tools/REVISION-ENLACES-MODERNISMO.md`.
  - Resultado: 131 enlaces se mantienen, 12 se reescriben, 3 se trasladan a otro hecho y 9 se eliminan.
  - Fuentes registradas para los 146 enlaces que siguen: unos 115 con fuente y unos 30 con ⚠.
  - Se proponen reescribir L131 y L138 (Tatra: Ledwinka y Übelacker, no Jaray) y L133.
  - Correcciones en la sección 7: *El Peneca*, Stölzl, Cassandre, Deauville, el cartel *Power* y el `where` del vestido langosta.
  - Correcciones encontradas: fecha de Deauville y enlace `where` del vestido langosta (sección 7).
  - **Decidido (3 oct 2026):** CORFO y Primeras transmisiones de televisión se retiran del Modernismo y se recuperan en la fase B (CORFO → INTEC; la televisión, con su efecto en el diseño de posguerra).
  - Corrección encontrada: el cartel *Power* es de 1930 (MoMA), no de 1931. de los 154 enlaces y el plan de ids y matriz de enlaces. **No se implementa hasta «implementa».**

## 44. ✅ Fuentes numeradas en la revisión de cada ficha (modo `?editar`; implementado en v21)

- **Pedido (3 oct 2026):**
  - En el modo `?editar`, dentro de la sección «Revisión» de cada ficha, una subsección **«Fuentes»** con las fuentes de información y de verificación, con enlace directo.
  - Si se puede, las afirmaciones del texto llevan un **número en superíndice** y las fuentes van numeradas en cada ficha. Sirve para la revisión.
- **Propuesta (sin implementar):**
  - **Campo nuevo `refs`** en cada elemento de `src-data/`: `[{label, url, checks, date}]`. El número es la posición en la lista.
    - `checks`: qué verifica (por ejemplo, «fecha y atribución»).
    - `date`: cuándo se consultó.
  - **Marcas en el texto:** `[1]`, `[2]`… al final de la frase que sostienen, en EN y ES con los mismos números.
    - En el sitio normal se borran: no se ven ni se buscan.
    - En `?editar` se ven como superíndices; al hacer clic se baja a la fuente.
  - **Separación de campos:** `refs` es interno, para verificar. «Saber más» (`where`) sigue siendo lo público. Una misma fuente puede estar en ambos.
  - **Build:**
    - da `PROBLEM` si una marca no tiene fuente o si la URL no es https;
    - da `WARN` si una fuente no se usa en el texto o si es de Wikipedia.
  - **Pruebas:** se amplía `test_editar` (superíndices visibles solo en `?editar`; el texto público sin marcas).
- **Decisiones de la persona responsable (3 oct 2026):**
  1. Las fuentes van en `src-data/` y las escribe Claude. En `?editar` son de solo lectura; no hace falta agregarlas desde ahí.
  2. **Alcance:** desde ya en todo lo de la fase A (A1 a A4).
     - Las fichas existentes se completan en una tarea propia del plan (**A6**), antes de pasar a los otros tramos.
     - Son 264 elementos en `all.json`, no 246.
  3. Los enlaces de contexto llevan fuentes propias.
  4. Sin maqueta. Más adelante puede haber cambios menores de formato.
  5. **Lo importante es la trazabilidad:** guardar la información desde ahora en toda tarea de revisión.
- **Documentado:**
  - `MANUAL-CONTENIDO.md` 7.1 y lista de control;
  - `PLAN-FASES.md` (procedimiento común, A0 y A6);
  - `GUIA-REDACCION-FASE1.md`;
  - `SPEC.md`;
  - `INICIO-SESION-NUEVA.md`.
- **Interfaz y build (A0):** esperan «implementa».

## 45. ✅ Decisiones del 3 oct 2026 sobre los pendientes abiertos

- **Orden de trabajo:** primero la revisión independiente de lo nuevo de v21 (en `tools/REVISION-INDEPENDIENTE-FASE-A.md`) y después A6.
- **Filtro «Solo» de la Bauhaus:** se deja como está; sigue mostrando a Taut y a Le Corbusier por las obras compartidas. **Cerrado.**
- **Fechas de los macromovimientos:** se confirman Modernismo 1907–1970 y Posmodernismo 1966–1995. **Cerrado.**
- **Conceptos:** **sí** se muestran también en la ficha del macromovimiento (pendiente 6). ✅ Implementado en v22.
- **Proporciones de niveles:** 37 ★ (27 %), 71 en Normal y 30 en Completo. Aprobadas. **Cerrado.**
- **Fichas de `?editar` con fuentes numeradas:** aprobadas como están. **Cerrado.**

## 46. ✅ Revisión independiente de la fase A (v21)

- **Informe:** `tools/REVISION-INDEPENDIENTE-FASE-A.md` (3 oct 2026). Lo hizo un agente que no escribió el contenido.
- **Resultado:** 11 errores, 29 dudosos y 21 de estilo. Cada hallazgo trae su evidencia y una propuesta de texto en EN y ES.
- **Errores principales:**
  - el nombre de nacimiento de Adrian;
  - la ficha del Frye usada como fuente seis veces sin sostener el contenido;
  - fuentes cuyo `checks` dice más de lo que dice la página (Kubus, Popover, el museo de Neurath «independiente»);
  - el proyecto ganador del Ministerio de Río era «marajoara» y no «neocolonial»;
  - las ocho páginas de Vogue no eran todas del vestido langosta;
  - las divisiones de carteles de la WPA eran 17 estados más D. C.;
  - los carteles de Beall eran litografías;
  - Campari trabajó con varios artistas;
  - el contexto «Migraciones y exilios» no corresponde a Brodovitch, a Breuer ni al Grupo Austral.
- **Dudosos:**
  - la fecha del logotipo de Johnston (1916 o 1917);
  - Klutsis y los tirajes;
  - la nota sobre el teléfono modelo 302;
  - cuatro enlaces que son solo coincidencia (Vionnet ↔ revistas de moda, el bar de Perriand ↔ trabajo de las mujeres, Chanel ↔ cine sonoro, Méndez ↔ muralismo);
  - las escuelas de O’Gorman (seis o unas 25).
- **Vacíos:**
  - los 13 diseñadores nuevos no tienen enlaces propios;
  - tres obras nuevas quedaron sin enlaces;
  - la Revolución mexicana tiene un solo enlace.
- **Propuesta:** aplicar todas las correcciones del informe.
- ✅ **Implementado en v22** («implementa y sigue», 3 oct 2026). Detalle en la sección 5 del informe. Quedan para A6/A2: enlaces propios de Stam, Teague, Prouvé, Grupo Austral y McCardell; enlaces de Deere, Co-op y Clichy; cobertura de la Revolución mexicana y del teléfono; obras ★ con un solo enlace; museo para el cartel ¡Libros!; DBH 1001; fechas generales de NEP, Vargas y Revolución mexicana.


## 47. ✅ A6, lote 1: fuentes de las 30 obras ★ (v23)

- **Hecho:** las 30 obras ★ que no tenían `refs` ahora tienen de 2 a 7 fuentes cada una (museos, archivos, sitios oficiales; sin Wikipedia) y marcas `[n]` en EN y ES. Registro completo en `tools/A6-LOTE1-FUENTES.md`.
- **Ojo con el protocolo:** el plan dice que en A6 lo que no se sostiene se registra y **no se corrige sin aprobación**. En este lote las correcciones de contenido **ya se aplicaron** junto con las fuentes. Si prefieres revisarlas antes, v22 es el estado anterior.
- **Correcciones más visibles:**
  - KdF-Wagen: lo encargó la asociación de la industria automotriz (1934), no Hitler; más de 330.000 ahorrantes y ninguno recibió auto; sin Karl Rabe.
  - Tipografía Johnston: la cita de Pick era otra; mayúsculas en junio de 1916 y minúsculas en julio.
  - Mapa del metro: 750.000 ejemplares en enero de 1933.
  - Narkomfin: 1928–1930; todos los departamentos tenían cocina; Le Corbusier retomó su planta.
  - Utility: diseños de Clinch y Cutler; el plan duró hasta 1952.
  - Pequeño vestido negro: la frase de Vogue era «the frock that all the world will wear».
  - Vestido langosta: Paul Sache era diseñador, no una empresa.
  - Adolf, el superhombre: las monedas forman el esófago.
  - Cartel de Kitchener: cliente London Opinion.
  - Medias de nailon: sin los «64 millones de pares» (sin fuente).
- **Pendiente de contrastar:** Weissenhof (21 semanas, 21 edificios), infusor de Brandt («primera mujer admitida»), Kitchener (30.000 hombres al día) y el papel de Lilly Reich en miesbcn.com.
- ✅ **Aprobado** (4 oct 2026): las correcciones se mantienen. Sigue el lote 2 (obras Normal y Completo).


## 48. ✅ Solo dos niveles de detalle: «Imprescindibles» y «Normal» (4 oct 2026)

- **Pedido:** se elimina el nivel «Completo». Las obras que hoy están en Completo pasan a Normal. Ya no hace falta ampliar el catálogo para llenar Completo. Cuando la línea esté terminada se reevaluará un nivel de alto detalle.
- **Implica:**
  - Datos: `level: "complete"` pasa a `"normal"` (30 obras y los diseñadores o elementos que lo tengan).
  - Interfaz: quitar el botón «Completo» y la subida automática de nivel con aviso al abrir un elemento de Completo.
  - Build y pruebas (`test_v20`) ajustados.
  - Manuales y listas: `MANUAL-CONTENIDO.md` (niveles e inclusión), `PROPUESTA-NIVELES.md`, `GUIA-REDACCION-FASE1.md`, `SPEC.md`, `LISTAS-FASE-A.md`, `INICIO-SESION-NUEVA.md`.
  - Replanificar `PLAN-FASES.md`: la meta de 130–150 obras deja de ser criterio; las fases B (1750–1914) y C/D (1945–hoy) se dimensionan solo con ★ y Normal.
- ✅ **Implementado en v24.** 48 elementos pasaron de Completo a Normal; manuales, listas y `PLAN-FASES.md` replanificados (A4 cerrada con 138 obras; tamaños de las fases B a E reducidos).

## 49. ✅ La página abre con todo el contexto colapsado (4 oct 2026)

- **Pedido:** al cargar, todas las filas de contexto aparecen cerradas.
- **Decisión:** sí, incluye «Productivo».
- El estado de filas abiertas no se guarda entre visitas, así que siempre abrirá colapsado.
- ✅ **Implementado en v24.**

## 50. ✅ Macromovimientos dentro de «Movimientos» (4 oct 2026)

- **Pedido:** sin fila propia; se comportan como cualquier movimiento (ocultar, «Solo»/pintar, foco, niveles, búsqueda).
- **Propuesta (aprobada):** van primero dentro de la fila «Movimientos», con el mismo estilo de barra que los demás. La ficha sigue siendo la del macromovimiento (contexto por factor, cambios clave, partes, conceptos).
- **Ojo:**
  - la barra del Modernismo (1907–1970) es muy larga y ocupará una franja completa arriba de los movimientos;
  - hay que quitar la fila y el interruptor propios de macromovimientos, y ajustar `test_v20` y `test_general`.
- ✅ **Implementado en v24.** La etiqueta del Modernismo se desliza para seguir visible mientras su tramo está en pantalla (empieza en 1907, antes de la vista por defecto).

## 51. ✅ Contraseña de `?editar`: «lhd» (4 oct 2026)

- **Pedido (confirmado):** cambiar la constante `CLAVE` de `editar.php` a `lhd`.
- **Ojo:** es muy fácil de adivinar. Sirve mientras el sitio sea interno; antes de publicar hay que cambiarla (ya está anotado).
- Ajustar `test_editar` y `test_v21`, que usan la contraseña actual.
- ✅ **Implementado en v24.**


## 52. ✅ A6, lote 2: fuentes de las 62 obras Normal (v25)

- **Hecho:** las 62 obras Normal que no tenían `refs` ahora tienen de 2 a 7 fuentes y marcas `[n]` en EN y ES. **Las 138 obras del Modernismo quedan trazadas.** Registro completo en `tools/A6-LOTE2-FUENTES.md`.
- Igual que en el lote 1, las correcciones de contenido **ya se aplicaron** (v24 es el estado anterior). Un revisor independiente contrastó 12 correcciones clave (todas confirmadas) y encontró 6 problemas menores en otras frases, ya corregidos.
- **Correcciones más visibles:**
  - Casa Modernista (Warchavchik): no tenía techo plano, sino de tejas oculto tras un parapeto.
  - Club Rusakov: Mélnikov hizo seis clubes, cinco en Moscú.
  - Villa Tugendhat: sin la «planta del Pabellón de Barcelona»; el ónix vino de la misma firma.
  - Siedlung Herradura: 1925–1930.
  - Sonia Delaunay: Casa Sonia abrió en 1918; sin la frase atribuida a Apollinaire.
  - Chanel N.º 5: frasco cuadrado. Jeep: Probst, ingeniero contratado por Bantam.
  - Pabellón de L’Esprit Nouveau: sin «sillas Thonet» ni Plan Voisin.
  - Gill Sans: «influida por» Johnston; Cassandre ganó el gran premio con Au Bûcheron.
  - Varias cifras de producción sin fuente quitadas (De Stijl, DBH 1001, Gill Sans…).
- **Sin verificar:** el tapiz de Anni Albers (Harvard y la fundación no abrieron); páginas de «Saber más» que no se pudieron abrir (lista en el registro).
- ✅ **Aprobado** (4 oct 2026). Siguen los lotes de diseñadores (56), hechos de contexto (34), instituciones (16), teoría (14), productivos (16) y movimientos (11).

---
# PENDIENTES PARA RECORDAR (después de v20)

1. ✅ (CERRADO el 4 de octubre de 2026 por Mauricio; cubierto por el plan v8) **Revisión y ampliación del contenido (punto 41).** Es la próxima etapa grande.
   - **Enlaces de contexto directos** (hoy):
     - diseñadores: 16 de 59;
     - teoría: 0 de 14;
     - instituciones: 7 de 17;
     - movimientos: 9 de 11;
     - obras: 66 de 96.
   - Agregar hechos de contexto donde falten (hoy hay 41).
   - Seguir el método del manual (sección 5).
2. ✅ (CERRADO el 4 de octubre de 2026 por Mauricio; cubierto por el plan v8) **Más obras (punto 37).**
   - Meta: 130–150 en el Modernismo.
   - 34 diseñadores imprescindibles o normales tienen una sola obra, entre ellos Bayer, Van Doesburg, Johnston, Renner, Beck, Heartfield, Stepanova, Isotype, Wagenfeld, Eileen Gray, Perriand, Dreyfuss, Vionnet, Sonia Delaunay, Anni Albers, Schütte-Lihotzky, Melnikov, Ginzburg y O’Gorman.
3. ✅ (CERRADO el 4 de octubre de 2026 por Mauricio; cubierto por el plan v8) **Clasificación de niveles:** quedó «ok por ahora» (`tools/PROPUESTA-NIVELES.md`); revisarla cuando entre contenido nuevo.
4. ✅ (CERRADO el 4 de octubre de 2026 por Mauricio; cubierto por el plan v8) **Posmodernismo:**
   - el macromovimiento no tiene aún movimientos («parts» vacío) ni enlaces de contexto propios;
   - se completa al escribir el tramo 1945–hoy;
   - confirmar sus fechas (1966–1995) y las del Modernismo (1907–1970).
5. ✅ (CERRADO el 4 de octubre de 2026 por Mauricio; cubierto por el plan v8) **Tramos sin contenido:**
   - 1750–1914 y 1945–hoy solo tienen elementos de prueba (Taylorismo, el computador personal, Susan Kare y los íconos del Macintosh) y la Revolución Industrial;
   - decidir cuándo se escriben y si el contenido de prueba se reemplaza.
6. ✅ (CERRADO el 4 de octubre de 2026 por Mauricio; cubierto por el plan v8) (punto 45, v22: también en la ficha del macromovimiento) **Conceptos:**
   - los 8 conceptos del Modernismo se mostraban en la ficha de época;
   - ahora solo aparecen en las fichas de los elementos que los usan;
   - decidir si van también en la ficha del macromovimiento.
7. **Lecciones de la literatura académica (decidido el 3 de octubre de 2026):** se incorpora **solo la 1**, «la conexión de contexto debe ser más profunda que una coincidencia de fechas», con su prueba de tres preguntas (manual, sección 9.1). Las demás no se incorporan.
8. ✅ (punto 45: se deja así) **Filtro «Solo» de Bauhaus:** también muestra a Bruno Taut y a Le Corbusier porque comparten obras con diseñadores de la Bauhaus. ¿Se dejan o se limitan a los diseñadores del movimiento? Pregunta abierta desde v19.2.
9. ✅ (CERRADO el 4 de octubre de 2026 por Mauricio) **Revisar las cuatro obras nuevas** (textos y fuentes) en la próxima sesión de revisión.
10. **Fuentes numeradas (punto 44):** implementado en v21. Falta trazar las fichas existentes (A6) antes de la fase B: en v25, 163 de 310 elementos del Modernismo (todas las obras) y 225 de 232 enlaces tienen `refs` (lotes 1 y 2, puntos 47 y 52).
11. **Fase A pendiente (v21):**
    - **A2 incompleto:**
      - teoría con enlace propio: 8 de 14 (faltan «Topografía de la tipografía», «bauen», «The Crystal Goblet», *Art and Industry*, *Pioneers* y *Space, Time and Architecture*);
      - diseñadores con enlace propio: 31 de 71;
      - instituciones: 12 de 17.
      - Solo se agregaron los que tienen fuente.
    - **Obras ★ con un solo enlace:** 14 (entre ellas Silla Roja y Azul, Wassily, Barcelona, Paimio, Van Nelle y el Ministerio de Río).
    - ✅ **Revisión independiente** de lo nuevo (`tools/REVISION-INDEPENDIENTE-FASE-A.md`), aplicada en v22.
    - **Puntos con ⚠** en las fuentes: buscarlos en `refs[].checks` o en `tools/REVISION-ENLACES-MODERNISMO.md`.
    - **Obra en reserva:** *Het boek van PTT* (Zwart, 1938), sin fuente sobre su contenido.

53. ✅ **A6, lote 3 (v26): fuentes de los 56 diseñadores** (con verificación de fechas de vida). Registro en `tools/A6-LOTE3-FUENTES.md`; revisor independiente: 12 correcciones clave, ninguna refutada. Aprobado el 4 de octubre de 2026. Quedan para A6: 34 hechos de contexto, 16 instituciones, 14 teorías, 16 productivo y 11 movimientos.

54. **A6, lote 4 y A2 (v27): trazabilidad de 130 elementos y 23 enlaces nuevos.** Ver `tools/A6-LOTE4-FUENTES.md`. Aprobado por ti: «termina A6» y «termina toda la fase 2». ✅ **Aprobado por Mauricio el 4 de octubre de 2026** (correcciones de A6 lote 4). Lo que quedó sin fuente sigue en la Parte II. Quedan sin fuente por límite de búsquedas web de la sesión: Cranbrook, Revolución Industrial (y su enlace con el Modernismo), macromovimiento Posmodernismo, y varias frases de Leica, rayón y cromado.

55. **Plan de cierre del sitio** (`tools/PLAN-CIERRE.md`, v1): reemplaza las fases B–F de `PLAN-FASES.md`. Tamaños reducidos, ids fijos antes de redactar, tres vistos buenos (plan, listas maestras, revisión final) y reglas R1–R6 de aprobación automática. ✅ Reemplazado por el plan v4 (punto 58).

56. **Más obras, menos revisión** (4 de octubre de 2026): no se recorta la cantidad de obras; el ahorro de esfuerzo viene de reducir la revisión. `PLAN-CIERRE.md` queda con 210 obras nuevas (348 en total: Posguerra 70, Reforma 45, Posmoderno 65, Industrial 30), sin revisión independiente ni capturas por tramo (una sola global), fuentes proporcionales (R7–R9) y unas 19 sesiones. ✅ Reemplazado por el plan v4.

57. **Contenido y conexiones primero; fuentes y revisión aparte** (4 de octubre de 2026): `PLAN-CIERRE.md` v3. Parte I escribe ~245 obras nuevas (383 en total), 120 diseñadores, 115 hechos de contexto y ~430 enlaces, sin fuentes (`refs: []`); Parte II (R1–R5) trae fuentes y revisión por lotes, separada; solo R1 y R5 son obligatorias antes de publicar. ✅ Reemplazado por el plan v4 (punto 58).

58. **Proporción de contenido según la importancia histórica; recorte del Modernismo** (4 de octubre de 2026). Pregunta: ¿los períodos quedan con contenido razonable frente al Modernismo actual? Respuesta: no del todo; Posguerra y Posmoderno quedaban flacos. Decisión: **opción con recorte**. `PLAN-CIERRE.md` v4: **380 obras en total (121 ★)** = Industrial 30, Reforma 55, Modernismo 100 (de 138; se recortan 38 Normal, 16 diseñadores y 6 hechos de contexto, nada ★), Posguerra 100, Posmoderno 95; 163 hechos de contexto, 188 diseñadores, ~705 enlaces. Obras nuevas a redactar: 280 (279 más los íconos del Macintosh, ya hechos). Parte I ~19 sesiones, Parte II ~15. El recorte lo elige Opus en la etapa 1 (paso 1.6, con la aprobación V1) y lo aplica un script (1.7); lo recortado queda en `RESERVA-FASE-B.json`. ✅ **V0 (plan) aprobado** con esta opción. Quedan V1 (listas maestras y lista de recorte) y V2 (sitio con todo el contenido). Además, en v29 se limpió el paquete (registros de fases anteriores, punto de retorno de la prueba por fecha) y se agregó `tools/pipeline/` para ejecutar el plan desde una sesión nueva.

59. **Fuentes visibles en el sitio público y revisión simplificada** (4 de octubre de 2026; **decidido, NO implementado**: se hace en la etapa previa P de `PLAN-CIERRE.md`, sección 5A, cuando la persona responsable lo ordene).
- Por transparencia, las fuentes (superíndices y lista numerada) se ven en el sitio real y en `?editar`.
- Cada ficha termina con la sección **«Fuentes»**, colapsable y **colapsada por defecto**. Si la ficha no tiene fuentes, el título lleva un **ícono de advertencia** (visible con la sección cerrada) y el texto dice que el contenido **no ha sido revisado**.
- En `?editar` se conserva el cambio de imagen con otro enlace. La sección «Revisión» pasa a **«Observaciones»** y queda solo el campo de texto (sin casilla «Revisada»).
- El resumen de revisión muestra: avance de la revisión por IA (fichas con y sin fuentes), fichas con observaciones humanas pendientes (si se borra el texto, salen de la lista) y fichas con la imagen cambiada manualmente.
- Supuestos confirmados en el punto 60 (salvo la nota de IA, que se quitó): «revisada por IA» = tiene `refs`; «Observaciones» va antes de «Fuentes» para que esta sea la última; el clic en un superíndice abre la sección.

60. **Ajustes al plan v6** (4 de octubre de 2026; decididos, no implementados salvo los documentos).
- **Sin nota de IA** en la sección «Fuentes»: solo la lista de fuentes o la advertencia. Los demás supuestos del punto 59 quedan confirmados.
- **Modelos:** el tipo A (decidir qué entra y cómo se conecta) pasa de Opus alto a **Sonnet de esfuerzo medio**, para ahorrar recursos; Opus de esfuerzo medio solo si V1 muestra fallas graves.
- **Contraseña:** se elimina el cambio de clave antes de publicar. En la etapa P (paso P.2b) la clave de `?editar` pasa a **`lhd2026`** y queda así; se acepta que es insegura porque el sitio es personal.
- **ZIP único de continuidad** después de cada paso del plan (plan, sección 5B): todo el proyecto, probado en carpeta limpia, con `ESTADO-ACTUAL.md` y `LEEME-PROBAR-EN-WEB.md`. Primer ZIP de este tipo: `LHD-v29q.zip`.
- **Proporciones:** revisión en el plan, sección 3.2. **Propuesta pendiente de decisión:** Industrial 30, Reforma 60, Modernismo 120 (recorte de 18), Posguerra 90, Posmoderno 75 (375 en total). También queda por decidir cómo resolver la contradicción con C5 sobre los elementos japoneses.
- **Resumen de etapas y sesiones Claude** para seguimiento: documento aparte.

61. **Proporciones aprobadas y elementos orientales permitidos** (4 de octubre de 2026; plan v7, secciones 3, 3.0, 3.2 y etapas 2 a 4).
- **Obras: 375 en total** (antes 380): Industrial 30 (9 ★), Reforma 60 (18 ★), Modernismo 120 (37 ★), Posguerra 90 (27 ★), Posmoderno 75 (22 ★). Nuevas: 255.
- **Recorte del Modernismo reducido:** 18 obras Normal (gráfica 5, producto 5, arquitectura 5, moda 3), 8 diseñadores y 3 hechos de contexto; quedan 120 obras, 64 diseñadores y 39 hechos de contexto.
- Se ajustan también los demás tipos por tramo, las sesiones (Posguerra 4, Posmoderno 4, R2 4, R4 3) y el total: unas **32 a 33 sesiones Claude**.
- **Elementos orientales:** se permiten cuando tengan influencia demostrable en el diseño occidental (japonismo, metabolismo, Muji, Kawakubo, Yamamoto y similares), con una línea de mecanismo, `regions: ["global"]` y su país en `countries`; orientativo 6 a 10 en toda la línea. Paso 0.10 del plan: comprobar cómo se ven en los filtros y en «Organizar por región». Se actualizan `SPEC.md` (alcance regional) y, en la etapa 0, `MANUAL-CONTENIDO.md`.

62. ✅ **Etapa P implementada (v30)** (4 de octubre de 2026; orden «implementa» sobre los puntos 59 y 60). Ver `PROJECT.md`, entrada v30.
- Sitio público: superíndices y sección «Fuentes (n)» al final de cada ficha (cerrada al abrir; con triángulo de advertencia y mensaje «no ha sido revisada» si no hay fuentes). El clic en un superíndice abre la sección y resalta la fuente. Las fichas de época, foco e información no la llevan.
- `?editar`: «Revisión» pasa a «Observaciones» (solo texto; sin casilla «Revisada»); «Observaciones» va antes de «Fuentes». El resumen tiene tres bloques (revisión por IA, observaciones pendientes, imágenes cambiadas a mano); la exportación `.md` suma imágenes y la cuenta sin fuentes. El lápiz de imagen se conserva.
- Clave de `?editar`: `lhd2026` (sin cambio posterior). Pruebas: `test_v21` y `test_editar` ajustadas, `test_v30` nueva, todas PASS.
- Observación: con la advertencia visible, hoy solo muestran «no revisada» `macro-postmodernism`, `inst-cranbrook`, `ctx-industrial-revolution` y los 8 conceptos (los conceptos no tienen `refs`; decidir en la etapa 0 o en la Parte II si se les agregan o se les quita la sección).
- Pendiente de ti: mirar el sitio (ficha con fuentes, ficha sin fuentes, resumen en `?editar`) y comentar. El próximo punto es el **64**.

63. **Los conceptos también deben tener al menos una fuente** (4 de octubre de 2026; **decidido: se hace en la Parte II, lote R3, junto con contexto y teoría**; mientras tanto sus fichas muestran la advertencia «no revisada»).
- Hoy los 8 conceptos del Modernismo (`standardisation`, `functionalism`, `gesamtkunstwerk`, `streamlining`, `styling`, `corporate-identity`, `minimum-dwelling`, `grid`) tienen `refs: []` y por eso su ficha muestra la advertencia «no revisada».
- Trabajo necesario: (a) código: `rfPrepare` no incluye los conceptos, así que sus marcas `[n]` no funcionarían; hay que agregarlos (y a `srcCount`); (b) búsqueda de 1 a 2 fuentes por concepto con web (brief de la Parte II, `BRIEF-FUENTES.md`), con marcas `[n]` en `key` EN y ES; (c) el build ya admite el campo `refs`, falta que lo valide como aviso; (d) aplicar con `apply2.py` (revisar que acepte conceptos); (e) prueba nueva.
- Aviso: varias `key` de conceptos son largas (240 a 370 caracteres) y los avisos del build ya lo marcan; al agregar marcas conviene acortarlas.
- Regla para el futuro: los conceptos nuevos (deseable D2) también nacen con fuente.

64. ✅ **Etapa 0 implementada (v31)** (4 de octubre de 2026; orden «implementa la etapa 0»). Detalle en `PROJECT.md`, entrada v31.
- Hecho: build ajustado (0.1), pipeline revisado (0.2), `validate_out.py` (0.3), `apply_new.py` (0.4), `EJEMPLOS.md` (0.5), briefs al día (0.6), scripts del recorte (0.7), `INICIO-SESION-NUEVA.md` (0.8), `empaquetar.sh` y plantillas (0.9), prueba de elementos orientales (0.10). Todas las pruebas PASS.
- Cambios respecto del plan: (a) el tipo de registro de los agentes es `rtype` y no `type` (choca con el tipo de obra); (b) elementos orientales: el grupo «Global» se subdivide en la zona «Más allá de Occidente» solo si existe alguno, y el filtro de región no los oculta (son `global`).
- **Hallazgo para la etapa 1:** hoy 37 obras y 13 diseñadores del Modernismo no tienen ningún enlace de contexto propio (el sitio los conecta de forma indirecta). La meta «toda obra con ≥ 1 enlace» del plan no se cumple en el Modernismo; hay que decidir en la etapa 1 (o en 8.5) si se agregan enlaces o se acepta. `candidatos_recorte.py` ya los pone primero entre los recortables. De las 139 obras, 62 están protegidas y 77 son recortables (el plan decía 79; el criterio de «citada en concepto o macromovimiento» se aplica por nombre).
- El próximo punto es el **65**.

65. ✅ (decidido el 4 de octubre de 2026: **sí se cuenta**; ver abajo) **Obras con enlaces indirectos** (4 de octubre de 2026; decisión sobre el hallazgo del punto 64; documentada en el plan, regla C4b, no hay código nuevo).
- La meta «toda obra con al menos un enlace de contexto» **puede cumplirse con enlaces indirectos**, aunque es preferible que sean directos. Queda resuelta la duda del punto 64: no hace falta agregar enlaces a las obras actuales del Modernismo solo para cumplirla.
- Definición usada (C4b): para una obra, indirecto = un productivo en `tech`, un enlace de contexto de alguno de sus diseñadores, o de un movimiento o institución de sus diseñadores; para un diseñador, un enlace de contexto de alguna de sus obras. Las ★ siguen con ≥ 2 enlaces directos de subcategorías distintas.
- Hoy en el Modernismo: 102 obras con enlace directo, 32 solo indirecto, 5 sin ninguno (`bauhaus-exhibition-poster`, `gill-sans`, `times-new-roman`, `faaborg-chair`, `coca-cola-bottle`); 6 diseñadores sin ninguno (`eric-gill`, `stanley-morison`, `perriand`, `kaare-klint`, `chareau`, `jean-prouve`). Las 5 obras son candidatas naturales al recorte (3 de ellas ya salen primero en `candidatos_recorte.py`).
- Pendiente de ti (opcional): ¿quieres que el build y la auditoría de la Parte II (R1) cuenten «con contexto directo / solo indirecto / sin contexto»? Hoy el build solo cuenta lo directo (`worksWithContext`). Se haría solo con tu «implementa».
- El próximo punto es el **67**.

66. **V1: se mantienen cinco elementos del recorte del Modernismo** (4 de octubre de 2026; **implementado en v33** con el V1 aprobado).
- Sacar de `RECORTE-MODERNISMO.json/.md`: las obras `stool-60`, `maison-du-peuple-clichy` y `lacoste-polo`, y los diseñadores `jean-prouve` y `lacoste` (René Lacoste).
- Efecto: el recorte pasa a 15 obras, 6 diseñadores y 3 hechos de contexto. Para llegar a 18 / 8 / 3 hay que elegir 3 obras y 2 diseñadores más (a definir con tu «implementa»); si no, el Modernismo queda con 123 obras y 66 diseñadores.
- Nota: `jean-prouve` y `chareau` estaban entre los diseñadores sin enlace de contexto (punto 65); si Prouvé se queda, su obra queda indirecta a través de Posguerra.
- Resolución: el recorte repuso Letty Lynton (Adrian), EKCO AD65 (Wells Coates) y Zonnestraal para seguir en 18 / 8 / 3. Se probó Fuller/Dymaxion, pero Posguerra lo usa (cúpula geodésica, Expo 67).

67. ✅ **APROBADO por Mauricio el 4 de octubre de 2026 (visto bueno de las desviaciones).** **Etapa 2 (Posguerra) implementada (v35)** (4 de octubre de 2026; orden «implementa la etapa 2»). Detalle en `PROJECT.md`, entrada v35.
- Resultado: 90 obras (24 ★), 44 diseñadores, 36 hechos de contexto, 142 enlaces y 16 conexiones; `ctx-corfo` y `ctx-early-television` reintegrados al Modernismo.
- Para tu visto bueno (desviaciones de la lista aprobada en V1): `eames-lounge`, `ulm-stool`, `hfg-ulm-building` y `max-bill` pasaron de ★ a Normal (no se pudo escribir un segundo enlace directo cierto); `xerox-914` y `larrea-hermanos` fueron a la reserva; 23 enlaces quedaron sin escribir (`PENDIENTES-FUENTES.md`). Si prefieres mantener alguno como ★, se hace con tu «implementa».

68. ✅ **APROBADO por Mauricio el 4 de octubre de 2026 (visto bueno de las desviaciones).** **Etapa 3 (Reforma) implementada (v36)** (4 de octubre de 2026; orden «implementa la etapa 3»). Detalle en `PROJECT.md`, entrada v36.
- Resultado: 60 obras (18 ★), 28 diseñadores, 30 hechos de contexto, 103 enlaces y 18 conexiones.
- Para tu visto bueno: `ctx-telephone` y `aluminium` fueron a la reserva; 20 enlaces quedaron sin escribir (`PENDIENTES-FUENTES.md`); cinco hechos de contexto quedan con 1 solo enlace (meta 2) y dos obras sin enlace directo. Si quieres reponer alguno, se hace con tu «implementa».

69. ✅ **APROBADO por Mauricio el 4 de octubre de 2026 (visto bueno de las desviaciones).** **Etapa 4 (Posmoderno) implementada (v37)** (4 de octubre de 2026; orden «implementa la etapa 4»). Detalle en `PROJECT.md`, entrada v37.
- Resultado: 73 obras (21 ★), 35 diseñadores, 30 hechos de contexto, 112 enlaces y 14 conexiones.
- Para tu visto bueno: `ctx-fall-berlin-wall` y `ctx-fast-fashion` a la reserva; 39 enlaces sin escribir (`PENDIENTES-FUENTES.md`); cinco obras bajaron de ★ y tres subieron; cinco hechos de contexto con 1 solo enlace y ocho obras sin enlace directo. Si quieres reponer o cambiar alguno, se hace con tu «implementa».

70. ✅ **Movimientos y macromovimientos: mostrar su extensión temporal real, sin comprimir** (implementado en v38, 4 de octubre de 2026).
- Hoy algunas líneas de movimiento y macromovimiento (modernismo, arts and crafts, esteticismo, diseño de interacción y otros) se ven comprimidas, y se pierde visualmente su duración real, que es un dato importante.
- Pedido: que cada línea se dibuje en su extensión real (inicio a fin), sin acortarla. Propuesta de Mauricio: hacerlo antes de la etapa 5 (se evalúa al implementar el alcance real: cómo se apilan las líneas largas, etiquetas y tests).
- Hecho en v38: los movimientos (macros incluidos) ya no se acortan a «punto + etiqueta + flecha»: se dibujan siempre sobre su extensión real, y la etiqueta se mantiene a la vista mientras se recorre la barra. Siguen acortadas las instituciones y los hechos de contexto largos (si quieres lo mismo para ellos, se hace con tu «implementa»).

71. ✅ **Nueva etapa 6 (levantamiento transversal y complemento de obras y diseñadores), entre la etapa 5 y la Parte II** (4 de octubre de 2026; **plan actualizado a v8 en v39**: `PLAN-CIERRE.md` sección 9b, regla C4c y documentos relacionados; la etapa 6 misma aún NO se ejecuta).
- **Pedido:**
  - Después de la etapa 5 (y del V2 o antes de él, ver dudas) va una etapa 6, antes de la Parte II.
  - Hace un **levantamiento transversal** de toda la línea (1750 a hoy) y propone **complementar obras y diseñadores**, para que la inmensa mayoría de las obras más icónicas del diseño y la arquitectura de todas las épocas estén incluidas.
  - **Cobertura de movimientos arquitectónicos de las últimas 4 décadas** (desde ~1985).
  - **Criterio:** priorizar que lo icónico esté incluido, relajando un poco la exigencia de conexión con el contexto, pero **sin elementos totalmente desconectados**. Se aprovechan las conexiones secundarias (indirectas): un elemento puede tener solo esas. Si hace falta, se agregan **hechos de contexto nuevos** para enriquecer el mapa.
  - **Resultado de la propuesta:** el detalle de cada obra o diseñador nuevo, con las conexiones que tendría, y cuánto crece cada período.
  - **Después de tu aprobación:** dentro de la etapa 6 se escribe el contenido completo de todos los elementos nuevos, y recién después se pasa a la Parte II.
- **Esquema propuesto de la etapa 6** (para tu visto bueno):
  - **6.1 Levantamiento** `[A]`: auditoría de lo que hay por época, disciplina y región, contra un canon de obras icónicas (obras y diseñadores faltantes), más una lista de movimientos arquitectónicos desde ~1985.
  - **6.2 Propuesta (V3)** `[A]`: documento con la lista de obras, diseñadores, movimientos y hechos de contexto nuevos, el enlace de contexto (directo o indirecto) de cada uno, una tabla de crecimiento por período y las obras que no logran conexión (a la reserva).
  - **6.3 Tu aprobación (V3).**
  - **6.4 a 6.6 Redacción** `[B]`: mismo método de las etapas 2 a 5 (lotes de agentes Sonnet, `validate_out.py`, `apply_new.py`, enlaces y conexiones), sin fuentes (Parte I).
  - **6.7 Integración y pruebas** `[C]`, y un nuevo **V4** para tu revisión del sitio completo.
- **Cambios que habría que hacer al plan (al implementar):**
  - Sección 4 (mapa de etapas), sección 9 y Anexo C: agregar la etapa 6.
  - Sección 3 (tamaños) y punto 61: la meta de **375 obras deja de ser el techo**; la cifra final sale de la propuesta V3.
  - Regla C4b: nueva excepción para la etapa 6 (enlace directo o indirecto, mínimo 1; ★ sin los 2 directos).
  - Parte II: sube el número de sesiones de R2 a R4 según el crecimiento (hoy 12 sesiones para 255 obras nuevas).
  - Checklist del V2: pasa a ser un V2 intermedio o se mueve al final de la etapa 6.
- **Riesgos y avisos:**
  - **Crecimiento del contenido y del trabajo de fuentes.** Cada obra nueva suma trabajo en la Parte II. Es la mayor consecuencia en sesiones.
  - **El «canon» de lo icónico es subjetivo.** Para no inventarlo, el levantamiento se apoya en listas de la bibliografía del curso y en la lista maestra ya aprobada; tú recortas o agregas en el V3.
  - **Fechas y datos en la Parte I:** sigue valiendo que no se busca en la web ni se agregan fuentes. Obras de arquitectura de los últimos 40 años tienen mucha información cambiante (fechas de término, demolición).
  - **Equilibrio entre épocas:** la proporción por importancia (punto 61) podría distorsionarse si lo icónico se concentra en el siglo XX. Por eso la tabla de crecimiento por período.
  - **Rendimiento visual:** la línea pasaría de ~375 a quizá 500 a 600 obras; conviene probar densidad, niveles por zoom y velocidad.
  - **Duplicados:** mucho de lo «icónico» ya está en la reserva (`RESERVA-FASE-B.json`); se parte de ahí.
- **Dudas para ti:**
  - **a)** ¿Tamaño aproximado? Para orientar al levantamiento: (i) cerca de +100 a +150 obras (≈ 500 en total), (ii) +200 (≈ 575), (iii) sin tope, lo que salga del canon.
  - **b)** ¿La etapa 6 va **antes del V2** (un solo V2 al final, con todo) o **después** (V2 al terminar la etapa 5 y V4 al terminar la 6)? Recomiendo después: se revisa el sitio antes de seguir creciendo.
  - **c)** ¿Los movimientos arquitectónicos de las últimas 4 décadas entran como movimientos (barras), con sus obras y arquitectos? Por ejemplo, deconstructivismo, high-tech, regionalismo crítico, minimalismo, parametricismo, arquitectura sostenible y otros. Propongo que sí, con la lista a definir en el V3.
  - **d)** ¿Incluyo también diseño gráfico, producto y moda en el levantamiento, o solo arquitectura y diseño en general? Entiendo que todo.
  - **e)** ¿Se mantiene la regla de que las ★ del complemento necesitan 2 enlaces directos o se relaja a 1 directo + indirectos?
- (El próximo punto era el 72; ver abajo: ahora es el 73.)

### Punto 71: respuestas a las dudas a) a e) (4 de octubre de 2026; **incorporadas al plan v8**)
- **a)** Tamaño: **mínimo 500 obras** en total (hoy 343; meta anterior 375). Más obras, si el canon lo pide.
- **b)** **V2 al final de la etapa 6** (un solo V2, con todo el sitio). La etapa 5 no tiene V2 propio: cierra con la integración de la Parte I y sigue la etapa 6. El V3 (aprobación de la lista de la etapa 6) se mantiene.
- **c)** Movimientos arquitectónicos de las últimas 4 décadas: sí. Se suman también **documentos e instituciones relevantes** (por ejemplo, el Premio Pritzker, bienales, premios, manifiestos, cartas, escuelas y museos).
- **d)** Todas las disciplinas: gráfico, producto, moda y arquitectura.
- **e)** Regla de enlaces: se puede **relajar un poco, solo en casos excepcionales**, la exigencia de enlaces directos (obras ★ con 2 directos). Cada excepción queda anotada en la propuesta V3. Ningún elemento queda sin conexión (directa o secundaria).
- **Criterio rector de la etapa 6:** que estén **todos los diseñadores y obras que sería razonable encontrar en un curso universitario de historia del diseño** (gráfico + producto + moda + arquitectura). La prueba de inclusión pasa de «equilibrio por época» a «¿se esperaría verlo en un curso?», cuidando que ninguna época quede muy desbalanceada (tabla de crecimiento).
- **Avisos al implementar:**
  - «Documentos» y premios: hoy existen los tipos institución y teoría. Un premio (Pritzker) calza como **institución**; un manifiesto o carta como **teoría**. No se crea un tipo nuevo salvo que me lo pidas.
  - Con 500 o más obras, el plan de la Parte II sube de tamaño (R2 a R4); lo recalculo en el plan.
  - Pruebas de rendimiento de la línea con más de 500 obras.
- Con esto el punto 71 queda **definido, listo para implementar** (modificar `PLAN-CIERRE.md` a v8 y documentos de estado) cuando digas «implementa».

72. ✅ **Renombrar el nivel de detalle «Normal» a «Completo»** (4 de octubre de 2026; **incorporado al plan v8 como paso 6.7**; el cambio en el sitio y en los textos se hace al ejecutar ese paso, no antes).
- **Pedido:** en el selector «Detalle», el nivel «Normal» pasa a llamarse **«Completo»** (EN: «Complete»). Es un cambio de nombre, no de función: siguen siendo dos niveles, Imprescindible (★) y el resto.
- **Qué toca (al implementar, dentro de la etapa 6):**
  - Textos de la interfaz en `UI.es` y `UI.en` (`lv_normal`, `lvTip_normal`; hoy «Normal» en ambos idiomas) y los textos de ayuda y de la ficha general (i); se regeneran las imágenes de la ayuda si muestran el nombre.
  - Tooltip nuevo: hoy «Todos los elementos: imprescindibles y normales»; pasaría a «Todos los elementos: imprescindibles y el resto».
  - Documentos: `MANUAL-CONTENIDO.md`, `PLAN-CIERRE.md`, `PROPUESTA-NIVELES.md`, `LISTAS-CIERRE.md` y los briefs, donde dice «Normal» como nivel.
  - Pruebas de navegador que busquen el texto «Normal».
- **Avisos:**
  - **No cambiar el valor interno `level: "normal"`** en los ~418 elementos de `src-data/`, en el build ni en los agentes: solo cambia la etiqueta visible. Así no se toca ningún dato ni se rompe la validación (`essential` o `normal`). Si prefieres renombrar también el valor interno, avísame; es más trabajo y más riesgo, sin ganancia visible.
  - **Posible confusión con el «Completo» antiguo:** el punto 48 fusionó el antiguo nivel «Completo» con Normal, y el deseable D5 (`PLAN-CIERRE.md`) habla de un «nivel de alto detalle (antiguo Completo)». Si más adelante se quisiera un tercer nivel, ya no podría llamarse «Completo». Se actualiza la redacción de D5.
  - La preferencia de detalle guardada en el navegador usa el valor interno, así que no se pierde.
- Pendiente de ti: nada, salvo confirmar que basta con cambiar la etiqueta visible.
- El próximo punto es el **73**.

73. ✅ **Plan actualizado a v8 (v39, solo documentos)** (4 de octubre de 2026; orden «implementa esto en el plan» sobre los puntos 71 y 72). Detalle en `PROJECT.md`, entrada v39.
- `PLAN-CIERRE.md` v8: etapa 6 (sección 9b, pasos 6.1 a 6.8), regla C4c, V3 nuevo, V2 movido al final de la etapa 6 (la etapa 5 ya no lo pide), mapa de etapas, tamaños, Parte II (sesiones recalculadas), deseable D5 y seguimiento.
- Documentos ajustados con notas: `MANUAL-CONTENIDO.md`, `PROPUESTA-NIVELES.md`, `LISTAS-CIERRE.md`, `SPEC.md`, `INICIO-SESION-NUEVA.md`, `ESTADO-ACTUAL.md`, `PROJECT.md`.
- No se tocó el sitio (`app.js`, `style.css`, datos): el rótulo «Completo» se aplica en el paso 6.7.
- La etapa 5 no se ha iniciado. El próximo punto es el **74**.

74. ✅ **Cierre de pendientes y decisión sobre el conteo de contexto** (4 de octubre de 2026; v40, solo documentos).
- **Aprobados por Mauricio:** puntos 67, 68 y 69 (desviaciones de las listas de Posguerra, Reforma y Posmoderno) y punto 54 (correcciones de A6 lote 4).
- **Cerrados:** punto 41 y los puntos 1 a 6 y 9 de «PENDIENTES PARA RECORDAR» (los cubren el plan v8 y la etapa 6).
- **Punto 65: decidido que sí.** El build y la auditoría R1 deben contar las obras (y diseñadores) «con contexto directo / solo indirecto / sin contexto», con la definición C4b del plan. **NO implementado**: es un cambio de código (`tools/build_data.py`, auditoría R1) que se hace cuando digas «implementa»; propuesta: dentro del paso 6.7 (integración de la etapa 6), para que cuente también lo nuevo, o antes si prefieres.
- **Actualización:** el 4 de octubre de 2026 Mauricio **confirmó el punto 65 en el paso 6.7**; quedó incorporado al plan (v40: paso 6.7 apartado (c), paso 6.2 y R1.1). El código sigue sin escribirse hasta ejecutar 6.7.
- Siguen abiertos solo: los puntos 7, 10 y 11 de «PENDIENTES PARA RECORDAR» (fuentes y A2, que van a la Parte II) y el punto 63 (conceptos con fuente, R3).
- El próximo punto es el **75**.

75. ✅ **Etapa 5 (Industrial) implementada (v42)** (4 de octubre de 2026; orden «Implementa la fase 5»). Detalle en `PROJECT.md`, entrada v42. Sin V2 (pasó al final de la etapa 6).
- Resultado: Industrial con 30 obras (9 ★), 14 diseñadores, 23 hechos de contexto, 9 productivos, 5 teorías, 5 movimientos, 6 instituciones, 63 enlaces y 16 conexiones. Total de la línea: 373 obras (109 ★), 185 diseñadores, 160 hechos de contexto, 656 enlaces y 87 conexiones. Carga del sitio: 0,45 s, `all.json` de 2,8 MB, sin errores de página.
- Para tu visto bueno (desviaciones de la lista; detalle en `PENDIENTES-FUENTES.md`): `ctx-telegraph`, `ctx-photography` y `cylinder-textile-printing` a la reserva; el Manuale de Bodoni pasa a 1788 (`bodoni-manuale-1788`, Normal) porque el de 1818 es póstumo; cinco diseñadores de ★ a Normal (Chippendale, Adam, Percier y Fontaine, Schinkel, Bodoni) y la silla Boppard de Thonet de Normal a ★; cinco contextos con un solo enlace; 8 enlaces o conexiones sin escribir (`sin_enlace`).
- Próximo paso: **etapa 6** (propuesta V3). No se inicia sin tu «implementa». El próximo punto es el **76**.

76. ✅ **Etapa 6, pasos 6.1 y 6.2 implementados (v43)** (4 de octubre de 2026; orden «Implementa la fase 6»). **Se detiene en el V3 (paso 6.3): no se ha escrito ninguna ficha.** Detalle en `PROJECT.md`, entrada v43.
- Documentos: `tools/LEVANTAMIENTO-ETAPA6.md` (6.1) y `tools/PROPUESTA-ETAPA6.md` (+ `.json` con los registros; 6.2), generados con `tools/pipeline/propuesta_etapa6.py` y el brief `briefs/BRIEF-ETAPA6.md`.
- La propuesta: obras 373 → **585** (+212; 57 ★), diseñadores +157, movimientos +35 (10 arquitectónicos de las últimas cuatro décadas), instituciones y premios +35 (Pritzker, Red Dot, iF, Aga Khan, Bienales…), teoría +35, hechos de contexto +23. Crecimiento por período: Industrial +76 %, Reforma +56 %, Modernismo +29 %, Posguerra +58 %, Posmoderno +91 %.
- Conexiones: ningún elemento desconectado; 157 con solo conexiones secundarias; 18 obras ★ con un solo enlace directo (excepciones C4c para tu decisión).
- **Pendiente de ti (V3):** decisiones de la sección 7 de la propuesta (aprobar o recortar la lista; excepciones C4c; elementos «global»: 37 frente al orientativo de 6 a 10; posterior a 2010; reparto por época; América Latina 12 %).
- El próximo punto es el **77**.

77. ✅ **V3 aprobado y etapa 6, pasos 6.4 a 6.8 implementados (v44)** (5 de octubre de 2026; orden «Apruebo la lista completa; implementa los pasos 6.4 a 6.8»). Detalle en `PROJECT.md`, entrada v44.
- Resultado: **585 obras** (165 ★; Industrial 53, Reforma 94, Modernismo 155, Posguerra 143, Posmoderno 140), 339 diseñadores, 76 movimientos, 94 instituciones, 78 teorías, 65 productivos, 183 hechos de contexto, 1.118 enlaces y 107 conexiones. América Latina: 71 obras (12 %); «global»: 30. Build «OK: no PROBLEM»; `run_all.sh` sin fallas (se ajustaron `test_preview` y `test_etapa1` a las nuevas cifras).
- **Rótulo «Normal» → «Completo» («Complete»)** en la interfaz, el tooltip («Todos los elementos: imprescindibles y el resto») y la ayuda; el valor interno sigue siendo `normal`.
- **Punto 65 implementado** en `tools/build_data.py`: obras con contexto directo / solo indirecto / sin contexto, por tramo y total (hoy 540 / 25 / 20), WARN con la lista de las que no tienen ninguno.
- Desviaciones para tu visto bueno (detalle en `PENDIENTES-FUENTES.md`): a la reserva `gary-anderson`, `danne-blackburn` y `estudio-america` (sin año de nacimiento; sus obras quedan con `maker`), `th-futurist-manifesto-1909` (duplicado), `th-charter-athens` (duplicado); `english-landscape-garden` empieza en 1750 (origen en la década de 1720, dicho en el texto); Panteón de París y La Moneda con año de inicio (1764 y 1784) por la vida de su arquitecto; Jatiya Sangsad sin diseñador enlazado (Kahn murió en 1974; queda como `maker`); SANAA, Pezo von Ellrichshausen, Beggarstaffs y Bresciani et al. pasan a `collective`; 12 contextos con 1 solo enlace; 20 obras sin ningún contexto (Reforma 1, Modernismo 6, Posguerra 9, Posmoderno 4); varias fichas con `maker` genérico. Todo sin fuentes (`refs: []`); muchas fechas y datos «de memoria» se verifican en la Parte II.
- Próximo paso: **tu V2** (cantidades por período, % América Latina, excepciones C4c, reserva). La Parte II no empieza sin tu visto bueno. El próximo punto es el **78**.

78. ✅ (paso 7.1) / ⏳ (V4) **Revisión editorial externa: nueva etapa 7 (v45, solo documentos)** (5 de octubre de 2026). Pedido de Mauricio: antes de pasar a la Parte II, una revisión editorial externa, independiente de las decisiones anteriores (puede contradecirlas) y en tono académico, del listado de movimientos, instituciones, obras teóricas, diseñadores, obras y contexto, para que la línea contenga todo lo que un curso universitario de historia del diseño enseña (general y gráfico, producto, moda y arquitectura, de 1750 a hoy), con lo que falte en una lista para crear sus fichas, y revisando que los imprescindibles sean los que todo estudiante debe conocer (que no falten ni sobren). Registrarla como paso 7 y documentar las correcciones para que otro asistente complete el contenido.
- **Hecho (paso 7.1):** `tools/REVISION-EDITORIAL-ETAPA7.md` (dictamen, criterios y canon de contraste, diagnóstico por tipo, imprescindibles, correcciones de datos, decisiones D1 a D8 e instrucciones; anexos A a F), `tools/REVISION-ETAPA7.json` (193 elementos nuevos con el formato de `PROPUESTA-ETAPA6.json` y `prioridad` A/B/C: 84 obras, 53 diseñadores, 7 movimientos, 9 instituciones, 26 teorías, 10 hechos de contexto, 4 productivos; A 56, B 109, C 28; 15 se reponen desde la reserva), `tools/REVISION-ETAPA7-AJUSTES.json` (102 cambios de nivel, 15 fusiones/renombres/retiros, pertenencias de 37 movimientos y 49 instituciones, 11 correcciones, 4 candidatos a la reserva) y `tools/pipeline/etapa7_anexos.py`. Ids validados contra v44 (ninguno repetido; todas las referencias existen o son nuevas; los niveles «de» coinciden con los actuales).
- **Hallazgos principales:** (1) 33 de 74 movimientos y 33 de 94 instituciones muestran 0 o 1 obra en su ficha (p. ej. arquitectura posmoderna ★ solo con la Piazza d'Italia; diseño de interacción ★ y Beaux-Arts ★ sin obras), corregible sin redactar (Anexo D); (2) faltas canónicas: Farnsworth, Casa de Vidrio, Lever House, Wainwright, Teague, Maison de Verre, Karl-Marx-Hof, Candela, Dieste, Villanueva, Lubalin, Weingart, gráfica punk y activista, Engelbart, Moggridge, Denise Scott Brown, textos de Morris, Wright, Giedion, Barthes, Simon y Forty, y movimientos como neogótico, futurismo completo, suprematismo, Plakatstil y metabolismo; (3) el ★ bajó obras canónicas solo por la regla C4 (Eames 670, Carlton, Portland, Westwood) y tiene ★ locales o coyunturales (La Aurora de Chile, Seaside, Villa Olímpica, Burj Khalifa) y redundancias (Apple).
- **Resultado si se aprueban A y B:** 654 obras (181 ★, 27,7 %), 388 diseñadores (102 ★), 80 movimientos (35 ★), 100 instituciones, 100 teorías, 191 hechos de contexto; reparto por época y disciplina casi igual al actual; América Latina 11,5 % (Posguerra 20 %).
- **Plan v9:** nueva sección 9c (etapa 7, pasos 7.1 a 7.8) entre la etapa 6 y la Parte II; nuevo visto bueno **V4**; se propone mover el V2 del paso 6.8 al paso 7.8.
- **No se tocó** el sitio ni los datos (`app.js`, `style.css`, `src-data/`, `data/all.json` iguales a v44); `index.html` sube a `?v=45`.
- **Pendiente de Mauricio (V4, decisiones D1 a D8 de la revisión, sección 11):** D1 alcance A/B/C; D2 rótulo «Moda y textil»; D3 el ★ se decide por importancia y no por conectividad; D4 cuatro ★ chilenos (Cybersyn, Quinta Monroy, arpilleras, franja del NO) y La Aurora de Chile a Completo; D5 Elbphilharmonie como ancla y contextos condicionales (COVID-19, IA generativa); D6 V2 al final de la etapa 7; D7 candidatos a la reserva; D8 citar a Forty en «Acerca de».
- El próximo punto es el **79**.

79. ✅ **V4 dado; etapa 7 preparada para ejecutarse con Sonnet; nueva etapa 8 y nueva Parte III (v46, plan v10)** (5 de octubre de 2026).
- **Decisiones del V4 (Mauricio):** D1 se aprueban A y B; la C queda para una etapa futura (Parte III). D2 se mantiene «Moda»; internamente es «moda y textil»; se explicará en una ficha de disciplina (etapa 8). D3 la ★ se decide por importancia; a toda obra ★ se le deben buscar conexiones al contexto sin forzarlas, y se pueden agregar hechos de contexto. D4 aprobadas las ★ chilenas. D5 se agregan los contextos de COVID-19 e IA. D6 el V2 se traslada al final, antes de la Parte II, con una etapa 8 nueva. D7 los candidatos pasan a la reserva. D8 en «Acerca de», subsección nueva sobre el fundamento conceptual y bibliográfico: Forty como base conceptual y luego las obras de base (canon de la sección 1.1 de la revisión).
- **Pedido 1:** documento muy explicativo y detallado con todas las correcciones, ejecutable en una sesión nueva con Sonnet → **`tools/GUIA-EJECUCION-ETAPA7.md`**.
- **Pedido 2:** nueva **etapa 8**: (a) fichas de foco (político, económico, social, cultural, tecnológico, productivo) con un ensayo breve de varios párrafos («La historia del diseño desde lo…»), con eventos, movimientos y obras como ejemplos enlazados a sus fichas y un vínculo al final para descargarlo como PDF con imágenes de las obras citadas y referencias (estas en la Parte II); (b) los botones de disciplina pasan a ser botones de alcance: filtran lo relevante de esa disciplina (contexto, movimientos, instituciones, diseñadores, obras) y muestran «La historia del diseño XXXX», un panorama de 1750 a hoy con los eventos de contexto que la determinaron y ejemplos de obras y diseñadores, también en PDF; (c) botones de foco y de disciplina con apariencia equivalente (etiqueta, ícono de color, borde del color, sombreado muy suave) y barra en el orden Foco | Disciplinas | [Conexiones] | Detalle; (d) el V2 al final de la etapa 8, antes de la Parte II; (e) en las fichas no revisadas, el ícono de advertencia de «Fuentes» también arriba, bajo el título y los años, al lado de «Imprescindible». → plan, sección 9d, y **`tools/ESPEC-ETAPA8.md`**.
- **Hecho en v46 (solo documentos y herramientas; el sitio y los datos no cambian):**
  - `REVISION-ETAPA7.json`: campo `estado` (171 `aprobado-V4`, 26 `parte-III`); COVID-19 e IA generativa pasan a B con anclas nuevas (`cdc-sars-cov-2-illustration-2020`, `cosmopolitan-ai-cover-2022`, productivo `generative-image-models`); contexto nuevo `ctx-suez-crisis-1956` para el Mini (D3). Total: 197 registros.
  - `REVISION-ETAPA7-AJUSTES.json`: decisiones del V4, reserva D7 aprobada, D2 sin cambio de rótulo, `critical-speculative-design` se mantiene (su obra a la Parte III), reposiciones (11 fichas del recorte del Modernismo y `ctx-photography`) y **`enlaces_estrella`** (D3: 59 obras ★ con menos de dos enlaces directos de subcategorías distintas: 25 enlaces propuestos, 2 con contexto nuevo, 4 enlaces suspendidos que esperan fuente y 28 excepciones previstas).
  - **Paso 7.3 hecho:** `tools/pipeline/ajustes_etapa7.py` (fases `estructura`, `relaciones`, `niveles`; probado en una copia: 225 cambios en 45 archivos, build sin PROBLEM), `prep_etapa7.py` (30 lotes), `check_etapa7.py`, `briefs/BRIEF-ETAPA7-REDACCION.md`; `validate_out.py` reconoce los ids aprobados; `build_data.py` acepta `posthumous: true` (Bodoni 1818; `SPEC.md` 5.5).
  - `REVISION-EDITORIAL-ETAPA7.md`: recuadro con las decisiones del V4 y anexos al día (nuevo Anexo G, enlaces D3).
  - Plan v10: 7.2 y 7.3 marcados; 7.4 a 7.8 reescritos (7.8 sin V2); regla **C4d** (★ por importancia); **sección 9d (etapa 8, pasos 8.1 a 8.7, con el V2)**; **Parte III** (sección 17: elementos C y deseables); mapa de etapas, sesiones, R3 (referencias de los ensayos), R5 (`ensayos/`) y seguimiento al día. `MANUAL-CONTENIDO.md`: notas D3 y D2.
- **Siguiente paso:** 7.4 (ajustes estructurales) con la guía; no se inicia sin tu «implementa». El próximo punto es el **80**.

80. ✅ **Etapa 7, paso 7.4 ejecutado: ajustes estructurales (v47)** (5 de octubre de 2026; orden «Ejecuta 7.4»).
- `ajustes_etapa7.py estructura --prueba` (225 cambios, 45 archivos, 57 pendientes, build OK) y luego `--aplicar`. Resultado en `data/all.json`: **587 obras, 341 diseñadores, 73 movimientos, 93 instituciones, 64 productivos** (lo esperado); build «OK: no PROBLEM». Detalle de retiros, reserva D7 y reposiciones en `PENDIENTES-FUENTES.md` («Etapa 7»).
- **Pruebas (C6, solo pruebas y un verificador; el sitio y `app.js` no cambian):** `test_etapa1` (las 11 fichas repuestas ya no cuentan como «recortadas»), `test_preview` (la vista previa de las listas aún trae los 3 elementos retirados) y `listas_check.py` (los ids `th-werkbund-debate` y `werkbund-cologne-1914` pasaron a `modernism`). **`test_v31` estaba rota en silencio desde antes** (se caía con `StopIteration` al no existir `kaare-klint`, y no imprimía FAIL; la reposición lo dejó correr): desde la etapa 6 los datos reales sí tienen el grupo «Global» con «Más allá de Occidente» (95 elementos), así que la prueba ahora lo espera. Aviso para el resto de la etapa: el filtro `grep FAIL|Error|Timeout` de la guía no ve un `Traceback`; usar también `grep -c Traceback`.
- Próximo paso: **7.5 y 7.6** (agentes Sonnet), a la espera de tu OK. El próximo punto es el **81**.

81. 📝 **Nueva tarea en la etapa 8: imágenes en todas las fichas de obra y de diseñador, y galería en las fichas de estilos (paso 8.5b)** (5 de octubre de 2026). Pedido de Mauricio: antes de su revisión final (V2), asegurar que toda ficha de obra y de diseñador tenga imagen; sugerir fuentes cuando Wikimedia no la tenga; y que las fichas de estilos lleven una o varias imágenes, con puntitos abajo para pasar de una a otra.
- **Registrado solo en los documentos** (plan sección 9d, paso 8.5b; `tools/ESPEC-ETAPA8.md` sección 11; casilla en el seguimiento); no se implementó nada.
- **Hallazgos al revisar el código y los datos (v47):** hoy solo 75 de 587 obras y 75 de 341 diseñadores tienen `wiki`; la ficha muestra solo imágenes de Commons (las de «uso legítimo» de Wikipedia no se ven); solo hay una imagen por ficha. Faltan unas 512 obras y 266 diseñadores, y muchas obras posteriores a 1950 no tendrán imagen libre.
- **Propuesta:** auditoría de cobertura real, búsqueda por lotes (primero ★), campo `images` con crédito y licencia, aviso del build «N sin imagen» (meta 0 con excepciones anotadas), sucedáneos (réplica, anuncio antiguo, otra obra del diseñador) y galería con puntitos; en los estilos, de 3 a 5 imágenes armadas por defecto con las obras ★ del propio movimiento. Fuentes sugeridas en la sección 11.4 de la especificación.
- **Pendiente de Mauricio (no bloquea):** D-IMG1 (¿solo imágenes libres, o también enlazar imágenes con derechos reservados con crédito?), D-IMG2 (diseñadores vivos sin retrato: ¿una obra suya o nada?) y D-IMG3 (¿galería también en instituciones y teorías?).
- **Avisos:** el paso agrega peso al sitio si se guardan copias locales (se propone enlazar las de Commons y guardar solo CC0/dominio público en `img/`, ≈ 40 KB cada una); la meta «todas con imagen» puede no cumplirse al 100 % por derechos, y se anotará cada excepción. El próximo punto es el **82**.

82. ✅ **Decisiones D-IMG1 a D-IMG3 del paso 8.5b** (5 de octubre de 2026; respuesta de Mauricio al punto 81).
- **D-IMG1:** el sitio es privado e interno, no se publicará: la imagen **no tiene que ser libre**; puede venir de un sitio legítimo y confiable con derechos reservados. En ese caso la ficha muestra un pequeño enlace **«Créditos»**.
- **D-IMG2:** para el diseñador sin retrato, **una obra suya**.
- **D-IMG3:** **instituciones sí** (imagen y galería) y **teorías con su portada**, bajo el mismo criterio de D-IMG1.
- **Registrado solo en documentos** (`ESPEC-ETAPA8.md` secciones 11.2, 11.4 y 11.6; plan, paso 8.5b); no se implementó nada. Detalles técnicos que se agregan: campo `rights` (`free`/`reserved`) en cada imagen; copia local en `img/` de las de derechos reservados (los sitios de origen suelen bloquear el enlace directo); el build podrá listar las `reserved` por si el sitio llegara a publicarse. Fuentes aceptables: museos, archivos, bibliotecas, fundaciones, fabricantes, editoriales y prensa reconocida; no blogs, Pinterest ni buscadores de imágenes. Se sigue prefiriendo la libre.
- **Aviso:** si el sitio se hiciera público alguna vez, habría que revisar o reemplazar las imágenes `reserved`. El próximo punto es el **83**.

83. 📝 **Nueva tarea en la etapa 8: modo edición y resumen de revisión (paso 8.5c)** (5 de octubre de 2026). Pedido de Mauricio: (1) la contraseña se pide al editar algo, no apenas se abre el modo edición; (2) la contraseña será **`uai2026`**; (3) el resumen muestra también datos de imágenes (con/sin, libre, con derechos, etc.) y un listado de fichas por imagen parecido al de fuentes, además de un listado de fichas con comentarios; (4) los listados de fuentes, imágenes y observaciones son colapsables y parten colapsados; (5) las épocas se llaman por sus años («1914–1945»), no por etiquetas.
- **Registrado solo en documentos** (plan sección 9d, paso 8.5c; `ESPEC-ETAPA8.md` sección 12); no se implementó nada, ni se cambió la contraseña actual (`lhd2026`) en `editar.php`.
- **Cómo queda:** `?editar` abre sin pedir nada; la contraseña se pide al primer intento de editar (lápiz de la imagen, observaciones, cambiar imagen) y la acción sigue sola al acertar; el resumen abre sin contraseña y solo las observaciones (privadas) la piden. Las cifras de imágenes usan el campo `images` del paso 8.5b, por eso 8.5c va después. La nueva contraseña **reemplaza la decisión del punto 60** y obliga a actualizar `editar.php`, tres pruebas, `empaquetar.sh` y los documentos (lista en la sección 12.1).
- **Avisos y pregunta (no bloquean):** (a) los años de las épocas en los datos se tocan en los bordes (1851, 1914, 1945, 1975); propongo mostrar **1750–1850 · 1851–1913 · 1914–1944 · 1945–1974 · 1975–hoy** (sin repetir años), aunque el plan escribe el Modernismo como 1914–1945; (b) ¿las épocas por años solo en el modo edición y la exportación (propuesta), o también en el resto del sitio? (c) `uai2026` queda escrita en `editar.php`, aceptable en un sitio privado.
- El próximo punto es el **84**.

84. ✅ **Épocas por años en todo el sitio (respuestas al punto 83)** (5 de octubre de 2026).
- **Corte:** sin años repetidos: **1750–1850 · 1851–1913 · 1914–1944 · 1945–1974 · 1975–hoy** (en inglés «1975–today»).
- **Alcance:** **todo el sitio**, no solo el modo edición: franja de épocas, ficha de época, buscador, tooltips, resumen de revisión, exportación, ayuda, «Acerca de» y PDF. El texto introductorio de cada época se conserva; solo cambia el rótulo.
- **Macromovimientos:** **Modernismo y Posmodernismo quedan como macromovimientos** (así desaparece la confusión con la época «Modernismo»). Mauricio **evaluará más adelante** si se agrega otro macromovimiento (Industrial, Reforma y Posguerra no tienen hoy); no se hace en esta etapa.
- **Registrado solo en documentos:** `ESPEC-ETAPA8.md` sección 12.3 (reescrita), plan paso 8.5c (ahora «modo edición, resumen y épocas por años») y seguimiento. No se implementó nada. **Aviso:** al tocar todo el sitio, 8.5c crece (franja de épocas, ficha de época, buscador, ayuda, imágenes de la ayuda, pruebas que buscan las etiquetas viejas); sigue siendo un solo paso, con el código en un asistente único `eraName(e)`.
- El próximo punto es el **85**.

85. ✅ **Etapa 7, pasos 7.5 y 7.6 hechos en tandas (v48 a v51)** (5 de octubre de 2026; orden «comienza con 7.5 y 7.6, de a grupos»). Los lotes y las salidas de los agentes están en `tools/pipeline/e7_work/` (lotes `*.json`, salidas en `out/`), de modo que otra sesión puede seguir.
- **Estado: 7.5 y 7.6 completos (v51).**
- **Tanda 1 ✅ (Industrial, Reforma, Modernismo; 49 fichas):** aplicada, `relaciones` aplicado, build «OK: no PROBLEM», `run_all.sh` sin fallas. Cifras: 604 obras, 352 diseñadores, 77 movimientos, 97 instituciones, 66 productivos, 186 contextos, 86 teorías. Ajustes a mano y excepciones C4c en `PENDIENTES-FUENTES.md` («tanda 1»).
- **Tanda 2 ✅ (Posguerra; 57 fichas; v49):** aplicada, build OK, 151 PASS sin fallas. Cifras: 627 obras, 367 diseñadores, 79 movimientos, 100 instituciones, 189 contextos, 96 teorías. `photocopying` diferido a la tanda 3 (su ancla es de Posmoderno); ajustes a mano y excepciones en `PENDIENTES-FUENTES.md` («tanda 2»).
- **Tanda 3 ✅ (Posmoderno; 54 fichas; v50): 7.5 queda completo.** Cifras: 652 obras, 385 diseñadores, 80 movimientos, 100 instituciones, 68 productivos, 194 contextos, 100 teorías (65 obras, 44 diseñadores, 22 teorías, 11 contextos, 7 instituciones, 7 movimientos y 4 productivos nuevos, como se preveía). Build OK, 151 PASS sin fallas. Ajustes a mano y desviaciones en `PENDIENTES-FUENTES.md` («tanda 3»).
- **Tanda 4 ✅ (7.6; v51):** 5 lotes `_e` (enlaces D3: 13 aplicados, 7 `sin_enlace` o ya existentes) y `textos_1` (9 reescrituras aplicadas con `apply2.py`; `werkbund-cologne-1914` y `critical-speculative-design` sin cambios; `refs` y marcas `[n]` intactos). Build OK, 151 PASS sin fallas. **Excepciones C4c anotadas una por una** (23 obras ★; otras 6 bajan a Completo en 7.7) en `PENDIENTES-FUENTES.md` («paso 7.6»).
- **Siguiente:** 7.7 (niveles, «Acerca de» D8, verificación) y 7.8 (entrega), a la espera de tu OK. El próximo punto es el **86**.

86. ✅ **Etapa 7, pasos 7.7 y 7.8 hechos (v52): etapa 7 cerrada** (5 de octubre de 2026; orden «Sigue con 7.7 y 7.8»).
- **Niveles:** `ajustes_etapa7.py niveles --aplicar` (102 cambios, build OK). **652 obras (181 ★, 27,8 %), 385 diseñadores (102 ★), 80 movimientos (35 ★), 100 instituciones, 100 teorías, 194 contextos, 1.311 enlaces, 114 conexiones.** Por período: Industrial 53 obras (14 ★), Reforma 99 (32 ★), Modernismo 172 (46 ★), Posguerra 166 (50 ★), Posmoderno 162 (39 ★). Por disciplina: arquitectura 209, producto 173, gráfico 171, moda 99. América Latina: 73 obras (11,2 %; Posguerra 19,9 %).
- **«Acerca de» (D8):** nueva sección «Fundamento conceptual y bibliográfico» con los textos y la bibliografía de la guía, en ES y EN. Revisada en pantalla (claro y oscuro).
- **Verificación (`check_etapa7.py --estricto`):** diseñadores ★ sin obra ★: 0; aprobados que faltan: 0. **No queda en 0 el punto 2 de la guía:** 4 movimientos ★ sin obra ★ visible (Beaux-Arts, Dadá, diseño sostenible y regionalismo crítico); sin pertenencias que corregir. **Decisión pendiente de Mauricio:** A) dejarlos, B) subir una obra a ★ en cada uno (+4 ★; propuesta en `PENDIENTES-FUENTES.md`) o C) bajar el movimiento a Completo. Recomendado: B para Beaux-Arts (Ópera Garnier), Dadá (*Merz*) y regionalismo crítico (Museo Romano de Mérida o Ciudad Abierta) y A para diseño sostenible.
- **Excepciones C4c:** 35 obras ★ anotadas una por una; 22 movimientos o instituciones sin obras visibles anotados; sin descartes de fichas; a la reserva: 4 obras, 3 diseñadores y 5 fusiones o retiros (paso 7.4; `RESERVA-FASE-B.json` → `etapa7_retirados`) y 7 `sin_enlace`.
- **Pruebas:** `run_all.sh` 151 PASS, sin `Traceback`; contraste 0 valores bajos. El sitio móvil sigue mostrando su aviso de «versión de escritorio» (sin cambios).
- **Siguiente:** etapa 8 (`tools/ESPEC-ETAPA8.md`; 8.1 maquetas), con las tareas 8.5b (imágenes) y 8.5c (modo edición, resumen y épocas por años) ya registradas; no se inicia sin tu «implementa». El próximo punto es el **87**.

87. ✅ **Decisión sobre los 4 movimientos ★ sin obra ★ (v53)** (5 de octubre de 2026; respuesta de Mauricio al punto 86).
- **B para Beaux-Arts, Dadá y regionalismo crítico:** suben a ★ la Ópera Garnier, *Merz* (Schwitters) y Ciudad Abierta (Ritoque). **A para diseño sostenible:** se deja como está.
- **Resultado:** 184 obras ★ (28,2 %); `check_etapa7.py --estricto` punto 2 queda solo con `sustainable-design` (decidido). Build OK. Dos excepciones C4c nuevas (*Merz* y Ciudad Abierta, con un solo enlace directo), anotadas en `PENDIENTES-FUENTES.md`.
- **Cerrado:** la decisión pendiente del punto 86. El próximo punto es el **88**.

88. ✅ **Etapa 8, pasos 8.1 a 8.5 hechos (v54)** (5 de octubre de 2026; orden «implementa 8.1 a 8.5, con una entrega al final de 8.5»).
- **8.1/8.4 Interfaz:** barra con el orden Foco · Disciplinas · Conexiones · Detalle y botones de foco y disciplina con la misma apariencia (`.chip.scope`, color propio, borde, sombra suave; contraste 0 valores bajos). **Alcance por disciplina** (`S.scope`, una a la vez; reemplaza mostrar/ocultar; combinable con el foco; la ficha muestra el último que se encendió; al quitarlo vuelve el estado anterior). Ficha de disciplina (`discCard`), ficha de foco con el ensayo al comienzo y las listas actuales debajo, vínculos del ensayo que abren fichas sin quitar foco ni alcance, advertencia «No revisada» en la cabecera de toda ficha sin fuentes y de los ensayos (clic abre «Fuentes»), ayuda en ES y EN.
- **8.2 Datos:** `src-essays/essays.json` + validación en `build_data.py` (ids, largo, `es` completo, ≥ 15 vínculos de ≥ 3 tipos y ≥ 4 épocas, imágenes) → `data/essays.json` (con la lista de PDF existentes).
- **8.3 Ensayos:** 10 ensayos (6 de foco, 4 de disciplina) en ES y EN redactados con agentes Sonnet (`briefs/BRIEF-ENSAYOS.md`, `pipeline/validate_essay.py`), `refs: []` (todos «no revisados»). Títulos puestos según la tabla de la especificación (arquitectura: «La historia de la arquitectura»; alternativa «La historia del diseño arquitectónico» sigue abierta).
- **8.5 PDF:** `tools/make_essays_pdf.py` genera los 20 PDF en `ensayos/` (A4, advertencia, «Referencias»). **Limitación:** Wikimedia está bloqueado desde el entorno de Claude, así que los PDF salen **sin figuras**; al ejecutar el script con acceso a internet se llenan (caché en `ensayos/img/`). Solo las obras con `wiki` pueden traer figura; el resto llega con 8.5b.
- **Pruebas:** nuevo `test_etapa8.py`; `test_general.py` ajustado (disciplina ya no es mostrar/ocultar, C6). Ver `run_all.sh`.
- **Siguiente:** 8.5b, 8.5c, 8.6 y 8.7 (a la espera de tu «implementa»). El próximo punto es el **89**.

89. ✅ **Etapa 8, paso 8.5b hecho (v55): imágenes, galería y PDF en 2 columnas** (5 de octubre de 2026; orden «sigue con 8.5; busca las imágenes por tandas; PDF con 2 columnas y pocas imágenes»).
- **Búsqueda por tandas** (10 tandas, punto de control en disco `tools/pipeline/e8_img/res/NNN.json`; se hizo desde el navegador del computador del usuario porque Wikimedia no es accesible desde el entorno de Claude). `merge_images.py` las junta en `src-images/images.json`: **816 de 1.237 elementos con imagen** (obras 428/652, diseñadores 322/385, instituciones ~62/100, teorías ~4/100). Homónimos descartados a mano. Quedan **421 sin imagen** (segunda pasada pendiente: fuentes de la sección 11.4; teorías por la vía «derechos reservados»).
- **Build:** `build_data.py` lee `src-images/images.json`, valida (elemento existe, archivo y licencia) y agrega `images:[{f,c,l,r}]`; avisa «N obras / N diseñadores sin imagen».
- **Interfaz:** `imgGallery` (reemplaza `imgBox`): 1 imagen como antes; 2 o más, carrusel con puntitos, flechas del teclado y deslizar; pie con autor, licencia y «Fuente» (o «Créditos» si es de derechos reservados); la imagen elegida en modo edición reemplaza la primera; sin imagen propia se mantiene la de Wikipedia. **Movimientos y macromovimientos:** 2 a 4 imágenes de sus obras ★ (pie con enlace a la obra). **Diseñadores sin retrato:** una obra («Obra más conocida: …»). **Teorías:** portada.
- **PDF (ANULADO en el punto 90):** `make_essays_pdf.py` reescrito: **2 columnas** (imágenes con pie a la izquierda, texto a la derecha), **máximo 4 imágenes** por ensayo, cada una junto al párrafo que la cita y nunca en párrafos seguidos. Las imágenes se bajan de Commons y se guardan en `ensayos/img/`: **correr `python3 tools/make_essays_pdf.py` en el computador con internet** (los 20 PDF de esta entrega salen sin figuras).
- **Pruebas:** `test_imagenes.py` (1 imagen, carrusel, galería de movimiento, crédito visible, sin imagen, 390 px).
- **Pendiente:** segunda pasada de imágenes; `audit/INFORME-IMAGENES.md`; 8.5c, 8.6 y 8.7 a la espera de tu «implementa». Próximo punto: **90**.

90. ✅ **Se eliminan los PDF de los ensayos; aviso «no revisada» en rojo claro (v56)** (5 de octubre de 2026; orden «olvídate de los PDF de los ensayos; elimina el link y todo lo asociado»).
- **PDF eliminados:** se borran `tools/make_essays_pdf.py`, la carpeta `ensayos/` (20 PDF), el botón «Descargar PDF» de las fichas (`essayPdf`, `ES.pdfs`, clave `dlPdf`, `.pdf-btn`), el campo `pdfs` de `data/essays.json` y su recuento en el build, y las comprobaciones de PDF de `test_etapa8.py`. Quedan sin efecto el paso 8.5 del plan y lo dicho de PDF en la ESPEC-ETAPA8 (sección 6 y punto 6 de la sección 11) y en el punto 89. Los ensayos siguen en pantalla.
- **Aviso «no revisada»:** `--warn` y `--warn-bg` pasan de amarillo a **rojo claro** (modo claro `#9B1C1C` / `#FDE3E3`; oscuro `#F5A3A3` / `#3F1A1A`); lo usan la insignia de la cabecera, el resumen de fuentes y el recuadro «sin fuentes».
- Próximo punto: **91**.
- **Limpieza (v56):** se quitó «y PDF» de los textos de ayuda, se reescribieron la ESPEC (sección 6 y menciones), el plan y PROJECT.md, y se borró un archivo suelto `disc-product.json`. Ya no queda en el proyecto el generador, los PDF ni el botón; solo la historia de la anulación (puntos 88–90).

91. ✅ **Subtítulos en negro y texto de presentación (v57)** (5 de octubre de 2026; dos cambios menores pedidos antes de seguir con el plan).
- **Subtítulos de las fichas en negro:** `.sect h3` (títulos de sección de toda ficha) y `.essay-sub` (subtítulo del ensayo) pasan de gris a `var(--ink)` (negro en modo claro, claro en modo oscuro); tamaño y estilo no cambian.
- **Ficha «Acerca de la línea de tiempo»** reescrita con el borrador del usuario (cambios menores de redacción: «vinculado con otras obras…», «encarnan» en lugar de «toman» en la frase de Forty; revisar si se prefiere otra palabra), en ES y EN: **Presentación** (un solo párrafo), **Fundamento conceptual y bibliográfico** (párrafo corto de Forty + canon + lista de fuentes, igual a la anterior), **Secciones de la línea** (Contexto, Diseño y «Cómo leer la línea» con Niveles de detalle y Conexiones; sin notas ni la sección «Qué es cada elemento»; descripciones abreviadas), **Datos generales** con cifras reales y el enlace «Cómo usar la línea del tiempo →».
- **Error corregido:** «Obras con contexto» mostraba **NaN** (la celda aplicaba el formato de número a «92 %»); ahora muestra 92 %.
- Próximo punto: **92**.

92. ✅ **Subtítulos de los tipos de bibliografía en gris (v58)** (5 de octubre de 2026): en la ficha de presentación, «Historia general del diseño», «Diseño gráfico», «Arquitectura», «Moda» y «América Latina» pasan a gris (`.info-sub.basis-h`, `var(--muted)`), un nivel por debajo de los títulos de sección (negro). Contexto y Diseño (subtítulos de «Secciones de la línea») no cambian. Próximo punto: **93**.

93. 📝 **Con un foco encendido, mostrar al diseñador de las obras conectadas (opción B, aprobada la maqueta; PENDIENTE de «implementa»)** (5 de octubre de 2026; pregunta: «¿por qué aparecen obras sueltas, sin la línea de vida de su autor?»).
- **Causa:** `designerVisible` (`app.js`) con `S.F` activo solo muestra a los diseñadores con enlace directo al foco («una obra conectada sola se muestra suelta»). En «Productivo» casi todos los enlaces (`tech`) son a obras, así que sus autores no se dibujan y las obras quedan flotando.
- **Cambio acordado (opción B):** con foco, un diseñador se muestra también cuando alguna de sus obras está dentro del foco (`keepOk(a.id) || ws.some(workOk)`). Los diseñadores conectados directamente al foco se ven como hoy (barra continua, nombre en negrita); los que entran **solo por una obra** llevan barra **punteada y tenue** y nombre en gris (clase `ind`, `opacity` .35 en la barra y .6 en el nombre). Maqueta: foco Productivo, 111 diseñadores, 73 con estilo tenue.
- **A cuidar:** más densidad en la zona de diseñadores y solapamiento de nombres con íconos; contraste en claro y oscuro (`check_contrast.py`); que el alcance por disciplina y el chip «Solo» sigan funcionando; ajustar `test_etapa8.py` / `test_general.py` si cuentan diseñadores con foco; agregar una comprobación (con foco, ninguna obra queda sin su diseñador; existen diseñadores `.ind`).
- **Fase del plan:** paso **8.6** (pruebas e integración), antes de correr las pruebas, para que queden cubiertas. Es un ajuste de interfaz de 8.4(a), no cambia los datos.
- Próximo punto: **94**.

94. 📝 **«Por disciplina»: eliminar el grupo «Interdisciplinario» (PENDIENTE de «implementa»; va en el paso 8.6)** (5 de octubre de 2026).
- **Hoy** (`discGroup`, `arrangeOrder` en `app.js`): al organizar «Por disciplina» hay 5 grupos: «Interdisciplinario» (elementos con 2 o más disciplinas y teorías sin género de disciplina) + las 4 disciplinas. Cada elemento va en un solo grupo.
- **Reglas pedidas:** (1) las **obras** se dibujan en su disciplina, **junto con la línea de vida de su diseñador**, que mantiene sus **colores segmentados** (franjas de `desBar`) para mostrar su interdisciplinariedad; (2) un diseñador con obras de **2 disciplinas distintas se dibuja 2 veces**, una en cada disciplina; (3) **instituciones y teorías** se dibujan en la o las disciplinas que afectaron **mayormente**. **Criterio:** la línea de cada disciplina debe ser robusta y contar la historia completa.
- **Propuesta de implementación (a confirmar):** quedan solo 4 grupos (gráfico, producto, moda, arquitectura); `inter` desaparece de `arrangeOrder`, de `UI` (`ag_inter`) y de la ayuda. **Diseñadores:** una copia por cada disciplina en que tienen obras (hoy 29 de 385 tienen obras en 2 o más); en cada copia solo cuelgan las obras de esa disciplina y la barra conserva todas las franjas de color; sin obras visibles, por su campo `disciplines`. **Instituciones (19 de 100 con 3 o 4 disciplinas) y teorías (genéricas: método, sociedad, manifiesto, crítica, historia, pedagogía):** la regla «mayormente» se calcularía con sus enlaces: se dibujan en las disciplinas que concentran al menos ~30 % de las obras y diseñadores a que se enlazan (mínimo una; respaldo: campo `disciplines` / `GENRE_DISC`). **Movimientos** (17 de 80 con 3 o 4 disciplinas; no los mencionaste): misma regla que las instituciones, para que ningún grupo quede sin su contexto de estilos.
- **A cuidar:** (a) el mismo `data-id` aparecería en dos grupos: la selección, el foco y las curvas de conexiones deben resaltar ambas copias y las curvas partir de la copia visible más cercana; (b) los conteos del grupo y «Ajustar»/`visibleSpan` deben contar copias; (c) la leyenda «varias disciplinas» (`lg-des multi`) sigue valiendo para la barra; (d) interacción con el **alcance por disciplina** (punto 8.4): con alcance, un solo grupo; (e) más altura total de la zona de diseño al repetir diseñadores; (f) pruebas: `test_general.py`/`test_v24.py` si usan `inter`; prueba nueva (ningún grupo «Interdisciplinario»; un diseñador con obras en 2 disciplinas aparece en ambos grupos; obras bajo su diseñador).
- **Fase:** paso **8.6**, junto con el punto 93 (misma zona del código: `designerVisible` / `dsAll`). Antes de implementarlo mostraría una maqueta, como hice con el 93.
- Próximo punto: **95**.
- **Maqueta aprobada (punto 94):** hecha sobre una copia con `discGroups(it)` (varios grupos por elemento; diseñadores como copia por disciplina con solo las obras de esa disciplina) y umbral de 30 % por enlaces para instituciones, movimientos y teorías. Resultado: 4 grupos (Gráfico 190, Producto 182, Moda 75, Arquitectura 196), 25 diseñadores duplicados con las obras visibles en el nivel «Completo» (William Morris, Peter Behrens y Rodchenko en 3 grupos), franjas de color conservadas. **Queda para implementar en 8.6** (con el punto 93) cuando digas «implementa»; falta resolver en la implementación la selección/foco/curvas con copias, los conteos y «Ajustar».

95. 📝 **Imágenes de las fichas: pie de foto mínimo, imagen como enlace y referencia en «Fuentes» (PENDIENTE de «implementa»; va en el paso 8.6)** (5 de octubre de 2026; reemplaza el punto 95 anterior, que se eliminó).
- **Pie de foto:** solo hay pie cuando la ficha muestra un **carrusel de varias imágenes** (movimientos y macromovimientos). El pie dice **solo qué es la foto** («Edificio XXXX», «Silla YYYY»), sin «Public domain», «CC BY…», «Fuente» ni otros textos. Las fichas de **obra, diseñador, institución y teoría con una sola imagen no llevan pie**: la imagen misma es el enlace.
- **Imagen como enlace:** en todos los casos, la imagen actúa como **enlace a la fuente** (página del archivo en Commons o página de origen; se abre en pestaña nueva, con `title`/`aria-label` «Abrir la fuente de la imagen»).
- **Marca de derechos:** si la imagen **no es de dominio público**, el pie (en el carrusel) lleva **«(C)»** si es copyright / derechos reservados o **«(CC)»** si es Creative Commons. Dominio público, CC0 y «sin restricciones conocidas» no llevan marca. En las fichas sin pie (imagen única) la marca no se muestra en la imagen; la información de licencia queda en la referencia de «Fuentes» (ver abajo). *A confirmar:* si en las fichas de una sola imagen quieres igual una marca «(C)»/«(CC)» pequeña sobre la imagen (hoy se entiende que no, por «sin texto de pie de imagen»).
- **Referencia en «Fuentes» (todos los casos):** al final de la ficha, en la sección «Fuentes», **antes de la primera fuente de texto**, una línea **«Imagen: …»** con la referencia de la imagen (autor o titular, título del archivo, licencia, enlace). En un carrusel, una línea por imagen mostrada (en el orden del carrusel). Esta línea **no cuenta como fuente** para «No revisada» ni para `srcCount` (una ficha con solo la referencia de imagen sigue «No revisada» y la sección «Fuentes» mantiene su advertencia); la sección aparece también en fichas sin fuentes de texto, con las líneas de imagen y la advertencia.
- **Efectos que hay que resolver al implementar:**
  - El pie de las galerías de movimientos hoy lleva el nombre de la obra con **enlace a su ficha** (punto 89): con la imagen como enlace a la fuente, ese enlace se pierde. Propuesta: el pie conserva el nombre de la obra (texto) y la ficha de la obra se abre desde un pequeño enlace «ver ficha» o desde el propio nombre del pie; a decidir con la maqueta.
  - Diseñadores sin retrato que muestran una obra («Obra más conocida: …», D-IMG2): sin pie, esa aclaración se pierde; propuesta: va en la línea «Imagen: obra más conocida, …» de «Fuentes».
  - El enlace «Créditos» de las imágenes de derechos reservados (D-IMG1) se reemplaza por la referencia en «Fuentes» y la marca «(C)».
  - Imágenes tomadas de Wikipedia por `wiki` (`fetchImage`) y las cambiadas a mano en `?editar` (`imagenes.json`): la primera trae licencia y página de la API; la segunda no tiene autor (la línea dirá «Imagen: elegida en modo edición» con su URL).
  - En `images.json` 112 imágenes no tienen autor (`c`); la línea mostrará solo archivo, licencia y enlace.
  - Mapeo de licencias: «Public domain», «CC0», «No known restrictions» → sin marca; «CC BY…», «CC BY-SA…» y «Free Art License» → **(CC)**; `rights: reserved` → **(C)**.
- **Pruebas (8.6):** carrusel con pie sin textos de licencia y con «(CC)» o «(C)» cuando corresponde; ficha de obra y de diseñador sin pie y con la imagen dentro de un enlace a la fuente; «Fuentes» con la línea «Imagen:» antes de la primera fuente de texto; ficha sin fuentes de texto sigue «No revisada»; 390 px; claro y oscuro. Actualizar `ESPEC-ETAPA8.md` (sección 11.4, enlace «Créditos») y la ayuda.
- .

## 96. v59 — Etapa 8, paso 8.5b: segunda pasada de imágenes (HECHO)
Se buscó imagen libre (Wikimedia Commons, vía el navegador integrado) para las 421 fichas pendientes: se añadieron **286**, de modo que **1.102 de 1.237** fichas (89 %) tienen imagen (obras 562/652, diseñadores 363/385, instituciones 87/100, teorías 90/100). Quedan **135 excepciones** (obras con derechos vigentes sin foto libre, algunos diseñadores y teorías sin candidato adecuado), listadas una por una en `audit/INFORME-IMAGENES.md`. No se tocó la interfaz. Los picks quedan en `tools/pipeline/e8_img/res/011.json`.

## 97. v60 — Etapa 8, paso 8.5c: modo edición, resumen y épocas por años (HECHO)
- **Punto 95, respuesta:** las fichas con una sola imagen **no** llevan marca (C)/(CC). Queda así para 8.6.
- **Contraseña al editar (punto 83):** `?editar` abre sin pedir nada; la contraseña se pide en la primera acción de edición (lápiz, observaciones, resolver, cambiar imagen, exportar) en un cuadro pequeño (`Esc` cancela, error si es incorrecta) y la acción sigue sola. Se guarda en `sessionStorage`. La caja de observaciones también la pide al tocarla (para no pisar texto que aún no se ha leído). La contraseña pasa a **`uai2026`** (`editar.php`, pruebas, `empaquetar.sh`, LEEME y su plantilla); reemplaza lo decidido en el punto 60.
- **Resumen ampliado:** se abre sin contraseña. Cifras de imágenes (con/sin; libre, derechos reservados, sucedánea; por tipo y época; cambiadas a mano) y listados **Fuentes**, **Imágenes** y **Observaciones** colapsables, cerrados al abrir el resumen (las observaciones, que son privadas, piden la contraseña con un botón).
- **Épocas por años (punto 84):** `eraName(e)` único: 1750–1850 · 1851–1913 · 1914–1944 · 1945–1974 · 1975–hoy (en inglés «today»); se usa en la ficha de época, el resumen y la exportación .md. Modernismo y Posmodernismo siguen como macromovimientos.
- Pruebas: `test_editar.py` reescrita; `test_v21.py` sin el ingreso de contraseña.

## 98. v61 — Etapa 8, paso 8.6: pruebas e integración (HECHO)
Se implementaron los tres puntos pendientes de 8.6:
- **93 (hecho):** con un foco, un diseñador se muestra también cuando alguna de sus obras está dentro del foco; los que entran solo por una obra llevan clase `ind` (barra punteada y tenue, nombre gris). Con foco Productivo: 111 diseñadores, 73 `.ind`, ninguna obra queda sin su línea de vida.
- **94 (hecho):** «Por disciplina» queda con 4 grupos (Gráfico 190, Producto 182, Moda 75, Arquitectura 196); `discGroups(it)` reparte cada elemento en una o más disciplinas; el diseñador se dibuja una vez por disciplina en que tiene obras visibles (25 duplicados: William Morris, Behrens, Poiret…), con solo las obras de esa disciplina y todas sus franjas de color; instituciones, movimientos y teorías van donde concentran ≥30 % de sus enlaces (respaldo: `disciplines` / género). La selección marca todas las copias; con alcance por disciplina hay un solo grupo y no hay copias. Se eliminó `ag_inter` y se actualizó la ayuda.
- **95 (hecho):** pie de foto solo en carruseles (nombre de la foto con enlace a su ficha y marca «(C)» o «(CC)» solo cuando no es dominio público); la imagen es siempre el enlace a su fuente («Abrir la fuente de la imagen»); fichas de una sola imagen sin pie ni marca; en «Fuentes», antes de la primera fuente de texto, la línea «Imagen: …» (archivo, autor, licencia, enlace), que no cuenta como fuente (la ficha sigue «No revisada» si no tiene fuentes de texto). La imagen de Wikipedia que llega tarde agrega su línea al abrirse.
- **Pruebas:** nueva `test_etapa86.py` (22 comprobaciones; agregada a `run_all.sh`); rendimiento (organizar por disciplina 65 ms, foco 62 ms); contraste sin valores bajos; imágenes de la ayuda sin cambios (la interfaz que muestran no cambió).


## 99. v62 — Paso 8.7: V2 dado (HECHO)
- **Mauricio da su visto bueno (V2, «OK»)** al sitio completo (5 de octubre de 2026): contenido de las etapas 6 y 7, ensayos, barra Foco · Disciplinas · Conexiones · Detalle, imágenes y advertencias. **Sin observaciones ni cambios pedidos.**
- **La Parte I (contenido nuevo, sin fuentes) queda CERRADA.** Cifras finales: 652 obras (184 ★), 385 diseñadores, 80 movimientos, 100 instituciones, 100 teorías, 194 contextos, 1.311 enlaces, 114 conexiones.
- Cambio técnico: solo documentos y versión de caché (`?v=62`); datos y código iguales a v61.
- **Siguiente:** Parte II (fuentes y revisión), empezando por R1 (`tools/pipeline/auditoria.py`). No se inicia sin «implementa».

## 100. v63 — Parte II, R1: auditoría y limpieza (HECHO)
- **R1.1 `tools/pipeline/auditoria.py`** (solo lee `data/all.json`; `-v` lista ids, `--md F` escribe el informe, `--strict` falla con ERROR sin anotar). Informa: elementos por tramo y tipo; obras por disciplina, región y nivel; % con fuentes; contexto directo / indirecto / ninguno de obras y diseñadores (C4b); enlaces por contexto; ids inexistentes o de tipo equivocado; marcas `[n]` sin fuente o corchetes sin cerrar; enlaces y conexiones repetidos; textos duplicados; etiquetas, `key` y fichas largas; elementos desconectados; metas C4 (contexto con ≥ 2 enlaces, ★ con 2 enlaces directos de subcategorías distintas, diseñador sin obra). Marca `[anotada]` lo que ya figura como excepción en `PENDIENTES-FUENTES.md`, `CAMBIOS-PENDIENTES.md` o `LISTAS-CIERRE.md`. Informe completo: `audit/INFORME-R1.md`. Prueba nueva: `tools/tests/test_r1.py`.
- **R1.2:** la falta de fuente https en una teoría sigue en WARN; el interruptor `STRICT_THEORY_SOURCES` (`build_data.py`) la vuelve PROBLEM cuando R3 termine las teorías.
- **R1.3 `tools/pipeline/r1_limpieza.py`** (idempotente): (a) **209 elementos con `short`** (EN y ES; solo EN en diseñadores, cuyo nombre no se traduce; máx. 22 caracteres; lista en `r1_shorts.py`): ya no hay avisos de etiqueta larga; (b) **2 enlaces de contexto repetidos quitados** (`ctx-personal-computer→macintosh-icons-1984`: queda el de `90-test-content.json`, con fuentes; `ctx-urban-informality→participatory-social-architecture`: queda el segundo); (c) **1 enlace nuevo** `ctx-design-museums→inst-design-museum-london` (el propio texto del contexto cita ese museo), con lo que el museo deja de estar desconectado. Enlaces: 1.311 → 1.310.
- **Quedan sin tocar (no son mecánicos):** `levis-riveted-jeans` (sin diseñador ni contexto que se sostenga; excepción ya anotada), 14 contextos con 1 enlace (13 anotados; `ctx-latam-centenaries-1910` sin anotar), los `key` largos de 5 conceptos y la fuente 2 de `streamlining` sin citar (R3, junto con las marcas de los conceptos, punto 63), títulos con paréntesis o largos (~120 avisos del build, de estilo), 86 teorías sin fuente (R3).
- Pruebas: 226 PASS antes de `test_r1`; `test_r1` PASS. Build sin PROBLEM.

## 101. v64 — Parte II, R2: primer lote de fuentes (HECHO, 4 de 143 obras ★)
- **Método:** WebSearch + WebFetch por obra; textos reescritos con marcas `[n]`, 2 a 3 fuentes con `checks`; lo que no sostienen las fuentes se quita o se corrige (`issues` en `tools/pipeline/r2_work/lote01.py`). Se aplica con `cd tools/pipeline && python3 apply2.py r2_work/loteNN.json` (las salidas de R2 **no** pasan por `validate_out.py`, que es para elementos nuevos; el control es el build: marca sin fuente = PROBLEM, fuente sin citar = WARN).
- **Lote 01 (industrial):** `baskerville-virgil-1757`, `bodoni-manuale-1788`, `penny-black-1840`, `encyclopedie-plates-1762`. Correcciones de fondo: el Virgilio solo está **en parte** en papel avitelado (el resto, verjurado); el Penny Black se reemplazó por el Penny Red porque la **cancelación roja podía quitarse** y el sello reutilizarse (el texto decía que «no se veía bien» sobre negro); se quitaron afirmaciones sin fuente (contraste de trazos y serifas de Bodoni, disposición de las láminas de la Encyclopédie, «grabado en hueco» del Penny Black).
- **Estado de R2:** obras ★ con fuentes 45 de 184 (141 sin fuentes tras este lote: 139 ★ + 2 que ya figuraban; ver auditoría); diseñadores, movimientos e instituciones sin empezar. **Ritmo real: ~20 llamadas web por 4 obras**; el plan prevé agentes en paralelo (lotes de 6 a 8 elementos, `BRIEF-FUENTES.md`). Hacerlo uno por uno en esta sesión tomaría cientos de llamadas.

- **Tandas 1 y 2 (v65), con 3 agentes Sonnet en paralelo (límite fijado por Mauricio: 2 o 3):** 48 obras ★ más (industrial, reforma, modernismo hasta `plan-voisin-1925`). Flujo por tanda: `prep_r2.py obras tNN` → agentes (`BRIEF-FUENTES.md`; salida `out_tNN_k.json`) → `check_r2.py` → `apply2.py` → build → `r2_incidencias.py`. Obras ★ con fuentes: 93 de 184. Hallazgos de fondo en `tools/R2-INCIDENCIAS.md`: p. ej. cartel Bauhaus 1923 es litografía (corregido `materials`), Delphos se atribuye también a Adèle Nigrin, tetera de Dresser (la del V&A es de James Dixon & Sons; `maker` de la ficha dice Hukin & Heath, sin tocar), Jacquard sin patente fechada en 1804.

- **Tanda 3 (v66):** 24 obras ★ más (de `lc2-armchair-1928` a `univers`); 117 de 184 con fuentes. Correcciones de fondo: LCW fabricada por Evans Products (Herman Miller solo la distribuyó); Unité d’Habitation encargo 1945, inauguración 1952; Chandigarh (Le Corbusier asesor desde 1951); Pruitt-Igoe 33 bloques de once pisos terminados en 1954; Ronchamp 1953–55. Datos de ficha dudosos sin tocar en `tools/R2-INCIDENCIAS.md` (p. ej. `maker` vacío en el LC2, `designers` del 2CV).

- **Tanda 4 (v67):** 18 obras ★ más (de `mole-armchair` a `sgt-pepper-cover-1967`); 135 de 184 con fuentes. **Incompleta:** el tope de 200 búsquedas web por turno dejó pendientes 6 obras (ver `ESTADO-ACTUAL.md`). Correcciones de fondo: el saco de Balenciaga fue ridiculizado y la confección industrial perdió dinero al principio (el texto decía «rápidamente copiado»); vidrio del Seagram gris rosado, no bronce; Bazaar 1957 (Britannica) frente a 1955 (V&A) para Quant; MoMA y Cooper Hewitt difieren en el cliente del cartel de Dylan. Duda sobre `designers` del Cadillac Eldorado 1959 (el Henry Ford nombra a Bill Mitchell, no a Harley Earl).

- **Tanda 5 (v68):** 21 obras ★ más (incluye las 6 que quedaron de la tanda 4); 156 de 184 con fuentes. Correcciones de fondo: Marimekko usó Unikko primero en cortinas y sofás, y en ropa 36 años después; Le Smoking fue rechazado por la clientela (una sola pieza vendida); el Walkman salió con otros nombres (Soundabout, Stowaway, Freestyle) y «Walkman» se fijó en abril de 1980; Portlandia es de 1985; concurso de la Ópera de Sídney 1956–57. Pendientes: `masp`, `god-save-the-queen-1977`, `pompidou-centre-1977`. `i-love-ny-1977` quedó con una sola fuente. Duda de dato: tipografía de Múnich 72 (Helvetica Bold según Smithsonian, Univers según el sitio de Aicher).

- **Tanda 6 y 7 (v69, 6 de octubre):** tanda 6 (24 obras, de `masp` a `gando-school-2001`) y las últimas 4 obras (`quinta-monroy-2004`, `seattle-library-2004`, `iphone-2007`, `hope-poster-2008`): **184 de 184 obras ★ con fuentes**. Primeros 16 diseñadores ★ (fechas de vida confirmadas; `dates` sin cambios): de Baskerville a Edison; 45 de 102 diseñadores ★. Correcciones de fondo: Franja del NO ganó con 54,71 % (no «cerca de 56»); la web de Berners-Lee existía hacia diciembre de 1990 y 1991 es el anuncio externo; MASP, luz libre de 74 m; Hope: la campaña no pudo respaldar el afiche por derechos y encargó otras versiones. Discrepancias sin resolver (anotadas en `R2-INCIDENCIAS.md`): lugar de muerte de Pugin, nacimiento de Paxton (1803 Science Museum, 1801 Britannica), Etruria (1769 / 1771–73), inauguración del Guggenheim Bilbao («construido hasta octubre de 1997»).

- **Tandas 8 y 9 (v72, 6 de octubre):** 48 diseñadores ★ más con 3 agentes Sonnet por tanda (t08d: de Gaudí a Paul Rand; t09d: de Müller-Brockmann a Yohji Yamamoto); **93 de 102 diseñadores ★ con fuentes**. `dates` sin cambios. Se quitaron o suavizaron frases sin respaldo (p. ej. Loos sin año de *Ornamento y delito*, Earl «dirigió» y no «fundó» Art and Colour, Frutiger sin década del estudio, Bass con el logo Bell suavizado). Datos de ficha dudosos, sin tocar (en `R2-INCIDENCIAS.md`): **Gehry murió el 5-dic-2025** (la ficha dice «n. 1929»); **Philip Johnson nació en Cleveland**, no en New Haven; Armani murió el 4 o el 5-sep-2025; Posada 1851 o 1852; Kahn nacido en Saaremaa o Pärnu; *Ornamento y delito* 1908 (ficha 1910); Castel Béranger 1894–98; Casa Tassel 1892–93; Purkersdorf 1903–05; Mirella 1956–57; Superstudio disuelto 1978 o 1982; Vanna Venturi 1961–64; Bazaar 1955 o 1957; Rams director 1961 o 1962. Fuentes débiles o de fabricante marcadas con ⚠ (Vitra, &Tradition, Knoll, Vitsœ, Fritz Hansen, Dazed, Designboom, EBSCO, visitBerlin). Pruebas sin FAIL; build sin PROBLEM.

- **Tanda 10 (v73, 6 de octubre):** los últimos 9 diseñadores ★ (de Koolhaas a Aravena): **102 de 102 diseñadores ★ con fuentes**; y los primeros 8 movimientos ★ (neoclasicismo, Beaux-Arts, neogótico, Arts and Crafts, cartel ilustrado, Escuela de Chicago, Art Nouveau, Secesión de Viena): **16 de 35 movimientos ★**. Correcciones de fondo en movimientos: Pugin aceptaba la industria (Bard Graduate Center); los rascacielos de Chicago llegaron 10 a 15 años después del incendio de 1871, no de inmediato; «modernisme en Cataluña» pasa a «modernista en España»; se quitaron frases sin respaldo («urnas, guirnaldas, palmetas», «Modern Style», Bradley y los Beggarstaffs, etc.). Datos de ficha dudosos, sin tocar: **Fernando Campana murió el 16-nov-2022** (la ficha lo da vivo); silla Vermelha 1993 (ficha 1998) y Banquete 2002 (ficha 2006); Carson 1954 o 1955; Kunsthal 1992 o 1993; Café Costes 1982 o 1984; `illustrated-poster` empieza en 1880 pero Chéret hacía carteles en color desde 1866; `arts-and-crafts` empieza en 1861 (Ruskin 1853, Casa Roja 1859–60); Home Insurance Building 1884–85. Fuentes más débiles: Dezeen (Ive), History Today y Google Arts & Culture (Secesión), página de J. Ochshorn (Cornell) para la cita de Sullivan. Pruebas sin FAIL; build sin PROBLEM. **Por pedido de Mauricio, la R2 se detiene aquí (v73).**

## 102. v74 — Nuevo plan de cierre: «LHD v1.0» (solo documentos; pendiente de «implementa»)
- **Decisión de Mauricio (6 oct 2026):** cerrar la primera versión pública cuando estén revisadas **todas las fichas ★**, con un proyecto limpio, documentación nueva sin historial y un `ROADMAP.md`. El plan está en **`tools/PLAN-V1.md`** y reemplaza las secciones 11 a 14 de `PLAN-CIERRE.md`.
- **Etapas:** R2 ampliada (fichas ★ restantes, contexto y productivo, ensayos, enlaces y conexiones de fichas ★, refuerzo de fuentes débiles, incidencias en hoja de cálculo, revisión independiente con escalada) → R2b (limpieza sin cambios de contenido, renombres por script con prueba de equivalencia) → R2c (README, BRIEF, CLAUDE, docs/, schema/) → R2d (ROADMAP) → R2e (ZIP de respaldo, web y proyecto limpio).
- **Decisiones:** (1) ensayos: solo sus propias fuentes; (2) enlaces: solo de fichas ★; (3) el sitio abre en «★ Imprescindible»; (4) modo edición se mantiene con contraseña nueva y segura en `editar.php`, entregada solo por el chat; (5) renombrar todo lo interno inconsistente (no los ids de elementos), con auditoría de no ruptura; (6) sin licencia; (7) incidencias en hoja de cálculo editable; (8) README bilingüe y el resto en español, con **nombres de archivo en inglés** (`docs/CONTENT.md`, `DATA.md`, `SOURCES.md`, `INTERFACE.md`); (9) v74, v75… hasta el paquete «LHD v1.0».
- **Confirmado por Mauricio:** «elementos de contexto» incluye los 52 productivos sin fuentes (fila «Productivo» del contexto).
- **v75:** paquete de arranque para una sesión nueva que parte en R2.0 (`CONTINUAR-R2.md` reescrito con notas técnicas; mensaje para pegar en `ESTADO-ACTUAL.md`).
- Vistos buenos: V-R2, V-nombres, V-limpieza, V-docs y V-1.0.

## 103. v76 — R2.0: herramientas de la R2 ampliada (HECHO; sin agentes ni cambios de contenido)
- **Instrucciones de Mauricio (6 oct 2026):** implementar R2.0 (herramientas) de `tools/PLAN-V1.md`; entregar la primera hoja `.xlsx` de incidencias (bloque 1, ~40 filas, clase A primero) y el ZIP; **solo cuando él lo diga explícitamente, seguir con R2.1** por tandas (máx. 3 agentes Sonnet en paralelo, 8 elementos cada uno), checkpoint con ZIP cada 2 tandas. Reglas: nada de Wikipedia; no inventar URL ni datos; cada marca [n] con su fuente; los datos de ficha dudosos no se cambian en la tanda (van a incidencias); si se alcanza un límite, se reencola y se entrega el ZIP; **nada se marca como aprobado sin su visto bueno**.
- **Herramientas** (cada una con su prueba, todas sobre copias del proyecto):
  - `prep_r2.py` (`test_r2_tools`): tipos `obras`, `diseñadores`, `movimientos`, `instituciones`, `teorias`, `contextos`, `productivos`, `ensayos`, `enlaces` y `conexiones` (de fichas ★); lleva el contexto de ambos extremos de cada enlace o conexión y los elementos citados por cada ensayo; escribe también `prompt_TANDA_k.txt`. Alcance medido: 19 movimientos, 18 instituciones, 28 teorías, 152 contextos, 52 productivos, 10 ensayos, 359 enlaces y 72 conexiones (coincide con la tabla del plan).
  - `check_r2.py`: valida los 10 tipos (campos permitidos y obligatorios por tipo, listas `traits`/`ideas`, marcas por campo y por párrafo, `[[id|texto]]` en los ensayos, `note` de enlaces y conexiones, propuestas `drop`, fuentes prohibidas, fecha AAAA-MM-DD, `--con-fuentes` para el refuerzo de la R2.5). Las 220 salidas reales anteriores pasan sin ERROR.
  - `apply2.py`: aplica ensayos a `src-essays/essays.json`; las conexiones se buscan en las 5 épocas (antes solo en el Modernismo); todo o nada; `--dry`. **Cambio de comportamiento:** `drop` ya no borra el enlace ni la conexión (antes iba directo a la reserva): queda como DROP-PROPUESTO y va a incidencias (clase E), como pide el plan.
  - Sitio y build: las marcas `[n]` de un ensayo se ven como superíndices y hay una sección «Fuentes del ensayo (n)», cerrada al abrir (`test_ensayos_fuentes`); el build rechaza marcas de ensayo sin fuente, distintas entre EN y ES o dentro de un `[[id|texto]]`, y no cuenta las marcas en el largo de los párrafos.
  - `auditoria.py --v1` (`test_r2_auditoria`): 14 categorías de la definición de terminado; código 1 mientras quede algo. Hoy: 1.434 pendientes (19 movimientos, 18 instituciones y 28 teorías ★; 152 contextos; 52 productivos; 10 ensayos; 359 enlaces; 72 conexiones; 717 incidencias abiertas; 7 obras ★ con una sola fuente; 0 marcas huérfanas ni fuentes sin citar).
  - Incidencias como datos (`test_r2_incidencias`): `tools/r2_incidencias.json` (717 incidencias de 224 elementos; fuente de verdad; clases A a E; estados `abierta|decidida|aplicada|cerrada`) y `incidencias_xlsx.py export|import|cerrar|resumen`. Se agregó una **clase E** (propuesta de quitar un enlace o conexión) que el plan no nombra, porque `drop` necesita dónde decidirse. La clase automática es un filtro por palabras clave (hoy 13 A, 22 B, 558 C, 124 D antes de curar): **solo el bloque 1 está curado a mano**; los siguientes se revisan antes de enviarlos.
  - Plantillas de prompt por tipo: `tools/pipeline/plantillas_r2.json` (fuente única) y sección regenerable de `CONTINUAR-R2.md` (`prep_r2.py --doc`); una prueba comprueba que coinciden.
- **Hoja .xlsx, bloque 1 (40 filas):** 4 de clase A (Philip Johnson nació en Cleveland, no en New Haven; Gehry murió en 2025; Fernando Campana murió en 2022; atribución del Delphos también a Adèle Henriette Nigrin), 24 de clase B (fuentes en desacuerdo: Paxton 1801/1803, Posada 1851/1852, Bazaar 1955/1957, Etruria, Pugin, Múnich 72, etc.) y 12 de clase D (`dresser-teapot` maker, `citroen-2cv-1948` designers, `lc2-armchair-1928` maker, `cadillac-eldorado-1959` designers, Guggenheim Bilbao, etc.). Todas las propuestas salen de lo que dicen las fuentes que abrieron los agentes; donde no hay base para cambiar, la propuesta es «Mantener». Solo la clase A trae «Aceptar» por defecto, y solo con una corrección concreta (`cambios` en el JSON, que una prueba contrasta con los datos actuales). Se reclasificaron a mano 6 «A» automáticas que no lo eran y Paxton, Posada y la tipografía de Múnich 72 (C o A → B).
- **A decidir / avisos:**
  1. Las 7 obras ★ con **una sola** fuente que lista `auditoria.py --v1` (`e1027-house`, `casa-del-fascio-como`, `van-nelle-factory`…) **no son** las 7 de «fuentes débiles» del plan (R2.5: `seagram-building`, `think-small`, …). Propongo reforzar ambas listas en la R2.5 (14 obras); confírmame.
  2. Falta decidir cómo se aplican las incidencias de texto (p. ej. cambiar «New Haven» por «Cleveland» en `more`): los `cambios` ya traen `de` y `a` por idioma; el paso de aplicar (R2.6) los usará y pasará por el build.
  3. `test_preview.py` lanzaba Chromium sin `executable_path` (fallaba en este entorno); ahora usa `$CHROMIUM` o `/opt/pw-browsers/chromium`, como las demás. Para correr las pruebas en un entorno nuevo hace falta `pip install playwright`.
- Pruebas: todas PASS (con las 4 nuevas: `test_ensayos_fuentes`, `test_r2_tools`, `test_r2_incidencias`, `test_r2_auditoria`). Build sin PROBLEM. Los datos de contenido no cambiaron (solo `r2_incidencias.json`, `R2-INCIDENCIAS.md` y la curaduría); el sitio cambió solo en la ficha de los ensayos.

- **Decisión de Mauricio (6 oct 2026, sobre el bloque 1):** leyó la hoja y todas las incidencias y pidió marcar las 40 como **Aceptar**. Registrado con `incidencias_xlsx.py import`: las 40 pasan a `decidida` (A 4, B 24, D 12). **Aún no se aplicó ningún cambio a los datos** (eso es la R2.6, con build y estado `aplicada`). Lectura de «Aceptar» por clase: A = adoptar la corrección (Delphos: solo acreditar a Nigrin en el texto, sin ficha nueva); B = adoptar la propuesta, casi siempre «Mantener»; D = adoptar la propuesta (p. ej. `dresser-teapot` maker → James Dixon & Sons; `lc2-armchair-1928` maker → Cassina (desde 1965); fechas de Vermelha y Banquete; materials de Beethoven y Lettera 22). Las D con «Mantener…» no cambian nada.

Próximo punto: **104**
