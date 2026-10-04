#!/usr/bin/env python3
"""Traveller navigation PDF for Tour #43 (V5.1). Cloned from the Tour #49 route-map pattern (house palette,
header band, zone bands), driven by the bundle's plan.json so numbers always match the audio files.
Page 1: how to use, current notices, route at a glance. Then per track: number, room (with the name on the
museum's own signs), title, where to stand (the @where card) and approximate length.
Shared with travellers alongside the MP3s; works printed or offline on a phone."""
import json, os, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_RIGHT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Flowable, KeepTogether
from xml.sax.saxutils import escape

B = sys.argv[1]; OUT = os.path.join(B, "Palazzo_Pitti_Audio_Guide_Route.pdf")
plan = json.load(open(os.path.join(B, "plan.json")))
CREAM, INK, INK_SOFT = HexColor('#F2F1EA'), HexColor('#1F1F1F'), HexColor('#565650')
CRIMSON, CRIM_LIGHT, GREY_LN = HexColor('#A4161A'), HexColor('#C9444A'), HexColor('#C4C2B8')
ZTINTS = [HexColor(h) for h in ('#EEEBE1', '#E8E6DC', '#E2E0D6', '#DCDAD0', '#E6E4DA', '#E0DED4', '#EEEBE1', '#E8E6DC')]
tr = plan["tracks"]

def seqs(pred):
    s = [t["seq"] for t in tr if pred(t)]
    return (s[0] + "–" + s[-1]) if len(s) > 1 else (s[0] if s else "?")
def room(r): return lambda t: t["folder"] == "01_Palatine_Gallery" and t["room"] == r
def folder(f): return lambda t: t["folder"] == f

# Palatine room numbers -> the room's name as on the museum's signs (official one-way route, G6_ROUTE §1.2)
SIGN = {"Rooms 1–2": "Galleria delle Statue", "Room 3": "Sala Castagnoli", "Room 14": "Sala di Prometeo",
        "Room 19": "Sala di Ulisse", "Room 21": "Sala dell'Educazione di Giove", "Room 22": "Sala della Stufa",
        "Room 23": "Sala dell'Iliade", "Room 24": "Sala di Saturno", "Room 25": "Sala di Giove",
        "Room 26": "Sala di Marte", "Room 27": "Sala di Apollo", "Room 28": "Sala di Venere"}

ZONE = {
 "00_Welcome": ("Before you go in", "Ground", "Piazza Pitti, facing the palace. The ticket office is on the right of the façade."),
 "01_Palatine_Gallery": ("Palatine Gallery", "First floor",
   "The museum's one-way route: Rooms 1–3, the inner rooms (14–23), then the five Planet Rooms from Saturn (24) to Venus (28). "
   "You leave through the Sala delle Nicchie. Room names are on the signs above the doors. The Volterrano Wing (Rooms 4–11), "
   "to the right of the Castagnoli Room, is often closed for restoration and has no tracks. Stairs and lifts are on the right "
   "side of the Ammannati Courtyard."),
 "02_Imperial_and_Royal_Apartments": ("Imperial & Royal Apartments", "First floor",
   "Staff-led group visit of about 30 minutes, from the Palatine entrance atrium, at set times. Play "
   + seqs(folder("02_Imperial_and_Royal_Apartments")).replace("–", " while you wait and ") + " afterwards. Don't play audio during the visit."),
 "03_Gallery_of_Modern_Art": ("Gallery of Modern Art", "Second floor", "From the landing, follow the corridor to the left. Rooms are numbered; the loop runs from Room 1 to Room 30."),
 "04_Museum_of_Fashion_and_Costume": ("Museum of Fashion & Costume", "Second floor",
   "Palazzina della Meridiana: back to the landing, corridor to the right, a staircase of two short flights "
   "(stair-lift available). A dead end: leave the way you came. Displays rotate, so the tracks avoid room-by-room claims."),
 "05_Russian_Icons_and_Palatine_Chapel": ("Russian Icons & Palatine Chapel", "Ground floor", "Off the Ammannati Courtyard. Follow the signs for the Palatine Chapel."),
 "06_Boboli_Gardens": ("Boboli Gardens", "Garden", "Up from the back of the courtyard. Can be done before the palace. Stops in walking "
   "order: east past the grottoes, uphill to the amphitheatre and the top of the hill, then down the cypress avenue to the Isolotto. "
   "Some areas are fenced for the Boboli 2030 restoration but visible from the paths."),
 "07_Closing": ("Closing", "Anywhere", "Anywhere you like, once you've finished."),
}
SHORT = {"00_Welcome": "Piazza", "01_Palatine_Gallery": "Palatine Gallery", "02_Imperial_and_Royal_Apartments": "Royal Apartments",
         "03_Gallery_of_Modern_Art": "Modern Art", "04_Museum_of_Fashion_and_Costume": "Fashion & Costume",
         "05_Russian_Icons_and_Palatine_Chapel": "Icons & Chapel", "06_Boboli_Gardens": "Boboli Gardens", "07_Closing": "Closing"}
# headline stops (red badges): mapped from the V5.0 set via v5/RENUMBER_5OCT2026.md
STAR = {"001", "004", "006", "008", "011", "013", "015", "020", "021", "022", "025", "029", "032", "038", "044", "051", "053", "058"}

S_TITLE = ParagraphStyle('t', fontName='Times-Bold', fontSize=23, leading=25, textColor=CREAM)
S_SUB = ParagraphStyle('s', fontName='Times-Italic', fontSize=11.5, leading=14, textColor=CRIM_LIGHT)
S_LOC = ParagraphStyle('l', fontName='Helvetica', fontSize=7, leading=10, textColor=HexColor('#BFBDB2'))
S_PILL = ParagraphStyle('p', fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=CRIM_LIGHT, alignment=TA_RIGHT)
S_META = ParagraphStyle('m', fontName='Times-Italic', fontSize=10.5, leading=13, textColor=CRIM_LIGHT, alignment=TA_RIGHT)
S_NOTE = ParagraphStyle('nt', fontName='Helvetica', fontSize=7.9, leading=10.4, textColor=INK)
S_H2 = ParagraphStyle('h2', fontName='Times-Bold', fontSize=12.5, leading=15, textColor=CRIMSON)
S_ZONE = ParagraphStyle('z', fontName='Times-Bold', fontSize=12.5, leading=15, textColor=CRIMSON)
S_CUE = ParagraphStyle('c', fontName='Times-Italic', fontSize=9, leading=11, textColor=INK_SOFT)
S_ROOM = ParagraphStyle('r', fontName='Helvetica-Bold', fontSize=7, leading=8.6, textColor=INK_SOFT)
S_NAME = ParagraphStyle('n', fontName='Helvetica-Bold', fontSize=8.2, leading=9.8, textColor=INK)
S_WHERE = ParagraphStyle('w', fontName='Helvetica', fontSize=7.4, leading=9.2, textColor=INK)
S_MIN = ParagraphStyle('mi', fontName='Helvetica', fontSize=7, leading=8.6, textColor=INK_SOFT, alignment=TA_CENTER)

class Badge(Flowable):
    def __init__(self, n, star):
        Flowable.__init__(self); self.n, self.star = n, star; self.width = self.height = 0.7*cm
    def draw(self):
        c = self.canv; r = self.width/2
        c.setFillColor(CRIMSON if self.star else INK); c.circle(r, r, r, stroke=0, fill=1)
        c.setFillColor(CREAM); c.setFont('Times-Bold', 8.5); c.drawCentredString(r, r-3.0, self.n)

class RouteFlow(Flowable):
    """Route at a glance: the eight sections as boxes in walking order, two rows, snaking."""
    def __init__(self, width, items):
        Flowable.__init__(self); self.width, self.items = width, items; self.height = 4.3*cm
    def draw(self):
        c = self.canv; n = len(self.items); per = (n + 1) // 2
        gap = 0.55*cm; bw = (self.width - gap*(per-1)) / per; bh = 1.65*cm
        pos = []
        for i in range(n):
            row, col = divmod(i, per)
            if row == 1: col = per - 1 - col          # snake back on the second row
            x = col*(bw+gap); y = self.height - bh - row*(bh+0.75*cm)
            pos.append((x, y))
        c.setStrokeColor(CRIMSON); c.setFillColor(CRIMSON); c.setLineWidth(1.2)
        for i in range(n-1):
            (x1, y1), (x2, y2) = pos[i], pos[i+1]
            if y1 == y2:
                xa, xb = (x1+bw, x2) if x2 > x1 else (x1, x2+bw); ym = y1 + bh/2
                c.line(xa, ym, xb, ym); d = 1 if xb > xa else -1
                c.line(xb, ym, xb-d*4, ym+3); c.line(xb, ym, xb-d*4, ym-3)
            else:
                xm = x1 + bw/2; c.line(xm, y1, xm, y2+bh); c.line(xm, y2+bh, xm-3, y2+bh+4); c.line(xm, y2+bh, xm+3, y2+bh+4)
        for (x, y), (label, floor, rng, mins) in zip(pos, self.items):
            c.setFillColor(HexColor('#F7F6F1')); c.setStrokeColor(HexColor('#8E8A7C')); c.setLineWidth(0.6)
            c.roundRect(x, y, bw, bh, 4, stroke=1, fill=1)
            c.setFillColor(CRIMSON); c.setFont('Times-Bold', 9.5); c.drawCentredString(x+bw/2, y+bh-12, label)
            c.setFillColor(INK_SOFT); c.setFont('Helvetica', 6.8); c.drawCentredString(x+bw/2, y+bh-22, floor.upper())
            c.setFillColor(INK); c.setFont('Helvetica-Bold', 8); c.drawCentredString(x+bw/2, y+11, f"Tracks {rng}")
            c.setFillColor(INK_SOFT); c.setFont('Helvetica', 6.8); c.drawCentredString(x+bw/2, y+3.5, f"about {mins} min of audio")

def minutes(words):  # same basis as plan.json total_min: 125 words a minute
    return max(1, round(words / 125))

def box(html, W):
    t = Table([[Paragraph(html, S_NOTE)]], colWidths=[W])
    t.setStyle(TableStyle([('BOX', (0,0), (-1,-1), 0.8, CRIMSON), ('BACKGROUND', (0,0), (-1,-1), HexColor('#F7F6F1')),
        ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8), ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6)]))
    return t

def build():
    W = A4[0] - 3.0*cm
    doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=1.5*cm, rightMargin=1.5*cm, topMargin=0.95*cm,
        bottomMargin=1.1*cm, title="Palazzo Pitti + Boboli — Audio Guide Route", author="Humanized Audio Guide",
        subject="Walking order, room names and where to stand for each audio track, Tour No. 43")
    st = []
    total = plan["total_min"]; hrs = f"{total // 60} hours {round(total % 60 / 5) * 5} minutes" if total >= 60 else f"{total} minutes"
    left = [Paragraph("PALAZZO PITTI + BOBOLI", S_TITLE),
            Paragraph("Audio guide route · which track to play, and where", S_SUB), Spacer(1, 3),
            Paragraph("FLORENCE · OLTRARNO · ENGLISH · OCTOBER 2026", S_LOC)]
    right = [Paragraph("TOUR NO. 43", S_PILL), Paragraph(f"{len(tr)} tracks<br/>about {total} min of audio", S_META)]
    h = Table([[left, right]], colWidths=[W*0.68, W*0.32])
    h.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), INK), ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 14), ('RIGHTPADDING', (0,0), (-1,-1), 14),
        ('TOPPADDING', (0,0), (-1,-1), 9), ('BOTTOMPADDING', (0,0), (-1,-1), 9)]))
    st += [h, Spacer(1, 8)]

    st += [Paragraph("How to use this guide", S_H2), Spacer(1, 2), box(
        "<b>1. Download before you go.</b> The tracks are ordinary MP3 files: they play offline, with no app and no signal needed. "
        "Bring earphones.<br/>"
        "<b>2. Play the tracks in number order.</b> The numbers follow the museum's own one-way route, and match the file names.<br/>"
        "<b>3. Start each track where this sheet says to stand.</b> In the Palatine Gallery, the room number and the room's "
        "Italian name are the ones on the signs above the doors, e.g. <i>Room 24 · Sala di Saturno</i>.<br/>"
        "<b>4. Every track ends by telling you where to go next.</b> Pause, walk, then play the next number when you arrive.<br/>"
        "<b>5. Skip freely.</b> If a painting is away on loan or a room is closed, move on to the next number. Paintings are "
        "sometimes moved: an attendant can tell you where a work is today. Red numbers mark the highlights if you are short of time.", W),
        Spacer(1, 8)]

    jup, sat, ili = seqs(room("Room 25")), seqs(room("Room 24")), seqs(room("Room 23"))
    mars_first = [t["seq"] for t in tr if room("Room 26")(t)][0]
    stufa = seqs(room("Room 22"))
    st += [Paragraph("Notices for October 2026", S_H2), Spacer(1, 2), box(
        f"<b>Iliad Room (Room 23) closed until 25 October 2026.</b> At the Sala della Stufa (track {stufa}), staff send visitors "
        f"back toward the Room of Jupiter. Then play {jup} in Jupiter, {sat} in Saturn, and carry on from {mars_first}. Skip {ili}.<br/>"
        "<b>Royal Apartments.</b> Guided visits only, at set times, for small groups. If your slot comes before the Palatine Gallery, "
        f"play {seqs(folder('02_Imperial_and_Royal_Apartments'))} around it and pick up the Palatine where you left off.<br/>"
        "<b>Boboli Gardens.</b> Parts of the garden are fenced off during the Boboli 2030 restoration, including the Amphitheatre "
        "tiers, the Neptune basin, the Abundance statue, the inner Isolotto and the Limonaia gates. Everything on the route can "
        "still be seen from the paths, and the tracks tell you where.", W), Spacer(1, 10)]

    items = []
    for s in plan["sections"]:
        fo = s["folder"]; ts = [t for t in tr if t["folder"] == fo]
        items.append((SHORT[fo], ZONE[fo][1], seqs(folder(fo)), sum(minutes(t["words"]) for t in ts)))
    st += [Paragraph("The route at a glance", S_H2), Spacer(1, 4), RouteFlow(W, items), Spacer(1, 4),
           Paragraph("The Boboli Gardens can also be done first, straight from the back of the courtyard. "
                     "Allow at least half a day for everything; the audio alone runs about " + hrs + ".", S_CUE)]

    for zi, s in enumerate(plan["sections"]):
        fo = s["folder"]; label, floor, cue = ZONE[fo]; tint = ZTINTS[zi % len(ZTINTS)]
        rows = []
        for t in [t for t in tr if t["folder"] == fo]:
            rm = "" if fo in ("00_Welcome", "07_Closing") else t["room"]
            if fo == "01_Palatine_Gallery" and rm in SIGN: rm = f"{rm} · {SIGN[rm]}"
            rows.append([Badge(t["seq"], t["seq"] in STAR),
                         [Paragraph(escape(rm.upper()), S_ROOM), Paragraph(escape(t["title"]), S_NAME)],
                         Paragraph(escape(t["where"]), S_WHERE),
                         Paragraph(f"{minutes(t['words'])} min", S_MIN)])
        cw = [1.0*cm, W*0.33, W - 1.0*cm - W*0.33 - 1.1*cm, 1.1*cm]
        tb = Table(rows, colWidths=cw, repeatRows=0)
        tb.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BACKGROUND', (0,0), (-1,-1), tint),
            ('LINEBELOW', (0,0), (-1,-2), 0.4, GREY_LN), ('BOX', (0,0), (-1,-1), 0.6, HexColor('#8E8A7C')),
            ('LEFTPADDING', (0,0), (-1,-1), 5), ('RIGHTPADDING', (0,0), (-1,-1), 5),
            ('TOPPADDING', (0,0), (-1,-1), 3.5), ('BOTTOMPADDING', (0,0), (-1,-1), 4)]))
        head = [Spacer(1, 6), Paragraph(escape(f"{label} · {floor}") if floor not in ("Anywhere",) else escape(label), S_ZONE),
                Paragraph(escape(cue), S_CUE), Spacer(1, 3)]
        if len(rows) <= 6:
            st.append(KeepTogether(head + [tb]))
        else:
            st += head; st.append(tb)
    def bg(canv, d):
        canv.saveState(); canv.setFillColor(CREAM); canv.rect(0, 0, A4[0], A4[1], stroke=0, fill=1)
        canv.setFont('Helvetica', 6.8); canv.setFillColor(INK_SOFT)
        canv.drawString(1.5*cm, 0.55*cm, "Tour No. 43 · Palazzo Pitti + Boboli · audio guide route · placements checked October 2026 · rooms can change: ask an attendant")
        canv.drawRightString(A4[0]-1.5*cm, 0.55*cm, f"{d.page}")
        canv.restoreState()
    doc.build(st, onFirstPage=bg, onLaterPages=bg)
    print("built", OUT)
build()
