#!/usr/bin/env python3
"""Album cover for the Uffizi Gallery audio guide (Yo Tours), shown by phone music players. Run once; output: ../static/cover.jpg.
Original artwork: a line drawing of the long Uffizi courtyard in perspective (two colonnaded wings closing on the river arch),
with a tower behind, and type. No museum logo, no artwork reproduced."""
import os
from PIL import Image, ImageDraw, ImageFont
S = 1600                                      # drawn large, saved at 800 px for smooth edges
INK, GOLD, CREAM, MUTED = (24, 30, 44), (201, 165, 92), (243, 236, 222), (150, 140, 120)
STONE = (196, 178, 150)
F = "/usr/share/fonts/truetype/dejavu/"
serif_b, serif_i, sans = F + "DejaVuSerif-Bold.ttf", F + "DejaVuSerif-Italic.ttf", F + "DejaVuSans.ttf"
im = Image.new("RGB", (S, S), INK); d = ImageDraw.Draw(im)
cx = S // 2
top, base = int(S * 0.16), int(S * 0.56)       # height band of the drawing
vx, vy = cx, int(S * 0.43)                     # vanishing point at the far (river) end
far_w, far_top = int(S * 0.13), int(S * 0.33)  # the far loggia with its arch
# tower behind the left wing (generic crenellated tower)
tx = cx + 70
d.rectangle([tx - 38, top + 70 - 40, tx + 38, far_top], outline=STONE, width=6)
d.rectangle([tx - 52, top + 70 - 70, tx + 52, top + 70 - 40], outline=STONE, width=6)
for k in range(5):
    d.rectangle([tx - 52 + k * 24, top + 70 - 92, tx - 40 + k * 24, top + 70 - 70], outline=STONE, width=4)
d.rectangle([tx - 18, top + 70 - 150, tx + 18, top + 70 - 92], outline=STONE, width=5)
# the two long wings, drawn as receding lines of arches
def wing(side):
    x_near = cx - side * int(S * 0.40); x_far = cx - side * far_w
    for frac, col, w in ((0.0, STONE, 7), (1.0, GOLD, 6)):
        pass
    y_top_near, y_top_far = top + 40, far_top
    d.line([x_near, y_top_near, x_far, y_top_far], fill=STONE, width=7)       # roof line
    d.line([x_near, base, x_far, vy + 20], fill=GOLD, width=6)               # ground line
    n = 9
    for i in range(n + 1):                                                   # piers getting closer together
        t = 1 - (1 - i / n) ** 1.8
        x = x_near + (x_far - x_near) * t
        yt = y_top_near + (y_top_far - y_top_near) * t + 70 * (1 - t) + 10
        yb = base + (vy + 20 - base) * t
        d.line([x, yt + (yb - yt) * 0.45, x, yb], fill=CREAM if i == 0 else MUTED, width=max(2, int(6 * (1 - t)) + 2))
        if i < n:                                                            # windows on the upper floors
            t2 = 1 - (1 - (i + 0.5) / n) ** 1.8
            xw = x_near + (x_far - x_near) * t2
            ywt = y_top_near + (y_top_far - y_top_near) * t2 + 40 * (1 - t2) + 18
            hw = max(4, int(16 * (1 - t2)) + 3)
            d.rectangle([xw - hw, ywt, xw + hw, ywt + hw * 3], outline=MUTED, width=2)
wing(1); wing(-1)
# the far loggia over the river: an arch between two smaller openings
d.rectangle([cx - far_w, far_top, cx + far_w, vy + 20], outline=STONE, width=6)
d.arc([cx - 46, vy - 70, cx + 46, vy + 22], 180, 360, fill=GOLD, width=6)
d.line([cx - 46, vy - 24, cx - 46, vy + 20], fill=GOLD, width=6); d.line([cx + 46, vy - 24, cx + 46, vy + 20], fill=GOLD, width=6)
for s in (-1, 1):
    d.rectangle([cx + s * 82 - 16, vy - 40, cx + s * 82 + 16, vy + 20], outline=MUTED, width=4)
d.line([int(S * 0.08), base + 30, int(S * 0.92), base + 30], fill=GOLD, width=5)
def centred(text, font, y, fill, spacing=0):
    if spacing:
        widths = [d.textlength(ch, font=font) for ch in text]; total = sum(widths) + spacing * (len(text) - 1)
        x = (S - total) / 2
        for ch, w in zip(text, widths):
            d.text((x, y), ch, font=font, fill=fill); x += w + spacing
    else:
        d.text(((S - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)
centred("YO TOURS", ImageFont.truetype(sans, 58), int(S * 0.05), GOLD, spacing=22)
centred("Uffizi Gallery", ImageFont.truetype(serif_b, 120), int(S * 0.64), CREAM)
centred("Florence", ImageFont.truetype(serif_i, 80), int(S * 0.76), CREAM)
d.line([S * 0.36, S * 0.862, S * 0.64, S * 0.862], fill=GOLD, width=4)
centred("Audio Guide", ImageFont.truetype(serif_i, 80), int(S * 0.88), GOLD)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static", "cover.jpg")
im.resize((800, 800), Image.LANCZOS).save(out, quality=90)
print("OK ->", os.path.abspath(out))
