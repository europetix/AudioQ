#!/usr/bin/env bash
# Rebuilds the whole V5 test bundle + zip from v5/tracks/*.perf.txt and build/static/. Run from anywhere.
set -e
cd /home/claude/orsay
B=bundle/Orsay_V5_EN
python3 build/make_bundle.py
python3 build/route_sheet.py $B || echo 'route map: pending (Orsay layout)'
python3 build/feedback_form.py $B
find bundle -name __pycache__ -prune -exec rm -rf {} \;
mkdir -p /home/user/AudioQ/orsay_v5/outputs && rm -f /home/user/AudioQ/orsay_v5/outputs/Orsay_V5_EN.zip
(cd bundle && zip -qr -X /home/user/AudioQ/orsay_v5/outputs/Orsay_V5_EN.zip Orsay_V5_EN)
echo "OK -> /home/user/AudioQ/orsay_v5/outputs/Orsay_V5_EN.zip"
