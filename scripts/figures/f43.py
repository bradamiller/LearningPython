import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from common import *
g=G(95,95); b=g.base()
pts=[(0,0),(2,0),(2,3)]
b.append(g.route(pts))
steps=[(1,0),(2,0),(2,1),(2,2),(2,3)]
x,y=g.p(0,0)
b.append(f'<use href="#pcXRP" transform="translate({x} {y}) rotate(0) scale(0.42)"/>')
b.append(tag(x+2,y-44,"start",fill="#F1F3F5",stroke="#868E96",cls="nb",w=50))
for i,(r,c) in enumerate(steps):
    b.append(g.dot(r,c,"#FFFFFF","#22527B",7))
    px,py=g.p(r,c)
    if c==0: b.append(tag(px,py+28,f"path[{i}]",fill="#DCE8F3"))
    else: b.append(tag(px+50,py+2,f"path[{i}]",fill="#DCE8F3"))
X=405; Y=150; bw=50
b.append(f'<text class="h" x="{X}" y="70">The list holds where it drives TO</text>')
b.append(f'<text class="m" x="{X}" y="{Y-24}">path =</text>')
for i,(r,c) in enumerate(steps):
    bx=X+i*bw
    b.append(f'<rect x="{bx}" y="{Y-14}" width="{bw}" height="30" fill="#DCE8F3" stroke="#22527B" stroke-width="1.4"/>')
    b.append(f'<text class="ms" x="{bx+bw/2}" y="{Y+5}" text-anchor="middle">({r},{c})</text>')
    b.append(f'<text class="sm" x="{bx+bw/2}" y="{Y+34}" text-anchor="middle">[{i}]</text>')
b+=[f'<text class="n" x="{X}" y="{Y+76}">5 places to drive to, so</text>',
    f'<text class="m" x="{X}" y="{Y+96}">len(path)</text><text class="n" x="{X+78}" y="{Y+96}">is 5: the number of steps.</text>',
    f'<text class="n" x="{X}" y="{Y+132}">The robot already stands on (0, 0),</text>',
    f'<text class="n" x="{X}" y="{Y+150}">so the start is <tspan font-weight="700">not</tspan> in the list.</text>']
open(OUTDIR+'path-list.svg','w').write(svg('A path is a list of the places the robot drives to',
 'The 4 by 4 grid with the route from (0, 0), the bottom-left corner, to (2, 3): two steps right, then three steps up. The robot sits on (0, 0), marked start. The five intersections it drives to are tagged path[0] (1, 0), path[1] (2, 0), path[2] (2, 1), path[3] (2, 2) and path[4] (2, 3). Beside it the list is drawn as five boxes with indexes 0 to 4: len(path) is 5, the number of steps, and the start is not in the list.',b,H=385))
