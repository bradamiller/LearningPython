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


def draw(name, title, start, dest, blocked=(), upto=-1, new=(), paths=(), desc='',
         visited=None, ring=(), lists=(), shown=None, side=False):
    """upto: show numbers 0..upto (-1: none). new: numbers to circle in orange.
    paths: [(list of intersections, 'main' | 'alt')]
    The computer's way (5-2): shown = the intersections numbered so far (overrides upto);
    visited = those already visited, drawn gray, with a legend; ring = intersections to
    circle in orange; lists = [(label, [items])] to-visit lists drawn under the grid."""
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
            if shown is not None:
                on = n in shown
            else:
                on = num is not None and num <= upto
            if n == start:
                fill, stroke = '#142D50', '#142D50'
            elif n == dest:
                fill, stroke = '#2E7D32', '#2E7D32'
            elif on and visited is not None and n in visited:
                fill, stroke = '#8A939C', '#8A939C'
            elif on:
                fill, stroke = '#4C8BF5', '#4C8BF5'
            else:
                fill, stroke = '#FFFFFF', '#ADB5BD'
            if on and (num in new or n in ring):
                o.append(f'<circle cx="{x}" cy="{y}" r="{R + 8}" fill="none" stroke="#C77C02" stroke-width="4"/>')
            o.append(f'<circle cx="{x}" cy="{y}" r="{R}" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>')
            if on:
                o.append(f'<text class="nm" x="{x}" y="{y + 7.5}" text-anchor="middle">{num}</text>')
    for n, lab in ((start, 'S'), (dest, 'D')):
        x, y = P(*n)
        dx = 46 if n[0] == N - 1 else -46
        o.append(f'<text class="lb" x="{x + dx}" y="{y - 22}" text-anchor="middle">{lab}</text>')
    w, h = X0 + (N - 1) * SP + 80, Y0 + (N - 1) * SP + 74
    if visited is not None:
        y = h + 14
        o.append(f'<circle cx="40" cy="{y}" r="12" fill="#8A939C"/>'
                 f'<text class="ax" x="60" y="{y + 6}">visited</text>'
                 f'<circle cx="190" cy="{y}" r="12" fill="#4C8BF5"/>'
                 f'<text class="ax" x="210" y="{y + 6}">numbered, waiting</text>')
        h += 40
    gw, gh = w, h
    if side:
        w, h = w + 470, 30
    for label, items in lists:
        y = h + 10
        lx = gw + 20 if side else 28
        o.append(f'<text class="ax" x="{lx}" y="{y + 14}">{label}</text>')
        y += 28
        if not items:
            o.append(f'<rect x="{lx}" y="{y}" width="150" height="40" rx="7" fill="#FFFFFF" stroke="#ADB5BD" stroke-width="2" stroke-dasharray="6 5"/>'
                     f'<text class="ax" x="{lx + 75}" y="{y + 26}" text-anchor="middle">empty</text>')
        for i, it in enumerate(items):
            x = lx + i * 104
            o.append(f'<rect x="{x}" y="{y}" width="92" height="40" rx="7" fill="#FFFFFF" stroke="#22527B" stroke-width="2.5"/>'
                     f'<text class="lb" x="{x + 46}" y="{y + 28}" text-anchor="middle" style="font-size:19px">({it[0]},{it[1]})</text>')
        if items:
            o.append(f'<text class="ax" x="{lx + 46}" y="{y + 64}" text-anchor="middle">front</text>'
                     f'<text class="ax" x="{lx + (len(items) - 1) * 104 + 46}" y="{y + 64}" text-anchor="middle">end</text>')
            h += 26
        h += 82
    if side:
        h = max(gh, h)
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


# Lesson 5-2, "How a computer numbers the grid": the open 4x4 from 5-1, S (0,0), D (3,3),
# neighbors checked left, right, down, up.
S, D = (0, 0), (3, 3)
draw('dc-visit-d', 'Visiting D', S, D, shown={D, (2, 3), (3, 2)}, visited={D}, ring={(2, 3), (3, 2)},
     desc='The 4 by 4 grid with D at (3, 3). D has been visited: its open neighbors (2, 3) and (3, 2) got a 1 and are circled.')
draw('dc-q1', 'Which one next?', S, D, shown={D, (2, 3), (3, 2), (1, 3), (2, 2)}, visited={D, (2, 3)},
     ring={(3, 2), (1, 3), (2, 2)},
     desc='D and the 1 at (2, 3) have been visited and are gray. Three intersections are numbered and waiting, circled: the 1 at (3, 2) and the 2s at (1, 3) and (2, 2).')
draw('dc-a1', 'Visit (3,2) next', S, D, shown={D, (2, 3), (3, 2), (1, 3), (2, 2), (3, 1)},
     visited={D, (2, 3), (3, 2)}, ring={(3, 1)},
     desc='(3, 2), the 1, has now been visited too: its neighbor (3, 1) got a 2, circled. Both 1s are visited before any 2.')
draw('dc-a2', 'The to-visit list', S, D, shown={D, (2, 3), (3, 2), (1, 3), (2, 2), (3, 1)},
     visited={D, (2, 3), (3, 2)}, ring={(3, 1)},
     lists=[('Before visiting (3,2):', [(3, 2), (1, 3), (2, 2)]),
            ('After: (3,2) off the front, (3,1) on the end', [(1, 3), (2, 2), (3, 1)])], side=True,
     desc='The grid after visiting (3, 2), with the to-visit list before, (3, 2), (1, 3), (2, 2), and after, (1, 3), (2, 2), (3, 1).')
ALL = set(bfs(D, set()))
draw('dc-a3', 'Every intersection visited', S, D, shown=ALL, visited=ALL, lists=[('To-visit list:', [])],
     desc='The whole 4 by 4 grid numbered from D and visited. S is 6. The to-visit list is empty.')
draw('dc-walk', 'Walking downhill needs only the numbers', S, D, upto=6,
     paths=[([(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)], 'main')],
     desc='The numbered 4 by 4 grid with a walk from S, the 6, always to a neighbor one less: right along the bottom, then up the right side to D.')
draw('dc-full', 'Every intersection numbered', S, D, upto=6,
     desc='The 4 by 4 grid numbered from D: each intersection holds its steps to D. S, at (0, 0), is 6.')
