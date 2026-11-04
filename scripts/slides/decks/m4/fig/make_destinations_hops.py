"""Slide-only figure for Module 4: a list of far-apart destinations, and the
list of single-hop intersections the planner returns for each leg.

    python3 scripts/slides/decks/m4/fig/make_destinations_hops.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'figures'))
from common import G, svg  # noqa: E402

HOME = (0, 0)
DESTS = [(2, 0), (2, 3), (0, 3)]
COLORS = ['#4C8BF5', '#2E7D32', '#8E44AD']


def manhattan(a, b):
    """Same rule as compute_manhattan_path: across until x is right, then up or down."""
    (x, y), path = a, []
    while x != b[0]:
        x += 1 if b[0] > x else -1
        path.append((x, y))
    while y != b[1]:
        y += 1 if b[1] > y else -1
        path.append((x, y))
    return path


g = G(70, 62, sp=86, n=4)
body = g.base()
legs, pos = [], HOME
for dest, col in zip(DESTS, COLORS):
    path = manhattan(pos, dest)
    legs.append((pos, dest, path, col))
    body.append(g.route([pos] + path, col))
    pos = dest
for start, dest, path, col in legs:
    for q in path[:-1]:
        body.append(g.dot(*q, fill='#FFFFFF', stroke=col, rad=7))
hx, hy = g.p(*HOME)
body.append(f'<circle cx="{hx}" cy="{hy}" r="13" fill="#142D50"/>'
            f'<text class="nb" x="{hx}" y="{hy+4.5}" text-anchor="middle" style="fill:#FFFFFF">H</text>')
for i, (start, dest, path, col) in enumerate(legs, 1):
    x, y = g.p(*dest)
    body.append(f'<circle cx="{x}" cy="{y}" r="14" fill="#F28C28" stroke="#FFFFFF" stroke-width="2.5"/>'
                f'<text class="nb" x="{x}" y="{y+4.5}" text-anchor="middle" style="fill:#FFFFFF">{i}</text>')

X = 420
body.append(f'<text class="h" x="{X}" y="40">Handed in: the destinations, far apart</text>')
body.append(f'<rect x="{X}" y="52" width="320" height="30" rx="6" fill="#FFF4E6" stroke="#F28C28" stroke-width="1.6"/>')
body.append(f'<text class="m" x="{X+12}" y="72">destinations = [(2, 0), (2, 3), (0, 3)]</text>')
body.append(f'<text class="sm" x="{X}" y="100">Each one can be many intersections from the last.</text>')
body.append(f'<text class="h" x="{X}" y="140">Handed back: one list of hops per leg</text>')
y = 168
for i, (start, dest, path, col) in enumerate(legs, 1):
    txt = '[' + ', '.join(f'({a}, {b})' for a, b in path) + ']'
    body.append(f'<rect x="{X}" y="{y-16}" width="320" height="50" rx="6" fill="#FFFFFF" stroke="{col}" stroke-width="2"/>')
    body.append(f'<text class="nb" x="{X+12}" y="{y+2}" style="fill:{col}">Leg {i}: {start} to {dest}, {len(path)} hops</text>')
    body.append(f'<text class="m" x="{X+12}" y="{y+22}">{txt}</text>')
    y += 62
body.append(f'<text class="n" x="{X}" y="{y+2}">Each intersection in a list is <tspan class="nb">one hop</tspan> from the one</text>')
body.append(f'<text class="n" x="{X}" y="{y+20}">before it, so the driver only ever goes one block.</text>')

out = svg('Destinations, and the hops the planner returns',
          'A 4 by 4 grid. From home at (0, 0) the robot visits three destinations: (2, 0), (2, 3) and '
          '(0, 3). The destinations are several intersections apart. For each leg the planner returns '
          'a list of adjacent intersections: leg 1 is [(1, 0), (2, 0)], leg 2 is [(2, 1), (2, 2), (2, 3)], '
          'leg 3 is [(1, 3), (0, 3)].',
          body, W=760, H=430)
open(os.path.join(HERE, 'destinations-hops.svg'), 'w').write(out)
print('wrote destinations-hops.svg')
