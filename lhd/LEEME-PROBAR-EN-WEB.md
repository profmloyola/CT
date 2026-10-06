# Cómo probar la LHD en la web (antes de publicar)

## En tu computador
1. Descomprime el ZIP. La carpeta `lhd/` es el sitio completo.
2. Desde esa carpeta: `python3 -m http.server 8000` y abre http://localhost:8000.
3. Para probar también el modo edición (`?editar`) hace falta PHP: `php -S 127.0.0.1:8000` y abre http://127.0.0.1:8000/?editar.

## En un hosting
1. Sube el contenido de `lhd/` (o, para publicar, el paquete `LHD-publicar.zip` de la etapa R5, que lleva solo lo necesario).
2. **Sitio público:** funciona en cualquier hosting de archivos estáticos (`index.html`, `app.js`, `style.css`, `data/all.json`, `help/`).
3. **Modo `?editar`:** necesita PHP. La carpeta `ediciones/` debe poder escribirse por el servidor, y su `.htaccess` debe respetarse (protege `revision.json` y las copias).
4. Contraseña de `?editar`: constante `CLAVE` de `editar.php`. Vale `uai2026` (desde v60).
5. Antes de subir, deja `ediciones/imagenes.json` con `{}` y sin `revision.json` ni `copias/*.json`.

## Para armar el ZIP de continuidad
`sh tools/empaquetar.sh NN` (NN = versión de `index.html`) verifica `ediciones/` limpia y la clave, corre el build, arma `LHD-vNN.zip` y lo prueba en una carpeta limpia. `OUT=/ruta sh tools/empaquetar.sh NN` elige dónde dejarlo.

## Vista previa de toda la línea (etapa 1b)
`python3 tools/pipeline/preview_listas.py --out /ruta/LHD-vista-previa --zip /ruta/LHD-vista-previa-1b.zip` arma un sitio aparte con todos los elementos de las listas y fichas «en desarrollo» (ver `INFORME-VISTA-PREVIA.md` dentro). No toca el proyecto real.

## Si algo falla
- Pantalla en blanco: abre la consola del navegador; lo más común es `data/all.json` mal subido o un caché viejo (cambia `?v=NN` en `index.html`).
- El resto del proyecto (datos fuente, scripts, pruebas, plan) está en `src-data/` y `tools/`; ver `INICIO-SESION-NUEVA.md`.
