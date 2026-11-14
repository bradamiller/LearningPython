"""Module 4 test (top-down trial), Lesson 4-0: the same tree as fdecomp.py with the trial's lesson numbers.

Original: Lesson 4-5 opening: Module 4's problem broken down into parts (problem decomposition).

A tree that opens one level per click on the page (<TreeFigure>): every element
carries data-parent, the box it belongs under; a box that breaks down further
carries data-node and data-expand. The page SVG has everything showing, so it
reads in full where scripts don't run; the component hides levels on load.

Outputs:
  out/decomposition.svg -> static/img/lesson-m4-05/decomposition.svg (the page)
  out/decomposition-1.svg .. -4.svg -> scripts/slides/decks/m4/fig/l05-decomp-N.svg
    (the deck: one slide per level, the levels below simply left out)
(renamed 2026-11-08 when the top box changed, so browsers don't show the cached old one)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR
from common import *

BLUE, BLUE_BG = "#22527B", "#F1F6FB"
RED, RED_BG = "#D1182C", "#FDF2F3"
GRAY, GRAY_BG = "#495057", "#F8F9FA"
EXPAND = ["whole", "driver", "turn"]          # the boxes that break down, top to bottom
LEVEL = {None: 0, "whole": 1, "driver": 2, "turn": 3}   # elements under a box are one level deeper

STYLE = '''<style>
    [data-parent] { transition: opacity .3s ease; }
    .hid { opacity: 0; visibility: hidden; }
    [data-expand] { cursor: pointer; }
    [data-expand]:hover rect.bx, [data-expand]:focus rect.bx { stroke-width: 3.5; }
    [data-expand]:focus { outline: none; }
    .ind-minus { display: none; }
    .open .ind-minus { display: inline; }
    .open .ind-plus { display: none; }
  </style>'''

items = []   # (parent, svg text)


def box(x, y, w, h, head, code, sub, stroke, fill, hcls="h", node=None, parent=None):
    mid = y + h / 2
    o = [f'<rect class="bx" x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="2"/>']
    if isinstance(head, tuple) and code:   # a two-line heading, then the code line
        o += [f'<text class="{hcls}" x="{x+w/2}" y="{mid-26}" text-anchor="middle">{head[0]}</text>',
              f'<text class="{hcls}" x="{x+w/2}" y="{mid-7}" text-anchor="middle">{head[1]}</text>',
              f'<text class="ms" x="{x+w/2}" y="{mid+13}" text-anchor="middle">{code}</text>',
              f'<text class="sm" x="{x+w/2}" y="{mid+31}" text-anchor="middle">{sub}</text>']
        head = " ".join(head)
    elif isinstance(head, tuple):   # a two-line heading, no code line
        o += [f'<text class="{hcls}" x="{x+w/2}" y="{mid-18}" text-anchor="middle">{head[0]}</text>',
              f'<text class="{hcls}" x="{x+w/2}" y="{mid+1}" text-anchor="middle">{head[1]}</text>',
              f'<text class="sm" x="{x+w/2}" y="{mid+22}" text-anchor="middle">{sub}</text>']
        head = " ".join(head)
    elif code:
        o += [f'<text class="{hcls}" x="{x+w/2}" y="{mid-16}" text-anchor="middle">{head}</text>',
              f'<text class="ms" x="{x+w/2}" y="{mid+4}" text-anchor="middle">{code}</text>',
              f'<text class="sm" x="{x+w/2}" y="{mid+22}" text-anchor="middle">{sub}</text>']
    else:
        o += [f'<text class="{hcls}" x="{x+w/2}" y="{mid-4}" text-anchor="middle">{head}</text>',
              f'<text class="sm" x="{x+w/2}" y="{mid+16}" text-anchor="middle">{sub}</text>']
    attrs = f' data-parent="{parent}"' if parent else ''
    if node in EXPAND:
        cx, cy = x + w - 15, y + 15
        o += [f'<circle cx="{cx}" cy="{cy}" r="9.5" fill="{stroke}"/>',
              f'<text class="ind-plus" x="{cx}" y="{cy+5.5}" text-anchor="middle" font-family="Arial" font-size="17" font-weight="700" fill="#FFFFFF">+</text>',
              f'<text class="ind-minus" x="{cx}" y="{cy+5.5}" text-anchor="middle" font-family="Arial" font-size="17" font-weight="700" fill="#FFFFFF">&#8722;</text>']
        attrs += f' data-node="{node}" data-expand="1" aria-label="{head}: show its parts"'
    items.append((parent, f'<g{attrs}>' + ''.join(o) + '</g>'))


def under(parent, *els):
    items.append((parent, f'<g data-parent="{parent}">' + ''.join(els) + '</g>'))


def elbow(x1, y1, xs, y2, ymid):
    """A bracket from (x1, y1) down to ymid, across, and down to y2 at each x in xs."""
    o = [f'<line x1="{x1}" y1="{y1}" x2="{x1}" y2="{ymid}" stroke="#ADB5BD" stroke-width="2"/>',
         f'<line x1="{min(xs)}" y1="{ymid}" x2="{max(xs)}" y2="{ymid}" stroke="#ADB5BD" stroke-width="2"/>']
    for x in xs:
        o.append(f'<line x1="{x}" y1="{ymid}" x2="{x}" y2="{y2-2}" stroke="#ADB5BD" stroke-width="2" marker-end="url(#aG)"/>')
    return ''.join(o)


# Level 1: the whole problem
box(160, 12, 360, 52, "The main program, Lesson 4-1", None,
    "for each destination: plan the route, then drive it", GRAY, GRAY_BG, node="whole")

# Level 2: the planner and the driver
PX, DX, W2, Y2, H2 = 16, 428, 236, 112, 76
under("whole", elbow(340, 64, [PX + W2/2, DX + W2/2], Y2, 88))
box(PX, Y2, W2, H2, "The planner", "compute_manhattan_path()", "Lessons 4-2 and 4-3", BLUE, BLUE_BG,
    parent="whole")
box(DX, Y2, W2, H2, "The driver", "drive_path()", "Lesson 4-4", RED, RED_BG,
    node="driver", parent="whole")
under("whole",
      f'<line x1="{PX+W2+2}" y1="{Y2+50}" x2="{DX-4}" y2="{Y2+50}" stroke="#495057" stroke-width="2.2" marker-end="url(#aG)"/>',
      tag(340, Y2 + 30, "list of (x, y) coordinates", fill="#FFFFFF", stroke="#ADB5BD", cls="nb", w=172),
      f'<text class="sm" x="340" y="{Y2+70}" text-anchor="middle">the one thing they share</text>',
      f'<text class="sm" x="{PX+W2/2}" y="{Y2+H2+40}" text-anchor="middle">built and tested</text>',
      f'<text class="sm" x="{PX+W2/2}" y="{Y2+H2+56}" text-anchor="middle">with no robot</text>')

# Level 3: the driver, two steps at each intersection
W3, G3, Y3, H3 = 210, 12, 240, 92
x0 = 680 - 10 - 2 * W3 - G3
xs = [x0 + i * (W3 + G3) for i in range(2)]
under("driver", elbow(DX + W2/2, Y2 + H2, [x + W3/2 for x in xs], Y3, Y2 + H2 + 24))
box(xs[0], Y3, W3, H3, ("1 · Turn to face", "the next intersection"), None, "Lessons 4-4 and 4-5", RED, "#FFFFFF",
    hcls="nb", node="turn", parent="driver")
box(xs[1], Y3, W3, H3, ("2 · Drive to", "the next intersection"), "LINE TRACKING", "Module 2, used in 4-6", RED, "#FFFFFF",
    hcls="nb", parent="driver")

# Level 4: turning, which way and then the turn
W4, G4, Y4, H4 = 200, 12, 376, 92
tc = xs[0] + W3 / 2
x4 = [tc - W4 - G4 / 2, tc + G4 / 2]
under("turn", elbow(tc, Y3 + H3, [x + W4/2 for x in x4], Y4, Y3 + H3 + 22))
box(x4[0], Y4, W4, H4, "Which way to face?", "get_desired_heading()", "Lesson 4-4", RED, "#FFFFFF",
    hcls="nb", parent="turn")
box(x4[1], Y4, W4, H4, ("Turn until facing", "the next intersection"), "turn_to()", "Lesson 4-5", RED, "#FFFFFF",
    hcls="nb", parent="turn")

DESC = ('A tree with four levels. At the top, the main program, Lesson 4-1: for each destination, plan '
        'the route, then drive it. It splits into two parts. The planner, compute_manhattan_path(), '
        'Lessons 4-2 and 4-3, is built and tested on its own. The driver, drive_path(), Lesson 4-4, '
        'splits into two steps at each intersection: 1, turn to face the next intersection, Lessons 4-4 '
        'and 4-5; 2, drive to the next intersection, with the LINE TRACKING functions built in Module 2, '
        'used on the robot in Lesson 4-6. Turning splits once more: which way to face, '
        'get_desired_heading(), Lesson 4-4, and turn until facing the next intersection, turn_to(), '
        'Lesson 4-5. An arrow from planner to driver is labeled "list of (x, y) coordinates, the one '
        'thing they share".')


def render(levels, opened):
    body = [STYLE]
    for parent, el in items:
        if LEVEL[parent] < levels:
            if opened:
                el = el.replace(' data-expand="1"', ' data-expand="1" class="open"', 1) if (
                    'data-expand' in el and LEVEL[el.split('data-node="')[1].split('"')[0]] < levels) else el
            body.append(el)
    # Every level keeps the full canvas, so on slides the boxes stay put as levels appear.
    return svg('Module 4, broken into parts', DESC, body, H=480)


# Opened boxes show a minus; on the page the component sets which are open.
open(OUTDIR + 'decomposition-topdown-v2.svg', 'w').write(render(4, True))

