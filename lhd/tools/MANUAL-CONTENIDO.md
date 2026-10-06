# Manual de contenido de la LHD

*Vigente desde v20 (3 de octubre de 2026); sección 7.1 (fuentes numeradas) agregada el mismo día. Sirve para todas las fases: completar el Modernismo y escribir los demás tramos de la línea (1750–1914 y 1945–hoy).*

Este manual define **qué entra a la línea, con qué nivel de detalle y cómo se escribe y se conecta**. Es la guía de contenido vigente (la antigua guía de la fase 1 se retiró del paquete). El formato técnico de los datos está en `tools/SPEC.md` y lo valida `tools/build_data.py`.

---

## 1. La idea que ordena todo

La LHD entiende **el diseño como respuesta a su contexto**. Lo distintivo de la línea no es la lista de obras, sino **las conexiones**:

- entre el **contexto** (político, económico, social, cultural, tecnológico y productivo) y el diseño;
- entre los elementos de diseño: obras, diseñadores, movimientos, instituciones y textos.

Cada hecho de contexto está en la línea **solo porque afectó al diseño**. Cada obra y cada diseñador deberían mostrar, cuando sea verificable, **qué del contexto** los explica. Si hay que elegir entre sumar una obra más o conectar bien las que ya están, se prioriza conectar.

---

## 2. Tipos de elementos

| Tipo | Qué es | Dónde va |
|---|---|---|
| Hecho de contexto | Hecho político, económico, social, cultural o tecnológico que afectó al diseño | Filas de CONTEXTO |
| Productivo | Material, proceso o herramienta | Fila Productivo (CONTEXTO) |
| Macromovimiento | Movimiento amplio que abarca décadas y reúne a varios movimientos (Modernismo, Posmodernismo) | Primera fila de DISEÑO |
| Movimiento | Grupo o tendencia con un lenguaje y unas ideas comunes | DISEÑO |
| Institución | Escuela, empresa, estudio, exposición, asociación, museo o publicación | DISEÑO |
| Teoría | Manifiesto, tratado, libro o programa de escuela sobre el diseño | DISEÑO |
| Diseñador | Persona, dúo o colectivo | DISEÑO (línea de vida) |
| Obra | Objeto, edificio, prenda o pieza gráfica | DISEÑO (marcador) |

**Épocas.** Desde v20 no se muestran.
- Las carpetas `src-data/<época>/` (`industrial`, `reform`, `modernism`, `postwar`, `postmodern`) siguen siendo solo una forma de ordenar los archivos. Cada elemento va en la carpeta del tramo donde **empieza**: 1750–1850, 1851–1913, 1914–1944, 1945–1974 y 1975–hoy.
- El panorama que antes daba la ficha de época ahora lo da la ficha del **macromovimiento**.
- Los nombres de período que no son movimientos («Revolución Industrial») van como **hechos de contexto**.

---

## 3. Niveles de detalle

Cada elemento de diseño (movimiento, macromovimiento, institución, teoría, diseñador, obra) lleva `level`. El contexto y lo productivo no llevan nivel: **se ven siempre**.

| `level` | En el sitio | Criterio |
|---|---|---|
| `essential` | Imprescindible ★ | Lo que un curso introductorio **no puede omitir**: hitos que se citan en cualquier historia general y que todo estudiante debería reconocer. |
| `normal` | Normal | Todo lo demás: lo que da **cuerpo y variedad** (otras disciplinas y regiones, incluida América Latina y Chile; ejemplos claros de cómo un contexto afectó al diseño; la obra principal de diseñadores no imprescindibles) y también los casos más especializados (segundas obras, variantes, piezas de interés local o técnico). Es el nivel que se ve al abrir el sitio. |

*Punto 72 (4 de octubre de 2026; APLICADO en v44, paso 6.7):* la **etiqueta visible** del nivel `normal` pasó de «Normal» a **«Completo»** (EN «Complete»); el valor interno `normal` no cambia. Hasta entonces el sitio sigue diciendo «Normal». En este manual y en los briefs, «Normal» y «Completo» designan el mismo nivel.

*Punto 79 (5 de octubre de 2026, decisión D3 del V4; regla C4d del plan):* **el nivel ★ se decide por importancia historiográfica**, con la definición de esta sección («hitos que se citan en cualquier historia general»). A toda obra ★ se le buscan enlaces de contexto (idealmente dos directos de subcategorías distintas) **sin forzarlos**; si no hay un enlace cierto, se anota una excepción C4c. Nunca se baja una ★ por falta de enlaces. Los hitos chilenos ★ se limitan a los aprobados (Cybersyn, Quinta Monroy, arpilleras, franja del NO).

*Punto 79 (decisión D2 del V4):* la disciplina `fashion` se rotula «Moda», pero abarca **moda y textil** (estampados, tejidos, tapices, arpilleras). La ficha de disciplina de la etapa 8 lo explica.

*Punto 71 (etapa 6, regla C4c del plan):* para los elementos agregados en la etapa 6 la exigencia de enlaces directos puede relajarse en casos excepcionales (anotados en la propuesta V3); ningún elemento queda sin conexión directa o secundaria. Sigue mandando el resto de este manual.

*Decisión del 4 de octubre de 2026 (punto 48):* hay **solo dos niveles**. El antiguo «Completo» se fusionó con Normal y ya no se amplía el catálogo para llenarlo. Cuando la línea esté terminada se reevaluará un nivel de alto detalle.

**Reglas:**
1. **Los niveles se suman.** «Imprescindible» muestra solo lo ★; «Normal» muestra todo.
2. **Proporciones orientativas:**
   - Imprescindible: alrededor del 25–35 % de cada tipo. Por ejemplo, en el Modernismo hay 37 obras ★ de 138.
   - El resto es Normal.
3. **Diseñadores:** su nivel sale de **sus obras y de su importancia histórica**.
   - **Regla dura (el build la exige):** un diseñador debe tener al menos una obra de su mismo nivel o de uno más básico. Si no, su línea de vida aparecería vacía en ese nivel.
   - Si un diseñador es históricamente imprescindible pero ninguna de sus obras lo es, se sube a ★ su obra más representativa. Así se hizo con Rodchenko (cartel «Libros») y Tschichold (*Die neue Typographie*).
4. **Macromovimientos:** siempre `essential`.
5. **Todo `essential` necesita al menos un enlace de contexto** (el build avisa).
6. **Las fichas siempre muestran todas las conexiones**, aunque apunten a elementos de otro nivel. Al ir a uno de esos elementos con el detalle en «Imprescindible», el detalle pasa a «Normal».
7. **La ★** marca todo lo imprescindible: obras, diseñadores, movimientos, instituciones y teoría.

---

## 4. Qué entra a la línea

- **Diseñadores:**
  - **Todo diseñador tiene al menos una obra relevante y verificada.** Sin obra no entra (el build da `PROBLEM`).
  - Si un diseñador muy importante no tiene obra, se le agrega al menos una.
  - **Meta:** al menos dos obras por diseñador importante.
- **Obras:**
  - **Meta de cantidad:** la línea necesita más obras. Para el Modernismo, entre 130 y 150 (hoy 96).
  - **Equilibrio:** entre disciplinas, regiones y géneros. Visibilizar a las mujeres, los colectivos y el trabajo en empresas.
- **Contexto:** un hecho entra solo si explica al menos un elemento de diseño (el build da `PROBLEM` si no tiene enlaces). **Si para conectar bien el diseño hace falta un hecho que no está, se agrega**: ampliar el contexto es parte del trabajo, no una excepción.
- **Macromovimientos:** solo para tendencias amplias que la historiografía reconoce como tales y que reúnen varios movimientos.
  - Hoy son Modernismo (1907–1970) y Posmodernismo (1966–1995). Sus fechas son aproximadas, con bordes difusos (`fadeIn`/`fadeOut`).
  - No se crean macromovimientos para nombres de períodos («Reforma», «Posguerra»), que se eliminaron en v20.
- **No forzar:** un elemento que no se sostiene con fuentes se propone para retiro, no se deja «por si acaso».

---

## 5. Conexiones

### 5.1 Enlaces de contexto (`links` en `80-context-links.json`)

Son el corazón de la línea. Formato: `{ctx, item, note, es:{note}}`.

1. **Explicar un mecanismo, no una coincidencia de fechas** (prueba de tres preguntas en la sección 9.1). La nota responde *qué del contexto* cambió *qué decisión de diseño*, en una o dos frases (≤ ~200 caracteres).
   - Mal: «Relacionado con la guerra».
   - Bien: «La escasez de la guerra y los nuevos roles de las mujeres favorecieron su ropa simple de jersey».
2. **No forzar.** Un enlace débil es peor que ninguno; si no se encuentra una relación verificable, no se pone.
3. **Sin determinismo.** El contexto condiciona, no causa. Usar «respondió a», «hizo posible», «empujó hacia», «se difundió con». Si corresponde, decir también cómo el diseño modificó el contexto.
4. **Cobertura (metas):**
   - Toda obra con al menos un enlace donde la relación sea verificable; las imprescindibles, con 2 o 3 enlaces de **distintas** subcategorías.
   - Todo diseñador con enlaces propios, no solo heredados de sus obras.
   - Todo movimiento, institución y texto teórico con al menos un enlace. Hoy la teoría tiene 0 de 14.
   - Todo hecho de contexto debe explicar varios elementos, de más de una disciplina.
5. **Enlaces entre tramos** se admiten. Por ejemplo, el taylorismo de 1911 explica la cocina de 1926, y la Revolución Industrial explica el Modernismo.

### 5.2 Conexiones indirectas (las calcula el sitio)

El sitio muestra y dibuja, con **línea más fina**, las relaciones heredadas:
- un diseñador hereda el contexto de sus obras («Vía: obra»);
- una obra hereda los movimientos e instituciones de su diseñador;
- un movimiento o una institución incluye las obras que sus diseñadores hicieron mientras existió.

No hay que escribirlas como enlaces propios, **pero no reemplazan a los enlaces directos**: si la relación es directa y verificable, se escribe.

### 5.3 Conexiones de diseño (`connections`)

`{from, to, note, es:{note}}` entre cualquier par de elementos (influencias, respuestas, continuidades), siempre con matiz.

---

## 6. Cómo se escribe cada ficha

Valen las reglas de estilo de la guía de la Fase 1 (sección 8):
- inglés principal y `es` completo en español de Chile o neutro;
- nombres cortos y sin paréntesis;
- `key` de una oración;
- largos máximos;
- tipografía (’, –, →).

Los cambios de v20 son estos.

**Campos nuevos o cambiados:**
- `level` (`essential|normal`) en movimientos, instituciones, teoría, diseñadores y obras. **Reemplaza a `star`**: el build rechaza `star` en las fuentes y lo calcula solo.
- Ya no hay `lane` en ningún tipo. El agrupamiento lo hace «Organizar».
- **Macromovimiento:** es un movimiento con estos campos:
  - `macro: true`;
  - `parts`: los ids de los movimientos que reúne;
  - `context_summary` {political, economic, social, cultural, technological}, en EN y ES, obligatorio;
  - `shifts`: 3 a 5 cambios clave, en EN y ES y en igual número;
  - además de `key`, `traits`, `context` y `shift`.

**Fuentes y enlaces («Saber más»):**
- `where` [{label, url https}] en las obras: la **fuente** (museo, archivo, colección, catálogo) y **páginas relevantes** (empresa fabricante, fundación, sitio patrimonial, archivo del diseñador). Es lo que la ficha muestra en «Saber más». **Nunca Wikipedia.**
- Teoría: `sources` [{label, es, url https}], al menos una (texto en línea o edición).
- `wiki` (título de Wikipedia en inglés) **se mantiene solo para obtener la imagen** de Wikimedia Commons. No se muestra como enlace: al hacer clic en la imagen se abre su página de origen. Sin imagen libre, la ficha no muestra imagen.
- Ya no existen las secciones «Buscar en» ni «Dónde verla».

---

## 7. Verificación

Vale el protocolo de la sección 7 de la guía de la Fase 1:
- cada fecha, nombre, atribución y cifra se verifica en una fuente confiable (museo, archivo, catálogo razonado, bibliografía académica);
- lo dudoso se dice en el texto («hacia 1927», «atribuida a»);
- nada se escribe de memoria sin comprobar.

Las fuentes de «Saber más» deben ser enlaces vivos con `https`.

### 7.1 Trazabilidad: fuentes numeradas en cada ficha (`refs`)

*Decisión del 3 de octubre de 2026 (punto 44 de `CAMBIOS-PENDIENTES.md`).* **Toda información que se escriba o se revise queda trazada a su fuente desde ese momento.** Vale en todas las tareas: redacción, verificación, revisión de enlaces y revisión independiente.

1. **Campo `refs`** en cada elemento (hecho de contexto, productivo, macromovimiento, movimiento, institución, teoría, diseñador, obra) y en cada enlace de contexto (`links`):

   ```json
   "refs": [
     {"label": "V&A, Kubus-Geschirr, C.63-1993", "url": "https://collections.vam.ac.uk/item/O249831/…",
      "checks": "fecha (1938), fabricante, uso en el refrigerador", "date": "2026-10-03"}
   ]
   ```

   - `label`: institución y documento.
   - `url`: enlace **directo** a la página consultada (https), no a la portada del sitio.
   - `checks`: qué afirmaciones sostiene, en español.
   - `date`: fecha de consulta (AAAA-MM-DD).
   - El número de cada fuente es su posición en la lista (1, 2, 3…), **por ficha**.
2. **Marcas en el texto:** `[1]`, `[2]`… al final de la frase o afirmación que sostiene esa fuente. *(Desde v30, punto 59, las marcas se ven en el sitio público como superíndices y las fuentes van en la sección «Fuentes» al final de cada ficha; ya no son internas de `?editar`. Una ficha sin fuentes muestra la advertencia «no revisada».)*
   - Van en todos los campos de texto (`key`, `more`, `happened`, `note`, etc.) en EN y ES, con **los mismos números** en ambos idiomas.
   - Una frase puede llevar varias marcas (`[1][3]`), y una fuente puede citarse varias veces.
   - Las fechas, cifras y atribuciones siempre llevan marca.
   - **Excepción (v22):** la `key` de un hecho de contexto resume lo que ya está marcado en `happened` y `effect`; no lleva marca si no agrega datos nuevos. La `key` de obras, diseñadores y demás elementos sí lleva marca.
   - **Solo se marca lo que la fuente dice.** Si una frase mezcla un dato general (por ejemplo, las fechas de un gobierno) con lo que la fuente sostiene, se separan las frases y la marca va solo donde corresponde; lo general queda sin marca y se anota como pendiente en `checks` (⚠).
   - Lo que solo dice el fabricante actual o un blog se **atribuye** en el texto («según Thonet…», «según se dice…»).
   - En el sitio público las marcas no se ven ni se buscan. Solo aparecen como superíndices en el modo `?editar`, sección «Revisión → Fuentes».
3. **Enlaces de contexto:** sus `refs` sostienen el mecanismo de la nota (la tercera pregunta de la prueba, 9.1: «¿cómo lo sabemos?»). Se ven en la revisión de las dos fichas que conecta.
4. **Qué fuentes valen:** las de la sección 7 (museo, archivo, catálogo, bibliografía académica, sitio patrimonial u oficial).
   - **Wikipedia no es fuente de verificación**: puede servir para orientarse, pero no se registra.
   - Lo que solo se confirmó en una fuente secundaria se escribe con cautela y su `checks` lo dice («⚠ fuente secundaria»).
   - Si la página se leyó a través de un resumen automático y no completa, las citas textuales se comprueban de nuevo antes de publicarlas.
5. **Relación con «Saber más»:** `where` y `sources` son lo **público**. `refs` es **interno**, para revisar. Una misma fuente puede estar en ambos.
6. **El build:**
   - da `PROBLEM` si una marca no tiene fuente o si una URL no es https;
   - da `WARN` si una fuente no se cita en el texto, si es de Wikipedia o si un elemento no tiene `refs`.
7. **Registro de lo dudoso:** lo pendiente de fuentes se anota en `tools/PENDIENTES-FUENTES.md`. Las fuentes de cada afirmación se guardan en `refs`, para que la ficha sea trazable por sí sola.

---

## 8. Lista de control para cada lote

- [ ] Cada elemento de diseño tiene `level` y respeta las proporciones del punto 3.
- [ ] Cada diseñador tiene al menos una obra de su nivel o de uno más básico.
- [ ] Cada obra y cada diseñador tienen enlaces de contexto donde la relación es verificable; los imprescindibles, al menos uno.
- [ ] Cada hecho de contexto nuevo explica al menos un elemento.
- [ ] «Saber más» (`where`) con fuente y páginas relevantes, sin Wikipedia.
- [ ] Cada ficha y cada enlace nuevos o revisados llevan `refs` con enlace directo, y sus afirmaciones llevan marcas `[n]` en EN y ES (sección 7.1).
- [ ] `python3 tools/build_data.py` sin `PROBLEM`, con los `WARN` revisados.
- [ ] Revisión en el navegador: los niveles Imprescindible y Normal; el filtro «Solo» de algunos elementos; las curvas finas.

---

## 9. Lecciones de la literatura académica

**Decisión del 3 de octubre de 2026:** de las lecciones conversadas se incorpora **solo la primera**. Las demás no se incorporan por ahora:
- la mediación y el consumo como tipo de enlace;
- más diseño anónimo, vernáculo y femenino (antes pensado para el nivel Completo, que ya no existe);
- la biografía de los objetos;
- evitar el relato de progreso hacia el modernismo (la eliminación de las épocas ya avanza en esa línea).

### 9.1 La conexión con el contexto debe ser más profunda que una coincidencia de fechas (incorporada)

Viene de la historia del diseño basada en el contexto, en particular Adrian Forty, *Objects of Desire* (1986), y del debate posterior: el diseño materializa ideas, condiciones y necesidades de su sociedad. Que dos cosas ocurran en los mismos años **no** es una conexión.

**Prueba para cada enlace (`note`).** Antes de escribirlo, responder tres preguntas:
1. **¿Qué cambió en el contexto?** Una ley, una escasez, un mercado nuevo, una técnica, una idea, un grupo social.
2. **¿Qué decisión de diseño cambió por eso?** Forma, material, tamaño, precio, público, uso, modo de producción o de difusión.
3. **¿Cómo lo sabemos?** Hay una fuente que lo sostiene: un testimonio de la época, un encargo, una cifra, la bibliografía.

Si no se pueden responder las tres, **no se crea el enlace**.

| No sirve (coincidencia) | Sirve (mecanismo) |
|---|---|
| «Diseñada durante la Gran Depresión.» | «Con la caída de las ventas tras 1929, los fabricantes encargaron rediseños de carcasa para renovar productos sin cambiar la mecánica; el Coldspot se vendió por su aspecto.» |
| «Obra de la época de la vanguardia.» | «La serie dio a las vanguardias un estante común: Mondrian, Van Doesburg y Malévich explicaron sus ideas en libros diseñados con la misma tipografía nueva.» |
| «Relacionada con la vivienda social.» | «Hecha para los departamentos pequeños y estandarizados del Nuevo Frankfurt, donde una cocina eficiente ahorraba pasos y tiempo.» |

**Matices obligatorios:**
- El contexto **condiciona, no causa**. Usar verbos como «respondió a», «hizo posible», «empujó hacia», «limitó», «se difundió con».
- Cuando corresponda, decir también **cómo el diseño actuó sobre el contexto**: la propaganda que movilizó, la vivienda que cambió la vida doméstica.
- Una sola relación bien explicada vale más que tres vagas.

**En la revisión de cada lote:**
- Leer todas las notas nuevas con esta prueba.
- Reescribir o eliminar las que solo describen simultaneidad.
- Los enlaces existentes del Modernismo se revisan con este criterio en la fase de ampliación (ver `tools/PLAN-CIERRE.md`, Parte II).

## 11. Elementos de fuera de Occidente (punto 61, v31)

La LHD cubre Europa, Norteamérica y América Latina (más lo `global`). Asia, África, Medio Oriente y Oceanía no tienen elementos propios, **salvo los que tengan influencia demostrable en el diseño occidental** (japonismo, metabolismo, Muji, Kawakubo, Yamamoto y similares; orientativo 6 a 10 en toda la línea, no es tope).
- Llevan `regions: ["global"]`, su país en `countries` y **una línea de mecanismo** que explica la influencia (en su enlace de contexto o en su ficha).
- Como son `global`, se ven siempre (el filtro de región no los oculta); en «Organizar por región» caen en el grupo «Global», zona «Más allá de Occidente», que solo aparece si existe alguno.
- `tools/pipeline/validate_out.py` exige `regions: ["global"]` cuando `countries` trae un país de esa zona (códigos en `ZONE_OF` de `app.js`).

