#!/usr/bin/env python3
"""Album cover for the Park Güell (Barcelona) audio guide (Yo Tours). Run once; output: ../static/cover.jpg.
Original artwork: an abstract wavy band of broken-tile pieces (the idea of a tiled bench seen from the front) and the
outline of a gatehouse tower with a chequered top, in broken-tile colours; and type. No logo, no photograph, no artwork
reproduced or traced."""
import math, os, random
from PIL import Image, ImageDraw, ImageFont
S = 1600
INK, CREAM, GOLD = (22, 34, 46), (244, 237, 222), (214, 170, 82)
TILE = [(28, 104, 168), (52, 150, 190), (236, 196, 58), (222, 120, 46), (196, 58, 52), (86, 152, 84), (240, 236, 224), (150, 196, 214)]
F = "/usr/share/fonts/truetype/dejavu/"
serif_b, serif_i, sans = F + "DejaVuSerif-Bold.ttf", F + "DejaVuSerif-Italic.ttf", F + "DejaVuSans.ttf"
rnd = random.Random(1926)
im = Image.new("RGB", (S, S), INK); d = ImageDraw.Draw(im)


def shard(cx, cy, r, colour):
    """One irregular broken-tile piece: a random 4-6 sided polygon round (cx, cy)."""
    n = rnd.randint(4, 6); a0 = rnd.random() * math.tau
    pts = [(cx + r * (.55 + .45 * rnd.random()) * math.cos(a0 + k * math.tau / n + rnd.uniform(-.3, .3)),
            cy + r * (.55 + .45 * rnd.random()) * math.sin(a0 + k * math.tau / n + rnd.uniform(-.3, .3))) for k in range(n)]
    d.polygon(pts, fill=colour)


# the gatehouse tower: a tapering shaft with a chequered top and a small four-armed finial (simple geometry, our own)
tx, base = int(S * 0.70), int(S * 0.56)
shaft = [(tx - 70, base), (tx - 48, int(S * 0.24)), (tx + 48, int(S * 0.24)), (tx + 70, base)]
d.polygon(shaft, fill=(58, 72, 86))
for row in range(6):                                              # chequered band near the top
    y0 = int(S * 0.24) + row * 22
    for col in range(5):
        if (row + col) % 2 == 0:
            x0 = tx - 46 + col * 19
            d.rectangle([x0, y0, x0 + 18, y0 + 21], fill=TILE[0] if row % 3 else TILE[6])
d.polygon([(tx - 48, int(S * 0.24)), (tx, int(S * 0.16)), (tx + 48, int(S * 0.24))], fill=TILE[1])   # the spire
for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):                 # a small four-armed finial
    d.rectangle([tx - 7 + dx * 16, int(S * 0.135) - 7 + dy * 16, tx + 7 + dx * 16, int(S * 0.135) + 7 + dy * 16], fill=GOLD)
d.rectangle([tx - 7, int(S * 0.135) - 7, tx + 7, int(S * 0.135) + 7], fill=GOLD)
for k in range(3):                                                # windows
    y = int(S * 0.36) + k * 50
    d.rounded_rectangle([tx - 10, y, tx + 10, y + 30], radius=10, fill=INK)

# the wavy band of broken tile, in front of the tower
def wave_y(x): return base + 34 * math.sin(x / S * math.tau * 2.2 + .6)
x = -20
while x < S + 20:
    yc = wave_y(x)
    for layer in range(4):
        shard(x + rnd.uniform(-6, 6), yc - 52 + layer * 34 + rnd.uniform(-6, 6), rnd.uniform(16, 24), rnd.choice(TILE))
    x += rnd.uniform(22, 30)
for xx in range(0, S, 4):                                         # a cream top edge, like a bench's rounded rim
    d.ellipse([xx - 4, wave_y(xx) - 74, xx + 4, wave_y(xx) - 66], fill=CREAM)


def centred(text, font, y, fill, spacing=0):
    if spacing:
        widths = [d.textlength(ch, font=font) for ch in text]; total = sum(widths) + spacing * (len(text) - 1)
        x = (S - total) / 2
        for ch, ww in zip(text, widths):
            d.text((x, y), ch, font=font, fill=fill); x += ww + spacing
    else:
        d.text(((S - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)


centred("YO TOURS", ImageFont.truetype(sans, 58), int(S * 0.05), GOLD, spacing=22)
centred("Park Güell", ImageFont.truetype(serif_b, 128), int(S * 0.68), CREAM)
d.line([S * 0.36, S * 0.81, S * 0.64, S * 0.81], fill=GOLD, width=4)
centred("Yo Tours audio guide", ImageFont.truetype(serif_i, 76), int(S * 0.84), GOLD)
centred("Barcelona", ImageFont.truetype(sans, 44), int(S * 0.925), CREAM, spacing=10)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static", "cover.jpg")
im.resize((800, 800), Image.LANCZOS).save(out, quality=90)
print("OK ->", os.path.abspath(out))
