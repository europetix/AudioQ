#!/bin/bash
# Musée de l'Orangerie — Generador de audio en español (castellano)
# Voz: es-ES-AlvaroNeural a -8%

set -e
cd "$(dirname "$0")"

VOICE="es-ES-AlvaroNeural"
RATE="-8%"
OUT_DIR="$HOME/Desktop/Orangerie_Audio_ES"

echo "=================================================="
echo "  Musée de l'Orangerie — Audio en español"
echo "  Voz: Álvaro (es-ES)"
echo "  Velocidad: $RATE"
echo "  Carpeta de salida: $OUT_DIR"
echo "=================================================="

PYBIN="$(command -v python3 || true)"
if [ -z "$PYBIN" ]; then
    echo ""
    echo "ERROR: no se encuentra python3 en su sistema."
    echo "Instale Python 3 desde https://www.python.org/downloads/"
    echo "Luego ejecute este script de nuevo."
    exit 1
fi

echo "Usando Python: $PYBIN"
echo ""

if ! "$PYBIN" -c "import edge_tts" >/dev/null 2>&1; then
    echo "edge-tts no está instalado. Instalando ahora..."
    "$PYBIN" -m pip install --user --quiet edge-tts || {
        echo ""
        echo "ERROR: la instalación falló."
        echo "Pruebe a ejecutar manualmente primero:"
        echo "  $PYBIN -m pip install --user edge-tts"
        exit 1
    }
    echo "edge-tts instalado."
fi

if ! "$PYBIN" -c "import edge_tts" >/dev/null 2>&1; then
    echo ""
    echo "ERROR: edge-tts instalado pero no se puede importar."
    echo "Pruebe reiniciar la Terminal, o ejecute:"
    echo "  $PYBIN -m pip install --user --upgrade edge-tts"
    exit 1
fi

mkdir -p "$OUT_DIR"

TOTAL=$(ls scripts/*.txt 2>/dev/null | wc -l | tr -d ' ')
DONE=0
SKIP=0
NEW=0

if [ "$TOTAL" -eq 0 ]; then
    echo "ERROR: no se encuentran scripts en ./scripts/"
    exit 1
fi

echo ""
echo "Generando $TOTAL pistas MP3..."
echo "Las pistas ya existentes se omitirán — es seguro re-ejecutar."
echo ""

for txt in scripts/*.txt; do
    base=$(basename "$txt" .txt)
    mp3="$OUT_DIR/${base}.mp3"
    DONE=$((DONE+1))

    if [ -f "$mp3" ] && [ -s "$mp3" ]; then
        echo "[$DONE/$TOTAL] SKIP ${base}.mp3 (ya existe)"
        SKIP=$((SKIP+1))
        continue
    fi

    echo "[$DONE/$TOTAL] GEN  ${base}.mp3"
    "$PYBIN" -m edge_tts --voice="$VOICE" --rate="$RATE" --file="$txt" --write-media="$mp3"
    NEW=$((NEW+1))
done

echo ""
echo "=================================================="
echo "  Listo."
echo "  Total pistas:  $TOTAL"
echo "  Generadas:     $NEW"
echo "  Omitidas:      $SKIP"
echo "  Carpeta:       $OUT_DIR"
echo "=================================================="
echo ""
echo "Pulse Enter para abrir la carpeta (o Ctrl+C para salir)."
read -r
open "$OUT_DIR"
