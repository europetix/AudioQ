#!/usr/bin/env bash
# V5 TEST BUILD - Musee d'Orsay - EN  (same launcher shape as V4.5)
# Pick a voice at runtime: Ava (default, edge-tts), am_michael (Kokoro, via uv), Andrew or Brian (edge-tts).
# V5: each track is performed from its direction layer (perf/), with real pauses and mastering.
cd "$(dirname "$0")"

BASE_DIR="$HOME/Desktop/Orsay_V5_EN"

echo ""
echo "================================================================"
echo "  V5 - Musee d Orsay"
echo "  Musee d Orsay - English  (75 tracks, ~2 h 45)"
echo "================================================================"
echo ""
echo "Choose a voice:"
echo "  1) Ava        - Microsoft edge-tts, warm natural female. THE CHOSEN VOICE. Needs internet."
echo "  2) am_michael - Kokoro (warmer). First run sets up Python+model via uv (~2GB)."
echo "  3) Andrew     - Microsoft edge-tts, warm conversational male (trial voice)."
echo "  4) Brian      - Microsoft edge-tts (the earlier V5 test voice)."
echo ""
printf "Enter 1, 2, 3 or 4 [1]: "
read CHOICE
CHOICE="${CHOICE:-1}"
case "$CHOICE" in
    3) VOICE_NAME="Andrew"; export EDGE_VOICE="en-US-AndrewMultilingualNeural" ;;
    4) VOICE_NAME="Brian";  export EDGE_VOICE="en-US-BrianMultilingualNeural" ;;
    2) VOICE_NAME="am_michael" ;;
    *) CHOICE=1; VOICE_NAME="Ava"; export EDGE_VOICE="en-US-AvaMultilingualNeural" ;;
esac
echo ""
echo "What should be rendered?"
echo "  1) The full tour (75 tracks)"
echo "  2) Two voice samples only: 013 Olympia + 044 Van Gogh self-portrait (a few minutes)"
printf "Enter 1 or 2 [1]: "
read SCOPE
if [ "$SCOPE" = "2" ]; then
    export ONLY="013 044"
    BASE_DIR="$HOME/Desktop/Orsay_V5_Voice_Samples/Sample"
fi

HAVE_FFMPEG=1
command -v ffmpeg >/dev/null 2>&1 || { HAVE_FFMPEG=0; echo "WARNING: ffmpeg not found. Install it with: brew install ffmpeg"; }

if [ "$CHOICE" = "2" ]; then
    echo ""
    echo "Voice: am_michael (Kokoro)."
    OUTPUT_DIR="${BASE_DIR}_${VOICE_NAME}"; mkdir -p "$OUTPUT_DIR"
    echo "Output: $OUTPUT_DIR"
    command -v uv >/dev/null 2>&1 || export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"
    if ! command -v uv >/dev/null 2>&1; then
        echo "Installing uv (one-time; it manages the right Python for you, nothing system-wide)..."
        curl -LsSf https://astral.sh/uv/install.sh | sh || { echo "uv install failed."; read -p "Press enter..."; exit 1; }
        export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"
    fi
    echo "Rendering with Kokoro (first run downloads Python 3.11 + model, please be patient)..."
    uv run --python 3.11 --with "kokoro>=0.9.4" --with soundfile --with numpy \
        python render_kokoro.py "$OUTPUT_DIR" || { echo "Kokoro render failed."; read -p "Press enter..."; exit 1; }
else
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
    python3 render_edge.py "$OUTPUT_DIR" || { echo "$VOICE_NAME render failed."; read -p "Press enter..."; exit 1; }
fi

# navigation PDF + guides into the tour folder (not for voice samples)
echo ""
[ -n "$ONLY" ] || for f in Orsay_Audio_Guide_Route.pdf README.txt; do
    cp "$f" "$OUTPUT_DIR/" 2>/dev/null && echo "  [copy] $f"
done
if [ -z "$ONLY" ] && [ -d USER_TEST ]; then
    mkdir -p "$OUTPUT_DIR/USER_TEST" && cp USER_TEST/* "$OUTPUT_DIR/USER_TEST/" && echo "  [copy] USER_TEST/"
fi

echo ""
echo "================================================================"
echo "  Done. Tour saved to: $OUTPUT_DIR"
echo "  One folder per section, tracks numbered in walking order."
echo "  Orsay_Audio_Guide_Route.pdf: the route and where to stand for every track."
echo "================================================================"
read -p "Press enter to close..."
