#!/usr/bin/env bash
# V4.5 Humanized Audio Guide - Tour #43 EN  (per-section folders + maps)
# Pick a voice at runtime: Brian (edge-tts) or am_michael (Kokoro, via uv).
cd "$(dirname "$0")"

BASE_DIR="$HOME/Desktop/Palazzo_Pitti_Audio_EN"
TMP_DIR="$(pwd)/.tmp_audio_$$"
mkdir -p "$TMP_DIR"
trap 'rm -rf "$TMP_DIR"' EXIT

echo ""
echo "================================================================"
echo "  V4.5 Humanized Audio Guide - Tour #43"
echo "  Palazzo Pitti - English  (92 tracks, ~201 min)"
echo "================================================================"
echo ""
echo "Choose a voice:"
echo "  1) Brian      - Microsoft edge-tts. Fast, no extra setup."
echo "  2) am_michael - Kokoro (warmer). First run sets up Python+model via uv (~2GB)."
echo ""
printf "Enter 1 or 2 [1]: "
read CHOICE
CHOICE="${CHOICE:-1}"

HAVE_FFMPEG=1
command -v ffmpeg >/dev/null 2>&1 || { HAVE_FFMPEG=0; echo "WARNING: ffmpeg not found."; }

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
    VOICE="en-US-BrianMultilingualNeural"; RATE="-8%"; PAUSE_S=5
    SILENCE_MP3="$TMP_DIR/silence.mp3"
    if [ "$HAVE_FFMPEG" = "1" ]; then
        ffmpeg -hide_banner -loglevel error -y -f lavfi \
            -i "anullsrc=channel_layout=mono:sample_rate=24000" \
            -t "$PAUSE_S" -q:a 9 -acodec libmp3lame -f mp3 "$SILENCE_MP3"
    fi
    echo "Generating MP3s by section..."
    for secdir in scripts/*/ ; do
        sec="$(basename "$secdir")"
        mkdir -p "$OUTPUT_DIR/$sec"
        for f in "$secdir"*.txt ; do
            [ -e "$f" ] || continue
            base="$(basename "${f%.txt}")"
            out="$OUTPUT_DIR/$sec/$base.mp3"
            if [ -f "$out" ]; then echo "  [skip] $sec/$base"; continue; fi
            python3 -c 'import sys; from pronunciation import apply_respelling; sys.stdout.write(apply_respelling(open(sys.argv[1],encoding="utf-8").read(),True))' "$f" > "$TMP_DIR/in.txt"
            SPEECH_MP3="$TMP_DIR/speech.mp3"
            python3 -m edge_tts --voice "$VOICE" --rate="$RATE" --file "$TMP_DIR/in.txt" --write-media "$SPEECH_MP3"
            if [ "$HAVE_FFMPEG" = "1" ]; then
                CL="$TMP_DIR/concat.txt"
                printf "file '%s'\nfile '%s'\n" "$SPEECH_MP3" "$SILENCE_MP3" > "$CL"
                ffmpeg -hide_banner -loglevel error -y -f concat -safe 0 -i "$CL" \
                    -acodec libmp3lame -q:a 4 -f mp3 "$out"
                rm -f "$CL" "$SPEECH_MP3"
            else
                mv "$SPEECH_MP3" "$out"
            fi
            echo "  [gen]  $sec/$base"
        done
    done
fi

# drop each section's map (HTML poster + image) into its output folder
if [ -d maps ]; then
    echo ""
    echo "Copying section maps + images..."
    for d in maps/*/ ; do
        sec="$(basename "$d")"
        mkdir -p "$OUTPUT_DIR/$sec"
        for m in "$d"* ; do
            [ -e "$m" ] || continue
            cp "$m" "$OUTPUT_DIR/$sec/" && echo "  [map]  $sec/$(basename "$m")"
        done
    done
fi
cp Palazzo_Pitti_EN.pdf "$OUTPUT_DIR/" 2>/dev/null || true
cp README.txt "$OUTPUT_DIR/" 2>/dev/null || true

echo ""
echo "================================================================"
echo "  Done. Tour saved to: $OUTPUT_DIR"
echo "  One folder per section, each with audio + map (HTML) + image."
echo "================================================================"
read -p "Press enter to close..."
