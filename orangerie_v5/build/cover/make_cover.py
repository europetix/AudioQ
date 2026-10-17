#!/usr/bin/env python3
"""Album cover for the Musée de l'Orangerie audio guide (Yo Tours), shown by phone music players. Run once; output: ../static/cover.jpg.
Original artwork: two oval rooms seen from above with generic lily pads, and type. No museum logo, no painting reproduced."""
import math, os
from PIL import Image, ImageDraw, ImageFont
S = 1600                                      # drawn large, saved at 800 px for smooth edges
INK, GOLD, CREAM, MUTED = (24, 30, 44), (201, 165, 92), (243, 236, 222), (150, 140, 120)
F = "/usr/share/fonts/truetype/dejavu/"
serif_b, serif_i, sans = F + "DejaVuSerif-Bold.ttf", F + "DejaVuSerif-Italic.ttf", F + "DejaVuSans.ttf"
im = Image.new("RGB", (S, S), INK); d = ImageDraw.Draw(im)
cx, cy = S // 2, int(S * 0.40)
# an oval room seen from above (the museum's galleries are ovals) with a few generic lily pads; original drawing,
# no logo, no reproduction of any painting
rx, ry = int(S * 0.36), int(S * 0.22)
d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], outline=GOLD, width=10)
d.ellipse([cx - rx + 30, cy - ry + 30, cx + rx - 30, cy + ry - 30], outline=MUTED, width=3)
PADS = [(-0.42, -0.18, 1.0), (-0.30, -0.05, 0.7), (-0.47, 0.12, 0.8), (0.05, 0.28, 0.9), (0.18, 0.15, 0.6),
        (0.40, -0.22, 0.85), (0.50, 0.02, 0.65), (0.30, -0.02, 0.5), (-0.12, -0.30, 0.55)]
for fx, fy, k in PADS:                                   # flattened pads with a notch, as seen at an angle on water
    px, py = cx + int(fx * rx), cy + int(fy * ry); w, h = int(46 * k), int(20 * k)
    d.pieslice([px - w, py - h, px + w, py + h], 300, 270 + 360, fill=MUTED)
for fx, fy in [(-0.30, -0.05), (0.18, 0.15)]:            # two small blossoms
    px, py = cx + int(fx * rx), cy + int(fy * ry) - 10
    d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=GOLD)
def centred(text, font, y, fill, spacing=0):
    if spacing:
        widths = [d.textlength(ch, font=font) for ch in text]; total = sum(widths) + spacing * (len(text) - 1)
        x = (S - total) / 2
        for ch, w in zip(text, widths):
            d.text((x, y), ch, font=font, fill=fill); x += w + spacing
    else:
        d.text(((S - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)
centred("YO TOURS", ImageFont.truetype(sans, 58), int(S * 0.06), GOLD, spacing=22)
centred("Musée de", ImageFont.truetype(serif_i, 80), int(S * 0.665), CREAM)
centred("l'Orangerie", ImageFont.truetype(serif_b, 140), int(S * 0.715), CREAM)
d.line([S * 0.36, S * 0.862, S * 0.64, S * 0.862], fill=GOLD, width=4)
centred("Audio Guide", ImageFont.truetype(serif_i, 80), int(S * 0.88), GOLD)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static", "cover.jpg")
im.resize((800, 800), Image.LANCZOS).save(out, "JPEG", quality=88, optimize=True)
print("cover ->", os.path.normpath(out), os.path.getsize(out), "bytes")
