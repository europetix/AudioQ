#!/usr/bin/env python3
"""Musée d'Orsay V5 — "Route at a glance", customer edition (A3 landscape, one page).
Left: the three visited levels as simplified floor plans, drawn west (entrance and clock end) to east (Pavillon Amont), with the
real room numbers of the museum's summer 2026 plan-guide; every track badge sits in its room; a red line joins them in walking
order; escalator/lift moves between levels; START / FINISH. Right: the track index by level. Driven by plan.json (@room labels),
so numbers always match the audio. Schematic, not to scale."""
import json, os, re, sys
from reportlab.lib.pagesizes import A3, landscape
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfgen import canvas

B = sys.argv[1]; OUT = os.path.join(B, "Orsay_Audio_Guide_Route.pdf")
plan = json.load(open(os.path.join(B, "plan.json"))); tr = plan["tracks"]
W, H = landscape(A3)
INK, SOFT, CREAM, PAPER = HexColor('#1F1F1F'), HexColor('#5F5D55'), HexColor('#F4F1E8'), HexColor('#FFFDF8')
RED, WALL, AISLE = HexColor('#B3261E'), HexColor('#B9B3A3'), HexColor('#E7E1D2')
LEVEL_TINT = {0: HexColor('#F6E3DF'), 5: HexColor('#E2ECEE'), 2: HexColor('#E3ECF6')}
LEVEL_INK = {0: HexColor('#A4362B'), 5: HexColor('#2E6E73'), 2: HexColor('#2F5D8A')}
SEC_COL = {"00_Welcome": INK, "01_L0_Academic_Art": HexColor('#8A5A2E'), "02_L0_Realism": HexColor('#5E7D2E'),
           "03_L0_Manet_and_Friends": HexColor('#2F5D8A'), "04_L0_End_of_the_Nave": HexColor('#7A3E8E'),
           "05_L5_Impressionism": HexColor('#2E6E73'), "06_L5_Van_Gogh": HexColor('#B07A12'),
           "07_L5_Post_Impressionism": HexColor('#B5476B'), "08_L2_Symbolism_Nabis_Lautrec": HexColor('#A4161A'),
           "09_L2_Art_Nouveau_and_Sculpture": HexColor('#3F6B24'), "10_Closing": INK}

c = canvas.Canvas(OUT, pagesize=(W, H))
c.setTitle("Musée d'Orsay — audio route at a glance"); c.setAuthor("Humanized Audio Guide")
c.setFillColor(CREAM); c.rect(0, 0, W, H, stroke=0, fill=1)


def txt(x, y, s, font='Helvetica', size=8, col=INK, align='c'):
    c.setFillColor(col); c.setFont(font, size)
    {'c': c.drawCentredString, 'l': c.drawString, 'r': c.drawRightString}[align](x, y, s)


# ---------- geometry: each level is a band; rooms in fractions of the band (fx, fy, fw, fh) ----------
MAPX, MAPW = 1.6*cm, W * 0.66
BANDS = {0: (H - 3.1*cm, 7.9*cm), 5: (H - 12.3*cm, 7.2*cm), 2: (H - 20.8*cm, 7.9*cm)}   # top y, height
ROOMS = {0: {  # Lille side on top, Seine side below, the central aisle between; west = left
        'entrance': (0.0, 0.30, 0.07, 0.40, "Entrance"),
        '1': (0.08, 0.70, 0.07, 0.26, "1"), '2': (0.155, 0.70, 0.07, 0.26, "2"), '3': (0.23, 0.70, 0.07, 0.26, "3"),
        '9': (0.305, 0.70, 0.07, 0.26, "9"), '11': (0.38, 0.70, 0.07, 0.26, "11"), '10a': (0.455, 0.70, 0.06, 0.26, "10a"),
        '10b': (0.52, 0.70, 0.07, 0.26, "10b"), '12': (0.595, 0.70, 0.07, 0.26, "12"), '13': (0.67, 0.70, 0.08, 0.26, "13"),
        '4': (0.08, 0.04, 0.07, 0.26, "4"), '5': (0.155, 0.04, 0.07, 0.26, "5"), '6': (0.23, 0.04, 0.07, 0.26, "6"),
        '7': (0.305, 0.04, 0.09, 0.26, "7"), 'GS1': (0.40, 0.04, 0.09, 0.26, "Gal. Seine 1"), '14': (0.495, 0.04, 0.08, 0.26, "14"),
        'GS2': (0.58, 0.04, 0.08, 0.26, "Gal. Seine 2"), '18': (0.665, 0.04, 0.085, 0.26, "18"),
        'aisle': (0.08, 0.34, 0.67, 0.32, "Central sculpture aisle"),
        'paris': (0.76, 0.04, 0.13, 0.92, "Paris rooms · Opéra"),
        'gates': (0.90, 0.30, 0.09, 0.40, "Gates of Hell")},
    5: {  # the Impressionist gallery runs from the clock salon (east, right) to the west block (left)
        '28': (0.86, 0.30, 0.13, 0.60, "28 Clock salon"),
        'imp': (0.39, 0.04, 0.46, 0.22, "Impressionism, rooms 29–35 · room to confirm on site"),
        '35': (0.39, 0.30, 0.0657, 0.60, "35"), '34': (0.4557, 0.30, 0.0657, 0.60, "34"), '33': (0.5214, 0.30, 0.0657, 0.60, "33"),
        '32': (0.5871, 0.30, 0.0657, 0.60, "32"), '31': (0.6528, 0.30, 0.0657, 0.60, "31"), '30': (0.7185, 0.30, 0.0657, 0.60, "30"),
        '29': (0.7842, 0.30, 0.0658, 0.60, "29"),
        '36': (0.29, 0.30, 0.095, 0.60, "36 Van Gogh"),
        '38': (0.19, 0.56, 0.09, 0.34, "37–40"), 'cafe': (0.19, 0.10, 0.09, 0.40, "Café Campana"),
        '43': (0.10, 0.56, 0.08, 0.34, "43 Pont-Aven"), '44': (0.10, 0.10, 0.08, 0.40, "44 Tahiti"),
        '45': (0.01, 0.56, 0.08, 0.34, "45 Redon, Nabis"), '46': (0.01, 0.10, 0.08, 0.40, "46–47")},
    2: {  # west block (51, 55–60), Lille rooms 67–72 on top, sculpture terraces, Art Nouveau 61–66 at the east end
        '51': (0.0, 0.04, 0.09, 0.42, "51 Salle des fêtes"), '59': (0.0, 0.52, 0.09, 0.44, "57–60 Symbolism"),
        '55': (0.10, 0.52, 0.08, 0.44, "55"),
        '72': (0.20, 0.66, 0.08, 0.30, "72"), '71': (0.29, 0.66, 0.08, 0.30, "71"), '70': (0.38, 0.66, 0.08, 0.30, "70"),
        '69': (0.47, 0.66, 0.08, 0.30, "69"), '68': (0.56, 0.66, 0.09, 0.30, "68 Lautrec"), '67': (0.66, 0.66, 0.07, 0.30, "67"),
        'terr': (0.20, 0.36, 0.53, 0.24, "Sculpture terraces"),
        'an': (0.47, 0.04, 0.26, 0.26, "Art Nouveau 61–66"),
        'rodin': (0.75, 0.36, 0.12, 0.60, "Terrasse Rodin"),
        'exit': (0.89, 0.30, 0.10, 0.40, "↓ Exit")}}
LEVEL_OF = {k: lv for lv, rs in ROOMS.items() for k in rs}


def where(t):
    """Map a track to a room key from its @room label and title."""
    r, ti = t["room"], t["title"]
    for key, kw in (('entrance', 'Arrival'), ('exit', 'exit'), ('cafe', 'Café Campana'), ('28', 'Clock'), ('28', 'clock window'),
                    ('rodin', 'Terrasse Rodin'), ('paris', 'Opéra space'), ('paris', 'Back of the nave'), ('gates', 'between the towers'),
                    ('GS2', 'Galerie Seine 2'), ('GS2', 'Seine gallery'), ('GS1', 'Chauchard'), ('51', 'Salle des fêtes'),
                    ('aisle', 'aisle'), ('terr', 'terrace')):
        if kw.lower() in r.lower():
            return key
    m = re.search(r"Rooms? (\d+[ab]?)", r)
    if m:
        n = m.group(1); lv = 0 if 'Level 0' in r else 5 if 'Level 5' in r else 2
        num = int(re.match(r"\d+", n).group())
        if lv == 5:
            return '28' if num == 28 else '36' if num in (36, 37) else '38' if 37 <= num <= 42 else \
                   '43' if num == 43 else '44' if num == 44 else '45' if num == 45 else '46' if num in (46, 47) else \
                   str(num) if 29 <= num <= 35 else 'imp'
        if lv == 2:
            return '59' if 56 <= num <= 60 else '55' if num == 55 else '51' if num in (50, 51) else \
                   'an' if 61 <= num <= 66 else '69' if n.startswith('69') else n if n in ROOMS[2] else 'terr'
        return n if n in ROOMS[0] else 'aisle'
    for key, kw in (('5', 'Millet'), ('6', 'Courbet'), ('imp', 'Impressionist'), ('imp', 'Cézanne'), ('36', 'Van Gogh'),
                    ('44', 'Gauguin'), ('45', 'Nabi'), ('68', 'Lautrec'), ('59', 'Symbol')):
        if kw.lower() in r.lower():
            return key
    if 'Level 0' in r: return 'aisle'
    if 'Level 5' in r: return 'imp'
    return 'terr'


def rect(lv, key):
    top, h = BANDS[lv]; fx, fy, fw, fh, _ = ROOMS[lv][key]
    return MAPX + fx*MAPW, top - h + fy*h, fw*MAPW, fh*h


# ---------- title ----------
c.setFillColor(INK); c.rect(0, H - 2.3*cm, W, 2.3*cm, stroke=0, fill=1)
txt(1.6*cm, H - 1.45*cm, "MUSÉE D'ORSAY", 'Times-Bold', 28, CREAM, 'l')
txt(10.6*cm, H - 1.42*cm, "the audio route at a glance", 'Times-Italic', 16, HexColor('#E58A80'), 'l')
txt(W - 1.6*cm, H - 1.42*cm, f"{len(tr)} tracks  ·  about {plan['total_min'] // 60} h {plan['total_min'] % 60:02d} of listening  ·  level 0 → 5 → 2",
    'Helvetica', 11, CREAM, 'r')

# ---------- floors ----------
BAND_NAME = {0: ("LEVEL 0", "The nave · 1848–1870s"), 5: ("LEVEL 5", "Impressionists & after"), 2: ("LEVEL 2", "Terraces · 1880–1914")}
for lv in (0, 5, 2):
    top, h = BANDS[lv]
    c.setFillColor(PAPER); c.setStrokeColor(WALL); c.setLineWidth(1.0)
    c.roundRect(MAPX - 0.25*cm, top - h - 0.25*cm, MAPW + 0.5*cm, h + 0.5*cm, 8, stroke=1, fill=1)
    c.saveState(); c.translate(MAPX - 0.75*cm, top - h/2); c.rotate(90)
    txt(0, 0.05*cm, BAND_NAME[lv][0], 'Helvetica-Bold', 11, LEVEL_INK[lv]); c.restoreState()
    txt(MAPX + MAPW*0.5, top + 0.4*cm, BAND_NAME[lv][1], 'Helvetica-Oblique', 8.5, SOFT)
    for key, (fx, fy, fw, fh, lab) in ROOMS[lv].items():
        x, y, w, hh = rect(lv, key)
        big = key in ('aisle', 'terr', 'imp', 'paris', 'an', 'rodin')
        if key == 'imp':
            c.setDash(3, 2)
        c.setFillColor(AISLE if key in ('aisle', 'terr') else LEVEL_TINT[lv]); c.setStrokeColor(WALL); c.setLineWidth(0.7)
        c.roundRect(x + 1.2, y + 1.2, w - 2.4, hh - 2.4, 4, stroke=1, fill=1)
        txt(x + w/2 if big else x + 0.12*cm, y + hh - 0.42*cm, lab, 'Helvetica-Bold' if not big else 'Helvetica', 7 if not big else 7.2,
            SOFT, 'c' if big else 'l')
        c.setDash()
    if lv == 0:
        txt(MAPX + MAPW*0.25, top + 0.4*cm, "LILLE SIDE ↑", 'Helvetica', 6.5, WALL)
        txt(MAPX + MAPW*0.25, top - h - 0.62*cm, "SEINE SIDE ↓", 'Helvetica', 6.5, WALL)

# ---------- badges + route ----------
by_room = {}
for t in tr:
    by_room.setdefault(where(t), []).append(t)
pos = {}
R = 0.29*cm
for key, ts in by_room.items():
    lv = LEVEL_OF[key]; x, y, w, hh = rect(lv, key)
    per_row = max(1, int((w - 0.2*cm) // (2*R + 0.12*cm)))
    rows = -(-len(ts) // per_row)
    for i, t in enumerate(ts):
        r_, k_ = divmod(i, per_row); n_in_row = min(per_row, len(ts) - r_*per_row)
        cx = x + w/2 + (k_ - (n_in_row - 1)/2) * (2*R + 0.12*cm)
        cy = y + (hh - 0.45*cm)/2 + ((rows - 1)/2 - r_) * (2*R + 0.1*cm)
        pos[t["seq"]] = (cx, cy, lv)
# route lines (per level, in walking order)
c.setStrokeColor(Color(0.70, 0.15, 0.12, alpha=0.55)); c.setLineWidth(2.2); c.setLineJoin(1); c.setLineCap(1)
prev = None
for t in tr:
    cx, cy, lv = pos[t["seq"]]
    if prev and prev[2] == lv:
        c.line(prev[0], prev[1], cx, cy)
    prev = (cx, cy, lv)
for t in tr:
    cx, cy, lv = pos[t["seq"]]; col = SEC_COL.get(t["folder"], INK)
    c.setFillColor(col); c.setStrokeColor(PAPER); c.setLineWidth(1.3); c.circle(cx, cy, R, stroke=1, fill=1)
    txt(cx, cy - 2.6, str(int(t["seq"])), 'Helvetica-Bold', 7.2, PAPER)
    if "optional" in t["title"].lower():
        c.setStrokeColor(col); c.setDash(1.5, 1.5); c.circle(cx, cy, R + 2.2, stroke=1, fill=0); c.setDash()


def flag(x, y, label, col):
    c.setFillColor(col); c.roundRect(x - 0.9*cm, y, 1.8*cm, 0.5*cm, 3, stroke=0, fill=1); txt(x, y + 0.15*cm, label, 'Helvetica-Bold', 8, PAPER)


f0 = pos[tr[0]["seq"]]; flag(f0[0], f0[1] + 0.45*cm, "START", RED)
fl = pos[tr[-1]["seq"]]; flag(fl[0], fl[1] + 0.45*cm, "FINISH", INK)


def connector(x, y, label):
    c.setFillColor(INK); c.roundRect(x - 3.2*cm, y - 0.28*cm, 6.4*cm, 0.56*cm, 4, stroke=0, fill=1)
    txt(x, y - 0.09*cm, label, 'Helvetica-Bold', 8, PAPER)


connector(MAPX + MAPW*0.88, BANDS[5][0] + 0.75*cm, "▲ escalators / lifts up to level 5")
connector(MAPX + MAPW*0.18, BANDS[2][0] + 0.75*cm, "▼ from the café, down to level 2")
txt(MAPX, 1.0*cm, "Schematic, not to scale. West (entrance, great clock) on the left, Pavillon Amont on the right. Room numbers from the "
    "museum's summer 2026 plan; ask staff if a work has moved.", 'Helvetica-Oblique', 7.5, SOFT, 'l')

# ---------- index ----------
IX = MAPX + MAPW + 1.3*cm; IW = W - IX - 1.2*cm
c.setFillColor(PAPER); c.setStrokeColor(WALL); c.roundRect(IX - 0.3*cm, 1.6*cm, IW + 0.6*cm, H - 4.4*cm, 8, stroke=1, fill=1)
y = H - 3.25*cm
txt(IX, y, "TRACKS", 'Helvetica-Bold', 10, INK, 'l'); y -= 0.55*cm


def short(t):
    s = t["title"]; s = s.split(" — ", 1)[1] if " — " in s else s
    s = re.sub(r"\s*\((?!optional)[^)]*\)", "", s).replace("(optional)", "· optional")
    art = t["title"].split(" — ", 1)[0] if " — " in t["title"] else ""
    s = ((art if len(art) <= 16 else art.split()[-1]) + ": " if art else "") + s
    return s if len(s) <= 42 else s[:40].rstrip() + "…"


lead = min(0.36*cm, (y - 2.0*cm) / (len(tr) + 2*len(plan["sections"])))
lastsec = None
for t in tr:
    if t["folder"] != lastsec:
        lastsec = t["folder"]; y -= lead*0.4
        c.setFillColor(SEC_COL.get(lastsec, INK)); c.rect(IX, y - 1.5, 0.22*cm, 0.22*cm, stroke=0, fill=1)
        txt(IX + 0.35*cm, y, [s["section"] for s in plan["sections"] if s["folder"] == lastsec][0].upper(), 'Helvetica-Bold', 6.6,
            SEC_COL.get(lastsec, INK), 'l'); y -= lead
    txt(IX + 0.1*cm, y, t["seq"], 'Helvetica-Bold', 6.8, SEC_COL.get(t["folder"], INK), 'l')
    txt(IX + 0.85*cm, y, short(t), 'Helvetica', 6.8, INK, 'l'); y -= lead
txt(IX, 1.0*cm, "Lent to Tokyo 14 Nov 2026 – 28 Mar 2027 (008, 046, 053, perhaps 021): the track tells you where to go.", 'Helvetica-Oblique', 6.8, SOFT, 'l')
c.showPage(); c.save(); print("built", OUT)
