#!/usr/bin/env bash
# V5 TEST BUILD - Tour #43 Palazzo Pitti + Boboli - EN  (same launcher shape as V4.5)
# Pick a voice at runtime: Brian (edge-tts) or am_michael (Kokoro, via uv).
# V5: each track is performed from its direction layer (perf/), with real pauses and mastering.
cd "$(dirname "$0")"

BASE_DIR="$HOME/Desktop/Palazzo_Pitti_V5_1_EN"

echo ""
echo "================================================================"
echo "  V5.1 - Tour #43"
echo "  Palazzo Pitti + Boboli - English  (61 tracks, ~142 min)"
echo "================================================================"
echo ""
echo "Choose a voice:"
echo "  1) Brian      - Microsoft edge-tts. Needs internet, no big download."
echo "  2) am_michael - Kokoro (warmer). First run sets up Python+model via uv (~2GB)."
echo ""
printf "Enter 1 or 2 [1]: "
read CHOICE
CHOICE="${CHOICE:-1}"

HAVE_FFMPEG=1
command -v ffmpeg >/dev/null 2>&1 || { HAVE_FFMPEG=0; echo "WARNING: ffmpeg not found. Install it with: brew install ffmpeg"; }

if [ "$CHOICE" = "2" ]; then
    echo ""
    echo "Voice: am_michael (Kokoro)."
    OUTPUT_DIR="${BASE_DIR}_am_michael"; mkdir -p "$OUTPUT_DIR"
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
    echo "Voice: Brian (edge-tts)."
    if [ "$HAVE_FFMPEG" = "0" ]; then
        echo "ERROR: the V5 Brian render needs ffmpeg (for the pauses and the volume levelling)."
        echo "Install it with:  brew install ffmpeg   then run this again."
        read -p "Press enter..."; exit 1
    fi
    OUTPUT_DIR="${BASE_DIR}_Brian"; mkdir -p "$OUTPUT_DIR"
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
    python3 render_edge.py "$OUTPUT_DIR" || { echo "Brian render failed."; read -p "Press enter..."; exit 1; }
fi

# navigation PDF + guides into the tour folder
echo ""
for f in Palazzo_Pitti_Audio_Guide_Route.pdf README.txt; do
    cp "$f" "$OUTPUT_DIR/" 2>/dev/null && echo "  [copy] $f"
done
if [ -d USER_TEST ]; then
    mkdir -p "$OUTPUT_DIR/USER_TEST" && cp USER_TEST/* "$OUTPUT_DIR/USER_TEST/" && echo "  [copy] USER_TEST/"
fi

echo ""
echo "================================================================"
echo "  Done. Tour saved to: $OUTPUT_DIR"
echo "  One folder per section, tracks numbered in walking order."
echo "  Palazzo_Pitti_Audio_Guide_Route.pdf: the route and where to stand for every track."
echo "================================================================"
read -p "Press enter to close..."
