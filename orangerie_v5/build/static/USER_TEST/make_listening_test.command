#!/usr/bin/env bash
# Builds the blind desk-listening test (TEST_PLAN.md, Test 1) from the folders already on your Desktop:
#   June guide  ~/Desktop/Palazzo_Pitti_Audio_EN_am_michael
#   V5          ~/Desktop/Palazzo_Pitti_V5_1_EN_am_michael  and  ~/Desktop/Palazzo_Pitti_V5_1_EN_Ava
# Output: ~/Desktop/Pitti_Listening_Test/  (clips named by random code + ANSWER_KEY.txt; keep the key away from listeners)
D="$HOME/Desktop"; OUT="$D/Pitti_Listening_Test"
OLD="$D/Palazzo_Pitti_Audio_EN_am_michael"; V5K="$D/Palazzo_Pitti_V5_1_EN_am_michael"; V5B="$D/Palazzo_Pitti_V5_1_EN_Ava"
for d in "$OLD" "$V5K" "$V5B"; do [ -d "$d" ] || { echo "Missing folder: $d  (render it first)"; read -p "Press enter..."; exit 1; }; done
mkdir -p "$OUT"
python3 - "$OLD" "$V5K" "$V5B" "$OUT" <<'PY'
import sys, glob, os, random, shutil
old, v5k, v5b, out = sys.argv[1:]
pick = [("Throne Room",   ("015_", "021_")),
        ("Seggiola",      ("019_", "015_")),
        ("Amphitheatre",  ("081_", "053_"))]
def find(folder, prefix):
    m = glob.glob(os.path.join(folder, "*", prefix + "*.mp3"))
    if not m: sys.exit(f"Not found: {prefix}* in {folder}")
    return m[0]
items = []
for name, (o, n) in pick:
    items += [(name, "A  June guide, am_michael", find(old, o)),
              (name, "B  V5, am_michael", find(v5k, n)),
              (name, "C  V5, Ava", find(v5b, n))]
random.shuffle(items)
codes = random.sample(range(100, 1000), len(items))
key = ["Pitti listening test - ANSWER KEY (do not show listeners)", ""]
for i, ((name, ver, src), code) in enumerate(zip(items, codes), 1):
    dst = os.path.join(out, f"{i:02d}_clip_{code}.mp3"); shutil.copy(src, dst)
    key.append(f"{i:02d}_clip_{code}.mp3   {name:<13} {ver}")
open(os.path.join(out, "ANSWER_KEY.txt"), "w").write("\n".join(key) + "\n")
print("\n".join(key[2:]))
PY
echo ""; echo "Done: $OUT  (play clips in number order; score each on the feedback sheet)"
read -p "Press enter to close..."
