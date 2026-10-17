#!/usr/bin/env bash
# V5.1 - Tour #43 Palazzo Pitti + Boboli - female voice samples in Spanish, French and German.
# Two translated tracks (015 Madonna della Seggiola, 053 The Amphitheatre) per voice, same direction layer,
# pauses and mastering as the English guide. English name respellings are switched off (RESPELL=0).
# Output: ~/Desktop/Palazzo_Pitti_V5_1_Voice_Samples/<LANG>_<Voice>/   (Spanish v2: ES_v2_<Voice>)
# Optional: pass a language to render only that one, e.g.   bash voice_samples_ES_FR_DE.command es
cd "$(dirname "$0")"
OUT="$HOME/Desktop/Palazzo_Pitti_V5_1_Voice_Samples"
VOICES="es:Ximena:es-ES-XimenaNeural es:Dalia:es-MX-DaliaNeural fr:Vivienne:fr-FR-VivienneMultilingualNeural fr:Denise:fr-FR-DeniseNeural de:Seraphina:de-DE-SeraphinaMultilingualNeural de:Katja:de-DE-KatjaNeural"

echo ""
echo "================================================================"
echo "  Tour #43 - voice samples: Spanish, French, German (female)"
echo "================================================================"
command -v ffmpeg >/dev/null 2>&1 || { echo "ERROR: ffmpeg is needed.  brew install ffmpeg  then run this again."; read -p "Press enter..."; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo "ERROR: python3 not found."; read -p "Press enter..."; exit 1; }
if ! python3 -c "import edge_tts" 2>/dev/null; then
    echo "Installing edge-tts (one-time)..."
    python3 -m pip install --user --quiet edge-tts || python3 -m pip install --user --quiet --break-system-packages edge-tts
fi
OK=""; MISSING=""
for v in $VOICES; do
    LANG_CODE="${v%%:*}"; rest="${v#*:}"; NAME="${rest%%:*}"; VOICE="${rest#*:}"
    [ -n "$1" ] && [ "$1" != "$LANG_CODE" ] && continue
    TAG="$(echo "$LANG_CODE" | tr a-z A-Z)_${NAME}"; [ "$LANG_CODE" = "es" ] && TAG="ES_v2_${NAME}"
    echo ""; echo "--- $TAG  ($VOICE)"
    if ( cd "languages/$LANG_CODE" && ONLY="015 053" EDGE_VOICE="$VOICE" RESPELL=0 python3 ../../render_edge.py "$OUT/$TAG" ); then
        OK="$OK $TAG"
    else
        MISSING="$MISSING $TAG"; echo "  (no audio for $VOICE - this voice may not be offered by the free service; skipping)"
    fi
done
echo ""
echo "================================================================"
echo "  Done. Samples in: $OUT"
echo "  Rendered:$OK"
[ -n "$MISSING" ] && echo "  Not available:$MISSING"
echo "================================================================"
read -p "Press enter to close..."
