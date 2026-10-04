#!/usr/bin/env python3
"""Traveller route map for the Musée de l'Orangerie V5: ONE landscape page, pictorial "Route at a glance".
Ground floor (the two oval Water Lilies rooms, each composition on its wall with its track number) and lower level (the
Walter-Guillaume collection as a path of artist rooms), the walking path in red, track numbers everywhere, minimal text.
Same house pattern as the Pitti V5.1 map. Driven by plan.json, so numbers always match the audio files.
Walls: Matin = Room 1 south (OFF); Room 2 Matin aux saules north, Matin clair aux saules south (OFF); Deux Saules east (SEC1);
the other Room 1 / Room 2 positions follow the museum's sunrise-east / sunset-west principle and are schematic."""
import json, os, sys, math
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

B = sys.argv[1]; OUT = os.path.join(B, "Orangerie_Audio_Guide_Route.pdf")
plan = json.load(open(os.path.join(B, "plan.json"))); tr = plan["tracks"]
CREAM, INK, SOFT = HexColor('#F2F1EA'), HexColor('#1F1F1F'), HexColor('#565650')
RED, RED2, EDGE = HexColor('#A4161A'), HexColor('#C9444A'), HexColor('#8E8A7C')
PANEL, FLOOR, STAIR = HexColor('#FBFAF6'), HexColor('#ECE9DF'), HexColor('#D6D2C4')
WATER, WATER2 = HexColor('#2E6E73'), HexColor('#DCEBE8')
COL = {"00_Arrival": INK, "01_Water_Lilies": WATER, "02_The_Collectors": HexColor('#A87A12'), "03_Renoir": HexColor('#B5476B'),
       "04_Cezanne": HexColor('#3F6B24'), "05_Rousseau": HexColor('#5E7D2E'), "06_Matisse": HexColor('#2F5D8A'),
       "07_Picasso": HexColor('#7A3E8E'), "08_Modigliani": HexColor('#8A5A2E'), "09_Soutine": HexColor('#A4161A'),
       "10_Derain": HexColor('#1F7A72'), "11_Finale": WATER, "12_Closing": INK}
def sec(f): return [t for t in tr if t["folder"] == f]
def rng(ts):
    s = [t["seq"] for t in ts]; return s[0] if len(s) == 1 else f"{s[0]}–{s[-1]}"
def mins(f): return max(1, round(sum(t["words"] for t in sec(f)) / 125))
def num(title_part):
    for t in tr:
        if title_part.lower() in t["title"].lower(): return t["seq"]
    raise SystemExit(f"route map: no track title contains {title_part!r}")

W, H = landscape(A4); c = canvas.Canvas(OUT, pagesize=(W, H))
c.setTitle("Musée de l'Orangerie — audio route at a glance"); c.setAuthor("Humanized Audio Guide")
c.setFillColor(CREAM); c.rect(0, 0, W, H, stroke=0, fill=1)
def text(x, y, s, font='Helvetica', size=7, col=INK, lead=None):
    c.setFillColor(col); c.setFont(font, size); lead = lead or size * 1.15
    for i, line in enumerate(s.split("\n")): c.drawCentredString(x, y - i * lead, line)
def badge(x, y, n, col, r=0.34*cm):
    c.setFillColor(col); c.setStrokeColor(CREAM); c.setLineWidth(1.2); c.circle(x, y, r, stroke=1, fill=1)
    text(x, y - 3.4, str(n), 'Times-Bold', 10.5, CREAM)
def box(x, y, w, h, col, dash=False, fill=PANEL, lw=1.3):
    c.setFillColor(fill); c.setStrokeColor(col); c.setLineWidth(lw)
    if dash: c.setDash(4, 2)
    c.roundRect(x, y, w, h, 4, stroke=1, fill=1); c.setDash()
def star(x, y, r=4.2, col=HexColor('#D9A400')):
    import math; p = c.beginPath()
    for k in range(10):
        a = math.pi/2 + k * math.pi/5; rr = r if k % 2 == 0 else r * 0.45
        (p.moveTo if k == 0 else p.lineTo)(x + rr*math.cos(a), y + rr*math.sin(a))
    p.close(); c.setFillColor(col); c.drawPath(p, stroke=0, fill=1)
def path(pts, lw=2.4, col=RED):
    c.setStrokeColor(col); c.setLineWidth(lw); c.setLineJoin(1); p = c.beginPath(); p.moveTo(*pts[0])
    for q in pts[1:]: p.lineTo(*q)
    c.drawPath(p, stroke=1, fill=0)
def arrow(x, y, d, col=RED):
    c.setFillColor(col); s = 5; p = c.beginPath()
    pts = {'r': [(x, y), (x-s, y+s*0.7), (x-s, y-s*0.7)], 'l': [(x, y), (x+s, y+s*0.7), (x+s, y-s*0.7)],
           'u': [(x, y), (x-s*0.7, y-s), (x+s*0.7, y-s)], 'd': [(x, y), (x-s*0.7, y+s), (x+s*0.7, y+s)]}[d]
    p.moveTo(*pts[0]); [p.lineTo(*q) for q in pts[1:]]; p.close(); c.drawPath(p, stroke=0, fill=1)

def icon(kind, x, y, col, s=0.62*cm):
    """Small pictogram, lower-left corner at (x, y), size s."""
    c.saveState(); c.setStrokeColor(col); c.setFillColor(col); c.setLineWidth(1.1); c.setLineJoin(1)
    if kind == "frame":       # framed painting
        c.rect(x, y, s, s*0.8, stroke=1, fill=0); c.rect(x+s*0.14, y+s*0.12, s*0.72, s*0.56, stroke=1, fill=0)
        p = c.beginPath(); p.moveTo(x+s*0.18, y+s*0.16); p.lineTo(x+s*0.42, y+s*0.48); p.lineTo(x+s*0.58, y+s*0.3); p.lineTo(x+s*0.82, y+s*0.16); c.drawPath(p, stroke=1, fill=0)
    elif kind == "easel":     # easel with canvas
        c.line(x+s*0.2, y, x+s*0.5, y+s); c.line(x+s*0.8, y, x+s*0.5, y+s); c.line(x+s*0.5, y+s*0.5, x+s*0.5, y)
        c.setFillColor(PANEL); c.rect(x+s*0.12, y+s*0.38, s*0.76, s*0.45, stroke=1, fill=1)
    elif kind == "dress":     # hanger + dress
        c.line(x+s*0.5, y+s*0.98, x+s*0.5, y+s*0.86); c.line(x+s*0.15, y+s*0.74, x+s*0.5, y+s*0.86); c.line(x+s*0.85, y+s*0.74, x+s*0.5, y+s*0.86)
        p = c.beginPath(); p.moveTo(x+s*0.35, y+s*0.74); p.lineTo(x+s*0.65, y+s*0.74); p.lineTo(x+s*0.6, y+s*0.5)
        p.lineTo(x+s*0.85, y); p.lineTo(x+s*0.15, y); p.lineTo(x+s*0.4, y+s*0.5); p.close(); c.drawPath(p, stroke=0, fill=1)
    elif kind == "crown":
        p = c.beginPath(); p.moveTo(x, y+s*0.15); p.lineTo(x, y+s*0.75); p.lineTo(x+s*0.25, y+s*0.45); p.lineTo(x+s*0.5, y+s*0.85)
        p.lineTo(x+s*0.75, y+s*0.45); p.lineTo(x+s, y+s*0.75); p.lineTo(x+s, y+s*0.15); p.close(); c.drawPath(p, stroke=0, fill=1)
    elif kind == "chapel":    # small church with a cross
        p = c.beginPath(); p.moveTo(x+s*0.1, y); p.lineTo(x+s*0.1, y+s*0.5); p.lineTo(x+s*0.5, y+s*0.78); p.lineTo(x+s*0.9, y+s*0.5)
        p.lineTo(x+s*0.9, y); p.close(); c.drawPath(p, stroke=0, fill=1)
        c.line(x+s*0.5, y+s*0.78, x+s*0.5, y+s*1.05); c.line(x+s*0.38, y+s*0.94, x+s*0.62, y+s*0.94)
        c.setFillColor(PANEL); c.rect(x+s*0.4, y, s*0.2, s*0.3, stroke=0, fill=1)
    elif kind == "tree":
        c.rect(x+s*0.44, y, s*0.12, s*0.4, stroke=0, fill=1); c.circle(x+s*0.5, y+s*0.62, s*0.32, stroke=0, fill=1)
    elif kind == "door":      # palace door
        p = c.beginPath(); p.moveTo(x+s*0.15, y); p.lineTo(x+s*0.15, y+s*0.55); p.arcTo(x+s*0.15, y+s*0.25, x+s*0.85, y+s*0.95, 180, -180)
        p.lineTo(x+s*0.85, y); c.drawPath(p, stroke=1, fill=0); c.line(x+s*0.5, y, x+s*0.5, y+s*0.9)
    c.restoreState()
def flag(x, y, label, col):
    c.setFillColor(col); c.roundRect(x, y, 1.55*cm, 0.5*cm, 3, stroke=0, fill=1); text(x + 0.775*cm, y + 0.16*cm, label, 'Helvetica-Bold', 7.5, CREAM)


def star(x, y, r=4.2, col=HexColor('#D9A400')):
    p = c.beginPath()
    for k in range(10):
        a = math.pi/2 + k * math.pi/5; rr = r if k % 2 == 0 else r * 0.45
        (p.moveTo if k == 0 else p.lineTo)(x + rr*math.cos(a), y + rr*math.sin(a))
    p.close(); c.setFillColor(col); c.drawPath(p, stroke=0, fill=1)
def flag(x, y, label, col):
    c.setFillColor(col); c.roundRect(x, y, 1.55*cm, 0.5*cm, 3, stroke=0, fill=1); text(x + 0.775*cm, y + 0.16*cm, label, 'Helvetica-Bold', 7.5, CREAM)

# title strip
c.setFillColor(INK); c.rect(0, H - 1.7*cm, W, 1.7*cm, stroke=0, fill=1)
c.setFillColor(CREAM); c.setFont('Times-Bold', 20); c.drawString(1.2*cm, H - 1.15*cm, "MUSÉE DE L'ORANGERIE")
c.setFillColor(RED2); c.setFont('Times-Italic', 12); c.drawString(12.3*cm, H - 1.15*cm, "audio route at a glance")
c.setFont('Times-Italic', 11); c.drawRightString(W - 1.2*cm, H - 1.15*cm, f"{len(tr)} tracks · about {plan['total_min'] // 60} h {plan['total_min'] % 60:02d} min")

# ── GROUND FLOOR band
GX, GY, GW, GH = 1.2*cm, 9.6*cm, W - 2.4*cm, 8.6*cm
c.setFillColor(FLOOR); c.setStrokeColor(EDGE); c.setLineWidth(0.6); c.roundRect(GX, GY, GW, GH, 4, stroke=1, fill=1)
c.saveState(); c.translate(GX - 0.38*cm, GY + GH/2); c.rotate(90); text(0, 0, "GROUND FLOOR", 'Helvetica-Bold', 7, SOFT); c.restoreState()
text(GX + GW/2, GY + GH + 0.15*cm, "Tuileries garden (north)", 'Helvetica-Oblique', 6.8, SOFT)
text(GX + GW/2, GY - 0.38*cm, "Seine side (south)", 'Helvetica-Oblique', 6.8, SOFT)
# arrival + vestibule (west, Concorde side)
ax, ay = GX + 0.4*cm, GY + 1.0*cm
box(ax, ay, 3.6*cm, 5.4*cm, INK)
text(ax + 1.8*cm, ay + 4.75*cm, "Arrival &\nentrance hall", 'Times-Bold', 10, INK)
text(ax + 1.8*cm, ay + 3.35*cm, rng(sec("00_Arrival")), 'Helvetica-Bold', 11, INK)
text(ax + 1.8*cm, ay + 2.8*cm, f"{mins('00_Arrival')} min", 'Helvetica', 6.6, SOFT)
badge(ax + 0.05*cm, ay + 5.4*cm, 1, INK); flag(ax + 1.0*cm, ay + 5.15*cm, "START", RED)
# stairs block inside the hall
c.setFillColor(STAIR); c.rect(ax + 0.35*cm, ay + 0.35*cm, 2.9*cm, 1.6*cm, stroke=0, fill=1)
c.setStrokeColor(HexColor('#B9B4A3')); c.setLineWidth(0.5)
for i in range(6): c.line(ax + 0.55*cm + i*0.45*cm, ay + 0.5*cm, ax + 0.55*cm + i*0.45*cm, ay + 1.8*cm)
text(ax + 1.8*cm, ay + 1.0*cm, "stairs & lift", 'Helvetica-Bold', 6.3, SOFT)
text(ax - 0.1*cm, GY + GH - 0.5*cm, "", 'Helvetica', 6)
# the two ovals
def oval(cx, cy, rx, ry, label, step, centre, walls):
    c.setFillColor(WATER2); c.setStrokeColor(WATER); c.setLineWidth(1.6); c.ellipse(cx - rx, cy - ry, cx + rx, cy + ry, stroke=1, fill=1)
    text(cx, cy + 0.35*cm, label, 'Times-Bold', 10, WATER); text(cx, cy - 0.25*cm, centre, 'Helvetica-Bold', 8.5, WATER)
    badge(cx - rx + 0.25*cm, cy + ry - 0.25*cm, step, WATER)
    for (ang, n, name, st, below) in walls:
        a = math.radians(ang); px, py = cx + rx*math.cos(a), cy + ry*math.sin(a)
        c.setFillColor(CREAM); c.setStrokeColor(WATER); c.setLineWidth(1.4); c.circle(px, py, 0.38*cm, stroke=1, fill=1)
        text(px, py - 2.6, n, 'Helvetica-Bold', 7, WATER)
        ox, oy = math.cos(a), math.sin(a)
        lx, ly = px + ox*0.95*cm, py + oy*0.62*cm
        c.setFillColor(INK); c.setFont('Helvetica', 6.6)
        lines = name.split("\n")
        if below:
            text(px, py - 0.7*cm, name, 'Helvetica', 6.6, INK, lead=7.4)
            if st: star(px + 0.34*cm, py + 0.3*cm)
            continue
        for k, line in enumerate(lines):
            yy = ly - 2.2 - k*7.4 + (3.7 if len(lines) > 1 else 0)
            if abs(ox) < 0.3: c.drawCentredString(lx, yy if oy < 0 else yy + 2, line)
            elif ox > 0: c.drawString(px + 0.5*cm, yy, line)
            else: c.drawRightString(px - 0.5*cm, yy, line)
        if st: star(px + 0.34*cm, py + 0.3*cm)
r1x, r2x, ocy, rx, ry = GX + 8.3*cm, GX + 18.9*cm, GY + GH/2 - 0.1*cm, 3.6*cm, 2.55*cm
oval(r1x, ocy, rx, ry, "Room 1", 2, num("Inside the infinity") if any("infinity" in t["title"].lower() for t in tr) else sec("01_Water_Lilies")[0]["seq"], [
    (207, num("Setting Sun"), "Setting Sun", False, True), (90, num("Clouds"), "Clouds", False, False),
    (28, num("Green Reflections"), "Green\nReflections", False, False), (270, num("Matin (Morning)") if any("matin (morning)" in t["title"].lower() for t in tr) else num("Morning"), "Morning", True, False)])
oval(r2x, ocy, rx, ry, "Room 2", 3, sec("01_Water_Lilies")[5]["seq"] + " · bench " + num("last years"), [
    (207, num("Reflections of Trees"), "Reflections\nof Trees", False, True), (90, num("Morning with Willows"), "Morning with\nWillows", False, False),
    (270, num("Clear Morning"), "Clear Morning\nwith Willows", False, False), (0, num("Two Willows"), "The Two\nWillows", True, False)])
c.setFillColor(WATER2); c.setStrokeColor(WATER); c.setLineWidth(1.6)
c.rect(r1x + rx - 0.05*cm, ocy - 0.45*cm, r2x - r1x - 2*rx + 0.1*cm, 0.9*cm, stroke=0, fill=1)
c.line(r1x + rx, ocy + 0.45*cm, r2x - rx, ocy + 0.45*cm); c.line(r1x + rx, ocy - 0.45*cm, r2x - rx, ocy - 0.45*cm)
text((r1x + r2x)/2, ocy - 0.12*cm, "passage", 'Helvetica-Oblique', 6.2, WATER)
text((r1x + r2x)/2, GY + 0.45*cm, f"Water Lilies {rng(sec('01_Water_Lilies'))}  ·  {mins('01_Water_Lilies')} min  ·  back through Room 1: {num('Hidden')}", 'Helvetica-Bold', 7.2, WATER)
# exit (north side) + finale
ex, ey = (r1x + r2x)/2 - 0.6*cm, GY + GH - 0.95*cm
flag(ex + 2.6*cm, ey + 0.05*cm, "FINISH", INK)
c.setFillColor(INK); c.roundRect(ex - 1.3*cm, ey - 0.05*cm, 3.75*cm, 0.62*cm, 3, stroke=0, fill=1)
text(ex + 0.57*cm, ey + 0.13*cm, f"Exit to the garden · {rng(sec('12_Closing'))}", 'Helvetica-Bold', 7, CREAM)
text(ex + 0.6*cm, ey - 0.45*cm, f"{rng(sec('11_Finale'))}: one last look at the lilies first", 'Helvetica-Oblique', 6.6, WATER)

# ── LOWER LEVEL band
LX, LY, LW, LH = 1.2*cm, 1.25*cm, W - 2.4*cm, 7.5*cm
c.setFillColor(FLOOR); c.setStrokeColor(EDGE); c.setLineWidth(0.6); c.roundRect(LX, LY, LW, LH, 4, stroke=1, fill=1)
c.saveState(); c.translate(LX - 0.38*cm, LY + LH/2); c.rotate(90); text(0, 0, "LOWER LEVEL", 'Helvetica-Bold', 7, SOFT); c.restoreState()
text(LX + LW/2, LY + LH - 0.55*cm, "The Walter-Guillaume collection · rooms by artist: follow the names on the walls (order may vary)", 'Helvetica-Oblique', 7, SOFT)
ROOMS = [("02_The_Collectors", "The collectors", 4), ("03_Renoir", "Renoir", 5), ("04_Cezanne", "Cézanne", 6), ("05_Rousseau", "Henri Rousseau", 7),
         ("06_Matisse", "Matisse", 8), ("07_Picasso", "Picasso", 9), ("08_Modigliani", "Modigliani", 10), ("09_Soutine", "Soutine", 11),
         ("10_Derain", "Derain", 12)]
per = 5; bw, bh = 4.5*cm, 2.35*cm; gapx = (LW - 0.8*cm - per*bw) / (per - 1)
pos = []
for i, (fo, name, step) in enumerate(ROOMS):
    row, col = divmod(i, per)
    if row == 1: col = per - 1 - col
    x = LX + 0.4*cm + col*(bw + gapx); y = LY + LH - 1.1*cm - bh - row*(bh + 0.95*cm)
    pos.append((x, y))
    k = COL[fo]; box(x, y, bw, bh, k)
    text(x + bw/2, y + bh - 0.62*cm, name, 'Times-Bold', 10.5, k)
    text(x + bw/2, y + 0.95*cm, rng(sec(fo)), 'Helvetica-Bold', 11, k)
    text(x + bw/2, y + 0.4*cm, f"{mins(fo)} min", 'Helvetica', 6.6, SOFT)
    badge(x + 0.05*cm, y + bh, step, k)
for i in range(len(pos) - 1):
    (x1, y1), (x2, y2) = pos[i], pos[i+1]
    if abs(y1 - y2) < 1:
        ym = y1 + bh/2
        if x2 > x1: path([(x1 + bw, ym), (x2, ym)]); arrow(x2, ym, 'r')
        else: path([(x1, ym), (x2 + bw, ym)]); arrow(x2 + bw, ym, 'l')
    else:
        xm = x1 + bw/2; path([(xm, y1), (xm, y2 + bh)]); arrow(xm, y2 + bh, 'd')
# stairs link between levels (left) and the way back up after Derain
sx = ax + 1.8*cm
path([(sx, ay + 0.35*cm), (sx, pos[0][1] + bh + 0.55*cm), (pos[0][0] + bw/2, pos[0][1] + bh + 0.55*cm), (pos[0][0] + bw/2, pos[0][1] + bh)], 2.0)
arrow(pos[0][0] + bw/2, pos[0][1] + bh, 'd')
lx, ly = pos[-1]
path([(lx, ly + bh/2), (LX + 0.25*cm, ly + bh/2), (LX + 0.25*cm, ay + 0.7*cm), (ax, ay + 0.7*cm)], 1.6)
arrow(ax, ay + 0.7*cm, 'r')
text(LX + 1.6*cm, ly + bh/2 + 0.15*cm, "back up", 'Helvetica-Oblique', 6.3, RED)
# ground-floor path: hall -> Room 1 -> Room 2 -> back
path([(ax + 3.6*cm, ocy), (r1x - rx, ocy)]); arrow(r1x - rx, ocy, 'r')
# key
ky = 0.42*cm; kx = LX
c.setStrokeColor(RED); c.setLineWidth(2.4); c.line(kx, ky + 3, kx + 0.8*cm, ky + 3); arrow(kx + 0.85*cm, ky + 3, 'r')
c.setFillColor(SOFT); c.setFont('Helvetica', 7); c.drawString(kx + 1.05*cm, ky, "your route"); kx += 3.0*cm
badge(kx + 0.2*cm, ky + 3, 2, WATER, r=0.22*cm); c.setFillColor(SOFT); c.setFont('Helvetica', 7); c.drawString(kx + 0.55*cm, ky, "step"); kx += 1.9*cm
c.setFillColor(WATER); c.setFont('Helvetica-Bold', 7.5); c.drawString(kx, ky, "005"); c.setFillColor(SOFT); c.setFont('Helvetica', 7); c.drawString(kx + 0.7*cm, ky, "track to play there"); kx += 3.8*cm
star(kx + 0.15*cm, ky + 3); c.setFillColor(SOFT); c.drawString(kx + 0.45*cm, ky, "don't miss"); kx += 2.4*cm
c.drawString(kx, ky, "Water Lilies positions are schematic; Morning is on the Seine side.")
c.showPage(); c.save(); print("built", OUT)
