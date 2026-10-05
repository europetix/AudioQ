#!/usr/bin/env bash
# V5 - Musee d'Orsay - Spanish / French / German audio guides (same launcher shape as English).
# Voices chosen 5 Oct 2026 (all female): ES Dalia (es-MX), FR Vivienne, DE Katja. Same direction layer, pauses and
# mastering as the English guide; English name respellings are off (RESPELL=0). Scripts: languages/<lang>/.
cd "$(dirname "$0")"

echo ""
echo "================================================================"
echo "  V5 - Musee d'Orsay  (75 tracks)"
echo "================================================================"
echo ""
echo "Choose a language:"
echo "  1) Espanol   - voice Dalia    (es-MX-DaliaNeural)"
echo "  2) Francais  - voice Vivienne (fr-FR-VivienneMultilingualNeural)"
echo "  3) Deutsch   - voice Katja    (de-DE-KatjaNeural)"
printf "Enter 1, 2 or 3: "
read CHOICE
case "$CHOICE" in
    1) L=es; TAG=ES; VOICE_NAME=Dalia;    export EDGE_VOICE="es-MX-DaliaNeural" ;;
    2) L=fr; TAG=FR; VOICE_NAME=Vivienne; export EDGE_VOICE="fr-FR-VivienneMultilingualNeural" ;;
    3) L=de; TAG=DE; VOICE_NAME=Katja;    export EDGE_VOICE="de-DE-KatjaNeural" ;;
    *) echo "Please run again and enter 1, 2 or 3."; read -p "Press enter..."; exit 1 ;;
esac
echo ""
echo "What should be rendered?"
echo "  1) The full guide (75 tracks)"
echo "  2) Two voice samples only: 013 Olympia + 044 Van Gogh self-portrait (a few minutes)"
printf "Enter 1 or 2 [1]: "
read SCOPE
OUTPUT_DIR="$HOME/Desktop/Orsay_V5_${TAG}_${VOICE_NAME}"
if [ "$SCOPE" = "2" ]; then export ONLY="013 044"; OUTPUT_DIR="$HOME/Desktop/Orsay_V5_Voice_Samples/${TAG}_${VOICE_NAME}"; fi
export RESPELL=0

[ -d "languages/$L/scripts" ] || { echo "ERROR: languages/$L is missing from this bundle."; read -p "Press enter..."; exit 1; }
command -v ffmpeg >/dev/null 2>&1 || { echo "ERROR: ffmpeg is needed.  brew install ffmpeg  then run this again."; read -p "Press enter..."; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo "ERROR: python3 not found. Install Python 3.9+ first."; read -p "Press enter..."; exit 1; }
if ! python3 -c "import edge_tts" 2>/dev/null; then
    echo "Installing edge-tts (one-time)..."
    python3 -m pip install --user --quiet edge-tts || python3 -m pip install --user --quiet --break-system-packages edge-tts
fi
mkdir -p "$OUTPUT_DIR"
echo ""
echo "Voice: $VOICE_NAME ($EDGE_VOICE)"
echo "Output: $OUTPUT_DIR"
echo "Generating MP3s by section (each passage is voiced separately, so this takes a while)..."
( cd "languages/$L" && python3 ../../render_edge.py "$OUTPUT_DIR" ) || { echo "$VOICE_NAME render failed (run it again: finished tracks are skipped)."; read -p "Press enter..."; exit 1; }
if [ -z "$ONLY" ]; then cp Orsay_Audio_Guide_Route.pdf "$OUTPUT_DIR/" 2>/dev/null && echo "  [copy] route map"; fi

echo ""
echo "================================================================"
echo "  Done. Guide saved to: $OUTPUT_DIR"
echo "  One folder per section, tracks numbered in walking order."
echo "================================================================"
read -p "Press enter to close..."
