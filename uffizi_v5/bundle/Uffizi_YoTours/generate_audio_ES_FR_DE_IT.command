#!/usr/bin/env bash
# Yo Tours - Uffizi Gallery - Spanish / French / German / Italian audio guides (same launcher shape as English).
# Voices chosen 5 Oct 2026 (all female): ES Dalia (es-MX), FR Vivienne, DE Katja; IT Isabella added 24 Oct 2026 (Uffizi). Same direction layer, pauses and
# mastering as the English guide; English name respellings are off (RESPELL=0). Scripts: languages/<lang>/.
cd "$(dirname "$0")"

echo ""
echo "================================================================"
echo "  Yo Tours - Uffizi Gallery, Florence  (67 tracks: 53 main + 14 Extras, 24 Oct 2026 edition)"
echo "================================================================"
echo ""
echo "Choose a language:"
echo "  1) Espanol   - voice Dalia    (es-MX-DaliaNeural)"
echo "  2) Francais  - voice Vivienne (fr-FR-VivienneMultilingualNeural)"
echo "  3) Deutsch   - voice Katja    (de-DE-KatjaNeural)"
echo "  4) Italiano  - voice Isabella (it-IT-IsabellaNeural)"
printf "Enter 1, 2, 3 or 4: "
read CHOICE
case "$CHOICE" in
    1) L=es; TAG=ES; VOICE_NAME=Dalia;    export EDGE_VOICE="es-MX-DaliaNeural" ;;
    2) L=fr; TAG=FR; VOICE_NAME=Vivienne; export EDGE_VOICE="fr-FR-VivienneMultilingualNeural" ;;
    3) L=de; TAG=DE; VOICE_NAME=Katja;    export EDGE_VOICE="de-DE-KatjaNeural" ;;
    4) L=it; TAG=IT; VOICE_NAME=Isabella; export EDGE_VOICE="it-IT-IsabellaNeural" ;;
    *) echo "Please run again and enter 1, 2, 3 or 4."; read -p "Press enter..."; exit 1 ;;
esac
echo ""
echo "What should be rendered?"
echo "  1) The guide in all three lengths: Full (67 tracks, about 2 h 45), Essential (40 tracks, about 2 h)"
echo "     and Highlights (19 tracks, about 1 h 15). Records once, then makes the three folders."
echo "  2) Two voice samples only: 018 Birth of Venus + 062 Medusa (a few minutes)"
echo "  3) Highlights only (19 tracks, about 1 h 15; quickest to make; option 1 later reuses them)"
printf "Enter 1, 2 or 3 [1]: "
read SCOPE
OUTPUT_DIR="$HOME/Desktop/Uffizi_YoTours_${TAG}_${VOICE_NAME}"
if [ "$SCOPE" = "2" ]; then export ONLY="018 062"; OUTPUT_DIR="$HOME/Desktop/Uffizi_YoTours_Voice_Samples/${TAG}_${VOICE_NAME}"; fi
if [ "$SCOPE" = "3" ]; then export ONLY="001 002 006 007 017 018 022 025 030 034 035 037 046 052 057 062 063 064 067"; fi   # into the full-tour folder; option 1 later skips them
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
if [ "$SCOPE" != "2" ]; then cp Uffizi_Audio_Guide_Route.pdf "$OUTPUT_DIR/" 2>/dev/null && echo "  [copy] route map"; fi
ESSENTIAL="001 002 004 006 007 009 012 014 015 017 018 020 022 023 025 029 030 031 034 035 036 037 041 042 045 046 048 049 052 055 057 059 060 061 062 063 064 065 066 067"
HIGHLIGHTS="001 002 006 007 017 018 022 025 030 034 035 037 046 052 057 062 063 064 067"
make_length () {   # a shorter version out of the full render (no re-recording), with spoken "next stop" bridges: $1 = name, $2 = tracks
    python3 make_lengths.py "$OUTPUT_DIR" "languages/$L" "$L" "$1" "$2" && python3 tag_tracks.py "${OUTPUT_DIR}_$1" "languages/$L" "$L" >/dev/null
    cp Uffizi_Audio_Guide_Route.pdf "${OUTPUT_DIR}_$1/" 2>/dev/null
}
if [ "$SCOPE" != "2" ] && [ "$SCOPE" != "3" ]; then make_length Essential "$ESSENTIAL"; make_length Highlights "$HIGHLIGHTS"; fi
if [ "$SCOPE" = "3" ]; then make_length Highlights "$HIGHLIGHTS"; fi

echo ""
echo "================================================================"
echo "  Done. Full guide saved to: $OUTPUT_DIR"
[ "$SCOPE" = "2" ] || [ "$SCOPE" = "3" ] || echo "  Shorter versions: ${OUTPUT_DIR}_Essential and ${OUTPUT_DIR}_Highlights"
[ "$SCOPE" = "3" ] && echo "  Highlights (with the spoken 'next stop' lines): ${OUTPUT_DIR}_Highlights"
echo "  One folder per section, tracks numbered in walking order."
echo "================================================================"
read -p "Press enter to close..."
