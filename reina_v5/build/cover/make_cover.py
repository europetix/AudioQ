#!/usr/bin/env python3
"""Album cover for the Museo del Prado audio guide (Yo Tours), shown by phone music players. Run once; output: ../static/cover.jpg.
Original artwork: a generic neoclassical portico, and type. No museum logo."""
import math, os
from PIL import Image, ImageDraw, ImageFont
S = 1600                                      # drawn large, saved at 800 px for smooth edges
INK, GOLD, CREAM, MUTED = (24, 30, 44), (201, 165, 92), (243, 236, 222), (150, 140, 120)
F = "/usr/share/fonts/truetype/dejavu/"
serif_b, serif_i, sans = F + "DejaVuSerif-Bold.ttf", F + "DejaVuSerif-Italic.ttf", F + "DejaVuSans.ttf"
im = Image.new("RGB", (S, S), INK); d = ImageDraw.Draw(im)
cx, cy = S // 2, int(S * 0.40)
# a generic neoclassical portico (six columns, entablature, steps); original drawing, no logo
pw = int(S * 0.56); px0 = cx - pw // 2; top = int(S * 0.20); base = int(S * 0.56)
d.polygon([(px0 - 30, top + 70), (cx, top - 40), (px0 + pw + 30, top + 70)], outline=GOLD, width=10)   # pediment
d.rectangle([px0 - 30, top + 70, px0 + pw + 30, top + 130], outline=GOLD, width=8)                    # entablature
d.line([px0 - 30, top + 100, px0 + pw + 30, top + 100], fill=MUTED, width=3)
n = 6; colw = 44; gapw = (pw - n * colw) / (n - 1)
for k in range(n):                                                                                      # columns
    x = int(px0 + k * (colw + gapw))
    d.rectangle([x - 8, top + 136, x + colw + 8, top + 156], outline=GOLD, width=5)                     # capital
    d.rectangle([x, top + 156, x + colw, base - 26], outline=GOLD, width=6)
    for f in (1, 2): d.line([x + f * colw // 3, top + 168, x + f * colw // 3, base - 38], fill=MUTED, width=2)
    d.rectangle([x - 8, base - 26, x + colw + 8, base - 6], outline=GOLD, width=5)                      # base
for k in range(3):                                                                                      # steps
    d.rectangle([px0 - 50 - k * 30, base + k * 26, px0 + pw + 50 + k * 30, base + 20 + k * 26], outline=MUTED, width=4)
def centred(text, font, y, fill, spacing=0):
    if spacing:
        widths = [d.textlength(ch, font=font) for ch in text]; total = sum(widths) + spacing * (len(text) - 1)
        x = (S - total) / 2
        for ch, w in zip(text, widths):
            d.text((x, y), ch, font=font, fill=fill); x += w + spacing
    else:
        d.text(((S - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)
centred("YO TOURS", ImageFont.truetype(sans, 58), int(S * 0.06), GOLD, spacing=22)
centred("Museo del Prado", ImageFont.truetype(serif_b, 132), int(S * 0.67), CREAM)
centred("Madrid", ImageFont.truetype(serif_i, 80), int(S * 0.775), CREAM)
d.line([S * 0.36, S * 0.862, S * 0.64, S * 0.862], fill=GOLD, width=4)
centred("Audio Guide", ImageFont.truetype(serif_i, 80), int(S * 0.88), GOLD)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static", "cover.jpg")
im.resize((800, 800), Image.LANCZOS).save(out, "JPEG", quality=88, optimize=True)
print("cover ->", os.path.normpath(out), os.path.getsize(out), "bytes")
