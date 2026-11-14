#!/usr/bin/env bash
# Rebuilds the FC Barcelona Museum · Spotify Camp Nou bundle + zip from v5/tracks/*.perf.txt, v5/bridges/*.txt,
# v5/i18n/ (none yet: ES/FR/DE come later) and build/static/. Run from anywhere.
set -e
cd "$(dirname "$0")/.."
B=bundle/SpotifyCampNou_YoTours
[ -f build/static/cover.jpg ] || python3 build/cover/make_cover.py
python3 build/make_bundle.py
python3 build/route_map.py $B
cp v5/ONSITE_CHECKLIST.txt $B/ 2>/dev/null || true
find bundle -name __pycache__ -prune -exec rm -rf {} \;
mkdir -p /mnt/user-data/outputs && rm -f /mnt/user-data/outputs/SpotifyCampNou_YoTours_ALL_LANGUAGES.zip
(cd bundle && zip -qr -X /mnt/user-data/outputs/SpotifyCampNou_YoTours_ALL_LANGUAGES.zip SpotifyCampNou_YoTours)
echo "OK -> /mnt/user-data/outputs/SpotifyCampNou_YoTours_ALL_LANGUAGES.zip"
