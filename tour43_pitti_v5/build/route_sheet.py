#!/usr/bin/env python3
"""Traveller route map for Tour #43 (V5.1): ONE landscape page, pictorial "Route at a glance".
Palace cross-section (ground / first / second floor) + Boboli garden, the walking path in red, and each room or
stop with its track numbers. House palette from the Tour #49 route-map pattern. Driven by the bundle's plan.json,
so the track numbers always match the audio files. Deliberately almost no text."""
import json, os, sys
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

B = sys.argv[1]; OUT = os.path.join(B, "Palazzo_Pitti_Audio_Guide_Route.pdf")
plan = json.load(open(os.path.join(B, "plan.json"))); tr = plan["tracks"]
CREAM, INK, SOFT = HexColor('#F2F1EA'), HexColor('#1F1F1F'), HexColor('#565650')
RED, RED2, STONE, EDGE = HexColor('#A4161A'), HexColor('#C9444A'), HexColor('#E6E3D8'), HexColor('#8E8A7C')
GREEN, GREEN2, PANEL = HexColor('#DCE5D0'), HexColor('#7C8F66'), HexColor('#F7F6F1')

def rng(ts):
    s = [t["seq"] for t in ts]; return s[0] if len(s) == 1 else f"{s[0]}–{s[-1]}"
def sec(f): return [t for t in tr if t["folder"] == f]

PAL = sec("01_Palatine_Gallery")
SHORT = {"Rooms 1–2": "Statues", "Room 3": "Castagnoli", "Room 14": "Prometeo", "Room 19": "Ulisse",
         "Room 21": "Educazione\ndi Giove", "Room 22": "Stufa", "Room 23": "Iliade", "Room 24": "Saturno",
         "Room 25": "Giove", "Room 26": "Marte", "Room 27": "Apollo", "Room 28": "Venere"}
rooms = []
for t in PAL:
    if not rooms or rooms[-1][0] != t["room"]: rooms.append((t["room"], []))
    rooms[-1][1].append(t)
GARDEN = ["Courtyard", "Bacchino", "Grotta\nGrande", "Grotta di\nMadama", "Amphitheatre", "Neptune", "Kaffeehaus",
          "Abundance", "Viottolone", "Isolotto", "Limonaia", "Ways out"]
BOB = sec("06_Boboli_Gardens"); assert len(BOB) == len(GARDEN), "update GARDEN labels to match the Boboli tracks"

W, H = landscape(A4); c = canvas.Canvas(OUT, pagesize=(W, H))
c.setTitle("Palazzo Pitti + Boboli — audio route at a glance"); c.setAuthor("Humanized Audio Guide")
c.setFillColor(CREAM); c.rect(0, 0, W, H, stroke=0, fill=1)

def text(x, y, s, font='Helvetica', size=7, col=INK, lead=None):
    c.setFillColor(col); c.setFont(font, size); lead = lead or size * 1.15
    for i, line in enumerate(s.split("\n")): c.drawCentredString(x, y - i * lead, line)
def badge(x, y, n, r=0.33*cm, col=RED):
    c.setFillColor(col); c.circle(x, y, r, stroke=0, fill=1); text(x, y - 3.3, str(n), 'Times-Bold', 10, CREAM)
def box(x, y, w, h, fill=STONE, dash=False, edge=EDGE, lw=0.6):
    c.setFillColor(fill); c.setStrokeColor(edge); c.setLineWidth(lw)
    if dash: c.setDash(3, 2)
    c.roundRect(x, y, w, h, 3, stroke=1, fill=1); c.setDash()
def path(pts, lw=2.4, dash=False):
    c.setStrokeColor(RED); c.setLineWidth(lw); c.setLineJoin(1)
    if dash: c.setDash(4, 3)
    p = c.beginPath(); p.moveTo(*pts[0])
    for q in pts[1:]: p.lineTo(*q)
    c.drawPath(p, stroke=1, fill=0); c.setDash()
def arrow(x, y, d):
    c.setFillColor(RED); s = 4.5; p = c.beginPath()
    pts = {'r': [(x, y), (x-s, y+s*0.7), (x-s, y-s*0.7)], 'l': [(x, y), (x+s, y+s*0.7), (x+s, y-s*0.7)],
           'u': [(x, y), (x-s*0.7, y-s), (x+s*0.7, y-s)], 'd': [(x, y), (x-s*0.7, y+s), (x+s*0.7, y+s)]}[d]
    p.moveTo(*pts[0]); [p.lineTo(*q) for q in pts[1:]]; p.close(); c.drawPath(p, stroke=0, fill=1)

# title strip
c.setFillColor(INK); c.rect(0, H - 1.7*cm, W, 1.7*cm, stroke=0, fill=1)
c.setFillColor(CREAM); c.setFont('Times-Bold', 20); c.drawString(1.2*cm, H - 1.15*cm, "PALAZZO PITTI + BOBOLI")
c.setFillColor(RED2); c.setFont('Times-Italic', 12); c.drawString(10.9*cm, H - 1.15*cm, "audio route at a glance")
c.setFont('Times-Italic', 11); c.drawRightString(W - 1.2*cm, H - 1.15*cm, f"{len(tr)} tracks · about {plan['total_min'] // 60} h {plan['total_min'] % 60:02d} min")

# palace cross-section
PX, PW = 1.2*cm, 19.0*cm
FL = {"2": (13.3*cm, 5.0*cm), "1": (6.4*cm, 6.4*cm), "0": (1.0*cm, 4.9*cm)}   # floor: (y, height)
SX, SW = PX + 0.15*cm, 1.5*cm
for k, (y, h) in FL.items():
    box(PX, y, PW, h, fill=HexColor('#ECE9DF'))
    c.saveState(); c.translate(PX - 0.35*cm, y + h/2); c.rotate(90)
    text(0, 0, {"2": "SECOND FLOOR", "1": "FIRST FLOOR", "0": "GROUND FLOOR"}[k], 'Helvetica-Bold', 6.5, SOFT); c.restoreState()
c.setFillColor(HexColor('#D6D2C4')); c.rect(SX, FL["0"][0] + 0.15*cm, SW, FL["2"][0] + FL["2"][1] - FL["0"][0] - 0.3*cm, stroke=0, fill=1)
c.setStrokeColor(HexColor('#B9B4A3')); c.setLineWidth(0.5)
for i in range(33):
    yy = FL["0"][0] + 1.3*cm + i * 0.48*cm; c.line(SX + 0.2*cm, yy, SX + SW - 0.2*cm, yy)
text(SX + SW/2, FL["0"][0] + 0.75*cm, "stairs\n& lift", 'Helvetica-Bold', 6, SOFT)
SPX = SX + SW/2

g_y, g_h = FL["0"]; f_y, f_h = FL["1"]; s_y, s_h = FL["2"]
# ground floor
ent_x = PX + 3.2*cm; box(ent_x, g_y + 0.9*cm, 4.0*cm, 2.7*cm, fill=PANEL)
text(ent_x + 2.0*cm, g_y + 2.85*cm, "Piazza Pitti\n& courtyard", 'Times-Bold', 9.5, RED); text(ent_x + 2.0*cm, g_y + 1.3*cm, "001", 'Helvetica-Bold', 9)
badge(ent_x + 0.1*cm, g_y + 3.6*cm, 1)
ic = sec("05_Russian_Icons_and_Palatine_Chapel"); icx = PX + 8.6*cm
box(icx, g_y + 0.9*cm, 4.6*cm, 2.7*cm, fill=PANEL)
text(icx + 2.3*cm, g_y + 2.85*cm, "Russian Icons\n& Palatine Chapel", 'Times-Bold', 9.5, RED); text(icx + 2.3*cm, g_y + 1.3*cm, rng(ic), 'Helvetica-Bold', 9)
badge(icx + 0.1*cm, g_y + 3.6*cm, 6)
# first floor: Royal Apartments at the atrium, then the Palatine rooms in walking order
rx = PX + 1.95*cm; roy = sec("04_Imperial_and_Royal_Apartments")
RB, RT = f_y + 1.2*cm, f_y + f_h - 1.6*cm
box(rx, RB, 2.3*cm, RT - RB, fill=PANEL, dash=True, edge=RED, lw=1.0)
text(rx + 1.15*cm, RT - 0.7*cm, "Royal\nApartments", 'Times-Bold', 9, RED); text(rx + 1.15*cm, RB + 1.3*cm, rng(roy), 'Helvetica-Bold', 9)
text(rx + 1.15*cm, RB + 0.65*cm, "separate ticket", 'Helvetica-Oblique', 6.3, RED)
badge(rx + 0.05*cm, RT, 5)
chain_x0 = PX + 4.7*cm; n = len(rooms); cw = (PX + PW - 0.25*cm - chain_x0) / n; bw = cw - 0.12*cm
cy, ch = f_y + 1.5*cm, 3.0*cm
text(chain_x0 + (PX + PW - chain_x0) / 2, f_y + f_h - 0.5*cm, "Palatine Gallery  ·  " + rng(PAL), 'Times-Bold', 10, RED)
badge(chain_x0 - 0.05*cm, f_y + f_h - 0.35*cm, 2)
for i, (rm, ts) in enumerate(rooms):
    x = chain_x0 + i * cw; box(x, cy, bw, ch, fill=HexColor('#FBFAF6'))
    text(x + bw/2, cy + ch - 0.42*cm, rm.replace("Rooms ", "").replace("Room ", ""), 'Helvetica-Bold', 7.5, SOFT)
    text(x + bw/2, cy + ch - 0.95*cm, SHORT.get(rm, rm), 'Helvetica', 6.3, INK)
    text(x + bw/2, cy + 0.55*cm, rng(ts).replace("–", "–\n"), 'Helvetica-Bold', 7.2, RED, lead=8)
# second floor
gam, fas = sec("02_Gallery_of_Modern_Art"), sec("03_Museum_of_Fashion_and_Costume")
SB, ST = s_y + 1.2*cm, s_y + s_h - 0.6*cm
gx = PX + 3.2*cm; box(gx, SB, 6.6*cm, ST - SB, fill=PANEL)
text(gx + 3.3*cm, ST - 1.0*cm, "Gallery of Modern Art", 'Times-Bold', 11, RED); text(gx + 3.3*cm, SB + 0.8*cm, "rooms 1–30  ·  " + rng(gam), 'Helvetica-Bold', 9)
badge(gx + 0.05*cm, ST, 3)
fx = PX + 11.4*cm; box(fx, SB, 6.6*cm, ST - SB, fill=PANEL)
text(fx + 3.3*cm, ST - 1.0*cm, "Fashion & Costume", 'Times-Bold', 11, RED); text(fx + 3.3*cm, SB + 0.8*cm, rng(fas), 'Helvetica-Bold', 9)
badge(fx + 0.05*cm, ST, 4)

# garden
GX, GY = PX + PW + 0.6*cm, 1.4*cm; GW, GH = W - GX - 1.0*cm, 16.9*cm
c.setFillColor(GREEN); c.setStrokeColor(GREEN2); c.setLineWidth(0.8); c.roundRect(GX, GY, GW, GH, 8, stroke=1, fill=1)
text(GX + GW/2, GY + GH - 0.65*cm, "Boboli Gardens  ·  " + rng(BOB), 'Times-Bold', 10, RED); badge(GX + 0.45*cm, GY + GH - 0.45*cm, 7)
G = [(0.12, 0.08), (0.34, 0.16), (0.60, 0.16), (0.74, 0.30), (0.52, 0.42), (0.24, 0.48), (0.55, 0.60), (0.30, 0.76),
     (0.66, 0.86), (0.86, 0.66), (0.84, 0.44), (0.90, 0.10)]
gp = [(GX + a * GW, GY + 0.35*cm + b * (GH - 1.6*cm)) for a, b in G]
c.setStrokeColor(GREEN2); c.setLineWidth(6); c.setLineCap(1)
p = c.beginPath(); p.moveTo(*gp[0]); [p.lineTo(*q) for q in gp[1:]]; c.drawPath(p, stroke=1, fill=0)
path(gp, 1.6)
for (x, y), lab, t in zip(gp, GARDEN, BOB):
    c.setFillColor(CREAM); c.setStrokeColor(RED); c.setLineWidth(1.2); c.circle(x, y, 0.38*cm, stroke=1, fill=1)
    text(x, y - 2.6, t["seq"], 'Helvetica-Bold', 7, RED)
    if lab in ("Bacchino", "Grotta\nGrande"):
        text(x, y - 0.68*cm, lab, 'Helvetica', 6.6, INK, lead=7.4); continue
    right = (x - GX) / GW < 0.5 or lab == "Courtyard"; c.setFillColor(INK); c.setFont('Helvetica', 6.6)
    for k, line in enumerate(lab.split("\n")):
        yy = y - 2.2 - k * 7.4 + (3.7 if "\n" in lab else 0)
        (c.drawString if right else c.drawRightString)(x + (0.5*cm if right else -0.5*cm), yy, line)
c.setFillColor(INK); c.roundRect(GX + GW - 3.6*cm, 0.3*cm, 3.6*cm, 0.75*cm, 3, stroke=0, fill=1)
text(GX + GW - 1.8*cm, 0.58*cm, "8  Closing · " + sec("07_Closing")[0]["seq"], 'Helvetica-Bold', 8, CREAM)

# red walking path through the palace: enters and leaves boxes only at their edges
L1, L2, L3 = SPX - 0.35*cm, SPX, SPX + 0.35*cm              # three lanes in the stair column
top1 = f_y + f_h - 1.0*cm; low1 = f_y + 0.6*cm; last = chain_x0 + (n - 1) * cw + bw
gmid = g_y + 2.25*cm; smid = (SB + ST) / 2; slow = s_y + 0.6*cm
path([(ent_x, gmid), (L2, gmid), (L2, top1), (last + 0.15*cm, top1), (last + 0.15*cm, low1), (L3, low1),
      (L3, smid), (gx, smid)]); arrow(L2, f_y + 0.3*cm, 'u'); arrow(chain_x0 + 5*cw, top1, 'r'); arrow(chain_x0 + 5*cw, low1, 'l')
arrow(L3, s_y + 0.3*cm, 'u'); arrow(gx, smid, 'r')
path([(gx + 6.6*cm, smid), (fx, smid)]); arrow(fx, smid, 'r')
path([(fx + 3.3*cm, SB), (fx + 3.3*cm, slow), (L1, slow), (L1, (RB + RT) / 2), (rx, (RB + RT) / 2)])
arrow(fx + 1.6*cm, slow, 'l'); arrow(L1, f_y + f_h - 0.3*cm, 'd'); arrow(rx, (RB + RT) / 2, 'r')
path([(rx + 1.15*cm, RB), (rx + 1.15*cm, RB - 0.3*cm), (L1, RB - 0.3*cm), (L1, g_y + 0.45*cm), (icx + 2.3*cm, g_y + 0.45*cm), (icx + 2.3*cm, g_y + 0.9*cm)])
arrow(L1, g_y + 2.8*cm, 'd'); arrow(icx + 2.3*cm, g_y + 0.9*cm, 'u')
ey = gp[0][1]; path([(icx + 4.6*cm, ey), (gp[0][0] - 0.42*cm, ey)]); arrow(gp[0][0] - 0.4*cm, ey, 'r')
c.showPage(); c.save(); print("built", OUT)
