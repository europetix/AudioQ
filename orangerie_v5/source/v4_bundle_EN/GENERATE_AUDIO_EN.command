#!/bin/bash
# Musée de l'Orangerie — English Audio Generator
# Voice: en-US-BrianMultilingualNeural at -8%

set -e
cd "$(dirname "$0")"

VOICE="en-US-BrianMultilingualNeural"
RATE="-8%"
OUT_DIR="$HOME/Desktop/Orangerie_Audio_EN"

echo "=================================================="
echo "  Musée de l'Orangerie — English Audio Generator"
echo "  Voice: Brian Multilingual (US)"
echo "  Rate:  $RATE"
echo "  Output: $OUT_DIR"
echo "=================================================="

PYBIN="$(command -v python3 || true)"
if [ -z "$PYBIN" ]; then
    echo ""
    echo "ERROR: python3 not found on your system."
    echo "Install Python 3 from https://www.python.org/downloads/"
    echo "Then run this script again."
    exit 1
fi

echo "Using Python: $PYBIN"
echo ""

# Make sure edge_tts is importable
if ! "$PYBIN" -c "import edge_tts" >/dev/null 2>&1; then
    echo "edge-tts not installed. Installing now..."
    "$PYBIN" -m pip install --user --quiet edge-tts || {
        echo ""
        echo "ERROR: pip install failed."
        echo "Try running this manually first:"
        echo "  $PYBIN -m pip install --user edge-tts"
        exit 1
    }
    echo "edge-tts installed."
fi

if ! "$PYBIN" -c "import edge_tts" >/dev/null 2>&1; then
    echo ""
    echo "ERROR: edge-tts installed but cannot be imported."
    echo "Try restarting your terminal, or run:"
    echo "  $PYBIN -m pip install --user --upgrade edge-tts"
    exit 1
fi

mkdir -p "$OUT_DIR"

TOTAL=$(ls scripts/*.txt 2>/dev/null | wc -l | tr -d ' ')
DONE=0
SKIP=0
NEW=0

if [ "$TOTAL" -eq 0 ]; then
    echo "ERROR: no scripts found in ./scripts/"
    exit 1
fi

echo ""
echo "Generating $TOTAL MP3 tracks..."
echo "Existing files will be skipped — safe to re-run."
echo ""

for txt in scripts/*.txt; do
    base=$(basename "$txt" .txt)
    mp3="$OUT_DIR/${base}.mp3"
    DONE=$((DONE+1))

    if [ -f "$mp3" ] && [ -s "$mp3" ]; then
        echo "[$DONE/$TOTAL] SKIP ${base}.mp3 (already exists)"
        SKIP=$((SKIP+1))
        continue
    fi

    echo "[$DONE/$TOTAL] GEN  ${base}.mp3"
    "$PYBIN" -m edge_tts --voice="$VOICE" --rate="$RATE" --file="$txt" --write-media="$mp3"
    NEW=$((NEW+1))
done

echo ""
echo "=================================================="
echo "  Done."
echo "  Total tracks:  $TOTAL"
echo "  Generated:     $NEW"
echo "  Skipped:       $SKIP"
echo "  Folder:        $OUT_DIR"
echo "=================================================="
echo ""
echo "Press Enter to open the folder (or Ctrl+C to exit)."
read -r
open "$OUT_DIR"
