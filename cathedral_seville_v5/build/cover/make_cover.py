#!/usr/bin/env python3
"""Album cover for the Seville Cathedral and Giralda audio guide (Yo Tours). Run once; output: ../static/cover.jpg.
Original artwork: a line drawing of a tall square bell tower with a lattice-panelled shaft, a tiered Renaissance belfry and a
weathervane figure, beside the line of a Gothic roof with pinnacles; and type. No logo, no artwork reproduced."""
import os
from PIL import Image, ImageDraw, ImageFont
S = 1600
INK, GOLD, CREAM, MUTED = (24, 30, 44), (201, 165, 92), (243, 236, 222), (150, 140, 120)
F = "/usr/share/fonts/truetype/dejavu/"
serif_b, serif_i, sans = F + "DejaVuSerif-Bold.ttf", F + "DejaVuSerif-Italic.ttf", F + "DejaVuSans.ttf"
im = Image.new("RGB", (S, S), INK); d = ImageDraw.Draw(im)
cx, base = int(S * 0.56), int(S * 0.58)
w = 150; shaft_top = int(S * 0.32)
d.rectangle([cx - w // 2, shaft_top, cx + w // 2, base], outline=CREAM, width=6)               # minaret shaft
for k in range(3):                                                                               # lattice panels
    y0 = shaft_top + 30 + k * 95
    for s in (-1, 1):
        x0 = cx + s * 38 - 22
        d.rectangle([x0, y0, x0 + 44, y0 + 70], outline=MUTED, width=3)
        d.line([x0, y0 + 70, x0 + 22, y0 + 40, x0 + 44, y0 + 70], fill=MUTED, width=3)
d.line([cx - w // 2 - 12, shaft_top, cx + w // 2 + 12, shaft_top], fill=GOLD, width=6)
b1 = shaft_top - 90; d.rectangle([cx - 60, b1, cx + 60, shaft_top], outline=GOLD, width=5)         # belfry tiers
d.arc([cx - 30, b1 + 20, cx + 30, b1 + 80], 180, 360, fill=GOLD, width=4)
b2 = b1 - 60; d.rectangle([cx - 44, b2, cx + 44, b1], outline=CREAM, width=4)
b3 = b2 - 45; d.rectangle([cx - 30, b3, cx + 30, b2], outline=CREAM, width=4)
d.ellipse([cx - 22, b3 - 40, cx + 22, b3], outline=GOLD, width=4)                                # small dome
d.line([cx, b3 - 40, cx, b3 - 95], fill=GOLD, width=4)                                           # weathervane figure
d.ellipse([cx - 9, b3 - 112, cx + 9, b3 - 94], outline=GOLD, width=3)
d.line([cx, b3 - 80, cx - 28, b3 - 60], fill=GOLD, width=3)
roof_y = int(S * 0.47)                                                                           # Gothic roofline at left
d.line([int(S * 0.10), roof_y, cx - w // 2, roof_y], fill=MUTED, width=5)
for k in range(6):
    x = int(S * 0.13) + k * 85
    d.line([x, roof_y, x, roof_y - 60], fill=MUTED, width=3); d.line([x - 8, roof_y - 45, x, roof_y - 75, x + 8, roof_y - 45], fill=MUTED, width=3)
d.line([int(S * 0.08), base, int(S * 0.92), base], fill=GOLD, width=5)
def centred(text, font, y, fill, spacing=0):
    if spacing:
        widths = [d.textlength(ch, font=font) for ch in text]; total = sum(widths) + spacing * (len(text) - 1)
        x = (S - total) / 2
        for ch, ww in zip(text, widths):
            d.text((x, y), ch, font=font, fill=fill); x += ww + spacing
    else:
        d.text(((S - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)
centred("YO TOURS", ImageFont.truetype(sans, 58), int(S * 0.05), GOLD, spacing=22)
centred("Seville Cathedral", ImageFont.truetype(serif_b, 104), int(S * 0.64), CREAM)
centred("and the Giralda", ImageFont.truetype(serif_i, 80), int(S * 0.75), CREAM)
d.line([S * 0.36, S * 0.862, S * 0.64, S * 0.862], fill=GOLD, width=4)
centred("Audio Guide", ImageFont.truetype(serif_i, 80), int(S * 0.88), GOLD)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static", "cover.jpg")
im.resize((800, 800), Image.LANCZOS).save(out, quality=90)
print("OK ->", os.path.abspath(out))
