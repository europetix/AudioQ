#!/usr/bin/env python3
"""Album cover for the Palazzo Pitti + Boboli audio guide (Yo Tours), shown by phone music players. Run once; output: ../static/cover.jpg.
Original artwork: a generic arched window in rusticated stone, and type. No museum logo."""
import math, os
from PIL import Image, ImageDraw, ImageFont
S = 1600                                      # drawn large, saved at 800 px for smooth edges
INK, GOLD, CREAM, MUTED = (24, 30, 44), (201, 165, 92), (243, 236, 222), (150, 140, 120)
F = "/usr/share/fonts/truetype/dejavu/"
serif_b, serif_i, sans = F + "DejaVuSerif-Bold.ttf", F + "DejaVuSerif-Italic.ttf", F + "DejaVuSans.ttf"
im = Image.new("RGB", (S, S), INK); d = ImageDraw.Draw(im)
cx, cy = S // 2, int(S * 0.40)
# a generic rusticated arched window (the palace's facade is built of rough stone blocks); original drawing, no logo
w, h = int(S * 0.30), int(S * 0.40); x0, y0 = cx - w // 2, cy - h // 2 + 40
for row in range(7):                               # stone courses around the window
    y = y0 - 70 + row * 92
    for col in range(-1, 4):
        off = 0 if row % 2 else 60
        bx = cx - w // 2 - 170 + col * 190 + off
        d.rounded_rectangle([bx, y, bx + 170, y + 78], radius=10, outline=MUTED, width=3)
d.rectangle([x0 - 14, y0 + w // 2 - 14, x0 + w + 14, y0 + h + 14], fill=INK)
d.pieslice([x0 - 14, y0 - 14, x0 + w + 14, y0 + w + 14], 180, 360, fill=INK)
d.rectangle([x0, y0 + w // 2, x0 + w, y0 + h], outline=GOLD, width=10)
d.arc([x0, y0, x0 + w, y0 + w], 180, 360, fill=GOLD, width=10)
d.line([x0, y0 + w // 2, x0 + w, y0 + w // 2], fill=INK, width=12)
for k in range(1, 3):                              # window bars
    d.line([x0 + k * w // 3, y0 + w // 2, x0 + k * w // 3, y0 + h], fill=MUTED, width=4)
d.line([x0, y0 + w // 2 + (h - w // 2) // 2, x0 + w, y0 + w // 2 + (h - w // 2) // 2], fill=MUTED, width=4)
d.line([cx, y0, cx, y0 + w // 2], fill=MUTED, width=4)
def centred(text, font, y, fill, spacing=0):
    if spacing:
        widths = [d.textlength(ch, font=font) for ch in text]; total = sum(widths) + spacing * (len(text) - 1)
        x = (S - total) / 2
        for ch, w in zip(text, widths):
            d.text((x, y), ch, font=font, fill=fill); x += w + spacing
    else:
        d.text(((S - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)
centred("YO TOURS", ImageFont.truetype(sans, 58), int(S * 0.06), GOLD, spacing=22)
centred("Palazzo Pitti", ImageFont.truetype(serif_b, 150), int(S * 0.69), CREAM)
centred("& Boboli", ImageFont.truetype(serif_i, 80), int(S * 0.785), CREAM)
d.line([S * 0.36, S * 0.862, S * 0.64, S * 0.862], fill=GOLD, width=4)
centred("Audio Guide", ImageFont.truetype(serif_i, 80), int(S * 0.88), GOLD)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static", "cover.jpg")
im.resize((800, 800), Image.LANCZOS).save(out, "JPEG", quality=88, optimize=True)
print("cover ->", os.path.normpath(out), os.path.getsize(out), "bytes")
