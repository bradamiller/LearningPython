import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from pathanim import *
B="#22527B"
c1=["path = []","for x in range(1, 4):","    path.append((x, 0))","print(path)"]
ev1=[dict(dur=1.0,line=0,label=("Start empty","the robot is already at (0, 0)",B))]
for x in range(1,4):
    ev1+=[dict(dur=0.8,line=1,vars=f"x = {x}",label=(f"Pass {x}",f"range(1, 4) gives x = {x}",B)),
          dict(dur=1.0,line=2,vars=f"x = {x}",move=(x,0),append=(x,0),label=(f"Pass {x}",f"append ({x}, 0): the list grows by one",B))]
ev1+=[dict(dur=2.0,line=3,label=("len(path) is 3","three places to drive to: three steps","#2E7D32"))]
c2=["path = []","for x in range(1, 3):","    path.append((x, 0))","for y in range(1, 4):","    path.append((2, y))"]
ev2=[dict(dur=1.0,line=0,label=("Start empty","right two, then up three",B))]
for x in range(1,3):
    ev2+=[dict(dur=0.6,line=1,vars=f"x = {x}"),dict(dur=0.9,line=2,vars=f"x = {x}",move=(x,0),append=(x,0),label=("The go-right loop",f"append ({x}, 0)",B))]
for y in range(1,4):
    ev2+=[dict(dur=0.6,line=3,vars=f"y = {y}"),dict(dur=0.9,line=4,vars=f"y = {y}",move=(2,y),append=(2,y),label=("The go-up loop",f"append (2, {y})",B))]
ev2[-1]['hold']=0.6
ev2+=[dict(dur=2.0,label=("len(path) is 5","(0, 0) to (2, 3) in five steps","#2E7D32"))]
make(OUTDIR+'build-path.svg','Building a path in a loop',
 [dict(code=c1,start=(0,0),events=ev1),dict(code=c2,start=(0,0),events=ev2)],
 ["Start empty, append inside a loop: the","list grows by one on every pass, and","the start is never in it."],
 'An animation of a 4 by 4 grid with Python beside it. First, path = [] and a for loop over range(1, 4): on each pass x is 1, 2, then 3, a red dot steps one intersection to the right, the tuple (x, 0) is appended, and a new box joins the list, numbered 0, 1, 2. The start (0, 0) is ringed and never added. len(path) is 3. Then two loops one after the other: a go-right loop appends (1, 0) and (2, 0), and a go-up loop appends (2, 1), (2, 2) and (2, 3): the path from (0, 0) to (2, 3), five steps.',cell=39)
