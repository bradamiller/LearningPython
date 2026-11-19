"""Grids for the Module 4 guided discussions (Lessons 4-2 and 4-4).

4-2, "Where does the path go?": a 4x4 grid, S (0,0), D (2,3) (Leg 1 of the
delivery run), then Leg 2, (2,3) to (1,0).
4-4, "Driving the path": the robot at (1,0) on Leg 1, and which way to face.

Same look as the Module 5 discussion grids (scripts/slides/decks/m5/fig/).
Lesson pages and slide decks use the same files.

    python3 m4discuss.py     # writes out/m4d-*.svg
    cp out/m4d-*.svg ../../static/img/lesson-m4-discuss/
"""
from _paths import OUTDIR

SP, R, X0, Y0, N = 110, 24, 110, 50, 4
NAVY, GREEN, RED, ORANGE, BLUE, GRAY = '#142D50', '#2E7D32', '#D1182C', '#C77C02', '#22527B', '#ADB5BD'

STYLE = '''<style>
    .ax { font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 17px; font-weight: 700; fill: #6C757D; }
    .lb { font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 22px; font-weight: 800; fill: #142D50; }
    .nm { font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 800; fill: #FFFFFF; }
    .co { font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 700; fill: #142D50; }
    .dir { font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 800; fill: #22527B; }
  </style>'''
DEFS = f'''<defs>
    <marker id="aR" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{RED}"/></marker>
    <marker id="aT" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{ORANGE}"/></marker>
    <marker id="aB" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{BLUE}"/></marker>
  </defs>'''

LEG1 = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]
UP_FIRST = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3)]
LEG2 = [(2, 3), (1, 3), (1, 2), (1, 1), (1, 0)]


def P(a, b):
    return X0 + a * SP, Y0 + (N - 1 - b) * SP


def draw(name, title, desc, start=None, dest=None, paths=(), numbered=None, coords=False,
         robot=None, ring=(), arrows=(), faint=()):
    """paths: [(points, 'main' | 'alt')]. numbered: points to number 1, 2, 3, ... in order.
    coords: label each numbered point with its (x, y). robot: the robot's intersection.
    ring: intersections circled in orange. arrows: [(from, to, label)], drawn blue.
    faint: a path drawn light gray (the planned path, for context)."""
    o = []
    for a in range(N):
        for b in range(N):
            for n2 in ((a + 1, b), (a, b + 1)):
                if n2[0] >= N or n2[1] >= N:
                    continue
                (x1, y1), (x2, y2) = P(a, b), P(*n2)
                o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{GRAY}" stroke-width="3"/>')
    for i in range(N):
        o.append(f'<text class="ax" x="{X0 + i * SP}" y="{Y0 + (N - 1) * SP + 58}" text-anchor="middle">x = {i}</text>')
        o.append(f'<text class="ax" x="{X0 - 48}" y="{Y0 + (N - 1 - i) * SP + 6}" text-anchor="end">y = {i}</text>')
    if faint:
        d = 'M ' + ' L '.join(f'{P(*q)[0]} {P(*q)[1]}' for q in faint)
        o.append(f'<path d="{d}" fill="none" stroke="#F1A9B1" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>')
    for pts, kind in paths:
        col, dash, mk = ((RED, '', 'aR') if kind == 'main' else (ORANGE, ' stroke-dasharray="14 10"', 'aT'))
        d = 'M ' + ' L '.join(f'{P(*q)[0]} {P(*q)[1]}' for q in pts)
        o.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="8"{dash} '
                 f'stroke-linejoin="round" stroke-linecap="round" opacity="0.85"/>')
        for a, c in zip(pts, pts[1:]):
            (x1, y1), (x2, y2) = P(*a), P(*c)
            dx, dy = (x2 - x1) / SP, (y2 - y1) / SP
            o.append(f'<line x1="{x1 + dx * 34}" y1="{y1 + dy * 34}" x2="{x1 + dx * 72}" y2="{y1 + dy * 72}" '
                     f'stroke="{col}" stroke-width="3.5" marker-end="url(#{mk})"/>')
    for a, c, label in arrows:
        (x1, y1), (x2, y2) = P(*a), P(*c)
        dx, dy = (x2 - x1) / SP, (y2 - y1) / SP
        o.append(f'<line x1="{x1 + dx * 30}" y1="{y1 + dy * 30}" x2="{x2 - dx * 36}" y2="{y2 - dy * 36}" '
                 f'stroke="{BLUE}" stroke-width="6" marker-end="url(#aB)"/>')
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        if dy == 0:
            o.append(f'<text class="dir" x="{mx}" y="{my + 34}" text-anchor="middle">{label}</text>')
        else:
            o.append(f'<text class="dir" x="{mx + 18}" y="{my + 6}">{label}</text>')
    nums = {p: i + 1 for i, p in enumerate(numbered or [])}
    for a in range(N):
        for b in range(N):
            n = (a, b)
            x, y = P(*n)
            if n == robot or n == start:
                fill = NAVY
            elif n == dest:
                fill = GREEN
            elif n in nums:
                fill = '#4C8BF5'
            else:
                fill = None
            if n in ring:
                o.append(f'<circle cx="{x}" cy="{y}" r="{R + 8}" fill="none" stroke="{ORANGE}" stroke-width="4"/>')
            if fill:
                o.append(f'<circle cx="{x}" cy="{y}" r="{R}" fill="{fill}" stroke="{fill}" stroke-width="2.5"/>')
            else:
                o.append(f'<circle cx="{x}" cy="{y}" r="{R}" fill="#FFFFFF" stroke="{GRAY}" stroke-width="2.5"/>')
            if n in nums:
                o.append(f'<text class="nm" x="{x}" y="{y + 7}" text-anchor="middle">{nums[n]}</text>')
            if coords and n in nums:
                o.append(f'<text class="co" x="{x + 30}" y="{y + 32}">({a},{b})</text>')
    for n, lab in ((start, 'S'), (dest, 'D'), (robot, 'robot')):
        if n is None:
            continue
        x, y = P(*n)
        o.append(f'<text class="lb" x="{x - 34}" y="{y - 26}" text-anchor="middle">{lab}</text>')
    w, h = X0 + (N - 1) * SP + 90, Y0 + (N - 1) * SP + 74
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="fT fD">
  <title id="fT">{title}</title>
  <desc id="fD">{desc}</desc>
  {STYLE}
  {DEFS}
  <rect width="{w}" height="{h}" fill="#FFFFFF"/>
  {(chr(10) + '  ').join(o)}
</svg>
'''
    with open(OUTDIR + name + '.svg', 'w') as f:
        f.write(svg)


# ---- Lesson 4-2, "Where does the path go?" ----
S, D = (0, 0), (2, 3)
draw('m4d-42-grid', 'A 4 by 4 grid, S to D',
     'A 4 by 4 grid with S at (0, 0), bottom-left, and D at (2, 3), on the top row.',
     S, D)
draw('m4d-42-routes', 'Two of the shortest routes',
     'The 4 by 4 grid from S at (0, 0) to D at (2, 3). A solid red route goes right to (2, 0), '
     'then up to D. A dashed orange route goes up to (0, 3), then right to D. Both are 5 blocks.',
     S, D, paths=[(UP_FIRST, 'alt'), (LEG1, 'main')])
draw('m4d-42-route', 'East, then north',
     'The 4 by 4 grid with one route from S at (0, 0) to D at (2, 3): right to (2, 0), then up to D.',
     S, D, paths=[(LEG1, 'main')])
draw('m4d-42-path', 'The path, east then north',
     'The 4 by 4 grid with the route from S at (0, 0) to D at (2, 3): right to (1, 0) and (2, 0), '
     'then up to (2, 1), (2, 2) and (2, 3). The five intersections it drives to are numbered 1 to 5 '
     'and labeled with their coordinates. S has no number.',
     S, D, paths=[(LEG1, 'main')], numbered=LEG1[1:], coords=True)
draw('m4d-42-leg2-q', 'Leg 2: S at (2, 3), D at (1, 0)',
     'The 4 by 4 grid with S at (2, 3), on the top row, and D at (1, 0), on the bottom row.',
     (2, 3), (1, 0))
draw('m4d-42-leg2', 'Leg 2: west, then south',
     'The 4 by 4 grid from S at (2, 3) to D at (1, 0): one step left to (1, 3), then down to (1, 2), '
     '(1, 1) and (1, 0), numbered 1 to 4 with their coordinates. Both x and y get smaller.',
     (2, 3), (1, 0), paths=[(LEG2, 'main')], numbered=LEG2[1:], coords=True)

# ---- Lesson 4-4, "Driving the path" ----
draw('m4d-44-q1', 'At (1, 0), the next stop is (2, 0)',
     'The 4 by 4 grid with Leg 1\'s path from (0, 0) to (2, 3) drawn faintly. The robot is at (1, 0). '
     'The next stop on the path, (2, 0), is circled.',
     robot=(1, 0), ring={(2, 0)}, faint=LEG1)
draw('m4d-44-a1', 'Face East',
     'The robot at (1, 0) with an arrow right to the next stop, (2, 0), labeled East.',
     robot=(1, 0), ring={(2, 0)}, faint=LEG1, arrows=[((1, 0), (2, 0), 'East')])
draw('m4d-44-q2', 'Other next stops',
     'The robot at (1, 0). Two other possible next stops are circled: (1, 1), above it, and (0, 0), '
     'to its left.',
     robot=(1, 0), ring={(1, 1), (0, 0)})
draw('m4d-44-a2', 'North and West',
     'The robot at (1, 0), with an arrow up to (1, 1) labeled North and an arrow left to (0, 0) '
     'labeled West.',
     robot=(1, 0), ring={(1, 1), (0, 0)},
     arrows=[((1, 0), (1, 1), 'North'), ((1, 0), (0, 0), 'West')])
print('wrote m4d-*.svg to', OUTDIR)
