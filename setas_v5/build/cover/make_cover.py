#!/usr/bin/env python3
"""Album cover for the Setas de Sevilla and Antiquarium audio guide (Yo Tours). Run once; output: ../static/cover.jpg.
Original artwork: three abstract lattice parasols on flared trunks under a walkway line, with a row of arches below the
ground line for the Roman remains; and type. No logo, no photograph, no artwork reproduced."""
import os
from PIL import Image, ImageDraw, ImageFont
S = 1600
INK, GOLD, CREAM, MUTED = (24, 30, 44), (201, 165, 92), (243, 236, 222), (150, 140, 120)
F = "/usr/share/fonts/truetype/dejavu/"
serif_b, serif_i, sans = F + "DejaVuSerif-Bold.ttf", F + "DejaVuSerif-Italic.ttf", F + "DejaVuSans.ttf"
im = Image.new("RGB", (S, S), INK); d = ImageDraw.Draw(im)
base = int(S * 0.58)
# three abstract parasols: a trunk widening into a flat lattice canopy, a walkway line along the top
tops = [(int(S * 0.26), int(S * 0.27), 230), (int(S * 0.52), int(S * 0.22), 280), (int(S * 0.78), int(S * 0.29), 220)]
for cx, ty, hw in tops:
    tw = 34                                                                                      # trunk half-width at the foot
    d.line([cx - tw, base, cx - tw - 10, ty + 170, cx - hw, ty + 60], fill=CREAM, width=6)       # flaring sides
    d.line([cx + tw, base, cx + tw + 10, ty + 170, cx + hw, ty + 60], fill=CREAM, width=6)
    d.line([cx - hw, ty + 60, cx - hw, ty, cx + hw, ty, cx + hw, ty + 60], fill=CREAM, width=6)  # canopy
    for k in range(1, 9):                                                                        # waffle grid
        x = cx - hw + k * (2 * hw) // 9
        d.line([x, ty + 4, x, ty + 56], fill=MUTED, width=3)
    for k in (1, 2):
        y = ty + k * 20
        d.line([cx - hw + 4, y, cx + hw - 4, y], fill=MUTED, width=2)
    for k in range(1, 5):                                                                        # grid down the trunk
        y = ty + 60 + k * (base - ty - 60) // 5
        if y <= ty + 170: half = int(hw + (tw + 10 - hw) * (y - ty - 60) / 110)                  # follow the flared edge
        else: half = int(tw + 10 - 10 * (y - ty - 170) / (base - ty - 170))
        d.line([cx - half + 6, y, cx + half - 6, y], fill=MUTED, width=2)
d.line([int(S * 0.06), int(S * 0.20), int(S * 0.94), int(S * 0.20)], fill=GOLD, width=5)          # the walkway on top
for x in range(int(S * 0.10), int(S * 0.92), 70):                                                # Roman arches below the ground line
    d.arc([x, base + 24, x + 50, base + 74], 180, 360, fill=GOLD, width=3)
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
centred("Setas de Sevilla", ImageFont.truetype(serif_b, 104), int(S * 0.66), CREAM)
centred("and the Antiquarium", ImageFont.truetype(serif_i, 76), int(S * 0.765), CREAM)
d.line([S * 0.36, S * 0.862, S * 0.64, S * 0.862], fill=GOLD, width=4)
centred("Audio Guide", ImageFont.truetype(serif_i, 80), int(S * 0.88), GOLD)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static", "cover.jpg")
im.resize((800, 800), Image.LANCZOS).save(out, quality=90)
print("OK ->", os.path.abspath(out))
