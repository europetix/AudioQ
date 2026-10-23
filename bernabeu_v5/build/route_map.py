#!/usr/bin/env python3
"""Yo Tours · Estadio Santiago Bernabéu — route map, edition of 23 Oct 2026.
Three pages made for phones:
  1. Your route through the stadium: a drawn cross-section of the bowl (west, Castellana, on the left; east, Padre Damián,
     on the right) with the roof, the screen ring, the steel skin and the hypogeum where the grass is stored, and every
     zone of the tour with its stop numbers; plus the three lengths (Full / Essential / Highlights).
  2. Around the stadium: a drawing from above with the four streets, the tour entrance, the store and exit, and the way
     to the S10 bus (the metro station is closed).
  3. Every stop, with the length it belongs to.
Our own schematic drawing (not to scale), after the club's tour pages and brochure; the club publishes no floor plan of the
tour, so the position of each zone inside the stands is indicative. Driven by plan.json, so stop numbers match the audio.
Usage: python3 route_map.py <bundle folder> [--png <dir>]   -> <bundle>/Bernabeu_Audio_Guide_Route.pdf"""
import json, os, sys, html, asyncio

B = sys.argv[1]
PNG_DIR = sys.argv[sys.argv.index("--png") + 1] if "--png" in sys.argv else None
plan = json.load(open(os.path.join(B, "plan.json"), encoding="utf-8")); TR = plan["tracks"]
XS = {int(t["seq"]) for t in TR if t.get("register") == "X"}
OUT_PDF = os.path.join(B, "Bernabeu_Audio_Guide_Route.pdf")
ESSENTIAL = {1, 2, 3, 4, 7, 9, 10, 11, 13, 14, 16, 19, 22, 23, 24, 25, 28}      # same lists as the launchers
HIGHLIGHTS = {1, 3, 7, 10, 16, 22, 23, 25, 28}
MIN = lambda ns: int(sum(t["words"] for t in TR if int(t["seq"]) in ns) / 125 * 1.08 // 5) * 5

PAPER, INK, MUTED, LINE, GOLD, NAVY = "#F6F1E7", "#1F1B17", "#776E62", "#D8CEBD", "#A9812F", "#1D2B4A"
STEEL, STAND, STAND_E, GRASS, SKY = "#9AA3B2", "#E4DED2", "#CFC6B6", "#7FA36B", "#EEF2F5"
ZC = {"out": "#5B6B2E", "pan": "#2C4A6E", "mus": "#8C1C13", "dr": "#6A3A6B", "store": "#A4581B"}
def esc(s): return html.escape(s, quote=True)

def zone_key(room):
    for k, z in (("Outside", "out"), ("Panoramic", "pan"), ("Museum", "mus"), ("Dressing", "dr"), ("Benches", "dr"),
                 ("Press", "dr"), ("Store", "store"), ("Exit", "store")):
        if room.startswith(k): return z
    return "out"

def pill(x, y, text, col, sub="", anchor="start", w=None):
    w = w or (len(text) * 2.05 + 5.5)
    x0 = x if anchor == "start" else x - w
    o = [f'<rect x="{x0:.1f}" y="{y-3.6:.1f}" width="{w:.1f}" height="7.2" rx="3.6" fill="{col}"/>',
         f'<text x="{x0 + w/2:.1f}" y="{y+1.15:.1f}" class="pt">{esc(text)}</text>']
    if sub:
        sx = x0 + w + 1.6 if anchor == "start" else x0 - 1.6
        o.append(f'<text x="{sx:.1f}" y="{y+1.0:.1f}" class="ps" style="text-anchor:{"start" if anchor == "start" else "end"}">{esc(sub)}</text>')
    return "".join(o)

# ------------------------------------------------------------------ page 1: the section
def section_svg():
    W, H = 182.0, 132.0
    G = 92.0                                   # ground / pitch level
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}mm" height="{H}mm">',
         f'<rect x="0" y="0" width="{W}" height="{G}" fill="{SKY}"/>',
         f'<rect x="0" y="{G}" width="{W}" height="{H-G}" fill="#E9E3D6"/>']
    # hypogeum with six trays
    hx0, hx1, hy0, hy1 = 60.0, 122.0, G + 4, G + 25
    o.append(f'<rect x="{hx0}" y="{hy0}" width="{hx1-hx0}" height="{hy1-hy0}" rx="1.5" fill="#F4F1EA" stroke="{STAND_E}" stroke-width=".5"/>')
    for r in range(3):
        for c in range(2):
            o.append(f'<rect x="{hx0 + 3 + c*29.5:.1f}" y="{hy0 + 2.4 + r*6.4:.1f}" width="26.5" height="4.6" rx="1" fill="{GRASS}" opacity=".85"/>')
    o.append(f'<text x="{(hx0+hx1)/2}" y="{hy1+4.4}" class="lab" style="text-anchor:middle">The hipogeo: the grass in six trays, stored here between matches</text>')
    # pitch level (usually bare)
    o.append(f'<line x1="56" y1="{G}" x2="126" y2="{G}" stroke="{MUTED}" stroke-width=".8" stroke-dasharray="1.6,1.2"/>')
    o.append(f'<text x="104" y="{G-2.2}" class="lab" style="text-anchor:middle">pitch level: on most days a bare floor</text>')
    # stands, both sides (mirror)
    L = [(57, G), (45, 77), (43, 75), (33, 56), (31, 53), (21, 27), (15, 27), (15, G)]
    for side in (1, -1):
        pts = [(x if side == 1 else W - x, y) for x, y in L]
        o.append('<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f'" fill="{STAND}" stroke="{STAND_E}" stroke-width=".6"/>')
        for (xa, ya), (xb, yb) in zip(L[:6], L[1:6]):          # seat rows on the slopes
            n = int(abs(ya - yb) / 2.6)
            for k in range(1, n):
                t = k / n; x = xa + (xb - xa) * t; y = ya + (yb - ya) * t
                xx = x if side == 1 else W - x; x2 = xx - 3.2 * side
                o.append(f'<line x1="{xx:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y:.1f}" stroke="{STAND_E}" stroke-width=".35"/>')
        # steel skin: curved bands outside the stands
        ex = 15 if side == 1 else W - 15
        o.append(f'<path d="M{ex},20 Q{ex - 9*side},57 {ex},{G}" fill="none" stroke="{STEEL}" stroke-width="1.1"/>')
        for k in range(9):
            y = 24 + k * 7.6; bulge = 9 * (1 - ((y - 57) / 37) ** 2) * 0.5
            o.append(f'<line x1="{ex:.1f}" y1="{y:.1f}" x2="{ex - (bulge + 1.2)*side:.1f}" y2="{y:.1f}" stroke="{STEEL}" stroke-width=".6"/>')
    # roof, with the retractable middle
    o.append(f'<path d="M9,21 Q91,9 173,21" fill="none" stroke="{NAVY}" stroke-width="1.5"/>')
    o.append(f'<path d="M52,15.6 Q91,11.2 130,15.6" fill="none" stroke="{GOLD}" stroke-width="1.5" stroke-dasharray="2.2,1.4"/>')
    o.append(f'<text x="91" y="9.4" class="lab" style="text-anchor:middle">the roof: its middle closes in about fifteen minutes</text>')
    # screen ring
    for x in (33, 141):
        o.append(f'<rect x="{x}" y="19.6" width="8" height="3.2" rx=".6" fill="{NAVY}"/>')
    o.append(f'<text x="45" y="27.6" class="lab">360° screen ring</text>')
    o.append(f'<line x1="44.6" y1="26.4" x2="41" y2="22.6" stroke="{MUTED}" stroke-width=".3"/>')
    # compass words
    o.append(f'<text x="2" y="{G+8.5}" class="st">◀ Paseo de la</text><text x="2" y="{G+12.3}" class="st">Castellana · west</text>')
    o.append(f'<text x="{W-2}" y="{G+8.5}" class="st" style="text-anchor:end">Calle Padre ▶</text><text x="{W-2}" y="{G+12.3}" class="st" style="text-anchor:end">Damián · east</text>')
    # the route (schematic): street → up → top tier → museum → pitch level → round to the store
    rt = [(4, G - 2.5), (17.5, G - 2.5), (17.5, 31.5), (24, 31.5), (25, 66), (37, 86), (55, 89.5)]
    o.append('<path d="M' + " L".join(f"{x},{y}" for x, y in rt) + f'" fill="none" stroke="{GOLD}" stroke-width="1.1" stroke-dasharray="2,1.3" stroke-linejoin="round"/>')
    o.append(f'<path d="M66,84 Q118,52 162,{G-11}" fill="none" stroke="{GOLD}" stroke-width="1.1" stroke-dasharray="2,1.3"/>')
    o.append(f'<path d="M-2.4,-1.8 L1.8,0 L-2.4,1.8 Z" fill="{GOLD}" transform="translate(162 {G-11}) rotate(28)"/>')
    o.append(f'<text x="122" y="57.5" class="lab" style="text-anchor:middle">then round the stadium, along its corridors, to the store</text>')
    o.append(f'<text x="19.5" y="62" class="lab" transform="rotate(-90 19.5 62)">up by lifts and stairs</text>')
    # zone pills
    o.append(pill(2.5, G - 7.5, "1–3", ZC["out"], ""))
    o.append(pill(24, 33.2, "4–8", ZC["pan"], "top tier: the panoramic view"))
    o.append(pill(26.5, 64, "9–22", ZC["mus"], "museum and trophy hall"))
    o.append(pill(31, 80.5, "23", ZC["dr"], "dressing room"))
    o.append(pill(49, 86.4, "24–26", ZC["dr"], "benches · press room"))
    o.append(pill(W - 2.5, G - 7.5, "27–28", ZC["store"], "store · way out", anchor="end"))
    o.append("</svg>")
    return "".join(o)

def length_cards():
    alln = {int(t["seq"]) for t in TR}
    rows = [("Full tour", alln, "Everything: 23 main stops and 5 short Extras."),
            ("Essential", ESSENTIAL, "The main story, for a quicker visit."),
            ("Highlights", HIGHLIGHTS, "The best stops, when time is short.")]
    return "".join(f'<div class="len"><div class="lt">{esc(n)}</div><div class="lm">about {MIN(s)} min · {len(s)} tracks</div>'
                   f'<div class="ld">{esc(d)}</div></div>' for n, s, d in rows)

# ------------------------------------------------------------------ page 2: from above
def aerial_svg():
    W, H = 182.0, 168.0
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}mm" height="{H}mm">',
         f'<rect x="0" y="0" width="{W}" height="{H}" fill="#EFEADF"/>']
    # streets
    o.append(f'<rect x="6" y="0" width="22" height="{H}" fill="#FFFFFF"/>')                       # Castellana, wide
    o.append(f'<line x1="17" y1="0" x2="17" y2="{H}" stroke="{LINE}" stroke-width=".6" stroke-dasharray="3,2"/>')
    o.append(f'<rect x="0" y="12" width="{W}" height="11" fill="#FFFFFF"/>')                        # Concha Espina
    o.append(f'<rect x="158" y="0" width="10" height="{H}" fill="#FFFFFF"/>')                       # Padre Damián
    o.append(f'<rect x="0" y="150" width="{W}" height="9" fill="#FFFFFF"/>')                        # Rafael Salgado
    o.append(f'<text x="18.5" y="110" class="sn" transform="rotate(-90 18.5 110)">PASEO DE LA CASTELLANA</text>')
    o.append(f'<text x="95" y="19.4" class="sn" style="text-anchor:middle">AVENIDA DE CONCHA ESPINA</text>')
    o.append(f'<text x="164.6" y="95" class="sn" transform="rotate(90 164.6 95)" style="text-anchor:middle">CALLE PADRE DAMIÁN</text>')
    o.append(f'<text x="95" y="156.3" class="sn" style="text-anchor:middle">CALLE DE RAFAEL SALGADO</text>')
    # the stadium: steel skin, stands, pitch
    x0, y0, x1, y1 = 38.0, 31.0, 150.0, 143.0
    for k, (inset, col, sw) in enumerate([(0, STEEL, 1.4), (2.2, STEEL, .5), (4.4, STEEL, .5), (6.6, STEEL, .5)]):
        o.append(f'<rect x="{x0+inset}" y="{y0+inset}" width="{x1-x0-2*inset}" height="{y1-y0-2*inset}" rx="{30-inset}" fill="{"#DADDE2" if k == 0 else "none"}" stroke="{col}" stroke-width="{sw}"/>')
    o.append(f'<rect x="{x0+9}" y="{y0+9}" width="{x1-x0-18}" height="{y1-y0-18}" rx="22" fill="{STAND}" stroke="{STAND_E}" stroke-width=".6"/>')
    for k in range(1, 6):
        i = 9 + k * 3.4
        o.append(f'<rect x="{x0+i}" y="{y0+i}" width="{x1-x0-2*i}" height="{y1-y0-2*i}" rx="{max(4, 22-k*3.2)}" fill="none" stroke="{STAND_E}" stroke-width=".35"/>')
    px0, py0, px1, py1 = 70.0, 56.0, 118.0, 118.0
    o.append(f'<rect x="{px0}" y="{py0}" width="{px1-px0}" height="{py1-py0}" fill="#D9D3C6" stroke="#FFFFFF" stroke-width=".7"/>')
    o.append(f'<line x1="{px0}" y1="{(py0+py1)/2}" x2="{px1}" y2="{(py0+py1)/2}" stroke="#FFFFFF" stroke-width=".5"/>')
    o.append(f'<circle cx="{(px0+px1)/2}" cy="{(py0+py1)/2}" r="6" fill="none" stroke="#FFFFFF" stroke-width=".5"/>')
    o.append(f'<text x="{(px0+px1)/2}" y="{(py0+py1)/2 + 14}" class="lab" style="text-anchor:middle">the pitch:</text>')
    o.append(f'<text x="{(px0+px1)/2}" y="{(py0+py1)/2 + 17.6}" class="lab" style="text-anchor:middle">grass stored below</text>')
    o.append(f'<text x="{(px0+px1)/2}" y="{(py0+py1)/2 + 21.2}" class="lab" style="text-anchor:middle">except on match days</text>')
    o.append(f'<text x="94" y="{py0 - 4}" class="lab" style="text-anchor:middle;font-weight:700;fill:{NAVY}">ESTADIO SANTIAGO BERNABÉU</text>')
    # markers
    def dot(x, y, col, r=2.6):
        return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}" stroke="#fff" stroke-width=".7"/>'
    o.append(dot(37, 27.5, ZC["out"]))
    o.append(pill(41, 27.5, "Tour entrance · stops 1–3 outside", ZC["out"]))
    o.append(dot(151.5, 87, ZC["store"]))
    o.append(f'<line x1="151.5" y1="87" x2="146" y2="124" stroke="{ZC["store"]}" stroke-width=".4"/>')
    o.append(pill(148, 126, "27–28 · store and exit", ZC["store"], anchor="end"))
    # metro (closed) and S10 bus
    o.append(f'<circle cx="17" cy="132" r="3.4" fill="#fff" stroke="#9E2A2B" stroke-width=".8"/><text x="17" y="133.3" class="mt">M</text>')
    o.append(f'<line x1="14.6" y1="134.4" x2="19.4" y2="129.6" stroke="#9E2A2B" stroke-width=".8"/>')
    o.append(f'<text x="30" y="138.5" class="lab">Metro station:</text><text x="30" y="142" class="lab">closed until</text><text x="30" y="145.5" class="lab">early 2027</text>')
    o.append(f'<rect x="12.5" y="161.5" width="9" height="5.4" rx="1.2" fill="{NAVY}"/><text x="17" y="165.3" class="bus">S10</text>')
    o.append(f'<text x="24" y="165.2" class="lab">free replacement bus · Plaza de Lima</text>')
    # the walk back to the Castellana after the store
    o.append(f'<path d="M152,99 L160,108 L160,148 L150,154.5 L30,154.5 L20,160" fill="none" stroke="{GOLD}" stroke-width="1" stroke-dasharray="2,1.3"/>')
    o.append(f'<text x="100" y="147.8" class="lab" style="text-anchor:middle">after the tour: walk round to the Castellana</text>')
    # north arrow
    o.append(f'<g transform="translate(174 36)"><path d="M0,-6 L2.6,2 L0,0.6 L-2.6,2 Z" fill="{NAVY}"/><text x="0" y="7" class="lab" style="text-anchor:middle;font-weight:700">N</text></g>')
    o.append("</svg>")
    return "".join(o)

def stop_rows():
    rows = []
    for t in TR:
        n = int(t["seq"]); z = zone_key(t["room"]); c = ZC[z]
        title = t["title"].split(" · ", 1)[1] if " · " in t["title"] else t["title"]
        title = title.replace("Extra · ", "")
        zone = t["room"].replace(" · ", ", ").replace("Panoramic view, third tier", "Top tier")
        dotc = f'<span class="dot hol" style="color:{c};border-color:{c}">{n}</span>' if n in XS else f'<span class="dot" style="background:{c}">{n}</span>'
        ex = f'<i style="color:{c}">Extra</i> ' if n in XS else ""
        tick = lambda s: '<span class="tk">●</span>' if n in s else '<span class="tk off">·</span>'
        rows.append(f'<div class="row">{dotc}<span class="tt">{ex}{esc(title)}<span class="zn">{esc(zone)}</span></span>'
                    f'<span class="tk">●</span>{tick(ESSENTIAL)}{tick(HIGHLIGHTS)}</div>')
    return "".join(rows)

pages = [
f'''<section class="page">
 <header><div class="brand">YO TOURS · AUDIO GUIDE</div><h1>Estadio Santiago Bernabéu</h1>
 <p class="lede">Your route through the stadium: from the street to the top of the stands, down through the museum to pitch level, and out through the store.</p></header>
 <div class="fig">{section_svg()}</div>
 <div class="lens">{length_cards()}</div>
 <div class="note"><b>Match day, or the day before?</b> The dressing room and benches are closed: after the museum, play 22, then 27 and 28.
 <b>Sent to the museum first?</b> Play 1–3, then 9–22, then 4–8, then 23 onwards. The tracks remind you at each step.</div>
 <footer>A drawing of the stadium in section, not to scale. Where each zone sits inside the stands is indicative: the club can change the route, and staff show the way.</footer>
</section>''',
f'''<section class="page">
 <header class="fh"><div class="brand">YO TOURS · ESTADIO SANTIAGO BERNABÉU</div><h2>Around the stadium</h2>
 <p class="sub">The tour starts at the corner of the Castellana and Concha Espina and ends in the store on the opposite side, on Calle Padre Damián.</p></header>
 <div class="fig">{aerial_svg()}</div>
 <footer>A drawing from above, north at the top, not to scale. Check the door number on the signs at the entrance.</footer>
</section>''',
f'''<section class="page">
 <header class="fh"><div class="brand">YO TOURS · ESTADIO SANTIAGO BERNABÉU</div><h2>Every stop, in three lengths</h2>
 <p class="sub">Stop numbers are the track numbers on your phone. Full tour about {MIN({int(t["seq"]) for t in TR})} min · Essential about {MIN(ESSENTIAL)} min · Highlights about {MIN(HIGHLIGHTS)} min.</p></header>
 <div class="th"><span></span><span>Stop</span><span>Full</span><span>Essential</span><span>Highlights</span></div>
 <div class="list">{stop_rows()}</div>
 <footer>Yo Tours · edition of 23 October 2026 · hollow circles are short, optional Extras</footer>
</section>''']

CSS = f'''
@page {{ size: A4; margin: 0 }} * {{ box-sizing: border-box }}
html, body {{ margin: 0; background: {PAPER}; color: {INK}; font-family: Inter, "DejaVu Sans", sans-serif }}
.page {{ width: 210mm; height: 297mm; padding: 13mm 14mm 10mm; position: relative; page-break-after: always; overflow: hidden; background: {PAPER} }}
.brand {{ font: 600 7.6pt Inter; letter-spacing: .28em; color: {GOLD} }}
h1 {{ font: 700 29pt Lora, serif; margin: 2mm 0 1mm }} h2 {{ font: 700 21pt Lora, serif; margin: 2mm 0 1mm }}
.lede {{ font: 400 11pt Lora, serif; color: {MUTED}; margin: 0 0 4mm; line-height: 1.4 }}
.sub {{ font: 400 9.4pt Inter; color: {MUTED}; margin: 0 0 4mm; line-height: 1.4 }}
.fig {{ background: #fff; border: .3mm solid {LINE}; border-radius: 4mm; padding: 2mm 0; overflow: hidden }}
.fig svg {{ display: block; margin: 0 auto }}
.lab {{ font: 500 2.75px Inter; fill: {MUTED} }} .st {{ font: 600 2.9px Inter; fill: {INK} }}
.sn {{ font: 700 2.9px Inter; fill: #A39886; letter-spacing: .35px }}
.pt {{ font: 700 3.3px Inter; fill: #fff; text-anchor: middle }} .ps {{ font: 600 3.0px Inter; fill: {INK} }}
.mt {{ font: 700 3.2px Inter; fill: #9E2A2B; text-anchor: middle }} .bus {{ font: 700 3px Inter; fill: #fff; text-anchor: middle }}
.lens {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 3mm; margin-top: 4mm }}
.len {{ background: {NAVY}; color: #fff; border-radius: 3mm; padding: 3mm 3.5mm }}
.lt {{ font: 700 12pt Lora }} .lm {{ font: 700 8pt Inter; color: #E5C88F; margin: .8mm 0 }} .ld {{ font: 400 7.8pt Inter; color: #DDE2EA; line-height: 1.35 }}
.note {{ margin-top: 3.5mm; font: 400 8.2pt Inter; line-height: 1.45; background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; padding: 2.6mm 3.5mm }}
.note b {{ color: {NAVY} }}
footer {{ position: absolute; left: 14mm; right: 14mm; bottom: 7mm; font: 400 7pt Inter; color: {MUTED}; border-top: .3mm solid {LINE}; padding-top: 2mm }}
.th, .row {{ display: grid; grid-template-columns: 9mm 1fr 15mm 18mm 20mm; align-items: center }}
.th {{ font: 700 7.4pt Inter; color: {MUTED}; padding-bottom: 1.2mm; border-bottom: .4mm solid {INK} }} .th span:nth-child(n+3) {{ text-align: center }}
.row {{ padding: .55mm 0; border-bottom: .25mm solid {LINE} }}
.dot {{ width: 5.4mm; height: 5.4mm; border-radius: 50%; color: #fff; font: 700 7.8pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.hol {{ background: #fff; border: .45mm solid }}
.tt {{ font: 600 8.6pt Inter; line-height: 1.25 }} .tt i {{ font-style: normal; font-weight: 700; font-size: 7pt; margin-right: 1mm }}
.zn {{ display: block; font: 400 7pt Inter; color: {MUTED} }}
.tk {{ text-align: center; color: {NAVY}; font-size: 9pt }} .tk.off {{ color: {LINE} }}
'''
doc = f'<!doctype html><html><head><meta charset="utf-8"><title>Bernabéu · Yo Tours route</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
hp = os.path.join(B, "route_map.html"); open(hp, "w", encoding="utf-8").write(doc)

async def render():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        br = await p.chromium.launch(); pg = await br.new_page()
        await pg.goto("file://" + os.path.abspath(hp)); await pg.wait_for_timeout(300)
        await pg.pdf(path=OUT_PDF, format="A4", print_background=True, margin=dict(top="0", bottom="0", left="0", right="0"))
        if PNG_DIR:
            os.makedirs(PNG_DIR, exist_ok=True); await pg.set_viewport_size({"width": 794, "height": 1123})
            for i, el in enumerate(await pg.query_selector_all(".page")):
                await el.screenshot(path=os.path.join(PNG_DIR, f"route_p{i+1}.png"), scale="device")
        await br.close()
asyncio.run(render())
os.remove(hp)
print("OK ->", OUT_PDF, len(pages), "pages")
