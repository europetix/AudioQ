#!/usr/bin/env python3
"""Album cover for the Poble Espanyol (Barcelona) audio guide (Yo Tours). Run once; output: ../static/cover.jpg.
Original artwork: a town gate with two round towers and merlons joined by a bridge, roofs and a bell tower behind; and
type. No logo, no photograph, no artwork reproduced."""
import os
from PIL import Image, ImageDraw, ImageFont
S = 1600
INK, GOLD, CREAM, MUTED = (24, 30, 44), (201, 165, 92), (243, 236, 222), (150, 140, 120)
F = "/usr/share/fonts/truetype/dejavu/"
serif_b, serif_i, sans = F + "DejaVuSerif-Bold.ttf", F + "DejaVuSerif-Italic.ttf", F + "DejaVuSans.ttf"
im = Image.new("RGB", (S, S), INK); d = ImageDraw.Draw(im)
base = int(S * 0.58)
# a town gate with two round towers and merlons, a bridge between them; roofs and a bell tower behind
for cx in (int(S * 0.40), int(S * 0.60)):
    w = int(S * 0.075); top = int(S * 0.30)
    d.line([cx - w, base, cx - w, top, cx + w, top, cx + w, base], fill=CREAM, width=6)
    for k in range(5):                                            # merlons
        x0 = cx - w + k * (2 * w) // 5 + 4
        d.rectangle([x0, top - 26, x0 + (2 * w) // 10, top], outline=CREAM, width=4)
d.line([int(S * 0.475), int(S * 0.36), int(S * 0.525), int(S * 0.36)], fill=GOLD, width=6)   # the bridge
d.arc([int(S * 0.478), int(S * 0.42), int(S * 0.522), int(S * 0.50)], 180, 360, fill=GOLD, width=6); d.line([int(S * 0.478), int(S * 0.46), int(S * 0.478), base], fill=GOLD, width=6); d.line([int(S * 0.522), int(S * 0.46), int(S * 0.522), base], fill=GOLD, width=6)  # the arch
for x0, y0, x1 in ((0.10, 0.48, 0.30), (0.70, 0.46, 0.90)):     # roofs
    d.line([int(S * x0), base, int(S * x0), int(S * y0), int(S * (x0 + x1) / 2), int(S * (y0 - 0.06)), int(S * x1), int(S * y0), int(S * x1), base], fill=MUTED, width=4)
tx = int(S * 0.80)                                              # a brick bell tower behind
d.rectangle([tx - 28, int(S * 0.22), tx + 28, int(S * 0.46)], outline=MUTED, width=4)
d.line([tx - 28, int(S * 0.22), tx, int(S * 0.17), tx + 28, int(S * 0.22)], fill=MUTED, width=4)
d.line([int(S * 0.06), base, int(S * 0.94), base], fill=GOLD, width=5)
def centred(text, font, y, fill, spacing=0):
    if spacing:
        widths = [d.textlength(ch, font=font) for ch in text]; total = sum(widths) + spacing * (len(text) - 1)
        x = (S - total) / 2
        for ch, ww in zip(text, widths):
            d.text((x, y), ch, font=font, fill=fill); x += ww + spacing
    else:
        d.text(((S - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)
centred("YO TOURS", ImageFont.truetype(sans, 58), int(S * 0.05), GOLD, spacing=22)
centred("Poble Espanyol", ImageFont.truetype(serif_b, 104), int(S * 0.66), CREAM)
centred("Barcelona · the village of 1929", ImageFont.truetype(serif_i, 64), int(S * 0.765), CREAM)
d.line([S * 0.36, S * 0.862, S * 0.64, S * 0.862], fill=GOLD, width=4)
centred("Audio Guide", ImageFont.truetype(serif_i, 80), int(S * 0.88), GOLD)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static", "cover.jpg")
im.resize((800, 800), Image.LANCZOS).save(out, quality=90)
print("OK ->", os.path.abspath(out))
