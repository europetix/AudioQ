#!/usr/bin/env python3
"""Traveller navigation PDF for Tour #43 (V5.1): ONE page, "Route at a glance".
Cloned from the Tour #49 route-map pattern (house palette, header band), driven by the bundle's plan.json so the
track ranges always match the audio files. Each stop: step, section, floor, track range, minutes, how to get there.
Shared with travellers alongside the MP3s; works printed or offline on a phone."""
import json, os, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_RIGHT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Flowable
from xml.sax.saxutils import escape

B = sys.argv[1]; OUT = os.path.join(B, "Palazzo_Pitti_Audio_Guide_Route.pdf")
plan = json.load(open(os.path.join(B, "plan.json")))
CREAM, INK, INK_SOFT = HexColor('#F2F1EA'), HexColor('#1F1F1F'), HexColor('#565650')
CRIMSON, CRIM_LIGHT = HexColor('#A4161A'), HexColor('#C9444A')
PANEL, EDGE = HexColor('#F7F6F1'), HexColor('#8E8A7C')
tr = plan["tracks"]

def seqs(pred):
    s = [t["seq"] for t in tr if pred(t)]
    return (s[0] + "–" + s[-1]) if len(s) > 1 else (s[0] if s else "?")
def room(r): return lambda t: t["folder"] == "01_Palatine_Gallery" and t["room"] == r
def folder(f): return lambda t: t["folder"] == f
def mins(f): return max(1, round(sum(t["words"] for t in tr if t["folder"] == f) / 125))  # same basis as plan total_min

ROYAL = "04_Imperial_and_Royal_Apartments"
roy = [t["seq"] for t in tr if t["folder"] == ROYAL]
jup, sat, ili = seqs(room("Room 25")), seqs(room("Room 24")), seqs(room("Room 23"))
mars_first = [t["seq"] for t in tr if room("Room 26")(t)][0]

# (folder, name, floor, directions, flag)
STOPS = [
 ("00_Welcome", "Piazza Pitti", "Outside", "The ticket office is on the right of the façade. Go through the central doorway into the "
  "Ammannati Courtyard. Stairs and lifts are on its right-hand side: go up to the first floor.", None),
 ("01_Palatine_Gallery", "Palatine Gallery", "First floor", "The museum's one-way route: Rooms 1–3, the inner rooms 14–23, then the "
  "five Planet Rooms from Saturn (24) to Venus (28). Room names are on the signs above the doors. Exit through the Sala delle "
  "Nicchie to the entrance atrium. The Volterrano Wing (Rooms 4–11) is often closed and has no tracks.",
  f"Iliad Room (23) closed until 25 Oct 2026: staff send you back to Jupiter. Play {jup}, then {sat}, carry on from {mars_first}; skip {ili}."),
 ("02_Gallery_of_Modern_Art", "Gallery of Modern Art", "Second floor", "From the Palatine atrium, take the stairs or lift up one floor. "
  "Follow the corridor and turn left. Rooms 1–30 run in a loop.", None),
 ("03_Museum_of_Fashion_and_Costume", "Museum of Fashion & Costume", "Second floor", "Back to the landing, then the corridor to the "
  "right and a staircase of two short flights (stair-lift available). A dead end: leave the way you came.", None),
 (ROYAL, "Imperial & Royal Apartments", "First floor", "Separate ticket. On your way back down, stop one floor below at the Palatine "
  f"entrance atrium: the meeting point. Staff-led group visit of about 30 minutes, at set times. Play {roy[0]} while you wait and "
  f"{roy[-1]} afterwards. Please keep the audio paused inside.", "No Royal Apartments ticket? Carry straight on down to step 6."),
 ("05_Russian_Icons_and_Palatine_Chapel", "Russian Icons & Palatine Chapel", "Ground floor", "Down to the Ammannati Courtyard and "
  "follow the signs for the Palatine Chapel.", None),
 ("06_Boboli_Gardens", "Boboli Gardens", "Garden", "Up from the back of the courtyard. East past the Bacchino and the grottoes, uphill "
  "to the Amphitheatre, Neptune, the Kaffeehaus and Abundance, down the cypress avenue to the Isolotto, then back north to the "
  "Limonaia and out by any gate. Some areas are fenced for restoration but visible from the paths. Can also be done first.", None),
 ("07_Closing", "Closing", "Anywhere", "Once you've finished, wherever you come out.", None),
]

S_TITLE = ParagraphStyle('t', fontName='Times-Bold', fontSize=23, leading=25, textColor=CREAM)
S_SUB = ParagraphStyle('s', fontName='Times-Italic', fontSize=11.5, leading=14, textColor=CRIM_LIGHT)
S_LOC = ParagraphStyle('l', fontName='Helvetica', fontSize=7, leading=10, textColor=HexColor('#BFBDB2'))
S_PILL = ParagraphStyle('p', fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=CRIM_LIGHT, alignment=TA_RIGHT)
S_META = ParagraphStyle('m', fontName='Times-Italic', fontSize=10.5, leading=13, textColor=CRIM_LIGHT, alignment=TA_RIGHT)
S_HOW = ParagraphStyle('h', fontName='Helvetica', fontSize=8, leading=10.4, textColor=INK)
S_NAME = ParagraphStyle('n', fontName='Times-Bold', fontSize=12, leading=14, textColor=CRIMSON)
S_FLOOR = ParagraphStyle('f', fontName='Helvetica-Bold', fontSize=6.8, leading=8.5, textColor=INK_SOFT)
S_DIR = ParagraphStyle('d', fontName='Helvetica', fontSize=7.8, leading=9.9, textColor=INK)
S_FLAG = ParagraphStyle('g', fontName='Helvetica-Bold', fontSize=7.6, leading=9.6, textColor=CRIMSON)
S_TRK = ParagraphStyle('k', fontName='Helvetica-Bold', fontSize=10, leading=12, textColor=INK, alignment=TA_CENTER)
S_MIN = ParagraphStyle('mi', fontName='Helvetica', fontSize=7, leading=9, textColor=INK_SOFT, alignment=TA_CENTER)
S_FOOT = ParagraphStyle('ft', fontName='Helvetica', fontSize=7, leading=9, textColor=INK_SOFT, alignment=TA_CENTER)

class Step(Flowable):
    def __init__(self, n, hot):
        Flowable.__init__(self); self.n, self.hot = n, hot; self.width = self.height = 0.85*cm
    def draw(self):
        c = self.canv; r = self.width/2
        c.setFillColor(CRIMSON if self.hot else INK); c.circle(r, r, r, stroke=0, fill=1)
        c.setFillColor(CREAM); c.setFont('Times-Bold', 11); c.drawCentredString(r, r-3.8, str(self.n))

class Down(Flowable):
    """Arrow between two stops, under the step badges."""
    def __init__(self): Flowable.__init__(self); self.width, self.height = 10, 0.42*cm
    def draw(self):
        c = self.canv; c.setStrokeColor(CRIMSON); c.setLineWidth(1.4); x, h = self.width/2, self.height
        c.line(x, h, x, 1.5); c.line(x, 1.5, x-3.5, 5.5); c.line(x, 1.5, x+3.5, 5.5)

def build():
    W = A4[0] - 3.0*cm
    doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=1.5*cm, rightMargin=1.5*cm, topMargin=0.9*cm,
        bottomMargin=0.9*cm, title="Palazzo Pitti + Boboli — Audio Guide: Route at a Glance", author="Humanized Audio Guide",
        subject="Walking order and track numbers for the Palazzo Pitti + Boboli audio guide, Tour No. 43")
    left = [Paragraph("PALAZZO PITTI + BOBOLI", S_TITLE), Paragraph("Audio guide · route at a glance", S_SUB), Spacer(1, 3),
            Paragraph("FLORENCE · OLTRARNO · ENGLISH · OCTOBER 2026", S_LOC)]
    right = [Paragraph("TOUR NO. 43", S_PILL), Paragraph(f"{len(tr)} tracks<br/>about {plan['total_min']} min of audio", S_META)]
    h = Table([[left, right]], colWidths=[W*0.68, W*0.32])
    h.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), INK), ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 14), ('RIGHTPADDING', (0,0), (-1,-1), 14),
        ('TOPPADDING', (0,0), (-1,-1), 9), ('BOTTOMPADDING', (0,0), (-1,-1), 9)]))
    how = Paragraph("<b>How to use it.</b> Download the MP3s before you go: they play offline, no app needed. Play the tracks in "
                    "number order. Each track tells you where to stand, and ends by telling you where to go next. "
                    "If a room is closed or a painting is away, skip to the next number.", S_HOW)
    st = [h, Spacer(1, 7), how, Spacer(1, 8)]
    cw = [1.15*cm, W - 1.15*cm - 2.6*cm, 2.6*cm]
    for i, (fo, name, floor, dirs, flag) in enumerate(STOPS, 1):
        body = [Paragraph(escape(name), S_NAME), Paragraph(escape(floor.upper()), S_FLOOR), Spacer(1, 2), Paragraph(escape(dirs), S_DIR)]
        if flag: body += [Spacer(1, 2), Paragraph(escape(flag), S_FLAG)]
        rng = seqs(folder(fo)); n = sum(1 for t in tr if t["folder"] == fo)
        trk = [Paragraph("Track" + ("s" if n > 1 else ""), S_MIN), Paragraph(rng, S_TRK), Paragraph(f"about {mins(fo)} min", S_MIN)]
        t = Table([[Step(i, fo == ROYAL), body, trk]], colWidths=cw)
        t.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('VALIGN', (1,0), (1,0), 'TOP'),
            ('BACKGROUND', (1,0), (-1,0), PANEL), ('BOX', (1,0), (-1,0), 0.7 if fo != ROYAL else 1.4, EDGE if fo != ROYAL else CRIMSON),
            ('LINEBEFORE', (2,0), (2,0), 0.5, EDGE), ('ALIGN', (0,0), (0,0), 'CENTER'), ('LEFTPADDING', (0,0), (0,0), 0), ('RIGHTPADDING', (0,0), (0,0), 0),
            ('LEFTPADDING', (1,0), (-1,0), 8), ('RIGHTPADDING', (1,0), (-1,0), 8),
            ('TOPPADDING', (1,0), (-1,0), 5), ('BOTTOMPADDING', (1,0), (-1,0), 6)]))
        st.append(t)
        if i < len(STOPS):
            a = Table([[Down(), "", ""]], colWidths=cw)
            a.setStyle(TableStyle([('ALIGN', (0,0), (0,0), 'CENTER'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0),
                ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
            st.append(a)
    st += [Spacer(1, 8), Paragraph("Rooms and hangings can change: ask an attendant. Placements checked October 2026.", S_FOOT)]
    def bg(canv, d):
        canv.saveState(); canv.setFillColor(CREAM); canv.rect(0, 0, A4[0], A4[1], stroke=0, fill=1); canv.restoreState()
    doc.build(st, onFirstPage=bg, onLaterPages=bg)
    print("built", OUT)
build()
