import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
from common import *
# ---------- 5-0 overview: one box, two planners ----------
RED,GRN,NAVY="#D1182C","#2E7D32","#142D50"
BOX=(2,0)
manh=[(0,0),(1,0),(2,0),(3,0),(3,1),(3,2)]
bfs=[(0,0),(1,0),(1,1),(2,1),(3,1),(3,2)]
g=G(80,112,sp=80)
b=['<text class="h" x="20" y="26">One box, two planners</text>']
b+=g.base(axes=True,north=False)
# Manhattan: drawn up to the box, then faded where it would have gone
pts=[g.p(*q) for q in manh]
b.append(f'<path d="M {pts[0][0]} {pts[0][1]} L {pts[2][0]} {pts[2][1]}" fill="none" stroke="{RED}" stroke-width="6" stroke-linecap="round" opacity="0.85"/>')
b.append(f'<path d="M {pts[2][0]} {pts[2][1]} L {pts[3][0]} {pts[3][1]} L {pts[5][0]} {pts[5][1]}" fill="none" stroke="{RED}" stroke-width="3" stroke-dasharray="6 5" stroke-linejoin="round" opacity="0.6"/>')
# BFS: around the box
b.append(g.route(bfs,GRN).replace('stroke-width="9"','stroke-width="6"'))
# the box
x,y=g.p(*BOX)
b.append(f'<rect x="{x-16}" y="{y-16}" width="32" height="32" rx="3" fill="#C8A26B" stroke="#7A5C2E" stroke-width="1.6"/>')
b.append(f'<path d="M {x-9} {y-9} L {x+9} {y+9} M {x+9} {y-9} L {x-9} {y+9}" stroke="{RED}" stroke-width="3.2" stroke-linecap="round"/>')
for q,l,c in (((0,0),"S",NAVY),((3,2),"D",GRN)):
    x,y=g.p(*q); b.append(f'<circle cx="{x}" cy="{y}" r="11" fill="{c}" stroke="#FFFFFF" stroke-width="2"/><text class="sm" x="{x}" y="{y+4}" text-anchor="middle" style="fill:#FFFFFF;font-weight:700">{l}</text>')
def card(x,y,w,h,col,lines):
    o=[f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#FFFFFF" stroke="{col}" stroke-width="2"/>']
    for i,(cls,t) in enumerate(lines):
        st=f' style="fill:{col}"' if i==0 else ''
        o.append(f'<text class="{cls}" x="{x+14}" y="{y+24+i*20}"{st}>{t}</text>')
    return o
X=400
b+=card(X,92,262,92,RED,[("nb","Module 4 · Manhattan"),("n","across, then up: one route only"),("n","and it runs through the box")])
b+=card(X,202,262,92,GRN,[("nb","Module 5 · breadth-first search"),("n","finds a shortest route around"),("n","anything blocked: 5 steps")])
b+=[f'<text class="sm" x="{X}" y="322">And if a box turns up while it drives, the</text>',
    f'<text class="sm" x="{X}" y="338">rangefinder sees it and the robot plans again.</text>']
open(OUTDIR+'blocked-route.svg','w').write(svg('One box, two planners',
 'A 4 by 4 grid of tape with (0, 0) at the bottom-left. A box blocks the intersection (2, 0). From S at (0, 0) to D at (3, 2), the Manhattan route goes across first, through (1, 0) and into the box at (2, 0), where it is crossed out; the rest of its route, on to (3, 0) and up to (3, 2), is faded. The breadth-first search route finds a shortest way around: right to (1, 0), up to (1, 1), right through (2, 1) to (3, 1), and up to D: 5 steps, the same as if the box were not there. A note: if a box turns up while the robot drives, the rangefinder sees it and the robot plans again.',b,H=430))
