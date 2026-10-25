import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from common import *
g=G(95,70); b=g.base()
x0,y0=g.p(0,0); x1,y1=g.p(2,0); x2,y2=g.p(2,3)
b.append(f'<path d="M {x0} {y0} L {x1} {y1} L {x2} {y2}" fill="none" stroke="#2E7D32" stroke-width="4" stroke-dasharray="8 5" stroke-linejoin="round"/>')
b.append(f'<text class="nb" x="{(x0+x1)/2+20}" y="{y0-14}" text-anchor="middle" style="fill:#2E7D32;paint-order:stroke;stroke:#F3F4F6;stroke-width:5px">2 right</text>')
b.append(f'<text class="nb" x="{x1+40}" y="{y1-44}" text-anchor="middle" style="fill:#2E7D32;paint-order:stroke;stroke:#F3F4F6;stroke-width:5px">3 up</text>')
for (a,c),fill,st in [((0,0),"#FFFFFF","#142D50"),((3,3),"#FFFFFF","#142D50"),((2,3),"#4C8BF5","#22527B"),((3,2),"#F59F00","#C77C02")]:
    b.append(g.dot(a,c,fill,st,8))
b.append(tag(g.p(0,0)[0]+34,g.p(0,0)[1]+22,"(0, 0)"))
b.append(tag(g.p(3,3)[0]+2,g.p(3,3)[1]-22,"(3, 3)"))
b.append(tag(g.p(2,3)[0]-38,g.p(2,3)[1]-22,"(2, 3)",fill="#DCE8F3"))
b.append(tag(g.p(3,2)[0]+2,g.p(3,2)[1]+26,"(3, 2)",fill="#FFF0D1",stroke="#C77C02"))
b.append(f'<text class="sm" x="{x0+40}" y="{y0+84}" text-anchor="middle" style="fill:#22527B;font-weight:700">you stand on this side</text>')
X=410
b+=[f'<text class="h" x="{X}" y="60">x first, then y</text>',
    f'<text class="n" x="{X}" y="82">x: how far <tspan font-weight="700">across</tspan> to the right</text>',
    f'<text class="n" x="{X}" y="100">y: how far <tspan font-weight="700">up</tspan>, away from you</text>',
    f'<text class="n" x="{X}" y="118">both count from 0, so the corner</text>',
    f'<text class="n" x="{X}" y="136">nearest you is (0, 0)</text>',
    f'<text class="h" x="{X}" y="180">Order matters</text>',
    f'<text class="n" x="{X}" y="202"><tspan font-weight="700" fill="#22527B">(2, 3)</tspan> and <tspan font-weight="700" fill="#C77C02">(3, 2)</tspan> are different</text>',
    f'<text class="n" x="{X}" y="220">intersections.</text>',
    f'<text class="h" x="{X}" y="264">Steps between two spots</text>',
    f'<text class="n" x="{X}" y="286">(0, 0) to (2, 3): <tspan fill="#2E7D32" font-weight="700">2 right + 3 up</tspan></text>',
    f'<text class="n" x="{X}" y="304">= 5 steps, the Manhattan distance.</text>',
    f'<text class="sm" x="{X}" y="330">No diagonals: the robot follows the lines.</text>']
open(OUTDIR+'coordinates.svg','w').write(svg('(x, y) coordinates on the grid',
 'A 4 by 4 grid of taped lines as it lies in front of you. x is numbered 0 to 3 along the bottom, left to right; y is numbered 0 to 3 up the left side, from the near edge to the far edge; north is away from you. The bottom-left intersection, nearest you, is (0, 0) and the far top-right is (3, 3). Two highlighted intersections, (2, 3) and (3, 2), are in different places. A dotted path from (0, 0) goes 2 right and 3 up to (2, 3): 5 steps, the Manhattan distance.',b,H=400))
