#!/usr/bin/env bash
# Yo Tours - Estadio Santiago Bernabeu - English audio guide (23 Oct 2026 edition)
# Pick a voice at runtime: Ava (default, edge-tts), Andrew or Brian (edge-tts).
# V5: each track is performed from its direction layer (perf/), with real pauses and mastering.
cd "$(dirname "$0")"

BASE_DIR="$HOME/Desktop/Bernabeu_YoTours_EN"   # new folder name: older Bernabeu renders stay untouched

echo ""
echo "================================================================"
echo "  Yo Tours - Estadio Santiago Bernabeu (23 Oct 2026 edition)"
echo "  Estadio Santiago Bernabeu - English  (28 tracks: 23 main stops + 5 short Extras)"
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
echo "  1) The guide in all three lengths: Full (28 tracks, about 65 min), Essential (17 tracks, about 40 min)"
echo "     and Highlights (9 tracks, about 20 min). Records once, then makes the three folders."
echo "  2) Two voice samples only: 016 La Decima + 025 The late comebacks (a few minutes)"
echo "  3) Highlights only (9 tracks, about 20 min; quickest to make)"
printf "Enter 1, 2 or 3 [1]: "
read SCOPE
if [ "$SCOPE" = "2" ]; then
    export ONLY="016 025"
    BASE_DIR="$HOME/Desktop/Bernabeu_YoTours_Voice_Samples/Sample"
fi
if [ "$SCOPE" = "3" ]; then
    export ONLY="001 003 007 010 016 022 023 025 028"
    BASE_DIR="$HOME/Desktop/Bernabeu_YoTours_EN_Highlights_only"
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
# navigation PDF + guides into the tour folder (not for voice samples)
echo ""
[ "$SCOPE" = "2" ] || for f in Bernabeu_Audio_Guide_Route.pdf README.txt; do
    cp "$f" "$OUTPUT_DIR/" 2>/dev/null && echo "  [copy] $f"
done
if [ "$SCOPE" != "2" ] && [ "$SCOPE" != "3" ]; then make_length Essential "$ESSENTIAL"; make_length Highlights "$HIGHLIGHTS"; fi
if [ "$SCOPE" != "2" ] && [ -d USER_TEST ]; then
    mkdir -p "$OUTPUT_DIR/USER_TEST" && cp USER_TEST/* "$OUTPUT_DIR/USER_TEST/" && echo "  [copy] USER_TEST/"
fi

echo ""
echo "================================================================"
echo "  Done. Full tour saved to: $OUTPUT_DIR"
[ "$SCOPE" = "2" ] || [ "$SCOPE" = "3" ] || echo "  Shorter versions: ${OUTPUT_DIR}_Essential and ${OUTPUT_DIR}_Highlights"
echo "  One folder per section, tracks numbered in walking order."
echo "  Bernabeu_Audio_Guide_Route.pdf: the route and where to stand for every track."
echo "================================================================"
read -p "Press enter to close..."
