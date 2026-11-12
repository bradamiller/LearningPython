"""Lesson 4-0: plan first, then drive. The plan is a list of (x, y) coordinates.

Same grid, start and destination as drive-to-destination.svg, now with the route
and each intersection's coordinates; beside it the two steps and what passes between them.

Output: out/plan-then-drive.svg -> static/img/lesson-m4-00/plan-then-drive.svg
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR
from common import *

BLUE, BLUE_BG = "#22527B", "#F1F6FB"
RED, RED_BG = "#D1182C", "#FDF2F3"
g = G(70, 70, sp=60, pad=30)
b = g.base(axes=True, north=False)

route = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]
b.append(g.route(route, "#4C8BF5"))
sx, sy = g.p(0, 0)
b.append(f'<use href="#pcXRP" transform="translate({sx} {sy}) rotate(0) scale(0.36)"/>')
for i, (x, y) in enumerate(route[1:], 1):
    px, py = g.p(x, y)
    b.append(f'<circle cx="{px}" cy="{py}" r="6" fill="#FFFFFF" stroke="{BLUE}" stroke-width="2.4"/>')
    lx, ly = (px, py + 26) if y == 0 else (px + 40, py + 4)
    b.append(tag(lx, ly, f"({x}, {y})", stroke="#4C8BF5", cls="ms", w=52))

# the two steps
X, W = 330, 330
b.append(f'<rect x="{X}" y="40" width="{W}" height="78" rx="10" fill="{BLUE_BG}" stroke="{BLUE}" stroke-width="2"/>')
b.append(f'<text class="h" x="{X+16}" y="66">1 · Plan</text>')
b.append(f'<text class="n" x="{X+16}" y="88">Work out the route, print it, check it.</text>')
b.append(f'<text class="nb" x="{X+16}" y="106">No robot needed.</text>')

b.append(f'<line x1="{X+W/2}" y1="120" x2="{X+W/2}" y2="147" stroke="#495057" stroke-width="2.2"/>')
b.append(f'<line x1="{X+W/2}" y1="169" x2="{X+W/2}" y2="196" stroke="#495057" stroke-width="2.2" marker-end="url(#aG)"/>')
b.append(tag(X + W/2, 158, "(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)", fill="#FFFFFF", stroke="#ADB5BD", cls="ms", w=300))
b.append(f'<text class="sm" x="{X+W/2+12}" y="188">a list of (x, y) coordinates</text>')

b.append(f'<rect x="{X}" y="200" width="{W}" height="78" rx="10" fill="{RED_BG}" stroke="{RED}" stroke-width="2"/>')
b.append(f'<text class="h" x="{X+16}" y="226" style="fill:{RED}">2 · Drive</text>')
b.append(f'<text class="n" x="{X+16}" y="248">Take the list and drive it,</text>')
b.append(f'<text class="n" x="{X+16}" y="266">one intersection at a time.</text>')

open(OUTDIR + 'plan-then-drive.svg', 'w').write(svg(
    'Plan first, then drive: the plan is a list of (x, y) coordinates',
    'Left: a 4 by 4 grid with (0, 0) at the bottom-left. The robot starts at (0, 0). A blue route goes '
    'right to (1, 0) and (2, 0), then up to (2, 1), (2, 2) and (2, 3), each intersection labeled with '
    'its coordinates. Right: step 1, Plan: work out the route, print it, check it, no robot needed. An arrow '
    'carries the points (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), a list of (x, y) coordinates, down to '
    'step 2, Drive: take the list and drive it, one intersection at a time.',
    b, H=330))
