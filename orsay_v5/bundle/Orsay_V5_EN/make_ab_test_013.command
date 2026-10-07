#!/usr/bin/env bash
# A/B listening test (7 Oct 2026): track 013 Olympia, voice Ava, four versions side by side.
#   A - current                     what the guide sounds like today
#   B - voice finish                rumble cut, a touch of warmth and presence, softer "s" sounds, light compression
#   C - voice finish + room tone    as B, with a barely audible room tone so pauses sound like a recording
#   D - B + C + chime               as C, with a soft two-note chime before the voice starts
# Listen on earbuds, ideally the ones a visitor would use. Output: ~/Desktop/Orsay_V5_AB_Test_013/
cd "$(dirname "$0")"
OUT="$HOME/Desktop/Orsay_V5_AB_Test_013"
command -v ffmpeg >/dev/null 2>&1 || { echo "ERROR: ffmpeg is needed.  brew install ffmpeg  then run this again."; exit 1; }
python3 -c "import edge_tts" 2>/dev/null || python3 -m pip install --user --quiet edge-tts || \
    python3 -m pip install --user --quiet --break-system-packages edge-tts
mkdir -p "$OUT"; WORK="$(mktemp -d)"
export EDGE_VOICE="en-US-AvaMultilingualNeural" ONLY="013"
echo ""; echo "Making four versions of 013 Olympia (about 1-2 minutes each)..."
for V in "A - current|" "B - voice finish|VOICE_FINISH=1" "C - voice finish + room tone|VOICE_FINISH=1 ROOM_TONE=1" \
         "D - voice finish + room tone + chime|VOICE_FINISH=1 ROOM_TONE=1 CHIME=1"; do
    NAME="${V%%|*}"; FLAGS="${V#*|}"; KEY="${NAME%% *}"
    [ -f "$OUT/$NAME.mp3" ] && { echo "  [skip] $NAME"; continue; }
    echo "  $NAME"
    env $FLAGS python3 render_edge.py "$WORK/$KEY" > "$WORK/$KEY.log" 2>&1 || { echo "    not finished, run this again"; continue; }
    cp "$(find "$WORK/$KEY" -name '013_*.mp3' | head -1)" "$OUT/$NAME.mp3"
done
echo ""; echo "Done. Compare the four files in: $OUT"
open "$OUT" 2>/dev/null
