#!/usr/bin/env python3
"""Yo Tours · Poble Espanyol de Montjuïc (Barcelona) — route map, 31 Oct 2026 edition.
A PDF made to be read on a phone: page 1 = the whole village with the loop from the Ávila gate up to the monastery and
back down to the Plaza Mayor, and the three lengths; page 2 = the lower village (the gate, Plaza Castellana, Calle
Caballeros, Calle Príncipe de Viana, the Plaza Mayor and the town hall, 21); page 3 = the middle (Plaza Aragonesa and the
brick tower, Plaza de la Iglesia, Plaza del Carmen, the Fran Daurel Museum, Carrer de la Davallada, Carrer Mercaders with
81 and 83, Plaça de la Font); page 4 = the top and Andalusia (the Baluard, Barcelona Panorama, the Sculpture Garden, the
Monastery of Sant Miquel, 69, the Vidre art gallery, Plaza de la Hermandad, Plaza Peñaflor, Calle Arcos and the Tablao at
61, the Gradas de Santiago, Rincón del Triste); page 5 = the stop table.
Our OWN schematic of the village, not traced and not a copy of the official artwork: simplified blocks in the four
region colours of the official plan (North green, Centre pink, South yellow, Mediterranean purple), the official street
and square names, and only the house numbers the tracks use. Orientation as on the official plan (the gate low down at
one end, the monastery at the top of the hill at the other); no compass. Placements follow v5/PLAN.md ("The route",
House key), research/map/OFFICIAL_PLAN_NOTES_31OCT2026.md and the last paragraph (the directions) of every track, which
the lead made the source for cues. Unconfirmed spots are dashed or dotted with a legend: the Sculpture Garden's way in
(O10), the steps from the Baluard to the monastery (O8), whether house numbers are posted on the houses (O2). The
step-free route is not drawn: "ask for the official step-free route at the entrance". No prices, hours, logo or photos.
Stops come from v5/tracks/NNN.perf.txt (@title, @room, @where, @type, @section); lengths from build/static/lengths.json.
Usage (from the guide folder): python3 build/route_map.py <bundle folder> [--png <dir>]
  -> <bundle>/PobleEspanyol_Audio_Guide_Route.pdf"""
import json, math, os, re, sys, html, asyncio, glob

B = sys.argv[1]
PNG_DIR = sys.argv[sys.argv.index("--png") + 1] if "--png" in sys.argv else None
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
TRACKS = os.path.join(ROOT, "v5", "tracks")
LENGTHS_JSON = os.path.join(HERE, "static", "lengths.json")
OUT_PDF = os.path.join(B, "PobleEspanyol_Audio_Guide_Route.pdf")
FOOTER = "Yo Tours · Poble Espanyol audio guide · 31 Oct 2026 edition · schematic plan, not to scale"
if not os.environ.get("PLAYWRIGHT_BROWSERS_PATH") and os.path.isdir("/opt/pw-browsers"):
    os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "/opt/pw-browsers"

# ---------------------------------------------------------------- stops, from the track files
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
    n = int(os.path.basename(f)[:3]); h, w = read_track(f)
    t = h.get("title", "").strip(); ttype = h.get("type", "R")
    extra = ttype == "X" or " Extra · " in t or t.startswith("Extra · ")
    t = re.sub(r"^.*?·\s*Extra\s*·\s*", "", t) if extra else t
    if " — " in t: t = t.split(" — ", 1)[1]
    where = re.sub(r"\s*\[[^\]]*\]", "", h.get("where", "")).strip()
    TR[n] = dict(type=ttype, room=h.get("room", "").strip(), title=t, words=w, section=h.get("section", ""),
                 extra=extra, where=where)
if not TR: sys.exit("no track files in " + TRACKS)
NUMS = sorted(TR)
XS = {n for n in NUMS if TR[n]["extra"]}

# ---------------------------------------------------------------- the three lengths (visit times as spoken in 001, walking included)
J = json.load(open(LENGTHS_JSON, encoding="utf-8"))
H_SET = {int(x) for x in J["HIGHLIGHTS"].split()}; E_SET = {int(x) for x in J["ESSENTIAL"].split()}
F_SET = set(NUMS)
FX = len(XS)
LENGTHS = [("Full tour", F_SET, "about 1 h 30", f"every stop and all {FX} Extras; nearer two hours with the Fran Daurel Museum"),
           ("Essential", E_SET, "about 1 h 15", "the streets house by house, the makers, the art museum, the glassblower, the town hall, two Extras"),
           ("Highlights", H_SET, "about 45 min", "the gate, the road trip, the brick tower, the Rupit stair, the view, the monastery, Andalusia, the Plaza Mayor")]

# ---------------------------------------------------------------- palette, sections, regions
PAPER, INK, MUTED, LINE = "#F6F1E7", "#1F1B17", "#776E62", "#D8CEBD"
RED, GOLD, NAVY = "#C0262D", "#A9812F", "#1D2B4A"
SECS = {  # @section -> (short title, dot colour)
    "The gate": ("The gate", "#1D2B4A"),
    "Calle Caballeros": ("Calle Caballeros", "#A8325C"),
    "The brick tower": ("The brick tower", "#A4581B"),
    "Catalonia": ("Catalonia", "#5B2A6E"),
    "The top of the hill": ("The top of the hill", "#2C5A7E"),
    "Andalusia": ("Andalusia", "#8C6100"),
    "Back to the Plaza Mayor": ("Back to the Plaza Mayor", "#2E6A52"),
}
REG = {  # the official plan's region colours: (name, edge, fill)
    "N": ("North", "#2F8A64", "#A8D5BF"),
    "C": ("Centre", "#C9577F", "#F4C4D5"),
    "S": ("South", "#C99A12", "#F8DC8A"),
    "M": ("Mediterranean", "#5E2D5C", "#C3A6CB"),
    "G": ("grey on the plan (museums)", "#8F8A82", "#D3CFC8"),
}
def colour(n): return SECS.get(TR[n]["section"], ("", INK))[1]
def esc(s): return html.escape(s, quote=True)
def sec_ns(*secs): return [n for n in NUMS if TR[n]["section"] in secs]
def rng(sec):
    ns = sec_ns(sec)
    return (f"{ns[0]}–{ns[-1]}" if len(ns) > 1 else f"{ns[0]}") if ns else ""
def has(sub): return [n for n in NUMS if sub in TR[n]["room"]]
def ds(prefix): return [n for n in NUMS if TR[n]["room"].startswith(prefix)]
def one(ns, what):
    if not ns: sys.exit("route_map: no track for " + what)
    return ns[0]
def lst(ns): return ", ".join(map(str, ns[:-1])) + " and " + str(ns[-1]) if len(ns) > 1 else str(ns[0])
# the track numbers the drawings and texts name, all derived from @room / @section / @type of the track files
N_WELCOME = one([n for n in NUMS if TR[n]["type"] == "ANCHOR"], "the welcome")
N_GATE = one([n for n in has("two towers") if n not in XS], "facing the gate")
N_GATEX = one([n for n in sec_ns("The gate") if n in XS], "the gate Extra")
N_CABS = one(has("Calle Caballeros · at its start"), "the start of Calle Caballeros")
N_CABW = one(ds("Calle Caballeros · walking"), "walking up Calle Caballeros")
N_JUNC = one(ds("Junction"), "the junction at 102/103")
N_PVW = one(ds("Calle Príncipe de Viana · walking"), "walking up Calle Príncipe de Viana")
N_TOWER = one(ds("Plaza Aragonesa"), "Plaza Aragonesa and the tower")
N_CHURCH = one(has("church front"), "the church front")
N_FIESTA = one(has("FIESTA"), "the FIESTA door")
N_DAUREL = one(has("Fran Daurel"), "the Fran Daurel door")
N_83 = one(has("house 83"), "house 83")
N_81 = one(has("house 81"), "house 81")
N_FONT = one(ds("Plaça de la Font"), "Plaça de la Font")
N_PANO = one(ds("Barcelona Panorama"), "Barcelona Panorama")
N_GARDEN = one(ds("Sculpture Garden"), "the Sculpture Garden")
N_MON = one(ds("Monastery"), "the monastery")
N_HERM = one(ds("Plaza de la Hermandad"), "Plaza de la Hermandad")
N_ARCOS = one(ds("Calle Arcos"), "Calle Arcos")
N_CARMEN = one(ds("Plaza del Carmen"), "Plaza del Carmen")
N_GRADAS = one(ds("Gradas de Santiago"), "the Gradas de Santiago")
N_RIAZA = one(has("on the steps"), "the Plaza Mayor steps")
N_TH = one(ds("Town hall"), "the town hall")
N_SIT = one(has("sitting on the steps"), "sitting on the steps")
N_CLOSE = one([n for n in NUMS if TR[n]["type"] == "CLOSE"], "the close")

DASH = "1.2,.8"
PAVE, GRASS, GRASS_D, PATH = "#EFE7D7", "#DCE6CC", "#B9C9A6", "#E8E1D3"
BRICK, STONE, WATER = "#B8693A", "#CDBB97", "#BFD9E3"

# ---------------------------------------------------------------- SVG kit: world units (a schematic grid, no scale) -> page mm
class Svg:
    _n = 0
    def __init__(self, view, W=184, bg="#FDFBF7"):
        x0, y0, x1, y1 = view; self.k = W / (x1 - x0); self.x0, self.y0 = x0, y0
        self.W, self.H = W, round((y1 - y0) * self.k, 2)
        Svg._n += 1; cid = f"clip{Svg._n}"
        self.o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {self.H}" width="{W}mm" height="{self.H}mm">',
                  f'<defs><clipPath id="{cid}"><rect x="0" y="0" width="{W}" height="{self.H}" rx="2"/></clipPath></defs>',
                  f'<rect x="0" y="0" width="{W}" height="{self.H}" rx="2" fill="{bg}"/>', f'<g clip-path="url(#{cid})">']
        self.top = []
    def T(self, x, y): return ((x - self.x0) * self.k, (y - self.y0) * self.k)
    def add(self, s, top=False): (self.top if top else self.o).append(s)
    def d(self, pts, close=False):
        return "M" + " L".join(f"{a:.2f},{b:.2f}" for a, b in (self.T(*p) for p in pts)) + (" Z" if close else "")
    def poly(self, pts, fill="none", strk=INK, sw=.3, dash=None, close=True, op=1, fop=1, top=False):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<path d="{self.d(pts, close)}" fill="{fill}" fill-opacity="{fop}" stroke="{strk}" stroke-width="{sw}" stroke-opacity="{op}"{da} stroke-linecap="round" stroke-linejoin="round"/>', top)
    def line(self, pts, strk=INK, sw=.3, dash=None, op=1, top=False): self.poly(pts, "none", strk, sw, dash, False, op, top=top)
    def rect(self, x0, y0, x1, y1, fill, strk="none", sw=.3, dash=None, rx=0):
        (a, b), (c, e) = self.T(x0, y0), self.T(x1, y1); da = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<rect x="{a:.2f}" y="{b:.2f}" width="{c - a:.2f}" height="{e - b:.2f}" rx="{rx}" fill="{fill}" stroke="{strk}" stroke-width="{sw}"{da}/>')
    def circle(self, x, y, r, fill, strk="none", sw=.3, dash=None, top=False):
        cx, cy = self.T(x, y); da = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" fill="{fill}" stroke="{strk}" stroke-width="{sw}"{da}/>', top)
    def text(self, x, y, t, cls="pl", anc="middle", fs=2.4, fill=None, rot=None, top=False, page=False):
        if not page: x, y = self.T(x, y)
        lines = t.split("\n")
        st = f"font-size:{fs:.2f}px;text-anchor:{anc}" + (f";fill:{fill}" if fill else "")
        tr = f' transform="rotate({rot} {x:.2f} {y:.2f})"' if rot else ""
        y0 = y - (len(lines) - 1) * fs * 1.18 / 2 + fs * .35
        sp = "".join(f'<tspan x="{x:.2f}" dy="{0 if i == 0 else fs * 1.18:.2f}">{esc(l)}</tspan>' for i, l in enumerate(lines))
        self.add(f'<text x="{x:.2f}" y="{y0:.2f}" class="{cls}" style="{st}"{tr}>{sp}</text>', top)
    def arrowhead(self, x, y, ang, k=1.05, fill=INK, op=.85):
        self.add(f'<path d="M{-k:.2f},{-k * .8:.2f} L{k:.2f},0 L{-k:.2f},{k * .8:.2f} Z" fill="{fill}" fill-opacity="{op}" transform="translate({x:.2f},{y:.2f}) rotate({ang:.1f})"/>')
    def route(self, pts, kind="main", mid=True, end=True, minlen=12):
        """main = dashed with arrows (the walking order); unc = dotted (path to be confirmed on site)."""
        P = [self.T(*p) for p in pts]; d = "M" + " L".join(f"{x:.2f},{y:.2f}" for x, y in P)
        self.add(f'<path d="{d}" fill="none" stroke="#FDFBF7" stroke-opacity=".8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>')
        if kind == "main":
            self.add(f'<path d="{d}" fill="none" stroke="{INK}" stroke-opacity=".78" stroke-width=".55" stroke-dasharray="1.5,1" stroke-linecap="round" stroke-linejoin="round"/>')
        else:
            self.add(f'<path d="{d}" fill="none" stroke="{INK}" stroke-opacity=".75" stroke-width=".8" stroke-dasharray=".1,1.2" stroke-linecap="round" stroke-linejoin="round"/>')
        if mid:
            for (xa, ya), (xb, yb) in zip(P, P[1:]):
                if math.hypot(xb - xa, yb - ya) < minlen: continue
                self.arrowhead((xa + xb) / 2, (ya + yb) / 2, math.degrees(math.atan2(yb - ya, xb - xa)))
        if end:
            (xa, ya), (xb, yb) = P[-2], P[-1]
            self.arrowhead(xb, yb, math.degrees(math.atan2(yb - ya, xb - xa)))
    def dots(self, x, y, ns, dr="r", rad=2.4, page=False):
        if not page: x, y = self.T(x, y)
        step = rad * 2.18
        vx, vy = {"r": (step, 0), "l": (-step, 0), "d": (0, step), "u": (0, -step)}[dr]
        for i, s in enumerate(ns):
            cx, cy = x + i * vx, y + i * vy; c = colour(s)
            if s in XS:
                self.add(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{rad * .94:.2f}" fill="#fff" stroke="{c}" stroke-width="{rad * .2:.2f}"/>'
                         f'<text x="{cx:.2f}" y="{cy + rad * .36:.2f}" class="sn" style="font-size:{rad * .98:.2f}px;fill:{c}">{s}</text>', True)
            else:
                self.add(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{rad:.2f}" fill="{c}" stroke="#fff" stroke-width="{rad * .14:.2f}"/>'
                         f'<text x="{cx:.2f}" y="{cy + rad * .36:.2f}" class="sn" style="font-size:{rad:.2f}px">{s}</text>', True)
    def note(self, px, py, text, kind, tx, ty, fs=2.4):
        """A pill callout centred at page (tx, ty), with a leader to world (px, py) (None: no leader)."""
        colr = {"start": INK, "finish": INK, "info": MUTED, "warn": GOLD, "top": SECS["The top of the hill"][1]}[kind]
        lines = text.split("\n"); wmax = max(len(l) for l in lines) * fs * .55 + fs * 1.6
        hb = fs * 1.36 * len(lines) + fs * .6
        bx = min(max(tx - wmax / 2, .8), self.W - wmax - .8); by = min(max(ty - hb / 2, .8), self.H - hb - .8)
        if px is not None:
            qx, qy = self.T(px, py)
            self.add(f'<line x1="{qx:.2f}" y1="{qy:.2f}" x2="{bx + wmax / 2:.2f}" y2="{by + hb / 2:.2f}" stroke="{colr}" stroke-width=".35" stroke-dasharray="1,.7"/>'
                     f'<circle cx="{qx:.2f}" cy="{qy:.2f}" r=".8" fill="{colr}"/>', True)
        self.add(f'<rect x="{bx:.2f}" y="{by:.2f}" width="{wmax:.2f}" height="{hb:.2f}" rx="{min(hb / 2, 2):.2f}" fill="{colr}"/>', True)
        for i, l in enumerate(lines):
            self.add(f'<text x="{bx + fs * .8:.2f}" y="{by + fs * 1.2 + i * fs * 1.36:.2f}" class="note" style="font-size:{fs:.2f}px">{esc(l)}</text>', True)
    def chip(self, x, y, t, fs=2.1, top=True):
        """A house number from the official plan, in a dashed box: whether it is posted on the house is unconfirmed."""
        cx, cy = self.T(x, y); w = len(t) * fs * .62 + fs * .9; h = fs * 1.45
        self.add(f'<rect x="{cx - w / 2:.2f}" y="{cy - h / 2:.2f}" width="{w:.2f}" height="{h:.2f}" rx=".5" fill="#fff" stroke="{INK}" stroke-width=".25" stroke-dasharray="{DASH}"/>'
                 f'<text x="{cx:.2f}" y="{cy + fs * .36:.2f}" class="hn" style="font-size:{fs:.2f}px">{esc(t)}</text>', top)
    def stairs(self, a, b, w, n, colr="#8F8473", dash=None, fill="#E4DACA"):
        """A flight of steps seen from above, from world a to world b, w world units wide, n treads."""
        (x0, y0), (x1, y1) = a, b; L = math.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / L, (y1 - y0) / L; nx, ny = -uy * w / 2, ux * w / 2
        self.poly([(x0 + nx, y0 + ny), (x1 + nx, y1 + ny), (x1 - nx, y1 - ny), (x0 - nx, y0 - ny)], fill, colr, .3, dash)
        for i in range(1, n):
            t = i / n; px, py = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
            self.line([(px + nx, py + ny), (px - nx, py - ny)], colr, .22)
    def done(self): return "".join(self.o) + "</g>" + "".join(self.top) + "</svg>"

# ---------------------------------------------------------------- the village, schematic (one geometry, four views)
# A schematic grid (no scale): the gate low down at the end of the lower village, the monastery at the top of the hill.
GROUND = [(225, 92), (380, 100), (520, 112), (600, 150), (740, 235), (880, 292), (1005, 330), (1060, 425), (1205, 440),
          (1258, 495), (1256, 728), (1218, 770), (1085, 772), (1060, 798), (1030, 798), (995, 776), (900, 770), (820, 700),
          (705, 600), (660, 470), (610, 440), (560, 438), (440, 410), (300, 415), (262, 360), (330, 318), (300, 270), (232, 210)]
GARDEN = [(285, 330), (360, 318), (440, 330), (520, 352), (582, 392), (585, 418), (520, 412), (440, 392), (360, 398), (292, 392)]
BLOCKS = [  # (region, polygon)
    # lower village: Calle Caballeros, outer side
    ("C", [(812, 640), (850, 662), (872, 700), (840, 712), (800, 672)]),
    ("N", [(876, 690), (948, 716), (946, 752), (902, 748), (860, 716)]),
    ("C", [(952, 720), (996, 728), (994, 766), (952, 764)]),
    # Calle Caballeros, inner side; Travesía del Maestrazgo; Calle Alcalde de Móstoles
    ("C", [(862, 616), (906, 628), (936, 650), (936, 676), (908, 668), (872, 650), (848, 632)]),
    ("M", [(938, 650), (992, 662), (990, 684), (938, 676)]),
    ("C", [(938, 680), (990, 688), (996, 700), (944, 696)]),
    ("N", [(996, 662), (1044, 670), (1046, 702), (998, 704)]),
    ("N", [(1062, 678), (1146, 678), (1146, 698), (1062, 698)]),
    ("C", [(1062, 700), (1146, 700), (1146, 716), (1062, 716)]),
    ("N", [(822, 584), (852, 576), (862, 604), (834, 618)]),
    ("M", [(856, 560), (896, 548), (904, 596), (866, 606)]),
    ("C", [(780, 546), (822, 556), (816, 586), (786, 578)]),
    ("C", [(770, 582), (812, 610), (800, 640), (762, 612)]),
    # Calle Príncipe de Viana, outer side
    ("N", [(668, 412), (700, 418), (744, 500), (764, 560), (738, 576), (716, 520), (680, 470)]),
    # between Calle Príncipe de Viana and the Bajada de Cervantes; round the Gradas de Santiago
    ("N", [(724, 444), (790, 446), (798, 520), (782, 544), (756, 540), (736, 498)]),
    ("N", [(808, 500), (868, 506), (868, 548), (842, 556), (806, 538)]),
    ("N", [(800, 438), (852, 438), (882, 482), (872, 500), (808, 494)]),
    ("M", [(872, 506), (904, 508), (904, 530), (872, 530)]),
    ("C", [(872, 532), (904, 532), (904, 548), (872, 548)]),
    # the Plaza Mayor: north side, east side, the bandstand corner
    ("C", [(996, 456), (1096, 456), (1096, 484), (996, 484)]),
    ("N", [(1098, 456), (1150, 456), (1150, 484), (1098, 484)]),
    ("C", [(1152, 462), (1186, 462), (1186, 490), (1152, 490)]),
    ("N", [(1190, 464), (1246, 490), (1248, 540), (1196, 540)]),
    ("C", [(1198, 544), (1246, 544), (1244, 712), (1196, 712)]),
    ("C", [(1150, 720), (1214, 720), (1212, 764), (1150, 762)]),
    ("C", [(1066, 730), (1130, 730), (1130, 768), (1072, 768)]),
    # above the square: the green North (29–37)
    ("N", [(894, 330), (1004, 346), (1040, 426), (990, 450), (964, 468), (902, 468), (872, 420)]),
    ("C", [(1040, 428), (1102, 432), (1100, 452), (1040, 452)]),
    # the church (57–59) and the grey museums
    ("N", [(770, 372), (852, 386), (846, 412), (774, 404)]),
    ("G", [(738, 255), (850, 290), (884, 318), (860, 382), (772, 368), (738, 330)]),
    ("G", [(886, 318), (924, 336), (904, 390), (862, 384)]),
    # the Mediterranean: Carrer de la Davallada, Carrer Mercaders, Plaça de la Font, 69
    ("M", [(612, 420), (684, 420), (690, 434), (640, 444), (612, 438)]),
    ("M", [(549, 304), (574, 308), (640, 366), (656, 396), (626, 398), (560, 350), (544, 322)]),
    ("M", [(440, 300), (522, 312), (600, 372), (592, 394), (566, 386), (502, 336), (438, 322)]),
    ("M", [(505, 160), (578, 168), (572, 250), (505, 244)]),
    ("M", [(452, 214), (504, 222), (504, 246), (570, 256), (568, 276), (450, 284)]),
    # the Monastery of Sant Miquel (116)
    ("M", [(266, 142), (338, 146), (372, 168), (366, 200), (322, 206), (266, 180)]),
    # the South: Andalusia
    ("S", [(580, 166), (662, 176), (652, 220), (600, 214), (580, 206)]),
    ("S", [(556, 216), (598, 214), (604, 300), (584, 312), (554, 300)]),
    ("S", [(654, 222), (734, 242), (744, 266), (700, 298), (664, 280), (632, 246)]),
    ("S", [(598, 316), (622, 310), (618, 350), (626, 388), (606, 392), (600, 350)]),
    ("S", [(656, 298), (700, 304), (724, 340), (708, 368), (660, 374), (646, 340)]),
]
LAB = [  # (x, y, text, class, size zoom/overview, rotation, minimum level: 0 every view, 1 zooms only)
    (1034, 722, "Plaza\nCastellana", "plb", 2.6, 0, 0),
    (912, 694, "Calle Caballeros", "st", 2.2, 24, 0, (872, 700, 24)),
    (752, 520, "Calle Príncipe de Viana", "st", 2.2, 58, 0, (716, 536, 58)),
    (850, 566, "Travesía del\nMaestrazgo", "sts", 1.8, -38, 1),
    (860, 528, "Bajada de\nCervantes\n(steps, off\nthe route)", "sts", 1.8, 0, 1),
    (918, 622, "Calle Alcalde de Móstoles", "sts", 1.8, 22, 1),
    (1050, 496, "Calle Alcalde Zalamea", "sts", 1.8, 0, 1),
    (1225, 740, "Calle\nTercio", "sts", 1.8, 0, 1),
    (1100, 725, "Calle Conquista", "sts", 1.7, 0, 1),
    (1110, 632, "PLAZA MAYOR", "plb", 3.2, 0, 0),
    (738, 438, "Plaza Aragonesa", "plb", 2.4, 0, 0),
    (830, 458, "Plaza de la\nIglesia", "plb", 2.3, 0, 0, (864, 452, 0)),
    (700, 354, "Plaza del\nCarmen", "plb", 2.1, 0, 1),
    (652, 430, "Carrer de la Davallada", "st", 2.0, -4, 0, (600, 452, 0)),
    (596, 378, "Carrer Mercaders", "st", 2.0, 41, 0, (540, 352, 41)),
    (505, 296, "Plaça de la Font", "plb", 2.3, 0, 0, (510, 262, 0)),
    (412, 248, "Baluard", "plb", 2.4, 0, 0),
    (330, 296, "Barcelona\nPanorama", "plb", 2.3, 0, 0),
    (400, 368, "Sculpture Garden", "plb", 2.3, 0, 0),
    (500, 384, "giant slides", "sts", 1.8, 18, 1),
    (300, 100, "Monastery of Sant Miquel", "plb", 2.5, 0, 0),
    (588, 232, "Calle\nLevante", "sts", 1.6, 0, 1),
    (626, 264, "Plaza de la\nHermandad", "plb", 2.1, 0, 0),
    (668, 286, "Plaza\nPeñaflor", "plb", 2.0, 0, 1),
    (612, 352, "Calle Arcos", "st", 1.9, 80, 1),
    (694, 318, "Calle Bulas", "sts", 1.8, 42, 1),
    (620, 156, "Vidre art gallery", "plm", 2.0, 0, 0),
    (796, 312, "Fran Daurel\nMuseum", "plm", 2.3, 0, 0),
    (896, 360, "Guinovart\nSpace", "pls", 1.8, 0, 1),
    (948, 484, "Gradas de\nSantiago", "plb", 2.1, 0, 0),
    (1000, 444, "Rincón del\nTriste", "plm", 1.9, 0, 0),
    (950, 528, "town hall", "plm", 2.1, 0, 1),
    (1166, 552, "bandstand", "pls", 1.8, 0, 1),
    (812, 420, "the church", "pls", 1.8, 0, 1),
]
CHIPS = [  # (x, y, house number as the tracks use it, minimum level)
    (972, 590, "21", 0), (1022, 686, "26", 0), (640, 402, "83", 1), (588, 344, "81", 1), (540, 196, "69", 0),
    (300, 190, "116", 0), (610, 330, "61", 1),
    (978, 676, "115", 1), (974, 742, "2", 1), (896, 650, "113", 1), (842, 620, "102", 1), (796, 614, "103", 1),
    (838, 596, "41", 1), (610, 192, "67/68", 1), (810, 392, "57–59", 1), (890, 382, "56", 1), (604, 426, "89", 1),
    (1092, 748, "3", 1),
]
TOWER = (752, 352)
def tower_icon(s, x, y, k):
    """The brick tower, an elevation icon (our own drawing): a tall square shaft with an octagonal top."""
    (cx, cy) = s.T(x, y); h = 13 * k; w = 3.4 * k
    s.add(f'<g transform="translate({cx:.2f},{cy:.2f})">'
          f'<rect x="{-w / 2:.2f}" y="{-h * .55:.2f}" width="{w:.2f}" height="{h:.2f}" fill="{BRICK}" stroke="#6E3A1C" stroke-width=".25"/>'
          f'<rect x="{-w * .38:.2f}" y="{-h * .82:.2f}" width="{w * .76:.2f}" height="{h * .28:.2f}" fill="#C9845A" stroke="#6E3A1C" stroke-width=".25"/>'
          f'<path d="M{-w * .38:.2f},{-h * .82:.2f} L0,{-h * .98:.2f} L{w * .38:.2f},{-h * .82:.2f} Z" fill="#8A4A26"/>'
          + "".join(f'<rect x="{-w * .3:.2f}" y="{-h * .5 + i * h * .2:.2f}" width="{w * .6:.2f}" height="{h * .05:.2f}" fill="#E7C27A" opacity=".8"/>' for i in range(4))
          + '</g>', True)
def gate_icon(s, x, y, k):
    """The Ávila gate: two round towers joined by a walkway, seen from above (our own drawing)."""
    for dx in (-26, 26): s.circle(x + dx, y, 4.0 * k, STONE, "#7E6A45", .35)
    s.rect(x - 22, y - 9, x + 22, y + 9, "#D9C9A6", "#7E6A45", .3)
    for dx in (-26, 26):
        cx, cy = s.T(x + dx, y)
        for a in range(0, 360, 45):
            r = math.radians(a); s.add(f'<rect x="{cx + math.cos(r) * 3.4 * k - .35 * k:.2f}" y="{cy + math.sin(r) * 3.4 * k - .35 * k:.2f}" width="{.7 * k:.2f}" height="{.7 * k:.2f}" fill="#7E6A45"/>')
def monastery_icon(s, x, y, k):
    """The monastery: a nave and a square bell tower (our own drawing)."""
    cx, cy = s.T(x, y)
    s.add(f'<g transform="translate({cx:.2f},{cy:.2f})">'
          f'<rect x="{-7 * k:.2f}" y="{-1.6 * k:.2f}" width="{9 * k:.2f}" height="{4.4 * k:.2f}" fill="#E9D6B4" stroke="#7E6A45" stroke-width=".3"/>'
          f'<path d="M{-7.6 * k:.2f},{-1.6 * k:.2f} L{-2.5 * k:.2f},{-4 * k:.2f} L{2.6 * k:.2f},{-1.6 * k:.2f} Z" fill="#C46A44"/>'
          f'<rect x="{2.4 * k:.2f}" y="{-6.2 * k:.2f}" width="{2.8 * k:.2f}" height="{9 * k:.2f}" fill="#E9D6B4" stroke="#7E6A45" stroke-width=".3"/>'
          f'<path d="M{2.1 * k:.2f},{-6.2 * k:.2f} L{3.8 * k:.2f},{-7.6 * k:.2f} L{5.5 * k:.2f},{-6.2 * k:.2f} Z" fill="#C46A44"/>'
          f'<path d="M{-3.6 * k:.2f},{2.8 * k:.2f} L{-3.6 * k:.2f},{.6 * k:.2f} A{.9 * k:.2f},{.9 * k:.2f} 0 0 1 {-1.8 * k:.2f},{.6 * k:.2f} L{-1.8 * k:.2f},{2.8 * k:.2f} Z" fill="#7E6A45"/>'
          '</g>', True)

def village(s, lvl):
    """Ground, the garden, blocks, steps, landmarks and labels; lvl 0 = the whole village, 1 = a zoom."""
    k = s.k
    s.rect(s.x0 - 50, s.y0 - 50, s.x0 + s.W / k + 50, s.y0 + s.H / k + 50, GRASS)
    s.poly(GROUND, PAVE, "#CBBFA8", .35)
    s.poly(GARDEN, "#CFE0BC", GRASS_D, .35)
    for x, y in ((330, 360), (380, 352), (452, 372), (520, 392), (350, 384), (420, 386)):     # trees in the garden
        s.circle(x, y, max(.9, 5 * k), "#9DBB85", "none")
    for i in range(2):                                                                     # the giant slides
        s.line([(470 + i * 14, 352), (482 + i * 14, 364), (494 + i * 14, 368)], "#C0262D", max(.35, 2.2 * k), op=.7)
    # the monastery's path loop and the top path down toward 69
    s.line([(350, 128), (515, 130), (560, 160), (580, 200)], PATH, max(1.2, 9 * k), op=1)
    s.line([(266, 142), (248, 160), (262, 200), (330, 222), (420, 205), (515, 130)], PATH, max(1.0, 7 * k))
    s.poly([(470, 210), (490, 228), (510, 254)], "none", PATH, max(1.0, 7 * k), close=False)
    for reg, pts in BLOCKS:
        s.poly(pts, REG[reg][2], REG[reg][1], .3 if lvl else .22)
    # the Plaza Mayor's inner steps (a level change of about 2 m, RAH11)
    s.stairs((1004, 528), (1146, 528), 10, 12)
    s.stairs((1146, 528), (1146, 652), 10, 9)
    # the Gradas de Santiago, the Bajada de Cervantes (off the route), steps on Calle Arcos
    s.stairs((872, 420), (900, 474), 32, 8)
    s.stairs((798, 498), (842, 566), 9, 6)
    s.stairs((700, 372), (716, 368), 12, 3)
    s.stairs((634, 296), (644, 306), 10, 3)
    # the steps from the Baluard up to the monastery path (O8: to be confirmed) and the steps by 89 (garden way in? O10)
    s.stairs((382, 252), (360, 216), 14, 5, dash=DASH, fill="#fff")
    s.stairs((596, 418), (574, 418), 10, 4, dash=DASH, fill="#fff")
    # the Baluard terrace and the viewpoint
    s.poly([(372, 232), (448, 236), (452, 300), (360, 306)], "#F2ECDF", "#A79A82", .3)
    vx, vy = s.T(346, 284); r = max(1.4, 9 * k)
    s.add(f'<path d="M{vx - r:.2f},{vy:.2f} Q{vx:.2f},{vy - r * .8:.2f} {vx + r:.2f},{vy:.2f} Q{vx:.2f},{vy + r * .8:.2f} {vx - r:.2f},{vy:.2f} Z" fill="#fff" stroke="{INK}" stroke-width=".3"/>'
          f'<circle cx="{vx:.2f}" cy="{vy:.2f}" r="{r * .35:.2f}" fill="{INK}"/>', True)
    # the fountain, the town hall arcade, the bandstand, the arcade at 26
    s.circle(505, 280, max(.9, 6 * k), WATER, "#5F8FA0", .3)
    s.rect(912, 520, 1000, 604, REG["N"][2], REG["N"][1], .35)
    for i in range(6):
        y = 526 + i * 13; s.rect(992, y, 1000, y + 9, "#fff", REG["N"][1], .25)
    cx, cy = s.T(1166, 520); r = 2.2 * max(k / .32, .5)
    s.add(f'<polygon points="{" ".join(f"{cx + r * math.cos(math.radians(a + 22.5)):.2f},{cy + r * math.sin(math.radians(a + 22.5)):.2f}" for a in range(0, 360, 45))}" fill="#C46A44" stroke="#6E3A1C" stroke-width=".25"/>')
    for i in range(3):
        y = 666 + i * 12; s.rect(1006, y, 1014, y + 8, "#fff", REG["N"][1], .22)
    gate_icon(s, 1052, 784, max(k / .32, .5))
    monastery_icon(s, 304, 142, max(k / .3, .55))
    tower_icon(s, *TOWER, max(k / .32, .55))
    for x, y, t, cls, fs, rot, ml, *ov in LAB:
        if lvl < ml: continue
        if not lvl and ov: x, y, rot = ov[0]
        s.text(x, y, t, cls, "middle", fs if lvl else fs * .8, rot=rot or None, top=True)
    for x, y, t, ml in CHIPS:
        if lvl >= ml: s.chip(x, y, t, 2.1 if lvl else 1.75)

# ---------------------------------------------------------------- the route (walking order), shared by every view
R_UP = [(1052, 772), (1040, 728), (1000, 708), (950, 704), (904, 676), (862, 640), (826, 606), (790, 566), (756, 512),
        (726, 466), (712, 432), (770, 424), (842, 424)]
R_CAT = [(842, 432), (712, 440), (680, 410), (640, 410), (612, 404), (590, 388), (558, 352), (524, 318), (500, 300), (452, 268), (400, 266), (360, 278)]
R_MON = [(360, 216), (368, 192)]
R_DOWN = [(376, 172), (420, 140), (515, 132), (560, 160), (580, 200), (600, 236), (640, 280), (634, 320), (638, 360), (660, 384), (704, 380), (726, 372)]
R_BACK = [(726, 372), (760, 404), (842, 416), (868, 422), (900, 474), (980, 478), (1022, 520), (1060, 560)]
R_SQ = [(1060, 560), (1006, 570), (1060, 600), (1020, 672), (1040, 728), (1050, 768)]
def draw_route(s):
    s.route(R_UP, "main", minlen=18)
    s.route(R_CAT, "main", minlen=18)
    s.route([(400, 266), (382, 252)], "main", mid=False, end=False)
    s.route([(382, 252), (360, 216)], "unc", mid=False, end=False)      # the steps from the Baluard (O8)
    s.route(R_MON, "main", mid=False)
    s.route(R_DOWN, "main", minlen=18)
    s.route(R_BACK, "main", minlen=18)
    s.route(R_SQ, "main", minlen=18)
    # the Sculpture Garden, in and back: two possible ways in (O10)
    s.route([(380, 300), (390, 340)], "unc", mid=False)
    s.route([(596, 418), (560, 404), (520, 384)], "unc", mid=False)

PLACES = {  # default world positions of every stop dot
    N_WELCOME: (1010, 730), N_GATE: (1084, 768), N_GATEX: (1084, 768), N_CABS: (976, 712), N_CABW: (918, 668),
    N_JUNC: (816, 596), N_PVW: (736, 512), N_TOWER: (712, 430), N_CHURCH: (812, 430), N_FIESTA: (770, 396),
    N_DAUREL: (856, 410), N_83: (650, 408), N_81: (572, 318), N_FONT: (490, 306), N_PANO: (352, 300),
    N_GARDEN: (420, 352), N_MON: (330, 172), N_HERM: (606, 240), N_ARCOS: (630, 336), N_CARMEN: (722, 384),
    N_GRADAS: (868, 448), N_RIAZA: (1074, 552), N_TH: (1004, 580), N_SIT: (1082, 600), N_CLOSE: (1030, 676),
}

# ---------------------------------------------------------------- stop lists, dots in text, legends
def dot(n, cls="dot"):
    c = colour(n)
    if n in XS: return f'<span class="{cls} hol" style="color:{c};border-color:{c}">{n}</span>'
    return f'<span class="{cls}" style="background:{c}">{n}</span>'
def stop_list(ns):
    rows = []
    for n in ns:
        t = TR[n]; c = colour(n); x = ' x' if n in XS else ''
        ex = f'<i style="color:{c}">Extra</i> ' if n in XS else ''
        rows.append(f'<div class="row{x}">{dot(n)}<span class="tt"><b>{esc(t["room"])}</b><br>{ex}{esc(t["title"])}</span></div>')
    return "".join(rows)
def sw(svg): return f'<svg width="9mm" height="3mm" viewBox="0 0 9 3">{svg}</svg>'
_ROUTE_SW = sw(f'<path d="M.5,1.5 L8.5,1.5" stroke="{INK}" stroke-opacity=".78" stroke-width=".55" stroke-dasharray="1.5,1"/>')
_UNC_SW = sw(f'<path d="M.5,1.5 L8.5,1.5" stroke="{INK}" stroke-width=".8" stroke-dasharray=".1,1.2" stroke-linecap="round"/>')
_STEP_SW = sw(f'<rect x=".5" y=".4" width="8" height="2.2" fill="#fff" stroke="#8F8473" stroke-width=".3" stroke-dasharray="{DASH}"/>'
              '<path d="M2.5,.4 V2.6 M4.5,.4 V2.6 M6.5,.4 V2.6" stroke="#8F8473" stroke-width=".22"/>')
LEGEND = ('<div class="legend">'
          f'<span>{dot(N_TOWER, "ldot")} track</span><span><span class="ldot hol" style="color:{INK};border-color:{INK}">X</span> Extra</span>'
          f'<span>{_ROUTE_SW} route, in walking order</span><span>{_UNC_SW} way to be confirmed on site</span>'
          f'<span>{_STEP_SW} steps to be confirmed</span>'
          '<span><span class="lchip">83</span> house number on the official plan; posted on the house? to be confirmed</span>'
          '</div>')
REGKEY = ('<div class="regkey">' + "".join(f'<span><i style="background:{REG[r][2]};border-color:{REG[r][1]}"></i>{esc(REG[r][0])}</span>' for r in "NCSMG")
          + '<em>the four region colours of the official plan</em></div>')

pages = []
def map_page(kicker, title, sub, svg, ns, extra="", inset=None):
    lst_ = f'<div class="list">{stop_list(ns)}</div>' if ns else ""
    if inset: lst_ = f'<div class="split"><div class="inset">{inset}</div><div class="list one">{stop_list(ns)}</div></div>'
    return f'''<section class="page">
 <header class="fh"><div class="brand">YO TOURS · POBLE ESPANYOL · {esc(kicker)}</div>
 <h2>{esc(title)}</h2><p class="sub">{sub}</p></header>
 <div class="plan">{svg}{REGKEY}{LEGEND}</div>{lst_}{extra}
 <footer>{esc(FOOTER)}</footer>
</section>'''

# ---------------------------------------------------------------- page 1: the whole village
def whole_svg():
    s = Svg((215, 84, 1268, 812))
    village(s, 0); draw_route(s)
    r = 2.15
    groups = [((1000, 742), [N_WELCOME, N_GATE, N_GATEX], "l"), ((972, 690), [N_CABS], "r"), ((900, 662), [N_CABW], "r"),
              ((806, 596), [N_JUNC], "r"), ((768, 486), [N_PVW], "r"), ((690, 450), [N_TOWER], "r"),
              ((790, 392), [N_CHURCH, N_FIESTA, N_DAUREL], "r"), ((652, 392), [N_83], "r"), ((560, 302), [N_81], "r"),
              ((452, 284), [N_FONT], "r"), ((338, 318), [N_PANO], "r"), ((452, 350), [N_GARDEN], "r"),
              ((392, 180), [N_MON], "r"), ((626, 230), [N_HERM], "r"), ((660, 334), [N_ARCOS], "r"),
              ((736, 398), [N_CARMEN], "r"), ((904, 412), [N_GRADAS], "r"), ((1060, 556), [N_RIAZA, N_TH, N_SIT], "r"),
              ((1040, 650), [N_CLOSE], "r")]
    for (x, y), ns, dr in groups: s.dots(x, y, ns, dr, r)
    s.note(1052, 792, "START and END · the Ávila gate", "start", 104, s.H - 4, 2.3)
    s.text(s.W - 2, 4, "SCHEMATIC · NOT TO SCALE", "scl", "end", 2.2, page=True, top=True)
    return s.done()

KEYS = "".join(f'<span><i style="background:{SECS[k][1]}"></i><em>{esc(SECS[k][0])} <b>{rng(k)}</b></em></span>' for k in SECS if rng(k))
def len_card(i, name, ns, when, desc):
    ds_ = "".join(dot(n, "mdot") for n in sorted(ns))
    return (f'<div class="card"><div class="ch"><div class="cnum">{i}</div><div><div class="ct">{esc(name)}</div>'
            f'<div class="cs"><b>{esc(when)}</b> · {len(ns)} tracks</div></div></div>'
            f'<div class="cdots">{ds_}</div><div class="cs2">{esc(desc)}</div></div>')
lens = "".join(len_card(i, n, ns, m, d) for i, (n, ns, m, d) in enumerate(LENGTHS, 1))
pages.append(f'''<section class="page">
 <header><div class="brand">YO TOURS · AUDIO GUIDE</div><h1>Poble Espanyol de Montjuïc</h1>
 <p class="lede">A 1929 village where every house is modelled on one somewhere in Spain: {len(F_SET) - FX} main stops plus {FX} short Extras in one loop, in three lengths.</p></header>
 <div class="how"><div><b>1</b> <strong>Up the hill, then back down.</strong> From the Ávila gate up Calle Caballeros to the brick tower and through Catalonia to the monastery; down through Andalusia and the Gradas de Santiago to the Plaza Mayor.</div>
 <div><b>2</b> Each circle is the track to play there; hollow ones are short Extras. Every track ends by telling you where to go next. Pages 2–4 zoom in.</div>
 <div><b>3</b> House numbers and colours are the official plan's. <strong>Dotted and dashed: not yet confirmed on site.</strong> Step-free: ask for the official step-free route at the entrance.</div></div>
 <div class="ov">{whole_svg()}<div class="keys">{KEYS}</div>{REGKEY}{LEGEND}</div>
 <div class="cards">{lens}</div>
 <div class="warn"><b>Steps</b> on the Gradas de Santiago, Calle Arcos, up to the monastery and in the Plaza Mayor. Times include walking (and on the Full tour the ten-minute FIESTA show), not queues or time in museums and workshops. Shorter versions: the numbers jump.</div>
 <footer>{esc(FOOTER)}</footer>
</section>''')

# ---------------------------------------------------------------- page 2: the lower village
def lower_svg():
    s = Svg((690, 395, 1262, 800))
    village(s, 1); draw_route(s)
    r = 2.55
    for n in (N_CABS, N_CABW, N_JUNC, N_PVW, N_TH):
        s.dots(*PLACES[n], [n], "r", r)
    s.dots(1020, 754, [N_WELCOME], "r", r); s.dots(1104, 778, [N_GATE, N_GATEX], "r", r)
    s.dots(912, 418, [N_GRADAS], "r", r); s.dots(1036, 648, [N_CLOSE], "r", r)
    s.dots(1074, 552, [N_RIAZA], "r", r); s.dots(1086, 604, [N_SIT], "r", r)
    s.note(1052, 790, "START and END · the Ávila gate", "start", 60, s.H - 4, 2.4)
    s.note(712, 432, "up to the brick tower · page 3", "info", 30, 6, 2.2)
    s.note(890, 430, "down from the Plaza de la Iglesia · page 4", "info", 110, 6, 2.2)
    s.text(s.W - 2, s.H - 2.4, "SCHEMATIC · NOT TO SCALE", "scl", "end", 2.2, page=True, top=True)
    return s.done()
LOW_NS = sec_ns("The gate", "Calle Caballeros") + [n for n in NUMS if TR[n]["room"].startswith(("Plaza Mayor", "Town hall"))]
lowextra = f'''<div class="boxes">
 <div class="box"><h3>In and up ({N_WELCOME}–{N_PVW})</h3><p>Play {N_WELCOME} and {N_GATE} in Plaza Castellana, facing the gate's two round towers. Calle Caballeros starts between houses 115 and 2 ({N_CABS}); play {N_CABW} walking up. It becomes Calle Príncipe de Viana at 102 and 103 ({N_JUNC}); play {N_PVW} walking up to Plaza Aragonesa.</p></div>
 <div class="box"><h3>The Plaza Mayor ({N_RIAZA}–{N_SIT})</h3><p>You come back down the Gradas de Santiago, past Rincón del Triste, into the square. Play {N_RIAZA} on its steps with the whole square in view, {N_TH} under the arcade of the town hall, house 21 (the photographs of the building site are inside, if open), {N_SIT} sitting on the steps.</p></div>
 <div class="box"><h3>The end ({N_CLOSE})</h3><p>The last stop is by the arcade at house 26, the passage to Plaza Castellana. The way out is the Ávila gate, the way you came in. If event structures fill the square, play the square's stops at its quiet edge. Step-free: ask for the official step-free route at the entrance.</p></div>
</div>'''
pages.append(map_page("THE LOWER VILLAGE", f"The gate and the Plaza Mayor · {LOW_NS[0]}–{N_PVW}, {N_RIAZA}–{N_CLOSE}",
    f"Plaza Castellana and the Ávila gate ({N_WELCOME}, {N_GATE}, Extra {N_GATEX}), up Calle Caballeros ({N_CABS}, {N_CABW}) to the junction at 102/103 ({N_JUNC}) and up Calle Príncipe de Viana ({N_PVW}). "
    f"At the end of the loop: the Plaza Mayor ({N_RIAZA}, {N_SIT}), the town hall, house 21 ({N_TH}), and the arcade at 26 ({N_CLOSE}).",
    lower_svg(), LOW_NS, lowextra))

# ---------------------------------------------------------------- page 3: the middle
def middle_svg():
    s = Svg((455, 246, 890, 576))
    village(s, 1); draw_route(s)
    r = 2.6
    s.dots(696, 448, [N_TOWER], "r", r); s.dots(800, 440, [N_CHURCH], "r", r); s.dots(782, 392, [N_FIESTA], "r", r)
    s.dots(858, 404, [N_DAUREL], "r", r); s.dots(662, 398, [N_83], "r", r); s.dots(545, 342, [N_81], "r", r)
    s.dots(470, 314, [N_FONT], "r", r); s.dots(738, 386, [N_CARMEN], "r", r); s.dots(658, 336, [N_ARCOS], "r", r)
    s.dots(738, 512, [N_PVW], "r", r)
    s.note(400, 266, "on to the Baluard and the view · page 4", "info", 34, 4, 2.2)
    s.note(596, 418, "steps by 89: a way into the\nSculpture Garden? (to confirm)", "warn", 36, 62, 2.1)
    s.note(890, 478, "down to the Plaza Mayor · page 2", "info", 150, s.H - 5, 2.2)
    s.note(756, 540, "from the gate · page 2", "info", 100, s.H - 5, 2.2)
    s.text(s.W - 2, 4, "SCHEMATIC · NOT TO SCALE", "scl", "end", 2.2, page=True, top=True)
    return s.done()
MID_NS = sec_ns("The brick tower", "Catalonia") + [N_CARMEN]
midextra = f'''<div class="boxes">
 <div class="box"><h3>Round the church ({N_TOWER}–{N_DAUREL})</h3><p>Play {N_TOWER} in Plaza Aragonesa with the whole brick tower in view. Walk along the church front to the Plaza de la Iglesia, the small square where a wide flight of steps goes down: {N_CHURCH} facing the church, Extra {N_FIESTA} at the FIESTA door before you go in, {N_DAUREL} at the Fran Daurel Museum door.</p></div>
 <div class="box"><h3>Up into Catalonia ({N_83}–{N_FONT})</h3><p>Back along the church to Plaza Aragonesa and up Carrer de la Davallada to house 83, the one with an outside stair ({N_83}). Carrer Mercaders, the street of Rupit house fronts, leads up past house 81, where a glass furnace may be at work ({N_81}), to Plaça de la Font and its fountain ({N_FONT}).</p></div>
 <div class="box"><h3>Back past the tower ({N_CARMEN})</h3><p>On the way down from Andalusia, Calle Arcos comes out by the brick tower, where the little Plaza del Carmen opens. Play {N_CARMEN} there or walking past the tower and along the church to the Plaza de la Iglesia and the top of the Gradas de Santiago.</p></div>
</div>'''
pages.append(map_page("THE MIDDLE OF THE VILLAGE", f"The brick tower and Catalonia · {N_TOWER}–{N_FONT}, {N_CARMEN}",
    f"Plaza Aragonesa and the brick tower ({N_TOWER}), the Plaza de la Iglesia with the church, FIESTA and the Fran Daurel Museum ({N_CHURCH}, Extra {N_FIESTA}, {N_DAUREL}), "
    f"up Carrer de la Davallada to house 83 ({N_83}), Carrer Mercaders and house 81 ({N_81}), Plaça de la Font ({N_FONT}); later, on the way down, the Plaza del Carmen ({N_CARMEN}).",
    middle_svg(), MID_NS, midextra))

# ---------------------------------------------------------------- page 4: the top of the hill and Andalusia
def top_svg():
    s = Svg((225, 88, 775, 470))
    village(s, 1); draw_route(s)
    r = 2.5
    s.dots(470, 314, [N_FONT], "r", r); s.dots(334, 318, [N_PANO], "r", r); s.dots(452, 350, [N_GARDEN], "r", r)
    s.dots(392, 182, [N_MON], "r", r); s.dots(624, 230, [N_HERM], "r", r); s.dots(658, 336, [N_ARCOS], "r", r)
    s.dots(738, 392, [N_CARMEN], "r", r); s.dots(652, 398, [N_83], "r", r); s.dots(545, 342, [N_81], "r", r)
    s.note(372, 236, "steps up from the Baluard\n(to be confirmed on site)", "warn", 100, 47, 2.1)
    s.note(390, 336, "the garden's way in: from the viewpoint,\nor by the steps at 89? (to confirm)", "warn", 40, s.H - 6, 2.1)
    s.text(s.W - 2, 4, "SCHEMATIC · NOT TO SCALE", "scl", "end", 2.2, page=True, top=True)
    return s.done()
def gradas_svg():
    s = Svg((790, 372, 1030, 512), W=74)
    village(s, 1); draw_route(s)
    s.dots(912, 416, [N_GRADAS], "r", 2.5)
    s.note(1022, 520, "into the Plaza Mayor · page 2", "info", 52, s.H - 3.6, 2.0)
    return s.done()
TOP_NS = sec_ns("The top of the hill", "Andalusia") + [N_GRADAS]
topextra = f'''<div class="boxes">
 <div class="box"><h3>The view and the garden ({N_PANO}, {N_GARDEN})</h3><p>From Plaça de la Font, walk on past the Baluard, the terrace beside the square, to the viewpoint the plan calls Barcelona Panorama ({N_PANO}). Extra {N_GARDEN} is just inside the Sculpture Garden, below the viewpoint, where the giant slides are; it is a dead end, so come back the same way.</p></div>
 <div class="box"><h3>Up to the monastery ({N_MON})</h3><p>Take the steps from the Baluard up to the Romanesque church with the square bell tower, house 116, and play {N_MON} in front of the portal. A step-free path climbs to it round the houses at the top of Plaça de la Font. The monastery itself is not step-free.</p></div>
 <div class="box"><h3>Down through Andalusia ({N_HERM}–{N_GRADAS})</h3><p>The path from the monastery runs down toward house 69 and on between 69 and the Vidre art gallery into Plaza de la Hermandad, where the walls turn white ({N_HERM}). Extra {N_ARCOS}: through Plaza Peñaflor and down Calle Arcos, which has steps, to the Tablao de Carmen, house 61. {N_GRADAS}: at the top of the Gradas de Santiago; Rincón del Triste is the corner at their foot.</p></div>
</div>'''
pages.append(map_page("THE TOP OF THE HILL AND ANDALUSIA", f"The monastery and Andalusia · {TOP_NS[0]}–{TOP_NS[-1]}",
    f"Barcelona Panorama by the Baluard ({N_PANO}), the Sculpture Garden (Extra {N_GARDEN}), the Monastery of Sant Miquel ({N_MON}), down past house 69 and the Vidre art gallery to Plaza de la Hermandad ({N_HERM}), "
    f"Calle Arcos and the Tablao de Carmen (Extra {N_ARCOS}), then, past the tower, the top of the Gradas de Santiago ({N_GRADAS}). Highlights skips Calle Arcos and takes Calle Bulas.",
    top_svg(), TOP_NS, topextra, f'<h4>The Gradas de Santiago and Rincón del Triste</h4>{gradas_svg()}'))

# ---------------------------------------------------------------- page 5: the stop table
rows = []; last_sec = None
for n in NUMS:
    s_ = TR[n]["section"]
    if s_ != last_sec: rows.append(("sec", s_)); last_sec = s_
    rows.append(("stop", n))
trs = []
mk = lambda on: '<span class="mk">●</span>' if on else '<span class="no">·</span>'
for kind, v in rows:
    if kind == "sec":
        c = SECS.get(v, ("", INK))[1]
        trs.append(f'<tr class="sh"><td colspan="7" style="color:{c};border-bottom-color:{c}">{esc(SECS.get(v, (v,))[0])}</td></tr>')
    else:
        n = v; t = TR[n]; x = ' class="x"' if n in XS else ''
        ty = f'<i style="color:{colour(n)}">Extra</i>' if n in XS else 'main'
        trs.append(f'<tr{x}><td>{dot(n)}</td><td class="tt">{esc(t["title"])}</td><td class="pc">{esc(t["room"])}</td><td class="ty">{ty}</td>'
                   f'<td>{mk(n in F_SET)}</td><td>{mk(n in E_SET)}</td><td>{mk(n in H_SET)}</td></tr>')
trs.append(f'<tr class="tot"><td colspan="4">Tracks · visit time, walking included</td>'
           f'<td>{len(F_SET)}<br><span>{LENGTHS[0][2].replace("about ", "≈ ")}</span></td><td>{len(E_SET)}<br><span>{LENGTHS[1][2].replace("about ", "≈ ")}</span></td><td>{len(H_SET)}<br><span>{LENGTHS[2][2].replace("about ", "≈ ")}</span></td></tr>')
head = '<tr class="th"><th>#</th><th>Title</th><th>Where to play it</th><th>Type</th><th>Full</th><th>Essen&shy;tial</th><th>High&shy;lights</th></tr>'
pages.append(f'''<section class="page">
 <header class="fh"><div class="brand">YO TOURS · POBLE ESPANYOL · ALL STOPS</div>
 <h2>The stops</h2>
 <p class="sub">Every track in walking order: # on your player, the title, where to play it, main stop or Extra, and the lengths it belongs to (Full, {LENGTHS[0][2]}; Essential, {LENGTHS[1][2]}; Highlights, {LENGTHS[2][2]}; walking included). Hollow circles are Extras.</p></header>
 <table class="tbl">{head}{"".join(trs)}</table>
 <p class="tfoot">Step-free: ask for the official step-free route at the entrance. House numbers are the official plan's; whether they are posted on the houses is to be confirmed on site.</p>
 <footer>{esc(FOOTER)}</footer>
</section>''')

CSS = f'''
@page {{ size: A4; margin: 0 }}
* {{ box-sizing: border-box }}
html, body {{ margin: 0; background: {PAPER}; color: {INK}; font-family: Inter, "DejaVu Sans", sans-serif }}
.page {{ width: 210mm; height: 297mm; padding: 11mm 13mm 10mm; position: relative; page-break-after: always; overflow: hidden; background: {PAPER} }}
.brand {{ font: 600 7.6pt Inter; letter-spacing: .28em; color: {GOLD} }}
h1 {{ font: 700 25pt Lora, serif; margin: 1.6mm 0 1mm; letter-spacing: -.01em }}
h2 {{ font: 700 18pt Lora, serif; margin: 1.6mm 0 1mm }}
h3 {{ font: 700 9.6pt Lora, serif; margin: 0 0 1mm }}
.lede {{ font: 400 10.4pt Lora, serif; color: {MUTED}; margin: 0 0 2.6mm; line-height: 1.35 }}
.sub {{ font: 400 8.6pt Inter; color: {MUTED}; margin: 0 0 2.2mm; max-width: 184mm; line-height: 1.38 }}
.how {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 3mm; margin-bottom: 2.4mm }}
.how div {{ background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; padding: 2mm 2.6mm; font: 500 7.7pt Inter; line-height: 1.32 }}
.how b {{ display: inline-flex; width: 5mm; height: 5mm; border-radius: 50%; background: {INK}; color: #fff; font: 700 7.5pt Inter; align-items: center; justify-content: center; margin-right: 1.2mm }}
.how strong {{ color: {RED} }}
.ov {{ background: #FDFBF7; border: .3mm solid {LINE}; border-radius: 4mm; padding: 1.5mm 1mm; margin-bottom: 2.4mm }}
.ov > svg, .plan > svg {{ display: block; margin: 0 auto; width: 100%; height: auto }}
.keys {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: .8mm 3mm; padding: 1.4mm 3mm 0; font: 500 6.9pt Inter; color: {INK} }}
.keys span {{ display: flex; align-items: flex-start; gap: 1.4mm }} .keys em {{ font-style: normal; line-height: 1.25 }} .keys b {{ color: {MUTED}; font-weight: 600; white-space: nowrap }}
.keys i {{ width: 3mm; height: 3mm; border-radius: 50%; flex: none; margin-top: .2mm }}
.regkey {{ display: flex; flex-wrap: wrap; gap: 1mm 3.4mm; justify-content: center; padding: 1.6mm 1mm 0; font: 500 6.9pt Inter; color: {INK}; align-items: center }}
.regkey span {{ display: inline-flex; align-items: center; gap: 1.2mm }} .regkey i {{ width: 4.4mm; height: 3mm; border: .3mm solid; border-radius: .6mm }}
.regkey em {{ font-style: normal; color: {MUTED} }}
.warn {{ background: #fff; border: .3mm solid {GOLD}; border-left: 1.6mm solid {GOLD}; border-radius: 2.4mm; padding: 2mm 3mm; font: 400 7.9pt Inter; line-height: 1.36; margin-bottom: 3mm }}
.cards {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.4mm; margin-bottom: 2.4mm }}
.card {{ background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; padding: 2mm 2.4mm }}
.ch {{ display: grid; grid-template-columns: 9mm 1fr; align-items: center }}
.cnum {{ width: 7mm; height: 7mm; border-radius: 50%; color: #fff; background: {NAVY}; font: 700 11pt Inter; display: flex; align-items: center; justify-content: center }}
.ct {{ font: 700 10.2pt Lora; margin-bottom: .2mm }} .cs {{ font: 400 7.9pt Inter; color: {MUTED} }} .cs b {{ color: {INK} }}
.cdots {{ display: flex; flex-wrap: wrap; gap: .8mm; margin: 1.4mm 0 1mm }}
.mdot {{ width: 4.6mm; height: 4.6mm; border-radius: 50%; color: #fff; font: 700 6.2pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.cs2 {{ font: 400 7pt Inter; color: {MUTED}; line-height: 1.3 }}
footer {{ position: absolute; left: 13mm; right: 13mm; bottom: 6mm; font: 400 7pt Inter; color: {MUTED}; border-top: .3mm solid {LINE}; padding-top: 1.6mm }}
.plan {{ background: #FDFBF7; border: .3mm solid {LINE}; border-radius: 4mm; padding: 2mm; margin-bottom: 2.4mm }}
.split {{ display: grid; grid-template-columns: 78mm 1fr; gap: 4mm; align-items: start; margin-bottom: 2.4mm }} .split .list {{ columns: 1; margin: 0 }}
.inset {{ background: #FDFBF7; border: .3mm solid {LINE}; border-radius: 3mm; padding: 1.4mm 2mm 2mm }} .inset svg {{ display: block; width: 100% ; height: auto }}
h4 {{ font: 700 8pt Inter; margin: 0 0 1mm; color: {MUTED} }}
.list {{ columns: 2; column-gap: 7mm; margin-bottom: 2.4mm }} .list .row {{ break-inside: avoid }}
.boxes {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.4mm }}
.box {{ background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; padding: 2mm 2.6mm }}
.box p {{ font: 400 7.6pt Inter; line-height: 1.34; margin: 0 }}
.sn {{ font-family: Inter; font-weight: 700; fill: #fff; text-anchor: middle }}
.note {{ font-family: Inter; font-weight: 600; fill: #fff }}
.hn {{ font-family: Inter; font-weight: 700; fill: {INK}; text-anchor: middle }}
.pl, .plb, .plm, .pls, .st, .sts {{ paint-order: stroke; stroke: #FDFBF7; stroke-width: .7px; stroke-linejoin: round }}
.pl {{ font-family: Inter; font-weight: 700; fill: {INK} }} .plb {{ font-family: Lora, serif; font-weight: 700; fill: {INK} }}
.plm {{ font-family: Inter; font-weight: 600; fill: #3E3830 }} .pls {{ font-family: Inter; font-weight: 500; fill: #5F574C }}
.st {{ font-family: Inter; font-weight: 700; fill: #4A3F33; letter-spacing: .1px }} .sts {{ font-family: Inter; font-weight: 600; fill: #6F665A }}
.scl {{ font-family: Inter; font-weight: 700; fill: #A39886; letter-spacing: .25px }}
.legend {{ display: flex; flex-wrap: wrap; gap: 1.2mm 3.6mm; justify-content: center; padding: 1.6mm 1mm .4mm; font: 500 6.9pt Inter; color: {MUTED}; align-items: center }}
.legend > span {{ display: inline-flex; align-items: center; gap: 1.3mm }}
.ldot {{ width: 4.4mm; height: 4.4mm; border-radius: 50%; color: #fff; font: 700 6pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.lchip {{ font: 700 6.4pt Inter; color: {INK}; background: #fff; border: .3mm dashed {INK}; border-radius: .6mm; padding: 0 .9mm }}
.list .row {{ display: grid; grid-template-columns: 7.5mm 1fr; align-items: center; padding: .5mm 0; border-bottom: .25mm solid {LINE} }}
.dot {{ width: 6mm; height: 6mm; border-radius: 50%; color: #fff; font: 700 7.6pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.hol {{ background: #fff; border: .45mm solid; box-sizing: border-box }}
.row.x .tt {{ color: {MUTED} }} .tt i {{ font-style: normal; font-weight: 700; font-size: 7pt; letter-spacing: .04em; margin-right: 1mm }}
.tt {{ font: 500 7.6pt Inter; line-height: 1.2 }} .list .tt {{ padding-left: 1.6mm }} .tt b {{ font-weight: 700; color: {INK} }}
.tbl {{ width: 100%; border-collapse: collapse; background: #fff; border: .3mm solid {LINE}; border-radius: 3mm }}
.tbl th {{ font: 700 6.6pt Inter; color: {MUTED}; text-align: left; padding: 1.4mm 1.2mm 1.1mm; border-bottom: .35mm solid {INK}; letter-spacing: .04em; text-transform: uppercase }}
.tbl th:nth-child(n+5) {{ text-align: center; width: 12mm }} .tbl th:first-child {{ width: 9mm; padding-left: 2mm }} .tbl th:nth-child(3) {{ width: 72mm }} .tbl th:nth-child(4) {{ width: 11mm }}
.tbl td {{ padding: .5mm 1.2mm; line-height: 1.16; border-bottom: .2mm solid {LINE}; vertical-align: middle }}
.tbl td:first-child {{ padding-left: 2mm }} .tbl td:nth-child(n+5) {{ text-align: center }}
.tbl .dot {{ width: 5.2mm; height: 5.2mm; font-size: 6.8pt; vertical-align: middle }}
.tbl .tt {{ font: 700 8pt Inter }} .tbl .pc {{ font: 500 7.5pt Inter; color: #4A443C }} .tbl tr.x .tt, .tbl tr.x .pc {{ color: {MUTED} }}
.tbl .ty {{ font: 500 7.2pt Inter; color: {MUTED} }} .tbl .ty i {{ font-style: normal; font-weight: 700 }}
.mk {{ color: {NAVY}; font-size: 8.6pt }} .no {{ color: #C9BFAE }}
.tbl tr.sh td {{ font: 700 7.8pt Inter; padding: 1.6mm 2mm .3mm; border-bottom: .3mm solid; letter-spacing: .02em }}
.tbl tr.tot td {{ font: 700 7.8pt Inter; border-top: .35mm solid {INK}; border-bottom: none; padding: 1.4mm 1.2mm 1.4mm 2mm }} .tbl tr.tot span {{ font-weight: 500; color: {MUTED}; white-space: nowrap }}
.tfoot {{ font: 400 7.6pt Inter; color: {MUTED}; margin: 2.4mm 0 0 }}
'''

def build():
    doc = f'<!doctype html><html><head><meta charset="utf-8"><title>Poble Espanyol · Yo Tours route</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
    os.makedirs(B, exist_ok=True)
    hp = os.path.join(B, "route_map.html"); open(hp, "w", encoding="utf-8").write(doc)
    async def render():
        from playwright.async_api import async_playwright
        async with async_playwright() as p:
            br = await p.chromium.launch(); pg = await br.new_page(device_scale_factor=2)
            await pg.goto("file://" + os.path.abspath(hp)); await pg.wait_for_timeout(300)
            await pg.pdf(path=OUT_PDF, format="A4", print_background=True, margin=dict(top="0", bottom="0", left="0", right="0"))
            if PNG_DIR:
                os.makedirs(PNG_DIR, exist_ok=True)
                await pg.set_viewport_size({"width": 794, "height": 1123})
                for i, el in enumerate(await pg.query_selector_all(".page")):
                    await el.screenshot(path=os.path.join(PNG_DIR, f"route_p{i+1}.png"), scale="device")
            await br.close()
    asyncio.run(render())
    if not os.environ.get("RM_KEEP_HTML"): os.remove(hp)
    print(f"stops: {len(NUMS)} tracks ({len(F_SET)} Full, {len(E_SET)} Essential, {len(H_SET)} Highlights, {len(XS)} Extras)")
    print("OK ->", OUT_PDF, len(pages), "pages")

build()
