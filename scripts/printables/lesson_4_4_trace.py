"""Lesson 4-4 worksheet: trace path 1 move by move, then all six test paths.
Writes static/printables/lesson-4-4-trace-worksheet.pdf. Needs reportlab."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, black

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'static', 'printables', 'lesson-4-4-trace-worksheet.pdf')
W, H = letter
M = 50
INK, MUTE, LINE, HEAD = black, HexColor('#6C757D'), HexColor('#868E96'), HexColor('#E9ECEF')
RED, GREEN = HexColor('#D1182C'), HexColor('#2E7D32')

c = canvas.Canvas(OUT, pagesize=letter)
c.setTitle('Lesson 4-4 · Trace it on paper')

def text(x, y, s, font='Helvetica', size=10, col=INK):
    c.setFont(font, size); c.setFillColor(col); c.drawString(x, y, s)

def ctext(x, y, s, font='Helvetica', size=10, col=INK):
    c.setFont(font, size); c.setFillColor(col); c.drawCentredString(x, y, s)

def arrow(x1, y1, x2, y2):
    c.setStrokeColor(INK); c.setLineWidth(0.8); c.line(x1, y1, x2, y2)
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    for d in (2.6, -2.6):
        c.line(x2, y2, x2 - 5 * math.cos(a + d / 6), y2 - 5 * math.sin(a + d / 6))

def table(x, y, widths, header, rows, rh=20, hh=20, mono=(), shade=()):
    tw = sum(widths)
    c.setFillColor(HEAD); c.rect(x, y - hh, tw, hh, stroke=0, fill=1)
    c.setStrokeColor(LINE); c.setLineWidth(0.7)
    cx = x
    for w, h in zip(widths, header):
        lines = h.split('\n')
        for k, l in enumerate(lines):
            text(cx + 5, y - 13 - (k - (len(lines) - 1) / 2) * 9 + (len(lines) - 1) * 4.5 - (len(lines) - 1) * 4.5, l, 'Helvetica-Bold', 8.5 if len(lines) > 1 else 9.5)
        cx += w
    yy = y - hh; groups = []
    for r in rows:
        if isinstance(r, str):  # group label row
            groups.append((yy, r)); c.line(x, yy - 15, x + tw, yy - 15); yy -= 15; continue
        cx = x
        for i, (w, v) in enumerate(zip(widths, r)):
            if v:
                f = 'Courier' if i in mono else 'Helvetica'
                text(cx + 5, yy - rh / 2 - 3.5, v, f, 9.5, INK if i not in shade else MUTE)
            cx += w
        yy -= rh
        c.line(x, yy, x + tw, yy)
    c.rect(x, yy, tw, y - yy, stroke=1, fill=0)
    cx = x
    for w in widths[:-1]:
        cx += w; c.line(cx, y, cx, yy)
    for gy, r in groups:
        c.setFillColor(HexColor('#F8F9FA')); c.rect(x + 0.5, gy - 14.6, tw - 1, 14.2, stroke=0, fill=1)
        text(x + 5, gy - 11, r, 'Courier-Bold', 8.5)
    return yy

# header
text(M, H - 58, 'Lesson 4-4 · Trace it on paper', 'Helvetica-Bold', 17)
text(M, H - 82, 'Name: ________________________________', size=10)
text(W - M - 160, H - 82, 'Date: ______________', size=10)
intro = ['Trace by hand the six paths your tests will check. Across first, then up or down. Each move',
         'changes x or y by 1, never both. The start is never in the path.',
         'When you run your code, this sheet is your answer key: every line on screen should match it.']
for k, l in enumerate(intro):
    text(M, H - 104 - 13 * k, l, size=10)

# grid
gx, gy, sp = M + 32, H - 296, 34
c.setStrokeColor(HexColor('#212529')); c.setLineWidth(4.5)
for i in range(4):
    c.line(gx + i * sp, gy - 10, gx + i * sp, gy + 3 * sp + 10)
    c.line(gx - 10, gy + i * sp, gx + 3 * sp + 10, gy + i * sp)
for i in range(4):
    ctext(gx + i * sp, gy - 24, str(i), 'Helvetica-Bold', 9)
    text(gx - 26, gy + i * sp - 3, str(i), 'Helvetica-Bold', 9)
ctext(gx + 1.5 * sp - 6, gy - 38, 'x (across)', size=8.5)
arrow(gx + 1.5 * sp + 18, gy - 35, gx + 1.5 * sp + 34, gy - 35)
c.saveState(); c.translate(gx - 40, gy + 1.5 * sp - 16); c.rotate(90)
text(0, 0, 'y (away)', size=8.5); c.restoreState()
arrow(gx - 43, gy + 1.5 * sp + 18, gx - 43, gy + 1.5 * sp + 32)
text(M - 6, gy - 58, 'Draw each path in pencil; erase it before the next.', size=8, col=MUTE)

# part 1
px = M + 200
text(px, H - 160, '1. Path 1, move by move: (0, 0) to (2, 3)', 'Helvetica-Bold', 11)
text(px, H - 174, 'One row per move. Row 1 is done for you.', size=9, col=MUTE)
table(px, H - 182, [50, 80, 132], ['Step', 'Action', 'New position'],
      [['1', 'x + 1', '(1, 0)'], ['2', '', ''], ['3', '', ''], ['4', '', ''], ['5', '', '']],
      rh=20, shade=(1, 2))

# part 2
y2 = H - 380
text(M, y2, '2. All six paths', 'Helvetica-Bold', 11)
text(M, y2 - 14, 'Write each expected path and its number of steps. Steps = |end x - start x| + |end y - start y|.',
     size=9, col=MUTE)
rows = ['test_paper_paths()', ['1', '(0, 0) to (2, 3)', '', '', 'Y / N'], ['2', '(0, 1) to (3, 3)', '', '', 'Y / N'],
        ['3', '(3, 3) to (1, 0)', '', '', 'Y / N'], 'test_edge_cases()', ['4', '(2, 0) to (2, 3)', '', '', 'Y / N'],
        ['5', '(0, 2) to (3, 2)', '', '', 'Y / N'], ['6', '(1, 1) to (1, 1)', '', '', 'Y / N']]
yb = table(M, y2 - 22, [24, 96, 282, 44, 66], ['#', 'From / to', 'Expected path', 'Steps', 'Program\nmatched?'],
           rows, rh=26, hh=24, shade=(4,))
text(M, yb - 13, 'Fill in Expected path and Steps now. Circle Y or N after you run your tests.',
     'Helvetica-Oblique', 8.5, MUTE)

# part 3
y3 = yb - 42
text(M, y3, '3. What is different about path 3 compared with paths 1 and 2?', 'Helvetica-Bold', 11)
text(M + 14, y3 - 14, '(Look at which way x and y change.)', size=9, col=MUTE)
c.setStrokeColor(LINE); c.setLineWidth(0.7)
for k in range(3):
    c.line(M + 14, y3 - 38 - 22 * k, W - M, y3 - 38 - 22 * k)

ctext(W / 2, 30, 'XRP Intro to Python · learningpython.bradhouse.com', size=8, col=MUTE)
c.showPage(); c.save()
print(OUT)
