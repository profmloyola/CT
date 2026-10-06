#!/bin/sh
# ZIP único de continuidad (plan, sección 5B). Uso, desde cualquier carpeta:  sh tools/empaquetar.sh NN   (NN = versión de index.html, por ejemplo 31)
# Variables: OUT = carpeta donde dejar LHD-vNN.zip (por omisión, la carpeta que contiene `lhd`; en la sesión de Claude: /mnt/user-data/outputs)
# Pasos: (1) verifica ediciones/ limpia y la clave; (2) build sin PROBLEM, ESTADO-ACTUAL.md con la versión e index.html con ?v=NN;
#        (3) arma el ZIP; (4) lo prueba en una carpeta limpia (build + servidor + HTTP 200 + JSON válido). La entrega al usuario
#        (SendUserFile y carpeta conectada) la hace Claude después. Nunca usa pkill: el servidor se cierra por su PID.
set -u
NN="${1:-}"
case "$NN" in ''|*[!0-9]*) echo "Uso: sh tools/empaquetar.sh NN (número de versión, p. ej. 31)"; exit 2;; esac
HERE="$(cd "$(dirname "$0")/.." && pwd)"          # carpeta lhd
PARENT="$(dirname "$HERE")"
NAME="$(basename "$HERE")"
OUT="${OUT:-$PARENT}"
ZIP="$OUT/LHD-v$NN.zip"
fail() { echo "ERROR: $1"; exit 1; }
cd "$HERE" || exit 1

# 1. ediciones/ limpia y clave acordada
[ "$(tr -d ' \n\r\t' < ediciones/imagenes.json)" = "{}" ] || fail "ediciones/imagenes.json no está vacío ({})"
[ ! -e ediciones/revision.json ] || fail "hay ediciones/revision.json (observaciones privadas): borrarlo antes de empaquetar"
ls ediciones/copias/*.json >/dev/null 2>&1 && fail "hay copias en ediciones/copias/*.json"
grep -q "const CLAVE = 'uai2026';" editar.php || fail "editar.php no tiene la clave acordada (uai2026)"
[ ! -e ediciones/.lock ] || fail "hay ediciones/.lock"

# 2. build, estado y versión
BUILD="$(python3 tools/build_data.py 2>&1)"; echo "$BUILD" | tail -1
echo "$BUILD" | grep -q "^OK: no PROBLEM" || { echo "$BUILD" | grep PROBLEM | head; fail "el build tiene PROBLEM"; }
grep -q "v$NN" ESTADO-ACTUAL.md || fail "ESTADO-ACTUAL.md no menciona v$NN (actualizarlo antes de empaquetar)"
grep -q "app.js?v=$NN" index.html && grep -q "style.css?v=$NN" index.html || fail "index.html no usa ?v=$NN"
find . -name __pycache__ -type d -prune -exec rm -rf {} + 2>/dev/null

# 3. el ZIP (carpeta lhd completa, sin caches, capturas ni copias de ediciones)
mkdir -p "$OUT"; rm -f "$ZIP"
( cd "$PARENT" && zip -qr "$ZIP" "$NAME" -x "*/__pycache__/*" "*.pyc" "$NAME/ediciones/copias/*.json" ) || fail "no se pudo crear el ZIP"
unzip -tq "$ZIP" >/dev/null || fail "el ZIP está dañado"

# 4. prueba del ZIP en una carpeta limpia
T="$(mktemp -d)"; unzip -q "$ZIP" -d "$T" || fail "no se pudo descomprimir"
( cd "$T/$NAME" && python3 tools/build_data.py 2>&1 | tail -1 | grep -q "^OK: no PROBLEM" ) || { rm -rf "$T"; fail "el build del ZIP descomprimido falla"; }
PORT="$(python3 -c "import socket;s=socket.socket();s.bind(('127.0.0.1',0));print(s.getsockname()[1]);s.close()")"
( cd "$T/$NAME" && exec python3 -m http.server "$PORT" --bind 127.0.0.1 >/dev/null 2>&1 ) &
PID=$!; sleep 1
BAD=0
for f in index.html app.js style.css data/all.json; do
  C="$(python3 - "$PORT" "$f" <<'PY'
import sys, urllib.request
try: print(urllib.request.urlopen(f"http://127.0.0.1:{sys.argv[1]}/{sys.argv[2]}", timeout=5).status)
except Exception as e: print(getattr(e, 'code', 'ERR'))
PY
)"
  [ "$C" = "200" ] || { echo "  $f -> $C"; BAD=1; }
done
python3 -c "import json,sys;json.load(open('$T/$NAME/data/all.json'))" 2>/dev/null || { echo "  all.json no es JSON válido"; BAD=1; }
kill "$PID" 2>/dev/null; wait "$PID" 2>/dev/null
rm -rf "$T"
[ "$BAD" = "0" ] || fail "la prueba del ZIP falló"
echo "ZIP listo y probado: $ZIP ($(du -h "$ZIP" | cut -f1))"
