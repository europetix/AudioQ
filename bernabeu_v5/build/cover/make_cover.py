#!/usr/bin/env python3
"""Album cover for the Estadio Santiago Bernabéu audio guide (Yo Tours), shown by phone music players. Run once; output: ../static/cover.jpg.
Original artwork: a generic stadium wrapped in curved bands, and type. No club crest, logo or photo."""
import math, os
from PIL import Image, ImageDraw, ImageFont
S = 1600                                      # drawn large, saved at 800 px for smooth edges
INK, GOLD, CREAM, MUTED = (24, 30, 44), (201, 165, 92), (243, 236, 222), (150, 140, 120)
F = "/usr/share/fonts/truetype/dejavu/"
serif_b, serif_i, sans = F + "DejaVuSerif-Bold.ttf", F + "DejaVuSerif-Italic.ttf", F + "DejaVuSans.ttf"
im = Image.new("RGB", (S, S), INK); d = ImageDraw.Draw(im)
cx, cy = S // 2, int(S * 0.40)
# a generic stadium wrapped in curved horizontal bands, seen from the street; original drawing, no club crest or logo
w, h = int(S * 0.70), int(S * 0.30); x0, y0 = cx - w // 2, int(S * 0.20)
d.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=int(h * 0.42), outline=GOLD, width=8)
for k in range(1, 9):                                    # curved steel bands
    t = k / 9.0; y = y0 + int(h * t); bow = int(26 * math.sin(math.pi * t))
    inset = int(h * 0.42 * (1 - math.sin(math.pi * t) ** 0.5)) + 14
    d.arc([x0 + inset, y - bow - 40, x0 + w - inset, y + bow + 40], start=200, end=340, fill=MUTED if k % 2 else CREAM, width=5)
d.line([x0 - 40, y0 + h + 34, x0 + w + 40, y0 + h + 34], fill=GOLD, width=5)   # street line
def centred(text, font, y, fill, spacing=0):
    if spacing:
        widths = [d.textlength(ch, font=font) for ch in text]; total = sum(widths) + spacing * (len(text) - 1)
        x = (S - total) / 2
        for ch, w in zip(text, widths):
            d.text((x, y), ch, font=font, fill=fill); x += w + spacing
    else:
        d.text(((S - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)
centred("YO TOURS", ImageFont.truetype(sans, 58), int(S * 0.06), GOLD, spacing=22)
centred("Estadio Santiago", ImageFont.truetype(serif_b, 104), int(S * 0.60), CREAM)
centred("Bernabéu", ImageFont.truetype(serif_b, 118), int(S * 0.68), CREAM)
centred("Madrid", ImageFont.truetype(serif_i, 80), int(S * 0.785), CREAM)
d.line([S * 0.36, S * 0.862, S * 0.64, S * 0.862], fill=GOLD, width=4)
centred("Audio Guide", ImageFont.truetype(serif_i, 80), int(S * 0.88), GOLD)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static", "cover.jpg")
im.resize((800, 800), Image.LANCZOS).save(out, "JPEG", quality=88, optimize=True)
print("cover ->", os.path.normpath(out), os.path.getsize(out), "bytes")
