#!/usr/bin/env python3
"""Album cover for the Museo Nacional Thyssen-Bornemisza audio guide (Yo Tours), shown by phone music players. Run once; output: ../static/cover.jpg.
Original artwork: a generic palace front with a garden, and type. No museum logo, no artwork reproduced."""
import math, os
from PIL import Image, ImageDraw, ImageFont
S = 1600                                      # drawn large, saved at 800 px for smooth edges
INK, GOLD, CREAM, MUTED = (24, 30, 44), (201, 165, 92), (243, 236, 222), (150, 140, 120)
F = "/usr/share/fonts/truetype/dejavu/"
serif_b, serif_i, sans = F + "DejaVuSerif-Bold.ttf", F + "DejaVuSerif-Italic.ttf", F + "DejaVuSans.ttf"
im = Image.new("RGB", (S, S), INK); d = ImageDraw.Draw(im)
cx, cy = S // 2, int(S * 0.40)
# a generic neoclassical palace front with a garden in front; original drawing, no museum logo, no artwork reproduced
fw, fh = int(S * 0.66), int(S * 0.25); fx0 = cx - fw // 2; fy0 = int(S * 0.23)
SALMON = (214, 150, 120)
d.rectangle([fx0, fy0, fx0 + fw, fy0 + fh], outline=SALMON, width=8)
d.line([fx0 - 20, fy0, fx0 + fw + 20, fy0], fill=GOLD, width=8)            # cornice
for r in range(2):                                                         # two rows of tall windows
    for c in range(9):
        wx = fx0 + 34 + c * (fw - 68) // 9; wy = fy0 + 30 + r * (fh - 40) // 2
        d.rectangle([wx, wy, wx + 34, wy + 70], outline=CREAM if c == 4 else MUTED, width=3)
d.rectangle([cx - 34, fy0 + fh - 96, cx + 34, fy0 + fh], outline=GOLD, width=6)   # main door
for k in range(7):                                                         # garden trees along the front
    tx = fx0 + 30 + k * (fw - 60) // 6
    d.ellipse([tx - 30, fy0 + fh + 18, tx + 30, fy0 + fh + 70], outline=(120, 150, 110), width=5)
d.line([fx0 - 40, fy0 + fh + 80, fx0 + fw + 40, fy0 + fh + 80], fill=GOLD, width=5)   # Paseo line
def centred(text, font, y, fill, spacing=0):
    if spacing:
        widths = [d.textlength(ch, font=font) for ch in text]; total = sum(widths) + spacing * (len(text) - 1)
        x = (S - total) / 2
        for ch, w in zip(text, widths):
            d.text((x, y), ch, font=font, fill=fill); x += w + spacing
    else:
        d.text(((S - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)
centred("YO TOURS", ImageFont.truetype(sans, 58), int(S * 0.06), GOLD, spacing=22)
centred("Museo Nacional", ImageFont.truetype(serif_b, 92), int(S * 0.62), CREAM)
centred("Thyssen-Bornemisza", ImageFont.truetype(serif_b, 104), int(S * 0.69), CREAM)
centred("Madrid", ImageFont.truetype(serif_i, 80), int(S * 0.79), CREAM)
d.line([S * 0.36, S * 0.862, S * 0.64, S * 0.862], fill=GOLD, width=4)
centred("Audio Guide", ImageFont.truetype(serif_i, 80), int(S * 0.88), GOLD)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static", "cover.jpg")
im.resize((800, 800), Image.LANCZOS).save(out, "JPEG", quality=88, optimize=True)
print("cover ->", os.path.normpath(out), os.path.getsize(out), "bytes")
