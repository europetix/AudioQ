#!/usr/bin/env python3
"""Yo Tours · Barcelona Cathedral — route map, 14 Nov 2026 edition.
A PDF made to be read on a phone: page 1 = the whole route and the three lengths; page 2 = the square, inside the main
door, the left aisle and the roof; page 3 = the choir, the crypt and behind the high altar; page 4 = the cloister, the
Chapter Hall and the way out (pages 2-4: where to stand for every track); page 5 = visit notes (headphones, worship
and Mass, the lift wait, offline) and what to do if a space is closed.
Our OWN schematic plan of the cathedral, not traced and not a copy of any official plan: simple shapes, drawn with the
square and the main door on the left and the high altar on the right, so "left as you face the high altar" is the top
of the drawing and "right" the bottom: the Pla de la Seu and the front, the main door with the lantern tower over it,
the nave with the choir in the middle and the crypt stair before the high altar, the ambulatory behind it, the Sant Iu
door and the lift chapel on the left, the Lepanto chapel by the main door on the right, the white marble cloister door
on the right near the altar, the cloister (fountain, geese's pond, Pietat door, Santa Llúcia, Chapter Hall) and the
Santa Eulàlia door out to Carrer del Bisbe. Not to scale; no compass, no distances, no prices or hours, no logo or
photos. Writers' markers ([O5], ALT-K, notes for the on-site check, PLACEMENT PENDING) are never printed.
Stops come from v5/tracks/NNN.perf.txt (@title, @room, @where, @type, @section) at run time; lengths from
build/static/lengths.json.
Usage (from the guide folder): python3 build/route_map.py <bundle folder> [--png <dir>]
  -> <bundle>/BarcelonaCathedral_Audio_Guide_Route.pdf"""
import json, math, os, re, sys, html, asyncio, glob

B = sys.argv[1]
PNG_DIR = sys.argv[sys.argv.index("--png") + 1] if "--png" in sys.argv else None
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
TRACKS = os.path.join(ROOT, "v5", "tracks")
LENGTHS_JSON = os.path.join(HERE, "static", "lengths.json")
OUT_PDF = os.path.join(B, "BarcelonaCathedral_Audio_Guide_Route.pdf")
FOOTER = "Yo Tours · Barcelona Cathedral audio guide · 14 Nov 2026 edition · schematic plan, not to scale"
if not os.environ.get("PLAYWRIGHT_BROWSERS_PATH") and os.path.isdir("/opt/pw-browsers"):
    os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "/opt/pw-browsers"


# ---------------------------------------------------------------- stops, from the track files
def tidy(s):
    """Writers' markers are never printed: [O5], [O-map, O2], ALT-K, (G102: ...), PLACEMENT PENDING notes, and sentences
    that are notes for the on-site check."""
    s = re.sub(r"\s*\[[^\]]*\]", "", s)
    s = re.sub(r"\s*\([^)]*\b(?:G\d+|ALT-[A-Z0-9]+|O\d+)\b[^)]*\)", "", s)
    s = re.sub(r";?\s*PLACEMENT PENDING[^.;]*", "", s)
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
LENGTHS = [("Full tour", F_SET, "about 1 h 35", f"every stop and all {FX} Extras: the square, the roof, the choir, the crypt, the ambulatory, the cloister and the Chapter Hall"),
           ("Essential", E_SET, "about 1 h", "the square and the front, the Lepanto chapel, the choir screen and the baptistery, the roof, the shields, the crypt, the cloister, the Pietà"),
           ("Highlights", H_SET, "about 30 min", "the front, the lantern tower, the Golden Fleece shields, Santa Eulàlia's tomb, the dancing egg, the geese, the Pietà")]

# ---------------------------------------------------------------- palette, sections
PAPER, INK, MUTED, LINE = "#F6F1E7", "#1F1B17", "#776E62", "#D8CEBD"
RED, GOLD, NAVY = "#C0262D", "#A9812F", "#1D2B4A"
ONEWAY = RED
ROOFC = "#6B4E9B"
SECS = {  # @section -> (short title, dot colour, how to get there)
    "The square and the facade": ("The square and the front", "#1D2B4A",
        "On the Pla de la Seu, before you go in: beside the steps, at the end with the two Roman towers, facing the Casa de l'Ardiaca, then far enough back to see the whole front."),
    "Inside the main door": ("Inside the main door", "#B03A2E",
        "Just inside the main door, under the lantern tower: the Lepanto chapel on the right, the choir's white marble screen ahead, the baptistery on the left."),
    "Up the left aisle": ("Up the left aisle", "#8A5A2B",
        "Up the left aisle to the Sant Iu door, under the organ, beside the lift chapel."),
    "The roof": ("The roof", ROOFC,
        "Up by the small lift from the chapel of the Holy Innocents, beside the Sant Iu door (there may be a queue), onto the roof terraces, and back down."),
    "The choir": ("The choir", "#2C6E8F",
        "The wooden enclosure in the middle of the nave. Closed? Listen at its entrance, looking in."),
    "The crypt": ("The crypt", "#A87A0C",
        "The stair down in front of the high altar to Santa Eulàlia's tomb. Closed? Stay at the top of the stair: the tomb is in view below."),
    "Behind the high altar": ("Behind the high altar", "#3E7D3A",
        "Round the ambulatory, the walkway behind the altar, to the sacristy door and the white marble cloister door, both on the right."),
    "The cloister": ("The cloister", "#C05A3C",
        "Through the white marble door: the fountain, the geese's pond, the Pietat door, the chapel of Santa Llúcia."),
    "The Chapter Hall": ("The Chapter Hall", "#8C3B6E",
        "The museum beside the chapel of Santa Llúcia: Bermejo's Pietà and the great monstrance."),
    "The way out": ("The way out", "#4A5560",
        "The cloister's Santa Eulàlia door, out to Carrer del Bisbe."),
}
def colour(n): return SECS.get(TR[n]["section"], ("", INK))[1]
def esc(s): return html.escape(s, quote=True)
def sec_ns(*secs): return [n for n in NUMS if TR[n]["section"] in secs]
def rng(sec):
    ns = sec_ns(sec)
    return (f"{ns[0]}–{ns[-1]}" if len(ns) > 1 else f"{ns[0]}") if ns else ""

DASH = "1.2,.8"
SQUAREC, STREET, STONE, FLOOR, AISLE = "#EFE7D7", "#E2DCCF", "#CDBB97", "#F7F2E8", "#EEE6D6"
WALLC, GARTHC, WATER, CHAPEL, WOOD = "#8F7A55", "#DCE6CC", "#9CC3DD", "#E6DCC8", "#C9A97A"


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



# ---------------------------------------------------------------- the cathedral, schematic (one geometry, every view)
# World grid (no scale): the Pla de la Seu and the main door on the left, the high altar and the apse on the right;
# "left as you face the high altar" is the top of the drawing, "right" the bottom, where the cloister and Carrer del
# Bisbe are. Every position is a schematic choice of ours, not a measured one.
VIEW = (0, 0, 1150, 660)
SQUARE = (20, 40, 200, 408)
TOWERS = ((40, 420), (90, 420))
ARDIACA = (100, 428, 198, 600)
CHURCH = (222, 80, 780, 380)                   # chapels ring outside the aisles
AISLES = (222, 118, 780, 342)
NAVE = (222, 172, 780, 288)
APSE_C = (780, 230)
MAIN_DOOR = (222, 230)
LANTERN = (262, 230)
BAPTISTERY = (222, 80, 280, 118)
LEPANTO = (222, 342, 300, 395)
LIFT = (610, 80, 665, 118)
SANT_IU = (692, 80)
CHOIR = (380, 186, 580, 274)
CRYPT_STAIR = ((615, 230), (668, 230))
ALTAR = (690, 212, 720, 248)
SACRISTY = (782, 382, 846, 420)
CLOISTER_DOOR = (700, 380)
CLOISTER = (290, 392, 790, 602)
GARTH = (325, 425, 755, 568)
FOUNTAIN = (742, 438)
POND = (540, 497)
PIETAT = (790, 575)
CHAPTER = (222, 405, 290, 535)
LLUCIA = (222, 542, 290, 605)
EULALIA_DOOR = (520, 602)
ROOF = (330, 8, 560, 60)


def arc(c, r, a0, a1, n=24):
    return [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * k / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * k / n))) for k in range(n + 1)]


def door(s, x, y, vertical):
    w, h = (6, 18) if vertical else (18, 6)
    s.rect(x - w, y - h, x + w, y + h, "#FDFBF7", INK, .3)


def plan(s, lvl):
    """Streets, square, church, apse, choir, crypt stair, cloister, chapels and doors; lvl 0 = overview, 1 = locator."""
    k = s.k
    s.rect(s.x0 - 50, s.y0 - 50, VIEW[2] + 50, VIEW[3] + 50, "#ECE6DA")
    s.line([(65, 420), (65, 626), (900, 626)], STREET, max(.8, 30 * k))                    # Carrer del Bisbe
    s.line([(211, 408), (211, 612)], STREET, max(.6, 20 * k))                               # Carrer de Santa Llúcia
    s.rect(*SQUARE, SQUAREC, "#CBBFA8", .3)
    for x, y in TOWERS:
        s.circle(x, y, max(.8, 17 * k), STONE, WALLC, .3)
    s.rect(*ARDIACA, "#E9D6B4", "#7E6A45", .3)
    # the church: chapels ring, aisles, nave; the apse with its chapels, the ambulatory and the sanctuary
    x0, y0, x1, y1 = CHURCH
    s.poly([(x0, y0), (x1, y0)] + arc(APSE_C, 150, -90, 90) + [(x1, y1), (x0, y1)], CHAPEL, WALLC, .35)
    s.poly([(AISLES[0], AISLES[1]), (AISLES[2], AISLES[1])] + arc(APSE_C, 112, -90, 90) + [(AISLES[2], AISLES[3]), (AISLES[0], AISLES[3])], "#EEE6D6", "#B9A88A", .25)
    s.poly([(NAVE[0], NAVE[1]), (NAVE[2], NAVE[1])] + arc(APSE_C, 62, -90, 90) + [(NAVE[2], NAVE[3]), (NAVE[0], NAVE[3])], FLOOR, "none", .2)
    for x in range(280, 780, 58):                                                            # side chapels
        s.line([(x, y0), (x, AISLES[1])], WALLC, .22); s.line([(x, AISLES[3]), (x, y1)], WALLC, .22)
    for a in (-60, -30, 0, 30, 60):                                                          # apse chapels
        p, q = arc(APSE_C, 112, a, a, 1)[0], arc(APSE_C, 150, a, a, 1)[0]
        s.line([p, q], WALLC, .22)
    if lvl == 0:
        for x in range(296, 760, 56):
            s.circle(x, NAVE[1], max(.25, 5 * k), "#9C8A68"); s.circle(x, NAVE[3], max(.25, 5 * k), "#9C8A68")
    s.rect(*BAPTISTERY, "#D6E3EE", WALLC, .3)
    s.rect(*LEPANTO, "#EBD3C6", WALLC, .3)
    s.rect(*LIFT, "#DCD3EA", ROOFC, .3)
    # the lantern tower over the main door (dashed: it is overhead)
    s.poly([(LANTERN[0] + 30 * math.cos(math.radians(22.5 + 45 * i)), LANTERN[1] + 30 * math.sin(math.radians(22.5 + 45 * i))) for i in range(8)],
           "none", "#7E6A45", .3, dash=DASH)
    s.stairs((178, 230), MAIN_DOOR, 70, 5)
    # the choir: a wooden enclosure, the white marble screen at its end facing the main door, open at the altar end
    cx0, cy0, cx1, cy1 = CHOIR
    s.rect(cx0, cy0, cx1, cy1, "#E7D3B0")
    s.line([(cx1, 218), (cx1, cy0), (cx0, cy0)], "#7E6A45", max(.5, 6 * k)); s.line([(cx0, cy1), (cx1, cy1), (cx1, 242)], "#7E6A45", max(.5, 6 * k))
    s.line([(cx0, cy0), (cx0, cy1)], "#FDFBF7", max(.9, 11 * k)); s.line([(cx0, cy0), (cx0, cy1)], "#A39886", .25)
    s.stairs(*CRYPT_STAIR, 50, 6)
    s.rect(*ALTAR, "#D9B65E", "#8A6A22", .3)
    s.rect(*SACRISTY, CHAPEL, WALLC, .3)
    # the cloister: four walks round a garden with the geese's pond; the fountain pavilion in the corner by the church door
    s.rect(*CLOISTER, "#EFE7D7", WALLC, .35)
    s.rect(*GARTH, GARTHC, "#9DB78A", .3)
    s.add(f'<ellipse cx="{s.T(*POND)[0]:.2f}" cy="{s.T(*POND)[1]:.2f}" rx="{80 * k:.2f}" ry="{34 * k:.2f}" fill="{WATER}" stroke="#6C9BBB" stroke-width=".25"/>')
    if lvl == 0:
        for gx, gy in ((500, 488), (585, 506), (560, 480)):                                   # three small geese
            s.circle(gx, gy, max(.3, 4.5 * k), "#FDFBF7", "#8F8473", .15)
        for tx, ty in ((380, 460), (700, 530), (390, 540), (680, 455)):
            s.circle(tx, ty, max(.6, 10 * k), "#9DBB85")
    s.rect(FOUNTAIN[0] - 13, FOUNTAIN[1] - 13, FOUNTAIN[0] + 13, FOUNTAIN[1] + 13, "#D6E3EE", "#6C9BBB", .3)
    s.rect(*CHAPTER, "#E6D2DE", WALLC, .3)
    s.rect(*LLUCIA, "#E3D9C3", WALLC, .3)
    # the roof, reached by the lift: an inset above the church
    rx0, ry0, rx1, ry1 = ROOF
    s.rect(rx0, ry0, rx1, ry1, "#EFEAF5", ROOFC, .3, dash=DASH, rx=1.2)
    # doors
    for (x, y), v in ((MAIN_DOOR, True), (SANT_IU, False), (CLOISTER_DOOR, False), (EULALIA_DOOR, False), (PIETAT, True), ((782, 400), True)):
        door(s, x, y, v)
    if lvl:
        return
    for lab in LABELS:
        x, y, t, cls, fs = lab[:5]
        s.text(x, y, t, cls, "middle", fs, rot=(lab[5] if len(lab) > 5 else None), top=True)


LABELS = [  # (x, y, text, class, size[, rotation])
    (110, 66, "Pla de la Seu", "plb", 2.3),
    (65, 452, "Roman\ntowers", "pls", 1.6),
    (150, 512, "Casa de\nl'Ardiaca", "plm", 1.7),
    (211, 512, "Carrer de Santa Llúcia", "sts", 1.35, -90),
    (198, 186, "steps", "pls", 1.5),
    (310, 192, "lantern tower overhead", "pls", 1.45),
    (251, 66, "baptistery", "pls", 1.6),
    (261, 368, "Lepanto\nchapel", "plm", 1.6),
    (480, 204, "choir", "plb", 2.0),
    (640, 302, "crypt stair", "pls", 1.5),
    (705, 196, "high altar", "plm", 1.6),
    (1005, 230, "ambulatory\n(behind the altar)", "plm", 1.8),
    (700, 62, "Sant Iu door", "pls", 1.6),
    (637, 99, "lift", "pls", 1.5),
    (445, 20, "THE ROOF · by lift, up and back", "plw", 1.6),
    (815, 430, "sacristy", "pls", 1.5),
    (640, 361, "cloister door", "pls", 1.45),
    (440, 452, "cloister", "plb", 2.2),
    (540, 497, "geese's pond", "pls", 1.7),
    (712, 466, "fountain", "pls", 1.5),
    (838, 575, "Pietat door", "pls", 1.6),
    (256, 572, "Santa\nLlúcia", "plm", 1.5),
    (256, 512, "Chapter\nHall", "plm", 1.6),
    (330, 638, "Carrer del Bisbe", "st", 2.0),
    (520, 636, "Santa Eulàlia door", "pls", 1.5),
    (1010, 100, "LEFT as you face the altar", "sts", 1.6),
    (1010, 362, "RIGHT as you face the altar", "sts", 1.6),
]

# ---------------------------------------------------------------- the route (walking order), shared by every view
R_SQUARE = [(160, 308), (108, 350), (150, 352), (138, 300), (128, 250), (160, 232), (226, 230)]
R_INSIDE = [(226, 230), (268, 296), (290, 330), (332, 268), (352, 236), (300, 176), (262, 150), (420, 148), (606, 152), (690, 148)]
R_ROOF = [(632, 118), (612, 70), (566, 46)]
R_CHOIR = [(632, 160), (600, 180), (588, 230), (560, 232)]
R_CRYPT = [(590, 244), (604, 270), (622, 252)]
R_AMB = [(650, 210), (690, 168), (735, 150)] + arc(APSE_C, 87, -118, 88, 20)[2:] + [(760, 322), (712, 334), (700, 378)]
R_CLOISTER = [(700, 382), (700, 410), (772, 410), (772, 578), (306, 578), (306, 470), (292, 470)]
R_OUT = [(294, 520), (294, 594), (520, 594), (520, 640)]


def draw_route(s, scale=1.0):
    s.route(R_SQUARE, "main", minlen=14, end=False, scale=scale)
    s.route(R_INSIDE, "main", minlen=14, scale=scale)
    z = scale; P = R_ROOF
    s.add(f'<path d="{s.d(P)}" fill="none" stroke="{ROOFC}" stroke-opacity=".9" stroke-width="{.7 * z:.2f}" stroke-dasharray="{.1 * z:.2f},{1.1 * z:.2f}" stroke-linecap="round"/>')
    s.route(R_CHOIR, "main", minlen=14, scale=scale)
    s.route(R_CRYPT, "main", mid=False, scale=scale)
    s.route(R_AMB, "main", minlen=16, scale=scale)
    s.route(R_CLOISTER, "main", minlen=16, scale=scale)
    s.route(R_OUT, "main", minlen=16, scale=scale)


# where every track's dot goes: the first rule whose test matches the track's @section / @room (lower case) wins;
# tracks with the same group share a row of dots. Renumbering keeps working; a track no rule matches is placed at its
# section's default and reported.
def _r(n): return TR[n]["room"].lower()
def _s(n): return TR[n]["section"]
def _place(n): return _r(n).split("·", 1)[0]
GROUPS = [  # (name, test, overview position, direction)
    ("sq_steps", lambda n: _s(n) == "The square and the facade" and (TR[n]["type"] == "ANCHOR" or "steps" in _r(n)), (165, 290), "r"),
    ("towers", lambda n: "roman towers" in _r(n), (95, 370), "r"),
    ("ardiaca", lambda n: "ardiaca" in _r(n), (160, 370), "r"),
    ("facade", lambda n: _s(n) == "The square and the facade", (108, 196), "d"),
    ("door_in", lambda n: "inside the main door" in _place(n), (250, 266), "r"),
    ("lepanto", lambda n: "lepanto" in _place(n), (292, 318), "r"),
    ("screen", lambda n: "choir screen" in _place(n), (348, 212), "r"),
    ("baptistery", lambda n: "baptistery" in _place(n), (251, 145), "r"),
    ("sant_iu", lambda n: "sant iu" in _place(n), (705, 146), "r"),
    ("lift", lambda n: _s(n) == "The roof" and "lift" in _place(n), (580, 146), "r"),
    ("roof", lambda n: _s(n) == "The roof", (418, 42), "r"),
    ("choir_entr", lambda n: _s(n) == "The choir" and "pulpit" in _r(n), (600, 202), "r"),
    ("choir", lambda n: _s(n) == "The choir", (412, 238), "r"),
    ("crypt_top", lambda n: _s(n) == "The crypt" and "at the top of the stair" in _r(n), (602, 262), "r"),
    ("crypt", lambda n: _s(n) == "The crypt", (662, 270), "r"),
    ("amb_pen", lambda n: "penyafort" in _r(n), (864, 262), "r"),
    ("amb", lambda n: "ambulatory" in _r(n), (823, 156), "r"),
    ("sacristy", lambda n: "sacristy" in _place(n), (762, 318), "r"),
    ("cl_door", lambda n: "cloister door" in _place(n), (705, 318), "r"),
    ("cl_through", lambda n: _s(n) == "The cloister" and "just through" in _r(n), (700, 408), "r"),
    ("fountain", lambda n: _s(n) == "The cloister" and "fountain" in _r(n), (772, 452), "r"),
    ("pond", lambda n: _s(n) == "The cloister" and "pond" in _r(n), (772, 506), "r"),
    ("pietat", lambda n: _s(n) == "The cloister" and "pietat" in _r(n), (772, 560), "r"),
    ("llucia", lambda n: "santa llúcia" in _r(n), (310, 590), "r"),
    ("jewish", lambda n: "jewish" in _r(n), (310, 412), "r"),
    ("chapter", lambda n: _s(n) == "The Chapter Hall", (256, 440), "d"),
    ("out", lambda n: _s(n) == "The way out", (520, 580), "r"),
]
DEFAULT = {"The square and the facade": (110, 230), "Inside the main door": (250, 266), "Up the left aisle": (705, 146),
           "The roof": (418, 42), "The choir": (412, 238), "The crypt": (662, 270), "Behind the high altar": (823, 156),
           "The cloister": (540, 410), "The Chapter Hall": (256, 440), "The way out": (520, 580)}
PLACED, UNPLACED = {}, []
for n in NUMS:
    for name, test, pos, dr in GROUPS:
        if test(n):
            PLACED.setdefault(name, (pos, dr, []))[2].append(n); break
    else:
        UNPLACED.append(n); PLACED.setdefault("sec:" + _s(n), (DEFAULT.get(_s(n), (500, 230)), "r", []))[2].append(n)
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
        short, c, how = SECS[sec]
        out.append(f'<div class="sech" style="border-color:{c}"><b style="color:{c}">{esc(short)}</b> <span>{rng(sec)}</span><p>{esc(how)}</p></div>')
        for n in ns:
            t = TR[n]; x = ' x' if n in XS else ''
            out.append(f'<div class="row{x}">{dot(n)}<div class="tt"><b>{esc(t["title"])}</b> {badges(n)}'
                       f'<div class="rm" style="color:{c}">{esc(t["room"])}</div><div class="wh">{esc(t["where"])}</div></div></div>')
    return "".join(out)
def sw(svg): return f'<svg width="9mm" height="3mm" viewBox="0 0 9 3">{svg}</svg>'
_ROUTE_SW = sw(f'<path d="M.5,1.5 L8.5,1.5" stroke="{INK}" stroke-opacity=".78" stroke-width=".55" stroke-dasharray="1.5,1"/>')
_ROOF_SW = sw(f'<path d="M.5,1.5 L8.5,1.5" stroke="{ROOFC}" stroke-width=".7" stroke-dasharray=".1,1.1" stroke-linecap="round"/>')
_DOOR_SW = sw(f'<rect x="3" y=".6" width="3" height="1.8" fill="#FDFBF7" stroke="{INK}" stroke-width=".3"/>')
N_ANY = next((n for n in NUMS if n not in XS), NUMS[0])
LEGEND = ('<div class="legend">'
          f'<span>{dot(N_ANY, "ldot")} track</span><span><span class="ldot hol" style="color:{INK};border-color:{INK}">X</span> Extra</span>'
          f'<span>{_ROUTE_SW} route, in walking order</span><span>{_ROOF_SW} up to the roof by lift, and back down</span>'
          f'<span>{_DOOR_SW} door</span><span>left / right: as you face the high altar</span>'
          '</div>')


# ---------------------------------------------------------------- page 1: the whole route
def whole_svg():
    s = Svg(VIEW)
    plan(s, 0); draw_route(s); place_dots(s, 2.05)
    s.note(None, None, "START · the Pla de la Seu", "start", 18, 4.2, 2.1)
    s.note(520, 640, "END · out to Carrer del Bisbe", "finish", 110, s.H - 3.6, 2.1)
    s.text(s.W - 2, 4, "SCHEMATIC · NOT TO SCALE", "scl", "end", 2.2, page=True, top=True)
    return s.done()


def locator(box):
    """The whole plan, small, with the part a page covers framed and the rest dimmed."""
    s = Svg(VIEW, W=64)
    plan(s, 1); draw_route(s, .45)
    x0, y0, x1, y1 = box
    (a, b), (c, e) = s.T(x0, y0), s.T(x1, y1)
    s.add(f'<path d="M0,0 H{s.W} V{s.H} H0 Z M{a:.2f},{b:.2f} V{e:.2f} H{c:.2f} V{b:.2f} Z" fill="#FDFBF7" fill-opacity=".62" fill-rule="evenodd"/>', True)
    s.add(f'<rect x="{a:.2f}" y="{b:.2f}" width="{c - a:.2f}" height="{e - b:.2f}" rx="1" fill="none" stroke="{GOLD}" stroke-width=".5"/>', True)
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
 <header><div class="brand">YO TOURS · AUDIO GUIDE</div><h1>Barcelona Cathedral</h1>
 <p class="lede">The cathedral of the Holy Cross and Saint Eulàlia, la Seu (not the Sagrada Família): {len(F_SET) - FX} main stops plus {FX} short Extras on one route, from the square to the cloister door, in three lengths.</p></header>
 <div class="how"><div><b>1</b> <strong>One route, directions at every step.</strong> The square and the front first, then in at the main door, up to the roof by lift, the choir, the crypt, behind the high altar, the cloister and the Chapter Hall, and out at the Santa Eulàlia door.</div>
 <div><b>2</b> Each circle is the track to play there; hollow ones are short Extras. Every track ends by telling you where to go next. Pages 2–4 say where to stand for every track.</div>
 <div><b>3</b> <strong>A working church.</strong> Headphones, voice low. If Mass is on, the Lepanto chapel is heard from its doorway, and the choir and the crypt from their entrance or the top of the stair.</div></div>
 <div class="ov">{whole_svg()}<div class="keys">{KEYS}</div>{LEGEND}</div>
 <div class="cards">{lens}</div>
 <div class="warn"><b>The roof lift is small:</b> expect a wait; the times above include walking but not the wait. Left and right are always as you face the high altar. Shorter versions: the numbers jump, and a spoken line tells you the next stop.</div>
 <footer>{esc(FOOTER)}</footer>
</section>''')


# ---------------------------------------------------------------- pages 2-4: where to stand, section by section
def list_page(kicker, title, secs, box, intro):
    ns = sec_ns(*secs)
    span = f"{ns[0]}–{ns[-1]}" if ns else ""
    return f'''<section class="page">
 <header class="lh"><div class="lhl"><div class="brand">YO TOURS · CATHEDRAL · {esc(kicker)}</div>
 <h2>{esc(title)} · {span}</h2><p class="sub">{intro}</p></div>
 <div class="loc">{locator(box)}<div class="locl">this page, on the whole plan</div></div></header>
 <div class="stops">{stop_rows(secs)}</div>
 <footer>{esc(FOOTER)}</footer>
</section>'''


pages.append(list_page("WHERE TO STAND · 1", "The square, the main door, the left aisle and the roof",
    ("The square and the facade", "Inside the main door", "Up the left aisle", "The roof"), (0, 0, 730, 410),
    "The square first, before you go in. Inside, left and right are as you face the high altar. The roof is reached by a "
    "small lift beside the Sant Iu door: there may be a queue, and the two lift tracks can be heard in it."))
pages.append(list_page("WHERE TO STAND · 2", "The choir, the crypt and behind the high altar",
    ("The choir", "The crypt", "Behind the high altar"), (360, 90, 960, 395),
    "Back down from the roof to the choir in the middle of the nave, then the crypt stair in front of the high altar, round "
    "the ambulatory, and to the white marble door into the cloister. If the choir or the crypt is closed, each track says where to listen."))
pages.append(list_page("WHERE TO STAND · 3", "The cloister, the Chapter Hall and the way out",
    ("The cloister", "The Chapter Hall", "The way out"), (210, 365, 900, 660),
    "Through the white marble door into the cloister: the fountain, the geese, the Pietat door, the chapel of Santa Llúcia "
    "and the Chapter Hall museum beside it, then out at the Santa Eulàlia door to Carrer del Bisbe."))

# ---------------------------------------------------------------- page 5: visit notes
CLOSED = [("The Lepanto chapel", "007–008", "Listen at its doorway, outside and to one side. Never go in during a service."),
          ("The lift", "012–013", "No queue? Play both tracks at the top, to one side of the lift."),
          ("The choir", "016–020", "Closed? Listen at its entrance, looking in."),
          ("The crypt", "021–023", "Closed? Stay at the top of its stair: the tomb is in view below."),
          ("The chapels", "010, 032", "Stay at the doorway if worshippers are there or visitors are not clearly allowed in."),
          ("Jewish memory", "033, Extra", "An Extra, only if the room is open and signposted; where it is reached from is still to be confirmed.")]
offrows = "".join(f'<tr><td><b>{esc(a)}</b></td><td class="tn">{esc(b)}</td><td>{esc(c)}</td></tr>' for a, b, c in CLOSED)
NOTES = [
    ("Headphones", "Listen on headphones, at a volume low enough to hear what is around you. This is a church: no speakers."),
    ("Worship and Mass", "Barcelona Cathedral is a working church. Hat off and voice low. Never go into a chapel during a service, and take no photos then. Where a service can close a space, the guide says where to listen instead (see below)."),
    ("The lift wait", "The roof is reached by a small lift from the chapel of the Holy Innocents, beside the Sant Iu door, so there may be a queue. The two lift tracks are made to be heard while you wait. The times on page 1 allow for a short wait; a long queue adds more."),
    ("Offline", "Once the MP3s are on your phone, the guide needs no signal and no data."),
    ("Left and right", "Inside, left and right are always as you face the high altar. On the square, each track tells you which way to face."),
    ("Out of the way", "Stand to one side of doors, steps, the lift and the crypt stair; let worshippers and other visitors pass, and let the geese be."),
    ("Steps", "Steps up to the main door and down into the crypt; walkways and steps on the roof. Watch your step."),
    ("Shorter versions", "In Essential and Highlights the numbers jump. A short spoken line at the end of a track tells you where the next one is."),
]
notes = "".join(f'<div class="nbox"><h3>{esc(h)}</h3><p>{esc(p)}</p></div>' for h, p in NOTES)
pages.append(f'''<section class="page">
 <header class="fh"><div class="brand">YO TOURS · BARCELONA CATHEDRAL · ON SITE</div>
 <h2>Before you start</h2><p class="sub">A few things to know on the ground. No prices, hours or tickets here: check them with the cathedral before your visit.</p></header>
 <div class="notes">{notes}</div>
 <h3 class="oh">If a space is closed, or a service is on</h3>
 <p class="sub">The route never asks you to go into a space during a service. Where a space may be closed, the track tells you where to listen instead.</p>
 <table class="off">{offrows}</table>
 <p class="tfoot">This plan is our own schematic drawing, not to scale, made from the guide's own directions. Where the ground differs, follow the cathedral's signs and staff.</p>
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
'''



def build():
    doc = f'<!doctype html><html><head><meta charset="utf-8"><title>Barcelona Cathedral · Yo Tours route</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
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
