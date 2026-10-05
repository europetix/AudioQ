#!/usr/bin/env python3
"""Traveller route map for the Musée d'Orsay V5: ONE landscape page, "Route at a glance".
Three bands in walking order: Level 0 (nave), Level 5 (Impressionist gallery), Level 2 (terraces), joined by the
escalator/lift moves. Each section is a coloured box listing its track numbers and short names. Schematic, not to scale:
room numbers are printed only where the official pages give them (from @room). Driven by plan.json."""
import json, os, re, sys
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

B = sys.argv[1]; OUT = os.path.join(B, "Orsay_Audio_Guide_Route.pdf")
plan = json.load(open(os.path.join(B, "plan.json"))); tr = plan["tracks"]
CREAM, INK, SOFT = HexColor('#F2F1EA'), HexColor('#1F1F1F'), HexColor('#565650')
RED, EDGE, PANEL, FLOOR = HexColor('#A4161A'), HexColor('#8E8A7C'), HexColor('#FBFAF6'), HexColor('#ECE9DF')
COL = {"00_Welcome": INK, "01_L0_Academic_Art": HexColor('#8A5A2E'), "02_L0_Realism": HexColor('#5E7D2E'),
       "03_L0_Manet_and_Friends": HexColor('#2F5D8A'), "04_L0_End_of_the_Nave": HexColor('#7A3E8E'),
       "05_L5_Impressionism": HexColor('#2E6E73'), "06_L5_Van_Gogh": HexColor('#B07A12'),
       "07_L5_Post_Impressionism": HexColor('#B5476B'), "08_L2_Lautrec_and_Nabis": HexColor('#A4161A'),
       "09_L2_Art_Nouveau_and_Sculpture": HexColor('#3F6B24'), "10_Closing": INK}
NAME = {s["folder"]: s["section"] for s in plan["sections"]}


def sec(f): return [t for t in tr if t["folder"] == f]


def short(t):
    s = t["title"]
    s = s.split(" — ", 1)[1] if " — " in s else s
    s = re.sub(r"\s*\(optional\)", " (opt.)", s)
    s = re.sub(r"\s*\((?!opt)[^)]*\)", "", s)
    return s if len(s) <= 34 else s[:32].rstrip() + "…"


def room(t):
    m = re.match(r"(Rooms? [0-9][0-9a-z–and ]*)", t["room"])
    return m.group(1).replace("Rooms ", "").replace("Room ", "") if m else ""


W, H = landscape(A4); c = canvas.Canvas(OUT, pagesize=(W, H))
c.setTitle("Musée d'Orsay — audio route at a glance"); c.setAuthor("Humanized Audio Guide")
c.setFillColor(CREAM); c.rect(0, 0, W, H, stroke=0, fill=1)


def text(x, y, s, font='Helvetica', size=7, col=INK, align='c'):
    c.setFillColor(col); c.setFont(font, size)
    {'c': c.drawCentredString, 'l': c.drawString, 'r': c.drawRightString}[align](x, y, s)


def badge(x, y, n, col, r=0.3*cm):
    c.setFillColor(col); c.setStrokeColor(CREAM); c.setLineWidth(1.1); c.circle(x, y, r, stroke=1, fill=1)
    text(x, y - 2.6, str(n), 'Helvetica-Bold', 7.5, CREAM)


def flag(x, y, label, col):
    c.setFillColor(col); c.roundRect(x, y, 1.5*cm, 0.46*cm, 3, stroke=0, fill=1); text(x + 0.75*cm, y + 0.14*cm, label, 'Helvetica-Bold', 7, CREAM)


def arrow(x1, y1, x2, y2, col=RED):
    c.setStrokeColor(col); c.setFillColor(col); c.setLineWidth(1.6); c.line(x1, y1, x2, y2)
    import math
    a = math.atan2(y2 - y1, x2 - x1); L = 5
    p = c.beginPath(); p.moveTo(x2, y2)
    p.lineTo(x2 - L*math.cos(a - 0.45), y2 - L*math.sin(a - 0.45)); p.lineTo(x2 - L*math.cos(a + 0.45), y2 - L*math.sin(a + 0.45))
    p.close(); c.drawPath(p, stroke=0, fill=1)


def box(x, y, w, h, folder, step, cols=1):
    col = COL[folder]; ts = sec(folder)
    c.setFillColor(PANEL); c.setStrokeColor(col); c.setLineWidth(1.4); c.roundRect(x, y, w, h, 5, stroke=1, fill=1)
    c.setFillColor(col); c.roundRect(x, y + h - 0.55*cm, w, 0.55*cm, 5, stroke=0, fill=1)
    c.rect(x, y + h - 0.55*cm, w, 0.25*cm, stroke=0, fill=1)
    text(x + w/2, y + h - 0.39*cm, NAME[folder].split(" · ")[-1].upper(), 'Helvetica-Bold', 7, CREAM)
    badge(x + 0.05*cm, y + h + 0.02*cm, step, col)
    per = -(-len(ts) // cols); cw = w / cols
    for i, t in enumerate(ts):
        cx = x + 0.18*cm + (i // per) * cw; cy = y + h - 0.95*cm - (i % per) * 0.36*cm
        text(cx, cy, t["seq"], 'Helvetica-Bold', 6.8, col, 'l')
        r = room(t)
        text(cx + 0.62*cm, cy, short(t), 'Helvetica', 6.3, INK, 'l')
        if r: text(cx + cw - 0.3*cm, cy, r, 'Helvetica-Oblique', 5.8, SOFT, 'r')
    return x, y, w, h


def need(folder, cols=1):
    return 0.85*cm + (-(-len(sec(folder)) // cols)) * 0.36*cm + 0.1*cm


# title strip
c.setFillColor(INK); c.rect(0, H - 1.5*cm, W, 1.5*cm, stroke=0, fill=1)
c.setFillColor(CREAM); c.setFont('Times-Bold', 19); c.drawString(1.0*cm, H - 1.0*cm, "MUSÉE D'ORSAY")
c.setFillColor(HexColor('#C9444A')); c.setFont('Times-Italic', 12); c.drawString(8.2*cm, H - 1.0*cm, "audio route at a glance")
c.setFont('Times-Italic', 11); c.drawRightString(W - 1.0*cm, H - 1.0*cm, f"{len(tr)} tracks · about {plan['total_min'] // 60} h {plan['total_min'] % 60:02d} min")

M = 1.0*cm; GAP = 0.35*cm


def band(y_top, label, folders, widths, colsets, step0, hfix=None):
    hs = [need(f, k) for f, k in zip(folders, colsets)]; h = hfix or max(hs)
    y = y_top - h - 0.25*cm
    c.setFillColor(FLOOR); c.setStrokeColor(EDGE); c.setLineWidth(0.5)
    c.roundRect(M - 0.15*cm, y - 0.2*cm, W - 2*M + 0.3*cm, h + 0.55*cm, 4, stroke=1, fill=1)
    c.saveState(); c.translate(M - 0.45*cm, y + h/2); c.rotate(90); text(0, 0, label, 'Helvetica-Bold', 7.5, SOFT); c.restoreState()
    x = M; boxes = []
    tot = W - 2*M - GAP*(len(folders)-1)
    for i, (f, wf, k) in enumerate(zip(folders, widths, colsets)):
        w = tot * wf; boxes.append(box(x, y, w, h, f, step0 + i, k)); x += w + GAP
    for a, b in zip(boxes, boxes[1:]):
        arrow(a[0] + a[2] + 0.02*cm, a[1] + a[3]/2, b[0] - 0.04*cm, b[1] + b[3]/2)
    return y, boxes


y0, b0 = band(H - 1.75*cm, "LEVEL 0 · THE NAVE",
              ["00_Welcome", "01_L0_Academic_Art", "02_L0_Realism", "03_L0_Manet_and_Friends", "04_L0_End_of_the_Nave"],
              [0.17, 0.19, 0.21, 0.21, 0.22], [1, 1, 1, 1, 1], 1)
flag(b0[0][0] + 0.45*cm, b0[0][1] + b0[0][3] + 0.03*cm - 0.23*cm, "START", RED)
y5, b5 = band(y0 - 0.75*cm, "LEVEL 5 · IMPRESSIONISTS",
              ["05_L5_Impressionism", "06_L5_Van_Gogh", "07_L5_Post_Impressionism"], [0.5, 0.22, 0.28], [2, 1, 1], 6)
y2, b2 = band(y5 - 0.75*cm, "LEVEL 2 · TERRACES",
              ["08_L2_Lautrec_and_Nabis", "09_L2_Art_Nouveau_and_Sculpture", "10_Closing"], [0.32, 0.38, 0.30], [1, 1, 1], 9)
# level changes
L = b0[-1]; F = b5[0]
mid = (L[1] + F[1] + F[3]) / 2 + 0.05*cm
c.setFillColor(INK); c.roundRect(W/2 - 3.4*cm, mid - 0.2*cm, 6.8*cm, 0.5*cm, 3, stroke=0, fill=1)
text(W/2, mid - 0.03*cm, "▲ escalators or lifts up to level 5", 'Helvetica-Bold', 7, CREAM)
mid2 = (b5[0][1] + b2[0][1] + b2[0][3]) / 2 + 0.05*cm
c.setFillColor(INK); c.roundRect(W/2 - 3.4*cm, mid2 - 0.2*cm, 6.8*cm, 0.5*cm, 3, stroke=0, fill=1)
text(W/2, mid2 - 0.03*cm, "▼ down to level 2 after the Café Campana", 'Helvetica-Bold', 7, CREAM)
E = b2[-1]; flag(E[0] + E[2] - 1.6*cm, E[1] + E[3] + 0.03*cm - 0.23*cm, "FINISH", INK)
# key
ky = 0.55*cm
text(M, ky, "Room numbers in grey where the museum's own pages give them · to be confirmed on site · schematic, not to scale", 'Helvetica-Oblique', 6.5, SOFT, 'l')
text(W - M, ky, "Loans to Tokyo 14 Nov 2026 – 28 Mar 2027: 008, 044, 051 tell you where to go instead", 'Helvetica-Oblique', 6.5, SOFT, 'r')
c.showPage(); c.save(); print("built", OUT)
