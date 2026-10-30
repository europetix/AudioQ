#!/usr/bin/env python3
"""Album cover for the Real Alcázar de Sevilla audio guide (Yo Tours). Run once; output: ../static/cover.jpg.
Original artwork: a line drawing of a courtyard arcade of lobed arches reflected in a long pool, and type.
No logo, no artwork reproduced."""
import os
from PIL import Image, ImageDraw, ImageFont
S = 1600
INK, GOLD, CREAM, MUTED, WATER = (24, 30, 44), (201, 165, 92), (243, 236, 222), (150, 140, 120), (90, 140, 160)
F = "/usr/share/fonts/truetype/dejavu/"
serif_b, serif_i, sans = F + "DejaVuSerif-Bold.ttf", F + "DejaVuSerif-Italic.ttf", F + "DejaVuSans.ttf"
im = Image.new("RGB", (S, S), INK); d = ImageDraw.Draw(im)
x0, x1, top, base = int(S * 0.12), int(S * 0.88), int(S * 0.17), int(S * 0.46)
n = 5; w = (x1 - x0) / n
d.line([x0 - 20, top, x1 + 20, top], fill=GOLD, width=7)                       # cornice
d.rectangle([x0, top + 14, x1, top + 70], outline=MUTED, width=3)              # band of plasterwork
for k in range(18):                                                             # lattice hint in the band
    xx = x0 + 10 + k * (x1 - x0 - 20) / 17
    d.line([xx, top + 18, xx + 18, top + 66], fill=MUTED, width=2); d.line([xx + 18, top + 18, xx, top + 66], fill=MUTED, width=2)
spring = top + 150
for i in range(n):                                                              # lobed arches on slim columns
    a, b = x0 + i * w, x0 + (i + 1) * w
    cx, r = (a + b) / 2, (b - a) / 2 - 14
    lobes = 7
    import math
    pts = []
    for j in range(lobes):
        t0 = math.pi + j * math.pi / lobes; t1 = math.pi + (j + 1) * math.pi / lobes
        lx, ly = cx + r * math.cos((t0 + t1) / 2), spring + r * math.sin((t0 + t1) / 2)
        lr = r * math.sin(math.pi / lobes / 2) * 1.15
        d.arc([lx - lr, ly - lr, lx + lr, ly + lr], 180 + math.degrees((t0 + t1) / 2 - math.pi) - 90, 180 + math.degrees((t0 + t1) / 2 - math.pi) + 90, fill=CREAM, width=4)
    d.line([a + 8, spring, a + 8, base], fill=CREAM if i == 0 else MUTED, width=5)
    d.line([b - 8, spring, b - 8, base], fill=MUTED, width=5)
d.line([x0 - 30, base, x1 + 30, base], fill=GOLD, width=6)                      # pavement edge
for k in range(4):                                                              # the long pool and its reflection lines
    y = base + 30 + k * 26
    d.line([cx_ := S // 2 - 230 + k * 18, y, S // 2 + 230 - k * 18, y], fill=WATER, width=4)
def centred(text, font, y, fill, spacing=0):
    if spacing:
        widths = [d.textlength(ch, font=font) for ch in text]; total = sum(widths) + spacing * (len(text) - 1)
        x = (S - total) / 2
        for ch, ww in zip(text, widths):
            d.text((x, y), ch, font=font, fill=fill); x += ww + spacing
    else:
        d.text(((S - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)
centred("YO TOURS", ImageFont.truetype(sans, 58), int(S * 0.06), GOLD, spacing=22)
centred("Real Alcázar", ImageFont.truetype(serif_b, 124), int(S * 0.64), CREAM)
centred("Seville", ImageFont.truetype(serif_i, 80), int(S * 0.76), CREAM)
d.line([S * 0.36, S * 0.862, S * 0.64, S * 0.862], fill=GOLD, width=4)
centred("Audio Guide", ImageFont.truetype(serif_i, 80), int(S * 0.88), GOLD)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static", "cover.jpg")
im.resize((800, 800), Image.LANCZOS).save(out, quality=90)
print("OK ->", os.path.abspath(out))
