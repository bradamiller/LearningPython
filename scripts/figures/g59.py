import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from common import *
b=['<text class="h" x="12" y="24">The capstone run</text>']
g=G(52,66,sp=54,pad=24); b+=g.base(axes=False,north=False)
for q in [(1,0),(2,2),(3,1)]:
    x,y=g.p(*q); b.append(f'<rect x="{x-12}" y="{y-12}" width="24" height="24" rx="3" fill="#C8A26B" stroke="#7A5C2E" stroke-width="1.5"/>')
x,y=g.p(0,0); b.append(f'<use href="#pcXRP" transform="translate({x} {y}) scale(0.3)"/>')
for i,q in enumerate([(1,3),(3,3),(3,0),(0,0)]):
    x,y=g.p(*q); dx,dy=(14,-14) if q!=(0,0) else (22,22)
    b.append(f'<circle cx="{x+dx}" cy="{y+dy}" r="11" fill="#22527B" stroke="#FFFFFF" stroke-width="2"/><text class="sm" x="{x+dx}" y="{y+dy+4}" text-anchor="middle" style="fill:#FFFFFF;font-weight:700">{i+1}</text>')
b.append('<text class="sm" x="12" y="290">CAPSTONE_DESTINATIONS, in order;</text><text class="sm" x="12" y="306">boxes = SIMULATED_OBSTACLES</text>')
X=250
b.append(f'<text class="h" x="{X}" y="24">The blocked list is the thread</text>')
legs=[("leg 1","→ (1, 3)","4 steps, 1 reroute",["(1,0)"]),("leg 2","→ (3, 3)","2 steps",["(1,0)"]),("leg 3","→ (3, 0)","9 steps, 2 reroutes",["(1,0)","(3,1)","(2,2)"]),("leg 4","→ (0, 0)","5 steps",["(1,0)","(3,1)","(2,2)"])]
b.append(f'<text class="nb" x="{X}" y="52">Run 1, starting from []</text>')
for i,(l,d,s,lst) in enumerate(legs):
    y=66+i*44
    b.append(f'<rect x="{X}" y="{y}" width="130" height="36" rx="6" fill="#F1F6FB" stroke="#22527B" stroke-width="1.4"/><text class="nb" x="{X+8}" y="{y+15}">{l} <tspan class="ms" style="font-size:11px">{d}</tspan></text><text class="sm" x="{X+8}" y="{y+30}">{s}</text>')
    b.append(f'<line x1="{X+132}" y1="{y+18}" x2="{X+150}" y2="{y+18}" stroke="#C77C02" stroke-width="1.6" marker-end="url(#aG)"/>')
    for j,item in enumerate(lst):
        new = (i==0 and j==0) or (i==2 and j>0)
        b.append(f'<rect x="{X+154+j*58}" y="{y+6}" width="54" height="24" rx="5" fill="{"#FFE3A8" if new else "#FFF8E8"}" stroke="#C77C02" stroke-width="{2 if new else 1.2}"/><text class="ms" x="{X+181+j*58}" y="{y+22}" text-anchor="middle" style="font-size:11px">{item}</text>')
b.append(f'<text class="sm" x="{X}" y="252">Run 1: 20 steps, 3 reroutes. It prints the list at the end;</text>')
b.append(f'<text class="sm" x="{X}" y="268">you type it into KNOWN_OBSTACLES.</text>')
b.append(f'<rect x="{X}" y="280" width="418" height="34" rx="6" fill="#F2F8F2" stroke="#2E7D32" stroke-width="1.6"/><text class="nb" x="{X+10}" y="302">Run 2 starts with <tspan class="ms" style="font-size:11.5px">[(1,0), (3,1), (2,2)]</tspan>: 18 steps, 0 reroutes</text>')
open(OUTDIR+'capstone-thread.svg','w').write(svg('The blocked list across the capstone',
 'Left: the 4 by 4 grid with the robot at home, (0, 0), the bottom-left corner, the four capstone destinations numbered in order, (1, 3), (3, 3), (3, 0) and (0, 0), and three pretend boxes at (1, 0), (2, 2) and (3, 1). Right: Run 1 starts with an empty blocked list. Leg 1 to (1, 3) takes 4 steps and 1 reroute and adds (1, 0). Leg 2 to (3, 3) takes 2 steps. Leg 3 to (3, 0) takes 9 steps and 2 reroutes and adds (3, 1) and (2, 2). Leg 4 home takes 5 steps. Run 1 totals 20 steps and 3 reroutes and prints the list, which you type into KNOWN_OBSTACLES; Run 2 starts with [(1, 0), (3, 1), (2, 2)] and takes 18 steps with 0 reroutes.',b,H=326))
