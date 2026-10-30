#!/usr/bin/env bash
# Rebuilds the Setas bundle + zip from v5/tracks/*.perf.txt, v5/i18n/ and build/static/. Run from anywhere.
set -e
cd "$(dirname "$0")/.."
B=bundle/Setas_YoTours
python3 build/make_bundle.py
python3 build/route_map.py $B
cp v5/ONSITE_CHECKLIST.txt $B/ 2>/dev/null || true
find bundle -name __pycache__ -prune -exec rm -rf {} \;
mkdir -p /mnt/user-data/outputs && rm -f /mnt/user-data/outputs/Setas_YoTours_ALL_LANGUAGES.zip
(cd bundle && zip -qr -X /mnt/user-data/outputs/Setas_YoTours_ALL_LANGUAGES.zip Setas_YoTours)
echo "OK -> /mnt/user-data/outputs/Setas_YoTours_ALL_LANGUAGES.zip"
