#!/usr/bin/env python3
"""Yo Tours · Museo del Prado — route map, edition of 10 Oct 2026.
A short PDF made to be read on a phone: page 1 = the whole visit as five chapters on a cross-section of the building;
then one page per part of the route, each a clean plan of only the rooms you walk through (north = Goya end at the top),
with every stop as a numbered circle, the path with arrows, floor changes, and a stop list.
Our own schematic drawing after the museum's 2026 floor plan (research/map/); not to scale.
Driven by plan.json, so the stop numbers always match the audio files.
Usage: python3 route_map.py <bundle folder>      -> <bundle>/Prado_Audio_Guide_Route.pdf (+ preview PNGs with --png <dir>)"""
import json, math, os, re, sys, html, asyncio

B = sys.argv[1]
PNG_DIR = sys.argv[sys.argv.index("--png") + 1] if "--png" in sys.argv else None
plan = json.load(open(os.path.join(B, "plan.json"), encoding="utf-8")); TR = plan["tracks"]
_ORD = [l.split() for l in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "v5", "ORDER_081.txt"))]
OLD = {int(n): o for n, o in _ORD}                  # new number -> old id ("019" core, "x09" extra)
NEW = {o: int(n) for n, o in _ORD}
N = lambda old: NEW[f"{old:03d}"]                   # new number of an old core stop
XS = {int(t["seq"]) for t in TR if t.get("register") == "X"}
MAIN = len(TR) - len(XS)

# ---------------------------------------------------------------- palette & chapters
PAPER, INK, MUTED, LINE, CTX = "#F6F1E7", "#1F1B17", "#776E62", "#D8CEBD", "#ECE5D7"
RED, GOLD = "#8C1C13", "#A9812F"
_CH = [  # (number, title, subtitle, colour, first core stop in the 59-stop plan)
    (1, "Floor 0 · Flemish & Italian masters", "Bosch, Bruegel, Dürer, Fra Angelico, Raphael, Van der Weyden", "#2C4A6E", 1),
    (2, "Floor 2 · Rembrandt & the Dauphin's Treasure", "Rembrandt, Rubens, the royal jewels, Clara Peeters", "#6A3A6B", 15),
    (3, "Floor 1 · Titian, El Greco, Velázquez", "Titian, Caravaggio, El Greco, Ribera, Zurbarán, Las Meninas", RED, 19),
    (4, "Floor 1 · Murillo, Rubens & Goya at court", "Murillo, Van Dyck, Rubens, Goya's royal family, the Majas", "#A4581B", 42),
    (5, "Goya's story, then the 19th century", "Tapestry cartoons, 2nd & 3rd of May, Black Paintings, Sorolla", "#2E6A62", 50),
]
CH = [(c[0], c[1], c[2], c[3], N(c[4]), (N(_CH[i + 1][4]) - 1) if i + 1 < len(_CH) else len(TR)) for i, c in enumerate(_CH)]
def chapter(n):
    for c in CH:
        if c[4] <= n <= c[5]: return c
    return CH[-1]

def short(t):
    s = {19: "Leoni — Charles V and the Fury · the round room", 34: "Velázquez — the royal riders", 1: "Welcome",
         59: "Closing words", 16: "The Dauphin's Treasure — the mermaid cup", 17: "Clara Peeters — Still Life with a Sparrowhawk",
         52: "The San Ildefonso Group", 10: "Raphael — The Cardinal · La Perla", 5: "Bosch — The Haywain · Seven Deadly Sins",
         46: "Rubens — The Three Graces & more", 28: "El Greco — The Adoration of the Shepherds",
         12: "Antonello — The Dead Christ supported by an Angel", 18: "Brueghel & Rubens — The Sense of Sight",
         15: "Rembrandt — Judith at the Banquet", 29: "Ribera — Isaac and Jacob · Saint Philip", 56: "Gisbert — The Execution of Torrijos",
         57: "Rosales — Isabella the Catholic's Will", 6: "Dürer — Self-portrait · Adam and Eve", 21: "Titian — Danaë",
         44: "Van Dyck — Endymion Porter", 13: "Memling — The Adoration of the Magi", 14: "Bermejo — Saint Dominic of Silos",
         26: "El Greco — The Nobleman with his Hand on his Chest", 42: "Murillo — The Immaculate of Los Venerables",
         48: "Goya — The Naked & the Clothed Maja", 22: "Claude Lorrain — The Embarkation of Saint Paula",
         24: "Artemisia Gentileschi — The Birth of Saint John", 11: "Van der Weyden — The Descent from the Cross",
         36: "Titian — Charles V at Mühlberg", 2: "Patinir — Charon Crossing the Styx", 49: "Tiepolo — The Immaculate Conception",
         25: "Caravaggio — David with the Head of Goliath", 41: "Velázquez — The Spinners", 43: "Murillo — The Holy Family with a Little Bird",
         51: "Goya — The Threshing Floor (Summer)", 9: "Botticelli — Nastagio degli Onesti"}
    old = OLD[int(t["seq"])]
    x = t["title"]
    if old.startswith("x"): return "Extra · " + x.split("Extra · ", 1)[-1]
    if int(old) in s: return s[int(old)]
    return x.split(" · ", 1)[1] if x.startswith("Room") else x

def rkey(room):
    m = re.search(r"Room (\w+)", room); return m.group(1) if m else "HALL"
STOPS = {}
for t in TR: STOPS.setdefault(rkey(t["room"]), []).append(int(t["seq"]))

# ---------------------------------------------------------------- geometry
# Room centres measured on the museum's 2026 floor plan (research/map/plano_ing_2026.pdf): the room-number labels were
# read from the PDF and converted from the isometric drawing to plan axes. a = along the building (smaller = north,
# the Goya end), b = across it (smaller = west, the Paseo del Prado side). Units: one room = about 1.
# Optional 3rd/4th values = size along / across (default 0.8 x 0.8). Not to scale beyond that.
def _g(d, sizes):
    return {k: ((v[0] / 12.5, v[1] / 15.5) + tuple(sizes.get(k, ()))) for k, v in d.items()}
F0 = _g({"52A": (-446.1, 62.3), "51A": (-445.9, 109.9), "51B": (-429.5, 110.7), "52B": (-428.9, 62.9), "51": (-428.2, 86.2),
         "51C": (-407.8, 110.4), "52C": (-407.8, 62.8), "50": (-405.1, 86.3), "58": (-392.6, 118.8), "58A": (-392.5, 132.5),
         "58B": (-391.9, 102.7), "57B": (-381.4, 103.4), "57A": (-381.2, 132.6), "57": (-381.0, 119.0), "56": (-364.5, 118.7),
         "56A": (-364.0, 132.2), "56B": (-363.6, 103.0), "49": (-370.0, 85.7), "55A": (-347.7, 132.9), "55B": (-347.7, 102.7),
         "55": (-347.4, 118.8), "47": (-316.5, 86.9), "60A": (-286.1, 133.7), "60": (-285.3, 118.3), "61B": (-272.6, 104.4),
         "61": (-266.6, 119.0), "61A": (-264.5, 132.5), "75": (-262.7, 86.1), "62": (-252.5, 119.3), "62A": (-252.3, 132.7),
         "62B": (-252.2, 103.4), "63B": (-241.1, 103.7), "63": (-240.6, 118.4), "63A": (-239.9, 134.1), "73": (-227.8, 63.2),
         "64": (-225.2, 110.4), "74": (-221.2, 87.0), "65": (-215.8, 110.6), "66": (-203.1, 110.1), "72": (-202.1, 62.9),
         "67": (-184.2, 110.8), "71": (-179.8, 63.2), "MUSES": (-314.0, 124.0), "HALL": (-352.0, 166.0)},
        {"49": (3.0, .85), "75": (2.6, .85), "51": (1.35, 1.35), "47": (.9, .9), "MUSES": (1.7, 1.55), "HALL": (2.4, 1.3), "50": (.8, .8)})
F1 = _g({"2": (-439.9, 103.1), "40": (-439.4, 55.6), "3": (-427.7, 103.7), "41": (-426.6, 56.4), "4": (-414.5, 103.7),
         "42": (-413.9, 55.7), "1": (-412.4, 79.7), "5": (-403.1, 103.5), "43": (-402.4, 55.8), "6": (-390.3, 103.9),
         "24": (-389.6, 78.2), "44": (-389.1, 55.3), "7A": (-377.0, 126.6), "7": (-377.0, 111.6), "8A": (-365.4, 127.0),
         "8": (-365.1, 110.9), "8B": (-365.0, 95.4), "25": (-364.1, 78.5), "9A": (-347.8, 126.6), "9": (-347.5, 111.7),
         "9B": (-345.3, 95.3), "26": (-333.2, 78.6), "10B": (-331.3, 95.7), "10": (-331.2, 111.4), "10A": (-331.1, 126.5),
         "11": (-318.3, 111.1), "27": (-299.0, 78.4), "12": (-297.9, 106.3), "14": (-279.2, 111.4), "15": (-267.1, 111.3),
         "15A": (-266.9, 126.1), "28": (-265.7, 78.5), "16": (-249.7, 111.5), "16A": (-249.4, 126.2), "16B": (-238.0, 95.4),
         "17": (-233.1, 110.9), "17A": (-232.9, 125.7), "29": (-228.1, 78.5), "18": (-221.3, 112.7), "18A": (-221.3, 126.1),
         "34": (-208.5, 55.3), "19": (-207.9, 103.1), "32": (-201.3, 78.3), "20": (-196.0, 103.2), "35": (-195.5, 55.3),
         "21": (-184.2, 103.4), "36": (-183.1, 55.1), "22": (-171.1, 102.7), "37": (-169.7, 54.7), "39": (-160.8, 79.0),
         "38": (-159.1, 55.5), "23": (-158.7, 103.1)},
        {"24": (1.3, .85), "25": (1.8, .85), "26": (1.8, .85), "27": (1.9, .85), "28": (2.1, .85), "29": (2.0, .85), "12": (1.35, 1.25),
         "1": (1.35, 1.35), "32": (1.1, 1.1), "39": (1.0, .8)})
F2 = _g({"83": (-457.2, 126.0), "76": (-456.8, 75.2), "82": (-443.3, 126.5), "77": (-443.1, 76.1), "79B": (-437.2, 110.0),
         "78": (-431.0, 75.4), "81": (-430.5, 126.3), "79": (-410.4, 75.0), "80": (-410.3, 125.9), "94": (-211.3, 127.1),
         "89": (-203.7, 75.7), "93": (-197.9, 126.9), "92": (-185.2, 126.8), "88": (-184.6, 76.0), "91": (-172.4, 128.0),
         "87": (-171.8, 75.4), "85": (-161.1, 102.1), "90": (-159.0, 127.0), "86": (-158.9, 74.9)},
        {"79B": (1.3, 1.3), "79": (1.3, .8), "80": (1.3, .8)})
ROUND = {"12", "1", "51", "79B", "32", "MUSES"}
NAMES = {"MUSES": "Room of the Muses", "HALL": "Entrance hall"}

# walking paths, exactly as the cues describe them
PATHS = {
 "f0n": ["HALL", "55A", "56A", "56", "55", "55B", "56B", "49", "58B", "58", "58A", "58", "58B", "50", "51", "51B", "51A", "51"],
 "f2n": ["76", "77", "78", "79", "79B", "80", "81", "82", "83"],
 "f1n": ["1", "40", "41", "42", "43", "44", "43", "42", "41", "40", "1", "2", "3", "4", "5", "6", "7", "7A", "7", "8", "8B", "9B", "9", "9A",
         "10A", "10", "11", "12", "27", "26", "25", "26", "27", "12", "14", "15", "15A", "15", "16"],
 "f1s": ["15", "16", "17", "16B", "28", "29", "32", "34", "35", "36", "37", "38", "39", "23", "39"],
 "f2s": ["85", "90", "91", "92", "93", "92", "91", "90", "85"],
 "f0s": ["71", "74", "67", "66", "65", "64", "63", "63B", "75", "62B", "61B", "61", "60", "60A", "MUSES", "HALL"],
}

def esc(s): return html.escape(s, quote=True)

def plan_svg(rooms, paths, width_mm, max_h_mm, notes=(), only=None, colour_of=None, ends=("Goya end · north", "Murillo end · south")):
    """A plan of the chosen rooms: north (the Goya end) at the top, west (Paseo del Prado side) on the left. Sizes in mm."""
    if only: rooms = {k: v for k, v in rooms.items() if k in only}
    def dims(v): return (v[2], v[3]) if len(v) > 2 else (.8, .8)
    a0 = min(v[0] - dims(v)[0] / 2 for v in rooms.values()); a1 = max(v[0] + dims(v)[0] / 2 for v in rooms.values())
    b0 = min(v[1] - dims(v)[1] / 2 for v in rooms.values()); b1 = max(v[1] + dims(v)[1] / 2 for v in rooms.values())
    m = .9                                               # margin in room units (labels, notes)
    S = min(width_mm / (b1 - b0 + 2 * m), (max_h_mm - 12) / (a1 - a0 + 2 * m))
    W = width_mm; H = (a1 - a0 + 2 * m) * S + 12
    offx = (W - (b1 - b0) * S) / 2
    def box(r):
        v = rooms[r]; du, dv = dims(v)
        return offx + (v[1] - dv / 2 - b0) * S, 6 + (m + v[0] - du / 2 - a0) * S, dv * S, du * S
    def centre(r):
        x, y, w, h = box(r); return x + w / 2, y + h / 2
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.1f} {H:.1f}" width="{W:.1f}mm" height="{H:.1f}mm">']
    if ends[0]: out.append(f'<text x="3" y="4.2" class="endl">▲  {esc(ends[0])}</text>')
    if ends[1]: out.append(f'<text x="{W-3:.1f}" y="{H - 1.4:.1f}" class="endr">▼  {esc(ends[1])}</text>')
    # paths under the rooms: they read as the way through the doorways
    for p, col in paths:
        runs, cur = [], []
        for r in PATHS[p]:
            if r in rooms: cur.append(centre(r))
            elif cur: runs.append(cur); cur = []
        if cur: runs.append(cur)
        seen, segs = set(), []
        for pts in runs:
            if len(pts) < 2: continue
            d = "M" + " L".join(f"{x:.2f},{y:.2f}" for x, y in pts)
            out.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{S*.085:.2f}" stroke-linecap="round" stroke-linejoin="round"/>')
            segs += list(zip(pts, pts[1:]))
        for (x1, y1), (x2, y2) in segs:
            L = math.hypot(x2 - x1, y2 - y1)
            if L < S * .4: continue
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            if (round(mx), round(my)) in seen: continue
            seen.add((round(mx), round(my)))
            a = math.degrees(math.atan2(y2 - y1, x2 - x1)); k = S * .14
            out.append(f'<path d="M{-k:.2f},{-k*.8:.2f} L{k:.2f},0 L{-k:.2f},{k*.8:.2f} Z" fill="{col}" stroke="#fff" stroke-width="{S*.02:.2f}" '
                       f'transform="translate({mx:.2f},{my:.2f}) rotate({a:.1f})"/>')
    on_path = {r for p, _ in paths for r in PATHS[p]}
    for r in rooms:
        x, y, w, h = box(r)
        stops = [s for s in STOPS.get(r, []) if colour_of and colour_of(s)]
        col = colour_of(stops[0]) if stops else None
        if col:   fill, stroke, sw, tc, fw = "#FFFFFF", col, S * .05, INK, 700
        elif r in on_path: fill, stroke, sw, tc, fw = "#F3ECDF", "#C2B59F", S * .022, MUTED, 600
        else:     fill, stroke, sw, tc, fw = CTX, "#DDD4C4", S * .016, "#ABA192", 500
        if r in ROUND:
            out.append(f'<ellipse cx="{x+w/2:.2f}" cy="{y+h/2:.2f}" rx="{w/2:.2f}" ry="{h/2:.2f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw:.2f}"/>')
        else:
            out.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{S*.08:.2f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw:.2f}"/>')
        label = NAMES.get(r, r)
        if r in NAMES:
            parts = {"MUSES": ["Room of", "the Muses"], "HALL": ["Jerónimos", "entrance hall"]}[r]
            fs = S * .16
            for i, ptxt in enumerate(parts):
                out.append(f'<text x="{x+w/2:.2f}" y="{y + h*(.3 if col else .45) + i*fs*1.2:.2f}" class="rn" style="font-size:{fs:.2f}px;fill:{tc};font-weight:{fw}">{esc(ptxt)}</text>')
        else:
            fs = S * (.25 if col else .19)
            ty = y + (h * .40 if col else h / 2 + fs * .35)
            out.append(f'<text x="{x+w/2:.2f}" y="{ty:.2f}" class="rn" style="font-size:{fs:.2f}px;fill:{tc};font-weight:{fw}">{esc(label)}</text>')
        if col:
            n = len(stops); rad = min(S * .17, (w + S * .3) / (2.25 * n))
            gap = rad * 2.2; x0 = x + w / 2 - gap * (n - 1) / 2; cy = y + h - rad - S * .08
            for i, s in enumerate(stops):
                cx = x0 + i * gap
                if s in XS:
                    out.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{rad*.93:.2f}" fill="#fff" stroke="{colour_of(s)}" stroke-width="{rad*.16:.2f}"/>')
                    out.append(f'<text x="{cx:.2f}" y="{cy + rad*.37:.2f}" class="sn" style="font-size:{rad*1.0:.2f}px;fill:{colour_of(s)}">{s}</text>')
                else:
                    out.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{rad:.2f}" fill="{colour_of(s)}"/>')
                    out.append(f'<text x="{cx:.2f}" y="{cy + rad*.37:.2f}" class="sn" style="font-size:{rad*1.05:.2f}px">{s}</text>')
    for r, text, kind, dx, dy in notes:
        cx, cy = centre(r); tx, ty = cx + dx * S, cy + dy * S
        colr = {"start": INK, "finish": INK, "up": GOLD, "down": GOLD, "info": MUTED}[kind]
        icon = {"start": "●", "finish": "◉", "up": "▲", "down": "▼", "info": "›"}[kind]
        fs = 3.1
        lines = text.split("\n"); wmax = max(len(l) for l in lines) * fs * .56 + fs * 2.6
        hb = fs * 1.45 * len(lines) + fs * .7
        bx = min(max(tx - wmax / 2, 1), W - wmax - 1); by = min(max(ty - hb / 2, 1), H - hb - 1)
        out.append(f'<line x1="{cx:.2f}" y1="{cy:.2f}" x2="{bx + wmax/2:.2f}" y2="{by + hb/2:.2f}" stroke="{colr}" stroke-width=".35" stroke-dasharray="1,.8"/>')
        out.append(f'<rect x="{bx:.2f}" y="{by:.2f}" width="{wmax:.2f}" height="{hb:.2f}" rx="{min(hb/2, 2.2):.2f}" fill="{colr}"/>')
        for i, l in enumerate(lines):
            yy = by + fs * 1.3 + i * fs * 1.45
            out.append(f'<text x="{bx + fs*.9:.2f}" y="{yy:.2f}" class="note" style="font-size:{fs:.2f}px">{esc((icon + "  ") if i == 0 else "    ")}{esc(l)}</text>')
    out.append("</svg>")
    return "".join(out), W, H

def colour_in(first, last):
    return lambda s: chapter(s)[3] if first <= s <= last else None

def stop_list(first, last):
    rows = []
    for t in TR:
        n = int(t["seq"])
        if not first <= n <= last: continue
        col = chapter(n)[3]; room = rkey(t["room"])
        room = "Entrance hall" if room == "HALL" else f"Room {room}"
        if n in XS:
            title = short(t).replace("Extra · ", "")
            rows.append(f'<div class="row x"><span class="dot hol" style="color:{col};border-color:{col}">{n}</span>'
                        f'<span class="rm">{esc(room)}</span><span class="tt"><i style="color:{col}">Extra</i> {esc(title)}</span></div>')
        else:
            rows.append(f'<div class="row"><span class="dot" style="background:{col}">{n}</span>'
                        f'<span class="rm">{esc(room)}</span><span class="tt">{esc(short(t))}</span></div>')
    return "".join(rows)

def minutes(first, last):
    w = sum(t["words"] for t in TR if first <= int(t["seq"]) <= last); return max(5, round(w / 125 / 5) * 5)

# ---------------------------------------------------------------- pages
pages = []

# Page 1 — overview cross-section
def overview_svg():
    W, H = 182.0, 124.0
    L, R = 16.0, 176.0                          # the building, Murillo end (south, left) to Goya end (north, right)
    fy = {2: 8.0, 1: 40.0, 0: 72.0}; fh = 22.0
    X = lambda a: L + (R - L) * (-150.0 - a) / 325.0      # a: plan coordinate along the building (see geometry)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}mm" height="{H}mm">']
    for f in (2, 1, 0):
        y = fy[f]
        o.append(f'<rect x="{L}" y="{y}" width="{R-L}" height="{fh}" rx="2.4" fill="#FBF8F2" stroke="{LINE}" stroke-width=".4"/>')
        o.append(f'<text x="{L-3.2}" y="{y+fh/2+2.6}" class="fl">{f}</text>')
        o.append(f'<text x="{L-3.2}" y="{y+fh/2+6.6}" class="flc">FLOOR</text>')
    Z = [(0, -458, -336, CH[0][3], 1, "Flemish & Italian masters"), (2, -472, -392, CH[1][3], 2, "Rembrandt"),
         (1, -472, -262, CH[2][3], 3, "Titian · El Greco · Velázquez"), (1, -258, -171, CH[3][3], 4, "Rubens · Goya"),
         (2, -232, -171, CH[4][3], 5, "Cartoons"), (0, -300, -171, CH[4][3], 5, "Goya's war · 19th century")]
    for f, a0, a1, col, n, lab in Z:
        y = fy[f] + 3.0; x0, x1 = X(a0) + .8, X(a1) - .8; x0, x1 = min(x0, x1), max(x0, x1); hz = fh - 6.0
        o.append(f'<rect x="{x0:.1f}" y="{y:.1f}" width="{x1-x0:.1f}" height="{hz:.1f}" rx="2" fill="{col}" fill-opacity=".10" stroke="{col}" stroke-width=".55"/>')
        o.append(f'<circle cx="{x0+5.3:.1f}" cy="{y+hz/2:.1f}" r="3.7" fill="{col}"/>')
        o.append(f'<text x="{x0+5.3:.1f}" y="{y+hz/2+1.55:.1f}" class="zn">{n}</text>')
        o.append(f'<text x="{x0+10.6:.1f}" y="{y+hz/2+1.3:.1f}" class="zl" style="fill:{col}">{esc(lab)}</text>')
    def arrow(pts, col, w=1.1, dash=None):
        d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        da = f' stroke-dasharray="{dash}"' if dash else ""
        o.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"{da}/>')
        (x1, y1), (x2, y2) = pts[-2], pts[-1]; ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
        o.append(f'<path d="M-2.6,-2 L1.8,0 L-2.6,2 Z" fill="{col}" transform="translate({x2:.1f},{y2:.1f}) rotate({ang:.1f})"/>')
    hx, hy = X(-352), fy[0] + fh + 11
    yb = lambda f: fy[f] + fh - 1.6
    arrow([(hx + 8, hy - 4.2), (X(-362), yb(0) - .4)], INK, 1.0)                                       # start -> 1
    arrow([(X(-445), fy[0]), (X(-445), fy[2] + fh + .6)], GOLD, 1.0, "1.8,1.3")                         # lift up to Floor 2
    o.append(f'<text x="{X(-445)-1.6:.1f}" y="{fy[1]+fh+5.4:.1f}" class="upr">lift up</text>')
    arrow([(X(-462), fy[2] + fh), (X(-462), fy[1] - .6)], GOLD, 1.0, "1.8,1.3")                         # down to Floor 1
    o.append(f'<text x="{X(-462)+1.6:.1f}" y="{fy[2]+fh+5.4:.1f}" class="up">down</text>')
    arrow([(X(-470), yb(1)), (X(-262), yb(1))], CH[2][3], .9)
    arrow([(X(-258), yb(1)), (X(-172), yb(1))], CH[3][3], .9)
    arrow([(X(-160), fy[1]), (X(-160), fy[2] + fh + .6)], GOLD, 1.0, "1.8,1.3")                         # stairs up to Floor 2 south
    o.append(f'<text x="{X(-160)-1.6:.1f}" y="{fy[2]+fh+5.4:.1f}" class="upr">stairs up</text>')
    arrow([(X(-153) + 3.2, fy[2] + fh), (X(-153) + 3.2, fy[0] - .6)], GOLD, 1.0, "1.8,1.3")             # stairs down to Floor 0
    o.append(f'<text x="{X(-153)+4.6:.1f}" y="{fy[1]+fh+5.4:.1f}" class="up">down</text>')
    arrow([(X(-174), yb(0)), (X(-300), yb(0)), (hx - 8, hy - 4.2)], CH[4][3], .9)
    o.append(f'<rect x="{hx-17:.1f}" y="{hy-4.2:.1f}" width="34" height="8.4" rx="4.2" fill="{INK}"/>')
    o.append(f'<text x="{hx:.1f}" y="{hy+1.2:.1f}" class="hall">START  ·  FINISH</text>')
    o.append(f'<text x="{hx:.1f}" y="{hy+8.6:.1f}" class="hallc">Jerónimos entrance hall, Floor 0</text>')
    o.append(f'<text x="{L}" y="{H-2}" class="endl">◀  Murillo end · south</text>')
    o.append(f'<text x="{R}" y="{H-2}" class="endr">Goya end · north  ▶</text>')
    o.append("</svg>")
    return "".join(o)

cards = "".join(
    f'<div class="card"><div class="cbar" style="background:{c[3]}"></div><div class="cnum" style="background:{c[3]}">{c[0]}</div>'
    f'<div class="cbody"><div class="ct">{esc(c[1])}</div><div class="cs">{esc(c[2])}</div></div>'
    f'<div class="cmeta"><b>Stops {c[4]}–{c[5]}</b><br>{sum(1 for t in TR if c[4] <= int(t["seq"]) <= c[5] and int(t["seq"]) not in XS)} main · {sum(1 for x in XS if c[4] <= x <= c[5])} Extras</div></div>' for c in CH)
pages.append(f'''<section class="page">
 <header><div class="brand">YO TOURS · AUDIO GUIDE</div><h1>Museo del Prado</h1>
 <p class="lede">Your route over three floors: {MAIN} main stops, about two and a half hours, plus {len(XS)} short Extras if you have time.</p></header>
 <div class="how"><div><b>1</b> Every room's number is shown at its doorway.</div><div><b>2</b> Play the stops listed for that room. Hollow circles are short, optional Extras.</div>
 <div><b>3</b> Each stop ends by telling you which room is next.</div></div>
 <div class="ov">{overview_svg()}</div>
 <div class="cards">{cards}</div>
 <footer>Lost? Find the number at the nearest doorway and look it up on the pages that follow. Museums move things: if a painting isn't there, ask a guard.</footer>
</section>''')

def floor_page(chap_ids, title, sub, svg, first, last, aside="", stack=False):
    c = CH[chap_ids[0] - 1]
    badges = "".join(f'<span class="pb" style="background:{CH[i-1][3]}">{i}</span>' for i in chap_ids)
    return f'''<section class="page">
 <header class="fh"><div class="brand">YO TOURS · MUSEO DEL PRADO</div>
 <h2>{badges}{esc(title)}</h2><p class="sub">{esc(sub)}</p></header>
 <div class="{'stack' if stack else 'split'}"><div class="plan">{svg}</div><div class="list">{aside}{stop_list(first, last)}</div></div>
 <footer>Not to scale · drawn by Yo Tours after the museum's 2026 floor plan · stop numbers = track numbers on your phone</footer>
</section>'''

G = lambda d, lo=-9999, hi=9999: [k for k, v in d.items() if lo <= v[0] * 12.5 <= hi]
# Page 2 — Floor 0 north
svg, _, _ = plan_svg(F0, [("f0n", CH[0][3])], 182, 126,
    notes=[("HALL", "START here", "start", 0, 1.25), ("51", "Lift UP to Floor 2\n(signs: Rooms 76–83)", "up", -1.6, -1.4)],
    only=G(F0, hi=-336), colour_of=colour_in(CH[0][4], CH[0][5]))
pages.append(floor_page([1], "Floor 0 · Flemish & Italian masters", f"From the Jerónimos entrance hall through the Flemish rooms to Raphael and medieval Spain. Stops {CH[0][4]}–{CH[0][5]}.", svg, CH[0][4], CH[0][5], stack=True))

# Page 3 — Floor 2 north
svg, _, _ = plan_svg(F2, [("f2n", CH[1][3])], 182, 118,
    notes=[("76", "Arrive here\nfrom Floor 0", "up", -2.2, 0), ("83", "Then DOWN to Floor 1:\nthe round Room 1", "down", 2.6, 0)],
    only=G(F2, hi=-380), colour_of=colour_in(CH[1][4], CH[1][5]))
pages.append(floor_page([2], "Floor 2 · Rembrandt & the Dauphin's Treasure", f"A small top-floor wing above the Goya entrance. Stops {CH[1][4]}–{CH[1][5]}.", svg, CH[1][4], CH[1][5], stack=True))

# Page 4a — Floor 1, the north end
svg, _, _ = plan_svg(F1, [("f1n", CH[2][3])], 104, 226,
    notes=[("1", "Arrive from Floor 2", "down", .2, -2.75), ("8B", "Continues on\nthe next page", "info", -.4, 1.5)],
    only=G(F1, hi=-360), colour_of=colour_in(N(19), N(26) - 1))
pages.append(floor_page([3], "Floor 1 · Titian and the Italian rooms", f"Arrive in the round Room 1 by the Goya entrance. Titian's wing first, then Claude, Poussin, Artemisia Gentileschi and Caravaggio. Stops {N(19)}–{N(26) - 1}.", svg, N(19), N(26) - 1))

# Page 4b — Floor 1, El Greco to Velázquez
svg, _, _ = plan_svg(F1, [("f1n", CH[2][3])], 104, 226,
    notes=[("7", "From the previous page", "info", .6, -1.2), ("15", "Continues on\nthe next page", "info", .2, 1.4),
           ("26", "Central\nGallery", "info", -1.5, 0)],
    only=G(F1, lo=-380, hi=-255), colour_of=colour_in(N(26), N(42) - 1))
pages.append(floor_page([3], "Floor 1 · El Greco, Velázquez & the Central Gallery", f"El Greco and Ribera, then Velázquez room by room to Las Meninas, a short loop into the Central Gallery for Titian, Veronese and Tintoretto, and Velázquez's late rooms. Stops {N(26)}–{N(42) - 1}.", svg, N(26), N(42) - 1))

# Page 5 — Floor 1 south
svg, _, _ = plan_svg(F1, [("f1s", CH[3][3])], 104, 226,
    notes=[("15", "From the previous page", "info", .2, -1.2), ("39", "Stairs UP to Floor 2,\nRoom 85", "up", 0, 1.35)],
    only=G(F1, lo=-272), colour_of=colour_in(N(42), N(50) - 1))
pages.append(floor_page([4], "Floor 1 · Murillo, Rubens & Goya at court", f"Murillo and Van Dyck, then back into the Central Gallery for Rubens, and on to Goya's royal portraits. Stops {N(42)}–{N(50) - 1}.", svg, N(42), N(50) - 1))

# Page 6 — Goya's story and the 19th century
svg2, _, _ = plan_svg(F2, [("f2s", CH[4][3])], 72, 70,
    notes=[("85", "Same stairs DOWN\nto Floor 0", "down", -.4, 1.5)],
    only=G(F2, lo=-230), colour_of=colour_in(N(50), N(52) - 1), ends=("Floor 2 · south wing", ""))
svg0, _, _ = plan_svg(F0, [("f0s", CH[4][3])], 104, 226,
    notes=[("71", "Arrive here, by the\nMurillo entrance", "down", 1.9, .9), ("HALL", f"FINISH · stop {len(TR)}", "finish", -.3, 1.25)],
    only=G(F0, lo=-322) + ["HALL"], colour_of=colour_in(N(52), len(TR)))
aside = f'<div class="inset"><div class="it">Floor 2 · Goya&rsquo;s tapestry designs (stops {N(50)}–{N(52) - 1})</div>{svg2}</div>'
pages.append(floor_page([5], "Goya's story, then the 19th century", f"Up to Floor 2 for young Goya, down to Floor 0 for war and the Black Paintings, then Gisbert, Rosales and Sorolla on the way back to the entrance hall. Stops {N(50)}–{len(TR)}.", svg0, N(50), len(TR), aside))

CSS = f'''
@page {{ size: A4; margin: 0 }}
* {{ box-sizing: border-box }}
html, body {{ margin: 0; background: {PAPER}; color: {INK}; font-family: Inter, "DejaVu Sans", sans-serif }}
.page {{ width: 210mm; height: 297mm; padding: 13mm 13mm 10mm; position: relative; page-break-after: always; overflow: hidden;
        background: {PAPER} }}
.brand {{ font: 600 7.6pt Inter; letter-spacing: .28em; color: {GOLD} }}
h1 {{ font: 700 34pt Lora, serif; margin: 2mm 0 1mm; letter-spacing: -.01em }}
h2 {{ font: 700 19pt Lora, serif; margin: 2mm 0 1.2mm; display: flex; align-items: center; gap: 3mm }}
.lede {{ font: 400 11.5pt Lora, serif; color: {MUTED}; margin: 0 0 5mm }}
.sub {{ font: 400 9.4pt Inter; color: {MUTED}; margin: 0 0 4mm; max-width: 175mm; line-height: 1.4 }}
.pb {{ display: inline-flex; width: 9mm; height: 9mm; border-radius: 50%; color: #fff; font: 700 13pt Inter; align-items: center; justify-content: center }}
.how {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 3mm; margin-bottom: 4mm }}
.how div {{ background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; padding: 2.6mm 3mm; font: 500 8.6pt Inter; line-height: 1.35 }}
.how b {{ display: inline-flex; width: 5mm; height: 5mm; border-radius: 50%; background: {INK}; color: #fff; font: 700 7.5pt Inter;
          align-items: center; justify-content: center; margin-right: 1.5mm }}
.ov {{ background: #fff; border: .3mm solid {LINE}; border-radius: 4mm; padding: 3mm 1mm 2mm; margin-bottom: 4.5mm }}
.ov svg {{ display: block; margin: 0 auto }}
.fl {{ font: 700 9px Lora; fill: {INK}; text-anchor: end }} .flc {{ font: 600 2.6px Inter; fill: {MUTED}; text-anchor: end; letter-spacing: .3px }}
.zn {{ font: 700 4.4px Inter; fill: #fff; text-anchor: middle }} .zl {{ font: 600 3.5px Inter }}
.hall {{ font: 700 3.1px Inter; fill: #fff; text-anchor: middle; letter-spacing: .3px }} .hallc {{ font: 500 3px Inter; fill: {MUTED}; text-anchor: middle }}
.up {{ font: 600 2.9px Inter; fill: {GOLD} }} .upr {{ font: 600 2.9px Inter; fill: {GOLD}; text-anchor: end }}
.endl {{ font: 600 3px Inter; fill: {MUTED}; text-anchor: start; letter-spacing: .2px }} .end {{ font: 600 3.2px Inter; fill: {MUTED}; text-anchor: middle; letter-spacing: .2px }} .endr {{ font: 600 3px Inter; fill: {MUTED}; text-anchor: end; letter-spacing: .2px }}
.cards {{ display: grid; gap: 1.8mm }}
.card {{ display: grid; grid-template-columns: 1.6mm 11mm 1fr 30mm; align-items: center; background: #fff; border: .3mm solid {LINE};
         border-radius: 3mm; overflow: hidden; min-height: 12.2mm }}
.cbar {{ height: 100% }} .cnum {{ width: 8mm; height: 8mm; border-radius: 50%; color: #fff; font: 700 12pt Inter; display: flex;
         align-items: center; justify-content: center; margin-left: 2mm }}
.ct {{ font: 700 10.4pt Lora; margin-bottom: .6mm }} .cs {{ font: 400 8pt Inter; color: {MUTED} }}
.cmeta {{ font: 400 7.8pt Inter; color: {MUTED}; text-align: right; padding-right: 3.5mm; line-height: 1.45 }} .cmeta b {{ color: {INK} }}
footer {{ position: absolute; left: 13mm; right: 13mm; bottom: 7mm; font: 400 7pt Inter; color: {MUTED}; border-top: .3mm solid {LINE}; padding-top: 2mm }}
.split {{ display: grid; grid-template-columns: 108mm 1fr; gap: 5mm; align-items: start }}
.stack .plan {{ margin-bottom: 4mm }} .stack .list {{ columns: 2; column-gap: 7mm }} .stack .row {{ break-inside: avoid }}
.plan {{ background: #fff; border: .3mm solid {LINE}; border-radius: 4mm; padding: 2mm }}
.plan svg {{ display: block; margin: 0 auto; max-height: 222mm; width: auto }}
.rn {{ font-family: Inter; text-anchor: middle }} .sn {{ font-family: Inter; font-weight: 700; fill: #fff; text-anchor: middle }}
.note {{ font-family: Inter; font-weight: 600; fill: #fff }}
.list .row {{ display: grid; grid-template-columns: 7.5mm 15mm 1fr; align-items: center; padding: 1.25mm 0; border-bottom: .25mm solid {LINE} }}
.dot {{ width: 6mm; height: 6mm; border-radius: 50%; color: #fff; font: 700 8pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.rm {{ font: 600 7.6pt Inter; color: {MUTED} }} .hol {{ background: #fff; border: .45mm solid; box-sizing: border-box }} .row.x .tt {{ color: {MUTED} }} .tt i {{ font-style: normal; font-weight: 700; font-size: 7pt; letter-spacing: .04em; margin-right: 1mm }} .tt {{ font: 500 8.2pt Inter; line-height: 1.3 }}
.inset {{ background: #fff; border: .3mm solid {LINE}; border-radius: 4mm; padding: 2mm 2mm 1mm; margin-bottom: 3mm }}
.it {{ font: 700 8.6pt Lora; margin: .5mm 0 1mm 1mm }}
'''
doc = f'<!doctype html><html><head><meta charset="utf-8"><title>Museo del Prado · Yo Tours route</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
hp = os.path.join(B, "route_map.html"); open(hp, "w", encoding="utf-8").write(doc)

async def render():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        br = await p.chromium.launch()
        pg = await br.new_page()
        await pg.goto("file://" + os.path.abspath(hp)); await pg.wait_for_timeout(300)
        await pg.pdf(path=os.path.join(B, "Prado_Audio_Guide_Route.pdf"), format="A4", print_background=True, margin=dict(top="0", bottom="0", left="0", right="0"))
        if PNG_DIR:
            os.makedirs(PNG_DIR, exist_ok=True)
            await pg.set_viewport_size({"width": 794, "height": 1123})
            n = await pg.evaluate("document.querySelectorAll('.page').length")
            for i in range(n):
                el = (await pg.query_selector_all(".page"))[i]
                await el.screenshot(path=os.path.join(PNG_DIR, f"route_p{i+1}.png"), scale="device")
        await br.close()
asyncio.run(render())
os.remove(hp)
print("OK ->", os.path.join(B, "Prado_Audio_Guide_Route.pdf"), len(pages), "pages")
