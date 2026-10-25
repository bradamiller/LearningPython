import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from gridanim import *
import gridanim; gridanim.SPEED=130.0; gridanim.PAUSE=0.7
g=G(80,80,sp=90,n=4,pad=40)
DEST=[(2,0),(2,3),(0,3),(0,0)]
NAMES=["North","East","South","West"]
def manhattan(p,d):
    x,y=p; path=[]
    while x<d[0]: x+=1; path.append((x,y))
    while x>d[0]: x-=1; path.append((x,y))
    while y<d[1]: y+=1; path.append((x,y))
    while y>d[1]: y-=1; path.append((x,y))
    return path
def dh(p,q):
    dx,dy=q[0]-p[0],q[1]-p[1]
    return {(0,1):0,(1,0):1,(0,-1):2,(-1,0):3}[(dx,dy)]
pos=(0,0); hd=0; steps=[]; paths=[]
for li,d in enumerate(DEST):
    path=manhattan(pos,d); paths.append(path)
    steps.append(('mark',None,f"leg{li}"))
    steps.append(('hold',1,f"Leg {li+1}: plan to {d}",f"{len(path)} steps: across first, then up or down",1.3))
    steps.append(('hold',2,f"Leg {li+1}: plan to {d}","printed, then driven",0.5))
    for k,q in enumerate(path):
        want=dh(pos,q); n=0
        while hd!=want:
            n+=1
            steps.append(('cw',3,f"Leg {li+1}: turn_to({NAMES[want]})",f"right turn {n}, facing {NAMES[(hd+1)%4]}"))
            hd=(hd+1)%4
        steps.append(('track',3,f"Leg {li+1}: to {q}",f"step {k+1} of {len(path)}, facing {NAMES[hd]}"))
        steps.append(('past',3,f"Leg {li+1}: to {q}",f"step {k+1} of {len(path)}, facing {NAMES[hd]}"))
        pos=q
    steps.append(('hold',4,f"Arrived at {d}",f"facing {NAMES[hd]}; heading carries over",1.2))
lines=[(0,"for each destination:"),(1,"plan the path from here"),(1,"print the path"),(1,"drive it; keep where it ends"),(1,"print where it arrived")]
R=[dict(name="test_delivery()",start=(0,0),heading=0,lines=lines,steps=steps,done=("Delivery complete","home at (0, 0), facing South"))]
COL=["#D1182C","#E8890C","#2E7D32","#7B4FA0"]
def extra(vis,P,marks,T):
    out=[]
    for i,d in enumerate(DEST):
        x,y=P(*d)
        t0=marks[f"leg{i}"]
        # destination flag, always shown; ringed while it's the current target
        out.append(f'<g><circle cx="{x+20}" cy="{y-20}" r="11" fill="#FFFFFF" stroke="{COL[i]}" stroke-width="2.2"/><text class="ms" x="{x+20}" y="{y-16}" text-anchor="middle" style="fill:{COL[i]};font-weight:700">{i+1}</text></g>')
        t1=marks.get(f"leg{i+1}",T-2.2)
        out.append(f'<g opacity="0">{vis(t0,t1)}<circle cx="{x}" cy="{y}" r="22" fill="none" stroke="{COL[i]}" stroke-width="3" stroke-dasharray="5 4"/></g>')
        # planned path preview, dotted, from plan until leg ends
        pts=[P(*(DEST[i-1] if i else (0,0)))]+[P(*q) for q in paths[i]]
        if len(pts)>1:
            dd=' '.join(f'{a:.0f},{b:.0f}' for a,b in pts)
            out.append(f'<g opacity="0">{vis(t0+0.3,t1)}<polyline points="{dd}" fill="none" stroke="{COL[i]}" stroke-width="3" stroke-dasharray="3 6" stroke-linecap="round"/></g>')
    x,y=P(0,0)
    out.append(f'<text class="sm" x="{x-38}" y="{y+34}" style="font-weight:700">home</text>')
    return out
make(OUTDIR+'delivery-drive.svg','The delivery run, from above',g,R,
 ["Each leg is planned from wherever the last","one ended. turn_to() only turns clockwise,","so facing East and wanting North takes","three right turns. That is expected."],
 'An animation, seen from above, of the Lesson 4-9 delivery run on a 4 by 4 grid. The robot starts at home, (0, 0), facing North. The four destinations are numbered 1 to 4: (2, 0), (2, 3), (0, 3) and back to (0, 0). For each leg the planned Manhattan path appears as a dotted line from where the robot is, then the robot drives it: before each step it turns clockwise, one sensor-ended right turn at a time, until it faces the next intersection, then tracks to it and drives past. Leg 1 is one right turn and two steps east. Leg 2 needs three right turns to face North, then three steps up. Leg 3, three right turns to face West, two steps left. Leg 4, three right turns to face South, three steps down to home. Beside it, the main loop with the running line highlighted and a box naming the leg, the step and the heading.',
 panel_title="What test_delivery() does",extra=extra)
