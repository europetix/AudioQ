#!/usr/bin/env python3
"""Yo Tours · Catedral de Sevilla and the Giralda — route map, edition of 30 Oct 2026.
A PDF made to be read on a phone: page 1 = the whole site with the route, both ways in (Puerta del Lagarto, Puerta del
Príncipe / San Cristóbal), the Giralda first, the way out (Puerta del Perdón) and the three lengths; page 2 = the
Giralda (a schematic elevation, 002–006, and 007 at its foot); page 3 = the loop inside the church (007–024); page 4 =
the Patio de los Naranjos and the way out (024–028); then the stop table.
There is NO official visitor plan (research/VISIT_ROUTE_AND_SPACES_OCT2026.md §3). The plan is therefore a SCHEMATIC
drawing of well-documented features only, not to scale and not traced from anything: the rectangular five-aisled
church, W–E, with the high altar at the east; Capilla Mayor and Coro facing each other across the crossing in the
central nave; the transept doors (Concepción north, onto the Patio; Príncipe / San Cristóbal south); the Capilla Real
at the head; the sacristies and chapter house in the SE block; the Giralda at the NE corner; the Patio de los Naranjos
on the north side with the Nave del Lagarto (east gallery), the Perdón (north side) and the Sagrario (west).
Where v5/PLAN.md marks a position as provisional (ONSITE items O1–O18), it is drawn with a dashed outline or a dotted
line and the legend says so: San Antonio along the north aisle (O9), the Antigua (O11), Columbus's tomb (O12), the
Capilla de los Dolores and every room of the SE block (O13), the way from each entrance to the tower door (O1–O3).
Stops come from v5/tracks/NNN.perf.txt (@room, @title, @type, @section); lengths from build/static/lengths.json.
Usage (from the guide folder): python3 build/route_map.py <bundle folder> [--png <dir>]
  -> <bundle>/Cathedral_Audio_Guide_Route.pdf"""
import json, math, os, re, sys, html, asyncio, glob

B = sys.argv[1]
PNG_DIR = sys.argv[sys.argv.index("--png") + 1] if "--png" in sys.argv else None
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
TRACKS = os.path.join(ROOT, "v5", "tracks")
LENGTHS_JSON = os.path.join(HERE, "static", "lengths.json")
OUT_PDF = os.path.join(B, "Cathedral_Audio_Guide_Route.pdf")
FOOTER = "Yo Tours · Seville Cathedral and Giralda audio guide · 30 Oct 2026 edition · schematic plan, not to scale"

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

# ---------------------------------------------------------------- the three lengths (visit times: PLAN §3, walking and the Giralda included)
J = json.load(open(LENGTHS_JSON, encoding="utf-8"))
H_SET = {int(x) for x in J["HIGHLIGHTS"].split()}; E_SET = {int(x) for x in J["ESSENTIAL"].split()}
F_SET = set(NUMS)
FX = len(XS)
LENGTHS = [("Full tour", len(F_SET), "just over 1 h 30", f"all {len(F_SET) - FX} main stops and {FX} short Extras, with the Giralda"),
           ("Essential", len(E_SET), "about 1 h 15", "the Giralda, the heart of the church, Columbus, the sacristies"),
           ("Highlights", len(H_SET), "about 45 min", "the Giralda, the Capilla Mayor, Columbus, the Patio")]

# ---------------------------------------------------------------- palette & sections
PAPER, INK, MUTED, LINE, CTX = "#F6F1E7", "#1F1B17", "#776E62", "#D8CEBD", "#ECE5D7"
RED, GOLD, NAVY = "#C0262D", "#A9812F", "#1D2B4A"
SECS = {  # @section -> (short title, colour, tint for the plan)
    "Opening": ("Welcome", "#3D3A36", "#E2DCD0"),
    "La Giralda": ("La Giralda", "#A4581B", "#F1D6BC"),
    "The heart of the cathedral": ("The heart of the cathedral", "#7A3A5E", "#EEDDE6"),
    "Around the naves": ("Around the naves", "#2C5A7E", "#D7E3EE"),
    "Columbus": ("Columbus", "#8C6A2E", "#EFE2C2"),
    "Sacristies and chapter house": ("Sacristies and chapter house", "#5B4A8A", "#E3DDF0"),
    "Royal chapel and the way to the courtyard": ("Royal chapel, to the courtyard", "#A13A30", "#F2D9D3"),
    "Patio de los Naranjos": ("Patio de los Naranjos", "#2E6A52", "#D3E4C4"),
    "Closing": ("The way out", "#3D3A36", "#E2DCD0"),
}
def colour(n): return SECS.get(TR[n]["section"], ("", INK, CTX))[1]
def tint(sec): return SECS[sec][2]
def stroke(sec): return SECS[sec][1]
def esc(s): return html.escape(s, quote=True)

# ---------------------------------------------------------------- the schematic plan, in plan units (x west→east, y north→south)
# Church 120 × 76 (the real one is about 116 × 76 m without the later additions; proportion only, NOT to scale).
CH = (0, 0, 120, 76)
PIER_X = [8, 18, 28, 38, 48, 56, 68, 78, 88, 98, 108]
PIER_Y = [19, 31, 45, 57]
BAND_N, BAND_S = 7, 69                 # side-chapel bands along the north and south walls
TRANSEPT = (56, 68)                    # does not project beyond the rectangle
CORO = (40, 32.5, 54, 43.5)            # west of the crossing, facing the Capilla Mayor (BLDG)
CMAY = (70, 32.5, 84, 43.5)            # east of the crossing, in the central nave (BLDG)
CREAL = (113, 28, 128, 48)             # the head of the church (REN); apse beyond the east wall
GIR = (106, -12, 120, 2)               # NE corner, rising into the SE corner of the Patio
PATIO = (52, -50, 120, 0)              # north side; the Concepción opens onto it, the Perdón in its north side
LAGARTO = (112, -50, 120, -12)         # east gallery, north of the Giralda
SAGR = (16, -36, 52, 0)                # west of the Patio (its west gallery was demolished for it, PLAN 025)
SEB = (76, 76, 126, 102)               # the SE block: sacristies and chapter house (research)
# provisional placements (PLAN ONSITE items) -> dashed outlines
SANT = (18, 0, 28, 7)                  # Capilla de San Antonio, north aisle toward the west end [O9]
ANTIG = (42, 66, 56, 76)               # Capilla de la Antigua, south side west of the Príncipe, the largest there [O11]
COLON = (59, 61, 65, 67)               # Sepulcro de Colón, just inside the Puerta del Príncipe [O12]
DOLOR = (78, 69, 88, 76)               # Capilla de los Dolores, the way into the Cálices (WIKI-ES) [O13]
CALIC = (78, 78, 90, 89)               # Sacristía de los Cálices [O13]
PABEL = (78, 91, 90, 100)              # Sala del Pabellón, position not known [O13]
SMAY = (92, 78, 108, 99)               # Sacristía Mayor [O13]
ANTEC = (110, 78, 114, 99)             # Antecabildo [O13]
SCAP = (119.5, 90, 5.2, 7.5)           # Sala Capitular, oval (cx, cy, rx, ry) [O13]
# doors: (x, y, orientation, half-width)  'h' = in a north/south wall, 'v' = in an east/west wall
DOORS = {"lagarto": (120, -22, "v", 2.2), "perdon": (82, -50, "h", 2.4), "concepcion": (62, 0, "h", 2.2),
         "principe": (62, 76, "h", 2.2), "asuncion": (0, 38, "v", 2.4)}

# the route, in walking order (main line: dashed with arrows); provisional links: dotted
TOWER_DOOR = (108, 6)
MAIN = [TOWER_DOOR, (100, 13), (76, 27), (63, 35), (58, 31), (44, 26), (30, 24), (24, 10), (17, 18), (6, 37),
        (12, 57), (40, 59), (49, 63), (55, 63), (61, 60), (70, 64), (83, 65), (83, 72)]
SE_IN = [(83, 72), (84, 80), (84, 95), (99, 92), (100, 84), (112, 88), (119, 88)]
SE_BACK = [(119, 92), (112, 95), (96, 100), (86, 98), (86, 80), (86, 72)]
MAIN2 = [(86, 72), (100, 62), (108, 52), (111, 38), (104, 22), (72, 14), (62, 3), (62, -6), (72, -20), (90, -24),
         (100, -20), (114, -26), (114, -40), (96, -44), (82, -48), (82, -60)]
APPROACH_L = [(134, -22), (116, -22), (104, -16), (104, 3), TOWER_DOOR]       # O1, O3: path inside not known
APPROACH_P = [(62, 92), (62, 77), (62, 40), (64, 12), (96, 6), TOWER_DOOR]    # PLAN 001 cue: through the crossing

def plan_svg(crop, width_mm, max_h_mm, labels=(), dots=None, notes=(), route=True, approach=True, se_detail=True,
             compass=True, scale_note=True, lab_fs=2.2, rad=1.75, note_fs=2.3):
    """crop = (x0, x1, y0, y1) in plan units. dots: {key: ((x, y), dir, [tracks])}. labels: (x, y, text, anchor, cls)."""
    cx0, cx1, cy0, cy1 = crop; pad = 1.2
    S = min((width_mm - 2 * pad) / (cx1 - cx0), (max_h_mm - 2 * pad) / (cy1 - cy0))
    W = (cx1 - cx0) * S + 2 * pad; H = (cy1 - cy0) * S + 2 * pad
    def P(x, y): return pad + (x - cx0) * S, pad + (y - cy0) * S
    def R(x0, y0, x1, y1, fill, strk, sw, dash=None, rx=0, op=1):
        a, b = P(x0, y0); c, d = P(x1, y1)
        ds = f' stroke-dasharray="{dash}"' if dash else ""
        return (f'<rect x="{a:.2f}" y="{b:.2f}" width="{c - a:.2f}" height="{d - b:.2f}" rx="{rx}" fill="{fill}" fill-opacity="{op}" '
                f'stroke="{strk}" stroke-width="{sw:.2f}"{ds}/>')
    def L(pts, strk, sw, dash=None, op=1, cap="round"):
        d = "M" + " L".join(f"{P(*p)[0]:.2f},{P(*p)[1]:.2f}" for p in pts)
        ds = f' stroke-dasharray="{dash}"' if dash else ""
        return f'<path d="{d}" fill="none" stroke="{strk}" stroke-opacity="{op}" stroke-width="{sw:.2f}"{ds} stroke-linecap="{cap}" stroke-linejoin="round"/>'
    wall = max(.45, min(.8, .55 * S)); thin = max(.18, .2 * S)
    DASH = f"{1.1:.2f},{.7:.2f}"
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.2f} {H:.2f}" width="{W:.2f}mm" height="{H:.2f}mm">',
         f'<defs><clipPath id="c{id(crop)}"><rect x="0" y="0" width="{W:.2f}" height="{H:.2f}" rx="2"/></clipPath></defs>',
         f'<g clip-path="url(#c{id(crop)})"><rect x="0" y="0" width="{W:.2f}" height="{H:.2f}" fill="#FDFBF7"/>']
    # context: the Sagrario (not on the visit)
    o.append(R(*SAGR, CTX, "#B3A796", thin))
    # the Patio de los Naranjos: courtyard, orange trees in a grid, the fountain, the east gallery (Nave del Lagarto)
    o.append(R(*PATIO, "#E6EED8", "#8F8473", wall))
    for gx in range(58, 106, 6):
        for gy in range(-45, -3, 6):
            if GIR[0] - 2 < gx and gy > GIR[1] - 2: continue
            X, Y = P(gx, gy); o.append(f'<circle cx="{X:.2f}" cy="{Y:.2f}" r="{max(.35, .9 * S):.2f}" fill="#9DBF7E"/>')
    X, Y = P(80, -25); o.append(f'<circle cx="{X:.2f}" cy="{Y:.2f}" r="{1.6 * S:.2f}" fill="#AED3E6" stroke="#7FA9BF" stroke-width="{thin:.2f}"/>')
    o.append(R(*LAGARTO, "#EADFC4", "#8F8473", thin))
    # the Perdón: the gate block in the middle of the north side
    o.append(R(78, -53, 86, -50, "#E2D3B5", "#8F8473", thin))
    # the church
    o.append(R(*CH, "#F1EADC", "#6E665B", wall))
    o.append(R(CH[0], CH[1], CH[2], BAND_N, "#E7DECD", "none", 0)); o.append(R(CH[0], BAND_S, CH[2], CH[3], "#E7DECD", "none", 0))
    o.append(R(TRANSEPT[0], 0, TRANSEPT[1], 76, "#F8F3EA", "none", 0))
    for x in PIER_X:
        for (ya, yb) in ((0, BAND_N), (BAND_S, 76)):
            if TRANSEPT[0] < x < TRANSEPT[1]: continue
            o.append(L([(x, ya), (x, yb)], "#B9AD99", thin))
        for y in PIER_Y:
            X, Y = P(x, y); s = max(.5, 1.3 * S)
            o.append(f'<rect x="{X - s / 2:.2f}" y="{Y - s / 2:.2f}" width="{s:.2f}" height="{s:.2f}" fill="#9A8F7E"/>')
    o.append(R(*CH, "none", "#6E665B", wall))
    # Coro and Capilla Mayor
    o.append(R(*CORO, tint("The heart of the cathedral"), stroke("The heart of the cathedral"), thin * 1.6))
    o.append(R(*CMAY, "#F3E2B8", stroke("The heart of the cathedral"), thin * 1.6))
    a, b = P(CMAY[2] - 1.2, CMAY[1] + 1.2); c, d = P(CMAY[2] - .2, CMAY[3] - 1.2)   # the altarpiece, on the east side
    o.append(f'<rect x="{a:.2f}" y="{b:.2f}" width="{c - a:.2f}" height="{d - b:.2f}" fill="{GOLD}"/>')
    # Capilla Real at the head, its apse beyond the east wall; the grille on its west side
    x0, y0, x1, y1 = CREAL; r = (y1 - y0) / 2
    pa = [P(x0, y0), P(x1, y0)]; e = P(x1, y1); s0 = P(x0, y1)
    o.append(f'<path d="M{pa[0][0]:.2f},{pa[0][1]:.2f} L{pa[1][0]:.2f},{pa[1][1]:.2f} A{r * S:.2f},{r * S:.2f} 0 0 1 {e[0]:.2f},{e[1]:.2f} '
             f'L{s0[0]:.2f},{s0[1]:.2f} Z" fill="{tint("Royal chapel and the way to the courtyard")}" stroke="#6E665B" stroke-width="{wall:.2f}"/>')
    o.append(L([(x0, y0 + 3), (x0, y1 - 3)], INK, max(.35, .45 * S)))
    for yy in range(int(y0 + 4), int(y1 - 2), 2):
        o.append(L([(x0 - .7, yy), (x0 + .7, yy)], INK, thin))
    # the SE block (solid outline: research); its rooms (dashed: arrangement to be confirmed on site, O13)
    o.append(R(*SEB, "#EFE6D6", "#6E665B", wall))
    sacc, sact = stroke("Sacristies and chapter house"), tint("Sacristies and chapter house")
    if se_detail:
        for rr in (CALIC, PABEL, SMAY, ANTEC):
            o.append(R(*rr, sact, sacc, thin * 1.5, dash=DASH))
        X, Y = P((SMAY[0] + SMAY[2]) / 2, (SMAY[1] + SMAY[3]) / 2)
        o.append(f'<circle cx="{X:.2f}" cy="{Y - .8 * S:.2f}" r="{5.2 * S:.2f}" fill="none" stroke="{sacc}" stroke-opacity=".45" stroke-width="{thin:.2f}"/>')
    cx_, cy_, rx_, ry_ = SCAP; X, Y = P(cx_, cy_)
    o.append(f'<ellipse cx="{X:.2f}" cy="{Y:.2f}" rx="{rx_ * S:.2f}" ry="{ry_ * S:.2f}" fill="{sact}" stroke="{sacc}" stroke-width="{thin * 1.5:.2f}" stroke-dasharray="{DASH}"/>')
    # provisional chapels and the tomb (dashed)
    o.append(R(*SANT, tint("Around the naves"), stroke("Around the naves"), thin * 1.5, dash=DASH))
    o.append(R(*ANTIG, tint("Around the naves"), stroke("Around the naves"), thin * 1.5, dash=DASH))
    o.append(R(*DOLOR, sact, sacc, thin * 1.5, dash=DASH))
    o.append(R(*COLON, tint("Columbus"), stroke("Columbus"), thin * 1.5, dash=DASH))
    # the Giralda: square tower with its core (the ramps run round it)
    o.append(R(*GIR, tint("La Giralda"), stroke("La Giralda"), wall))
    o.append(R(GIR[0] + 4, GIR[1] + 4, GIR[2] - 4, GIR[3] - 4, "#E3B994", stroke("La Giralda"), thin))
    # doors: a gap in the wall with two jambs
    for k, (x, y, ori, hw) in DOORS.items():
        if ori == "h": seg, j1, j2 = [(x - hw, y), (x + hw, y)], [(x - hw, y - 1), (x - hw, y + 1)], [(x + hw, y - 1), (x + hw, y + 1)]
        else: seg, j1, j2 = [(x, y - hw), (x, y + hw)], [(x - 1, y - hw), (x + 1, y - hw)], [(x - 1, y + hw), (x + 1, y + hw)]
        o.append(L(seg, "#FDFBF7", wall + .25, cap="butt")); o.append(L(j1, "#6E665B", thin * 1.6)); o.append(L(j2, "#6E665B", thin * 1.6))
    # labels (under the route and the dots)
    for x, y, t, anc, cls in labels:
        X, Y = P(x, y); lines = t.split("\n")
        fs = {"pl": lab_fs, "pls": lab_fs * .86, "plb": lab_fs * 1.12, "plm": lab_fs * .86, "zl": lab_fs * 1.25}[cls]
        sp = "".join(f'<tspan x="{X:.2f}" dy="{0 if i == 0 else fs * 1.18:.2f}">{esc(l)}</tspan>' for i, l in enumerate(lines))
        o.append(f'<text x="{X:.2f}" y="{Y:.2f}" class="{cls}" style="font-size:{fs:.2f}px;text-anchor:{anc}">{sp}</text>')
    # route
    def line(pts, kind):
        q = [P(*p) for p in pts]; d = "M" + " L".join(f"{a:.2f},{b:.2f}" for a, b in q)
        if kind == "main":
            o.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-opacity=".7" stroke-width=".5" stroke-dasharray="1.4,.9" stroke-linecap="round" stroke-linejoin="round"/>')
            for (xa, ya), (xb, yb) in zip(q, q[1:]):
                Ln = math.hypot(xb - xa, yb - ya)
                if Ln < 7: continue
                mx, my = (xa + xb) / 2, (ya + yb) / 2; an = math.degrees(math.atan2(yb - ya, xb - xa)); kk = .95
                o.append(f'<path d="M{-kk:.2f},{-kk * .8:.2f} L{kk:.2f},0 L{-kk:.2f},{kk * .8:.2f} Z" fill="{INK}" fill-opacity=".8" transform="translate({mx:.2f},{my:.2f}) rotate({an:.1f})"/>')
        else:
            o.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-opacity=".55" stroke-width=".45" stroke-dasharray=".15,.9" stroke-linecap="round" stroke-linejoin="round"/>')
            (xa, ya), (xb, yb) = q[-2], q[-1]; an = math.degrees(math.atan2(yb - ya, xb - xa)); kk = .8
            o.append(f'<path d="M{-kk:.2f},{-kk * .8:.2f} L{kk:.2f},0 L{-kk:.2f},{kk * .8:.2f} Z" fill="{INK}" fill-opacity=".6" transform="translate({xb:.2f},{yb:.2f}) rotate({an:.1f})"/>')
    if approach:
        line(APPROACH_L, "unc")
        if approach != "lagarto": line(APPROACH_P, "unc")
    if route == "patio":
        line(MAIN2[4:], "main")
    elif route:
        line(MAIN, "main"); line(SE_IN, "unc"); line(SE_BACK, "unc"); line(MAIN2, "main")
    # callouts
    for key, text, kind, dx, dy in notes:
        cx, cy = P(*key)
        colr = {"start": INK, "finish": INK, "info": MUTED, "warn": GOLD, "gir": stroke("La Giralda")}[kind]
        fs = note_fs; lines = text.split("\n"); wmax = max(len(l) for l in lines) * fs * .55 + fs * 1.6
        hb = fs * 1.38 * len(lines) + fs * .62; tx, ty = cx + dx, cy + dy
        bx = min(max(tx - wmax / 2, .8), W - wmax - .8); by = min(max(ty - hb / 2, .8), H - hb - .8)
        o.append(f'<line x1="{cx:.2f}" y1="{cy:.2f}" x2="{bx + wmax / 2:.2f}" y2="{by + hb / 2:.2f}" stroke="{colr}" stroke-width=".35" stroke-dasharray="1,.7"/>')
        o.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r=".8" fill="{colr}"/>')
        o.append(f'<rect x="{bx:.2f}" y="{by:.2f}" width="{wmax:.2f}" height="{hb:.2f}" rx="{min(hb / 2, 2):.2f}" fill="{colr}"/>')
        for i, l in enumerate(lines):
            o.append(f'<text x="{bx + fs * .8:.2f}" y="{by + fs * 1.22 + i * fs * 1.38:.2f}" class="note" style="font-size:{fs:.2f}px">{esc(l)}</text>')
    # track dots
    for key, ((x, y), dr, st) in (dots or {}).items():
        X, Y = P(x, y); step = rad * 2.15
        vx, vy = {"r": (step, 0), "l": (-step, 0), "d": (0, step), "u": (0, -step)}[dr]
        for i, s in enumerate(st):
            cx, cy = X + i * vx, Y + i * vy; c = colour(s)
            if s in XS:
                o.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{rad * .94:.2f}" fill="#fff" stroke="{c}" stroke-width="{rad * .2:.2f}"/>'
                         f'<text x="{cx:.2f}" y="{cy + rad * .34:.2f}" class="sn" style="font-size:{rad * .92:.2f}px;fill:{c}">{s}</text>')
            else:
                o.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{rad:.2f}" fill="{c}" stroke="#fff" stroke-width="{rad * .12:.2f}"/>'
                         f'<text x="{cx:.2f}" y="{cy + rad * .34:.2f}" class="sn" style="font-size:{rad * .95:.2f}px">{s}</text>')
    # compass (the church's axis runs west–east, high altar at the east) and the scale warning
    if compass:
        X, Y = 7, 8
        o.append(f'<circle cx="{X:.2f}" cy="{Y + .6:.2f}" r="5" fill="#FDFBF7" fill-opacity=".9"/>')
        o.append(f'<path d="M{X:.2f},{Y - 4:.2f} L{X + 1.6:.2f},{Y + 1.6:.2f} L{X:.2f},{Y + .6:.2f} L{X - 1.6:.2f},{Y + 1.6:.2f} Z" fill="{INK}" fill-opacity=".75"/>'
                 f'<text x="{X:.2f}" y="{Y + 5:.2f}" class="cmp">N</text>')
    if scale_note:
        o.append(f'<text x="{W - 2.4:.2f}" y="{H - 2.4:.2f}" class="scl">SCHEMATIC · NOT TO SCALE</text>')
    o.append("</g></svg>")
    return "".join(o)

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
def rng(sec):
    ns = [n for n in NUMS if TR[n]["section"] == sec]
    return (f"{ns[0]}–{ns[-1]}" if len(ns) > 1 else f"{ns[0]}") if ns else ""

UNC_NOTE = "Dashed outlines and dotted lines: positions and paths not yet confirmed on site."
LEGEND = (f'<div class="legend"><span>{dot(8, "ldot")} track</span><span><span class="ldot hol" style="color:{INK};border-color:{INK}">X</span> Extra</span>'
          f'<span><svg width="9mm" height="3mm" viewBox="0 0 9 3"><path d="M.5,1.5 L8.5,1.5" stroke="{INK}" stroke-opacity=".7" stroke-width=".5" stroke-dasharray="1.4,.9"/></svg> route, in walking order</span>'
          f'<span><svg width="9mm" height="3mm" viewBox="0 0 9 3"><path d="M.5,1.5 L8.5,1.5" stroke="{INK}" stroke-opacity=".55" stroke-width=".45" stroke-dasharray=".15,.9" stroke-linecap="round"/></svg> path to be confirmed</span>'
          f'<span><svg width="7mm" height="4mm" viewBox="0 0 7 4"><rect x=".5" y=".5" width="6" height="3" fill="#fff" stroke="{INK}" stroke-width=".3" stroke-dasharray="1.1,.7"/></svg> position to be confirmed on site</span>'
          '</div>')

pages = []
# ---------------------------------------------------------------- page 1: the whole site
OV_LABELS = [
    (86, -32, "Patio de los Naranjos", "middle", "plb"), (34, -18, "Sagrario\nnot on the visit", "middle", "pls"),
    (116, -31, "Nave del\nLagarto", "middle", "plm"), (113, -5.5, "Giralda", "middle", "plb"),
    (47, 39, "Coro", "middle", "pl"), (77, 38.2, "Capilla\nMayor", "middle", "pl"), (121, 37.3, "Capilla\nReal", "middle", "pl"),
    (23, -3, "Capilla de San Antonio", "middle", "plm"), (49, 81, "Capilla de la Antigua", "middle", "plm"),
    (62, 55, "Colón", "middle", "plm"), (128, 95, "Sacristías\nSala Capitular", "start", "plm"),
    (64.5, -3, "Puerta de la Concepción", "start", "pls"), (62, 24, "transept", "middle", "pls"),
    (-2, 30, "Puerta de la\nAsunción\nnot a visitor door", "end", "pls"),
    (92, -62.5, "C/ Alemanes", "start", "pls"), (146, -19, "C/ Cardenal\nAmigo Vallejo", "middle", "pls"),
    (-12, 60, "Avenida de la\nConstitución", "middle", "pls"),
]
ov = plan_svg((-30, 160, -66, 108), 180, 140, labels=OV_LABELS, lab_fs=2.4, note_fs=2.2,
    notes=[((134, -22), "IN · Puerta del Lagarto\nonline tickets", "start", 9, -19),
           ((62, 92), "IN · Puerta del Príncipe\n(San Cristóbal) · ticket office", "start", -30, 3),
           ((120, -7), "FIRST · the Giralda", "gir", 16, 3),
           ((82, -60), "OUT · Puerta del Perdón", "finish", -26, 1)])
KEYS = "".join(f'<span><i style="background:{SECS[s][1]}"></i><em>{esc(SECS[s][0])} <b>{rng(s)}</b></em></span>' for s in SECS if rng(s))
lens = "".join(f'<div class="card"><div class="cnum" style="background:{NAVY}">{i}</div>'
               f'<div class="cbody"><div class="ct">{esc(n)}</div><div class="cs"><b>{esc(m)}</b> · {k} tracks</div><div class="cs2">{esc(d)}</div></div></div>'
               for i, (n, k, m, d) in enumerate(LENGTHS, 1))
pages.append(f'''<section class="page">
 <header><div class="brand">YO TOURS · AUDIO GUIDE</div><h1>Catedral de Sevilla and the Giralda</h1>
 <p class="lede">A mosque's tower and courtyard, the largest Gothic building in Europe and the rooms the canons built round it: {len(F_SET) - FX} main stops plus {FX} short Extras in one walking order, the Giralda first, in three lengths.</p></header>
 <div class="how"><div><b>1</b> <strong>Spanish names as on the signs; look for the landmark.</strong> Every stop is named in Spanish, as on the signs, with one big thing to look for: the gilded altarpiece, four heralds carrying a coffin.</div>
 <div><b>2</b> The coloured circle is the track to play there, in track order. Hollow circles are short, optional Extras, on the Full tour only. Pages 2 to 4 show every track in its place.</div>
 <div><b>3</b> Each track ends by telling you where to go next. The plan is schematic, not to scale; dashed outlines are positions still to be confirmed on site.</div></div>
 <div class="ov">{ov}<div class="keys">{KEYS}</div><div class="kn">The line shows the walking order, not the exact path. Dotted: the way from each door to the tower, and through the sacristies, still to be checked on site.</div></div>
 <div class="warn"><b>Whichever door you come in by, start at the Giralda, in the corner of the church by the courtyard.</b> Then one loop round the church, and out through the Patio de los Naranjos and the Puerta del Perdón; once you are out you cannot come back in. Not climbing? Go to the tower door anyway and start at 7. The Capilla Real is for prayer only: you see it through its grille.</div>
 <div class="cards">{lens}</div>
 <footer>{esc(FOOTER)}</footer>
</section>''')

def map_page(kicker, title, sub, body, ns, extra=""):
    return f'''<section class="page">
 <header class="fh"><div class="brand">YO TOURS · CATEDRAL DE SEVILLA · {esc(kicker)}</div>
 <h2>{esc(title)}</h2><p class="sub">{sub}</p></header>
 {body}<div class="list">{stop_list(ns)}</div>{extra}
 <footer>{esc(FOOTER)}</footer>
</section>'''

# ---------------------------------------------------------------- page 2: the Giralda (schematic elevation)
def giralda_svg():
    W, H = 96, 214; o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}mm" height="{H}mm">',
                         f'<rect x="0" y="0" width="{W}" height="{H}" rx="2" fill="#FDFBF7"/>']
    gc, gt = stroke("La Giralda"), tint("La Giralda")
    x0, x1 = 35, 63; base, top = 196, 84          # the Almohad shaft
    o.append(f'<line x1="4" y1="{base}" x2="{W - 4}" y2="{base}" stroke="#8F8473" stroke-width=".5"/>')
    o.append(f'<rect x="{x0}" y="{top}" width="{x1 - x0}" height="{base - top}" fill="{gt}" stroke="{gc}" stroke-width=".6"/>')
    # cutaway: the ramps (34), winding round the core
    cx0, cx1 = x0 + 4.5, x1 - 4.5; n = 34; y_lo, y_hi = base - 3, top + 2; hstep = (y_lo - y_hi) / n
    o.append(f'<rect x="{cx0}" y="{y_hi}" width="{cx1 - cx0}" height="{y_lo - y_hi}" fill="#FBF3EA" stroke="{gc}" stroke-width=".3"/>')
    pts = [(cx0 + .8 if i % 2 == 0 else cx1 - .8, y_lo - i * hstep) for i in range(n + 1)]
    o.append('<path d="M' + " L".join(f"{a:.2f},{b:.2f}" for a, b in pts) + f'" fill="none" stroke="{gc}" stroke-width=".35" stroke-opacity=".75"/>')
    for i in (1, 10, 20, 34):
        y = y_lo - (i - .5) * hstep
        o.append(f'<text x="{x0 + 2.25}" y="{y + .8:.2f}" class="gz" style="text-anchor:middle">{i}</text>')
    # the belfry (bell level: the top of the visit) and the Renaissance crown
    bt = 62
    o.append(f'<rect x="{x0 - .5}" y="{bt}" width="{x1 - x0 + 1}" height="{top - bt}" fill="#F6E3CF" stroke="{gc}" stroke-width=".6"/>')
    for i in range(4):
        ax = x0 + 2 + i * 6.4
        o.append(f'<path d="M{ax},{top - 2} L{ax},{bt + 8} A2.25,2.25 0 0 1 {ax + 4.5},{bt + 8} L{ax + 4.5},{top - 2} Z" fill="#fff" stroke="{gc}" stroke-width=".35"/>')
        o.append(f'<path d="M{ax + 1.1},{bt + 12} Q{ax + 2.25},{bt + 9.5} {ax + 3.4},{bt + 12} L{ax + 3.7},{bt + 14} L{ax + .8},{bt + 14} Z" fill="{GOLD}" fill-opacity=".8"/>')
    o.append(f'<rect x="{x0 + 2.5}" y="{bt - 14}" width="{x1 - x0 - 5}" height="14" fill="#F6E3CF" stroke="{gc}" stroke-width=".5"/>')
    o.append(f'<rect x="{x0 + 6}" y="{bt - 24}" width="{x1 - x0 - 12}" height="10" fill="#F6E3CF" stroke="{gc}" stroke-width=".5"/>')
    o.append(f'<path d="M{x0 + 8.5},{bt - 24} Q{(x0 + x1) / 2},{bt - 36} {x1 - 8.5},{bt - 24} Z" fill="#F6E3CF" stroke="{gc}" stroke-width=".5"/>')
    # the Giraldillo: a standing figure with a banner (schematic)
    fx = (x0 + x1) / 2; fy = bt - 35
    o.append(f'<line x1="{fx}" y1="{fy}" x2="{fx}" y2="{fy - 4}" stroke="{INK}" stroke-width=".5"/>')
    o.append(f'<path d="M{fx - 2},{fy - 4} L{fx + 2},{fy - 4} L{fx + 1},{fy - 11} L{fx - 1},{fy - 11} Z" fill="{GOLD}"/>'
             f'<circle cx="{fx}" cy="{fy - 12.3}" r="1.3" fill="{GOLD}"/>'
             f'<line x1="{fx + 1.5}" y1="{fy - 9}" x2="{fx + 1.5}" y2="{fy - 19}" stroke="{INK}" stroke-width=".35"/>'
             f'<path d="M{fx + 1.5},{fy - 19} L{fx + 8},{fy - 17.5} L{fx + 1.5},{fy - 15.5} Z" fill="{GOLD}" fill-opacity=".85"/>')
    def txt(x, y, lines, anc="start"):
        for i, (cls, t) in enumerate(lines):
            o.append(f'<text x="{x}" y="{y + i * 3.3:.2f}" class="{cls}" style="text-anchor:{anc}">{esc(t)}</text>')
    # side brackets: periods
    def brk(xa, ya, yb, lines, ly=None):
        o.append(f'<path d="M{xa},{ya} L{xa - 1.4},{ya} L{xa - 1.4},{yb} L{xa},{yb}" fill="none" stroke="{MUTED}" stroke-width=".3"/>')
        txt(xa - 3, ly if ly else (ya + yb) / 2 - 1.5, lines, "end")
    brk(x0 - 2.5, top + 1, base - 1, [("gl", "Almohad"), ("gl", "minaret"), ("gs", "1184–1198")], top + 14)
    brk(x0 - 2.5, fy - 1, top - 1, [("gl", "Renaissance"), ("gl", "belfry"), ("gs", "1560s")])
    txt(x1 + 3, fy - 16, [("gl", "Giraldillo"), ("gs", "bronze weathervane"), ("gs", "of Faith, 1568;"), ("gs", "seen from below:"), ("gs", "track 26")])
    txt(x1 + 3, bt + 5, [("gl", "Bell level"), ("gs", "the top of the climb")])
    txt(x1 + 3, top + 30, [("gl", "34 ramps"), ("gs", "not stairs")])
    # one-way, keep right: up and down arrows
    def arrow(x, ya, yb, lab):
        o.append(f'<line x1="{x}" y1="{ya}" x2="{x}" y2="{yb}" stroke="{INK}" stroke-width=".45" stroke-dasharray="1.2,.8"/>')
        d = 1 if yb > ya else -1
        o.append(f'<path d="M{x - 1.3},{yb - d * 2} L{x},{yb} L{x + 1.3},{yb - d * 2} Z" fill="{INK}"/>')
        my = (ya + yb) / 2
        o.append(f'<text x="{x - 1.6}" y="{my}" class="gs" transform="rotate(-90 {x - 1.6} {my})" style="text-anchor:middle">{esc(lab)}</text>')
    arrow(x1 + 5.5, base - 4, top + 44, "up · keep right"); arrow(x0 - 5.5, top + 46, base - 4, "down · keep right")
    o.append(f'<text x="{(x0 + x1) / 2}" y="{base + 4.4}" class="gs" style="text-anchor:middle">tower door: inside the cathedral, its north-east corner</text>')
    # dots
    rad = 2.6
    def dts(x, y, ns, dr=1):
        for i, s in enumerate(ns):
            cx = x + dr * i * rad * 2.15; c = colour(s)
            if s in XS:
                o.append(f'<circle cx="{cx}" cy="{y}" r="{rad * .94}" fill="#fff" stroke="{c}" stroke-width="{rad * .2}"/><text x="{cx}" y="{y + rad * .34}" class="sn" style="font-size:{rad * .92}px;fill:{c}">{s}</text>')
            else:
                o.append(f'<circle cx="{cx}" cy="{y}" r="{rad}" fill="{c}" stroke="#fff" stroke-width="{rad * .12}"/><text x="{cx}" y="{y + rad * .34}" class="sn" style="font-size:{rad * .95}px">{s}</text>')
    g = {r: [n for n in NUMS if TR[n]["room"] == r] for r in set(TR[n]["room"] for n in NUMS)}
    dts(x1 + 11, base - 8, g.get("Giralda · first ramps", []))
    dts(x1 + 11, top + 60, g.get("Giralda · ramps", []))
    dts(x1 + 5.5, bt + 14, g.get("Giralda · bell level", []))
    dts(x0 - 11, top + 75, g.get("Giralda · on the way down", []), -1)
    foot = g.get("Catedral · at the foot of the Giralda", [])
    dts(x0 + 2, base + 10, foot)
    o.append(f'<text x="{x0 + 2 + rad * 1.6}" y="{base + 11}" class="gs">at the foot of the tower, inside the church</text>')
    o.append(f'<text x="2.6" y="5" class="scl" style="text-anchor:start">SCHEMATIC ELEVATION · NOT TO SCALE</text>')
    o.append("</svg>")
    return "".join(o)

GIR_NS = [n for n in NUMS if TR[n]["section"] == "La Giralda"] + [n for n in NUMS if TR[n]["room"].startswith("Catedral · at the foot")]
gbody = f'''<div class="gwrap"><div class="plan gplan">{giralda_svg()}</div><div class="gside">
 <div class="list one">{stop_list(GIR_NS)}</div>
 <div class="box"><h3>Ramps, not stairs</h3><p>The way up winds round the core of the tower on 34 ramps. One-way rule: going up and coming down, <b>always keep to your right</b>. No wheelchairs or pushchairs.</p></div>
 <div class="box"><h3>Listen as you go</h3><p>Start 2 on the first ramps and 3 a few turns up. 4 (and the Extra, 5) are for the bell level, the top of the climb. 6 is for the way down: no need to stop. At the bottom, step just inside the church, out of the way of the tower door, for 7.</p></div>
 <div class="box"><h3>Not climbing?</h3><p>Go to the tower door anyway and start at 7, at the foot of the Giralda.</p></div>
 <div class="box"><h3>Works on the tower</h3><p>Restoration of the bell level and the Renaissance crown began in April 2026; the visit carries on, but parts of the view may be screened.</p></div>
</div></div>'''
pages.append(map_page("THE GIRALDA", "The Giralda · first, up and down",
    "The visit begins at the tower, as the cathedral's own route does. You enter it from inside the church, in the corner nearest the courtyard: follow the signs for the Giralda. "
    "The Almohad minaret carries the Renaissance bell chamber; the Giraldillo turns on top.", gbody, [], ""))

# ---------------------------------------------------------------- page 3: the loop inside the church
def ds(room_prefix): return [n for n in NUMS if TR[n]["room"].startswith(room_prefix)]
IN_NS = [n for n in NUMS if TR[n]["section"] in ("The heart of the cathedral", "Around the naves", "Columbus", "Sacristies and chapter house", "Royal chapel and the way to the courtyard")]
IN_LABELS = [
    (47, 39, "Coro", "middle", "pl"), (77, 38.2, "Capilla\nMayor", "middle", "pl"), (121, 37.3, "Capilla\nReal", "middle", "pl"),
    (122, 25.5, "the grille", "middle", "pls"),
    (23, -2.2, "Capilla de San Antonio", "middle", "plm"), (49, 84.5, "Capilla de la Antigua", "middle", "plm"),
    (62, 70.5, "Sepulcro\nde Colón", "middle", "pls"), (83, 74.2, "Dolores", "middle", "pls"),
    (84, 82, "Cálices", "middle", "pls"), (84, 94, "Pabellón ?", "middle", "pls"), (100, 81.5, "Sacristía Mayor", "middle", "pls"),
    (111, 105.5, "Antecabildo", "middle", "pls"), (128, 81.5, "Sala Capitular", "start", "pls"),
    (60.5, 93, "Puerta del Príncipe\n(San Cristóbal)", "end", "pls"), (62, -4, "Puerta de la Concepción", "end", "pls"),
    (-1.5, 30, "Puerta de la\nAsunción", "end", "pls"), (113, -5.5, "Giralda", "middle", "plb"),
    (82, -6.5, "Patio de los Naranjos · page 4", "middle", "plm"), (62, 25, "transept", "middle", "pls"),
]
IN_DOTS = {
    "pri": ((66.5, 90), "r", [1]),
    "foot": ((101, 8.5), "l", ds("Catedral · at the foot")),
    "cm": ((74.8, 48.5), "r", ds("Capilla Mayor")), "coro": ((47, 48.5), "r", ds("Coro")),
    "sant": ((31.5, 5), "r", ds("Capilla de San Antonio")), "west": ((6, 46), "d", ds("Puerta de la Asunción")),
    "ant": ((44.5, 80), "r", ds("Capilla de la Antigua")), "col": ((57.3, 55.5), "r", ds("Sepulcro de Cristóbal Colón")),
    "cal": ((84, 86), "r", ds("Sacristía de los Cálices")), "pab": ((84, 97.5), "r", ds("Sala del Pabellón")),
    "sm": ((95.3, 95.5), "r", ds("Sacristía Mayor")), "sc": ((130, 86), "d", ds("Sala Capitular")),
    "cr": ((123.5, 52.5), "r", ds("Capilla Real")), "conc": ((68, 4.5), "r", ds("Puerta de la Concepción")),
}
isvg = plan_svg((-14, 150, -13, 115), 178, 140, labels=IN_LABELS, dots=IN_DOTS, lab_fs=2.25, rad=1.85, note_fs=2.1,
    notes=[((120, -5), "2–6 · the Giralda\nsee page 2", "gir", 15, 3)])
pages.append(map_page("INSIDE THE CHURCH", "The loop inside · 7 to 24",
    "From the foot of the tower to the middle: the Capilla Mayor and the Coro. Round the church: San Antonio, the west end, the Antigua and Columbus by the Puerta del Príncipe. "
    "Through the sacristies to the Sala Capitular, back to the Capilla Real and on to the Puerta de la Concepción. The line gives the order, not the exact path.",
    f'<div class="plan">{isvg}{LEGEND}</div>', IN_NS))

# ---------------------------------------------------------------- page 4: the Patio de los Naranjos and the way out
PA_NS = [n for n in NUMS if TR[n]["section"] in ("Patio de los Naranjos", "Closing")]
PA_NS = ds("Puerta de la Concepción") + PA_NS
PA_LABELS = [
    (82, -29.5, "Patio de los Naranjos", "middle", "plb"), (77, -24.4, "fountain", "end", "pls"),
    (34, -16, "Sagrario\nnot on the visit", "middle", "pls"), (116, -33, "Nave del\nLagarto", "middle", "plm"),
    (113, -5.4, "Giralda", "middle", "plb"), (60, -2.6, "Puerta de la Concepción", "end", "pls"),
    (88, 13, "the church", "middle", "pls"), (121, 37.5, "Capilla Real", "middle", "pls"),
    (92, -64, "C/ Alemanes", "start", "pls"), (124, -36, "C/ Cardenal\nAmigo Vallejo", "start", "pls"),
]
PA_DOTS = {
    "conc": ((70.5, 4.5), "r", ds("Puerta de la Concepción")), "patio": ((70, -11), "r", ds("Patio de los Naranjos")[:1]),
    "view": ((100, -27), "d", [n for n in ds("Patio de los Naranjos") if "view" in TR[n]["room"]]),
    "lag": ((116, -41.5), "r", ds("Nave del Lagarto")), "perd": ((90, -54.5), "r", ds("Puerta del Perdón")),
    "in": ((138.5, -22), "r", [1]),
}
psvg = plan_svg((14, 146, -70, 18), 178, 150, labels=PA_LABELS, dots=PA_DOTS, lab_fs=2.5, rad=2.1, approach="lagarto", route="patio",
    notes=[((82, -60), "OUT · Puerta del Perdón", "finish", -32, 0), ((134, -22), "IN · Puerta del Lagarto", "start", 2, 11)])
pextra = '''<div class="warn"><b>The way out is the Puerta del Perdón</b>, the tall arched gateway in the middle of the far side of the courtyard, opposite the church. Once you pass through it, the visit is over and there is no way back in, so see the Giralda from the courtyard (26) and the Nave del Lagarto (27) first. If the staff send you into the courtyard by another door than the Concepción, follow the Salida signs.</div>
 <div class="box"><h3>On the shorter tours</h3><p>Essential goes from the Sala Capitular (22), and Highlights from Columbus's tomb (14), straight to the courtyard (25), through the same door at the end of the transept on the tower side. Both then end at the Puerta del Perdón (28).</p></div>'''
pages.append(map_page("THE PATIO DE LOS NARANJOS", "The courtyard and the way out · 24 to 28",
    "Through the Puerta de la Concepción, at the end of the transept on the tower side, into the mosque's old courtyard (25). Find a spot with a view of the top of the tower for the Giraldillo (26), "
    "then the covered gallery nearest the tower, the Nave del Lagarto, with the crocodile overhead (27), and out through the Puerta del Perdón (28).",
    f'<div class="plan">{psvg}{LEGEND}</div>', PA_NS, pextra))

# ---------------------------------------------------------------- page 5: the stop table
rows = []; last_sec = None
for n in NUMS:
    s = TR[n]["section"]
    if s != last_sec: rows.append(("sec", s)); last_sec = s
    rows.append(("stop", n))
tot = {k: sum(minutes(n) for n in NUMS if f(n)) for k, f in (("F", lambda n: n in F_SET), ("E", lambda n: n in E_SET), ("H", lambda n: n in H_SET))}
trs = []
for kind, v in rows:
    if kind == "sec":
        c = SECS.get(v, ("", INK))[1]
        trs.append(f'<tr class="sh"><td colspan="7" style="color:{c};border-bottom-color:{c}">{esc(SECS.get(v, (v,))[0])}</td></tr>')
    else:
        n = v; t = TR[n]; x = ' class="x"' if n in XS else ''
        ex = f'<i style="color:{colour(n)}">Extra</i> ' if n in XS else ''
        mk = lambda on: '<span class="mk">●</span>' if on else '<span class="no">·</span>'
        trs.append(f'<tr{x}><td>{dot(n)}</td><td class="pc">{esc(t["room"])}</td><td class="tt">{ex}{esc(t["title"])}</td>'
                   f'<td class="mn">{fmt_min(minutes(n))}</td><td>{mk(n in F_SET)}</td><td>{mk(n in E_SET)}</td><td>{mk(n in H_SET)}</td></tr>')
trs.append(f'<tr class="tot"><td colspan="3">Tracks · listening minutes (walking and the climb come on top)</td><td class="mn"></td>'
           f'<td>{len(F_SET)}<br><span>{round(tot["F"])}′</span></td><td>{len(E_SET)}<br><span>{round(tot["E"])}′</span></td><td>{len(H_SET)}<br><span>{round(tot["H"])}′</span></td></tr>')
head = '<tr class="th"><th>#</th><th>Place</th><th>Title</th><th>Min</th><th>Full</th><th>Essen&shy;tial</th><th>High&shy;lights</th></tr>'
pages.append(f'''<section class="page">
 <header class="fh"><div class="brand">YO TOURS · CATEDRAL DE SEVILLA · ALL STOPS</div>
 <h2>The stops</h2>
 <p class="sub">Every track in walking order: # on your player, the place as the guide names it, minutes of listening, and the lengths it belongs to (Full, {LENGTHS[0][2]}; Essential, {LENGTHS[1][2]}; Highlights, {LENGTHS[2][2]}; all with the Giralda, walking included). Hollow circles are Extras.</p></header>
 <table class="tbl">{head}{"".join(trs)}</table>
 <footer>{esc(FOOTER)}</footer>
</section>''')

CSS = f'''
@page {{ size: A4; margin: 0 }}
* {{ box-sizing: border-box }}
html, body {{ margin: 0; background: {PAPER}; color: {INK}; font-family: Inter, "DejaVu Sans", sans-serif }}
.page {{ width: 210mm; height: 297mm; padding: 13mm 13mm 10mm; position: relative; page-break-after: always; overflow: hidden; background: {PAPER} }}
.brand {{ font: 600 7.6pt Inter; letter-spacing: .28em; color: {GOLD} }}
h1 {{ font: 700 27pt Lora, serif; margin: 2mm 0 1mm; letter-spacing: -.01em }}
h2 {{ font: 700 19pt Lora, serif; margin: 2mm 0 1.2mm }}
h3 {{ font: 700 10pt Lora, serif; margin: 0 0 1mm }}
.lede {{ font: 400 10.6pt Lora, serif; color: {MUTED}; margin: 0 0 3mm; line-height: 1.35 }}
.sub {{ font: 400 8.9pt Inter; color: {MUTED}; margin: 0 0 3mm; max-width: 184mm; line-height: 1.4 }}
.how {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 3mm; margin-bottom: 3mm }}
.how div {{ background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; padding: 2.2mm 2.8mm; font: 500 7.9pt Inter; line-height: 1.34 }}
.how b {{ display: inline-flex; width: 5mm; height: 5mm; border-radius: 50%; background: {INK}; color: #fff; font: 700 7.5pt Inter; align-items: center; justify-content: center; margin-right: 1.2mm }}
.how strong {{ color: {RED} }}
.ov {{ background: #FDFBF7; border: .3mm solid {LINE}; border-radius: 4mm; padding: 1.5mm 1mm; margin-bottom: 3mm }}
.ov svg {{ display: block; margin: 0 auto }}
.keys {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1mm 3mm; padding: 1.4mm 4mm 0; font: 500 6.9pt Inter; color: {INK} }}
.keys .kh {{ font: 700 6.6pt Inter; letter-spacing: .08em; text-transform: uppercase; color: {MUTED} }}
.ov .kn {{ font: 500 6.8pt Inter; color: {MUTED}; text-align: center; padding: 1.4mm 0 .3mm }}
.keys span {{ display: flex; align-items: flex-start; gap: 1.6mm }} .keys em {{ font-style: normal; line-height: 1.25 }} .keys b {{ color: {MUTED}; font-weight: 600; white-space: nowrap }}
.keys i {{ width: 3mm; height: 3mm; border-radius: 50%; flex: none; margin-top: .2mm }}
.warn {{ background: #fff; border: .3mm solid {GOLD}; border-left: 1.6mm solid {GOLD}; border-radius: 2.4mm; padding: 2.2mm 3mm; font: 400 8.2pt Inter; line-height: 1.38; margin-bottom: 3mm }}
.cards {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.4mm }}
.card {{ display: grid; grid-template-columns: 10mm 1fr; align-items: center; background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; overflow: hidden; padding: 2mm 2mm 2mm 0 }}
.cnum {{ width: 7mm; height: 7mm; border-radius: 50%; color: #fff; font: 700 11pt Inter; display: flex; align-items: center; justify-content: center; margin-left: 2mm }}
.ct {{ font: 700 10.2pt Lora; margin-bottom: .4mm }} .cs {{ font: 400 7.9pt Inter; color: {MUTED} }} .cs b {{ color: {INK} }}
.cs2 {{ font: 400 7pt Inter; color: {MUTED}; margin-top: .4mm; line-height: 1.3 }}
footer {{ position: absolute; left: 13mm; right: 13mm; bottom: 7mm; font: 400 7pt Inter; color: {MUTED}; border-top: .3mm solid {LINE}; padding-top: 2mm }}
.plan {{ background: #FDFBF7; border: .3mm solid {LINE}; border-radius: 4mm; padding: 2mm; margin-bottom: 3mm }}
.plan svg {{ display: block; margin: 0 auto }}
.list {{ columns: 2; column-gap: 7mm }} .list .row {{ break-inside: avoid }} .list.one {{ columns: 1 }}
.gwrap {{ display: grid; grid-template-columns: 99mm 1fr; gap: 4mm; align-items: start }} .gplan {{ padding: 1mm; margin: 0 }}
.gside .list {{ margin-bottom: 3mm }}
.box {{ background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; padding: 2.2mm 2.8mm; margin-bottom: 2.4mm }}
.box p {{ font: 400 8pt Inter; line-height: 1.38; margin: 0 }}
.tg {{ font-family: Inter; font-weight: 800; text-anchor: middle }} .sn {{ font-family: Inter; font-weight: 700; fill: #fff; text-anchor: middle }}
.note {{ font-family: Inter; font-weight: 600; fill: #fff }}
.pl, .plb, .plm, .pls {{ paint-order: stroke; stroke: #FDFBF7; stroke-width: .55px; stroke-linejoin: round }}
.pl {{ font-family: Inter; font-weight: 700; fill: {INK} }} .plb {{ font-family: Lora; font-weight: 700; fill: {INK} }}
.plm {{ font-family: Inter; font-weight: 600; fill: #4A443C }} .pls {{ font-family: Inter; font-weight: 500; fill: #8A8072 }}
.cmp {{ font: 700 2.6px Inter; fill: {INK}; text-anchor: middle }}
.scl {{ font: 700 2.5px Inter; fill: #A39886; letter-spacing: .25px; text-anchor: end }}
.gl {{ font: 700 3.1px Inter; fill: {INK} }} .gs {{ font: 500 2.6px Inter; fill: {MUTED} }} .gz {{ font: 600 2.2px Inter; fill: #A4581B }}
.legend {{ display: flex; flex-wrap: wrap; gap: 1.2mm 4mm; justify-content: center; padding: 2mm 1mm .4mm; font: 500 7pt Inter; color: {MUTED}; align-items: center }}
.legend > span {{ display: inline-flex; align-items: center; gap: 1.3mm }} .legend .sc {{ font-weight: 700; color: {INK} }}
.ldot {{ width: 4.4mm; height: 4.4mm; border-radius: 50%; color: #fff; font: 700 6pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.list .row {{ display: grid; grid-template-columns: 7.5mm 1fr; align-items: center; padding: .5mm 0; border-bottom: .25mm solid {LINE} }}
.dot {{ width: 6mm; height: 6mm; border-radius: 50%; color: #fff; font: 700 7.6pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.hol {{ background: #fff; border: .45mm solid; box-sizing: border-box }}
.row.x .tt {{ color: {MUTED} }} .tt i {{ font-style: normal; font-weight: 700; font-size: 7pt; letter-spacing: .04em; margin-right: 1mm }}
.tt {{ font: 500 7.6pt Inter; line-height: 1.2 }} .list .tt {{ padding-left: 1.6mm }} .tt b {{ font-weight: 700; color: {INK} }}
.tbl {{ width: 100%; border-collapse: collapse; background: #fff; border: .3mm solid {LINE}; border-radius: 3mm }}
.tbl th {{ font: 700 6.6pt Inter; color: {MUTED}; text-align: left; padding: 1.6mm 1.2mm 1.2mm; border-bottom: .35mm solid {INK}; letter-spacing: .04em; text-transform: uppercase }}
.tbl th:nth-child(n+4) {{ text-align: center; width: 13mm }} .tbl th:first-child {{ width: 9mm; padding-left: 2mm }} .tbl th:nth-child(2) {{ width: 62mm }}
.tbl td {{ padding: .15mm 1.2mm; line-height: 1.15; border-bottom: .2mm solid {LINE}; vertical-align: middle }}
.tbl td:first-child {{ padding-left: 2mm }} .tbl td:nth-child(n+4) {{ text-align: center }}
.tbl .dot {{ width: 4.6mm; height: 4.6mm; font-size: 6.4pt; vertical-align: middle }}
.tbl .pc {{ font: 700 7.4pt Inter }} .tbl .tt {{ font: 500 7.5pt Inter }} .tbl tr.x .tt, .tbl tr.x .pc {{ color: {MUTED} }}
.tbl .mn {{ font: 600 7.4pt Inter; color: {INK} }} .mk {{ color: {NAVY}; font-size: 8.4pt }} .no {{ color: #C9BFAE }}
.tbl tr.sh td {{ font: 700 7.3pt Inter; padding: 1.2mm 2mm .3mm; border-bottom: .3mm solid; letter-spacing: .02em }}
.tbl tr.tot td {{ font: 700 7.6pt Inter; border-top: .35mm solid {INK}; border-bottom: none; padding: 1.6mm 1.2mm 1.6mm 2mm }} .tbl tr.tot span {{ font-weight: 500; color: {MUTED} }}
'''

def build():
    doc = f'<!doctype html><html><head><meta charset="utf-8"><title>Catedral de Sevilla · Yo Tours route</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
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
