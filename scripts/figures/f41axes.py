import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR
from common import *
# Lesson 4-1: the origin and the two directions coordinates grow in.
g=G(170,125,sp=80); b=g.base(axes=False,north=False)
n,sp,pad=g.n,g.sp,g.pad; L=(n-1)*sp
ox,oy=g.p(0,0)
for i in range(n):
    b.append(f'<text class="ax" x="{g.p(i,0)[0]}" y="{oy+pad+18}" text-anchor="middle">{i}</text>')
    b.append(f'<text class="ax" x="{ox-pad-12}" y="{g.p(0,i)[1]+4}" text-anchor="end">{i}</text>')
XC,YC="#D1182C","#2E7D32"
xe=ox+L+pad+46; ye=oy-L-pad-40
b.append(f'<line x1="{ox}" y1="{oy}" x2="{xe}" y2="{oy}" stroke="{XC}" stroke-width="5" stroke-linecap="round" marker-end="url(#aR)"/>')
b.append(f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{ye}" stroke="{YC}" stroke-width="5" stroke-linecap="round" marker-end="url(#aGr)"/>')
b.append(f'<text class="h" x="{xe+12}" y="{oy+5}" style="fill:{XC}">increasing x</text>')
b.append(f'<text class="h" x="{ox}" y="{ye-26}" text-anchor="middle" style="fill:{YC}">increasing y</text>')
for (a,c) in [(3,0),(0,3),(2,1),(1,2),(3,3)]:
    b.append(g.dot(a,c))
    x,y=g.p(a,c); b.append(tag(x+36,y-20,f"({a}, {c})"))
b.append(f'<circle cx="{ox}" cy="{oy}" r="15" fill="none" stroke="#142D50" stroke-width="2.4"/>')
b.append(g.dot(0,0,"#142D50","#142D50",8))
b.append(tag(ox+62,oy-22,"origin (0, 0)",fill="#DCE8F3",stroke="#142D50"))
W=640; H=oy+pad+44
open(OUTDIR+'coordinate-axes.svg','w').write(svg('x and y on the grid',
 'A 4 by 4 grid of black tape. The bottom-left intersection is ringed and labeled (0, 0), the origin. A red arrow starts at the origin and points right along the bottom line, labeled increasing x. A green arrow starts at the origin and points up along the left line, labeled increasing y. x is numbered 0 to 3 along the bottom and y 0 to 3 up the left side. Labeled intersections: (3, 0) bottom-right, (0, 3) top-left, (2, 1), (1, 2) and (3, 3) top-right.',b,W=W,H=H))
