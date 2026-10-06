# Listas de cierre (etapa 1): qué entra y cómo se conecta

> **Nota (plan v8, puntos 71 y 72):** estas listas cubren las etapas 2 a 5 (375 obras). La **etapa 6** agrega una propuesta aparte (`tools/PROPUESTA-ETAPA6.md`, aún no escrita) con obras, diseñadores, movimientos, instituciones y contexto nuevos hasta llegar a ≥ 500 obras. «N» en las tablas es el nivel `normal`, que desde el paso 6.7 se muestra como «Completo».

Generado en la etapa 1 (v32) a partir de `tools/listas/<tramo>.md`. **Pendiente de V1** (visto bueno de Mauricio). No es contenido final: define ids, nombres, nivel (★ o N) y la línea de mecanismo de cada enlace obra → contexto. `tools/pipeline/listas_check.py` lo verifica; `apply_new.py --links-from-lists` lee las columnas «relaciona».

- **Modernismo** no tiene lista nueva: se reduce con `tools/RECORTE-MODERNISMO.md` (paso 1.7, después de V1) y recibe de vuelta `ctx-corfo` y `ctx-early-television` desde la reserva.
- Los elementos que ya existen en `src-data/` van en las tablas con su mismo id. Las obras sin diseñador o con fechas inciertas se revisan en la Parte II (fuentes).
- Reserva: elementos que quedan fuera pero se pueden meter si falta en un tipo (no cuentan para las cantidades).

## Tramo: industrial

### Contextos

| id | nombre | sub | años | regiones | nivel | relaciona |
|---|---|---|---|---|---|---|
| `ctx-atlantic-revolutions` | Revoluciones de EE. UU. y Francia | political | 1776–1799 | europe, north-america | ★ | |
| `ctx-napoleonic-empire` | Imperio napoleónico | political | 1799–1815 | europe | ★ | `empire-regency` |
| `ctx-latin-american-independence` | Independencias latinoamericanas | political | 1808–1825 | latin-america | ★ | |
| `ctx-restoration-europe` | Restauración europea | political | 1815–1848 | europe | N | `biedermeier` |
| `ctx-penny-post` | Reforma postal británica | political | 1839–1840 | europe | N | |
| `ctx-industrial-revolution` | Revolución Industrial | economic | 1760–1840 | europe | ★ | `macro-modernism` |
| `ctx-division-of-labour` | División del trabajo y sistema de fábrica | economic | 1750–1850 | europe | ★ | `ctx-clock-time` |
| `ctx-cotton-colonial-trade` | Comercio colonial y algodón | economic | 1750–1850 | europe | N | |
| `ctx-middle-class-consumption` | Consumo de clase media | economic | 1750–1850 | europe | ★ | |
| `ctx-registered-designs` | Registro legal de diseños | economic | 1839–1842 | europe | N | `inst-government-school-of-design`, `th-journal-of-design`, `inst-thonet` |
| `ctx-urbanisation-working-class` | Urbanización y clase obrera | social | 1780–1850 | europe | ★ | `inst-government-school-of-design` |
| `ctx-clock-time` | Tiempo de reloj y disciplina de fábrica | social | 1760–1850 | europe | N | `ctx-railways` |
| `ctx-luddism` | Ludismo y resistencia a las máquinas | social | 1811–1816 | europe | N | `ctx-industrial-revolution` |
| `ctx-reading-public` | Público lector en expansión | social | 1750–1850 | europe | N | |
| `ctx-revolutionary-dress` | Vestido tras la Revolución | social | 1789–1815 | europe | N | |
| `ctx-enlightenment` | Ilustración y Encyclopédie | cultural | 1751–1789 | europe | ★ | |
| `ctx-neoclassical-antiquarianism` | Redescubrimiento de la Antigüedad | cultural | 1738–1830 | europe | ★ | |
| `ctx-romanticism-gothic` | Romanticismo y gusto gótico | cultural | 1750–1850 | europe | N | |
| `ctx-periodical-press` | Prensa periódica | cultural | 1750–1850 | europe, latin-america | ★ | |
| `ctx-egyptomania` | Egiptomanía tras la campaña de Napoleón | cultural | 1798–1830 | europe | N | `display-types`, `empire-regency` |
| `ctx-steam-power` | Máquina de vapor | technological | 1769–1850 | europe | ★ | `iron-printing-press`, `ctx-railways` |
| `ctx-railways` | Ferrocarril | technological | 1825–1850 | europe | N | `cast-iron` |
| `ctx-iron-construction` | Hierro fundido y construcción | technological | 1779–1850 | europe | N | |

### Productivo

| id | nombre | sub | años | nivel | relaciona |
|---|---|---|---|---|---|
| `creamware` | Loza cremosa (Queen's ware) | materials | 1760–1850 | ★ | `inst-wedgwood` |
| `cast-iron` | Hierro fundido | materials | 1779–1850 | N | `ctx-iron-construction` |
| `wove-paper` | Papel avitelado | materials | 1757–1850 | N | `inst-ackermann` |
| `lithography` | Litografía | processes | 1796–1850 | ★ | `inst-ackermann` |
| `steam-bentwood` | Madera curvada al vapor | processes | 1836–1850 | ★ | `inst-thonet` |
| `wood-engraving` | Grabado en madera de testa | processes | 1790–1850 | N | `ctx-reading-public` |
| `iron-printing-press` | Prensa de hierro | tools | 1800–1850 | N | `ctx-reading-public` |
| `punched-card-weaving` | Tarjetas perforadas para telares | tools | 1804–1850 | ★ | `inst-conservatoire-arts-metiers` |
| `display-types` | Tipos gruesos, egipcios y de palo seco | tools | 1803–1850 | N | `ctx-urbanisation-working-class` |

### Teoría

| id | nombre | años | nivel | relaciona |
|---|---|---|---|---|
| `th-chippendale-director` | The Gentleman and Cabinet-Maker's Director | 1754 | ★ | `thomas-chippendale` |
| `th-hepplewhite-guide` | The Cabinet-Maker and Upholsterer's Guide | 1788 | N | `th-chippendale-director` |
| `th-sheraton-drawing-book` | The Cabinet-Maker and Upholsterer's Drawing-Book | 1791–1794 | N | `th-hepplewhite-guide` |
| `th-pugin-true-principles` | The True Principles of Pointed or Christian Architecture | 1841 | ★ | `pugin`, `historicism` |
| `th-journal-of-design` | Journal of Design and Manufactures | 1849–1852 | N | `inst-government-school-of-design` |

### Movimientos

| id | nombre | años | nivel | relaciona |
|---|---|---|---|---|
| `neoclassicism` | Neoclasicismo | 1750–1830 | ★ | `ctx-neoclassical-antiquarianism` |
| `empire-regency` | Estilo Imperio y Regencia | 1799–1830 | ★ | `neoclassicism` |
| `historicism` | Historicismos (neogótico y otros revivals) | 1750–1900 | ★ | `ctx-romanticism-gothic` |
| `biedermeier` | Biedermeier | 1815–1848 | N | `empire-regency` |
| `shaker-design` | Diseño shaker | 1790–1860 | N | `shaker-ladderback-chair-1800` |

### Instituciones

| id | nombre | años | nivel | relaciona |
|---|---|---|---|---|
| `inst-wedgwood` | Wedgwood (Etruria) | 1769 | ★ | `ctx-division-of-labour` |
| `inst-soho-manufactory` | Soho Manufactory de Boulton | 1766 | N | `ctx-steam-power` |
| `inst-conservatoire-arts-metiers` | Conservatoire des arts et métiers | 1794 | N | `ctx-atlantic-revolutions`, `ctx-enlightenment` |
| `inst-government-school-of-design` | Government School of Design | 1837 | ★ | `ctx-industrial-revolution` |
| `inst-thonet` | Thonet | 1819 | N | `ctx-steam-power` |
| `inst-ackermann` | Ackermann y su Repository of Arts | 1795–1828 | N | `ctx-periodical-press` |

### Diseñadores

| id | nombre | años | disciplinas | nivel | obras | relaciona |
|---|---|---|---|---|---|---|
| `josiah-wedgwood` | Josiah Wedgwood | 1730–1795 | product | ★ | `queens-ware-1765`, `wedgwood-jasperware-1775` | `inst-wedgwood`, `neoclassicism` |
| `matthew-boulton` | Matthew Boulton | 1728–1809 | product | N | `boulton-ormolu-vases-1770` | `inst-soho-manufactory`, `neoclassicism` |
| `thomas-chippendale` | Thomas Chippendale | 1718–1779 | product | ★ | `chippendale-ribbon-chair-1754` | `th-chippendale-director` |
| `robert-adam` | Robert Adam | 1728–1792 | architecture, product | ★ | `osterley-etruscan-room-1775` | `neoclassicism` |
| `john-baskerville` | John Baskerville | 1706–1775 | graphic | ★ | `baskerville-virgil-1757` | `neoclassicism` |
| `giambattista-bodoni` | Giambattista Bodoni | 1740–1813 | graphic | N | `bodoni-manuale-1788` | `neoclassicism` |
| `firmin-didot` | Firmin Didot | 1764–1836 | graphic | N | `didot-type-1784` | `neoclassicism` |
| `thomas-bewick` | Thomas Bewick | 1753–1828 | graphic | N | `bewick-quadrupeds-1790` | |
| `percier-fontaine` | Charles Percier y Pierre Fontaine | 1764–1838 / 1762–1853 | architecture | ★ | `malmaison-1800` | `empire-regency` |
| `karl-friedrich-schinkel` | Karl Friedrich Schinkel | 1781–1841 | architecture | ★ | `altes-museum-1830`, `bauakademie-1836` | `neoclassicism` |
| `pugin` | Augustus Welby Northmore Pugin | 1812–1852 | architecture, product | ★ | `westminster-1840` | `historicism`, `th-pugin-true-principles` |
| `michael-thonet` | Michael Thonet | 1796–1871 | product | ★ | `thonet-boppard-chair-1836` | `inst-thonet`, `biedermeier` |
| `rose-bertin` | Rose Bertin | 1747–1813 | fashion | N | `marie-antoinette-gowns-1775` | |
| `joseph-marie-jacquard` | Joseph Marie Jacquard | 1752–1834 | product | N | `jacquard-loom-1804` | `empire-regency` |

### Obras

| id | título | disciplina | año | nivel | diseñadores | tech | regiones | contextos |
|---|---|---|---|---|---|---|---|---|
| `baskerville-virgil-1757` | Virgilio de Baskerville | graphic | 1757 | ★ | `john-baskerville` | `wove-paper` | europe | `ctx-enlightenment`: el gusto ilustrado por la claridad pide libros sobrios, de letra nítida y página limpia; `ctx-industrial-revolution`: Baskerville venía de la manufactura de Birmingham y aplicó método industrial a tinta, papel prensado en caliente y prensa |
| `bodoni-manuale-1788` | Manuale tipografico de Bodoni (1788) | graphic | 1788 | N | `giambattista-bodoni` | | europe | `ctx-neoclassical-antiquarianism`: el ideal clásico de orden y simetría inspira letras de contraste extremo y trazo geométrico; `ctx-napoleonic-empire`: Bodoni imprimió ediciones de lujo para cortes y gobiernos de la era napoleónica en Italia |
| `didot-type-1784` | Tipo Didot | graphic | 1784 | N | `firmin-didot` | | europe | `ctx-enlightenment`: la imprenta racional de la Ilustración busca letras de máxima nitidez y exactitud geométrica |
| `caslon-egyptian-1816` | Egyptian de Caslon (primer palo seco impreso) | graphic | 1816 | N | | `display-types` | europe | `ctx-egyptomania`: la fiebre egipcia posterior a la campaña de Napoleón da nombre y prestigio a las letras de trazo uniforme; `ctx-urbanisation-working-class`: la ciudad llena de avisos y carteles necesita letras gruesas, legibles desde lejos |
| `bewick-quadrupeds-1790` | General History of Quadrupeds | graphic | 1790 | N | `thomas-bewick` | `wood-engraving` | europe | `ctx-reading-public`: el público lector crece y compra libros ilustrados baratos que el grabado a contrafibra imprime junto al texto; `ctx-enlightenment`: la historia natural ilustrada pide imágenes exactas hechas por observación directa |
| `penny-black-1840` | Penny Black | graphic | 1840 | ★ | | | europe | `ctx-penny-post`: la tarifa única prepagada de 1840 obliga a diseñar un sello fácil de reconocer y difícil de falsificar; `ctx-railways`: el ferrocarril acelera el reparto nacional del correo y hace viable la tarifa única |
| `encyclopedie-plates-1762` | Láminas de oficios de la Encyclopédie | graphic | 1762 | ★ | | | europe | `ctx-enlightenment`: la Encyclopédie documenta oficios y técnicas con láminas precisas y dignifica el saber del trabajo manual; `ctx-division-of-labour`: las láminas muestran talleres con tareas separadas, la lógica de dividir el trabajo que describiría Adam Smith |
| `la-aurora-de-chile-1812` | La Aurora de Chile | graphic | 1812 | ★ | | | latin-america | `ctx-latin-american-independence`: la Junta chilena usa el primer periódico del país para dar forma pública a la causa patriota; `ctx-periodical-press`: la prensa periódica, impresa en una imprenta traída de Estados Unidos, difunde las ideas ilustradas y patriotas |
| `gaceta-de-buenos-aires-1810` | Gaceta de Buenos Aires | graphic | 1810 | N | | | latin-america | `ctx-latin-american-independence`: tras la Revolución de Mayo la gaceta lleva al papel la autoridad de la nueva Junta; `ctx-periodical-press`: es la voz impresa del gobierno patriota, con formato de periódico europeo |
| `bandera-belgrano-1812` | Bandera de Belgrano | graphic | 1812 | N | | | latin-america | `ctx-latin-american-independence`: la guerra de independencia exige emblemas propios y Belgrano propone en 1812 una bandera para el ejército patriota; `ctx-atlantic-revolutions`: las banderas y cucardas de EE. UU. y Francia dan el modelo del emblema nacional de colores simples |
| `queens-ware-1765` | Loza Queen's ware de Wedgwood | product | 1765 | ★ | `josiah-wedgwood` | `creamware` | europe | `ctx-division-of-labour`: Wedgwood separa tareas en Etruria y estandariza cada pieza, de modo que el diseño pasa a ser un paso previo; `ctx-middle-class-consumption`: una clase media creciente quiere vajilla elegante a precio razonable, que Wedgwood vende con catálogos ilustrados; `ctx-clock-time`: en Etruria se impone horario fijo y disciplina de fábrica a los operarios |
| `wedgwood-jasperware-1775` | Jasperware de Wedgwood | product | 1775 | N | `josiah-wedgwood` | | europe | `ctx-neoclassical-antiquarianism`: los relieves blancos sobre fondo de color reinterpretan camafeos y vasos antiguos que el público conoce por grabados; `ctx-middle-class-consumption`: se vende como objeto de adorno a coleccionistas y burguesía ilustrada |
| `chippendale-ribbon-chair-1754` | Silla ribbon-back de Chippendale | product | 1754 | N | `thomas-chippendale` | | europe | `ctx-middle-class-consumption`: el catálogo impreso ofrece modelos a comerciantes y terratenientes que antes no compraban muebles de diseño; `ctx-cotton-colonial-trade`: el comercio colonial trae caoba de las Antillas, la madera que define su estilo |
| `windsor-chair-1750` | Silla Windsor | product | 1750 | N | | | europe, north-america | `ctx-middle-class-consumption`: la silla de piezas torneadas, barata y fácil de armar, se vende a tabernas y hogares de ingreso medio; `ctx-urbanisation-working-class`: la vida urbana multiplica casas pequeñas y locales públicos que necesitan asientos baratos y livianos |
| `shaker-ladderback-chair-1800` | Silla de respaldo de escalera shaker | product | 1800 | N | | | north-america | `ctx-atlantic-revolutions`: la república estadounidense permite comunidades religiosas autónomas como los shakers, que fijan por regla un diseño sin ornamento; `ctx-industrial-revolution`: los shakers adoptaron pronto herramientas mecánicas y producción en serie en sus talleres |
| `thonet-boppard-chair-1836` | Silla Boppard de Thonet | product | 1836 | N | `michael-thonet` | `steam-bentwood` | europe | `ctx-steam-power`: el vapor ablanda la madera de haya, que se curva en moldes sin tallar; `ctx-restoration-europe`: bajo el Biedermeier la clientela burguesa quiere muebles sobrios y livianos que Thonet convierte en pieza de serie |
| `stanhope-press-1800` | Prensa Stanhope | product | 1800 | N | | `iron-printing-press` | europe | `ctx-iron-construction`: el hierro fundido sustituye a la madera y da a la prensa más fuerza y precisión; `ctx-reading-public`: la demanda de impresos del público lector empuja a buscar prensas más rápidas |
| `jacquard-loom-1804` | Telar Jacquard | product | 1804 | ★ | `joseph-marie-jacquard` | `punched-card-weaving` | europe | `ctx-luddism`: los tejedores veían en la máquina una amenaza para su oficio, como en las protestas obreras contra las máquinas; `ctx-napoleonic-empire`: Napoleón favoreció la industria sedera de Lyon y el telar se adoptó con apoyo oficial |
| `boulton-ormolu-vases-1770` | Jarrones de ormolú de Boulton | product | 1770 | N | `matthew-boulton` | | europe | `ctx-neoclassical-antiquarianism`: los jarrones de bronce dorado copian modelos antiguos de moda en Inglaterra; `ctx-industrial-revolution`: Boulton fabrica objetos de lujo en una manufactura de gran escala con división del trabajo |
| `ironbridge-1779` | Puente de hierro de Coalbrookdale | architecture | 1779 | N | | `cast-iron` | europe | `ctx-iron-construction`: la fundición de Coalbrookdale permitió producir piezas de hierro fundido para un puente de arco; `ctx-industrial-revolution`: se construye en el corazón industrial inglés, sobre el Severn, para el transporte de carbón y productos |
| `osterley-etruscan-room-1775` | Sala etrusca de Osterley Park | architecture | 1775 | N | `robert-adam` | | europe | `ctx-neoclassical-antiquarianism`: Adam toma decoración de Pompeya y pintura romana para componer el interior completo, de muros a muebles |
| `malmaison-1800` | Interiores de Malmaison | architecture | 1800 | N | `percier-fontaine` | | europe | `ctx-napoleonic-empire`: Josefina y Napoleón encargan interiores que expresan el poder del Consulado; `ctx-neoclassical-antiquarianism`: Percier y Fontaine adaptan modelos antiguos a muebles y decoración |
| `altes-museum-1830` | Altes Museum de Berlín | architecture | 1830 | N | `karl-friedrich-schinkel` | | europe | `ctx-enlightenment`: es un museo público pensado para educar al ciudadano con arte antiguo; `ctx-restoration-europe`: el Estado prusiano posterior a 1815 usa la arquitectura clásica para dar identidad al nuevo orden |
| `bauakademie-1836` | Bauakademie de Berlín | architecture | 1836 | N | `karl-friedrich-schinkel` | | europe | `ctx-industrial-revolution`: Schinkel viajó a Inglaterra en 1826 y quedó impresionado por las fábricas de ladrillo, de estructura visible |
| `westminster-1840` | Palacio de Westminster | architecture | 1840 | ★ | `pugin` | | europe | `ctx-romanticism-gothic`: el Parlamento reconstruido tras el incendio de 1834 adopta el gótico, asociado a la tradición nacional que reivindica el romanticismo; `ctx-industrial-revolution`: Pugin llena el edificio de diseños para fabricación industrial como baldosas, papeles y muebles |
| `strawberry-hill-1750` | Strawberry Hill | architecture | 1750 | N | | | europe | `ctx-romanticism-gothic`: Walpole, escritor y anticuario, convierte su casa en manifiesto del gusto por lo medieval y pintoresco |
| `empire-silhouette-1800` | Vestido de talle alto de estilo Imperio | fashion | 1800 | ★ | | | europe | `ctx-revolutionary-dress`: tras la Revolución se abandonan el corsé rígido y las marcas de rango y el vestido pasa a una silueta simple y ligera; `ctx-cotton-colonial-trade`: la muselina de algodón importada y la fiebre por telas livianas dan material al vestido blanco de talle alto; `ctx-neoclassical-antiquarianism`: las túnicas de estatuas y vasos antiguos son el modelo de la línea recta de talle alto |
| `heideloff-gallery-of-fashion-1794` | Gallery of Fashion de Heideloff | fashion | 1794 | N | | | europe | `ctx-periodical-press`: la prensa periódica incorpora láminas de moda coloreadas a mano que difunden modelos entre lectoras de otras ciudades; `ctx-reading-public`: un público lector femenino de clase media paga suscripciones para saber qué se lleva |
| `ackermann-fashion-plates-1809` | Láminas de moda de Ackermann's Repository | fashion | 1809 | N | | `lithography` | europe | `ctx-periodical-press`: la revista mensual lleva a sus suscriptores láminas de moda y muebles al día; `ctx-middle-class-consumption`: la clase media urbana consulta la revista para decidir compras de vestido y mobiliario |
| `marie-antoinette-gowns-1775` | Vestidos de corte de Rose Bertin para María Antonieta | fashion | 1775 | N | `rose-bertin` | | europe | `ctx-revolutionary-dress`: el lujo cortesano de las modistas de la reina contrasta con la sencillez que impondrá la Revolución |

### Conexiones

| from | to | línea |
|---|---|---|
| `ctx-neoclassical-antiquarianism` | `neoclassicism` | Pompeya y Herculano ofrecen un repertorio de formas antiguas que el gusto ilustrado convierte en estilo. |
| `neoclassicism` | `empire-regency` | El Imperio napoleónico endurece el vocabulario neoclásico y lo carga de símbolos de poder y de campaña. |
| `empire-regency` | `biedermeier` | El Biedermeier simplifica las líneas del estilo Imperio para la sala burguesa de después de 1815. |
| `th-pugin-true-principles` | `historicism` | Pugin sostiene que el gótico es la forma verdadera y cristiana, y da base moral al revival medieval. |
| `th-pugin-true-principles` | `macro-modernism` | Su exigencia de que la forma exprese la construcción anticipa el funcionalismo que defenderá el Modernismo. |
| `th-journal-of-design` | `inst-government-school-of-design` | La revista continúa el debate sobre calidad del diseño y manufactura que abrió la escuela de diseño. |
| `josiah-wedgwood` | `matthew-boulton` | Wedgwood y Boulton, socios de la Lunar Society, comparten el modelo de manufactura con diseño encargado. |
| `th-chippendale-director` | `th-hepplewhite-guide` | Los catálogos de muebles difunden modelos impresos a talleres de todo el país, en lugar del encargo directo. |
| `th-hepplewhite-guide` | `th-sheraton-drawing-book` | Sheraton continúa el género del libro de modelos, con dibujos de muebles neoclásicos más livianos. |
| `john-baskerville` | `giambattista-bodoni` | Bodoni admira a Baskerville y radicaliza el contraste y el espaciado de sus letras. |
| `punched-card-weaving` | `ctx-personal-computer` | La tarjeta perforada que programa el telar es antecedente de la programación por tarjetas de la informática. |
| `ctx-egyptomania` | `display-types` | La moda egipcia posterior a 1798 se asocia con los nombres y con el éxito de las letras gruesas de trazo uniforme. |
| `la-aurora-de-chile-1812` | `gaceta-de-buenos-aires-1810` | Ambos periódicos patriotas fijan por escrito la imagen pública de los gobiernos que desafían al poder colonial. |
| `ctx-industrial-revolution` | `macro-modernism` | La separación entre diseñar y fabricar, y la mala calidad de lo masivo, plantean los problemas que el Modernismo dice resolver. |
| `inst-thonet` | `macro-modernism` | La silla de madera curvada en serie muestra el diseño industrial que los modernistas defenderán un siglo después. |
| `inst-ackermann` | `heideloff-gallery-of-fashion-1794` | Las revistas con láminas de moda coloreadas amplían el modelo que Heideloff había abierto en Londres. |
| `inst-conservatoire-arts-metiers` | `jacquard-loom-1804` | El Conservatoire guardó el telar y otras máquinas como modelos para enseñar las artes mecánicas. |

### Reserva

| id | tipo | nombre | motivo |
|---|---|---|---|
| `ctx-metric-system` | contexts | Sistema métrico (1795) | estandarización de medidas; depende de poder enlazarlo con una obra |
| `ctx-factory-acts` | contexts | Leyes de fábricas y trabajo infantil | social; falta obra que lo cite con mecanismo claro |
| `ctx-us-patent-system` | contexts | Patentes en EE. UU. (1790) | económico; entra si se agrega obra estadounidense |
| `ctx-first-railway-timetables` | contexts | Horarios ferroviarios y hora estándar | verificar fechas |
| `continuous-paper-machine` | production | Máquina de papel continuo (c. 1803) | candidato a productivo adicional |
| `interchangeable-parts` | production | Piezas intercambiables | candidato a productivo; relaciona con Reforma |
| `th-wealth-of-nations` | theories | La riqueza de las naciones (1776) | teoría económica más que de diseño |
| `picturesque` | movements | Lo pintoresco | se solapa con historicismos |
| `inst-sevres` | institutions | Manufactura de Sèvres | falta enlace claro con el resto |
| `inst-bodoni-stamperia` | institutions | Stamperia Reale de Parma | se recoge en Bodoni |
| `george-hepplewhite` | designers | George Hepplewhite | sin obra propia segura |
| `william-caslon-iv` | designers | William Caslon IV | atribución de la Egyptian por confirmar |
| `ctx-telegraph` | contexts | Telégrafo eléctrico (1837) | etapa 5: ningún elemento de diseño del tramo tiene un mecanismo cierto con él |
| `ctx-photography` | contexts | Fotografía (1839) | etapa 5: sin elemento de diseño con mecanismo cierto antes de 1850; entra con Reforma o la etapa 6 |
| `cylinder-textile-printing` | production | Estampado textil con cilindros (1783) | etapa 5: sin obra, diseñador ni movimiento al que enlazar con certeza |
| `crystal-palace-1851` | works | Crystal Palace | probablemente va en Reforma |
| `tricolore-1794` | works | Bandera tricolor francesa | alternativa a símbolos patrios |
| `portland-vase-copy-1790` | works | Copia Wedgwood del jarrón Portland | segunda pieza de jasperware |
| `journal-des-dames-et-des-modes-1797` | works | Journal des Dames et des Modes (1797) | alternativa de moda |

## Tramo: reform

### Contextos

| id | nombre | sub | años | regiones | nivel | relaciona |
|---|---|---|---|---|---|---|
| `ctx-great-exhibition` | Gran Exposición de Londres | political | 1851 | europe | ★ | `inst-south-kensington`, `th-grammar-of-ornament` |
| `ctx-paris-1900` | Exposición Universal de París | political | 1900 | europe | N | `inst-liberty` |
| `ctx-national-unifications` | Unificaciones de Italia y Alemania | political | 1861–1871 | europe | N | `inst-werkbund`, `th-werkbund-debate` |
| `ctx-british-empire-trade` | Imperio y comercio colonial británico | political | 1850–1914 | europe, global | N | `inst-liberty`, `inst-south-kensington` |
| `ctx-catalan-renaixenca` | Renaixença catalana | political | 1860–1910 | europe | N | `art-nouveau` |
| `ctx-mexican-revolution` | Revolución mexicana | political | 1910 | latin-america | N | `jose-guadalupe-posada` |
| `ctx-second-industrial-revolution` | Segunda revolución industrial | economic | 1870–1914 | europe, north-america | ★ | `inst-aeg`, `iron-steel-frame` |
| `ctx-trademark-branding` | Marcas registradas y marca comercial | economic | 1875 | europe, north-america | ★ | `inst-liberty` |
| `ctx-department-stores` | Grandes almacenes | economic | 1852 | europe, north-america | N | `inst-liberty` |
| `ctx-mass-advertising-catalogue` | Publicidad y venta por catálogo | economic | 1870–1914 | europe, north-america | N | `chromolithography` |
| `ctx-nitrate-boom` | Auge del salitre | economic | 1880–1920 | latin-america | N | `ctx-latam-urbanisation` |
| `ctx-taylorism` | Taylorismo | economic | 1911 | north-america | N | `th-werkbund-debate` |
| `ctx-labour-movement` | Movimiento obrero y vivienda obrera | social | 1850–1914 | europe, north-america | ★ | `arts-and-crafts`, `inst-morris-and-co` |
| `ctx-bourgeois-home-hygiene` | Hogar burgués e higiene | social | 1850–1914 | europe, north-america | N | `arts-and-crafts` |
| `ctx-women-office-work` | Mujeres en las oficinas | social | 1870–1914 | europe, north-america | N | `typewriter` |
| `ctx-urban-leisure` | Ocio urbano: café, teatro y cabaré | social | 1860–1914 | europe, north-america | N | `illustrated-poster` |
| `ctx-dress-reform` | Reforma del vestido | social | 1851–1914 | europe, north-america | N | `aesthetic-movement` |
| `ctx-latam-urbanisation` | Crecimiento urbano e inmigración en América Latina | social | 1870–1914 | latin-america | N | `inst-zig-zag` |
| `ctx-japonisme` | Japonismo | cultural | 1860–1910 | global | ★ | `art-nouveau`, `aesthetic-movement` |
| `ctx-victorian-taste-crisis` | Crisis del gusto victoriano | cultural | 1851–1880 | europe | N | `inst-south-kensington`, `th-grammar-of-ornament` |
| `ctx-gothic-revival` | Neogótico y medievalismo romántico | cultural | 1840–1900 | europe | N | `th-nature-of-gothic` |
| `ctx-natural-forms-science` | Botánica, Darwin y formas de la naturaleza | cultural | 1860–1910 | europe | N | `art-nouveau` |
| `ctx-poster-craze` | Fiebre del cartel | cultural | 1880–1900 | europe | N | `chromolithography` |
| `ctx-vienna-1900` | Viena 1900 | cultural | 1897–1914 | europe | N | `vienna-secession`, `th-loos-ornament-and-crime` |
| `ctx-classical-archaeology` | Arqueología clásica y nostalgia de Grecia | cultural | 1870–1914 | europe | N | `ctx-dress-reform` |
| `ctx-electricity` | Electricidad y luz eléctrica | technological | 1879 | europe, north-america | ★ |  |
| `ctx-automobile` | Automóvil | technological | 1886 | europe, north-america | N |  |
| `ctx-safety-bicycle` | Bicicleta de seguridad | technological | 1885 | europe, north-america | N | `ctx-dress-reform` |
| `ctx-snapshot-photography` | Fotografía popular | technological | 1888 | europe, north-america | N | `celluloid`, `halftone-photoengraving` |
| `ctx-railways-steamships` | Ferrocarril y vapor | technological | 1840–1910 | europe, north-america, latin-america | N | `ctx-mass-advertising-catalogue` |

### Productivo

| id | nombre | sub | años | nivel | relaciona |
|---|---|---|---|---|---|
| `bentwood` | Madera curvada al vapor | processes | 1856 | N | `inst-thonet` |
| `chromolithography` | Cromolitografía | processes | 1837–1900 | N | `ctx-poster-craze` |
| `hot-metal-typesetting` | Linotipia y monotipia | processes | 1886 | N | `ctx-illustrated-press` |
| `halftone-photoengraving` | Fotograbado de medio tono | processes | 1880 | N | `ctx-illustrated-press` |
| `sewing-machine` | Máquina de coser | tools | 1851 | N | `ctx-dress-reform` |
| `typewriter` | Máquina de escribir | tools | 1874 | N | `ctx-women-office-work` |
| `paper-patterns` | Patrones de papel | tools | 1863 | N | `sewing-machine` |
| `celluloid` | Celuloide | materials | 1870 | N | `ctx-snapshot-photography` |
| `art-glass` | Vidrio artístico | materials | 1890–1914 | N | `ctx-natural-forms-science` |
| `reinforced-concrete` | Hormigón armado | materials | 1890–1914 | N | `ctx-second-industrial-revolution` |
| `iron-steel-frame` | Estructura de hierro y acero | materials | 1851–1914 | N | `ctx-railways-steamships` |

### Teoría

| id | nombre | años | nivel | relaciona |
|---|---|---|---|---|
| `th-grammar-of-ornament` | The Grammar of Ornament (Owen Jones) | 1856 | ★ | `christopher-dresser`, `ctx-victorian-taste-crisis` |
| `th-nature-of-gothic` | La naturaleza de lo gótico (Ruskin) | 1853 | ★ | `william-morris`, `arts-and-crafts` |
| `th-dresser-principles` | Principles of Decorative Design (Dresser) | 1873 | N | `christopher-dresser`, `aesthetic-movement` |
| `th-sullivan-function` | «La forma sigue a la función» (Sullivan) | 1896 | ★ | `louis-sullivan`, `macro-modernism` |
| `th-loos-ornament-and-crime` | Ornamento y delito (Loos) | 1910 | ★ | `adolf-loos`, `macro-modernism` |
| `th-werkbund-debate` | Debate Muthesius–Van de Velde en el Werkbund | 1914 | ★ | `inst-werkbund`, `henry-van-de-velde`, `peter-behrens` |

### Movimientos

| id | nombre | años | nivel | relaciona |
|---|---|---|---|---|
| `macro-modernism` | Modernismo | 1907–1970 | ★ | `inst-werkbund`, `peter-behrens` |
| `arts-and-crafts` | Arts and Crafts | 1861–1914 | ★ | `inst-morris-and-co`, `william-morris`, `philip-webb`, `frank-lloyd-wright` |
| `aesthetic-movement` | Esteticismo | 1860–1900 | N | `ctx-japonisme`, `inst-liberty` |
| `art-nouveau` | Art nouveau, Jugendstil y modernisme | 1890–1914 | ★ | `ctx-natural-forms-science`, `ctx-paris-1900` |
| `vienna-secession` | Secesión de Viena | 1897–1914 | ★ | `inst-wiener-werkstatte`, `ctx-vienna-1900` |
| `illustrated-poster` | Cartel ilustrado | 1880–1914 | ★ | `ctx-poster-craze`, `chromolithography` |

### Instituciones

| id | nombre | años | nivel | relaciona |
|---|---|---|---|---|
| `inst-south-kensington` | South Kensington Museum (hoy V&A) | 1852 | ★ | `ctx-great-exhibition` |
| `inst-morris-and-co` | Morris & Co. | 1861 | ★ | `arts-and-crafts`, `strawberry-thief` |
| `inst-liberty` | Liberty & Co. | 1875 | N | `ctx-japonisme` |
| `inst-kelmscott-press` | Kelmscott Press | 1891 | ★ | `kelmscott-chaucer`, `hot-metal-typesetting` |
| `inst-wiener-werkstatte` | Wiener Werkstätte | 1903 | ★ | `vienna-secession`, `josef-hoffmann` |
| `inst-werkbund` | Deutscher Werkbund | 1907 | ★ | `macro-modernism`, `inst-bauhaus` |
| `inst-aeg` | AEG | 1883 | ★ | `peter-behrens`, `ctx-electricity` |
| `inst-ford-motor` | Ford Motor Company | 1903 | N | `ford-model-t`, `ctx-taylorism` |
| `inst-glasgow-school-of-art` | Glasgow School of Art | 1845 | N | `charles-rennie-mackintosh` |

### Diseñadores

| id | nombre | años | disciplinas | nivel | obras | relaciona |
|---|---|---|---|---|---|---|
| `william-morris` | William Morris | 1834–1896 | graphic, product, fashion | ★ | `strawberry-thief`, `kelmscott-chaucer`, `morris-chair` | `arts-and-crafts`, `inst-morris-and-co`, `inst-kelmscott-press` |
| `philip-webb` | Philip Webb | 1831–1915 | architecture, product | ★ | `red-house`, `morris-chair` | `arts-and-crafts`, `inst-morris-and-co` |
| `christopher-dresser` | Christopher Dresser | 1834–1904 | product | N | `dresser-teapot` | `aesthetic-movement`, `inst-south-kensington` |
| `charles-rennie-mackintosh` | Charles Rennie Mackintosh | 1868–1928 | architecture, product | ★ | `hill-house-chair`, `glasgow-school-of-art`, `willow-tea-rooms` | `art-nouveau`, `inst-glasgow-school-of-art` |
| `margaret-macdonald` | Margaret Macdonald | 1864–1933 | product, graphic | N | `willow-tea-rooms` | `art-nouveau` |
| `josef-hoffmann` | Josef Hoffmann | 1870–1956 | architecture, product | ★ | `palais-stoclet`, `purkersdorf-sanatorium`, `sitzmaschine`, `ww-metalwork` | `vienna-secession`, `inst-wiener-werkstatte`, `inst-werkbund` |
| `koloman-moser` | Koloman Moser | 1868–1918 | graphic, product | N | `ver-sacrum`, `ww-metalwork` | `vienna-secession`, `inst-wiener-werkstatte` |
| `joseph-maria-olbrich` | Joseph Maria Olbrich | 1867–1908 | architecture, graphic | N | `secession-building`, `ver-sacrum` | `vienna-secession` |
| `henry-van-de-velde` | Henry van de Velde | 1863–1957 | architecture, product | N | `bloemenwerf`, `werkbund-cologne-1914` | `art-nouveau`, `inst-werkbund` |
| `victor-horta` | Victor Horta | 1861–1947 | architecture | ★ | `hotel-tassel` | `art-nouveau` |
| `hector-guimard` | Hector Guimard | 1867–1942 | architecture | ★ | `paris-metro-entrances`, `castel-beranger` | `art-nouveau` |
| `antoni-gaudi` | Antoni Gaudí | 1852–1926 | architecture | ★ | `casa-batllo` | `art-nouveau` |
| `louis-comfort-tiffany` | Louis Comfort Tiffany | 1848–1933 | product | N | `tiffany-lamps` | `art-nouveau` |
| `emile-galle` | Émile Gallé | 1846–1904 | product | N | `galle-vases` | `art-nouveau` |
| `rene-lalique` | René Lalique | 1860–1945 | product | N | `lalique-jewellery` | `art-nouveau` |
| `jules-cheret` | Jules Chéret | 1836–1932 | graphic | ★ | `cheret-posters` | `illustrated-poster` |
| `toulouse-lautrec` | Henri de Toulouse-Lautrec | 1864–1901 | graphic | N | `moulin-rouge-la-goulue` | `illustrated-poster` |
| `alfons-mucha` | Alfons Mucha | 1860–1939 | graphic | ★ | `mucha-gismonda` | `illustrated-poster`, `art-nouveau` |
| `aubrey-beardsley` | Aubrey Beardsley | 1872–1898 | graphic | N | `beardsley-salome` | `aesthetic-movement` |
| `peter-behrens` | Peter Behrens | 1868–1940 | architecture, product, graphic | ★ | `aeg-turbine-hall`, `aeg-kettle`, `aeg-arc-lamp`, `behrens-aeg-logo` | `inst-aeg`, `inst-werkbund`, `macro-modernism` |
| `charles-frederick-worth` | Charles Frederick Worth | 1825–1895 | fashion | N | `worth-haute-couture` | `ctx-trademark-branding` |
| `paul-poiret` | Paul Poiret | 1879–1944 | fashion | N | `poiret-high-waist` | `ctx-dress-reform` |
| `mariano-fortuny` | Mariano Fortuny | 1871–1949 | fashion | ★ | `fortuny-delphos` | `ctx-classical-archaeology` |
| `frank-lloyd-wright` | Frank Lloyd Wright | 1867–1959 | architecture | ★ | `robie-house`, `larkin-building` | `arts-and-crafts` |
| `louis-sullivan` | Louis Sullivan | 1856–1924 | architecture | N | `carson-pirie-scott` | `ctx-department-stores` |
| `adolf-loos` | Adolf Loos | 1870–1933 | architecture | N | `looshaus` | `macro-modernism`, `vienna-secession` |
| `joseph-paxton` | Joseph Paxton | 1803–1865 | architecture | ★ | `crystal-palace` | `ctx-great-exhibition` |
| `jose-guadalupe-posada` | José Guadalupe Posada | 1852–1913 | graphic | ★ | `posada-catrina` | `ctx-mexican-revolution` |

### Obras

| id | título | disciplina | año | nivel | diseñadores | tech | regiones | contextos |
|---|---|---|---|---|---|---|---|---|
| `crystal-palace` | Crystal Palace | architecture | 1851 | ★ | `joseph-paxton` | `iron-steel-frame` | europe | `ctx-great-exhibition`: la Exposición de 1851 exigía un recinto enorme, rápido de montar y desmontable; Paxton lo resolvió con piezas de hierro y vidrio prefabricadas; `ctx-railways-steamships`: la técnica de ingeniería ferroviaria y los trenes de excursión hicieron posible construirlo y llenarlo de visitantes |
| `red-house` | Red House | architecture | 1859 | ★ | `philip-webb` | | europe | `ctx-gothic-revival`: Webb y Morris buscaron una casa de ladrillo sin historicismo de catálogo, inspirada en lo medieval y lo vernáculo; `ctx-bourgeois-home-hygiene`: Morris encargó la casa y su mobiliario como hogar completo, en reacción a los interiores recargados del comercio victoriano |
| `hotel-tassel` | Hôtel Tassel | architecture | 1893 | ★ | `victor-horta` | `iron-steel-frame` | europe | `ctx-natural-forms-science`: el hierro de columnas y barandas se curva como tallos vegetales, siguiendo el gusto por las formas naturales; `ctx-second-industrial-revolution`: el hierro industrial barato permitió dejar la estructura a la vista dentro de una casa burguesa |
| `paris-metro-entrances` | Entradas del metro de París | architecture | 1900 | ★ | `hector-guimard` | `iron-steel-frame` | europe | `ctx-paris-1900`: el metro se inauguró para la Exposición de 1900 y sus accesos llevaron el art nouveau a la calle; `ctx-electricity`: la tracción eléctrica hizo posible el metro subterráneo y sus lámparas incorporadas en las entradas |
| `casa-batllo` | Casa Batlló | architecture | 1906 | ★ | `antoni-gaudi` | | europe | `ctx-catalan-renaixenca`: la burguesía catalana en auge encargó casas que afirmaran una cultura propia en Barcelona; `ctx-natural-forms-science`: Gaudí tomó de la naturaleza la estructura de huesos, escamas y tallos para fachada e interior |
| `aeg-turbine-hall` | Fábrica de turbinas de AEG | architecture | 1909 | ★ | `peter-behrens` | `iron-steel-frame` | europe | `ctx-second-industrial-revolution`: la gran industria eléctrica alemana quiso una arquitectura que la representara como empresa moderna; `ctx-electricity`: AEG fabricaba turbinas para el sistema eléctrico y su sede se leyó como templo de esa técnica |
| `robie-house` | Casa Robie | architecture | 1909 | ★ | `frank-lloyd-wright` | | north-america | `ctx-japonisme`: Wright conoció la arquitectura y los grabados japoneses en Chicago (pabellón Ho-o-den, 1893) y de ahí vienen aleros largos y planta abierta; `ctx-electricity`: luminarias integradas a la construcción y vitrales como difusores de luz eléctrica |
| `palais-stoclet` | Palacio Stoclet | architecture | 1911 | ★ | `josef-hoffmann` | | europe | `ctx-vienna-1900`: obra cumbre del círculo vienés de la Secesión, con revestimiento de mármol y mosaico de Klimt; `ctx-bourgeois-home-hygiene`: un mecenas de la alta burguesía pagó una casa total con muebles, textiles y vajilla de los Wiener Werkstätte |
| `secession-building` | Edificio de la Secesión | architecture | 1898 | N | `joseph-maria-olbrich` | | europe | `ctx-vienna-1900`: los artistas que rompieron con la academia necesitaban una sala propia de exposiciones y la cúpula de laurel dorado se volvió su emblema |
| `purkersdorf-sanatorium` | Sanatorio de Purkersdorf | architecture | 1904 | N | `josef-hoffmann` | `reinforced-concrete` | europe | `ctx-bourgeois-home-hygiene`: la cura de reposo y la higiene pedían superficies blancas, lisas y lavables, que Hoffmann convirtió en un lenguaje geométrico |
| `fagus-factory` | Fábrica Fagus | architecture | 1911 | N | `gropius` | `iron-steel-frame` | europe | `ctx-second-industrial-revolution`: una fábrica de hormas de calzado pidió una imagen racional y luminosa, con muros de vidrio que dejaban ver la estructura |
| `larkin-building` | Edificio Larkin | architecture | 1904 | N | `frank-lloyd-wright` | | north-america | `ctx-women-office-work`: la empresa de venta por correo empleaba a cientos de oficinistas, en su mayoría mujeres, y Wright organizó el trabajo en un gran patio central |
| `carson-pirie-scott` | Almacén Carson Pirie Scott | architecture | 1904 | N | `louis-sullivan` | `iron-steel-frame` | north-america | `ctx-department-stores`: el gran almacén necesitaba pisos de venta abiertos y mucha luz, resueltos con estructura de acero y ventanas anchas de Chicago |
| `glasgow-school-of-art` | Escuela de Arte de Glasgow | architecture | 1909 | N | `charles-rennie-mackintosh` | | europe | `ctx-japonisme`: Mackintosh combina la geometría de entramados y celosías de inspiración japonesa con la tradición escocesa |
| `willow-tea-rooms` | Willow Tea Rooms | architecture | 1903 | N | `charles-rennie-mackintosh`, `margaret-macdonald` | | europe | `ctx-urban-leisure`: los salones de té de Miss Cranston eran espacios públicos para mujeres, diseñados como interior completo con Macdonald y Mackintosh |
| `ascensor-concepcion` | Ascensor Concepción de Valparaíso | architecture | 1883 | N | | `iron-steel-frame` | latin-america | `ctx-nitrate-boom`: el comercio del salitre y de los puertos del Pacífico llenó de capital y de gente los cerros de Valparaíso; `ctx-latam-urbanisation`: los ascensores resolvieron el acceso a los cerros de una ciudad que crecía con la inmigración |
| `werkbund-cologne-1914` | Exposición del Werkbund en Colonia | architecture | 1914 | N | `henry-van-de-velde`, `gropius` | `iron-steel-frame` | europe | `ctx-national-unifications`: el Werkbund quiso mostrar un diseño industrial alemán unificado y competitivo frente a Gran Bretaña y Francia |
| `bloemenwerf` | Casa Bloemenwerf | architecture | 1895 | N | `henry-van-de-velde` | | europe | `ctx-dress-reform`: Van de Velde diseñó la casa, el mobiliario y hasta el vestido reformado de su esposa como un hogar total libre del corsé y del historicismo |
| `castel-beranger` | Castel Béranger | architecture | 1898 | N | `hector-guimard` | | europe | `ctx-natural-forms-science`: fachada y rejas con motivos vegetales y asimétricos que aplican la ornamentación orgánica a un edificio de renta |
| `looshaus` | Looshaus | architecture | 1911 | N | `adolf-loos` | | europe | `ctx-vienna-1900`: frente a la Hofburg, la fachada lisa sobre un zócalo de mármol provocó un escándalo en la Viena de la Secesión |
| `highland-park-plant` | Planta de Highland Park | architecture | 1910 | N | | `reinforced-concrete` | north-america | `ctx-taylorism`: Ford organizó la planta por flujos de trabajo estudiados y cadena de montaje; `ctx-automobile`: producir un automóvil económico en masa exigió una fábrica construida para ese solo fin |
| `thonet-chair-14` | Silla n.º 14 de Thonet | product | 1859 | ★ | `michael-thonet` | `bentwood` | europe | `ctx-great-exhibition`: Thonet mostró madera curvada en Londres 1851 y ganó una medalla, base de su expansión comercial; `ctx-urban-leisure`: los cafés y salones de la burguesía urbana compraron millones de sillas livianas y apilables |
| `singer-sewing-machine` | Máquina de coser Singer | product | 1851 | ★ | | `sewing-machine` | north-america | `ctx-second-industrial-revolution`: la fabricación mecanizada, la red de agentes y la venta a plazos difundieron la máquina por el mundo; `ctx-bourgeois-home-hygiene`: la costura salió del taller y entró al hogar como aparato doméstico |
| `hill-house-chair` | Silla de Hill House | product | 1902 | ★ | `charles-rennie-mackintosh` | | europe | `ctx-japonisme`: respaldo alto y rectilíneo de inspiración japonesa, tratado como forma escultórica; `ctx-bourgeois-home-hygiene`: encargada por un editor próspero para su casa, como parte de un interior total |
| `sitzmaschine` | Sitzmaschine | product | 1905 | N | `josef-hoffmann` | `bentwood` | europe | `ctx-vienna-1900`: un sillón reclinable de líneas geométricas concebido para el sanatorio, símbolo del racionalismo de los Wiener Werkstätte |
| `aeg-kettle` | Hervidor eléctrico de AEG | product | 1909 | N | `peter-behrens` | | europe | `ctx-electricity`: la electrificación de las casas abrió un mercado de aparatos domésticos que AEG quiso dotar de formas propias, no de ornamentos heredados |
| `aeg-arc-lamp` | Lámpara de arco de AEG | product | 1907 | N | `peter-behrens` | | europe | `ctx-electricity`: la luz eléctrica pública pedía un objeto sin tradición, que Behrens resolvió con una forma industrial coherente |
| `ford-model-t` | Ford modelo T | product | 1908 | ★ | | | north-america | `ctx-taylorism`: el estudio de tiempos y la división del trabajo bajaron el costo de fabricar, sobre todo desde la cadena de montaje de 1913; `ctx-automobile`: un automóvil simple y barato convirtió el invento en producto de masas |
| `safety-bicycle` | Bicicleta de seguridad Rover | product | 1885 | N | | | europe | `ctx-safety-bicycle`: la cadena y las ruedas iguales hicieron un vehículo estable y barato que se popularizó en pocos años |
| `benz-motorwagen` | Benz Patent-Motorwagen | product | 1886 | N | | | europe | `ctx-automobile`: primer automóvil con motor de combustión y patente propia, origen de la industria que más transformaría el diseño de producto |
| `tiffany-lamps` | Lámparas de Tiffany | product | 1900 | N | `louis-comfort-tiffany` | `art-glass` | north-america | `ctx-electricity`: la luz eléctrica en el hogar creó un nuevo objeto, la lámpara de mesa, que Tiffany ofreció con pantallas de vidrio de colores |
| `galle-vases` | Vasos de Gallé | product | 1900 | N | `emile-galle` | `art-glass` | europe | `ctx-natural-forms-science`: Gallé, botánico aficionado, trabajó el vidrio con flores y plantas observadas del natural, mezclando esmaltes y capas |
| `lalique-jewellery` | Joyas de Lalique | product | 1900 | N | `rene-lalique` | | europe | `ctx-paris-1900`: sus joyas con libélulas y mujeres-insecto consagraron a Lalique en la Exposición de 1900 |
| `dresser-teapot` | Tetera de Dresser | product | 1879 | N | `christopher-dresser` | | europe | `ctx-japonisme`: tras su viaje a Japón en 1876–77, Dresser aplicó formas geométricas y asimétricas de objetos japoneses a metalistería industrial; `ctx-british-empire-trade`: el comercio con Oriente trajo modelos y compradores al mercado británico |
| `kodak-no1` | Cámara Kodak n.º 1 | product | 1888 | N | | `celluloid` | north-america | `ctx-snapshot-photography`: cámara de caja prerrellenada con rollo y servicio de revelado, que sacó la fotografía de manos profesionales; `ctx-mass-advertising-catalogue`: «usted aprieta el botón, nosotros hacemos el resto» fue un lema publicitario de masas |
| `remington-no1` | Máquina de escribir Remington n.º 1 | product | 1874 | N | | `typewriter` | north-america | `ctx-women-office-work`: la máquina creó el oficio de mecanógrafa, ocupado por mujeres en las nuevas oficinas |
| `morris-chair` | Sillón Morris | product | 1866 | N | `william-morris`, `philip-webb` | | europe | `ctx-bourgeois-home-hygiene`: un sillón reclinable de respaldo ajustable para un hogar burgués que buscaba comodidad sin pompa |
| `ww-metalwork` | Metalistería de los Wiener Werkstätte | product | 1905 | N | `josef-hoffmann`, `koloman-moser` | | europe | `ctx-vienna-1900`: cestas y bandejas de metal perforado con retícula cuadrada, taller de oficio para el gusto de la burguesía vienesa |
| `strawberry-thief` | Strawberry Thief | fashion | 1883 | ★ | `william-morris` | | europe | `ctx-victorian-taste-crisis`: Morris rechazó el patrón de flores pesadas y realismo tridimensional del gusto victoriano; `ctx-labour-movement`: su textil estampado a mano con índigo expresaba su rechazo a la fábrica y su socialismo de 1883 |
| `fortuny-delphos` | Vestido Delphos | fashion | 1907 | ★ | `mariano-fortuny` | | europe | `ctx-classical-archaeology`: el nombre y los pliegues citan la estatua del Auriga de Delfos, hallada en las excavaciones francesas; `ctx-dress-reform`: túnica plisada sin corsé, afín a la reforma del vestido |
| `worth-haute-couture` | Alta costura de Worth | fashion | 1858 | N | `charles-frederick-worth` | | europe | `ctx-trademark-branding`: Worth cosió su etiqueta y presentó colecciones propias, a la manera de una marca registrada |
| `poiret-high-waist` | Línea de talle alto de Poiret | fashion | 1908 | N | `paul-poiret` | | europe | `ctx-dress-reform`: la crítica al corsé y la salud abrieron camino a vestidos de talle alto y caída recta |
| `bloomer-costume` | Traje Bloomer | fashion | 1851 | N | | | north-america | `ctx-dress-reform`: pantalones bajo una falda corta que defendían la libertad de movimiento de las mujeres |
| `butterick-patterns` | Patrones de papel Butterick | fashion | 1863 | N | | `paper-patterns`, `sewing-machine` | north-america | `ctx-mass-advertising-catalogue`: los patrones se vendían por agentes, tiendas y revistas, lo que difundió la moda por correo |
| `levis-riveted-jeans` | Pantalón con remaches de Levi Strauss | fashion | 1873 | N | | | north-america | `ctx-second-industrial-revolution`: confección industrial de ropa de trabajo reforzada con remaches metálicos para uso de mineros y obreros |
| `liberty-artistic-dress` | Vestido artístico de Liberty | fashion | 1884 | N | | | europe | `ctx-british-empire-trade`: Liberty importaba telas y estampados de India y Japón y los transformó en vestidos de moda para el gusto estético; `ctx-japonisme`: el kimono y los tejidos japoneses inspiraron sus siluetas sueltas |
| `bass-triangle` | Triángulo rojo de Bass | graphic | 1876 | N | | `chromolithography` | europe | `ctx-trademark-branding`: la ley británica de marcas de 1875 permitió que Bass registrara su triángulo rojo como primera marca registrada |
| `coca-cola-logo` | Logotipo de Coca-Cola | graphic | 1887 | N | | | north-america | `ctx-trademark-branding`: una marca de tipografía caligráfica reconocible reemplazó al nombre genérico del tónico en botellas y avisos |
| `kelmscott-chaucer` | Kelmscott Chaucer | graphic | 1896 | ★ | `william-morris` | | europe | `ctx-gothic-revival`: página con letras góticas, orlas y capitulares inspiradas en incunables medievales; `ctx-labour-movement`: libro hecho a mano como respuesta a la mala impresión industrial que Morris criticaba |
| `cheret-posters` | Carteles de Chéret | graphic | 1890 | ★ | `jules-cheret` | `chromolithography` | europe | `ctx-poster-craze`: la ley de 1881 sobre libertad de prensa y carteles llenó París de afiches y de coleccionistas; `ctx-mass-advertising-catalogue`: la cromolitografía a gran formato permitió anuncios en color para teatros y productos |
| `moulin-rouge-la-goulue` | Moulin Rouge: La Goulue | graphic | 1891 | N | `toulouse-lautrec` | `chromolithography` | europe | `ctx-urban-leisure`: el cabaré de Montmartre era un negocio de ocio masivo que necesitaba un cartel que atrajera clientes |
| `mucha-gismonda` | Cartel Gismonda | graphic | 1894 | ★ | `alfons-mucha` | `chromolithography` | europe | `ctx-poster-craze`: Sarah Bernhardt lo encargó y el cartel fue buscado por coleccionistas; `ctx-paris-1900`: Mucha decoró el pabellón de Bosnia-Herzegovina de la Exposición Universal de París |
| `beardsley-salome` | Ilustraciones de Salomé de Beardsley | graphic | 1894 | N | `aubrey-beardsley` | `halftone-photoengraving` | europe | `ctx-japonisme`: sus dibujos en blanco y negro de contornos y vacíos toman de los grabados japoneses la línea plana y la asimetría |
| `ver-sacrum` | Revista Ver Sacrum | graphic | 1898 | N | `koloman-moser`, `joseph-maria-olbrich` | | europe | `ctx-vienna-1900`: órgano de la Secesión, con diseño de página y tipografía de los propios artistas del grupo |
| `behrens-aeg-logo` | Logotipo e identidad de AEG | graphic | 1908 | N | `peter-behrens` | | europe | `ctx-trademark-branding`: marca, folletos y catálogos rediseñados con una sola línea visual por la empresa; `ctx-electricity`: una empresa eléctrica quiso comunicar modernidad |
| `michelin-bibendum` | Bibendum de Michelin | graphic | 1898 | N | | | europe | `ctx-automobile`: la marca de neumáticos creó una mascota para un mercado nuevo de automovilistas; `ctx-poster-craze`: nace en un cartel de O'Galop con el estilo de la fiebre del cartel |
| `lira-popular` | Pliegos de la Lira Popular | graphic | 1890 | N | | | latin-america | `ctx-latam-urbanisation`: pliegos de versos con grabados, vendidos en las calles de Santiago a un público urbano y recién alfabetizado; `ctx-nitrate-boom`: los poetas populares relataron la vida de la pampa salitrera y sus crímenes |
| `zig-zag-magazine` | Revista Zig-Zag | graphic | 1905 | N | | `halftone-photoengraving`, `hot-metal-typesetting` | latin-america | `ctx-latam-urbanisation`: semanario ilustrado de masas para el público de las ciudades chilenas, impreso con fotograbado y composición mecánica |
| `posada-catrina` | La Calavera Catrina | graphic | 1910 | ★ | `jose-guadalupe-posada` | | latin-america | `ctx-mexican-revolution`: Posada satirizó a la élite del porfiriato poco antes de su caída; `ctx-latam-urbanisation`: sus grabados se vendían como hojas sueltas a un público popular urbano de Ciudad de México |
| `montgomery-ward-catalogue` | Catálogo de Montgomery Ward | graphic | 1872 | N | | | north-america | `ctx-mass-advertising-catalogue`: la venta por correo con catálogo ilustrado llegó a las zonas rurales; `ctx-railways-steamships`: el ferrocarril permitió que los pedidos llegaran a todo el país |

### Conexiones

| from | to | línea |
|---|---|---|
| `th-nature-of-gothic` | `william-morris` | Ruskin elogia al artesano libre que talla a su manera y Morris convierte esa idea en crítica de la división industrial del trabajo. |
| `inst-south-kensington` | `christopher-dresser` | El Departamento de Ciencia y Arte de South Kensington enseñó ornamento y botánica a Dresser, que los llevó a su diseño industrial. |
| `ctx-japonisme` | `art-nouveau` | Los grabados japoneses ofrecieron línea plana, asimetría y recorte, que el art nouveau tomó para carteles y objetos. |
| `jules-cheret` | `toulouse-lautrec` | Chéret mostró que la litografía en color podía hacer carteles de calle, y Lautrec adoptó el formato con una línea más sintética. |
| `jules-cheret` | `alfons-mucha` | El cartel parisino de Chéret abrió el mercado donde Mucha triunfó con Sarah Bernhardt, con una figura decorativa. |
| `arts-and-crafts` | `vienna-secession` | La exposición de la Secesión de 1900 mostró obra de Mackintosh y de talleres ingleses, y Hoffmann y Moser adoptaron su idea de oficio. |
| `charles-rennie-mackintosh` | `josef-hoffmann` | La geometría de la Escuela de Glasgow, con retícula y cuadrado, influyó en el estilo más rectilíneo de Hoffmann y de los Wiener Werkstätte. |
| `peter-behrens` | `gropius` | Gropius trabajó en el taller de Behrens, donde conoció la arquitectura industrial y el diseño para una empresa. |
| `peter-behrens` | `le-corbusier` | Le Corbusier trabajó unos meses con Behrens en Berlín y retomó su idea de arquitectura para la industria. |
| `peter-behrens` | `mies-van-der-rohe` | Mies trabajó con Behrens, de quien tomó el rigor de proporción y la sobriedad en el detalle. |
| `inst-werkbund` | `inst-bauhaus` | El Werkbund unió arte, industria y comercio, un programa que Gropius, miembro del grupo, llevó a la Bauhaus de 1919. |
| `louis-sullivan` | `frank-lloyd-wright` | Wright trabajó con Sullivan en Chicago y heredó su idea de forma derivada del uso y de la naturaleza. |
| `th-loos-ornament-and-crime` | `le-corbusier` | Le Corbusier publicó textos de Loos en L'Esprit Nouveau y retomó la crítica del ornamento como base de la arquitectura moderna. |
| `jose-guadalupe-posada` | `inst-tgp` | Los grabadores del Taller de Gráfica Popular reconocieron a Posada como precedente de un grabado político hecho para el pueblo. |
| `frank-lloyd-wright` | `ctx-japonisme` | La arquitectura japonesa vista en Chicago en 1893 influyó en la casa de planta abierta y alero largo de Wright. |
| `william-morris` | `inst-wiener-werkstatte` | Los talleres de Morris y de la Guild of Handicraft fueron el modelo de taller de artistas que inspiró a los Wiener Werkstätte. |
| `lira-popular` | `inst-zig-zag` | La Lira Popular y Zig-Zag muestran dos caras de la prensa popular chilena entre el pliego de calle y el semanario ilustrado. |
| `ctx-taylorism` | `ford-model-t` | El estudio científico del trabajo se aplicó a la producción del Ford T, cuyo costo cayó con la cadena de montaje. |

### Reserva

| id | tipo | nombre | motivo |
|---|---|---|---|
| `ctx-columbian-exposition-1893` | contexto | Exposición Colombina de Chicago 1893 | difunde pabellón Ho-o-den y Ciudad Blanca; Wright y Sullivan |
| `ctx-ringstrasse` | contexto | Ringstrasse de Viena | marco urbano de Hoffmann, Loos y Wagner |
| `ctx-cinema-1895` | contexto | Cine (1895) | primeros cines, afiches; ya existe `ctx-cinema` en Modernismo |
| `ctx-assembly-line-1913` | contexto | Cadena de montaje de Ford (1913) | se funde hoy en `ctx-taylorism` |
| `ctx-celtic-revival` | contexto | Renacimiento celta | Glasgow y Mackintosh |
| `electroplating` | productivo | Galvanoplastia | metalistería de Dresser y Elkington |
| `cast-iron-prefabrication` | productivo | Prefabricación en hierro fundido | Crystal Palace y mercados |
| `th-semper-der-stil` | teoría | Der Stil (Semper) | influyó en Behrens y en la teoría del revestimiento |
| `glasgow-style` | movimiento | Escuela de Glasgow | se trata dentro de `art-nouveau` |
| `prairie-school` | movimiento | Escuela de la pradera | se trata junto a Wright |
| `inst-tiffany-studios` | institución | Tiffany Studios | taller del vidrio Favrile |
| `inst-coca-cola-company` | institución | The Coca-Cola Company | marca |
| `otto-wagner` | diseñador | Otto Wagner | Postsparkasse y estaciones de Viena |
| `walter-crane` | diseñador | Walter Crane | ilustración Arts and Crafts |
| `eugene-grasset` | diseñador | Eugène Grasset | cartel y tipografía art nouveau |
| `gustave-eiffel` | diseñador | Gustave Eiffel | Torre Eiffel 1889 |
| `hermann-muthesius` | diseñador | Hermann Muthesius | protagonista del debate del Werkbund; falta obra clara |
| `eiffel-tower` | obra | Torre Eiffel | 1889, obra de la Exposición Universal |
| `casa-vicens` | obra | Casa Vicens | primera casa de Gaudí |
| `postsparkasse` | obra | Caja Postal de Ahorros de Viena | 1904, Otto Wagner |
| `unity-temple` | obra | Unity Temple | 1908, Wright, hormigón |
| `sears-catalogue` | obra | Catálogo de Sears | venta por correo, 1890s |
| `sussex-chair` | obra | Silla Sussex de Morris & Co. | variante |
| `ctx-telephone` | contexto | Teléfono | v36: sin obra ni elemento de Reforma al que enlazarlo con mecanismo cierto |
| `aluminium` | productivo | Aluminio | v36: ninguna obra de Reforma lo usa ni hay elemento al que enlazarlo con certeza |

## Tramo: postwar

Posguerra (1945–1974). Ids de otros tramos usados como referencia: `macro-modernism`, `ctx-war-economy`, `ctx-second-world-war`, `ctx-fashion-magazines`, `ctx-mexican-muralism`, `ctx-planned-obsolescence`, `ctx-womens-vote-work`, `moulded-plywood`, `steel-body-pressing`, `inst-olivetti`, `dreyfuss`, `le-corbusier`, `mies-van-der-rohe`, `gropius`, `oscar-niemeyer`, `lucio-costa`, `juan-ogorman`, `buckminster-fuller`, `coco-chanel`; y de la reserva de Modernismo (solo referencias, no filas de este tramo): `ctx-corfo`, `ctx-early-television`.

### Contextos

| id | nombre | sub | años | regiones | nivel | relaciona |
|---|---|---|---|---|---|---|
| `ctx-cold-war` | Guerra Fría y diseño como modo de vida | political | 1947–1989 | europe, north-america, latin-america | ★ | `ctx-marshall-plan` |
| `ctx-marshall-plan` | Plan Marshall | political | 1948–1952 | europe | N | `ctx-german-italian-miracle` |
| `ctx-german-reconstruction` | Reconstrucción y reeducación en Alemania | political | 1945–1960 | europe | N | `inst-hfg-ulm`, `inst-braun` |
| `ctx-unidad-popular-golpe` | Unidad Popular y golpe de Estado, 1970–1973 | political | 1970–1973 | latin-america | N | `ctx-corfo`, `inst-intec` |
| `ctx-cuban-revolution` | Revolución Cubana | political | 1959–1975 | latin-america | N | `ctx-cold-war` |
| `ctx-may-68` | Mayo del 68 | political | 1968 | europe | ★ | `ctx-youth-counterculture`, `radical-design` |
| `ctx-brazil-developmentalism` | Desarrollismo de Kubitschek y «cincuenta años en cinco» | political | 1956–1961 | latin-america | N | `ctx-isi-cepal`, `inst-esdi` |
| `ctx-german-italian-miracle` | «Milagros» económicos alemán e italiano | economic | 1950–1963 | europe | ★ | `inst-braun`, `inst-olivetti` |
| `ctx-consumer-society` | Sociedad de consumo y crédito | economic | 1950–1973 | europe, north-america | ★ | `th-waste-makers`, `ctx-planned-obsolescence` |
| `ctx-isi-cepal` | Industrialización por sustitución de importaciones (CEPAL) | economic | 1948–1973 | latin-america | ★ | `inst-cidi`, `inst-esdi` |
| `ctx-tv-advertising` | Publicidad televisiva | economic | 1950–1970 | north-america, europe | N | `corporate-identity-design`, `th-hidden-persuaders` |
| `ctx-oil-crisis` | Crisis del petróleo de 1973 | economic | 1973–1974 | global | N | `ctx-plastics`, `ctx-ecology` |
| `ctx-jet-tourism` | Turismo de masas y aeropuertos | economic | 1958–1973 | europe, north-america | N | `ctx-jet-age` |
| `ctx-japan-miracle` | «Milagro» económico japonés | economic | 1955–1973 | global | N | `inst-sony`, `brutalism-metabolism` |
| `ctx-mass-motorisation` | Motorización de masas | economic | 1950–1970 | europe, north-america | ★ | `ctx-german-italian-miracle` |
| `ctx-pret-a-porter` | Prêt-à-porter y boutiques | economic | 1955–1970 | europe | N | `ctx-youth-counterculture` |
| `ctx-mexico-miracle` | «Milagro mexicano» y desarrollo estabilizador | economic | 1954–1970 | latin-america | N | `ctx-isi-cepal` |
| `ctx-corporate-office-boom` | Auge corporativo y de oficinas en Estados Unidos | economic | 1945–1970 | north-america | ★ | `corporate-identity-design`, `inst-herman-miller` |
| `ctx-baby-boom-suburbs` | Baby boom y suburbios | social | 1946–1964 | north-america | ★ | `inst-herman-miller` |
| `ctx-youth-counterculture` | Juventud y contracultura | social | 1955–1975 | europe, north-america | ★ | `ctx-rock-and-pop` |
| `ctx-second-wave-feminism` | Feminismo de segunda ola | social | 1963–1975 | north-america, europe | N | `ctx-youth-counterculture` |
| `ctx-ecology` | Conciencia ecológica | social | 1962–1973 | north-america, europe | N | `th-design-for-the-real-world` |
| `ctx-housing-reconstruction` | Reconstrucción de la vivienda y grandes conjuntos | social | 1945–1970 | europe | ★ | `brutalism-metabolism`, `ctx-marshall-plan` |
| `ctx-nordic-welfare` | Estado de bienestar nórdico | social | 1945–1970 | europe | N | `scandinavian-design`, `inst-ikea` |
| `ctx-latam-urbanisation-1950` | Urbanización acelerada de América Latina | social | 1950–1975 | latin-america | ★ | `ctx-isi-cepal` |
| `ctx-pop-art` | Arte pop | cultural | 1956–1970 | europe, north-america | ★ | `pop-design`, `th-understanding-media` |
| `ctx-rock-and-pop` | Rock y música pop | cultural | 1955–1975 | europe, north-america, latin-america | N | `pop-design` |
| `ctx-olympic-games` | Juegos Olímpicos como proyectos de diseño total (Tokio, México, Múnich) | cultural | 1964–1972 | europe, latin-america, global | ★ | `corporate-identity-design` |
| `ctx-expo-67` | Expo 67 de Montreal | cultural | 1967 | north-america | N | `buckminster-fuller` |
| `ctx-italian-design-culture` | Cultura italiana del diseño (Triennale, Domus, Compasso d’Oro) | cultural | 1946–1970 | europe | N | `italian-design`, `inst-compasso-doro` |
| `ctx-transistor` | Transistor | technological | 1947–1965 | north-america, europe | N | `inst-sony` |
| `ctx-mainframe-computing` | Computadores centrales | technological | 1946–1975 | north-america, europe | ★ | `th-notes-synthesis-form` |
| `ctx-space-race` | Carrera espacial y llegada a la Luna | technological | 1957–1972 | north-america, europe | ★ | `space-age-fashion` |
| `ctx-jet-age` | Era del avión a reacción | technological | 1952–1970 | north-america, europe | N | `ctx-jet-tourism` |
| `ctx-plastics` | Plásticos y petroquímica | technological | 1945–1973 | europe, north-america | ★ | `thermoplastics`, `fibreglass-polyester` |
| `ctx-phototypesetting` | Fotocomposición | technological | 1950–1975 | europe, north-america | N | `letraset`, `international-typographic-style` |

### Productivo

| id | nombre | sub | años | nivel | relaciona |
|---|---|---|---|---|---|
| `fibreglass-polyester` | Fibra de vidrio y poliéster | materials | 1946–1975 | N | `ctx-plastics` |
| `polyurethane-foam` | Espuma de poliuretano | materials | 1950–1975 | N | `ctx-plastics` |
| `thermoplastics` | Termoplásticos (ABS y polipropileno) | materials | 1950–1975 | N | `injection-moulding` |
| `synthetic-fibres` | Fibras sintéticas (poliéster y elastano) | materials | 1950–1975 | N | `ctx-pret-a-porter` |
| `pvc-vinyl` | PVC y vinilo | materials | 1955–1975 | N | `space-age-fashion` |
| `prestressed-concrete` | Hormigón armado y pretensado | materials | 1945–1975 | ★ | `brutalism-metabolism`, `ctx-latam-urbanisation-1950` |
| `aluminium-alloys` | Aleaciones de aluminio | materials | 1945–1975 | N | `good-design` |
| `injection-moulding` | Moldeo por inyección | processes | 1945–1975 | ★ | `ctx-plastics` |
| `flat-pack` | Mueble en caja plana | processes | 1956–1975 | N | `inst-ikea`, `scandinavian-design` |
| `screen-printing` | Serigrafía | processes | 1945–1975 | N | `ctx-youth-counterculture` |
| `modular-systems` | Sistemas modulares y retículas | processes | 1945–1975 | N | `ulm-functionalism`, `international-typographic-style` |
| `prefab-panels` | Paneles prefabricados | processes | 1945–1975 | N | `ctx-housing-reconstruction` |
| `letraset` | Letraset (letras transferibles) | tools | 1961–1975 | N | `international-typographic-style`, `pop-design` |
| `telex-network` | Red de télex | tools | 1945–1975 | N | `ctx-mainframe-computing` |
| `modulor` | Modulor | tools | 1948–1975 | N | `brutalism-metabolism` |

### Teoría

| id | nombre | años | nivel | relaciona |
|---|---|---|---|---|
| `th-rand-thoughts-on-design` | *Thoughts on Design* (Paul Rand) | 1947 | ★ | `paul-rand`, `corporate-identity-design` |
| `th-gute-form` | «Die gute Form» (Max Bill) | 1949 | ★ | `max-bill`, `good-design`, `ulm-functionalism` |
| `th-designing-for-people` | *Designing for People* (Henry Dreyfuss) | 1955 | N | `dreyfuss`, `good-design` |
| `th-hidden-persuaders` | *The Hidden Persuaders* (Vance Packard) | 1957 | N | `ctx-consumer-society`, `ctx-tv-advertising` |
| `th-waste-makers` | *The Waste Makers* (Vance Packard) | 1960 | N | `ctx-consumer-society`, `ctx-planned-obsolescence` |
| `th-neue-grafik` | Revista *Neue Grafik* | 1958 | ★ | `international-typographic-style`, `muller-brockmann` |
| `th-first-things-first` | Manifiesto «First Things First» | 1964 | ★ | `ctx-consumer-society`, `ctx-youth-counterculture` |
| `th-notes-synthesis-form` | *Notes on the Synthesis of Form* (Christopher Alexander) | 1964 | N | `ctx-mainframe-computing`, `inst-hfg-ulm` |
| `th-understanding-media` | *Understanding Media* (Marshall McLuhan) | 1964 | N | `ctx-pop-art`, `ctx-early-television` |
| `th-design-for-the-real-world` | *Design for the Real World* (Victor Papanek) | 1971 | ★ | `ctx-ecology`, `ctx-oil-crisis`, `ctx-consumer-society` |
| `th-learning-from-las-vegas` | *Learning from Las Vegas* (Venturi, Scott Brown e Izenour) | 1972 | ★ | `macro-postmodernism`, `pop-design`, `ctx-pop-art` |

### Movimientos

| id | nombre | años | nivel | relaciona |
|---|---|---|---|---|
| `good-design` | Good Design | 1950–1960 | ★ | `macro-modernism`, `inst-herman-miller`, `inst-knoll` |
| `scandinavian-design` | Diseño escandinavo | 1945–1970 | ★ | `ctx-nordic-welfare`, `inst-marimekko`, `inst-ikea` |
| `italian-design` | Diseño italiano | 1946–1970 | ★ | `ctx-italian-design-culture`, `inst-olivetti`, `inst-compasso-doro` |
| `ulm-functionalism` | Funcionalismo de Ulm | 1953–1968 | ★ | `macro-modernism`, `inst-hfg-ulm`, `inst-braun` |
| `international-typographic-style` | Estilo tipográfico internacional (suizo) | 1950–1975 | ★ | `macro-modernism`, `muller-brockmann`, `helvetica` |
| `corporate-identity-design` | Identidad corporativa | 1950–1975 | N | `macro-modernism`, `inst-unimark`, `ibm-logo` |
| `pop-design` | Diseño pop y psicodélico | 1962–1972 | ★ | `macro-postmodernism`, `ctx-pop-art`, `panton-chair` |
| `radical-design` | Diseño radical | 1966–1975 | N | `macro-postmodernism`, `archizoom`, `superstudio` |
| `brutalism-metabolism` | Brutalismo y metabolismo | 1950–1975 | N | `unite-habitation`, `nakagin-capsule-tower` |
| `space-age-fashion` | Moda de la era espacial | 1963–1968 | N | `andre-courreges`, `pierre-cardin` |
| `macro-postmodernism` | Posmodernismo | 1966–1995 | ★ | `macro-modernism`, `th-learning-from-las-vegas` |

### Instituciones

| id | nombre | años | nivel | relaciona |
|---|---|---|---|---|
| `inst-hfg-ulm` | Hochschule für Gestaltung de Ulm | 1953–1968 | ★ | `ulm-functionalism`, `ctx-german-reconstruction` |
| `inst-braun` | Braun (departamento de diseño) | 1955– | ★ | `ulm-functionalism`, `dieter-rams` |
| `inst-herman-miller` | Herman Miller | 1946– | N | `good-design`, `eames` |
| `inst-knoll` | Knoll | 1946– | N | `good-design`, `eero-saarinen` |
| `inst-marimekko` | Marimekko | 1951– | N | `scandinavian-design`, `maija-isola` |
| `inst-ikea` | IKEA | 1943– | N | `scandinavian-design`, `flat-pack` |
| `inst-compasso-doro` | Premio Compasso d’Oro | 1954– | N | `italian-design`, `inst-olivetti` |
| `inst-push-pin` | Push Pin Studios | 1954–1980 | N | `milton-glaser`, `pop-design` |
| `inst-esdi` | Escuela Superior de Diseño Industrial (ESDI), Río de Janeiro | 1963– | ★ | `inst-hfg-ulm`, `aloisio-magalhaes` |
| `inst-cidi` | Centro de Investigación de Diseño Industrial (CIDI), Buenos Aires | 1962–1970 | N | `ctx-isi-cepal`, `inst-hfg-ulm` |
| `inst-intec` | Instituto de Investigaciones Tecnológicas (INTEC), Chile | 1971–1973 | N | `ctx-corfo`, `ctx-unidad-popular-golpe` |
| `inst-sony` | Sony | 1946– | N | `ctx-japan-miracle`, `ctx-transistor` |
| `inst-unimark` | Unimark International | 1965–1977 | N | `corporate-identity-design`, `massimo-vignelli` |
| `inst-fiat` | Fiat | 1899– | N | `ctx-mass-motorisation`, `italian-design` |
| `inst-levitt` | Levitt & Sons | 1929–1968 | N | `ctx-baby-boom-suburbs`, `ctx-consumer-society` |

### Diseñadores

| id | nombre | años | disciplinas | nivel | obras | relaciona |
|---|---|---|---|---|---|---|
| `eames` | Charles y Ray Eames | 1907–1978 / 1912–1988 | product, architecture | ★ | `eames-lcw`, `eames-lounge`, `eames-fiberglass`, `eames-aluminium`, `eames-house` | `inst-herman-miller`, `good-design` |
| `george-nelson` | George Nelson | 1908–1986 | product | N | `marshmallow-sofa` | `inst-herman-miller`, `good-design` |
| `eero-saarinen` | Eero Saarinen | 1910–1961 | architecture, product | ★ | `tulip-chair`, `womb-chair`, `twa-terminal` | `inst-knoll`, `good-design` |
| `arne-jacobsen` | Arne Jacobsen | 1902–1971 | architecture, product | N | `ant-chair`, `series-7-chair`, `egg-chair`, `sas-royal-hotel` | `scandinavian-design` |
| `hans-wegner` | Hans Wegner | 1914–2007 | product | N | `wishbone-chair` | `scandinavian-design` |
| `verner-panton` | Verner Panton | 1926–1998 | product | ★ | `panton-chair`, `flowerpot-lamp` | `pop-design` |
| `dieter-rams` | Dieter Rams | 1932– | product | ★ | `braun-sk4`, `braun-606` | `inst-braun`, `ulm-functionalism` |
| `hans-gugelot` | Hans Gugelot | 1920–1965 | product | ★ | `braun-sk4` | `inst-hfg-ulm`, `inst-braun` |
| `otl-aicher` | Otl Aicher | 1922–1991 | graphic | ★ | `lufthansa-identity`, `munich72-pictograms` | `inst-hfg-ulm`, `corporate-identity-design` |
| `max-bill` | Max Bill | 1908–1994 | product, architecture, graphic | N | `ulm-stool`, `hfg-ulm-building` | `inst-hfg-ulm`, `ulm-functionalism` |
| `gui-bonsiepe` | Gui Bonsiepe | 1934– | product, graphic | ★ | `cybersyn-opsroom` | `inst-intec`, `inst-hfg-ulm` |
| `marcello-nizzoli` | Marcello Nizzoli | 1887–1969 | product | ★ | `lettera-22`, `mirella-sewing-machine` | `inst-olivetti`, `italian-design` |
| `ettore-sottsass` | Ettore Sottsass | 1917–2007 | product | N | `elea-9003`, `valentine-typewriter`, `carlton-bookcase-1981` | `inst-olivetti`, `italian-design`, `pop-design`, `memphis`, `inst-memphis-group` |
| `castiglioni` | Achille y Pier Giacomo Castiglioni | 1918–2002 / 1913–1968 | product | N | `arco-lamp` | `italian-design` |
| `joe-colombo` | Joe Colombo | 1930–1971 | product | N | `universale-4867` | `italian-design`, `pop-design` |
| `gio-ponti` | Gio Ponti | 1891–1979 | architecture, product | N | `pirelli-tower`, `superleggera-chair` | `italian-design` |
| `paul-rand` | Paul Rand | 1914–1996 | graphic | ★ | `ibm-logo`, `westinghouse-logo` | `corporate-identity-design`, `th-rand-thoughts-on-design` |
| `saul-bass` | Saul Bass | 1920–1996 | graphic | N | `vertigo-titles` | `corporate-identity-design` |
| `massimo-vignelli` | Massimo Vignelli | 1931–2014 | graphic | N | `nyc-transit-standards`, `american-airlines-logo` | `inst-unimark`, `international-typographic-style` |
| `milton-glaser` | Milton Glaser | 1929–2020 | graphic | ★ | `dylan-poster`, `i-love-ny-1977` | `inst-push-pin`, `pop-design`, `ctx-nyc-fiscal-crisis` |
| `muller-brockmann` | Josef Müller-Brockmann | 1914–1996 | graphic | N | `safety-poster-protect-child` | `international-typographic-style`, `th-neue-grafik` |
| `adrian-frutiger` | Adrian Frutiger | 1928–2015 | graphic | ★ | `univers` | `international-typographic-style` |
| `max-miedinger` | Max Miedinger | 1910–1980 | graphic | ★ | `helvetica` | `international-typographic-style` |
| `wim-crouwel` | Wim Crouwel | 1928–2019 | graphic | N | `new-alphabet` | `international-typographic-style` |
| `christian-dior` | Christian Dior | 1905–1957 | fashion | ★ | `dior-new-look`, `dior-trapeze` | |
| `balenciaga` | Cristóbal Balenciaga | 1895–1972 | fashion | N | `balenciaga-sack-dress` | |
| `mary-quant` | Mary Quant | 1930–2023 | fashion | ★ | `quant-miniskirt` | `ctx-youth-counterculture` |
| `yves-saint-laurent` | Yves Saint Laurent | 1936–2008 | fashion | ★ | `ysl-mondrian-dress`, `ysl-le-smoking`, `rive-gauche-boutique`, `dior-trapeze` | `ctx-pret-a-porter` |
| `pierre-cardin` | Pierre Cardin | 1922–2020 | fashion | N | `cardin-cosmocorps` | `space-age-fashion` |
| `andre-courreges` | André Courrèges | 1923–2016 | fashion | N | `courreges-space-age` | `space-age-fashion` |
| `maija-isola` | Maija Isola | 1927–2001 | fashion | ★ | `unikko-print` | `inst-marimekko`, `scandinavian-design` |
| `lina-bo-bardi` | Lina Bo Bardi | 1914–1992 | architecture, product | ★ | `masp`, `casa-de-vidro`, `bowl-chair`, `sesc-pompeia-1986`, `teatro-oficina-1984` | `brutalism-metabolism`, `ctx-latin-popular-craft` |
| `sergio-rodrigues` | Sergio Rodrigues | 1927–2014 | product | ★ | `mole-armchair` | `ctx-brazil-developmentalism` |
| `aloisio-magalhaes` | Aloísio Magalhães | 1927–1982 | graphic | N | `iv-centenario-rio-symbol` | `inst-esdi`, `corporate-identity-design` |
| `lance-wyman` | Lance Wyman | 1937– | graphic | ★ | `mexico68-identity` | `corporate-identity-design`, `ctx-olympic-games` |
| `archizoom` | Archizoom Associati | 1966–1974 | architecture | N | `no-stop-city` | `radical-design` |
| `superstudio` | Superstudio | 1966–1978 | architecture | ★ | `monumento-continuo` | `radical-design` |
| `ramirez-vazquez` | Pedro Ramírez Vázquez | 1919–2013 | architecture | N | `museo-antropologia-mexico`, `mexico68-identity` | `ctx-mexico-miracle` |
| `kinneir-calvert` | Jock Kinneir y Margaret Calvert | 1917–1994 / 1936– | graphic | N | `uk-road-signs` | `ctx-mass-motorisation` |
| `dascanio` | Corradino D’Ascanio | 1891–1981 | product | ★ | `vespa` | `italian-design` |
| `bertoni` | Flaminio Bertoni | 1903–1964 | product | N | `citroen-ds` | `ctx-mass-motorisation` |
| `kurokawa` | Kisho Kurokawa | 1934–2007 | architecture | N | `nakagin-capsule-tower` | `brutalism-metabolism` |
| `katsumie` | Masaru Katsumie | 1909–1983 | graphic | N | `tokyo64-pictograms` | `ctx-olympic-games` |
| `ricardo-porro` | Ricardo Porro | 1925–2014 | architecture | N | `cuba-escuelas-arte` | `ctx-cuban-revolution` |

### Obras

| id | título | disciplina | año | nivel | diseñadores | tech | regiones | contextos |
|---|---|---|---|---|---|---|---|---|
| `helvetica` | Helvetica (Neue Haas Grotesk) | graphic | 1957 | ★ | `max-miedinger` | | europe | `ctx-corporate-office-boom`: Las empresas de oficinas y servicios, en plena expansión, adoptaron una grotesca neutra que diera imagen de eficiencia sin estilo propio; `ctx-phototypesetting`: Su adaptación a la fotocomposición en los años sesenta la hizo barata de componer y nítida en cualquier tamaño |
| `univers` | Univers | graphic | 1957 | ★ | `adrian-frutiger` | | europe | `ctx-phototypesetting`: Frutiger la proyectó como familia sistemática de 21 variantes, pensada desde el inicio para la máquina de fotocomposición Lumitype; `ctx-olympic-games`: Aicher la eligió para Múnich 1972, porque un alfabeto sobrio y sin matices locales servía a visitantes de todo el mundo |
| `ibm-logo` | Logotipo de IBM | graphic | 1956 | ★ | `paul-rand` | | north-america | `ctx-corporate-office-boom`: IBM crecía vendiendo máquinas de oficina y necesitaba una marca única y coherente para todos sus productos y edificios; `ctx-mainframe-computing`: Las letras sólidas con serifas rectas daban imagen de solidez y fiabilidad a las nuevas máquinas de computar |
| `lufthansa-identity` | Identidad visual de Lufthansa | graphic | 1962 | N | `otl-aicher`, `inst-hfg-ulm` | | europe | `ctx-german-reconstruction`: Lufthansa, refundada en 1953, buscaba una imagen moderna y sin rastro del pasado, y recurrió al equipo de la HfG de Ulm; `ctx-jet-tourism`: La llegada de los reactores y del turismo masivo exigía una identidad unificada en aviones, aeropuertos e impresos |
| `munich72-pictograms` | Pictogramas e identidad de Múnich 1972 | graphic | 1972 | ★ | `otl-aicher` | | europe | `ctx-olympic-games`: Los Juegos se concibieron como proyecto de diseño total, y los pictogramas reemplazaron al texto para visitantes de muchos idiomas; `ctx-early-television`: La transmisión televisiva a todo el mundo exigía señales legibles a distancia y en pantalla, con formas y colores muy simples |
| `mexico68-identity` | Identidad gráfica de México 68 | graphic | 1968 | ★ | `lance-wyman`, `ramirez-vazquez` | | latin-america | `ctx-olympic-games`: El comité organizador usó los Juegos para mostrar un país moderno con un programa completo de logotipo, pictogramas, carteles y señalética; `ctx-mexico-miracle`: El crecimiento sostenido del desarrollo estabilizador dio al Estado los medios y la confianza para financiar un programa de diseño de esa escala |
| `tokyo64-pictograms` | Pictogramas e identidad de Tokio 1964 | graphic | 1964 | N | `katsumie` | | global | `ctx-olympic-games`: Ante visitantes que no leían japonés, el comité creó pictogramas de deportes y servicios que luego copiaron otras sedes; `ctx-japan-miracle`: Los Juegos mostraron al mundo la recuperación industrial de Japón, con diseño gráfico moderno como parte del mensaje |
| `vertigo-titles` | Títulos de crédito y cartel de *Vértigo* | graphic | 1958 | N | `saul-bass` | | north-america | `ctx-early-television`: Ante la competencia de la televisión, los estudios trataron los títulos de crédito y los carteles como parte del espectáculo y de la promoción de la película |
| `nyc-transit-standards` | Manual de normas gráficas del Metro de Nueva York | graphic | 1970 | N | `massimo-vignelli`, `inst-unimark` | `modular-systems` | north-america | `ctx-corporate-office-boom`: Unimark trasladó a la señalética pública el método de los programas de identidad corporativa, con manual, retícula y alfabeto único |
| `dylan-poster` | Cartel de Bob Dylan | graphic | 1966 | ★ | `milton-glaser` | | north-america | `ctx-rock-and-pop`: Se incluyó como regalo en un disco de éxitos de Dylan, de modo que el cartel llegó directo a un público joven de rock; `ctx-youth-counterculture`: Sus colores planos y cabellera ondulada expresaban una estética psicodélica opuesta al lenguaje sobrio de la publicidad corporativa |
| `new-alphabet` | Nuevo alfabeto de Wim Crouwel | graphic | 1967 | N | `wim-crouwel` | | europe | `ctx-mainframe-computing`: Crouwel lo planteó como una letra pensada para las limitaciones de las pantallas de tubo de rayos catódicos de la época, hecha solo de líneas rectas |
| `safety-poster-protect-child` | Cartel «¡Protejan al niño!» | graphic | 1953 | N | `muller-brockmann` | | europe | `ctx-mass-motorisation`: El aumento de coches y de accidentes llevó a campañas de seguridad vial, y Müller-Brockmann respondió con una imagen fotográfica y tipografía directa |
| `uk-road-signs` | Señalización vial británica (tipografía Transport) | graphic | 1959 | N | `kinneir-calvert` | | europe | `ctx-mass-motorisation`: Con las primeras autopistas y la mayor velocidad se necesitaban señales legibles a distancia, y el sistema de Kinneir y Calvert las unificó |
| `larrea-covers` | Carátulas de la Nueva Canción Chilena (Larrea) | graphic | 1970 | N | | | latin-america | `ctx-unidad-popular-golpe`: El proyecto cultural de la Unidad Popular y sus sellos discográficos dieron público masivo a la música y a carátulas de identidad propia; `ctx-rock-and-pop`: El disco de larga duración era el soporte masivo de la música joven, y su carátula la principal imagen de cada grupo |
| `brp-murals` | Murales de la Brigada Ramona Parra | graphic | 1970 | N | | | latin-america | `ctx-unidad-popular-golpe`: Las brigadas muralistas pintaron los muros de la campaña de 1970 y del gobierno popular con formas planas y consignas, con pintura barata y trabajo colectivo; `ctx-mexican-muralism`: Retomaron la idea del muro público como medio de arte político que había popularizado el muralismo mexicano |
| `icaic-ospaaal-posters` | Carteles del ICAIC y la OSPAAAL | graphic | 1960 | N | | `screen-printing` | latin-america | `ctx-cuban-revolution`: El Estado revolucionario encargó carteles de cine y de solidaridad internacional, impresos en serigrafía barata y con gran libertad estética; `ctx-cold-war`: La OSPAAAL difundió en varios idiomas carteles para los movimientos del Tercer Mundo dentro del conflicto entre bloques |
| `iv-centenario-rio-symbol` | Símbolo del IV Centenario de Río de Janeiro | graphic | 1965 | N | `aloisio-magalhaes` | | latin-america | `ctx-brazil-developmentalism`: El impulso modernizador de los años cincuenta creó un clima favorable a una gráfica abstracta y geométrica para celebraciones e instituciones públicas |
| `think-small` | Anuncio «Think Small» de Volkswagen (DDB) | graphic | 1959 | ★ | | | north-america | `ctx-consumer-society`: En un mercado saturado de coches grandes y de publicidad exagerada, el anuncio vendió el Escarabajo con humor, sinceridad y un diseño austero; `ctx-baby-boom-suburbs`: Apuntaba a las familias suburbanas que necesitaban un segundo coche barato para el uso diario |
| `atelier-populaire-posters` | Carteles del Atelier Populaire (Mayo del 68) | graphic | 1968 | ★ | | `screen-printing` | europe | `ctx-may-68`: Estudiantes y artistas de la École des Beaux-Arts imprimieron carteles anónimos para huelgas y marchas, en serigrafía rápida y con consignas directas; `ctx-youth-counterculture`: El rechazo a la autoría individual y a la publicidad comercial expresaba el cuestionamiento juvenil de la sociedad de consumo |
| `westinghouse-logo` | Logotipo de Westinghouse | graphic | 1960 | N | `paul-rand` | | north-america | `ctx-tv-advertising`: La publicidad en televisión pedía marcas que se reconocieran de un vistazo en pantallas pequeñas y en blanco y negro, y Rand propuso un símbolo geométrico simple |
| `american-airlines-logo` | Logotipo de American Airlines | graphic | 1967 | N | `massimo-vignelli`, `inst-unimark` | | north-america | `ctx-jet-tourism`: La competencia entre aerolíneas por un público masivo de viajeros llevó a renovar sus marcas con símbolos modernos y fáciles de aplicar en fuselajes y aeropuertos |
| `chase-manhattan-logo` | Logotipo de Chase Manhattan Bank (Chermayeff & Geismar) | graphic | 1960 | N | | | north-america | `ctx-corporate-office-boom`: El banco, que construía su nueva sede en el Bajo Manhattan, encargó un símbolo abstracto y neutro que reemplazara los escudos y emblemas tradicionales |
| `blue-note-covers` | Carátulas de Blue Note Records (Reid Miles) | graphic | 1956 | N | | | north-america | `ctx-consumer-society`: El disco LP de 33 revoluciones hizo de la carátula el principal anuncio del disco y llevó a los sellos a encargar tipografía y fotografía de gran audacia |
| `whole-earth-catalog` | *Whole Earth Catalog* | graphic | 1968 | N | | | north-america | `ctx-youth-counterculture`: Reunió herramientas, libros y oficios para comunidades jóvenes que querían vivir fuera del consumo convencional; `ctx-ecology`: Su portada con la Tierra vista desde el espacio y su lema de autosuficiencia expresaron la nueva conciencia ecológica |
| `dior-new-look` | Colección «Corolle» (New Look) de Dior | fashion | 1947 | ★ | `christian-dior` | | europe | `ctx-war-economy`: Tras años de racionamiento y uniformes, la colección usó metros de tela y cintura marcada como símbolo de abundancia recuperada; `ctx-fashion-magazines`: Carmel Snow, de *Harper’s Bazaar*, bautizó la silueta como «New Look» y la prensa de moda la difundió por el mundo |
| `dior-trapeze` | Línea Trapecio de Dior (Yves Saint Laurent) | fashion | 1958 | N | `yves-saint-laurent`, `christian-dior` | | europe | `ctx-consumer-society`: La casa Dior se convirtió en marca global con licencias, y cada temporada debía lanzar una silueta nueva que se pudiera copiar y vender en masa |
| `balenciaga-sack-dress` | Vestido saco de Balenciaga | fashion | 1957 | N | `balenciaga` | | europe | `ctx-fashion-magazines`: La prensa de moda difundió la línea suelta, sin cintura marcada, que rompía con el New Look y se copió enseguida en la confección industrial |
| `chanel-suit` | Traje de Chanel | fashion | 1954 | N | `coco-chanel` | | europe | `ctx-pret-a-porter`: Su corte cómodo y la tolerancia de la casa a las copias en confección anticipan el prêt-à-porter, con ropa de calidad para mujeres que trabajaban |
| `quant-miniskirt` | Minifalda de Mary Quant | fashion | 1965 | ★ | `mary-quant` | `synthetic-fibres` | europe | `ctx-youth-counterculture`: La falda corta y los colores fuertes expresaron la autonomía de las jóvenes londinenses, que no querían vestirse como sus madres; `ctx-pret-a-porter`: Quant vendía en su boutique de Chelsea y producía en serie para tiendas, lo que llevó la moda a un público masivo y joven |
| `ysl-mondrian-dress` | Vestido Mondrian de Yves Saint Laurent | fashion | 1965 | N | `yves-saint-laurent` | | europe | `ctx-pop-art`: Convirtió una obra de arte moderna en prenda, en el clima del arte pop que borraba la frontera entre arte, objeto y consumo |
| `ysl-le-smoking` | Le Smoking de Yves Saint Laurent | fashion | 1966 | ★ | `yves-saint-laurent` | | europe | `ctx-second-wave-feminism`: El esmoquin para mujeres tomó un código de vestuario masculino en los años en que las mujeres reclamaban igualdad pública y laboral; `ctx-pret-a-porter`: La apertura de Rive Gauche en 1966 llevó este tipo de propuestas a tiendas más accesibles que la alta costura |
| `courreges-space-age` | Colección «Era espacial» de Courrèges | fashion | 1964 | N | `andre-courreges` | `pvc-vinyl` | europe | `ctx-space-race`: Los vuelos de Gagarin y de los astronautas estadounidenses dieron un imaginario de trajes, botas blancas y siluetas geométricas que Courrèges trasladó a la calle |
| `cardin-cosmocorps` | Colección «Cosmocorps» de Pierre Cardin | fashion | 1967 | N | `pierre-cardin` | `pvc-vinyl` | europe | `ctx-space-race`: La carrera hacia la Luna inspiró túnicas, cascos y tejidos geométricos que Cardin presentó como ropa unisex del futuro |
| `rive-gauche-boutique` | Boutique Rive Gauche de Yves Saint Laurent | fashion | 1966 | N | `yves-saint-laurent` | | europe | `ctx-pret-a-porter`: La casa abrió una tienda de ropa lista para llevar, a precio menor que la alta costura, y legitimó el prêt-à-porter entre los grandes creadores; `ctx-consumer-society`: Un público más amplio con poder de compra quería ropa de firma sin esperar pruebas ni pagar precios de costura |
| `unikko-print` | Estampado Unikko de Marimekko | fashion | 1964 | ★ | `maija-isola`, `inst-marimekko` | | europe | `ctx-nordic-welfare`: El diseño textil de Marimekko se pensó como producto cotidiano y asequible para un país nórdico de bienestar y consumo doméstico; `ctx-consumer-society`: Los estampados grandes y coloridos se vendieron como ropa y decoración a un público de mercado masivo |
| `paper-dress` | Vestidos de papel de Scott Paper | fashion | 1966 | N | | | north-america | `ctx-consumer-society`: Una empresa de productos de papel lanzó vestidos desechables como promoción y los vendió como moda barata y de un solo uso; `ctx-pop-art`: Sus estampados de arte pop y su carácter efímero jugaban con la cultura de consumo que el arte pop celebraba y criticaba |
| `eames-lcw` | Silla LCW de Charles y Ray Eames | product | 1945 | ★ | `eames`, `inst-herman-miller` | `moulded-plywood` | north-america | `ctx-second-world-war`: Los Eames desarrollaron el terciado moldeado en tablillas y piezas para la Marina estadounidense, y esa técnica de guerra se convirtió en silla; `ctx-baby-boom-suburbs`: Las nuevas familias de posguerra necesitaban muebles livianos, baratos y modernos para casas pequeñas |
| `eames-lounge` | Sillón Lounge y otomana de los Eames | product | 1956 | N | `eames`, `inst-herman-miller` | `moulded-plywood` | north-america | `ctx-corporate-office-boom`: Se concibió como sillón de lujo para ejecutivos y profesionales de ingresos altos, un símbolo de estatus de la nueva clase corporativa; `ctx-early-television`: Se presentó en el programa *Home* de la televisión NBC en 1956, lo que mostró cómo el medio podía lanzar un producto de diseño |
| `eames-fiberglass` | Sillas de fibra de vidrio de los Eames | product | 1950 | N | `eames`, `inst-herman-miller` | `fibreglass-polyester` | north-america | `ctx-plastics`: Los plásticos reforzados con fibra de vidrio, desarrollados antes y durante la guerra, permitieron por primera vez moldear en serie una carcasa de silla de una sola pieza |
| `eames-aluminium` | Aluminum Group de los Eames | product | 1958 | N | `eames`, `inst-herman-miller` | `aluminium-alloys` | north-america | `ctx-corporate-office-boom`: Se vendió como silla de oficina y sala de reuniones de gama alta, con una estructura de aluminio fundido y tapiz tensado |
| `tulip-chair` | Silla Tulip de Eero Saarinen | product | 1956 | ★ | `eero-saarinen`, `inst-knoll` | `fibreglass-polyester`, `aluminium-alloys` | north-america | `ctx-plastics`: Una carcasa de plástico reforzado sobre un pie de aluminio fundido permitió formar el asiento de una pieza y suprimir las patas; `ctx-corporate-office-boom`: Knoll la vendió a oficinas y comedores corporativos que buscaban una imagen limpia y moderna |
| `womb-chair` | Sillón Womb de Eero Saarinen | product | 1948 | N | `eero-saarinen`, `inst-knoll` | `fibreglass-polyester` | north-america | `ctx-baby-boom-suburbs`: Florence Knoll pidió a Saarinen un sillón en el que se pudiera sentar de lado y acurrucarse, pensado para el living informal de las casas nuevas |
| `ant-chair` | Silla Ant de Arne Jacobsen | product | 1952 | N | `arne-jacobsen` | `moulded-plywood` | europe | `ctx-nordic-welfare`: Se diseñó para el comedor de empleados de una empresa farmacéutica danesa, es decir, para un mobiliario institucional apilable y barato del Estado de bienestar |
| `series-7-chair` | Silla Serie 7 de Arne Jacobsen | product | 1955 | N | `arne-jacobsen` | `moulded-plywood` | europe | `ctx-consumer-society`: Fritz Hansen la fabricó en grandes series y se vendió a hogares, oficinas y escuelas, con lo que se volvió la silla más vendida del diseño danés |
| `egg-chair` | Sillón Egg de Arne Jacobsen | product | 1958 | N | `arne-jacobsen` | `polyurethane-foam` | europe | `ctx-jet-tourism`: Se creó para el vestíbulo y las habitaciones del hotel de la aerolínea SAS en Copenhague, un hotel pensado para viajeros aéreos; `ctx-plastics`: Su carcasa moldeada con espuma y tapiz permitió una forma escultórica imposible con estructuras de madera |
| `wishbone-chair` | Silla Wishbone (CH24) de Hans Wegner | product | 1949 | N | `hans-wegner` | | europe | `ctx-nordic-welfare`: Combinó oficio de ebanista y producción en taller para un mercado doméstico de clase media con gusto por el diseño sobrio |
| `panton-chair` | Silla Panton | product | 1967 | ★ | `verner-panton` | `injection-moulding`, `thermoplastics` | europe | `ctx-plastics`: Los nuevos plásticos moldeables permitieron la primera silla de una sola pieza, de forma continua y sin juntas; `ctx-pop-art`: Su color brillante y su forma escultórica pertenecen al gusto pop de los sesenta, que celebraba el material sintético y lo artificial |
| `flowerpot-lamp` | Lámpara Flowerpot de Verner Panton | product | 1968 | N | `verner-panton` | | europe | `ctx-youth-counterculture`: Sus colores intensos y su forma de juguete reflejan el gusto juvenil por lo lúdico y lo psicodélico en el interior doméstico |
| `ulm-stool` | Taburete Ulm | product | 1954 | N | `max-bill`, `inst-hfg-ulm` | `modular-systems` | europe | `ctx-german-reconstruction`: Fue el mueble básico de la HfG, escuela fundada para renovar la cultura alemana tras el nazismo, y sirvió de asiento, mesa y repisa; `ctx-housing-reconstruction`: Las viviendas de reconstrucción eran pequeñas, y un mueble multifuncional de tablas y barra resolvía varios usos |
| `braun-sk4` | Radiogramófono Braun SK 4 | product | 1956 | ★ | `dieter-rams`, `hans-gugelot`, `inst-braun` | `modular-systems` | europe | `ctx-german-italian-miracle`: Los hogares alemanes ya tenían ingresos para comprar radios y tocadiscos, y Braun apostó por un producto sobrio como imagen de marca; `ctx-german-reconstruction`: La alianza con la HfG de Ulm dio a la empresa un diseño racional y sin ornamento, en contraste con el pasado reciente |
| `braun-606` | Sistema de estantes 606 | product | 1960 | N | `dieter-rams` | `modular-systems`, `aluminium-alloys` | europe | `ctx-housing-reconstruction`: Su sistema de rieles y módulos se adaptaba a viviendas pequeñas y cambiantes, en lugar del mueble pesado y fijo |
| `lettera-22` | Máquina de escribir Lettera 22 | product | 1950 | ★ | `marcello-nizzoli`, `inst-olivetti` | `aluminium-alloys` | europe | `ctx-german-italian-miracle`: Olivetti la exportó en el auge económico italiano como máquina portátil para profesionales y estudiantes de todo el mundo; `ctx-italian-design-culture`: La cultura del diseño italiana, con la Triennale y el premio Compasso d’Oro, valoró la máquina como objeto de arte industrial |
| `elea-9003` | Computador Olivetti Elea 9003 | product | 1959 | N | `ettore-sottsass`, `inst-olivetti` | | europe | `ctx-mainframe-computing`: Sottsass dio forma a los gabinetes del primer gran computador transistorizado de Olivetti, para mostrar una máquina compleja de manera ordenada; `ctx-italian-design-culture`: La empresa trataba el diseño industrial como parte de su proyecto cultural y recibió por esta máquina el premio Compasso d’Oro |
| `valentine-typewriter` | Máquina de escribir Valentine | product | 1969 | N | `ettore-sottsass`, `inst-olivetti` | `thermoplastics`, `injection-moulding` | europe | `ctx-pop-art`: Su plástico rojo brillante y su estuche de juguete rompieron la seriedad de la máquina de oficina y la acercaron al objeto pop; `ctx-plastics`: El moldeo por inyección de termoplásticos permitió una carcasa de color intenso y producción en serie barata |
| `mirella-sewing-machine` | Máquina de coser Mirella | product | 1957 | N | `marcello-nizzoli` | | europe | `ctx-german-italian-miracle`: Necchi vendió masivamente máquinas domésticas a familias italianas que mejoraban sus ingresos, y Nizzoli le dio una carcasa continua y limpia |
| `vespa` | Vespa 98 | product | 1946 | ★ | `dascanio` | `steel-body-pressing` | europe | `ctx-second-world-war`: Piaggio, fabricante de aviones destruido por la guerra, reconvirtió su industria y su personal técnico en un vehículo barato; `ctx-mass-motorisation`: Millones de italianos que no podían comprar un coche accedieron a la movilidad individual con una scooter económica |
| `fiat-500` | Fiat 500 (Dante Giacosa) | product | 1957 | N | `inst-fiat` | `steel-body-pressing` | europe | `ctx-german-italian-miracle`: El auge de los ingresos italianos creó una demanda de coche pequeño y barato para familias de obreros y empleados; `ctx-mass-motorisation`: Fiat produjo el modelo a gran escala como coche popular, con carrocería de acero estampado y motor trasero compacto |
| `citroen-ds` | Citroën DS | product | 1955 | N | `bertoni` | | europe | `ctx-mass-motorisation`: El coche mostró cómo la motorización europea buscaba el confort y el estatus además del transporte básico; `ctx-jet-age`: Su línea aerodinámica y su suspensión hidroneumática trasladaron al automóvil la imagen de la aviación a reacción |
| `mole-armchair` | Sillón Mole de Sergio Rodrigues | product | 1957 | ★ | `sergio-rodrigues` | | latin-america | `ctx-brazil-developmentalism`: El Brasil modernizador de Kubitschek impulsó un diseño propio con maderas nativas como el jacarandá, en lugar de depender de modelos europeos; `ctx-latam-urbanisation-1950`: La expansión de las ciudades creó una clase media de departamentos nuevos que quería muebles modernos hechos con materiales locales |
| `bowl-chair` | Bowl Chair de Lina Bo Bardi | product | 1951 | N | `lina-bo-bardi` | | latin-america | `ctx-brazil-developmentalism`: El clima modernizador del país favoreció un mobiliario moderno de producción local, con una estructura metálica sencilla y un cojín de cuero |
| `cybersyn-opsroom` | Sala de operaciones de Cybersyn | product | 1972 | ★ | `gui-bonsiepe`, `inst-intec` | `telex-network` | latin-america | `ctx-unidad-popular-golpe`: El gobierno de Allende buscó coordinar las empresas nacionalizadas con un sistema de información, y el diseño de la sala daba forma a esa idea; `ctx-corfo`: La CORFO administraba esas empresas, que enviaban los datos diarios de producción; `ctx-mainframe-computing`: La sala se apoyaba en computadores centrales y en el télex como red de datos |
| `sony-tr63` | Radio de bolsillo Sony TR-63 | product | 1957 | N | `inst-sony` | | global | `ctx-transistor`: El transistor permitió una radio pequeña y de pilas, que podía llevarse en un bolsillo y escucharse a solas; `ctx-japan-miracle`: Sony la exportó a Estados Unidos como parte del crecimiento industrial japonés y mostró que Japón podía competir en diseño electrónico |
| `universale-4867` | Silla Universale 4867 de Joe Colombo | product | 1967 | N | `joe-colombo` | `injection-moulding`, `thermoplastics` | europe | `ctx-plastics`: Fue de las primeras sillas de plástico moldeadas por inyección con ABS en piezas encajables; `ctx-italian-design-culture`: Las empresas italianas, como Kartell, trabajaron con diseñadores para convertir el plástico en un material de calidad |
| `arco-lamp` | Lámpara Arco de los hermanos Castiglioni | product | 1962 | N | `castiglioni` | | europe | `ctx-italian-design-culture`: El fabricante Flos y los diseñadores trabajaron juntos en objetos que resolvían un problema doméstico, como iluminar una mesa sin colgar el techo, con humor y oficio |
| `superleggera-chair` | Silla Superleggera de Gio Ponti | product | 1957 | N | `gio-ponti` | | europe | `ctx-italian-design-culture`: Ponti, desde la revista *Domus*, defendió unir oficio artesanal e industria, y la silla ligera de Cassina ganó el Compasso d’Oro; `ctx-german-italian-miracle`: El auge de los ingresos domésticos abrió un mercado para muebles de diseño |
| `marshmallow-sofa` | Sofá Marshmallow de George Nelson | product | 1956 | N | `george-nelson`, `inst-herman-miller` | `polyurethane-foam` | north-america | `ctx-consumer-society`: Herman Miller lo vendió como pieza de moda para hogares con mayores ingresos; `ctx-pop-art`: Sus discos de colores sobre una estructura metálica anticiparon el humor y el color del diseño pop |
| `unite-habitation` | Unité d’Habitation de Marsella | architecture | 1952 | ★ | `le-corbusier` | `modulor`, `prestressed-concrete` | europe | `ctx-housing-reconstruction`: El Estado francés encargó un bloque colectivo para responder a la falta de vivienda tras la guerra, con calles interiores, servicios comunes y departamentos dúplex; `ctx-marshall-plan`: El esfuerzo de reconstrucción europeo, apoyado por el Plan Marshall, dio al Estado medios para ensayar vivienda colectiva a gran escala |
| `ronchamp-chapel` | Capilla de Notre-Dame-du-Haut en Ronchamp | architecture | 1955 | N | `le-corbusier` | | europe | `ctx-second-world-war`: La capilla anterior, destruida en los combates de 1944, fue reemplazada por un santuario de hormigón de forma escultórica y muros gruesos |
| `seagram-building` | Seagram Building | architecture | 1958 | N | `mies-van-der-rohe` | | north-america | `ctx-corporate-office-boom`: La empresa Seagram quiso una sede que proyectara prestigio, y el rascacielos de bronce y vidrio se volvió el modelo de la torre de oficinas moderna |
| `interbau-hansaviertel` | Interbau, Hansaviertel de Berlín | architecture | 1957 | N | `gropius`, `le-corbusier`, `oscar-niemeyer` | | europe | `ctx-cold-war`: Berlín Occidental reunió a arquitectos de renombre para mostrar su modo de vida moderno frente a la Stalinallee del Este; `ctx-housing-reconstruction`: El barrio devastado por la guerra se reconstruyó como exposición de vivienda moderna en bloques y torres |
| `eames-house` | Casa Eames (Case Study House 8) | architecture | 1949 | N | `eames` | `modular-systems` | north-america | `ctx-baby-boom-suburbs`: El programa Case Study House buscó modelos de vivienda moderna y económica para la demanda de posguerra en California; `ctx-second-world-war`: La casa se armó con piezas de acero industriales de catálogo, un material que la economía de guerra había estandarizado |
| `hfg-ulm-building` | Edificio de la HfG de Ulm | architecture | 1955 | N | `max-bill`, `inst-hfg-ulm` | `modular-systems` | europe | `ctx-german-reconstruction`: La escuela nació como proyecto de reeducación democrática y recibió financiamiento privado y estadounidense, y su edificio expresó esa voluntad con hormigón a la vista; `ctx-german-italian-miracle`: Las empresas del milagro, como Braun, se volvieron clientes y aliadas de la escuela |
| `brasilia-plano-piloto` | Brasilia: Plan Piloto y Plaza de los Tres Poderes | architecture | 1957 | ★ | `lucio-costa`, `oscar-niemeyer` | `prestressed-concrete` | latin-america | `ctx-brazil-developmentalism`: El presidente Kubitschek quiso construir la capital en el interior en pocos años, como símbolo de un Brasil moderno; `ctx-latam-urbanisation-1950`: La ciudad nueva se proyectó para ordenar el crecimiento urbano acelerado, con separación de funciones y circulación en autos |
| `alvorada-palace` | Palacio de la Alvorada | architecture | 1958 | N | `oscar-niemeyer` | `prestressed-concrete` | latin-america | `ctx-brazil-developmentalism`: Fue la primera obra monumental de la nueva capital y mostró el hormigón curvo de Niemeyer como imagen del Brasil moderno |
| `brasilia-cathedral` | Catedral de Brasilia | architecture | 1970 | N | `oscar-niemeyer` | `prestressed-concrete` | latin-america | `ctx-latam-urbanisation-1950`: La catedral completó el eje monumental de una capital proyectada desde cero, con una estructura hiperboloide de hormigón visible desde la ciudad |
| `masp` | Museo de Arte de São Paulo (MASP) | architecture | 1968 | ★ | `lina-bo-bardi` | `prestressed-concrete` | latin-america | `ctx-latam-urbanisation-1950`: El crecimiento de São Paulo y de su avenida Paulista llevó a pensar un museo abierto al público, con una plaza cubierta bajo el volumen elevado; `ctx-isi-cepal`: La industrialización paulista creó la burguesía y los recursos que sostuvieron el museo y su colección |
| `casa-de-vidro` | Casa de Vidro de Lina Bo Bardi | architecture | 1951 | N | `lina-bo-bardi` | | latin-america | `ctx-latam-urbanisation-1950`: La expansión de São Paulo hacia barrios nuevos como el Morumbi permitió ensayar una casa moderna de vidrio sobre una ladera boscosa |
| `unam-central-library` | Biblioteca Central de la UNAM | architecture | 1952 | N | `juan-ogorman` | | latin-america | `ctx-mexico-miracle`: El crecimiento y la inversión pública de la época llevaron a construir la Ciudad Universitaria como emblema de modernidad; `ctx-mexican-muralism`: Los muros se cubrieron con mosaicos de piedra de colores que integraron arte público y arquitectura, en la tradición del muralismo |
| `museo-antropologia-mexico` | Museo Nacional de Antropología de México | architecture | 1964 | N | `ramirez-vazquez` | `prestressed-concrete` | latin-america | `ctx-mexico-miracle`: El Estado, con recursos del crecimiento sostenido, construyó el museo como monumento a la identidad nacional; `ctx-mexican-muralism`: Integró murales, relieves y esculturas con la arquitectura, tradición que el muralismo había hecho central en México |
| `cuba-escuelas-arte` | Escuelas Nacionales de Arte de La Habana | architecture | 1961 | N | `ricardo-porro` | | latin-america | `ctx-cuban-revolution`: El nuevo gobierno encargó escuelas de arte en un antiguo club de golf, con bóvedas de ladrillo catalanas por falta de acero y de hormigón |
| `casa-curutchet` | Casa Curutchet de Le Corbusier | architecture | 1953 | N | `le-corbusier` | `modulor` | latin-america | `ctx-latam-urbanisation-1950`: Un cirujano de La Plata, ciudad de clase media profesional en crecimiento, encargó una casa y consultorio en un lote entre medianeras |
| `pirelli-tower` | Torre Pirelli de Milán | architecture | 1958 | N | `gio-ponti` | `prestressed-concrete` | europe | `ctx-german-italian-miracle`: El rascacielos de la empresa de neumáticos fue el símbolo del boom económico de Milán y del orgullo industrial italiano |
| `sas-royal-hotel` | SAS Royal Hotel de Copenhague | architecture | 1960 | N | `arne-jacobsen` | | europe | `ctx-jet-tourism`: La aerolínea nórdica construyó un hotel y terminal en el centro de la ciudad para sus pasajeros, con diseño integral de edificio, muebles y cubiertos |
| `twa-terminal` | Terminal de TWA en Idlewild (JFK) | architecture | 1962 | N | `eero-saarinen` | `prestressed-concrete` | north-america | `ctx-jet-age`: La llegada de los reactores comerciales exigía terminales nuevas, y Saarinen expresó el vuelo con una cáscara de hormigón curva; `ctx-jet-tourism`: El turismo aéreo de masas hizo de la terminal un espacio de espectáculo para los viajeros de clase media |
| `nakagin-capsule-tower` | Torre Cápsula Nakagin | architecture | 1972 | N | `kurokawa` | `prefab-panels` | global | `ctx-japan-miracle`: El crecimiento de Tokio y de la economía japonesa creó demanda de pequeños departamentos urbanos para ejecutivos, resueltos con cápsulas prefabricadas intercambiables |
| `fuller-geodesic-dome` | Pabellón de Estados Unidos en la Expo 67 (domo geodésico) | architecture | 1967 | N | `buckminster-fuller` | | north-america | `ctx-expo-67`: La exposición de Montreal dio a Estados Unidos un escaparate mundial, y el domo de Fuller mostró una estructura ligera y repetible a gran escala; `ctx-ecology`: Las ideas de Fuller sobre la «nave espacio Tierra» y el uso eficiente de recursos dieron al domo un valor simbólico ecológico |
| `philips-pavilion` | Pabellón Philips de la Expo 58 | architecture | 1958 | N | `le-corbusier` | | europe | `ctx-cold-war`: La exposición de Bruselas enfrentó los pabellones de los dos bloques, y las empresas privadas europeas usaron el suyo para mostrar tecnología avanzada |
| `monumento-continuo` | Monumento continuo de Superstudio | architecture | 1969 | ★ | `superstudio` | | europe | `ctx-consumer-society`: El proyecto imaginó una arquitectura única que cubre el planeta, como crítica irónica al urbanismo del consumo masivo y de la ciudad homogénea; `ctx-may-68`: La radicalización política de 1968 impulsó a jóvenes arquitectos a usar la utopía como crítica del funcionalismo |
| `no-stop-city` | No-Stop City de Archizoom | architecture | 1970 | N | `archizoom` | | europe | `ctx-consumer-society`: El proyecto imaginó la ciudad como una gran fábrica o supermercado sin exterior, para llevar al límite la lógica de la sociedad de consumo |
| `levittown` | Levittown | architecture | 1947 | N | `inst-levitt` | | north-america | `ctx-baby-boom-suburbs`: Levitt & Sons construyó miles de casas idénticas en serie para veteranos y familias jóvenes, con métodos de producción tipo cadena; `ctx-consumer-society`: Cada casa incluía electrodomésticos y televisor, y el suburbio se vendió como un estilo de vida de consumo |

### Conexiones

| from | to | línea |
|---|---|---|
| `inst-hfg-ulm` | `inst-braun` | Profesores de Ulm como Gugelot y Aicher diseñaban para Braun, y así el método racional de la escuela pasó a los productos de la empresa. |
| `inst-hfg-ulm` | `inst-esdi` | La ESDI de Río se organizó siguiendo el modelo pedagógico de Ulm, con docentes formados allí. |
| `tokyo64-pictograms` | `munich72-pictograms` | Aicher partió de la lógica de pictogramas de Tokio 1964 para construir el sistema de Múnich, más sistemático. |
| `mexico68-identity` | `munich72-pictograms` | México 68 mostró que una identidad unificada podía cubrir un evento completo y alentó el programa total de Múnich. |
| `unite-habitation` | `brasilia-plano-piloto` | Los principios de Le Corbusier sobre bloques residenciales y separación de funciones marcaron el plan de Lúcio Costa. |
| `eames-fiberglass` | `panton-chair` | La carcasa de plástico de una pieza de los Eames abrió el camino a la silla de plástico continua de Panton. |
| `lettera-22` | `valentine-typewriter` | Sottsass rompió con la sobriedad de Nizzoli para Olivetti y volvió la máquina portátil un objeto pop. |
| `dior-new-look` | `dior-trapeze` | El joven Saint Laurent soltó la cintura marcada del New Look y abrió la silueta en trapecio. |
| `no-stop-city` | `monumento-continuo` | Ambos grupos florentinos usaron la utopía crítica para mostrar el absurdo de la ciudad homogénea del consumo masivo. |
| `th-gute-form` | `ulm-functionalism` | El texto de Max Bill sobre la buena forma dio a Ulm sus primeros principios de diseño. |
| `helvetica` | `univers` | Ambas grotescas de 1957 respondieron a la demanda de una sans serif neutra y se disputaron las identidades corporativas. |
| `th-learning-from-las-vegas` | `macro-postmodernism` | El libro de Venturi, Scott Brown e Izenour defendió el signo comercial y el ornamento que el funcionalismo rechazaba. |
| `inst-intec` | `cybersyn-opsroom` | INTEC reunió al equipo de diseñadores que dio forma industrial a la sala de operaciones del proyecto. |
| `larrea-covers` | `brp-murals` | Las carátulas y los murales de la Unidad Popular compartieron colores planos y una estética de cartel de bajo costo y alcance masivo. |
| `brutalism-metabolism` | `unite-habitation` | Los metabolistas tomaron de la Unité de Le Corbusier la idea del bloque como ciudad en altura, y la volvieron cápsulas renovables. |
| `courreges-space-age` | `cardin-cosmocorps` | Ambos diseñadores tradujeron el imaginario espacial a líneas geométricas y materiales sintéticos, y se disputaron la paternidad de la moda del futuro. |

### Reserva

| id | tipo | nombre | motivo |
|---|---|---|---|
| `ctx-decolonisation` | contexto | Descolonización | Solo explica obras de fuera de Occidente, que el plan limita |
| `ctx-container-shipping` | contexto | Contenedor y transporte marítimo | Difícil de conectar con una obra concreta del tramo |
| `ctx-civil-rights` | contexto | Movimiento por los derechos civiles | Sin obra del tramo que lo requiera |
| `ctx-vietnam-war` | contexto | Guerra de Vietnam | Efecto sobre carteles cubierto por Mayo del 68 y la contracultura |
| `ctx-swinging-london` | contexto | Londres de los sesenta | Cubierto por juventud y contracultura y prêt-à-porter |
| `ctx-latam-developmental-modernism` | contexto | Arquitectura moderna latinoamericana de Estado | Se cubre con desarrollismo brasileño y milagro mexicano |
| `vacuum-forming` | productivo | Termoformado | Cubierto por termoplásticos |
| `welded-wire-mesh` | productivo | Malla de alambre soldado (Bertoia) | Solo una obra posible, la silla Diamond |
| `acrylic-glass` | productivo | Acrílico y metacrilato | Sin obra del tramo que lo necesite |
| `th-architecture-without-architects` | teoría | *Architecture Without Architects* (Rudofsky) | Menor peso que las demás teorías del tramo |
| `th-bonsiepe-chile-texts` | teoría | Textos de Bonsiepe sobre la experiencia chilena (1974) | Título y año por verificar |
| `th-maldonado-ulm-texts` | teoría | Textos de Tomás Maldonado en Ulm | Sin cita exacta que pueda fecharse con seguridad |
| `british-pop-design` | movimiento | Pop británico (Swinging London) | Se absorbe en diseño pop y psicodélico |
| `inst-pentagram` | institución | Pentagram | Fundada en 1972, sin obra del tramo |
| `inst-vitra` | institución | Vitra | Sus obras entran por Panton y Herman Miller |
| `inst-icsid` | institución | ICSID | Sin obra ni diseñador enlazados |
| `inst-dicap` | institución | DICAP (sello discográfico chileno) | Fecha por verificar y cuenta contra el límite chileno |
| `inst-kartell` | institución | Kartell | Cubierta por Colombo y los plásticos |
| `tomas-maldonado` | diseñador | Tomás Maldonado | Sin obra del tramo bien atribuida |
| `reid-miles` | diseñador | Reid Miles | Entra como obra anónima de Blue Note |
| `sori-yanagi` | diseñador | Sori Yanagi | Oriental sin influencia demostrada suficiente |
| `alec-issigonis` | diseñador | Alec Issigonis | Cupo de diseñadores completo |
| `frei-otto` | diseñador | Frei Otto | Cupo de diseñadores completo |
| `helmut-krone` | diseñador | Helmut Krone | Obra «Think Small» entra con la agencia DDB |
| `alexandre-wollner` | diseñador | Alexandre Wollner | Sin obra con atribución segura |
| `butterfly-stool` | obra | Taburete Butterfly de Sori Yanagi | Oriental, se deja en reserva |
| `mini-1959` | obra | Austin Mini | Cupo de diseñadores completo |
| `sgt-pepper-cover` | obra | Carátula de *Sgt. Pepper* | Diseñadores fuera del cupo |
| `yellow-submarine-film` | obra | *Yellow Submarine* | Diseñador fuera del cupo |
| `fillmore-posters` | obra | Carteles del Fillmore (Wes Wilson) | Diseñador fuera del cupo |
| `optima-typeface` | obra | Optima de Hermann Zapf | Diseñador fuera del cupo |
| `bertoia-diamond` | obra | Silla Diamond de Harry Bertoia | Diseñador fuera del cupo |
| `pruitt-igoe` | obra | Pruitt-Igoe | Mejor tratarlo en Posmoderno como símbolo de la crisis moderna |
| `petrobras-logo` | obra | Logotipo de Petrobras (Magalhães) | Fecha por verificar |
| `habitat-67` | obra | Habitat 67 de Moshe Safdie | Diseñador fuera del cupo |
| `barbican-estate` | obra | Barbican Estate | Diseñadores colectivos fuera del cupo |
| `caracas-ciudad-universitaria` | obra | Ciudad Universitaria de Caracas | Fecha por verificar y sin diseñador en el cupo |
| `banco-de-londres-buenos-aires` | obra | Banco de Londres, Buenos Aires | Diseñador fuera del cupo |
| `munich-olympic-park` | obra | Parque Olímpico de Múnich | Diseñador fuera del cupo |
| `farnsworth-house` | obra | Casa Farnsworth | Sin contexto de posguerra que la explique bien |
| `xerox-914` | productivo | Fotocopiadora Xerox 914 | v35: sin obra, diseñador, institución ni movimiento al que enlazarla con mecanismo cierto |
| `larrea-hermanos` | diseñador | Vicente y Antonio Larrea | v35: sin años ni trayectoria conocidos con certeza; la obra `larrea-covers` va con `maker` |

## Tramo: postmodern

### Contextos

| id | nombre | sub | años | regiones | nivel | relaciona |
|---|---|---|---|---|---|---|
| `ctx-neoliberalism` | Neoliberalismo y desregulación | political | 1975–hoy | europe, north-america, latin-america | ★ | `ctx-globalisation`, `ctx-chile-market-economy`, `ctx-chile-dictatorship` |
| `ctx-chile-dictatorship` | Dictadura militar en Chile | political | 1973–1990 | latin-america | ★ | `ctx-human-rights-resistance` |
| `ctx-plebiscite-1988` | Plebiscito chileno de 1988 | political | 1988 | latin-america | ★ | `ctx-chile-dictatorship` |
| `ctx-obama-2008` | Campaña presidencial de Obama | political | 2008 | north-america | N | `ctx-internet-culture`, `ctx-crisis-2008` |
| `ctx-globalisation` | Globalización y deslocalización | economic | 1980–hoy | global | ★ | `ctx-branding` |
| `ctx-branding` | Marcas globales y branding | economic | 1980–hoy | global | ★ | `ctx-globalisation` |
| `ctx-crisis-2008` | Crisis financiera de 2008 | economic | 2008–2010 | global | N | `ctx-neoliberalism` |
| `ctx-nyc-fiscal-crisis` | Crisis fiscal de Nueva York | economic | 1975 | north-america | N | `ctx-branding`, `ctx-neoliberalism` |
| `ctx-japan-consumer-economy` | Auge económico y de consumo de Japón | economic | 1970–1990 | global | N | `ctx-globalisation` |
| `ctx-chile-market-economy` | Economía de mercado en Chile | economic | 1975–hoy | latin-america | N | `ctx-chile-dictatorship` |
| `ctx-platform-economy` | Economía de plataformas | economic | 2008–hoy | global | N | `ctx-smartphone` |
| `ctx-feminisms` | Feminismos y nuevas identidades de género | social | 1970–hoy | europe, north-america, latin-america | N | `ctx-postmodern-culture` |
| `ctx-climate-crisis` | Crisis climática y sostenibilidad | social | 1990–hoy | global | ★ | `ctx-globalisation` |
| `ctx-urban-informality` | Informalidad urbana y déficit de vivienda | social | 1975–hoy | latin-america | ★ | `ctx-chile-market-economy` |
| `ctx-ageing-accessibility` | Envejecimiento y diseño accesible | social | 1980–hoy | north-america, europe | N | `ctx-personal-computer` |
| `ctx-human-rights-resistance` | Resistencia y derechos humanos bajo dictaduras | social | 1974–1990 | latin-america | ★ | `ctx-plebiscite-1988` |
| `ctx-punk` | Punk y subculturas juveniles | cultural | 1976–1985 | europe, north-america | ★ | `ctx-postmodern-culture` |
| `ctx-postmodern-culture` | Cultura posmoderna | cultural | 1975–2000 | europe, north-america, global | ★ | `ctx-crisis-functionalism` |
| `ctx-mtv-club` | MTV y cultura de club | cultural | 1981–2000 | north-america, europe | N | `ctx-postmodern-culture` |
| `ctx-internet-culture` | Cultura de internet y redes sociales | cultural | 1995–hoy | global | ★ | `ctx-web` |
| `ctx-design-museums` | Museos de diseño y ciudad-espectáculo | cultural | 1980–hoy | europe, north-america | N | `ctx-globalisation` |
| `ctx-latin-popular-craft` | Artesanía y cultura popular latinoamericana | cultural | 1970–hoy | latin-america | N | `ctx-urban-informality` |
| `ctx-crisis-functionalism` | Crisis del funcionalismo | cultural | 1966–1985 | europe, north-america | ★ | `ctx-postmodern-culture` |
| `ctx-personal-computer` | El computador personal | technological | 1977–hoy | north-america, global | ★ | `ctx-desktop-publishing` |
| `ctx-desktop-publishing` | Autoedición y tipografía digital | technological | 1984–hoy | north-america, europe | ★ | `ctx-personal-computer` |
| `ctx-web` | La web | technological | 1991–hoy | global | ★ | `ctx-internet-culture` |
| `ctx-smartphone` | Teléfono móvil y smartphone | technological | 1990–hoy | global | ★ | `ctx-web` |
| `ctx-microelectronics` | Microelectrónica y miniaturización | technological | 1970–1995 | global | N | `ctx-japan-consumer-economy` |
| `ctx-digital-music` | Música digital portátil | technological | 1995–2010 | global | N | `ctx-smartphone` |
| `ctx-digital-fabrication` | Diseño asistido y fabricación digital | technological | 1980–hoy | global | N | `ctx-personal-computer` |

### Productivo

| id | nombre | sub | años | nivel | relaciona |
|---|---|---|---|---|---|
| `plastic-laminate` | Laminado plástico decorativo | materials | 1981 | N | `memphis`, `ctx-postmodern-culture` |
| `polycarbonate-shell` | Carcasas de policarbonato translúcido | materials | 1998 | N | `ctx-branding` |
| `scrap-materials` | Materiales de desecho y recuperados | materials | 1974–hoy | ★ | `ctx-latin-popular-craft` |
| `recycled-biomaterials` | Materiales reciclados y biomateriales | materials | 1990–hoy | N | `ctx-climate-crisis`, `th-cradle-to-cradle` |
| `postscript` | PostScript | processes | 1985 | ★ | `ctx-desktop-publishing`, `inst-apple` |
| `cad-cam` | Diseño y fabricación asistidos por computador | processes | 1980–hoy | ★ | `ctx-digital-fabrication` |
| `rapid-prototyping` | Prototipado rápido e impresión 3D | processes | 1990–hoy | N | `ctx-digital-fabrication`, `james-dyson` |
| `quick-response` | Cadena de suministro de respuesta rápida | processes | 1975–hoy | N | `inst-zara` |
| `cnc-unibody` | Mecanizado CNC de carcasa única | processes | 2008 | N | `ctx-digital-fabrication`, `jonathan-ive` |
| `pagemaker` | PageMaker y la autoedición | tools | 1985 | N | `ctx-desktop-publishing`, `inst-emigre` |
| `fontographer` | Fontographer y la tipografía digital | tools | 1986 | N | `zuzana-licko`, `ctx-desktop-publishing` |
| `photoshop` | Adobe Photoshop | tools | 1990 | N | `ctx-desktop-publishing`, `david-carson` |
| `multitouch` | Pantalla táctil multitáctil | tools | 2007 | ★ | `ctx-smartphone`, `interaction-design` |
| `web-type-css` | HTML, CSS y tipografía de pantalla | tools | 1991–hoy | N | `ctx-web`, `interaction-design` |

### Teoría

| id | nombre | años | nivel | relaciona |
|---|---|---|---|---|
| `th-rams-ten-principles` | Los diez principios del buen diseño de Dieter Rams | c. 1980 | N | `jonathan-ive`, `ctx-crisis-functionalism` |
| `th-grid-systems` | Grid Systems in Graphic Design (Müller-Brockmann) | 1981 | N | `new-wave-typography`, `ctx-desktop-publishing` |
| `th-design-everyday-things` | The Design of Everyday Things (Norman) | 1988 | ★ | `interaction-design`, `ctx-ageing-accessibility`, `ctx-personal-computer` |
| `th-incomplete-manifesto` | Incomplete Manifesto for Growth (Bruce Mau) | 1998 | N | `ctx-postmodern-culture`, `stefan-sagmeister` |
| `th-first-things-first-2000` | First Things First 2000 | 1999 | ★ | `ctx-branding`, `neville-brody` |
| `th-no-logo` | No Logo (Naomi Klein) | 1999 | ★ | `ctx-branding`, `ctx-globalisation` |
| `th-cradle-to-cradle` | Cradle to Cradle (McDonough y Braungart) | 2002 | N | `sustainable-design`, `ctx-climate-crisis` |
| `th-design-thinking-brown` | «Design Thinking» (Tim Brown) | 2008 | N | `inst-ideo`, `interaction-design` |
| `th-speculative-everything` | Speculative Everything (Dunne y Raby) | 2013 | N | `critical-speculative-design` |

### Movimientos

| id | nombre | años | nivel | relaciona |
|---|---|---|---|---|
| `memphis` | Memphis | 1981–1988 | ★ | `macro-postmodernism`, `inst-memphis-group`, `ctx-crisis-functionalism`, `alchimia` |
| `alchimia` | Alchimia | 1976–1992 | N | `macro-postmodernism`, `alessandro-mendini`, `ctx-crisis-functionalism` |
| `deconstructivism` | Deconstructivismo | 1982–2000 | ★ | `macro-postmodernism`, `frank-gehry`, `zaha-hadid`, `rem-koolhaas` |
| `new-wave-typography` | New Wave y tipografía experimental | 1975–1995 | ★ | `macro-postmodernism`, `inst-emigre`, `ctx-punk` |
| `droog-design` | Droog | 1993–hoy | N | `inst-droog`, `ctx-postmodern-culture` |
| `critical-speculative-design` | Diseño crítico y especulativo | 1990–hoy | N | `ctx-internet-culture` |
| `sustainable-design` | Diseño sostenible | 1990–hoy | N | `ctx-climate-crisis`, `recycled-biomaterials` |
| `interaction-design` | Diseño de interacción y de experiencia | 1984–hoy | ★ | `ctx-web`, `ctx-smartphone`, `inst-ideo` |

### Instituciones

| id | nombre | años | nivel | relaciona |
|---|---|---|---|---|
| `inst-memphis-group` | Grupo Memphis | 1981–1988 | ★ | `ettore-sottsass`, `michele-de-lucchi` |
| `inst-apple` | Apple | 1976–hoy | ★ | `ctx-personal-computer`, `ctx-branding` |
| `inst-ideo` | IDEO | 1991–hoy | N | `interaction-design` |
| `inst-emigre` | Emigre | 1984–2005 | ★ | `zuzana-licko`, `ctx-desktop-publishing` |
| `inst-alessi` | Alessi | 1921–hoy | N | `alessandro-mendini`, `michael-graves`, `philippe-starck` |
| `inst-vitra-design-museum` | Vitra Design Museum | 1989–hoy | N | `ctx-design-museums`, `frank-gehry` |
| `inst-droog` | Droog Design | 1993–hoy | N | `droog-design` |
| `inst-elemental` | Elemental | 2001–hoy | ★ | `alejandro-aravena`, `ctx-urban-informality` |
| `inst-zara` | Zara (Inditex) | 1975–hoy | N | `quick-response` |
| `inst-muji` | Muji | 1980–hoy | N | `ctx-japan-consumer-economy`, `ctx-branding` |
| `inst-frog-design` | frog design | 1969–hoy | N | `hartmut-esslinger`, `inst-apple` |
| `inst-design-museum-london` | Design Museum de Londres | 1989–hoy | N | `ctx-design-museums` |

### Diseñadores

| id | nombre | años | disciplinas | nivel | obras | relaciona |
|---|---|---|---|---|---|---|
| `susan-kare` | Susan Kare | n. 1954 | graphic | ★ | `macintosh-icons-1984`, `kare-chicago-geneva-1984` | `inst-apple` |
| `zuzana-licko` | Zuzana Licko | n. 1961 | graphic | ★ | `emigre-magazine-1984`, `emigre-bitmap-fonts-1985` | `inst-emigre`, `new-wave-typography` |
| `david-carson` | David Carson | n. 1954 | graphic | ★ | `ray-gun-1992` | `new-wave-typography` |
| `neville-brody` | Neville Brody | n. 1957 | graphic | N | `the-face-1981` | `new-wave-typography`, `ctx-punk` |
| `april-greiman` | April Greiman | n. 1948 | graphic | N | `design-quarterly-133-1986` | `new-wave-typography` |
| `paula-scher` | Paula Scher | n. 1948 | graphic | N | `public-theater-identity-1994`, `citibank-logo-1998` | `ctx-branding` |
| `stefan-sagmeister` | Stefan Sagmeister | n. 1962 | graphic | N | `aiga-detroit-poster-1999` | `ctx-postmodern-culture` |
| `shepard-fairey` | Shepard Fairey | n. 1970 | graphic | N | `hope-poster-2008` | `ctx-obama-2008` |
| `equipo-campana-del-no` | Equipo creativo de la campaña del NO | 1988 | graphic | ★ | `franja-del-no-1988` | `ctx-plebiscite-1988` |
| `matthew-carter` | Matthew Carter | n. 1937 | graphic | N | `verdana-1996`, `bell-centennial-1978` | `ctx-web` |
| `michele-de-lucchi` | Michele De Lucchi | n. 1951 | product, architecture | N | `first-chair-1983` | `memphis`, `inst-memphis-group` |
| `alessandro-mendini` | Alessandro Mendini | 1931–2019 | product, architecture | N | `proust-armchair-1978`, `anna-g-corkscrew-1994` | `alchimia`, `inst-alessi` |
| `philippe-starck` | Philippe Starck | n. 1949 | product | ★ | `juicy-salif-1990` | `inst-alessi` |
| `ron-arad` | Ron Arad | n. 1951 | product | N | `well-tempered-chair-1986` | `ctx-postmodern-culture` |
| `marc-newson` | Marc Newson | n. 1963 | product | N | `lockheed-lounge-1986` | `ctx-postmodern-culture` |
| `jasper-morrison` | Jasper Morrison | n. 1959 | product | N | `air-chair-1999` | `inst-muji` |
| `jonathan-ive` | Jonathan Ive | n. 1967 | product | ★ | `imac-1998`, `ipod-2001`, `iphone-2007`, `macbook-air-2008` | `inst-apple`, `th-rams-ten-principles` |
| `hartmut-esslinger` | Hartmut Esslinger | n. 1944 | product | N | `apple-iic-1984` | `inst-frog-design`, `inst-apple` |
| `james-dyson` | James Dyson | n. 1947 | product | N | `dyson-dc01-1993` | `rapid-prototyping` |
| `hermanos-campana` | Fernando y Humberto Campana | n. 1961 y 1953 | product | ★ | `favela-chair-1991`, `vermelha-chair-1998`, `banquete-chair-2006` | `scrap-materials`, `ctx-latin-popular-craft` |
| `vivienne-westwood` | Vivienne Westwood | 1941–2022 | fashion | N | `westwood-punk-1976`, `westwood-pirates-1981` | `ctx-punk` |
| `martin-margiela` | Martin Margiela | n. 1957 | fashion | N | `margiela-tabi-1988` | `deconstructivism` |
| `alexander-mcqueen` | Alexander McQueen | 1969–2010 | fashion | N | `mcqueen-highland-rape-1995`, `mcqueen-skull-scarf-2003`, `mcqueen-plato-atlantis-2010` | `ctx-internet-culture` |
| `rei-kawakubo` | Rei Kawakubo | n. 1942 | fashion | ★ | `paris-debut-1981` | `ctx-japan-consumer-economy` |
| `yohji-yamamoto` | Yohji Yamamoto | n. 1943 | fashion | ★ | `paris-debut-1981` | `ctx-japan-consumer-economy` |
| `jean-paul-gaultier` | Jean Paul Gaultier | n. 1952 | fashion | N | `gaultier-cone-bra-1990` | `ctx-feminisms` |
| `arpilleristas` | Arpilleristas chilenas | 1974–1990 | fashion | ★ | `arpilleras-1974` | `ctx-human-rights-resistance` |
| `alejandro-aravena` | Alejandro Aravena | n. 1967 | architecture | ★ | `quinta-monroy-2004`, `villa-verde-2013`, `torres-siamesas-2005` | `inst-elemental` |
| `paulo-mendes-da-rocha` | Paulo Mendes da Rocha | 1928–2021 | architecture | N | `mube-1988` | `ctx-urban-informality` |
| `rogelio-salmona` | Rogelio Salmona | 1927–2007 | architecture | N | `biblioteca-virgilio-barco-2001` | `ctx-latin-popular-craft` |
| `smiljan-radic` | Smiljan Radic | n. 1965 | architecture | N | `mestizo-restaurant-2007` | `ctx-chile-market-economy` |
| `frank-gehry` | Frank Gehry | n. 1929 | architecture | ★ | `gehry-house-1978`, `vitra-design-museum-1989`, `guggenheim-bilbao-1997`, `walt-disney-hall-2003` | `deconstructivism`, `inst-vitra-design-museum` |
| `zaha-hadid` | Zaha Hadid | 1950–2016 | architecture | N | `vitra-fire-station-1993` | `deconstructivism` |
| `michael-graves` | Michael Graves | 1934–2015 | architecture, product | N | `portland-building-1982`, `humana-building-1985`, `kettle-9093-1985` | `inst-alessi`, `macro-postmodernism` |
| `rem-koolhaas` | Rem Koolhaas | n. 1944 | architecture | N | `seattle-library-2004`, `kunsthal-rotterdam-1992` | `deconstructivism` |

### Obras

| id | título | disciplina | año | nivel | diseñadores | tech | regiones | contextos |
|---|---|---|---|---|---|---|---|---|
| `macintosh-icons-1984` | Íconos del Macintosh | graphic | 1984 | ★ | `susan-kare` | | north-america, global | `ctx-personal-computer`: la pantalla de mapa de bits obligó a dibujar cada ícono píxel por píxel en una grilla; `ctx-branding`: Apple necesitaba una cara amable para vender el computador a quienes no eran especialistas |
| `kare-chicago-geneva-1984` | Tipografías Chicago y Geneva | graphic | 1984 | N | `susan-kare` | | north-america | `ctx-desktop-publishing`: las fuentes de mapa de bits del Mac fueron las primeras tipografías de sistema que veía el gran público |
| `i-love-ny-1977` | Logotipo I ♥ NY | graphic | 1977 | ★ | `milton-glaser` | | north-america | `ctx-nyc-fiscal-crisis`: la ciudad en quiebra usó una campaña de marca para atraer turistas y levantar ánimo; `ctx-branding`: abrió el camino a la ciudad entendida como marca; `ctx-postmodern-culture`: el corazón y la tipografía de máquina de escribir citan lenguaje cotidiano y popular |
| `emigre-magazine-1984` | Revista Emigre | graphic | 1984 | ★ | `zuzana-licko` | `pagemaker` | north-america | `ctx-desktop-publishing`: se compuso con computadores Macintosh, sin fotocomposición profesional; `ctx-postmodern-culture`: la revista mezcló tipografía, crítica y arte con una estética deliberadamente híbrida |
| `emigre-bitmap-fonts-1985` | Tipografías de mapa de bits de Emigre | graphic | 1985 | N | `zuzana-licko` | `fontographer` | north-america | `ctx-desktop-publishing`: las limitaciones de la resolución de pantalla y de la impresora se convirtieron en la forma de las letras |
| `ray-gun-1992` | Revista Ray Gun | graphic | 1992 | ★ | `david-carson` | `postscript`, `photoshop` | north-america | `ctx-desktop-publishing`: la composición digital permitió superponer y distorsionar texto sin pasar por el taller; `ctx-mtv-club`: la revista hablaba el idioma visual de la música alternativa |
| `the-face-1981` | Revista The Face | graphic | 1981 | N | `neville-brody` | | europe | `ctx-punk`: la revista tradujo la energía visual del pospunk y la cultura de club a la página; `ctx-mtv-club`: la cultura de club británica era su público |
| `design-quarterly-133-1986` | Design Quarterly 133 (Greiman) | graphic | 1986 | N | `april-greiman` | `postscript` | north-america | `ctx-desktop-publishing`: un póster plegado de casi dos metros compuesto en un Macintosh con imagen digital |
| `public-theater-identity-1994` | Identidad del Public Theater | graphic | 1994 | N | `paula-scher` | | north-america | `ctx-branding`: una institución cultural adoptó una identidad tipográfica ruidosa y reconocible como marca |
| `citibank-logo-1998` | Logotipo de Citibank | graphic | 1998 | N | `paula-scher` | | north-america | `ctx-branding`: la fusión de Citicorp y Travelers pidió una marca unificada para un banco global; `ctx-globalisation`: el banco operaba en muchos países |
| `aiga-detroit-poster-1999` | Póster de la conferencia AIGA Detroit | graphic | 1999 | N | `stefan-sagmeister` | | north-america | `ctx-postmodern-culture`: el diseñador convirtió su propio cuerpo en soporte gráfico y puso el proceso a la vista |
| `hope-poster-2008` | Cartel Hope | graphic | 2008 | ★ | `shepard-fairey` | | north-america | `ctx-obama-2008`: el cartel nació como apoyo a la candidatura y se volvió su imagen más reproducida; `ctx-internet-culture`: se difundió por redes y correos más que por imprenta |
| `franja-del-no-1988` | Franja y logotipo del NO | graphic | 1988 | ★ | `equipo-campana-del-no` | | latin-america | `ctx-plebiscite-1988`: la franja televisiva de 15 minutos debía convencer en pocas semanas al electorado; `ctx-chile-dictatorship`: el miedo y el silencio de 15 años obligaron a una comunicación alegre; `ctx-chile-market-economy`: usó el lenguaje publicitario del consumo |
| `patagonia-dont-buy-this-jacket-2011` | Aviso «Don't Buy This Jacket» de Patagonia | graphic | 2011 | N | | | north-america | `ctx-crisis-2008`: tras la crisis, el aviso cuestionó el consumo en pleno Black Friday; `ctx-climate-crisis`: pidió comprar menos y reparar |
| `first-website-1991` | Primer sitio web del CERN | graphic | 1991 | ★ | | `web-type-css` | europe, global | `ctx-web`: era la primera página de hipertexto accesible en una red; `ctx-internet-culture`: de ahí se desprende la cultura de publicar y enlazar |
| `verdana-1996` | Tipografía Verdana | graphic | 1996 | N | `matthew-carter` | `web-type-css` | north-america, global | `ctx-web`: se diseñó para leerse bien a tamaños pequeños en pantallas de baja resolución |
| `bell-centennial-1978` | Tipografía Bell Centennial | graphic | 1978 | N | `matthew-carter` | | north-america | `ctx-microelectronics`: la composición electrónica de guías telefónicas en gran escala y con papel barato exigió letras que resistieran la impresión de baja calidad |
| `think-different-1997` | Campaña «Think Different» de Apple | graphic | 1997 | N | | | north-america | `ctx-branding`: la campaña vendió una actitud, no un producto, para reflotar la marca; `ctx-personal-computer`: Apple competía contra la hegemonía de los PC |
| `material-design-2014` | Material Design de Google | graphic | 2014 | N | | `web-type-css` | north-america, global | `ctx-smartphone`: unificó la interfaz en pantallas pequeñas y táctiles de distintos tamaños; `ctx-platform-economy`: ordenó el diseño de los servicios de una plataforma global |
| `mtv-logo-1981` | Logotipo de MTV | graphic | 1981 | ★ | | | north-america | `ctx-mtv-club`: la M monumental con logo cambiante expresaba un canal sin identidad fija; `ctx-branding`: fue uno de los primeros logos concebidos como marco variable |
| `wired-magazine-1993` | Revista Wired | graphic | 1993 | N | | | north-america | `ctx-internet-culture`: dio forma visual a la cultura digital naciente con colores fluorescentes; `ctx-desktop-publishing`: su maquetación explotaba capas y tintas planas de la composición digital |
| `carlton-bookcase-1981` | Librero Carlton | product | 1981 | N | `ettore-sottsass` | `plastic-laminate` | europe | `ctx-crisis-functionalism`: rechazó la sobriedad funcionalista con colores, patrones y una forma antropomórfica; `ctx-postmodern-culture`: mezcló kitsch y referencias populares; `ctx-branding`: Memphis se presentó en Milán como colección-marca con fuerte eco mediático |
| `first-chair-1983` | Silla First | product | 1983 | N | `michele-de-lucchi` | | europe | `ctx-crisis-functionalism`: formas geométricas y colores desconectados de la lógica funcional de la silla moderna |
| `proust-armchair-1978` | Sillón Proust | product | 1978 | N | `alessandro-mendini` | | europe | `ctx-postmodern-culture`: Mendini «redecoró» un sillón histórico con un puntillismo pictórico, como cita irónica |
| `kettle-9093-1985` | Tetera 9093 | product | 1985 | ★ | `michael-graves` | | north-america, europe | `ctx-branding`: Alessi vendió un objeto de diseño de autor que también era emblema de marca; `ctx-crisis-functionalism`: la figura del pájaro del silbato humaniza el objeto |
| `anna-g-corkscrew-1994` | Sacacorchos Anna G | product | 1994 | N | `alessandro-mendini` | | europe | `ctx-branding`: el objeto antropomórfico fue un producto de catálogo masivo con valor emocional |
| `juicy-salif-1990` | Exprimidor Juicy Salif | product | 1990 | ★ | `philippe-starck` | | europe | `ctx-branding`: más escultura que utensilio, convirtió el producto en marca de autor; `ctx-postmodern-culture`: pone la imagen por sobre la función |
| `well-tempered-chair-1986` | Silla Well Tempered | product | 1986 | N | `ron-arad` | | europe | `ctx-postmodern-culture`: una silla de acero laminado doblado a mano, entre obra única y producto |
| `lockheed-lounge-1986` | Lockheed Lounge | product | 1986 | N | `marc-newson` | | europe, global | `ctx-postmodern-culture`: remachó paneles de aluminio sobre una forma fluida al estilo de un fuselaje |
| `air-chair-1999` | Silla Air-Chair | product | 1999 | N | `jasper-morrison` | `injection-moulding` | europe | `ctx-globalisation`: una silla plástica inyectada, ligera y apilable para un mercado europeo y global |
| `swatch-1983` | Reloj Swatch | product | 1983 | ★ | | `injection-moulding` | europe, global | `ctx-microelectronics`: un reloj de cuarzo con pocas piezas de plástico se podía fabricar barato; `ctx-branding`: ediciones y colores lo volvieron objeto de moda y colección |
| `apple-iic-1984` | Apple IIc | product | 1984 | N | `hartmut-esslinger` | `injection-moulding` | north-america | `ctx-personal-computer`: llevó el computador al hogar con una carcasa compacta; `ctx-branding`: el lenguaje Snow White definió una identidad de producto |
| `imac-1998` | iMac | product | 1998 | ★ | `jonathan-ive` | `polycarbonate-shell` | north-america, global | `ctx-personal-computer`: lo hizo accesible al consumidor doméstico con conexión a internet; `ctx-branding`: color y translucidez devolvieron a Apple a la cultura popular |
| `ipod-2001` | iPod | product | 2001 | ★ | `jonathan-ive` | | north-america, global | `ctx-digital-music`: miles de canciones en un reproductor de bolsillo con una interfaz simple; `ctx-microelectronics`: discos duros diminutos hicieron posible el tamaño; `ctx-branding`: los auriculares blancos y la campaña lo volvieron emblema de marca |
| `iphone-2007` | iPhone | product | 2007 | ★ | `jonathan-ive` | `multitouch` | north-america, global | `ctx-smartphone`: unió teléfono, internet y música en una sola pantalla táctil; `ctx-globalisation`: se diseña en California y se ensambla en China; `ctx-platform-economy`: la App Store creó un mercado para terceros |
| `macbook-air-2008` | MacBook Air | product | 2008 | N | `jonathan-ive` | `cnc-unibody` | north-america, global | `ctx-digital-fabrication`: la carcasa de aluminio mecanizada por CNC redujo piezas y grosor |
| `sony-walkman-1979` | Sony Walkman TPS-L2 | product | 1979 | ★ | | | global | `ctx-microelectronics`: la miniaturización de casete y amplificador permitió un reproductor personal; `ctx-japan-consumer-economy`: la industria japonesa de electrónica de consumo exportaba a todo el mundo |
| `dyson-dc01-1993` | Aspiradora Dyson DC01 | product | 1993 | N | `james-dyson` | | europe | `ctx-ageing-accessibility`: la bolsa transparente mostró el polvo y el diseño visible pasó a ser argumento de venta; `ctx-branding`: la tecnología ciclónica se vendió como seña de marca |
| `oxo-good-grips-1990` | Utensilios OXO Good Grips | product | 1990 | N | | | north-america | `ctx-ageing-accessibility`: se pensaron para manos con artritis y terminaron siendo mejores para todos |
| `fairphone-2013` | Fairphone | product | 2013 | N | | `recycled-biomaterials` | europe | `ctx-climate-crisis`: apostó por materiales de origen rastreable, reparación y vida útil larga; `ctx-smartphone`: respondió al modelo de reemplazo anual |
| `favela-chair-1991` | Silla Favela | product | 1991 | ★ | `hermanos-campana` | `scrap-materials` | latin-america, global | `ctx-urban-informality`: remedó la autoconstrucción con retazos de madera de las favelas; `ctx-latin-popular-craft`: el diseño partió de las técnicas manuales populares |
| `vermelha-chair-1998` | Silla Vermelha | product | 1998 | N | `hermanos-campana` | | latin-america, global | `ctx-latin-popular-craft`: una cuerda enrollada a mano sobre una estructura metálica |
| `banquete-chair-2006` | Silla Banquete | product | 2006 | N | `hermanos-campana` | `scrap-materials` | latin-america, global | `ctx-latin-popular-craft`: cubierta de peluches de segunda mano, une juguete popular y objeto de galería |
| `arpilleras-1974` | Arpilleras chilenas | fashion | 1974 | ★ | `arpilleristas` | `scrap-materials` | latin-america | `ctx-human-rights-resistance`: mujeres bordaron en retazos denuncias y escenas de la vida bajo la dictadura; `ctx-chile-dictatorship`: la represión y la cesantía llevaron a coser en talleres de la Vicaría de la Solidaridad; `ctx-feminisms`: el trabajo textil colectivo dio voz pública a mujeres |
| `westwood-punk-1976` | Ropa punk de Westwood y McLaren | fashion | 1976 | N | `vivienne-westwood` | | europe | `ctx-punk`: camisetas con consignas, alfileres y cortes rotos expresaron la rabia juvenil; `ctx-postmodern-culture`: se apropió de símbolos y los desacralizó con ironía; `ctx-nyc-fiscal-crisis`: Londres y Nueva York compartían ciudades en crisis |
| `westwood-pirates-1981` | Colección Pirates de Westwood | fashion | 1981 | N | `vivienne-westwood` | | europe | `ctx-postmodern-culture`: citó trajes históricos como pastiche teatral; `ctx-punk`: dejó el escándalo por una moda de referencia |
| `margiela-tabi-1988` | Bota Tabi de Margiela | fashion | 1988 | N | `martin-margiela` | | europe | `ctx-postmodern-culture`: citó el calzado japonés de dedo dividido y lo descontextualizó en la moda parisina |
| `mcqueen-highland-rape-1995` | Highland Rape de McQueen | fashion | 1995 | N | `alexander-mcqueen` | | europe | `ctx-postmodern-culture`: llevó el desfile a un terreno teatral, polémico y narrativo |
| `mcqueen-skull-scarf-2003` | Pañuelo de calaveras de McQueen | fashion | 2003 | N | `alexander-mcqueen` | | europe, global | `ctx-branding`: un estampado simple se volvió accesorio emblemático de una marca de lujo; `ctx-globalisation`: viajó a todos los mercados del lujo |
| `mcqueen-plato-atlantis-2010` | Plato's Atlantis de McQueen | fashion | 2010 | N | `alexander-mcqueen` | | europe | `ctx-internet-culture`: el desfile se transmitió en vivo por internet; `ctx-digital-fabrication`: los estampados se generaron con imágenes digitales |
| `paris-debut-1981` | Debut parisino de Kawakubo y Yamamoto | fashion | 1981 | ★ | `rei-kawakubo`, `yohji-yamamoto` | | global | `ctx-japan-consumer-economy`: el auge de las marcas de moda en Japón financió el salto a París; `ctx-postmodern-culture`: negro, asimetría y prendas rasgadas desafiaron las reglas del vestir occidental; `ctx-globalisation`: moda de origen japonés que cambió el gusto europeo |
| `gaultier-cone-bra-1990` | Corsé de conos de Gaultier | fashion | 1990 | ★ | `jean-paul-gaultier` | | europe, north-america | `ctx-feminisms`: sacó la ropa interior a la vista y jugó con roles de género; `ctx-mtv-club`: la gira de Madonna lo difundió por televisión |
| `nike-air-max-1987` | Zapatillas Nike Air Max 1 | fashion | 1987 | N | | `injection-moulding` | north-america, global | `ctx-branding`: la cámara de aire visible se convirtió en seña de marca; `ctx-globalisation`: producción en Asia para un mercado mundial |
| `air-jordan-1-1985` | Zapatillas Air Jordan 1 | fashion | 1985 | N | | | north-america, global | `ctx-branding`: ligó una zapatilla a la figura de un deportista y se volvió producto de coleccionista; `ctx-mtv-club`: la televisión amplificó el culto |
| `prada-nylon-backpack-1984` | Mochila de nailon de Prada | fashion | 1984 | N | | | europe | `ctx-branding`: un material utilitario sin ornamento se transformó en objeto de lujo con logo; `ctx-postmodern-culture`: invirtió la jerarquía de materiales nobles y humildes |
| `patagonia-synchilla-1985` | Polar Synchilla de Patagonia | fashion | 1985 | N | | `recycled-biomaterials` | north-america | `ctx-climate-crisis`: más tarde la fibra se fabricó con botellas plásticas recicladas; `ctx-branding`: ropa técnica convertida en señal de identidad |
| `quinta-monroy-2004` | Quinta Monroy | architecture | 2004 | ★ | `alejandro-aravena` | | latin-america | `ctx-urban-informality`: reemplazó un campamento en Iquique con casas que los vecinos podían ampliar; `ctx-chile-market-economy`: ajustó el diseño al valor del subsidio estatal de vivienda; `ctx-neoliberalism`: el Estado subsidiaba la demanda en vez de construir directo |
| `villa-verde-2013` | Villa Verde, Constitución | architecture | 2013 | N | `alejandro-aravena` | | latin-america | `ctx-urban-informality`: repitió el modelo de la media casa construida con vecinos; `ctx-chile-market-economy`: se financió con subsidio |
| `torres-siamesas-2005` | Torres Siamesas de la UC | architecture | 2005 | N | `alejandro-aravena` | | latin-america | `ctx-chile-market-economy`: una universidad privada de elite encargó un edificio emblema para su campus |
| `sesc-pompeia-1986` | SESC Pompéia | architecture | 1986 | N | `lina-bo-bardi` | | latin-america | `ctx-latin-popular-craft`: conservó la fábrica y sumó pasarelas y fuegos de cultura popular; `ctx-urban-informality`: abrió un centro de ocio y cultura para clases populares de São Paulo; `ctx-crisis-functionalism`: rehabilitó un edificio industrial sin borrar su historia |
| `teatro-oficina-1984` | Teatro Oficina | architecture | 1984 | N | `lina-bo-bardi` | | latin-america | `ctx-latin-popular-craft`: un teatro como calle cubierta, con un lenguaje material austero y popular |
| `mube-1988` | Museo Brasileño de la Escultura (MuBE) | architecture | 1988 | N | `paulo-mendes-da-rocha` | | latin-america | `ctx-urban-informality`: una gran losa de hormigón libera el terreno para el espacio público de la ciudad |
| `biblioteca-virgilio-barco-2001` | Biblioteca Virgilio Barco | architecture | 2001 | N | `rogelio-salmona` | | latin-america | `ctx-latin-popular-craft`: ladrillo a la vista y trabajo manual en un edificio público de Bogotá |
| `mestizo-restaurant-2007` | Restaurante Mestizo | architecture | 2007 | N | `smiljan-radic` | | latin-america | `ctx-chile-market-economy`: un encargo privado en un parque público como pieza arquitectónica de autor |
| `portland-building-1982` | Edificio Portland | architecture | 1982 | N | `michael-graves` | | north-america | `ctx-crisis-functionalism`: respondió con color, columnas y guirnaldas a la caja de vidrio; `ctx-postmodern-culture`: citó la historia como ornamento en un edificio público; `ctx-neoliberalism`: la ciudad quería un edificio con imagen propia para competir por inversión |
| `humana-building-1985` | Edificio Humana | architecture | 1985 | N | `michael-graves` | | north-america | `ctx-branding`: una torre corporativa pensada como imagen urbana de la empresa |
| `guggenheim-bilbao-1997` | Museo Guggenheim Bilbao | architecture | 1997 | ★ | `frank-gehry` | `cad-cam` | europe | `ctx-digital-fabrication`: el software CATIA permitió modelar y construir las curvas de titanio; `ctx-design-museums`: la ciudad industrial en declive apostó a un museo como motor turístico; `ctx-globalisation`: la fundación exportó su marca museística |
| `walt-disney-hall-2003` | Walt Disney Concert Hall | architecture | 2003 | N | `frank-gehry` | `cad-cam` | north-america | `ctx-digital-fabrication`: las superficies de acero se resolvieron con modelado digital |
| `gehry-house-1978` | Casa de Gehry en Santa Mónica | architecture | 1978 | N | `frank-gehry` | | north-america | `ctx-crisis-functionalism`: rodeó una casa existente con malla, madera cruda y metal acanalado en vez de ocultar lo cotidiano; `ctx-postmodern-culture`: valoró materiales baratos como lenguaje |
| `vitra-design-museum-1989` | Vitra Design Museum | architecture | 1989 | N | `frank-gehry` | | europe | `ctx-design-museums`: un museo de autor para una colección de diseño industrial |
| `vitra-fire-station-1993` | Estación de bomberos de Vitra | architecture | 1993 | N | `zaha-hadid` | | europe | `ctx-postmodern-culture`: ángulos y planos agudos como gesto escultórico dentro de una fábrica |
| `seattle-library-2004` | Biblioteca Central de Seattle | architecture | 2004 | N | `rem-koolhaas` | `cad-cam` | north-america | `ctx-digital-fabrication`: la estructura facetada de vidrio y acero se trabajó con software; `ctx-internet-culture`: la biblioteca se repensó como lugar de múltiples medios |
| `kunsthal-rotterdam-1992` | Kunsthal de Rotterdam | architecture | 1992 | N | `rem-koolhaas` | | europe | `ctx-postmodern-culture`: mezcla de materiales y recorridos como collage urbano |

### Conexiones

| from | to | línea |
|---|---|---|
| `macintosh-icons-1984` | `emigre-bitmap-fonts-1985` | La grilla de píxeles de los íconos del Mac enseñó a dibujar letras con la misma limitación de pantalla. |
| `emigre-magazine-1984` | `ray-gun-1992` | Emigre mostró que se podía componer y distorsionar texto en el computador, y Carson llevó esa libertad al público de revistas de música. |
| `carlton-bookcase-1981` | `first-chair-1983` | Ambas piezas de Memphis comparten laminados de colores y formas geométricas sin función evidente, mostrando el mismo rechazo al funcionalismo. |
| `proust-armchair-1978` | `carlton-bookcase-1981` | La ironía decorativa de Alchimia preparó el terreno para el vocabulario de color y pastiche de Memphis. |
| `portland-building-1982` | `kettle-9093-1985` | Graves llevó el mismo vocabulario de color y figuras simbólicas de su arquitectura a un objeto doméstico de Alessi. |
| `gehry-house-1978` | `guggenheim-bilbao-1997` | La estética de fragmentos y materiales crudos de la casa se retomó, con modelado digital, en las superficies del museo. |
| `imac-1998` | `ipod-2001` | El éxito del iMac devolvió a Apple los recursos y la confianza para desarrollar un reproductor de música propio. |
| `ipod-2001` | `iphone-2007` | La rueda y la interfaz simple del iPod se transformaron en la pantalla táctil que reunió música, teléfono e internet. |
| `apple-iic-1984` | `imac-1998` | La idea de un computador doméstico con identidad de producto propia pasó del Snow White de frog al color y la translucidez del iMac. |
| `sony-walkman-1979` | `ipod-2001` | El hábito de llevar la música propia por la calle, creado por el Walkman, fue el terreno cultural del reproductor digital. |
| `paris-debut-1981` | `margiela-tabi-1988` | El desfile de los japoneses abrió París a la deconstrucción de la prenda que Margiela desarrolló después. |
| `westwood-punk-1976` | `mcqueen-highland-rape-1995` | La provocación teatral del punk londinense fue herencia directa para el escándalo calculado de los desfiles de McQueen. |
| `favela-chair-1991` | `banquete-chair-2006` | Los Campana pasaron de los retazos de madera a otros materiales descartados, conservando la misma forma de trabajo manual. |
| `quinta-monroy-2004` | `villa-verde-2013` | Elemental repitió y afinó en Constitución la fórmula de media casa ampliable de Iquique. |
| `arpilleras-1974` | `franja-del-no-1988` | La resistencia civil expresada en arpilleras y otras formas de testimonio preparó el clima social del plebiscito. |
| `ray-gun-1992` | `th-first-things-first-2000` | La tipografía experimental de los noventa convivió con el debate sobre la responsabilidad social del diseñador gráfico. |
| `i-love-ny-1977` | `think-different-1997` | La idea de convertir un lema en marca ampliamente reconocible reapareció en campañas corporativas de identidad. |
| `swatch-1983` | `fairphone-2013` | El reloj popular mostró que un objeto electrónico podía venderse como moda; el Fairphone invirtió esa lógica para pedir uso prolongado. |
| `th-design-everyday-things` | `iphone-2007` | La insistencia de Norman en que el objeto debe mostrar cómo se usa se refleja en la interfaz táctil. |
| `verdana-1996` | `material-design-2014` | La preocupación por la legibilidad en pantalla pasó de las tipografías web a los sistemas de interfaz de Google. |

### Reserva

| id | tipo | nombre | motivo |
|---|---|---|---|
| `ctx-covid-2020` | contexts | Pandemia de COVID-19 | Evento reciente, aún sin canon de obras asentado |
| `ctx-generative-ai` | contexts | IA generativa | Posterior a 2022; sin consenso sobre obras |
| `ctx-kyoto-paris` | contexts | Kioto 1997 y Acuerdo de París | Se podría separar de la crisis climática |
| `ctx-september-11` | contexts | 11 de septiembre de 2001 | Sin obra clara de diseño que lo requiera |
| `ctx-arab-spring` | contexts | Primavera Árabe | Fuera de Occidente sin influencia demostrada en diseño |
| `lego-bricks-system` | production | Moldeo de precisión de piezas modulares | Dudas de fecha para el tramo |
| `laser-cutting` | production | Corte láser | Menos influyente que CAD/CAM |
| `th-complexity-contradiction` | theories | Learning from Las Vegas | Pertenece a Posguerra (1972) |
| `inst-pentagram` | institutions | Pentagram | Se podría sumar con Paula Scher |
| `inst-design-council-chile` | institutions | Instituciones chilenas de diseño | Faltan datos seguros |
| `wolfgang-weingart` | designers | Wolfgang Weingart | Sin obra con fecha segura |
| `oliviero-toscani` | designers | Oliviero Toscani | Campañas de Benetton, duda de fechas |
| `issey-miyake` | designers | Issey Miyake | Se evita sobrepasar el límite de elementos fuera de Occidente |
| `miuccia-prada` | designers | Miuccia Prada | Sin obra con atribución segura |
| `hella-jongerius` | designers | Hella Jongerius | Sin espacio en el cupo de diseñadores |
| `naoto-fukasawa` | designers | Naoto Fukasawa | Solo con Muji, límite de fuera de Occidente |
| `nintendo-game-boy-1989` | works | Game Boy de Nintendo | Cupo de fuera de Occidente |
| `rag-chair-1991` | works | Rag Chair de Tejo Remy | Sin diseñador en lista |
| `pompidou-1977` | works | Centro Pompidou | Pertenece a Posguerra |
| `piazza-d-italia-1978` | works | Plaza de Italia, Nueva Orleans | Sin diseñador en lista |
| `bosco-verticale-2014` | works | Bosco Verticale | Obra reciente, sin diseñador en lista |
| `casa-poli-2005` | works | Casa Poli | Sin diseñador en lista |
| `pavilion-chile-seville-1992` | works | Pabellón de Chile en Sevilla | Sin diseñador en lista |
| `windows-95-1995` | works | Interfaz de Windows 95 | Sin diseñador en lista |
| `muji-cd-player-1999` | works | Reproductor de CD de pared de Muji | Cupo de fuera de Occidente |
| `miyake-pleats-please-1993` | works | Pleats Please | Cupo de fuera de Occidente |
| `margiela-replica-1994` | works | Colección Replica | Dudas de fecha |
| `ctx-fall-berlin-wall` | contexto | Caída del Muro de Berlín | v37: ningún elemento del tramo se explica por él con mecanismo cierto |
| `ctx-fast-fashion` | contexto | Moda rápida | v37: ningún elemento del tramo se explica por él con mecanismo cierto |
