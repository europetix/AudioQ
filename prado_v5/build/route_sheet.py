#!/usr/bin/env python3
"""Yo Tours · Museo del Prado — route map (10 Oct 2026). ONE A3 landscape page.
Three floor panels drawn as a schematic of the museum's official 2026 floor plan (not to scale, our own drawing):
every room on the route with its number as written at the doorway and the track numbers played there, the walking
path in red, stairs/lift changes between floors, START/FINISH, and a track list. Driven by plan.json, so the track
numbers always match the audio files.  Usage: python3 route_sheet.py <bundle folder>"""
import json, os, re, sys
from reportlab.lib.pagesizes import A3, landscape
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas

B = sys.argv[1]; OUT = os.path.join(B, "Prado_Audio_Guide_Route.pdf")
plan = json.load(open(os.path.join(B, "plan.json"), encoding="utf-8")); tr = plan["tracks"]
INK, SOFT, CREAM, PANEL = HexColor('#1F1F1F'), HexColor('#5A5A55'), HexColor('#F3F1EA'), HexColor('#FBFAF6')
RED, GOLD, GREY, GREY2 = HexColor('#A4161A'), HexColor('#B58B2A'), HexColor('#E3E0D6'), HexColor('#B9B5A8')
COL = {"00_Welcome": INK, "01_Floor0_Flemish_Italian_Medieval": HexColor('#2F5D8A'),
       "02_Floor2_Rembrandt_Dauphins_Treasure": HexColor('#7A3E8E'), "03_Floor1_Titian_El_Greco_Velazquez": HexColor('#A4161A'),
       "04_Floor1_Murillo_Rubens_Goya": HexColor('#A87A12'), "05_Goyas_Story_Floors_2_and_0": HexColor('#3F3F3F'),
       "06_Floor0_Nineteenth_Century": HexColor('#1F7A72'), "07_Closing": INK}

# Schematic room positions (x along the building: left = Murillo end / south, right = Goya end / north;
# y across it). Taken from the official 2026 plan (research/map/). w,h in grid units (default 1 x 0.8).
F0 = {"67": (0, 2), "66": (1, 2), "65": (2, 2), "64": (3, 2), "71": (1, 4), "72": (2, 4), "73": (3, 4), "74": (2, 3),
      "63B": (4, 2), "62B": (5, 2), "61B": (6, 2), "63": (4, 1), "62": (5, 1), "61": (6, 1), "60": (7, 1),
      "63A": (4, 0), "62A": (5, 0), "61A": (6, 0), "60A": (7, 0), "75": (6, 3, 2.6, .8),
      "MUSES": (8.6, 1, 1.4, 1.6), "HALL": (8.6, -0.9, 2.2, .9), "47": (9, 3),
      "55A": (10.3, 0), "56A": (11.3, 0), "57A": (12.3, 0), "58A": (13.3, 0), "55": (10.3, 1), "56": (11.3, 1), "57": (12.3, 1), "58": (13.3, 1),
      "55B": (10.3, 2), "56B": (11.3, 2), "57B": (12.3, 2), "58B": (13.3, 2), "49": (11.8, 3, 3.6, .8), "50": (14.4, 2.6),
      "51": (15.5, 1.7, 1.1, 1.1), "51B": (15, .5), "51A": (16, .1), "51C": (14.4, 1.3), "52A": (16.8, 2), "52B": (16.6, 3), "52C": (15.8, 3.3)}
F1 = {"38": (1, 4), "37": (2, 4), "36": (3, 4), "35": (4, 4), "34": (5, 4), "39": (1, 3), "32": (3.5, 3, 1.3, .9),
      "23": (0, 2), "22": (1, 2), "21": (2, 2), "20": (3, 2), "19": (4, 2),
      "29": (6, 3, 1.4, .8), "28": (7.5, 3, 1.4, .8), "27": (9, 3, 1.4, .8), "26": (10.5, 3, 1.4, .8), "25": (12, 3, 1.4, .8), "24": (13.5, 3, 1.2, .8),
      "18": (5, 1), "18A": (5, 0), "17": (6, 1), "17A": (6, 0), "16B": (7, 2, 1.2, .8), "16": (7, 1), "16A": (7, 0), "15": (8, 1), "15A": (8, 0),
      "14": (8.4, 2), "12": (9.4, 1.4, 1.3, 1.1), "11": (10.6, 1), "10B": (11, 2), "10": (11.4, 1), "10A": (11.4, 0),
      "9B": (12.2, 2), "9": (12.4, 1), "9A": (12.4, 0), "8B": (13.2, 2), "8": (13.4, 1), "8A": (13.4, 0), "7": (14.4, 1), "7A": (14.4, 0),
      "6": (15.4, .6), "5": (16.2, .3), "4": (17, 0), "3": (17.8, -.3), "2": (18.6, -.6),
      "1": (14.9, 2.0, 1.2, 1.1), "44": (14.6, 4), "43": (15.6, 4), "42": (16.6, 4), "41": (17.6, 4), "40": (18.2, 3)}
F2 = {"85": (1, 3), "86": (2, 4), "87": (3, 4), "88": (4, 4), "89": (5, 4), "90": (0, 2), "91": (1, 2), "92": (2, 2), "93": (3, 2), "94": (4, 2),
      "79": (13.6, 4), "78": (14.6, 4), "77": (15.6, 4), "76": (16.6, 4), "79B": (15.1, 3, 1.3, .9),
      "80": (13.6, 2), "81": (14.6, 2), "82": (15.6, 2), "83": (16.6, 2)}
LABEL = {"MUSES": "Room of\nthe Muses", "HALL": "Jerónimos entrance hall"}
# walking path per floor, exactly as the cues describe it
PATH = {
 "F0a": ["HALL", "55A", "56A", "56", "55", "55B", "56B", "49", "58B", "58", "58A", "58", "58B", "50", "51", "51B", "51A", "51"],
 "F2N": ["76", "77", "78", "79", "79B", "80", "81", "82", "83"],
 "F1":  ["1", "40", "41", "42", "43", "44", "43", "42", "41", "40", "1", "2", "3", "4", "5", "6", "7", "7A", "7", "8", "8B", "9B", "9", "9A",
         "10A", "10", "11", "12", "27", "26", "25", "26", "27", "12", "14", "15", "15A", "15", "16", "17", "16B", "28", "29", "32", "34", "35",
         "36", "37", "38", "39", "23", "39"],
 "F2S": ["85", "90", "85"],
 "F0b": ["71", "74", "67", "66", "65", "64", "63", "63B", "75", "62B", "61B", "61", "60", "60A", "MUSES", "HALL"],
}

def key(room):
    m = re.search(r"Room (\w+)", room)
    return m.group(1) if m else "HALL"
tracks_at = {}
for t in tr:
    tracks_at.setdefault(key(t["room"]), []).append(t)

W, H = landscape(A3)
c = canvas.Canvas(OUT, pagesize=(W, H))
c.setTitle("Museo del Prado — Yo Tours audio guide route"); c.setAuthor("Yo Tours")
c.setFillColor(CREAM); c.rect(0, 0, W, H, stroke=0, fill=1)
# title band
c.setFillColor(INK); c.setFont('Times-Bold', 24); c.drawString(1.2*cm, H - 1.75*cm, "Museo del Prado · the route")
c.setFont('Helvetica', 9); c.setFillColor(SOFT)
c.drawString(1.2*cm, H - 2.35*cm, f"Yo Tours audio guide · {len(tr)} tracks · about 2 h 30 on foot · Each room's number is shown at its doorway: "
             "the boxes show that number and, below it, the tracks you play there.")
c.setFillColor(GOLD); c.setFont('Helvetica-Bold', 11); c.drawRightString(W - 1.2*cm, H - 1.75*cm, "YO TOURS")

LX, LW = 1.0*cm, 30.0*cm      # map area
UX = 1.38*cm                  # one grid unit
def panel(y0, ph, title, sub):
    c.setFillColor(PANEL); c.setStrokeColor(GREY2); c.setLineWidth(.6)
    c.roundRect(LX, y0, LW, ph, 6, stroke=1, fill=1)
    c.setFillColor(INK); c.setFont('Helvetica-Bold', 12); c.drawString(LX + .35*cm, y0 + ph - .6*cm, title)
    c.setFillColor(SOFT); c.setFont('Helvetica', 7.5); c.drawString(LX + .35*cm, y0 + ph - 1.0*cm, sub)
    c.setFont('Helvetica-Oblique', 6.5); c.drawString(LX + .35*cm, y0 + .25*cm, "< Murillo end (south)")
    c.drawRightString(LX + LW - .35*cm, y0 + .25*cm, "Goya end (north) >")

def geo(rooms, rid, ox, oy):
    v = rooms[rid]; x, y = v[0], v[1]; w, h = (v[2], v[3]) if len(v) > 2 else (.9, .72)
    return ox + x*UX, oy + y*UX*.82, w*UX*.95, h*UX*.82

def centre(rooms, rid, ox, oy):
    x, y, w, h = geo(rooms, rid, ox, oy); return x + w/2, y + h/2

def draw_rooms(rooms, ox, oy):
    for rid in rooms:
        x, y, w, h = geo(rooms, rid, ox, oy)
        here = tracks_at.get(rid)
        if here:
            col = COL[here[0]["folder"]]
            c.setFillColor(white); c.setStrokeColor(col); c.setLineWidth(1.4)
        else:
            c.setFillColor(GREY); c.setStrokeColor(GREY2); c.setLineWidth(.4)
        if rid in ("12", "1", "51", "79B", "32"):
            c.ellipse(x, y, x + w, y + h, stroke=1, fill=1)
        else:
            c.roundRect(x, y, w, h, 3, stroke=1, fill=1)
        lab = LABEL.get(rid, rid)
        c.setFillColor(INK if here else SOFT)
        if here:
            c.setFont('Helvetica-Bold', 8.5 if len(lab) < 5 else 6.5)
            lines = lab.split("\n")
            for i, ln in enumerate(lines):
                c.drawCentredString(x + w/2, y + h - .32*cm - i*.26*cm, ln)
            nums = [t["seq"] for t in here]
            txt = ", ".join(n.lstrip("0") for n in nums) if len(nums) < 4 else f"{nums[0].lstrip('0')}–{nums[-1].lstrip('0')}"
            c.setFillColor(COL[here[0]["folder"]]); c.setFont('Helvetica-Bold', 7)
            c.drawCentredString(x + w/2, y + .14*cm, txt)
        else:
            c.setFont('Helvetica', 6); c.drawCentredString(x + w/2, y + h/2 - .08*cm, lab)

def draw_path(rooms, seq, ox, oy, dashed_pairs=()):
    c.setStrokeColor(RED); c.setLineWidth(1.6); c.setLineCap(1); c.setLineJoin(1)
    pts = [centre(rooms, r, ox, oy) for r in seq]
    for i in range(len(pts) - 1):
        if (seq[i], seq[i + 1]) in dashed_pairs: c.setDash(3, 2)
        else: c.setDash()
        c.line(pts[i][0], pts[i][1] - .12*cm, pts[i + 1][0], pts[i + 1][1] - .12*cm)
    c.setDash()

def tag(x, y, text, col=RED):
    c.setFont('Helvetica-Bold', 6.6); tw = c.stringWidth(text, 'Helvetica-Bold', 6.6)
    c.setFillColor(col); c.roundRect(x, y, tw + .3*cm, .42*cm, 3, stroke=0, fill=1)
    c.setFillColor(white); c.drawString(x + .15*cm, y + .13*cm, text)

ph = 8.1*cm; gap = .45*cm; top = H - 2.9*cm
# Floor 2 (top), Floor 1, Floor 0 — a cross-section, as you'd see the building from the side
y2 = top - ph; y1 = y2 - gap - ph; y0 = y1 - gap - ph
ox = LX + .9*cm
panel(y2, ph, "FLOOR 2", "North wing: Rembrandt, the Dauphin's Treasure, Clara Peeters (tracks 15–18) · South wing: Goya's tapestry designs (50–51)")
panel(y1, ph, "FLOOR 1", "Round Room 1 by the Goya entrance → Titian → El Greco → Velázquez → Central Gallery → Murillo → Rubens → Goya (19–49)")
panel(y0, ph, "FLOOR 0", "Start and finish in the Jerónimos hall · Flemish & Italian masters (2–14) · Goya's war and Black Paintings, the 19th century (52–58)")
for rooms, yy, paths, dash in ((F2, y2, ("F2N", "F2S"), ()), (F1, y1, ("F1",), ()), (F0, y0, ("F0a", "F0b"), (("71", "74"), ("74", "67")))):
    oyy = yy + 1.15*cm
    draw_rooms(rooms, ox, oyy)
    for p in paths: draw_path(rooms, PATH[p], ox, oyy, dash)
    draw_rooms({k: v for k, v in rooms.items() if k in tracks_at}, ox, oyy)   # labels on top of the path

# floor changes
def at(rooms, rid, yy): return centre(rooms, rid, ox, yy + 1.15*cm)
x, y = at(F0, "HALL", y0); tag(x - 2.3*cm, y - .2*cm, "START · 1", INK)
x, y = at(F0, "51", y0); tag(x + .2*cm, y + .75*cm, "after 14: lift UP to Floor 2 (Rooms 76–83)")
x, y = at(F2, "83", y2); tag(x - 1.4*cm, y - .95*cm, "after 18: DOWN to Floor 1, Room 1")
x, y = at(F1, "23", y1); tag(x - .6*cm, y - 1.0*cm, "after 49: stairs in Room 39 UP to Floor 2, Room 85")
x, y = at(F2, "85", y2); tag(x + .4*cm, y - .2*cm, "after 51: same stairs DOWN to Floor 0")
x, y = at(F0, "71", y0); tag(x - .9*cm, y + .5*cm, "arrive by the Murillo entrance")
x, y = at(F0, "MUSES", y0); tag(x + .9*cm, y - .2*cm, "FINISH · 59 in the hall", INK)
# landmarks
c.setFillColor(SOFT); c.setFont('Helvetica-Oblique', 6.5)
x, y = at(F1, "2", y1); c.drawString(x + .7*cm, y - .1*cm, "Goya entrance")
x, y = at(F0, "47", y0); c.drawString(x - .6*cm, y + .55*cm, "Velázquez entrance")
x, y = at(F1, "26", y1); c.drawCentredString(x, y + .7*cm, "CENTRAL GALLERY")

# track list (right column)
TX = LX + LW + .6*cm; ty = H - 2.95*cm
c.setFillColor(INK); c.setFont('Helvetica-Bold', 9.5); c.drawString(TX, ty, "Tracks in walking order"); ty -= .45*cm
cur = None
for t in tr:
    if t["folder"] != cur:
        cur = t["folder"]; ty -= .08*cm
        c.setFillColor(COL[cur]); c.setFont('Helvetica-Bold', 6.6); c.drawString(TX, ty, t["section"].upper()); ty -= .34*cm
    c.setFillColor(COL[cur]); c.setFont('Helvetica-Bold', 6.6); c.drawString(TX, ty, t["seq"])
    c.setFillColor(SOFT); c.setFont('Helvetica', 6.6); c.drawString(TX + .55*cm, ty, key(t["room"]) if "Room" in t["room"] else "hall")
    title = t["title"].split(" · ", 1)[-1] if t["title"].startswith("Room") else t["title"]
    c.setFillColor(INK)
    while c.stringWidth(title, 'Helvetica', 6.6) > 7.3*cm: title = title[:-2]
    c.drawString(TX + 1.45*cm, ty, title + ("…" if title != (t["title"].split(" · ", 1)[-1] if t["title"].startswith("Room") else t["title"]) else ""))
    ty -= .325*cm
c.setFillColor(SOFT); c.setFont('Helvetica-Oblique', 6.2)
foot = ("Schematic drawing by Yo Tours after the museum's 2026 floor plan; not to scale. Rooms checked on each work's museodelprado.es page, "
        "10 Oct 2026. Museums move things: if a painting isn't there, look for the room number on the doorway and ask a guard.")
c.drawString(1.2*cm, .55*cm, foot)
c.save()
print("OK ->", OUT)
