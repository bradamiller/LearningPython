"""Lesson 5-2: breadth-first search from the destination, one step at a time, for <StepFigure>.

The lesson's 3x3 trace ((0, 0) to (2, 2), center blocked), numbered FROM D, with
Back / Step / Play: every frame is a step stop, and the panel on the right says in
plain words what just happened. After the wave fills the grid it walks downhill from S,
one step per frame, then says why the path is the shortest.

Output: out/bfs-downhill-steps.svg -> static/img/lesson-m5-03/bfs-downhill-steps-xy.svg
(replaces bfs-steps-xy.svg, the came-from version that g53steps.py still makes).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR
from common import *
# graph() and the arrow marker come from g51.py's preamble, as g53.py does it
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'g51.py')).read()
     .split("b=['<text class=\"h\" x=\"20\" y=\"26\">The 3×3")[0])

x0, y0, sp = 70, 100, 110
P = lambda a, b: (x0 + a * sp, y0 + (2 - b) * sp)
NUM = {(2, 2): 0, (1, 2): 1, (2, 1): 1, (0, 2): 2, (2, 0): 2, (0, 1): 3, (1, 0): 3, (0, 0): 4}
FROM = {}                       # no came-from arrows: the numbers are the map
PATH = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
W = list(zip(PATH, PATH[1:]))   # the walk downhill, one segment per step
# One dict per step: look = intersection being looked around, new = numbered this step,
# queue = to-visit list after the step, walk = segments of the downhill walk highlighted.
STEPS = [
    dict(new=[(2, 2)], queue=['(2,2)'], head='Write 0 on the destination, D.',
         lines=['D is 0 steps from itself.', 'It goes on the to-visit list.']),
    dict(look=(2, 2), new=[(1, 2), (2, 1)], queue=['(1,2)', '(2,1)'],
         head='Take the oldest: (2,2).',
         lines=['Its open neighbors, (1,2) and (2,1),', 'are 1 step from D: they get 1.']),
    dict(look=(1, 2), new=[(0, 2)], queue=['(2,1)', '(0,2)'], head='Take the oldest: (1,2).',
         lines=['(0,2) gets 2. The middle is blocked,', 'and (2,2) already has a number.']),
    dict(look=(2, 1), new=[(2, 0)], queue=['(0,2)', '(2,0)'], head='Take the oldest: (2,1).',
         lines=['(2,0) gets 2. Now every spot 1 step', 'from D has been looked around, and', 'every spot 2 steps away has a 2.']),
    dict(look=(0, 2), new=[(0, 1)], queue=['(2,0)', '(0,1)'], head='Take the oldest: (0,2).',
         lines=['(0,1) gets 3.']),
    dict(look=(2, 0), new=[(1, 0)], queue=['(0,1)', '(1,0)'], head='Take the oldest: (2,0).',
         lines=['(1,0) gets 3.']),
    dict(look=(0, 1), new=[(0, 0)], queue=['(1,0)', '(0,0)'], head='Take the oldest: (0,1).',
         lines=['S gets 4: it is 4 steps from D.', 'It still goes on the list.']),
    dict(look=(1, 0), new=[], queue=['(0,0)'], head='Take the oldest: (1,0).',
         lines=['Its neighbors already have numbers,', 'so nothing new is written. A number', 'is never changed.']),
    dict(look=(0, 0), new=[], queue=[], head='Take the oldest: (0,0), S.',
         lines=['Nothing new, and the list is empty:', 'every spot has its number. Now walk', 'downhill from S.']),
    dict(walk=W[:1], queue=[], head='From S, 4 to 3: step to (1,0).',
         lines=['S has two neighbors with a 3. Either', 'works; take the first one checked.']),
    dict(walk=W[:2], queue=[], head='3 to 2: step to (2,0).', lines=[]),
    dict(walk=W[:3], queue=[], head='2 to 1: step to (2,1).', lines=[]),
    dict(walk=W[:4], showpath=True, queue=[], head='1 to 0: that is D. Stop.',
         lines=['The spots you stepped onto, in order:']),
    dict(walk=W, showpath=True, queue=[], head='Why is it the shortest path?',
         lines=['Every 1 was written before any 2,', "every 2 before any 3. So S's 4 is", 'the fewest steps to D.']),
]
FD = 1.8                        # seconds per step when playing
N = len(STEPS)
T = N * FD + 2.5                # total, with a hold on the last step before it loops
DUR = f'dur="{T:.2f}s" repeatCount="indefinite"'


def vis(a, b):
    """Visible from step a through step b (inclusive)."""
    on = round(a * FD / T, 4) or 0.0001
    off = round((b + 1) * FD / T, 4) if b < N - 1 else 1
    if off >= 1:
        return f'<animate attributeName="opacity" values="0;1" keyTimes="0;{on}" calcMode="discrete" {DUR}/>'
    return (f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{on};{off}" '
            f'calcMode="discrete" {DUR}/>')


def at(a, b, body):
    return f'<g opacity="0">{vis(a, b)}{body}</g>'


b = ['<text class="h" x="20" y="28">Breadth-first search, one step at a time</text>']
mark = {(0, 0): ("#142D50", "#142D50"), (2, 2): ("#2E7D32", "#2E7D32")}
g = graph(x0, y0, sp, 3, blocked=[(1, 1)], deg=False, mark=mark)
g = [e.replace('style="font-size:10.5px">0,0<', 'style="font-size:13px;font-weight:800;fill:#FFFFFF">S<')
      .replace('style="font-size:10.5px">2,2<', 'style="font-size:13px;font-weight:800;fill:#FFFFFF">D<') for e in g]
under = []   # walk-back highlights, drawn before the graph so they sit beneath the circles
b_graph = g
anim, still, top = [], [], []   # top: number badges, drawn over the rings

first = {n: i for i, s in enumerate(STEPS) for n in s.get('new', [])}
for n, k in first.items():
    x, y = P(*n)
    badge = (f'<circle cx="{x + 20}" cy="{y - 20}" r="11" fill="#D1182C"/>'
             f'<text class="nb" x="{x + 20}" y="{y - 15.5}" text-anchor="middle" style="fill:#FFFFFF">{NUM[n]}</text>')
    top.append(at(k, N - 1, badge)); still.append(badge)
    # what changed this step: a green halo, on its own step only
    anim.append(at(k, k, f'<circle cx="{x}" cy="{y}" r="27" fill="none" stroke="#2E7D32" stroke-width="3.5"/>'))
    if n in FROM:
        (x1, y1), (x2, y2) = P(*FROM[n]), (x, y)
        dx, dy = (x2 - x1) / sp, (y2 - y1) / sp
        arrow = (f'<line x1="{x1 + dx * 24}" y1="{y1 + dy * 24}" x2="{x2 - dx * 26}" y2="{y2 - dy * 26}" '
                 f'stroke="#4C8BF5" stroke-width="3.5" marker-end="url(#aB)"/>')
        anim.append(at(k, N - 1, arrow)); still.append(arrow)

for i, s in enumerate(STEPS):
    if s.get('look'):
        x, y = P(*s['look'])
        anim.append(at(i, i, f'<circle cx="{x}" cy="{y}" r="27" fill="none" stroke="#C77C02" '
                             f'stroke-width="3.5" stroke-dasharray="6 4"/>'))
    for (a, c) in s.get('walk', []):
        (x1, y1), (x2, y2) = P(*a), P(*c)
        under.append(at(i, i, f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#D1182C" '
                             f'stroke-width="9" stroke-linecap="round" opacity="0.35"/>'))

X = 372
for i, s in enumerate(STEPS):
    t = [f'<text class="sm" x="{X}" y="68">step {i + 1} of {N}</text>',
         f'<text class="h" x="{X}" y="92">{s["head"]}</text>']
    for j, line in enumerate(s['lines']):
        t.append(f'<text class="n" x="{X}" y="{116 + j * 18}">{line}</text>')
    if s.get('showpath'):
        t.append(f'<text class="m" x="{X}" y="{116 + len(s["lines"]) * 18 + 4}">'
                 '[(1,0), (2,0), (2,1), (2,2)]</text>')
    anim.append(at(i, i, ''.join(t)))

# the to-visit list, as it stands after each step
b += [f'<text class="nb" x="{X}" y="206">to-visit list</text>',
      f'<rect x="{X}" y="216" width="296" height="44" rx="8" fill="#F8F9FA" stroke="#DEE2E6"/>',
      f'<text class="sm" x="{X}" y="278">take from the front</text>',
      f'<text class="sm" x="{X + 296}" y="278" text-anchor="end">add to the back</text>']
for i, s in enumerate(STEPS):
    els = []
    for j, item in enumerate(s['queue']):
        bx = X + 10 + j * 78
        els.append(f'<rect x="{bx}" y="224" width="70" height="28" rx="6" fill="#FFFFFF" '
                   f'stroke="#22527B" stroke-width="1.6"/>'
                   f'<text class="m" x="{bx + 35}" y="243" text-anchor="middle">{item}</text>')
    if not s['queue']:
        els.append(f'<text class="sm" x="{X + 14}" y="243">empty</text>')
    anim.append(at(i, i, ''.join(els)))

b += [f'<circle cx="{X + 8}" cy="318" r="8" fill="#D1182C"/><text class="sm" x="{X + 21}" y="322">steps to D</text>',
      f'<line x1="{X + 112}" y1="318" x2="{X + 136}" y2="318" stroke="#D1182C" stroke-width="8" stroke-linecap="round" opacity="0.4"/>'
      f'<text class="sm" x="{X + 142}" y="322">walk</text>',
      f'<circle cx="{X + 230}" cy="318" r="9" fill="none" stroke="#C77C02" stroke-width="3" stroke-dasharray="4 3"/>'
      f'<text class="sm" x="{X + 244}" y="322">looking</text>',
      f'<circle cx="{X + 8}" cy="344" r="9" fill="none" stroke="#2E7D32" stroke-width="3"/>'
      f'<text class="sm" x="{X + 21}" y="348">just numbered</text>']

b += ['<g class="anim">' + ''.join(under) + '</g>',
      '<g class="still">' + f'<path d="{"M " + " L ".join(f"{P(*q)[0]} {P(*q)[1]}" for q in PATH)}" fill="none" '
      'stroke="#D1182C" stroke-width="9" stroke-linejoin="round" stroke-linecap="round" opacity="0.35"/></g>']
b += b_graph
style = '<style>.still{display:none} @media (prefers-reduced-motion: reduce){.anim{display:none}.still{display:inline}}</style>'
b.append('<g class="anim">' + ''.join(anim) + ''.join(top) + '</g>')
pd = 'M ' + ' L '.join(f'{P(*q)[0]} {P(*q)[1]}' for q in PATH)
b.append('<g class="still">' + ''.join(still) +
         f'<text class="h" x="{X}" y="92">The finished search</text>'
         f'<text class="m" x="{X}" y="120">[(1,0), (2,0), (2,1), (2,2)]</text></g>')

DESC = ('A step-by-step animation of breadth-first search on the 3 by 3 grid, (0, 0) at the bottom-left, '
        'with the center (1, 1) blocked, from S at (0, 0) to D at (2, 2), with the numbers written from D. '
        'Step 1: D gets 0 and goes on the to-visit list. Each later step takes the oldest intersection from '
        'the front of the list; every open neighbor without a number gets the next number and a place at the '
        'back of the list. (1, 2) and (2, 1) get 1; (0, 2) and (2, 0) get 2; (0, 1) and (1, 0) get 3; S gets 4. '
        'When the list is empty every intersection has its number. Then the walk downhill from S, one step '
        'at a time, always to a neighbor one less: to (1, 0), (2, 0), (2, 1) and D, so the path is '
        '[(1, 0), (2, 0), (2, 1), (2, 2)]. The last step explains why it is the shortest: every 1 was written '
        "before any 2 and every 2 before any 3, so S's 4 is the fewest steps.")
out = svg('Breadth-first search, one step at a time', DESC, b, H=370)
out = out.replace('<rect width="680"', style + '\n  <rect width="680"', 1)
steps = ','.join(f'{(i + 1) * FD - 0.05:.2f}' for i in range(N))
out = out.replace('<svg ', f'<svg data-steps="{steps}" data-dur="{T:.2f}" ', 1)
open(OUTDIR + 'bfs-downhill-steps.svg', 'w').write(out)
print(OUTDIR + 'bfs-downhill-steps.svg', N, 'steps', round(T, 1), 's')
