import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from common import *
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'g51.py')).read().split("b=['<text class=\"h\" x=\"20\" y=\"26\">The 3×3")[0])
from sim import bfs
B=[(1,0),(1,1)]; pb=bfs((0,0),(3,0),B); pm=[(1,0),(2,0),(3,0)]
sp=52
def grid(gx,gy,path,col):
    P=lambda a,b:(gx+a*sp,gy+(3-b)*sp)
    g=graph(gx,gy,sp,4,blocked=B,deg=False,label=False)
    g=[e.replace('r="18"','r="9"').replace('stroke-width="4"','stroke-width="3"').replace('M {x-10} {y-10}','') for e in g]
    pts=[(0,0)]+path; d='M '+' L '.join(f'{P(*q)[0]} {P(*q)[1]}' for q in pts)
    g.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round" opacity="0.7"/>')
    for q,l,c in (((0,0),"S","#142D50"),((3,0),"D","#2E7D32")):
        x,y=P(*q); g.append(f'<circle cx="{x}" cy="{y}" r="11" fill="{c}"/><text class="sm" x="{x}" y="{y+4}" text-anchor="middle" style="fill:#FFFFFF;font-weight:700">{l}</text>')
    return g,P
def badge(x,y,n,col):
    return f'<circle cx="{x}" cy="{y}" r="9" fill="#FFFFFF" stroke="{col}" stroke-width="1.8"/><text class="sm" x="{x}" y="{y+4}" text-anchor="middle" style="fill:{col};font-weight:700">{n}</text>'
b=['<text class="h" x="12" y="24">BFS: all pass</text>']
g,P=grid(46,64,pb,"#2E7D32"); b+=g
x,y=P(0,1); b.append(badge(x-22,y,"1","#2E7D32"))
x,y=P(3,0); b.append(badge(x-22,y+18,"2","#2E7D32"))
x,y=P(2,2); b.append(badge(x+20,y,"3","#2E7D32"))
x,y=P(1,1); b.append(badge(x+16,y+16,"4","#2E7D32"))
b.append(f'<text class="nb" x="12" y="262" style="fill:#2E7D32">7 steps, PASS</text>')
legend=[("1","first step: next to the start"),("2","last step: the destination"),("3","every step: next to the one before"),("4","no step is blocked"),("5","open grid: steps = Manhattan distance")]
X=236
b.append(f'<text class="h" x="{X}" y="24">What must be true</text>')
for i,(n,t) in enumerate(legend):
    y=64+i*28
    b.append(badge(X+9,y-4,n,"#22527B")+f'<text class="n" x="{X+24}" y="{y}" style="font-size:12px">{t}</text>')
b+=[f'<text class="sm" x="{X}" y="214">Any path with all five is correct,</text>',f'<text class="sm" x="{X}" y="230">whichever of the shortest ones it is.</text>']
b.append('<text class="h" x="486" y="24" style="fill:#D1182C">Manhattan: FAIL</text>')
g,P=grid(504,64,pm,"#D1182C"); b+=g
x,y=P(1,0); b.append(badge(x+20,y,"4","#D1182C"))
b+=['<text class="nb" x="486" y="262" style="fill:#D1182C">drives through blocked</text>','<text class="nb" x="486" y="279" style="fill:#D1182C">intersection (1, 0)</text>']
open(OUTDIR+'path-properties.svg','w').write(svg('Five properties of a correct path',
 'Test 4: from S at (0, 0), the bottom-left, to D at (3, 0), the bottom-right, on a 4 by 4 grid with (1, 0) and (1, 1) blocked. Left, the BFS path around the wall, 7 steps, with badges showing properties 1 to 4 holding: the first step is next to the start, the last step is the destination, every step is next to the one before, and no step is blocked. Middle, the five properties; the fifth, steps equal the Manhattan distance, is only checked on an open grid. Right, Manhattan\'s path goes straight across through blocked (1, 0) and fails property 4.',b,H=292))
# planner slot
b=[]
b.append('<rect x="160" y="40" width="360" height="120" rx="12" fill="#F1F6FB" stroke="#22527B" stroke-width="2"/>')
b.append('<text class="m" x="340" y="68" text-anchor="middle">run_all_tests(name, planner)</text>')
b.append('<text class="sm" x="340" y="88" text-anchor="middle">the same six cases, the same checks</text>')
b.append('<rect x="222" y="104" width="236" height="40" rx="8" fill="#FFFFFF" stroke="#22527B" stroke-width="2" stroke-dasharray="6 4"/>')
b.append('<text class="ms" x="340" y="128" text-anchor="middle">planner(position, destination)</text>')
for x,name,col,res in ((60,"compute_manhattan_path","#C77C02","Manhattan: 4 of 6 passed"),(440,"compute_bfs_path","#2E7D32","BFS: 6 of 6 passed")):
    b.append(f'<rect x="{x}" y="196" width="190" height="38" rx="8" fill="#FFFFFF" stroke="{col}" stroke-width="2"/><text class="ms" x="{x+95}" y="219" text-anchor="middle">{name}</text>')
    b.append(f'<path d="M {x+95} 194 C {x+95} 172, 340 176, 340 148" fill="none" stroke="{col}" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#aG)"/>')
    b.append(f'<text class="nb" x="{x+95}" y="254" text-anchor="middle" style="fill:{col}">{res}</text>')
b+=['<text class="n" x="340" y="286" text-anchor="middle">Hand the harness a function, no parentheses: <tspan class="ms">run_all_tests("BFS", compute_bfs_path)</tspan></text>']
open(OUTDIR+'planner-slot.svg','w').write(svg('One harness, either planner',
 'The test harness run_all_tests(name, planner) runs the same six cases and checks, calling planner(position, destination) through a slot. Either compute_manhattan_path or compute_bfs_path can be handed in. Manhattan passes 4 of 6; BFS passes 6 of 6. Hand the harness the function with no parentheses: run_all_tests("BFS", compute_bfs_path).',b,H=300))
