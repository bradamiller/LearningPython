import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from common import *
rings={(0,0):0,(1,0):1,(0,1):1,(2,0):2,(0,2):2,(2,1):3,(1,2):3,(2,2):4}
parent={(1,0):(0,0),(0,1):(0,0),(2,0):(1,0),(0,2):(0,1),(2,1):(2,0),(1,2):(0,2),(2,2):(2,1)}
path=[(0,0),(1,0),(2,0),(2,1),(2,2)]
sp=80
def panel(gx,gy,title,arrows):
    P=lambda a,b:(gx+a*sp,gy+(2-b)*sp)
    o=[f'<text class="h" x="{gx-50}" y="30">{title}</text>']
    for a in range(3):
        for c in range(3):
            for da,dc in ((1,0),(0,1)):
                n2=(a+da,c+dc)
                if n2[0]>2 or n2[1]>2 or (1,1) in ((a,c),n2): continue
                (x1,y1),(x2,y2)=P(a,c),P(*n2)
                o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#ADB5BD" stroke-width="2"/>')
    for i in range(3):
        o.append(f'<text class="ax" x="{gx+i*sp}" y="{gy+2*sp+44}" text-anchor="middle">x = {i}</text>')
        o.append(f'<text class="ax" x="{gx-34}" y="{gy+(2-i)*sp+4}" text-anchor="end">y = {i}</text>')
    if arrows:
        d='M '+' L '.join(f'{P(*q)[0]} {P(*q)[1]}' for q in path)
        o.append(f'<path d="{d}" fill="none" stroke="#D1182C" stroke-width="5" stroke-linejoin="round" stroke-linecap="round" opacity="0.9"/>')
        for n,p in parent.items():
            (x1,y1),(x2,y2)=P(*n),P(*p); dx,dy=(x2-x1)/sp,(y2-y1)/sp
            o.append(f'<line x1="{x1+dx*20}" y1="{y1+dy*20}" x2="{x1+dx*44}" y2="{y1+dy*44}" stroke="#22527B" stroke-width="2.6" marker-end="url(#aB)"/>')
    x,y=P(1,1)
    o.append(f'<circle cx="{x}" cy="{y}" r="16" fill="#F8F9FA" stroke="#ADB5BD" stroke-width="1.6" stroke-dasharray="3 3"/><path d="M {x-9} {y-9} L {x+9} {y+9} M {x+9} {y-9} L {x-9} {y+9}" stroke="#D1182C" stroke-width="3" stroke-linecap="round"/>')
    for n,r in rings.items():
        x,y=P(*n); col="#142D50" if n==(0,0) else ("#2E7D32" if n==(2,2) else "#4C8BF5")
        o.append(f'<circle cx="{x}" cy="{y}" r="16" fill="{col}"/><text class="nb" x="{x}" y="{y+5}" text-anchor="middle" style="fill:#FFFFFF;font-size:15px">{r}</text>')
    return o
b=panel(110,74,"Ripples: how far from the start",False)
b+=panel(470,74,"Came from: walking back",True)
b+=['<text class="sm" x="60" y="300">Every ring is one step further out. The X never gets a number.</text>',
    '<text class="sm" x="420" y="300">4 came from 3, which came from 2, 1, 0.</text>',
    '<text class="ms" x="420" y="318">Read forward: (1,0), (2,0), (2,1), (2,2).</text>']
open(OUTDIR+'bfs-rings.svg','w').write(svg('Breadth-first search as ripples',
 'Left: a 3 by 3 grid of intersections with (0, 0) at the bottom-left. The start at the bottom-left is numbered 0. Its two neighbors are numbered 1, the two corners beyond them 2, the next two 3, and the top-right destination 4. The center intersection is crossed out and has no number. Right: the same grid with a small arrow on each numbered intersection pointing back to the one it was reached from, and the walk-back from the destination to the start highlighted: 4 to 3 to 2 to 1 to 0, down the right side and along the bottom.',b,W=720,H=332))
