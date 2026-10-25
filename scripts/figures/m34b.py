import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from gridanim import *
import gridanim; gridanim.SPEED=160.0; gridanim.PAUSE=0.6
g=G(80,80,sp=90,n=4,pad=40)
def shape(name,start,lens,turn,lines,done):
    st=[]
    for k,n in enumerate(lens):
        for i in range(n): st+=[('track',1,f"Side {k+1}",f"length {n}, arrival {i+1}"),('past',1,f"Side {k+1}",f"length {n}, arrival {i+1}")]
        st+=[(turn,2,f"Side {k+1}: corner","turn_clockwise()" if turn=='cw' else "turn_counterclockwise()")]
    return dict(name=name,start=start,heading=0,lines=lines,steps=st,done=done)
R=[shape("Bigger: SIDE = 3",(0,0),[3,3,3,3],'cw',[(0,"4 times:"),(1,"drive_intersections(SIDE)"),(1,"turn_clockwise()")],("Closed","a 3-per-side square")),
   shape("Rectangle: [2, 3, 2, 3]",(0,0),[2,3,2,3],'cw',[(0,"for each of 4 sides:"),(1,"drive that side's length"),(1,"turn_clockwise()")],("Closed","opposite sides match")),
   shape("Mirror: left turns",(3,0),[2,2,2,2],'ccw',[(0,"4 times:"),(1,"drive_intersections(SIDE)"),(1,"turn_counterclockwise()")],("Closed","the same square, the other way round"))]
make(OUTDIR+'m3-extensions.svg','Three extensions, from above',g,R,
 ["Each variation changes one thing: the","value of SIDE, a list of side lengths,","or which way the robot turns."],
 'An animation, seen from above, of the three Lesson 3-4 extensions on a 4 by 4 taped grid. First a bigger square with SIDE = 3, from the bottom-left corner. Then a rectangle with sides of 2, 3, 2 and 3 intersections. Then a square driven with left turns, starting from the bottom-right corner and going round counterclockwise. Each one ends back on its start corner facing the way it began. Beside it, the loop for each run, with the line running highlighted.')
