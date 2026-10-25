import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from common import *
COL=["#4C8BF5","#2E7D32","#C77C02","#8E44AD"]
def legs_map(g,stops,start=(0,0),robot_h=0,heads=True,steps=True):
    b=g.base()
    pos=start; segs=[]
    for i,d in enumerate(stops):
        corner=(d[0],pos[1])
        pts=[pos,corner,d] if corner not in (pos,d) else [pos,d]
        b.append(g.route(pts,COL[i]).replace('stroke-width="9"','stroke-width="7"'))
        segs.append((pos,d)); pos=d
    x,y=g.p(*start)
    b.append(f'<use href="#pcXRP" transform="translate({x} {y}) rotate({robot_h*90}) scale(0.36)"/>')
    for i,d in enumerate(stops):
        if d==start: continue
        px,py=g.p(*d)
        b.append(f'<circle cx="{px}" cy="{py}" r="12" fill="{COL[i]}" stroke="#FFFFFF" stroke-width="2"/><text class="nb" x="{px}" y="{py+4.5}" text-anchor="middle" style="fill:#FFFFFF">{i+1}</text>')
    return b
def legend(X,Y,stops,start=(0,0),extra=None):
    b=[]; pos=start
    for i,d in enumerate(stops):
        n=abs(d[0]-pos[0])+abs(d[1]-pos[1])
        y=Y+i*26
        b.append(f'<rect x="{X}" y="{y-12}" width="16" height="16" rx="4" fill="{COL[i]}"/>')
        b.append(f'<text class="n" x="{X+24}" y="{y+1}">leg {i+1}: {pos} → {d}' + (f'  <tspan class="sm">{n} steps</tspan>' if extra=='steps' else '') + '</text>')
        pos=d
    return b
# --- 4-0 overview map ---
g=G(110,96,sp=60,pad=30)
stops=[(2,0),(2,3),(0,3)]
b=legs_map(g,stops)
X=380
b+=[f'<text class="h" x="{X}" y="60">Where Module 4 is headed</text>',
    f'<text class="ms" x="{X}" y="88">destinations = [(2, 0), (2, 3), (0, 3)]</text>']
b+=legend(X,124,stops)
b+=[f'<text class="nb" x="{X}" y="210">Start: home, (0, 0), facing North.</text>',f'<text class="n" x="{X}" y="236">For each destination the robot plans</text>',
    f'<text class="n" x="{X}" y="253">a path from where it is, drives it,</text>',
    f'<text class="n" x="{X}" y="270">and remembers where it ended up.</text>',
    f'<text class="n" x="{X}" y="287">No remote control, no steering.</text>']
open(OUTDIR+'delivery-overview.svg','w').write(svg('Module 4: visit three destinations in order',
 'A 4 by 4 grid with (0, 0) at the bottom-left. The robot starts at home, (0, 0), facing north. Leg 1 goes right to destination 1 at (2, 0); leg 2 goes up to destination 2 at (2, 3); leg 3 goes left to destination 3 at (0, 3). Beside it: destinations = [(2, 0), (2, 3), (0, 3)]. For each destination the robot plans a path from where it is, drives it, and remembers where it ended up.',b,H=350))
# --- 4-9 project map ---
g=G(110,96,sp=60,pad=30)
stops=[(2,0),(2,3),(0,3),(0,0)]
b=legs_map(g,stops)
arr={0:(2,0,90),1:(2,3,0),2:(0,3,270),3:(0,0,180)}
for i,(r,c,h) in arr.items():
    px,py=g.p(r,c); import math
    a=math.radians(h); dx,dy=math.sin(a),-math.cos(a)
    ox,oy={0:(26,26),1:(26,-26),2:(-26,-26),3:(-26,26)}[i]
    cx,cy=px+ox,py+oy
    b.append(f'<circle cx="{cx}" cy="{cy}" r="11" fill="#FFFFFF" stroke="{COL[i]}" stroke-width="1.6"/><line x1="{cx-dx*6}" y1="{cy-dy*6}" x2="{cx+dx*6}" y2="{cy+dy*6}" stroke="{COL[i]}" stroke-width="2.4" marker-end="url(#aB)"/>')
X=380
b+=[f'<text class="h" x="{X}" y="52">The delivery run</text>',
    f'<text class="ms" x="{X}" y="78">DESTINATIONS = [(2, 0), (2, 3),</text>',
    f'<text class="ms" x="{X+120}" y="94">(0, 3), (0, 0)]</text>']
b+=legend(X,128,stops,extra='steps')
b+=[f'<text class="n" x="{X}" y="246">The small arrows are the heading each</text>',
    f'<text class="n" x="{X}" y="263">leg ends with. It is not reset: leg 2</text>',
    f'<text class="n" x="{X}" y="280">starts facing East because leg 1 ended</text>',
    f'<text class="n" x="{X}" y="297">that way, and turn_to() works from there.</text>']
open(OUTDIR+'delivery-run.svg','w').write(svg('The delivery run: four legs, heading carried over',
 'A 4 by 4 grid with (0, 0) at the bottom-left. The robot starts at home, (0, 0), facing north. Leg 1 goes right 2 steps to (2, 0), ending facing east. Leg 2 goes up 3 steps to (2, 3), ending facing north. Leg 3 goes left 2 steps to (0, 3), ending facing west. Leg 4 goes down 3 steps back home to (0, 0), ending facing south. The heading is not reset between legs: each leg starts facing the way the last one ended.',b,H=350))
# --- 4-5 told, not remembered ---
g=G(110,96,sp=60,pad=30)
stops=[(2,3),(0,3),(0,0)]
b=legs_map(g,stops)
X=372
b+=[f'<text class="h" x="{X}" y="52">The planner is told, every time</text>']
calls=[("(0, 0)","(2, 3)"),("(2, 3)","(0, 3)"),("(0, 3)","(0, 0)")]
for i,(p,d) in enumerate(calls):
    y=86+i*40
    b.append(f'<rect x="{X}" y="{y-16}" width="296" height="28" rx="6" fill="#F8F9FA" stroke="{COL[i]}" stroke-width="1.6"/>')
    b.append(f'<text class="ms" x="{X+8}" y="{y+3}">compute_manhattan_path(<tspan font-weight="800" fill="{COL[i]}">{p}</tspan>, {d})</text>')
b+=[f'<text class="n" x="{X}" y="226">Each call is handed where the robot is</text>',
    f'<text class="n" x="{X}" y="243">now. The planner keeps nothing between</text>',
    f'<text class="n" x="{X}" y="260">calls; only the driving code tracks</text>',
    f'<text class="n" x="{X}" y="277">position, and it passes the value in.</text>']
open(OUTDIR+'told-not-remembered.svg','w').write(svg('The planner is told where the robot is',
 'A 4 by 4 grid with (0, 0) at the bottom-left and three legs: (0, 0) to (2, 3), then (2, 3) to (0, 3), then (0, 3) back to (0, 0). Beside it the three planner calls, compute_manhattan_path((0, 0), (2, 3)), compute_manhattan_path((2, 3), (0, 3)) and compute_manhattan_path((0, 3), (0, 0)), with the first argument of each, the robot\'s current position, highlighted in its leg\'s color. Each call is handed where the robot is now; the planner keeps nothing between calls.',b,H=350))
