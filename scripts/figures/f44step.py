import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR
from common import *
# Lesson 4-3: one step changes x or y by 1, never both.
g=G(210,64,sp=110,n=3); b=g.base(axes=False,north=False)
n,sp,pad=g.n,g.sp,g.pad
ox,oy=g.p(0,0)
XC,YC,GC="#D1182C","#2E7D32","#868E96"
cx,cy=g.p(1,1); s=24
def arrow(a,c,col,mk):
    x,y=g.p(a,c); dx,dy=x-cx,y-cy; d=(dx*dx+dy*dy)**.5
    x1,y1=cx+dx/d*s,cy+dy/d*s; x2,y2=x-dx/d*s,y-dy/d*s
    return f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{col}" stroke-width="5" stroke-linecap="round" marker-end="url(#{mk})"/>'
# diagonal, crossed out
x,y=g.p(2,2); dx,dy=x-cx,y-cy; d=(dx*dx+dy*dy)**.5
b.append(f'<line x1="{cx+dx/d*s:.0f}" y1="{cy+dy/d*s:.0f}" x2="{x-dx/d*s:.0f}" y2="{y-dy/d*s:.0f}" stroke="{GC}" stroke-width="4" stroke-dasharray="8 7" stroke-linecap="round"/>')
mx,my=(cx+x)/2,(cy+y)/2
b.append(f'<path d="M{mx-13},{my-13} L{mx+13},{my+13} M{mx-13},{my+13} L{mx+13},{my-13}" stroke="{XC}" stroke-width="5" stroke-linecap="round"/>')
for a,c,col,mk in [(2,1,XC,'aR'),(0,1,XC,'aR'),(1,2,YC,'aGr'),(1,0,YC,'aGr')]:
    b.append(arrow(a,c,col,mk))
for a,c in [(0,1),(2,1),(1,0),(1,2),(2,2)]: b.append(g.dot(a,c))
b.append(g.dot(1,1,"#142D50","#142D50",9))
lab=lambda x,y,t,col,anc="middle": f'<text class="h" x="{x}" y="{y}" text-anchor="{anc}" style="fill:{col}">{t}</text>'
x,y=g.p(2,1); b.append(lab(x+42,y-14,"x + 1",XC,"start")); b.append(lab(x+42,y+10,"(2, 1)","#343A40","start"))
x,y=g.p(0,1); b.append(lab(x-46,y-14,"x − 1",XC,"end")); b.append(lab(x-46,y+10,"(0, 1)","#343A40","end"))
x,y=g.p(1,2); b.append(lab(x-18,y-22,"y + 1",YC,"end")); b.append(lab(x+18,y-22,"(1, 2)","#343A40","start"))
x,y=g.p(1,0); b.append(lab(x-18,y+44,"y − 1",YC,"end")); b.append(lab(x+18,y+44,"(1, 0)","#343A40","start"))
x,y=g.p(2,2); b.append(lab(x+42,y-14,"(2, 2): x and y",GC,"start")); b.append(lab(x+42,y+10,"both change.",GC,"start")); b.append(lab(x+42,y+34,"Not one step.",XC,"start"))
b.append(tag(cx+52,cy+28,"(1, 1)",fill="#DCE8F3",stroke="#142D50"))
W=640; H=oy+pad+46
open(OUTDIR+'one-step.svg','w').write(svg('One step changes x or y by 1',
 'A 3 by 3 grid of tape lines with the robot\'s intersection (1, 1) in the middle. Four arrows leave it, one to each neighbor: red arrows right to (2, 1), labeled x + 1, and left to (0, 1), labeled x − 1; green arrows up to (1, 2), labeled y + 1, and down to (1, 0), labeled y − 1. A dashed gray diagonal to (2, 2) is crossed out in red: x and y both change, so it is not one step.',b,W=W,H=H))
