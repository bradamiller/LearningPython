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
# --- 4-0 overview map: the five DELIVERY_STOPS of Lesson 4-1 ---
# Five legs share roads, so each leg is nudged a few pixels off the road's
# centre line (OFF) to keep every leg visible.
COL5=["#4C8BF5","#2E7D32","#C77C02","#8E44AD","#D1182C"]
OFF=[-8,-4,0,4,8]
g=G(110,96,sp=70,pad=30)
stops=[(2,3),(1,0),(3,1),(2,2),(0,0)]
b=g.base()
pos=(0,0)
for i,d in enumerate(stops):
    corner=(d[0],pos[1])
    pts=[pos,corner,d] if corner not in (pos,d) else [pos,d]
    o=OFF[i]
    dd='M '+' L '.join(f'{x+o} {y+o}' for x,y in (g.p(*q) for q in pts))
    b.append(f'<path d="{dd}" fill="none" stroke="{COL5[i]}" stroke-width="4.5" stroke-linejoin="round" stroke-linecap="round" opacity="0.9"/>')
    pos=d
x,y=g.p(0,0)
b.append(f'<use href="#pcXRP" transform="translate({x} {y}) rotate(0) scale(0.36)"/>')
for i,d in enumerate(stops):
    px,py=g.p(*d)
    if d==(0,0): px,py=px+24,py-24
    b.append(f'<circle cx="{px}" cy="{py}" r="12" fill="{COL5[i]}" stroke="#FFFFFF" stroke-width="2"/><text class="nb" x="{px}" y="{py+4.5}" text-anchor="middle" style="fill:#FFFFFF">{i+1}</text>')
X=400
b+=[f'<text class="h" x="{X}" y="60">Where Module 4 is headed</text>',
    f'<text class="nb" x="{X}" y="88">Five deliveries, in order:</text>']
pos=(0,0)
for i,d in enumerate(stops):
    yy=124+i*26
    b.append(f'<rect x="{X}" y="{yy-12}" width="16" height="16" rx="4" fill="{COL5[i]}"/>')
    b.append(f'<text class="n" x="{X+24}" y="{yy+1}">leg {i+1}: {pos} → {d}</text>')
    pos=d
b+=[f'<text class="nb" x="{X}" y="264">Start: home, (0, 0), facing North.</text>',
    f'<text class="n" x="{X}" y="290">For each destination the robot plans</text>',
    f'<text class="n" x="{X}" y="307">a path from where it is, drives it,</text>',
    f'<text class="n" x="{X}" y="324">and remembers where it ended up.</text>']
open(OUTDIR+'delivery-overview.svg','w').write(svg('Module 4: visit five destinations in order',
 'A 4 by 4 grid with (0, 0) at the bottom-left. The robot starts at home, (0, 0), facing north. Each leg goes across first, then up or down. Leg 1 goes to (2, 3), leg 2 to (1, 0), leg 3 to (3, 1), leg 4 to (2, 2), and leg 5 back home to (0, 0). For each destination the robot plans a path from where it is, drives it, and remembers where it ended up.',b,H=370))
# --- 4-7 project map ---
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
# --- 4-4 told, not remembered ---
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
