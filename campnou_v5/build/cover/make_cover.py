#!/usr/bin/env python3
"""Album cover for the FC Barcelona Museum · Spotify Camp Nou audio guide (Yo Tours). Run once; output: ../static/cover.jpg.
Original, abstract artwork: vertical blue and claret stripes (the club's colours as plain stripes), crossed by the
curve of a stadium bowl seen from above the rim (three tiers of white arcs, the top one left open like a ring still
being built), a pitch-green sliver at the bottom of the bowl, and type. No crest, no logo, no players, no photograph,
no sponsor's name; the shapes are our own and not the stadium's real outline."""
import math, os
from PIL import Image, ImageDraw, ImageFont
S = 1600
NAVY, BLUE, CLARET, CREAM, GOLD, GRASS = (14, 22, 48), (28, 62, 140), (150, 18, 62), (244, 237, 222), (226, 180, 72), (52, 120, 74)
F = "/usr/share/fonts/truetype/dejavu/"
serif_b, serif_i, sans = F + "DejaVuSerif-Bold.ttf", F + "DejaVuSerif-Italic.ttf", F + "DejaVuSans.ttf"
im = Image.new("RGB", (S, S), NAVY)

# the stripes: a field of equal vertical bands, blue and claret, in the upper two thirds
TOP, BOT = 0, int(S * 0.68)
band = S / 11
st = Image.new("RGB", (S, S), NAVY); g = ImageDraw.Draw(st)
for k in range(11):
    g.rectangle([k * band, TOP, (k + 1) * band, BOT], fill=BLUE if k % 2 == 0 else CLARET)
# a soft darkening towards the bottom of the stripes, so the bowl reads
shade = Image.new("L", (S, S), 0); sd = ImageDraw.Draw(shade)
for y in range(TOP, BOT):
    sd.line([(0, y), (S, y)], fill=int(170 * max(0, (y - S * .22) / (BOT - S * .22)) ** 1.5))
im.paste(st, (0, 0)); im.paste(Image.new("RGB", (S, S), NAVY), (0, 0), shade)
d = ImageDraw.Draw(im)


def ell(cx, cy, rx, ry, a0, a1, n=180):
    return [(cx + rx * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + ry * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]


# the bowl: three tiers as wide flat ellipses, the near half of each hidden under the next, seen from just above the rim
cx, cy = S / 2, S * 0.47
d.polygon(ell(cx, cy, S * .27, S * .055, 0, 360), fill=GRASS)                      # the pitch, far below
for i in range(1, 4):
    d.line(ell(cx, cy + 3, S * .27 - i * 22, S * .055 - i * 4, 200, 340, 60), fill=(98, 160, 110), width=3)
TIERS = [(S * .33, S * .085, 7), (S * .40, S * .125, 9), (S * .47, S * .17, 11)]
for j, (rx, ry, w) in enumerate(TIERS):
    pts = ell(cx, cy - j * 4, rx, ry, 180, 360)                                     # the far half of each tier
    d.line(pts, fill=CREAM, width=w, joint="curve")
    for a in range(186, 360, 9 - j):                                               # seat rows as short ticks
        p = ell(cx, cy - j * 4, rx, ry, a, a, 1)[0]; q = ell(cx, cy - j * 4, rx - 26, ry - 9, a, a, 1)[0]
        d.line([p, q], fill=(200, 196, 190), width=2)
# the rim still being built: the top ring drawn open, with a gap and a few dashes
rx, ry = S * .52, S * .205
for a0 in range(184, 356, 12):
    if 262 < a0 < 290:
        continue                                                                   # the gap in the ring
    d.line(ell(cx, cy - 16, rx, ry, a0, a0 + 7, 10), fill=GOLD, width=10)
# the near side of the bowl: a dark sweep closing the curve at the bottom of the stripes
d.polygon(ell(cx, cy, S * .56, S * .16, 0, 180) + [(0, S), (S, S)], fill=NAVY)
d.line(ell(cx, cy, S * .56, S * .16, 4, 176), fill=CREAM, width=6)


def centred(text, font, y, fill, spacing=0):
    if spacing:
        widths = [d.textlength(ch, font=font) for ch in text]; total = sum(widths) + spacing * (len(text) - 1)
        x = (S - total) / 2
        for ch, ww in zip(text, widths):
            d.text((x, y), ch, font=font, fill=fill); x += ww + spacing
    else:
        d.text(((S - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)


def fit(path, text, size, maxw):
    f = ImageFont.truetype(path, size)
    while d.textlength(text, font=f) > maxw:
        size -= 4; f = ImageFont.truetype(path, size)
    return f


d.rectangle([S * .31, S * .015, S * .69, S * .085], fill=NAVY)
centred("YO TOURS", ImageFont.truetype(sans, 58), int(S * 0.025), GOLD, spacing=22)
centred("FC Barcelona Museum", fit(serif_b, "FC Barcelona Museum", 124, S * .9), int(S * 0.72), CREAM)
d.line([S * .36, S * .835, S * .64, S * .835], fill=GOLD, width=4)
centred("Yo Tours audio guide", ImageFont.truetype(serif_i, 76), int(S * 0.855), GOLD)
centred("Camp Nou · Barcelona", ImageFont.truetype(sans, 44), int(S * 0.935), CREAM, spacing=8)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static", "cover.jpg")
im.resize((800, 800), Image.LANCZOS).save(out, quality=90)
print("OK ->", os.path.abspath(out))
