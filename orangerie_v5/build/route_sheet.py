#!/usr/bin/env python3
"""Traveller route map for Tour #43 (V5.1): ONE landscape page, pictorial "Route at a glance".
Palace cross-section (ground / first / second floor) + Boboli garden, the walking path in red, each section in its
own colour with a small pictogram, every room or stop with its track numbers, START / FINISH, highlight stars and
minutes per section. House palette from the Tour #49 route-map pattern. Driven by plan.json, so the track numbers
always match the audio files. Deliberately almost no text."""
import json, os, sys
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

B = sys.argv[1]; OUT = os.path.join(B, "Palazzo_Pitti_Audio_Guide_Route.pdf")
plan = json.load(open(os.path.join(B, "plan.json"))); tr = plan["tracks"]
CREAM, INK, SOFT = HexColor('#F2F1EA'), HexColor('#1F1F1F'), HexColor('#565650')
RED, RED2, EDGE = HexColor('#A4161A'), HexColor('#C9444A'), HexColor('#8E8A7C')
PANEL, FLOOR, STAIR = HexColor('#FBFAF6'), HexColor('#ECE9DF'), HexColor('#D6D2C4')
GREEN, GREEN2 = HexColor('#DCE5D0'), HexColor('#7C8F66')
# one colour per section, so travellers can tell them apart at a glance
COL = {"00_Welcome": INK, "01_Palatine_Gallery": HexColor('#A4161A'), "02_Gallery_of_Modern_Art": HexColor('#2F5D8A'),
       "03_Museum_of_Fashion_and_Costume": HexColor('#7A3E8E'), "04_Imperial_and_Royal_Apartments": HexColor('#A87A12'),
       "05_Russian_Icons_and_Palatine_Chapel": HexColor('#1F7A72'), "06_Boboli_Gardens": HexColor('#3F6B24'), "07_Closing": INK}

def sec(f): return [t for t in tr if t["folder"] == f]
def rng(ts):
    s = [t["seq"] for t in ts]; return s[0] if len(s) == 1 else f"{s[0]}–{s[-1]}"
def mins(f): return max(1, round(sum(t["words"] for t in sec(f)) / 125))

PAL = sec("01_Palatine_Gallery")
SHORT = {"Rooms 1–2": "Statues", "Room 3": "Castagnoli", "Room 14": "Prometeo", "Room 19": "Ulisse",
         "Room 21": "Educazione\ndi Giove", "Room 22": "Stufa", "Room 23": "Iliade", "Room 24": "Saturno",
         "Room 25": "Giove", "Room 26": "Marte", "Room 27": "Apollo", "Room 28": "Venere"}
WHO = {"Room 24": "Raphael", "Room 25": "Raphael", "Room 28": "Titian\n& Canova", "Room 21": "Caravaggio",
       "Room 23": "Artemisia"}                 # a name travellers recognise, under the room
STARRED = {"Room 24", "Room 25", "Room 28"}
rooms = []
for t in PAL:
    if not rooms or rooms[-1][0] != t["room"]: rooms.append((t["room"], []))
    rooms[-1][1].append(t)
GARDEN = ["Courtyard", "Bacchino", "Grotta\nGrande", "Grotta di\nMadama", "Amphitheatre", "Neptune", "Kaffeehaus",
          "Abundance", "Viottolone", "Isolotto", "Limonaia", "Ways out"]
GSTAR = {"Grotta\nGrande", "Amphitheatre", "Kaffeehaus"}
BOB = sec("06_Boboli_Gardens"); assert len(BOB) == len(GARDEN), "update GARDEN labels to match the Boboli tracks"

W, H = landscape(A4); c = canvas.Canvas(OUT, pagesize=(W, H))
c.setTitle("Palazzo Pitti + Boboli — audio route at a glance"); c.setAuthor("Humanized Audio Guide")
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

# title strip
c.setFillColor(INK); c.rect(0, H - 1.7*cm, W, 1.7*cm, stroke=0, fill=1)
c.setFillColor(CREAM); c.setFont('Times-Bold', 20); c.drawString(1.2*cm, H - 1.15*cm, "PALAZZO PITTI + BOBOLI")
c.setFillColor(RED2); c.setFont('Times-Italic', 12); c.drawString(10.9*cm, H - 1.15*cm, "audio route at a glance")
c.setFont('Times-Italic', 11); c.drawRightString(W - 1.2*cm, H - 1.15*cm, f"{len(tr)} tracks · about {plan['total_min'] // 60} h {plan['total_min'] % 60:02d} min")

# palace cross-section
PX, PW = 1.2*cm, 19.0*cm
FL = {"2": (13.3*cm, 5.0*cm), "1": (6.4*cm, 6.4*cm), "0": (1.0*cm, 4.9*cm)}
SX, SW = PX + 0.15*cm, 1.5*cm
for k, (y, h) in FL.items():
    c.setFillColor(FLOOR); c.setStrokeColor(EDGE); c.setLineWidth(0.6); c.roundRect(PX, y, PW, h, 3, stroke=1, fill=1)
    c.saveState(); c.translate(PX - 0.38*cm, y + h/2); c.rotate(90)
    text(0, 0, {"2": "SECOND FLOOR", "1": "FIRST FLOOR", "0": "GROUND FLOOR"}[k], 'Helvetica-Bold', 7, SOFT); c.restoreState()
c.setFillColor(STAIR); c.rect(SX, FL["0"][0] + 0.15*cm, SW, FL["2"][0] + FL["2"][1] - FL["0"][0] - 0.3*cm, stroke=0, fill=1)
c.setStrokeColor(HexColor('#B9B4A3')); c.setLineWidth(0.5)
for i in range(33):
    yy = FL["0"][0] + 1.3*cm + i * 0.48*cm; c.line(SX + 0.2*cm, yy, SX + SW - 0.2*cm, yy)
text(SX + SW/2, FL["0"][0] + 0.75*cm, "stairs\n& lift", 'Helvetica-Bold', 6.3, SOFT)
SPX = SX + SW/2
g_y, g_h = FL["0"]; f_y, f_h = FL["1"]; s_y, s_h = FL["2"]

def zone_box(x, y, w, h, fo, title, step, kind, dash=False, extra=None, note=None):
    col = COL[fo]; box(x, y, w, h, col, dash=dash); narrow = w < 3*cm
    text(x + w/2, y + h - 0.8*cm, title, 'Times-Bold', 10.5, col)
    text(x + w/2, y + 0.95*cm, rng(sec(fo)), 'Helvetica-Bold', 11, col)
    text(x + w/2, y + 0.45*cm, (extra + "  ·  " if extra else "") + f"{mins(fo)} min", 'Helvetica', 6.6, SOFT)
    if narrow:
        icon(kind, x + w/2 - 0.31*cm, y + h - 2.05*cm, col)
        if note: text(x + w/2, y + h - 2.5*cm, note, 'Helvetica-Oblique', 6.3, col)
    else:
        icon(kind, x + w - 0.8*cm, y + 0.3*cm, col)
    badge(x + 0.05*cm, y + h, step, col)

# ground floor
ent_x = PX + 3.2*cm; zone_box(ent_x, g_y + 0.75*cm, 4.0*cm, 3.25*cm, "00_Welcome", "Piazza Pitti\n& courtyard", 1, "door")
flag(ent_x + 2.35*cm, g_y + 3.75*cm, "START", RED)
icx = PX + 8.6*cm; zone_box(icx, g_y + 0.75*cm, 4.6*cm, 3.25*cm, "05_Russian_Icons_and_Palatine_Chapel", "Russian Icons\n& Palatine Chapel", 6, "chapel")
# first floor: Royal Apartments at the atrium, then the Palatine rooms
rx = PX + 1.95*cm; RB, RT = f_y + 1.2*cm, f_y + f_h - 1.35*cm
zone_box(rx, RB, 2.3*cm, RT - RB, "04_Imperial_and_Royal_Apartments", "Royal\nApartments", 5, "crown", dash=True, note="separate ticket")
PC = COL["01_Palatine_Gallery"]
chain_x0 = PX + 4.7*cm; n = len(rooms); cw = (PX + PW - 0.25*cm - chain_x0) / n; bw = cw - 0.12*cm
cy, ch = f_y + 1.5*cm, 3.0*cm
c.setFillColor(PC); c.setFont('Times-Bold', 11)
c.drawString(chain_x0 + 0.5*cm, f_y + f_h - 0.62*cm, f"Palatine Gallery   {rng(PAL)}")
c.setFillColor(SOFT); c.setFont('Helvetica', 6.6); c.drawString(chain_x0 + 6.4*cm, f_y + f_h - 0.62*cm, f"{mins('01_Palatine_Gallery')} min  ·  one-way route, rooms in this order")
icon("frame", PX + PW - 1.0*cm, f_y + f_h - 0.85*cm, PC); badge(chain_x0 - 0.05*cm, f_y + f_h - 0.42*cm, 2, PC)
for i, (rm, ts) in enumerate(rooms):
    x = chain_x0 + i * cw; box(x, cy, bw, ch, PC, lw=0.8 if rm not in STARRED else 1.6)
    c.setFillColor(PC); c.roundRect(x, cy + ch - 0.5*cm, bw, 0.5*cm, 4, stroke=0, fill=1); c.rect(x, cy + ch - 0.5*cm, bw, 0.25*cm, stroke=0, fill=1)
    text(x + bw/2, cy + ch - 0.36*cm, rm.replace("Rooms ", "").replace("Room ", ""), 'Helvetica-Bold', 7.8, CREAM)
    text(x + bw/2, cy + ch - 0.88*cm, SHORT.get(rm, rm), 'Helvetica-Bold', 6.3, INK)
    if rm in WHO: text(x + bw/2, cy + ch - (1.62 if "\n" in SHORT[rm] else 1.32)*cm, WHO[rm], 'Helvetica-Oblique', 5.9, SOFT, lead=6.6)
    text(x + bw/2, cy + 0.55*cm, rng(ts).replace("–", "–\n"), 'Helvetica-Bold', 7.4, PC, lead=8)
    if rm in STARRED: star(x + bw - 0.2*cm, cy + 0.2*cm)
# second floor
SB, ST = s_y + 1.2*cm, s_y + s_h - 0.6*cm
gx = PX + 3.2*cm; zone_box(gx, SB, 6.6*cm, ST - SB, "02_Gallery_of_Modern_Art", "Gallery of Modern Art", 3, "easel", extra="rooms 1–30")
fx = PX + 11.4*cm; zone_box(fx, SB, 6.6*cm, ST - SB, "03_Museum_of_Fashion_and_Costume", "Fashion & Costume", 4, "dress")

# garden
GC = COL["06_Boboli_Gardens"]
GX, GY = PX + PW + 0.6*cm, 1.4*cm; GW, GH = W - GX - 1.0*cm, 16.9*cm
c.setFillColor(GREEN); c.setStrokeColor(GC); c.setLineWidth(1.3); c.roundRect(GX, GY, GW, GH, 8, stroke=1, fill=1)
text(GX + GW/2 + 0.2*cm, GY + GH - 0.7*cm, f"Boboli Gardens   {rng(BOB)}", 'Times-Bold', 11, GC)
text(GX + GW/2 + 0.2*cm, GY + GH - 1.15*cm, f"{mins('06_Boboli_Gardens')} min  ·  uphill first, then down the cypress avenue", 'Helvetica', 6.6, SOFT)
badge(GX + 0.45*cm, GY + GH - 0.5*cm, 7, GC); icon("tree", GX + GW - 0.95*cm, GY + GH - 0.95*cm, GC)
G = [(0.12, 0.08), (0.34, 0.16), (0.60, 0.16), (0.74, 0.30), (0.52, 0.42), (0.24, 0.55), (0.55, 0.62), (0.30, 0.76),
     (0.66, 0.84), (0.86, 0.66), (0.84, 0.44), (0.90, 0.10)]
gp = [(GX + a * GW, GY + 0.35*cm + b * (GH - 2.0*cm)) for a, b in G]
# hill shading behind the upper garden
c.setFillColor(HexColor('#CBD8BC')); c.ellipse(GX + 0.08*GW, gp[7][1] - 3.6*cm, GX + 0.92*GW, gp[8][1] + 1.0*cm, stroke=0, fill=1)
c.setStrokeColor(GREEN2); c.setLineWidth(6); c.setLineCap(1)
p = c.beginPath(); p.moveTo(*gp[0]); [p.lineTo(*q) for q in gp[1:]]; c.drawPath(p, stroke=1, fill=0)
path(gp, 1.7)
for (a, b), (x, y), lab, t in zip(G, gp, GARDEN, BOB):
    c.setFillColor(CREAM); c.setStrokeColor(GC); c.setLineWidth(1.5); c.circle(x, y, 0.4*cm, stroke=1, fill=1)
    text(x, y - 2.6, t["seq"], 'Helvetica-Bold', 7.2, GC)
    if lab in GSTAR: star(x + 0.36*cm, y + 0.32*cm)
    if lab in ("Bacchino", "Grotta\nGrande", "Ways out"):
        text(x, y - 0.72*cm, lab, 'Helvetica', 6.6, INK, lead=7.4); continue
    right = a < 0.5 or lab == "Courtyard"; c.setFillColor(INK); c.setFont('Helvetica', 6.6)
    for k, line in enumerate(lab.split("\n")):
        yy = y - 2.2 - k * 7.4 + (3.7 if "\n" in lab else 0)
        (c.drawString if right else c.drawRightString)(x + (0.52*cm if right else -0.52*cm), yy, line)
flag(gp[-1][0] - 1.2*cm, gp[-1][1] - 1.5*cm, "FINISH", GC)
c.setFillColor(INK); c.roundRect(GX + GW - 3.6*cm, 0.3*cm, 3.6*cm, 0.75*cm, 3, stroke=0, fill=1)
text(GX + GW - 1.8*cm, 0.58*cm, "8  Closing · " + sec("07_Closing")[0]["seq"] + "  (anywhere)", 'Helvetica-Bold', 7.5, CREAM)

# red walking path through the palace: enters and leaves boxes only at their edges
L1, L2, L3 = SPX - 0.35*cm, SPX, SPX + 0.35*cm
top1 = f_y + f_h - 1.05*cm; low1 = f_y + 0.6*cm; last = chain_x0 + (n - 1) * cw + bw
gmid = g_y + 2.25*cm; smid = (SB + ST) / 2; slow = s_y + 0.6*cm
path([(ent_x, gmid), (L2, gmid), (L2, top1), (last + 0.15*cm, top1), (last + 0.15*cm, low1), (L3, low1),
      (L3, smid), (gx, smid)]); arrow(L2, f_y + 0.3*cm, 'u'); arrow(chain_x0 + 5*cw, top1, 'r'); arrow(chain_x0 + 5*cw, low1, 'l')
arrow(L3, s_y + 0.3*cm, 'u'); arrow(gx, smid, 'r')
path([(gx + 6.6*cm, smid), (fx, smid)]); arrow(fx, smid, 'r')
path([(fx + 3.3*cm, SB), (fx + 3.3*cm, slow), (L1, slow), (L1, (RB + RT) / 2), (rx, (RB + RT) / 2)])
arrow(fx + 1.6*cm, slow, 'l'); arrow(L1, f_y + f_h - 0.3*cm, 'd'); arrow(rx, (RB + RT) / 2, 'r')
path([(rx + 1.15*cm, RB), (rx + 1.15*cm, RB - 0.3*cm), (L1, RB - 0.3*cm), (L1, g_y + 0.4*cm), (icx + 2.3*cm, g_y + 0.4*cm), (icx + 2.3*cm, g_y + 0.75*cm)])
arrow(L1, g_y + 2.8*cm, 'd'); arrow(icx + 2.3*cm, g_y + 0.75*cm, 'u')
ey = gp[0][1]; path([(icx + 4.6*cm, ey), (gp[0][0] - 0.44*cm, ey)]); arrow(gp[0][0] - 0.42*cm, ey, 'r')

badge(rx + 0.05*cm, RT, 5, COL["04_Imperial_and_Royal_Apartments"])   # on top of the route line

# key (one line)
ky = 0.42*cm; kx = PX
c.setStrokeColor(RED); c.setLineWidth(2.4); c.line(kx, ky + 3, kx + 0.8*cm, ky + 3); arrow(kx + 0.85*cm, ky + 3, 'r')
c.setFillColor(SOFT); c.setFont('Helvetica', 7); c.drawString(kx + 1.05*cm, ky, "your route"); kx += 3.0*cm
badge(kx + 0.2*cm, ky + 3, 2, PC, r=0.22*cm); c.setFillColor(SOFT); c.setFont('Helvetica', 7); c.drawString(kx + 0.55*cm, ky, "step"); kx += 1.9*cm
c.setFillColor(PC); c.setFont('Helvetica-Bold', 7.5); c.drawString(kx, ky, "014–020"); c.setFillColor(SOFT); c.setFont('Helvetica', 7); c.drawString(kx + 1.3*cm, ky, "tracks to play there"); kx += 4.4*cm
star(kx + 0.15*cm, ky + 3); c.setFillColor(SOFT); c.drawString(kx + 0.45*cm, ky, "don't miss"); kx += 2.5*cm
c.setStrokeColor(COL["04_Imperial_and_Royal_Apartments"]); c.setLineWidth(1.2); c.setDash(4, 2); c.rect(kx, ky - 1, 0.6*cm, 0.3*cm, stroke=1, fill=0); c.setDash()
c.setFillColor(SOFT); c.drawString(kx + 0.8*cm, ky, "separate ticket")
c.showPage(); c.save(); print("built", OUT)
