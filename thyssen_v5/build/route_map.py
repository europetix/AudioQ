#!/usr/bin/env python3
"""Yo Tours · Museo Nacional Thyssen-Bornemisza — route map, edition of 23 Oct 2026.
A PDF made to be read on a phone: page 1 = the visit as three levels, top down, with chapters and the three lengths;
then one plan per part of the route, every stop as a numbered circle (hollow = Extra), the path with arrows, the stairs and
lifts, and a stop list. Our own schematic drawing after the museum's visitor map (Dec 2025, source/FolletoThyssen_EN_map.pdf);
not to scale. Driven by plan.json, so the stop numbers always match the audio files.
Usage: python3 route_map.py <bundle folder> [--png <dir>]   -> <bundle>/Thyssen_Audio_Guide_Route.pdf"""
import json, math, os, re, sys, html, asyncio

B = sys.argv[1]
PNG_DIR = sys.argv[sys.argv.index("--png") + 1] if "--png" in sys.argv else None
plan = json.load(open(os.path.join(B, "plan.json"), encoding="utf-8")); TR = plan["tracks"]
XS = {int(t["seq"]) for t in TR if t.get("register") == "X"}
MAIN = len(TR) - len(XS)
OUT_PDF = os.path.join(B, "Thyssen_Audio_Guide_Route.pdf")

# ---------------------------------------------------------------- palette & chapters (from the @section of each track)
PAPER, INK, MUTED, LINE, CTX = "#F6F1E7", "#1F1B17", "#776E62", "#D8CEBD", "#ECE5D7"
RED, GOLD, NAVY = "#B0281C", "#A9812F", "#1D2B4A"
SECS = [  # (@section, short title, subtitle, colour)
    ("Opening", "Welcome", "", "#3D3A36"),
    ("Level 2 · The first faces", "The first faces", "Duccio, Daret, the first portraits", "#8C6A2E"),
    ("Level 2 · Renaissance portraits and the Villahermosa Gallery", "Renaissance portraits", "Ghirlandaio, Holbein, Carpaccio, Cranach, Patinir", "#9A4E2C"),
    ("Level 2 · Venice and the Baroque", "Venice and the Baroque", "El Greco, Titian, Caravaggio, Zurbarán", RED),
    ("Level 2 · The 18th century in Italy", "The 18th century in Italy", "Piazzetta, Canaletto, Tiepolo", "#7A3A5E"),
    ("Level 2 · The Dutch Golden Age and the French salon", "The Dutch Golden Age", "Hals, Fragonard, Moillon, Rembrandt, Ruisdael", "#2C4A6E"),
    ("Level 2 · Goya's century without Goya", "Romanticism", "Friedrich, Delacroix", "#3D5A80"),
    ("Level 1 · America and the Impressionists", "America, Impressionists", "Church, Sargent, Morisot, Pissarro", "#2E6A62"),
    ("Level 1 · Expressionism and the avant-gardes", "Expressionism to Cubism", "Van Gogh, Münter, Kandinsky, Picasso, Sonia Delaunay", "#5B6B2E"),
    ("Level 1 · Surrealism, America and Pop", "Surrealism, America, Pop", "Magritte, Hopper, Pollock, O'Keeffe, Rothko, Freud", "#A4581B"),
    ("Level 0 · Carmen Thyssen collection · From Old Masters to the avant-gardes", "The Carmen Thyssen collection", "Brueghel, Van Gogh, Monet, Gauguin, Goncharova", "#6A3A6B"),
    ("Closing", "Closing", "", "#6A3A6B"),
]
SCOL = {s[0]: s[3] for s in SECS}
SEQ_SEC = {int(t["seq"]): t["section"] for t in TR}
def colour(n): return SCOL.get(SEQ_SEC.get(n), INK)
def rng(*secs):
    ns = [n for n, s in SEQ_SEC.items() if s in secs]; return min(ns), max(ns)

def short(t):
    x = re.sub(r"^Room (\d+|[A-J]) · ", "", t["title"])
    return x.replace("Extra · ", "")

def rkey(room):
    m = re.search(r"Room (\d+|[A-J])$", room); return m.group(1) if m else "HALL"
STOPS = {}
for t in TR: STOPS.setdefault(rkey(t["room"]), []).append(int(t["seq"]))

# ---------------------------------------------------------------- geometry: pixel boxes read from the museum's map pages
# (research/map/p-2.png Level 2, p-3.png Level 1, p-4.png Level 0, as rendered at 864 px wide), x0, x1, y0, y1 / 30.
def _px(x0, x1, y0, y1, u=30.0): return (x0 / u, y0 / u, (x1 - x0) / u, (y1 - y0) / u)
L2 = {k: _px(*v) for k, v in {
    "1": (124, 176, 452, 506), "2": (119, 171, 510, 558), "3": (112, 166, 562, 604), "4": (104, 158, 607, 652),
    "5": (162, 198, 607, 652), "6": (202, 472, 621, 652), "7": (205, 245, 540, 614), "8": (250, 292, 540, 614),
    "9": (297, 338, 540, 614), "10": (343, 383, 540, 614), "11": (388, 430, 580, 614), "12": (435, 474, 580, 614),
    "13": (478, 510, 620, 652), "14": (478, 510, 580, 616), "15": (478, 510, 530, 576), "16": (478, 510, 486, 526),
    "17": (435, 474, 480, 535), "18": (478, 510, 450, 482), "19": (370, 400, 437, 466), "20": (333, 368, 437, 466),
    "21": (297, 330, 437, 466), "22": (482, 510, 395, 445), "23": (487, 512, 322, 391), "24": (512, 672, 312, 340),
    "25": (515, 552, 226, 306), "26": (558, 593, 232, 306), "27": (598, 633, 240, 306), "28": (638, 673, 246, 306),
    "29": (680, 710, 258, 306), "COR2": (178, 296, 454, 468), "LIFT2W": (250, 286, 386, 434), "LIFT2E": (716, 792, 278, 314)}.items()}
L1 = {k: _px(*v) for k, v in {
    "30": (673, 708, 258, 346), "31": (633, 668, 255, 346), "32": (593, 628, 242, 346), "33": (553, 588, 242, 346),
    "34": (513, 548, 236, 346), "35": (482, 507, 326, 380), "36": (476, 507, 396, 460), "37": (476, 507, 463, 512),
    "38": (476, 507, 515, 560), "39": (476, 507, 563, 600), "40": (476, 507, 605, 655), "41": (432, 470, 600, 655),
    "42": (388, 428, 600, 655), "43": (341, 383, 545, 655), "44": (294, 336, 545, 655), "45": (248, 290, 545, 655),
    "46": (202, 243, 545, 655), "47": (158, 195, 610, 655), "48": (99, 152, 596, 655), "49": (106, 158, 556, 590),
    "50": (112, 163, 521, 550), "51": (118, 167, 486, 518), "52": (122, 175, 456, 482), "53": (294, 326, 437, 465),
    "54": (330, 362, 437, 465), "55": (366, 398, 437, 465), "56": (432, 470, 470, 535), "RODIN": (693, 722, 236, 270),
    "LIFT1E": (712, 788, 280, 316), "LIFT1W": (242, 280, 386, 436)}.items()}
L0 = {k: _px(*v) for k, v in {
    "A": (338, 378, 540, 652), "C": (293, 332, 540, 580), "B": (293, 332, 584, 652), "D": (245, 286, 540, 580),
    "E": (245, 286, 584, 652), "F": (200, 240, 540, 652), "G": (156, 193, 606, 652), "H": (104, 150, 576, 620),
    "I": (109, 156, 524, 570), "J": (115, 165, 460, 520), "HALL": (200, 500, 460, 536), "LIFT0": (216, 296, 372, 440),
    "TEMP": (510, 712, 205, 340), "GARDEN": (576, 724, 350, 608)}.items()}
L2_WAY = {"s2": (150 / 30, 430 / 30), "w2a": (494 / 30, 464 / 30), "w2b": (494 / 30, 400 / 30)}
L1_WAY = {"w1a": (493 / 30, 352 / 30), "s1": (205 / 30, 448 / 30)}
L0_WAY = {"in0": (230 / 30, 470 / 30), "ex0": (515 / 30, 503 / 30), "ac0": (385 / 30, 540 / 30)}
LABEL = {"COR2": "", "LIFT2W": "Lift", "LIFT2E": "Lift", "LIFT1E": "Lift", "LIFT1W": "Lift", "LIFT0": "Lift",
         "RODIN": "Rodin", "HALL": "Central hall", "TEMP": "Temporary exhibitions", "GARDEN": "Garden",
         "19": "19", "20": "20", "21": "21", "53": "53", "54": "54", "55": "55", "56": "56"}
PATHS = {
 "l2": ["s2", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "16", "18",
        "w2a", "22", "w2b", "23", "24", "25", "26", "27", "28", "29", "LIFT2E"],
 "l1": ["LIFT1E", "30", "31", "32", "33", "34", "w1a", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45",
        "46", "47", "48", "49", "50", "51", "52", "s1"],
 "l0": ["in0", "ac0", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "HALL", "ex0"],
}

def esc(s): return html.escape(s, quote=True)

def plan_svg(rooms, ways, path, width_mm, max_h_mm, notes=(), ends=("Back of the building", "Front · street side, glass lift towers"), show=(1, 999)):
    STP = {k: [n for n in v if show[0] <= n <= show[1]] for k, v in STOPS.items()}
    STP = {k: v for k, v in STP.items() if v}
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
    col_of = lambda k: colour(STP[k][0]) if k in STP else None
    on_path = set(path)
    # rooms first, path on top (thin), stops on top of everything
    for k, (x, y, w, h) in rooms.items():
        X, Y = P(x, y); Wd, Hd = w * S, h * S
        if k == "CLOISTER":
            out.append(f'<rect x="{X:.2f}" y="{Y:.2f}" width="{Wd:.2f}" height="{Hd:.2f}" rx="{S*.2:.2f}" fill="#E7EFE2" stroke="none"/>')
            out.append(f'<text x="{X+Wd/2:.2f}" y="{Y+Hd/2:.2f}" class="rn" style="font-size:{S*.32:.2f}px;fill:#93A58A;font-weight:600">cloister</text>'); continue
        if k == "GARDEN":
            out.append(f'<rect x="{X:.2f}" y="{Y:.2f}" width="{Wd:.2f}" height="{Hd:.2f}" rx="{S*.2:.2f}" fill="#DCEBD3" stroke="{colour(STOPS[k][0]) if k in STP else "#B9C9AF"}" stroke-width="{S*.05:.2f}"/>')
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
        if k not in STP: continue
        X, Y = P(x, y); Wd, Hd = w * S, h * S
        st = STP[k]; n = len(st); rad = min(S * .2, Wd / (2.3 * n), Hd / 2.6)
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
        room = {"HALL": "Central hall"}.get(k, f"Room {k}")
        if n in XS:
            rows.append(f'<div class="row x"><span class="dot hol" style="color:{c};border-color:{c}">{n}</span>'
                        f'<span class="rm">{esc(room)}</span><span class="tt"><i style="color:{c}">Extra</i> {esc(short(t))}</span></div>')
        else:
            rows.append(f'<div class="row"><span class="dot" style="background:{c}">{n}</span>'
                        f'<span class="rm">{esc(room)}</span><span class="tt">{esc(short(t) if t["register"] not in ("ANCHOR", "CLOSE") else t["title"])}</span></div>')
    return "".join(rows)

# ---------------------------------------------------------------- page 1: the three levels, top down
LENGTHS = [("Full tour", len(TR), "about 2 h 30"), ("Essential", 26, "about 1 h 15"), ("Highlights", 14, "about 40 min")]
def overview_svg():
    W, H = 182.0, 112.0
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}mm" height="{H}mm">']
    rows = [(2, 6, 40, [s for s in SECS if s[0].startswith("Level 2")]), (1, 52, 24, [s for s in SECS if s[0].startswith("Level 1")]),
            (0, 82, 24, [s for s in SECS if s[0].startswith("Level 0")])]
    for lev, y, hh, secs in rows:
        o.append(f'<rect x="16" y="{y}" width="150" height="{hh}" rx="2.4" fill="#fff" stroke="{LINE}" stroke-width=".4"/>')
        o.append(f'<text x="12.5" y="{y+hh/2+2.5}" class="fl">{lev}</text>')
        per = 3 if len(secs) > 3 else len(secs)
        w = (146 - 2 * (per - 1)) / per
        for i, sec in enumerate(secs):
            r, col = divmod(i, per)
            x = 18 + col * (w + 2); yy = y + 2.5 + r * 18.5; c = sec[3]; a, b = rng(sec[0])
            o.append(f'<rect x="{x:.1f}" y="{yy:.1f}" width="{w:.1f}" height="16.5" rx="2" fill="{c}" fill-opacity=".10" stroke="{c}" stroke-width=".55"/>')
            o.append(f'<text x="{x+2.4:.1f}" y="{yy+6.2:.1f}" class="zl" style="fill:{c}">{esc(sec[1])}</text>')
            o.append(f'<text x="{x+2.4:.1f}" y="{yy+10.4:.1f}" class="zs">{esc(sec[2] if len(sec[2]) <= int(w / 1.55) else sec[2][:int(w / 1.55) - 1].rsplit(", ", 1)[0] + "…")}</text>')
            o.append(f'<text x="{x+2.4:.1f}" y="{yy+14.4:.1f}" class="zs" style="font-weight:700">stops {a}–{b}</text>')
    for y0, y1 in ((46, 52), (76, 82)):
        o.append(f'<path d="M171,{y0-6} L171,{y1+6}" stroke="{GOLD}" stroke-width="1" stroke-dasharray="1.6,1.2"/>')
        o.append(f'<path d="M-2,-2.6 L0,1.8 L2,-2.6 Z" fill="{GOLD}" transform="translate(171 {y1+7})"/>')
    o.append(f'<text x="176" y="50" class="up" style="text-anchor:middle">stairs</text><text x="176" y="80" class="up" style="text-anchor:middle">stairs</text>')
    o.append(f'<text x="16" y="4" class="hallc">START · up from the central hall to Level 2, Room 1 ▲</text>')
    o.append(f'<text x="166" y="110.5" class="hallc" style="text-anchor:end">FINISH · out to the Paseo del Prado ▶</text>')
    o.append("</svg>")
    return "".join(o)

pages = []
lens = "".join(f'<div class="card"><div class="cbar" style="background:{NAVY}"></div><div class="cnum" style="background:{NAVY}">{i}</div>'
               f'<div class="cbody"><div class="ct">{esc(n)}</div><div class="cs">{k} tracks · {esc(m)}</div></div><div class="cmeta"></div></div>'
               for i, (n, k, m) in enumerate(LENGTHS, 1))
pages.append(f'''<section class="page">
 <header><div class="brand">YO TOURS · AUDIO GUIDE</div><h1>Museo Nacional Thyssen-Bornemisza</h1>
 <p class="lede">Seven centuries of painting, walked top down: {MAIN} main stops, about two hours, plus {len(XS)} short Extras. The guide comes in three lengths.</p></header>
 <div class="how"><div><b>1</b> Every room's number is on the museum's map and at the room. Level 2 is 1–29, Level 1 is 30–56, Level 0 is A–J.</div>
 <div><b>2</b> Play the stops for that room. Hollow circles are short, optional Extras.</div>
 <div><b>3</b> Each stop ends by telling you which room is next. In the shorter versions a short line tells you the next stop.</div></div>
 <div class="ov">{overview_svg()}</div>
 <div class="cards">{lens}</div>
 <footer>The museum lends works to exhibitions: if a painting isn't on the wall, a notice is usually in its place. Rooms 19–21 and 53–56 hold temporary displays and are not stops.</footer>
</section>''')

def floor_page(title, sub, svg, first, last, stack=True):
    return f'''<section class="page">
 <header class="fh"><div class="brand">YO TOURS · MUSEO NACIONAL THYSSEN-BORNEMISZA</div>
 <h2>{esc(title)}</h2><p class="sub">{esc(sub)}</p></header>
 <div class="stack"><div class="plan">{svg}</div><div class="list">{stop_list(first, last)}</div></div>
 <footer>Not to scale · drawn by Yo Tours after the museum's visitor map (Dec 2025) · stop numbers = track numbers on your phone</footer>
</section>'''

S2 = [s[0] for s in SECS if s[0].startswith("Level 2")]
a, b = rng("Opening", *S2[:3])
pages.append(floor_page("Level 2 · From gold to the Baroque", f"Start where the museum's map says: Room 1. Then the first faces, the Renaissance portraits along the long Villahermosa Gallery, Venice and the Baroque. Stops {a}–{b}.",
    plan_svg(L2, L2_WAY, PATHS["l2"], 182, 132, notes=[("1", "START · up from\nthe central hall", "start", -2.2, -2.4)], ends=("", ""), show=(a, b)), a, b))
a, b = rng(*S2[3:])
pages.append(floor_page("Level 2 · The 18th century, the Dutch and Romanticism", f"On through Rooms 16–18 to 22, then the Dutch rooms 23–28 and Room 29. Rooms 19–21 hold a temporary display and are not stops. Stops {a}–{b}.",
    plan_svg(L2, L2_WAY, PATHS["l2"], 182, 132, notes=[("LIFT2E", "Down to Level 1,\nRoom 30", "down", -1.6, 2.4)], ends=("", ""), show=(a, b)), a, b))
S1 = [s[0] for s in SECS if s[0].startswith("Level 1")]
a, b = rng(*S1[:2])
pages.append(floor_page("Level 1 · America to the avant-gardes", f"Arrive at Room 30 and walk west through the 19th century, then down the side rooms 35–40 for Expressionism and abstraction. Stops {a}–{b}.",
    plan_svg(L1, L1_WAY, PATHS["l1"], 182, 132, notes=[("LIFT1E", "Arrive from Level 2", "up", .2, -3.2)], ends=("", ""), show=(a, b)), a, b))
a, b = rng(S1[2])
pages.append(floor_page("Level 1 · Surrealism, America and Pop", f"Along the long row 41–48 and up to Room 52. Rooms 53–56 hold a temporary display and are not stops. Stops {a}–{b}.",
    plan_svg(L1, L1_WAY, PATHS["l1"], 182, 132, notes=[("s1", "Down to Level 0", "down", -.4, -2.2)], ends=("", ""), show=(a, b)), a, b))
a, b = rng(SECS[-2][0], "Closing")
pages.append(floor_page("Level 0 · The Carmen Thyssen collection", f"Rooms A to J, from Old Masters to the avant-gardes, then back to the central hall and out to the Paseo del Prado. Stops {a}–{b}.",
    plan_svg(L0, L0_WAY, PATHS["l0"], 182, 130, notes=[("in0", "Arrive from Level 1", "down", -1.2, -2.6), ("ex0", "Exit ·\nPaseo del Prado", "finish", 1.6, 2.2)], ends=("", ""), show=(a, b)), a, b))

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
.list .row {{ display: grid; grid-template-columns: 7.5mm 15mm 1fr; align-items: center; padding: .8mm 0; border-bottom: .25mm solid {LINE} }}
.dot {{ width: 6mm; height: 6mm; border-radius: 50%; color: #fff; font: 700 8pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.rm {{ font: 600 7.2pt Inter; color: {MUTED} }} .hol {{ background: #fff; border: .45mm solid; box-sizing: border-box }}
.row.x .tt {{ color: {MUTED} }} .tt i {{ font-style: normal; font-weight: 700; font-size: 7pt; letter-spacing: .04em; margin-right: 1mm }} .tt {{ font: 500 7.9pt Inter; line-height: 1.28 }}
'''
doc = f'<!doctype html><html><head><meta charset="utf-8"><title>Thyssen-Bornemisza · Yo Tours route</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
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
