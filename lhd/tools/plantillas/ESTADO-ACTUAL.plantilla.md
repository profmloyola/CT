# Estado actual de la LHD

*Se actualiza en cada entrega (plan, sección 5B). Última actualización: <FECHA>, **v<NN>**.*

## Dónde estamos
- **Versión:** v<NN> (`index.html` usa `?v=<NN>`). <qué cambió: código, datos o solo documentos>.
- **Hecho:** <etapa / paso terminado>.
- **Siguiente paso sin marcar:** <etapa y paso de tools/PLAN-CIERRE.md>.

## Decisiones ya tomadas (no volver a preguntarlas)
- <copiar las vigentes de la versión anterior y agregar las nuevas>

## Decisiones pendientes de la persona responsable
- <visto bueno V1 / V2, comentarios por responder, puntos registrados sin «implementa»>

## Cifras actuales (data/all.json)
- <obras (★), diseñadores, hechos de contexto, enlaces; con y sin fuentes; fichas que muestran «no revisada»>
- Build: <resultado de `python3 tools/build_data.py`>.
- Pruebas: <resultado de `sh tools/tests/run_all.sh`>.
- Meta final: 375 obras (113 ★), ~685 enlaces de contexto.

## Reglas vigentes que no hay que olvidar
- Después de cada paso: ZIP único `LHD-vNN.zip` (`sh tools/empaquetar.sh NN`) y actualizar este archivo.
- No implementar comentarios nuevos hasta que se diga «implementa»; registrarlos como puntos numerados (el próximo es el **<N>**).
- Hablar en español de Chile, respuestas breves.
- No usar `pkill -f "php -S"`; `ediciones/` debe quedar limpia antes de entregar.

## Mensaje para pegar en la sesión nueva
> Adjunto el ZIP de la LHD (v<NN>). Descomprímelo, lee `INICIO-SESION-NUEVA.md` y `ESTADO-ACTUAL.md` y ejecuta el siguiente paso sin marcar de `tools/PLAN-CIERRE.md`. Registra mis comentarios en `tools/CAMBIOS-PENDIENTES.md` y no implementes nada nuevo hasta que diga «implementa».
