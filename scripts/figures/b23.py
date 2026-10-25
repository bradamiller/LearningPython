import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from bounce import *
make(OUTDIR+'bounce-run.svg','The bounce, from above',20,[180,180,180,180],
 [(0,"loop forever:"),(1,"if the left sensor sees a line:"),(2,"stop, print a message"),(2,"turn around"),(1,"else:"),(2,"drive forward")],
 {'drive':(4,5),'if':(1,1),'stop':(2,2),'turn':(3,3)},
 lambda i,a:(f"Bounce {i+1}!","stop, then turn(180)"),
 ["Every bounce is exactly 180 degrees, so","the robot goes straight back the way it","came: it paces one line forever."],
 'An animation, seen from above, of the Lesson 2-3 activity. The robot starts in the middle of a taped circle and drives forward. While its sensor reads white, about 0.2, the program takes the else branch and keeps driving. When the sensor reaches the tape the reading jumps to 0.84, the if branch runs: the robot stops and turns 180 degrees in place, then drives straight back across the circle to the far side and bounces again. A blue line traces its path, and every bounce lands on the same line, so the robot paces back and forth across one diameter. Beside it, the outline of the test highlights the line that is running.')
