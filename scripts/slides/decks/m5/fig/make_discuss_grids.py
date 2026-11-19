"""Slide-only grids for the Module 5 discussions (Lessons 5-1 and 5-2).

Each question slide shows the grid as it stands when the question is asked;
each answer slide shows what the class has just written, new numbers circled.
Same look as the lessons' bfs-wave-from-d-xy.svg (scripts/figures/grings.py).

    python3 scripts/slides/decks/m5/fig/make_discuss_grids.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SP, R, X0, Y0, N = 110, 24, 110, 50, 4

STYLE = '''<style>
    .ax { font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 17px; font-weight: 700; fill: #6C757D; }
    .lb { font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 22px; font-weight: 800; fill: #142D50; }
    .nm { font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 21px; font-weight: 800; fill: #FFFFFF; }
  </style>'''
MARK = '''<defs>
    <marker id="aB" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#22527B"/></marker>
    <marker id="aT" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#C77C02"/></marker>
  </defs>'''


def P(a, b):
    return X0 + a * SP, Y0 + (N - 1 - b) * SP


def bfs(dest, blocked):
    dist, todo = {dest: 0}, [dest]
    while todo:
        x, y = todo.pop(0)
        for n in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= n[0] < N and 0 <= n[1] < N and n not in blocked and n not in dist:
                dist[n] = dist[(x, y)] + 1
                todo.append(n)
    return dist


def draw(name, title, start, dest, blocked=(), upto=-1, new=(), paths=(), desc=''):
    """upto: show numbers 0..upto (-1: none). new: numbers to circle in orange.
    paths: [(list of intersections, 'main' | 'alt')]"""
    blocked = set(blocked)
    dist = bfs(dest, blocked)
    o = []
    for a in range(N):
        for b in range(N):
            for n2 in ((a + 1, b), (a, b + 1)):
                if n2[0] >= N or n2[1] >= N or (a, b) in blocked or n2 in blocked:
                    continue
                (x1, y1), (x2, y2) = P(a, b), P(*n2)
                o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#ADB5BD" stroke-width="3"/>')
    for i in range(N):
        o.append(f'<text class="ax" x="{X0 + i * SP}" y="{Y0 + (N - 1) * SP + 58}" text-anchor="middle">x = {i}</text>')
        o.append(f'<text class="ax" x="{X0 - 48}" y="{Y0 + (N - 1 - i) * SP + 6}" text-anchor="end">y = {i}</text>')
    for pts, kind in paths:
        col, w, dash, mk = (('#D1182C', 8, '', 'aB') if kind == 'main'
                            else ('#C77C02', 8, ' stroke-dasharray="14 10"', 'aT'))
        off = 0
        d = 'M ' + ' L '.join(f'{P(*q)[0] + off} {P(*q)[1] + off}' for q in pts)
        o.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{w}"{dash} '
                 f'stroke-linejoin="round" stroke-linecap="round" opacity="0.85"/>')
        if pts:
            for a, c in zip(pts, pts[1:]):
                (x1, y1), (x2, y2) = P(*a), P(*c)
                dx, dy = (x2 - x1) / SP, (y2 - y1) / SP
                o.append(f'<line x1="{x1 + dx * 34}" y1="{y1 + dy * 34}" x2="{x1 + dx * 72}" '
                         f'y2="{y1 + dy * 72}" stroke="{'#22527B' if kind == 'main' else '#C77C02'}" stroke-width="3.5" marker-end="url(#{mk})"/>')
    for a in range(N):
        for b in range(N):
            n = (a, b)
            x, y = P(*n)
            if n in blocked:
                o.append(f'<circle cx="{x}" cy="{y}" r="{R}" fill="#F8F9FA" stroke="#ADB5BD" stroke-width="2" stroke-dasharray="4 4"/>'
                         f'<path d="M {x - 12} {y - 12} L {x + 12} {y + 12} M {x + 12} {y - 12} L {x - 12} {y + 12}" stroke="#D1182C" stroke-width="4" stroke-linecap="round"/>')
                continue
            num = dist.get(n)
            shown = num is not None and num <= upto
            if n == start:
                fill, stroke = '#142D50', '#142D50'
            elif n == dest:
                fill, stroke = '#2E7D32', '#2E7D32'
            elif shown:
                fill, stroke = '#4C8BF5', '#4C8BF5'
            else:
                fill, stroke = '#FFFFFF', '#ADB5BD'
            if shown and num in new:
                o.append(f'<circle cx="{x}" cy="{y}" r="{R + 8}" fill="none" stroke="#C77C02" stroke-width="4"/>')
            o.append(f'<circle cx="{x}" cy="{y}" r="{R}" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>')
            if shown:
                o.append(f'<text class="nm" x="{x}" y="{y + 7.5}" text-anchor="middle">{num}</text>')
    for n, lab in ((start, 'S'), (dest, 'D')):
        x, y = P(*n)
        dx = 46 if n[0] == N - 1 else -46
        o.append(f'<text class="lb" x="{x + dx}" y="{y - 22}" text-anchor="middle">{lab}</text>')
    w, h = X0 + (N - 1) * SP + 80, Y0 + (N - 1) * SP + 74
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="fT fD">
  <title id="fT">{title}</title>
  <desc id="fD">{desc}</desc>
  {STYLE}
  {MARK}
  <rect width="{w}" height="{h}" fill="#FFFFFF"/>
  {(chr(10) + '  ').join(o)}
</svg>
'''
    with open(os.path.join(HERE, name + '.svg'), 'w') as f:
        f.write(svg)


# Lesson 5-1, "How far away is everything?": 4x4, S (0,0), D (3,3), no obstacles
S, D = (0, 0), (3, 3)
draw('d51-grid', 'A 4 by 4 grid, S to D', S, D,
     desc='A 4 by 4 grid with S at (0, 0), bottom-left, and D at (3, 3), top-right. No numbers yet.')
draw('d51-zero', 'D gets 0', S, D, upto=0,
     desc='The 4 by 4 grid with D, at (3, 3), numbered 0.')
draw('d51-ones', 'The 1s', S, D, upto=1, new={1},
     desc='The 4 by 4 grid: D is 0, and (2, 3) and (3, 2) are circled with a 1.')
draw('d51-ones-q', 'The 1s', S, D, upto=1,
     desc='The 4 by 4 grid: D is 0, and (2, 3) and (3, 2) are 1.')
draw('d51-twos-q', 'The 2s', S, D, upto=2,
     desc='The 4 by 4 grid: D is 0, two 1s, and three 2s at (1, 3), (2, 2) and (3, 1).')
draw('d51-twos', 'The 2s', S, D, upto=2, new={2},
     desc='The 4 by 4 grid: D is 0, two 1s, and (1, 3), (2, 2) and (3, 1) circled with a 2.')
draw('d51-full', 'Every intersection numbered', S, D, upto=6, new={6},
     desc='The 4 by 4 grid numbered from D: each intersection holds its steps to D. S, at (0, 0), is 6.')

# The wall: (1,0) and (1,1) blocked, S (0,0), D (3,0). Used by 5-1 Q5 and all of 5-2's first discussion
S, D, WALL = (0, 0), (3, 0), {(1, 0), (1, 1)}
draw('d51-wall', 'The wall grid', S, D, WALL,
     desc='A 4 by 4 grid with (1, 0) and (1, 1) blocked. S is (0, 0) and D is (3, 0), across the bottom row. No numbers yet.')
draw('d51-wall-full', 'The wall grid, numbered from D', S, D, WALL, upto=7,
     desc='The wall grid numbered from D. The numbers flow around the blocked intersections; S is 7.')
draw('d52-first-step', 'First step from the 7', S, D, WALL, upto=7, paths=[([(0, 0), (0, 1)], 'main')],
     desc='The numbered wall grid with one step drawn from S, the 7, up to (0, 1), the 6: away from D.')
WALK = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (3, 1), (3, 0)]
draw('d52-walk', 'Walking downhill to D', S, D, WALL, upto=7, paths=[(WALK, 'main')],
     desc='The numbered wall grid with the walk from S: up the left column, along y = 2, down the right column to D. Each step goes to a neighbor one less: 7, 6, 5, 4, 3, 2, 1, 0.')
draw('d52-tie', 'Two shortest paths', S, D, WALL, upto=7,
     paths=[(WALK, 'main'), ([(2, 2), (2, 1), (2, 0), (3, 0)], 'alt')],
     desc='The walk from S, with a second, dashed route where (2, 2), a 3, has two neighbors numbered 2: one goes right then down, the other down the x = 2 column. Both reach D in 7 steps.')
