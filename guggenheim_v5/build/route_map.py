#!/usr/bin/env python3
"""Yo Tours · Guggenheim Museum Bilbao — route map, 31 Oct 2026 edition (the building and the permanent works).
A PDF made to be read on a phone: page 1 = the whole site from above (the Museum plaza with Puppy and the Txema Agirre
plaque, the broad stairway, the Hall, the Atrium, gallery 104 running under La Salve Bridge toward the tower, the terrace
and the pond on the river side, Maman by the footbridge, the river walk), the route and the three lengths; page 2 =
floor 1 inside (the Hall, ZERO, the Atrium, gallery 101, gallery 104 with the eight Serra sculptures as a SEQUENCE
only, the terrace); page 3 = floors 2 and 3 as a section (the balcony opposite gallery 204 over 104, the glass lifts
and walkways, the balcony opposite gallery 304 over the Atrium, the way down); page 4 = the river walk (the pond with
Kapoor, the fog and the fire, Maman, the titanium, La Salve Bridge with the tower and Buren's red arches); page 5 =
the stop table. Track numbers in the drawings and texts are derived from the track files (@room, @section), so a
renumbering only needs the track files.
Our OWN schematic, not traced from the museum's interactive map, using only placements the research documents
(v5/PLAN.md "The route"; research/VISIT_ROUTE_AND_SPACES_OCT2026.md §1, §3; research/map/OFFICIAL_MAP_NOTES_30OCT2026.md):
the plaza in line with Calle Iparragirre and at floor-2 level, the broad stairway down to the Hall; ZERO in the lobby;
the Atrium leading to every gallery and to the terrace; 101 seen from the Atrium; 104 the long gallery from the Atrium
under the bridge, an educational space with a video at its far end, apparently a dead end; the terrace off the Atrium
on the river side with the two Chillidas and the pond below; Kapoor, the fog and the fire in the pond by the river-side
galleries; Maman next to the footbridge, between the pond and the bridge; La Salve crossing over 104, the tower at the
building's end; Buren's arches on the bridge. No compass: the orientation (city side below, river above) is schematic.
Where PLAN marks a position as provisional (ONSITE items O1–O25, ALT cues) it is drawn with a dashed outline or a
dotted line and the legend says so. Only two timings are given, as spoken: the fog "on the hour", the fire "in the
evening". No prices, no hours, no logo, no photos. Gallery numbers: only 101, 104, 204, 304.
Stops come from v5/tracks/NNN.perf.txt (@room, @title, @type, @section, @where); lengths from build/static/lengths.json.
Usage (from the guide folder): python3 build/route_map.py <bundle folder> [--png <dir>]
  -> <bundle>/Guggenheim_Audio_Guide_Route.pdf"""
import json, math, os, re, sys, html, asyncio, glob

B = sys.argv[1]
PNG_DIR = sys.argv[sys.argv.index("--png") + 1] if "--png" in sys.argv else None
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
TRACKS = os.path.join(ROOT, "v5", "tracks")
LENGTHS_JSON = os.path.join(HERE, "static", "lengths.json")
OUT_PDF = os.path.join(B, "Guggenheim_Audio_Guide_Route.pdf")
FOOTER = "Yo Tours · Guggenheim Museum Bilbao audio guide · 31 Oct 2026 edition · schematic plan, not to scale"
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
LENGTHS = [("Full tour", F_SET, "about 1 h 40", f"every stop, with ZERO, Holzer's columns, all of Serra, both balconies and the {FX} Extras"),
           ("Essential", E_SET, "about 1 h 15", "the plaza and the plaque, the Atrium, Serra on foot, the terrace, the flower, the river walk"),
           ("Highlights", H_SET, "about 45 min", "Puppy, the Atrium, Serra's gallery, the flower, Maman, the bridge")]

# ---------------------------------------------------------------- palette & sections
PAPER, INK, MUTED, LINE, CTX = "#F6F1E7", "#1F1B17", "#776E62", "#D8CEBD", "#ECE5D7"
RED, GOLD, NAVY = "#C0262D", "#A9812F", "#1D2B4A"
SECS = {  # @section -> (short title, colour, tint)
    "The plaza": ("The plaza", "#2E6A52", "#D3E4C4"),
    "Going in": ("Going in", "#3D3A36", "#E2DCD0"),
    "The Matter of Time": ("Serra · gallery 104", "#A4581B", "#F1D6BC"),
    "Up and down": ("Terrace, up and down", "#5B4A8A", "#E3DDF0"),
    "The river walk": ("The river walk", "#2C5A7E", "#D7E3EE"),
}
def colour(n): return SECS.get(TR[n]["section"], ("", INK, CTX))[1]
def tint(sec): return SECS[sec][2]
def stroke(sec): return SECS[sec][1]
def esc(s): return html.escape(s, quote=True)
def ds(room_prefix): return [n for n in NUMS if TR[n]["room"].startswith(room_prefix)]
def sec_ns(*secs): return [n for n in NUMS if TR[n]["section"] in secs]
def rng(sec):
    ns = sec_ns(sec)
    return (f"{ns[0]}–{ns[-1]}" if len(ns) > 1 else f"{ns[0]}") if ns else ""
def has(sub): return [n for n in NUMS if sub in TR[n]["room"]]
def one(ns, what):
    if not ns: sys.exit("route_map: no track for " + what)
    return ns[0]
def lst(ns): return ", ".join(map(str, ns[:-1])) + " and " + str(ns[-1]) if len(ns) > 1 else str(ns[0])
# the track numbers the drawings and texts name, all derived from @room / @section / @type of the track files
PLAZA_NS = sec_ns("The plaza")
N_WELCOME = one([n for n in PLAZA_NS if TR[n]["type"] == "ANCHOR"], "the welcome")
N_PUPPY = one(has("facing Puppy"), "facing Puppy")
N_PLAQUE = one(has("plaque"), "the plaque")
N_FRONT = one(has("facing the building"), "facing the building")
N_STAIR = one(has("stairway"), "the broad stairway")
N_ZERO = one(has("ZERO"), "ZERO")
N_ATR = one(ds("Atrium · floor 1"), "the Atrium")
N_101 = one(has("gallery 101"), "facing gallery 101")
G104 = ds("Gallery 104")
N_IN104 = one(has("just inside"), "the 104 entrance")
N_FIRST = one(has("first sculptures"), "the first sculptures")
N_SNAKE = one(ds("Gallery 104 · Snake"), "Snake")
N_SPIR = one(has("the spirals"), "the spirals")
N_FAR = one(has("the far end"), "the far end of 104")
N_104X = one(ds("Gallery 104 (anywhere"), "the 104 Extra")
N_TERR = one(ds("Atrium terrace"), "the terrace")
N_204 = one(has("opposite gallery 204"), "the balcony opposite 204")
N_LIFTS = one(ds("Glass lifts"), "the glass lifts")
N_304 = one(has("opposite gallery 304"), "the balcony opposite 304")
N_DOWN = one(ds("Going down"), "going down")
N_HALL = one([n for n in NUMS if TR[n]["room"] == "The Hall"], "the Hall Extra")
N_OUT = one(ds("Outside"), "the way out")
POND = has("by the pond")
if not POND: sys.exit("route_map: no track for the pond")
N_MAMAN = one(has("Maman"), "Maman")
N_TI = one(has("titanium"), "the titanium")
N_SALVE = one(has("tower in view"), "La Salve Bridge and the tower")
N_RWX = one(ds("River walk (anywhere"), "the river-walk Extra")
N_CLOSE = one([n for n in NUMS if TR[n]["type"] == "CLOSE"], "the close")
UPPER = [N_204, N_LIFTS, N_304, N_DOWN]

TI, TI_D, WATER, WATER_D, GRASS, PAVE = "#DADDE0", "#8D949B", "#CFE1E8", "#7FA7B6", "#DCE6CC", "#ECE4D4"
STEEL = "#9C5A2E"
DASH = "1.2,.8"

# ---------------------------------------------------------------- SVG kit (units = mm)
class Svg:
    def __init__(self, W, H, bg="#FDFBF7"):
        self.W, self.H = W, H
        self.o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}mm" height="{H}mm">',
                  f'<rect x="0" y="0" width="{W}" height="{H}" rx="2" fill="{bg}"/>']
    def add(self, s): self.o.append(s)
    def rect(self, x0, y0, x1, y1, fill, strk="none", sw=.3, dash=None, rx=0, op=1):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<rect x="{x0:.2f}" y="{y0:.2f}" width="{x1 - x0:.2f}" height="{y1 - y0:.2f}" rx="{rx}" fill="{fill}" fill-opacity="{op}" stroke="{strk}" stroke-width="{sw}"{d}/>')
    def path(self, d, fill="none", strk=INK, sw=.3, dash=None, op=1, fop=1, extra=""):
        ds_ = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<path d="{d}" fill="{fill}" fill-opacity="{fop}" stroke="{strk}" stroke-width="{sw}" stroke-opacity="{op}"{ds_} stroke-linecap="round" stroke-linejoin="round"{extra}/>')
    def poly(self, pts, close=False, **kw):
        self.path("M" + " L".join(f"{x:.2f},{y:.2f}" for x, y in pts) + (" Z" if close else ""), **kw)
    def circle(self, x, y, r, fill, strk="none", sw=.3, dash=None, op=1):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{fill}" fill-opacity="{op}" stroke="{strk}" stroke-width="{sw}"{d}/>')
    def text(self, x, y, t, cls="pl", anc="start", fs=None, fill=None, rot=None, weight=None):
        lines = t.split("\n"); fs = fs or 2.8
        st = f"font-size:{fs:.2f}px;text-anchor:{anc}" + (f";fill:{fill}" if fill else "") + (f";font-weight:{weight}" if weight else "")
        tr = f' transform="rotate({rot} {x:.2f} {y:.2f})"' if rot is not None else ""
        sp = "".join(f'<tspan x="{x:.2f}" dy="{0 if i == 0 else fs * 1.2:.2f}">{esc(l)}</tspan>' for i, l in enumerate(lines))
        self.add(f'<text x="{x:.2f}" y="{y:.2f}" class="{cls}" style="{st}"{tr}>{sp}</text>')
    def arrowhead(self, x, y, ang, k=1.1, fill=INK, op=.85):
        self.add(f'<path d="M{-k:.2f},{-k * .8:.2f} L{k:.2f},0 L{-k:.2f},{k * .8:.2f} Z" fill="{fill}" fill-opacity="{op}" transform="translate({x:.2f},{y:.2f}) rotate({ang:.1f})"/>')
    def route(self, pts, kind="main", mid=True, end=True, minlen=9):
        """main = dashed with arrows (documented link); unc = dotted (path to be confirmed on site)."""
        d = "M" + " L".join(f"{x:.2f},{y:.2f}" for x, y in pts)
        self.add(f'<path d="{d}" fill="none" stroke="#FDFBF7" stroke-opacity=".75" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>')
        if kind == "main":
            self.add(f'<path d="{d}" fill="none" stroke="{INK}" stroke-opacity=".75" stroke-width=".55" stroke-dasharray="1.5,1" stroke-linecap="round" stroke-linejoin="round"/>')
        else:
            self.add(f'<path d="{d}" fill="none" stroke="{INK}" stroke-opacity=".7" stroke-width=".75" stroke-dasharray=".1,1.2" stroke-linecap="round" stroke-linejoin="round"/>')
        if mid:
            for (xa, ya), (xb, yb) in zip(pts, pts[1:]):
                if math.hypot(xb - xa, yb - ya) < minlen: continue
                self.arrowhead((xa + xb) / 2, (ya + yb) / 2, math.degrees(math.atan2(yb - ya, xb - xa)), 1.05)
        if end:
            (xa, ya), (xb, yb) = pts[-2], pts[-1]
            self.arrowhead(xb, yb, math.degrees(math.atan2(yb - ya, xb - xa)), 1.05)
    def dots(self, x, y, ns, dr="r", rad=2.4):
        step = rad * 2.18
        vx, vy = {"r": (step, 0), "l": (-step, 0), "d": (0, step), "u": (0, -step)}[dr]
        for i, s in enumerate(ns):
            cx, cy = x + i * vx, y + i * vy; c = colour(s)
            if s in XS:
                self.add(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{rad * .94:.2f}" fill="#fff" stroke="{c}" stroke-width="{rad * .2:.2f}"/>'
                         f'<text x="{cx:.2f}" y="{cy + rad * .36:.2f}" class="sn" style="font-size:{rad * .98:.2f}px;fill:{c}">{s}</text>')
            else:
                self.add(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{rad:.2f}" fill="{c}" stroke="#fff" stroke-width="{rad * .14:.2f}"/>'
                         f'<text x="{cx:.2f}" y="{cy + rad * .36:.2f}" class="sn" style="font-size:{rad * 1.0:.2f}px">{s}</text>')
    def note(self, px, py, text, kind, tx, ty, fs=2.5):
        """A pill callout at (tx, ty) (its centre), with a leader to (px, py)."""
        colr = {"start": INK, "finish": INK, "info": MUTED, "warn": GOLD, "river": stroke("The river walk"),
                "up": stroke("Up and down"), "serra": stroke("The Matter of Time")}[kind]
        lines = text.split("\n"); wmax = max(len(l) for l in lines) * fs * .56 + fs * 1.6
        hb = fs * 1.36 * len(lines) + fs * .6
        bx = min(max(tx - wmax / 2, .8), self.W - wmax - .8); by = min(max(ty - hb / 2, .8), self.H - hb - .8)
        if px is not None:
            self.add(f'<line x1="{px:.2f}" y1="{py:.2f}" x2="{bx + wmax / 2:.2f}" y2="{by + hb / 2:.2f}" stroke="{colr}" stroke-width=".35" stroke-dasharray="1,.7"/>')
            self.add(f'<circle cx="{px:.2f}" cy="{py:.2f}" r=".8" fill="{colr}"/>')
        self.add(f'<rect x="{bx:.2f}" y="{by:.2f}" width="{wmax:.2f}" height="{hb:.2f}" rx="{min(hb / 2, 2):.2f}" fill="{colr}"/>')
        for i, l in enumerate(lines):
            self.add(f'<text x="{bx + fs * .8:.2f}" y="{by + fs * 1.2 + i * fs * 1.36:.2f}" class="note" style="font-size:{fs:.2f}px">{esc(l)}</text>')
    def done(self): return "".join(self.o) + "</svg>"

def stairs(s, x0, y0, x1, y1, n, colr=INK, sw=.35, dash=None):
    """A little flight of steps from (x0, y0) to (x1, y1)."""
    pts = [(x0, y0)]; dx, dy = (x1 - x0) / n, (y1 - y0) / n
    for i in range(n):
        x, y = pts[-1]; pts += [(x, y + dy), (x + dx, y + dy)]
    s.poly(pts, strk=colr, sw=sw, dash=dash)

def stair_band(s, x0, y0, x1, y1, n, colr="#8F8473", fill=PAVE, dash=None):
    """Steps seen from above: a band with n treads across it (treads perpendicular to the long side)."""
    s.rect(min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1), fill, colr, .3, dash=dash)
    if abs(x1 - x0) >= abs(y1 - y0):
        for i in range(1, n): x = x0 + (x1 - x0) * i / n; s.path(f"M{x:.2f},{y0:.2f} L{x:.2f},{y1:.2f}", strk=colr, sw=.22)
    else:
        for i in range(1, n): y = y0 + (y1 - y0) * i / n; s.path(f"M{x0:.2f},{y:.2f} L{x1:.2f},{y:.2f}", strk=colr, sw=.22)

def puppy(s, x, y, k=1.0):
    """Puppy from above: a mound of flowers (dots of colour), schematic."""
    s.circle(x, y, 4.2 * k, "#BFD59A", "#6E8F4A", .35)
    for i, (dx, dy, c) in enumerate([(-1.8, -1.5, "#E4A0B5"), (1.4, -2, "#F2C84B"), (2.2, .8, "#E4A0B5"), (-.6, 1.9, "#F2C84B"),
                                      (-2.5, .6, "#D67A52"), (.6, -.2, "#D67A52"), (1.1, 2.7, "#B98ED0"), (-1.2, -3, "#B98ED0")]):
        s.circle(x + dx * k, y + dy * k, .65 * k, c)

def kapoor(s, x, y, k=1.0):
    """Tall Tree & the Eye from above: a cluster of silver balls."""
    for dx, dy, r in [(0, 0, 1.3), (-1.8, -.9, .9), (1.7, -1, .95), (-1.2, 1.5, .85), (1.4, 1.4, .9), (0, -2.2, .8), (-2.6, .7, .6), (2.6, .4, .6), (.2, 2.6, .6)]:
        s.circle(x + dx * k, y + dy * k, r * k, "#EEF1F3", "#7C858C", .22)

def maman(s, x, y, k=1.0):
    """Maman from above: a small body and eight long bent legs."""
    for a in (20, 50, 130, 160, 200, 230, 310, 340):
        r = math.radians(a); kx, ky = x + math.cos(r) * 3 * k, y + math.sin(r) * 3 * k
        ex, ey = x + math.cos(r) * 5.4 * k, y + math.sin(r) * 5.4 * k
        s.path(f"M{x:.2f},{y:.2f} L{kx:.2f},{ky:.2f} L{ex:.2f},{ey:.2f}", strk="#4A3A2E", sw=.38 * k)
    s.circle(x, y, 1.3 * k, "#4A3A2E")

def chillida(s, x, y, k=1.0):
    s.rect(x - 1.1 * k, y - 1.6 * k, x + 1.1 * k, y + 1.6 * k, "#3E3A36", "none", rx=.3)

def water(s, x0, y0, x1, y1, step=4.5):
    s.rect(x0, y0, x1, y1, WATER)
    for y in [y0 + step * (i + .6) for i in range(int((y1 - y0) / step))]:
        for x in range(int(x0) + 2, int(x1) - 4, 13):
            s.path(f"M{x},{y:.2f} q1.5,-.9 3,0 t3,0", strk=WATER_D, sw=.22, op=.7)

# ---------------------------------------------------------------- stop lists and dots in text
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

LEGEND = (f'<div class="legend"><span>{dot(N_ATR, "ldot")} track</span><span><span class="ldot hol" style="color:{INK};border-color:{INK}">X</span> Extra</span>'
          f'<span><svg width="9mm" height="3mm" viewBox="0 0 9 3"><path d="M.5,1.5 L8.5,1.5" stroke="{INK}" stroke-opacity=".75" stroke-width=".55" stroke-dasharray="1.5,1"/></svg> route, in walking order</span>'
          f'<span><svg width="9mm" height="3mm" viewBox="0 0 9 3"><path d="M.5,1.5 L8.5,1.5" stroke="{INK}" stroke-opacity=".7" stroke-width=".75" stroke-dasharray=".1,1.2" stroke-linecap="round"/></svg> path to be confirmed on site</span>'
          f'<span><svg width="7mm" height="4mm" viewBox="0 0 7 4"><rect x=".5" y=".5" width="6" height="3" fill="#fff" stroke="{INK}" stroke-width=".3" stroke-dasharray="1.1,.7"/></svg> position to be confirmed on site</span>'
          '</div>')

pages = []
def map_page(kicker, title, sub, body, ns, extra=""):
    lst_ = f'<div class="list">{stop_list(ns)}</div>' if ns else ""
    return f'''<section class="page">
 <header class="fh"><div class="brand">YO TOURS · GUGGENHEIM BILBAO · {esc(kicker)}</div>
 <h2>{esc(title)}</h2><p class="sub">{sub}</p></header>
 {body}{lst_}{extra}
 <footer>{esc(FOOTER)}</footer>
</section>'''

# ---------------------------------------------------------------- page 1: the whole site from above
# City side below, the river above, La Salve Bridge toward the right. Schematic orientation, NOT to scale, no compass.
def site_svg():
    s = Svg(184, 132)
    rw = stroke("The river walk"); pl = stroke("The plaza")
    # the river and the river walk
    water(s, 0, 0, 184, 15)
    s.rect(0, 15, 184, 23, PAVE, "none"); s.path("M0,15 L184,15", strk=WATER_D, sw=.4)
    s.text(4, 6.4, "THE RIVER · the Nervión", "lvt", "start", 2.5, fill="#3E6474")
    s.text(60, 22.3, "river walk", "plm", "middle", 2.1)
    # park and grass between the walk, the pond and the building
    s.rect(0, 23, 184, 40, GRASS, "none")
    # the footbridge by Maman (never named) [O14]
    s.rect(100, 0, 105, 15, "#E9E1D2", "#8F8473", .3, dash=DASH)
    s.text(107, 4.4, "footbridge", "pls", "start", 2.2)
    # the pond on the river side, by the river-side galleries [O13]
    s.rect(14, 24.5, 92, 35.5, WATER, WATER_D, .4, dash=DASH, rx=2.5)
    kapoor(s, 30, 30, .9)
    s.text(53, 29.2, "the pond", "plb", "middle", 2.7)
    s.text(53, 32.6, "Kapoor · fog · fire", "pls", "middle", 2.2)
    # the building: titanium massing (schematic)
    bld = ("M12,42 C14,38 30,37 44,39 C56,40 62,37 68,40 L100,40 C106,38 112,40 116,41 L168,41 C178,42 181,45 180,47 "
           "C179,50 172,52 160,53 L140,54 C136,62 124,66 112,66 L104,67 C102,72 98,74 92,74 L74,74 C70,72 66,72 60,73 "
           "C46,75 26,74 18,70 C12,66 10,52 12,42 Z")
    s.path(bld, fill=TI, strk=TI_D, sw=.4)
    # the terrace, off the Atrium on the river side [O7]
    s.rect(66, 35.5, 92, 40.8, "#F2EEE6", "#6E665B", .35, dash=DASH, rx=1)
    s.text(73.5, 39, "terrace", "plm", "middle", 2.2)
    # gallery 104, the long gallery from the Atrium under the bridge
    s.path("M96,43 L166,43.5 C176,44 178,46 177,47.5 C176,49 170,50 160,50.2 L96,51 Z", fill="#F1D6BC", strk=stroke("The Matter of Time"), sw=.4)
    s.text(160, 57.6, "gallery 104", "plb", "middle", 2.5)
    # the Atrium, the Hall, gallery 101
    s.path("M70,43 C76,41 88,41 94,44 C98,48 98,56 93,59 C86,62 76,61 71,57 C67,53 66,46 70,43 Z", fill="#FBF8F1", strk=INK, sw=.4)
    s.text(82, 47, "Atrium", "plb", "middle", 2.8)
    s.rect(72, 61.5, 96, 70, "#FBF8F1", "#6E665B", .35, rx=1)
    s.text(76, 66.6, "Hall", "plm", "middle", 2.3)
    s.path("M46,44 L64,43 L65,53 L47,55 Z", fill="#FBF8F1", strk="#6E665B", sw=.35)
    s.text(55.5, 47.4, "gallery 101", "plm", "middle", 2.3)
    s.text(36, 63.5, "exhibition galleries ·\nnot part of this guide", "pls", "middle", 2.1)
    # La Salve Bridge crossing over the end of the site, the tower at the building's end
    s.path("M128,132 L138,0 L148,0 L138,132 Z", fill="#D8D2C6", strk="#6E665B", sw=.4, fop=.88)
    s.text(135.9, 112, "La Salve Bridge", "plb", "middle", 2.6, rot=-85.7)
    s.rect(146, 30, 153, 37, "#C9CED3", TI_D, .4, rx=1)                         # the tower, beside the bridge
    s.text(155, 34.4, "the tower", "plm", "start", 2.3)
    for y0 in (19.6,):                                                          # Buren's red arches on the bridge
        s.path(f"M138.6,{y0 - 8} L147,{y0 - 7.4}", strk=RED, sw=1.1)
    s.text(150, 13.2, "red arches on the bridge", "plm", "start", 2.2, fill=RED)
    # the plaza (at floor-2 level), Puppy, the plaque, Calle Iparragirre
    s.path("M50,78 C60,76 104,76 114,79 L118,104 C100,107 66,107 48,104 Z", fill="#E8E0CF", strk="#8F8473", sw=.35)
    s.text(86, 102.4, "Museum plaza", "plb", "middle", 2.8)
    stair_band(s, 77, 70.5, 91, 78.5, 6)                                         # the broad stairway, plaza down to the Hall
    s.text(94, 75.6, "broad stairway", "pls", "start", 2.2)
    puppy(s, 62, 88, 1.0)
    s.text(62, 82.6, "Puppy", "plm", "middle", 2.4)
    s.rect(55, 105.5, 69, 111, "#F4EEE2", pl, .35, dash=DASH, rx=1)            # the small square in front of Puppy, city side [O2]
    s.rect(60.6, 107.2, 63.4, 109.2, "#8F8473", "none")
    s.text(62, 114.6, "the plaque", "plm", "middle", 2.3)
    s.rect(78, 107, 90, 132, "#E3DCCD", "#8F8473", .3)                          # Calle Iparragirre, in line with the plaza and entrance
    s.text(84.8, 120, "Calle Iparragirre", "pls", "middle", 2.1, rot=-90)
    s.text(4, 128.6, "CITY SIDE", "lvt", "start", 2.3)
    # the stairs down from the plaza toward the park and the river walk, on the side away from the bridge [O12]
    stair_band(s, 38, 84, 48, 90, 5, dash=DASH)
    # the route: plaza -> stairway -> inside -> out -> river walk -> bridge
    s.route([(98, 92), (84, 92), (84, 79)], "main", mid=False)
    s.route([(84, 72), (84, 61)], "main", mid=False)
    s.route([(92, 55), (100, 47)], "main", mid=False)
    s.route([(104, 47), (160, 47)], "main", mid=False)
    s.route([(160, 46), (104, 45)], "main", mid=False, end=False)
    s.route([(84, 43), (84, 39.5)], "main", mid=False)
    s.route([(70, 68), (60, 72), (50, 84), (43, 87), (8, 87), (8, 18.6), (14, 18.6)], "unc", mid=True, minlen=20)
    s.route([(14, 18.6), (130, 18.6), (160, 18.6)], "main", mid=True, minlen=30)
    # dots
    s.dots(102, 92, [N_WELCOME], rad=2.5)
    s.dots(68.5, 91, [N_PUPPY], rad=2.5)
    s.dots(52, 108.3, [N_PLAQUE], rad=2.5)
    s.dots(98, 84, [N_FRONT], rad=2.5)
    s.dots(96, 70.5, [N_STAIR], "r", rad=2.5)
    s.dots(88, 66, [N_ZERO], rad=2.3)
    s.dots(74, 53, [N_ATR, N_101], rad=2.3)
    s.dots(102.5, 47, G104, rad=2.15)
    s.dots(96, 37.6, [N_TERR], rad=2.3)
    s.dots(53, 58, UPPER, rad=2.3)
    s.dots(80.5, 66, [N_HALL], rad=2.0)
    s.dots(8, 55, [N_OUT], rad=2.5)
    s.dots(24, 18.6, POND, rad=2.3)
    maman(s, 108, 18.6, .75)
    s.dots(108, 27.5, [N_MAMAN], rad=2.3)
    s.text(111.6, 28.4, "Maman", "plm", "start", 2.3)
    s.dots(124, 33, [N_TI], rad=2.3)
    s.text(124, 38.3, "titanium", "pls", "middle", 2.0)
    s.dots(129, 18.6, [N_SALVE], rad=2.3)
    s.dots(160, 18.6, [N_RWX, N_CLOSE], rad=2.3)
    # callouts
    s.note(53, 56, "floors 2 and 3 · page 3", "up", 31, 52.5, 2.2)
    s.note(8, 87, "OUT · stairs down toward the park\nand the river walk (to be confirmed)", "info", 25, 117.5, 2.2)
    s.note(102, 94.5, "START · on the plaza", "start", 114, 114, 2.4)
    s.note(167, 20.5, "END · by the bridge", "finish", 168, 28, 2.4)
    s.text(181.5, 129.6, "SCHEMATIC · NOT TO SCALE", "scl", "end", 2.3)
    return s.done()

KEYS = "".join(f'<span><i style="background:{SECS[k][1]}"></i><em>{esc(SECS[k][0])} <b>{rng(k)}</b></em></span>' for k in SECS if rng(k))
def len_card(i, name, ns, when, desc):
    ds_ = "".join(dot(n, "mdot") for n in sorted(ns))
    return (f'<div class="card"><div class="ch"><div class="cnum">{i}</div><div><div class="ct">{esc(name)}</div>'
            f'<div class="cs"><b>{esc(when)}</b> · {len(ns)} tracks</div></div></div>'
            f'<div class="cdots">{ds_}</div><div class="cs2">{esc(desc)}</div></div>')
lens = "".join(len_card(i, n, ns, m, d) for i, (n, ns, m, d) in enumerate(LENGTHS, 1))
pages.append(f'''<section class="page">
 <header><div class="brand">YO TOURS · AUDIO GUIDE</div><h1>Guggenheim Museum Bilbao</h1>
 <p class="lede">The building, inside and out, and the works that live here: {len(F_SET) - FX} main stops plus {FX} short Extras in one walking order, in three lengths.</p></header>
 <div class="how"><div><b>1</b> <strong>Plaza, inside, then the river.</strong> Puppy and the plaza first, down the broad stairway, the Atrium and Serra's long gallery, up to the balconies, then out and round to the river walk, along the water to the bridge.</div>
 <div><b>2</b> The coloured circle is the track to play there, in track order. Hollow circles are short, optional Extras, on the Full tour only. Pages 2 to 4 show every track in its place.</div>
 <div><b>3</b> Each track ends by telling you where to go next. This is a schematic plan, not to scale. <strong>Dashed and dotted: not yet confirmed on site.</strong></div></div>
 <div class="ov">{site_svg()}<div class="keys">{KEYS}</div>{LEGEND}</div>
 <div class="cards">{lens}</div>
 <div class="warn"><b>Two timings only:</b> the fog in the pond runs on the hour; the fire fountains burn only in the evening. The changing exhibitions are not part of this guide; you will walk past some of them. Times include walking and the lifts, not queues or waiting for the fog. In the shorter versions the track numbers jump, and every stop tells you where to go next.</div>
 <footer>{esc(FOOTER)}</footer>
</section>''')

# ---------------------------------------------------------------- page 2: floor 1 inside (005–015)
SERRA_ORDER = ["Torqued Spiral\n(Closed Open Closed\nOpen Closed)", "Torqued\nEllipse", "Double Torqued\nEllipse", "Snake",
               "Torqued Spiral\n(Right Left)", "Torqued Spiral\n(Open Left\nClosed Right)", "Between the\nTorus and\nthe Sphere", "Blind Spot\nReversed"]
def floor1_svg():
    s = Svg(184, 114); sc = stroke("The Matter of Time"); up = stroke("Up and down")
    # outside, on the river side: the pond, seen from the terrace
    s.rect(0, 0, 184, 15, GRASS, "none")
    s.rect(14, 2.5, 120, 13, WATER, WATER_D, .4, dash=DASH, rx=2.5)
    kapoor(s, 28, 7.8, .8)
    s.text(72, 9, "the pond, outside, below the terrace · page 4", "plm", "middle", 2.4)
    s.text(181, 6, "RIVER SIDE", "lvt", "end", 2.3)
    # the building's floor 1 (schematic outline)
    s.path("M4,22 C10,17 40,18 58,19 L120,19 C150,20 172,20 180,23 L180,90 C150,93 130,92 112,93 L64,93 "
           "C54,93 30,93 10,92 C4,86 2,40 4,22 Z", fill="#F1EEE8", strk=TI_D, sw=.45)
    # the terrace, off the Atrium on the river side [O7], the two Chillidas on it
    s.rect(52, 14.5, 92, 24, "#F2EEE6", "#6E665B", .4, dash=DASH, rx=1.2)
    chillida(s, 58, 19.2); chillida(s, 63, 18.6)
    s.text(79, 20.6, "terrace", "plb", "middle", 2.6)
    s.text(60.5, 27.2, "two Chillidas", "pls", "middle", 2.1)
    # gallery 101 with Holzer's nine columns, seen from the Atrium
    s.path("M10,26 L44,26 L46,46 L12,48 Z", fill="#FBF8F1", strk="#6E665B", sw=.4)
    for i in range(9):
        x = 14 + i * 3.4; s.rect(x, 33, x + 1.4, 41, RED if i % 2 == 0 else "#2F5DA8", "none", rx=.2)
    s.text(28, 30.6, "gallery 101 · Holzer's columns", "plm", "middle", 2.4)
    # exhibition galleries: not part of the guide
    s.path("M8,54 L46,54 L48,88 L12,90 Z", fill="#E2DED6", strk="#B7AFA3", sw=.3)
    s.text(29, 69, "exhibition\ngalleries ·\nnot part of\nthis guide", "pls", "middle", 2.2)
    s.path("M120,68 L172,66 L174,86 L122,88 Z", fill="#E2DED6", strk="#B7AFA3", sw=.3)
    s.text(148, 78.6, "exhibition galleries · not part of this guide", "pls", "middle", 2.1)
    # the Atrium
    s.path("M54,30 C64,26 90,26 100,32 C108,40 108,56 100,62 C90,68 66,68 56,62 C48,56 46,38 54,30 Z", fill="#FBF8F1", strk=INK, sw=.5)
    s.text(78, 35, "Atrium", "plb", "middle", 3.2)
    s.text(78, 38.4, "the tall heart · skylight above", "pls", "middle", 2.1)
    for x in (80, 85):                                                            # glass lifts [O8]
        s.rect(x, 56, x + 3.6, 59.6, "#E6F0F4", "#6F8C99", .35, dash=DASH)
    s.text(84.4, 63.6, "glass lifts · up, page 3", "pls", "middle", 2.0, fill=up)
    # gallery 104, the long gallery from the Atrium under the bridge; the eight sculptures as a sequence only [O6, ALT-S]
    g = "M104,30 L170,31 C180,32 182,38 182,44 C182,50 178,55 170,56 L104,57 C106,48 106,38 104,30 Z"
    s.path(g, fill="#F7E7D6", strk=sc, sw=.5)
    s.rect(136, 24, 148, 59, "#BDB6A8", "#6E665B", .35, op=.45)                   # La Salve Bridge, overhead
    s.text(142, 62.2, "La Salve Bridge\noverhead", "pls", "middle", 2.0)
    s.rect(169, 37, 180.5, 50, "#FFF8EE", sc, .3, dash=DASH, rx=1)                # educational space at the far end
    s.text(174.8, 42, "video", "plm", "middle", 2.1); s.text(174.8, 45, "(far end)", "pls", "middle", 1.9)
    xs = [111 + i * 7.6 for i in range(8)]
    for i, x in enumerate(xs):
        s.add(f'<ellipse cx="{x:.2f}" cy="39" rx="3.1" ry="2.3" fill="#C98A5C" fill-opacity=".55" stroke="{STEEL}" stroke-width=".35" stroke-dasharray="{DASH}"/>')
        s.text(x, 39.9, str(i + 1), "plm", "middle", 2.3, fill="#4A2A14")
    s.route([(108, 34.2), (164, 34.2)], "unc", mid=False, end=True)
    s.text(106, 28.4, "gallery 104 · Serra, The Matter of Time", "plb", "start", 2.6)
    # track dots along 104, placed at their place in the sequence
    s.dots(xs[0] - 1, 47.8, [N_IN104], rad=2.3)
    s.dots(xs[1] + 1, 47.8, [N_FIRST], rad=2.3)
    s.dots(xs[3], 47.8, [N_SNAKE], rad=2.3)
    s.dots((xs[4] + xs[5]) / 2, 47.8, [N_SPIR], rad=2.3)
    s.dots((xs[6] + xs[7]) / 2, 47.8, [N_FAR], rad=2.3)
    s.dots(160, 52.6, [N_104X], rad=2.0)
    s.text(156.8, 53.4, "anywhere", "pls", "end", 1.9)
    s.route([(165, 54.4), (104, 54.4)], "main", mid=True, end=True, minlen=30)      # the walk back to the Atrium
    # ZERO in the lobby, beside the Hall [O4]
    s.rect(98, 70, 114, 80, "#F4F0C8", "#8F8A2A", .4, dash=DASH, rx=1)
    s.text(106, 75.6, "ZERO", "plb", "middle", 2.7)
    # the Hall, and the broad stairway down from the plaza
    s.path("M58,70 L94,70 L94,88 C86,90 66,90 58,88 Z", fill="#FBF8F1", strk="#6E665B", sw=.4)
    s.text(66, 76.6, "the Hall", "plb", "middle", 2.9)
    stair_band(s, 70, 93, 84, 111, 7)
    s.text(87, 103, "broad stairway\nup to the plaza", "pls", "start", 2.2)
    s.text(4, 111, "CITY SIDE · THE PLAZA ABOVE", "lvt", "start", 2.3)
    # the route on floor 1: stairway -> Hall -> ZERO -> Atrium -> 104 and back -> terrace
    s.route([(77, 112), (77, 89)], "main", mid=True, minlen=12)
    s.route([(80, 84), (97, 77)], "main", mid=False)
    s.route([(103, 69.5), (99, 63)], "main", mid=False)
    s.route([(62, 47), (102, 45)], "main", mid=True, minlen=20)
    s.route([(100, 52), (94, 36), (86, 25)], "main", mid=False)
    # dots
    s.dots(77, 99, [N_STAIR], rad=2.5)
    s.dots(90, 84, [N_ZERO], rad=2.5)
    s.dots(72, 54, [N_ATR], rad=2.5)
    s.dots(57, 44, [N_101], rad=2.5)
    s.dots(96.5, 19.2, [N_TERR], rad=2.5)
    s.dots(64.6, 82.6, [N_HALL], rad=2.4)
    s.text(64.6, 87.2, "on the way out", "pls", "middle", 1.9)
    s.text(181.5, 111, "SCHEMATIC · NOT TO SCALE", "scl", "end", 2.3)
    return s.done()

F1_NS = [n for n in NUMS if N_STAIR <= n <= N_TERR]
serra_li = "".join(f"<li><b>{i}</b> {esc(t.replace(chr(10), ' '))}</li>" for i, t in enumerate(SERRA_ORDER, 1))
f1extra = f'''<div class="boxes">
 <div class="box"><h3>The eight Serras, in order</h3><ol class="serra">{serra_li}</ol><p class="fine">Expected order from the Atrium end; only the sequence is drawn. Read the labels.</p></div>
 <div class="box"><h3>Gallery 104</h3><p>The long gallery that opens off the Atrium and runs under the bridge. Play {N_IN104} just inside, then walk the sculptures in order to the far end, where there is an educational space with a video. The gallery appears to be a dead end: walk back the same way to the Atrium ({N_104X} is an Extra for anywhere in 104).</p></div>
 <div class="box"><h3>The Hall, the Atrium, the terrace</h3><p>Play {N_STAIR} walking down the broad stairway, {N_ZERO} outside the door of ZERO, the small room in the lobby. In the Atrium, {N_ATR} near the middle, {N_101} where you can see into gallery 101. After 104, the terrace on the river side ({N_TERR}); then back in and up. The way out is still to be confirmed: follow the signs.</p></div>
</div>'''
pages.append(map_page("FLOOR 1 · THE ATRIUM LEVEL", f"Inside, floor 1 · {F1_NS[0]} to {F1_NS[-1]}",
    f"Down the broad stairway into the Hall ({N_STAIR}), ZERO in the lobby ({N_ZERO}), the Atrium ({N_ATR}) and Holzer's columns in gallery 101 ({N_101}), "
    f"then Serra's long gallery 104, under La Salve Bridge ({lst(G104)}), and the terrace on the river side ({N_TERR}). The museum calls this level floor 1; the plaza outside is one floor higher.",
    f'<div class="plan">{floor1_svg()}{LEGEND}</div>', F1_NS, f1extra))

# ---------------------------------------------------------------- page 3: floors 2 and 3, a section through the Atrium and 104 (016–021)
F1Y, F2Y, F3Y, ROOF = 104, 72, 42, 24
def upper_svg():
    s = Svg(184, 128); up = stroke("Up and down"); sc = stroke("The Matter of Time")
    # the ground; the plaza is at floor-2 level, the Hall and the Atrium at floor 1
    s.rect(0, F1Y, 184, 128, "#E6DCC8")
    s.path(f"M0,{F2Y} L30,{F2Y} L46,{F1Y} L184,{F1Y}", strk="#6E665B", sw=.6)
    s.path(f"M0,{F2Y} L30,{F2Y} L46,{F1Y} L0,{F1Y} Z", fill="#E6DCC8", strk="none")
    s.rect(0, F2Y - 1.4, 30, F2Y, "#E8E0CF")
    stairs(s, 30, F2Y, 46, F1Y, 8, "#6E665B", .45)
    puppy(s, 12, F2Y - 5.4, .9)
    s.text(14, F2Y + 6, "the plaza,\nlevel with\nfloor 2", "plm", "middle", 2.3)
    s.text(40, F2Y + 28.4, "broad stairway", "pls", "end", 2.1)
    # the building in section
    s.path(f"M46,{F1Y} L46,{F3Y - 6} C48,{ROOF} 56,{ROOF - 4} 62,{ROOF - 2} L112,{ROOF - 2} C118,{ROOF} 120,{ROOF + 8} 120,{F3Y + 8} "
           f"L120,{F1Y} Z", fill="#F1EEE8", strk=TI_D, sw=.45)
    # galleries on floors 2 and 3 beside the Atrium: exhibitions and the Collection, not stops
    s.rect(47, F3Y, 60, F2Y - .4, "#E2DED6", "#B7AFA3", .3)
    s.rect(47, F2Y + .4, 60, F1Y - 12, "#E2DED6", "#B7AFA3", .3)
    s.text(53.5, F3Y + 12, "galleries", "pls", "middle", 2.0, rot=-90)
    # the Atrium: the tall void, the metal-flower skylight on top
    s.rect(62, ROOF + 2, 112, F1Y, "#FBF8F1", "none")
    s.path(f"M60,{ROOF + 2} C66,{ROOF - 10} 74,{ROOF - 14} 87,{ROOF - 15} C100,{ROOF - 14} 108,{ROOF - 10} 114,{ROOF + 2} Z",
           fill="#E6F0F4", strk="#6F8C99", sw=.45)
    for x in (70, 78, 87, 96, 104):
        s.path(f"M87,{ROOF + 1.6} L{x},{ROOF - 9 - (6 - abs(x - 87) / 3):.1f}", strk="#6F8C99", sw=.3)
    s.text(87, ROOF - 16.4, "the metal-flower skylight", "plm", "middle", 2.4)
    # floor slabs, walkways (curved) and the glass lifts in the Atrium [O8]
    for y in (F2Y, F3Y):
        s.rect(47, y - .8, 62, y + .8, "#C9C3B8"); s.rect(112, y - .8, 120, y + .8, "#C9C3B8")
        s.path(f"M62,{y} C72,{y + 3.4} 92,{y - 3.4} 112,{y}", strk="#8F8473", sw=.7)
    for x in (70, 100):
        s.rect(x, ROOF + 6, x + 5, F1Y, "#E6F0F4", "#6F8C99", .35, dash=DASH, op=.8)
    s.text(72.5, F1Y - 3, "glass\nlift", "pls", "middle", 1.9)
    s.text(102.5, F1Y - 3, "glass\nlift", "pls", "middle", 1.9)
    s.text(87, F1Y - 12, "Atrium", "plb", "middle", 3.2)
    s.text(87, F2Y - 4, "walkways", "pls", "middle", 2.1)
    s.text(87, F3Y - 4, "walkways", "pls", "middle", 2.1)
    # gallery 104: the tall gallery from the Atrium under La Salve Bridge, the tower at the end
    s.path(f"M120,{F1Y} L120,{F2Y - 16} L170,{F2Y - 10} C176,{F2Y - 8} 178,{F2Y} 178,{F1Y} Z", fill="#F7E7D6", strk=sc, sw=.45)
    for i in range(8):
        x = 126 + i * 6.4; s.rect(x, F1Y - 9 - (i % 3), x + 3.6, F1Y, "#C98A5C", STEEL, .3, op=.7)
    s.text(176, F2Y - 3.6, "gallery 104 ·\nthe eight Serras", "plb", "end", 2.6)
    s.rect(139, F2Y - 24, 159, F2Y - 18, "#D8D2C6", "#6E665B", .4)                  # La Salve Bridge (cut through the deck)
    s.text(149, F2Y - 25.8, "La Salve Bridge", "plm", "middle", 2.3)
    s.rect(170, F3Y - 18, 178, F2Y - 10, "#C9CED3", TI_D, .4, rx=.8)               # the tower
    s.text(174, F3Y - 20, "tower", "pls", "middle", 2.1)
    # the balcony opposite gallery 204 (floor 2), looking down into 104 [O9]
    s.rect(112, F2Y - 2, 126, F2Y + 1, "#fff", up, .45, dash=DASH)
    s.path(f"M126,{F2Y - 1} L160,{F1Y - 14}", strk=up, sw=.35, dash="1,.8")
    s.arrowhead(160, F1Y - 14, math.degrees(math.atan2(F1Y - 14 - F2Y + 1, 34)), .9, fill=up)
    s.text(124, F2Y + 5.2, "balcony opposite gallery 204", "plm", "start", 2.3, fill=up)
    # the balcony opposite gallery 304 (floor 3), looking out over the Atrium [O10]
    s.rect(104, F3Y - 2, 118, F3Y + 1, "#fff", up, .45, dash=DASH)
    s.path(f"M104,{F3Y - 2} L90,{ROOF - 4}", strk=up, sw=.35, dash="1,.8"); s.arrowhead(90, ROOF - 4, math.degrees(math.atan2(-(F3Y - ROOF + 2), -14)), .9, fill=up)
    s.path(f"M104,{F3Y + 1} L84,{F2Y - 10}", strk=up, sw=.35, dash="1,.8"); s.arrowhead(84, F2Y - 10, math.degrees(math.atan2(F2Y - 10 - F3Y - 1, -20)), .9, fill=up)
    s.text(122, F3Y - 4.4, "balcony opposite\ngallery 304", "plm", "start", 2.3, fill=up)
    # level tags
    for y, t in ((F3Y - 2, "FLOOR 3"), (F2Y - 9, "FLOOR 2"), (F1Y + 5, "FLOOR 1 · the Atrium level")):
        s.text(2.6, y, t, "lvt", "start", 2.3)
    s.text(48, F1Y + 5, "the Hall", "plm", "start", 2.3)
    # the route: from the terrace (floor 1) up a glass lift, the 204 balcony, the walkways/lifts, the 304 balcony, down, the Hall, out
    s.route([(66, F1Y - 2), (72.5, F1Y - 6), (72.5, F2Y + 3)], "main", mid=False)
    s.route([(76, F2Y - 1.8), (96, F2Y - 2.6), (112, F2Y - 3.6)], "main", mid=False)
    s.route([(114, F2Y - 6), (102.5, F2Y - 9), (102.5, F3Y + 4)], "main", mid=False)
    s.route([(104, F3Y + 4), (108, F3Y + 1.8)], "main", mid=False, end=False)
    s.route([(64.5, F3Y + 2), (64.5, F1Y - 4), (56, F1Y - 3)], "unc", mid=True, minlen=20)
    s.route([(48, F1Y - 3), (40, F1Y - 10)], "unc", mid=False)
    # dots
    s.note(66, F1Y - 2, f"from the terrace · {N_TERR}", "up", 87, F1Y + 9, 2.4)
    s.dots(116, F2Y - 6.4, [N_204], rad=2.6)
    s.dots(96, F2Y - 12.2, [N_LIFTS], rad=2.6)
    s.dots(112, F3Y - 6.4, [N_304], rad=2.6)
    s.dots(64.5, F2Y + 10, [N_DOWN], rad=2.6)
    s.dots(52, F1Y - 6.6, [N_HALL], rad=2.4)
    s.dots(22, F2Y + 19.5, [N_OUT], rad=2.6)
    s.text(4, F1Y + 13, f"OUT ({N_OUT}): the way out is to be confirmed;\nfollow the signs (plaza or river side)", "plm", "start", 2.3)
    s.text(181.5, 125.4, "SCHEMATIC SECTION · NOT TO SCALE", "scl", "end", 2.3)
    return s.done()

UP_NS = [n for n in NUMS if N_204 <= n <= N_OUT]
upextra = f'''<div class="boxes">
 <div class="box"><h3>Serra from above ({N_204})</h3><p>From the terrace, go back into the Atrium and take a glass lift or the stairs to the second floor. The balcony opposite gallery 204 looks down into gallery 104 and all eight sculptures. Highlights: a look from here on the way up, with no track. If the balcony is closed, go on up.</p></div>
 <div class="box"><h3>Up to the flower ({N_LIFTS}, {N_304})</h3><p>Start {N_LIFTS} in a glass lift as the doors close, or on the curved walkways and stairs. On the third floor, the balcony opposite gallery 304 looks out over the Atrium to the great metal-flower skylight. The galleries around are not stops.</p></div>
 <div class="box"><h3>Down and out ({N_DOWN}, {N_HALL}, {N_OUT})</h3><p>Play {N_DOWN} on the way down to the Hall by a lift or the stairs; Extra {N_HALL} in the Hall. Then leave and play {N_OUT} as you go: it tells you the way to the river walk. Which door visitors leave by is still to be checked on site.</p></div>
</div>'''
pages.append(map_page("FLOORS 2 AND 3", f"Up and down · {UP_NS[0]} to {UP_NS[-1]}",
    f"A cut through the building: the plaza is level with floor 2, the Hall and the Atrium are on floor 1. Up a glass lift to the balcony opposite gallery 204, over Serra ({N_204}); "
    f"the lifts and walkways ({N_LIFTS}); the balcony opposite gallery 304, under the metal flower ({N_304}); down again ({N_DOWN}, Extra {N_HALL}) and out ({N_OUT}).",
    f'<div class="plan">{upper_svg()}{LEGEND}</div>', UP_NS, upextra))

# ---------------------------------------------------------------- page 4: the river walk (021–029)
def river_svg():
    H = 110
    s = Svg(184, H); rw = stroke("The river walk")
    water(s, 0, 0, 184, 30, 6)
    s.text(4, 7, "THE RIVER · the Nervión", "lvt", "start", 2.5, fill="#3E6474")
    s.add(f'<text x="4" y="12" class="scl" style="text-anchor:start">SCHEMATIC · NOT TO SCALE</text>')
    s.rect(0, 30, 184, 41, PAVE, "none"); s.path("M0,30 L184,30", strk=WATER_D, sw=.45)
    s.text(44, 40.2, "RIVER WALK", "lvt", "start", 2.3)
    s.rect(0, 41, 184, H, GRASS, "none")
    # the footbridge by Maman (not named) [O14]
    s.rect(97, 0, 104, 30, "#E9E1D2", "#8F8473", .3, dash=DASH)
    s.text(106, 5, "footbridge", "pls", "start", 2.3)
    # the building on the river side: titanium, limestone, glass
    s.path(f"M0,82 C20,78 40,80 60,84 L64,92 L100,90 C112,84 126,80 140,80 L184,80 L184,{H} L0,{H} Z", fill=TI, strk=TI_D, sw=.45)
    for x in range(8, 180, 9):
        s.path(f"M{x},{99} q3,-4 7,-1", strk="#B3BAC0", sw=.3)
    s.text(122, 104.6, "THE MUSEUM · river side", "lvt", "middle", 2.6, fill="#59626A")
    # the terrace, off the Atrium, above the pond [O7]
    s.rect(62, 78, 96, 90, "#F2EEE6", "#6E665B", .4, dash=DASH, rx=1.2)
    chillida(s, 70, 84, .9); chillida(s, 76, 83.4, .9)
    s.text(88, 85, "terrace", "plm", "middle", 2.4)
    s.text(79, 94.4, "(inside: page 2)", "pls", "middle", 2.0)
    # the pond, between the walk and the building [O13]: Kapoor, the fog, the fire
    s.rect(14, 45, 112, 74, WATER, WATER_D, .45, dash=DASH, rx=4)
    kapoor(s, 36, 58, 1.5)
    s.text(36, 69, "Tall Tree & the Eye", "plm", "middle", 2.4)
    for (x, y, r) in [(60, 52, 5), (67, 55, 6), (75, 51, 4.6), (84, 56, 5.4)]:
        s.circle(x, y, r, "#FFFFFF", "none", op=.6)
    s.text(72, 54, "fog · on the hour", "pl", "middle", 2.5)
    s.text(72, 57.4, "for about eight minutes", "pls", "middle", 2.1)
    for i in range(5):
        x = 66 + i * 5; s.path(f"M{x},{68} c-1.4,-1.6 -.4,-3.2 .6,-4 c0,1.4 1.4,1.6 1.2,3 c-.2,.8 -1,1.2 -1.8,1 Z", fill="#E0782F", strk="#B4561C", sw=.2)
    s.text(91, 66.4, "five fire\nfountains ·\nin the evening", "pl", "start", 2.3)
    s.text(60, 48.8, "the pond", "plb", "middle", 2.8)
    # Maman, by the footbridge [O14]
    maman(s, 112, 36, 1.4)
    s.text(112, 25.6, "Maman", "plb", "middle", 2.8)
    # the titanium close to the path [O15]
    s.rect(118, 74, 138, 82, "#fff", TI_D, .35, dash=DASH, rx=1)
    s.text(128, 79, "titanium", "plm", "middle", 2.3)
    # La Salve Bridge crossing over the end of the museum; the tower; Buren's red arches
    s.path(f"M148,{H} L150,0 L164,0 L162,{H} Z", fill="#D8D2C6", strk="#6E665B", sw=.45, fop=.92)
    s.text(157.4, 62, "La Salve Bridge", "plb", "middle", 2.7, rot=-90)
    s.rect(167, 58, 179, 74, "#C9CED3", TI_D, .45, rx=1)
    s.text(173, 77.6, "the tower", "plm", "middle", 2.4)
    s.path("M149.4,22 C151,15 163,15 164.4,22", strk=RED, sw=1.2)
    s.path("M149.6,22 L164.4,22", strk=RED, sw=.6)
    s.text(167, 19, "red arches", "plm", "start", 2.4, fill=RED)
    s.text(167, 22.4, "on the bridge", "pls", "start", 2.1)
    # the route: from the plaza (stairs on the side away from the bridge, O12) along the water toward the bridge
    s.route([(6, 72), (6, 36), (12, 36)], "unc", mid=True, minlen=20)
    s.route([(12, 36), (100, 36), (144, 36)], "main", mid=True, minlen=30)
    s.route([(124, 36), (124, 73)], "unc", mid=False)
    # dots
    s.dots(6, 58, [N_OUT], rad=2.6)
    s.dots(26, 36, POND, rad=2.6)
    s.dots(107, 45, [N_MAMAN], rad=2.6)
    s.dots(129.6, 69, [N_TI], rad=2.6)
    s.dots(132, 36, [N_SALVE], rad=2.6)
    s.dots(82, 36, [N_RWX], rad=2.4)
    s.text(82, 41.2, "anywhere", "pls", "middle", 2.0)
    s.dots(141, 36, [N_CLOSE], rad=2.6)
    s.note(6, 72, "from the plaza: the stairs down toward the park\nand the river walk, on the side away from the bridge", "info", 40, 101, 2.3)
    s.note(142.5, 38.6, "END · near the bridge", "finish", 134, 52, 2.3)
    return s.done()

RW_NS = [N_OUT] + [n for n in sec_ns("The river walk") if n != N_OUT]
rwextra = f'''<div class="boxes">
 <div class="box"><h3>The pond ({lst(POND)})</h3><p>Walk along the water toward the big road bridge to the pond beside the building, with the tall tree of silver balls in it. The fog rises from this water on the hour, for about eight minutes. The five fire fountains, in the same pond, burn only in the evening.</p></div>
 <div class="box"><h3>Maman and the titanium ({N_MAMAN}, {N_TI})</h3><p>Maman stands by the footbridge, toward the bridge: stay on the path around her. Then find a spot where the titanium skin comes close to the path, ideally with limestone and glass in the same view. Look, don't touch.</p></div>
 <div class="box"><h3>The bridge, the end ({N_SALVE}, {N_RWX}, {N_CLOSE})</h3><p>Stop where La Salve Bridge, the tall tower beside it and the red frame on the bridge are all in view. Extra {N_RWX} plays anywhere on the river walk. The last stop: a quiet place near the bridge, with the museum beside you.</p></div>
</div>'''
pages.append(map_page("THE RIVER WALK", f"The river walk · {RW_NS[0]} to {RW_NS[-1]}",
    f"Out and round to the river ({N_OUT}), then along the water toward the bridge: the pond with Kapoor's tree, the fog and the fire ({lst(POND)}), Maman by the footbridge ({N_MAMAN}), "
    f"the titanium up close ({N_TI}), La Salve Bridge with the tower and Buren's red arches ({N_SALVE}), and the end by the bridge ({N_CLOSE}). The order of the pond and Maman is still to be checked on site.",
    f'<div class="plan">{river_svg()}{LEGEND}</div>', RW_NS, rwextra))

# ---------------------------------------------------------------- page 5: the stop table
rows = []; last_sec = None
for n in NUMS:
    s_ = TR[n]["section"]
    if s_ != last_sec: rows.append(("sec", s_)); last_sec = s_
    rows.append(("stop", n))
trs = []
for kind, v in rows:
    if kind == "sec":
        c = SECS.get(v, ("", INK))[1]
        trs.append(f'<tr class="sh"><td colspan="7" style="color:{c};border-bottom-color:{c}">{esc(SECS.get(v, (v,))[0])}</td></tr>')
    else:
        n = v; t = TR[n]; x = ' class="x"' if n in XS else ''
        ty = f'<i style="color:{colour(n)}">Extra</i>' if n in XS else 'main'
        mk = lambda on: '<span class="mk">●</span>' if on else '<span class="no">·</span>'
        trs.append(f'<tr{x}><td>{dot(n)}</td><td class="tt">{esc(t["title"])}</td><td class="pc">{esc(t["room"])}</td><td class="ty">{ty}</td>'
                   f'<td>{mk(n in F_SET)}</td><td>{mk(n in E_SET)}</td><td>{mk(n in H_SET)}</td></tr>')
trs.append(f'<tr class="tot"><td colspan="4">Tracks · visit time, walking and lifts included</td>'
           f'<td>{len(F_SET)}<br><span>{LENGTHS[0][2].replace("about ", "≈ ")}</span></td><td>{len(E_SET)}<br><span>{LENGTHS[1][2].replace("about ", "≈ ")}</span></td><td>{len(H_SET)}<br><span>{LENGTHS[2][2].replace("about ", "≈ ")}</span></td></tr>')
head = '<tr class="th"><th>#</th><th>Title</th><th>Where to play it</th><th>Type</th><th>Full</th><th>Essen&shy;tial</th><th>High&shy;lights</th></tr>'
pages.append(f'''<section class="page">
 <header class="fh"><div class="brand">YO TOURS · GUGGENHEIM BILBAO · ALL STOPS</div>
 <h2>The stops</h2>
 <p class="sub">Every track in walking order: # on your player, the title, where to play it, main stop or Extra, and the lengths it belongs to (Full, {LENGTHS[0][2]}; Essential, {LENGTHS[1][2]}; Highlights, {LENGTHS[2][2]}; walking included). Hollow circles are Extras, on the Full tour only.</p></header>
 <table class="tbl">{head}{"".join(trs)}</table>
 <footer>{esc(FOOTER)}</footer>
</section>''')

CSS = f'''
@page {{ size: A4; margin: 0 }}
* {{ box-sizing: border-box }}
html, body {{ margin: 0; background: {PAPER}; color: {INK}; font-family: Inter, "DejaVu Sans", sans-serif }}
.page {{ width: 210mm; height: 297mm; padding: 12mm 13mm 10mm; position: relative; page-break-after: always; overflow: hidden; background: {PAPER} }}
.brand {{ font: 600 7.6pt Inter; letter-spacing: .28em; color: {GOLD} }}
h1 {{ font: 700 25pt Lora, serif; margin: 2mm 0 1mm; letter-spacing: -.01em }}
h2 {{ font: 700 19pt Lora, serif; margin: 2mm 0 1.2mm }}
h3 {{ font: 700 10pt Lora, serif; margin: 0 0 1mm }}
.lede {{ font: 400 10.6pt Lora, serif; color: {MUTED}; margin: 0 0 3mm; line-height: 1.35 }}
.sub {{ font: 400 8.9pt Inter; color: {MUTED}; margin: 0 0 2.6mm; max-width: 184mm; line-height: 1.4 }}
.how {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 3mm; margin-bottom: 2.6mm }}
.how div {{ background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; padding: 2.2mm 2.8mm; font: 500 7.9pt Inter; line-height: 1.34 }}
.how b {{ display: inline-flex; width: 5mm; height: 5mm; border-radius: 50%; background: {INK}; color: #fff; font: 700 7.5pt Inter; align-items: center; justify-content: center; margin-right: 1.2mm }}
.how strong {{ color: {RED} }}
.ov {{ background: #FDFBF7; border: .3mm solid {LINE}; border-radius: 4mm; padding: 1.5mm 1mm; margin-bottom: 2.6mm }}
.ov > svg, .plan > svg {{ display: block; margin: 0 auto; width: 100%; height: auto }}
.keys {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1mm 3mm; padding: 1.4mm 4mm 0; font: 500 6.9pt Inter; color: {INK} }}
.keys span {{ display: flex; align-items: flex-start; gap: 1.6mm }} .keys em {{ font-style: normal; line-height: 1.25 }} .keys b {{ color: {MUTED}; font-weight: 600; white-space: nowrap }}
.keys i {{ width: 3mm; height: 3mm; border-radius: 50%; flex: none; margin-top: .2mm }}
.warn {{ background: #fff; border: .3mm solid {GOLD}; border-left: 1.6mm solid {GOLD}; border-radius: 2.4mm; padding: 2mm 3mm; font: 400 8pt Inter; line-height: 1.36; margin-bottom: 3mm }}
.cards {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.4mm; margin-bottom: 2.6mm }}
.card {{ background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; padding: 2mm 2.4mm }}
.ch {{ display: grid; grid-template-columns: 9mm 1fr; align-items: center }}
.cnum {{ width: 7mm; height: 7mm; border-radius: 50%; color: #fff; background: {NAVY}; font: 700 11pt Inter; display: flex; align-items: center; justify-content: center }}
.ct {{ font: 700 10.2pt Lora; margin-bottom: .2mm }} .cs {{ font: 400 7.9pt Inter; color: {MUTED} }} .cs b {{ color: {INK} }}
.cdots {{ display: flex; flex-wrap: wrap; gap: .8mm; margin: 1.6mm 0 1mm }}
.mdot {{ width: 4.6mm; height: 4.6mm; border-radius: 50%; color: #fff; font: 700 6.2pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.cs2 {{ font: 400 7pt Inter; color: {MUTED}; line-height: 1.3 }}
footer {{ position: absolute; left: 13mm; right: 13mm; bottom: 6mm; font: 400 7pt Inter; color: {MUTED}; border-top: .3mm solid {LINE}; padding-top: 1.6mm }}
.plan {{ background: #FDFBF7; border: .3mm solid {LINE}; border-radius: 4mm; padding: 2mm; margin-bottom: 2.6mm }}
.list {{ columns: 2; column-gap: 7mm; margin-bottom: 2.6mm }} .list .row {{ break-inside: avoid }}
.boxes {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.4mm }}
.box {{ background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; padding: 2.2mm 2.8mm }}
.box p {{ font: 400 7.9pt Inter; line-height: 1.36; margin: 0 }} .box.wide {{ grid-column: 1 / -1 }}
.box p.fine {{ font-size: 6.9pt; color: {MUTED}; margin-top: 1mm }}
ol.serra {{ margin: 0; padding: 0; list-style: none; font: 500 7.2pt Inter; line-height: 1.3 }} ol.serra b {{ color: {STEEL}; display: inline-block; width: 3.2mm }}
.sn {{ font-family: Inter; font-weight: 700; fill: #fff; text-anchor: middle }}
.note {{ font-family: Inter; font-weight: 600; fill: #fff }}
.pl, .plb, .plm, .pls, .lvt {{ paint-order: stroke; stroke: #FDFBF7; stroke-width: .6px; stroke-linejoin: round }}
.pl {{ font-family: Inter; font-weight: 700; fill: {INK} }} .plb {{ font-family: Lora; font-weight: 700; fill: {INK} }}
.plm {{ font-family: Inter; font-weight: 600; fill: #4A443C }} .pls {{ font-family: Inter; font-weight: 500; fill: #6F665A }}
.lvt {{ font-family: Inter; font-weight: 800; fill: {INK}; letter-spacing: .2px }}
.scl {{ font: 700 2.3px Inter; fill: #A39886; letter-spacing: .25px; text-anchor: end }}
.legend {{ display: flex; flex-wrap: wrap; gap: 1.2mm 4mm; justify-content: center; padding: 2mm 1mm .4mm; font: 500 7pt Inter; color: {MUTED}; align-items: center }}
.legend > span {{ display: inline-flex; align-items: center; gap: 1.3mm }}
.ldot {{ width: 4.4mm; height: 4.4mm; border-radius: 50%; color: #fff; font: 700 6pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.list .row {{ display: grid; grid-template-columns: 7.5mm 1fr; align-items: center; padding: .55mm 0; border-bottom: .25mm solid {LINE} }}
.dot {{ width: 6mm; height: 6mm; border-radius: 50%; color: #fff; font: 700 7.6pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.hol {{ background: #fff; border: .45mm solid; box-sizing: border-box }}
.row.x .tt {{ color: {MUTED} }} .tt i {{ font-style: normal; font-weight: 700; font-size: 7pt; letter-spacing: .04em; margin-right: 1mm }}
.tt {{ font: 500 7.8pt Inter; line-height: 1.22 }} .list .tt {{ padding-left: 1.6mm }} .tt b {{ font-weight: 700; color: {INK} }}
.tbl {{ width: 100%; border-collapse: collapse; background: #fff; border: .3mm solid {LINE}; border-radius: 3mm }}
.tbl th {{ font: 700 6.6pt Inter; color: {MUTED}; text-align: left; padding: 1.4mm 1.2mm 1.1mm; border-bottom: .35mm solid {INK}; letter-spacing: .04em; text-transform: uppercase }}
.tbl th:nth-child(n+5) {{ text-align: center; width: 12mm }} .tbl th:first-child {{ width: 9mm; padding-left: 2mm }} .tbl th:nth-child(3) {{ width: 70mm }} .tbl th:nth-child(4) {{ width: 11mm }}
.tbl td {{ padding: .42mm 1.2mm; line-height: 1.16; border-bottom: .2mm solid {LINE}; vertical-align: middle }}
.tbl td:first-child {{ padding-left: 2mm }} .tbl td:nth-child(n+5) {{ text-align: center }}
.tbl .dot {{ width: 5mm; height: 5mm; font-size: 6.6pt; vertical-align: middle }}
.tbl .tt {{ font: 700 7.8pt Inter }} .tbl .pc {{ font: 500 7.4pt Inter; color: #4A443C }} .tbl tr.x .tt, .tbl tr.x .pc {{ color: {MUTED} }}
.tbl .ty {{ font: 500 7.2pt Inter; color: {MUTED} }} .tbl .ty i {{ font-style: normal; font-weight: 700 }}
.mk {{ color: {NAVY}; font-size: 8.6pt }} .no {{ color: #C9BFAE }}
.tbl tr.sh td {{ font: 700 7.6pt Inter; padding: 1.5mm 2mm .3mm; border-bottom: .3mm solid; letter-spacing: .02em }}
.tbl tr.tot td {{ font: 700 7.8pt Inter; border-top: .35mm solid {INK}; border-bottom: none; padding: 1.4mm 1.2mm 1.4mm 2mm }} .tbl tr.tot span {{ font-weight: 500; color: {MUTED}; white-space: nowrap }}
'''

def build():
    doc = f'<!doctype html><html><head><meta charset="utf-8"><title>Guggenheim Museum Bilbao · Yo Tours route</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
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
                for i, el in enumerate(await pg.query_selector_all(".page")):
                    await el.screenshot(path=os.path.join(PNG_DIR, f"route_p{i+1}.png"), scale="device")
            await br.close()
    asyncio.run(render())
    if not os.environ.get("RM_KEEP_HTML"): os.remove(hp)
    print(f"stops: {len(NUMS)} tracks ({len(F_SET)} Full, {len(E_SET)} Essential, {len(H_SET)} Highlights, {len(XS)} Extras)")
    print("OK ->", OUT_PDF, len(pages), "pages")

build()
