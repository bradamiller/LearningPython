import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from floorrun import *
def tri(a):
    c=[]; tot=0
    for k in range(1,4):
        tot+=a
        c+=[('S',20,f"Side {k}","Straight 20 cm"),('T',a,f"Corner {k}: Turn {a}",f"turned {tot} degrees so far")]
    return c
make(OUTDIR+'l2-triangle-tries.svg','Two tries that do not close',
 [dict(name="Turn 90: three sides of a square",blocks=None,cmds=tri(90),done=("Not closed","turned 270 in total, not 360","#D1182C")),
  dict(name="Turn 60",blocks=None,cmds=tri(60),done=("Not closed","turned only 180 in total","#D1182C")),
],
 ["Watch the running total. To end facing","the way it started, the robot has to","turn all the way around: 360 degrees","by the last corner. What does each of","three corners need to be?"],
 'An animation, seen from above, of two tries at a triangle that do not close, each three sides of 20 cm with a different turn. With Turn 90 the robot draws three sides of a square and stops, having turned 270 degrees in total. With Turn 60 it draws a wide open zig-zag, having turned only 180 degrees. A box beside it names each side and corner and keeps a running total of the degrees turned, and a note says that a closed shape needs 360 degrees of turning in all.',
 start=(300,300),side=120.0,panel_title="What happens")
# The triangle that closes: Repeat 3 { Straight 20, Turn 120 }
make(OUTDIR+'l2-triangle-closes.svg','The triangle that closes',
 [dict(name="Repeat 3, Turn 120",
       blocks=["Wait for button press","Repeat  3 times","    Straight  cm: 20","    Turn  Deg: 120"],
       hl={0:2,1:3,2:2,3:3,4:2,5:3},
       cmds=tri(120),done=("Closed!","turned 360 in total: back at the start","#2E7D32"))],
 ["Three corners of 120 add up to 360,","one full turn, so the robot ends on","its start mark facing the way it began.","360 / 3 sides = 120 per corner."],
 'An animation, seen from above, of an XRP robot carrying a marker drawing a triangle. The program beside it is Wait for button press, then Repeat 3 times: Straight 20 cm, Turn 120 degrees, with the block that is running highlighted. The robot waits for the button, then drives a 20 cm side and turns 120 degrees in place, three times, drawing a blue triangle. A box names each side and corner and keeps a running total of the degrees turned: 120, 240, then 360. The triangle closes and the robot ends on its start mark facing the way it began.',
 start=(290,312),side=150.0,panel_title="Your program")
