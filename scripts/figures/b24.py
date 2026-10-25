import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math; from bounce import *
make(OUTDIR+'random-bounce-run.svg','The random bounce, from above',20,[143,112,196,221,131,168,254,207],
 [(0,"loop forever:"),(1,"if either sensor sees a line:"),(2,"stop"),(2,"pick an angle, 90 to 270"),(2,"print it, turn by it"),(1,"else:"),(2,"drive forward")],
 {'drive':(5,6),'if':(1,1),'stop':(2,3),'turn':(4,4)},
 lambda i,a:(f"Bounce {i+1}: turn {a}",f"randint(90, 270) picked {a}"),
 ["A new angle every bounce sends the robot","somewhere new each time. Watch the blue","lines fan out to cover the whole circle."],
 'An animation, seen from above, of the Lesson 2-4 activity. The robot starts in the middle of a taped circle and drives forward until its sensor reads the tape. Each time, it stops, picks a random angle between 90 and 270 degrees, prints it, and turns by that much before driving on: 143, 112, 196, 221, 131, 168, 254 and 207 degrees. A blue line traces its path, and the lines fan out across the whole circle instead of retracing one line. Beside it, the outline of the test highlights the line that is running and shows the angle each bounce picked.', either=True)
