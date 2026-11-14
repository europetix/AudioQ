#!/usr/bin/env bash
# Yo Tours - FC Barcelona Museum · Spotify Camp Nou - English audio guide (14 Nov 2026 edition)
# Pick a voice at runtime: Ava (default, edge-tts), Andrew or Brian (edge-tts).
# V5: each track is performed from its direction layer (perf/), with real pauses and mastering.
cd "$(dirname "$0")"

BASE_DIR="$HOME/Desktop/SpotifyCampNou_YoTours_EN"

echo ""
echo "================================================================"
echo "  Yo Tours - FC Barcelona Museum · Spotify Camp Nou: a club that keeps coming home (14 Nov 2026 edition)"
echo "  FC Barcelona Museum - English  (34 tracks: 24 main stops + 10 Extras)"
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
echo "  1) The guide in all three lengths: Full (34 tracks, a little over 1 h 30), Essential (18 tracks, about 1 h)"
echo "     and Highlights (6 tracks, about 35 min). Times include walking and the show in the round room; a wait for the next show adds more."
echo "     Records once, then makes the three folders."
echo "  2) Two voice samples only: 013 a name the registrar refused + 029 where the players sat (a few minutes)"
echo "  3) Highlights only (6 tracks, about 35 min; quickest to make; option 1 later reuses them)"
printf "Enter 1, 2 or 3 [1]: "
read SCOPE
if [ "$SCOPE" = "2" ]; then
    export ONLY="013 029"
    BASE_DIR="$HOME/Desktop/SpotifyCampNou_YoTours_Voice_Samples/Sample"
fi
if [ "$SCOPE" = "3" ]; then
    export ONLY="001 008 022 024 028 034"   # recorded into the full-tour folder (option 1 later skips them), then the Highlights folder is made
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

ESSENTIAL="001 006 008 009 011 012 014 015 016 021 022 023 024 026 027 028 029 034"
HIGHLIGHTS="001 008 022 024 028 034"
make_length () {   # a shorter version out of the full render (no re-recording), with spoken "next stop" bridges: $1 = name, $2 = tracks
    python3 make_lengths.py "$OUTPUT_DIR" "." "en" "$1" "$2" && python3 tag_tracks.py "${OUTPUT_DIR}_$1" "." "en" >/dev/null
    cp SpotifyCampNou_Audio_Guide_Route.pdf "${OUTPUT_DIR}_$1/" 2>/dev/null
}
# navigation PDF + guides into the tour folder (not for voice samples)
echo ""
[ "$SCOPE" = "2" ] || for f in SpotifyCampNou_Audio_Guide_Route.pdf README.txt; do
    cp "$f" "$OUTPUT_DIR/" 2>/dev/null && echo "  [copy] $f"
done
if [ "$SCOPE" != "2" ] && [ "$SCOPE" != "3" ]; then make_length Essential "$ESSENTIAL"; make_length Highlights "$HIGHLIGHTS"; fi
if [ "$SCOPE" = "3" ]; then make_length Highlights "$HIGHLIGHTS"; fi
if [ "$SCOPE" != "2" ] && [ -d USER_TEST ]; then
    mkdir -p "$OUTPUT_DIR/USER_TEST" && cp USER_TEST/* "$OUTPUT_DIR/USER_TEST/" && echo "  [copy] USER_TEST/"
fi

echo ""
echo "================================================================"
if [ "$SCOPE" = "3" ]; then echo "  Done. The Highlights tracks are recorded in: $OUTPUT_DIR (option 1 later adds the rest)"; else echo "  Done. Full tour saved to: $OUTPUT_DIR"; fi
[ "$SCOPE" = "2" ] || [ "$SCOPE" = "3" ] || echo "  Shorter versions: ${OUTPUT_DIR}_Essential and ${OUTPUT_DIR}_Highlights"
[ "$SCOPE" = "3" ] && echo "  Highlights (with the spoken 'next stop' lines): ${OUTPUT_DIR}_Highlights"
echo "  One folder per section, tracks numbered in walking order."
echo "  SpotifyCampNou_Audio_Guide_Route.pdf: the route and where to stand for every track."
echo "================================================================"
read -p "Press enter to close..."
