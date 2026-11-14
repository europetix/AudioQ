#!/usr/bin/env python3
"""Album cover for the Barcelona Cathedral audio guide (Yo Tours). Run once; output: ../static/cover.jpg.
Original artwork: an abstract Gothic silhouette made of simple geometry (a tall pointed arch with a few panes of
stained-glass colour, two slim spires either side and a taller one behind, like a lantern tower), a strip of water at
its foot with a small goose shape (the cloister's geese), and type. No logo, no photograph, no artwork reproduced or
traced; the shapes are our own and not the cathedral's real outline."""
import math, os, random
from PIL import Image, ImageDraw, ImageFont
S = 1600
INK, CREAM, GOLD, STONE, STONE_D = (20, 26, 40), (244, 237, 222), (214, 170, 82), (64, 70, 86), (44, 50, 66)
GLASS = [(30, 70, 150), (170, 40, 48), (214, 170, 82), (46, 120, 96), (110, 60, 140), (40, 110, 170)]
F = "/usr/share/fonts/truetype/dejavu/"
serif_b, serif_i, sans = F + "DejaVuSerif-Bold.ttf", F + "DejaVuSerif-Italic.ttf", F + "DejaVuSans.ttf"
rnd = random.Random(1448)
im = Image.new("RGB", (S, S), INK); d = ImageDraw.Draw(im)


def pointed_arch(cx, base, w, h, steps=40):
    """A pointed (two-centred) Gothic arch: straight sides up to the springing line, then two arcs meeting at the top."""
    r = w                                  # equilateral arch: each arc's radius = the arch's width
    spring = base - (h - r * math.sin(math.acos(.5)))
    left = [(cx - w / 2, base), (cx - w / 2, spring)]
    arc_l = [(cx + w / 2 - r * math.cos(a), spring - r * math.sin(a)) for a in [k / steps * math.pi / 3 for k in range(steps + 1)]]
    arc_r = [(cx - w / 2 + r * math.cos(a), spring - r * math.sin(a)) for a in [(steps - k) / steps * math.pi / 3 for k in range(steps + 1)]]
    return left + arc_l + arc_r + [(cx + w / 2, spring), (cx + w / 2, base)]


def spire(cx, base, w, top, colour):
    """A slim tower with a pointed roof and a few small crockets (little bumps) up its edges."""
    shaft_top = top + (base - top) * .42
    d.rectangle([cx - w / 2, shaft_top, cx + w / 2, base], fill=colour)
    d.polygon([(cx - w / 2 - 6, shaft_top), (cx, top), (cx + w / 2 + 6, shaft_top)], fill=colour)
    for k in range(1, 5):
        t = k / 5; y = shaft_top - (shaft_top - top) * t; hw = (w / 2 + 6) * (1 - t)
        for sgn in (-1, 1):
            d.ellipse([cx + sgn * hw - 5, y - 5, cx + sgn * hw + 5, y + 5], fill=colour)
    d.line([(cx, top - 26), (cx, top)], fill=GOLD, width=5)
    d.line([(cx - 11, top - 16), (cx + 11, top - 16)], fill=GOLD, width=5)
    for k in range(3):                     # tall slit windows
        y = shaft_top + 40 + k * 70
        if y + 46 < base:
            d.polygon(pointed_arch(cx, y + 46, 14, 46, 8), fill=INK)


base = int(S * 0.585)
# the tall one behind (the lantern-tower idea), then the two flanking spires
spire(S * .5, base - 40, 92, int(S * .105), STONE_D)
spire(S * .24, base, 70, int(S * .17), STONE)
spire(S * .76, base, 70, int(S * .17), STONE)
# the front: a block of stone with a great pointed arch in the middle
d.rectangle([S * .29, S * .30, S * .71, base], fill=STONE)
d.polygon([(S * .29, S * .30), (S * .5, S * .21), (S * .71, S * .30)], fill=STONE)          # a gable
arch = pointed_arch(S * .5, base, S * .26, S * .27)
d.polygon(arch, fill=INK)
# stained glass inside the arch: small coloured panes in a lattice, clipped to the arch
glass = Image.new("RGB", (S, S), INK); g = ImageDraw.Draw(glass)
pane = 34
for yy in range(int(S * .30), base, pane):
    for xx in range(int(S * .36), int(S * .64), pane):
        if rnd.random() < .82:
            g.rectangle([xx + 3, yy + 3, xx + pane - 3, yy + pane - 3], fill=rnd.choice(GLASS))
rose_c, rose_r = (S * .5, S * .405), S * .06                                                 # a round window high in the arch
g.ellipse([rose_c[0] - rose_r, rose_c[1] - rose_r, rose_c[0] + rose_r, rose_c[1] + rose_r], fill=INK)
for k in range(12):
    a = k / 12 * math.tau
    g.polygon([rose_c, (rose_c[0] + rose_r * .92 * math.cos(a - .2), rose_c[1] + rose_r * .92 * math.sin(a - .2)),
               (rose_c[0] + rose_r * .92 * math.cos(a + .2), rose_c[1] + rose_r * .92 * math.sin(a + .2))], fill=GLASS[k % len(GLASS)])
g.ellipse([rose_c[0] - 12, rose_c[1] - 12, rose_c[0] + 12, rose_c[1] + 12], fill=GOLD)
mask = Image.new("L", (S, S), 0); ImageDraw.Draw(mask).polygon(pointed_arch(S * .5, base - 18, S * .26 - 36, S * .27 - 30), fill=255)
im.paste(glass, (0, 0), mask); d = ImageDraw.Draw(im)
d.line([(S * .5, S * .47), (S * .5, base - 18)], fill=INK, width=8)                           # a central mullion
d.line(arch, fill=GOLD, width=4)
# the water at the foot, and a small goose
d.rectangle([0, base, S, base + 70], fill=(30, 52, 78))
for k in range(9):
    x0 = 90 + k * 170 + rnd.randint(-20, 20); y0 = base + 22 + (k % 3) * 14
    d.arc([x0, y0, x0 + 90, y0 + 18], 200, 340, fill=(90, 130, 170), width=3)
gx, gy = S * .62, base + 18                                                                     # the goose, facing left
d.ellipse([gx - 34, gy - 4, gx + 34, gy + 26], fill=CREAM)                                     # body
d.polygon([(gx + 26, gy + 2), (gx + 52, gy - 10), (gx + 34, gy + 14)], fill=CREAM)              # tail
d.line([(gx - 22, gy + 4), (gx - 30, gy - 40)], fill=CREAM, width=12)                         # neck
d.ellipse([gx - 42, gy - 54, gx - 18, gy - 32], fill=CREAM)                                    # head
d.polygon([(gx - 40, gy - 46), (gx - 60, gy - 40), (gx - 40, gy - 38)], fill=(222, 140, 50))   # beak
d.ellipse([gx - 34, gy - 48, gx - 29, gy - 43], fill=INK)                                      # eye


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


centred("YO TOURS", ImageFont.truetype(sans, 58), int(S * 0.025), GOLD, spacing=22)
centred("Barcelona Cathedral", fit(serif_b, "Barcelona Cathedral", 124, S * .9), int(S * 0.68), CREAM)
d.line([S * .36, S * .81, S * .64, S * .81], fill=GOLD, width=4)
centred("Yo Tours audio guide", ImageFont.truetype(serif_i, 76), int(S * 0.84), GOLD)
centred("Barcelona", ImageFont.truetype(sans, 44), int(S * 0.925), CREAM, spacing=10)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static", "cover.jpg")
im.resize((800, 800), Image.LANCZOS).save(out, quality=90)
print("OK ->", os.path.abspath(out))
