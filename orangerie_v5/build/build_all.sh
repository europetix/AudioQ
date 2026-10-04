#!/usr/bin/env bash
# Rebuilds the whole V5 test bundle + zip from v5/tracks/*.perf.txt and build/static/. Run from anywhere.
set -e
cd /home/claude/orangerie
B=bundle/Orangerie_V5_EN
python3 build/make_bundle.py
python3 build/route_sheet.py $B || echo 'route map: pending (Orangerie layout)'
python3 build/feedback_form.py $B
find bundle -name __pycache__ -prune -exec rm -rf {} \;
mkdir -p /home/user/AudioQ/orangerie_v5/outputs && rm -f /home/user/AudioQ/orangerie_v5/outputs/Orangerie_V5_EN.zip
(cd bundle && zip -qr -X /home/user/AudioQ/orangerie_v5/outputs/Orangerie_V5_EN.zip Orangerie_V5_EN)
echo "OK -> /home/user/AudioQ/orangerie_v5/outputs/Orangerie_V5_EN.zip"
