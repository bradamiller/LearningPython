import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math; from common import *
def pt(cx,cy,r,a): a=math.radians(a); return (cx+r*math.sin(a), cy-r*math.cos(a))
b=[]
panels=[("Start","(0, 0), heading 0 (N)",None,None,[(0,0,0)],[],None),
        ("Step 1 → (1, 0)","needed 1 (E)","N → E","1 clockwise turn, arrive",[(1,0,90)],[(0,0),(1,0)],((0,0),0,90,1)),
        ("Step 2 → (1, 1)","needed 0 (N)","E → S → W → N","3 clockwise turns (270°)",[(1,1,0)],[(0,0),(1,0),(1,1)],((1,0),90,360,1))]
for i,(t,l1,l2,l3,robots,route,turn) in enumerate(panels):
    x0=14+i*224
    g=G(x0+62,100,sp=100,n=2,pad=40)
    b.append(f'<text class="h" x="{x0}" y="24">{t}</text>')
    b+=[e for e in g.base(axes=True,north=False) if 'x →' not in e and 'y →' not in e]
    if route: b.append(g.route(route).replace('stroke-width="9"','stroke-width="7"'))
    if turn:
        (r,c),a0,a1,cw=turn; cx,cy=g.p(r,c); R=46
        b.append(f'<use href="#pcXRP" transform="translate({cx} {cy}) rotate({a0}) scale(0.4)" opacity="0.3"/>')
        if cw: p0,p1=pt(cx,cy,R,a0+12),pt(cx,cy,R,a1-12); flag=('1 1' if a1-a0>180 else '0 1')
        else: p0,p1=pt(cx,cy,R,a0-12),pt(cx,cy,R,a1+12); flag='0 0'
        b.append(f'<path d="M {p0[0]:.1f} {p0[1]:.1f} A {R} {R} 0 {flag} {p1[0]:.1f} {p1[1]:.1f}" fill="none" stroke="#D1182C" stroke-width="2.6" stroke-dasharray="5 3" marker-end="url(#aR)"/>')
    for r,c,h in robots:
        x,y=g.p(r,c); b.append(f'<use href="#pcXRP" transform="translate({x} {y}) rotate({h}) scale(0.4)"/>')
    y=292
    b.append(f'<text class="nb" x="{x0}" y="{y}">{l1}</text>')
    if l2: b.append(f'<text class="ms" x="{x0}" y="{y+19}">{l2}</text>')
    if l3: b.append(f'<text class="n" x="{x0}" y="{y+38}" style="fill:#D1182C;font-weight:700">{l3}</text>')
open(OUTDIR+'drive-path-loop.svg','w').write(svg('Tracing drive_path() through [(1, 0), (1, 1)]',
 'Three snapshots on the 2 by 2 corner of the grid nearest you, with (0, 0) at the bottom-left. Start: the robot at (0, 0), heading 0, north. Step 1, to (1, 0), one step right: the heading needed is 1, east; the loop turns clockwise north to east, one turn, then it arrives at (1, 0) facing east. Step 2, to (1, 1), one step up: the heading needed is 0, north; the loop turns clockwise east to south to west to north, three turns, 270 degrees, then it arrives at (1, 1) facing north.',b,H=350))
