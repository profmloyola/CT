<?php
/*
 * LHD — modo ?editar (servidor).
 *
 * Guarda dos cosas, siempre por POST con la contraseña:
 *   - ediciones/imagenes.json : URL de imagen que reemplaza la imagen automática de Wikipedia (pública: el sitio la lee).
 *   - ediciones/revision.json : observaciones de cada ficha (texto, fecha e historial). No es pública
 *                               (ediciones/.htaccess la bloquea); solo se lee con la contraseña a través de este archivo.
 * Antes de cada escritura se guarda una copia en ediciones/copias/ (se conservan las 30 más recientes de cada archivo).
 *
 * La contraseña está escrita aquí (decisión de la persona responsable, sitio personal).
 * La clave es insegura a propósito (decisión del punto 60: sitio personal); no se publica en un repositorio.
 */
const CLAVE = 'uai2026';

const DIR = __DIR__ . '/ediciones';
const F_IMG = DIR . '/imagenes.json';
const F_REV = DIR . '/revision.json';
const COPIAS = DIR . '/copias';
const MAX_COPIAS = 30;

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
header('X-Content-Type-Options: nosniff');

function salir($code, $data) {
    http_response_code($code);
    echo json_encode($data, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    exit;
}
function leer_json($f) {
    if (!is_file($f)) return [];
    $d = json_decode((string) file_get_contents($f), true);
    return is_array($d) ? $d : [];
}
function escribir_json($f, $data) {
    if (!is_dir(COPIAS)) @mkdir(COPIAS, 0775, true);
    if (is_file($f)) {
        $base = basename($f, '.json');
        @copy($f, COPIAS . '/' . $base . '-' . date('Ymd-His') . '-' . substr(md5(uniqid('', true)), 0, 6) . '.json');
        $old = glob(COPIAS . '/' . $base . '-*.json') ?: [];
        sort($old);
        while (count($old) > MAX_COPIAS) @unlink(array_shift($old));
    }
    $tmp = $f . '.tmp';
    $json = json_encode($data === [] ? new stdClass() : $data, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT);
    if (file_put_contents($tmp, $json . "\n") === false || !rename($tmp, $f)) salir(500, ['ok' => false, 'error' => 'No se pudo escribir ' . basename($f) . ' (revisa los permisos de la carpeta ediciones/).']);
}
function texto($v, $max) {
    $v = is_string($v) ? trim($v) : '';
    $v = preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/u', '', $v);
    return mb_substr($v, 0, $max);
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') salir(405, ['ok' => false, 'error' => 'Usa POST.']);
$raw = file_get_contents('php://input', false, null, 0, 20000);
$in = json_decode((string) $raw, true);
if (!is_array($in)) salir(400, ['ok' => false, 'error' => 'JSON no válido.']);
if (!is_string($in['clave'] ?? null) || !hash_equals(CLAVE, $in['clave'])) {
    usleep(800000); // frena los intentos a ciegas
    salir(403, ['ok' => false, 'error' => 'Contraseña incorrecta.']);
}
$accion = $in['accion'] ?? '';
if ($accion === 'leer' || $accion === 'login') {
    salir(200, ['ok' => true, 'imagenes' => (object) leer_json(F_IMG), 'revision' => (object) leer_json(F_REV)]);
}
$id = $in['id'] ?? '';
if (!is_string($id) || strlen($id) > 80 || !preg_match('/^[a-z0-9]+(-[a-z0-9]+)*$/', $id)) salir(400, ['ok' => false, 'error' => 'Identificador no válido.']);

if (!is_dir(DIR)) @mkdir(DIR, 0775, true);
$lock = fopen(DIR . '/.lock', 'c');
if (!$lock || !flock($lock, LOCK_EX)) salir(500, ['ok' => false, 'error' => 'No se pudo bloquear la carpeta ediciones/.']);

if ($accion === 'imagen') {
    $url = texto($in['url'] ?? '', 600);
    $img = leer_json(F_IMG);
    if ($url === '') unset($img[$id]);
    else {
        if (!preg_match('#^https://[^\s"<>]+$#', $url)) salir(400, ['ok' => false, 'error' => 'La URL debe empezar con https:// y no tener espacios.']);
        $img[$id] = $url;
    }
    ksort($img);
    escribir_json(F_IMG, $img);
    salir(200, ['ok' => true, 'imagenes' => (object) $img]);
}

if ($accion === 'revision' || $accion === 'resolver') {
    $rev = leer_json(F_REV);
    $r = $rev[$id] ?? ['obs' => '', 'historial' => []];
    if (!is_array($r['historial'] ?? null)) $r['historial'] = [];
    $hoy = date('Y-m-d H:i');
    if ($accion === 'revision') {
        $r['obs'] = texto($in['obs'] ?? '', 3000);
    } else {
        if (($r['obs'] ?? '') !== '') array_unshift($r['historial'], ['obs' => $r['obs'], 'resuelta' => $hoy]);
        $r['historial'] = array_slice($r['historial'], 0, 10);
        $r['obs'] = '';
    }
    unset($r['revisada']);   // v30: ya no existe la casilla «Revisada»; los registros viejos se limpian aquí
    $r['fecha'] = $hoy;
    if ($r['obs'] === '' && !$r['historial']) unset($rev[$id]);
    else $rev[$id] = $r;
    ksort($rev);
    escribir_json(F_REV, $rev);
    salir(200, ['ok' => true, 'id' => $id, 'registro' => $rev[$id] ?? null]);
}

salir(400, ['ok' => false, 'error' => 'Acción desconocida.']);
