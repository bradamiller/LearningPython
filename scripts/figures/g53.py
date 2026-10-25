import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from common import *
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'g51.py')).read().split("b=['<text class=\"h\" x=\"20\" y=\"26\">The 3×3")[0])
FR=10; FD=1.7; TOT=FR*FD+3.5
DUR=f'dur="{TOT}s" repeatCount="indefinite"'
def kt(i): return round(i*FD/TOT,4)
def vis(a,b=None):
    # visible from frame a through frame b (inclusive); b None = until end of loop hold
    end = kt(b+1) if b is not None else round((FR*FD+3.0)/TOT,4)
    return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{kt(a) if a>0 else 0.0001};{end}" calcMode="discrete" {DUR}/>'
x0,y0,sp=70,96,110
P=lambda a,b:(x0+a*sp,y0+(2-b)*sp)
b=['<text class="h" x="20" y="28">Breadth-first search, ring by ring</text>']
mark={(0,0):("#142D50","#142D50"),(2,2):("#2E7D32","#2E7D32")}
g=graph(x0,y0,sp,3,blocked=[(1,1)],deg=False,mark=mark)
g=[e.replace('style="font-size:10.5px">0,0<','style="font-size:13px;font-weight:800;fill:#FFFFFF">S<').replace('style="font-size:10.5px">2,2<','style="font-size:13px;font-weight:800;fill:#FFFFFF">D<') for e in g]
b+=g
rings={(0,0):(0,0),(1,0):(1,1),(0,1):(1,1),(2,0):(2,2),(0,2):(2,3),(2,1):(3,4),(1,2):(3,5),(2,2):(4,6)}
parent={(1,0):(0,0),(0,1):(0,0),(2,0):(1,0),(0,2):(0,1),(2,1):(2,0),(1,2):(0,2),(2,2):(2,1)}
anim=[]; still=[]
for n,(ring,f) in rings.items():
    x,y=P(*n); el=f'<circle cx="{x+20}" cy="{y-20}" r="11" fill="#D1182C"/><text class="nb" x="{x+20}" y="{y-15.5}" text-anchor="middle" style="fill:#FFFFFF">{ring}</text>'
    anim.append(f'<g opacity="0">{vis(f)}{el}</g>'); still.append(el)
for n,p in parent.items():
    (x1,y1),(x2,y2)=P(*p),P(*n); dx,dy=(x2-x1)/sp,(y2-y1)/sp
    el=f'<line x1="{x1+dx*24}" y1="{y1+dy*24}" x2="{x2-dx*26}" y2="{y2-dy*26}" stroke="#4C8BF5" stroke-width="3.5" marker-end="url(#aB)"/>'
    f=rings[n][1]; anim.append(f'<g opacity="0">{vis(f)}{el}</g>'); still.append(el)
pathn=[(0,0),(1,0),(2,0),(2,1),(2,2)]
pd='M '+' L '.join(f'{P(*q)[0]} {P(*q)[1]}' for q in pathn)
pel=f'<path d="{pd}" fill="none" stroke="#D1182C" stroke-width="9" stroke-linejoin="round" stroke-linecap="round" opacity="0.35"/>'
anim.insert(0,f'<g opacity="0">{vis(9)}{pel}</g>'); still.insert(0,pel)
look=[None,(0,0),(1,0),(0,1),(2,0),(0,2),(2,1),(1,2),(2,2),None]
for f,n in enumerate(look):
    if n: x,y=P(*n); anim.append(f'<g opacity="0">{vis(f,f)}<circle cx="{x}" cy="{y}" r="25" fill="none" stroke="#C77C02" stroke-width="3.5"/></g>')
queues=[["(0,0)"],["(1,0)","(0,1)"],["(0,1)","(2,0)"],["(2,0)","(0,2)"],["(0,2)","(2,1)"],["(2,1)","(1,2)"],["(1,2)","(2,2)"],["(2,2)"],[],[]]
caps=[("Write 0 on the start.","It goes on the to-visit list."),
 ("Take the oldest, (0,0).","Its open neighbors get 1."),
 ("Take (1,0).","(2,0) gets 2."),("Take (0,1).","(0,2) gets 2."),
 ("Take (2,0).","(2,1) gets 3."),("Take (0,2).","(1,2) gets 3."),
 ("Take (2,1).","(2,2) gets 4."),("Take (1,2). Both neighbors","already have numbers: nothing new."),
 ("Take (2,2): the destination.","Stop."),
 ("Walk back along the arrows:","path = [(1,0), (2,0), (2,1), (2,2)]")]
X=380
b+=[f'<text class="nb" x="{X}" y="200">to-visit</text>',f'<text class="sm" x="{X}" y="276">take from the front</text>',f'<text class="sm" x="668" y="276" text-anchor="end">add to the back</text>']
b.append(f'<rect x="{X}" y="212" width="288" height="44" rx="8" fill="#F8F9FA" stroke="#DEE2E6"/>')
for f,q in enumerate(queues):
    els=[]
    for i,item in enumerate(q):
        bx=X+10+i*78
        els.append(f'<rect x="{bx}" y="220" width="70" height="28" rx="6" fill="#FFFFFF" stroke="#22527B" stroke-width="1.6"/><text class="m" x="{bx+35}" y="239" text-anchor="middle">{item}</text>')
    if not q: els.append(f'<text class="sm" x="{X+14}" y="239">empty</text>')
    anim.append(f'<g opacity="0">{vis(f,f if f<9 else None)}{"".join(els)}</g>')
for f,(l1,l2) in enumerate(caps):
    t=f'<text class="sm" x="{X}" y="74">step {f} of 9</text><text class="h" x="{X}" y="100">{l1}</text><text class="n" x="{X}" y="122">{l2}</text>' if f<9 else f'<text class="h" x="{X}" y="100">{l1}</text><text class="ms" x="{X}" y="124">{l2}</text>'
    anim.append(f'<g opacity="0">{vis(f,f if f<9 else None)}{t}</g>')
legend=[f'<circle cx="{X+8}" cy="318" r="8" fill="#D1182C"/><text class="sm" x="{X+22}" y="322">ring number</text>',
        f'<line x1="{X+120}" y1="318" x2="{X+146}" y2="318" stroke="#4C8BF5" stroke-width="3" marker-end="url(#aB)"/><text class="sm" x="{X+152}" y="322">came from</text>',
        f'<circle cx="{X+240}" cy="318" r="9" fill="none" stroke="#C77C02" stroke-width="3"/><text class="sm" x="{X+254}" y="322">looking</text>']
b+=legend
style_extra='''<style>.still{display:none} @media (prefers-reduced-motion: reduce){.anim{display:none}.still{display:inline}}</style>'''
b.append('<g class="anim">'+''.join(anim)+'</g>')
b.append('<g class="still">'+''.join(still)+f'<text class="h" x="{X}" y="100">Walk back along the arrows:</text><text class="ms" x="{X}" y="124">path = [(1,0), (2,0), (2,1), (2,2)]</text></g>')
out=svg('Breadth-first search, ring by ring',
 'An animation of breadth-first search on the 3 by 3 grid, (0, 0) at the bottom-left, with the center (1, 1) blocked, from S at (0, 0) to D at (2, 2). The start gets 0 and goes on the to-visit list. Each step takes the oldest intersection from the front of the list, and every open neighbor without a number gets the next number, an arrow showing where it came from, and a place at the back of the list: (1, 0) and (0, 1) get 1, (2, 0) and (0, 2) get 2, (2, 1) and (1, 2) get 3, and (2, 2) gets 4. When (1, 2) is taken its neighbors already have numbers, so nothing new is written. When (2, 2) is taken the search stops, and walking back along the arrows gives the path [(1, 0), (2, 0), (2, 1), (2, 2)]. The animation repeats.',b,H=340)
out=out.replace('<rect width="680"',style_extra+'\n  <rect width="680"',1)
open(OUTDIR+'bfs-ripple.svg','w').write(out)
# wall problem grid (4x4) for 5-3 first activity
b=['<text class="h" x="20" y="28">Write a rule that gets from S to D</text>']
mark={(0,0):("#142D50","#142D50"),(3,0):("#2E7D32","#2E7D32")}
g=graph(80,80,76,4,blocked=[(1,0),(1,1)],deg=False,mark=mark)
g=[e.replace('style="font-size:10.5px">0,0<','style="font-size:13px;font-weight:800;fill:#FFFFFF">S<').replace('style="font-size:10.5px">3,0<','style="font-size:13px;font-weight:800;fill:#FFFFFF">D<') for e in g]
b+=g
X=410
b+=[f'<text class="n" x="{X}" y="110">Start at S, (0, 0). The destination</text>',f'<text class="n" x="{X}" y="127">D, (3, 0), is straight across the</text>',
    f'<text class="n" x="{X}" y="144">bottom row; (1, 0) and (1, 1) are blocked.</text>',
    f'<text class="nb" x="{X}" y="184">The catch:</text>',f'<text class="n" x="{X}" y="204">your reader sees one intersection</text>',f'<text class="n" x="{X}" y="221">and its open neighbors at a time,</text>',f'<text class="n" x="{X}" y="238">never the whole grid.</text>']
open(OUTDIR+'wall-problem.svg','w').write(svg('A wall between S and D',
 'A 4 by 4 grid graph. S is the bottom-left intersection, (0, 0); D is (3, 0), straight across the bottom row. Intersections (1, 0) and (1, 1) are blocked and crossed out, with their edges removed. Your reader sees one intersection and its open neighbors at a time, never the whole grid.',b,H=340))
