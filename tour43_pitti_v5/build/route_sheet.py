#!/usr/bin/env python3
"""Route sheet for Tour #43 V5 test build. Cloned from the Tour #49 route-map pattern (house palette,
header band, zone bands), driven by the bundle's plan.json so numbers always match the audio files.
Per track: number, room, title, and where to stand (the @where card)."""
import json, os, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_RIGHT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Flowable, KeepTogether
from xml.sax.saxutils import escape

B = sys.argv[1]; OUT = os.path.join(B, "Palazzo_Pitti_V5_Route_Sheet.pdf")
plan = json.load(open(os.path.join(B, "plan.json")))
CREAM, INK, INK_SOFT = HexColor('#F2F1EA'), HexColor('#1F1F1F'), HexColor('#565650')
CRIMSON, CRIM_LIGHT, GREY_LN = HexColor('#A4161A'), HexColor('#C9444A'), HexColor('#C4C2B8')
ZTINTS = [HexColor(h) for h in ('#EEEBE1', '#E8E6DC', '#E2E0D6', '#DCDAD0', '#E6E4DA', '#E0DED4', '#EEEBE1', '#E8E6DC')]

ZONE = {
 "00_Welcome": ("Before you go in", "Piazza Pitti, facing the palace. The ticket office is on the right of the façade."),
 "01_Palatine_Gallery": ("Palatine Gallery · first floor",
   "The museum's one-way route: Rooms 1–3, the Volterrano Wing (4–11), the inner rooms (14–23), then the five "
   "Planet Rooms from Saturn (24) to Venus (28). You leave through the Sala delle Nicchie. Stairs and lifts are on "
   "the right side of the Ammannati Courtyard."),
 "02_Imperial_and_Royal_Apartments": ("Imperial & Royal Apartments · first floor",
   "Staff-led group visit of about 30 minutes, from the Palatine entrance atrium. Play 047 while you wait and 048 "
   "afterwards. Don't play audio during the visit."),
 "03_Gallery_of_Modern_Art": ("Gallery of Modern Art · second floor", "From the landing, follow the corridor to the left."),
 "04_Museum_of_Fashion_and_Costume": ("Museum of Fashion & Costume · second floor",
   "Palazzina della Meridiana: back to the landing, corridor to the right, a staircase of two short flights "
   "(stair-lift available). A dead end: leave the way you came. Displays rotate, so the tracks avoid room-by-room claims."),
 "05_Russian_Icons_and_Palatine_Chapel": ("Russian Icons & Palatine Chapel · ground floor", "Off the Ammannati Courtyard."),
 "06_Boboli_Gardens": ("Boboli Gardens", "Up from the back of the courtyard. Can be done before the palace. Stops in walking "
   "order, uphill first, then down the Viottolone. Some areas are fenced for the Boboli 2030 restoration but visible from the paths."),
 "07_Closing": ("Closing", "Anywhere you like, once you've finished."),
}
STAR = {"001", "004", "016", "020", "023", "025", "027", "032", "033", "034", "038", "043", "046", "052", "061", "068", "070", "076"}

S_TITLE = ParagraphStyle('t', fontName='Times-Bold', fontSize=23, leading=25, textColor=CREAM)
S_SUB = ParagraphStyle('s', fontName='Times-Italic', fontSize=11.5, leading=14, textColor=CRIM_LIGHT)
S_LOC = ParagraphStyle('l', fontName='Helvetica', fontSize=7, leading=10, textColor=HexColor('#BFBDB2'))
S_PILL = ParagraphStyle('p', fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=CRIM_LIGHT, alignment=TA_RIGHT)
S_META = ParagraphStyle('m', fontName='Times-Italic', fontSize=10.5, leading=13, textColor=CRIM_LIGHT, alignment=TA_RIGHT)
S_NOTE = ParagraphStyle('nt', fontName='Helvetica', fontSize=7.8, leading=10.2, textColor=INK)
S_ZONE = ParagraphStyle('z', fontName='Times-Bold', fontSize=12.5, leading=15, textColor=CRIMSON)
S_CUE = ParagraphStyle('c', fontName='Times-Italic', fontSize=9, leading=11, textColor=INK_SOFT)
S_ROOM = ParagraphStyle('r', fontName='Helvetica-Bold', fontSize=7, leading=8.6, textColor=INK_SOFT)
S_NAME = ParagraphStyle('n', fontName='Helvetica-Bold', fontSize=8.2, leading=9.8, textColor=INK)
S_WHERE = ParagraphStyle('w', fontName='Helvetica', fontSize=7.4, leading=9.2, textColor=INK)
S_FOOT = ParagraphStyle('f', fontName='Helvetica', fontSize=6.8, leading=8.5, textColor=INK_SOFT)

class Badge(Flowable):
    def __init__(self, n, star):
        Flowable.__init__(self); self.n, self.star = n, star; self.width = self.height = 0.7*cm
    def draw(self):
        c = self.canv; r = self.width/2
        c.setFillColor(CRIMSON if self.star else INK); c.circle(r, r, r, stroke=0, fill=1)
        c.setFillColor(CREAM); c.setFont('Times-Bold', 8.5); c.drawCentredString(r, r-3.0, self.n)

def build():
    tr = plan["tracks"]; W = A4[0] - 3.0*cm
    doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=1.5*cm, rightMargin=1.5*cm, topMargin=0.95*cm,
        bottomMargin=1.1*cm, title="Palazzo Pitti + Boboli — V5 Route Sheet", author="Humanized Audio Guide",
        subject="Walking order and where to stand for each track, Tour No. 43 V5 test build")
    st = []
    left = [Paragraph("PALAZZO PITTI + BOBOLI", S_TITLE),
            Paragraph("Route sheet · where to stand for every track, in walking order", S_SUB), Spacer(1, 3),
            Paragraph("FLORENCE · OLTRARNO · V5 TEST BUILD · OCTOBER 2026", S_LOC)]
    right = [Paragraph("TOUR NO. 43", S_PILL), Paragraph(f"{len(tr)} tracks<br/>~{plan['total_min']} min · English", S_META)]
    h = Table([[left, right]], colWidths=[W*0.68, W*0.32])
    h.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), INK), ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 14), ('RIGHTPADDING', (0,0), (-1,-1), 14),
        ('TOPPADDING', (0,0), (-1,-1), 9), ('BOTTOMPADDING', (0,0), (-1,-1), 9)]))
    st += [h, Spacer(1, 7)]
    notes = ("<b>How it works.</b> Track numbers are the walking order and match the audio file names. Each track "
             "ends by naming the next place to go. A red number marks a headline stop.<br/>"
             "<b>Iliad Room (23), closed until 25 October 2026.</b> Staff send visitors from the Sala della Stufa (22) "
             "back to the Room of Jupiter. Play 033–035 in Jupiter, then 026–032 in Saturn, then carry on from 036. "
             "Skip 022–025.<br/><b>Royal Apartments.</b> Guided visits only, with set times. If yours comes earlier, "
             "play 047–048 around it and pick up the Palatine where you left off.")
    nb = Table([[Paragraph(notes, S_NOTE)]], colWidths=[W])
    nb.setStyle(TableStyle([('BOX', (0,0), (-1,-1), 0.8, CRIMSON), ('BACKGROUND', (0,0), (-1,-1), HexColor('#F7F6F1')),
        ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8), ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6)]))
    st += [nb, Spacer(1, 4)]
    folders = [s["folder"] for s in plan["sections"]]
    for zi, fo in enumerate(folders):
        label, cue = ZONE[fo]; tint = ZTINTS[zi % len(ZTINTS)]
        rows = []
        for t in [t for t in tr if t["folder"] == fo]:
            room = "" if fo in ("00_Welcome", "07_Closing") else t["room"].upper()
            rows.append([Badge(t["seq"], t["seq"] in STAR),
                         [Paragraph(escape(room), S_ROOM), Paragraph(escape(t["title"]), S_NAME)],
                         Paragraph(escape(t["where"]), S_WHERE)])
        tb = Table(rows, colWidths=[1.0*cm, W*0.33, W - 1.0*cm - W*0.33], repeatRows=0)
        tb.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BACKGROUND', (0,0), (-1,-1), tint),
            ('LINEBELOW', (0,0), (-1,-2), 0.4, GREY_LN), ('BOX', (0,0), (-1,-1), 0.6, HexColor('#8E8A7C')),
            ('LEFTPADDING', (0,0), (-1,-1), 5), ('RIGHTPADDING', (0,0), (-1,-1), 5),
            ('TOPPADDING', (0,0), (-1,-1), 3.5), ('BOTTOMPADDING', (0,0), (-1,-1), 4)]))
        head = [Spacer(1, 6), Paragraph(escape(label), S_ZONE), Paragraph(escape(cue), S_CUE), Spacer(1, 3)]
        if len(rows) <= 6:
            st.append(KeepTogether(head + [tb]))
        else:
            st += head; st.append(tb)
    def bg(canv, d):
        canv.saveState(); canv.setFillColor(CREAM); canv.rect(0, 0, A4[0], A4[1], stroke=0, fill=1)
        canv.setFont('Helvetica', 6.8); canv.setFillColor(INK_SOFT)
        canv.drawString(1.5*cm, 0.55*cm, "Tour No. 43 · Palazzo Pitti + Boboli · V5 test build · placements checked on uffizi.it, Oct 2026 · rooms can change: ask an attendant")
        canv.drawRightString(A4[0]-1.5*cm, 0.55*cm, f"{d.page}")
        canv.restoreState()
    doc.build(st, onFirstPage=bg, onLaterPages=bg)
    print("built", OUT)
build()
