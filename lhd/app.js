/* LHD — Línea de Historia del Diseño. Timeline app (no dependencies). */
(() => {
  'use strict';

  // ---------- Configuration ----------
  const CFG = window.LHD_CONFIG || {};

  const TRACKS = ['political', 'economic', 'social', 'cultural', 'technological'];
  const PSUBS = ['materials', 'processes', 'tools'];
  const DISCS = ['graphic', 'product', 'fashion', 'architecture'];
  const REGIONS = ['europe', 'north-america', 'latin-america'];
  const TYPES = ['movements', 'institutions', 'theory', 'designers', 'works'];
  const LEVELS = ['essential', 'normal'];   // v24: two detail levels (cumulative); essential = ★ (the old «complete» was merged into normal)
  const LEVEL_RANK = { essential: 0, normal: 1, complete: 1 };
  // marker shape by discipline: graphic = circle, product = diamond, fashion = triangle, architecture = square
  const GLYPH = {
    graphic: 'M1,5 A4,4 0 1,0 9,5 A4,4 0 1,0 1,5 Z',
    product: 'M5,0.6 L9.4,5 L5,9.4 L0.6,5 Z',
    fashion: 'M5,0.8 L9.6,9 L0.4,9 Z',
    architecture: 'M1.2,1.2 H8.8 V8.8 H1.2 Z'
  };
  const STAR = 'M5,0.3 L6.2,3.6 L9.7,3.7 L6.9,5.8 L7.9,9.2 L5,7.2 L2.1,9.2 L3.1,5.8 L0.3,3.7 L3.8,3.6 Z';
  // small 11 px icons of the kinds of institution
  const INST_ICON = {
    school: 'M5.5,1.5 L10.5,4 L5.5,6.5 L0.5,4 Z M2.5,5.4 V8 C4,9.2 7,9.2 8.5,8 V5.4',
    company: 'M1,9.5 V4.5 L4,6.5 V4.5 L7,6.5 V2 H9 V9.5 Z',
    studio: 'M1.5,9.5 L2,7 L7.8,1.2 L9.8,3.2 L4,9 Z M6.6,2.4 L8.6,4.4',
    exhibition: 'M1.5,2 H9.5 V8 H1.5 Z M3.5,9.5 H7.5 M5.5,8 V9.5',
    association: 'M3.8,4.2 A1.6,1.6 0 1,0 3.8,1 A1.6,1.6 0 1,0 3.8,4.2 Z M8,5 A1.4,1.4 0 1,0 8,2.2 A1.4,1.4 0 1,0 8,5 Z M0.8,9.5 C0.8,6.5 6.8,6.5 6.8,9.5 M6.6,7.2 C8.4,6.5 10.2,7.6 10.2,9.5',
    museum: 'M0.8,4 L5.5,1 L10.2,4 Z M2,5 V8.3 M4.2,5 V8.3 M6.8,5 V8.3 M9,5 V8.3 M0.8,9.5 H10.2',
    publication: 'M1,2 C3,1.2 4.6,1.4 5.5,2.4 C6.4,1.4 8,1.2 10,2 V8.8 C8,8 6.4,8.2 5.5,9.2 C4.6,8.2 3,8 1,8.8 Z M5.5,2.4 V9.2'
  };
  const PADL = 16, PADR = 90, LINE_START = 1750;
  const LONG_YEARS = 30, LONG_FRAC = 0.75;   // a bar longer than this (years, or share of the visible width) is drawn as point + label + arrow
  const LOD_MID = 4, LOD_NEAR = 12;         // local pixels per year from which more detail and labels appear
  const MAX_LOCAL_PX = 60;                  // maximum zoom: pixels per year in the most stretched decade

  const UI = {
    en: {
      title: 'Design History Timeline', searchLbl: 'Search the timeline', search: 'Search works, designers, movements, institutions, context…', loading: 'Loading…', close: 'Close', noMatch: 'No matches.', langBtn: 'ES', langTitle: 'Ver en español',
      themeToDark: 'Dark theme', themeToLight: 'Light theme', expand: 'Expand', collapse: 'Collapse', openCtx: 'Open all context rows', closeCtx: 'Close all context rows', openDes: 'Open all design rows', closeDes: 'Close all design rows',
      mobileTitle: 'Desktop only', mobileMsg: 'This timeline can only be viewed on a desktop or laptop computer. Please open it on a larger screen.',
      helpBtn: 'Help', helpTitle: 'How to use the timeline',
      help: {
        lead: 'An interactive timeline of design history: one continuous line from 1750 to today. Design (movements, institutions, designers and works) sits under the context facts that explain it.',
        h1: 'The parts of the site', f1: 'The main areas of the site',
        parts: [['Top bar', 'Search, light or dark theme, language, the presentation (i) and this help. In edit mode it also has the review summary.'], ['Filters', 'Lens: each button reads the line from one kind of context (political, economic, social, cultural, technological, productive or theoretical): its facts and the design connected to them stay, the rest is hidden, the card explains that view, and the curves come on. Click it again to turn it off. Connections shows or hides the curves. Disciplines sets the scope on one discipline (one at a time, combinable with a lens): its works and the design and context connected to it stay, and the card tells its history as an essay with links; another click removes it. Detail chooses how much design is shown: must-know ★ or normal (the default, everything); context is always shown, and going to an element that is not must-know switches to normal. Arrange orders the design by category (movements, institutions, designers), by date (one row per element, sorted by start year), by discipline (four groups; a designer working in several disciplines appears in each, with only the works of that discipline) or by region (split into cultural zones). Show picks the kinds of element. Scale switches between “visual” (busy decades are wider) and “chronological” (every year the same width). The “Only:” chip undoes the filter of a card.'], ['Year axis', 'Above the years, the time minimap shows the whole line and, between brackets, the part you see: drag a bracket to change the start or the end, drag the window to move, or click elsewhere to go there. Drag on the years to zoom to a span (the span is shaded down the whole line). Near the ends, the ‹ › arrows add years on that side (hold to keep going). In the “visual” scale, the zigzag marks show where the scale changes.'], ['Visible years', 'The two boxes (first and last year): type a year and press Enter. “All” shows the whole line again, and “Fit” fits the years to what is shown now (filters, lens, “Only”). The double arrow to the left of CONTEXT and DESIGN works like the small arrows: ⌄⌄ means something is open and a click closes all its rows and groups; ›› means all is closed and a click opens them (with a lens on, CONTEXT only acts on the lens row).'], ['Rows', 'Click the name of a context row to turn on its lens; the small arrow opens or closes the row. The design has no folding rows: what is shown is chosen in Show, and how it is ordered in Arrange. The macro-movements (Modernism, Postmodernism) go first in the Movements row: click one to read its overview.'], ['Card', 'Details of the selected item, or the active lens when nothing is selected.']],
        h2: 'Moving and zooming',
        move: ['<b>Scroll:</b> mouse wheel (vertical), trackpad, or drag the timeline with the mouse.', '<b>Zoom:</b> <kbd>Ctrl</kbd>/<kbd>⌘</kbd> + wheel (centred on the cursor), the <kbd>+</kbd> and <kbd>−</kbd> keys, or the buttons next to the years. The ↔ button shows the whole line again.', '<b>Detail:</b> from far away you see the movements, the must-know works and their designers (within the chosen detail level); labels, institutions and the other works appear as you zoom in, when they can be read.', '<b>Macro-movements:</b> click one (first in the Movements row) to read its overview: its context factor by factor, its key shifts and the movements it gathers.'],
        h3: 'Reading the timeline', hDesign: 'Design', hContext: 'Context', hConn: 'Connections',
        lgDesign: ['Macro-movement (first row of DESIGN)', 'Movement (soft edges: there are no exact limits)', 'Institution (white bar with a grey outline, ending in an arrow tip)', 'Designer, with a life line in the colour of their discipline (with Works also on, the works sit on it without labels)', 'Designer of several disciplines (stripes)', 'Graphic work', 'Product work', 'Fashion work', 'Architecture work', 'Must-know work', 'Theory: manifesto, treatise, book or school programme (author’s surname)'],
        lgContext: ['Fact at a point in time', 'Fact with a duration', 'Short arrow after a bar: it goes on after that year', 'Point + label + arrow: a long fact or institution, shortened; click it to see the whole bar', 'Productive: materials, processes and tools'],
        lgConn: ['Curve to a context fact, in the colour of its row', 'Curve to a work or another relation (influences, people, institutions)', 'Thin curve: an indirect relation (through a work or a designer)', 'Arrow: the related item is in a closed section or outside the view'],
        lgTone: 'Colour of the context rows:',
        legendNote: 'Works carry a discipline, shown by the shape and colour of the marker; designers take the colour of their disciplines on their life line; movements and institutions are drawn in neutral tones. Selecting an item highlights it in black (white in the dark theme); its related items are shown in bold and in their own colour, and so are the curves.',
        h4: 'Cards, connections and focus',
        card: ['Click any item to open its card: key idea, context, connections and links. Curves join it to its relations; indirect ones (for example a designer and the context of their works) have a thinner line. Hover a curve to read the note of that link.', '<b>Sources:</b> at the end of each card, the “Sources” section (closed when it opens) lists what the facts rest on; the small numbers in the text lead to them. If a card has no sources, a warning triangle says it has not been reviewed yet. “Learn more” is different: recommended further reading.', 'Hovering an item shows a faint preview of its curves (when Connections is on).', 'Click a chip in the card to jump to that item.', '<b>Lens:</b> it is turned on the same way everywhere, by clicking the name of a context sub-category: in the filter bar, on the line (row names), in the macro-movement cards, in the Context section of any card and above the title of the cards of facts, productive items and theory. When you turn the lens off (the same name again or the ✕ of its card), everything goes back to how it was: open rows, card and position. Its facts stay on the line; only the movements, institutions, designers and works connected to them are shown (a designer only if they are connected themselves; otherwise only the work), and the parts that have them open. The card shows the lens: the design seen from that context, by macro-movement, with its facts and the connected design. With a lens on, the curves to context only go to facts of that lens. One lens at a time.', 'On any card, the filter button (or a double click on the item in the line) hides everything except that element and all its connections (the curves stay on if Connections is on); the “Only:” chip brings everything back. It can be combined with a focus.', 'Click the item again, the ✕ or <kbd>Esc</kbd> to close the card. Drag the card’s left edge to change its width.'],
        h5: 'Shortcuts',
        keys: [['<kbd>+</kbd> <kbd>−</kbd>', 'Zoom in / out'], ['<kbd>Ctrl</kbd>/<kbd>⌘</kbd> + <kbd>wheel</kbd>', 'Zoom at the cursor'], ['Drag', 'Move the timeline (on the years: zoom to that span)'], ['Double click', 'On an item: select it and show only its connections (again: show everything). On an era: zoom to it'], ['<kbd>↑</kbd> <kbd>↓</kbd> <kbd>Enter</kbd>', 'Move through search results and choose one'], ['<kbd>Esc</kbd>', 'Close card, help or information']]
      },
      inPrep: 'in preparation', inPrepTitle: 'In preparation', emptyEra: 'This era is in preparation.',
      secContext: 'Context', secDesign: 'Design', nFacts: 'facts', nFact1: 'fact', nItems: 'items', nItem1: 'item', nothingShown: 'Nothing to show with these filters.',
      tr_political: 'Political', tr_economic: 'Economic', tr_social: 'Social', tr_cultural: 'Cultural', tr_technological: 'Technological', tr_production: 'Productive', tr_theory: 'Theoretical',
      ps_materials: 'Materials', ps_processes: 'Processes', ps_tools: 'Tools',
      d_graphic: 'Graphic', d_product: 'Product', d_fashion: 'Fashion', d_architecture: 'Architecture',
      rg_europe: 'Europe', 'rg_north-america': 'North America', 'rg_latin-america': 'Latin America', rg_global: 'Global',
      ty_movements: 'Movements', ty_institutions: 'Institutions', ty_theory: 'Theory', desOffDate: 'The by-date view does not show the designers (select one to see its life line)', dt_theory: 'Theory', ty_designers: 'Designers', ty_works: 'Works',
      fContext: 'Context', fDisc: 'Disciplines', fRegions: 'Regions', fShow: 'Show', fLevel: 'Detail', lv_essential: 'Must-know', lv_normal: 'Complete', lv_complete: 'Complete', lvTip_essential: 'Only the must-know elements ★', lvTip_normal: 'All elements: must-know and the rest', lvTip_complete: 'Everything, including specialised cases', lvRaised: 'Detail changed to', 
      fLens: 'Lens', kDisc: 'Discipline', essayWord: 'Essay', minRead: 'min read', unrevShort: 'Not reviewed', unrevTip: 'Card not reviewed: it has no sources yet', ctxTop: 'Most connected context facts', seeAll: 'See all', lensElems: 'connected elements', scopeOff: 'Remove the scope', scopeTip_graphic: 'See the history of graphic design', scopeTip_product: 'See the history of product design', scopeTip_fashion: 'See the history of fashion design', scopeTip_architecture: 'See the history of architecture', dt_graphic: 'The history of graphic design', dt_product: 'The history of product design', dt_fashion: 'The history of fashion design', dt_architecture: 'The history of architecture', scopeTip: 'Only this discipline and what is connected to it stays on the line. Click its button again (or the ✕) to see everything.', lensKicker: 'Lens', lensHow: 'Design through this lens', lensByEra: 'By macro-movement', lensFacts: 'Facts on this row', lensDesign: 'Connected design', lensLinked: 'connected design items', lensEraCard: 'Open card', lensTip: 'Only the design connected to these facts is on the line. Click an item to open its card; the curves only go to facts of this lens. Turn the lens off by clicking its name again or with the ✕: everything goes back to how it was.', lens_political: 'Through the political lens, design appears as a tool of power and a field where power is contested. States, parties and movements use it to communicate, persuade and organise life: propaganda, national identity, public housing, rules and standards. Wars, revolutions and regimes change who commissions design, what for and within which limits, and they push many designers towards commitment or exile.', lens_economic: 'Through the economic lens, design answers to how things are produced, sold and consumed. Industrialisation, markets, crises and credit decide which objects can be made, at what price and for whom. Here design shows up as added value, as a sales strategy (style, obsolescence, brand) and as a response to scarcity.', lens_social: 'Through the social lens, design answers to how people live. The city, work, the family, gender, health and migration raise new needs (housing, kitchens, clothing, leisure), and design proposes ways of living with them, sometimes to order everyday life and sometimes to free it.', lens_cultural: 'Through the cultural lens, design talks with art, ideas and the media. Avant-gardes, the press, cinema, radio and new forms of leisure give it languages, images and audiences. Here you can see how a way of seeing the world turns into a typeface, a poster, an object or a building.', lens_technological: 'Through the technological lens, design answers to the great techniques of each period (energy, transport, communications, computing), which change speed, distance and daily life, and open up objects, images and services that did not exist before.', lens_production: 'Through the productive lens, design is understood through its means: the materials, processes and tools with which it is drawn and made. A new material or machine does not only make things cheaper: it changes the forms that are possible and the way designers work.', lens_theory: 'Through the theoretical lens, design is read through what was written about it: manifestos, treatises, books and school programmes that define what good design is, for whom and why, and that often anticipate or justify the works.',
      fArrange: 'Arrange', ar_chrono: 'By category', ar_date: 'By date', ar_disc: 'By discipline', ar_region: 'By region', erasLbl: 'Eras', macroLbl: 'Macro-movements', ag_all: '', ag_graphic: 'Graphic', ag_product: 'Product', ag_fashion: 'Fashion', ag_architecture: 'Architecture', ag_europe: 'Europe', 'ag_north-america': 'North America', 'ag_latin-america': 'Latin America', ag_multi: 'Several regions', ag_global: 'Global', 'zn_british-isles': 'British Isles', 'zn_france-benelux': 'France and Benelux', zn_germanic: 'German-speaking world', 'zn_central-east': 'Central and Eastern Europe', zn_russia: 'Russia and Soviet space', zn_nordic: 'Nordic countries', zn_mediterranean: 'Mediterranean', zn_usa: 'United States', zn_canada: 'Canada', 'zn_mexico-ca': 'Mexico and Central America', zn_caribbean: 'Caribbean', zn_andes: 'Andes', zn_brazil: 'Brazil', 'zn_southern-cone': 'Southern Cone', zn_beyond: 'Beyond the West', zn_other: 'Other', emptyMsg: 'Select an item on the line to see its card.', emptyEraHint: 'Click a macro-movement (first in the Movements row) to read its overview.', emptyInfo: 'The (i) button opens the presentation of the site.',
      fConn: 'Connections', cn_ctx: 'Context', cn_works: 'Works', cn_other: 'Other', connTip: 'Show or hide the curves that join the selected item to its relations (a lens turns them on)',
      fScale: 'Scale', sc_uneven: 'Visual', sc_linear: 'Chronological', sc_unevenTip: 'Visual: decades with more elements are wider (with a minimum width)', sc_linearTip: 'Chronological: every year has the same width',
      scaleMark: 'The scale changes here', zoomMore: 'Zoom in to see more', zoomFit: 'See the whole line', zoomVis: 'Fit to what is shown', rangeFrom: 'From', rangeTo: 'to', rangeAll: 'All', rangeFit: 'Fit', rangeFromTip: 'First visible year (type one and press Enter)', rangeToTip: 'Last visible year (type one and press Enter)', edgeL: 'Show more years to the left (hold to keep going)', edgeR: 'Show more years to the right (hold to keep going)', axisTip: 'Drag on the years to zoom to a span', eraZoom: 'Zoom to this era',
      dt_movements: 'Movements', dt_institutions: 'Institutions', dt_designers: 'Designers and works',
      rv_btn: 'Review summary (edit mode)', focusBtn: 'Lens', focusOff: 'Turn the lens off', focusShort: 'Lens', focusTip: 'Use a lens to read the era from one kind of context: only its facts and the design they explain stay on the line.',
      isoBtn: 'Show only its connections', isoOff: 'Show everything again', isoChip: 'Only:', isoClear: 'Show everything',
      k_movement: 'Movement', k_institution: 'Institution', k_designer: 'Designer', k_work: 'Work', k_context: 'Context', k_production: 'Productive', k_theory: 'Theory', k_concept: 'Concept',
      ik_school: 'School', ik_company: 'Company', ik_studio: 'Studio', ik_exhibition: 'Exhibition', ik_association: 'Association', ik_museum: 'Museum', ik_publication: 'Publication',
      g_manifesto: 'Manifestos and programmes', g_criticism: 'Criticism', g_history: 'Design history', g_method: 'Method and practice', g_pedagogy: 'School programmes', g_typography: 'Typography and graphic design', g_architecture: 'Architecture', g_society: 'Design, society and ethics',
      keyIdea: 'Key idea', ctx: 'Context', analysis: 'Analysis', designProd: 'Design and production', byDesigner: 'Designer or studio', maker: 'Maker', client: 'Client', materials: 'Materials', prodItems: 'Materials and processes',
      lifeInProd: 'Manufacturing span', designYear: 'Designed', moveInst: 'Movement and institution', conn: 'Connections', whereSee: 'Where to see it', status: 'Current state', viaWork: 'Via',
      learn: 'Learn more', noFreeImg: 'No free image here.', seeCollection: 'See in the collection', openCommons: 'Open images on Wikimedia Commons', loadingImg: 'Loading image…', imgOpen: 'Open the image source',
      happened: 'What happened', effect: 'Effect on design', related: 'Related design', bio: 'Biography', recognise: 'How to recognise it', shift: 'The shift', ctxText: 'Context',
      works: 'Works', designers: 'Designers', institutions: 'Institutions', movements: 'Movements', history: 'History', people: 'People', production: 'Productive', theory: 'Theory',
      origin: 'Origin', enabled: 'What it made possible', change: 'How it changed design', economy: 'Economics', relations: 'Relationship with design', whatIs: 'What it is',
      th_ideas: 'Main ideas', th_impact: 'Impact on design', th_sources: 'Read the source', linkedTo: 'Linked to',
      whereSeeIt: 'Where you see it', context: 'Context', placeLbl: 'Place',
      mustKnow: 'Must-know', since: 'since', today: 'today', stillProd: 'still in production', inProdUntil: 'in production',
      overview: 'Era overview', k_macro: 'Macro-movement', ctxByFactor: 'The context, factor by factor', macroParts: 'Movements it gathers', macroNoParts: 'Its movements will be added when this part of the line is completed.', bigPicture: 'The big picture', keyShifts: 'Key shifts', ctxSynth: 'The context in brief',
      n_movements: 'movements', n_institutions: 'institutions', n_designers: 'designers', n_works: 'works', n_stars: 'must-know', n_contexts: 'context facts', n_production: 'productive items', n_theories: 'theoretical texts', n_concepts: 'concepts', n_eras: 'eras', n_conn: 'connections',
      byDisc: 'Works by discipline', byTrack: 'Context by kind', byEra: 'By era', totalRow: 'All eras', pctCtx: 'Works with context', ofWorks: 'of the works have at least one context link', colDes: 'Des.', colWorks: 'Works', colCtx: 'Ctx', colPct: '% ctx',
      infoKicker: 'About this timeline', infoAbout: 'Presentation', infoBasis: 'Conceptual and bibliographic basis', basis_gen: 'General design history', basis_graphic: 'Graphic design', basis_architecture: 'Architecture', basis_fashion: 'Fashion', basis_latam: 'Latin America', infoBasisText: 'The timeline follows, in part, an approach similar to the social history of design proposed by Forty (1986): the material forms of objects embody, affect and reflect the ideas, needs and conflicts of each society. The choice of movements, institutions, texts, designers and works follows the canon of the general histories used in university teaching of design and of its four disciplines (graphic/visual communication; product and industrial; fashion and textiles; architecture and interior design). The main sources of this timeline are:', infoSecs: 'Sections of the timeline', infoStats: 'Overall figures', infoSpan: '1750–today', infoThesis: 'Design is understood as a response to its context.',
      infoIntro: 'A timeline of design history, built on the thesis that design is a response to its context. Here every work, designer, movement and institution appears next to the political, economic, social, cultural and technological facts that explain it, and is linked to other related works and designers.',
      infoCtxHead: 'Context', infoDesignHead: 'Design', infoOtherHead: 'Reading the line', infoCtxNote: 'Five kinds of facts, plus the productive row (materials, processes and tools).', infoDesNote: 'Movements (the macro-movements first), institutions, theory, designers and works, which can be arranged by category, date, discipline or region.',
      infoCtx: [['political', 'Wars, revolutions, regimes, state policies and laws.'], ['economic', 'Industrialisation, markets, crises, consumption, trade, globalisation and resources.'], ['social', 'Urbanisation, work, gender, home life, migration, health and the environment.'], ['cultural', 'Artistic movements, media (press, film, radio, TV, internet), ideas and leisure.'], ['technological', 'General technology: energy, transport, communications and computing.'], ['production', 'With what and how design is made and manufactured: materials, processes and tools.']],
      infoDesign: [['Macro-movements', 'Broad movements that span decades and gather several movements.'], ['Movements', 'Groups and tendencies with a shared language and ideas. Soft-edged ends show that they have no exact start or end dates.'], ['Institutions', 'Schools, companies, studios, exhibitions, museums and publications that made design possible.'], ['Theory', 'Manifestos, treatises, books and school programmes that defined what design is.'], ['Designers', 'People, duos and collectives, with a life line in the colour of their disciplines.'], ['Works', 'Objects, buildings, garments and graphics; the shape and colour of the marker show the discipline: graphic (circle), product (diamond), fashion (triangle), architecture (square).']],
      infoOther: [['Detail levels', 'Elements marked with ★ are essential in an introductory course.'], ['Connections', 'Direct and indirect relations (for example, a designer and the context of their works).']],
      infoTypes: 'What each element is', infoHowTo: 'How to use the timeline', infoHowToTip: 'Open the help: how to navigate, filter and read the line', infoDisclaimer: 'This is a project in development: it may contain errors and incomplete content.'
    },
    es: {
      title: 'Línea de Historia del Diseño', searchLbl: 'Buscar en la línea de tiempo', search: 'Buscar obras, diseñadores, movimientos, instituciones, contexto…', loading: 'Cargando…', close: 'Cerrar', noMatch: 'Sin resultados.', langBtn: 'EN', langTitle: 'View in English',
      themeToDark: 'Tema oscuro', themeToLight: 'Tema claro', expand: 'Desplegar', collapse: 'Plegar', openCtx: 'Desplegar todo el contexto', closeCtx: 'Plegar todo el contexto', openDes: 'Desplegar todo el diseño', closeDes: 'Plegar todo el diseño',
      mobileTitle: 'Solo en computador', mobileMsg: 'Esta línea de tiempo solo puede visualizarse en un computador (escritorio o notebook). Ábrela desde una pantalla más grande.',
      helpBtn: 'Ayuda', helpTitle: 'Cómo usar la línea de tiempo',
      help: {
        lead: 'Una línea de tiempo interactiva de la historia del diseño: una sola línea continua desde 1750 hasta hoy. El diseño (movimientos, instituciones, diseñadores y obras) está bajo los hechos de contexto que lo explican.',
        h1: 'Las partes del sitio', f1: 'Las áreas principales del sitio',
        parts: [['Barra superior', 'Búsqueda, tema claro u oscuro, idioma, la presentación (i) y esta ayuda. En el modo edición tiene además el resumen de revisión.'], ['Filtros', 'Foco: cada botón lee la línea desde un tipo de contexto (político, económico, social, cultural, tecnológico, productivo o teórico): quedan sus hechos y el diseño conectado con ellos, lo demás se esconde, la ficha explica esa mirada y se encienden las curvas. Otro clic lo quita. Conexiones muestra u oculta las curvas. Disciplinas pone el alcance en una disciplina (una a la vez, combinable con un foco): quedan sus obras y el diseño y el contexto ligados a ella, y la ficha cuenta su historia en un ensayo con enlaces; otro clic lo quita. Detalle elige cuánto diseño se muestra: imprescindible ★ o normal (por defecto, todo); el contexto se ve siempre, y al ir a un elemento que no es imprescindible el detalle pasa a normal. Organizar ordena el diseño por categoría (movimientos, instituciones, diseñadores), por fecha (una fila por elemento, según su año de inicio), por disciplina (cuatro grupos; un diseñador que trabaja en varias disciplinas aparece en cada una, con las obras de esa disciplina) o por región (dividida en zonas culturales). Mostrar elige los tipos de elemento. Escala cambia entre «visual» (las décadas con más elementos son más anchas) y «cronológica» (todos los años miden lo mismo). El chip «Solo:» deshace el filtro de una ficha.'], ['Eje de años', 'Sobre los años, el minimapa del tiempo muestra toda la línea y, entre corchetes, el tramo que ves: arrastra un corchete para cambiar el inicio o el fin, arrastra el tramo para moverte o haz clic en otro lugar para ir ahí. Arrastra sobre los años para acercarte a un tramo (el tramo se sombrea en toda la línea). Cerca de los extremos, las flechas ‹ › suman años por ese lado (mantén apretado para seguir). En la escala «visual», las marcas en zigzag muestran dónde cambia la escala.'], ['Años visibles', 'Las dos casillas (primer y último año): escribe un año y presiona Enter. «Todo» vuelve a mostrar la línea completa y «Ajustar» ajusta los años a lo que se muestra ahora (filtros, foco, «Solo»). La flecha doble a la izquierda de CONTEXTO y DISEÑO funciona como las flechitas: ⌄⌄ indica que hay algo abierto y un clic pliega todas sus filas y grupos; ›› indica que todo está plegado y un clic los despliega (con un foco activo, en CONTEXTO solo actúa sobre la fila del foco).'], ['Filas', 'Haz clic en el nombre de una fila de contexto para ponerle el foco; la flechita abre o cierra la fila. El diseño no tiene filas plegables: lo que se ve se elige en Mostrar y cómo se ordena, en Organizar. Los macromovimientos (Modernismo, Posmodernismo) van primero en la fila de movimientos: haz clic en uno para leer su panorama.'], ['Ficha', 'Detalle del elemento seleccionado, o el foco activo cuando no hay nada seleccionado.']],
        h2: 'Moverse y hacer zoom',
        move: ['<b>Desplazarse:</b> rueda del mouse (vertical), trackpad, o arrastrar la línea con el mouse.', '<b>Zoom:</b> <kbd>Ctrl</kbd>/<kbd>⌘</kbd> + rueda (centrado en el cursor), las teclas <kbd>+</kbd> y <kbd>−</kbd>, o los botones junto a los años. El botón ↔ vuelve a mostrar la línea completa.', '<b>Detalle:</b> de lejos se ven los movimientos, las obras imprescindibles y sus diseñadores (dentro del nivel de detalle elegido); las etiquetas, las instituciones y las demás obras aparecen al acercar, cuando se pueden leer.', '<b>Macromovimientos:</b> haz clic en uno (primeros en la fila de movimientos) para leer su panorama: su contexto factor por factor, sus cambios clave y los movimientos que reúne.'],
        h3: 'Cómo leer la línea', hDesign: 'Diseño', hContext: 'Contexto', hConn: 'Conexiones',
        lgDesign: ['Macromovimiento (primera fila de DISEÑO)', 'Movimiento (bordes difusos: no tienen límites exactos)', 'Institución (barra blanca con contorno gris que termina en punta de flecha)', 'Diseñador, con su línea de vida en el color de su disciplina (con Obras también encendido, las obras van encima, sin etiquetas)', 'Diseñador de varias disciplinas (rayas)', 'Obra gráfica', 'Obra de producto', 'Obra de moda', 'Obra de arquitectura', 'Obra imprescindible', 'Teoría: manifiesto, tratado, libro o programa de escuela (apellido del autor)'],
        lgContext: ['Hecho en un momento', 'Hecho con duración', 'Flecha corta tras una barra: sigue después de ese año', 'Punto + etiqueta + flecha: un hecho o una institución larga, abreviada; haz clic para ver la barra completa', 'Productivo: materiales, procesos y herramientas'],
        lgConn: ['Curva hacia un hecho de contexto, en el color de su fila', 'Curva hacia una obra u otra relación (influencias, personas, instituciones)', 'Curva fina: una relación indirecta (a través de una obra o de un diseñador)', 'Flecha: el elemento relacionado está en una sección cerrada o fuera de la vista'],
        lgTone: 'Color de las filas de contexto:',
        legendNote: 'Las obras llevan disciplina, que se ve en la forma y el color del marcador; los diseñadores llevan el color de sus disciplinas en su línea de vida; movimientos e instituciones van en tonos neutros. Al elegir un elemento, este se destaca en negro (blanco en el tema oscuro); lo relacionado se ve en negrita y en su propio color, igual que las curvas.',
        h4: 'Fichas, conexiones y foco',
        card: ['Haz clic en cualquier elemento para abrir su ficha: idea clave, contexto, conexiones y enlaces. Unas curvas lo unen con sus relaciones; las indirectas (por ejemplo, un diseñador y el contexto de sus obras) van con una línea más fina. Pasa el cursor por una curva para leer la nota de ese enlace.', '<b>Fuentes:</b> al final de cada ficha, la sección «Fuentes» (cerrada al abrir) lista en qué se apoyan los datos; los números pequeños del texto llevan a ellas. Si una ficha no tiene fuentes, un triángulo de advertencia avisa que aún no ha sido revisada. «Saber más» es otra cosa: lecturas recomendadas para profundizar.', 'Al pasar el cursor por un elemento se ve una insinuación tenue de sus curvas (si Conexiones está encendido).', 'Haz clic en un chip de la ficha para saltar a ese elemento.', '<b>Foco:</b> se activa igual en todo el sitio, haciendo clic en el nombre de una subcategoría de contexto: en la barra de filtros, en la línea (nombre de la fila), en las fichas de macromovimiento, en la sección Contexto de cualquier ficha y sobre el título de las fichas de hechos, productivo y teoría. Al quitar el foco (otro clic en el mismo nombre o la ✕ de su ficha) todo vuelve a como estaba: filas abiertas, ficha y posición. Quedan sus hechos en la línea y solo los movimientos, instituciones, diseñadores y obras conectados con ellos (un diseñador solo si está conectado él mismo; si no, solo la obra), y se abren las partes que los tienen. La ficha muestra el foco: el diseño desde ese contexto, por macromovimiento, con sus hechos y el diseño conectado. Con un foco activo, las curvas hacia el contexto solo van a hechos de ese foco. Un foco a la vez.', 'En cualquier ficha, el botón de filtro (o un doble clic sobre el elemento en la línea) esconde todo menos ese elemento y todas sus conexiones (las curvas siguen si Conexiones está encendido); el chip «Solo:» vuelve a mostrar todo. Se puede combinar con un foco.', 'Haz clic de nuevo en el elemento, en la ✕ o <kbd>Esc</kbd> para cerrar la ficha. Arrastra el borde izquierdo de la ficha para cambiar su ancho.'],
        h5: 'Atajos',
        keys: [['<kbd>+</kbd> <kbd>−</kbd>', 'Acercar / alejar'], ['<kbd>Ctrl</kbd>/<kbd>⌘</kbd> + <kbd>rueda</kbd>', 'Zoom en el cursor'], ['Arrastrar', 'Mover la línea (sobre los años: acercarse a ese tramo)'], ['Doble clic', 'En un elemento: elegirlo y ver solo sus conexiones (otra vez: ver todo). En una época: acercarse a ella'], ['<kbd>↑</kbd> <kbd>↓</kbd> <kbd>Enter</kbd>', 'Moverse por los resultados de la búsqueda y elegir uno'], ['<kbd>Esc</kbd>', 'Cerrar ficha, ayuda o información']]
      },
      inPrep: 'en preparación', inPrepTitle: 'En preparación', emptyEra: 'Esta época está en preparación.',
      secContext: 'Contexto', secDesign: 'Diseño', nFacts: 'hechos', nFact1: 'hecho', nItems: 'elementos', nItem1: 'elemento', nothingShown: 'No hay nada que mostrar con estos filtros.',
      tr_political: 'Político', tr_economic: 'Económico', tr_social: 'Social', tr_cultural: 'Cultural', tr_technological: 'Tecnológico', tr_production: 'Productivo', tr_theory: 'Teórico',
      ps_materials: 'Materiales', ps_processes: 'Procesos', ps_tools: 'Herramientas',
      d_graphic: 'Gráfico', d_product: 'Producto', d_fashion: 'Moda', d_architecture: 'Arquitectura',
      rg_europe: 'Europa', 'rg_north-america': 'Norteamérica', 'rg_latin-america': 'América Latina', rg_global: 'Global',
      ty_movements: 'Movimientos', ty_institutions: 'Instituciones', ty_theory: 'Teoría', desOffDate: 'La vista por fecha no muestra los diseñadores (elige uno para ver su línea de vida)', dt_theory: 'Teoría', ty_designers: 'Diseñadores', ty_works: 'Obras',
      fContext: 'Contexto', fDisc: 'Disciplinas', fRegions: 'Regiones', fShow: 'Mostrar', fLevel: 'Detalle', lv_essential: 'Imprescindible', lv_normal: 'Completo', lv_complete: 'Completo', lvTip_essential: 'Solo los elementos imprescindibles ★', lvTip_normal: 'Todos los elementos: imprescindibles y el resto', lvTip_complete: 'Todo, incluidos los casos especializados', lvRaised: 'Detalle cambiado a', 
      fLens: 'Foco', kDisc: 'Disciplina', essayWord: 'Ensayo', minRead: 'min de lectura', unrevShort: 'No revisada', unrevTip: 'Ficha no revisada: aún no tiene fuentes', ctxTop: 'Hechos de contexto más conectados', seeAll: 'Ver todo', lensElems: 'elementos conectados', scopeOff: 'Quitar el alcance', scopeTip_graphic: 'Ver la historia del diseño gráfico', scopeTip_product: 'Ver la historia del diseño de producto', scopeTip_fashion: 'Ver la historia del diseño de moda', scopeTip_architecture: 'Ver la historia de la arquitectura', dt_graphic: 'La historia del diseño gráfico', dt_product: 'La historia del diseño de producto', dt_fashion: 'La historia del diseño de moda', dt_architecture: 'La historia de la arquitectura', scopeTip: 'En la línea solo queda esta disciplina y lo conectado con ella. Haz clic de nuevo en su botón (o en la ✕) para volver a ver todo.', lensKicker: 'Foco', lensHow: 'El diseño desde este foco', lensByEra: 'Por macromovimiento', lensFacts: 'Hechos de esta fila', lensDesign: 'Diseño conectado', lensLinked: 'elementos de diseño conectados', lensEraCard: 'Abrir ficha', lensTip: 'En la línea solo queda el diseño conectado con estos hechos. Haz clic en un elemento para abrir su ficha; las curvas solo van a hechos de este foco. Quita el foco con otro clic en su nombre o con la ✕: todo vuelve a como estaba.', lens_political: 'Desde lo político, el diseño aparece como herramienta del poder y como terreno donde ese poder se disputa. Estados, partidos y movimientos lo usan para comunicar, persuadir y organizar la vida: propaganda, identidad nacional, vivienda pública, reglas y normas. Las guerras, las revoluciones y los regímenes cambian quién encarga el diseño, para qué y con qué límites, y empujan a muchos diseñadores al compromiso o al exilio.', lens_economic: 'Desde lo económico, el diseño responde a cómo se produce, se vende y se consume. La industrialización, los mercados, las crisis y el crédito deciden qué objetos se pueden fabricar, a qué precio y para quién. Aquí el diseño aparece como valor agregado, como estrategia de venta (estilo, obsolescencia, marca) y como respuesta a la escasez.', lens_social: 'Desde lo social, el diseño responde a cómo vive la gente. La ciudad, el trabajo, la familia, el género, la salud y las migraciones plantean necesidades nuevas (vivienda, cocina, vestuario, ocio), y el diseño propone formas de habitarlas, a veces para ordenar la vida cotidiana y otras para liberarla.', lens_cultural: 'Desde lo cultural, el diseño dialoga con el arte, las ideas y los medios. Las vanguardias, la prensa, el cine, la radio y las nuevas formas de ocio le dan lenguajes, imágenes y públicos. Aquí se ve cómo una manera de ver el mundo se vuelve tipografía, cartel, objeto o edificio.', lens_technological: 'Desde lo tecnológico, el diseño responde a las grandes técnicas de cada época (energía, transporte, comunicaciones, computación), que cambian la velocidad, las distancias y la vida diaria, y abren objetos, imágenes y servicios que antes no existían.', lens_production: 'Desde lo productivo, el diseño se entiende por sus medios: los materiales, los procesos y las herramientas con que se dibuja y se fabrica. Un material o una máquina nueva no solo abarata: cambia las formas posibles y la manera de trabajar de quien diseña.', lens_theory: 'Desde lo teórico, el diseño se lee a través de lo que se escribió sobre él: manifiestos, tratados, libros y programas de escuelas que definen qué es diseñar bien, para quién y por qué, y que muchas veces anticipan o justifican las obras.',
      fArrange: 'Organizar', ar_chrono: 'Por categoría', ar_date: 'Por fecha', ar_disc: 'Por disciplina', ar_region: 'Por región', erasLbl: 'Épocas', macroLbl: 'Macromovimientos', ag_all: '', ag_graphic: 'Gráfico', ag_product: 'Producto', ag_fashion: 'Moda', ag_architecture: 'Arquitectura', ag_europe: 'Europa', 'ag_north-america': 'Norteamérica', 'ag_latin-america': 'América Latina', ag_multi: 'Varias regiones', ag_global: 'Global', 'zn_british-isles': 'Islas Británicas', 'zn_france-benelux': 'Francia y Benelux', zn_germanic: 'Mundo germánico', 'zn_central-east': 'Europa central y del este', zn_russia: 'Rusia y espacio soviético', zn_nordic: 'Países nórdicos', zn_mediterranean: 'Mediterráneo', zn_usa: 'Estados Unidos', zn_canada: 'Canadá', 'zn_mexico-ca': 'México y Centroamérica', zn_caribbean: 'Caribe', zn_andes: 'Andes', zn_brazil: 'Brasil', 'zn_southern-cone': 'Cono Sur', zn_beyond: 'Más allá de Occidente', zn_other: 'Otros', emptyMsg: 'Selecciona un elemento de la línea para ver su ficha.', emptyEraHint: 'Haz clic en un macromovimiento (primero en la fila de movimientos) para leer su panorama.', emptyInfo: 'El botón (i) abre la presentación del sitio.',
      fConn: 'Conexiones', cn_ctx: 'Contexto', cn_works: 'Obras', cn_other: 'Otras', connTip: 'Muestra u oculta las curvas que unen el elemento elegido con sus relaciones (un foco las enciende)',
      fScale: 'Escala', sc_uneven: 'Visual', sc_linear: 'Cronológica', sc_unevenTip: 'Visual: las décadas con más elementos son más anchas (con un ancho mínimo)', sc_linearTip: 'Cronológica: todos los años miden lo mismo',
      scaleMark: 'Aquí cambia la escala', zoomMore: 'Acerca para ver más', zoomFit: 'Ver la línea completa', zoomVis: 'Ajustar a lo que se muestra', rangeFrom: 'De', rangeTo: 'a', rangeAll: 'Todo', rangeFit: 'Ajustar', rangeFromTip: 'Primer año visible (escribe uno y presiona Enter)', rangeToTip: 'Último año visible (escribe uno y presiona Enter)', edgeL: 'Ver más años a la izquierda (mantén apretado para seguir)', edgeR: 'Ver más años a la derecha (mantén apretado para seguir)', axisTip: 'Arrastra sobre los años para acercarte a un tramo', eraZoom: 'Acercar a esta época',
      dt_movements: 'Movimientos', dt_institutions: 'Instituciones', dt_designers: 'Diseñadores y obras',
      rv_btn: 'Resumen de revisión (modo edición)', focusBtn: 'Foco', focusOff: 'Quitar el foco', focusShort: 'Foco', focusTip: 'Pon el foco en un tipo de contexto para leer la época desde él: solo quedan sus hechos y el diseño que explican.',
      isoBtn: 'Ver solo sus conexiones', isoOff: 'Volver a ver todo', isoChip: 'Solo:', isoClear: 'Volver a ver todo',
      k_movement: 'Movimiento', k_institution: 'Institución', k_designer: 'Diseñador', k_work: 'Obra', k_context: 'Contexto', k_production: 'Productivo', k_theory: 'Teoría', k_concept: 'Concepto',
      ik_school: 'Escuela', ik_company: 'Empresa', ik_studio: 'Estudio', ik_exhibition: 'Exposición', ik_association: 'Asociación', ik_museum: 'Museo', ik_publication: 'Publicación',
      g_manifesto: 'Manifiestos y programas', g_criticism: 'Crítica', g_history: 'Historia del diseño', g_method: 'Métodos y práctica', g_pedagogy: 'Programas de escuelas', g_typography: 'Tipografía y diseño gráfico', g_architecture: 'Arquitectura', g_society: 'Diseño, sociedad y ética',
      keyIdea: 'Idea clave', ctx: 'Contexto', analysis: 'Análisis', designProd: 'Diseño y producción', byDesigner: 'Diseñador o estudio', maker: 'Fabricante', client: 'Cliente', materials: 'Materiales', prodItems: 'Materiales y procesos',
      lifeInProd: 'Período de fabricación', designYear: 'Diseño', moveInst: 'Movimiento e institución', conn: 'Conexiones', whereSee: 'Dónde verla', status: 'Estado actual', viaWork: 'Vía',
      learn: 'Saber más', noFreeImg: 'Sin imagen libre.', seeCollection: 'Ver en la colección', openCommons: 'Ver imágenes en Wikimedia Commons', loadingImg: 'Cargando imagen…', imgOpen: 'Abrir la fuente de la imagen',
      happened: 'Qué pasó', effect: 'Efecto en el diseño', related: 'Diseño relacionado', bio: 'Biografía', recognise: 'Cómo reconocerlo', shift: 'El cambio', ctxText: 'Contexto',
      works: 'Obras', designers: 'Diseñadores', institutions: 'Instituciones', movements: 'Movimientos', history: 'Historia', people: 'Personas', production: 'Productivo', theory: 'Teoría',
      origin: 'Origen', enabled: 'Qué permitió', change: 'Cómo cambió el diseño', economy: 'Economía', relations: 'Relación con el diseño', whatIs: 'Qué es',
      th_ideas: 'Ideas principales', th_impact: 'Impacto en el diseño', th_sources: 'Leer la fuente', linkedTo: 'Enlazado con',
      whereSeeIt: 'Dónde se ve', context: 'Contexto', placeLbl: 'Lugar',
      mustKnow: 'Imprescindible', since: 'desde', today: 'hoy', stillProd: 'sigue en producción', inProdUntil: 'en producción',
      overview: 'Panorama de la época', k_macro: 'Macromovimiento', ctxByFactor: 'El contexto, factor por factor', macroParts: 'Movimientos que reúne', macroNoParts: 'Sus movimientos se agregarán cuando se complete esta parte de la línea.', bigPicture: 'Visión general', keyShifts: 'Cambios clave', ctxSynth: 'El contexto en síntesis',
      n_movements: 'movimientos', n_institutions: 'instituciones', n_designers: 'diseñadores', n_works: 'obras', n_stars: 'imprescindibles', n_contexts: 'hechos de contexto', n_production: 'elementos productivos', n_theories: 'textos teóricos', n_concepts: 'conceptos', n_eras: 'épocas', n_conn: 'conexiones',
      byDisc: 'Obras por disciplina', byTrack: 'Contexto por tipo', byEra: 'Por época', totalRow: 'Todas las épocas', pctCtx: 'Obras con contexto', ofWorks: 'de las obras tiene al menos un enlace de contexto', colDes: 'Dis.', colWorks: 'Obras', colCtx: 'Ctx', colPct: '% ctx',
      infoKicker: 'Acerca de la línea de tiempo', infoAbout: 'Presentación', infoBasis: 'Fundamento conceptual y bibliográfico', basis_gen: 'Historia general del diseño', basis_graphic: 'Diseño gráfico', basis_architecture: 'Arquitectura', basis_fashion: 'Moda', basis_latam: 'América Latina', infoBasisText: 'La línea sigue, en parte, una aproximación similar a la historia social del diseño propuesta por Forty (1986): las formas materiales de los objetos encarnan, afectan y reflejan las ideas, las necesidades y los conflictos de cada sociedad. La selección de movimientos, instituciones, textos, diseñadores y obras sigue el canon de las historias generales que se usan en la enseñanza universitaria del diseño y de sus cuatro disciplinas (gráfico/comunicación visual; productos e industrial; moda y textil; arquitectura y diseño interior). Las principales fuentes de esta línea son:', infoSecs: 'Secciones de la línea', infoStats: 'Datos generales', infoSpan: '1750–hoy', infoThesis: 'El diseño se entiende como respuesta a su contexto.',
      infoIntro: 'Una línea de tiempo de la historia del diseño, formulada a partir de la tesis de que el diseño es una respuesta a su contexto. Aquí cada obra, diseñador, movimiento e institución aparece junto a los hechos políticos, económicos, sociales, culturales y tecnológicos que lo explican, y vinculado con otras obras y diseñadores relacionados.',
      infoCtxHead: 'Contexto', infoDesignHead: 'Diseño', infoOtherHead: 'Cómo leer la línea', infoCtxNote: 'Cinco tipos de hechos, más la fila productiva (materiales, procesos y herramientas).', infoDesNote: 'Movimientos (primero los macromovimientos), instituciones, teoría, diseñadores y obras, que se pueden organizar por categoría, fecha, disciplina o región.',
      infoCtx: [['political', 'Guerras, revoluciones, regímenes, políticas de Estado y leyes.'], ['economic', 'Industrialización, mercados, crisis, consumo, comercio, globalización y recursos.'], ['social', 'Urbanización, trabajo, género, vida doméstica, migraciones, salud y medio ambiente.'], ['cultural', 'Movimientos artísticos, medios (prensa, cine, radio, TV, internet), ideas y ocio.'], ['technological', 'Tecnología general: energía, transporte, comunicaciones y computación.'], ['production', 'Con qué y cómo se diseña y se fabrica: materiales, procesos y herramientas.']],
      infoDesign: [['Macromovimientos', 'Movimientos amplios que abarcan décadas y reúnen a varios movimientos.'], ['Movimientos', 'Grupos y tendencias con un lenguaje y unas ideas comunes. Los extremos difuminados muestran que no tienen fechas de inicio o término exactas.'], ['Instituciones', 'Escuelas, empresas, estudios, exposiciones, museos y publicaciones que hicieron posible el diseño.'], ['Teoría', 'Manifiestos, tratados, libros y programas de escuelas que definieron qué es el diseño.'], ['Diseñadores', 'Personas, dúos y colectivos, con una línea de vida en el color de sus disciplinas.'], ['Obras', 'Objetos, edificios, prendas y gráfica; la forma y el color del marcador indican la disciplina: gráfico (círculo), producto (rombo), moda (triángulo), arquitectura (cuadrado).']],
      infoOther: [['Niveles de detalle', 'Los elementos marcados con ★ son imprescindibles en un curso introductorio.'], ['Conexiones', 'Relaciones directas, e indirectas (por ejemplo, un diseñador y el contexto de sus obras).']],
      infoTypes: 'Qué es cada elemento', infoHowTo: 'Cómo usar la línea del tiempo', infoHowToTip: 'Abre la ayuda: cómo navegar, filtrar y leer la línea', infoDisclaimer: 'Este es un proyecto en desarrollo: puede contener errores y contenido incompleto.'
    }
  };
  // names of the usual kinds of work (the data holds the English word)
  const TYPE_ES = { poster: 'cartel', typeface: 'tipografía', book: 'libro', magazine: 'revista', identity: 'identidad', logo: 'logotipo', signage: 'señalética', infographic: 'gráfico de información', map: 'mapa', stamp: 'sello', banknote: 'billete', package: 'envase', interface: 'interfaz', icon: 'ícono', cover: 'portada', illustration: 'ilustración', print: 'grabado', album: 'carátula', pictogram: 'pictograma', typography: 'tipografía', furniture: 'mueble', chair: 'silla', lamp: 'lámpara', utensil: 'utensilio', appliance: 'aparato', device: 'dispositivo', machine: 'máquina', vehicle: 'vehículo', toy: 'juguete', tool: 'herramienta', object: 'objeto', instrument: 'instrumento', kitchenware: 'utensilios de cocina', tableware: 'vajilla', watch: 'reloj', bottle: 'botella', ceramics: 'cerámica', garment: 'prenda', collection: 'colección', accessory: 'accesorio', textile: 'textil', footwear: 'calzado', dress: 'vestido', fragrance: 'fragancia', costume: 'traje', building: 'edificio', housing: 'vivienda', interior: 'interior', complex: 'conjunto', city: 'ciudad', pavilion: 'pabellón', estate: 'conjunto residencial', infrastructure: 'infraestructura' };

  // Museums and collections: matched against the labels of "where to see it" and used for search links.
  const COLLECTION_SEARCH = [
    ['MoMA', (q) => 'https://www.moma.org/collection/?q=' + q],
    ['V&A', (q) => 'https://collections.vam.ac.uk/search/?q=' + q],
    ['Google Arts & Culture', (q) => 'https://artsandculture.google.com/search?q=' + q]
  ];

  // ---------- State ----------
  const $ = (id) => document.getElementById(id);
  const store = { get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }, set(k, v) { try { localStorage.setItem(k, v); } catch (e) { /* ignore */ } } };
  // light / dark theme: follows the system until the visitor picks one with the button (remembered per browser)
  const mqDark = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;
  const effTheme = () => document.documentElement.dataset.theme || (mqDark && mqDark.matches ? 'dark' : 'light');
  function syncTheme() {
    const b = $('themeBtn'); if (!b) return;
    const dark = effTheme() === 'dark', lbl = t(dark ? 'themeToLight' : 'themeToDark');
    b.title = lbl; b.setAttribute('aria-label', lbl); b.setAttribute('aria-pressed', String(dark));
    b.innerHTML = dark
      ? '<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="3.2" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M8 1v1.8M8 13.2V15M1 8h1.8M13.2 8H15M3 3l1.3 1.3M11.7 11.7L13 13M3 13l1.3-1.3M11.7 4.3L13 3" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>'
      : '<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.5 9.6A5.8 5.8 0 0 1 6.4 2.5a5.8 5.8 0 1 0 7.1 7.1z" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg>';
  }
  function setTheme(th, save) {
    if (th === 'light' || th === 'dark') document.documentElement.dataset.theme = th; else document.documentElement.removeAttribute('data-theme');
    if (save) store.set('lhd-theme', th);
    syncTheme(); if (S.data) render();
  }
  { const th0 = store.get('lhd-theme'); if (th0 === 'light' || th0 === 'dark') document.documentElement.dataset.theme = th0; }
  if (mqDark && mqDark.addEventListener) mqDark.addEventListener('change', syncTheme);

  const S = {
    data: null, eraId: 'modernism', px: 0, zoomed: false, info: false, help: false, review: false,
    lang: (store.get('lhd-lang') || 'es') === 'en' ? 'en' : 'es',
    scale: store.get('lhd-scale') === 'linear' ? 'linear' : 'uneven',
    ctxShow: { political: true, economic: true, social: true, cultural: true, technological: true, production: true, theory: true },
    disc: new Set(DISCS), regions: new Set(REGIONS), iso: null, isoPrev: null, types: new Set(TYPES), level: LEVELS.includes(store.get('lhd-level')) ? store.get('lhd-level') : 'normal',
    connAll: store.get('lhd-conn2') !== '0', connPrev: null, showEraCard: false,   // connection curves on/off (the lens turns them on)
    focus: null, scope: null, SC: null, scopeSnap: null, cardOwner: null, arrange: ['chrono', 'date', 'disc', 'region'].includes(store.get('lhd-arrange')) ? store.get('lhd-arrange') : 'chrono', collapsed: new Set(), sel: null, hover: null, pos: new Map()
  };
  const idx = {};
  const G = { map: new Map(), eras: [], eraById: new Map(), stats: {} };
  const t = (k) => (UI[S.lang][k] != null ? UI[S.lang][k] : UI.en[k]);
  // edit mode (?editar): replaced by the real module further down when the address asks for it
  let ED = { on: false, state: () => null, img: () => null, pencil: () => '', init: async () => {}, reviewHtml: () => '', summaryCard: () => '', panelClick: () => false };
  // ---------- Helpers ----------
  const esc = (s) => String(s == null ? '' : s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const norm = (s) => String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[’']/g, '');
  const R = (n) => Math.round(n * 10) / 10;
  const nfl = (n) => Number(n).toLocaleString(S.lang === 'es' ? 'es-ES' : 'en-US');
  const fmtR = (a, b) => a + '–' + b;
  const tx = (it, f) => (it && S.lang === 'es' && it.es && it.es[f]) || (it ? it[f] : '');
  // ---------- Sources (v21, point 44): [n] markers in the texts and numbered refs ----------
  // Public site: the markers are removed from every text. Edit mode (logged in): each marker becomes a token
  // ⟦owner|n⟧ that renderPanel turns into a superscript pointing to the "Sources" list of the review section.
  const RF = { list: [], owners: new Map(), mode: null };
  const RF_MARK = /\s?\[(\d{1,2})\]/g;
  const RF_TOK = /⟦([^|⟧]+)\|(\d{1,2})⟧/g;
  const RF_SKIP = new Set(['refs', 'where', 'sources', 'links', 'id', 'wiki', 'img', 'designers', 'movements', 'institutions', 'tech', 'parts', 'regions', 'countries', 'disciplines', 'terms', 'maker', 'client', 'ctx', 'item', 'from', 'to', 'track']);
  function rfCollect(o, owner) {
    Object.keys(o).forEach((k) => {
      if (RF_SKIP.has(k)) return;
      const v = o[k];
      if (typeof v === 'string') { if (/\[\d{1,2}\]/.test(v)) RF.list.push([o, k, v, owner]); } else if (v && typeof v === 'object') rfCollect(v, owner);
    });
  }
  function rfPrepare(d) {
    ['movements', 'institutions', 'designers', 'works', 'contexts', 'production', 'theories'].forEach((k) => (d[k] || []).forEach((it) => { RF.owners.set(it.id, { refs: it.refs || [] }); rfCollect(it, it.id); }));
    (d.ctxLinks || []).forEach((l) => { const key = 'L:' + l.ctx + '~' + l.item; RF.owners.set(key, { refs: l.refs || [], link: l }); rfCollect(l, key); });
    (d.connections || []).forEach((c) => { const key = 'C:' + c.from + '~' + c.to; RF.owners.set(key, { refs: c.refs || [], conn: c }); rfCollect(c, key); });
  }
  function rfMode(on) {
    on = !!on;
    if (RF.mode === on) return;
    RF.mode = on;
    RF.list.forEach(([o, k, raw, owner]) => { o[k] = on ? raw.replace(RF_MARK, (m, n) => `⟦${owner}|${n}⟧`) : raw.replace(RF_MARK, ''); });
  }
  const rfPlain = (s) => String(s == null ? '' : s).replace(RF_TOK, '');
  const paras = (s) => String(s || '').split(/\n\s*\n/).map((p) => `<p>${esc(p.trim())}</p>`).join('');
  const TL_FONT = "'IBM Plex Sans', system-ui, sans-serif";
  const mctx = document.createElement('canvas').getContext('2d');
  const twCache = new Map();
  function tw(text, size = 11, weight = 400) {
    const k = size + '|' + weight + '|' + text;
    let v = twCache.get(k);
    if (v == null) { mctx.font = `${weight} ${size}px ${TL_FONT}`; v = mctx.measureText(text).width; twCache.set(k, v); }
    return v;
  }
  function pack(list, range) {
    const rows = [];
    for (const it of list) {
      const [a, b] = range(it);
      let r = rows.findIndex((end) => end <= a);
      if (r < 0) { r = rows.length; rows.push(b); } else rows[r] = b;
      it._row = r;
    }
    return rows.length;
  }
  const enc = encodeURIComponent;
  const wikiUrl = (w) => 'https://en.wikipedia.org/wiki/' + encodeURI(w);
  const commons = (q) => 'https://commons.wikimedia.org/w/index.php?search=' + enc(q) + '&title=Special:MediaSearch&type=image';
  const typeLabel = (ty) => (S.lang === 'es' ? TYPE_ES[ty] || ty : ty);
  const DESIGN_KINDS = ['movement', 'institution', 'designer', 'work'];
  const kindOf = (id) => idx.kind.get(id) || (G.map.get(id) || {}).kind || null;

  // ---------- Data index ----------
  function buildIndex(d) {
    idx.byId = new Map(); idx.kind = new Map();
    const add = (kind, list) => (list || []).forEach((it) => { idx.byId.set(it.id, it); idx.kind.set(it.id, kind); });
    add('movement', d.movements); add('institution', d.institutions); add('designer', d.designers); add('work', d.works);
    add('context', d.contexts); add('production', d.production); add('theory', d.theories); add('concept', d.concepts);
    const push = (m, k, v) => { if (!m.has(k)) m.set(k, []); m.get(k).push(v); };
    idx.linksByItem = new Map(); idx.linksByCtx = new Map();
    (d.ctxLinks || []).forEach((ln) => { push(idx.linksByItem, ln.item, ln); push(idx.linksByCtx, ln.ctx, ln); });
    idx.worksByDesigner = new Map(); idx.worksByMaker = new Map(); idx.worksByMovement = new Map();
    d.works.forEach((w) => {
      (w.designers || []).forEach((x) => push(idx.worksByDesigner, x, w));
      [w.maker, w.client].forEach((x) => { if (x && idx.byId.has(x)) push(idx.worksByMaker, x, w); });
      (w.movements || []).forEach((x) => push(idx.worksByMovement, x, w));
    });
    idx.worksByDesigner.forEach((l) => l.sort((a, b) => a.year - b.year));
    idx.designersByMovement = new Map(); idx.designersByInst = new Map();
    d.designers.forEach((a) => {
      (a.movements || []).forEach((x) => push(idx.designersByMovement, x, a));
      (a.institutions || []).forEach((x) => push(idx.designersByInst, x, a));
    });
    d.institutions.forEach((i) => ((i.links || {}).designers || []).forEach((x) => { const a = idx.byId.get(x); if (a && !(idx.designersByInst.get(i.id) || []).includes(a)) push(idx.designersByInst, i.id, a); }));
    // production and theory linked to each design element
    idx.prodByItem = new Map(); idx.theoryByItem = new Map();
    const linkIds = (lk) => [].concat(lk.movements || [], lk.institutions || [], lk.designers || [], lk.works || []);
    (d.production || []).forEach((p) => linkIds(p.links || {}).forEach((i) => push(idx.prodByItem, i, p.id)));
    d.works.forEach((w) => (w.tech || []).forEach((p) => { if (!(idx.prodByItem.get(w.id) || []).includes(p)) push(idx.prodByItem, w.id, p); }));
    (d.theories || []).forEach((th) => linkIds(th.links || {}).forEach((i) => push(idx.theoryByItem, i, th.id)));
    idx.conn = new Map();
    (d.connections || []).forEach((c) => {
      [c.from, c.to].forEach((id) => { if (!idx.conn.has(id)) idx.conn.set(id, []); });
      idx.conn.get(c.from).push({ other: c.to, c, dir: 'to' });
      idx.conn.get(c.to).push({ other: c.from, c, dir: 'from' });
    });
    // concepts: an item is linked to a concept when its English text contains one of the concept's terms
    idx.itemConcepts = new Map(); idx.conceptItems = new Map();
    idx.concepts = d.concepts || [];
    const texts = [];
    ['movements', 'institutions', 'designers', 'works', 'contexts', 'production', 'theories'].forEach((k) => (d[k] || []).forEach((it) => texts.push([it.id, norm([it.key, it.more, it.context, it.shift, it.effect, it.happened, it.origin, it.enabled, it.change, it.relations, it.economy, it.impact, (it.ideas || []).join(' ')].join(' '))])));
    d.concepts.forEach((c) => {
      const terms = (c.terms || [c.name]).map(norm);
      const hits = [];
      texts.forEach(([id, tt]) => { if (terms.some((term) => tt.includes(term))) hits.push(id); });
      idx.conceptItems.set(c.id, hits);
      hits.forEach((id) => { if (!idx.itemConcepts.has(id)) idx.itemConcepts.set(id, []); idx.itemConcepts.get(id).push(c.id); });
    });
    // who uses each productive item (through its links and through the "tech" of the works)
    idx.techUsers = new Map();
    (d.production || []).forEach((p) => linkIds(p.links || {}).forEach((x) => push(idx.techUsers, p.id, x)));
    d.works.forEach((w) => (w.tech || []).forEach((p) => { if (!(idx.techUsers.get(p) || []).includes(w.id)) push(idx.techUsers, p, w.id); }));
  }
  // ---------- Filters ----------
  const regionOk = (it) => {
    const r = it.regions || [];
    return r.includes('global') || r.some((x) => S.regions.has(x));
  };
  const discOk = (it) => (it.disciplines || []).some((x) => S.disc.has(x));
  // "only its connections" (button on a card) and the focus on a context row both hide what is not connected
  const isoOk = (id) => !S.iso || S.iso.set.has(id);
  const focOk = (id) => !S.F || S.F.ids.has(id);
  const keepOk = (id) => isoOk(id) && focOk(id);
  // detail level (v20): an element shows when its level is at or below the chosen one (context is always shown)
  const levelOk = (it) => !it.level || LEVEL_RANK[it.level] <= LEVEL_RANK[S.level];
  const workShown = (w) => S.disc.has(w.discipline) && levelOk(w) && regionOk(w);
  const workOk = (w) => S.types.has('works') && workShown(w) && keepOk(w.id);
  // a designer shows when one of their disciplines is on OR one of their works is visible; on the line, only works of the active disciplines
  const designerVisible = (a) => {
    if (!S.types.has('designers') || !regionOk(a) || !levelOk(a)) return false;
    const ws = idx.worksByDesigner.get(a.id) || [];
    const base = discOk(a) || ws.some(workShown);
    if (!base) return false;
    return keepOk(a.id) || ws.some(workOk);   // kept when connected, or when it holds a connected work (point 93: also with a focus; those entering only by a work are drawn faint, class ind)
  };
  const scOk = (id) => !!(S.SC && S.SC.ids.has(id));
  const movementVisible = (m) => S.types.has('movements') && regionOk(m) && (discOk(m) || scOk(m.id)) && levelOk(m) && keepOk(m.id);
  const institutionVisible = (i) => S.types.has('institutions') && regionOk(i) && (discOk(i) || scOk(i.id)) && levelOk(i) && keepOk(i.id);
  const ctxVisible = (c) => regionOk(c) && isoOk(c.id) && (!S.SC || S.SC.facts.has(c.id));
  const prodVisible = (p) => regionOk(p) && isoOk(p.id) && (!S.SC || S.SC.facts.has(p.id));
  const theoryVisible = (th) => S.types.has('theory') && regionOk(th) && levelOk(th) && keepOk(th.id) && (!S.SC || S.SC.ids.has(th.id));

    const ctxKeys = () => TRACKS.map((x) => 'trk:' + x).concat(['trk:production'], PSUBS.map((x) => 'psub:' + x));
  const allKeys = () => ctxKeys();
  // the context keys that are on screen now (with a lens, only the lens row); sub-rows count only when their row is open
  function ctxShownKeys() {
    const out = [];
    TRACKS.concat(['production']).forEach((tr) => {
      if (S.focus ? S.focus !== tr : !S.ctxShow[tr]) return;
      out.push('trk:' + tr);
      if (tr === 'production' && isOpen('trk:production')) PSUBS.forEach((x) => out.push('psub:' + x));
    });
    return out;
  }
  // ---------- Dates ----------
  const arrowTxt = (a) => a + ' →';
  function dateOf(it) {
    const k = idx.kind.get(it.id) || it._kind;
    if (k === 'movement') return fmtR(it.start, it.end);
    if (k === 'institution') return it.end == null ? arrowTxt(it.start) : fmtR(it.start, it.end);
    if (k === 'designer') return tx(it, 'dates') || (it.died == null ? t('since') + ' ' + it.born : fmtR(it.born, it.died));
    if (k === 'work') return tx(it, 'date') || String(it.year);
    if (k === 'theory') return tx(it, 'date') || String(it.year);
    if (k === 'context' || k === 'production') return tx(it, 'date') || (it.end ? fmtR(it.start, it.end) : it.cont ? arrowTxt(it.start) : String(it.start));
    return '';
  }
  function yearOf(it) {
    const k = idx.kind.get(it.id);
    return k === 'designer' ? it.born : k === 'work' || k === 'theory' ? it.year : it.start || 0;
  }
  const nameOf = (it) => tx(it, 'title') || tx(it, 'name');
  // timeline labels: short, and never with parentheses (the card keeps the long name)
  const plain = (x) => String(x == null ? '' : x).replace(/\s*\([^)]*\)/g, '').replace(/\s{2,}/g, ' ').trim();
  const lab = (it) => plain(tx(it, 'short') || nameOf(it));
  const trackOf = (id) => { const it = idx.byId.get(id); const k = idx.kind.get(id); return k === 'context' ? it.track : k === 'production' ? 'production' : null; };
  const trLabel = (id) => t('tr_' + id);
  const discLabel = (it) => (it.disciplines || []).map((x) => t('d_' + x)).join(', ');
  // ---------- Relations (first degree: what lights up and gets a curve when something is selected) ----------
  // type: 'ctx' (context links, productive and theoretical items), 'works' (a work at one end) or 'other'.
  function relations(id) {
    const out = [], seen = new Set();
    if (!id || !idx.byId.has(id)) return out;
    const k = idx.kind.get(id), it = idx.byId.get(id);
    const add = (o, type, note, tone, via) => {
      if (!o || o === id || !idx.byId.has(o)) return;
      const key = o + '|' + type;
      if (seen.has(key)) { if (note) { const r = out.find((x) => x.other === o && x.type === type); if (r && !r.note) r.note = note; } return; }
      seen.add(key); out.push({ other: o, type, note: note || '', tone: tone || null, via: via || null });
    };
    const lk = it.links || {};
    const linkIds = [].concat(lk.movements || [], lk.institutions || [], lk.designers || [], lk.works || []);
    if (k === 'context') (idx.linksByCtx.get(id) || []).forEach((l) => add(l.item, 'ctx', tx(l, 'note'), it.track));
    else if (k === 'production') {
      linkIds.forEach((x) => add(x, 'ctx', '', k));
      (idx.techUsers.get(id) || []).forEach((x) => add(x, 'ctx', '', k));
    } else {
      (idx.linksByItem.get(id) || []).forEach((l) => add(l.ctx, 'ctx', tx(l, 'note'), l.track));
      (idx.prodByItem.get(id) || []).forEach((p) => add(p, 'ctx', '', 'production'));
    }
    const des = (o) => add(o, k === 'work' || idx.kind.get(o) === 'work' ? 'works' : 'other');
    // theory is design since v18: its links are design relations
    if (k === 'theory') linkIds.forEach(des);
    else (idx.theoryByItem.get(id) || []).forEach(des);
    if (k === 'work') {
      (it.designers || []).forEach(des); des(it.maker); des(it.client); (it.movements || []).forEach(des);
    } else if (k === 'designer') {
      (idx.worksByDesigner.get(id) || []).forEach((w) => des(w.id)); (it.movements || []).forEach(des); (it.institutions || []).forEach(des);
    } else if (k === 'institution') {
      linkIds.forEach(des); (idx.designersByInst.get(id) || []).forEach((a) => des(a.id)); (idx.worksByMaker.get(id) || []).forEach((w) => des(w.id));
    } else if (k === 'movement') {
      (idx.designersByMovement.get(id) || []).forEach((a) => des(a.id)); (idx.worksByMovement.get(id) || []).forEach((w) => des(w.id));
    }
    (idx.conn.get(id) || []).forEach((c) => add(c.other, 'other', (c.dir === 'to' ? '→ ' : '← ') + tx(c.c, 'note')));
    // v20: indirect relations, the same ones the card shows ("Via …"); added after the direct ones, so a direct
    // relation always wins. They are drawn with a thinner line and count for "only its connections".
    if (k === 'designer') (idx.worksByDesigner.get(id) || []).forEach((w) => (idx.linksByItem.get(w.id) || []).forEach((l) => add(l.ctx, 'ctx', tx(l, 'note'), l.track, w.id)));
    if (k === 'work') (it.designers || []).forEach((dn) => { const a = idx.byId.get(dn); if (a) [].concat(a.movements || [], a.institutions || []).forEach((x) => add(x, 'other', '', null, dn)); });
    if (k === 'context') (idx.linksByCtx.get(id) || []).forEach((l) => { if (idx.kind.get(l.item) === 'work') (idx.byId.get(l.item).designers || []).forEach((dn) => add(dn, 'ctx', tx(l, 'note'), it.track, l.item)); });
    if (k === 'movement' || k === 'institution') (k === 'movement' ? idx.designersByMovement : idx.designersByInst).get(id)?.forEach((a) => (idx.worksByDesigner.get(a.id) || []).forEach((w) => { if (it.macro) return; const y1 = it.end != null ? it.end : NOWY(); if (w.year >= it.start && w.year <= y1) add(w.id, 'works', '', null, a.id); }));
    return out;
  }
  function relatedIds(id) {
    return new Set(relations(id).map((r) => r.other));
  }

  // ---------- Focus on one context row ----------
  // The facts of that row stay visible; the design they explain lights up in the row colour and the rest dims.
  function makeFocus(track) {
    const d = S.data, ids = new Set(), facts = new Set();
    if (track === 'production') {
      d.production.filter((p) => regionOk(p)).forEach((p) => {
        facts.add(p.id);
        relations(p.id).forEach((r) => ids.add(r.other));
      });
    } else {
      (d.ctxLinks || []).forEach((ln) => {
        const c = idx.byId.get(ln.ctx);
        if (ln.track === track && c && regionOk(c)) { ids.add(ln.item); facts.add(ln.ctx); }
      });
    }
    return { track, ids, facts };
  }
  // state of the lens, without drawing. Turning one on: the curves come on (their previous state comes back when no lens is
  // left), the card shows the lens, and every design part with connected elements opens.
  // A "photo" is taken when the first lens comes on (sections, Connections, the card and the view) and everything
  // comes back when the last lens goes off. partial: only sections and Connections (leaving the lens by choosing
  // something else, which then opens its own card).
  function applyFocus(track, o = {}) {
    const next = track && track !== S.focus ? track : null;
    if (next && !S.focus) {
      const vp = $('viewport');
      S.focusSnap = { collapsed: new Set(S.collapsed), conn: S.connAll, sel: S.sel, info: S.info, review: S.review, showEraCard: S.showEraCard, eraId: S.eraId,
        year: S.data ? yearAtX(vp.scrollLeft + vp.clientWidth / 2) : null, top: vp.scrollTop };
    }
    if (!next && S.focus && S.focusSnap) {
      const f = S.focusSnap; S.focusSnap = null;
      S.collapsed = f.collapsed; S.connAll = f.conn;
      if (!o.partial) {
        S.sel = f.sel && idx.byId.has(f.sel) ? f.sel : null; S.info = f.info; S.review = f.review; S.showEraCard = f.showEraCard; S.eraId = f.eraId;
        setHash(S.sel);
        S.pendingScroll = { year: f.year, top: f.top };
      }
    }
    S.focus = next;
    if (!next) return;
    S.cardOwner = 'focus';
    S.connAll = true;
    S.ctxShow[next] = true;
    S.sel = null; S.info = false; S.review = false; S.showEraCard = false; setHash(null);
    ctxKeys().filter((k) => keyTrack(k) === next).forEach((k) => S.collapsed.delete(k));
    [...S.collapsed].forEach((k) => { if (/^[gbz]:/.test(k)) S.collapsed.delete(k); });
  }
  function setFocus(track) {
    applyFocus(track);
    if (S.focus) S.pendingScroll = { year: null, top: 0 };
    render();
  }
  // ---------- Scope by discipline (stage 8) ----------
  // One discipline at a time. Works of that discipline only; designers, movements, institutions and theory linked to them;
  // context facts only when they are directly linked to a design item that stays visible.
  function makeScope(disc) {
    const d = S.data, ids = new Set(), facts = new Set(), works = d.works.filter((w) => w.discipline === disc && regionOk(w));
    const wsel = new Set(works.map((w) => w.id)), mset = new Set(), iset = new Set(), desg = new Set();
    works.forEach((w) => { ids.add(w.id); (w.movements || []).forEach((x) => mset.add(x)); [w.maker, w.client].forEach((x) => { if (x) iset.add(x); }); });
    d.designers.forEach((a) => {
      if ((a.disciplines || []).includes(disc) || (idx.worksByDesigner.get(a.id) || []).some((w) => wsel.has(w.id))) {
        ids.add(a.id); desg.add(a.id);
        (a.institutions || []).forEach((x) => iset.add(x)); (a.movements || []).forEach((x) => mset.add(x));
      }
    });
    d.movements.forEach((m) => { if ((m.disciplines || []).includes(disc) || mset.has(m.id)) ids.add(m.id); });
    d.institutions.forEach((i) => { if ((i.disciplines || []).includes(disc) || iset.has(i.id)) ids.add(i.id); });
    const lk = (it) => [].concat(...['movements', 'institutions', 'designers', 'works'].map((k) => (it.links || {})[k] || []));
    d.theories.forEach((th) => { if (lk(th).some((x) => ids.has(x))) ids.add(th.id); });
    const cnt = new Map();
    (d.ctxLinks || []).forEach((ln) => { if (ids.has(ln.item)) { facts.add(ln.ctx); cnt.set(ln.ctx, (cnt.get(ln.ctx) || 0) + 1); } });
    d.production.forEach((p) => { const n = relations(p.id).filter((r) => ids.has(r.other)).length; if (n) { facts.add(p.id); cnt.set(p.id, n); } });
    return { disc, ids, facts, cnt, nWorks: works.length, nDesigners: desg.size };
  }
  // same idea as the lens: a "photo" when it comes on, everything back when it goes off (unless a lens is still on)
  function applyScope(disc) {
    const next = disc && disc !== S.scope ? disc : null;
    if (next && !S.scope) {
      const vp = $('viewport');
      S.scopeSnap = { collapsed: new Set(S.collapsed), sel: S.sel, info: S.info, review: S.review, showEraCard: S.showEraCard, eraId: S.eraId,
        year: S.data ? yearAtX(vp.scrollLeft + vp.clientWidth / 2) : null, top: vp.scrollTop };
    }
    if (!next && S.scope && S.scopeSnap) {
      const f = S.scopeSnap; S.scopeSnap = null;
      if (!S.focus) {
        S.collapsed = f.collapsed;
        S.sel = f.sel && idx.byId.has(f.sel) ? f.sel : null; S.info = f.info; S.review = f.review; S.showEraCard = f.showEraCard; S.eraId = f.eraId;
        setHash(S.sel);
        S.pendingScroll = { year: f.year, top: f.top };
      }
    }
    S.scope = next;
    if (!next) return;
    S.cardOwner = 'scope';
    S.sel = null; S.info = false; S.review = false; S.showEraCard = false; setHash(null);
    [...S.collapsed].forEach((k) => { if (/^[gbz]:/.test(k)) S.collapsed.delete(k); });
  }
  function setScope(disc) {
    applyScope(disc);
    if (S.scope) S.pendingScroll = { year: null, top: 0 };
    render();
  }
  // which card the panel shows when nothing is selected: the last of focus / scope that was turned on
  const cardKind = () => (S.focus && S.scope ? S.cardOwner || 'focus' : S.focus ? 'focus' : S.scope ? 'scope' : null);
  // ---------- Essays (stage 8): data/essays.json is loaded the first time a focus or discipline card opens ----------
  const ES = { map: null, loading: false };
  function essayOf(id) {
    if (ES.map) return ES.map.get(id) || null;
    if (!ES.loading) {
      ES.loading = true;
      fetch('data/essays.json').then((r) => r.json()).then((j) => { ES.map = new Map((j.essays || []).map((e) => [e.id, e])); renderPanel(); })
        .catch(() => { ES.map = new Map(); });
    }
    return null;
  }
  const essayLang = (e) => (S.lang === 'es' && e.es ? e.es : e);
  const essayMin = (e) => Math.max(1, Math.round(essayLang(e).paras.join(' ').replace(/\[\d{1,2}\]/g, '').split(/\s+/).length / 200));
  const ESS_LINK = /\[\[([^\]|]+)(?:\|([^\]]*))?\]\]/g;
  // R2.3: the [n] marks of an essay become superscripts that point to the essay's own sources list (essaySources)
  const essayMarks = (s) => esc(s).replace(/\[(\d{1,2})\]/g, (m, n) => `<sup class="rf"><a href="#rf-${n}" data-rf="${n}">${n}</a></sup>`);
  function essayText(p) {
    let out = '', last = 0, m;
    ESS_LINK.lastIndex = 0;
    while ((m = ESS_LINK.exec(p))) {
      out += essayMarks(p.slice(last, m.index));
      const id = m[1], it = idx.byId.get(id), name = m[2] || (it ? nameOf(it) : id), kd = idx.kind.get(id), tn = it ? toneOf(id) : null;
      out += it ? `<button class="el-link" data-go="${esc(id)}" data-k="${esc(kd)}"${tn ? ` style="--lk:var(--t-${tn})"` : ''}>${esc(name)}</button>` : esc(name);
      last = m.index + m[0].length;
    }
    return out + essayMarks(p.slice(last));
  }
  const essayParas = (e) => essayLang(e).paras.map((p) => `<p>${essayText(p)}</p>`).join('');
  const warnIcon = () => '<svg class="rf-warn" aria-hidden="true" width="13" height="13" viewBox="0 0 16 16"><path d="M8 1.8L15 14H1z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M8 6.2v3.8M8 12v.1" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>';
  const essayWarn = (e) => (e && !(e.refs || []).length ? `<div class="unrev-note" title="${esc(t('unrevTip'))}">${warnIcon()}${esc(t('unrevShort'))}</div>` : '');
  // with a lens on, the curves and highlights to context only go to facts of that lens
  const relFocus = (rs) => (S.focus ? rs.filter((r) => r.type !== 'ctx' || r.tone === S.focus) : rs);
  // ---------- Scale (one continuous line, 1750–today) ----------
  // Two modes. Linear: every year is as wide as any other. Uneven ("by density"): each decade gets a width that grows
  // with the number of elements that start in it (square root, so a full decade does not crush the rest), with a
  // minimum width so that empty decades stay visible. The zoom (S.px) multiplies the whole scale.
  const SC = { key: null, dec: [], total: 1, wmax: 1, y1: 2026 };
  function buildScale() {
    const d = S.data;
    const y1 = Math.max(...G.eras.map((e) => e.end), new Date().getFullYear());
    const key = S.scale + '|' + y1;
    if (SC.key === key) return;
    const n = Math.ceil((y1 - LINE_START) / 10);
    const counts = new Array(n).fill(0);
    const bump = (y) => { if (typeof y === 'number') { const i = Math.floor((y - LINE_START) / 10); if (i >= 0 && i < n) counts[i]++; } };
    d.works.forEach((w) => bump(w.year)); d.theories.forEach((x) => bump(x.year));
    [d.contexts, d.production, d.movements, d.institutions].forEach((l) => l.forEach((x) => bump(x.start)));
    SC.dec = []; let u = 0; SC.wmax = 1;
    for (let i = 0; i < n; i++) {
      const w = S.scale === 'linear' ? 1 : Math.max(1, Math.sqrt(counts[i] / 2));
      SC.dec.push({ y: LINE_START + i * 10, u0: u, w, n: counts[i] });
      u += 10 * w; SC.wmax = Math.max(SC.wmax, w);
    }
    SC.y1 = y1; SC.key = key;
    SC.total = U(y1);
  }
  const decAt = (y) => SC.dec[Math.max(0, Math.min(SC.dec.length - 1, Math.floor((y - LINE_START) / 10)))];
  const U = (y) => { const k = decAt(y); return k.u0 + (y - k.y) * k.w; };
  function yearAtU(u) {
    let k = SC.dec[0];
    for (const x of SC.dec) { if (x.u0 <= u) k = x; else break; }
    return k.y + (u - k.u0) / k.w;
  }
  const lp = (y) => S.px * decAt(y).w;                         // local pixels per year
  const lod = (y) => { const p = lp(y); return p >= LOD_NEAR ? 2 : p >= LOD_MID ? 1 : 0; };

  // ---------- Layout ----------
  const L = { x0: PADL, w: 0, h: 0, fit: 1, max: 40, vw: 900 };
  const xOf = (y) => L.x0 + U(y) * S.px;
  const yearAtX = (x) => yearAtU((x - L.x0) / S.px);
  const NOWY = () => SC.y1;
  const CARET_DOWN = '<svg width="10" height="10" viewBox="0 0 10 10" aria-hidden="true"><path d="M2,3.5 L5,6.5 L8,3.5" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  const CARET_RIGHT = '<svg width="10" height="10" viewBox="0 0 10 10" aria-hidden="true"><path d="M3.5,2 L6.5,5 L3.5,8" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  const DOUBLE_DOWN = '<svg width="10" height="12" viewBox="0 0 10 12" aria-hidden="true"><path d="M2,2 L5,5 L8,2 M2,6.5 L5,9.5 L8,6.5" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  const DOUBLE_UP = '<svg width="12" height="10" viewBox="0 0 12 10" aria-hidden="true"><path d="M2,2 L5,5 L2,8 M6.5,2 L9.5,5 L6.5,8" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  const FOCUS_ICON = '<svg width="12" height="12" viewBox="0 0 12 12" aria-hidden="true"><circle cx="6" cy="6" r="4.4" fill="none" stroke="currentColor" stroke-width="1.3"/><circle cx="6" cy="6" r="1.6" fill="currentColor"/></svg>';

  function setBase() {
    buildScale();
    L.vw = $('viewport').clientWidth || 900;
    L.x0 = PADL;
    L.fit = Math.max(0.05, (L.vw - PADL - PADR) / SC.total);
    L.max = Math.max(L.fit, MAX_LOCAL_PX / SC.wmax);
    if (!S.px || S.px < L.fit) S.px = L.fit;
    if (S.px > L.max) S.px = L.max;
    L.w = Math.ceil(L.x0 + SC.total * S.px + PADR);
  }

  function tickYears() {
    const steps = [1, 2, 5, 10, 25, 50, 100];
    const out = []; let last = -1e9;
    for (let y = LINE_START; y <= NOWY(); y++) {
      const st = steps.find((s) => s * lp(y) >= 46) || 100;
      if (y % st) continue;
      const x = xOf(y);
      if (x - last < 40) continue;
      out.push(y); last = x;
    }
    return out;
  }
  // where the uneven scale changes clearly (marked on the axis)
  function scaleMarks() {
    if (S.scale === 'linear') return [];
    const out = [];
    for (let i = 1; i < SC.dec.length; i++) {
      const r = SC.dec[i].w / SC.dec[i - 1].w;
      if (r > 1.3 || r < 1 / 1.3) out.push({ y: SC.dec[i].y, r });
    }
    return out;
  }

  // v19 (point 26): a designer's life line takes the colour of their disciplines (curated field, not the visible works):
  // one discipline = its colour; several = alternating 10 px stripes in the order of the field. --dbf is the full-strength
  // version used when the designer is related to the selection.
  const desDiscs = (a) => (a.disciplines || []).filter((k) => DISCS.includes(k));
  function desBar(a) {
    const ds = desDiscs(a);
    if (!ds.length) return '';
    if (ds.length === 1) return `--dbg:rgba(var(--c-${ds[0]}),.55);--dbf:rgb(var(--c-${ds[0]}))`;
    const st = (al) => 'repeating-linear-gradient(90deg,' + ds.map((k, i) => `rgba(var(--c-${k}),${al}) ${i * 10}px ${(i + 1) * 10}px`).join(',') + ')';
    return `--dbg:${st(0.6)};--dbf:${st(1)}`;
  }

  // ---------- Build the rows ----------
  const bandHtml = (cls, top, h, tone, dim, w) => `<div class="band ${cls}${dim ? ' dim' : ''}"${tone ? ` data-t="${tone}"` : ''} style="top:${top}px;height:${h}px;${w ? 'width:' + w : ''}"></div>`;
  function selCls(id) {
    return (S.sel === id ? ' sel' : S.rel && S.rel.has(id) ? ' rel' : '');
  }
  // focus mode: the design explained by the focused facts lights up in the track colour; the rest is dimmed
  const focCls = (id) => (S.F && S.F.ids.has(id) ? ' foc' : '');
  const focTone = (id) => (S.F && S.F.ids.has(id) ? ` data-t="${S.F.track}"` : '');
  const shown = (id) => S.sel === id || (S.rel && S.rel.has(id));
  // v20: ★ after the name of every must-know element on the line (works carry it on their marker)
  const starMark = (it) => (it && it.level === 'essential' ? `<svg class="stm" width="9" height="9" viewBox="0 0 10 10" aria-hidden="true"><path d="${STAR}"/></svg>` : '');
  const obsMark = (id) => (ED.on && ED.state(id) === 'observed' ? '<i class="obs" aria-hidden="true"></i>' : '');

  // section keys: open or closed (focus mode closes the other context rows)
  const keyTrack = (k) => (k.startsWith('trk:') ? k.slice(4) : k.startsWith('psub:') ? 'production' : null);
  function isOpen(k) {
    const tr = keyTrack(k);
    if (S.focus && tr) return tr === S.focus && !S.collapsed.has(k);
    return !S.collapsed.has(k);
  }

  function build() {
    const d = S.data;
    const B = { y: 0, cb: [], lb: [], ci: [] };
    S.pos = new Map();
    const band = (cls, h, tone, dim) => { B.cb.push(bandHtml(cls, B.y, h, tone, dim, L.w + 'px')); B.lb.push(bandHtml(cls, B.y, h, tone, dim, '100%')); };
    const labelBtn = (key, text, count, tone, opts = {}) => {
      const open = isOpen(key);
      const sw = opts.sw ? `<i class="sw" style="--tc:${opts.sw}"></i>` : opts.tone ? '<i class="sw"></i>' : '';
      if (opts.focusable) {
        const on = S.focus === opts.focusable, lbl = t(on ? 'focusOff' : 'focusBtn') + ': ' + t('tr_' + opts.focusable);
        B.lb.push(`<div class="lane-label lens-row${on ? ' on' : ''}" data-t="${tone}" style="top:${B.y + 3}px"><button class="car" data-k="${key}" aria-expanded="${open}" aria-label="${esc(t(open ? 'collapse' : 'expand'))}">${open ? CARET_DOWN : CARET_RIGHT}</button><button class="lname" data-focus="${opts.focusable}" aria-pressed="${on}" title="${esc(lbl)}">${sw}<span class="lt">${esc(text)}${count != null ? ` <span class="cnt">${count}</span>` : ''}</span></button></div>`);
        return;
      }
      B.lb.push(`<button class="lane-label${opts.sub ? ' tsub' : ''}" data-k="${key}"${tone ? ` data-t="${tone}"` : ''} aria-expanded="${open}" style="top:${B.y + 4}px"><span class="car">${open ? CARET_DOWN : CARET_RIGHT}</span>${sw}<span class="lt">${esc(text)}${count != null ? ` <span class="cnt">${count}</span>` : ''}</span></button>`);
    };
    const note = (key, text, dim) => B.ci.push(`<button class="collapsed-note${dim ? ' dim' : ''}" data-k="${key}" style="left:${L.x0 + 4}px;top:${B.y + 4}px">${esc(text)}</button>`);
    const hint = (text) => B.ci.push(`<div class="zoom-note" style="left:${L.x0 + 4}px;top:${B.y + 4}px">${esc(text)}</div>`);
    // v19: one double arrow per section that toggles like the single carets (⌄⌄ when something is open, ›› when all is folded).
    // The state is only known once the section is built, so the label is filled in at the end of build().
    B.sec = {};
    const secHead = (sec, text) => { B.sec[sec] = { i: B.lb.length, y: B.y, text }; B.lb.push(''); };
    const secFill = (sec, anyOpen) => {
      const h = B.sec[sec]; if (!h) return;
      const l = t(anyOpen ? (sec === 'ctx' ? 'closeCtx' : 'closeDes') : (sec === 'ctx' ? 'openCtx' : 'openDes'));
      B.lb[h.i] = `<div class="sec has-acts" style="top:${h.y + 3}px"><span class="sec-acts"><button class="sec-b" data-secall="${sec}:${anyOpen ? 'close' : 'open'}" aria-expanded="${anyOpen}" title="${esc(l)}" aria-label="${esc(l)}">${anyOpen ? DOUBLE_DOWN : DOUBLE_UP}</button></span><span class="st">${esc(h.text)}</span></div>`;
    };
    // positions for the connection curves; items inside a closed section point at its row
    const at = (id, x, y, extra) => { if (!S.pos.has(id)) S.pos.set(id, Object.assign({ x, y }, extra || {})); };
    const atClosed = (ids, years) => ids.forEach((id, i) => at(id, xOf(years[i]), B.y + 12, { coll: true }));
    const isLong = (s, e) => e != null && e > s && ((e - s) > LONG_YEARS || (xOf(e) - xOf(s)) > L.vw * LONG_FRAC);

    // ---- context-type rows (political … technological, production, theory)
    function ctxPlace(list, kind) {
      const out = [];
      for (const it of list) {
        const s0 = kind === 'theory' ? it.year : it.start;
        const e1 = kind === 'theory' ? null : it.end != null ? it.end : it.cont ? NOWY() : null;
        const hasSpan = e1 != null && e1 > s0;
        const long = hasSpan && isLong(s0, e1) && S.sel !== it.id;
        const showL = shown(it.id) || lod(s0) >= 1;
        const label = lab(it);
        const lw = showL ? tw(label, 11) : 0;
        const a = xOf(s0);
        const o = { it, kind, label, showL, a, long, expanded: hasSpan && S.sel === it.id && isLong(s0, e1) };
        if (hasSpan && !long) {
          o.span = true; o.bw = Math.max(xOf(e1) - a, 6); o.arrR = !!it.cont && it.end != null;
          o.e0 = a; o.e1 = a + Math.max(o.bw + (o.arrR ? 7 : 0), lw + 4) + 8;
        } else {
          o.span = false; o.arrR = long;
          o.e0 = a - 3.5; o.e1 = a + 3.5 + (showL ? 6 + lw : 0) + (long ? 12 : 0) + 8;
        }
        out.push(o);
      }
      out.sort((x, y) => x.e0 - y.e0);
      const rows = pack(out, (o) => [o.e0, o.e1]);
      return { out, rows };
    }
    function ctxHtml(o, top, tone) {
      const it = o.it, base = o.kind === 'production' ? 'prod ' : o.kind === 'theory' ? 'theory ' : '';
      const lbl = o.showL ? `<span class="t">${esc(o.label)}</span>` : '';
      at(it.id, o.a, top + (o.span ? 14 : 8));
      if (o.span) {
        return `<div class="it ${base}ev-span${selCls(it.id)}${o.expanded ? ' expanded' : ''}" data-id="${it.id}" data-t="${tone}" style="left:${R(o.a)}px;top:${top}px;width:${R(o.bw)}px;height:16px"><i class="bar" style="width:${R(o.bw)}px"></i>${o.arrR ? `<i class="ar" style="left:${R(o.bw - 1)}px"></i>` : ''}${o.showL ? `<span class="t" style="position:absolute;left:0;top:0">${esc(o.label)}</span>` : ''}${obsMark(it.id)}</div>`;
      }
      const mark = o.kind === 'theory' ? '<i class="bk"></i>' : '<i class="d"></i>';
      return `<div class="it ${base}ev-pt${o.long ? ' lng' : ''}${selCls(it.id)}" data-id="${it.id}" data-t="${tone}" style="left:${R(o.a - 3.5)}px;top:${top}px">${mark}${lbl}${o.long ? '<i class="lar"></i>' : ''}${obsMark(it.id)}</div>`;
    }
    function ctxBlock(key, tone, text, list, kind, opts = {}) {
      const open = isOpen(key);
      const n = list.length;
      if (!open || !n) {
        band('ctx', 24, tone);
        labelBtn(key, text, n, tone, { tone: 1, sub: opts.sub, focusable: opts.focusable });
        if (n) note(key, `${n} ${t(n === 1 ? (opts.noteKey === 'nItems' ? 'nItem1' : 'nFact1') : (opts.noteKey || 'nFacts'))}`);
        atClosed(list.map((x) => x.id), list.map((x) => (kind === 'theory' ? x.year : x.start)));
        B.y += 24; return;
      }
      const { out, rows } = ctxPlace(list, kind);
      const h = Math.max(1, rows) * 19 + 10;
      band('ctx', h, tone);
      labelBtn(key, text, n, tone, { tone: 1, sub: opts.sub, focusable: opts.focusable });
      out.forEach((o) => B.ci.push(ctxHtml(o, B.y + 5 + o._row * 19, tone)));
      B.y += h;
    }

    // ---- CONTEXT
    band('head', 26); secHead('ctx', t('secContext')); B.y += 26;
    for (const tr of TRACKS) {
      if (!S.ctxShow[tr] && S.focus !== tr) continue;
      ctxBlock('trk:' + tr, tr, t('tr_' + tr), d.contexts.filter((c) => c.track === tr && ctxVisible(c)), 'context', { focusable: tr });
    }
    if (S.ctxShow.production || S.focus === 'production') {
      const prods = d.production.filter((p) => prodVisible(p));
      if (!isOpen('trk:production') || !prods.length) {
        ctxBlock('trk:production', 'production', t('tr_production'), prods, 'production', { noteKey: 'nItems', focusable: 'production' });
      } else {
        band('ctx', 24, 'production'); labelBtn('trk:production', t('tr_production'), prods.length, 'production', { tone: 1, focusable: 'production' }); B.y += 24;
        for (const sub of PSUBS) ctxBlock('psub:' + sub, 'production', t('ps_' + sub), prods.filter((p) => p.sub === sub), 'production', { sub: true, noteKey: 'nItems' });
      }
    }
    if (false) ctxBlock('trk:theory', 'theory', t('tr_theory'), d.theories.filter((x) => theoryVisible(x)), 'theory', { noteKey: 'nItems', focusable: 'theory' });

    // ---- DESIGN (v18): the era bar, then the design arranged by category, by date, by discipline or by region.
    // Every group and sub-group folds with its caret (keys g:<view>:<group>, b:<view>:<group>:<block>, z:region:<region>:<zone>).
    band('head', 26); secHead('des', t('secDesign')); B.y += 26;
    S.designKeys = []; S.itemKeys = new Map();
    const NEU = 'var(--c-neutral)', MVT = 'var(--ink-2)';
    const dateView = S.arrange === 'date';
    // "by date" hides the designers (their birth year would put them all at the top), except the selected one
    const selDes = dateView ? [S.sel, S.iso && S.iso.id].find((x) => x && idx.kind.get(x) === 'designer') || null : null;
    const mvAll = d.movements.filter(movementVisible);
    const insAll = d.institutions.filter(institutionVisible);
    const thAll = d.theories.filter(theoryVisible);
    const dsAll = d.designers.filter(designerVisible).filter((a) => !dateView || a.id === selDes);
    const wsAll = d.works.filter(workOk);
    const dsSet = new Set(dsAll.map((a) => a.id));
    const lineOf = (w) => (w.designers || []).find((x) => dsSet.has(x)) || null;   // first visible designer
    const onLine = new Map(), loose = [];
    wsAll.forEach((w) => { const a = lineOf(w); if (a) { if (!onLine.has(a)) onLine.set(a, []); onLine.get(a).push(w); } else loose.push(w); });
    const bothOn = S.types.has('designers') && S.types.has('works') && !dateView;   // works on the lines: no labels
    // level of detail: from far away only movements, theory, must-know works and their designers
    const workLod = (w) => shown(w.id) || w.star || lod(w.year) >= 1 || !!S.F || !!S.SC || !!S.iso;
    const designerYear = (a) => { const ws = idx.worksByDesigner.get(a.id) || []; return ws.length ? ws[0].year : a.born + 35; };
    const designerLod = (a) => shown(a.id) || lod(designerYear(a)) >= 1 || (onLine.get(a.id) || []).some((w) => w.star || shown(w.id)) || !!S.F || !!S.SC || !!S.iso;
    const instLod = (i) => shown(i.id) || lod(i.start) >= 1 || !!S.F || !!S.SC || !!S.iso;
    const insDrawn = insAll.filter(instLod), dsDrawn = dsAll.filter(designerLod), looseDrawn = loose.filter(workLod);
    const hiddenByZoom = insDrawn.length < insAll.length || dsDrawn.length < dsAll.length || looseDrawn.length < loose.length;
    const yearOfIt = (it) => { const k = idx.kind.get(it.id); return k === 'designer' ? designerYear(it) : k === 'work' || k === 'theory' ? it.year : it.start; };
    const nItems = (n) => `${n} ${t(n === 1 ? 'nItem1' : 'nItems')}`;
    // the keys that hold each element (to open them when it is selected)
    let KS = [];
    const reg = (id) => { S.itemKeys.set(id, KS.slice()); };
    const regPart = (P) => {
      ['mv', 'ins', 'th', 'ds', 'lw'].forEach((k) => P[k].forEach((it) => reg(it.id)));
      P.ds.forEach((a) => (onLine.get(a.id) || []).filter((w) => !a.__grp || w.discipline === a.__grp).forEach((w) => reg(w.id)));
    };
    const partIds = (P) => {
      const ids = [], ys = [];
      ['mv', 'ins', 'th', 'ds', 'lw'].forEach((k) => P[k].forEach((it) => { ids.push(it.id); ys.push(yearOfIt(it)); }));
      P.ds.forEach((a) => (onLine.get(a.id) || []).filter((w) => !a.__grp || w.discipline === a.__grp).forEach((w) => { ids.push(w.id); ys.push(w.year); }));
      return [ids, ys];
    };
    const closedAt = (P, y) => { const [ids, ys] = partIds(P); ids.forEach((id, i) => at(id, xOf(ys[i]), y, { coll: true })); };
    const partN = (P) => P.mv.length + P.ins.length + P.th.length + P.ds.length + P.lw.length;
    const caret = (key) => (isOpen(key) ? CARET_DOWN : CARET_RIGHT);
    const capLabel = (cls, key, text, y0, y1, extra) => `<button class="${cls} sticky" data-k="${key}" aria-expanded="${isOpen(key)}"${extra || ''} data-y0="${y0}" data-y1="${Math.max(y0, y1)}" style="top:${y0}px"><span class="car">${caret(key)}</span><span class="lt">${text}</span></button>`;
    const closedNote = (key, n, y) => B.ci.push(`<button class="collapsed-note" data-k="${key}" style="left:${L.x0 + 4}px;top:${y}px">${esc(nItems(n))}</button>`);

    // v24 (point 50): the macro-movements no longer have their own row; they are drawn first in the Movements row, like any movement
    if (hiddenByZoom) B.lb.push(`<div class="lane-hint" style="top:${B.y + 2}px">${esc(t('zoomMore'))}</div>`);

    // ---- painters of each kind; each returns the height used
    function drawMv(y, mv) {
      const ms = mv.map((m) => {
        const e = m.end != null ? m.end : NOWY();
        const long = false;   // v38 (point 70): movements are always drawn over their real span
        const lwm = tw(lab(m), 12, 500);
        // a long macro-movement reserves its whole span, so its label can slide along it (stickyNames) without overlapping
        if (long) { const l = xOf(m.start); return { m, long, l, w: lwm + 22, e0: l, e1: m.macro ? Math.max(xOf(e), l + lwm + 36) : l + lwm + 22 + 14 }; }
        const fi = (m.fadeIn || 0) * lp(m.start), fo = (m.fadeOut || 0) * lp(e);
        const l = Math.max(PADL, xOf(m.start) - fi), r = xOf(e) + fo;
        return { m, long, l, r, fi, fo, w: Math.max(r - l, 8), fit: r - l >= lwm + fi + fo + 10, e0: l, e1: Math.max(r, l + lwm + fi + 10) + 4 };
      }).sort((p, q) => p.e0 - q.e0);
      // macro-movements first, in their own top rows; the other movements below
      const msA = ms.filter((o) => o.m.macro), msB = ms.filter((o) => !o.m.macro);
      const rowsA = msA.length ? pack(msA, (o) => [o.e0, o.e1]) : 0;
      const rows = rowsA + (msB.length ? pack(msB, (o) => [o.e0, o.e1]) : 0);
      msB.forEach((o) => { o._row += rowsA; });
      ms.forEach((o) => {
        const top = y + o._row * 21, c = NEU;
        at(o.m.id, xOf(o.m.start), top + 9);
        if (o.long) {
          B.ci.push(`<div class="it movement lng fit${o.m.macro ? ' mac' : ''}${selCls(o.m.id)}${focCls(o.m.id)}"${focTone(o.m.id)} data-id="${o.m.id}"${o.m.macro ? ` data-x1="${R(o.e1)}"` : ''} style="left:${R(o.l)}px;top:${top}px;width:${R(o.w)}px;height:18px;line-height:18px;padding-left:6px;color:${MVT};background:rgba(${c}, var(--m-alpha))">${esc(lab(o.m))}${starMark(o.m)}<i class="lar"></i>${obsMark(o.m.id)}</div>`);
          return;
        }
        const bg = `linear-gradient(90deg, rgba(${c},0) 0, rgba(${c}, var(--m-alpha)) ${R(o.fi)}px, rgba(${c}, var(--m-alpha)) calc(100% - ${R(o.fo)}px), rgba(${c},0) 100%)`;
        B.ci.push(`<div class="it movement${o.fit ? ' fit' : ''}${selCls(o.m.id)}${focCls(o.m.id)}"${focTone(o.m.id)} data-id="${o.m.id}" data-x1="${R(o.l + o.w)}" data-fi="${R(o.fi + 4)}" style="left:${R(o.l)}px;top:${top}px;width:${R(o.w)}px;height:18px;line-height:18px;padding-left:${R(o.fi + 4)}px;color:${MVT};background:${bg}"><span class="mt">${esc(lab(o.m))}${starMark(o.m)}</span>${obsMark(o.m.id)}</div>`);
      });
      return rows * 21 + 4;
    }
    function drawIns(y, ins) {
      const is = ins.map((i) => {
        const e = i.end != null ? i.end : NOWY();
        const long = isLong(i.start, e) && S.sel !== i.id;
        const a = xOf(i.start), lbl = lab(i), lwi = tw(lbl, 12, 500);
        if (long) return { i, a, w: lwi + 26, lbl, long, fit: true, e0: a, e1: a + lwi + 26 + 16 };
        const w = Math.max(xOf(e) - a, 6) + 8;   // + the tip
        return { i, a, w, lbl, long, fit: w >= lwi + 16, e0: a, e1: a + Math.max(w, lwi + 10) + 6 };
      }).sort((p, q) => p.e0 - q.e0);
      const rows = pack(is, (o) => [o.e0, o.e1]);
      is.forEach((o) => {
        const top = y + o._row * 21;
        at(o.i.id, o.a, top + 9);
        B.ci.push(`<div class="it inst${o.long ? ' lng' : ''}${o.fit ? ' fit' : ''}${selCls(o.i.id)}${focCls(o.i.id)}${S.sel === o.i.id && isLong(o.i.start, o.i.end != null ? o.i.end : NOWY()) ? ' expanded' : ''}"${focTone(o.i.id)} data-id="${o.i.id}" style="left:${R(o.a)}px;top:${top}px;width:${R(o.w)}px"><i class="ib"></i><span class="t">${esc(o.lbl)}${starMark(o.i)}${o.long ? '<i class="lar"></i>' : ''}</span>${obsMark(o.i.id)}</div>`);
      });
      return rows * 21 + 4;
    }
    // theory: book marker + author's surname (the title is in the tooltip and the card)
    function drawTh(y, th) {
      const ts = th.map((x) => { const a = xOf(x.year), lw = tw(lab(x), 11); return { x, a, e0: a - 4, e1: a + 6 + lw + 10 }; }).sort((p, q) => p.e0 - q.e0);
      const rows = pack(ts, (o) => [o.e0, o.e1]);
      ts.forEach((o) => {
        const top = y + o._row * 19;
        at(o.x.id, o.a, top + 8);
        B.ci.push(`<div class="it ev-pt theory${selCls(o.x.id)}${focCls(o.x.id)}"${focTone(o.x.id) || ' data-t="theory"'} data-id="${o.x.id}" style="left:${R(o.a - 3.5)}px;top:${top}px"><i class="bk"></i><span class="t">${esc(lab(o.x))}${starMark(o.x)}</span>${obsMark(o.x.id)}</div>`);
      });
      return rows * 19 + 4;
    }
    function drawDs(y, ds, lw) {
      let y1 = y;
      if (ds.length) {
        const dd = ds.map((a) => {
          const l0 = xOf(a.born), l1 = xOf(a.died == null ? NOWY() : a.died);
          const works = (onLine.get(a.id) || []).filter((w) => !a.__grp || w.discipline === a.__grp).filter(workLod).sort((p, q) => p.year - q.year);
          return { a, l0, l1: Math.max(l1, l0 + 6), works, e0: l0, e1: Math.max(l1, l0 + tw(lab(a), 11) + 8) + 6 };
        }).sort((p, q) => p.e0 - q.e0);
        const nrows = pack(dd, (o) => [o.e0, o.e1]);
        dd.forEach((o) => {
          const a = o.a, top = y1 + o._row * 25;
          at(a.id, o.l0, top + 17);
          B.ci.push(`<div class="it designer${S.F && !S.F.ids.has(a.id) ? ' ind' : ''}${selCls(a.id)}${focCls(a.id)}"${focTone(a.id)} data-id="${a.id}" style="left:${R(o.l0)}px;top:${top}px;width:${R(Math.max(o.l1 - o.l0, 6))}px;height:22px"><span class="nm">${esc(lab(a))}${starMark(a)}${obsMark(a.id)}</span><i class="bar" style="${desBar(a)}"></i></div>`);
          o.works.forEach((w) => {
            at(w.id, xOf(w.year), top + 17, { line: a.id });
            B.ci.push(workHtml(w, xOf(w.year), top + 17, 0, 0, null, null, true));
          });
          (onLine.get(a.id) || []).filter((w) => !a.__grp || w.discipline === a.__grp).forEach((w) => at(w.id, xOf(w.year), top + 17, { line: a.id, hidden: true }));
        });
        y1 += nrows * 25 + 2;
      }
      if (lw.length) {
        // works without a visible designer: grouped by discipline; a discipline may share its first row with the
        // last row of the one before (fewer rows)
        const labels = !bothOn;
        const rows = [];
        let start = 0;
        DISCS.forEach((dc) => {
          const ws = lw.filter((w) => w.discipline === dc).map((w) => {
            const x = xOf(w.year), lbl = lab(w);
            const showL = labels && (shown(w.id) || w.star || lod(w.year) >= 2 || dateView);
            return { w, x, showL, e0: x - 7, e1: x + 7 + (showL ? Math.min(tw(lbl, 10.5, w.star ? 600 : 400), 160) + 6 : 0) };
          }).sort((p, q) => p.e0 - q.e0);
          if (!ws.length) return;
          ws.forEach((o) => {
            let r = -1;
            for (let i = start; i < rows.length; i++) if (rows[i] <= o.e0) { r = i; break; }
            if (r < 0) { r = rows.length; rows.push(o.e1); } else rows[r] = o.e1;
            o._row = r;
          });
          start = Math.max(0, rows.length - 1);
          ws.forEach((o) => {
            const top = y1 + 2 + o._row * 20;
            at(o.w.id, o.x, top + 8);
            B.ci.push(workHtml(o.w, o.x, top + 8, top + 2, o.showL, null, null, false));
          });
        });
        y1 += rows.length * 20 + 4;
      }
      return y1 - y;
    }
    // paint a part (group, zone or row). With prefix: one foldable block per kind, with a faint line and a small
    // name between them (labels go to `labels`, drawn after the band so they stay on top)
    const BLOCKS = [['movements', (P) => P.mv.length, (y, P) => drawMv(y, P.mv)], ['institutions', (P) => P.ins.length, (y, P) => drawIns(y, P.ins)],
      ['theory', (P) => P.th.length, (y, P) => drawTh(y, P.th)], ['designers', (P) => P.ds.length + P.lw.length, (y, P) => drawDs(y, P.ds, P.lw)]];
    const blockPart = (P, name) => ({ mv: name === 'movements' ? P.mv : [], ins: name === 'institutions' ? P.ins : [], th: name === 'theory' ? P.th : [], ds: name === 'designers' ? P.ds : [], lw: name === 'designers' ? P.lw : [] });
    function paintPart(y0, P, prefix, labels, off) {
      let y = y0, nb = 0;
      BLOCKS.forEach(([name, count, draw]) => {
        const n = count(P); if (!n) return;
        if (!prefix) { y += draw(y, P); return; }
        const key = prefix + ':' + name;
        S.designKeys.push(key);
        if (nb++) { B.ci.push(`<div class="zone-line" style="top:${y}px;width:${L.w}px"></div>`); y += 4; }
        const bp = blockPart(P, name), yb = y;
        KS.push(key);
        if (!isOpen(key)) {
          regPart(bp); closedAt(bp, y + 10); closedNote(key, n, y + 4); y += 24;
        } else {
          regPart(bp); y += 2 + draw(y + 2, P);
        }
        KS.pop();
        labels.push(capLabel('zone-label', key, esc(t('dt_' + name)), yb + 1, y - 14, ` data-off="${off}"`));
      });
      if (!prefix) regPart(P);
      return y - y0;
    }
    const emptyPart = () => ({ mv: [], ins: [], th: [], ds: [], lw: [] });

    // ---- by date: one row per element (designers hidden, except the selected one), by decade
    if (dateView) {
      const kindOrder = { mv: 0, ins: 1, th: 2, ds: 3, lw: 4 };
      const rows = [].concat(
        mvAll.map((it) => ({ k: 'mv', it, y: it.start })), insDrawn.map((it) => ({ k: 'ins', it, y: it.start })), thAll.map((it) => ({ k: 'th', it, y: it.year })),
        dsDrawn.map((it) => ({ k: 'ds', it, y: designerYear(it) })), looseDrawn.map((it) => ({ k: 'lw', it, y: it.year }))
      ).sort((p, q) => (p.y - q.y) || (kindOrder[p.k] - kindOrder[q.k]) || lab(p.it).localeCompare(lab(q.it)));
      const decs = new Map();
      rows.forEach((r) => { const dd = Math.floor(r.y / 10) * 10; if (!decs.has(dd)) decs.set(dd, []); decs.get(dd).push(r); });
      const top0 = B.y, labels = [];
      let y = top0 + 4, i = 0;
      decs.forEach((list, dd) => {
        const key = 'g:date:' + dd; S.designKeys.push(key);
        if (i++) { B.ci.push(`<div class="zone-line" style="top:${y}px;width:${L.w}px"></div>`); y += 4; }
        const yb = y;
        KS = [key];
        if (!isOpen(key)) {
          list.forEach((r) => { const P = emptyPart(); P[r.k].push(r.it); regPart(P); closedAt(P, y + 10); });
          closedNote(key, list.length, y + 4); y += 24;
        } else {
          y += 2;
          list.forEach((r) => { const P = emptyPart(); P[r.k].push(r.it); y += paintPart(y, P, null); });
        }
        labels.push(capLabel('zone-label', key, esc(`${dd}–${dd + 9}`), yb + 1, y - 14, ' data-off="4"'));
      });
      KS = [];
      const h = Math.max(y - top0 + 4, 30);
      band('b', h);
      labels.forEach((x) => B.lb.push(x));
      B.y += h;
      if (!rows.length) { band('a', 40); B.ci.push(`<div class="collapsed-note" style="left:${L.x0}px;top:${B.y + 11}px;cursor:default">${esc(t(hiddenByZoom ? 'zoomMore' : 'nothingShown'))}</div>`); B.y += 40; }
      L.h = B.y;
      secFill('ctx', ctxShownKeys().some(isOpen));
      secFill('des', S.designKeys.some(isOpen));
      return B;
    }

    // ---- by category, by discipline, by region
    const groupOf = arrangeGroupOf();
    const groups = new Map();
    const put = (g, kind, it) => { if (!groups.has(g)) groups.set(g, emptyPart()); groups.get(g)[kind].push(it); };
    // 8.6 (point 94): by discipline an element may belong to several groups; a designer is a copy per discipline
    // (class-less proxy carrying __grp: only the works of that discipline hang from it)
    const MG = S.arrange === 'disc';
    const putM = (kind, it) => { if (MG) discGroups(it).forEach((g) => put(g, kind, kind === 'ds' ? Object.assign(Object.create(it), { __grp: g }) : it)); else put(groupOf(it), kind, it); };
    mvAll.forEach((m) => putM('mv', m));
    insDrawn.forEach((i) => putM('ins', i));
    thAll.forEach((x) => putM('th', x));
    dsDrawn.forEach((a) => putM('ds', a));
    looseDrawn.forEach((w) => put(groupOf(w), 'lw', w));
    const order = arrangeOrder().filter((g) => groups.has(g));
    let gN = 0;
    order.forEach((g) => {
      const G1 = groups.get(g), top0 = B.y, labels = [];
      const n = partN(G1);
      const cls = (++gN) % 2 ? 'b' : 'a';
      let h;
      if (S.arrange === 'chrono') {
        KS = [];
        h = 6 + paintPart(top0 + 6, G1, 'b:chrono:all', labels, 4);
      } else {
        const gk = 'g:' + S.arrange + ':' + g; S.designKeys.push(gk);
        KS = [gk];
        if (!isOpen(gk)) {
          regPart(G1); closedAt(G1, top0 + 13);
          band(cls, 28);
          B.lb.push(capLabel('grp-label', gk, `${esc(t('ag_' + g))} <span class="cnt">${n}</span>`, top0 + 5, top0 + 5));
          closedNote(gk, n, top0 + 7);
          B.y += 28; KS = [];
          return;
        }
        h = 24;   // room for the group name
        if (S.arrange === 'region' && REGION_ZONES[g] && (g !== 'global' || G1.mv.concat(G1.ins, G1.th, G1.ds, G1.lw).some((it) => zoneOf(it, g) === 'beyond'))) {
          // faint subdivisions by stable cultural zone, each foldable
          const zones = new Map();
          ['mv', 'ins', 'th', 'ds', 'lw'].forEach((kind) => G1[kind].forEach((it) => { const z = zoneOf(it, g); if (!zones.has(z)) zones.set(z, emptyPart()); zones.get(z)[kind].push(it); }));
          const zorder = REGION_ZONES[g].concat(['other']).filter((z) => zones.has(z));
          zorder.forEach((z, i) => {
            const zy = top0 + h, zk = 'z:region:' + g + ':' + z, Z = zones.get(z);
            S.designKeys.push(zk);
            if (i > 0) B.ci.push(`<div class="zone-line" style="top:${zy - 3}px;width:${L.w}px"></div>`);
            KS = [gk, zk];
            let zh;
            if (!isOpen(zk)) { regPart(Z); closedAt(Z, zy + 10); closedNote(zk, partN(Z), zy + 4); zh = 26; }
            else zh = Math.max(paintPart(zy + 4, Z, null) + 10, 30);
            labels.push(capLabel('zone-label', zk, esc(t('zn_' + z)), zy + 1, zy + zh - 16));
            h += zh;
          });
        } else {
          h += paintPart(top0 + 24, G1, 'b:' + S.arrange + ':' + g, labels, 22);
        }
        labels.unshift(capLabel('grp-label', gk, `${esc(t('ag_' + g))} <span class="cnt">${n}</span>`, top0 + 5, top0 + Math.max(h, 30) - 22));
      }
      KS = [];
      h = Math.max(h + 4, 30);
      band(cls, h);
      labels.forEach((x) => B.lb.push(x));
      B.y += h;
    });
    if (!order.length) {
      band('a', 40);
      B.ci.push(`<div class="collapsed-note" style="left:${L.x0}px;top:${B.y + 11}px;cursor:default">${esc(t(hiddenByZoom ? 'zoomMore' : 'nothingShown'))}</div>`);
      B.y += 40;
    }
    L.h = B.y;
    secFill('ctx', ctxShownKeys().some(isOpen));
    secFill('des', S.designKeys.some(isOpen));
    return B;

    // a work marker, with its label to the right when asked (never on a designer's line)
    function workHtml(w, x, cy, labelTop, showL, _a, _b, onLineW) {
      const dc = w.discipline, c = `var(--c-${dc})`;
      let html = '';
      const gl = `<svg width="12" height="12" viewBox="0 0 10 10" aria-hidden="true"><path class="g" d="${GLYPH[dc]}" fill="rgb(${c})"/>${w.star ? `<path class="st" d="${STAR}" transform="translate(4.6,-6.4) scale(.78)"/>` : ''}</svg>`;
      const rel = S.sel !== w.id && S.rel && S.rel.has(w.id);
      if (S.sel === w.id) html += `<div class="ring" style="left:${R(x)}px;top:${R(cy)}px"></div>`;
      else if (rel) html += `<div class="ring rel" style="left:${R(x)}px;top:${R(cy)}px;border-color:rgb(${c})"></div>`;
      html += `<div class="it work${selCls(w.id)}${focCls(w.id)}"${focTone(w.id)} data-id="${w.id}" style="left:${R(x)}px;top:${R(cy)}px">${gl}${obsMark(w.id)}</div>`;
      if (!onLineW && showL) html += `<span class="wlabel${w.star ? ' star' : ''}${rel ? ' rel' : ''}" data-id="${w.id}" style="${rel ? `color:var(--t-${dc});` : ''}left:${R(x + 9)}px;top:${R(labelTop)}px;max-width:162px;overflow:hidden;text-overflow:ellipsis">${esc(lab(w))}</span>`;
      return html;
    }
  }

  // ---------- Arranging the design (v15) ----------
  // chrono: one group. disc: Interdisciplinary (two or more disciplines) + the four disciplines; a loose work goes by
  // its own discipline. region: Europe, North America, Latin America, Several regions, Global, each region split into
  // stable cultural zones by the element's main country (the first of its countries that belongs to that region).
  const REGION_ZONES = {
    europe: ['british-isles', 'france-benelux', 'germanic', 'central-east', 'russia', 'nordic', 'mediterranean'],
    'north-america': ['usa', 'canada'],
    'latin-america': ['mexico-ca', 'caribbean', 'andes', 'brazil', 'southern-cone'],
    global: ['beyond']   // v31 (point 61): elements from outside the West kept for their influence on Western design
  };
  const ZONE_OF = {
    GB: 'british-isles', IE: 'british-isles',
    FR: 'france-benelux', BE: 'france-benelux', NL: 'france-benelux', LU: 'france-benelux',
    DE: 'germanic', AT: 'germanic', CH: 'germanic', LI: 'germanic',
    CZ: 'central-east', SK: 'central-east', HU: 'central-east', PL: 'central-east', RO: 'central-east', BG: 'central-east', SI: 'central-east', HR: 'central-east', RS: 'central-east', BA: 'central-east', ME: 'central-east', MK: 'central-east', AL: 'central-east', LT: 'central-east', LV: 'central-east', EE: 'central-east',
    RU: 'russia', UA: 'russia', BY: 'russia', GE: 'russia', AM: 'russia', AZ: 'russia', MD: 'russia',
    DK: 'nordic', NO: 'nordic', SE: 'nordic', FI: 'nordic', IS: 'nordic',
    IT: 'mediterranean', ES: 'mediterranean', PT: 'mediterranean', GR: 'mediterranean', MT: 'mediterranean', CY: 'mediterranean',
    US: 'usa', CA: 'canada',
    MX: 'mexico-ca', GT: 'mexico-ca', BZ: 'mexico-ca', HN: 'mexico-ca', SV: 'mexico-ca', NI: 'mexico-ca', CR: 'mexico-ca', PA: 'mexico-ca',
    CU: 'caribbean', DO: 'caribbean', PR: 'caribbean', HT: 'caribbean', JM: 'caribbean',
    CO: 'andes', VE: 'andes', EC: 'andes', PE: 'andes', BO: 'andes',
    BR: 'brazil', CL: 'southern-cone', AR: 'southern-cone', UY: 'southern-cone', PY: 'southern-cone',
    JP: 'beyond', CN: 'beyond', KR: 'beyond', TW: 'beyond', HK: 'beyond', IN: 'beyond', LK: 'beyond', TH: 'beyond', VN: 'beyond', ID: 'beyond', MY: 'beyond', SG: 'beyond', PH: 'beyond', PK: 'beyond', BD: 'beyond', NP: 'beyond', MN: 'beyond',
    IR: 'beyond', IQ: 'beyond', TR: 'beyond', SA: 'beyond', IL: 'beyond', EG: 'beyond', MA: 'beyond', NG: 'beyond', GH: 'beyond', ET: 'beyond', ZA: 'beyond', KE: 'beyond', SN: 'beyond', AU: 'beyond', NZ: 'beyond'
  };
  function regionGroup(it) {
    const rs = (it.regions || []).filter((r) => r !== 'global');
    return rs.length === 0 ? 'global' : rs.length === 1 ? rs[0] : 'multi';
  }
  const GENRE_DISC = { typography: 'graphic', architecture: 'architecture' };
  // 8.6 (point 94): no "Interdisciplinary" group. Works go in their discipline; a designer in each discipline where they have
  // visible works (else the first of their own); movements, institutions and theories in the disciplines that gather at least
  // 30 % of the works and designers they are linked to (fallback: their disciplines field / genre).
  const _dgCache = new Map();
  function discGroups(it) {
    const k = idx.kind.get(it.id);
    if (k === 'work') return [it.discipline];
    if (k === 'designer') {
      const ds = [...new Set((idx.worksByDesigner.get(it.id) || []).filter(workOk).map((w) => w.discipline))];
      return ds.length ? ds : [desDiscs(it)[0] || 'graphic'];
    }
    if (_dgCache.has(it.id)) return _dgCache.get(it.id);
    const cnt = {}; let tot = 0;
    relations(it.id).forEach((r) => {
      const o = idx.byId.get(r.other), kk = idx.kind.get(r.other);
      const ds = kk === 'work' ? [o.discipline] : kk === 'designer' ? [...new Set((idx.worksByDesigner.get(o.id) || []).map((w) => w.discipline))] : [];
      ds.forEach((d) => { cnt[d] = (cnt[d] || 0) + 1; tot++; });
    });
    let out = DISCS.filter((d) => tot && cnt[d] / tot >= 0.3);
    if (!out.length) out = (it.disciplines || []).filter((d) => DISCS.includes(d));
    if (!out.length && k === 'theory') out = [GENRE_DISC[it.genre] || 'graphic'];
    if (!out.length) out = ['graphic'];
    _dgCache.set(it.id, out);
    return out;
  }
  function arrangeGroupOf() {
    if (S.arrange === 'disc') return (it) => discGroups(it)[0];
    if (S.arrange === 'region') return (it) => regionGroup(it);
    return () => 'all';
  }
  function arrangeOrder() {
    if (S.arrange === 'disc') return [...DISCS];
    if (S.arrange === 'region') return ['europe', 'north-america', 'latin-america', 'multi', 'global'];
    return ['all'];
  }
  function zoneOf(it, region) {
    const zs = REGION_ZONES[region] || [];
    const c = (it.countries || []).find((x) => zs.includes(ZONE_OF[x]));
    return c ? ZONE_OF[c] : 'other';
  }

  // ---------- Render ----------
  function render() {
    const d = S.data;
    if (!d) return;
    S.disc = S.scope ? new Set([S.scope]) : new Set(DISCS);
    S.SC = S.scope ? makeScope(S.scope) : null;
    setBase();
    S.F = S.focus ? makeFocus(S.focus) : null;
    S.rel = new Set(relFocus(relations(S.sel)).map((r) => r.other));
    const B = build();
    const yrs = tickYears();
    const grid = yrs.map((y) => `<div class="gridline" style="left:${R(xOf(y))}px;height:${L.h}px"></div>`).join('');
    const eraLines = '';   // v20: no eras on the line
    $('content').style.cssText = `width:${L.w}px;height:${L.h}px`;
    $('content').innerHTML = B.cb.join('') + grid + eraLines + `<svg class="curves" id="curves" width="${L.w}" height="${L.h}" aria-hidden="true"></svg>` + B.ci.join('');
    $('labelsInner').style.height = L.h + 'px';
    $('labelsInner').innerHTML = B.lb.join('');
    renderAxis(yrs);
    renderTmap();
    syncScroll();
    renderFilters(); renderPanel(); syncTheme();
    if (S.pendingScroll) {
      const vp = $('viewport'), p = S.pendingScroll; S.pendingScroll = null;
      if (p.year != null) vp.scrollLeft = xOf(p.year) - vp.clientWidth / 2;
      vp.scrollTop = p.top;
      syncScroll();
    }
    drawCurves();
  }
  function renderAxis(yrs) {
    const sm = scaleMarks(), smx = sm.map((m) => xOf(m.y));
    yrs = yrs.filter((y) => smx.every((x) => Math.abs(xOf(y) - x) > 16));
    const marks = sm.map((m) => `<span class="scm" style="left:${R(xOf(m.y))}px" title="${esc(t('scaleMark'))}"></span>`).join('');
    $('axis').style.width = L.w + 'px';
    $('axis').innerHTML = marks + yrs.map((y) => `<span class="tick" style="left:${R(xOf(y))}px">${y}</span>`).join('');
  }
  let edgeRaf = 0;
  function syncScroll() {
    const vp = $('viewport');
    $('labelsInner').style.transform = `translateY(${-vp.scrollTop}px)`;
    $('axis').style.transform = `translateX(${-vp.scrollLeft}px)`;
    if (!edgeRaf) edgeRaf = requestAnimationFrame(() => { edgeRaf = 0; updateEdges(); stickyNames(); updateRangeUI(); });
  }

  // ---------- Visible range: "From … to … / All", time minimap, drag on the axis, edge arrows (v18) ----------
  function viewRangeU() {
    const vp = $('viewport');
    return [(vp.scrollLeft - L.x0) / S.px, (vp.scrollLeft + vp.clientWidth - L.x0) / S.px];
  }
  function setRangeU(u0, u1) {
    const vp = $('viewport'), vw = vp.clientWidth;
    u0 = Math.max(0, u0); u1 = Math.min(SC.total, u1);
    if (u1 - u0 <= 0) return;
    S.px = Math.max(L.fit, Math.min(L.max, vw / (u1 - u0)));
    S.zoomed = S.px > L.fit + 1e-6;
    render();
    vp.scrollLeft = L.x0 + u0 * S.px; syncScroll();
  }
  const setRangeYears = (y0, y1) => setRangeU(U(y0), U(y1));
  // v19 |⟷|: the span of what is shown now (filters, lens, "only", open context rows), from the earliest to the latest
  // start, plus the end of short bars (the ends of long or open bars are ignored), with a 4 % margin. Folding the design
  // groups and the zoom level are not taken into account, so the result does not change after fitting.
  function visibleSpan() {
    const d = S.data; let a = Infinity, b = -Infinity;
    const add = (s, e) => {
      if (s == null) return;
      a = Math.min(a, s); b = Math.max(b, s);
      if (e != null && e > s && e - s <= LONG_YEARS) b = Math.max(b, e);
    };
    const rowOn = (tr) => (S.focus ? S.focus === tr : S.ctxShow[tr]) && isOpen('trk:' + tr);
    d.contexts.forEach((c) => { if (rowOn(c.track) && ctxVisible(c)) add(c.start, c.end); });
    (d.production || []).forEach((p) => { if (rowOn('production') && prodVisible(p)) add(p.start, p.end); });
    d.movements.forEach((m) => { if (movementVisible(m) && !m.macro) add(m.start, m.end); });
    d.institutions.forEach((i) => { if (institutionVisible(i)) add(i.start, i.end); });
    d.theories.forEach((th) => { if (theoryVisible(th)) add(th.year); });
    d.works.forEach((w) => { if (workOk(w)) add(w.year); });
    if (S.arrange !== 'date') d.designers.forEach((x) => { if (designerVisible(x)) add(x.born, x.died); });
    if (!Number.isFinite(a)) return null;
    const m = Math.max(1, (b - a) * 0.04);
    return [Math.max(LINE_START, a - m), Math.min(NOWY(), b + m)];
  }
  const sameView = (r) => { const [u0, u1] = viewRangeU(), tol = Math.max(0.5, (u1 - u0) * 0.01); return Math.abs(u0 - r[0]) < tol && Math.abs(u1 - r[1]) < tol; };
  function fitVisible() {
    const sp = visibleSpan(); if (!sp) return;
    setRangeYears(sp[0], sp[1]);
    S.fitDone = { key: sp.join('-'), view: viewRangeU() };
    updateRangeUI();
  }
  function renderTmap() {
    const m = $('tmap'); if (!m || !SC.total) return;
    const W = m.clientWidth || 1, f = (y) => (U(y) / SC.total) * W;
    // v20: no eras; the minimap is one track with a mark at each century
    const cent = []; for (let y = Math.ceil(LINE_START / 100) * 100; y <= NOWY(); y += 100) cent.push(y);
    m.innerHTML = `<i class="te" style="left:0;width:${R(W - 1)}px"></i>` + cent.map((y) => `<i class="tcm" style="left:${R(f(y))}px" title="${y}"></i>`).join('') +
      '<div class="tw" id="tmapWin"><i class="bl"></i><i class="br"></i></div>';
    updateRangeUI();
  }
  function updateRangeUI() {
    if (!S.data || !SC.total) return;
    const [u0, u1] = viewRangeU();
    const y0 = Math.max(LINE_START, Math.round(yearAtU(Math.max(0, u0)))), y1 = Math.min(NOWY(), Math.round(yearAtU(Math.min(SC.total, u1))));
    const fi = $('yFrom'), ti = $('yTo');
    if (fi && document.activeElement !== fi) fi.value = y0;
    if (ti && document.activeElement !== ti) ti.value = y1;
    const w = $('tmapWin'), m = $('tmap');
    if (w && m) {
      const W = m.clientWidth || 1, a = Math.max(0, u0 / SC.total) * W, b = Math.min(1, u1 / SC.total) * W;
      w.style.left = R(a) + 'px'; w.style.width = R(Math.max(b - a, 6)) + 'px';
    }
    $('edgeL').classList.toggle('lim', u0 <= 0.5);
    $('edgeR').classList.toggle('lim', u1 >= SC.total - 0.5);
    $('zoomFit').disabled = !S.zoomed;
    const sp = visibleSpan();
    const whole = sp && !S.zoomed && $('viewport').clientWidth / (U(sp[1]) - U(sp[0])) <= L.fit * 1.06;
    $('zoomVis').disabled = !sp || whole || !!(S.fitDone && S.fitDone.key === sp.join('-') && sameView(S.fitDone.view));
  }
  function applyYearInputs() {
    const fi = $('yFrom'), ti = $('yTo');
    let a = parseInt(fi.value, 10), b = parseInt(ti.value, 10);
    if (!Number.isFinite(a) || !Number.isFinite(b)) return updateRangeUI();
    a = Math.max(LINE_START, Math.min(NOWY(), a)); b = Math.max(LINE_START, Math.min(NOWY(), b));
    if (a >= b) { fi.classList.add('bad'); ti.classList.add('bad'); setTimeout(() => { fi.classList.remove('bad'); ti.classList.remove('bad'); }, 900); return updateRangeUI(); }
    fi.blur(); ti.blur();
    setRangeYears(a, b);
  }
  function wireRange() {
    const vp = $('viewport'), clip = $('axisClip'), m = $('tmap'), sel = $('axsel'), vsel = $('vsel');
    const hideSel = () => { sel.hidden = true; vsel.hidden = true; };
    ['yFrom', 'yTo'].forEach((id) => {
      $(id).addEventListener('keydown', (ev) => { if (ev.key === 'Enter') { ev.preventDefault(); applyYearInputs(); } else if (ev.key === 'Escape') { $(id).blur(); updateRangeUI(); } });
      $(id).addEventListener('change', applyYearInputs);
    });
    // time minimap: move a bracket (start or end), drag the window (pan) or click elsewhere (jump)
    let tm = null, raf = 0;
    const uAt = (ev) => ((ev.clientX - m.getBoundingClientRect().left) / (m.clientWidth || 1)) * SC.total;
    m.addEventListener('mousedown', (ev) => {
      ev.preventDefault();
      const [u0, u1] = viewRangeU(), u = uAt(ev);
      const mode = ev.target.classList.contains('bl') ? 'l' : ev.target.classList.contains('br') ? 'r' : ev.target.closest('.tw') ? 'pan' : 'jump';
      if (mode === 'jump') { vp.scrollLeft = L.x0 + (u - (u1 - u0) / 2) * S.px; syncScroll(); }
      const r = viewRangeU();
      tm = { mode: mode === 'jump' ? 'pan' : mode, u, u0: r[0], u1: r[1], sl: vp.scrollLeft };
      document.body.classList.add('dragging');
    });
    window.addEventListener('mousemove', (ev) => {
      if (!tm) return;
      const u = uAt(ev), minSpan = vp.clientWidth / L.max;
      if (tm.mode === 'pan') { vp.scrollLeft = tm.sl + (u - tm.u) * S.px; syncScroll(); return; }
      if (raf) return;
      raf = requestAnimationFrame(() => {
        raf = 0; if (!tm) return;
        if (tm.mode === 'l') setRangeU(Math.min(u, tm.u1 - minSpan), tm.u1);
        else setRangeU(tm.u0, Math.max(u, tm.u0 + minSpan));
      });
    });
    window.addEventListener('mouseup', () => { if (tm) { tm = null; document.body.classList.remove('dragging'); } });
    // drag on the years to choose a span
    let ds = null;
    const clipX = (ev) => ev.clientX - clip.getBoundingClientRect().left;
    clip.addEventListener('mousedown', (ev) => {
      if (ev.button !== 0 || ev.target.closest('#tmap, .ax-edge')) return;
      ev.preventDefault();
      ds = { x: clipX(ev) };
    });
    window.addEventListener('mousemove', (ev) => {
      if (!ds) return;
      const x = Math.max(0, Math.min(clip.clientWidth, clipX(ev))), a = Math.min(ds.x, x), b = Math.max(ds.x, x);
      ds.x1 = x;
      if (b - a < 6) { hideSel(); return; }
      const ya = Math.round(yearAtX(vp.scrollLeft + a)), yb = Math.round(yearAtX(vp.scrollLeft + b));
      sel.hidden = false; sel.style.left = a + 'px'; sel.style.width = (b - a) + 'px';
      sel.dataset.a = ya; sel.dataset.b = yb;
      sel.innerHTML = `<span class="a">${ya}</span><span class="b">${yb}</span>`;
      // v19: the same span is shaded down the whole line, so you can see what will fill the screen
      const ox = vp.offsetLeft + (clip.getBoundingClientRect().left - vp.getBoundingClientRect().left);
      vsel.hidden = false; vsel.style.left = (ox + a) + 'px'; vsel.style.width = (b - a) + 'px';
      vsel.style.height = (vp.clientHeight) + 'px';
    });
    window.addEventListener('mouseup', () => {
      if (!ds) return;
      const d0 = ds; ds = null; hideSel();
      if (d0.x1 == null || Math.abs(d0.x1 - d0.x) < 6) return;
      const a = Math.min(d0.x, d0.x1), b = Math.max(d0.x, d0.x1);
      setRangeU((vp.scrollLeft + a - L.x0) / S.px, (vp.scrollLeft + b - L.x0) / S.px);
    });
    document.addEventListener('keydown', (ev) => { if (ev.key === 'Escape' && ds) { ds = null; hideSel(); } });
    // edge arrows: each click adds 25 % more years on that side (the other edge stays); holding repeats
    let rep = null;
    const extend = (side) => {
      const [u0, u1] = viewRangeU(), d = (u1 - u0) * 0.25;
      if (side === 'l') setRangeU(u0 - d, u1); else setRangeU(u0, u1 + d);
    };
    ['l', 'r'].forEach((side) => {
      const b = $(side === 'l' ? 'edgeL' : 'edgeR');
      b.addEventListener('mousedown', (ev) => {
        ev.preventDefault(); ev.stopPropagation();
        extend(side);
        clearTimeout(rep && rep.t); clearInterval(rep && rep.i);
        rep = { t: setTimeout(() => { rep.i = setInterval(() => extend(side), 160); }, 380) };
      });
    });
    const stopRep = () => { if (rep) { clearTimeout(rep.t); clearInterval(rep.i); rep = null; } };
    window.addEventListener('mouseup', stopRep);
    clip.addEventListener('mousemove', (ev) => {
      const x = clipX(ev), w = clip.clientWidth;
      $('edgeL').classList.toggle('near', x < 44 && ev.clientY - clip.getBoundingClientRect().top > 12);
      $('edgeR').classList.toggle('near', x > w - 44 && ev.clientY - clip.getBoundingClientRect().top > 12);
    });
    clip.addEventListener('mouseleave', () => { $('edgeL').classList.remove('near'); $('edgeR').classList.remove('near'); stopRep(); });
  }

  // designer names follow the view, so a life line that starts off-screen still says whose it is
  function stickyNames() {
    const vt = $('viewport').scrollTop;
    document.querySelectorAll('#labelsInner .sticky').forEach((el) => {
      const y0 = +el.dataset.y0, y1 = +el.dataset.y1, zone = el.classList.contains('zone-label');
      const want = vt + (el.dataset.off ? +el.dataset.off : zone ? 22 : 4);
      el.style.top = Math.max(y0, Math.min(y1, want)) + 'px';
      if (zone) el.style.visibility = want > y1 + 4 ? 'hidden' : '';
    });
    const vx = $('viewport').scrollLeft + 6;
    // v24/v38: the label of a movement stays in view while its span is on screen
    document.querySelectorAll('#content .it.movement[data-x1]').forEach((el) => {
      const mt = el.querySelector('.mt'); if (!mt) return;
      const fi = +el.dataset.fi || 6;
      const dx = Math.max(0, Math.min(vx - el.offsetLeft - fi, +el.dataset.x1 - el.offsetLeft - mt.offsetWidth - fi - 4));
      mt.style.transform = dx > 0 ? `translateX(${Math.round(dx)}px)` : '';
    });
    document.querySelectorAll('#content .it.designer').forEach((el) => {
      const nm = el.firstElementChild; if (!nm) return;
      const dx = Math.max(0, Math.min(vx - el.offsetLeft, el.offsetWidth - nm.offsetWidth - 4));
      nm.style.transform = dx > 0 ? `translateX(${Math.round(dx)}px)` : '';
    });
  }

  // ---------- Connection curves ----------
  // When an element is selected, curves join it to its first-degree relations. Three kinds, each with its own button:
  // context (in the colour of the context row), works and other relations (neutral grey). Hovering an element shows
  // a faint preview. A curve that ends in a closed section, or leaves the visible area, ends in an arrow.
  function curvePts(a, b) {
    const mx = (a.x + b.x) / 2;
    return [a, { x: mx, y: a.y }, { x: mx, y: b.y }, b];
  }
  const bez = (p, t2) => {
    const u = 1 - t2;
    return { x: u * u * u * p[0].x + 3 * u * u * t2 * p[1].x + 3 * u * t2 * t2 * p[2].x + t2 * t2 * t2 * p[3].x, y: u * u * u * p[0].y + 3 * u * u * t2 * p[1].y + 3 * u * t2 * t2 * p[2].y + t2 * t2 * t2 * p[3].y };
  };
  function arrowHead(p, from, col, op) {
    let dx = p.x - from.x, dy = p.y - from.y; const n = Math.hypot(dx, dy) || 1; dx /= n; dy /= n;
    const s = 7, px2 = -dy, py2 = dx;
    const b1 = { x: p.x - dx * s + px2 * s * 0.55, y: p.y - dy * s + py2 * s * 0.55 }, b2 = { x: p.x - dx * s - px2 * s * 0.55, y: p.y - dy * s - py2 * s * 0.55 };
    return `<path d="M${R(p.x)},${R(p.y)} L${R(b1.x)},${R(b1.y)} L${R(b2.x)},${R(b2.y)} Z" fill="${col}" opacity="${op}"/>`;
  }
  // v19: curves keep the colour of what they reach: a fact its row, a work its discipline, a designer the first colour
  // of its line; movements, institutions and theory stay neutral
  const curveCol = (c) => {
    if (c.r.type === 'ctx' && c.r.tone) return `rgb(var(--c-${c.r.tone}))`;
    const k = idx.kind.get(c.r.other), it = idx.byId.get(c.r.other);
    if (k === 'work' && it) return `rgb(var(--c-${it.discipline}))`;
    if (k === 'designer' && it) { const ds = desDiscs(it); if (ds.length) return `rgb(var(--c-${ds[0]}))`; }
    return 'rgb(var(--c-neutral))';
  };
  function drawCurves() {
    const svg = $('curves'); if (!svg) return;
    const list = [];
    const from = (id, faint) => {
      const p0 = S.pos.get(id); if (!p0 || p0.coll || p0.hidden) return;
      if (!S.connAll) return;
      relFocus(relations(id)).forEach((r) => {
        const p1 = S.pos.get(r.other); if (!p1 || (p1.hidden && !p1.coll)) return;
        if (p1.line === id || p0.line === r.other) return;  // a designer and the works on its own line
        list.push({ a: p0, b: p1, r, faint, pts: curvePts(p0, p1) });
      });
    };
    if (S.sel) from(S.sel, false);
    if (S.hover && S.hover !== S.sel) from(S.hover, true);
    S.curves = list;
    svg.innerHTML = list.map((c, i) => {
      const col = curveCol(c), op = c.faint ? 0.28 : 0.8, p = c.pts;
      const d = `M${R(p[0].x)},${R(p[0].y)} C${R(p[1].x)},${R(p[1].y)} ${R(p[2].x)},${R(p[2].y)} ${R(p[3].x)},${R(p[3].y)}`;
      const head = c.b.coll ? arrowHead(p[3], bez(p, 0.9), col, op) : `<circle cx="${R(p[3].x)}" cy="${R(p[3].y)}" r="2.2" fill="${col}" opacity="${op}"/>`;
      const sw = c.faint ? 1.2 : c.r.via ? 0.8 : 1.6;   // v20: indirect relations with a thinner line
      return `<path d="${d}" fill="none" stroke="${col}" stroke-width="${sw}" opacity="${op}"${c.b.coll ? ' stroke-dasharray="4 3"' : ''}/>${head}` + (c.faint ? '' : `<path class="hit" data-ci="${i}" d="${d}"/>`);
    }).join('') + '<g id="edges"></g>';
    updateEdges();
  }
  function updateEdges() {
    const g = document.getElementById('edges'); if (!g) return;
    const vp = $('viewport');
    const r = { x0: vp.scrollLeft + 4, y0: vp.scrollTop + 4, x1: vp.scrollLeft + vp.clientWidth - 4, y1: vp.scrollTop + vp.clientHeight - 4 };
    const inside = (p) => p.x >= r.x0 && p.x <= r.x1 && p.y >= r.y0 && p.y <= r.y1;
    let html = '';
    (S.curves || []).forEach((c) => {
      if (c.faint || !inside(c.a) || inside(c.b)) return;
      let prev = c.a;
      for (let i = 1; i <= 60; i++) {
        const q = bez(c.pts, i / 60);
        if (!inside(q)) { html += arrowHead(prev, bez(c.pts, Math.max(0, (i - 3) / 60)), curveCol(c), 0.9); break; }
        prev = q;
      }
    });
    g.innerHTML = html;
  }

  // ---------- Era bar label and filters ----------
  // 8.5c (point 84): an era is named by its years only; the end shown is the next era's start minus one (no repeated years)
  const eraName = (e) => { if (typeof e === 'string') e = G.eraById.get(e); if (!e) return ''; const i = G.eras.indexOf(e), nx = G.eras[i + 1]; return `${e.start}–${nx ? nx.start - 1 : t('today')}`; };
  const eraSpan = eraName;
  const pressed = (b) => `aria-pressed="${!!b}"`;
  function renderFilters() {
    const f = [];
    const ctxKeys2 = TRACKS.concat(['production']);
    const connBtn = `<button class="chip conn" data-connall="1" ${pressed(S.connAll)} title="${esc(t('connTip'))}"><svg width="14" height="11" viewBox="0 0 14 11" aria-hidden="true"><path d="M1.5 9.5 C7 9.5 7 1.5 12.5 1.5" fill="none" stroke="currentColor" stroke-width="1.5"/><circle cx="12.5" cy="1.5" r="1.4" fill="currentColor"/><circle cx="1.5" cy="9.5" r="1.4" fill="currentColor"/></svg>${esc(t('fConn'))}</button>`;
    f.push(`<div class="frow"><span class="flabel lens-l">${esc(t('fLens'))}</span>` +
      ctxKeys2.map((k) => `<button class="chip scope lens" data-focus="${k}" data-t="${k}" style="--sc:var(--c-${k})" ${pressed(S.focus === k)} title="${esc(t(S.focus === k ? 'focusOff' : 'focusBtn') + ': ' + t('tr_' + k))}"><i class="dot" style="background:rgb(var(--c-${k}))"></i>${esc(t('tr_' + k))}</button>`).join('') +
      `<span class="sep"></span><span class="flabel lens-l">${esc(t('fDisc'))}</span>` +
      DISCS.map((k) => `<button class="chip scope disc" data-disc="${k}" style="--sc:var(--c-${k})" ${pressed(S.scope === k)} title="${esc(S.scope === k ? t('scopeOff') : t('scopeTip_' + k))}"><svg width="11" height="11" viewBox="0 0 10 10" aria-hidden="true"><path d="${GLYPH[k]}" fill="rgb(var(--c-${k}))"/></svg>${esc(t('d_' + k))}</button>`).join('') +
      `<span class="sep"></span>` + connBtn +
      `<span class="sep"></span><span class="flabel lens-l">${esc(t('fLevel'))}</span>` +
      LEVELS.map((k) => `<button class="chip lvl" data-level="${k}" ${pressed(S.level === k)} title="${esc(t('lvTip_' + k))}">${k === 'essential' ? `<svg width="11" height="11" viewBox="0 0 10 10" aria-hidden="true"><path d="${STAR}"/></svg>` : ''}${esc(t('lv_' + k))}</button>`).join('') +
      '</div>');
    f.push('<div class="frow">' +
      `<span class="flabel">${esc(t('fShow'))}</span>` +
      TYPES.map((k) => { const off = k === 'designers' && S.arrange === 'date'; return `<button class="chip${off ? ' off' : ''}" data-type="${k}" ${pressed(S.types.has(k) && !off)}${off ? ` aria-disabled="true" title="${esc(t('desOffDate'))}"` : ''}>${esc(t('ty_' + k))}</button>`; }).join('') +
      `<span class="sep"></span><span class="flabel">${esc(t('fArrange'))}</span>` +
      ['chrono', 'date', 'disc', 'region'].map((k) => `<button class="chip" data-arrange="${k}" ${pressed(S.arrange === k)}>${esc(t('ar_' + k))}</button>`).join('') +
      `<span class="sep"></span><span class="flabel">${esc(t('fScale'))}</span>` +
      ['uneven', 'linear'].map((k) => `<button class="chip" data-scale="${k}" ${pressed(S.scale === k)} title="${esc(t('sc_' + k + 'Tip'))}">${esc(t('sc_' + k))}</button>`).join('') +
      (S.iso && idx.byId.get(S.iso.id) ? `<button class="chip iso" data-isoclear="1" title="${esc(t('isoClear'))}">${esc(t('isoChip'))} ${esc(lab(idx.byId.get(S.iso.id)))}  ✕</button>` : '') +
      '</div>');
    $('filters').innerHTML = f.join('');
    $('infoBtn').setAttribute('aria-pressed', String(S.info));
    $('langBtn').textContent = t('langBtn'); $('langBtn').title = t('langTitle'); $('langBtn').setAttribute('aria-label', t('langTitle'));
    if ($('reviewBtn')) $('reviewBtn').setAttribute('aria-pressed', String(!!S.review));
  }

  // ---------- Panel pieces ----------
  const toneOf = (id) => {
    const k = idx.kind.get(id) || (G.map.get(id) || {}).kind;
    if (k === 'context') { const c = idx.byId.get(id); return c ? c.track : null; }
    if (k === 'production') return 'production';
    if (k === 'theory') return 'theory';
    const it = idx.byId.get(id);
    if (it && k === 'work') return it.discipline;
    return null;
  };
  // a clickable chip for any element (also of another era)
  function pchip(id, o = {}) {
    const it = idx.byId.get(id), g = G.map.get(id);
    if (!it && !g) return '';
    const k = it ? idx.kind.get(id) : g.kind;
    const name = it ? nameOf(it) : (S.lang === 'es' ? g.nameEs : g.name);
    const yr = it ? (k === 'concept' ? '' : yearOf(it) || '') : (g.year || '');
    const tone = it ? toneOf(id) : null;
    const star = (it ? it.star : g && g.star) ? '<span class="st" aria-hidden="true">★</span> ' : '';
    const sw = k === 'context' || k === 'production' || k === 'theory' ? `<i class="sw" style="--tc:var(--c-${tone || (it ? '' : 'neutral')})"></i>` : '';
    const eraTag = '';
    return `<button class="pchip${o.conn ? ' conn' : ''}" data-go="${esc(id)}">${sw}${star}${esc(name)}${yr ? ` <span class="y">${esc(yr)}</span>` : ''}${eraTag}</button>`;
  }
  const chipsOf = (ids) => ids.filter((x, i) => ids.indexOf(x) === i).map((x) => pchip(x)).filter(Boolean).join('');
  const sect = (title, html, cls) => (html ? `<section class="sect${cls ? ' ' + cls : ''}"><h3>${esc(title)}</h3>${html}</section>` : '');
  const upFirst = (x) => (typeof x === 'string' && x ? x.charAt(0).toUpperCase() + x.slice(1) : x);
  const textSect = (title, s, cls) => (s ? sect(title, paras(s), cls) : '');
  const kvHtml = (rows) => { const r = rows.filter((x) => x && x[1]); return r.length ? `<dl class="kv">${r.map(([a, b]) => `<dt>${esc(a)}</dt><dd>${b}</dd>`).join('')}</dl>` : ''; };
  const extLink = (url, label) => `<a href="${esc(url)}" target="_blank" rel="noopener noreferrer">${esc(label)}</a>`;

  function ctxGroups(id, viaWorks) {
    let lns = (idx.linksByItem.get(id) || []).slice();
    const seen = new Set(lns.map((l) => l.ctx));
    const via = new Map();
    (viaWorks || []).forEach((w) => (idx.linksByItem.get(w.id) || []).forEach((ln) => { if (!seen.has(ln.ctx)) { seen.add(ln.ctx); lns.push(ln); via.set(ln, w); } }));
    if (!lns.length) return '';
    const by = new Map();
    lns.forEach((ln) => { if (!by.has(ln.track)) by.set(ln.track, []); by.get(ln.track).push(ln); });
    const html = TRACKS.concat(['production']).filter((k) => by.has(k)).map((k) =>
      `<div class="ctx-group" data-t="${k}"><div class="gh">${lensWord(k)}</div>` +
      by.get(k).map((ln) => `<div class="link-item">${pchip(ln.ctx)}<span class="note">${esc(tx(ln, 'note'))}${via.has(ln) ? ` <em>${esc(t('viaWork'))}: ${esc(nameOf(via.get(ln)))}</em>` : ''}</span></div>`).join('') + '</div>').join('');
    return sect(t('ctx'), html, 'ctxs');
  }
  function connHtml(id) {
    const cs = idx.conn.get(id) || [];
    if (!cs.length) return '';
    return sect(t('conn'), '<div class="link-list">' + cs.map((c) => `<div class="link-item">${pchip(c.other, { conn: true })}<span class="note">${c.dir === 'to' ? '→ ' : '← '}${esc(tx(c.c, 'note'))}</span></div>`).join('') + '</div>');
  }
  // v20: "Learn more" lists the sources and relevant pages (museums, archives, companies); never Wikipedia
  const learnHtml = (it) => {
    const ls = [].concat(it.where || [], it.links_more || []).filter((x) => x && /^https:\/\//.test(x.url) && !/wikipedia\.org/.test(x.url));
    return ls.length ? sect(t('learn'), `<ul class="learn">${ls.map((x) => `<li>${extLink(x.url, (S.lang === 'es' && x.es) || x.label)}</li>`).join('')}</ul>`) : '';
  };
  const conceptsHtml = (id) => {
    const cs = idx.itemConcepts.get(id) || [];
    return cs.length ? sect(S.lang === 'es' ? 'Conceptos' : 'Concepts', `<div class="chips">${cs.map((c) => pchip(c)).join('')}</div>`) : '';
  };
  // v22: the macromovement card lists the concepts of the eras it spans (the old era card did this)
  const macroConceptsHtml = (m) => {
    const eras = new Set((G.eras || []).filter((e) => e.start < (m.end || m.start) && e.end > m.start).map((e) => e.id));
    const own = idx.itemConcepts.get(m.id) || [];
    const cs = [...new Set(own.concat(idx.concepts.filter((c) => eras.has(c.era)).map((c) => c.id)))];
    return cs.length ? sect(S.lang === 'es' ? 'Conceptos' : 'Concepts', `<div class="chips">${cs.map((c) => pchip(c)).join('')}</div>`) : '';
  };
  const worksSorted = (ids) => ids.map((x) => idx.byId.get(x)).filter(Boolean).sort((a, b) => a.year - b.year).map((w) => w.id);

  // ---------- Images (Wikipedia API; only files hosted on Wikimedia Commons are shown) ----------
  const imgCache = new Map();
  async function fetchImage(title) {
    if (imgCache.has(title)) return imgCache.get(title);
    const p = (async () => {
      try {
        const u1 = 'https://en.wikipedia.org/w/api.php?action=query&format=json&origin=*&redirects=1&prop=pageimages&piprop=thumbnail|name&pithumbsize=720&titles=' + enc(title);
        const j1 = await (await fetch(u1)).json();
        const pg = Object.values((j1.query || {}).pages || {})[0];
        if (!pg || !pg.thumbnail || !pg.pageimage) return null;
        const u2 = 'https://en.wikipedia.org/w/api.php?action=query&format=json&origin=*&prop=imageinfo&iiprop=extmetadata|url&titles=' + enc('File:' + pg.pageimage);
        const j2 = await (await fetch(u2)).json();
        const fp = Object.values((j2.query || {}).pages || {})[0];
        if (!fp || fp.imagerepository !== 'shared') return null; // not on Commons: may be non-free
        const ii = (fp.imageinfo || [])[0] || {}, md = ii.extmetadata || {};
        return { src: pg.thumbnail.source, page: ii.descriptionurl || '', license: (md.LicenseShortName || {}).value || '' };
      } catch (err) { return null; }
    })();
    imgCache.set(title, p);
    return p;
  }
  // v20: without a free image the card simply has no picture (no text or links in its place)
  function imgFallback() { return ''; }
  const commonsSrc = (f) => 'https://commons.wikimedia.org/wiki/Special:FilePath/' + enc(f) + '?width=720';
  const commonsPage = (f) => 'https://commons.wikimedia.org/wiki/File:' + enc(f.replace(/ /g, '_'));
  const altOf = (it) => (S.lang === 'es' ? 'Imagen: ' : 'Image: ') + nameOf(it);
  // slides of an element: its own images; movements/macros: 3-5 from their ★ works; designers without a portrait: a work
  function slidesOf(it, kind) {
    const own = (it.images || []).map((i) => ({ src: commonsSrc(i.f), page: commonsPage(i.f), file: i.f, credit: i.c || '', lic: i.l || '', res: !!i.r, alt: altOf(it) }));
    if (kind === 'work' || kind === 'institution' || kind === 'theory') return own;
    if (kind === 'designer') {
      if (own.length) return own;
      const ws = (idx.worksByDesigner && idx.worksByDesigner.get(it.id)) || [];
      const w = ws.slice().sort((a, b) => (b.star ? 1 : 0) - (a.star ? 1 : 0)).find((x) => x.images && x.images.length);
      return w ? [Object.assign(workSlide(w), { cap: (S.lang === 'es' ? 'Obra más conocida: ' : 'Best-known work: ') + nameOf(w), go: w.id })] : [];
    }
    if (kind === 'movement') {
      const parts = it.macro ? (it.parts || []) : [it.id];
      const lists = parts.map((pid) => (idx.worksByMovement.get(pid) || []).filter((w) => w.images && w.images.length)
        .sort((a, b) => (b.star ? 1 : 0) - (a.star ? 1 : 0) || a.year - b.year));
      const out = [], seen = new Set();
      for (let r = 0; out.length < 4 && r < 4; r++) lists.forEach((l) => { const w = l[r]; if (w && out.length < 4 && !seen.has(w.id)) { seen.add(w.id); out.push(w); } });
      return out.sort((a, b) => a.year - b.year).map(workSlide);
    }
    return [];
  }
  function workSlide(w) {
    const i = w.images[0];
    return { src: commonsSrc(i.f), page: commonsPage(i.f), file: i.f, credit: i.c || '', lic: i.l || '', res: !!i.r, alt: altOf(w), cap: nameOf(w) + (w.year ? ' (' + w.year + ')' : ''), go: w.id };
  }
  // 8.6 (point 95): a caption only in carousels (what the photo is, with (C) or (CC) when it is not public domain);
  // the image is always the link to its source; the reference goes to "Fuentes" as an "Imagen:" line
  const licMark = (sl) => {
    if (sl.res) return '(C)';
    const l = String(sl.lic || '').trim();
    return !l || /^(public domain|pd\b|cc0|no known|no restrictions|dominio p)/i.test(l) ? '' : '(CC)';
  };
  function slideHtml(sl, n, i) {
    const mk = licMark(sl);
    const cap = n > 1 ? (sl.go ? `<button class="pchip-lnk" data-go="${esc(sl.go)}">${esc(sl.cap)}</button>` : sl.cap ? esc(sl.cap) : '') : '';
    const fc = n > 1 && (cap || mk) ? `<figcaption>${cap ? `<span class="gc">${cap}</span>` : ''}${mk ? ` <span class="gl">${mk}</span>` : ''}</figcaption>` : '';
    return `<figure class="gal-s"><a href="${esc(sl.page)}" target="_blank" rel="noopener noreferrer" title="${esc(t('imgOpen'))}" aria-label="${esc(t('imgOpen'))}"><img src="${esc(sl.src)}" alt="${esc(sl.alt)}" ${i ? 'loading="lazy"' : ''} referrerpolicy="no-referrer" onerror="this.closest('figure').classList.add('bad')"></a>${fc}</figure>`;
  }
  // reference line of an image, for the "Fuentes" section (not counted as a source)
  function imgRefHtml(sl) {
    const L2 = (es, en) => (S.lang === 'es' ? es : en);
    const title = sl.file ? sl.file.replace(/\.[A-Za-z0-9]{2,5}$/, '') : sl.label || '';
    const pre = sl.cap ? ` (${sl.cap})` : '';
    const meta = [sl.credit, sl.lic, sl.res ? L2('derechos reservados', 'rights reserved') : ''].filter(Boolean).join(', ');
    return `<li class="rf-img"><span class="rf-ik">${esc(L2('Imagen', 'Image'))}${esc(pre)}:</span> <a href="${esc(sl.page)}" target="_blank" rel="noopener noreferrer">${esc(title || L2('fuente de la imagen', 'image source'))}</a>${meta ? ` <span class="rf-dom">${esc(meta)}</span>` : ''}</li>`;
  }
  function imgGallery(it, kind) {
    const ov = ED.img(it.id);   // an image chosen in edit mode replaces the first one
    let sl = ['movement', 'institution', 'designer', 'work', 'theory'].includes(kind) ? slidesOf(it, kind) : [];
    if (ov) sl = [{ src: ov, page: ov, label: (S.lang === 'es' ? 'elegida en modo edición' : 'chosen in edit mode'), credit: '', lic: '', res: false, alt: nameOf(it) }].concat(sl.slice(1));
    sl.forEach((x) => { if (S.imgRefs) S.imgRefs.push(imgRefHtml(x)); });
    let html;
    if (sl.length) {
      html = sl.length === 1 ? `<div class="p-img gal one">${slideHtml(sl[0], 1, 0)}</div>`
        : `<div class="p-img gal" tabindex="0" role="group" aria-roledescription="carousel" aria-label="${esc(nameOf(it))}"><div class="gal-track">${sl.map((x, i) => slideHtml(x, sl.length, i)).join('')}</div>` +
          `<div class="gal-dots">${sl.map((x, i) => `<button class="gal-dot${i ? '' : ' on'}" data-gi="${i}" aria-label="${i + 1}/${sl.length}"></button>`).join('')}</div></div>`;
    } else if (['movement', 'institution', 'designer', 'work'].includes(kind) && it.wiki) {
      html = `<div class="p-img empty" data-img="${esc(it.wiki)}" data-for="${esc(it.id)}">${esc(t('loadingImg'))}</div>`;
    } else html = imgFallback(it, kind);
    const pen = ED.pencil(it.id);
    return pen ? `<div class="p-imgwrap">${html}${pen}</div>` : html;
  }
  const imgBox = imgGallery;
  function galGo(g, i) {
    const tr = g.querySelector('.gal-track'); if (!tr) return;
    const n = tr.children.length; i = Math.max(0, Math.min(n - 1, i));
    tr.scrollTo({ left: tr.clientWidth * i, behavior: 'smooth' });
  }
  function galSync(tr) {
    const g = tr.parentNode, i = Math.round(tr.scrollLeft / Math.max(1, tr.clientWidth));
    g.querySelectorAll('.gal-dot').forEach((d, k) => d.classList.toggle('on', k === i));
  }
  // an image that arrives after the card was drawn (Wikipedia lookup) adds its line to "Fuentes"
  function addImgRef(li) {
    const sd = document.querySelector('#panel details.sources'); if (!sd) return;
    let ul = sd.querySelector('.rf-imgs');
    if (!ul) { ul = document.createElement('ul'); ul.className = 'rf-imgs'; const first = sd.querySelector('.rf-list, .rf-none'); if (first) sd.insertBefore(ul, first); else sd.appendChild(ul); }
    ul.insertAdjacentHTML('beforeend', li);
  }
  function hydrateImages(token) {
    const el = document.querySelector('#panel [data-img]');
    if (!el) return;
    const id = el.dataset.for, title = el.dataset.img;
    fetchImage(title).then((r) => {
      if (token !== S.panelToken || !el.isConnected) return;
      if (r) {
        const it = idx.byId.get(id);
        el.className = 'p-img';
        const img = `<img src="${esc(r.src)}" alt="${esc(it ? nameOf(it) : '')}" loading="lazy" referrerpolicy="no-referrer">`;
        const tip = [t('imgOpen'), r.license, 'Wikimedia Commons'].filter(Boolean).join(' · ');
        el.innerHTML = r.page ? `<a href="${esc(r.page)}" target="_blank" rel="noopener noreferrer" title="${esc(t('imgOpen'))}" aria-label="${esc(t('imgOpen'))}">${img}</a>` : img;
        if (r.page) addImgRef(imgRefHtml({ page: r.page, label: 'Wikimedia Commons', lic: r.license || '', credit: '' }));
      } else {
        const it = idx.byId.get(id); const k = idx.kind.get(id);
        el.outerHTML = imgFallback(it, k);
      }
    });
  }

  // ---------- Cards ----------
  const UNREV_KINDS = ['work', 'designer', 'movement', 'institution', 'context', 'production', 'theory', 'concept'];
  // header warning (stage 8): an element card with no sources shows "Not reviewed" under the title (click: opens Sources)
  function unrevFlag() {
    if (S.info || S.review || !S.sel || !idx.byId.has(S.sel) || !UNREV_KINDS.includes(idx.kind.get(S.sel))) return false;
    return srcCount(S.sel) === 0;
  }
  function head(kicker, title, meta, star, acts, kickerHtml, unrev) {
    const un = unrev === undefined ? unrevFlag() : unrev;
    const L2 = (es, en) => (S.lang === 'es' ? es : en);
    const warn = un ? `<button class="unrev-note" data-unrev="1" title="${esc(L2('Ficha no revisada: aún no tiene fuentes', 'Card not reviewed: it has no sources yet'))}" aria-label="${esc(L2('Ficha no revisada: aún no tiene fuentes', 'Card not reviewed: it has no sources yet'))}">${warnIcon()}${esc(t('unrevShort'))}</button>` : '';
    return `<div class="p-head"><div style="min-width:0"><div class="kicker">${kickerHtml || esc(kicker)}</div><h2 class="p-title">${esc(title)}</h2>${meta ? `<div class="p-meta">${meta}</div>` : ''}${star || warn ? `<div class="p-flags">${warn}` : ''}${star ? `<span class="must"><svg width="11" height="11" viewBox="0 0 10 10" aria-hidden="true"><path d="${STAR}"/></svg>${esc(t('mustKnow'))}</span>` : ''}${star || warn ? '</div>' : ''}</div><div class="p-acts">${acts || ''}<button class="p-btn" data-close="1" aria-label="${esc(t('close'))}" title="${esc(t('close'))}"><svg width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><path d="M3 3l8 8M11 3l-8 8" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></button></div></div>`;
  }
  const metaPlace = (it) => [it.place, (it.countries || []).join(', ')].filter(Boolean).map(esc).join(' · ');

  // filter button of a card: show only this element and its connections
  function isoButton(id) {
    const isoOn = !!(S.iso && S.iso.id === id), isoLbl = esc(t(isoOn ? 'isoOff' : 'isoBtn'));
    return `<button class="p-btn${isoOn ? ' on' : ''}" id="isoBtn" title="${isoLbl}" aria-label="${isoLbl}" aria-pressed="${isoOn}"><svg width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><path d="M1.5,2 H12.5 L8.2,7.2 V11.8 L5.8,10.4 V7.2 Z" fill="${isoOn ? 'currentColor' : 'none'}" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/></svg></button>`;
  }
  function workCard(w) {
    const dn = (w.designers || []).map((x) => idx.byId.get(x)).filter(Boolean);
    const instOf = (x) => (x && idx.byId.has(x) ? pchip(x) : x ? esc(x) : '');
    const prod = w.production && w.production.from != null
      ? (w.production.to == null ? `${w.production.from} → ${t('stillProd')}` : fmtR(w.production.from, w.production.to)) + (w.production.note ? ' · ' + esc((S.lang === 'es' && w.es && w.es.production && w.es.production.note) || w.production.note) : '') : '';
    const movs = [].concat(w.movements || [], ...dn.map((a) => a.movements || []));
    const insts = [].concat(w.maker && idx.kind.get(w.maker) === 'institution' ? [w.maker] : [], ...dn.map((a) => a.institutions || []));
    const kind = `${t('k_work')} · ${typeLabel(w.type)} · ${t('d_' + w.discipline)}`;
    const meta = `${dn.length ? dn.map((a) => esc(a.name)).join(', ') + ' · ' : ''}${esc(dateOf(w))}${metaPlace(w) ? ' · ' + metaPlace(w) : ''}`;
    return head(kind, nameOf(w), meta, w.star, isoButton(w.id)) + imgBox(w, 'work') +
      sect(t('keyIdea'), `<p class="key">${esc(tx(w, 'key'))}</p>`) + ctxGroups(w.id) + textSect(t('analysis'), tx(w, 'more')) +
      sect(t('designProd'), kvHtml([
        [t('byDesigner'), dn.map((a) => pchip(a.id)).join('')], [t('maker'), instOf(w.maker)], [t('client'), instOf(w.client)],
        [t('materials'), esc(tx(w, 'materials'))], [t('designYear'), esc(String(w.year))], [t('lifeInProd'), prod]]) +
        ((idx.prodByItem.get(w.id) || []).length ? `<div class="chips" style="margin-top:8px">${chipsOf(idx.prodByItem.get(w.id))}</div>` : '')) +
      textSect(t('status'), upFirst(tx(w, 'status'))) +
      sect(t('moveInst'), `<div class="chips">${chipsOf(movs.concat(insts))}</div>`) +
      ((idx.theoryByItem.get(w.id) || []).length ? sect(t('theory'), `<div class="chips">${chipsOf(idx.theoryByItem.get(w.id))}</div>`) : '') +
      connHtml(w.id) + conceptsHtml(w.id) + learnHtml(w);
  }
  function designerCard(a) {
    const ws = worksSorted((idx.worksByDesigner.get(a.id) || []).map((w) => w.id));
    const kindLbl = a.kind === 'duo' ? (S.lang === 'es' ? 'Dúo' : 'Duo') : a.kind === 'collective' ? (S.lang === 'es' ? 'Colectivo' : 'Collective') : t('k_designer');
    return head(`${kindLbl} · ${discLabel(a)}`, a.name, `${esc(dateOf(a))}${(a.countries || []).length ? ' · ' + esc(a.countries.join(', ')) : ''}`, a.star, isoButton(a.id)) + imgBox(a, 'designer') +
      sect(t('keyIdea'), `<p class="key">${esc(tx(a, 'key'))}</p>`) + textSect(t('bio'), tx(a, 'more')) + ctxGroups(a.id, idx.worksByDesigner.get(a.id)) +
      sect(t('works'), `<div class="chips">${chipsOf(ws)}</div>`) +
      sect(t('moveInst'), `<div class="chips">${chipsOf([].concat(a.movements || [], a.institutions || []))}</div>`) +
      ((idx.prodByItem.get(a.id) || []).length ? sect(t('production'), `<div class="chips">${chipsOf(idx.prodByItem.get(a.id))}</div>`) : '') +
      ((idx.theoryByItem.get(a.id) || []).length ? sect(t('theory'), `<div class="chips">${chipsOf(idx.theoryByItem.get(a.id))}</div>`) : '') +
      connHtml(a.id) + conceptsHtml(a.id) + learnHtml(a);
  }
  function institutionCard(i) {
    const ds = (idx.designersByInst.get(i.id) || []).map((a) => a.id);
    const ws = worksSorted([...new Set([].concat(((i.links || {}).works || []), (idx.worksByMaker.get(i.id) || []).map((w) => w.id), relations(i.id).filter((r) => r.type === 'works').map((r) => r.other)))]);
    return head(`${t('ik_' + i.kind)} · ${discLabel(i)}`, nameOf(i), `${esc(dateOf(i))}${metaPlace(i) ? ' · ' + metaPlace(i) : ''}`, i.star, isoButton(i.id)) + imgBox(i, 'institution') +
      sect(t('keyIdea'), `<p class="key">${esc(tx(i, 'key'))}</p>`) + textSect(t('history'), tx(i, 'more')) + ctxGroups(i.id) +
      sect(t('people'), `<div class="chips">${chipsOf(ds)}</div>`) + sect(t('works'), `<div class="chips">${chipsOf(ws)}</div>`) +
      ((idx.prodByItem.get(i.id) || []).length ? sect(t('production'), `<div class="chips">${chipsOf(idx.prodByItem.get(i.id))}</div>`) : '') +
      ((idx.theoryByItem.get(i.id) || []).length ? sect(t('theory'), `<div class="chips">${chipsOf(idx.theoryByItem.get(i.id))}</div>`) : '') +
      connHtml(i.id) + conceptsHtml(i.id) + learnHtml(i);
  }
  // v20: macro-movement card: the overview that the era card used to give, now attached to the broad movement
  function macroCard(m) {
    const tr = (S.lang === 'es' && m.es && m.es.traits) || m.traits || [];
    const shifts = (S.lang === 'es' && m.es && m.es.shifts) || m.shifts || [];
    const cs = (S.lang === 'es' && m.es && m.es.context_summary) || m.context_summary || {};
    const sum = TRACKS.filter((k) => cs[k]).map((k) => `<div class="sum-item" data-t="${k}"><div class="sum-h">${lensWord(k)}</div>${esc(cs[k])}</div>`).join('');
    const parts = (m.parts || []).filter((x) => idx.byId.has(x)).sort((a, b) => idx.byId.get(a).start - idx.byId.get(b).start);
    const ds = [...new Set(parts.flatMap((p) => (idx.designersByMovement.get(p) || []).map((a) => a.id)))];
    return head('', nameOf(m), esc(dateOf(m)), m.star, isoButton(m.id), esc(t('k_macro'))) + imgBox(m, 'movement') +
      sect(t('keyIdea'), `<p class="key">${esc(tx(m, 'key'))}</p>`) +
      textSect(t('ctxText'), tx(m, 'context')) +
      (sum ? sect(t('ctxByFactor'), `<p class="sum-tip">${esc(t('focusTip'))}</p><div class="sum-list">${sum}</div>`) : '') +
      (shifts.length ? sect(t('keyShifts'), `<ul>${shifts.map((x) => `<li>${esc(x)}</li>`).join('')}</ul>`) : '') +
      (tr.length ? sect(t('recognise'), `<ul class="traits">${tr.map((x) => `<li>${esc(x)}</li>`).join('')}</ul>`) : '') +
      textSect(t('shift'), tx(m, 'shift')) + ctxGroups(m.id) +
      (parts.length ? sect(t('macroParts'), `<div class="chips">${chipsOf(parts)}</div>`) : sect(t('macroParts'), `<p class="muted">${esc(t('macroNoParts'))}</p>`)) +
      (ds.length ? sect(t('designers'), `<div class="chips">${chipsOf(ds)}</div>`) : '') +
      connHtml(m.id) + macroConceptsHtml(m) + learnHtml(m);
  }
  function movementCard(m) {
    if (m.macro) return macroCard(m);
    const ds = (idx.designersByMovement.get(m.id) || []).map((a) => a.id);
    const ws = worksSorted([...new Set([].concat((idx.worksByMovement.get(m.id) || []).map((w) => w.id), relations(m.id).filter((r) => r.type === 'works').map((r) => r.other)))]);
    const tr = (S.lang === 'es' && m.es && m.es.traits) || m.traits || [];
    const isoIcon = isoButton(m.id);
    return head(`${t('k_movement')} · ${discLabel(m)}`, nameOf(m), `${esc(dateOf(m))}${(m.countries || []).length ? ' · ' + esc(m.countries.join(', ')) : ''}`, m.star, isoIcon) + imgBox(m, 'movement') +
      sect(t('keyIdea'), `<p class="key">${esc(tx(m, 'key'))}</p>`) +
      (tr.length ? sect(t('recognise'), `<ul class="traits">${tr.map((x) => `<li>${esc(x)}</li>`).join('')}</ul>`) : '') +
      textSect(t('ctxText'), tx(m, 'context')) + textSect(t('shift'), tx(m, 'shift')) + ctxGroups(m.id) +
      sect(t('designers'), `<div class="chips">${chipsOf(ds)}</div>`) + sect(t('works'), `<div class="chips">${chipsOf(ws)}</div>`) +
      ((idx.prodByItem.get(m.id) || []).length ? sect(t('production'), `<div class="chips">${chipsOf(idx.prodByItem.get(m.id))}</div>`) : '') +
      ((idx.theoryByItem.get(m.id) || []).length ? sect(t('theory'), `<div class="chips">${chipsOf(idx.theoryByItem.get(m.id))}</div>`) : '') +
      connHtml(m.id) + conceptsHtml(m.id) + learnHtml(m);
  }
  function designLinksHtml(c) {
    const lns = idx.linksByCtx.get(c.id) || [];
    if (!lns.length) return '';
    return sect(t('related'), '<div class="link-list">' + lns.map((ln) => `<div class="link-item">${pchip(ln.item)}<span class="note">${esc(tx(ln, 'note'))}</span></div>`).join('') + '</div>');
  }
  // lens button for a card: turns on the lens of that kind of context
  // the name of a context sub-category is the lens switch, the same everywhere (like the row names on the line)
  function lensWord(track, text) {
    const on = S.focus === track, lbl = on ? t('focusOff') : t('focusBtn') + ': ' + t('tr_' + track);
    return `<button class="lens-word${on ? ' on' : ''}" data-focus="${track}" data-t="${track}" title="${esc(lbl)}" aria-pressed="${on}"><i class="sw"></i>${esc(text || t('tr_' + track))}</button>`;
  }
  function contextCard(c) {
    return head('', nameOf(c), `${esc(dateOf(c))}${(c.countries || []).length ? ' · ' + esc(c.countries.join(', ')) : ''}`, false, isoButton(c.id), `${esc(t('k_context'))} · ${lensWord(c.track)}`) +
      sect(t('keyIdea'), `<p class="key">${esc(tx(c, 'key'))}</p>`) + textSect(t('happened'), tx(c, 'happened')) +
      textSect(t('effect'), tx(c, 'effect'), 'effect') + designLinksHtml(c) + connHtml(c.id) + conceptsHtml(c.id) + learnHtml(c);
  }
  function designChips(it) {
    const lk = it.links || {};
    return [].concat(lk.movements || [], lk.institutions || [], lk.designers || [], lk.works || []);
  }
  function productionCard(p) {
    return head('', nameOf(p), esc(dateOf(p)), false, isoButton(p.id), `${lensWord('production', t('k_production'))} · ${esc(t('ps_' + p.sub))}`) +
      sect(t('keyIdea'), `<p class="key">${esc(tx(p, 'key'))}</p>`) + textSect(t('origin'), tx(p, 'origin')) + textSect(t('enabled'), tx(p, 'enabled')) +
      textSect(t('economy'), tx(p, 'economy')) + textSect(t('change'), tx(p, 'change'), 'effect') + textSect(t('relations'), tx(p, 'relations')) +
      sect(t('linkedTo'), `<div class="chips">${chipsOf(designChips(p))}</div>`) + ctxGroups(p.id) + connHtml(p.id) + conceptsHtml(p.id) + learnHtml(p);
  }
  function theoryCard(th) {
    const ideas = (S.lang === 'es' && th.es && th.es.ideas) || th.ideas || [];
    const src = (th.sources || []).map((s) => `<li>${extLink(s.url, (S.lang === 'es' && s.es) || s.label)}</li>`).join('');
    return head('', nameOf(th), `${th.author ? esc(th.author) + ' · ' : ''}${esc(dateOf(th))}`, th.star, isoButton(th.id), `${esc(t('k_theory'))} · ${esc(t('g_' + th.genre))}`) +
      imgGallery(th, 'theory') + sect(t('keyIdea'), `<p class="key">${esc(tx(th, 'key'))}</p>`) +
      (ideas.length ? sect(t('th_ideas'), `<ul class="traits">${ideas.map((x) => `<li>${esc(x)}</li>`).join('')}</ul>`) : '') +
      textSect(t('th_impact'), tx(th, 'impact')) + sect(t('th_sources'), `<ul>${src}</ul>`) +
      sect(t('linkedTo'), `<div class="chips">${chipsOf(designChips(th))}</div>`) + ctxGroups(th.id) + connHtml(th.id) + conceptsHtml(th.id) + learnHtml(th);
  }
  function conceptCard(c) {
    const hits = (idx.conceptItems.get(c.id) || []).slice();
    const order = { work: 0, designer: 1, movement: 2, institution: 3, context: 4, production: 5, theory: 6 };
    hits.sort((a, b) => (order[idx.kind.get(a)] - order[idx.kind.get(b)]) || String(a).localeCompare(b));
    return head(t('k_concept'), nameOf(c), '') + sect(t('whatIs'), `<p class="key">${esc(tx(c, 'key'))}</p>`) +
      sect(t('linkedTo'), `<div class="chips">${hits.slice(0, 40).map((x) => pchip(x)).join('')}</div>`) + learnHtml(c);
  }

  // ---------- Era overview and general card ----------
  function statsBlock(st) {
    const cell = (n, l) => `<div class="stat"><b>${typeof n === 'string' ? esc(n) : nfl(n)}</b><span>${esc(l)}</span></div>`;
    return `<div class="stats">${cell(st.works, t('n_works'))}${cell(st.designers, t('n_designers'))}${cell(st.movements, t('n_movements'))}${cell(st.institutions, t('n_institutions'))}${cell(st.contexts, t('n_contexts'))}${cell(st.theories, t('n_theories'))}${cell(st.production, t('n_production'))}</div>`;
  }
  function barsHtml(vals, keys, label) {
    const tot = keys.reduce((s, k) => s + (vals[k] || 0), 0) || 1;
    return `<div class="mbar" role="img" aria-label="${esc(label === 'disc' ? t('byDisc') : t('byTrack'))}">${keys.map((k) => `<i style="width:${(100 * (vals[k] || 0)) / tot}%;background:rgb(var(--c-${k}))"></i>`).join('')}</div>` +
      `<ul class="mlegend">${keys.map((k) => `<li><i class="sw" style="background:rgb(var(--c-${k}))"></i><span>${esc(label === 'disc' ? t('d_' + k) : t('tr_' + k))}</span><b>${nfl(vals[k] || 0)}</b><em>${Math.round((100 * (vals[k] || 0)) / tot)}%</em></li>`).join('')}</ul>`;
  }
  function eraCard() {
    const e = G.eraById.get(S.eraId) || G.eras[0];
    const zoomBtn = `<button class="p-btn" data-zoomera="${e.id}" title="${esc(t('eraZoom'))}" aria-label="${esc(t('eraZoom'))}"><svg width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><circle cx="6" cy="6" r="4.2" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M9.2 9.2L12.5 12.5M4 6h4M6 4v4" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg></button>`;
    const h = head(t('overview'), eraName(e), '', false, zoomBtn);
    const intro = `<section class="sect"><p class="key">${esc(tx(e, 'intro'))}</p></section>`;
    if (!e.ready) return h + intro + `<section class="sect"><p class="muted">${esc(t('emptyEra'))}</p></section>`;
    const shifts = (S.lang === 'es' && e.es && e.es.shifts) || e.shifts || [];
    const cs = (S.lang === 'es' && e.es && e.es.context_summary) || e.context_summary || {};
    const sum = TRACKS.filter((k) => cs[k]).map((k) => {
      return `<div class="sum-item" data-t="${k}"><div class="sum-h">${lensWord(k)}</div>${esc(cs[k])}</div>`;
    }).join('');
    const st = G.stats[e.id];
    const cons = S.data.concepts.filter((c) => c.era === e.id);
    const concepts = cons.length ? sect(S.lang === 'es' ? 'Conceptos' : 'Concepts', `<div class="chips">${cons.map((c) => pchip(c.id)).join('')}</div>`) : '';
    return h + intro +
      (shifts.length ? sect(t('keyShifts'), `<ul>${shifts.map((x) => `<li>${esc(x)}</li>`).join('')}</ul>`) : '') +
      (sum ? sect(t('ctxSynth'), `<p class="sum-tip">${esc(t('focusTip'))}</p><div class="sum-list">${sum}</div>`) : '') + concepts +
      (st ? sect(t('infoStats'), statsBlock(st)) : '');
  }
  // the lens card: design seen from one kind of context
  function lensCard() {
    const k = S.focus, F = S.F || makeFocus(k), d = S.data;
    const facts = [...F.facts].filter((x) => !S.SC || S.SC.facts.has(x)).map((x) => idx.byId.get(x)).filter(Boolean).sort((a, b) => (yearOf(a) || 0) - (yearOf(b) || 0));
    const byKind = { movement: [], institution: [], designer: [], work: [] };
    [...F.ids].forEach((x) => { const kd = idx.kind.get(x); if (byKind[kd]) byKind[kd].push(x); });
    const sortY = (l) => l.map((x) => idx.byId.get(x)).filter(Boolean).sort((a, b) => (yearOf(a) || 0) - (yearOf(b) || 0)).map((x) => x.id);
    if (S.SC) { Object.keys(byKind).forEach((kd) => { byKind[kd] = byKind[kd].filter((x) => S.SC.ids.has(x)); }); }
    const nDesign = Object.values(byKind).reduce((a, l) => a + l.length, 0);
    // v20: the summary of this kind of context in each macro-movement (the eras are gone)
    const eras = TRACKS.includes(k) ? d.movements.filter((m) => m.macro).sort((a, b) => a.start - b.start).map((m) => {
      const cs = (S.lang === 'es' && m.es && m.es.context_summary) || m.context_summary || {};
      return cs[k] ? `<div class="sum-item" data-t="${k}"><div class="sum-h"><b>${esc(nameOf(m))} <span class="y">${esc(dateOf(m))}</span></b><button class="lens-mini" data-go="${m.id}">${esc(t('lensEraCard'))}</button></div>${esc(cs[k])}</div>` : '';
    }).join('') : '';
    const designSects = [['movement', 'n_movements'], ['institution', 'n_institutions'], ['designer', 'n_designers'], ['work', 'n_works']]
      .filter(([kd]) => byKind[kd].length).map(([kd, lbl]) => `<div class="info-sub">${esc(upFirst(t(lbl)))} · ${byKind[kd].length}</div><div class="chips">${chipsOf(sortY(byKind[kd]))}</div>`).join('');
    const e = essayOf('lens-' + k);
    const metaTail = `${nfl(facts.length)} ${t(k === 'production' || k === 'theory' ? 'nItems' : 'nFacts')} · ${nfl(nDesign)} ${t(e ? 'lensElems' : 'lensLinked')}`;
    const meta = e ? `${t('essayWord')} · ${essayMin(e)} ${t('minRead')} · ${metaTail}` : metaTail;
    return `<div class="lens-card" data-t="${k}">` + head(t('lensKicker'), e ? essayLang(e).title : t('tr_' + k), esc(meta), false, '', '', false) + essayWarn(e) +
      (e ? `<section class="sect essay"><p class="essay-sub">${esc(essayLang(e).subtitle)}</p>${essayParas(e)}</section>${essaySources(e)}` : sect(t('lensHow'), paras(t('lens_' + k)))) +
      (eras ? sect(t('lensByEra'), `<div class="sum-list">${eras}</div>`) : '') +
      sect(t('lensFacts'), `<div class="chips">${chipsOf(facts.map((x) => x.id))}</div>`) +
      (designSects ? sect(t('lensDesign'), designSects) : '') +
      `<section class="sect"><p class="sum-tip">${esc(t('lensTip'))}</p></section></div>`;
  }
  // the discipline card (scope): essay on the history of that discipline plus what stays on the line
  function discCard() {
    const disc = S.scope, SC = S.SC || makeScope(disc), d = S.data, e = essayOf('disc-' + disc);
    const L2 = (es, en) => (S.lang === 'es' ? es : en);
    const sortY = (l) => l.filter((x) => SC.ids.has(x.id) && !x.macro && levelOk(x) && regionOk(x)).sort((a, b) => (yearOf(a) || 0) - (yearOf(b) || 0));
    const meta = [e ? `${t('essayWord')} · ${essayMin(e)} ${t('minRead')}` : null, `${nfl(SC.nWorks)} ${t('n_works')}`, `${nfl(SC.nDesigners)} ${t('n_designers')}`].filter(Boolean).join(' · ');
    const plain = (label, l) => (l.length ? `<div class="info-sub">${esc(upFirst(label))} · ${l.length}</div><div class="chips">${chipsOf(l.map((x) => x.id))}</div>` : '');
    const starred = (label, l) => {
      if (!l.length) return '';
      const st = l.filter((x) => x.star), rest = l.filter((x) => !x.star);
      return `<div class="info-sub">${esc(upFirst(label))} ★ · ${st.length}</div><div class="chips">${chipsOf(st.map((x) => x.id))}</div>` +
        (rest.length && S.level === 'normal' ? `<details class="see-all"><summary>${esc(t('seeAll'))} (${rest.length})</summary><div class="chips">${chipsOf(rest.map((x) => x.id))}</div></details>` : '');
    };
    const facts = [...SC.facts].filter((x) => idx.byId.has(x)).sort((a, b) => (SC.cnt.get(b) || 0) - (SC.cnt.get(a) || 0)).slice(0, 12);
    return `<div class="lens-card disc-card" style="--tc:var(--c-${disc});--tt:var(--t-${disc})" data-disc="${disc}">` +
      head(t('kDisc'), e ? essayLang(e).title : t('dt_' + disc), esc(meta), false, '', '', false) + essayWarn(e) +
      (e ? `<section class="sect essay"><p class="essay-sub">${esc(essayLang(e).subtitle)}</p>${essayParas(e)}</section>${essaySources(e)}` : '') +
      sect(L2('En la línea', 'On the line'),
        plain(t('n_movements'), sortY(d.movements)) + plain(t('n_institutions'), sortY(d.institutions)) +
        starred(t('n_designers'), sortY(d.designers)) + starred(t('n_works'), sortY(d.works)) +
        (facts.length ? `<div class="info-sub">${esc(t('ctxTop'))}</div><div class="chips">${chipsOf(facts)}</div>` : '')) +
      `<section class="sect"><p class="sum-tip">${esc(t('scopeTip'))}</p></section></div>`;
  }
  // v52 (D8, etapa 7): conceptual and bibliographic basis of the timeline (Forty first, then the general histories by discipline)
  const BASIS = [
    ['Adrian Forty', 'Objects of Desire: Design and Society since 1750', 1986, 'gen'],
    ['Nikolaus Pevsner', 'Pioneers of the Modern Movement', 1936, 'gen'], ['Sigfried Giedion', 'Mechanization Takes Command', 1948, 'gen'],
    ['Reyner Banham', 'Theory and Design in the First Machine Age', 1960, 'gen'], ['John Heskett', 'Industrial Design', 1980, 'gen'],
    ['Penny Sparke', 'An Introduction to Design and Culture', 1986, 'gen'], ['Jonathan Woodham', 'Twentieth-Century Design', 1997, 'gen'],
    ['David Raizman', 'History of Modern Design', 2003, 'gen'], ['Victor Margolin', 'World History of Design', 2015, 'gen'],
    ['Philip B. Meggs y Alston W. Purvis', "Meggs' History of Graphic Design", 1983, 'graphic'], ['Stephen Eskilson', 'Graphic Design: A New History', 2007, 'graphic'],
    ['Kenneth Frampton', 'Modern Architecture: A Critical History', 1980, 'architecture'], ['William J. R. Curtis', 'Modern Architecture since 1900', 1982, 'architecture'],
    ['Christopher Breward', 'The Culture of Fashion', 1995, 'fashion'], ['Valerie Steele', 'Fifty Years of Fashion: New Look to Now', 1997, 'fashion'],
    ['Silvia Fernández y Gui Bonsiepe (coords.)', 'Historia del diseño en América Latina y el Caribe', 2008, 'latam'],
  ];
  function basisList() {
    const groups = ['gen', 'graphic', 'architecture', 'fashion', 'latam'];
    const au = (a) => (S.lang === 'es' ? a : a.replace(' y ', ' and ').replace('(coords.)', '(eds.)'));
    return groups.map((g) => `<div class="info-sub basis-h">${esc(t('basis_' + g))}</div><ul class="basis">` +
      BASIS.filter((b) => b[3] === g).map((b) => `<li>${esc(au(b[0]))}, <i>${esc(b[1])}</i> (${b[2]})</li>`).join('') + '</ul>').join('');
  }

  function infoCard() {
    const eras = G.stats || {};
    const tot = { movements: 0, institutions: 0, designers: 0, works: 0, stars: 0, contexts: 0, production: 0, theories: 0, concepts: 0, connections: 0, worksWithContext: 0, byDiscipline: {}, byTrack: {} };
    Object.values(eras).forEach((s) => {
      ['movements', 'institutions', 'designers', 'works', 'stars', 'contexts', 'production', 'theories', 'concepts', 'connections', 'worksWithContext'].forEach((k) => { tot[k] += s[k] || 0; });
      DISCS.forEach((k) => { tot.byDiscipline[k] = (tot.byDiscipline[k] || 0) + ((s.byDiscipline || {})[k] || 0); });
      TRACKS.forEach((k) => { tot.byTrack[k] = (tot.byTrack[k] || 0) + ((s.byTrack || {})[k] || 0); });
    });
    const list = (rows, tone) => `<dl class="info-list">${rows.map(([k, v]) => `<dt${tone ? ` data-t="${k}"` : ''}>${tone ? '<i></i>' : ''}${esc(tone ? t('tr_' + k) : k)}</dt><dd>${esc(v)}</dd>`).join('')}</dl>`;
    const pct = tot.works ? Math.round((100 * tot.worksWithContext) / tot.works) : 0;
    const mini = (v) => { const tt = DISCS.reduce((a, k) => a + (v[k] || 0), 0) || 1; return `<span class="mbar">${DISCS.map((k) => `<i style="width:${(100 * (v[k] || 0)) / tt}%;background:rgb(var(--c-${k}))"></i>`).join('')}</span>`; };
    // v20: presentation, sections, element types, figures, a link to the help and a disclaimer (no instructions here)
    const nOf = (k) => (S.data[k] || []).filter((x) => !x.macro).length;
    const nMacro = S.data.movements.filter((m) => m.macro).length;
    const lvN = (k) => ['movements', 'institutions', 'designers', 'works', 'theories'].reduce((a, key) => a + S.data[key].filter((x) => x.level === k).length, 0);
    const cell = (n, l) => `<div class="stat"><b>${typeof n === 'string' ? esc(n) : nfl(n)}</b><span>${esc(l)}</span></div>`;
    return head(t('infoKicker'), t('title'), esc(t('infoSpan'))) +
      `<section class="sect"><div class="thesis">${esc(t('infoThesis'))}</div></section>` +
      sect(t('infoAbout'), paras(t('infoIntro'))) +
      sect(t('infoBasis'), paras(t('infoBasisText')) + basisList()) +
      sect(t('infoSecs'), `<div class="info-sub">${esc(t('infoCtxHead'))}</div>${list(t('infoCtx'), true)}<div class="info-sub">${esc(t('infoDesignHead'))}</div>${list(t('infoDesign'), false)}<div class="info-sub">${esc(t('infoOtherHead'))}</div>${list(t('infoOther'), false)}`) +
      sect(t('infoStats'), `<div class="stats">${cell(tot.works, t('n_works'))}${cell(tot.designers, t('n_designers'))}${cell(nOf('movements'), t('n_movements'))}${cell(nMacro, S.lang === 'es' ? 'macromovimientos' : 'macro-movements')}${cell(tot.institutions, t('n_institutions'))}${cell(tot.theories, t('n_theories'))}${cell(tot.contexts, t('n_contexts'))}${cell(tot.production, t('n_production'))}${cell(pct + '%', t('pctCtx'))}</div>` +
        `<p class="sum-tip" style="margin-top:8px">${esc(t('lv_essential'))} ★ ${nfl(lvN('essential'))} · ${esc(t('lv_normal'))} ${nfl(lvN('normal'))}</p>`) +
      sect(t('byDisc'), barsHtml(tot.byDiscipline, DISCS, 'disc')) + sect(t('byTrack'), barsHtml(tot.byTrack, TRACKS, 'track')) +
      `<section class="sect"><button class="focus-btn inline help-link" data-help="1" title="${esc(t('infoHowToTip'))}">${esc(t('infoHowTo'))} →</button></section>` +
      `<section class="sect"><p class="disclaimer">${esc(t('infoDisclaimer'))}</p></section>`;
  }

  // nothing selected: an empty card with a short hint
  function emptyCard() {
    return `<div class="empty-card"><svg width="40" height="40" viewBox="0 0 40 40" aria-hidden="true"><rect x="7" y="5" width="26" height="30" rx="3" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 13h16M12 19h16M12 25h10" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg><p class="em">${esc(t('emptyMsg'))}</p><p>${esc(t('emptyEraHint'))}</p><p>${esc(t('emptyInfo'))}</p></div>`;
  }
  // Edit mode: number the sources of the open card. Its own refs keep their numbers (1..n); the refs of its
  // context links follow (n+1...), in the order they are cited and then the rest.
  function rfRender(html, id) {
    const own = (id && RF.owners.get(id) && RF.owners.get(id).refs) || [];
    const gmap = new Map();   // 'owner|n' -> number in this card
    html = html.replace(/="([^"]*)"/g, (m, v) => (v.includes('⟦') ? '="' + v.replace(RF_TOK, '') + '"' : m));
    html = html.replace(RF_TOK, (m, owner, n) => {
      let g;
      if (owner === id) g = +n;
      else { const k = owner + '|' + n; if (!gmap.has(k)) gmap.set(k, own.length + gmap.size + 1); g = gmap.get(k); }
      return `<sup class="rf"><a href="#rf-${g}" data-rf="${g}">${g}</a></sup>`;
    });
    return html.replace('⟦FUENTES⟧', id ? rfList(id, own, gmap) : '');
  }
  // one row of a sources list (cards and essays)
  function rfRow(g, r, of) {
    const u = r.url ? `<a href="${esc(r.url)}" target="_blank" rel="noopener noreferrer">${esc(r.label)}</a> <span class="rf-dom">${esc((r.url.match(/^https:\/\/(?:www\.)?([^/]+)/) || [])[1] || '')}</span>` : esc(r.label);
    return `<li id="rf-${g}"><span class="rf-n">${g}</span><div>${u}${r.checks ? `<div class="rf-ck">${esc(r.checks)}${r.date ? ` · <span class="rf-dt">${esc(r.date)}</span>` : ''}</div>` : ''}${of ? `<div class="rf-of">${of}</div>` : ''}</div></li>`;
  }
  // the "Sources" section of an essay (its own refs, numbered as the superscripts of its text); closed on opening
  function essaySources(e) {
    const refs = (e && e.refs) || [];
    if (!refs.length) return '';
    const title = S.lang === 'es' ? 'Fuentes del ensayo' : 'Essay sources';
    return `<details class="sect sources essay-sources"><summary><span class="rf-t">${esc(title)} (${refs.length})</span></summary><ol class="rf-list">${refs.map((r, i) => rfRow(i + 1, r, '')).join('')}</ol></details>`;
  }
  function rfList(id, own, gmap) {
    const L2 = (es, en) => (S.lang === 'es' ? es : en);
    const row = rfRow;
    const rows = own.map((r, i) => [i + 1, row(i + 1, r, '')]);
    // direct context links of this card (as fact or as design element)
    const lks = [].concat(idx.linksByItem.get(id) || [], idx.kind.get(id) === 'context' ? idx.linksByCtx.get(id) || [] : []);
    lks.forEach((l) => {
      const key = 'L:' + l.ctx + '~' + l.item, o = RF.owners.get(key);
      if (!o || !o.refs.length) return;
      const of = esc(L2('Enlace', 'Link')) + ': ' + esc(rfPlain(nameOf(idx.byId.get(l.ctx)))) + ' → ' + esc(rfPlain(nameOf(idx.byId.get(l.item))));
      o.refs.forEach((r, i) => {
        const k = key + '|' + (i + 1);
        if (!gmap.has(k)) gmap.set(k, own.length + gmap.size + 1);
        rows.push([gmap.get(k), row(gmap.get(k), r, of)]);
      });
    });
    // refs cited from other owners (connections) that are not direct links
    gmap.forEach((g, k) => {
      if (rows.some((x) => x[0] === g)) return;
      const [owner, n] = k.split('|'), o = RF.owners.get(owner), r = o && o.refs[+n - 1];
      if (r) rows.push([g, row(g, r, esc(L2('Conexión', 'Connection')))]);
    });
    rows.sort((a, b) => a[0] - b[0]);
    // v30 (point 59): public "Sources" section, last of the card, collapsed by default. No sources = not reviewed (warning).
    const warn = `<svg class="rf-warn" role="img" aria-label="${esc(L2('Ficha no revisada', 'Card not reviewed'))}" width="15" height="15" viewBox="0 0 16 16"><title>${esc(L2('Ficha no revisada', 'Card not reviewed'))}</title><path d="M8 1.8L15 14H1z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M8 6.2v3.8M8 12v.1" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>`;
    const imgs = (S.imgRefs && S.imgRefs.length) ? `<ul class="rf-imgs">${S.imgRefs.join('')}</ul>` : '';
    const body = imgs + (rows.length ? `<ol class="rf-list">${rows.map((x) => x[1]).join('')}</ol>`
      : `<p class="rf-none">${esc(L2('Esta ficha aún no ha sido revisada: no tiene fuentes registradas, así que su contenido podría contener errores.', 'This card has not been reviewed yet: it has no recorded sources, so its content may contain errors.'))}</p>`);
    return `<details class="sect sources${rows.length ? '' : ' unrev'}"${S.srcOpen === id ? ' open' : ''}><summary>${rows.length ? '' : warn}<span class="rf-t">${esc(L2('Fuentes', 'Sources'))} (${rows.length})</span></summary>${body}</details>`;
  }
  // number of recorded sources of a card: its own plus those of the context links that touch it (same rule as rfList)
  function srcCount(id) {
    const o = RF.owners.get(id);
    let n = o ? o.refs.length : 0;
    [].concat(idx.linksByItem.get(id) || [], idx.kind.get(id) === 'context' ? idx.linksByCtx.get(id) || [] : []).forEach((l) => { const q = RF.owners.get('L:' + l.ctx + '~' + l.item); if (q) n += q.refs.length; });
    return n;
  }

  function renderPanel() {
    const p = $('panel');
    const d = S.data;
    let html = '', withSrc = false;
    // the [n] markers become tokens only while the card is built (so search, tooltips and labels never see them)
    rfMode(true); S.imgRefs = [];
    try {
      if (S.info) html = infoCard();
      else if (S.review && ED.on) html = ED.summaryCard();
      else if (!d) html = '';
      else if ((!S.sel || !idx.byId.has(S.sel)) && cardKind() === 'focus') html = lensCard();
      else if ((!S.sel || !idx.byId.has(S.sel)) && cardKind() === 'scope') html = discCard();
      else if (!S.sel || !idx.byId.has(S.sel)) html = emptyCard();
      else {
        const id = S.sel, k = idx.kind.get(id), it = idx.byId.get(id);
        html = k === 'work' ? workCard(it) : k === 'designer' ? designerCard(it) : k === 'institution' ? institutionCard(it) : k === 'movement' ? movementCard(it)
          : k === 'context' ? contextCard(it) : k === 'production' ? productionCard(it) : k === 'theory' ? theoryCard(it) : conceptCard(it);
        if (ED.on) html += ED.reviewHtml(id);
        html += '⟦FUENTES⟧'; withSrc = true;
      }
      html = withSrc ? rfRender(html, S.sel) : rfPlain(html.replace(/="([^"]*)"/g, (m, v) => (v.includes('⟦') ? '="' + rfPlain(v) + '"' : m)));
    } finally { rfMode(false); }
    const key = S.info ? 'info' : S.review && ED.on ? 'review' : S.sel || (S.showEraCard ? 'era:' + S.eraId + S.lang : cardKind() === 'focus' ? 'lens:' + S.focus + S.lang : cardKind() === 'scope' ? 'scope:' + S.scope + S.lang : 'empty');
    S.panelToken = (S.panelToken || 0) + 1;
    p.innerHTML = html;
    if (S.panelKey !== key) { p.scrollTop = 0; S.panelKey = key; }
    hydrateImages(S.panelToken);
  }

  // ---------- Selection and navigation ----------
  const laneKeyOf = (id) => {
    const k = idx.kind.get(id), it = idx.byId.get(id);
    if (!it) return [];
    if (k === 'context') return ['trk:' + it.track];
    if (k === 'production') return ['trk:production', 'psub:' + it.sub];
    if (['movement', 'institution', 'designer', 'work', 'theory'].includes(k)) return (S.itemKeys && S.itemKeys.get(id)) || [];
    return [];
  };
  function setHash(id) {
    try { history.replaceState(null, '', id ? '#' + id : location.pathname + location.search); } catch (err) { /* ignore */ }
  }
  function resetFilters() {
    S.scope = null; S.scopeSnap = null; S.disc = new Set(DISCS); S.regions = new Set(REGIONS); S.types = new Set(TYPES);
    Object.keys(S.ctxShow).forEach((k) => { S.ctxShow[k] = true; });
  }
  function scrollToItem(id) {
    const el = $('content').querySelector(`.it[data-id="${CSS.escape(id)}"]`);
    if (!el) return false;
    const vp = $('viewport');
    const x = el.offsetLeft, y = el.offsetTop;
    const vx = vp.scrollLeft, vy = vp.scrollTop, vw = vp.clientWidth, vh = vp.clientHeight;
    const nx = x < vx + 20 || x > vx + vw - 80 ? Math.max(0, x - vw * 0.35) : vx;
    const ny = y < vy + 10 || y > vy + vh - 50 ? Math.max(0, y - vh * 0.3) : vy;
    vp.scrollTo(nx, ny);
    syncScroll();
    return true;
  }
  // the era card, without moving the view (era bar in Movements, info card)
  // v20: the eras are not shown any more (they are only data folders); these zoom to an era's span, for old links and tests
  function setEraView(eraId) {
    const e = G.eraById.get(eraId); if (!e) return;
    if (S.help) setHelp(false);
    setRangeYears(e.start, Math.min(e.end, NOWY()));
  }
  const showEra = setEraView;
  // ---------- Help window (button ?) ----------
  function helpHTML() {
    const H = t('help'), L = S.lang;
    const ic = (id) => `<span class="ic">${$(id).innerHTML}</span>`;
    const sv = (w, h, inner) => `<svg width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" aria-hidden="true">${inner}</svg>`;
    const gl = (d, col) => `<svg width="14" height="14" viewBox="-2 -2 14 14" aria-hidden="true"><path d="${GLYPH[d]}" fill="${col}"/></svg>`;
    const dc = (k) => `rgb(var(--c-${k}))`;
    const lgDesignIcons = [
      '<span class="lg-macro"></span>',
      '<span class="lg-mv"></span>',
      sv(26, 14, `<path d="M1 2.5 H19 L24.5 7 L19 11.5 H1 Z" fill="var(--surface)" stroke="rgb(var(--c-neutral))" stroke-width="1" stroke-linejoin="round"/>`),
      '<span class="lg-des"></span>',
      '<span class="lg-des multi"></span>',
      gl('graphic', dc('graphic')), gl('product', dc('product')), gl('fashion', dc('fashion')), gl('architecture', dc('architecture')),
      sv(14, 14, `<path d="${STAR}" transform="translate(2,2) scale(1)" fill="var(--star)"/>`),
      sv(14, 14, `<rect x="3.2" y="2.5" width="7.6" height="9" rx="1" fill="var(--surface)" stroke="rgb(var(--c-theory))" stroke-width="1.5"/><path d="M3.2 2.5v9" stroke="rgb(var(--c-theory))" stroke-width="3"/>`)
    ];
    const tone = 'rgb(var(--c-neutral))';
    const lgContextIcons = [
      sv(14, 14, `<circle cx="7" cy="7" r="3.5" fill="${tone}"/>`),
      '<span class="lg-span"></span>',
      sv(22, 14, `<rect x="0" y="6" width="14" height="3" rx="1.5" fill="${tone}" opacity=".6"/><path d="M14 3.5L20 7.5l-6 4z" fill="${tone}"/>`),
      sv(34, 14, `<circle cx="4" cy="7" r="3.5" fill="${tone}"/><rect x="10" y="5.5" width="14" height="3" rx="1.5" fill="var(--muted)" opacity=".5"/><path d="M27 3L33 7l-6 4z" fill="${tone}"/>`),
      sv(14, 14, `<rect x="3.5" y="3.5" width="7" height="7" rx="1" transform="rotate(45 7 7)" fill="${tone}"/>`)
    ];
    const lgConnIcons = [
      sv(34, 14, `<path d="M2 12 C17 12 17 2 32 2" fill="none" stroke="rgb(var(--c-political))" stroke-width="1.6"/><circle cx="32" cy="2" r="2" fill="rgb(var(--c-political))"/>`),
      sv(34, 14, `<path d="M2 12 C17 12 17 2 32 2" fill="none" stroke="${tone}" stroke-width="1.6"/><circle cx="32" cy="2" r="2" fill="${tone}"/>`),
      sv(34, 14, `<path d="M2 12 C17 12 17 2 32 2" fill="none" stroke="${tone}" stroke-width="0.8"/><circle cx="32" cy="2" r="2" fill="${tone}"/>`),
      sv(34, 14, `<path d="M2 12 C15 12 15 4 26 4" fill="none" stroke="${tone}" stroke-width="1.6" stroke-dasharray="4 3"/><path d="M33 4 L26 0.5 L26 7.5Z" fill="${tone}"/>`)
    ];
    const parts = H.parts.map(([n, d], i) => `<li><span class="hb">${i + 1}</span><span><b>${esc(n)}.</b> ${esc(d)}</span></li>`).join('');
    const row = (icons, labels) => labels.map((x, i) => `<div>${icons[i]}<span>${esc(x)}</span></div>`).join('');
    const tones = [...TRACKS, 'production'].map((k) => `<span class="lg-tone"><i style="background:rgb(var(--c-${k}))"></i>${esc(t('tr_' + k))}</span>`).join('');
    const keys = H.keys.map(([k, d]) => `<tr><td>${k}</td><td>${esc(d)}</td></tr>`).join('');
    return `<div class="hin"><p class="help-lead">${esc(H.lead)}</p>
      <section class="hsec"><h3>${esc(H.h1)}</h3><figure class="hfig"><img src="help/overview-${L}.webp" alt="${esc(H.f1)}" width="1800" height="1125" loading="lazy"><figcaption>${esc(H.f1)}</figcaption></figure><ol class="hparts">${parts}</ol></section>
      <section class="hsec"><h3>${esc(H.h2)}</h3><ul>${H.move.map((m) => `<li>${m}</li>`).join('')}</ul></section>
      <section class="hsec"><h3>${esc(H.h3)}</h3>
        <h4>${esc(H.hDesign)}</h4><div class="hlegend">${row(lgDesignIcons, H.lgDesign)}</div>
        <h4>${esc(H.hContext)}</h4><div class="hlegend">${row(lgContextIcons, H.lgContext)}</div>
        <h4>${esc(H.hConn)}</h4><div class="hlegend">${row(lgConnIcons, H.lgConn)}</div>
        <div class="lg-tones"><span>${esc(H.lgTone)}</span>${tones}</div>
        <p>${esc(H.legendNote)}</p></section>
      <section class="hsec"><h3>${esc(H.h4)}</h3><ul>${H.card.map((m) => `<li>${m}</li>`).join('')}</ul></section>
      <section class="hsec"><h3>${esc(H.h5)}</h3><table class="hkeys"><tbody>${keys}</tbody></table></section></div>`;
  }
  function syncHelpBtn() {
    const b = $('helpBtn'); if (!b) return;
    b.setAttribute('aria-pressed', String(!!S.help)); b.title = t('helpBtn'); b.setAttribute('aria-label', t('helpBtn'));
    $('helpClose').title = t('close'); $('helpClose').setAttribute('aria-label', t('close'));
    $('helpTitle').textContent = t('helpTitle');
  }
  function setHelp(on) {
    S.help = !!on;
    $('help').hidden = !S.help;
    if (S.help) { $('helpBody').innerHTML = helpHTML(); $('helpBody').scrollTop = 0; $('helpClose').focus({ preventScroll: true }); }
    syncHelpBtn();
    if (!S.help) $('viewport').focus({ preventScroll: true });
  }

  // ---------- Only this movement ----------
  // "only its connections": the element and everything it is directly connected to (all kinds of relation)
  function makeIso(id) {
    const set = new Set([id, ...relations(id).map((r) => r.other)]);
    // v19.2 (point 33): a movement or an institution also keeps the works its designers made while it existed
    // (an institution with no end counts up to today). They hang on the designer's line, without a curve of their own.
    const k = idx.kind.get(id), it = idx.byId.get(id);
    if (it && (k === 'movement' || k === 'institution')) {
      const y0 = it.start, y1 = it.end != null ? it.end : NOWY();
      const des = (k === 'movement' ? idx.designersByMovement : idx.designersByInst).get(id) || [];
      des.forEach((a) => (idx.worksByDesigner.get(a.id) || []).forEach((w) => { if (w.year >= y0 && w.year <= y1) set.add(w.id); }));
    }
    return { id, set };
  }
  function setIso(mid) {
    if (!mid) {
      if (S.iso && S.isoPrev) S.collapsed = S.isoPrev;
      S.iso = null; S.isoPrev = null;
    } else {
      if (!S.iso) S.isoPrev = new Set(S.collapsed);
      S.iso = makeIso(mid);
      S.iso.set.forEach((x) => laneKeyOf(x).forEach((k) => S.collapsed.delete(k)));
    }
    render();
    if (mid) { $('viewport').scrollTop = 0; scrollToItem(mid); }
  }

  function reveal(id) {
    const tr = trackOf(id);
    if (S.focus && tr && tr !== S.focus) applyFocus(null, { partial: true });   // a fact of another row: leave the lens
    laneKeyOf(id).forEach((k) => S.collapsed.delete(k));
    if (tr && !S.ctxShow[tr]) S.ctxShow[tr] = true;
  }
  // a short message at the bottom of the line (v20)
  let toastT = 0;
  function toast(msg) {
    let el = document.getElementById('toast');
    if (!el) { el = document.createElement('div'); el.id = 'toast'; el.className = 'toast'; el.setAttribute('role', 'status'); document.body.appendChild(el); }
    el.textContent = msg; el.classList.add('on');
    clearTimeout(toastT); toastT = setTimeout(() => el.classList.remove('on'), 2600);
  }
  function select(id, o = {}) {
    if (S.help) setHelp(false);
    if (S.iso && id && !S.iso.set.has(id)) { if (S.isoPrev) S.collapsed = S.isoPrev; S.iso = null; S.isoPrev = null; }
    if (id !== S.sel) S.srcOpen = null;
    S.info = false; S.review = false; S.sel = id || null; S.showEraCard = false;
    if (ED.on) { ED.msg = ''; ED.imgForm = null; }
    const it = id && idx.byId.get(id);
    if (it && it.era) S.eraId = it.era;
    // v20: going to an element of a higher detail level raises the level (it never lowers by itself)
    if (it && it.level && LEVEL_RANK[it.level] > LEVEL_RANK[S.level]) { S.level = it.level; store.set('lhd-level', S.level); toast(t('lvRaised') + ' «' + t('lv_' + S.level) + '»'); }
    if (id && o.reveal !== false) reveal(id);
    setHash(S.sel);
    render();
    if (id && o.scroll && kindOf(id) !== 'concept' && !scrollToItem(id)) {
      // hidden by a filter: show everything and try again
      resetFilters(); render(); scrollToItem(id);
    }
  }
  // jump to an element from search, a chip or the address: zoom in when it is too far to read
  function go(id) {
    if (!idx.byId.has(id)) return;
    const it = idx.byId.get(id), y = yearOf(it);
    if (y && lp(y) < LOD_NEAR) { S.px = Math.min(L.max, LOD_NEAR / decAt(y).w); S.zoomed = true; }
    select(id, { scroll: true });
  }

  // ---------- Edit mode (?editar) ----------
  // Everyone gets the image overrides (ediciones/imagenes.json). With ?editar in the address, and the password that
  // lives in editar.php on the server, the card shows a pencil over the photo and a "Notes" section, and the top bar
  // gets a review summary. Nothing here holds the password: it is typed once per browser session.
  // 8.5c: how an element gets its picture: own free, own with rights reserved, stand-in (a work's or a movement's gallery), none
  function imgClass(it, kind) {
    const own = it.images || [];
    if (own.length) return own.some((i) => !i.r) ? 'free' : 'res';
    return slidesOf(it, kind).length ? 'proxy' : 'none';
  }
  function makeEditor() {
    const on = /(^|[?&])editar(=|&|$)/.test(location.search.slice(1));
    const L2 = (es, en) => (S.lang === 'es' ? es : en);
    const ss = { get(k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } }, set(k, v) { try { if (v == null) sessionStorage.removeItem(k); else sessionStorage.setItem(k, v); } catch (e) { /* ignore */ } } };
    const E = { on, key: null, imgs: {}, rev: {}, imgForm: null, msg: '', filt: { src: 'none', img: 'none', era: 'all' } };
    // v30 (point 59): a card is "observed" only while it has text in Observaciones (empty text = out of the lists)
    E.state = (id) => { const r = E.rev[id]; return r && r.obs ? 'observed' : 'none'; };
    E.img = (id) => E.imgs[id] || null;
    async function post(body) {
      const res = await fetch('editar.php', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(Object.assign({ clave: E.key }, body)) });
      let j = null; try { j = await res.json(); } catch (e) { /* not JSON: no PHP on this server */ }
      if (!j) throw new Error(L2('El servidor no respondió como se esperaba (¿hay PHP?).', 'The server did not answer as expected (is PHP available?).'));
      if (!j.ok) throw new Error(j.error || ('HTTP ' + res.status));
      return j;
    }
    // 8.5c (point 83): the page opens without asking; the password is asked on the first editing action
    // (pencil, notes, resolve, image change) and the action continues by itself once it is right.
    E.pending = null; E.mmsg = ''; E.open = { src: false, img: false, obs: false };
    async function login(k, quiet) {
      E.key = k;
      try {
        const j = await post({ accion: 'leer' });
        E.imgs = j.imagenes || {}; E.rev = j.revision || {}; E.msg = ''; E.mmsg = '';
        ss.set('lhd-ed-clave', k);
        return true;
      } catch (err) {
        E.key = null; ss.set('lhd-ed-clave', null);
        E.mmsg = quiet ? '' : err.message;
        return false;
      }
    }
    function closeModal() { const m = $('edModal'); if (m) m.remove(); E.pending = null; E.mmsg = ''; }
    function askKey(then) {
      E.pending = then || null; E.mmsg = '';
      let m = $('edModal'); if (m) m.remove();
      m = document.createElement('div'); m.id = 'edModal'; m.className = 'ed-modal';
      m.innerHTML = `<div class="ed-box" role="dialog" aria-modal="true" aria-labelledby="edModalT"><h3 id="edModalT">${esc(L2('Contraseña del modo edición', 'Edit-mode password'))}</h3><p class="rv-note">${esc(L2('Escríbela para editar. No se vuelve a pedir en esta sesión del navegador.', 'Type it to edit. It is not asked again in this browser session.'))}</p><div class="ed-login"><input type="password" id="edPass" autocomplete="current-password" aria-label="${esc(L2('Contraseña', 'Password'))}" placeholder="${esc(L2('Contraseña', 'Password'))}"><button class="ed-b pri" data-edlogin="1">${esc(L2('Entrar', 'Enter'))}</button><button class="ed-b" data-edmodalcancel="1">${esc(L2('Cancelar', 'Cancel'))}</button></div><p class="rv-err" id="edModalErr" role="alert"></p></div>`;
      document.body.appendChild(m);
      const i = $('edPass'); if (i) i.focus();
    }
    async function submitKey() {
      const v = (($('edPass') || {}).value || ''); if (!v) return;
      const ok = await login(v);
      if (!ok) { const e = $('edModalErr'); if (e) e.textContent = E.mmsg || L2('Contraseña incorrecta.', 'Wrong password.'); const i = $('edPass'); if (i) { i.select(); i.focus(); } return; }
      const fn = E.pending; closeModal(); render();
      if (fn) fn();
    }
    E.need = (fn) => { if (E.key) fn(); else askKey(fn); };
    E.init = async () => {
      try { const r = await fetch('ediciones/imagenes.json', { cache: 'no-store' }); if (r.ok) E.imgs = (await r.json()) || {}; } catch (err) { /* none */ }
      if (!on) return;
      document.documentElement.classList.add('editing');
      const bar = document.querySelector('.top .zoom');
      if (bar && !$('reviewBtn')) {
        const b = document.createElement('button');
        b.className = 'btn info'; b.id = 'reviewBtn'; b.type = 'button'; b.setAttribute('aria-pressed', 'false');
        b.innerHTML = '<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><rect x="2.5" y="2" width="11" height="12.5" rx="1.5" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M5 6l1.3 1.3L8.6 5M5 10.5h6M9.5 7h1.5" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>';
        b.addEventListener('click', () => { S.review = !S.review; S.info = false; E.open = { src: false, img: false, obs: false }; renderFilters(); renderPanel(); });
        bar.insertBefore(b, bar.firstChild);
        const tag = document.createElement('span'); tag.className = 'ed-tag'; tag.textContent = L2('Modo edición', 'Edit mode');
        document.querySelector('.brand').appendChild(tag);
        b.title = t('rv_btn'); b.setAttribute('aria-label', t('rv_btn'));
      }
      const k = ss.get('lhd-ed-clave');
      if (k) { await login(k, true); render(); }
    };
    E.pencil = (id) => {
      if (!on) return '';
      const lbl = L2('Cambiar la imagen (pegar una URL)', 'Change the image (paste a URL)');
      const form = E.imgForm === id ? `<div class="ed-imgform"><input type="url" id="edImgUrl" value="${esc(E.img(id) || '')}" placeholder="https://upload.wikimedia.org/…" aria-label="URL"><div class="rv-acts"><button class="ed-b pri" data-edimgsave="${esc(id)}">${esc(L2('Guardar', 'Save'))}</button>${E.img(id) ? `<button class="ed-b" data-edimgclear="${esc(id)}">${esc(L2('Volver a la automática', 'Back to automatic'))}</button>` : ''}<button class="ed-b" data-edimgcancel="1">${esc(L2('Cancelar', 'Cancel'))}</button></div><p class="rv-note">${esc(L2('Pega el enlace directo a una imagen (https). Reemplaza la imagen automática de Wikipedia para todos.', 'Paste the direct link to an image (https). It replaces the automatic Wikipedia image for everyone.'))}</p>${E.msg ? `<p class="rv-err">${esc(E.msg)}</p>` : ''}</div>` : '';
      return `<button class="p-edit" data-edimg="${esc(id)}" title="${esc(lbl)}" aria-label="${esc(lbl)}"><svg width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><path d="M2 12l.6-2.8L9.8 2l2.2 2.2-7.2 7.2zM8.6 3.2l2.2 2.2" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/></svg></button>${form}`;
    };
    E.reviewHtml = (id) => {
      if (!on) return '';
      const r = E.rev[id] || {};
      const hist = (r.historial || []).map((h) => `<li><span class="rv-date">${esc(h.resuelta || '')}</span> ${esc(h.obs)}</li>`).join('');
      return `<section class="sect review" data-rv="${esc(id)}"><h3>${esc(L2('Observaciones', 'Notes'))}</h3>
        <textarea id="rvObs" rows="3" aria-label="${esc(L2('Observaciones', 'Notes'))}" placeholder="${esc(L2('Observaciones sobre esta ficha (si dejas el texto vacío, la ficha sale de la lista de pendientes)', 'Notes about this card (empty text takes the card out of the pending list)'))}">${esc(r.obs || '')}</textarea>
        <div class="rv-acts"><button class="ed-b pri" data-rvsave="${esc(id)}">${esc(L2('Guardar', 'Save'))}</button>${r.obs ? `<button class="ed-b" data-rvresolve="${esc(id)}">${esc(L2('Resolver', 'Resolve'))}</button>` : ''}${r.fecha ? `<span class="rv-date">${esc(L2('Último cambio', 'Last change'))}: ${esc(r.fecha)}</span>` : ''}</div>
        ${E.msg ? `<p class="rv-err">${esc(E.msg)}</p>` : ''}
        ${hist ? `<details class="rv-hist"><summary>${esc(L2('Observaciones resueltas', 'Resolved notes'))} (${(r.historial || []).length})</summary><ul>${hist}</ul></details>` : ''}</section>`;
    };
    const allIds = () => [...idx.byId.keys()];
    E.summaryCard = () => {
      const ids = allIds(), f = E.filt;
      const eras = G.eras.filter((e) => e.ready);
      const eraIx = new Map(G.eras.map((e, i) => [e.id, i]));
      const byName = (a, b) => (eraIx.get(idx.byId.get(a).era) - eraIx.get(idx.byId.get(b).era)) || nameOf(idx.byId.get(a)).localeCompare(nameOf(idx.byId.get(b)));
      const has = new Set(ids.filter((id) => srcCount(id) > 0));
      const chip = (k, v, lbl) => `<button class="chip" data-rvf="${k}:${v}" ${pressed(f[k] === v)}>${esc(lbl)}</button>`;
      const pct = (a, b) => (b ? Math.round((100 * a) / b) : 0);
      const bar = (a, b) => `<span class="rv-bar" role="img" aria-label="${pct(a, b)}%"><i style="width:${pct(a, b)}%"></i></span>`;
      const eraOf = (id) => idx.byId.get(id).era;
      const eraOk = (id) => f.era === 'all' || eraOf(id) === f.era;
      // collapsible list: closed when the summary opens; keeps its state while filters change
      const det = (key, title, count, body) => `<details class="sect rv-det" data-rvd="${key}"${E.open[key] ? ' open' : ''}><summary><span class="rv-dt">${esc(title)}</span> <span class="rv-dn">${nfl(count)}</span></summary>${body}</details>`;
      // 1. AI review = cards with at least one recorded source
      const kinds = ['work', 'designer', 'movement', 'institution', 'context', 'production', 'theory', 'concept'];
      const tbl = (groups, has2) => `<table class="rv-tbl"><tbody>${groups.map(([lbl, list]) => { const a = list.filter((id) => has2.has(id)).length; return `<tr><th scope="row">${esc(lbl)}</th><td>${bar(a, list.length)}</td><td class="n">${nfl(a)}/${nfl(list.length)}</td></tr>`; }).join('')}</tbody></table>`;
      const byKind = kinds.map((k) => [t('k_' + k), ids.filter((id) => idx.kind.get(id) === k)]).filter((x) => x[1].length);
      const byEra = eras.map((e) => [eraName(e), ids.filter((id) => eraOf(id) === e.id)]).filter((x) => x[1].length);
      const srcList = ids.filter((id) => (f.src === 'has' ? has.has(id) : !has.has(id)) && eraOk(id)).sort(byName);
      const shown = srcList.slice(0, 150);
      const none = (m) => `<p class="rv-note">${esc(m)}</p>`;
      const more = (n, k) => (n > k ? none(L2(`Se muestran las primeras ${k}; filtra por época para ver el resto.`, `Showing the first ${k}; filter by era to see the rest.`)) : '');
      const srows = shown.map((id) => { const it = idx.byId.get(id); return `<button class="rv-row" data-go="${esc(id)}"><span class="nm">${esc(nameOf(it))}</span><span class="k">${esc(t('k_' + idx.kind.get(id)))} · ${esc(eraName(it.era))}${has.has(id) ? ` · ${srcCount(id)} ${esc(L2('fuentes', 'sources'))}` : ''}</span></button>`; }).join('');
      const eraChips = `<div class="chips">${chip('era', 'all', L2('Todas las épocas', 'All eras'))}${eras.map((e) => chip('era', e.id, eraName(e))).join('')}</div>`;
      // 2. images (own free / own with reserved rights / stand-in / none), for the kinds that carry a photo
      const IMGK = ['work', 'designer', 'movement', 'institution', 'theory'];
      const imgIds = ids.filter((id) => IMGK.includes(idx.kind.get(id)));
      const ik = new Map(imgIds.map((id) => [id, imgClass(idx.byId.get(id), idx.kind.get(id))]));
      const cnt = (c, list) => list.filter((id) => ik.get(id) === c).length;
      const withImg = (list) => list.filter((id) => ik.get(id) !== 'none');
      const kindsI = IMGK.map((k) => [t('k_' + k), imgIds.filter((id) => idx.kind.get(id) === k)]);
      const eraI = eras.map((e) => [eraName(e), imgIds.filter((id) => eraOf(id) === e.id)]).filter((x) => x[1].length);
      const wset = new Set(withImg(imgIds));
      const handIds = Object.keys(E.imgs).filter((id) => idx.byId.has(id)).sort(byName);
      const dom = (u) => (String(u).match(/^https:\/\/(?:www\.)?([^/]+)/) || [])[1] || '';
      const imgList = imgIds.filter((id) => (f.img === 'all' ? true : ik.get(id) === f.img) && eraOk(id)).sort(byName);
      const originOf = (it, c) => (c === 'none' ? '' : c === 'proxy' ? L2('sucedánea', 'stand-in') : c === 'res' ? L2('derechos reservados', 'rights reserved') : L2('libre', 'free'));
      const imgRows = imgList.slice(0, 150).map((id) => { const it = idx.byId.get(id), c = ik.get(id), sl = c === 'none' ? [] : slidesOf(it, idx.kind.get(id)), th = sl[0] ? `<img class="rv-th" src="${esc(sl[0].src.replace('width=720', 'width=80'))}" alt="" loading="lazy" referrerpolicy="no-referrer">` : '<span class="rv-th"></span>'; return `<button class="rv-row img" data-go="${esc(id)}">${th}<span class="nm">${esc(nameOf(it))}</span><span class="k">${esc(t('k_' + idx.kind.get(id)))} · ${esc(eraName(it.era))}${c === 'none' ? '' : ' · ' + esc(originOf(it, c))}</span></button>`; }).join('');
      const hrows = handIds.map((id) => { const it = idx.byId.get(id), u = E.imgs[id]; return `<button class="rv-row img" data-go="${esc(id)}"><img class="rv-th" src="${esc(u)}" alt="" loading="lazy" referrerpolicy="no-referrer"><span class="nm">${esc(nameOf(it))}</span><span class="k">${esc(dom(u))}</span><span class="ob">${esc(u)}</span></button>`; }).join('');
      const imgBody = `<div class="rv-total"><b>${nfl(wset.size)}</b> / ${nfl(imgIds.length)} ${esc(L2('con imagen', 'with an image'))} · ${pct(wset.size, imgIds.length)}% ${bar(wset.size, imgIds.length)}</div>` +
        `<dl class="info-list"><dt>${esc(L2('Libre', 'Free'))}</dt><dd>${nfl(cnt('free', imgIds))}</dd><dt>${esc(L2('Derechos reservados', 'Rights reserved'))}</dt><dd>${nfl(cnt('res', imgIds))}</dd><dt>${esc(L2('Sucedánea', 'Stand-in'))}</dt><dd>${nfl(cnt('proxy', imgIds))}</dd><dt>${esc(L2('Sin imagen', 'No image'))}</dt><dd>${nfl(cnt('none', imgIds))}</dd><dt>${esc(L2('Cambiadas a mano', 'Changed by hand'))}</dt><dd>${nfl(handIds.length)}</dd></dl>` +
        `<div class="info-sub">${esc(L2('Por tipo (con imagen)', 'By type (with an image)'))}</div>${tbl(kindsI, wset)}<div class="info-sub">${esc(L2('Por época (con imagen)', 'By era (with an image)'))}</div>${tbl(eraI, wset)}` +
        `<div class="chips">${chip('img', 'none', `${L2('Sin imagen', 'No image')} (${nfl(cnt('none', imgIds))})`)}${chip('img', 'free', L2('Libre', 'Free'))}${chip('img', 'res', L2('Derechos reservados', 'Rights reserved'))}${chip('img', 'proxy', L2('Sucedánea', 'Stand-in'))}</div>${eraChips}` +
        `<h3>${esc(L2('Fichas', 'Cards'))} · ${nfl(imgList.length)}</h3><div class="rv-list">${imgRows || none(L2('Nada con estos filtros.', 'Nothing with these filters.'))}</div>${more(imgList.length, 150)}` +
        `<h3>${esc(L2('Imágenes cambiadas manualmente', 'Images changed by hand'))} · ${nfl(handIds.length)}</h3><div class="rv-list">${hrows || none(L2('Ninguna imagen cambiada.', 'No image changed.'))}</div>`;
      // 3. pending human notes (private: they need the password)
      const obsAll = ids.filter((id) => E.state(id) === 'observed').length;
      const obs = ids.filter((id) => E.state(id) === 'observed' && eraOk(id)).sort(byName);
      const orows = obs.map((id) => { const it = idx.byId.get(id), r = E.rev[id]; return `<button class="rv-row" data-go="${esc(id)}"><span class="nm">${esc(nameOf(it))}</span><span class="k">${esc(t('k_' + idx.kind.get(id)))} · ${esc(eraName(it.era))}${r.fecha ? ' · ' + esc(r.fecha) : ''}</span><span class="ob">${esc(r.obs)}</span></button>`; }).join('');
      const nRes = ids.reduce((a, id) => a + ((E.rev[id] && E.rev[id].historial) || []).length, 0);
      const obsBody = !E.key ? `<p class="rv-note">${esc(L2('Las observaciones son privadas.', 'Notes are private.'))}</p><button class="ed-b pri" data-edlogin="1">${esc(L2('Ingresar contraseña para ver las observaciones', 'Enter the password to see the notes'))}</button>`
        : `${eraChips}<div class="rv-list">${orows || none(L2('No hay observaciones pendientes con este filtro de época.', 'No pending notes for this era filter.'))}</div>${nRes ? none(L2(`${nfl(nRes)} observaciones resueltas.`, `${nfl(nRes)} resolved notes.`)) : ''}`;
      return head(L2('Modo edición', 'Edit mode'), L2('Resumen de revisión', 'Review summary'), esc(`${nfl(ids.length)} ${L2('fichas', 'cards')}`), false,
        `<button class="p-btn" data-rvexport="1" title="${esc(L2('Exportar observaciones', 'Export notes'))}" aria-label="${esc(L2('Exportar observaciones', 'Export notes'))}"><svg width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><path d="M7 2v7M4 6.5L7 9.5l3-3M2.5 11.5h9" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg></button>`) +
        `<section class="sect"><h3>${esc(L2('Revisión por IA', 'AI review'))}</h3><p class="rv-note">${esc(L2('Una ficha cuenta como revisada cuando tiene al menos una fuente registrada.', 'A card counts as reviewed when it has at least one recorded source.'))}</p>` +
        `<div class="rv-total"><b>${nfl(has.size)}</b> / ${nfl(ids.length)} ${esc(L2('con fuentes', 'with sources'))} · ${pct(has.size, ids.length)}% ${bar(has.size, ids.length)}</div>` +
        `<div class="info-sub">${esc(L2('Por tipo', 'By type'))}</div>${tbl(byKind, has)}<div class="info-sub">${esc(L2('Por época', 'By era'))}</div>${tbl(byEra, has)}</section>` +
        det('src', L2('Fuentes', 'Sources'), srcList.length, `<div class="chips">${chip('src', 'none', `${L2('Sin fuentes', 'No sources')} (${nfl(ids.length - has.size)})`)}${chip('src', 'has', `${L2('Con fuentes', 'With sources')} (${nfl(has.size)})`)}</div>${eraChips}<div class="rv-list">${srows || none(L2('Nada con estos filtros.', 'Nothing with these filters.'))}</div>${more(srcList.length, 150)}`) +
        det('img', L2('Imágenes', 'Images'), imgList.length, imgBody) +
        det('obs', L2('Observaciones', 'Notes'), E.key ? obsAll : 0, obsBody) +
        `<section class="sect"><button class="ed-b" data-rvexport="1">${esc(L2('Exportar observaciones (.md)', 'Export notes (.md)'))}</button><p class="rv-note">${esc(L2('Descarga un archivo con las observaciones abiertas y resueltas por época, la lista de imágenes cambiadas y la cuenta de fichas sin fuentes.', 'Downloads a file with open and resolved notes by era, the list of changed images and the count of cards without sources.'))}</p></section>`;
    };
    function exportNotes() {
      const day = new Date().toISOString().slice(0, 10);
      const lines = [`# ${L2('Observaciones de revisión', 'Review notes')} · LHD`, '', `${L2('Fecha', 'Date')}: ${day}`, ''];
      const ids = allIds();
      const nObs = ids.filter((id) => E.state(id) === 'observed').length, nSrc = ids.filter((id) => srcCount(id) === 0).length;
      const imgs = Object.keys(E.imgs).filter((id) => idx.byId.has(id));
      lines.push(`${L2('Observaciones abiertas', 'Open notes')}: ${nObs} · ${L2('Fichas sin fuentes', 'Cards without sources')}: ${nSrc} / ${ids.length} · ${L2('Imágenes cambiadas', 'Changed images')}: ${imgs.length}`, '');
      G.eras.forEach((e) => {
        const mine = ids.filter((id) => idx.byId.get(id).era === e.id && E.rev[id] && (E.rev[id].obs || (E.rev[id].historial || []).length));
        if (!mine.length) return;
        lines.push(`## ${eraName(e)}`, '');
        mine.forEach((id) => {
          const it = idx.byId.get(id), r = E.rev[id];
          lines.push(`### ${nameOf(it)} (${t('k_' + idx.kind.get(id))} · \`${id}\`)`);
          if (r.obs) lines.push('', `- **${L2('Abierta', 'Open')}** (${r.fecha || ''}): ${r.obs}`);
          (r.historial || []).forEach((h) => lines.push(`- ${L2('Resuelta', 'Resolved')} ${h.resuelta || ''}: ${h.obs}`));
          lines.push('');
        });
      });
      if (imgs.length) {
        lines.push(`## ${L2('Imágenes cambiadas manualmente', 'Images changed by hand')}`, '');
        imgs.sort().forEach((id) => lines.push(`- ${nameOf(idx.byId.get(id))} (\`${id}\`): ${E.imgs[id]}`));
        lines.push('');
      }
      const blob = new Blob([lines.join('\n')], { type: 'text/markdown;charset=utf-8' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob); a.download = `observaciones-lhd-${day}.md`;
      document.body.appendChild(a); a.click(); setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 500);
    }
    async function act(fn) {
      try { await fn(); E.msg = ''; } catch (err) { E.msg = err.message; }
      render();
    }
    E.panelClick = (ev) => {
      const b = ev.target.closest('button'); if (!b) return false;
      const ds = b.dataset;
      if (ds.edlogin) {
        if ($('edModal')) { submitKey(); return true; }
        askKey(() => { renderPanel(); }); return true;
      }
      if (ds.edmodalcancel) { closeModal(); return true; }
      if (ds.edimg) { E.need(() => { E.imgForm = E.imgForm === ds.edimg ? null : ds.edimg; E.msg = ''; renderPanel(); const i = $('edImgUrl'); if (i) i.focus(); }); return true; }
      if (ds.edimgcancel) { E.imgForm = null; E.msg = ''; renderPanel(); return true; }
      if (ds.edimgsave || ds.edimgclear) {
        const id = ds.edimgsave || ds.edimgclear, url = ds.edimgsave ? (($('edImgUrl') || {}).value || '').trim() : '';
        E.need(() => act(async () => { const j = await post({ accion: 'imagen', id, url }); E.imgs = j.imagenes || {}; E.imgForm = null; }));
        return true;
      }
      if (ds.rvsave) {
        const id = ds.rvsave, obs = (($('rvObs') || {}).value || '').trim();
        E.need(() => act(async () => { const j = await post({ accion: 'revision', id, obs }); if (j.registro) E.rev[id] = j.registro; else delete E.rev[id]; }));
        return true;
      }
      if (ds.rvresolve) {
        const id = ds.rvresolve;
        E.need(() => act(async () => { const j = await post({ accion: 'resolver', id }); if (j.registro) E.rev[id] = j.registro; else delete E.rev[id]; }));
        return true;
      }
      if (ds.rvf) { const [k, v] = ds.rvf.split(':'); E.filt[k] = v; renderPanel(); return true; }
      if (ds.rvexport) { E.need(exportNotes); return true; }
      return false;
    };
    document.addEventListener('click', (ev) => {
      const m = ev.target.closest && ev.target.closest('#edModal'); if (!m) return;
      const b = ev.target.closest('button');
      if (b && b.dataset.edlogin) submitKey(); else if (b && b.dataset.edmodalcancel) closeModal(); else if (ev.target === m) closeModal();
    });
    // the notes box is private: reading or typing in it asks for the password first
    document.addEventListener('focusin', (ev) => { if (on && !E.key && ev.target.id === 'rvObs') { ev.target.blur(); askKey(() => { renderPanel(); const o = $('rvObs'); if (o) o.focus(); }); } });
    // collapsible lists of the summary remember their state while filters re-render the card
    document.addEventListener('toggle', (ev) => { const d = ev.target; if (d && d.dataset && d.dataset.rvd) E.open[d.dataset.rvd] = d.open; }, true);
    document.addEventListener('keydown', (ev) => { if (ev.key === 'Escape' && $('edModal')) { ev.stopPropagation(); closeModal(); } }, true);
    // Enter in the password or URL field
    document.addEventListener('keydown', (ev) => {
      if (ev.key !== 'Enter') return;
      if (ev.target.id === 'edPass' && ev.target.value) { ev.preventDefault(); submitKey(); }
      if (ev.target.id === 'edImgUrl') { ev.preventDefault(); const b = document.querySelector('[data-edimgsave]'); if (b) b.click(); }
    });
    return E;
  }
  ED = makeEditor();

  // ---------- Search ----------
  const search = { items: [], active: -1, list: [] };
  function runSearch(q) {
    const box = $('results'), inp = $('q');
    q = norm(q.trim());
    if (!q) { box.hidden = true; inp.setAttribute('aria-expanded', 'false'); search.list = []; return; }
    const words = q.split(/\s+/);
    const hits = [];
    for (const g of G.map.values()) {
      const hay = norm(g.name + ' ' + g.nameEs + ' ' + (g.by || ''));
      if (!words.every((w) => hay.includes(w))) continue;
      const nm = norm(S.lang === 'es' ? g.nameEs : g.name);
      const score = (nm.startsWith(q) ? 0 : nm.includes(q) ? 1 : 2) * 10 + (g.star ? -1 : 0) + (g.era === S.eraId ? -0.5 : 0);
      hits.push([score, g]);
    }
    hits.sort((a, b) => a[0] - b[0] || String(a[1].name).localeCompare(b[1].name));
    search.list = hits.slice(0, 14).map((h) => h[1]); search.active = -1;
    const kindName = (k) => t('k_' + k);
    box.innerHTML = search.list.length
      ? search.list.map((g, i) => `<button role="option" data-i="${i}" aria-selected="false"><span class="kind">${esc(kindName(g.kind))}</span><span>${g.star ? '<span class="st">★ </span>' : ''}${esc(S.lang === 'es' ? g.nameEs : g.name)}</span><span class="sub">${esc([g.by, g.year].filter(Boolean).join(' · '))}</span></button>`).join('')
      : `<div class="none">${esc(t('noMatch'))}</div>`;
    box.hidden = false; inp.setAttribute('aria-expanded', 'true');
  }
  function pickResult(i) {
    const g = search.list[i];
    if (!g) return;
    $('results').hidden = true; $('q').setAttribute('aria-expanded', 'false'); $('q').value = '';
    go(g.id);
  }
  function markActive() {
    [...$('results').querySelectorAll('button')].forEach((b, i) => { b.setAttribute('aria-selected', String(i === search.active)); if (i === search.active) b.scrollIntoView({ block: 'nearest' }); });
  }

  // ---------- Tooltip ----------
  function showTip(el, ev) {
    const id = el.dataset.id;
    const it = idx.byId.get(id);
    if (!it) return;
    const k = idx.kind.get(id);
    tipAt(`<span class="k">${esc(t('k_' + k))} · ${esc(dateOf(it))}</span><br>${esc(nameOf(it))}`, ev);
  }
  function tipAt(html, ev) {
    const tip = $('tip');
    tip.innerHTML = rfPlain(html);
    tip.hidden = false;
    const w = tip.offsetWidth, h = tip.offsetHeight;
    tip.style.left = Math.min(window.innerWidth - w - 8, ev.clientX + 14) + 'px';
    tip.style.top = Math.min(window.innerHeight - h - 8, ev.clientY + 16) + 'px';
  }
  function curveTip(i, ev) {
    const c = (S.curves || [])[+i]; if (!c) return;
    const o = idx.byId.get(c.r.other);
    const kind = t('cn_' + c.r.type);
    const via = c.r.via && idx.byId.get(c.r.via);
    tipAt(`<span class="k">${esc(kind)}${via ? ' · ' + esc(t('viaWork')) + ': ' + esc(nameOf(via)) : ''}</span><br><b>${esc(o ? nameOf(o) : '')}</b>${c.r.note ? '<br>' + esc(c.r.note) : ''}`, ev);
  }

  // ---------- Zoom ----------
  function zoomTo(px, cx) {
    const vp = $('viewport');
    const old = S.px;
    px = Math.max(L.fit, Math.min(L.max, px));
    if (Math.abs(px - old) < 1e-6) return;
    const u = (vp.scrollLeft + cx - L.x0) / old;   // scale units do not change with the zoom
    S.px = px; S.zoomed = px > L.fit + 1e-6;
    render();
    vp.scrollLeft = L.x0 + u * px - cx;
    syncScroll();
  }
  // switch between the linear and the uneven scale, keeping the year in the middle of the view
  function setScale(mode) {
    if (mode === S.scale) return;
    const vp = $('viewport'), cx = vp.clientWidth / 2;
    const y = yearAtX(vp.scrollLeft + cx), local = lp(y);
    S.scale = mode; store.set('lhd-scale', mode);
    buildScale();
    S.px = S.zoomed ? local / decAt(y).w : 0;
    render();
    vp.scrollLeft = xOf(y) - cx; syncScroll();
  }

  // ---------- Language ----------
  function applyLang() {
    document.documentElement.lang = S.lang;
    document.title = t('title');
    document.querySelectorAll('[data-i18n]').forEach((el) => { el.textContent = t(el.dataset.i18n); });
    $('q').placeholder = t('search');
    $('infoBtn').setAttribute('aria-label', t('infoKicker')); $('infoBtn').title = t('infoKicker');
    syncHelpBtn(); if (S.help) $('helpBody').innerHTML = helpHTML();
    $('yFrom').title = t('rangeFromTip'); $('yTo').title = t('rangeToTip'); $('yFrom').setAttribute('aria-label', t('rangeFromTip')); $('yTo').setAttribute('aria-label', t('rangeToTip'));
    $('edgeL').title = t('edgeL'); $('edgeR').title = t('edgeR'); $('axis').title = t('axisTip');
    $('zoomFit').setAttribute('aria-label', t('zoomFit')); $('zoomFit').title = t('zoomFit');
    $('zoomVis').setAttribute('aria-label', t('zoomVis')); $('zoomVis').title = t('zoomVis');
    document.querySelector('.timeline').setAttribute('aria-label', t('title'));
    $('viewport').setAttribute('aria-label', t('title'));
    if ($('reviewBtn')) { $('reviewBtn').title = t('rv_btn'); $('reviewBtn').setAttribute('aria-label', t('rv_btn')); }
  }

  // ---------- Wiring ----------
  function wire() {
    const vp = $('viewport');
    vp.addEventListener('scroll', syncScroll);
    $('filters').addEventListener('click', (ev) => {
      const b = ev.target.closest('button'); if (!b) return;
      const ds = b.dataset;
      if (ds.focus) return setFocus(ds.focus);
      if (ds.disc) return setScope(ds.disc);
      else if (ds.arrange) { S.arrange = ds.arrange; store.set('lhd-arrange', S.arrange); }
      else if (ds.type && b.getAttribute('aria-disabled') === 'true') return;
      else if (ds.type) { S.types.has(ds.type) ? S.types.delete(ds.type) : S.types.add(ds.type); if (!S.types.size) S.types = new Set(TYPES); }
      else if (ds.level) { S.level = ds.level; store.set('lhd-level', S.level); }
      else if (ds.connall) { S.connAll = !S.connAll; if (!S.focus) store.set('lhd-conn2', S.connAll ? '1' : '0'); }
      else if (ds.scale) return setScale(ds.scale);
      else if (ds.isoclear) { setIso(null); return; }
      else return;
      render();
    });
    const toggleKey = (k) => {
      const tr = keyTrack(k);
      if (S.focus && tr && k.startsWith('trk:') && tr !== S.focus) { applyFocus(null); S.collapsed.delete(k); render(); return; }   // another row: leave the lens and open it
      S.collapsed.has(k) ? S.collapsed.delete(k) : S.collapsed.add(k); render();
    };
    $('labelsInner').addEventListener('click', (ev) => {
      const f = ev.target.closest('[data-focus]'); if (f) return setFocus(f.dataset.focus);
      const b = ev.target.closest('[data-k]'); if (b) toggleKey(b.dataset.k);
    });
    $('content').addEventListener('click', (ev) => {
      if (S.dragged) { S.dragged = false; return; }
      if (ev.detail > 1) return;   // the second click of a double click is handled by dblclick
      if (ev.target.closest('.hit')) return;
      const n = ev.target.closest('[data-k]'); if (n) return toggleKey(n.dataset.k);
      const er = ev.target.closest('[data-era]'); if (er) return showEra(er.dataset.era);
      const el = ev.target.closest('[data-id]');
      if (el) return select(el.dataset.id === S.sel ? null : el.dataset.id);
      if (S.sel || S.info || S.review) { S.info = false; S.review = false; select(null); }
    });
    // double click: select and show only its connections (again: remove the filter); on the era bar, zoom to the era
    $('content').addEventListener('dblclick', (ev) => {
      const er = ev.target.closest('[data-era]'); if (er) return setEraView(er.dataset.era);
      const el = ev.target.closest('[data-id]'); if (!el) return;
      const id = el.dataset.id;
      if (S.iso && S.iso.id === id) { setIso(null); return; }
      if (S.sel !== id) select(id);
      setIso(id);
    });
    // double arrows of CONTEXT and DESIGN: open or close all their rows (with a lens, CONTEXT only acts on the lens row)
    $('labelsInner').addEventListener('click', (ev) => {
      const b = ev.target.closest('[data-secall]'); if (!b) return;
      ev.stopPropagation();
      const [sec, act] = b.dataset.secall.split(':');
      if (sec === 'des') {
        const pre = new RegExp('^[gbz]:' + S.arrange + ':');
        if (act === 'open') [...S.collapsed].forEach((k) => { if (pre.test(k)) S.collapsed.delete(k); });
        else (S.designKeys || []).forEach((k) => S.collapsed.add(k));
        return render();
      }
      let keys = ctxKeys();
      if (sec === 'ctx' && S.focus) keys = keys.filter((k) => keyTrack(k) === S.focus);
      keys.forEach((k) => (act === 'open' ? S.collapsed.delete(k) : S.collapsed.add(k)));
      render();
    }, true);
    wireRange();
    $('zoomFit').addEventListener('click', () => { S.px = 0; S.zoomed = false; render(); vp.scrollLeft = 0; syncScroll(); });
    $('zoomVis').addEventListener('click', fitVisible);
    $('panel').addEventListener('toggle', (ev) => { if (ev.target.matches && ev.target.matches('details.sources')) S.srcOpen = ev.target.open ? S.sel : null; }, true);
    $('panel').addEventListener('scroll', (ev) => { if (ev.target.classList && ev.target.classList.contains('gal-track')) galSync(ev.target); }, true);
    $('panel').addEventListener('keydown', (ev) => {
      const g = ev.target.closest && ev.target.closest('.gal');
      if (g && (ev.key === 'ArrowRight' || ev.key === 'ArrowLeft')) { const tr = g.querySelector('.gal-track'); ev.preventDefault(); galGo(g, Math.round(tr.scrollLeft / tr.clientWidth) + (ev.key === 'ArrowRight' ? 1 : -1)); }
    });
    $('panel').addEventListener('click', (ev) => {
      const gd = ev.target.closest('.gal-dot');
      if (gd) { galGo(gd.closest('.gal'), +gd.dataset.gi); return; }
      const rf = ev.target.closest('[data-rf]');
      if (rf) {   // v21: superscript → its source in the review section
        ev.preventDefault();
        const li = $('panel').querySelector('#rf-' + rf.dataset.rf);
        const sd = $('panel').querySelector('details.sources');
        if (sd && !sd.open) { sd.open = true; S.srcOpen = S.sel; }
        if (li) { li.scrollIntoView({ block: 'center', behavior: 'smooth' }); li.classList.remove('rf-hi'); void li.offsetWidth; li.classList.add('rf-hi'); }
        return;
      }
      if (ED.on && ED.panelClick(ev)) return;
      if (ev.target.closest('[data-unrev]')) {
        const sd = $('panel').querySelector('details.sources');
        if (sd) { sd.open = true; S.srcOpen = S.sel; sd.scrollIntoView({ block: 'center', behavior: 'smooth' }); }
        return;
      }
      if (ev.target.closest('#isoBtn')) { setIso(S.iso && S.iso.id === S.sel ? null : S.sel); return; }
      const f = ev.target.closest('[data-focus]'); if (f) return setFocus(f.dataset.focus);
      const z = ev.target.closest('[data-zoomera]'); if (z) return setEraView(z.dataset.zoomera);
      if (ev.target.closest('[data-help]')) { S.info = false; render(); return setHelp(true); }
      const g = ev.target.closest('[data-go]'); if (g) return go(g.dataset.go);
      const c = ev.target.closest('[data-close]'); if (c) {
        if (S.info) { S.info = false; renderFilters(); return render(); }
        if (S.review) { S.review = false; return render(); }
        if (S.sel) return select(null);
        if (S.showEraCard) { S.showEraCard = false; return render(); }
        if (cardKind() === 'scope') return setScope(null);
        if (S.focus) return setFocus(null);
        return;
      }
      const e = ev.target.closest('[data-era]'); if (e) return showEra(e.dataset.era);
    });
    $('langBtn').addEventListener('click', () => { S.lang = S.lang === 'es' ? 'en' : 'es'; store.set('lhd-lang', S.lang); applyLang(); if (S.data) render(); runSearch($('q').value); });
    $('themeBtn').addEventListener('click', () => setTheme(effTheme() === 'dark' ? 'light' : 'dark', true));
    $('infoBtn').addEventListener('click', () => { S.info = !S.info; S.review = false; renderFilters(); renderPanel(); });
    $('helpBtn').addEventListener('click', () => setHelp(!S.help));
    $('helpClose').addEventListener('click', () => setHelp(false));
    $('help').addEventListener('mousedown', (ev) => { if (ev.target === $('help')) setHelp(false); });
    // search
    const q = $('q');
    q.addEventListener('input', () => runSearch(q.value));
    q.addEventListener('focus', () => { if (q.value) runSearch(q.value); });
    q.addEventListener('keydown', (ev) => {
      const n = search.list.length;
      if (ev.key === 'ArrowDown' && n) { ev.preventDefault(); search.active = (search.active + 1) % n; markActive(); }
      else if (ev.key === 'ArrowUp' && n) { ev.preventDefault(); search.active = (search.active - 1 + n) % n; markActive(); }
      else if (ev.key === 'Enter') { pickResult(search.active >= 0 ? search.active : 0); }
      else if (ev.key === 'Escape') { $('results').hidden = true; q.setAttribute('aria-expanded', 'false'); }
    });
    $('results').addEventListener('mousedown', (ev) => { const b = ev.target.closest('button[data-i]'); if (b) { ev.preventDefault(); pickResult(+b.dataset.i); } });
    document.addEventListener('click', (ev) => { if (!ev.target.closest('.search')) { $('results').hidden = true; q.setAttribute('aria-expanded', 'false'); } });
    // tooltip, curve notes and the faint preview of the curves on hover
    const setHover = (id) => { if (id === S.hover) return; S.hover = id; if (S.connAll) drawCurves(); };
    $('content').addEventListener('mousemove', (ev) => {
      const hit = ev.target.closest('.hit');
      if (hit) { curveTip(hit.dataset.ci, ev); return; }
      const el = ev.target.closest('#content [data-id]');
      if (el) { showTip(el, ev); setHover(el.dataset.id); } else { $('tip').hidden = true; setHover(null); }
    });
    $('content').addEventListener('mouseleave', () => { $('tip').hidden = true; setHover(null); });
    // zoom with ctrl/cmd + wheel; drag to pan
    vp.addEventListener('wheel', (ev) => {
      if (!(ev.ctrlKey || ev.metaKey) || !S.data) return;
      ev.preventDefault();
      const r = vp.getBoundingClientRect();
      zoomTo(S.px * Math.exp(-ev.deltaY * 0.0025), ev.clientX - r.left);
    }, { passive: false });
    let drag = null;
    vp.addEventListener('mousedown', (ev) => {
      if (ev.button !== 0 || ev.target.closest('[data-id],[data-k]')) return;
      drag = { x: ev.clientX, y: ev.clientY, sl: vp.scrollLeft, st: vp.scrollTop, moved: false };
    });
    window.addEventListener('mousemove', (ev) => {
      if (!drag) return;
      const dx = ev.clientX - drag.x, dy = ev.clientY - drag.y;
      if (!drag.moved && Math.abs(dx) + Math.abs(dy) < 4) return;
      drag.moved = true; vp.scrollLeft = drag.sl - dx; vp.scrollTop = drag.st - dy;
    });
    window.addEventListener('mouseup', () => { if (drag && drag.moved) { S.dragged = true; setTimeout(() => { S.dragged = false; }, 0); } drag = null; });
    document.addEventListener('keydown', (ev) => {
      if (ev.ctrlKey || ev.metaKey || ev.altKey || /^(INPUT|TEXTAREA|SELECT)$/.test((ev.target || {}).tagName || '') || !S.data) return;
      if (ev.key === '+' || ev.key === '=') zoomTo(S.px * 1.3, vp.clientWidth / 2);
      else if (ev.key === '-' || ev.key === '_') zoomTo(S.px / 1.3, vp.clientWidth / 2);
    });
    document.addEventListener('keydown', (ev) => {
      if (ev.key === 'Escape' && S.help) { setHelp(false); return; }
      if (ev.key === 'Escape' && (S.sel || S.info || S.review) && document.activeElement !== q && !/^(INPUT|TEXTAREA)$/.test((document.activeElement || {}).tagName || '')) { S.info = false; S.review = false; select(null); }
    });
    // resizable panel
    const pr = $('panelResize');
    pr.addEventListener('mousedown', (ev) => {
      ev.preventDefault(); pr.classList.add('on');
      const mv = (e2) => { const w = Math.max(300, Math.min(720, window.innerWidth - e2.clientX)); document.documentElement.style.setProperty('--panel-w', w + 'px'); };
      const up = () => { pr.classList.remove('on'); window.removeEventListener('mousemove', mv); window.removeEventListener('mouseup', up); if (S.data) render(); };
      window.addEventListener('mousemove', mv); window.addEventListener('mouseup', up);
    });
    let rz = 0;
    window.addEventListener('resize', () => { clearTimeout(rz); rz = setTimeout(() => { if (S.data) { if (!S.zoomed) S.px = 0; render(); } }, 120); });
    window.addEventListener('hashchange', () => { const h = decodeURIComponent(location.hash.slice(1)); if (h && h !== S.sel) go(h); });
  }

  // ---------- Start ----------
  async function init() {
    applyLang(); syncTheme(); wire();
    let d = null;
    try { d = await (await fetch('data/all.json')).json(); } catch (err) { $('content').innerHTML = `<div class="loading">Error: ${esc(err.message)}</div>`; return; }
    G.eras = d.eras; G.eraById = new Map(d.eras.map((e) => [e.id, e])); G.stats = d.stats || {};
    d.items.forEach((r) => G.map.set(r[0], { id: r[0], era: r[1], kind: r[2], name: r[3], nameEs: r[4], year: r[5], by: r[6], star: !!r[7] }));
    S.data = d;
    rfPrepare(d); rfMode(false);
    buildIndex(d);
    await ED.init();
    const hash = decodeURIComponent(location.hash.slice(1));
    const target = hash && idx.byId.has(hash) ? hash : null;
    const pref = CFG.defaultEra || 'modernism';
    S.eraId = G.eraById.has(pref) ? pref : G.eras[0].id;
    S.info = !target;
    ctxKeys().forEach((k) => S.collapsed.add(k));   // v24 (point 49): the page opens with all the context collapsed, productive included
    render();
    if (target) go(target);
  }
  window.LHD = { state: S, go, select, relatedIds, relations, setEraView, showEra, setIso, setScale, setFocus, setScope }; // handy for testing
  init();
})();
