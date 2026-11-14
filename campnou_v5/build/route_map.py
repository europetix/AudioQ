#!/usr/bin/env python3
"""Yo Tours · FC Barcelona Museum · Spotify Camp Nou — route sheet, 14 Nov 2026 edition (bcncat_v5's route_map.py, adapted).
A PDF made to be read on a phone: page 1 = the route outside and inside, and the three lengths; pages 2-4 = where to
stand for every track; page 5 = visit notes (this ticket does not include the stadium, headphones, the show, offline)
and what to do if a display or a space is not where the guide expects it.
Our OWN schematic drawing, not traced and not a copy of the club's maps: outside, simple shapes for Av. de Joan XXIII,
the long building with the ridged roof (the museum, in the club's old ice rink), the round Palau Blaugrana beside it
and the stadium beyond (geography from research/map/OFFICIAL_ACCESS_MAP_NOTES_14NOV2026.md: the museum at the corner
of Av. de Joan XXIII and Arístides Maillol, the arena beside it, the stadium further in); inside, not a floor plan but
the displays in the guide's order, which the museum may change ("room order may change"). Not to scale; no compass,
no distances, no gate or door numbers, no prices or hours, no crest, logo or photos. Writers' markers ([O5], ALT-K,
notes for the on-site check) are never printed.
Stops come from v5/tracks/NNN.perf.txt (@title, @room, @where, @type, @section) at run time; lengths from
build/static/lengths.json.
Usage (from the guide folder): python3 build/route_map.py <bundle folder> [--png <dir>]
  -> <bundle>/SpotifyCampNou_Audio_Guide_Route.pdf"""
import json, math, os, re, sys, html, asyncio, glob

B = sys.argv[1]
PNG_DIR = sys.argv[sys.argv.index("--png") + 1] if "--png" in sys.argv else None
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
TRACKS = os.path.join(ROOT, "v5", "tracks")
LENGTHS_JSON = os.path.join(HERE, "static", "lengths.json")
OUT_PDF = os.path.join(B, "SpotifyCampNou_Audio_Guide_Route.pdf")
FOOTER = "Yo Tours · FC Barcelona Museum · Spotify Camp Nou audio guide · 14 Nov 2026 edition · schematic, not to scale"
if not os.environ.get("PLAYWRIGHT_BROWSERS_PATH") and os.path.isdir("/opt/pw-browsers"):
    os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "/opt/pw-browsers"


# ---------------------------------------------------------------- stops, from the track files
def tidy(s):
    """Writers' markers are never printed: [O5], [O-map, O2], ALT-K, (G102: ...), and sentences that are notes for the
    on-site check. Gate numbers are never printed either (none are in the @where lines; checked below)."""
    s = re.sub(r"\s*\[[^\]]*\]", "", s)
    s = re.sub(r"\s*\([^)]*\b(?:G\d+|ALT-[A-Z0-9]+|O\d+)\b[^)]*\)", "", s)
    s = re.sub(r"\bALT-[A-Z0-9]+\b:?\s*", "", s)
    s = re.sub(r";\s*\)", ")", s).replace("()", "").replace("( ", "(")
    keep = [x for x in re.split(r"(?<=[.!?])\s+", s) if not re.search(r"\bO\d+\b|\bO-map\b|on-site check", x)]
    s = re.sub(r"\s{2,}", " ", " ".join(keep)).strip()
    return re.sub(r"\s+([.,;])", r"\1", s)


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
    extra = ttype == "X" or " Extra · " in t or t.startswith("Extra · ")     # story Extras are typed W: "Extra" is in the title
    t = re.sub(r"^.*?·\s*Extra\s*·\s*", "", t) if extra else (t.split(" · ", 1)[1] if " · " in t else t)
    TR[n] = dict(type=ttype, room=tidy(h.get("room", "")), title=tidy(t), words=w, section=h.get("section", ""),
                 extra=extra, where=tidy(h.get("where", "")))
    for k in ("room", "where", "title"):
        if re.search(r"\b(Access|Gate|Accés|Acceso)\s*\d", TR[n][k]):
            sys.exit(f"route_map: track {n} {k} names a gate number; the route sheet never prints one")
if not TR: sys.exit("no track files in " + TRACKS)
NUMS = sorted(TR)
XS = {n for n in NUMS if TR[n]["extra"]}

# ---------------------------------------------------------------- the three lengths (visit times as in 001, the launchers and README)
J = json.load(open(LENGTHS_JSON, encoding="utf-8"))
H_SET = {int(x) for x in J["HIGHLIGHTS"].split()}; E_SET = {int(x) for x in J["ESSENTIAL"].split()}
F_SET = set(NUMS)
FX = len(XS)
LENGTHS = [("Full tour", F_SET, "a little over 1 h 30", f"every stop, with all {FX} Extras: by the museum door, in a quiet corner and on the old benches"),
           ("Essential", E_SET, "about 1 h", "no outside stops or Extras: the cups, the women's team, Cruyff, La Masia, Messi, the show, the models, the viewpoint"),
           ("Highlights", H_SET, "about 35 min", "the European Cups, Messi's golden balls, the round room and its show, the viewpoint over the works")]
VER = lambda n: "".join(v for v, s_ in (("H", H_SET), ("E", E_SET), ("F", F_SET)) if n in s_)

# ---------------------------------------------------------------- palette, sections
PAPER, INK, MUTED, LINE = "#F6F1E7", "#1F1B17", "#776E62", "#D8CEBD"
RED, GOLD, NAVY = "#A5174A", "#A9812F", "#1D2B4A"
ONEWAY = RED
SECS = {  # @section -> (short title, dot colour, how to get there)
    "Outside the museum": ("Outside the museum", "#1D2B4A",
        "On Av. de Joan XXIII, by the long building with the ridged roof beside the round Palau Blaugrana; then onto the campus, where the stadium shows over the lower buildings, and back by the museum's door."),
    "The entrance hall": ("The entrance hall", "#5E6B78",
        "In through the ticket check; stop to one side of the hall, near the orientation map if there is one."),
    "The trophies": ("The trophies", "#A9812F",
        "The wall of trophies, the five big silver European Cups, the women's trophies and the wall of shirts, in whatever order the museum shows them."),
    "The club's history": ("The club's history", "#8C3B6E",
        "The displays given to Johan Cruyff, to La Masia and to Més que un club; these stops work in any order."),
    "More stories inside": ("A quiet corner", "#6B4E9B",
        "Full tour only: four Extras on a bench or in any quiet corner, out of the flow and away from the screens."),
    "Messi's space": ("Messi's space", "#2C6E8F",
        "Its way in first, then where his golden balls are in view."),
    "The round room": ("The round room", "#B03A2E",
        "The round room with the screens, where the exhibition ends: one track at its way in, then stop the guide for the show; one just outside after it."),
    "The models": ("The models", "#3E7D3A",
        "The models of the finished stadium."),
    "The viewpoint": ("The viewpoint", "#C05A3C",
        "The rail of the viewpoint over the works, with the stadium in front of you; then the original benches from the old stadium."),
    "The way out": ("The way out", "#4A5560",
        "The exit of the visit, or just outside it, out of the way."),
}
def colour(n): return SECS.get(TR[n]["section"], ("", INK))[1]
def esc(s): return html.escape(s, quote=True)
def sec_ns(*secs): return [n for n in NUMS if TR[n]["section"] in secs]
def rng(sec):
    ns = sec_ns(sec)
    return (f"{ns[0]}–{ns[-1]}" if len(ns) > 1 else f"{ns[0]}") if ns else ""

DASH = "1.2,.8"


# ---------------------------------------------------------------- SVG kit: world units (a schematic grid, no scale) -> page mm
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
    def stairs(self, a, b, w, n, colr="#8F8473", dash=None, fill="#E4DACA"):
        """A flight of steps seen from above, from world a to world b, w world units wide, n treads."""
        (x0, y0), (x1, y1) = a, b; L = math.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / L, (y1 - y0) / L; nx, ny = -uy * w / 2, ux * w / 2
        self.poly([(x0 + nx, y0 + ny), (x1 + nx, y1 + ny), (x1 - nx, y1 - ny), (x0 - nx, y0 - ny)], fill, colr, .3, dash)
        for i in range(1, n):
            t = i / n; px, py = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
            self.line([(px + nx, py + ny), (px - nx, py - ny)], colr, .22)
    def done(self): return "".join(self.o) + "</g>" + "".join(self.top) + "</svg>"



def vmarks(s, x, y, ns, rad, fs=None):
    """Under each dot of a row (page coordinates, first dot at x): the versions it plays in, H E F; absent ones pale."""
    step = rad * 2.18; fs = fs or rad * .78
    for i, n in enumerate(ns):
        cx = x + i * step; v = VER(n); parts = []
        for j, L in enumerate("HEF"):
            on = L in v
            parts.append(f'<tspan style="fill:{INK if on else "#CFC6B6"};font-weight:{800 if on else 500}">{L}</tspan>')
        s.add(f'<text x="{cx:.2f}" y="{y + rad + fs * 1.15:.2f}" class="vm" style="font-size:{fs:.2f}px;letter-spacing:{fs * .12:.2f}px">{"".join(parts)}</text>', True)


def dot_row(s, cx, cy, ns, rad, marks=True):
    """A row of track dots centred on world (cx, cy), with the versions under each."""
    px, py = s.T(cx, cy); step = rad * 2.18; x0 = px - (len(ns) - 1) * step / 2
    s.dots(x0, py, ns, "r", rad, page=True)
    if marks: vmarks(s, x0, py, ns, rad)


# ---------------------------------------------------------------- outside: the museum, the arena, the stadium beyond (schematic)
# World grid (no scale). Av. de Joan XXIII along the top, the side avenue (Arístides Maillol) down the left; the museum
# in the corner between them, the round Palau Blaugrana beside it, further into the campus the lower buildings, and
# the stadium beyond. Every position is a schematic choice of ours, read from the official maps' layout, not traced.
VIEW_OUT = (0, 0, 1000, 310)
CAMPUS, STREET, BLDG, ARENA, LOWB, STAD, BOWL, PITCH = "#ECE6DA", "#DDD6C8", "#D3C9B6", "#E2D6C0", "#E4DDCF", "#D9CFBE", "#E9E1D2", "#CFE0C4"
MUSEUM = (66, 64, 356, 150)
ARENA_C, ARENA_R = (462, 190), 80
ST_C = (900, 250)


def outside(s, lvl=0):
    k = s.k
    s.rect(-20, -20, 1020, 360, CAMPUS)
    s.rect(-20, -20, 1020, 44, STREET)                                                        # Av. de Joan XXIII
    s.rect(-20, 44, 40, 360, STREET)                                                          # the side avenue
    s.line([(40, 44), (1020, 44)], "#C2B8A6", .25); s.line([(40, 44), (40, 360)], "#C2B8A6", .25)
    # the stadium beyond: an outer ring, the bowl and the pitch; the unfinished top tier dashed
    s.add(f'<ellipse cx="{s.T(*ST_C)[0]:.2f}" cy="{s.T(*ST_C)[1]:.2f}" rx="{270 * k:.2f}" ry="{200 * k:.2f}" fill="{STAD}" stroke="#A89C86" stroke-width=".3"/>')
    s.add(f'<ellipse cx="{s.T(*ST_C)[0]:.2f}" cy="{s.T(*ST_C)[1]:.2f}" rx="{290 * k:.2f}" ry="{218 * k:.2f}" fill="none" stroke="#A89C86" stroke-width=".35" stroke-dasharray="{DASH}"/>')
    s.add(f'<ellipse cx="{s.T(*ST_C)[0]:.2f}" cy="{s.T(*ST_C)[1]:.2f}" rx="{190 * k:.2f}" ry="{135 * k:.2f}" fill="{BOWL}" stroke="#B9AE98" stroke-width=".25"/>')
    s.rect(ST_C[0] - 110, ST_C[1] - 66, ST_C[0] + 110, ST_C[1] + 66, PITCH, "#9DB78A", .25)
    # lower buildings between the arena and the stadium
    for x0, y0, x1, y1 in ((560, 70, 650, 118), (575, 250, 640, 300), (668, 96, 708, 150)):
        s.rect(x0, y0, x1, y1, LOWB, "#B9AE98", .2)
    # the round Palau Blaugrana
    s.poly([(ARENA_C[0] + ARENA_R * math.cos(math.radians(22.5 + 45 * i)), ARENA_C[1] + ARENA_R * .82 * math.sin(math.radians(22.5 + 45 * i))) for i in range(8)],
           ARENA, "#8F7A55", .35)
    # the museum: a long building with a ridged roof (the club's old ice rink)
    x0, y0, x1, y1 = MUSEUM
    s.rect(x0, y0, x1, y1, BLDG, "#7E6A45", .35)
    for x in range(x0 + 18, x1, 22):
        s.line([(x, y0 + 4), (x, y1 - 4)], "#A8987A", .25)
    if lvl:
        return
    for x, y, t, cls, fs, *rot in LABELS_OUT:
        s.text(x, y, t, cls, "middle", fs, rot=(rot[0] if rot else None), top=True)


LABELS_OUT = [  # (x, y, text, class, size[, rotation])
    (250, 22, "Av. de Joan XXIII", "st", 2.3),
    (20, 210, "side avenue (Arístides Maillol)", "sts", 1.5, -90),
    (211, 107, "THE MUSEUM\nthe long building with the ridged roof\n(the club's old ice rink)", "plb", 1.75),
    (462, 190, "Palau Blaugrana\n(the round arena)", "plm", 1.6),
    (612, 168, "lower\nbuildings", "pls", 1.35),
    (900, 250, "THE STADIUM\nnot on this ticket: seen from\noutside and from the viewpoint", "plb", 1.7),
]

# the route outside: 001 on the avenue by the museum -> onto the campus, the stadium in view (002) -> back by the
# museum's door (003-005) -> in. The door's face is still to be confirmed on site: "follow the museum signs".
STOPS_OUT = {"001": (392, 58), "002": (640, 214), "003": (262, 192)}
R_OUT = [(392, 70), (470, 92), (560, 140), (624, 196)]
R_BACK = [(640, 232), (560, 268), (380, 268), (322, 200)]
R_IN = [(176, 200), (176, 156)]


def place_out(s, rad, marks=True):
    groups = {"001": [], "002": [], "003": []}
    for n in NUMS:
        if TR[n]["section"] != "Outside the museum": continue
        place = TR[n]["room"].split("·", 1)[0].strip().lower()
        if TR[n]["type"] == "ANCHOR": groups["001"].append(n)
        elif place == "the campus": groups["002"].append(n)
        else: groups["003"].append(n)
    for g, ns in groups.items():
        if ns: dot_row(s, *STOPS_OUT[g], ns, rad, marks)


def outside_svg(W=184, rad=2.2, marks=True, notes=True):
    s = Svg(VIEW_OUT, W=W)
    outside(s, 0 if notes else 1)
    s.route(R_OUT, "main", minlen=10, scale=W / 184); s.route(R_BACK, "main", minlen=10, scale=W / 184)
    s.route(R_IN, "oneway", mid=False, scale=W / 184)
    place_out(s, rad, marks)
    if notes:
        s.note(176, 156, "IN · follow the museum signs to the door\nand the ticket check; inside: below", "start", 40, 45, 1.9)
        s.note(None, None, "START · on Av. de Joan XXIII, by the museum", "start", 118, 4.4, 1.9)
        s.text(s.W - 2, 4.6, "SCHEMATIC · NOT TO SCALE", "scl", "end", 2.0, page=True, top=True)
    return s.done()


# ---------------------------------------------------------------- inside: the displays in the guide's order (not a floor plan)
VIEW_IN = (0, 0, 1000, 492)
STATIONS = [  # (key, label, place names in @room (lower case, before "·"), row, column)
    ("hall", "The entrance hall", ("the entrance hall",), 0, 0),
    ("wall", "The wall of trophies", ("the wall of trophies",), 0, 1),
    ("cups", "The European Cups", ("the european cups",), 0, 2),
    ("women", "The women's trophies", ("the women's trophies",), 0, 3),
    ("shirts", "The wall of shirts", ("the wall of shirts",), 0, 4),
    ("cruyff", "Cruyff", ("cruyff's display",), 1, 4),
    ("masia", "La Masia", ("the masia display",), 1, 3),
    ("mqc", "Més que un club", ("the més que un club display",), 1, 2),
    ("corner", "A quiet corner", ("a quiet corner",), 1, 1),
    ("messi", "Messi's space", ("messi's space",), 1, 0),
    ("round", "The round room", ("the round room",), 2, 0),
    ("models", "The models", ("the models",), 2, 1),
    ("view", "The viewpoint", ("the viewpoint",), 2, 2),
    ("benches", "The old benches", ("the old benches",), 2, 3),
    ("out", "The way out", ("the way out",), 2, 4),
]
COLX = [104, 302, 500, 698, 896]; ROWY = [92, 250, 408]; BW, BH = 176, 108
SUBS = {"round": "stop the guide for the show\nbetween the two tracks", "corner": "Full tour only: a bench,\naway from the screens",
        "view": "at the rail, the works\nin front of you", "benches": "sitting where the\nplayers sat", "cups": "the five big silver cups",
        "hall": "past the ticket check", "out": "the exit, or just outside"}
ZONES = [("THE TROPHIES · in any order", 0, 1, 4), ("THE CLUB'S HISTORY · in any order", 1, 2, 4)]
ST_TR = {k: [] for k, *_ in STATIONS}
for n in NUMS:
    if TR[n]["section"] == "Outside the museum": continue
    place = TR[n]["room"].split("·", 1)[0].strip().lower()
    for k, lab, places, r, c in STATIONS:
        if place in places: ST_TR[k].append(n); break
    else:
        sys.exit(f"route_map: track {n}'s place '{place}' is not on the inside drawing (STATIONS)")


def box_of(r, c): return (COLX[c] - BW / 2, ROWY[r] - BH / 2, COLX[c] + BW / 2, ROWY[r] + BH / 2)


def inside_svg(W=184, rad=2.05, marks=True, notes=True, hi=None):
    s = Svg(VIEW_IN, W=W); z = W / 184
    s.rect(-20, -20, 1020, 540, "#F3EEE4")
    for name, r, c0, c1 in ZONES:                                                               # zones that are order-free
        a, b = box_of(r, c0), box_of(r, c1)
        s.rect(min(a[0], b[0]) - 10, a[1] - 22, max(a[2], b[2]) + 10, a[3] + 8, "none", GOLD, .3 * z, dash=DASH, rx=1.6 * z)
        if notes: s.text((min(a[0], b[0]) + max(a[2], b[2])) / 2, a[1] - 12, name, "zn", "middle", 1.55, top=True)
    # the way through, as a snake: row 1 left to right, row 2 right to left, row 3 left to right
    path = [(COLX[0] - BW / 2 - 40, ROWY[0]), (COLX[4] + BW / 2 - 30, ROWY[0]), (COLX[4] + BW / 2 - 30, ROWY[1]),
            (COLX[0] - BW / 2 + 30, ROWY[1]), (COLX[0] - BW / 2 + 30, ROWY[2]), (COLX[4] + BW / 2 + 40, ROWY[2])]
    s.route(path, "main", minlen=14, scale=z)
    for k, lab, places, r, c in STATIONS:
        x0, y0, x1, y1 = box_of(r, c); ns = ST_TR[k]
        col = SECS[TR[ns[0]]["section"]][1] if ns else MUTED
        dim = hi is not None and not (set(ns) & hi)
        s.add(f'<g opacity="{.28 if dim else 1}">')
        s.rect(x0, y0, x1, y1, "#FFFFFF", col, .45 * z, rx=2.2 * z)
        s.rect(x0, y0, x1, y0 + 26, col, "none", rx=2.2 * z); s.rect(x0, y0 + 14, x1, y0 + 26, col)
        s.add('</g>')
        s.text((x0 + x1) / 2, y0 + 13, lab, "stt", "middle", 1.75 * z, top=True)
        if notes and k in SUBS: s.text((x0 + x1) / 2, y1 - 13, SUBS[k], "sbt", "middle", 1.2, top=True)
        if ns and not dim: dot_row(s, (x0 + x1) / 2, (y0 + y1) / 2 - 2 if notes else (y0 + y1) / 2 + 6, ns, rad, marks)
    if notes:
        s.note(None, None, "ROOM ORDER MAY CHANGE    ", "warn", 23, 3.0, 1.9)
        s.note(None, None, "END", "finish", s.W - 8, s.T(0, ROWY[2])[1], 1.9)
        s.text(s.W - 2, s.H - 2, "SCHEMATIC · THE DISPLAYS IN THE GUIDE'S ORDER · NOT A FLOOR PLAN", "scl", "end", 1.7, page=True, top=True)
    return s.done()


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
    if not b or n in XS: b.append('<span class="bf">Full only</span>')
    return "".join(b)
def stop_rows(secs):
    out = []
    for sec in secs:
        ns = sec_ns(sec)
        if not ns: continue
        short, c, how = SECS[sec]
        out.append(f'<div class="sech" style="border-color:{c}"><b style="color:{c}">{esc(short)}</b> <span>{rng(sec)}</span><p>{esc(how)}</p></div>')
        for n in ns:
            t = TR[n]; x = ' x' if n in XS else ''
            out.append(f'<div class="row{x}">{dot(n)}<div class="tt"><b>{esc(t["title"])}</b> {badges(n)}'
                       f'<div class="rm" style="color:{c}">{esc(t["room"])}</div><div class="wh">{esc(t["where"])}</div></div></div>')
    return "".join(out)
def sw(svg): return f'<svg width="9mm" height="3mm" viewBox="0 0 9 3">{svg}</svg>'
_ROUTE_SW = sw(f'<path d="M.5,1.5 L8.5,1.5" stroke="{INK}" stroke-opacity=".78" stroke-width=".55" stroke-dasharray="1.5,1"/>')
_IN_SW = sw(f'<path d="M.5,1.5 L8.5,1.5" stroke="{ONEWAY}" stroke-width=".75"/>')
_ZONE_SW = sw(f'<rect x=".6" y=".4" width="7.8" height="2.2" rx=".5" fill="none" stroke="{GOLD}" stroke-width=".3" stroke-dasharray="{DASH}"/>')
N_ANY = next((n for n in NUMS if n not in XS), NUMS[0])
LEGEND = ('<div class="legend">'
          f'<span>{dot(N_ANY, "ldot")} track</span><span><span class="ldot hol" style="color:{INK};border-color:{INK}">X</span> Extra (Full tour only)</span>'
          '<span class="vml"><b>H</b><b>E</b><b>F</b> under a track: the versions it plays in (Highlights, Essential, Full); pale = not in that one</span>'
          f'<span>{_ROUTE_SW} route, in walking order</span><span>{_IN_SW} in through the museum door</span>'
          f'<span>{_ZONE_SW} stops that work in any order</span>'
          '</div>')


# ---------------------------------------------------------------- page 1: the whole route
KEYS = "".join(f'<span><i style="background:{SECS[k][1]}"></i><em>{esc(SECS[k][0])} <b>{rng(k)}</b></em></span>' for k in SECS if rng(k))
def len_card(i, name, ns, when, desc):
    ds_ = "".join(dot(n, "mdot") for n in sorted(ns))
    return (f'<div class="card"><div class="ch"><div class="cnum">{i}</div><div><div class="ct">{esc(name)}</div>'
            f'<div class="cs"><b>{esc(when.replace("about ", "≈ "))}</b> · {len(ns)} tracks</div></div></div>'
            f'<div class="cdots">{ds_}</div><div class="cs2">{esc(desc)}</div></div>')
lens = "".join(len_card(i, n, ns, m, d) for i, (n, ns, m, d) in enumerate(LENGTHS, 1))
pages = []
pages.append(f'''<section class="page">
 <header><div class="brand">YO TOURS · AUDIO GUIDE</div><h1>FC Barcelona Museum · Spotify Camp Nou</h1>
 <p class="lede">The club's museum, in its temporary home in the old ice rink: {len(F_SET) - FX} main stops plus {FX} Extras on one route, from the avenue outside to the viewpoint over the works, in three lengths. <b>This ticket does not include the stadium</b>: you see it from outside and from the viewpoint.</p></header>
 <div class="pt"><b>Outside</b> · start on the avenue, step onto the campus for the stadium, then in at the museum's door</div>
 <div class="ov">{outside_svg()}</div>
 <div class="pt"><b>Inside, by displays</b> · the order of the rooms may change: every track says what to look for</div>
 <div class="ov">{inside_svg()}<div class="keys">{KEYS}</div>{LEGEND}</div>
 <div class="cards">{lens}</div>
 <footer>{esc(FOOTER)}</footer>
</section>''')


# ---------------------------------------------------------------- pages 2-4: where to stand, section by section
def list_page(kicker, title, secs, loc, intro):
    ns = sec_ns(*secs)
    span = f"{ns[0]}–{ns[-1]}" if ns else ""
    return f'''<section class="page">
 <header class="lh"><div class="lhl"><div class="brand">YO TOURS · FC BARCELONA MUSEUM · {esc(kicker)}</div>
 <h2>{esc(title)} · {span}</h2><p class="sub">{intro}</p></div>
 <div class="loc">{loc}<div class="locl">this page, on the route</div></div></header>
 <div class="stops">{stop_rows(secs)}</div>
 <footer>{esc(FOOTER)}</footer>
</section>'''


def hi_set(*secs): return set(sec_ns(*secs))
P2 = ("Outside the museum", "The entrance hall", "The trophies")
P3 = ("The club's history", "More stories inside", "Messi's space", "The round room")
P4 = ("The models", "The viewpoint", "The way out")
pages.append(list_page("WHERE TO STAND · 1", "Outside, the entrance hall and the trophies", P2,
    outside_svg(W=66, rad=1.5, marks=False, notes=False),
    "Outside first: on the avenue by the museum, then onto the campus where the stadium shows, then back by the museum's "
    "door (in the queue, if there is one). Inside, the trophy stops work in any order: find each display by what is on it."))
pages.append(list_page("WHERE TO STAND · 2", "The history, a quiet corner, Messi and the round room", P3,
    inside_svg(W=66, rad=1.35, marks=False, notes=False, hi=hi_set(*P3)),
    "The history stops work in any order. Full tour only: four Extras on a bench or in a quiet corner. Then Messi's space, "
    "and the round room, where the exhibition ends: stop the guide while the show plays."))
pages.append(list_page("WHERE TO STAND · 3", "The models, the viewpoint and the way out", P4,
    inside_svg(W=66, rad=1.35, marks=False, notes=False, hi=hi_set(*P4)),
    "After the show, the models of the finished stadium, then the viewpoint over the works and the original benches from "
    "the old stadium, and the way out."))

# ---------------------------------------------------------------- page 5: visit notes
CLOSED = [("A quiet corner", "017–020", "No bench or rest area? Any quiet corner out of the flow, away from the loud screens."),
          ("A history display", "013–016", "Not where you expect it? Play the track wherever the story is shown; if you can't find it, any quiet spot nearby."),
          ("The round room", "024–025", "Stop the guide during the show; play 025 just outside the room, or inside once the show has ended."),
          ("The models", "026–027", "Elsewhere or gone? Play 026 wherever the route first reaches the stadium."),
          ("The viewpoint", "028", "Crowded at the rail? Step back to any spot with a view of the stands."),
          ("The old benches", "029–033", "Full? Stand beside them, out of the way; the Extras can be heard anywhere quiet nearby."),
          ("The way out", "034", "If the way out is back past the viewpoint, play it there before you leave.")]
offrows = "".join(f'<tr><td><b>{esc(a)}</b></td><td class="tn">{esc(b)}</td><td>{esc(c)}</td></tr>' for a, b, c in CLOSED)
NOTES = [
    ("Not the stadium", "This guide is for the museum ticket. It does not take you into the stadium: no pitch, no stands, no dressing room. You see the stadium from outside and from the viewpoint over the works."),
    ("Headphones", "Listen on headphones, at a volume low enough to hear what is around you and the staff."),
    ("The show", "In the round room, stop the guide while the show plays. The club does not recommend the show for people with epilepsy or photosensitivity, and asks them to tell the staff before going in."),
    ("Room order may change", "The museum may move its displays. Every track names what to look for, and the trophy and history stops work in any order. Where the ground differs, follow the museum's signs and staff."),
    ("Offline", "Once the MP3s are on your phone, the guide needs no signal and no data."),
    ("Out of the way", "Stand to one side of doors, the ticket check, the displays and the rail; let other visitors pass."),
    ("The works", "The stadium is still being finished. Stay behind every barrier and never step onto the works."),
    ("Shorter versions", "In Essential and Highlights the numbers jump. A short spoken line at the end of a track tells you where the next one is."),
]
notes = "".join(f'<div class="nbox"><h3>{esc(h)}</h3><p>{esc(p)}</p></div>' for h, p in NOTES)
pages.append(f'''<section class="page">
 <header class="fh"><div class="brand">YO TOURS · FC BARCELONA MUSEUM · ON SITE</div>
 <h2>Before you start</h2><p class="sub">A few things to know on the ground. No prices, hours or tickets here: check them with the club before your visit.</p></header>
 <div class="notes">{notes}</div>
 <h3 class="oh">If a display or a space is not where the guide expects it</h3>
 <p class="sub">The museum is a temporary one, and its rooms can change. Each track already says where else it can be heard.</p>
 <table class="off">{offrows}</table>
 <p class="tfoot">These drawings are our own schematics, not to scale and not the club's maps, made from the guide's own directions. Where the ground differs, follow the museum's signs and staff.</p>
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
.off td {{ padding: 1.3mm 2mm; border-bottom: .2mm solid {LINE}; font: 400 8pt Inter; vertical-align: middle }} .off td:first-child {{ width: 34mm }} .off td.tn {{ width: 20mm; color: {MUTED}; font-weight: 600; white-space: nowrap }}
.tfoot {{ font: 400 7.6pt Inter; color: {MUTED}; margin: 3mm 0 0; line-height: 1.36 }}
.pt {{ font: 500 8pt Inter; color: {MUTED}; margin: 0 0 1mm }} .pt b {{ color: {INK}; font: 700 9.4pt Lora, serif }}
.lede b {{ color: {RED} }}
.zn {{ font-family: Inter; font-weight: 700; fill: {GOLD}; letter-spacing: .2px; paint-order: stroke; stroke: #F3EEE4; stroke-width: .7px }}
.stt {{ font-family: Inter; font-weight: 700; fill: #fff }}
.sbt {{ font-family: Inter; font-weight: 500; fill: #5F574C }}
.vm {{ font-family: Inter; text-anchor: middle }}
.vml b {{ font: 800 6.4pt Inter; color: {INK}; margin-right: .5mm }}
.bf {{ display: inline-block; font: 700 5.4pt Inter; letter-spacing: .03em; border-radius: 1mm; padding: 0 .8mm; margin-left: .6mm; vertical-align: .2mm; background: #EEE8DC; color: #6F665A }}
'''


def build():
    doc = f'<!doctype html><html><head><meta charset="utf-8"><title>FC Barcelona Museum · Spotify Camp Nou · Yo Tours route</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
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
