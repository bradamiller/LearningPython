import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from common import *
DEG={2:("#FFFFFF","#22527B"),3:("#DCE8F3","#22527B"),4:("#9EC1E6","#142D50")}
def graph(x0,y0,sp,n,blocked=(),lost=(),deg=True,label=True,dashed_edges=(),mark=None):
    o=[]; P=lambda a,b:(x0+a*sp,y0+(n-1-b)*sp)
    nodes=[(r,c) for r in range(n) for c in range(n)]
    for r,c in nodes:
        for dr,dc in ((0,1),(1,0)):
            r2,c2=r+dr,c+dc
            if r2>=n or c2>=n: continue
            a,b=(r,c),(r2,c2); (x1,y1),(x2,y2)=P(*a),P(*b)
            if a in blocked or b in blocked:
                if a in dashed_edges or b in dashed_edges:
                    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#D1182C" stroke-width="2.5" stroke-dasharray="5 4" opacity="0.7"/>')
                continue
            o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#495057" stroke-width="4"/>')
    for r,c in nodes:
        x,y=P(r,c)
        if (r,c) in blocked:
            o.append(f'<circle cx="{x}" cy="{y}" r="18" fill="#F8F9FA" stroke="#ADB5BD" stroke-width="1.6" stroke-dasharray="3 3"/>')
            o.append(f'<path d="M {x-10} {y-10} L {x+10} {y+10} M {x+10} {y-10} L {x-10} {y+10}" stroke="#D1182C" stroke-width="3.2" stroke-linecap="round"/>')
            continue
        d=sum(1 for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)) if 0<=r+dr<n and 0<=c+dc<n and (r+dr,c+dc) not in blocked)
        fill,st=DEG[min(max(d,2),4)] if deg else ("#FFFFFF","#22527B")
        if (r,c) in lost: fill,st="#FFF0D1","#C77C02"
        if mark and (r,c) in mark: fill,st=mark[(r,c)]
        o.append(f'<circle cx="{x}" cy="{y}" r="18" fill="{fill}" stroke="{st}" stroke-width="2.4"/>')
        if label: o.append(f'<text class="ms" x="{x}" y="{y+4}" text-anchor="middle" style="font-size:10.5px">{r},{c}</text>')
    return o
b=['<text class="h" x="20" y="26">The 3×3 grid as a graph</text>']
b+=graph(70,80,100,3)
b+=[f'<circle cx="28" cy="318" r="9" fill="#FFFFFF" stroke="#22527B" stroke-width="2"/><text class="sm" x="42" y="322">corner: 2</text>',
    f'<circle cx="118" cy="318" r="9" fill="#DCE8F3" stroke="#22527B" stroke-width="2"/><text class="sm" x="132" y="322">edge: 3</text>',
    f'<circle cx="196" cy="318" r="9" fill="#9EC1E6" stroke="#142D50" stroke-width="2"/><text class="sm" x="210" y="322">interior: 4</text>']
open(OUTDIR+'graph-3x3.svg','w').write(svg('The 3x3 grid as a graph',
 'The 3 by 3 grid drawn as a graph: nine nodes labeled (x, y) with (0, 0) at the bottom-left, joined by edges to their neighbors above, below, left and right. The four corner nodes have 2 neighbors, the four edge nodes 3, and the center node 4.',b,W=350,H=336))
b=['<text class="h" x="20" y="26">Block (1, 1)</text>']
b+=graph(70,80,100,3,blocked=[(1,1)],lost=[(0,1),(1,0),(1,2),(2,1)],deg=False,dashed_edges=[(1,1)])
b+=['<circle cx="28" cy="318" r="9" fill="#FFF0D1" stroke="#C77C02" stroke-width="2"/><text class="sm" x="42" y="322">lost a neighbor</text>',
    '<line x1="160" y1="318" x2="186" y2="318" stroke="#D1182C" stroke-width="2.5" stroke-dasharray="5 4"/><text class="sm" x="192" y="322">edge removed</text>']
open(OUTDIR+'graph-blocked.svg','w').write(svg('Blocking a node',
 'The 3 by 3 graph with (1, 1) blocked: the node is crossed out and its four edges are removed, so the four nodes that touched it, (0, 1), (1, 0), (1, 2) and (2, 1), have each lost a neighbor.',b,W=350,H=336))
# detour problem
b=['<text class="h" x="20" y="26">Block (1, 0): get from S to D</text>']
mark={(0,0):("#142D50","#142D50"),(2,0):("#2E7D32","#2E7D32")}
b+=graph(90,80,100,3,blocked=[(1,0)],deg=False,mark=mark,label=True)
b=[e.replace('style="font-size:10.5px">0,0<','style="font-size:13px;font-weight:800;fill:#FFFFFF">S<').replace('style="font-size:10.5px">2,0<','style="font-size:13px;font-weight:800;fill:#FFFFFF">D<') for e in b]
b.append('<path d="M 106 300 C 150 336, 230 336, 272 300" fill="none" stroke="#D1182C" stroke-width="2.5" stroke-dasharray="6 4" marker-end="url(#aR)"/>')
X=380
b+=[f'<text class="n" x="{X}" y="96">Manhattan tries straight across,</text>',
    f'<text class="n" x="{X}" y="113">(0, 0) → (1, 0) → (2, 0), and</text>',
    f'<text class="n" x="{X}" y="130">(1, 0) is blocked.</text>',
    f'<text class="nb" x="{X}" y="170">Find a way around.</text>',
    f'<text class="n" x="{X}" y="190">Trace it with your finger and count</text>',
    f'<text class="n" x="{X}" y="207">the steps.</text>']
open(OUTDIR+'detour.svg','w').write(svg('Find a path around a blocked node',
 'The 3 by 3 graph with (1, 0) blocked and its edges removed. S is (0, 0) and D is (2, 0). S is the bottom-left corner and D is two to its right. A red dashed arrow shows Manhattan trying to go straight across through (1, 0), which is blocked. The task: find a way around and count the steps.',b,H=350))
