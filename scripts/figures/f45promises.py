import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR
from common import *
# Lesson 4-5: the planner's three promises, labeled on one path.
g=G(84,62,sp=72); b=g.base(north=False)
BL,OR="#4C8BF5","#C77C02"
start,dest=(0,0),(2,1)
path=[(1,0),(2,0),(2,1)]
b.append(g.route([start]+path,BL))
for q in path[:-1]: b.append(g.dot(*q))
b.append(g.dot(*dest,"#142D50","#142D50",9))
x,y=g.p(*start)
b.append(f'<use href="#pcXRP" transform="translate({x} {y}) scale(0.36)"/>')
def badge(cx,cy,n): return f'<circle cx="{cx}" cy="{cy}" r="12" fill="{OR}"/><text class="nb" x="{cx}" y="{cy+4.5}" text-anchor="middle" style="fill:#FFFFFF">{n}</text>'
b.append(badge(x+30,y-30,1))
dx,dy=g.p(*dest)
b.append(badge(dx+30,dy-30,2))
X=372
b+=[f'<text class="h" x="{X}" y="44">Three promises</text>',
    f'<text class="ms" x="{X}" y="72">compute_manhattan_path((0, 0), (2, 1))</text>',
    f'<text class="ms" x="{X}" y="92">→ [(1, 0), (2, 0), (2, 1)]</text>']
rows=[(1,'Never includes the start.','(0, 0) is where the robot already is.'),
      (2,'Ends at the destination.','The last element is (2, 1).'),
      (3,'Empty if already there.',None)]
for i,(n,a,c) in enumerate(rows):
    yy=136+i*56
    b.append(badge(X+12,yy-4,n))
    b.append(f'<text class="nb" x="{X+32}" y="{yy}">{a}</text>')
    if c: b.append(f'<text class="sm" x="{X+32}" y="{yy+18}">{c}</text>')
yy=136+2*56+18
b.append(f'<text class="ms" x="{X+32}" y="{yy}">compute_manhattan_path((1, 1), (1, 1))</text>')
b.append(f'<text class="ms" x="{X+32}" y="{yy+18}">→ []</text>')
open(OUTDIR+'three-promises.svg','w').write(svg('The planner\'s three promises',
 'A 4 by 4 grid with the robot at (0, 0) and the path from (0, 0) to (2, 1) drawn in blue through (1, 0) and (2, 0). Badge 1 sits by the robot at (0, 0), badge 2 by the destination (2, 1). Beside it, compute_manhattan_path((0, 0), (2, 1)) returns [(1, 0), (2, 0), (2, 1)], and the three promises: 1, never includes the start, because (0, 0) is where the robot already is; 2, ends at the destination, the last element is (2, 1); 3, empty if already there: compute_manhattan_path((1, 1), (1, 1)) returns [].',b,W=690,H=360))
