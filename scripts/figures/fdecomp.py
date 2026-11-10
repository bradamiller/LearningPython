"""Lesson 4-0: Module 4's problem broken down into parts (problem decomposition).

Output: out/decomposition.svg -> static/img/lesson-m4-00/decomposition-one-destination.svg
(renamed 2026-11-08 when the top box changed, so browsers don't show the cached old one)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR
from common import *

BLUE, BLUE_BG = "#22527B", "#F1F6FB"
RED, RED_BG = "#D1182C", "#FDF2F3"
GRAY, GRAY_BG = "#495057", "#F8F9FA"
b = []


def box(x, y, w, h, head, code, sub, stroke, fill, hcls="h"):
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="2"/>',
         f'<text class="{hcls}" x="{x+w/2}" y="{y+22}" text-anchor="middle">{head}</text>']
    if code:
        o.append(f'<text class="ms" x="{x+w/2}" y="{y+42}" text-anchor="middle">{code}</text>')
    o.append(f'<text class="sm" x="{x+w/2}" y="{y+(60 if code else 42)}" text-anchor="middle">{sub}</text>')
    return o


def elbow(x1, y1, xs, y2, ymid):
    """A bracket from (x1, y1) down to ymid, across, and down to y2 at each x in xs."""
    o = [f'<line x1="{x1}" y1="{y1}" x2="{x1}" y2="{ymid}" stroke="#ADB5BD" stroke-width="2"/>',
         f'<line x1="{min(xs)}" y1="{ymid}" x2="{max(xs)}" y2="{ymid}" stroke="#ADB5BD" stroke-width="2"/>']
    for x in xs:
        o.append(f'<line x1="{x}" y1="{ymid}" x2="{x}" y2="{y2-2}" stroke="#ADB5BD" stroke-width="2" marker-end="url(#aG)"/>')
    return o


# Level 1: the whole problem
b += box(160, 12, 360, 52, "The whole problem", None,
         "drive from the start to a destination, on its own", GRAY, GRAY_BG)

# Level 2: two parts
PX, DX, W2, Y2, H2 = 16, 428, 236, 112, 76
b += elbow(340, 64, [PX + W2/2, DX + W2/2], Y2, 88)
b += box(PX, Y2, W2, H2, "The planner", "compute_manhattan_path()", "Lessons 4-4 and 4-5", BLUE, BLUE_BG)
b += box(DX, Y2, W2, H2, "The driver", "drive_path()", "Lessons 4-6 and 4-7", RED, RED_BG)

# The handoff between them
b.append(f'<line x1="{PX+W2+2}" y1="{Y2+50}" x2="{DX-4}" y2="{Y2+50}" stroke="#495057" stroke-width="2.2" marker-end="url(#aG)"/>')
b.append(tag(340, Y2 + 30, "list of (x, y) tuples", fill="#FFFFFF", stroke="#ADB5BD", cls="nb", w=158))
b.append(f'<text class="sm" x="340" y="{Y2+70}" text-anchor="middle">the one thing they share</text>')

# The planner is small enough already
b.append(f'<text class="sm" x="{PX+W2/2}" y="{Y2+H2+40}" text-anchor="middle">small enough to build</text>')
b.append(f'<text class="sm" x="{PX+W2/2}" y="{Y2+H2+56}" text-anchor="middle">and test in one go</text>')

# Level 3: the driver splits again
W3, G3, Y3, H3 = 146, 10, 240, 76
x0 = 680 - 10 - 3 * W3 - 2 * G3
xs = [x0 + i * (W3 + G3) for i in range(3)]
b += elbow(DX + W2/2, Y2 + H2, [x + W3/2 for x in xs], Y3, Y2 + H2 + 24)
b += box(xs[0], Y3, W3, H3, "Which way to face?", "desired_heading()", "Lesson 4-6", RED, "#FFFFFF", hcls="nb")
b += box(xs[1], Y3, W3, H3, "Turn to face it", "turn_to()", "Lesson 4-7", RED, "#FFFFFF", hcls="nb")
b += box(xs[2], Y3, W3, H3, "Follow the tape", "LINE TRACKING", "built in Module 2", RED, "#FFFFFF", hcls="nb")

open(OUTDIR + 'decomposition.svg', 'w').write(svg(
    'Module 4, broken into parts',
    'A tree with three levels. At the top, the whole problem: drive from the start to a destination, '
    'on its own. It splits into two parts. The planner, compute_manhattan_path(), built in Lessons 4-4 '
    'and 4-5, is small enough to build and test in one go. The driver, drive_path(), built in '
    'Lessons 4-6 and 4-7, splits again into three smaller parts: which way to face, '
    'desired_heading(), Lesson 4-6; turn to face it, turn_to(), Lesson 4-7; and follow the tape, '
    'the LINE TRACKING functions built in Module 2. An arrow from planner to driver is labeled '
    '"list of (x, y) tuples, the one thing they share".',
    b, H=330))
