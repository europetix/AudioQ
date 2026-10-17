#!/usr/bin/env bash
# Builds the blind desk-listening test (TEST_PLAN.md, Test 1) from the folders on your Desktop:
#   V4 guide  ~/Desktop/Orangerie_Audio_EN          (Track_NN_*.mp3)
#   V5 guide  ~/Desktop/Orangerie_V5_EN_Ava         (<section>/NNN_*.mp3)
# Output: ~/Desktop/Orangerie_Listening_Test/  (clips named by random code + ANSWER_KEY.txt; keep the key away from listeners)
D="$HOME/Desktop"; OUT="$D/Orangerie_Listening_Test"; V4="$D/Orangerie_Audio_EN"; V5="$D/Orangerie_V5_EN_Ava"
for d in "$V4" "$V5"; do [ -d "$d" ] || { echo "Missing folder: $d  (render it first)"; read -p "Press enter..."; exit 1; }; done
mkdir -p "$OUT"
python3 - "$V4" "$V5" "$OUT" <<'PY'
import sys, glob, os, random, shutil
v4, v5, out = sys.argv[1:]
pick = [("Morning", "Track_05_", "007_"), ("Lerolle sisters", "Track_14_", "020_"), ("Pastry cook", "Track_24_", "046_")]
def find(pattern):
    m = glob.glob(pattern)
    if not m: sys.exit(f"Not found: {pattern}")
    return m[0]
items = []
for name, a, b in pick:
    items += [(name, "A  V4, Brian", find(os.path.join(v4, a + "*.mp3"))), (name, "B  V5, Ava", find(os.path.join(v5, "*", b + "*.mp3")))]
random.shuffle(items); codes = random.sample(range(100, 1000), len(items))
key = ["Orangerie listening test - ANSWER KEY (do not show listeners)", ""]
for i, ((name, ver, src), code) in enumerate(zip(items, codes), 1):
    dst = os.path.join(out, f"{i:02d}_clip_{code}.mp3"); shutil.copy(src, dst); key.append(f"{i:02d}_clip_{code}.mp3   {name:<16} {ver}")
open(os.path.join(out, "ANSWER_KEY.txt"), "w").write("\n".join(key) + "\n"); print("\n".join(key[2:]))
PY
echo ""; echo "Done: $OUT"; read -p "Press enter to close..."
