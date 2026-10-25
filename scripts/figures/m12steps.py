import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from floorrun import *
make(OUTDIR+'l2-step1.svg','Step 1: drive straight',
 [dict(name="Step 1",blocks=["Wait for button press","Straight  cm: 20"],cmds=[('S',20,"Straight","driving 20 cm forward")],done=("Done","20 cm ahead, facing the same way","#2E7D32"))],
 ["Straight drives the distance and then","stops by itself, so the program ends","with the robot still facing forward."],
 'An animation, seen from above, of the step 1 program: Wait for button press, then Straight 20 cm. The robot waits, then drives forward 20 cm, drawing a short blue line from its start mark, and stops facing the same way it started. Beside it, the two blocks, with the one running highlighted.')
make(OUTDIR+'l2-step2.svg','Step 2: add a turn',
 [dict(name="Step 2",blocks=["Wait for button press","Straight  cm: 20","Turn  Deg: 90"],cmds=[('S',20,"Straight","driving 20 cm forward"),('T',90,"Turn","a quarter turn, in place")],done=("Done","20 cm ahead, turned a quarter","#2E7D32"))],
 ["One side and one corner: an L.","Every shape you draw today is built","from this pair."],
 'An animation, seen from above, of the step 2 program: Wait for button press, Straight 20 cm, Turn 90 degrees. The robot drives forward 20 cm, drawing a blue line, then turns a quarter turn in place without moving, ending 20 cm from its start mark and facing a quarter turn away from where it started. Beside it, the three blocks, with the one running highlighted.')
side=lambda k:[('S',20,f"Side {k}","Straight 20 cm"),('T',90,f"Corner {k}","Turn 90 degrees")]
make(OUTDIR+'l2-step3.svg','Step 3: make a square',
 [dict(name="A first try: three sides",blocks=None,cmds=side(1)+side(2)+side(3),done=("Not closed","one side short: count again","#D1182C")),
  dict(name="Fixed: four sides",blocks=None,cmds=side(1)+side(2)+side(3)+side(4),done=("Closed!","back at the start, facing the same way","#2E7D32"))],
 ["A wrong shape is information: it tells","you what to change. Here, one more side","and one more corner close the square."],
 'An animation, seen from above, of two attempts at step 3. In the first, the robot drives a side and turns a corner three times, drawing an open box that stops one side short of its start mark. In the second, it does it four times, drawing a closed square, and ends on its start mark facing the way it began. Beside it, a box names each side and corner as it happens and says whether the shape closed.',panel_title="What happens")
