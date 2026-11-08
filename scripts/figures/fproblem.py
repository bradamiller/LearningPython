"""Lesson 4-0: the whole problem, before anything is broken down.

The robot at its start, a destination across the grid, no route drawn: the
students work out the sub-problems themselves, so the figure gives none away.

Output: out/drive-to-destination.svg -> static/img/lesson-m4-00/drive-to-destination.svg
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR
from common import *

RED = "#D1182C"
g = G(110, 96, sp=60, pad=30)
b = g.base(axes=False)

# start: the robot at the bottom-left corner, facing North
sx, sy = g.p(0, 0)
b.append(f'<use href="#pcXRP" transform="translate({sx} {sy}) rotate(0) scale(0.36)"/>')
b.append(tag(sx, sy + 48, "start", stroke="#22527B", cls="nb", w=56))

# destination: a red target at (2, 3)
dx, dy = g.p(2, 3)
b.append(f'<circle cx="{dx}" cy="{dy}" r="15" fill="#FFFFFF" stroke="{RED}" stroke-width="3"/>')
b.append(f'<circle cx="{dx}" cy="{dy}" r="7" fill="{RED}"/>')
b.append(tag(dx, dy - 46, "destination", stroke=RED, cls="nb", w=98))

# no route yet: a big question mark between them
qx, qy = g.x0 + 1.5 * g.sp, g.y0 + 1.5 * g.sp + 12
b.append(f'<circle cx="{qx}" cy="{qy-12}" r="22" fill="#FFFFFF" stroke="#ADB5BD" stroke-width="2" stroke-dasharray="5 4"/>')
b.append(f'<text x="{qx}" y="{qy}" text-anchor="middle" style="font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 32px; font-weight: 800; fill: #6C757D">?</text>')

X = 380
b += [f'<text class="h" x="{X}" y="70">The problem</text>',
      f'<text class="nb" x="{X}" y="102">Get the robot from where it starts</text>',
      f'<text class="nb" x="{X}" y="120">to the destination, all by itself.</text>',
      f'<text class="n" x="{X}" y="160">It can only drive along the tape.</text>',
      f'<text class="n" x="{X}" y="180">Nobody steers it, and nobody tells it</text>',
      f'<text class="n" x="{X}" y="197">which way to go at each corner.</text>',
      f'<text class="sm" x="{X}" y="240">First, one destination. By the end of</text>',
      f'<text class="sm" x="{X}" y="256">the module, several in a row.</text>']

open(OUTDIR + 'drive-to-destination.svg', 'w').write(svg(
    'The problem: drive from the start to a destination',
    'A 4 by 4 grid of black tape. The robot sits at the bottom-left corner, labeled start, '
    'facing north. A red target near the top, two columns across and three rows up, is '
    'labeled destination. Between them is a question mark and no route. Beside it: the '
    'problem is to get the robot from where it starts to the destination, all by itself. '
    'It can only drive along the tape, and nobody steers it or tells it which way to go '
    'at each corner.',
    b, H=350))
