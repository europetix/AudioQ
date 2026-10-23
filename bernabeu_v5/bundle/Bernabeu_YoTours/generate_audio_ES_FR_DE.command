#!/usr/bin/env bash
# Yo Tours - Estadio Santiago Bernabeu - Spanish / French / German audio guides (same launcher shape as English).
# Voices chosen 5 Oct 2026 (all female): ES Dalia (es-MX), FR Vivienne, DE Katja. Same direction layer, pauses and
# mastering as the English guide; English name respellings are off (RESPELL=0). Scripts: languages/<lang>/.
cd "$(dirname "$0")"

echo ""
echo "================================================================"
echo "  Yo Tours - Estadio Santiago Bernabeu  (28 tracks: 23 main + 5 Extras, 23 Oct 2026 edition)"
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
echo "  1) The guide in all three lengths: Full (28 tracks, about 65 min), Essential (17 tracks, about 40 min)"
echo "     and Highlights (9 tracks, about 20 min). Records once, then makes the three folders."
echo "  2) Two voice samples only: 016 La Decima + 025 The late comebacks (a few minutes)"
echo "  3) Highlights only (9 tracks, about 20 min; quickest to make)"
printf "Enter 1, 2 or 3 [1]: "
read SCOPE
OUTPUT_DIR="$HOME/Desktop/Bernabeu_YoTours_${TAG}_${VOICE_NAME}"
if [ "$SCOPE" = "2" ]; then export ONLY="016 025"; OUTPUT_DIR="$HOME/Desktop/Bernabeu_YoTours_Voice_Samples/${TAG}_${VOICE_NAME}"; fi
if [ "$SCOPE" = "3" ]; then export ONLY="001 003 007 010 016 022 023 025 028"; OUTPUT_DIR="$HOME/Desktop/Bernabeu_YoTours_${TAG}_${VOICE_NAME}_Highlights_only"; fi
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
if ! ( cd "languages/$L" && python3 ../../render_edge.py "$OUTPUT_DIR" ); then
    python3 tag_tracks.py "$OUTPUT_DIR" "languages/$L" "$L"
    echo ""; echo "Not finished yet. Run the same command again: finished tracks are skipped."
    read -p "Press enter..."; exit 1
fi
python3 tag_tracks.py "$OUTPUT_DIR" "languages/$L" "$L"
if [ "$SCOPE" != "2" ]; then cp Bernabeu_Audio_Guide_Route.pdf "$OUTPUT_DIR/" 2>/dev/null && echo "  [copy] route map"; fi
ESSENTIAL="001 002 003 004 007 009 010 011 013 014 016 019 022 023 024 025 028"
HIGHLIGHTS="001 003 007 010 016 022 023 025 028"
make_length () {   # copy a shorter version out of the full render (no re-recording): $1 = name, $2 = track numbers
    dst="${OUTPUT_DIR}_$1"; mkdir -p "$dst"
    for n in $2; do
        f=$(find "$OUTPUT_DIR" -name "${n}_*.mp3" | head -1)
        [ -n "$f" ] && { d="$dst/$(basename "$(dirname "$f")")"; mkdir -p "$d"; cp "$f" "$d/"; }
    done
    cp Bernabeu_Audio_Guide_Route.pdf "$dst/" 2>/dev/null
    echo "  [length] $1: $(echo $2 | wc -w | tr -d ' ') tracks -> $dst"
}
if [ "$SCOPE" != "2" ] && [ "$SCOPE" != "3" ]; then make_length Essential "$ESSENTIAL"; make_length Highlights "$HIGHLIGHTS"; fi

echo ""
echo "================================================================"
echo "  Done. Full guide saved to: $OUTPUT_DIR"
[ "$SCOPE" = "2" ] || [ "$SCOPE" = "3" ] || echo "  Shorter versions: ${OUTPUT_DIR}_Essential and ${OUTPUT_DIR}_Highlights"
echo "  One folder per section, tracks numbered in walking order."
echo "================================================================"
read -p "Press enter to close..."
