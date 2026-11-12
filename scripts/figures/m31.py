import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from gridanim import *
g=G(100,100,sp=110,n=3,pad=62)
L1=[(0,"print what it is about to do"),(0,"track_to_intersection()"),(0,"print that it got there")]
L2=[(0,"track_to_intersection()"),(0,"print before the turn"),(0,"turn_clockwise()"),(0,"print after it")]
R=[dict(name="Step 1: test_first_intersection()",start=(1,0.22),heading=0,lines=L1,
        steps=[('hold',0,"Starting","on a segment, facing an intersection",0.7),
               ('track',1,"Tracking","following until both sensors see the cross"),
               ('past',1,"Driving 8.75 cm","the center onto the intersection"),
               ('hold',2,"Printing","it got there",0.6)],done=("Parked on the intersection","its center on it, sensors just past")),
   dict(name="Step 2: test_arrive_and_turn()",start=(1,0.22),heading=0,lines=L2,
        steps=[('track',0,"Tracking","following until both sensors see the cross"),
               ('past',0,"Driving 8.75 cm","the center onto the intersection"),
               ('hold',1,"Printing","about to turn",0.6),
               ('cw',2,"Turning clockwise","blind turn, then spin until a sensor finds the line"),
               ('hold',3,"Printing","the turn is done",0.6)],done=("Facing along the crossing line","a sensor on the tape")),]
make(OUTDIR+'m3-reach-and-turn.svg','Reach it, then turn, from above',g,R,
 ["One call arrives: track until the sensors","reach the intersection, then 8.75 cm more","so the center sits on it. Parked there,","the robot can pivot onto the crossing line."],
 'An animation, seen from above, of the two Lesson 3-1 tests on a 3 by 3 taped grid. In step 1 the robot starts on a segment of the middle column, facing the next intersection. It follows the line until both sensors reach the intersection, which flashes, then drives forward 8.75 cm until its center sits on it, and stops. In step 2 it does the same from the same spot, then turns clockwise in place on the intersection and stops facing along the crossing line to the right. Beside it, the steps of each test, with the one running highlighted.')
