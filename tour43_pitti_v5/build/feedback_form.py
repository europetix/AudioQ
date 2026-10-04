import json, sys, os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('DejaVu', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
B = sys.argv[1]; plan = json.load(open(os.path.join(B, "plan.json")))
OUT = os.path.join(B, "USER_TEST", "Pitti_V5_Feedback_Form.pdf")
INK, SOFT, CRIM, LN, CREAM = HexColor('#1F1F1F'), HexColor('#565650'), HexColor('#A4161A'), HexColor('#9C998E'), HexColor('#F2F1EA')
H = ParagraphStyle('h', fontName='Times-Bold', fontSize=17, leading=20, textColor=CRIM)
H2 = ParagraphStyle('h2', fontName='Times-Bold', fontSize=11.5, leading=14, textColor=INK, spaceBefore=6)
P = ParagraphStyle('p', fontName='Helvetica', fontSize=8, leading=10.5, textColor=INK)
SM = ParagraphStyle('s', fontName='Helvetica', fontSize=6.6, leading=7.6, textColor=INK)
W = A4[0] - 2.6*cm
doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=1.3*cm, rightMargin=1.3*cm, topMargin=1.0*cm, bottomMargin=1.0*cm,
                        title="Palazzo Pitti V5 — Tester Feedback Form")
st = [Paragraph("Palazzo Pitti + Boboli · Tester feedback", H),
      Paragraph("Name ______________________ &nbsp; Date ________ &nbsp; Guide: <font name='DejaVu'>&#9744;</font> June &nbsp;<font name='DejaVu'>&#9744;</font> V5 &nbsp;&nbsp; Voice: <font name='DejaVu'>&#9744;</font> am_michael &nbsp;<font name='DejaVu'>&#9744;</font> Brian &nbsp;&nbsp; Phone/earphones ______________", P),
      Spacer(1, 4),
      Paragraph("<b>While you walk</b>, tick a box next to the track number whenever it happens. Leave it blank if all was fine. "
                "<b>L</b> = I wasn't where the audio thought I was &nbsp; <b>W</b> = didn't match what I was looking at &nbsp; "
                "<b>R</b> = voice sounded robotic &nbsp; <b>B</b> = bored, I skipped or stopped listening. "
                "If you use the June guide, use its own track numbers (1–90).", P), Spacer(1, 5)]
N = 90  # covers both versions (June 90, V5 79)
cols = 5; per = (N + cols - 1) // cols
hdr = []
for c in range(cols): hdr += ["#", "L", "W", "R", "B"]
rows = [hdr]
box = "☐"
for r in range(per):
    row = []
    for c in range(cols):
        n = c * per + r + 1
        row += ([f"{n:03d}", "", "", "", ""] if n <= N else ["", "", "", "", ""])
    rows.append(row)
cw = []
for c in range(cols): cw += [0.95*cm] + [(W/cols - 0.95*cm)/4]*4
t = Table(rows, colWidths=cw, rowHeights=[0.62*cm]*(per+1))
sty = [('FONT', (0,0), (-1,-1), 'Helvetica', 7.5), ('FONT', (0,0), (-1,0), 'Helvetica-Bold', 7),
       ('ALIGN', (0,0), (-1,-1), 'CENTER'), ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
       ('GRID', (0,0), (-1,-1), 0.3, LN), ('BACKGROUND', (0,0), (-1,0), CREAM)]
for c in range(cols): sty.append(('LINEAFTER', (c*5+4, 0), (c*5+4, -1), 1.2, INK))
t.setStyle(TableStyle(sty)); st.append(t)
st.append(Spacer(1, 4))
st.append(Paragraph("Notes on any ticked track (number + what happened):", P))
st.append(Table([[""]]*5, colWidths=[W], rowHeights=[0.55*cm]*5, style=[('LINEBELOW', (0,0), (-1,-1), 0.3, LN)]))
st.append(PageBreak())
st.append(Paragraph("After your visit", H))
Q = ["The voice sounded like a real person telling me stories.",
     "The stories held my attention.",
     "The audio matched where I was standing.",
     "I always knew where to go next.",
     "The pace felt right (not too fast, not too slow).",
     "The tracks were the right length.",
     "Names and places were pronounced clearly.",
     "I trust what the guide told me.",
     "I would recommend this audio guide to a friend."]
qrows = [["", "1 disagree", "2", "3", "4", "5 agree"]] + [[Paragraph(q, P), box, box, box, box, box] for q in Q]
qt = Table(qrows, colWidths=[W*0.55] + [W*0.09]*5)
qt.setStyle(TableStyle([('FONT', (0,0), (-1,0), 'Helvetica-Bold', 7.5), ('FONT', (1,1), (-1,-1), 'DejaVu', 13),
    ('ALIGN', (1,0), (-1,-1), 'CENTER'), ('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LINEBELOW', (0,0), (-1,-1), 0.3, LN),
    ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4)]))
st += [qt, Spacer(1, 6)]
for q in ["Where did you get lost or confused, if anywhere?", "Which moment or story did you enjoy most?",
          "What, if anything, sounded artificial or annoying about the voice?", "Anything that seemed wrong or out of date?"]:
    st.append(Paragraph(f"<b>{q}</b>", P))
    st.append(Table([[""]]*2, colWidths=[W], rowHeights=[0.6*cm]*2, style=[('LINEBELOW', (0,0), (-1,-1), 0.3, LN)]))
    st.append(Spacer(1, 3))
st.append(Paragraph("Desk listening test (Test 1) — score each clip", H2))
st.append(Paragraph("1 = strongly disagree, 5 = strongly agree. &nbsp; S1: <i>This sounds like a real person telling me a story.</i> &nbsp; "
                    "S2: <i>I'd happily listen to 30 more tracks of this.</i>", P))
lrows = [["Clip", "S1 (1–5)", "S2 (1–5)", "What sounded artificial?"]] + [[f"{i:02d}", "", "", ""] for i in range(1, 10)]
lt = Table(lrows, colWidths=[1.3*cm, 1.8*cm, 1.8*cm, W - 4.9*cm], rowHeights=[0.5*cm]*10)
lt.setStyle(TableStyle([('FONT', (0,0), (-1,-1), 'Helvetica', 8), ('FONT', (0,0), (-1,0), 'Helvetica-Bold', 8),
    ('GRID', (0,0), (-1,-1), 0.3, LN), ('BACKGROUND', (0,0), (-1,0), CREAM), ('ALIGN', (0,0), (2,-1), 'CENTER'), ('VALIGN', (0,0), (-1,-1), 'MIDDLE')]))
st.append(lt)
doc.build(st); print("built", OUT)
