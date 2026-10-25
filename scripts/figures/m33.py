import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from gridanim import *
g=G(80,80,sp=90,n=4,pad=40)
def leg(li,n,name):
    s=[]
    for i in range(n): s+=[('track',li,name,f"arrival {i+1} of {n}: tracking"),('past',li,name,f"arrival {i+1} of {n}: driving past")]
    return s
R=[dict(name="Step 1: test_l_shape()",start=(1,0.22),heading=0,
        lines=[(0,"leg 1: 2 intersections"),(0,"corner: turn right"),(0,"leg 2: 2 intersections")],
        steps=leg(0,2,"Leg 1")+[('cw',1,"Corner","turn_clockwise() on the intersection")]+leg(2,2,"Leg 2"),
        done=("L complete","parked on the fourth intersection")),
   dict(name="Step 2: a plan of your own",start=(2,0.22),heading=0,
        lines=[(0,"leg 1: 3 intersections"),(0,"corner: turn left"),(0,"leg 2: 1 intersection")],
        steps=leg(0,3,"Leg 1")+[('ccw',1,"Corner","turn_counterclockwise()")]+leg(2,1,"Leg 2"),
        done=("Ended where the plan says","one line of code per leg or corner"))]
make(OUTDIR+'m3-l-and-plan.svg','The L, then a plan, from above',g,R,
 ["A plan reads like directions, and each","line of it becomes one line of code:","drive_intersections() for a leg, a turn","for a corner."],
 'An animation, seen from above, of the Lesson 3-3 activity on a 4 by 4 taped grid. In step 1 the robot starts on a segment facing away from you, arrives at two intersections, turns right on the second, and arrives at two more along the crossing line, ending parked on the fourth. In step 2 it follows an example plan from a different start: three intersections, a left turn, one intersection. Beside it, the plan for each run, with the leg or corner being driven highlighted.')
