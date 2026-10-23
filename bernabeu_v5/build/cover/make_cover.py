#!/usr/bin/env python3
"""Album cover for the Museo Reina Sofía audio guide (Yo Tours), shown by phone music players. Run once; output: ../static/cover.jpg.
Original artwork: a generic façade with two glass towers, and type. No museum logo, no artwork reproduced."""
import math, os
from PIL import Image, ImageDraw, ImageFont
S = 1600                                      # drawn large, saved at 800 px for smooth edges
INK, GOLD, CREAM, MUTED = (24, 30, 44), (201, 165, 92), (243, 236, 222), (150, 140, 120)
F = "/usr/share/fonts/truetype/dejavu/"
serif_b, serif_i, sans = F + "DejaVuSerif-Bold.ttf", F + "DejaVuSerif-Italic.ttf", F + "DejaVuSans.ttf"
im = Image.new("RGB", (S, S), INK); d = ImageDraw.Draw(im)
cx, cy = S // 2, int(S * 0.40)
# a generic long hospital façade with a grid of windows and two slim glass lift towers in front; original drawing, no logo
fw, fh = int(S * 0.62), int(S * 0.24); fx0 = cx - fw // 2; fy0 = int(S * 0.24)
d.rectangle([fx0, fy0, fx0 + fw, fy0 + fh], outline=GOLD, width=8)
for r in range(4):                                       # window grid
    for c in range(11):
        wx = fx0 + 26 + c * (fw - 52) // 11; wy = fy0 + 24 + r * (fh - 40) // 4
        d.rectangle([wx, wy, wx + 30, wy + 34], outline=MUTED, width=3)
for tx in (cx - int(S * 0.13), cx + int(S * 0.13) - 70):   # two glass towers, taller than the façade
    d.rectangle([tx, fy0 - 70, tx + 70, fy0 + fh + 40], fill=INK, outline=GOLD, width=7)
    for k in range(1, 9):
        y = fy0 - 70 + k * (fh + 110) // 9
        d.line([tx + 8, y, tx + 62, y], fill=MUTED, width=2)
d.line([fx0 - 40, fy0 + fh + 40, fx0 + fw + 40, fy0 + fh + 40], fill=GOLD, width=5)   # street line
def centred(text, font, y, fill, spacing=0):
    if spacing:
        widths = [d.textlength(ch, font=font) for ch in text]; total = sum(widths) + spacing * (len(text) - 1)
        x = (S - total) / 2
        for ch, w in zip(text, widths):
            d.text((x, y), ch, font=font, fill=fill); x += w + spacing
    else:
        d.text(((S - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)
centred("YO TOURS", ImageFont.truetype(sans, 58), int(S * 0.06), GOLD, spacing=22)
centred("Museo Reina Sofía", ImageFont.truetype(serif_b, 118), int(S * 0.67), CREAM)
centred("Madrid", ImageFont.truetype(serif_i, 80), int(S * 0.775), CREAM)
d.line([S * 0.36, S * 0.862, S * 0.64, S * 0.862], fill=GOLD, width=4)
centred("Audio Guide", ImageFont.truetype(serif_i, 80), int(S * 0.88), GOLD)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static", "cover.jpg")
im.resize((800, 800), Image.LANCZOS).save(out, "JPEG", quality=88, optimize=True)
print("cover ->", os.path.normpath(out), os.path.getsize(out), "bytes")
