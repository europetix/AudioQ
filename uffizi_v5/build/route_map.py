#!/usr/bin/env python3
"""Yo Tours · Uffizi Gallery — route map, edition of 24 Oct 2026.
A PDF made to be read on a phone: page 1 = the visit on two floors (second floor on top), the way down (Lanzi staircase,
one floor only), the way out (Magliabechi staircase) and the three lengths; then one plan per part of the route, every
stop as a numbered circle (hollow = Extra), the path with arrows, the staircases and lifts; then the stop table with the
length each stop belongs to. Our own schematic drawing after the museum's October 2026 map (research/map/p-1.png,
p-2.png, p-3.png, hi-3.png); not to scale. Rooms the map marks closed or work in progress are hatched.
Stops come from v5/tracks/NNN.perf.txt (@room, @title, @type); numbers with no track file yet fall back to the track
table in v5/PLAN.md. Lengths come from build/static/lengths.json if present, else from PLAN section 3.
Usage (from the guide folder): python3 build/route_map.py <bundle folder> [--png <dir>]
  -> <bundle>/Uffizi_Audio_Guide_Route.pdf"""
import json, math, os, re, sys, html, asyncio, glob

B = sys.argv[1]
PNG_DIR = sys.argv[sys.argv.index("--png") + 1] if "--png" in sys.argv else None
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
PLAN_MD = os.path.join(ROOT, "v5", "PLAN.md"); TRACKS = os.path.join(ROOT, "v5", "tracks")
LENGTHS_JSON = os.path.join(HERE, "static", "lengths.json")
OUT_PDF = os.path.join(B, "Uffizi_Audio_Guide_Route.pdf")
FOOTER = "Yo Tours · Uffizi Gallery audio guide · 24 Oct 2026 edition · plan drawn from the museum's October 2026 map"

# ---------------------------------------------------------------- stops: tracks first, PLAN only for missing numbers
plan_txt = open(PLAN_MD, encoding="utf-8").read()
PLAN_ROWS = {}
for line in plan_txt.splitlines():
    c = [x.strip() for x in line.strip().strip("|").split("|")]
    if len(c) >= 9 and re.fullmatch(r"\d{3}", c[0]) and c[1] in ("ANCHOR", "W", "R", "X", "CLOSE"):
        PLAN_ROWS[int(c[0])] = dict(type=c[1], section=c[2], room=c[3], title=c[4], he=c[-1], src="PLAN")
SECRANGE = []  # (first, last, section) from PLAN section 1 "Sections" table
for m in re.finditer(r"^\| \d\d \| (.+?) \| (\d{3})(?:–(\d{3}))? \|", plan_txt, re.M):
    SECRANGE.append((int(m.group(2)), int(m.group(3) or m.group(2)), m.group(1).strip()))

def read_track(path):
    head, body, seen = {}, [], False
    for line in open(path, encoding="utf-8"):
        if not seen:
            if line.strip() == "---": seen = True; continue
            m = re.match(r"^@(\w+):\s*(.*?)\s*$", line)
            if m: head[m.group(1)] = m.group(2)
        else: body.append(line)
    words = len(re.sub(r"\[[^\]]*\]", " ", "".join(body)).split()) if seen else 0
    return head, words

TR = {}
for f in sorted(glob.glob(os.path.join(TRACKS, "[0-9][0-9][0-9].perf.txt"))):
    n = int(os.path.basename(f)[:3]); h, w = read_track(f); p = PLAN_ROWS.get(n, {})
    TR[n] = dict(type=h.get("type") or p.get("type", "R"), room=h.get("room") or p.get("room", ""),
                 title=h.get("title") or p.get("title", ""), words=w, src="track")
for n, p in PLAN_ROWS.items():
    if n not in TR: TR[n] = dict(p, words=0)
NUMS = sorted(TR)
N_TRACK = sum(1 for n in NUMS if TR[n]["src"] == "track")
XS = {n for n in NUMS if TR[n]["type"] == "X"}
MID = {"W": 300, "R": 230, "X": 190, "ANCHOR": 320, "CLOSE": 320}
def minutes(n):
    t = TR[n]; w = t["words"] if t["words"] > 40 else MID.get(t["type"], 230)
    return w / 125.0
def fmt_min(m):
    h = round(m * 2) / 2; whole = int(h)
    return f"{whole}½" if h - whole else f"{whole}"

# ---------------------------------------------------------------- the three lengths
def plan_list(head):
    m = re.search(r"^### " + head + r".*?$(.*?)^###", plan_txt, re.M | re.S)
    return [int(x) for x in re.findall(r"^\| (\d{3}) \|", m.group(1), re.M)] if m else []
H_SET = E_SET = None
if os.path.exists(LENGTHS_JSON):
    try:
        J = json.load(open(LENGTHS_JSON, encoding="utf-8"))
        H_SET = {int(x) for x in J["HIGHLIGHTS"].split()}; E_SET = {int(x) for x in J["ESSENTIAL"].split()}
    except Exception as e:
        print("lengths.json not usable, reading PLAN section 3:", e)
if H_SET is None:
    H_SET = set(plan_list("Highlights"))
    m = re.search(r"Full order of Essential:\s*([\d\s]+)", plan_txt)
    E_SET = {int(x) for x in m.group(1).split()} if m else set(plan_list("Essential")) | H_SET
LENGTHS = [("Full tour", len(NUMS), "about 2 h 45", f"all {len(NUMS) - len(XS)} main stops and {len(XS)} Extras"),
           ("Essential", len(E_SET), "about 2 h", "the main line with fewer stops per room"),
           ("Highlights", len(H_SET), "about 1 h 15", "the great names, on both floors")]

# ---------------------------------------------------------------- palette & sections
PAPER, INK, MUTED, LINE, CTX = "#F6F1E7", "#1F1B17", "#776E62", "#D8CEBD", "#ECE5D7"
RED, GOLD, NAVY, RIVER = "#B0281C", "#A9812F", "#1D2B4A", "#CFE2EA"
SECS = {  # PLAN section -> (short title, subtitle, colour)
    "Opening": ("Welcome", "outside, before you go in", "#3D3A36"),
    "Second floor · The 13th and 14th centuries": ("13th and 14th centuries", "Cimabue, Duccio, Giotto, Simone Martini", "#8C6A2E"),
    "Second floor · Early Renaissance": ("Early Renaissance", "Masaccio, Fra Angelico, Uccello", "#9A4E2C"),
    "Second floor · The Botticelli rooms and the Tribune": ("Botticelli and the Tribune", "Primavera, Venus, Portinari, Tribune", RED),
    "Second floor · High Renaissance": ("High Renaissance", "Piero, Perugino, Leonardo", "#7A3A5E"),
    "Second floor · Raphael, Michelangelo and the Niobe Room": ("Raphael, Michelangelo, Niobe", "Doni Tondo, Goldfinch, Niobe Room", "#2C4A6E"),
    "First floor · Contini Bonacossi collection": ("Contini Bonacossi", "Bellini, Bramantino, Bernini", "#2E6A62"),
    "First floor · Self-portraits": ("Self-portraits", "from the Medici to Bill Viola", "#5B6B2E"),
    "First floor · The 16th century": ("The 16th century", "Parmigianino, Rosso, Bronzino", "#A4581B"),
    "First floor · Venice and the Verone": ("Venice and the Verone", "Titian, Veronese, the Verone", "#3D5A80"),
    "First floor · The 17th century": ("The 17th century", "Caravaggio, Artemisia, Rembrandt", "#6A3A6B"),
    "Closing": ("The way out", "Magliabechi staircase", "#6A3A6B"),
}
def section(n):
    for a, b, s in SECRANGE:
        if a <= n <= b: return s
    return PLAN_ROWS.get(n, {}).get("section", "")
def colour(n): return SECS.get(section(n), ("", "", INK))[2]
def rng(*secs):
    ns = [n for n in NUMS if section(n) in secs]; return (min(ns), max(ns)) if ns else (0, -1)

BOTTI = {"A9", "A10", "A11", "A12"}  # the museum's own sources disagree on these codes: never printed
def rcode(n):
    r = TR[n]["room"].strip()
    if "botticelli" in r.lower(): return "A11"
    if r.lower().startswith("outside"): return "OUT"
    if "magliabechi" in r.lower(): return "MAG"
    m = re.search(r"\b([A-E]\d{1,2})\b", r)
    return m.group(1) if m else r
def room_name(n):
    k = rcode(n)
    return {"OUT": "Outside", "MAG": "Magliabechi staircase"}.get(k, "Botticelli rooms" if k in BOTTI else k)
def short(n):
    t = TR[n]["title"]; x = re.sub(r"^[A-E]\d+(?:[–-][A-E]?\d+)? · ", "", t)
    return x.replace("Extra · ", "")
def floor_of(k):
    return 2 if k == "OUT" or k.startswith("A") else 1

# ---------------------------------------------------------------- geometry: pixel boxes read from the museum's map
# (research/map/p-3.png second floor, p-2.png first floor, 1300 px wide; hi-3.png for detail): x0, x1, y0, y1, kind.
# kinds: room, closed, cor (corridor), stair, lift, ctx (other parts of the building), oct (the Tribune), bot (Botticelli)
def five(x0, x1):
    w = (x1 - x0) / 5; return [(x0 + i * w, x0 + (i + 1) * w) for i in range(5)]
F2 = {
    "OUT": (470, 524, 100, 142, "ctx"), "GRAND": (558, 604, 104, 176, "stair"), "LIFTG": (527, 550, 146, 174, "lift"),
    "A1": (555, 602, 176, 216, "room"), "A3": (466, 522, 186, 216, "room"), "A6": (604, 641, 104, 172, "room"),
    "A5": (604, 641, 172, 216, "room"), "A7": (641, 712, 104, 150, "room"), "A4": (641, 730, 150, 216, "room"),
    "A8": (712, 755, 104, 150, "room"), "A9": (730, 800, 150, 216, "closed"), "A10": (755, 800, 104, 150, "bot"),
    "BOT": (800, 885, 104, 216, "bot"), "A14": (885, 926, 124, 155, "room"), "A13": (885, 945, 155, 216, "room"),
    "A15": (945, 970, 155, 216, "room"), "A16": (971, 1031, 148, 216, "oct"),
    **{f"A{17 + i}": (a, b, 155, 216, "closed") for i, (a, b) in enumerate(five(1032, 1194))},
    "A22": (1194, 1232, 150, 188, "room"), "A2": (466, 1196, 216, 258, "cor"), "A23": (1196, 1232, 188, 385, "cor"),
    "A24": (468, 1196, 340, 385, "cor"), "TERR": (400, 468, 340, 535, "ctx"), "LANZI": (508, 558, 386, 452, "stair"),
    "LIFTL": (528, 552, 470, 496, "lift"), "A42": (558, 600, 385, 440, "closed"), "A40": (600, 645, 385, 411, "closed"),
    "A41": (600, 645, 411, 440, "closed"), "A39": (700, 856, 385, 436, "room"), "A38": (856, 904, 385, 442, "room"),
    "BUON": (904, 928, 386, 470, "stair"), "LIFTB": (904, 928, 472, 498, "lift"), "A36": (928, 985, 385, 440, "closed"),
    "A37": (928, 976, 440, 500, "room"), "A35": (985, 1055, 385, 440, "room"), "A34": (1055, 1112, 385, 462, "room"),
    "A25": (1112, 1180, 385, 430, "room"), "A26": (1112, 1180, 430, 470, "room"), "A33": (1078, 1112, 462, 505, "closed"),
    "A27": (1112, 1180, 470, 510, "room"), "A32": (1078, 1112, 505, 552, "room"), "A28": (1112, 1180, 510, 552, "room"),
    "A31": (1078, 1104, 552, 590, "room"), "A29": (1104, 1145, 552, 590, "room"), "A30": (1145, 1180, 552, 590, "room"),
}
F1 = {
    "MAG": (878, 922, 28, 64, "stair"), "LIFTM": (822, 846, 30, 58, "lift"), "MAGP": (872, 928, 64, 226, "ctx"),
    "ECOR": (872, 1178, 226, 252, "ctx"),
    "E7": (940, 975, 155, 226, "room"), "E6": (975, 1010, 155, 226, "room"), "E5": (1010, 1045, 155, 226, "room"),
    "E4": (1045, 1080, 155, 226, "room"), "D27": (1178, 1222, 226, 398, "room"),
    "C3": (375, 415, 368, 420, "room"), "C2": (375, 415, 420, 450, "room"), "C1": (375, 415, 450, 622, "room"),
    "C4": (415, 450, 368, 415, "room"), "C5": (450, 478, 368, 415, "room"), "C6": (478, 525, 368, 415, "closed"),
    "C9": (525, 565, 368, 415, "closed"), "C10": (565, 620, 368, 415, "closed"), "C11": (620, 680, 368, 415, "closed"),
    "C12": (680, 738, 368, 415, "closed"), "C7": (478, 535, 415, 445, "closed"), "C8": (478, 535, 445, 485, "closed"),
    "LANZI": (445, 468, 494, 556, "stair"), "LIFTL": (420, 444, 486, 510, "lift"), "INFO": (418, 490, 560, 622, "ctx"),
    "B2": (490, 525, 522, 560, "room"), "B4": (525, 575, 536, 560, "room"), "B6": (575, 620, 536, 560, "room"),
    "B1": (490, 620, 560, 585, "room"), "B8": (620, 642, 536, 612, "room"), "B3": (490, 535, 585, 622, "room"),
    "B5": (535, 575, 585, 622, "room"), "B7": (575, 620, 585, 622, "room"),
    "DCOR": (738, 1178, 368, 398, "cor"),
    "D1": (738, 800, 398, 440, "room"), "D6": (800, 845, 398, 420, "room"), "D13": (845, 880, 398, 420, "room"),
    "D14": (880, 975, 398, 420, "room"), "D15": (975, 1080, 398, 425, "room"), "D26": (1080, 1178, 398, 420, "room"),
    "D2": (738, 790, 440, 494, "room"), "D4": (790, 820, 440, 494, "room"), "D5": (820, 845, 440, 494, "room"),
    "D3": (738, 778, 494, 510, "closed"), "D7": (845, 880, 420, 456, "room"), "D8": (845, 880, 456, 496, "room"),
    "D9": (880, 900, 420, 530, "room"), "D12": (900, 950, 420, 452, "room"), "D10": (900, 950, 452, 515, "closed"),
    "D11": (912, 950, 515, 548, "closed"), "BUON": (878, 902, 530, 564, "stair"), "LIFTB": (853, 877, 510, 538, "lift"),
    "D16": (950, 1030, 425, 495, "room"), "D17": (950, 986, 495, 548, "room"), "D18": (986, 1022, 495, 548, "room"),
    "D19": (1030, 1060, 425, 494, "room"), "D20": (1060, 1100, 420, 460, "room"), "D21": (1060, 1100, 460, 494, "room"),
    "D22": (1100, 1120, 420, 540, "room"), "D25": (1120, 1180, 420, 480, "room"), "D24": (1120, 1180, 480, 540, "room"),
    "D23": (1100, 1180, 540, 582, "room"),
}
LABEL = {"OUT": "Outside", "GRAND": "", "LANZI": "", "BUON": "", "MAG": "", "TERR": "terrace", "INFO": "Info Point",
         "A16": "A16\nTribune", "A9": "", "A10": "", "BOT": "Botticelli\nrooms", "A39": "A39 · Niobe Room",
         "A2": "A2 · Eastern Corridor", "A24": "A24 · Western Corridor", "A23": "A23", "D27": "D27–28\nVerone",
         "DCOR": "", "MAGP": "", "ECOR": "", "B1": "B1"}
# where corridor stops sit (map px), and the route: main line (dashed, arrows) and there-and-back branches (dotted)
COR_MID = {"A24": 780}
STOP_AT = {"A2": (650, 248), "A23": (1222, 296), "A24": (575, 372), "OUT": (497, 126), "MAG": (900, 46)}
ROOM_KEY = {**{k: "BOT" for k in ("A9", "A10", "A11", "A12")}, "D28": "D27"}
MAIN2 = [[(581, 112), (581, 233), (1206, 233), (1206, 356), (1146, 356), (1146, 408), (1146, 450), (1146, 490),
          (1146, 531), (1126, 571), (1092, 571), (1095, 528), (1095, 484), (1083, 424), (1083, 356), (533, 356), (533, 392)]]
SPUR2 = [[(581, 233), (494, 233)], [(1206, 233), (1213, 170)], [(930, 356), (930, 444), (946, 462)]]
MAIN1 = [[(456, 498), (456, 574), (397, 574), (397, 386), (1000, 386), (1012, 412), (1045, 452), (1080, 477),
          (1110, 500), (1140, 561), (1150, 510), (1150, 450), (1130, 409), (1199, 386), (1199, 239), (900, 239), (900, 64)]]
SPUR1 = [[(456, 574), (631, 572)], [(890, 386), (890, 437), (925, 437)], [(770, 386), (770, 465), (805, 465)],
         [(822, 386), (832, 466)], [(1012, 412), (990, 460)], [(1045, 440), (1080, 440)]]

STOPS = {}
for n in NUMS:
    k = rcode(n); k = ROOM_KEY.get(k, k); STOPS.setdefault(k, []).append(n)
for k in STOPS:
    if k not in F2 and k not in F1: print(f"warning: no place on the plan for {k} (stops {STOPS[k]})")

def esc(s): return html.escape(s, quote=True)
_uid = [0]

def plan_svg(rooms, crop, main, spurs, width_mm, max_h_mm, sy=1.0, show=(1, 999), notes=(), overview=False,
             river=True, texts=()):
    """Draw one floor. crop = (x0, x1, y0, y1) in map px. Returns (svg, P) where P maps map px -> svg mm."""
    _uid[0] += 1; u = _uid[0]
    cx0, cx1, cy0, cy1 = crop; pad = 1.2
    S = min((width_mm - 2 * pad) / (cx1 - cx0), (max_h_mm - 2 * pad) / ((cy1 - cy0) * sy)); Sy = S * sy
    W = (cx1 - cx0) * S + 2 * pad; H = (cy1 - cy0) * Sy + 2 * pad
    def P(x, y): return pad + (x - cx0) * S, pad + (y - cy0) * Sy
    STP = {k: [n for n in v if show[0] <= n <= show[1]] for k, v in STOPS.items() if k in rooms}
    STP = {k: v for k, v in STP.items() if v}
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.2f} {H:.2f}" width="{W:.2f}mm" height="{H:.2f}mm">',
         f'<defs><clipPath id="c{u}"><rect x="0" y="0" width="{W:.2f}" height="{H:.2f}" rx="2"/></clipPath>'
         f'<pattern id="h{u}" width="1.3" height="1.3" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
         f'<rect width="1.3" height="1.3" fill="#E6E0D6"/><line x1="0" y1="0" x2="0" y2="1.3" stroke="#B9AF9F" stroke-width=".45"/></pattern></defs>',
         f'<g clip-path="url(#c{u})">']
    # courtyard and river
    if river:
        rx, _ = P(1242, 0); o.append(f'<rect x="{rx:.2f}" y="0" width="{W - rx + 2:.2f}" height="{H:.2f}" fill="{RIVER}"/>')
        o.append(f'<text transform="translate({rx + (W - rx) / 2 + 1.1:.2f} {H / 2:.2f}) rotate(90)" class="riv">ARNO</text>')
    for x, y, t, cls in texts:
        X, Y = P(x, y); o.append(f'<text x="{X:.2f}" y="{Y:.2f}" class="{cls}">{esc(t)}</text>')
    labels, dots = [], []
    for k, (x0, x1, y0, y1, kind) in rooms.items():
        X, Y = P(x0, y0); Wd, Hd = (x1 - x0) * S, (y1 - y0) * Sy
        gk = "BOT" if kind == "bot" else k   # the Botticelli rooms are drawn as one group
        has = gk in STP; anyst = gk in STOPS
        col = colour(STP[gk][0]) if has else (colour(STOPS[gk][0]) if anyst else None)
        if kind == "stair":
            o.append(f'<rect x="{X:.2f}" y="{Y:.2f}" width="{Wd:.2f}" height="{Hd:.2f}" rx=".5" fill="#FBF3DF" stroke="{GOLD}" stroke-width=".35"/>')
            step = 1.0 if not overview else .8; i = Y + step
            while i < Y + Hd - .3:
                o.append(f'<line x1="{X + .4:.2f}" y1="{i:.2f}" x2="{X + Wd - .4:.2f}" y2="{i:.2f}" stroke="{GOLD}" stroke-opacity=".55" stroke-width=".22"/>'); i += step
        elif kind == "lift":
            o.append(f'<rect x="{X:.2f}" y="{Y:.2f}" width="{Wd:.2f}" height="{Hd:.2f}" rx=".5" fill="#D9E8EE" stroke="#7FA3B3" stroke-width=".3"/>')
            if not overview:
                fs = min(2.0, Wd / 2.4)
                o.append(f'<text x="{X + Wd / 2:.2f}" y="{Y + Hd / 2 + fs * .36:.2f}" class="rn" style="font-size:{fs:.2f}px;fill:#3E6B7D;font-weight:700">lift</text>')
            continue
        elif kind == "closed":
            o.append(f'<rect x="{X:.2f}" y="{Y:.2f}" width="{Wd:.2f}" height="{Hd:.2f}" fill="url(#h{u})" stroke="#CFC6B6" stroke-width=".25"/>')
        elif kind == "ctx":
            if overview and k == "OUT": continue
            o.append(f'<rect x="{X:.2f}" y="{Y:.2f}" width="{Wd:.2f}" height="{Hd:.2f}" rx=".6" fill="{CTX}" stroke="none"/>')
        elif kind == "cor":
            fill = "#EFE7D8" if not has else "#FFFFFF"
            o.append(f'<rect x="{X:.2f}" y="{Y:.2f}" width="{Wd:.2f}" height="{Hd:.2f}" fill="{fill}" stroke="#D3C8B5" stroke-width=".25"/>')
        else:
            if overview and col: fill, stroke, sw = col, col, .25
            elif has: fill, stroke, sw = "#FFFFFF", col, .55
            elif anyst: fill, stroke, sw = "#F7F1E6", "#CDBFA8", .3
            else: fill, stroke, sw = "#F1EBDF", "#D8CEBD", .25
            op = ' fill-opacity=".22"' if overview and col else ""
            if kind == "oct":
                c = min(Wd, Hd) * .28
                pts = [(X + c, Y), (X + Wd - c, Y), (X + Wd, Y + c), (X + Wd, Y + Hd - c), (X + Wd - c, Y + Hd), (X + c, Y + Hd), (X, Y + Hd - c), (X, Y + c)]
                o.append(f'<polygon points="{" ".join(f"{a:.2f},{b:.2f}" for a, b in pts)}" fill="{fill}"{op} stroke="{stroke}" stroke-width="{sw}"/>')
            else:
                o.append(f'<rect x="{X:.2f}" y="{Y:.2f}" width="{Wd:.2f}" height="{Hd:.2f}" rx=".5" fill="{fill}"{op} stroke="{stroke}" stroke-width="{sw}"/>')
        # label
        lab = LABEL.get(k, k)
        if kind == "bot" and k != "BOT": lab = ""
        if overview and kind not in ("bot",) and k not in ("A16", "A39"): lab = "" if kind != "ctx" else ""
        if overview and k == "A39": lab = "Niobe"
        if overview and k == "A16": lab = "Tribune"
        if kind == "closed" and Wd < 6: lab = lab  # small closed rooms keep their code
        if not lab or x0 < cx0 or x1 > cx1 or y0 < cy0 or y1 > cy1: continue
        lines = lab.split("\n"); fs = (1.55 if overview else (2.35 if has else 1.9))
        if kind == "cor": fs = 1.9 if not overview else 1.4
        if kind == "bot" and not overview: fs = 2.4
        tw = max(len(l) for l in lines) * fs * .56
        bold = has or kind in ("bot", "oct")
        fillc = INK if has else ("#8F8473" if kind != "closed" else "#8F8473")
        if kind == "bot": fillc = RED if not overview else RED
        style = f"font-size:{fs:.2f}px;fill:{fillc};font-weight:{700 if bold else 500}"
        if kind == "cor" and Hd > Wd * 2:   # vertical corridor: label upright near the top
            o_ = (X + Wd / 2, Y + fs * 1.1); labels.append(f'<text x="{o_[0]:.2f}" y="{o_[1]:.2f}" class="rn lb" style="{style}">{esc(lab)}</text>')
            continue
        if kind == "cor":
            if k in COR_MID:
                lx, _ = P(COR_MID[k], 0)
                labels.append(f'<text x="{lx:.2f}" y="{Y + fs * 1.15:.2f}" class="rn lb" style="{style}">{esc(lab)}</text>')
            else:
                labels.append(f'<text x="{X + Wd - 1.2:.2f}" y="{Y + Hd - 1.1:.2f}" class="rn lb" style="{style};text-anchor:end">{esc(lab)}</text>')
            continue
        if tw > Wd - .6 and Hd > Wd * 1.3 and len(lines) == 1:   # narrow, tall room: write upright
            fs2 = min(fs, (Hd - 1) / (len(lab) * .6)); style = style.replace(f"font-size:{fs:.2f}px", f"font-size:{fs2:.2f}px")
            labels.append(f'<text transform="translate({X + fs2 * .95:.2f} {Y + .8:.2f}) rotate(90)" class="lb" style="{style};text-anchor:start">{esc(lab)}</text>')
            rooms_lab = ("left", fs2 * 1.3)
        else:
            if tw > Wd - .6:
                fs = max(1.1, (Wd - .6) / (max(len(l) for l in lines) * .56)); style = re.sub(r"font-size:[\d.]+px", f"font-size:{fs:.2f}px", style)
            for i, l in enumerate(lines):
                labels.append(f'<text x="{X + Wd / 2:.2f}" y="{Y + fs * (1.05 + i * 1.08):.2f}" class="rn lb" style="{style}">{esc(l)}</text>')
    # route
    def poly(pts, main_line):
        q = [P(*p) for p in pts]; d = "M" + " L".join(f"{a:.2f},{b:.2f}" for a, b in q)
        if main_line:
            o.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-opacity=".6" stroke-width="{.55 if not overview else .5}" stroke-dasharray="1.4,.9" stroke-linecap="round" stroke-linejoin="round"/>')
            for (xa, ya), (xb, yb) in zip(q, q[1:]):
                L = math.hypot(xb - xa, yb - ya)
                if L < (9 if not overview else 7): continue
                for f_ in ((.5,) if L < 40 else (.3, .7)):
                    mx, my = xa + (xb - xa) * f_, ya + (yb - ya) * f_; a = math.degrees(math.atan2(yb - ya, xb - xa)); kk = 1.05
                    o.append(f'<path d="M{-kk:.2f},{-kk * .8:.2f} L{kk:.2f},0 L{-kk:.2f},{kk * .8:.2f} Z" fill="{INK}" fill-opacity=".75" transform="translate({mx:.2f},{my:.2f}) rotate({a:.1f})"/>')
        else:
            o.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-opacity=".45" stroke-width=".4" stroke-dasharray=".2,.8" stroke-linecap="round"/>')
    for s in spurs: poly(s, False)
    for m_ in main: poly(m_, True)
    o.extend(labels)
    # stops
    if not overview:
        for k, st in STP.items():
            x0, x1, y0, y1, kind = rooms[k]
            if k in STOP_AT:
                cx, cy = P(*STOP_AT[k]); n = len(st); rad = 2.3
                pos = [(cx + (i - (n - 1) / 2) * rad * 2.25, cy) for i in range(n)]
            else:
                X, Y = P(x0, y0); Wd, Hd = (x1 - x0) * S, (y1 - y0) * Sy
                lab = LABEL.get(k, k); nl = len(lab.split("\n")) if lab else 0
                fsl = 2.4 if kind == "bot" else 2.35
                band = (fsl * (0.35 + 1.08 * nl)) if nl else 0
                narrow = lab and len(lab.split("\n")[0]) * fsl * .56 > Wd - .6 and Hd > Wd * 1.3 and nl == 1
                ax, ay, aw, ah = (X + (fsl * 1.3 if narrow else 0), Y + (0 if narrow else band), Wd - (fsl * 1.3 if narrow else 0), Hd - (0 if narrow else band))
                n = len(st); best = None
                for cols in range(1, n + 1):
                    rows = math.ceil(n / cols); r = min(2.6, aw / (2.3 * cols), ah / (2.3 * rows))
                    if best is None or r > best[0] + 1e-6: best = (r, cols, rows)
                rad, cols, rows = best
                if rad < 1.5:   # too tight below the label: use the whole room
                    ax, ay, aw, ah = X, Y, Wd, Hd; best = None
                    for cols in range(1, n + 1):
                        rows = math.ceil(n / cols); r = min(2.6, aw / (2.3 * cols), ah / (2.3 * rows))
                        if best is None or r > best[0] + 1e-6: best = (r, cols, rows)
                    rad, cols, rows = best
                gap = rad * 2.25; pos = []
                for i in range(n):
                    r_, c_ = divmod(i, cols); inrow = min(cols, n - r_ * cols)
                    pos.append((ax + aw / 2 + (c_ - (inrow - 1) / 2) * gap, ay + ah / 2 + (r_ - (rows - 1) / 2) * gap))
            for (cx, cy), s in zip(pos, st):
                c = colour(s)
                if s in XS:
                    dots.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{rad * .95:.2f}" fill="#fff" stroke="{c}" stroke-width="{rad * .2:.2f}"/>'
                                f'<text x="{cx:.2f}" y="{cy + rad * .34:.2f}" class="sn" style="font-size:{rad * .92:.2f}px;fill:{c}">{s}</text>')
                else:
                    dots.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{rad:.2f}" fill="{c}" stroke="#fff" stroke-width="{rad * .12:.2f}"/>'
                                f'<text x="{cx:.2f}" y="{cy + rad * .34:.2f}" class="sn" style="font-size:{rad * .95:.2f}px">{s}</text>')
    o.extend(dots)
    for key, text, kind, dx, dy in notes:
        if isinstance(key, tuple): cx, cy = P(*key)
        else:
            x0, x1, y0, y1, _ = rooms[key]; cx, cy = P((x0 + x1) / 2, (y0 + y1) / 2)
        colr = {"start": INK, "finish": INK, "down": GOLD, "info": MUTED, "warn": RED}[kind]
        fs = 2.5 if not overview else 2.3; lines = text.split("\n"); wmax = max(len(l) for l in lines) * fs * .55 + fs * 1.6
        hb = fs * 1.38 * len(lines) + fs * .62; tx, ty = cx + dx, cy + dy
        bx = min(max(tx - wmax / 2, .8), W - wmax - .8); by = min(max(ty - hb / 2, .8), H - hb - .8)
        o.append(f'<line x1="{cx:.2f}" y1="{cy:.2f}" x2="{bx + wmax / 2:.2f}" y2="{by + hb / 2:.2f}" stroke="{colr}" stroke-width=".35" stroke-dasharray="1,.7"/>')
        o.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r=".75" fill="{colr}"/>')
        o.append(f'<rect x="{bx:.2f}" y="{by:.2f}" width="{wmax:.2f}" height="{hb:.2f}" rx="{min(hb / 2, 2):.2f}" fill="{colr}"/>')
        for i, l in enumerate(lines):
            o.append(f'<text x="{bx + fs * .8:.2f}" y="{by + fs * 1.22 + i * fs * 1.38:.2f}" class="note" style="font-size:{fs:.2f}px">{esc(l)}</text>')
    o.append("</g></svg>")
    return "".join(o), P, (W, H)

# ---------------------------------------------------------------- stop lists (floor pages) and the stop table
def dot(n, cls="dot"):
    c = colour(n)
    if n in XS: return f'<span class="{cls} hol" style="color:{c};border-color:{c}">{n}</span>'
    return f'<span class="{cls}" style="background:{c}">{n}</span>'
def stop_list(first, last):
    rows = []
    for n in NUMS:
        if not first <= n <= last: continue
        c = colour(n); x = ' x' if n in XS else ''
        ex = f'<i style="color:{c}">Extra</i> ' if n in XS else ''
        rows.append(f'<div class="row{x}">{dot(n)}<span class="rm">{esc(room_name(n))}</span><span class="tt">{ex}{esc(short(n))}</span></div>')
    return "".join(rows)

# ---------------------------------------------------------------- page 1: the two floors, second floor on top
F2_CROP, F1_CROP = (395, 1262, 96, 598), (365, 1262, 22, 628)
def overview_svg():
    W = 182.0
    s2, P2, (w2, h2) = plan_svg(F2, F2_CROP, MAIN2, SPUR2, 160, 72, overview=True,
        notes=[("GRAND", "START · up the Granducal staircase", "start", 30, -2), ((533, 420), "DOWN the Lanzi staircase\nONE floor only", "down", 34, 6)],
        texts=[(820, 300, "Uffizi courtyard", "yard"), (405, 300, "Piazza della Signoria ←", "side")])
    s1, P1, (w1, h1) = plan_svg(F1, F1_CROP, MAIN1, SPUR1, 160, 80, overview=True,
        notes=[((922, 46), "OUT · Magliabechi staircase\ndown to the ground floor", "finish", 30, 3)],
        texts=[(760, 310, "Uffizi courtyard", "yard")])
    x2 = 18 + (W - 18 - w2) / 2; x1 = 18 + (W - 18 - w1) / 2; y2 = 1.5; y1 = y2 + h2 + 7
    H = y1 + h1 + 1.5
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H:.1f}" width="{W}mm" height="{H:.1f}mm">']
    o.append(f'<text x="10" y="{y2 + h2 / 2 + 1:.1f}" class="fl">2</text><text x="10" y="{y2 + h2 / 2 + 5:.1f}" class="fls">second floor</text>')
    o.append(f'<text x="10" y="{y1 + h1 / 2 + 1:.1f}" class="fl">1</text><text x="10" y="{y1 + h1 / 2 + 5:.1f}" class="fls">first floor</text>')
    o.append(f'<svg x="{x2:.2f}" y="{y2:.2f}" width="{w2:.2f}" height="{h2:.2f}" viewBox="0 0 {w2:.2f} {h2:.2f}">{s2[s2.index(">") + 1:]}')
    o.append(f'<svg x="{x1:.2f}" y="{y1:.2f}" width="{w1:.2f}" height="{h1:.2f}" viewBox="0 0 {w1:.2f} {h1:.2f}">{s1[s1.index(">") + 1:]}')
    # the Lanzi staircase links the two floors
    ax, ay = P2(533, 452); bx, by = P1(456, 494); ax += x2; ay += y2; bx += x1; by += y1
    o.append(f'<path d="M{ax:.2f},{ay:.2f} C{ax:.2f},{ay + 6:.2f} {bx:.2f},{by - 8:.2f} {bx:.2f},{by - 1.6:.2f}" fill="none" stroke="{GOLD}" stroke-width=".9" stroke-dasharray="1.6,1.1"/>')
    o.append(f'<path d="M-1.8,-2.4 L0,1.4 L1.8,-2.4 Z" fill="{GOLD}" transform="translate({bx:.2f} {by - .6:.2f})"/>')
    my = (ay + by) / 2; mx = min(ax, bx) - 2
    o.append(f'<text x="{mx:.2f}" y="{my - 1:.2f}" class="up" style="text-anchor:end">Lanzi staircase</text><text x="{mx:.2f}" y="{my + 2.2:.2f}" class="up" style="text-anchor:end">one floor down</text>')
    o.append("</svg>")
    return "".join(o)

pages = []
lens = "".join(f'<div class="card"><div class="cnum" style="background:{NAVY}">{i}</div>'
               f'<div class="cbody"><div class="ct">{esc(n)}</div><div class="cs"><b>{esc(m)}</b> · {k} tracks</div><div class="cs2">{esc(d)}</div></div></div>'
               for i, (n, k, m, d) in enumerate(LENGTHS, 1))
pages.append(f'''<section class="page">
 <header><div class="brand">YO TOURS · AUDIO GUIDE</div><h1>Uffizi Gallery</h1>
 <p class="lede">From gold-ground Madonnas to Caravaggio, on two floors: {len(NUMS) - len(XS)} main stops plus {len(XS)} short Extras, in one walking order. The guide comes in three lengths.</p></header>
 <div class="how"><div><b>1</b> Rooms carry the museum's codes: A on the second floor, B to E on the first. Every stop on these plans sits in its room.</div>
 <div><b>2</b> Play the stops in number order. Hollow circles are short, optional Extras. Hatched rooms are closed or work in progress.</div>
 <div><b>3</b> Each stop ends by naming the next room. In Essential and Highlights a short line tells you the next stop.</div></div>
 <div class="ov">{overview_svg()}</div>
 <div class="warn"><b>At the Lanzi staircase go down one floor only.</b> The stairs go on to the street, and once you are out you cannot come back in to the cloakroom or the audioguide desk. The way out is at the end, by the Magliabechi staircase.</div>
 <div class="cards">{lens}</div>
 <footer>{esc(FOOTER)}</footer>
</section>''')

LEGEND = (f'<div class="legend"><span>{dot(1, "ldot")} stop</span><span><span class="ldot hol" style="color:{INK};border-color:{INK}">X</span> Extra</span>'
          f'<span><svg width="9mm" height="3mm" viewBox="0 0 9 3"><path d="M.5,1.5 L8.5,1.5" stroke="{INK}" stroke-opacity=".6" stroke-width=".55" stroke-dasharray="1.4,.9"/></svg> route</span>'
          f'<span><svg width="9mm" height="3mm" viewBox="0 0 9 3"><path d="M.5,1.5 L8.5,1.5" stroke="{INK}" stroke-opacity=".5" stroke-width=".45" stroke-dasharray=".2,.8" stroke-linecap="round"/></svg> there and back</span>'
          f'<span><i class="sw hatch"></i> closed / work in progress</span><span><i class="sw st"></i> stairs</span><span><i class="sw lift"></i> lift</span></div>')

def floor_page(title, sub, svg, first, last, kicker):
    return f'''<section class="page">
 <header class="fh"><div class="brand">YO TOURS · UFFIZI GALLERY · {esc(kicker)}</div>
 <h2>{esc(title)}</h2><p class="sub">{esc(sub)}</p></header>
 <div class="stack"><div class="plan">{svg}{LEGEND}</div><div class="list">{stop_list(first, last)}</div></div>
 <footer>{esc(FOOTER)}</footer>
</section>'''

# page 2: second floor, east wing and the Tribune
S2 = [s for _, _, s in SECRANGE]
a, b = rng("Opening", S2[1], S2[2], S2[3]); b = 23 if 23 in TR else b
svg, _, _ = plan_svg(F2, (440, 1262, 60, 368), MAIN2, SPUR2, 182, 112, sy=1.6, show=(a, b),
    notes=[((581, 104), "START · up the Granducal staircase", "start", 30, -6.2)],
    texts=[(445, 300, "← Piazza della Signoria", "side"), (760, 305, "Uffizi courtyard", "yard")])
pages.append(floor_page("Second floor · East wing and the Tribune",
    f"Start outside (stop 1), go up the Granducal staircase to the Lorenese Vestibule, A1, and out into the Eastern Corridor. "
    f"The rooms open off the side away from the courtyard windows. The Botticelli rooms come after A8; follow the museum's signs into them. "
    f"Rooms A17–A21 are closed. Stops {a}–{b}.", svg, a, b, "SECOND FLOOR"))
# page 3: second floor, west wing and down the Lanzi staircase
a, b = rng(S2[4], S2[5]); a = 24 if 24 in TR else a
svg, _, _ = plan_svg(F2, (468, 1262, 318, 598), MAIN2, SPUR2, 182, 130, sy=2.0, show=(a, b),
    notes=[((533, 430), "DOWN the Lanzi staircase\nONE floor only", "down", 30, 30), ((1206, 330), "from the Eastern Corridor", "info", -22, -1.5)],
    texts=[(760, 320, "Uffizi courtyard", "yard")])
pages.append(floor_page("Second floor · West wing, Leonardo to Michelangelo",
    f"Round the Southern Corridor, A23, into the Western Corridor, A24: the rooms are on your left. "
    f"Loop through A25 to A32 and back out by A34; if A33 is shut, walk back the way you came. Then A35, the Cabinet of Marbles by the Buontalenti staircase, "
    f"A38 and the Niobe Room. Stops {a}–{b}.", svg, a, b, "SECOND FLOOR"))
# page 4: first floor, Contini Bonacossi, self-portraits, the 16th century
S1 = S2
a, b = rng(S1[6], S1[7], S1[8])
svg, _, _ = plan_svg(F1, (360, 1112, 356, 632), MAIN1, SPUR1, 182, 134, sy=2.0, show=(a, b), river=False,
    notes=[("LANZI", "Arrive down the\nLanzi staircase", "down", 22, -10)],
    texts=[(780, 365, "", "yard")])
pages.append(floor_page("First floor · From Contini to Bronzino",
    f"At the foot of the Lanzi staircase walk the hall of the Contini Bonacossi rooms, B1, to B8 and back. Then up through the self-portraits, C1–C5, "
    f"straight on through C6–C12 (being rehung) to D1, and along the corridor of the D rooms, with a short passage, D9, down to D12. Stops {a}–{b}.",
    svg, a, b, "FIRST FLOOR"))
# page 5: first floor, Venice, the Verone, the 17th century and out
a, b = rng(S1[9], S1[10], "Closing")
svg, _, _ = plan_svg(F1, (812, 1262, 18, 596), MAIN1, SPUR1, 182, 142, sy=0.6, show=(a, b),
    notes=[((922, 46), "OUT · Magliabechi staircase\n(and lift) to the ground floor", "finish", 40, 2), ((955, 386), "from D15", "info", 2, -12)],
    texts=[(1060, 320, "Uffizi courtyard", "yard")])
pages.append(floor_page("First floor · Venice, the Verone and Caravaggio",
    f"From D19 through D20 and D21 to Titian's Venus in D23, round to D26 and up the Verone, the covered loggia on the Arno. "
    f"Then along to E4–E7 and out by the Magliabechi staircase. Stops {a}–{b}.", svg, a, b, "FIRST FLOOR"))

# pages 6+: the stop table
rows = []; last_sec = None
for n in NUMS:
    s = section(n)
    if s != last_sec:
        rows.append(("sec", s)); last_sec = s
    rows.append(("stop", n))
chunks, cur = [], []
for r in rows:
    PER = 40 if not chunks else 44   # the first table page carries the introduction
    if len(cur) >= PER or (r[0] == "sec" and len(cur) >= PER - 2):
        chunks.append(cur); cur = []
    cur.append(r)
chunks.append(cur)
tot = {k: sum(minutes(n) for n in NUMS if f(n)) for k, f in (("F", lambda n: True), ("E", lambda n: n in E_SET), ("H", lambda n: n in H_SET))}
for i, ch in enumerate(chunks):
    trs = []
    for kind, v in ch:
        if kind == "sec":
            c = SECS.get(v, ("", "", INK))[2]
            trs.append(f'<tr class="sh"><td colspan="7" style="color:{c};border-bottom-color:{c}">{esc(v)}</td></tr>')
        else:
            n = v; x = ' class="x"' if n in XS else ''
            ex = f'<i style="color:{colour(n)}">Extra</i> ' if n in XS else ''
            mk = lambda on: '<span class="mk">●</span>' if on else '<span class="no">·</span>'
            trs.append(f'<tr{x}><td>{dot(n)}</td><td class="rm">{esc(room_name(n))}</td><td class="tt">{ex}{esc(short(n))}</td>'
                       f'<td class="mn">{fmt_min(minutes(n))}</td><td>{mk(True)}</td><td>{mk(n in E_SET)}</td><td>{mk(n in H_SET)}</td></tr>')
    if i == len(chunks) - 1:
        trs.append(f'<tr class="tot"><td colspan="3">Tracks · listening minutes (walking comes on top)</td><td class="mn"></td>'
                   f'<td>{len(NUMS)}<br><span>{round(tot["F"])}′</span></td><td>{len(E_SET)}<br><span>{round(tot["E"])}′</span></td><td>{len(H_SET)}<br><span>{round(tot["H"])}′</span></td></tr>')
    head = ('<tr class="th"><th>#</th><th>Room</th><th>Stop</th><th>Min</th><th>Full</th><th>Essen&shy;tial</th><th>High&shy;lights</th></tr>')
    pages.append(f'''<section class="page">
 <header class="fh"><div class="brand">YO TOURS · UFFIZI GALLERY · ALL STOPS</div>
 <h2>The stops{" (continued)" if i else ""}</h2>
 {"" if i else f'<p class="sub">Every track in walking order, with its room, its listening time and the lengths it belongs to: Full ({LENGTHS[0][2]}), Essential ({LENGTHS[1][2]}), Highlights ({LENGTHS[2][2]}). The lengths include walking. Rooms may be rehung: if a work is not on the wall, a notice is usually in its place.</p>'}</header>
 <table class="tbl">{head}{"".join(trs)}</table>
 <footer>{esc(FOOTER)}</footer>
</section>''')

CSS = f'''
@page {{ size: A4; margin: 0 }}
* {{ box-sizing: border-box }}
html, body {{ margin: 0; background: {PAPER}; color: {INK}; font-family: Inter, "DejaVu Sans", sans-serif }}
.page {{ width: 210mm; height: 297mm; padding: 13mm 13mm 10mm; position: relative; page-break-after: always; overflow: hidden; background: {PAPER} }}
.brand {{ font: 600 7.6pt Inter; letter-spacing: .28em; color: {GOLD} }}
h1 {{ font: 700 34pt Lora, serif; margin: 2mm 0 1mm; letter-spacing: -.01em }}
h2 {{ font: 700 19pt Lora, serif; margin: 2mm 0 1.2mm }}
.lede {{ font: 400 11.5pt Lora, serif; color: {MUTED}; margin: 0 0 4mm }}
.sub {{ font: 400 9.2pt Inter; color: {MUTED}; margin: 0 0 3.5mm; max-width: 184mm; line-height: 1.4 }}
.how {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 3mm; margin-bottom: 3.5mm }}
.how div {{ background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; padding: 2.4mm 3mm; font: 500 8.2pt Inter; line-height: 1.35 }}
.how b {{ display: inline-flex; width: 5mm; height: 5mm; border-radius: 50%; background: {INK}; color: #fff; font: 700 7.5pt Inter; align-items: center; justify-content: center; margin-right: 1.5mm }}
.ov {{ background: #fff; border: .3mm solid {LINE}; border-radius: 4mm; padding: 2.5mm 1mm 2mm; margin-bottom: 3mm }}
.ov svg {{ display: block; margin: 0 auto }}
.fl {{ font: 700 9px Lora; fill: {INK}; text-anchor: middle }} .fls {{ font: 600 2.2px Inter; fill: {MUTED}; text-anchor: middle; letter-spacing: .1px }}
.up {{ font: 700 2.5px Inter; fill: {GOLD} }}
.warn {{ background: #fff; border: .3mm solid {GOLD}; border-left: 1.6mm solid {GOLD}; border-radius: 2.4mm; padding: 2.2mm 3mm; font: 400 8.2pt Inter; line-height: 1.38; margin-bottom: 3mm }}
.cards {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.4mm }}
.card {{ display: grid; grid-template-columns: 10mm 1fr; align-items: center; background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; overflow: hidden; padding: 2mm 2mm 2mm 0 }}
.cnum {{ width: 7mm; height: 7mm; border-radius: 50%; color: #fff; font: 700 11pt Inter; display: flex; align-items: center; justify-content: center; margin-left: 2mm }}
.ct {{ font: 700 10.2pt Lora; margin-bottom: .4mm }} .cs {{ font: 400 7.9pt Inter; color: {MUTED} }} .cs b {{ color: {INK} }}
.cs2 {{ font: 400 7pt Inter; color: {MUTED}; margin-top: .4mm; line-height: 1.3 }}
footer {{ position: absolute; left: 13mm; right: 13mm; bottom: 7mm; font: 400 7pt Inter; color: {MUTED}; border-top: .3mm solid {LINE}; padding-top: 2mm }}
.stack .plan {{ margin-bottom: 3.5mm }} .stack .list {{ columns: 2; column-gap: 7mm }} .stack .row {{ break-inside: avoid }}
.plan {{ background: #fff; border: .3mm solid {LINE}; border-radius: 4mm; padding: 2mm }}
.plan svg {{ display: block; margin: 0 auto }}
.rn {{ font-family: Inter; text-anchor: middle }} .sn {{ font-family: Inter; font-weight: 700; fill: #fff; text-anchor: middle }}
.lb {{ font-family: Inter; paint-order: stroke; stroke: #fff; stroke-width: .5px; stroke-linejoin: round }}
.note {{ font-family: Inter; font-weight: 600; fill: #fff }}
.riv {{ font: 700 2.3px Inter; fill: #5E8797; letter-spacing: .9px; text-anchor: middle }}
.yard {{ font: 600 2.4px Inter; fill: #A39886; text-anchor: middle; letter-spacing: .5px; text-transform: uppercase }}
.side {{ font: 600 2.2px Inter; fill: #A39886; letter-spacing: .2px }}
.legend {{ display: flex; flex-wrap: wrap; gap: 1.2mm 4.5mm; justify-content: center; padding: 2mm 1mm .4mm; font: 500 7pt Inter; color: {MUTED}; align-items: center }}
.legend > span {{ display: inline-flex; align-items: center; gap: 1.3mm }}
.ldot {{ width: 4.4mm; height: 4.4mm; border-radius: 50%; color: #fff; font: 700 6pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.sw {{ display: inline-block; width: 5mm; height: 3.4mm; border-radius: .6mm }}
.sw.hatch {{ background: repeating-linear-gradient(45deg, #E6E0D6 0 .55mm, #B9AF9F .55mm .8mm); border: .2mm solid #CFC6B6 }}
.sw.st {{ background: repeating-linear-gradient(0deg, #FBF3DF 0 .7mm, #D8C398 .7mm .9mm); border: .25mm solid {GOLD} }}
.sw.lift {{ background: #D9E8EE; border: .25mm solid #7FA3B3 }}
.list .row {{ display: grid; grid-template-columns: 7.5mm 23mm 1fr; align-items: center; padding: .8mm 0; border-bottom: .25mm solid {LINE} }}
.dot {{ width: 6mm; height: 6mm; border-radius: 50%; color: #fff; font: 700 7.6pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.rm {{ font: 600 7.2pt Inter; color: {MUTED} }} .hol {{ background: #fff; border: .45mm solid; box-sizing: border-box }}
.row.x .tt {{ color: {MUTED} }} .tt i {{ font-style: normal; font-weight: 700; font-size: 7pt; letter-spacing: .04em; margin-right: 1mm }} .tt {{ font: 500 7.9pt Inter; line-height: 1.28 }}
.tbl {{ width: 100%; border-collapse: collapse; background: #fff; border: .3mm solid {LINE}; border-radius: 3mm }}
.tbl th {{ font: 700 6.6pt Inter; color: {MUTED}; text-align: left; padding: 1.6mm 1.2mm 1.2mm; border-bottom: .35mm solid {INK}; letter-spacing: .04em; text-transform: uppercase }}
.tbl th:nth-child(n+4) {{ text-align: center; width: 13mm }} .tbl th:first-child {{ width: 9mm; padding-left: 2mm }} .tbl th:nth-child(2) {{ width: 27mm }}
.tbl td {{ padding: .15mm 1.2mm; line-height: 1.12; border-bottom: .2mm solid {LINE}; vertical-align: middle }}
.tbl td:first-child {{ padding-left: 2mm }} .tbl td:nth-child(n+4) {{ text-align: center }}
.tbl .dot {{ width: 4mm; height: 4mm; font-size: 6pt; vertical-align: middle }}
.tbl .tt {{ font: 500 7.7pt Inter }} .tbl .rm {{ font: 600 7pt Inter }} .tbl tr.x .tt {{ color: {MUTED} }}
.tbl .mn {{ font: 600 7.4pt Inter; color: {INK} }} .mk {{ color: {NAVY}; font-size: 8.4pt }} .no {{ color: #C9BFAE }}
.tbl tr.sh td {{ font: 700 7.4pt Inter; padding: 1.6mm 2mm .6mm; border-bottom: .3mm solid; letter-spacing: .02em }}
.tbl tr.tot td {{ font: 700 7.6pt Inter; border-top: .35mm solid {INK}; border-bottom: none; padding: 1.6mm 1.2mm 1.6mm 2mm }} .tbl tr.tot span {{ font-weight: 500; color: {MUTED} }}
'''
doc = f'<!doctype html><html><head><meta charset="utf-8"><title>Uffizi Gallery · Yo Tours route</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
os.makedirs(B, exist_ok=True)
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
print(f"stops: {len(NUMS)} ({N_TRACK} from track files, {len(NUMS) - N_TRACK} from PLAN)")
print("OK ->", OUT_PDF, len(pages), "pages")
