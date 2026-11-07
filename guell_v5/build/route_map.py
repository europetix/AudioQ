#!/usr/bin/env python3
"""Yo Tours · Park Güell (Barcelona) — route map, 7 Nov 2026 edition.
A PDF made to be read on a phone: page 1 = the whole loop and the three lengths; page 2 = the gate, the Casa del Guarda
and the viaducts; page 3 = the Dragon Stairway, the Hypostyle Room and the Austria Gardens; page 4 = the Nature Square,
the Portico, Casa Larrard and the way out (pages 2-4: where to stand for every track); page 5 = on-site notes.
Our OWN schematic of the park, not traced and not a copy of the official artwork: simple shapes, the official stop
letters A-I and names, drawn looking up the hill from Carrer d'Olot (the street along the bottom), "left/right" as seen
on the esplanade facing the stairway, as in research/map/OFFICIAL_ROUTE_MAP_NOTES_7NOV2026.md: the gate -> the
viaducts side trip (not on the official drawing) -> the second ticket check and the stairway -> the hall -> up its
right-hand side into the Austria Gardens -> the upper path -> round the Nature Square -> out at its left-hand corner ->
the path above Casa Larrard -> the Portico -> the ramp -> down past the bandstand and along the wall to the gate.
Not to scale; no compass, no distances, no prices or hours, no logo or photos. Writers' markers ([O5], ALT-K, notes for
the on-site check) are never printed.
Stops come from v5/tracks/NNN.perf.txt (@title, @room, @where, @type, @section) at run time; lengths from
build/static/lengths.json.
Usage (from the guide folder): python3 build/route_map.py <bundle folder> [--png <dir>]
  -> <bundle>/ParkGuell_Audio_Guide_Route.pdf"""
import json, math, os, re, sys, html, asyncio, glob

B = sys.argv[1]
PNG_DIR = sys.argv[sys.argv.index("--png") + 1] if "--png" in sys.argv else None
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
TRACKS = os.path.join(ROOT, "v5", "tracks")
LENGTHS_JSON = os.path.join(HERE, "static", "lengths.json")
OUT_PDF = os.path.join(B, "ParkGuell_Audio_Guide_Route.pdf")
FOOTER = "Yo Tours · Park Güell audio guide · 7 Nov 2026 edition · schematic plan, not to scale"
if not os.environ.get("PLAYWRIGHT_BROWSERS_PATH") and os.path.isdir("/opt/pw-browsers"):
    os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "/opt/pw-browsers"


# ---------------------------------------------------------------- stops, from the track files
def tidy(s):
    """Writers' markers are never printed: [O5], [O-map, O2], ALT-K, and sentences that are notes for the on-site check."""
    s = re.sub(r"\s*\[[^\]]*\]", "", s)
    s = re.sub(r"\bALT-[A-Z0-9]+\b:?\s*", "", s)
    s = re.sub(r";\s*\)", ")", s).replace("()", "").replace("( ", "(")
    keep = [x for x in re.split(r"(?<=[.!?])\s+", s) if not re.search(r"\bO\d+\b|\bO-map\b|on-site check", x)]
    return re.sub(r"\s{2,}", " ", " ".join(keep)).strip()


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
    TR[n] = dict(type=ttype, room=tidy(h.get("room", "")), title=tidy(t), words=w, section=h.get("section", ""),
                 extra=extra, where=tidy(h.get("where", "")))
if not TR: sys.exit("no track files in " + TRACKS)
NUMS = sorted(TR)
XS = {n for n in NUMS if TR[n]["extra"]}

# ---------------------------------------------------------------- the three lengths (visit times as in the launchers and README)
J = json.load(open(LENGTHS_JSON, encoding="utf-8"))
H_SET = {int(x) for x in J["HIGHLIGHTS"].split()}; E_SET = {int(x) for x in J["ESSENTIAL"].split()}
F_SET = set(NUMS)
FX = len(XS)
LENGTHS = [("Full tour", F_SET, "about 2 h 10", f"every stop and all {FX} Extras: the Casa del Guarda floor by floor, the viaducts, the gardens, the square in full"),
           ("Essential", E_SET, "about 1 h 15", "the gate and its gatehouses, the Low Viaduct, the stairway, the hall, the gardens, the square and the view, the Portico, Casa Larrard"),
           ("Highlights", H_SET, "about 45 min", "the gate, the dragon, the hall and its ceiling, the bench, the view, the Portico")]

# ---------------------------------------------------------------- palette, sections
PAPER, INK, MUTED, LINE = "#F6F1E7", "#1F1B17", "#776E62", "#D8CEBD"
RED, GOLD, NAVY = "#C0262D", "#A9812F", "#1D2B4A"
ONEWAY = "#C0262D"
SECS = {  # @section -> (short title, dot colour, official letters, how to get there)
    "The gate": ("The gate", "#1D2B4A", "A, B",
                 "Inside the Carrer d'Olot gate: the entrance esplanade between the two gatehouses. Coming in by another gate? Play the first track just inside it: it tells you how to reach the start."),
    "Inside the Casa del Guarda": ("Inside the Casa del Guarda", "#6B4E9B", "B, inside",
                 "Three short Extras, one per floor, if you can go inside the Casa del Guarda."),
    "The viaducts": ("The viaducts", "#8A5A2B", "not on the official drawing",
                 "A side trip before the second ticket check, there and back: along the inside of the wall past the Casa del Guarda to the Marianao entrance, up the steps and ramps to the Low Viaduct."),
    "The Dragon Stairway": ("The Dragon Stairway", "#B03A2E", "C",
                 "The second ticket check is at the foot of the stairway. From here on the route is one way: there is no going back."),
    "The Hypostyle Room": ("The Hypostyle Room", "#2C6E8F", "D, E",
                 "At the top of the stairway: the hall's front first (D), then inside, among the columns (E)."),
    "The Austria Gardens": ("The Austria Gardens", "#3E7D3A", "F",
                 "Up the hall's right-hand side into the terraced gardens, up through the terraces and along the upper path to the square."),
    "The Nature Square": ("The Nature Square", "#A87A0C", "G",
                 "The great square on the roof of the hall. Hear the view before you leave it: you can't come back."),
    "The Portico": ("The Portico", "#8C3B6E", "H",
                 "Out at the square's other corner, through the old iron door, along the path among the pines above Casa Larrard."),
    "Casa Larrard": ("Casa Larrard", "#C05A3C", "I",
                 "At the foot of the spiral ramp. The house is a school: outside only."),
    "The way out": ("The way out", "#4A5560", "",
                 "Down past a small round bandstand and along the inside of the wall to the Carrer d'Olot gate."),
}
def colour(n): return SECS.get(TR[n]["section"], ("", INK))[1]
def esc(s): return html.escape(s, quote=True)
def sec_ns(*secs): return [n for n in NUMS if TR[n]["section"] in secs]
def rng(sec):
    ns = sec_ns(sec)
    return (f"{ns[0]}–{ns[-1]}" if len(ns) > 1 else f"{ns[0]}") if ns else ""

DASH = "1.2,.8"
GRASS, PAVE, PATH, WALL = "#DCE6CC", "#EFE7D7", "#E8E1D3", "#B9A88A"
STONE, PINK, TREE = "#CDBB97", "#E9B7AE", "#9DBB85"


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
    def route(self, pts, kind="main", mid=True, end=True, minlen=12, scale=1.0):
        """main = dashed ink with arrows (outside the one-way section); oneway = solid red with arrows;
        unc = dotted (a way not on the official drawing, to be confirmed on site)."""
        P = [self.T(*p) for p in pts]; d = "M" + " L".join(f"{x:.2f},{y:.2f}" for x, y in P)
        z = scale
        self.add(f'<path d="{d}" fill="none" stroke="#FDFBF7" stroke-opacity=".8" stroke-width="{1.5 * z:.2f}" stroke-linecap="round" stroke-linejoin="round"/>')
        col = INK
        if kind == "main":
            self.add(f'<path d="{d}" fill="none" stroke="{INK}" stroke-opacity=".78" stroke-width="{.55 * z:.2f}" stroke-dasharray="{1.5 * z:.2f},{1 * z:.2f}" stroke-linecap="round" stroke-linejoin="round"/>')
        elif kind == "oneway":
            col = ONEWAY
            self.add(f'<path d="{d}" fill="none" stroke="{ONEWAY}" stroke-opacity=".9" stroke-width="{.75 * z:.2f}" stroke-linecap="round" stroke-linejoin="round"/>')
        else:
            self.add(f'<path d="{d}" fill="none" stroke="{INK}" stroke-opacity=".75" stroke-width="{.8 * z:.2f}" stroke-dasharray="{.1 * z:.2f},{1.2 * z:.2f}" stroke-linecap="round" stroke-linejoin="round"/>')
        if mid:
            for (xa, ya), (xb, yb) in zip(P, P[1:]):
                if math.hypot(xb - xa, yb - ya) < minlen * z: continue
                self.arrowhead((xa + xb) / 2, (ya + yb) / 2, math.degrees(math.atan2(yb - ya, xb - xa)), 1.05 * z, col)
        if end:
            (xa, ya), (xb, yb) = P[-2], P[-1]
            self.arrowhead(xb, yb, math.degrees(math.atan2(yb - ya, xb - xa)), 1.05 * z, col)
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
        colr = {"start": INK, "finish": INK, "info": MUTED, "warn": GOLD, "oneway": ONEWAY}[kind]
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
    def letter(self, x, y, L, fs=2.3):
        """An official stop letter (A-I, as on the park's own route drawing), in a gold square."""
        cx, cy = self.T(x, y); h = fs * 1.5
        self.add(f'<rect x="{cx - h / 2:.2f}" y="{cy - h / 2:.2f}" width="{h:.2f}" height="{h:.2f}" rx=".5" fill="{GOLD}" stroke="#fff" stroke-width=".25"/>'
                 f'<text x="{cx:.2f}" y="{cy + fs * .36:.2f}" class="lt" style="font-size:{fs:.2f}px">{L}</text>', True)
    def stairs(self, a, b, w, n, colr="#8F8473", dash=None, fill="#E4DACA"):
        """A flight of steps seen from above, from world a to world b, w world units wide, n treads."""
        (x0, y0), (x1, y1) = a, b; L = math.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / L, (y1 - y0) / L; nx, ny = -uy * w / 2, ux * w / 2
        self.poly([(x0 + nx, y0 + ny), (x1 + nx, y1 + ny), (x1 - nx, y1 - ny), (x0 - nx, y0 - ny)], fill, colr, .3, dash)
        for i in range(1, n):
            t = i / n; px, py = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
            self.line([(px + nx, py + ny), (px - nx, py - ny)], colr, .22)
    def done(self): return "".join(self.o) + "</g>" + "".join(self.top) + "</svg>"


# ---------------------------------------------------------------- the park, schematic (one geometry, every view)
# World grid (no scale): Carrer d'Olot along the bottom, the hill rising toward the top; left/right as seen on the
# esplanade facing up the stairway. Positions follow the official drawing as read in the MAP note; the viaducts (not on
# the drawing) are placed to the right, beyond the Casa del Guarda, as PLAN_V2 describes the way to them.
VIEW = (40, 140, 1190, 800)
GATE = (610, 742)
A_PAV, B_PAV = (470, 668), (752, 668)            # the tower pavilion (left), the Casa del Guarda (right)
CONTROL = (610, 596)
ESPLANADE = [(420, 724), (800, 724), (790, 610), (430, 610)]
HALL = (515, 352, 705, 452)                      # the Hypostyle Room (its front faces the stairway)
SQUARE = [(430, 190), (812, 186), (820, 300), (792, 340), (440, 342), (420, 300)]
GARDENS = [(735, 340), (990, 330), (1000, 600), (812, 604), (740, 470)]
LARRARD = (205, 392, 390, 450)                   # Casa Larrard, the long house, with the school's yard in front
PORTICO = [(112, 268), (150, 268), (152, 482), (114, 482)]
RAMP = (152, 535)
BANDSTAND = (238, 650)
MARIANAO = (930, 724)
LOW_VIADUCT = [(968, 668), (1120, 560)]
MID_VIADUCT = [(1090, 452), (1170, 388)]
IRON_DOOR = (432, 252)
SANT_JOSEP = (78, 700)


def bench_pts():
    """The wavy tiled bench along the square's front edge (the stairway side)."""
    return [(452 + i * 7, 333 + 9 * math.sin(i * 7 / 340 * math.tau * 2.5)) for i in range(int((790 - 452) / 7) + 1)]


def park(s, lvl):
    """Ground, wall, buildings, square, gardens, stairway, landmarks and labels; lvl 0 = overview, 1 = locator."""
    k = s.k
    s.rect(s.x0 - 50, s.y0 - 50, VIEW[2] + 50, VIEW[3] + 50, GRASS)
    s.rect(s.x0 - 50, 748, VIEW[2] + 50, VIEW[3] + 50, "#E2DCCF")                    # Carrer d'Olot
    s.line([(60, 742), (580, 742)], WALL, max(.6, 7 * k)); s.line([(640, 742), (1180, 742)], WALL, max(.6, 7 * k))   # the wall
    for x in range(70, 1180, 26):
        if not 575 < x < 645: s.circle(x, 742, max(.25, 2.4 * k), "#3E7FB0")               # its tiled top, a hint
    s.poly(ESPLANADE, PAVE, "#CBBFA8", .3)
    # paths: along the inside of the wall, to the Marianao entrance, round the Portico and the ramp
    for pts in ([(160, 716), (590, 716)], [(640, 716), (930, 716)], [(930, 716), (968, 668)],
                [(150, 300), (330, 250), (430, 252)], [(132, 482), RAMP, (180, 600), BANDSTAND, (300, 712)],
                [(1120, 560), (1130, 500), (1090, 452)], [(78, 700), (160, 716)]):
        s.line(pts, PATH, max(.8, 11 * k))
    # the Austria Gardens: terraces
    s.poly(GARDENS, "#CFE0BC", "#9DB78A", .3)
    for i, y in enumerate(range(380, 600, 44)):
        s.line([(760 + (i % 2) * 20, y), (990, y - 6)], "#9DB78A", .22, dash=DASH)
    for x, y in ((960, 360), (860, 360), (950, 560), (830, 580), (900, 420)):
        s.circle(x, y, max(.6, 7 * k), TREE)
    # the square and its wavy bench; the hall below it (the square is the hall's roof)
    s.poly(SQUARE, "#F1E6CC", "#C9B68E", .35)
    hx0, hy0, hx1, hy1 = HALL
    s.rect(hx0, hy0, hx1, hy1, "#E6DCC8", "#9C8A68", .35)
    if lvl == 0:
        for i in range(8):
            for j in range(4):
                s.circle(hx0 + 16 + i * 23, hy0 + 14 + j * 24, max(.25, 3.2 * k), "#9C8A68")
    BP = bench_pts()
    s.line(BP, "#FDFBF7", max(1.0, 12 * k)); s.line(BP, "#2F7DB6", max(.6, 7 * k))
    for i, p in enumerate(BP[::3]):
        s.circle(p[0], p[1], max(.2, 2.6 * k), ("#E8C33A", "#C8452F", "#4E9A5B", "#FDFBF7")[i % 4])
    # the Dragon Stairway (C), two flights either side of the middle, from the control up to the hall
    s.stairs((610, 590), (610, 456), 46, 14)
    # the gatehouses
    for (x, y), roof in ((A_PAV, "tower"), (B_PAV, "cap")):
        s.rect(x - 36, y - 22, x + 36, y + 22, "#E9D6B4", "#7E6A45", .3)
        cx, cy = s.T(x, y); z = max(k / .16, .45)
        if roof == "tower":
            s.add(f'<g transform="translate({cx + 3.2 * z:.2f},{cy - 1 * z:.2f})"><rect x="{-1 * z:.2f}" y="{-5 * z:.2f}" width="{2 * z:.2f}" height="{5.6 * z:.2f}" fill="#3E7FB0"/>'
                  f'<path d="M{-1.1 * z:.2f},{-5 * z:.2f} L0,{-6.6 * z:.2f} L{1.1 * z:.2f},{-5 * z:.2f} Z" fill="#2B5E86"/></g>', True)
        else:
            s.add(f'<ellipse cx="{cx:.2f}" cy="{cy - 1.6 * z:.2f}" rx="{1.8 * z:.2f}" ry="{1.2 * z:.2f}" fill="#FDFBF7" stroke="#7E6A45" stroke-width=".25"/>', True)
    # Casa Larrard and the Portico, the ramp, the bandstand
    s.rect(*LARRARD, PINK, "#A86A5E", .3)
    s.poly(PORTICO, STONE, "#8F7A55", .3)
    for y in range(282, 480, 18):
        s.circle(118, y, max(.25, 3.2 * k), "#8F7A55")
    rx, ry = s.T(*RAMP); r = max(1.2, 16 * k)
    s.add(f'<path d="M{rx:.2f},{ry:.2f} m{-r:.2f},0 a{r:.2f},{r:.2f} 0 1,1 {2 * r:.2f},0 a{r * .7:.2f},{r * .7:.2f} 0 1,1 {-1.4 * r:.2f},0 a{r * .35:.2f},{r * .35:.2f} 0 1,1 {.7 * r:.2f},0" fill="none" stroke="#8F7A55" stroke-width=".35"/>', True)
    s.circle(*BANDSTAND, max(.7, 10 * k), "#E9D6B4", "#7E6A45", .3)
    # the viaducts: the Low Viaduct and the Middle Viaduct (not on the official drawing; schematic)
    s.line(LOW_VIADUCT, "#8F7A55", max(.9, 14 * k)); s.line(LOW_VIADUCT, "#E4DACA", max(.5, 8 * k))
    s.line(MID_VIADUCT, "#8F7A55", max(.9, 12 * k), dash=DASH)
    # the second ticket check: a red bar across the foot of the stairway
    s.line([(CONTROL[0] - 40, CONTROL[1]), (CONTROL[0] + 40, CONTROL[1])], ONEWAY, max(.6, 7 * k))
    # the iron door
    s.rect(IRON_DOOR[0] - 7, IRON_DOOR[1] - 9, IRON_DOOR[0] + 7, IRON_DOOR[1] + 9, "#4A3F33")
    # gate symbols
    for (x, y) in (GATE, SANT_JOSEP, MARIANAO):
        s.rect(x - 14, y - 6, x + 14, y + 6, "#FDFBF7", INK, .3)
    if lvl:
        return
    for x, y, t, cls, fs in LABELS:
        s.text(x, y, t, cls, "middle", fs, top=True)
    for x, y, L in LETTERS:
        s.letter(x, y, L)


LABELS = [  # (x, y, text, class, size)
    (800, 775, "Carrer d'Olot", "st", 2.3),
    (610, 760, "main gate", "pls", 1.8),
    (440, 625, "tower\npavilion", "plm", 1.8), (790, 625, "Casa del\nGuarda", "plm", 1.9),
    (700, 640, "entrance esplanade", "sts", 1.8),
    (600, 616, "2nd ticket check", "plw", 1.9),
    (690, 520, "Dragon\nStairway", "plb", 2.1),
    (610, 438, "Hypostyle Room", "plb", 2.1),
    (620, 268, "Nature Square", "plb", 2.5), (620, 204, "(on the roof of the hall)", "sts", 1.7),
    (895, 600, "Austria Gardens", "plb", 2.1),
    (298, 421, "Casa Larrard (a school)", "plm", 1.8),
    (290, 226, "path above Casa Larrard", "sts", 1.8),
    (90, 380, "Portico of the\nWasherwoman", "plb", 1.8),
    (212, 548, "spiral ramp", "pls", 1.7), (282, 638, "bandstand", "pls", 1.7),
    (432, 230, "iron door", "pls", 1.7),
    (92, 728, "Sant Josep de la\nMuntanya gate", "pls", 1.6),
    (935, 760, "Marianao entrance", "pls", 1.7),
    (1035, 580, "Low Viaduct", "plb", 1.9), (1110, 362, "Middle Viaduct\n(in view, if open)", "pls", 1.7),
    (380, 732, "along the inside of the wall", "sts", 1.7),
]
LETTERS = [(A_PAV[0] - 52, A_PAV[1] - 6, "A"), (B_PAV[0] - 52, B_PAV[1] - 6, "B"), (580, 530, "C"), (500, 400, "D"),
           (720, 420, "E"), (1010, 470, "F"), (440, 205, "G"), (200, 268, "H"), (118, 535, "I")]

# ---------------------------------------------------------------- the route (walking order), shared by every view
R_GATE = [GATE, (610, 700), (520, 690), (470, 640), (752, 640), (790, 690), (800, 716), (930, 716)]
R_VIA = [(930, 716), (968, 668), (1040, 618), (1110, 566)]
R_VIA_MID = [(1110, 566), (1125, 500), (1100, 462)]
R_BACK = [(1092, 590), (1020, 638), (952, 690), (900, 700), (800, 700), (700, 652), (640, 622), (CONTROL[0], CONTROL[1] + 10)]
R_ONEWAY = [(CONTROL[0], CONTROL[1] - 8), (610, 462), (540, 452), (560, 400), (650, 380), (712, 400), (760, 480), (800, 560),
            (930, 560), (800, 490), (960, 440), (930, 380), (880, 330), (812, 250), (720, 220), (650, 300), (540, 312),
            (450, 262), IRON_DOOR, (330, 252), (190, 270), (134, 300), (134, 470), (RAMP[0], RAMP[1] - 20)]
R_OUT = [(RAMP[0], RAMP[1] + 18), (180, 600), BANDSTAND, (300, 712), (560, 716), (GATE[0] - 6, GATE[1] - 14)]


def draw_route(s, scale=1.0):
    s.route(R_GATE, "main", minlen=14, end=False, scale=scale)
    s.route(R_VIA, "main", minlen=14, scale=scale)
    s.route(R_VIA_MID, "unc", mid=False, scale=scale)
    s.route(R_BACK, "main", minlen=14, scale=scale)
    s.route(R_ONEWAY, "oneway", minlen=16, scale=scale)
    s.route(R_OUT, "main", minlen=16, scale=scale)


# where every track's dot goes: the first rule whose test matches the track's @section / @room (lower case) wins;
# tracks with the same group share a row of dots. Renumbering keeps working; a track no rule matches is placed at its
# section's default and reported.
def _r(n): return TR[n]["room"].lower()
def _s(n): return TR[n]["section"]
GROUPS = [  # (name, test, overview position, direction)
    ("gate_in", lambda n: _s(n) == "The gate" and (TR[n]["type"] == "ANCHOR" or _r(n).startswith(("anywhere", "the carrer d'olot gate")) or "facing the wall" in _r(n)), (548, 700), "r"),
    ("between", lambda n: "between the two pavilions" in _r(n), (610, 650), "r"),
    ("tower", lambda n: "tower pavilion" in _r(n), (470, 612), "r"),
    ("guarda_door", lambda n: _s(n) == "The gate" and "casa del guarda" in _r(n), (752, 612), "r"),
    ("guarda_in", lambda n: _s(n) == "Inside the Casa del Guarda", (812, 668), "r"),
    ("viaduct_on", lambda n: "low viaduct" in _r(n) and "on the viaduct" in _r(n), (1000, 616), "r"),
    ("viaduct_by", lambda n: "low viaduct" in _r(n), (1070, 640), "r"),
    ("viaduct_mid", lambda n: "middle viaduct" in _r(n), (1072, 418), "r"),
    ("queue", lambda n: "queue" in _r(n), (524, 600), "r"),
    ("stair_foot", lambda n: _s(n) == "The Dragon Stairway" and "at the foot" in _r(n), (662, 588), "r"),
    ("stair_mid", lambda n: _s(n) == "The Dragon Stairway" and ("halfway" in _r(n) or "dragon" in _r(n).split("·", 1)[-1]), (652, 546), "r"),
    ("stair_top", lambda n: _s(n) == "The Dragon Stairway", (662, 478), "r"),
    ("hall_out", lambda n: _s(n) == "The Hypostyle Room" and "outside" in _r(n), (480, 440), "r"),
    ("hall_in", lambda n: _s(n) == "The Hypostyle Room", (555, 410), "r"),
    ("gardens_in", lambda n: _s(n) == "The Austria Gardens" and "just inside" in _r(n), (780, 520), "r"),
    ("gardens_mid", lambda n: _s(n) == "The Austria Gardens" and ("middle" in _r(n) or "pink house" in _r(n)), (850, 470), "r"),
    ("gardens_terrace", lambda n: _s(n) == "The Austria Gardens" and "terrace" in _r(n), (950, 405), "r"),
    ("gardens_upper", lambda n: _s(n) == "The Austria Gardens", (880, 300), "r"),
    ("square_open", lambda n: _s(n) == "The Nature Square" and "bench" not in _r(n), (680, 240), "r"),
    ("square_bench", lambda n: _s(n) == "The Nature Square", (530, 312), "r"),
    ("pines", lambda n: "path above casa larrard" in _r(n), (350, 278), "r"),
    ("portico", lambda n: _s(n) == "The Portico", (170, 330), "d"),
    ("larrard", lambda n: _s(n) == "Casa Larrard", (196, 498), "r"),
    ("wall_walk", lambda n: _s(n) == "The way out" and "walking" in _r(n), (420, 700), "r"),
    ("gate_out", lambda n: _s(n) == "The way out", (700, 700), "r"),
]
DEFAULT = {"The gate": (610, 650), "Inside the Casa del Guarda": (812, 668), "The viaducts": (1040, 640),
           "The Dragon Stairway": (662, 520), "The Hypostyle Room": (555, 410), "The Austria Gardens": (870, 470),
           "The Nature Square": (620, 300), "The Portico": (170, 330), "Casa Larrard": (232, 520), "The way out": (420, 700)}
PLACED, UNPLACED = {}, []
for n in NUMS:
    for name, test, pos, dr in GROUPS:
        if test(n):
            PLACED.setdefault(name, (pos, dr, []))[2].append(n); break
    else:
        UNPLACED.append(n); PLACED.setdefault("sec:" + _s(n), (DEFAULT.get(_s(n), (610, 650)), "r", []))[2].append(n)
if UNPLACED: print("route_map: placed by section only:", UNPLACED)


def place_dots(s, rad):
    for name, (pos, dr, ns) in PLACED.items():
        s.dots(*pos, ns, dr, rad)


# ---------------------------------------------------------------- stop lists, dots in text, legends
def dot(n, cls="dot"):
    c = colour(n)
    if n in XS: return f'<span class="{cls} hol" style="color:{c};border-color:{c}">{n}</span>'
    return f'<span class="{cls}" style="background:{c}">{n}</span>'
def badges(n):
    b = []
    if n in XS: b.append(f'<span class="bx" style="color:{colour(n)};border-color:{colour(n)}">Extra</span>')
    if n in E_SET: b.append('<span class="be">Essential</span>')
    if n in H_SET: b.append('<span class="bh">Highlights</span>')
    return "".join(b)
def stop_rows(secs):
    out = []
    for sec in secs:
        ns = sec_ns(sec)
        if not ns: continue
        short, c, letters, how = SECS[sec]
        lt = f' · official {esc(letters)}' if letters and len(letters) <= 9 else (f' · {esc(letters)}' if letters else "")
        out.append(f'<div class="sech" style="border-color:{c}"><b style="color:{c}">{esc(short)}</b> <span>{rng(sec)}{lt}</span><p>{esc(how)}</p></div>')
        for n in ns:
            t = TR[n]; x = ' x' if n in XS else ''
            out.append(f'<div class="row{x}">{dot(n)}<div class="tt"><b>{esc(t["title"])}</b> {badges(n)}'
                       f'<div class="rm" style="color:{c}">{esc(t["room"])}</div><div class="wh">{esc(t["where"])}</div></div></div>')
    return "".join(out)
def sw(svg): return f'<svg width="9mm" height="3mm" viewBox="0 0 9 3">{svg}</svg>'
_ROUTE_SW = sw(f'<path d="M.5,1.5 L8.5,1.5" stroke="{INK}" stroke-opacity=".78" stroke-width=".55" stroke-dasharray="1.5,1"/>')
_ONEWAY_SW = sw(f'<path d="M.5,1.5 L8.5,1.5" stroke="{ONEWAY}" stroke-width=".75"/>')
_UNC_SW = sw(f'<path d="M.5,1.5 L8.5,1.5" stroke="{INK}" stroke-width=".8" stroke-dasharray=".1,1.2" stroke-linecap="round"/>')
_CTRL_SW = sw(f'<path d="M1,1.5 L8,1.5" stroke="{ONEWAY}" stroke-width="1.1"/>')
N_ANY = next((n for n in NUMS if n not in XS), NUMS[0])
LEGEND = ('<div class="legend">'
          f'<span>{dot(N_ANY, "ldot")} track</span><span><span class="ldot hol" style="color:{INK};border-color:{INK}">X</span> Extra</span>'
          f'<span>{_ROUTE_SW} route, in walking order</span><span>{_ONEWAY_SW} one-way section: no going back</span>'
          f'<span>{_CTRL_SW} second ticket check</span><span>{_UNC_SW} only if the path is open</span>'
          '<span><span class="llt">A</span> official stop letter</span>'
          '</div>')


# ---------------------------------------------------------------- page 1: the whole loop
def whole_svg():
    s = Svg(VIEW)
    park(s, 0); draw_route(s); place_dots(s, 2.05)
    s.note(GATE[0], GATE[1], "START and END · the Carrer d'Olot gate", "start", 62, s.H - 3.6, 2.2)
    s.note(1080, 600, "viaducts: there and back,\nbefore the second check", "info", s.W - 22, s.H - 14, 2.0)
    s.note(CONTROL[0] - 40, CONTROL[1], "ONE WAY from here", "oneway", 46, 72, 2.1)
    s.text(s.W - 2, 4, "SCHEMATIC · NOT TO SCALE", "scl", "end", 2.2, page=True, top=True)
    return s.done()


def locator(box):
    """The whole loop, small, with the part a page covers framed and the rest dimmed."""
    s = Svg(VIEW, W=64)
    park(s, 1); draw_route(s, .45)
    x0, y0, x1, y1 = box
    (a, b), (c, e) = s.T(x0, y0), s.T(x1, y1)
    s.add(f'<path d="M0,0 H{s.W} V{s.H} H0 Z M{a:.2f},{b:.2f} V{e:.2f} H{c:.2f} V{b:.2f} Z" fill="#FDFBF7" fill-opacity=".62" fill-rule="evenodd"/>', True)
    s.add(f'<rect x="{a:.2f}" y="{b:.2f}" width="{c - a:.2f}" height="{e - b:.2f}" rx="1" fill="none" stroke="{GOLD}" stroke-width=".5"/>', True)
    for x, y, L in LETTERS:
        s.letter(x, y, L, 1.7)
    return s.done()


KEYS = "".join(f'<span><i style="background:{SECS[k][1]}"></i><em>{esc(SECS[k][0])} <b>{rng(k)}</b></em></span>' for k in SECS if rng(k))
def len_card(i, name, ns, when, desc):
    ds_ = "".join(dot(n, "mdot") for n in sorted(ns))
    return (f'<div class="card"><div class="ch"><div class="cnum">{i}</div><div><div class="ct">{esc(name)}</div>'
            f'<div class="cs"><b>{esc(when.replace("about ", "≈ "))}</b> · {len(ns)} tracks</div></div></div>'
            f'<div class="cdots">{ds_}</div><div class="cs2">{esc(desc)}</div></div>')
lens = "".join(len_card(i, n, ns, m, d) for i, (n, ns, m, d) in enumerate(LENGTHS, 1))
pages = []
pages.append(f'''<section class="page">
 <header><div class="brand">YO TOURS · AUDIO GUIDE</div><h1>Park Güell</h1>
 <p class="lede">The estate that became a park: {len(F_SET) - FX} main stops plus {FX} short Extras in one loop, in the park's own A–I order, in three lengths.</p></header>
 <div class="how"><div><b>1</b> <strong>Outside first, then one way.</strong> The gate, the Casa del Guarda and the viaducts come first. From the second ticket check at the foot of the stairway the route is one way, A to I, and ends back at the Carrer d'Olot gate.</div>
 <div><b>2</b> Each circle is the track to play there; hollow ones are short Extras. Every track ends by telling you where to go next. Pages 2–4 say where to stand for every track.</div>
 <div><b>3</b> Any gate works: play the first track just inside it. <strong>Headphones only</strong>: the park does not allow speakers. Once you leave the park you can't come back in.</div></div>
 <div class="ov">{whole_svg()}<div class="keys">{KEYS}</div>{LEGEND}</div>
 <div class="cards">{lens}</div>
 <div class="warn"><b>Steep paths and steps</b> on the way to the viaducts, on the Dragon Stairway, in the gardens and down the ramp. Times include walking and a short wait at the second ticket check. Shorter versions: the numbers jump, and a spoken line tells you the next stop.</div>
 <footer>{esc(FOOTER)}</footer>
</section>''')


# ---------------------------------------------------------------- pages 2-4: where to stand, section by section
def list_page(kicker, title, secs, box, intro):
    ns = sec_ns(*secs)
    span = f"{ns[0]}–{ns[-1]}" if ns else ""
    return f'''<section class="page">
 <header class="lh"><div class="lhl"><div class="brand">YO TOURS · PARK GÜELL · {esc(kicker)}</div>
 <h2>{esc(title)} · {span}</h2><p class="sub">{intro}</p></div>
 <div class="loc">{locator(box)}<div class="locl">this page, on the whole loop</div></div></header>
 <div class="stops">{stop_rows(secs)}</div>
 <footer>{esc(FOOTER)}</footer>
</section>'''


pages.append(list_page("WHERE TO STAND · 1", "The gate, the Casa del Guarda and the viaducts",
    ("The gate", "Inside the Casa del Guarda", "The viaducts"), (400, 440, 1190, 795),
    "Everything here is outside the one-way section, so it comes first: past the second ticket check there is no way back. "
    "Left and right are as you stand on the esplanade facing the stairway."))
pages.append(list_page("WHERE TO STAND · 2", "The stairway, the hall and the Austria Gardens",
    ("The Dragon Stairway", "The Hypostyle Room", "The Austria Gardens"), (440, 300, 1010, 620),
    "From the second ticket check the route is one way, in the official order: the stairway (C), the hall's front (D) and "
    "inside (E), then up the hall's right-hand side into the Austria Gardens (F)."))
pages.append(list_page("WHERE TO STAND · 3", "The square, the Portico, Casa Larrard and the way out",
    ("The Nature Square", "The Portico", "Casa Larrard", "The way out"), (60, 170, 830, 790),
    "Round the Nature Square (G), out at its other corner along the path above Casa Larrard (H) to the Portico, down the "
    "ramp (I), and back along the inside of the wall to the Carrer d'Olot gate."))

# ---------------------------------------------------------------- page 5: on-site notes
OFFICIAL = [("A", "Entrance and concierge", "the tower pavilion, left of the gate"), ("B", "The guardhouse", "the Casa del Guarda, right of the gate"),
            ("C", "Monumental staircase", "the Dragon Stairway"), ("D", "The hypostyle room, outdoor", "the hall's front"),
            ("E", "The hypostyle room, inside", "among the columns"), ("F", "The Austria Gardens", "the terraced gardens"),
            ("G", "Nature square", "the square and the bench"), ("H", "The roadways, paths and viaducts", "drawn on the Portico path"),
            ("I", "Ramp and house Larrard", "the spiral ramp, Casa Larrard")]
offrows = "".join(f'<tr><td><span class="llt big">{L}</span></td><td><b>{esc(a)}</b></td><td>{esc(b)}</td></tr>' for L, a, b in OFFICIAL)
NOTES = [
    ("Headphones only", "The park does not allow speakers. Keep the volume low enough to hear what is around you."),
    ("No re-entry", "Once you leave the park you cannot come back in. That is why the gate, the Casa del Guarda and the viaducts come first, and why the loop ends at the Carrer d'Olot gate."),
    ("One-way section", "From the second ticket check at the foot of the Dragon Stairway the route is one way: the stairway, the hall, the Austria Gardens, the Nature Square, the Portico and the ramp. There is no going back, so hear the view from the bench before you leave the square."),
    ("Steep paths and steps", "Steps and ramps up to the viaducts, the stairway itself, the garden terraces and the spiral ramp down. Watch your step, above all on the way down."),
    ("Any gate", "Coming in by another gate? Play the first track just inside it, out of the way of the ticket check: it tells you how to reach the start on the entrance esplanade."),
    ("Only if it is open", "The Casa del Guarda's three floors (Extras), the Middle Viaduct (Extra, only if the path is open; never go past a works closure) and the Font Sarva room (Extra) are for when you can reach them."),
    ("Outside only", "Casa Larrard is a school, Casa Trias a private home, and the pink house with the pointed tower a museum: the guide looks at them from the path."),
    ("Out of the way", "Many tracks are played on busy paths: step to one side, keep clear of doorways, queues and people sitting on the bench, and let the one-way flow pass."),
]
notes = "".join(f'<div class="nbox"><h3>{esc(h)}</h3><p>{esc(p)}</p></div>' for h, p in NOTES)
pages.append(f'''<section class="page">
 <header class="fh"><div class="brand">YO TOURS · PARK GÜELL · ON SITE</div>
 <h2>Before you start</h2><p class="sub">A few things to know on the ground. No prices, hours or tickets here: check them with the park before your visit.</p></header>
 <div class="notes">{notes}</div>
 <h3 class="oh">The official stops, A to I</h3>
 <p class="sub">These are the letters of the park's own recommended-routes drawing; this guide follows them in the same order. The viaducts are not on the official drawing.</p>
 <table class="off">{offrows}</table>
 <p class="tfoot">This plan is our own schematic drawing, not to scale, made from the park's recommended-routes drawing and the guide's own directions. Where the ground differs, follow the park's signs and staff.</p>
 <footer>{esc(FOOTER)}</footer>
</section>''')

CSS = f'''
@page {{ size: A4; margin: 0 }}
* {{ box-sizing: border-box }}
html, body {{ margin: 0; background: {PAPER}; color: {INK}; font-family: Inter, "DejaVu Sans", sans-serif }}
.page {{ width: 210mm; height: 297mm; padding: 11mm 13mm 10mm; position: relative; page-break-after: always; overflow: hidden; background: {PAPER} }}
.brand {{ font: 600 7.6pt Inter; letter-spacing: .28em; color: {GOLD} }}
h1 {{ font: 700 25pt Lora, serif; margin: 1.6mm 0 1mm; letter-spacing: -.01em }}
h2 {{ font: 700 16pt Lora, serif; margin: 1.6mm 0 1mm }}
h3 {{ font: 700 9.6pt Lora, serif; margin: 0 0 1mm }}
.lede {{ font: 400 10.4pt Lora, serif; color: {MUTED}; margin: 0 0 2.6mm; line-height: 1.35 }}
.sub {{ font: 400 8.2pt Inter; color: {MUTED}; margin: 0 0 2.2mm; max-width: 184mm; line-height: 1.36 }}
.how {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 3mm; margin-bottom: 2.4mm }}
.how div {{ background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; padding: 2mm 2.6mm; font: 500 7.6pt Inter; line-height: 1.32 }}
.how b {{ display: inline-flex; width: 5mm; height: 5mm; border-radius: 50%; background: {INK}; color: #fff; font: 700 7.5pt Inter; align-items: center; justify-content: center; margin-right: 1.2mm }}
.how strong {{ color: {RED} }}
.ov {{ background: #FDFBF7; border: .3mm solid {LINE}; border-radius: 4mm; padding: 1.5mm 1mm; margin-bottom: 2.4mm }}
.ov > svg {{ display: block; margin: 0 auto; width: 100%; height: auto }}
.keys {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: .8mm 3mm; padding: 1.4mm 3mm 0; font: 500 6.7pt Inter; color: {INK} }}
.keys span {{ display: flex; align-items: flex-start; gap: 1.4mm }} .keys em {{ font-style: normal; line-height: 1.25 }} .keys b {{ color: {MUTED}; font-weight: 600; white-space: nowrap }}
.keys i {{ width: 3mm; height: 3mm; border-radius: 50%; flex: none; margin-top: .2mm }}
.warn {{ background: #fff; border: .3mm solid {GOLD}; border-left: 1.6mm solid {GOLD}; border-radius: 2.4mm; padding: 2mm 3mm; font: 400 7.8pt Inter; line-height: 1.36; margin-bottom: 3mm }}
.cards {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.4mm; margin-bottom: 2.4mm }}
.card {{ background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; padding: 2mm 2.4mm }}
.ch {{ display: grid; grid-template-columns: 9mm 1fr; align-items: center }}
.cnum {{ width: 7mm; height: 7mm; border-radius: 50%; color: #fff; background: {NAVY}; font: 700 11pt Inter; display: flex; align-items: center; justify-content: center }}
.ct {{ font: 700 10.2pt Lora; margin-bottom: .2mm }} .cs {{ font: 400 7.9pt Inter; color: {MUTED} }} .cs b {{ color: {INK} }}
.cdots {{ display: flex; flex-wrap: wrap; gap: .7mm; margin: 1.4mm 0 1mm }}
.mdot {{ width: 4.4mm; height: 4.4mm; border-radius: 50%; color: #fff; font: 700 5.8pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.cs2 {{ font: 400 7pt Inter; color: {MUTED}; line-height: 1.3 }}
footer {{ position: absolute; left: 13mm; right: 13mm; bottom: 6mm; font: 400 7pt Inter; color: {MUTED}; border-top: .3mm solid {LINE}; padding-top: 1.6mm }}
.lh {{ display: grid; grid-template-columns: 1fr 66mm; gap: 4mm; align-items: start; margin-bottom: 2mm }}
.loc {{ background: #FDFBF7; border: .3mm solid {LINE}; border-radius: 3mm; padding: 1mm }} .loc svg {{ display: block; width: 100%; height: auto }}
.locl {{ font: 500 6.2pt Inter; color: {MUTED}; text-align: center; padding-top: .6mm }}
.stops {{ columns: 2; column-gap: 6mm }}
.sech {{ break-inside: avoid; break-after: avoid; border-top: .5mm solid; padding: 1.4mm 0 .6mm; margin-top: 1.2mm }}
.sech b {{ font: 700 9.4pt Lora, serif }} .sech span {{ font: 600 7pt Inter; color: {MUTED} }}
.sech p {{ font: 400 6.9pt Inter; color: #4A443C; margin: .5mm 0 0; line-height: 1.3 }}
.row {{ display: grid; grid-template-columns: 7mm 1fr; align-items: start; padding: .9mm 0; border-bottom: .25mm solid {LINE}; break-inside: avoid }}
.dot {{ width: 6mm; height: 6mm; border-radius: 50%; color: #fff; font: 700 7.4pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.hol {{ background: #fff; border: .45mm solid; box-sizing: border-box }}
.tt {{ font: 500 7.4pt Inter; line-height: 1.24; padding-left: 1.2mm }} .tt > b {{ font-weight: 700; color: {INK} }}
.rm {{ font: 600 6.8pt Inter; margin-top: .3mm }} .wh {{ font: 400 6.8pt Inter; color: #4A443C; margin-top: .2mm }}
.row.x .tt > b {{ color: #4A443C }}
.bx, .be, .bh {{ display: inline-block; font: 700 5.4pt Inter; letter-spacing: .03em; border-radius: 1mm; padding: 0 .8mm; margin-left: .6mm; vertical-align: .2mm }}
.bx {{ border: .25mm solid; background: #fff }} .be {{ background: #E3E8F2; color: {NAVY} }} .bh {{ background: {NAVY}; color: #fff }}
.sn {{ font-family: Inter; font-weight: 700; fill: #fff; text-anchor: middle }}
.lt {{ font-family: Inter; font-weight: 800; fill: #fff; text-anchor: middle }}
.note {{ font-family: Inter; font-weight: 600; fill: #fff }}
.pl, .plb, .plm, .pls, .plw, .st, .sts {{ paint-order: stroke; stroke: #FDFBF7; stroke-width: .7px; stroke-linejoin: round }}
.pl {{ font-family: Inter; font-weight: 700; fill: {INK} }} .plb {{ font-family: Lora, serif; font-weight: 700; fill: {INK} }}
.plm {{ font-family: Inter; font-weight: 600; fill: #3E3830 }} .pls {{ font-family: Inter; font-weight: 500; fill: #5F574C }}
.plw {{ font-family: Inter; font-weight: 700; fill: {ONEWAY} }}
.st {{ font-family: Inter; font-weight: 700; fill: #4A3F33; letter-spacing: .1px }} .sts {{ font-family: Inter; font-weight: 600; fill: #6F665A }}
.scl {{ font-family: Inter; font-weight: 700; fill: #A39886; letter-spacing: .25px }}
.legend {{ display: flex; flex-wrap: wrap; gap: 1.2mm 3.6mm; justify-content: center; padding: 1.6mm 1mm .4mm; font: 500 6.8pt Inter; color: {MUTED}; align-items: center }}
.legend > span {{ display: inline-flex; align-items: center; gap: 1.3mm }}
.ldot {{ width: 4.4mm; height: 4.4mm; border-radius: 50%; color: #fff; font: 700 6pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.llt {{ display: inline-flex; width: 3.6mm; height: 3.6mm; border-radius: .6mm; background: {GOLD}; color: #fff; font: 800 6pt Inter; align-items: center; justify-content: center }}
.llt.big {{ width: 5.4mm; height: 5.4mm; font-size: 8pt }}
.notes {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 2.6mm; margin: 1mm 0 4mm }}
.nbox {{ background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; padding: 2.4mm 3mm }}
.nbox h3 {{ color: {RED} }} .nbox p {{ font: 400 8pt Inter; line-height: 1.38; margin: 0 }}
.oh {{ font: 700 12pt Lora, serif; margin: 2mm 0 1mm }}
.off {{ width: 100%; border-collapse: collapse; background: #fff; border: .3mm solid {LINE} }}
.off td {{ padding: 1.3mm 2mm; border-bottom: .2mm solid {LINE}; font: 400 8pt Inter; vertical-align: middle }} .off td:first-child {{ width: 10mm }}
.tfoot {{ font: 400 7.6pt Inter; color: {MUTED}; margin: 3mm 0 0; line-height: 1.36 }}
'''


def build():
    doc = f'<!doctype html><html><head><meta charset="utf-8"><title>Park Güell · Yo Tours route</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
    os.makedirs(B, exist_ok=True)
    hp = os.path.join(B, "route_map.html"); open(hp, "w", encoding="utf-8").write(doc)
    async def render():
        from playwright.async_api import async_playwright
        async with async_playwright() as p:
            br = await p.chromium.launch(); pg = await br.new_page(device_scale_factor=2)
            await pg.goto("file://" + os.path.abspath(hp)); await pg.wait_for_timeout(300)
            over = await pg.evaluate("[...document.querySelectorAll('.page')].map((p, i) => [i + 1, p.scrollHeight > p.clientHeight + 1, p.scrollWidth > p.clientWidth + 1])")
            for i, oh, ow in over:
                if oh or ow: print(f"route_map: WARNING page {i} overflows ({'height' if oh else ''}{' width' if ow else ''})")
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
