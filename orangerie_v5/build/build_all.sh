#!/usr/bin/env bash
# Rebuilds the whole V5 test bundle + zip from v5/tracks/*.perf.txt and build/static/. Run from anywhere.
set -e
cd /home/claude/orangerie
B=bundle/Palazzo_Pitti_V5_Test_EN
python3 build/make_bundle.py
python3 build/route_sheet.py $B
python3 build/feedback_form.py $B
find bundle -name __pycache__ -prune -exec rm -rf {} \;
mkdir -p /mnt/user-data/outputs && rm -f /mnt/user-data/outputs/Palazzo_Pitti_V5_Test_EN.zip
(cd bundle && zip -qr -X /mnt/user-data/outputs/Palazzo_Pitti_V5_Test_EN.zip Palazzo_Pitti_V5_Test_EN)
echo "OK -> /mnt/user-data/outputs/Palazzo_Pitti_V5_Test_EN.zip"
