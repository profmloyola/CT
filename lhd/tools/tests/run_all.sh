#!/bin/sh
# Runs every browser test of the LHD (Playwright + Chromium). From the lhd folder: sh tools/tests/run_all.sh
# test_editar.py needs PHP (php -S); it is skipped when php is not installed.
cd "$(dirname "$0")/../.." || exit 1
python3 tools/build_data.py | tail -1 || exit 1
for t in test_general test_eje test_v19 test_v20 test_v21 test_v22 test_v24 test_v30 test_v31 test_etapa8 test_etapa86 test_imagenes test_ensayos_fuentes; do echo "== $t"; python3 tools/tests/$t.py 2>&1 | grep -E "PASS|FAIL|error|Error|->" ; done
for t in test_etapa0 test_recorte test_etapa1 test_preview test_empaquetar test_r1 test_r2_tools test_r2_incidencias test_r2_auditoria; do echo "== $t"; python3 tools/tests/$t.py 2>&1 | grep -E "FAIL|RESULT|Error"; done
if command -v php >/dev/null 2>&1; then echo "== test_editar"; python3 tools/tests/test_editar.py 2>&1 | grep -E "PASS|FAIL|RESULT|Error"; fi
