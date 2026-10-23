#!/usr/bin/env python3
"""Yo Tours · Estadio Santiago Bernabéu — route sheet, edition of 23 Oct 2026.
The club publishes no floor plan of the tour and no stop numbers, so this is a schematic of the route by zone (not a plan
to scale): page 1 = the visit as a vertical flow with every stop number, the three cases (full tour / match day /
museum first); page 2 = the stop list with where each one is played.
Driven by plan.json, so the stop numbers always match the audio files.
Usage: python3 route_map.py <bundle folder> [--png <dir>]   -> <bundle>/Bernabeu_Audio_Guide_Route.pdf"""
import json, os, sys, html, asyncio

B = sys.argv[1]
PNG_DIR = sys.argv[sys.argv.index("--png") + 1] if "--png" in sys.argv else None
plan = json.load(open(os.path.join(B, "plan.json"), encoding="utf-8")); TR = plan["tracks"]
XS = {int(t["seq"]) for t in TR if t.get("register") == "X"}
MAIN = len(TR) - len(XS)
OUT_PDF = os.path.join(B, "Bernabeu_Audio_Guide_Route.pdf")
PAPER, INK, MUTED, LINE, GOLD, NAVY = "#F6F1E7", "#1F1B17", "#776E62", "#D8CEBD", "#A9812F", "#1D2B4A"
ZONES = [  # (zone @room prefix, label, where, colour, closed on match days?)
    ("Outside", "Outside", "Paseo de la Castellana and Avenida de Concha Espina, before you go in", "#5B6B2E", False),
    ("Panoramic", "Panoramic view", "Top tier of the stands: the whole bowl, the model, the roof and the screen ring", "#2C4A6E", False),
    ("Museum", "Museum", "The club's story and the trophy hall: the row of fifteen European Cups, the Ballon d'Or display", "#8C1C13", False),
    ("Dressing room", "Dressing room", "The first team's home dressing room", "#6A3A6B", True),
    ("Benches", "Benches", "Pitch level, at the dugouts", "#6A3A6B", True),
    ("Press room", "Press room", "The room where coaches face the press after matches", "#776E62", True),
    ("Store", "Store", "Where the tour ends", "#A4581B", False),
    ("Exit", "Way out", "Back to the street", "#A4581B", False),
]
def zone_of(t):
    for z in ZONES:
        if t["room"].startswith(z[0]): return z
    return ZONES[0]
def esc(s): return html.escape(s, quote=True)
def short(t):
    x = t["title"]
    if " · " in x: x = x.split(" · ", 1)[1]
    return x.replace("Extra · ", "")

def dots(z):
    out = []
    for t in TR:
        if zone_of(t)[0] != z[0]: continue
        n = int(t["seq"])
        cls = "dot hol" if n in XS else "dot"
        sty = f"color:{z[3]};border-color:{z[3]}" if n in XS else f"background:{z[3]}"
        out.append(f'<span class="{cls}" style="{sty}">{n}</span>')
    return "".join(out)

flow = []
for i, z in enumerate(ZONES):
    if not any(zone_of(t)[0] == z[0] for t in TR): continue
    tag = '<span class="closed">closed on match days and the day before</span>' if z[4] and z[0] != "Press room" else ""
    if z[0] == "Press room": tag = '<span class="closed">only when open</span>'
    flow.append(f'<div class="zone" style="border-left-color:{z[3]}"><div class="zt" style="color:{z[3]}">{esc(z[1])} {tag}</div>'
                f'<div class="zw">{esc(z[2])}</div><div class="zd">{dots(z)}</div></div>')
    flow.append('<div class="arrow">▼</div>')
flow = "".join(flow[:-1])

cases = f'''<div class="cases">
 <div class="case"><b>A · Full tour</b>Play 1 to {len(TR)} in order. Hollow circles are short, optional Extras.</div>
 <div class="case"><b>B · Match day, or the day before</b>Dressing room and benches are closed. After the museum, play 22, then 27 and 28.</div>
 <div class="case"><b>C · Museum first</b>If staff send you to the museum before the view: play 1–3, then 9–22, then 4–8, then 23 onwards.</div>
</div>'''

def stop_rows(lo, hi):
    rows = []
    for t in TR:
        n = int(t["seq"])
        if not lo <= n <= hi: continue
        z = zone_of(t)
        if n in XS:
            rows.append(f'<div class="row x"><span class="dot hol" style="color:{z[3]};border-color:{z[3]}">{n}</span><span class="rm">{esc(z[1])}</span>'
                        f'<span class="tt"><i style="color:{z[3]}">Extra</i> {esc(short(t))}</span></div>')
        else:
            rows.append(f'<div class="row"><span class="dot" style="background:{z[3]}">{n}</span><span class="rm">{esc(z[1])}</span><span class="tt">{esc(short(t))}</span></div>')
    return "".join(rows)

pages = [f'''<section class="page">
 <header><div class="brand">YO TOURS · AUDIO GUIDE</div><h1>Estadio Santiago Bernabéu</h1>
 <p class="lede">The Tour Bernabéu in {MAIN} stops, about an hour of listening, plus {len(XS)} short Extras. Allow about two hours: the route has many stairs.</p></header>
 <div class="flow">{flow}</div>
 {cases}
 <footer>A schematic of the route by zone, not a floor plan. The club can change the route for matches and events: staff at each zone show the way. The pitch is usually stored underground, so expect a bare floor.</footer>
</section>''',
f'''<section class="page">
 <header class="fh"><div class="brand">YO TOURS · ESTADIO SANTIAGO BERNABÉU</div><h2>Every stop</h2>
 <p class="sub">Stop numbers = track numbers on your phone. Each track ends by telling you where the route goes next.</p></header>
 <div class="list">{stop_rows(1, len(TR))}</div>
 <footer>Yo Tours · edition of 23 October 2026</footer>
</section>''']

CSS = f'''
@page {{ size: A4; margin: 0 }} * {{ box-sizing: border-box }}
html, body {{ margin: 0; background: {PAPER}; color: {INK}; font-family: Inter, "DejaVu Sans", sans-serif }}
.page {{ width: 210mm; height: 297mm; padding: 13mm 14mm 10mm; position: relative; page-break-after: always; overflow: hidden; background: {PAPER} }}
.brand {{ font: 600 7.6pt Inter; letter-spacing: .28em; color: {GOLD} }}
h1 {{ font: 700 29pt Lora, serif; margin: 2mm 0 1mm }} h2 {{ font: 700 20pt Lora, serif; margin: 2mm 0 1mm }}
.lede {{ font: 400 11pt Lora, serif; color: {MUTED}; margin: 0 0 4mm }} .sub {{ font: 400 9.4pt Inter; color: {MUTED}; margin: 0 0 4mm }}
.flow {{ display: flex; flex-direction: column; align-items: stretch }}
.zone {{ background: #fff; border: .3mm solid {LINE}; border-left: 2.2mm solid; border-radius: 3mm; padding: 2.2mm 3.5mm }}
.zt {{ font: 700 11pt Lora }} .zw {{ font: 400 8pt Inter; color: {MUTED}; margin: .6mm 0 1.4mm }}
.closed {{ font: 600 6.8pt Inter; color: #fff; background: {MUTED}; border-radius: 2mm; padding: .3mm 1.6mm; margin-left: 2mm; vertical-align: middle }}
.zd {{ display: flex; flex-wrap: wrap; gap: 1.4mm }}
.arrow {{ text-align: center; color: {GOLD}; font-size: 8pt; line-height: 1; margin: .7mm 0 }}
.dot {{ width: 6.2mm; height: 6.2mm; border-radius: 50%; color: #fff; font: 700 8pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.hol {{ background: #fff; border: .45mm solid }}
.cases {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.5mm; margin-top: 4mm }}
.case {{ background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; padding: 2.4mm 3mm; font: 400 8pt Inter; line-height: 1.35 }}
.case b {{ display: block; font: 700 8.6pt Inter; color: {NAVY}; margin-bottom: .8mm }}
footer {{ position: absolute; left: 14mm; right: 14mm; bottom: 7mm; font: 400 7pt Inter; color: {MUTED}; border-top: .3mm solid {LINE}; padding-top: 2mm }}
.list {{ columns: 2; column-gap: 7mm }} .row {{ break-inside: avoid; display: grid; grid-template-columns: 8mm 24mm 1fr; align-items: center; padding: 1.2mm 0; border-bottom: .25mm solid {LINE} }}
.rm {{ font: 600 7.3pt Inter; color: {MUTED} }} .tt {{ font: 500 8.2pt Inter; line-height: 1.3 }} .row.x .tt {{ color: {MUTED} }}
.tt i {{ font-style: normal; font-weight: 700; font-size: 7pt; margin-right: 1mm }}
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
