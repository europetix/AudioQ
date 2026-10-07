#!/usr/bin/env python3
"""Album cover for the Orsay audio guide (Yo Tours), shown by phone music players. Run once; output: ../static/cover.jpg.
Original artwork: a generic clock face (the guide begins and ends at the old station's clocks) and type. No museum logo."""
import math, os
from PIL import Image, ImageDraw, ImageFont
S = 1600                                      # drawn large, saved at 800 px for smooth edges
INK, GOLD, CREAM, MUTED = (24, 30, 44), (201, 165, 92), (243, 236, 222), (150, 140, 120)
F = "/usr/share/fonts/truetype/dejavu/"
serif_b, serif_i, sans = F + "DejaVuSerif-Bold.ttf", F + "DejaVuSerif-Italic.ttf", F + "DejaVuSans.ttf"
im = Image.new("RGB", (S, S), INK); d = ImageDraw.Draw(im)
cx, cy, r = S // 2, int(S * 0.40), int(S * 0.23)
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=GOLD, width=10)
d.ellipse([cx - r + 34, cy - r + 34, cx + r - 34, cy + r - 34], outline=MUTED, width=3)
for k in range(60):                            # minute and hour ticks
    a = math.radians(k * 6); long = k % 5 == 0
    r1, r2 = r - 46, r - (100 if long else 66)
    d.line([cx + r1 * math.sin(a), cy - r1 * math.cos(a), cx + r2 * math.sin(a), cy - r2 * math.cos(a)],
           fill=GOLD if long else MUTED, width=9 if long else 3)
for ang, ln, w in ((300, 0.50, 16), (60, 0.72, 10)):   # hands at ten to two
    a = math.radians(ang)
    d.line([cx, cy, cx + r * ln * math.sin(a), cy - r * ln * math.cos(a)], fill=CREAM, width=w)
d.ellipse([cx - 20, cy - 20, cx + 20, cy + 20], fill=GOLD)
def centred(text, font, y, fill, spacing=0):
    if spacing:
        widths = [d.textlength(ch, font=font) for ch in text]; total = sum(widths) + spacing * (len(text) - 1)
        x = (S - total) / 2
        for ch, w in zip(text, widths):
            d.text((x, y), ch, font=font, fill=fill); x += w + spacing
    else:
        d.text(((S - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)
centred("YO TOURS", ImageFont.truetype(sans, 58), int(S * 0.06), GOLD, spacing=22)
centred("Musée d'Orsay", ImageFont.truetype(serif_b, 150), int(S * 0.70), CREAM)
d.line([S * 0.36, S * 0.825, S * 0.64, S * 0.825], fill=GOLD, width=4)
centred("Audio Guide", ImageFont.truetype(serif_i, 92), int(S * 0.85), GOLD)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static", "cover.jpg")
im.resize((800, 800), Image.LANCZOS).save(out, "JPEG", quality=88, optimize=True)
print("cover ->", os.path.normpath(out), os.path.getsize(out), "bytes")
