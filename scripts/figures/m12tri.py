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
