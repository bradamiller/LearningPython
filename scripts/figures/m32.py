import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from gridanim import *
g=G(80,80,sp=90,n=4,pad=40)
A=lambda k,n: [('track',k,f"Arrival {n}: tracking","sensors reach the intersection"),('past',k+1,f"Arrival {n}: driving past","wheels onto it")]
L1=[(0,"track_to_intersection()"),(0,"drive_past_intersection()"),(0,"track_to_intersection()"),(0,"drive_past_intersection()"),(0,"print that it is done")]
L2=[(0,"drive_intersections(3):"),(1,"for each of count:"),(2,"track_to_intersection()"),(2,"drive_past_intersection()"),(2,"print which arrival")]
st2=[]
for i in range(3):
    st2+= [('hold',1,f"Pass {i+1} of 3","the loop body runs again",0.35),('track',2,f"Arrival {i+1} of 3","tracking to the next intersection"),('past',3,f"Arrival {i+1} of 3","driving past: wheels on it"),('hold',4,f"Arrival {i+1} of 3","printing",0.5)]
R=[dict(name="Step 1: test_two_by_hand()",start=(1,0.22),heading=0,lines=L1,
        steps=A(0,1)+A(2,2)+[('hold',4,"Printing","done",0.6)],done=("On the second intersection","the second track started past the first")),
   dict(name="Step 2: test_drive_run()",start=(1,0.22),heading=0,lines=L2,
        steps=[('hold',0,"drive_intersections(3)","count is 3",0.6)]+st2,done=("On the third intersection","three arrivals, one call"))]
make(OUTDIR+'m3-drive-run.svg','Two by hand, then the helper, from above',g,R,
 ["Each drive past leaves the sensors just","beyond the intersection, so the next","track starts on plain line and goes on","to the next one. The loop just repeats it."],
 'An animation, seen from above, of the two Lesson 3-2 tests on a 4 by 4 taped grid. In step 1 the robot starts on a segment facing the next intersection. It tracks to that intersection and drives past it so its wheels sit on it, then does the same again and stops on the second intersection. In step 2 it starts from the same spot and drive_intersections(3) repeats the pair three times, arriving at three intersections in a row and stopping on the third. Beside it, the steps of each test, with the one running highlighted.')
