#!/usr/bin/env python3
"""Yo Tours · Setas de Sevilla (Metropol Parasol) and the Antiquarium — route map, edition 5.1 of 31 Oct 2026 (21 tracks).
A PDF made to be read on a phone: page 1 = the whole visit as a vertical SECTION through the building (level −1 with the
taquilla, the Antiquarium and the lifts; the market at street level; the Plaza Mayor on the market's roof; the
experiences level at about 21 m; the walkways and the Mirador 360º on top), the route and the three lengths; page 2 = the
Antiquarium (002–007, with 006 the two birds, a mosaic hung on a wall whose position is not confirmed); page 3 = the
lifts and the walkways from above (008–015); page 4 = coming down and the Plaza Mayor (016–020), with the Extra 021
"After your visit" as a note (position-free, after the close, Full only: Plaza del Cristo de Burgos and the Alameda de
Hércules, nearby, not drawn); then the stop table. Track numbers in the drawings and texts are derived from the track
files (@room, @section), so a renumbering only needs the track files.
There is NO official visitor plan online (research/VISIT_ROUTE_AND_SPACES_OCT2026.md §2): the printed "plano guía" is
handed out at the taquilla (MAP-1). Everything here is therefore SCHEMATIC, not to scale and not traced from anything.
Drawn as documented (research §1–§3, v5/PLAN.md "The route"): the two accesses lead down to level −1; the taquilla on
−1; the Antiquarium entrance beside it and the lifts (Mirador access) beside that; two lifts inside the concrete trunks,
up to the top; the walkways and the Mirador 360º, the highest point, reached only by steps; the experiences level
inside the parasols (Feeling Sevilla, about 21 m); the way down past the exhibition; the end on the Plaza Mayor, the
raised square on the market's roof; the market at street level. The only views drawn are the three sourced ones: SOUTH
toward the Cathedral and the Giralda, WEST toward the river and the Aljarafe, NORTH toward the Macarena district, about a
kilometre away, direction only (PLAN_V5_1 "Views"; research §4.1; audit row 33; told in 013).
Where PLAN marks a position as provisional (ONSITE items O1–O19) it is drawn with a dashed outline or a dotted line and
the legend says so: the ramp from Calle Imagen (O1), the arrangement of level −1 (O3), the inside of the Antiquarium
(O4), where the lift lets you out (O5/O6), every spot on the walkway and the Mirador steps (O6–O9), the Feeling Sevilla
room (O11), the way down (O12) and the way from the Plaza Mayor to the street (O14).
Stops come from v5/tracks/NNN.perf.txt (@room, @title, @type, @section); lengths from build/static/lengths.json.
Usage (from the guide folder): python3 build/route_map.py <bundle folder> [--png <dir>]
  -> <bundle>/Setas_Audio_Guide_Route.pdf"""
import json, math, os, re, sys, html, asyncio, glob

B = sys.argv[1]
PNG_DIR = sys.argv[sys.argv.index("--png") + 1] if "--png" in sys.argv else None
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
TRACKS = os.path.join(ROOT, "v5", "tracks")
LENGTHS_JSON = os.path.join(HERE, "static", "lengths.json")
OUT_PDF = os.path.join(B, "Setas_Audio_Guide_Route.pdf")
FOOTER = "Yo Tours · Setas de Sevilla and Antiquarium audio guide · edition 5.1 · 31 Oct 2026 · schematic plan, not to scale"
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
    TR[n] = dict(type=ttype, room=h.get("room", "").strip(), title=t, words=w, section=h.get("section", ""), extra=extra)
if not TR: sys.exit("no track files in " + TRACKS)
NUMS = sorted(TR)
XS = {n for n in NUMS if TR[n]["extra"]}
MID = {"W": 300, "R": 230, "X": 190, "ANCHOR": 320, "CLOSE": 320}
def minutes(n):
    t = TR[n]; w = t["words"] if t["words"] > 40 else MID.get(t["type"], 230)
    return w / 125.0
def fmt_min(m):
    h = round(m * 2) / 2; whole = int(h)
    return f"{whole}½" if h - whole else f"{whole}"

# ---------------------------------------------------------------- the three lengths (visit times as spoken in 001: walking and lifts included, the film not)
J = json.load(open(LENGTHS_JSON, encoding="utf-8"))
H_SET = {int(x) for x in J["HIGHLIGHTS"].split()}; E_SET = {int(x) for x in J["ESSENTIAL"].split()}
F_SET = set(NUMS)
FX = len(XS)
LENGTHS = [("Full tour", F_SET, "about 1 h 10", "with the Antiquarium; every main stop and the Extras"),
           ("Essential", E_SET, "about 40 min", "no Antiquarium: from the lifts to the top, down to the plaza"),
           ("Highlights", H_SET, "about 25 min", "the welcome, the timber, the Mirador, the plaza")]

# ---------------------------------------------------------------- palette & sections
PAPER, INK, MUTED, LINE, CTX = "#F6F1E7", "#1F1B17", "#776E62", "#D8CEBD", "#ECE5D7"
RED, GOLD, NAVY = "#C0262D", "#A9812F", "#1D2B4A"
SECS = {  # @section -> (short title, colour, tint)
    "Opening": ("Welcome", "#3D3A36", "#E2DCD0"),
    "Antiquarium": ("The Antiquarium · Full only", "#8A4F2A", "#EFDCCB"),
    "Going up": ("Going up", "#2C5A7E", "#D7E3EE"),
    "Walkways and Mirador": ("Walkways and Mirador", "#A4581B", "#F1D6BC"),
    "Coming down": ("Coming down", "#5B4A8A", "#E3DDF0"),
    "Plaza Mayor": ("Plaza Mayor", "#2E6A52", "#D3E4C4"),
    "After your visit": ("After your visit · Full only", "#55616B", "#DDE2E5"),
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
# the track numbers the texts name, all derived from @room / @section of the track files
N_LIFTS = one(ds("Level −1 · by the lifts"), "the lifts on level −1")
N_LIFT = one(ds("Lift"), "the lift")
N_DIG = one(has("over the dig"), "over the dig")
N_ROMAN = has("Roman houses")
N_BIRDS = one(has("on the wall"), "the two birds")
N_ALMOHAD = one(has("Almohad house"), "the Almohad house")
N_SOUTH = one(ds("Walkway · south"), "the south view")
N_WEST = one(ds("Walkway · west"), "the west view")
N_GLUE = one([n for n in NUMS if TR[n]["room"] == "Walkway"], "the walkway")
N_MIRADOR = one(ds("Mirador"), "the Mirador")
N_TOWARD = one(ds("Walkway · toward"), "toward the way down")
N_AURORA = one(ds("Walkway (anywhere)"), "the walkway Extra")
N_FEEL = one(ds("Feeling Sevilla"), "Feeling Sevilla")
N_DOWN = one(ds("The way down"), "the way down")
PM_NS = sec_ns("Plaza Mayor")
N_UNDER = one(has("under the parasols"), "under the timber")
N_CLOSE = one([n for n in PM_NS if TR[n]["type"] == "CLOSE"], "the close")
AFTER_NS = sec_ns("After your visit")

TIMBER, TIMBER_D, CONC, EARTH = "#EBD3AE", "#B98B52", "#CFCAC1", "#E6DCC8"
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
    def path(self, d, fill="none", strk=INK, sw=.3, dash=None, op=1, extra=""):
        ds_ = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<path d="{d}" fill="{fill}" stroke="{strk}" stroke-width="{sw}" stroke-opacity="{op}"{ds_} stroke-linecap="round" stroke-linejoin="round"{extra}/>')
    def poly(self, pts, **kw): self.path("M" + " L".join(f"{x:.2f},{y:.2f}" for x, y in pts), **kw)
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
        colr = {"start": INK, "finish": INK, "info": MUTED, "warn": GOLD, "ant": stroke("Antiquarium"),
                "view": stroke("Walkways and Mirador")}[kind]
        lines = text.split("\n"); wmax = max(len(l) for l in lines) * fs * .56 + fs * 1.6
        hb = fs * 1.36 * len(lines) + fs * .6
        bx = min(max(tx - wmax / 2, .8), self.W - wmax - .8); by = min(max(ty - hb / 2, .8), self.H - hb - .8)
        if px is not None:
            self.add(f'<line x1="{px:.2f}" y1="{py:.2f}" x2="{bx + wmax / 2:.2f}" y2="{by + hb / 2:.2f}" stroke="{colr}" stroke-width=".35" stroke-dasharray="1,.7"/>')
            self.add(f'<circle cx="{px:.2f}" cy="{py:.2f}" r=".8" fill="{colr}"/>')
        self.add(f'<rect x="{bx:.2f}" y="{by:.2f}" width="{wmax:.2f}" height="{hb:.2f}" rx="{min(hb / 2, 2):.2f}" fill="{colr}"/>')
        for i, l in enumerate(lines):
            self.add(f'<text x="{bx + fs * .8:.2f}" y="{by + fs * 1.2 + i * fs * 1.36:.2f}" class="note" style="font-size:{fs:.2f}px">{esc(l)}</text>')
    def tag(self, x, y, t, fs=2.3):
        self.add(f'<text x="{x:.2f}" y="{y:.2f}" class="scl" style="font-size:{fs}px;text-anchor:start">{esc(t)}</text>')
    def done(self): return "".join(self.o) + "</svg>"

def stairs(s, x0, y0, x1, y1, n, colr=INK, sw=.35, dash=None):
    """A little flight of steps from (x0, y0) to (x1, y1)."""
    pts = [(x0, y0)]; dx, dy = (x1 - x0) / n, (y1 - y0) / n
    for i in range(n):
        x, y = pts[-1]; pts += [(x, y + dy), (x + dx, y + dy)]
    s.poly(pts, strk=colr, sw=sw, dash=dash)

def cap(cx, top, hw, by, stem=None):
    """A parasol seen in section: a dome on a tapering stem (stem = (half width at top, foot y, half width at foot))."""
    x0, x1 = cx - hw, cx + hw
    d = (f"M{x0:.2f},{by:.2f} C{x0:.2f},{top + (by - top) * .15:.2f} {cx - hw * .55:.2f},{top:.2f} {cx:.2f},{top:.2f} "
         f"C{cx + hw * .55:.2f},{top:.2f} {x1:.2f},{top + (by - top) * .15:.2f} {x1:.2f},{by:.2f} ")
    if stem:
        tw, fy, fw = stem
        d += (f"Q{cx + hw * .45:.2f},{by + 1:.2f} {cx + tw:.2f},{by + 3:.2f} L{cx + fw:.2f},{fy:.2f} L{cx - fw:.2f},{fy:.2f} "
              f"L{cx - tw:.2f},{by + 3:.2f} Q{cx - hw * .45:.2f},{by + 1:.2f} {x0:.2f},{by:.2f} Z")
    else:
        d += f"Q{cx:.2f},{by + 2.5:.2f} {x0:.2f},{by:.2f} Z"
    return d

def timber(s, caps, cid):
    """The parasols: overlapping timber caps with a waffle grid inside."""
    ds_ = [cap(*c) for c in caps]
    s.add(f'<defs><clipPath id="{cid}">' + "".join(f'<path d="{d}"/>' for d in ds_) + "</clipPath></defs>")
    for d in ds_: s.path(d, fill=TIMBER, strk=TIMBER_D, sw=.35)
    g = [f'<g clip-path="url(#{cid})" stroke="{TIMBER_D}" stroke-opacity=".35" stroke-width=".22">']
    for x in range(0, int(s.W) + 2, 3): g.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{s.H}"/>')
    for y in range(0, int(s.H) + 2, 3): g.append(f'<line x1="0" y1="{y}" x2="{s.W}" y2="{y}"/>')
    s.add("".join(g) + "</g>")

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

LEGEND = (f'<div class="legend"><span>{dot(8, "ldot")} track</span><span><span class="ldot hol" style="color:{INK};border-color:{INK}">X</span> Extra</span>'
          f'<span><svg width="9mm" height="3mm" viewBox="0 0 9 3"><path d="M.5,1.5 L8.5,1.5" stroke="{INK}" stroke-opacity=".75" stroke-width=".55" stroke-dasharray="1.5,1"/></svg> route, in walking order</span>'
          f'<span><svg width="9mm" height="3mm" viewBox="0 0 9 3"><path d="M.5,1.5 L8.5,1.5" stroke="{INK}" stroke-opacity=".7" stroke-width=".75" stroke-dasharray=".1,1.2" stroke-linecap="round"/></svg> path to be confirmed on site</span>'
          f'<span><svg width="7mm" height="4mm" viewBox="0 0 7 4"><rect x=".5" y=".5" width="6" height="3" fill="#fff" stroke="{INK}" stroke-width=".3" stroke-dasharray="1.1,.7"/></svg> position to be confirmed on site</span>'
          '</div>')

pages = []
def map_page(kicker, title, sub, body, ns, extra=""):
    lst = f'<div class="list">{stop_list(ns)}</div>' if ns else ""
    return f'''<section class="page">
 <header class="fh"><div class="brand">YO TOURS · SETAS DE SEVILLA · {esc(kicker)}</div>
 <h2>{esc(title)}</h2><p class="sub">{sub}</p></header>
 {body}{lst}{extra}
 <footer>{esc(FOOTER)}</footer>
</section>'''

# ---------------------------------------------------------------- page 1: a vertical section through the building
# y: street level 88, level −1 below it, the Plaza Mayor on the market's roof, the parasols above. NOT to scale.
STREET, DECK, M1 = 88, 66, 118
def section_svg():
    s = Svg(184, 128)
    # the ground and level −1
    s.rect(0, STREET, 184, 126, EARTH)
    for i in range(0, 184, 4): s.path(f"M{i},{126} L{i + 3},{123}", strk="#CDBFA4", sw=.25)
    s.rect(24, 94, 182, 121, "#F3ECDF", "#8F8473", .35)                       # level −1 (underground)
    s.path(f"M0,{STREET} L184,{STREET}", strk="#6E665B", sw=.6)
    # the Antiquarium: a large dashed area of remains under the square, its entrance at the lobby end [O3, O4]
    at = stroke("Antiquarium")
    s.rect(72, 97, 179, 119, tint("Antiquarium"), at, .4, dash=DASH, rx=1)
    for x in range(78, 176, 7):                                               # ruins: low wall stubs
        s.rect(x, 114.4, x + 3.6, 116.4, "#D8BFA6", "none")
    # the lobby on −1: taquilla, the Antiquarium entrance, the lifts [O3]
    s.rect(29, 106, 41, 115, "#fff", INK, .3, dash=DASH, rx=.8)
    # the market at street level, the Plaza Mayor on its roof
    s.rect(70, 72, 168, STREET, "#EEE7DA", "#8F8473", .35)
    for x in range(76, 166, 9):                                               # market stalls
        s.path(f"M{x},{STREET - 4.5} L{x + 5},{STREET - 4.5} L{x + 5},{STREET} M{x},{STREET - 4.5} L{x},{STREET}", strk="#B3A796", sw=.3)
    s.rect(44, DECK, 172, 70, "#DCD3C3", "#6E665B", .45)                      # the raised square
    s.rect(44, 70, 47, STREET, "#DCD3C3", "#8F8473", .3); s.rect(168, 70, 171, STREET, "#DCD3C3", "#8F8473", .3)
    # the parasols (timber), the two concrete trunks with the lifts
    timber(s, [(56, 26, 16, 38, (3, DECK, 4)), (86, 20, 18, 37, (2.6, DECK, 3.4)), (118, 11, 21, 37, (3, DECK, 4)),
               (153, 19, 22, 47, (3, DECK, 4))], "tp1")
    s.rect(47.5, 30, 54, 120, CONC, "#8F8473", .35); s.rect(57, 30, 63.5, 120, CONC, "#8F8473", .35)
    for x0 in (47.5, 57):
        s.rect(x0 + 1.4, 33, x0 + 5.1, 118, "#fff", "#8F8473", .25, op=.75)  # lift shaft
    # the experiences level (Feeling Sevilla room, about 21 m): position not known [O11]
    fc = stroke("Coming down")
    s.rect(138, 34.5, 167, 44.5, tint("Coming down"), fc, .4, dash=DASH, rx=1)
    # the Mirador 360º: platform at the highest point, reached by steps [O6, O9]
    wc = stroke("Walkways and Mirador")
    s.rect(110, 7, 126, 10.6, "#F6E3CF", wc, .4, dash=DASH, rx=.6)
    stairs(s, 102, 16.5, 110, 10.6, 4, wc, .4)
    # labels
    s.text(124, 82.4, "Mercado de la Encarnación\nthe market, at street level", "plm", "middle", 2.6)
    s.text(97, 64.2, "Plaza Mayor · the raised square", "plb", "middle", 3.0)
    s.text(152.5, 39.4, "Feeling Sevilla room", "plm", "middle", 2.4)
    s.text(152.5, 42.6, "about 21 m up", "pls", "middle", 2.2)
    s.text(118, 5.2, "Mirador 360º · the highest point", "plb", "middle", 2.9)
    s.text(35, 104.6, "taquilla", "pl", "middle", 2.4)
    s.text(126, 101.6, "Antiquarium · Roman and Moorish remains", "plb", "middle", 2.7, fill=at)
    s.text(126, 105, "own entrance and admission · Full tour only", "pls", "middle", 2.2)
    s.text(55.5, 125, "two lifts, in the concrete trunks", "pls", "middle", 2.1)
    # level tags (left)
    for y, t, sub in ((18, "TOP", "walkways and Mirador,\nclose to 30 m"), (40, "INSIDE", "experiences level,\nabout 21 m"),
                      (DECK + 2.5, "PLAZA MAYOR", "on the market's roof"), (STREET - 7.6, "STREET", "Plaza de la\nEncarnación"),
                      (100, "LEVEL −1", "under the street")):
        s.text(2.6, y, t, "lvt", "start", 2.3); s.text(2.6, y + 2.9, sub, "pls", "start", 2.05)
    # the route
    s.route([(22, STREET - 1), (25, 98), (29, 108)], "unc", mid=False)                     # ramp beside the escalators [O1]
    s.route([(41, 110.5), (72, 110.5), (79, 110.5)], "unc", mid=False)                     # into the Antiquarium [O3, O4]
    s.route([(92, 110.5), (174, 110.5), (174, 117.4), (66, 117.4)], "unc", mid=True, minlen=40)  # its walkway, out, to the lifts [O4]
    s.route([(60.3, 116), (60.3, 33)], "main", minlen=20)                                 # the lift, up to the top
    s.route([(64, 27), (78, 17), (98, 15.5)], "unc", mid=True, end=True)                   # the walkway [O6]
    s.route([(130, 14.5), (140, 17), (150, 17.5), (168, 22)], "unc", mid=False, end=False)
    s.route([(168, 22), (171, 30), (167, 34.5)], "unc", mid=False)                         # toward the film room [O11]
    s.route([(165, 44.5), (166, 54), (160, DECK - 1)], "unc", mid=False)                   # the way down [O12]
    s.route([(155, DECK - 3), (176, DECK - 3), (180, 72), (180, STREET - 1)], "unc", mid=False)  # out to the street [O14]
    stairs(s, 163.5, 47, 159.5, DECK - 1.2, 7, fc, .35, dash=None)
    # dots
    s.dots(22, 81.5, [1], rad=2.6)
    s.dots(86, 110.5, sec_ns("Antiquarium"), "r", rad=2.6)
    s.dots(67, 110.5, ds("Level −1 · by the lifts"), rad=2.6)
    s.dots(67, 34, ds("Lift"), rad=2.6)
    walk = [n for n in sec_ns("Walkways and Mirador") if n not in ds("Mirador")]
    pre = [n for n in walk if n < min(ds("Mirador"))]; post = [n for n in walk if n > min(ds("Mirador"))]
    s.dots(76.5, 22.5, pre, "r", rad=2.6)
    s.dots(118, 15.2, ds("Mirador"), rad=2.6)
    s.dots(135, 22, post, "r", rad=2.6)
    s.dots(176.5, 28, ds("Feeling Sevilla"), rad=2.6)
    s.dots(170, 51, ds("The way down"), rad=2.6)
    s.dots(142, 61.6, sec_ns("Plaza Mayor"), "r", rad=2.6)
    s.dots(175.4, 84.6, AFTER_NS, rad=2.6)                                  # after the visit, anywhere: not a place
    # callouts
    s.note(22, 78.6, "IN · Calle Imagen entrance\n(or the north entrance)", "start", 24, 56.5, 2.4)
    s.note(180, 80, "OUT · to the street", "finish", 160, 77.6, 2.4)
    s.text(181.5, 125, "SCHEMATIC SECTION · NOT TO SCALE", "scl", "end", 2.3)
    return s.done()

KEYS = "".join(f'<span><i style="background:{SECS[k][1]}"></i><em>{esc(SECS[k][0])} <b>{rng(k)}</b></em></span>' for k in SECS if rng(k))
def len_card(i, name, ns, when, desc):
    ds_ = "".join(dot(n, "mdot") for n in sorted(ns))
    return (f'<div class="card"><div class="ch"><div class="cnum">{i}</div><div><div class="ct">{esc(name)}</div>'
            f'<div class="cs"><b>{esc(when)}</b> · {len(ns)} tracks</div></div></div>'
            f'<div class="cdots">{ds_}</div><div class="cs2">{esc(desc)}</div></div>')
lens = "".join(len_card(i, n, ns, m, d) for i, (n, ns, m, d) in enumerate(LENGTHS, 1))
after_line = (f" Extra {lst(AFTER_NS)} is for after your visit, anywhere: play it once you have left." if AFTER_NS else "")
pages.append(f'''<section class="page">
 <header><div class="brand">YO TOURS · AUDIO GUIDE</div><h1>Setas de Sevilla and the Antiquarium</h1>
 <p class="lede">One building in four layers, from Roman Seville under the street to the walkways on top: {len(F_SET) - FX} main stops plus {FX} short Extras in one walking order, in three lengths.</p></header>
 <div class="how"><div><b>1</b> <strong>Bottom, top, then the middle.</strong> Down to level −1, up by lift to the walkways and the Mirador 360º, and down again to the Plaza Mayor, where the visit ends.</div>
 <div><b>2</b> The coloured circle is the track to play there, in track order. Hollow circles are short, optional Extras, on the Full tour only. Pages 2 to 4 show every track in its place.</div>
 <div><b>3</b> Each track ends by telling you where to go next. This is a schematic section, not to scale. <strong>Dashed and dotted: not yet confirmed on site.</strong></div></div>
 <div class="ov">{section_svg()}<div class="keys">{KEYS}</div>{LEGEND}</div>
 <div class="cards">{lens}</div>
 <div class="warn"><b>Shorter tours skip the Antiquarium:</b> after the taquilla, go to the lifts beside its entrance. It is a separate museum with its own entrance and admission; if it is closed, the Full tour carries on at the lifts with {N_LIFTS}.{after_line} Times include walking and the lifts, not the Feeling Sevilla film.</div>
 <footer>{esc(FOOTER)}</footer>
</section>''')

# ---------------------------------------------------------------- page 2: the Antiquarium (002–007)
def antiq_svg():
    """A schematic plan of the Antiquarium on level −1 (stops in order along its walkway) and a cut through the ground."""
    s = Svg(184, 136); at, att = stroke("Antiquarium"), tint("Antiquarium")
    s.rect(0, 0, 184, 136, "#F3ECDF")
    s.text(3, 6, "LEVEL −1 · UNDER THE PLAZA DE LA ENCARNACIÓN · SEEN FROM ABOVE", "lvt", "start", 2.4)
    # the lobby: taquilla, the Antiquarium entrance beside it, the lifts beside that [O3]
    s.rect(3, 12, 33, 92, "#FBF7F0", "#8F8473", .35, rx=1)
    s.rect(7, 18, 29, 36, CONC, "#8F8473", .35, dash=DASH, rx=.8)
    s.text(18, 26.4, "lifts", "pl", "middle", 2.8); s.text(18, 30.4, "Mirador access", "pls", "middle", 2.2)
    s.rect(7, 74, 29, 86, "#fff", INK, .3, dash=DASH, rx=.8); s.text(18, 81.2, "taquilla", "pl", "middle", 2.8)
    # the museum hall over the remains [O4]
    s.rect(37, 12, 181, 92, att, at, .45, dash=DASH, rx=1.5)
    s.path("M37,52 L37,62", strk="#FBF7F0", sw=1.4); s.path("M35.5,52 L38.5,52 M35.5,62 L38.5,62", strk=at, sw=.5)
    s.text(39, 50, "entrance", "plm", "start", 2.4)
    zones = [((42, 64, 66, 88), "entrance"), ((62, 16, 94, 44), "over the dig"), ((98, 46, 146, 88), "Roman houses"),
             ((150, 54, 178, 88), "on a wall"), ((146, 16, 178, 46), "Almohad house")]
    for (x0, y0, x1, y1), lab in zones:
        s.rect(x0, y0, x1, y1, "#F7E9DA", at, .3, dash=".9,.7", rx=2.5, op=.8)
    # remains: low walls (schematic, not the real plan)
    for (x0, y0, x1, y1) in ((101, 50, 120, 66), (124, 52, 143, 70), (106, 70, 126, 85), (130, 73, 143, 85), (150, 20, 174, 42)):
        s.rect(x0, y0, x1, y1, "none", "#B9926D", .5)
        s.path(f"M{(x0 + x1) / 2:.1f},{y0} L{(x0 + x1) / 2:.1f},{y0 + (y1 - y0) * .55:.1f} M{x0},{y0 + (y1 - y0) * .6:.1f} L{x0 + (x1 - x0) * .4:.1f},{y0 + (y1 - y0) * .6:.1f}", strk="#B9926D", sw=.45)
    s.rect(66, 22, 90, 40, "#C9A27A", "#9C7650", .4, op=.6)                  # the dig
    s.rect(70, 26, 86, 36, "#B98E62", "none", op=.7)
    # the two birds: a mosaic hung upright on a wall; where it hangs is not known [O4]
    s.rect(156, 59, 172, 61.2, "#B9926D", "none")                              # a wall, seen from above
    s.rect(160, 61.2, 168, 62.4, "#fff", at, .3, dash=".8,.5")                # the mosaic on it
    # the walkway (dotted: the way through is to be confirmed on site)
    s.route([(37, 57), (46, 66), (56, 64), (64, 46), (74, 44), (92, 50), (112, 52), (130, 70), (150, 67), (164, 67), (174, 60), (176, 48), (176, 14)],
            "unc", mid=True, minlen=11)
    # out, back to the lifts beside the entrance [O4]
    s.route([(176, 14), (176, 9.5), (34.5, 9.5), (31, 14), (29, 22)], "unc", mid=True, minlen=40)
    s.text(118, 14.8, f"out, then back to the lifts beside the entrance · play {N_LIFTS} there", "pls", "middle", 2.3)
    # shorter tours: the taquilla straight to the lifts
    s.route([(18, 74), (18, 37)], "unc", mid=True, minlen=20)
    s.text(16.4, 56, "Essential, Highlights", "pls", "middle", 2.1, rot=-90)
    s.route([(29, 80), (33, 70), (37, 59)], "unc", mid=False)
    s.text(25, 70, "Full", "plm", "middle", 2.2)
    # zone labels and dots
    spots = {"Antiquarium entrance": (54, 76), "over the dig": (78, 31), "Antiquarium, Roman houses": (112, 60),
             "through the Roman houses": (134, 62), "on the wall": (164, 68.6), "Almohad house": (162, 31)}
    for n in sec_ns("Antiquarium"):
        xy = next((v for k, v in spots.items() if k in TR[n]["room"]), None)
        if xy is None: sys.exit(f"route_map: no spot on page 2 for track {n} ({TR[n]['room']})")
        s.dots(*xy, [n], rad=3.0)
    s.text(54, 83.4, "entrance", "plm", "middle", 2.5)
    s.text(78, 19.8, "over the dig", "plm", "middle", 2.5)
    s.text(122, 91, "Roman houses", "plm", "middle", 2.6)
    s.text(162, 19.8, "Almohad house", "plm", "middle", 2.5)
    s.text(164, 79.4, "two birds, on a wall", "plm", "middle", 2.4)
    s.text(164, 82.8, "where: to be confirmed", "pls", "middle", 2.1)
    # a cut through the ground: the layers, as told in the dig track and the Almohad house track
    y0 = 100; s.text(3, y0 + 1, f"A CUT THROUGH THE GROUND · AS TOLD IN {N_DIG} AND {N_ALMOHAD}", "lvt", "start", 2.4)
    bands = [(y0 + 4, y0 + 8, "#EEE7DA", "street level: the market, the Plaza Mayor above", "#4A443C"),
             (y0 + 8, y0 + 13, "#E4D3BD", "convent remains, near the top", "#4A443C"),
             (y0 + 13, y0 + 21, "#D9BE9C", f"Moorish houses, about 3 m down (the Almohad house, {N_ALMOHAD})", "#3C2E22"),
             (y0 + 21, y0 + 33, "#C9A27A", f"Roman Seville, 7 to 9 m below the street (the Roman houses, {lst(N_ROMAN)})", "#2A2018")]
    for a, b, col, lab, fcol in bands:
        s.rect(3, a, 181, b, col); s.text(6, (a + b) / 2 + 1, lab, "pl", "start", 2.4, fill=fcol)
    s.path(f"M3,{y0 + 4} L181,{y0 + 4}", strk="#6E665B", sw=.6)
    s.text(181, 135, "SCHEMATIC · NOT TO SCALE", "scl", "end", 2.3)
    return s.done()

AN_NS = sec_ns("Antiquarium")
abody = f'<div class="plan">{antiq_svg()}{LEGEND}</div>'
aextra = f'''<div class="boxes">
 <div class="box"><h3>Separate museum, Full tour only</h3><p>The Antiquarium has its own entrance and its own admission, beside the taquilla on level −1. Essential and Highlights skip it and go straight to the lifts. If it is closed when you are there, go to the lifts beside its entrance and play {N_LIFTS}.</p></div>
 <div class="box"><h3>Find the label</h3><p>The way through has not been checked on site yet, so the drawing shows only the order. Each track names what to look for: the Casa de la Columna, the Casa de Baco, a mosaic with two birds hung on a wall ({N_BIRDS}: play it where you find it), the casa almohade.</p></div>
 <div class="box"><h3>After {AN_NS[-1]}</h3><p>Follow the exit signs, then go to the lifts beside the Antiquarium entrance, the Mirador access. Play {N_LIFTS} there, before you go up.</p></div>
</div>'''
pages.append(map_page("THE ANTIQUARIUM", f"The Antiquarium · {rng('Antiquarium')}",
    "Below the square, on level −1: the remains found when the city dug for a car park that was never built. Walkways run over the excavation, from the entrance "
    "to the dig, the Roman houses, a mosaic of two birds hung on a wall and the Almohad house. Order as in the guide; the positions inside are still to be checked on site.",
    abody, AN_NS, aextra))

# ---------------------------------------------------------------- page 3: the walkways from above (008–015)
def walk_svg():
    s = Svg(184, 132); wc = stroke("Walkways and Mirador")
    # six parasols seen from above: soft overlapping discs (shape, size and orientation NOT from a plan)
    discs = [(42, 72, 19), (70, 50, 21), (70, 92, 20), (104, 70, 25), (138, 50, 20), (140, 92, 21)]
    s.add('<defs><clipPath id="tp3">' + "".join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in discs) + "</clipPath></defs>")
    for x, y, r in discs: s.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{TIMBER}" stroke="{TIMBER_D}" stroke-width=".35"/>')
    g = [f'<g clip-path="url(#tp3)" stroke="{TIMBER_D}" stroke-opacity=".32" stroke-width=".22">']
    for x in range(0, 184, 3): g.append(f'<line x1="{x}" y1="0" x2="{x}" y2="132"/>')
    for y in range(0, 132, 3): g.append(f'<line x1="0" y1="{y}" x2="184" y2="{y}"/>')
    s.add("".join(g) + "</g>")
    # the Mirador 360º platform, at the highest point, reached by steps [O6, O9]
    s.add(f'<circle cx="104" cy="70" r="8" fill="#F6E3CF" stroke="{wc}" stroke-width=".45" stroke-dasharray="{DASH}"/>')
    stairs(s, 84, 56, 96.5, 64.5, 4, wc, .45)
    # the lifts arrive (concrete trunk) [O5, O6]
    s.add(f'<circle cx="150" cy="102" r="3.4" fill="{CONC}" stroke="#8F8473" stroke-width=".35" stroke-dasharray="{DASH}"/>')
    # the way down [O12]
    s.add(f'<rect x="152" y="58" width="9" height="9" rx="1" fill="{tint("Coming down")}" stroke="{stroke("Coming down")}" stroke-width=".4" stroke-dasharray="{DASH}"/>')
    stairs(s, 153.5, 59.5, 159.5, 65.5, 4, stroke("Coming down"), .35)
    # the walkway (all of it to be confirmed: no map yet), in walking order
    W = [(150, 102), (132, 108), (104, 100)]                               # lift -> first walkway -> the south view
    W2 = [(104, 100), (78, 108), (52, 92), (26, 72)]                        # -> the west view
    W3 = [(26, 72), (34, 50), (52, 38), (70, 33), (84, 40), (84, 56)]      # -> the glue -> the steps
    W5 = [(112, 64), (124, 52), (134, 38), (150, 38), (158, 46), (157, 57)]  # -> love it or hate it -> the way down
    for seg in (W, W2, W3, W5): s.route(seg, "unc", mid=True, minlen=16)
    # the three sourced views, as arrows at the edge (the only directions the guide uses; north: direction only)
    vc = stroke("Walkways and Mirador")
    s.route([(104, 117.5), (104, 130)], "main", mid=False)
    s.note(None, None, "SOUTH · the Cathedral and the Giralda", "view", 136, 125.5, 2.7)
    s.route([(21, 64), (2.5, 64)], "main", mid=False)
    s.text(11, 58.5, "WEST", "lvt", "middle", 3.0, fill=vc)
    s.text(11, 69, "the river\nand the\nAljarafe", "plm", "middle", 2.4, fill=vc)
    s.route([(104, 43.5), (104, 13)], "main", mid=False)
    s.note(None, None, "NORTH · toward the Macarena district", "view", 104, 7.2, 2.5)
    # labels
    s.text(104, 81.2, "Mirador 360º", "plb", "middle", 3.0)
    s.text(104, 84.6, "the highest point", "pls", "middle", 2.3)
    s.text(78, 61.6, "steps", "plm", "end", 2.5)
    s.text(150, 97.4, "lifts", "plm", "middle", 2.4)
    s.text(156.5, 71.6, "the way down\npage 4", "plm", "middle", 2.4)
    s.text(3, 128.6, "the six parasols · outline schematic, not from a plan", "pls", "start", 2.3)
    # dots
    s.dots(134, 114.5, ds("Lift"), rad=2.7)
    s.dots(104, 106, [n for n in ds("Walkway · south")], rad=2.7)
    s.dots(31, 78, ds("Walkway · west"), rad=2.7)
    s.dots(64, 28, [n for n in NUMS if TR[n]["room"] == "Walkway"], rad=2.7)
    s.dots(110, 64, ds("Mirador"), rad=2.7)
    s.dots(128, 37, ds("Walkway · toward"), rad=2.7)
    s.dots(144, 26, ds("Walkway (anywhere)"), rad=2.7)
    s.text(144, 21.4, "anywhere", "pls", "middle", 2.2)
    s.dots(172, 112, ds("Level −1 · by the lifts"), rad=2.7)
    s.text(172, 118.2, "by the lifts,\non level −1,\nbefore going up", "pls", "middle", 2.1)
    s.route([(169, 110), (154, 103.5)], "main", mid=False)
    # compass
    X, Y = 8, 10
    s.add(f'<path d="M{X},{Y - 5} L{X + 2},{Y + 2} L{X},{Y + .8} L{X - 2},{Y + 2} Z" fill="{INK}" fill-opacity=".8"/>'
          f'<text x="{X}" y="{Y + 6}" class="cmp">N</text>')
    s.text(181, 9.6, "SCHEMATIC · NOT TO SCALE", "scl", "end", 2.3)
    return s.done()

WK_NS = ds("Level −1 · by the lifts") + ds("Lift") + sec_ns("Walkways and Mirador")
wextra = f'''<div class="boxes">
 <div class="box"><h3>Only the order is fixed</h3><p>There is no official map of the walkway yet, and nobody has confirmed whether it runs one way. Every spot drawn here is a guess at the order, not the place. Play each track where it says.</p></div>
 <div class="box"><h3>Three views to find</h3><p><b>{N_SOUTH}</b>: wherever the Giralda and the cathedral are in clear view, to the south. <b>{N_WEST}</b>: stand with the Giralda on your left, facing west, toward the river, Triana and the Aljarafe. <b>{N_MIRADOR}</b>, on the Mirador: with the Giralda at your back you face north, toward the Macarena district, about a kilometre away.</p></div>
 <div class="box"><h3>Steps to the top</h3><p>The Mirador 360º, the highest point, is reached only by steps. Some walkway ramps are steep. After {N_MIRADOR}, go back down the steps and on toward the way down.</p></div>
</div>'''
pages.append(map_page("THE WALKWAYS", f"The walkways and the Mirador · {WK_NS[0]} to {WK_NS[-1]}",
    f"Play {N_LIFTS} by the lifts on level −1, and start {N_LIFT} as the lift doors close. On top, walk on until the Giralda is in clear view ({N_SOUTH}), face west toward the river ({N_WEST}), "
    f"walk on toward the steps ({N_GLUE}), climb to the Mirador 360º ({N_MIRADOR}), then back down the steps and on toward the way down ({N_TOWARD}; Extra {N_AURORA} anywhere).",
    f'<div class="plan">{walk_svg()}{LEGEND}</div>', WK_NS, wextra))

# ---------------------------------------------------------------- page 4: coming down and the Plaza Mayor (016–020), and 021 after the visit
def down_svg():
    s = Svg(184, 130); fc, ft = stroke("Coming down"), tint("Coming down")
    st_, dk = 112, 80                      # street level, the Plaza Mayor deck (NOT to scale)
    s.rect(0, st_, 184, 130, EARTH); s.path(f"M0,{st_} L184,{st_}", strk="#6E665B", sw=.6)
    # the market at street level and the Plaza Mayor on its roof
    s.rect(22, dk + 4, 168, st_, "#EEE7DA", "#8F8473", .35)
    for x in range(28, 166, 10):
        s.path(f"M{x},{st_ - 5} L{x + 6},{st_ - 5} L{x + 6},{st_} M{x},{st_ - 5} L{x},{st_}", strk="#B3A796", sw=.3)
    s.text(95, st_ - 10.5, "Mercado de la Encarnación · the market, at street level", "plm", "middle", 2.7)
    s.rect(14, dk, 176, dk + 4, "#DCD3C3", "#6E665B", .45)
    s.rect(14, dk + 4, 17.5, st_, "#DCD3C3", "#8F8473", .3); s.rect(172.5, dk + 4, 176, st_, "#DCD3C3", "#8F8473", .3)
    # the parasols above, the walkway on top
    timber(s, [(30, 24, 26, 42, (3.2, dk, 4.2)), (104, 14, 36, 46, (3.4, dk, 4.4)), (160, 22, 24, 48, None)], "tp4")
    # the experiences level: the Feeling Sevilla room; where it is is not known [O11]
    s.rect(110, 31, 148, 45, ft, fc, .45, dash=DASH, rx=1)
    s.text(129, 35.8, "Feeling Sevilla room", "plm", "middle", 2.6)
    s.text(129, 39.4, "about 21 m up", "pls", "middle", 2.2)
    s.text(129, 42.6, "where: to be confirmed", "pls", "middle", 2.2)
    # the way down past the exhibition panels: stairs, or a lift as well? [O12]
    stairs(s, 150, 47, 160, dk - .4, 8, fc, .5)
    for (x, y) in [(162, 55), (164, 63), (166, 71)]:
        s.rect(x, y - 4.4, x + 3.4, y, "#fff", fc, .3, dash=".8,.5")
    s.text(147, 55, "the way down,\npast the exhibition\n(stairs; a lift too?)", "plm", "end", 2.4)
    # the route: walkway -> (film room) -> the way down -> the Plaza Mayor -> the street
    s.route([(6, 26), (30, 18), (70, 9.5), (104, 7.5), (134, 10), (144, 15)], "unc", mid=True, minlen=24)
    s.route([(162, 17), (170, 24), (170, 36), (159.5, 39)], "unc", mid=False)
    s.route([(160, dk - 2.4), (60, dk - 2.4), (10, dk - 2.4), (6, dk + 6), (6, st_ - 1)], "unc", mid=True, minlen=30)
    # labels
    s.text(68, dk - 9.4, "Plaza Mayor · the raised square", "plb", "middle", 3.3)
    s.text(68, dk - 5.6, "on the market's roof · the visit ends here", "pls", "middle", 2.4)
    s.text(70, 4.6, f"the walkway, from {N_MIRADOR}", "pls", "middle", 2.3)
    s.text(181, 127.4, "SCHEMATIC SECTION · NOT TO SCALE", "scl", "end", 2.3)
    # dots
    s.dots(149, 15, ds("Walkway · toward") + ds("Walkway (anywhere)"), "r", rad=2.7)
    s.dots(156, 39, ds("Feeling Sevilla"), rad=2.7)
    s.dots(173, 62, ds("The way down"), rad=2.7)
    s.dots(136, dk - 8.2, sec_ns("Plaza Mayor"), "r", rad=2.7)
    s.note(6, st_ - 2, "OUT · stairs or escalators to the street", "finish", 40, 121, 2.6)
    # after the visit: an Extra for anywhere, about two places nearby (not drawn: no positions)
    if AFTER_NS:
        s.dots(86, 120.4, AFTER_NS, rad=2.7)
        s.text(90.4, 119.4, "after your visit, anywhere: the fig trees of the Plaza del Cristo de Burgos", "plm", "start", 2.3)
        s.text(90.4, 122.6, "and the Roman columns of the Alameda de Hércules, both nearby", "pls", "start", 2.3)
    return s.done()

DN_NS = sec_ns("Coming down", "Plaza Mayor")
PM_RNG = f"{PM_NS[0]}–{PM_NS[-1]}" if len(PM_NS) > 1 else f"{PM_NS[0]}"
PM_REST = [n for n in PM_NS if n != N_UNDER]
after_box = (f'''<div class="box wide"><h3>After your visit ({lst(AFTER_NS)}, Extra, Full tour)</h3><p>Not a stop on the route: play it anywhere once you have left the Setas, on the street, at a café, or on your way. It is about two places nearby, not drawn here: the Plaza del Cristo de Burgos, with the old fig trees that inspired the design, and the Alameda de Hércules, with its two Roman columns. Any map on your phone will show you the way.</p></div>''' if AFTER_NS else "")
dextra = f'''<div class="boxes">
 <div class="box"><h3>Feeling Sevilla ({N_FEEL})</h3><p>An optional Extra about the film room, on the experiences level inside the parasols. Play it before you go in. Where the room is, and when you reach it, is still to be confirmed on site.</p></div>
 <div class="box"><h3>The way down ({N_DOWN})</h3><p>Play {N_DOWN} as you walk down past the exhibition. At the bottom you come out on the Plaza Mayor, the big raised square under the parasols. Whether there is also a lift down is still to be confirmed.</p></div>
 <div class="box"><h3>The Plaza Mayor ({PM_RNG})</h3><p>Play {N_UNDER} where the way down comes out, with the timber overhead; then {lst(PM_REST)} in a quiet spot, with the market under your feet. To leave, follow the signs down to the street, by the stairs or the escalators. You do not go back to level −1.</p></div>
 {after_box}
</div>'''
after_sub = (f" Extra {lst(AFTER_NS)} is for after your visit, anywhere." if AFTER_NS else "")
pages.append(map_page("COMING DOWN", f"Coming down and the Plaza Mayor · {DN_NS[0]} to {DN_NS[-1]}",
    f"From the walkway, toward the way down. If you watch the Feeling Sevilla film, play Extra {N_FEEL} before you go in. Then the way down past the exhibition ({N_DOWN}), "
    f"and the Plaza Mayor, the raised square on the market's roof, where the visit ends ({lst(PM_NS)}).{after_sub}",
    f'<div class="plan">{down_svg()}{LEGEND}</div>', DN_NS + AFTER_NS, dextra))

# ---------------------------------------------------------------- page 5: the stop table
rows = []; last_sec = None
for n in NUMS:
    s_ = TR[n]["section"]
    if s_ != last_sec: rows.append(("sec", s_)); last_sec = s_
    rows.append(("stop", n))
tot = {k: sum(minutes(n) for n in NUMS if n in S) for k, S in (("F", F_SET), ("E", E_SET), ("H", H_SET))}
trs = []
for kind, v in rows:
    if kind == "sec":
        c = SECS.get(v, ("", INK))[1]
        trs.append(f'<tr class="sh"><td colspan="8" style="color:{c};border-bottom-color:{c}">{esc(SECS.get(v, (v,))[0])}</td></tr>')
    else:
        n = v; t = TR[n]; x = ' class="x"' if n in XS else ''
        ty = f'<i style="color:{colour(n)}">Extra</i>' if n in XS else 'main'
        mk = lambda on: '<span class="mk">●</span>' if on else '<span class="no">·</span>'
        trs.append(f'<tr{x}><td>{dot(n)}</td><td class="pc">{esc(t["room"])}</td><td class="tt">{esc(t["title"])}</td><td class="ty">{ty}</td>'
                   f'<td class="mn">{fmt_min(minutes(n))}</td><td>{mk(n in F_SET)}</td><td>{mk(n in E_SET)}</td><td>{mk(n in H_SET)}</td></tr>')
trs.append(f'<tr class="tot"><td colspan="4">Tracks · listening minutes (walking and the lifts come on top)</td><td class="mn"></td>'
           f'<td>{len(F_SET)}<br><span>{round(tot["F"])}′</span></td><td>{len(E_SET)}<br><span>{round(tot["E"])}′</span></td><td>{len(H_SET)}<br><span>{round(tot["H"])}′</span></td></tr>')
head = '<tr class="th"><th>#</th><th>Where to play it</th><th>Title</th><th>Type</th><th>Min</th><th>Full</th><th>Essen&shy;tial</th><th>High&shy;lights</th></tr>'
pages.append(f'''<section class="page">
 <header class="fh"><div class="brand">YO TOURS · SETAS DE SEVILLA · ALL STOPS</div>
 <h2>The stops</h2>
 <p class="sub">Every track in walking order: # on your player, where to play it, the title, main stop or Extra, minutes of listening, and the lengths it belongs to (Full, {LENGTHS[0][2]}; Essential, {LENGTHS[1][2]}; Highlights, {LENGTHS[2][2]}; walking and lifts included, the Feeling Sevilla film not). Hollow circles are Extras.</p></header>
 <table class="tbl">{head}{"".join(trs)}</table>
 <footer>{esc(FOOTER)}</footer>
</section>''')

CSS = f'''
@page {{ size: A4; margin: 0 }}
* {{ box-sizing: border-box }}
html, body {{ margin: 0; background: {PAPER}; color: {INK}; font-family: Inter, "DejaVu Sans", sans-serif }}
.page {{ width: 210mm; height: 297mm; padding: 13mm 13mm 10mm; position: relative; page-break-after: always; overflow: hidden; background: {PAPER} }}
.brand {{ font: 600 7.6pt Inter; letter-spacing: .28em; color: {GOLD} }}
h1 {{ font: 700 25pt Lora, serif; margin: 2mm 0 1mm; letter-spacing: -.01em }}
h2 {{ font: 700 19pt Lora, serif; margin: 2mm 0 1.2mm }}
h3 {{ font: 700 10pt Lora, serif; margin: 0 0 1mm }}
.lede {{ font: 400 10.6pt Lora, serif; color: {MUTED}; margin: 0 0 3mm; line-height: 1.35 }}
.sub {{ font: 400 8.9pt Inter; color: {MUTED}; margin: 0 0 3mm; max-width: 184mm; line-height: 1.4 }}
.how {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 3mm; margin-bottom: 3mm }}
.how div {{ background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; padding: 2.2mm 2.8mm; font: 500 7.9pt Inter; line-height: 1.34 }}
.how b {{ display: inline-flex; width: 5mm; height: 5mm; border-radius: 50%; background: {INK}; color: #fff; font: 700 7.5pt Inter; align-items: center; justify-content: center; margin-right: 1.2mm }}
.how strong {{ color: {RED} }}
.ov {{ background: #FDFBF7; border: .3mm solid {LINE}; border-radius: 4mm; padding: 1.5mm 1mm; margin-bottom: 3mm }}
.ov > svg, .plan > svg {{ display: block; margin: 0 auto; width: 100%; height: auto }}
.keys {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1mm 3mm; padding: 1.4mm 4mm 0; font: 500 6.9pt Inter; color: {INK} }}
.keys span {{ display: flex; align-items: flex-start; gap: 1.6mm }} .keys em {{ font-style: normal; line-height: 1.25 }} .keys b {{ color: {MUTED}; font-weight: 600; white-space: nowrap }}
.keys i {{ width: 3mm; height: 3mm; border-radius: 50%; flex: none; margin-top: .2mm }}
.warn {{ background: #fff; border: .3mm solid {GOLD}; border-left: 1.6mm solid {GOLD}; border-radius: 2.4mm; padding: 2.2mm 3mm; font: 400 8.2pt Inter; line-height: 1.38; margin-bottom: 3mm }}
.cards {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.4mm; margin-bottom: 3mm }}
.card {{ background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; padding: 2mm 2.4mm }}
.ch {{ display: grid; grid-template-columns: 9mm 1fr; align-items: center }}
.cnum {{ width: 7mm; height: 7mm; border-radius: 50%; color: #fff; background: {NAVY}; font: 700 11pt Inter; display: flex; align-items: center; justify-content: center }}
.ct {{ font: 700 10.2pt Lora; margin-bottom: .2mm }} .cs {{ font: 400 7.9pt Inter; color: {MUTED} }} .cs b {{ color: {INK} }}
.cdots {{ display: flex; flex-wrap: wrap; gap: .8mm; margin: 1.6mm 0 1mm }}
.mdot {{ width: 4.6mm; height: 4.6mm; border-radius: 50%; color: #fff; font: 700 6.2pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.cs2 {{ font: 400 7pt Inter; color: {MUTED}; line-height: 1.3 }}
footer {{ position: absolute; left: 13mm; right: 13mm; bottom: 7mm; font: 400 7pt Inter; color: {MUTED}; border-top: .3mm solid {LINE}; padding-top: 2mm }}
.plan {{ background: #FDFBF7; border: .3mm solid {LINE}; border-radius: 4mm; padding: 2mm; margin-bottom: 3mm }}
.list {{ columns: 2; column-gap: 7mm; margin-bottom: 3mm }} .list .row {{ break-inside: avoid }}
.boxes {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.4mm }}
.box {{ background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; padding: 2.2mm 2.8mm }}
.box p {{ font: 400 8pt Inter; line-height: 1.38; margin: 0 }} .box.wide {{ grid-column: 1 / -1 }}
.sn {{ font-family: Inter; font-weight: 700; fill: #fff; text-anchor: middle }}
.note {{ font-family: Inter; font-weight: 600; fill: #fff }}
.pl, .plb, .plm, .pls, .lvt {{ paint-order: stroke; stroke: #FDFBF7; stroke-width: .6px; stroke-linejoin: round }}
.pl {{ font-family: Inter; font-weight: 700; fill: {INK} }} .plb {{ font-family: Lora; font-weight: 700; fill: {INK} }}
.plm {{ font-family: Inter; font-weight: 600; fill: #4A443C }} .pls {{ font-family: Inter; font-weight: 500; fill: #7A7064 }}
.lvt {{ font-family: Inter; font-weight: 800; fill: {INK}; letter-spacing: .2px }}
.cmp {{ font: 700 2.8px Inter; fill: {INK}; text-anchor: middle }}
.scl {{ font: 700 2.3px Inter; fill: #A39886; letter-spacing: .25px; text-anchor: end }}
.legend {{ display: flex; flex-wrap: wrap; gap: 1.2mm 4mm; justify-content: center; padding: 2mm 1mm .4mm; font: 500 7pt Inter; color: {MUTED}; align-items: center }}
.legend > span {{ display: inline-flex; align-items: center; gap: 1.3mm }}
.ldot {{ width: 4.4mm; height: 4.4mm; border-radius: 50%; color: #fff; font: 700 6pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.list .row {{ display: grid; grid-template-columns: 7.5mm 1fr; align-items: center; padding: .6mm 0; border-bottom: .25mm solid {LINE} }}
.dot {{ width: 6mm; height: 6mm; border-radius: 50%; color: #fff; font: 700 7.6pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.hol {{ background: #fff; border: .45mm solid; box-sizing: border-box }}
.row.x .tt {{ color: {MUTED} }} .tt i {{ font-style: normal; font-weight: 700; font-size: 7pt; letter-spacing: .04em; margin-right: 1mm }}
.tt {{ font: 500 7.8pt Inter; line-height: 1.22 }} .list .tt {{ padding-left: 1.6mm }} .tt b {{ font-weight: 700; color: {INK} }}
.tbl {{ width: 100%; border-collapse: collapse; background: #fff; border: .3mm solid {LINE}; border-radius: 3mm }}
.tbl th {{ font: 700 6.6pt Inter; color: {MUTED}; text-align: left; padding: 1.6mm 1.2mm 1.2mm; border-bottom: .35mm solid {INK}; letter-spacing: .04em; text-transform: uppercase }}
.tbl th:nth-child(n+5) {{ text-align: center; width: 12mm }} .tbl th:first-child {{ width: 9mm; padding-left: 2mm }} .tbl th:nth-child(2) {{ width: 60mm }} .tbl th:nth-child(4) {{ width: 11mm }}
.tbl td {{ padding: .9mm 1.2mm; line-height: 1.2; border-bottom: .2mm solid {LINE}; vertical-align: middle }}
.tbl td:first-child {{ padding-left: 2mm }} .tbl td:nth-child(n+5) {{ text-align: center }}
.tbl .dot {{ width: 5.2mm; height: 5.2mm; font-size: 6.8pt; vertical-align: middle }}
.tbl .pc {{ font: 700 7.8pt Inter }} .tbl .tt {{ font: 500 7.9pt Inter }} .tbl tr.x .tt, .tbl tr.x .pc {{ color: {MUTED} }}
.tbl .ty {{ font: 500 7.2pt Inter; color: {MUTED} }} .tbl .ty i {{ font-style: normal; font-weight: 700 }}
.tbl .mn {{ font: 600 7.6pt Inter; color: {INK} }} .mk {{ color: {NAVY}; font-size: 8.6pt }} .no {{ color: #C9BFAE }}
.tbl tr.sh td {{ font: 700 7.6pt Inter; padding: 1.8mm 2mm .4mm; border-bottom: .3mm solid; letter-spacing: .02em }}
.tbl tr.tot td {{ font: 700 7.8pt Inter; border-top: .35mm solid {INK}; border-bottom: none; padding: 1.6mm 1.2mm 1.6mm 2mm }} .tbl tr.tot span {{ font-weight: 500; color: {MUTED} }}
'''

def build():
    doc = f'<!doctype html><html><head><meta charset="utf-8"><title>Setas de Sevilla · Yo Tours route</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
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
