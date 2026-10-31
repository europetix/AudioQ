#!/usr/bin/env python3
"""Album cover for the Guggenheim Museum Bilbao audio guide (Yo Tours). Run once; output: ../static/cover.jpg.
Original artwork: abstract overlapping metal curves with panel seams above a river line, a tower and a bridge deck; and
type. No logo, no photograph, no artwork reproduced."""
import os
from PIL import Image, ImageDraw, ImageFont
S = 1600
INK, GOLD, CREAM, MUTED = (24, 30, 44), (201, 165, 92), (243, 236, 222), (150, 140, 120)
F = "/usr/share/fonts/truetype/dejavu/"
serif_b, serif_i, sans = F + "DejaVuSerif-Bold.ttf", F + "DejaVuSerif-Italic.ttf", F + "DejaVuSans.ttf"
im = Image.new("RGB", (S, S), INK); d = ImageDraw.Draw(im)
base = int(S * 0.58)
import math
# abstract curved metal forms (overlapping arcs, like sheets of titanium) above a river line; a tower at the right
for k, (cx, cy, rx, ry, a0, a1, col) in enumerate([
        (0.30, 0.50, 0.22, 0.20, 190, 350, CREAM), (0.45, 0.44, 0.20, 0.24, 200, 345, MUTED),
        (0.58, 0.48, 0.24, 0.20, 185, 340, CREAM), (0.40, 0.56, 0.30, 0.12, 180, 330, GOLD),
        (0.70, 0.52, 0.16, 0.16, 200, 360, MUTED)]):
    box = [int(S * (cx - rx)), int(S * (cy - ry)), int(S * (cx + rx)), int(S * (cy + ry))]
    d.arc(box, a0, a1, fill=col, width=7)
    for t in range(1, 4):                                     # panel seams across each curve
        ang = math.radians(a0 + (a1 - a0) * t / 4)
        x0 = S * cx + S * rx * math.cos(ang); y0 = S * cy + S * ry * math.sin(ang)
        d.line([x0, y0, x0 + 0.25 * (S * cx - x0), y0 + 0.25 * (S * cy - y0)], fill=MUTED, width=2)
tx = int(S * 0.84)                                            # the tower beside the bridge
d.line([tx - 30, base, tx - 18, int(S * 0.30), tx + 18, int(S * 0.28), tx + 30, base], fill=CREAM, width=6)
d.line([int(S * 0.74), int(S * 0.40), int(S * 0.97), int(S * 0.40)], fill=GOLD, width=5)   # the bridge deck
for x in range(int(S * 0.06), int(S * 0.94), 60):             # the river
    d.arc([x, base + 18, x + 60, base + 48], 200, 340, fill=GOLD, width=3)
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
centred("Guggenheim Bilbao", ImageFont.truetype(serif_b, 100), int(S * 0.66), CREAM)
centred("the building and its works", ImageFont.truetype(serif_i, 70), int(S * 0.765), CREAM)
d.line([S * 0.36, S * 0.862, S * 0.64, S * 0.862], fill=GOLD, width=4)
centred("Audio Guide", ImageFont.truetype(serif_i, 80), int(S * 0.88), GOLD)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static", "cover.jpg")
im.resize((800, 800), Image.LANCZOS).save(out, quality=90)
print("OK ->", os.path.abspath(out))
