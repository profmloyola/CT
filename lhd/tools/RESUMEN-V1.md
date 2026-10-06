# Resumen para el visto bueno V1 (etapa 1, v32) — **APROBADO el 4 de octubre de 2026 con el cambio del punto 66 (v33)**

Se pide aprobar **dos cosas**: las listas de `tools/LISTAS-CIERRE.md` y el recorte de `tools/RECORTE-MODERNISMO.md`. Nada se aplicó todavía a `src-data/`.

## Cantidades (verificadas con `listas_check.py`: 0 errores, 0 avisos)

| Tramo | Contextos | Productivo | Teoría | Mov. | Inst. | Diseñadores | Obras (★) | Conexiones |
|---|---|---|---|---|---|---|---|---|
| Industrial | 25 | 10 | 5 | 5 | 6 | 14 | 30 (9) | 17 |
| Reforma | 31 | 12 | 6 | 6 | 9 | 28 | 60 (18) | 18 |
| Modernismo (tras recorte) | 39 | 16 | 14 | 13 | 17 | 64 | 120 (37) | 23 |
| Posguerra | 36 | 16 | 11 | 11 | 15 | 45 | 90 (27) | 16 |
| Posmoderno | 32 | 14 | 9 | 8 | 12 | 35 | 73 (23) | 20 |
| **Total** | | | | | | | **373 (114)** | |

Meta del plan: 375 obras y 113 ★. Todo está dentro de la tolerancia (±2; obras ±3).

**Disciplinas de obras** (gráfica / producto / moda / arquitectura): Industrial 10/9/4/7 · Reforma 14/17/8/21 · Posguerra 24/30/12/24 · Posmoderno 21/22/13/17.
**América Latina** (obras): Industrial 3 (10 %) · Reforma 4 (7 %) · Posguerra 17 (19 %) · Posmoderno 13 (18 %). Cumple C5 (≥ 15 % en Posguerra y Posmoderno; ≥ 2 en Industrial y Reforma). Chile 1970–73: 6 elementos (tope 6).
**Fuera de Occidente** (con influencia demostrable, `global`): Reforma 2 contextos (japonismo, comercio imperial británico) · Posguerra 3 obras (Tokio 64, Sony TR-63, Nakagin) + milagro japonés · Posmoderno 5 (Muji, Kawakubo, Yamamoto, Walkman, debut parisino de 1981) + contextos.
**Modernismo:** se le devuelven `ctx-corfo` y `ctx-early-television`; se mantienen `ctx-taylorism` y Kare/Macintosh/computador personal.

## Las 5 decisiones más discutibles

1. **Obras sin diseñador listado** (≈ 8 en Posguerra, 11 en Posmoderno, 8 en Industrial, p. ej. Swatch, Walkman, Penny Black, murales de la BRP). Se dejaron así para no pasar el tope de diseñadores; al escribir la ficha se les da `maker` o `client`.
2. **Enlaces de contexto débiles** que conviene mirar: `ctx-marshall-plan` en la Unité d’Habitation, `ctx-latam-urbanisation-1950` en Casa Curutchet, `ctx-brazil-developmentalism` en la Bowl Chair, y Zig-Zag solo con un contexto (urbanización) porque no se pudo escribir una línea segura sobre el salitre.
3. **Crystal Palace 1851** queda en la reserva de Industrial (se asume de Reforma) y Lautrec queda Normal para no pasar de 18 ★ en Reforma, aunque SPEC lo nombra.
4. **Duplicados entre tramos resueltos así:** Thonet (empresa y Michael) en Industrial; Sottsass, Glaser y Lina Bo Bardi en Posguerra (sus obras posmodernas los citan); moldeo por inyección en Posguerra; la urbanización latinoamericana tiene un hecho en Reforma (1870–1914) y otro en Posguerra (`…-1950`).
5. **Recorte del Modernismo** (18 obras, 8 diseñadores, 3 contextos): se quitan Normal sin enlaces ni protecciones, p. ej. Villa Mairea, Maison de Verre, Faaborg, Anglepoise, Popover (Stool 60, Maison du Peuple y la camisa Lacoste se mantienen, punto 66), y los contextos Jazz Age, teléfono automático y vida metropolitana. Se mantienen Eileen Gray, Perriand, Wagenfeld, Fuller, Cassandre y McKnight Kauffer (tienen otras obras). Los contextos quedan con las obras restantes (el ensayo no deja huérfanos).

## Lo que no se hizo (a propósito)
- No se aplicó el recorte (paso 1.7) ni se creó contenido de fichas: eso es después de V1.
- Fechas y atribuciones dudosas (Larrea, Cardin 1967, Didot 1784, Bertin, Thonet Boppard 1836, MuBE, Biblioteca Virgilio Barco) se revisan en la Parte II.

**Para avanzar:** responde «V1 aprobado» (o con cambios por punto). Siguiente: paso 1.7 `[C]` y luego etapa 2 (Posguerra).
