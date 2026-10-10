#!/usr/bin/env bash
# Yo Tours - Museo del Prado - English audio guide (10 Oct 2026 edition)
# Pick a voice at runtime: Ava (default, edge-tts), Andrew or Brian (edge-tts).
# V5: each track is performed from its direction layer (perf/), with real pauses and mastering.
cd "$(dirname "$0")"

BASE_DIR="$HOME/Desktop/Prado_YoTours_EN"   # new folder name: older Prado renders stay untouched

echo ""
echo "================================================================"
echo "  Yo Tours - Museo del Prado (10 Oct 2026 edition)"
echo "  Museo del Prado - English  (59 tracks, about 2 h 30 on foot)"
echo "================================================================"
echo ""
echo "Choose a voice:"
echo "  1) Ava        - Microsoft edge-tts, warm natural female. THE CHOSEN VOICE. Needs internet."
echo "  2) Andrew     - Microsoft edge-tts, warm conversational male (trial voice)."
echo "  3) Brian      - Microsoft edge-tts (earlier test voice)."
echo ""
printf "Enter 1, 2 or 3 [1]: "
read CHOICE
CHOICE="${CHOICE:-1}"
case "$CHOICE" in
    2) VOICE_NAME="Andrew"; export EDGE_VOICE="en-US-AndrewMultilingualNeural" ;;
    3) VOICE_NAME="Brian";  export EDGE_VOICE="en-US-BrianMultilingualNeural" ;;
    *) CHOICE=1; VOICE_NAME="Ava"; export EDGE_VOICE="en-US-AvaMultilingualNeural" ;;
esac
echo ""
echo "What should be rendered?"
echo "  1) The full tour (59 tracks)"
echo "  2) Two voice samples only: 035 Las Meninas + 053 The Black Paintings (a few minutes)"
printf "Enter 1 or 2 [1]: "
read SCOPE
if [ "$SCOPE" = "2" ]; then
    export ONLY="035 053"
    BASE_DIR="$HOME/Desktop/Prado_YoTours_Voice_Samples/Sample"
fi

HAVE_FFMPEG=1
command -v ffmpeg >/dev/null 2>&1 || { HAVE_FFMPEG=0; echo "WARNING: ffmpeg not found. Install it with: brew install ffmpeg"; }

    echo ""
    echo "Voice: $VOICE_NAME (edge-tts, $EDGE_VOICE)."
    if [ "$HAVE_FFMPEG" = "0" ]; then
        echo "ERROR: the V5 edge-tts render needs ffmpeg (for the pauses and the volume levelling)."
        echo "Install it with:  brew install ffmpeg   then run this again."
        read -p "Press enter..."; exit 1
    fi
    OUTPUT_DIR="${BASE_DIR}_${VOICE_NAME}"; mkdir -p "$OUTPUT_DIR"
    echo "Output: $OUTPUT_DIR"
    if ! command -v python3 >/dev/null 2>&1; then
        echo "ERROR: python3 not found. Install Python 3.9+ first."; read -p "Press enter..."; exit 1
    fi
    if ! python3 -c "import edge_tts" 2>/dev/null; then
        echo "Installing edge-tts (one-time)..."
        python3 -m pip install --user --quiet edge-tts || \
            python3 -m pip install --user --quiet --break-system-packages edge-tts
    fi
    echo "Generating MP3s by section (each passage is voiced separately, so this takes a while)..."
    if ! python3 render_edge.py "$OUTPUT_DIR"; then
        python3 tag_tracks.py "$OUTPUT_DIR" . en
        echo ""; echo "Not finished yet. Run the same command again: finished tracks are skipped."
        read -p "Press enter..."; exit 1
    fi
    python3 tag_tracks.py "$OUTPUT_DIR" . en

# navigation PDF + guides into the tour folder (not for voice samples)
echo ""
[ -n "$ONLY" ] || for f in Prado_Audio_Guide_Route.pdf README.txt; do
    cp "$f" "$OUTPUT_DIR/" 2>/dev/null && echo "  [copy] $f"
done
if [ -z "$ONLY" ] && [ -d USER_TEST ]; then
    mkdir -p "$OUTPUT_DIR/USER_TEST" && cp USER_TEST/* "$OUTPUT_DIR/USER_TEST/" && echo "  [copy] USER_TEST/"
fi

echo ""
echo "================================================================"
echo "  Done. Tour saved to: $OUTPUT_DIR"
echo "  One folder per section, tracks numbered in walking order."
echo "  Prado_Audio_Guide_Route.pdf: the route and where to stand for every track."
echo "================================================================"
read -p "Press enter to close..."
