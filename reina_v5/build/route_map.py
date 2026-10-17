#!/usr/bin/env python3
"""Yo Tours · Museo Reina Sofía — route map, edition of 17 Oct 2026.
A short PDF made to be read on a phone: page 1 = the whole visit on a cross-section of the two buildings;
then one plan per floor you walk (front of the building, the street side with the glass lift towers, at the bottom),
every stop as a numbered circle (hollow = Extra), the path with arrows, floor changes, and a stop list.
Our own schematic drawing after the museum's official plans (research/map/: easy-read plan Oct 2026–Feb 2027,
Floor 4 information map; Floor 2 collection-room plan viewed 17 Oct 2026, see research/FLOOR2_LAYOUT.md §6). Not to scale.
Driven by plan.json, so the stop numbers always match the audio files.
Usage: python3 route_map.py <bundle folder> [--png <dir>]   -> <bundle>/ReinaSofia_Audio_Guide_Route.pdf"""
import json, math, os, re, sys, html, asyncio

B = sys.argv[1]
PNG_DIR = sys.argv[sys.argv.index("--png") + 1] if "--png" in sys.argv else None
plan = json.load(open(os.path.join(B, "plan.json"), encoding="utf-8")); TR = plan["tracks"]
XS = {int(t["seq"]) for t in TR if t.get("register") == "X"}
MAIN = len(TR) - len(XS)
OUT_PDF = os.path.join(B, "ReinaSofia_Audio_Guide_Route.pdf")

# ---------------------------------------------------------------- palette & chapters (from the @section of each track)
PAPER, INK, MUTED, LINE, CTX = "#F6F1E7", "#1F1B17", "#776E62", "#D8CEBD", "#ECE5D7"
RED, GOLD = "#B0281C", "#A9812F"
SECS = [  # (@section, short title, subtitle, colour)
    ("Opening", "Welcome", "", "#3D3A36"),
    ("Floor 1 · Serra and the Garden", "Floor 1 · Serra and the garden", "Richard Serra, the cloister garden", "#2E6A62"),
    ("Floor 2 · Bohemia, Cities and Cubism", "Floor 2 · Bohemia, cities and Cubism", "Picasso, Solana, Miró, Juan Gris, María Blanchard", "#2C4A6E"),
    ("Floor 2 · War, Guernica and Surrealism", "Floor 2 · War, Guernica and Surrealism", "Renau, Dalí, Maruja Mallo, Capa, Picasso's Guernica", RED),
    ("Floor 4 · From the Transition to Grief", "Floor 4 · From the Transition to grief", "Genovés, feminisms, Matta-Clark, Barceló, Juan Muñoz", "#6A3A6B"),
    ("Floor 4 · Sculpture, Institutions and Images", "Floor 4 · Sculpture, institutions, images", "Cristina Iglesias, Chillida's logo, Ouka Leele, Belkis Ayón", "#A4581B"),
    ("Nouvel Roof Terrace", "Nouvel roof terrace", "Soto, Chirino, Negret, then the closing words", "#5B6B2E"),
    ("Closing", "Closing", "", "#5B6B2E"),
]
SCOL = {s[0]: s[3] for s in SECS}
SEQ_SEC = {int(t["seq"]): t["section"] for t in TR}
def colour(n): return SCOL.get(SEQ_SEC.get(n), INK)
# The section names in plan.json are the display names, identical to the @section values (see make_bundle.SECTIONS).
def rng(*secs):
    ns = [n for n, s in SEQ_SEC.items() if s in secs]; return min(ns), max(ns)

def short(t):
    x = t["title"]
    x = re.sub(r"^(Room [\d.]+( bis)?|Garden|Nouvel roof terrace) · ", "", x)
    return x.replace("Extra · ", "")

def rkey(room):
    if room.startswith("Sabatini entrance"): return "ENTR"
    if room.startswith("Sabatini Garden"): return "GARDEN"
    if room.startswith("Nouvel"): return "TERR"
    m = re.search(r"Room ([\d.]+)", room); return m.group(1) if m else "ENTR"
STOPS = {}
for t in TR: STOPS.setdefault(rkey(t["room"]), []).append(int(t["seq"]))

# ---------------------------------------------------------------- geometry (x right, y down; units ≈ 1 small room)
# Floor 2: read from the museum's collection-room plan, which is drawn with the street side on the right; turned a
# quarter-turn so the street side is at the bottom. ox0-ox1 / oy0-oy1 = the box in the original image (pixels).
def _rot(ox0, ox1, oy0, oy1, u=30.0):
    return ((640 - oy1) / u, (ox0 - 500) / u, (oy1 - oy0) / u, (ox1 - ox0) / u)
F2 = {k: _rot(*v) for k, v in {
    "205.02": (525, 553, 220, 245), "205.01": (553, 583, 220, 245), "205.03": (525, 583, 245, 258),
    "205.07": (525, 553, 258, 285), "205.04": (553, 583, 258, 285), "205.06": (525, 553, 285, 335),
    "205.05": (553, 583, 285, 335), "205.09": (525, 553, 335, 400), "205.10": (553, 583, 335, 400),
    "205.08": (502, 525, 350, 385), "205.13": (525, 553, 400, 460), "205.11": (553, 583, 400, 460),
    "205.14": (525, 553, 460, 480), "205.12": (553, 583, 460, 480), "205.15": (525, 553, 480, 500),
    "205.16": (525, 553, 500, 525), "205.17": (553, 583, 480, 525),
    "ST2a": (596, 622, 196, 222), "204.03": (622, 660, 196, 222), "204.02": (660, 715, 196, 222), "204.01": (715, 750, 196, 222),
    "ST2b": (596, 622, 518, 545), "206.01": (622, 660, 518, 545), "206.02": (660, 718, 518, 545), "206.03": (718, 752, 518, 545),
    "203": (765, 815, 122, 180), "ST2c": (765, 815, 197, 222), "202.01": (765, 787, 222, 290), "202.03": (787, 815, 222, 258),
    "202.02": (787, 815, 258, 290), "LIFTR": (818, 850, 288, 312), "201.01": (765, 787, 308, 400), "201.04": (765, 787, 400, 432),
    "201.02": (787, 815, 308, 370), "201.03": (787, 815, 370, 432), "LIFTL": (818, 850, 428, 452),
    "208": (765, 815, 450, 540), "207": (765, 815, 558, 620),
    "CLOISTER": (583, 750, 240, 500)}.items()}
F2_WAY = {"c2a": (F2["204.03"][0] + F2["204.03"][2] / 2, F2["205.01"][1] + F2["205.01"][3] * .5),
          "c2b": (F2["206.01"][0] + F2["206.01"][2] / 2, F2["205.17"][1] + F2["205.17"][3] * .5),
          "c2c": (F2["206.03"][0] + F2["206.03"][2] / 2, F2["201.04"][1] + F2["201.04"][3] * .5)}
# Floor 4: the museum's information map (front at the bottom), pixels of research/map/floor4_official_map.png / 60.
def _px(x0, x1, y0, y1, u=60.0): return (x0 / u, y0 / u, (x1 - x0) / u, (y1 - y0) / u)
F4 = {k: _px(*v) for k, v in {
    "14": (345, 405, 185, 320), "13": (405, 595, 185, 320), "12": (595, 745, 185, 320), "11": (745, 960, 185, 320),
    "10": (963, 1025, 395, 570), "9": (1025, 1085, 415, 490), "8": (1025, 1085, 490, 660), "7": (963, 1025, 570, 660),
    "6": (963, 1085, 660, 775), "5": (925, 1025, 775, 835), "4": (855, 925, 775, 835), "3": (735, 800, 835, 895),
    "2": (580, 735, 835, 895), "1": (510, 580, 835, 895), "15": (285, 345, 320, 475), "16": (285, 345, 485, 550),
    "17": (222, 282, 415, 690), "18": (285, 345, 555, 770), "21": (222, 455, 775, 835), "19": (222, 390, 840, 895),
    "20": (178, 222, 735, 870), "ALACENA": (560, 750, 775, 835), "LIFTL": (458, 508, 910, 970), "LIFTR": (800, 850, 910, 970),
    "CLOISTER": (345, 963, 320, 775)}.items()}
F4_WAY = {"c4a": (992 / 60, 250 / 60), "c4b": (314 / 60, 250 / 60), "l4": (483 / 60, 865 / 60)}
# Floor 1: the easy-read plan (research/map/f1.png), pixels / 60. Room 102 = the grey "Colección: Richard Serra" wing.
F1 = {k: _px(*v) for k, v in {
    "102": (305, 375, 600, 830), "GARDEN": (375, 745, 605, 835), "ENTR": (500, 625, 840, 940),
    "LIFTL": (428, 475, 850, 975), "LIFTR": (648, 695, 850, 975), "FRONTW": (195, 925, 830, 940),
    "RIGHTW": (745, 815, 505, 830), "BACKW": (305, 815, 505, 605), "NOUVEL": (760, 815, 455, 505)}.items()}
F1_WAY = {"g1": (560 / 60, 600 / 60)}
LABEL = {"ENTR": "Entrance", "GARDEN": "Garden", "LIFTL": "Lift", "LIFTR": "Lift", "ALACENA": "", "CLOISTER": "",
         "ST2a": "Stairs", "ST2b": "Stairs", "ST2c": "Stairs", "203": "203", "208": "208", "207": "207",
         "FRONTW": "", "RIGHTW": "", "BACKW": "", "NOUVEL": "To Nouvel"}

PATHS = {
 "f1": ["ENTR", "g1", "GARDEN", "102", "ENTR"],
 "f2": ["201.01", "201.02", "201.03", "201.04", "202.01", "202.02", "202.03", "204.01", "204.02", "204.03", "c2a",
        "205.01", "205.02", "205.03", "205.04", "205.05", "205.06", "205.07", "205.09", "205.10", "205.11", "205.12",
        "205.13", "205.14", "205.15", "205.16", "205.17", "c2b", "206.01", "206.02", "206.03", "c2c"],
 "f4": ["l4", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "c4a", "11", "12", "13", "14", "c4b", "15", "16",
        "17", "18", "19", "20", "21"],
}

def esc(s): return html.escape(s, quote=True)

def plan_svg(rooms, ways, path, width_mm, max_h_mm, notes=(), ends=("Back of the building", "Front · street side, glass lift towers")):
    xs = [v[0] for v in rooms.values()] + [v[0] + v[2] for v in rooms.values()]
    ys = [v[1] for v in rooms.values()] + [v[1] + v[3] for v in rooms.values()]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys); m = .6
    S = min(width_mm / (x1 - x0 + 2 * m), (max_h_mm - 14) / (y1 - y0 + 2 * m))
    W = width_mm; H = (y1 - y0 + 2 * m) * S + 14
    ox = (W - (x1 - x0) * S) / 2
    def P(x, y): return ox + (x - x0) * S, 7 + (m + y - y0) * S
    def centre(k):
        if k in ways: return P(*ways[k])
        x, y, w, h = rooms[k]; return P(x + w / 2, y + h / 2)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.1f} {H:.1f}" width="{W:.1f}mm" height="{H:.1f}mm">']
    if ends[0]: out.append(f'<text x="{W/2:.1f}" y="4.4" class="end">{esc(ends[0])}</text>')
    if ends[1]: out.append(f'<text x="{W/2:.1f}" y="{H - 1.6:.1f}" class="end">{esc(ends[1])}</text>')
    col_of = lambda k: colour(STOPS[k][0]) if k in STOPS else None
    on_path = set(path)
    # rooms first, path on top (thin), stops on top of everything
    for k, (x, y, w, h) in rooms.items():
        X, Y = P(x, y); Wd, Hd = w * S, h * S
        if k == "CLOISTER":
            out.append(f'<rect x="{X:.2f}" y="{Y:.2f}" width="{Wd:.2f}" height="{Hd:.2f}" rx="{S*.2:.2f}" fill="#E7EFE2" stroke="none"/>')
            out.append(f'<text x="{X+Wd/2:.2f}" y="{Y+Hd/2:.2f}" class="rn" style="font-size:{S*.32:.2f}px;fill:#93A58A;font-weight:600">cloister</text>'); continue
        if k == "GARDEN":
            out.append(f'<rect x="{X:.2f}" y="{Y:.2f}" width="{Wd:.2f}" height="{Hd:.2f}" rx="{S*.2:.2f}" fill="#DCEBD3" stroke="{colour(STOPS[k][0])}" stroke-width="{S*.05:.2f}"/>')
        elif k.startswith("LIFT"):
            out.append(f'<rect x="{X:.2f}" y="{Y:.2f}" width="{Wd:.2f}" height="{Hd:.2f}" rx="{S*.1:.2f}" fill="#D9E8EE" stroke="#7FA3B3" stroke-width="{S*.03:.2f}"/>')
            out.append(f'<text x="{X+Wd/2:.2f}" y="{Y+Hd/2+S*.08:.2f}" class="rn" style="font-size:{S*.2:.2f}px;fill:#3E6B7D;font-weight:700">Lift</text>'); continue
        else:
            col = col_of(k)
            if col: fill, stroke, sw = "#FFFFFF", col, S * .05
            elif k in on_path: fill, stroke, sw = "#F3ECDF", "#C2B59F", S * .025
            else: fill, stroke, sw = CTX, "#DDD4C4", S * .02
            out.append(f'<rect x="{X:.2f}" y="{Y:.2f}" width="{Wd:.2f}" height="{Hd:.2f}" rx="{S*.06:.2f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw:.2f}"/>')
        lab = LABEL.get(k, k)
        if lab:
            col = col_of(k); fs = S * (.2 if col else .16)
            if Wd < fs * len(lab) * .55 and Hd > Wd:   # tall, narrow room: write the label upright
                out.append(f'<text x="{X+Wd/2:.2f}" y="{Y+fs*1.1:.2f}" class="rn" style="font-size:{fs*.9:.2f}px;fill:{INK if col else "#A39886"};font-weight:{700 if col else 500}">{esc(lab)}</text>')
            else:
                out.append(f'<text x="{X+Wd/2:.2f}" y="{Y+fs*1.05:.2f}" class="rn" style="font-size:{fs:.2f}px;fill:{INK if col else "#A39886"};font-weight:{700 if col else 500}">{esc(lab)}</text>')
    pts = [centre(k) for k in path if k in rooms or k in ways]
    if len(pts) > 1:
        d = "M" + " L".join(f"{x:.2f},{y:.2f}" for x, y in pts)
        out.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-opacity=".55" stroke-width="{S*.045:.2f}" stroke-dasharray="{S*.12:.2f},{S*.08:.2f}" stroke-linecap="round" stroke-linejoin="round"/>')
        for (xa, ya), (xb, yb) in zip(pts, pts[1:]):
            if math.hypot(xb - xa, yb - ya) < S * .7: continue
            mx, my = (xa + xb) / 2, (ya + yb) / 2; a = math.degrees(math.atan2(yb - ya, xb - xa)); k = S * .1
            out.append(f'<path d="M{-k:.2f},{-k*.8:.2f} L{k:.2f},0 L{-k:.2f},{k*.8:.2f} Z" fill="{INK}" fill-opacity=".7" transform="translate({mx:.2f},{my:.2f}) rotate({a:.1f})"/>')
    for k, (x, y, w, h) in rooms.items():
        if k not in STOPS: continue
        X, Y = P(x, y); Wd, Hd = w * S, h * S
        st = STOPS[k]; n = len(st); rad = min(S * .2, Wd / (2.3 * n), Hd / 2.6)
        horiz = Wd >= Hd or n == 1
        for i, s in enumerate(st):
            if horiz: cx, cy = X + Wd / 2 + (i - (n - 1) / 2) * rad * 2.2, Y + Hd * .62
            else:
                rad = min(S * .2, Wd / 2.4, Hd / (2.3 * n)); cx, cy = X + Wd / 2, Y + Hd * .55 + (i - (n - 1) / 2) * rad * 2.2
            c = colour(s)
            if s in XS:
                out.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{rad*.93:.2f}" fill="#fff" stroke="{c}" stroke-width="{rad*.17:.2f}"/>')
                out.append(f'<text x="{cx:.2f}" y="{cy+rad*.36:.2f}" class="sn" style="font-size:{rad*.95:.2f}px;fill:{c}">{s}</text>')
            else:
                out.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{rad:.2f}" fill="{c}"/>')
                out.append(f'<text x="{cx:.2f}" y="{cy+rad*.36:.2f}" class="sn" style="font-size:{rad*1.0:.2f}px">{s}</text>')
    for k, text, kind, dx, dy in notes:
        cx, cy = centre(k); tx, ty = cx + dx * S, cy + dy * S
        colr = {"start": INK, "finish": INK, "up": GOLD, "down": GOLD, "info": MUTED}[kind]
        fs = 3.0; lines = text.split("\n"); wmax = max(len(l) for l in lines) * fs * .56 + fs * 1.8
        hb = fs * 1.45 * len(lines) + fs * .7
        bx = min(max(tx - wmax / 2, 1), W - wmax - 1); by = min(max(ty - hb / 2, 1), H - hb - 1)
        out.append(f'<line x1="{cx:.2f}" y1="{cy:.2f}" x2="{bx+wmax/2:.2f}" y2="{by+hb/2:.2f}" stroke="{colr}" stroke-width=".35" stroke-dasharray="1,.8"/>')
        out.append(f'<rect x="{bx:.2f}" y="{by:.2f}" width="{wmax:.2f}" height="{hb:.2f}" rx="{min(hb/2, 2.2):.2f}" fill="{colr}"/>')
        for i, l in enumerate(lines):
            out.append(f'<text x="{bx+fs*.9:.2f}" y="{by+fs*1.3+i*fs*1.45:.2f}" class="note" style="font-size:{fs:.2f}px">{esc(l)}</text>')
    out.append("</svg>")
    return "".join(out)

def stop_list(first, last):
    rows = []
    for t in TR:
        n = int(t["seq"])
        if not first <= n <= last: continue
        c = colour(n); k = rkey(t["room"])
        room = {"ENTR": "Entrance", "GARDEN": "Garden", "TERR": "Terrace"}.get(k, f"Room {k}")
        if n in XS:
            rows.append(f'<div class="row x"><span class="dot hol" style="color:{c};border-color:{c}">{n}</span>'
                        f'<span class="rm">{esc(room)}</span><span class="tt"><i style="color:{c}">Extra</i> {esc(short(t))}</span></div>')
        else:
            rows.append(f'<div class="row"><span class="dot" style="background:{c}">{n}</span>'
                        f'<span class="rm">{esc(room)}</span><span class="tt">{esc(short(t) if t["register"] not in ("ANCHOR", "CLOSE") else t["title"])}</span></div>')
    return "".join(rows)

# ---------------------------------------------------------------- page 1: the two buildings in cross-section
def overview_svg():
    W, H = 182.0, 112.0
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}mm" height="{H}mm">']
    SX0, SX1, NX0, NX1 = 22.0, 112.0, 124.0, 176.0; fh = 17.0
    fy = lambda f: 90.0 - f * 20.0
    for f in range(5):
        y = fy(f); used = f in (1, 2, 4)
        o.append(f'<rect x="{SX0}" y="{y}" width="{SX1-SX0}" height="{fh}" rx="2.2" fill="{"#fff" if used else "#F1EBE0"}" stroke="{LINE}" stroke-width=".4"/>')
        o.append(f'<text x="{SX0-3}" y="{y+fh/2+2.6}" class="fl">{f}</text>')
    for f in range(4):
        y = fy(f)
        o.append(f'<rect x="{NX0}" y="{y}" width="{NX1-NX0}" height="{fh}" rx="2.2" fill="{"#fff" if f == 3 else "#F1EBE0"}" stroke="{LINE}" stroke-width=".4"/>')
    o.append(f'<text x="{(SX0+SX1)/2}" y="{H-2.5}" class="end">SABATINI BUILDING · entrance on Calle Santa Isabel</text>')
    o.append(f'<text x="{(NX0+NX1)/2}" y="{H-2.5}" class="end">NOUVEL BUILDING</text>')
    o.append(f'<text x="{SX0+3}" y="{fy(3)+fh/2+1.2}" class="zl" style="fill:#A39886">Floor 3 · closed for now</text>')
    Z = [(1, SECS[1], "Serra · the garden"), (2, SECS[2], "Bohemia, cities, Cubism"), (2, SECS[3], "War · Guernica · Surrealism"),
         (4, SECS[4], "The Transition to grief"), (4, SECS[5], "Sculpture · institutions · images")]
    half = (SX1 - SX0 - 6) / 2
    slot = {}
    for f, sec, lab in Z:
        i = slot.get(f, 0); slot[f] = i + 1
        x0 = SX0 + 2 + i * (half + 2) if f != 1 else SX0 + 2; w = half if f != 1 else SX1 - SX0 - 4
        y = fy(f) + 2.5; h = fh - 5; c = sec[3]; a, b = rng(sec[0])
        o.append(f'<rect x="{x0:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="2" fill="{c}" fill-opacity=".10" stroke="{c}" stroke-width=".55"/>')
        o.append(f'<text x="{x0+3:.1f}" y="{y+5.4:.1f}" class="zl" style="fill:{c}">{esc(lab)}</text>')
        o.append(f'<text x="{x0+3:.1f}" y="{y+10.2:.1f}" class="zs">stops {a}–{b}</text>')
    c = SECS[6][3]; y = fy(3) + 2.5
    o.append(f'<rect x="{NX0+2}" y="{y}" width="{NX1-NX0-4}" height="{fh-5}" rx="2" fill="{c}" fill-opacity=".10" stroke="{c}" stroke-width=".55"/>')
    o.append(f'<text x="{NX0+5}" y="{y+5.4}" class="zl" style="fill:{c}">Roof terrace</text>')
    o.append(f'<text x="{NX0+5}" y="{y+10.2}" class="zs">stops {rng(SECS[6][0], "Closing")[0]}–{len(TR)}</text>')
    def arrow(pts, col, dash=None, w=1.0):
        d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts); da = f' stroke-dasharray="{dash}"' if dash else ""
        o.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"{da}/>')
        (xa, ya), (xb, yb) = pts[-2], pts[-1]; ang = math.degrees(math.atan2(yb - ya, xb - xa))
        o.append(f'<path d="M-2.6,-2 L1.8,0 L-2.6,2 Z" fill="{col}" transform="translate({xb:.1f},{yb:.1f}) rotate({ang:.1f})"/>')
    LX = SX1 + 5.5
    o.append(f'<rect x="{SX1+2}" y="{fy(4)}" width="7" height="{fy(1)+fh-fy(4)}" rx="1.5" fill="#D9E8EE" stroke="#7FA3B3" stroke-width=".35"/>')
    o.append(f'<text x="{LX}" y="{fy(4)-1.6}" class="up" style="text-anchor:middle">glass lifts</text>')
    arrow([(LX - 1.3, fy(1) + 3), (LX - 1.3, fy(2) + fh - 2)], GOLD, "1.6,1.2")
    arrow([(LX - 1.3, fy(2) + 3), (LX - 1.3, fy(4) + fh - 2)], GOLD, "1.6,1.2")
    arrow([(LX + 1.5, fy(4) + 3), (LX + 1.5, fy(1) + fh - 4)], GOLD, "1.6,1.2")
    arrow([(LX + 4, fy(1) + fh - 4), (NX0 + 8, fy(1) + fh - 4), (NX0 + 8, fy(3) + fh + .6)], GOLD, "1.6,1.2")
    o.append(f'<text x="{NX0+10}" y="{fy(2)+fh/2+1}" class="up">Nouvel lift</text>')
    o.append(f'<text x="{NX0+10}" y="{fy(2)+fh/2+4.6}" class="up">up to Floor 3</text>')
    o.append(f'<rect x="{SX0+30}" y="{fy(1)+fh+1.5}" width="30" height="6.6" rx="3.3" fill="{INK}"/>')
    o.append(f'<text x="{SX0+45}" y="{fy(1)+fh+5.9}" class="hall">START · entrance</text>')
    o.append(f'<text x="{NX1}" y="{fy(3)-2}" class="hallc" style="text-anchor:end">FINISH on the terrace ▲</text>')
    o.append("</svg>")
    return "".join(o)

pages = []
cards = "".join(
    f'<div class="card"><div class="cbar" style="background:{s[3]}"></div><div class="cnum" style="background:{s[3]}">{i}</div>'
    f'<div class="cbody"><div class="ct">{esc(s[1])}</div><div class="cs">{esc(s[2])}</div></div>'
    f'<div class="cmeta"><b>Stops {rng(*secs)[0]}–{rng(*secs)[1]}</b><br>{sum(1 for n, x in SEQ_SEC.items() if x in secs and n not in XS)} main · {sum(1 for n, x in SEQ_SEC.items() if x in secs and n in XS)} Extras</div></div>'
    for i, (s, secs) in enumerate([(SECS[1], ("Opening", SECS[1][0])), (SECS[2], (SECS[2][0],)), (SECS[3], (SECS[3][0],)),
                                   (SECS[4], (SECS[4][0],)), (SECS[5], (SECS[5][0],)), (SECS[6], (SECS[6][0], "Closing"))], 1))
pages.append(f'''<section class="page">
 <header><div class="brand">YO TOURS · AUDIO GUIDE</div><h1>Museo Reina Sofía</h1>
 <p class="lede">Your route over three floors and a roof terrace: {MAIN} main stops, about two hours, plus {len(XS)} short Extras if you have time.</p></header>
 <div class="how"><div><b>1</b> Floor 2 rooms are numbered like 205.10, Floor 4 rooms 1 to 21. Look for the number and the room title.</div>
 <div><b>2</b> Play the stops listed for that room. Hollow circles are short, optional Extras.</div>
 <div><b>3</b> Each stop ends by telling you which room is next.</div></div>
 <div class="ov">{overview_svg()}</div>
 <div class="cards">{cards}</div>
 <footer>Lost? Ask a room attendant for the room number or title on the pages that follow. The museum is rehanging its collection until 2028: if a work isn't there, ask an attendant.</footer>
</section>''')

def floor_page(title, sub, svg, first, last, extra_list=None, stack=False):
    lst = stop_list(first, last) + (stop_list(*extra_list) if extra_list else "")
    return f'''<section class="page">
 <header class="fh"><div class="brand">YO TOURS · MUSEO REINA SOFÍA</div>
 <h2>{esc(title)}</h2><p class="sub">{esc(sub)}</p></header>
 <div class="{'stack' if stack else 'split'}"><div class="plan">{svg}</div><div class="list">{lst}</div></div>
 <footer>Not to scale · drawn by Yo Tours after the museum's official plans (Oct 2026) · stop numbers = track numbers on your phone</footer>
</section>'''

a1, b1 = rng("Opening", SECS[1][0]); at, bt = rng(SECS[6][0], "Closing")
svg = plan_svg(F1, F1_WAY, PATHS["f1"], 182, 120,
    notes=[("ENTR", "START · Sabatini entrance", "start", 0, 1.0), ("LIFTR", "Then a glass lift\nup to Floor 2", "up", 2.0, .2),
           ("NOUVEL", "At the end: through here\nto the Nouvel building,\nlift up to the roof terrace", "finish", 2.6, -.6)],
    ends=("Back · towards the Nouvel building", "Front · Calle Santa Isabel"))
pages.append(floor_page("Floor 1 · Start, and the way to the terrace",
    f"Welcome at the Sabatini entrance, the cloister garden, Richard Serra in Room 102, then a glass lift up. At the very end you come back to Floor 1 and cross to the Nouvel building for the roof terrace. Stops {a1}–{b1} and {at}–{bt}.",
    svg, a1, b1, extra_list=(at, bt), stack=True))

a2, b2 = rng(SECS[2][0], SECS[3][0])
svg = plan_svg(F2, F2_WAY, PATHS["f2"], 182, 150,
    notes=[("201.01", "Arrive by a glass lift:\nthe rooms start here", "up", .3, 2.4), ("205.10", "Guernica", "info", 0, 1.6),
           ("c2c", "Back to the glass lifts,\nup to Floor 4", "up", -.4, 2.2), ("208", "207–208: not on\nthe route", "info", -1.2, 1.0)])
pages.append(floor_page("Floor 2 · From Bohemia to Guernica",
    f"One loop round the cloister: the 201 and 202 rooms along the front, the 204 rooms up one side, the 205 rooms along the back with Guernica in the middle, and the 206 rooms down the other side. Stops {a2}–{b2}.",
    svg, a2, b2, stack=True))

a4, b4 = rng(SECS[4][0], SECS[5][0])
svg = plan_svg(F4, F4_WAY, PATHS["f4"], 182, 150,
    notes=[("1", "Arrive by a glass lift:\nRoom 1 is between the lifts", "up", .2, 2.2), ("21", "Then a glass lift down to\nFloor 1, for the Nouvel terrace", "down", .6, 2.6)])
pages.append(floor_page("Floor 4 · From 1975 to now",
    f"Rooms 1 to 21 in one loop: between the lifts, up the right-hand side, along the back, and down the left-hand side to Room 21. Stops {a4}–{b4}.",
    svg, a4, b4, stack=True))

CSS = f'''
@page {{ size: A4; margin: 0 }}
* {{ box-sizing: border-box }}
html, body {{ margin: 0; background: {PAPER}; color: {INK}; font-family: Inter, "DejaVu Sans", sans-serif }}
.page {{ width: 210mm; height: 297mm; padding: 13mm 13mm 10mm; position: relative; page-break-after: always; overflow: hidden; background: {PAPER} }}
.brand {{ font: 600 7.6pt Inter; letter-spacing: .28em; color: {GOLD} }}
h1 {{ font: 700 34pt Lora, serif; margin: 2mm 0 1mm; letter-spacing: -.01em }}
h2 {{ font: 700 19pt Lora, serif; margin: 2mm 0 1.2mm }}
.lede {{ font: 400 11.5pt Lora, serif; color: {MUTED}; margin: 0 0 5mm }}
.sub {{ font: 400 9.4pt Inter; color: {MUTED}; margin: 0 0 4mm; max-width: 182mm; line-height: 1.4 }}
.how {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 3mm; margin-bottom: 4mm }}
.how div {{ background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; padding: 2.6mm 3mm; font: 500 8.4pt Inter; line-height: 1.35 }}
.how b {{ display: inline-flex; width: 5mm; height: 5mm; border-radius: 50%; background: {INK}; color: #fff; font: 700 7.5pt Inter; align-items: center; justify-content: center; margin-right: 1.5mm }}
.ov {{ background: #fff; border: .3mm solid {LINE}; border-radius: 4mm; padding: 3mm 1mm 2mm; margin-bottom: 4mm }}
.ov svg {{ display: block; margin: 0 auto }}
.fl {{ font: 700 8px Lora; fill: {INK}; text-anchor: end }}
.zl {{ font: 700 3.4px Inter }} .zs {{ font: 500 2.9px Inter; fill: {MUTED} }}
.hall {{ font: 700 3px Inter; fill: #fff; text-anchor: middle; letter-spacing: .2px }} .hallc {{ font: 700 3px Inter; fill: {INK} }}
.up {{ font: 600 2.8px Inter; fill: {GOLD} }}
.end {{ font: 600 3px Inter; fill: {MUTED}; text-anchor: middle; letter-spacing: .2px }}
.cards {{ display: grid; gap: 1.6mm }}
.card {{ display: grid; grid-template-columns: 1.6mm 11mm 1fr 30mm; align-items: center; background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; overflow: hidden; min-height: 11.5mm }}
.cbar {{ height: 100% }} .cnum {{ width: 8mm; height: 8mm; border-radius: 50%; color: #fff; font: 700 12pt Inter; display: flex; align-items: center; justify-content: center; margin-left: 2mm }}
.ct {{ font: 700 10.2pt Lora; margin-bottom: .5mm }} .cs {{ font: 400 7.9pt Inter; color: {MUTED} }}
.cmeta {{ font: 400 7.8pt Inter; color: {MUTED}; text-align: right; padding-right: 3.5mm; line-height: 1.45 }} .cmeta b {{ color: {INK} }}
footer {{ position: absolute; left: 13mm; right: 13mm; bottom: 7mm; font: 400 7pt Inter; color: {MUTED}; border-top: .3mm solid {LINE}; padding-top: 2mm }}
.stack .plan {{ margin-bottom: 3.5mm }} .stack .list {{ columns: 2; column-gap: 7mm }} .stack .row {{ break-inside: avoid }}
.plan {{ background: #fff; border: .3mm solid {LINE}; border-radius: 4mm; padding: 2mm }}
.plan svg {{ display: block; margin: 0 auto }}
.rn {{ font-family: Inter; text-anchor: middle }} .sn {{ font-family: Inter; font-weight: 700; fill: #fff; text-anchor: middle }}
.note {{ font-family: Inter; font-weight: 600; fill: #fff }}
.list .row {{ display: grid; grid-template-columns: 7.5mm 15mm 1fr; align-items: center; padding: 1.05mm 0; border-bottom: .25mm solid {LINE} }}
.dot {{ width: 6mm; height: 6mm; border-radius: 50%; color: #fff; font: 700 8pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.rm {{ font: 600 7.2pt Inter; color: {MUTED} }} .hol {{ background: #fff; border: .45mm solid; box-sizing: border-box }}
.row.x .tt {{ color: {MUTED} }} .tt i {{ font-style: normal; font-weight: 700; font-size: 7pt; letter-spacing: .04em; margin-right: 1mm }} .tt {{ font: 500 7.9pt Inter; line-height: 1.28 }}
'''
doc = f'<!doctype html><html><head><meta charset="utf-8"><title>Museo Reina Sofía · Yo Tours route</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
hp = os.path.join(B, "route_map.html"); open(hp, "w", encoding="utf-8").write(doc)

async def render():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        br = await p.chromium.launch(); pg = await br.new_page()
        await pg.goto("file://" + os.path.abspath(hp)); await pg.wait_for_timeout(300)
        await pg.pdf(path=OUT_PDF, format="A4", print_background=True, margin=dict(top="0", bottom="0", left="0", right="0"))
        if PNG_DIR:
            os.makedirs(PNG_DIR, exist_ok=True)
            await pg.set_viewport_size({"width": 794, "height": 1123})
            els = await pg.query_selector_all(".page")
            for i, el in enumerate(els):
                await el.screenshot(path=os.path.join(PNG_DIR, f"route_p{i+1}.png"), scale="device")
        await br.close()
asyncio.run(render())
os.remove(hp)
print("OK ->", OUT_PDF, len(pages), "pages")
