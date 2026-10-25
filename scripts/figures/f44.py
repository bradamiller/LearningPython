import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from common import *
b=[]
cx,cy=170,180
b.append('<text class="h" x="20" y="28">Four loops, one per direction</text>')
b.append(f'<rect x="20" y="44" width="300" height="300" rx="8" fill="#F8F9FA" stroke="#DEE2E6"/>')
b.append(f'<rect x="{cx-4.5}" y="{cy-44}" width="9" height="88" fill="#2B2B2B"/><rect x="{cx-44}" y="{cy-4.5}" width="88" height="9" fill="#2B2B2B"/>')
b.append(f'<circle cx="{cx}" cy="{cy}" r="8" fill="#FFFFFF" stroke="#22527B" stroke-width="2.4"/>')
cards=[("north","y + 1","while y &lt; dest",0,-1),("south","y − 1","while y &gt; dest",0,1),("east","x + 1","while x &lt; dest",1,0),("west","x − 1","while x &gt; dest",-1,0)]
for name,step,cond,dx,dy in cards:
    b.append(f'<line x1="{cx+dx*12}" y1="{cy+dy*12}" x2="{cx+dx*40}" y2="{cy+dy*40}" stroke="#4C8BF5" stroke-width="4"/>')
    b.append(f'<path d="M {cx+dx*50} {cy+dy*50} L {cx+dx*38-dy*7} {cy+dy*38-dx*7} L {cx+dx*38+dy*7} {cy+dy*38+dx*7} z" fill="#4C8BF5"/>')
    if dy: bx,by=cx,(cy-100 if dy<0 else cy+118)
    else: bx,by=cx+dx*70,cy+56
    w=124; h=44
    b.append(f'<rect x="{bx-w/2}" y="{by-h/2}" width="{w}" height="{h}" rx="7" fill="#FFFFFF" stroke="#22527B" stroke-width="1.4"/>')
    b.append(f'<text class="nb" x="{bx}" y="{by-4}" text-anchor="middle">{name}: {step}</text>')
    b.append(f'<text class="ms" x="{bx}" y="{by+13}" text-anchor="middle">{cond}</text>')
g=G(376,104,sp=52,pad=24); b+=['<text class="h" x="342" y="28">One trip: (1, 3) → (3, 0)</text>']
b+=g.base(axes=True,north=False)
b.append(g.route([(1,3),(3,3),(3,0)]))
for (r,c) in [(2,3),(3,3),(3,2),(3,1),(3,0)]: b.append(g.dot(r,c,"#FFFFFF","#22527B",6))
b.append(g.dot(1,3,"#142D50","#142D50",7))
x,y=g.p(1,3); b.append(tag(x-36,y-16,"start",fill="#F1F3F5",stroke="#868E96",cls="nb",w=46))
X=566; Y=104
rows=[("east","runs 2×",True),("west","skipped",False),("north","skipped",False),("south","runs 3×",True)]
for i,(n,t,on) in enumerate(rows):
    y=Y+i*32
    col="#2E7D32" if on else "#ADB5BD"; fill="#E1F0E3" if on else "#F8F9FA"
    b.append(f'<rect x="{X}" y="{y-15}" width="100" height="25" rx="12" fill="{fill}" stroke="{col}" stroke-width="1.4"/>')
    b.append(f'<text class="nb" x="{X+10}" y="{y+2}" style="fill:{col}">{n}</text><text class="sm" x="{X+92}" y="{y+2}" text-anchor="end" style="fill:{col}">{t}</text>')
b+=['<text class="n" x="342" y="336">A loop whose condition starts False</text>',
    '<text class="n" x="342" y="353">never runs, so no if/else is needed.</text>',
    '<text class="ms" x="342" y="376">[(2,3), (3,3), (3,2), (3,1), (3,0)]</text>']
open(OUTDIR+'four-loops.svg','w').write(svg('The four while loops of the Manhattan planner',
 'Left: one intersection with four arrows. North: y plus 1, while y &lt; dest. South: y minus 1, while y &gt; dest. East: x plus 1, while x &lt; dest. West: x minus 1, while x &gt; dest. Right: the trip from (1, 3) to (3, 0) on a 4 by 4 grid with (0, 0) at the bottom-left: the path goes two steps right, then three steps down. East runs twice, west is skipped, north is skipped, south runs three times. A loop whose condition starts False never runs, so no if/else is needed. The path is [(2,3), (3,3), (3,2), (3,1), (3,0)].',b,H=390))
