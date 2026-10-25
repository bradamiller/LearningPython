import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from gridanim import *
import gridanim; gridanim.SPEED=160.0; gridanim.PAUSE=0.6
g=G(100,100,sp=110,n=3,pad=62)
def side(k):
    return [('track',1,f"Side {k}","arrival 1 of SIDE = 2"),('past',1,f"Side {k}","wheels on it"),
            ('track',1,f"Side {k}","arrival 2 of SIDE = 2"),('past',1,f"Side {k}","wheels on the corner"),
            ('cw',2,f"Side {k}: corner","turn_clockwise()")]
def run(name,n,lines,done):
    st=[]
    for k in range(1,n+1): st+=([('hold',0,f"Pass {k}","",0.3)] if n>1 else [])+side(k)
    return dict(name=name,start=(0,0),heading=0,lines=lines,steps=st,done=done)
R=[run("1. test_one_side()",1,[(0,"one side:"),(1,"drive_intersections(SIDE)"),(1,"turn_clockwise()")],("One side done","on the corner, facing the next side")),
   run("2. test_square(), range(2)",2,[(0,"2 times:"),(1,"drive_intersections(SIDE)"),(1,"turn_clockwise()")],("Two sides","an L, facing the third side")),
   run("3. test_square(), range(4)",4,[(0,"4 times:"),(1,"drive_intersections(SIDE)"),(1,"turn_clockwise()")],("Closed!","back on the start corner, facing away"))]
make(OUTDIR+'m3-square-buildup.svg','One side, two, then four',g,R,
 ["Each pass of the loop draws one side and","turns the corner, so changing the number","in range() changes how much of the","square you get."],
 'An animation, seen from above, of the Lesson 3-4 build-up on a 3 by 3 taped grid, the robot starting parked on the bottom-left corner facing away from you. First test_one_side(): it arrives at two intersections up the left side and turns right on the top-left corner. Then test_square() with range(2): two sides, ending on the top-right corner facing down the right side. Then range(4): all four sides, ending back on the start corner facing the way it began. Beside it, the loop for each run, with the line running highlighted.')
