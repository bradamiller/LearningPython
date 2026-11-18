"""Lesson 4-4 and 4-5 step-through animations of Leg 1 of the delivery run,
(0, 0) to (2, 3), path [(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)], starting
facing North.
  drive-path-steps.svg: what drive_path() does at each intersection
      (heading, turn to face it, drive). The turn is drawn the short way;
      turn_to() is still a stub in 4-4.
  turn-to-steps.svg: the real turn_to(), one clockwise quarter turn per
      stop (1, 0, 3, 0, 0 turns).
Both are StepFigures (Back / Step / Play)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR
import gridanim; from gridanim import G, make
gridanim.SPEED=130.0; gridanim.PAUSE=0.7
g=G(80,80,sp=90,n=4,pad=40)
PATH=[(1,0),(2,0),(2,1),(2,2),(2,3)]
L=["N","E","S","W"]; NAME=["North","East","South","West"]
def dh(p,q): return {(0,1):0,(1,0):1,(0,-1):2,(-1,0):3}[(q[0]-p[0],q[1]-p[1])]

def extra(vis,P,marks,T):
    x,y=P(2,3)
    return [f'<circle cx="{x}" cy="{y}" r="22" fill="none" stroke="#2E7D32" stroke-width="3" stroke-dasharray="5 4"/>',
            f'<text class="sm" x="{x-14}" y="{y-30}" style="font-weight:700">(2, 3)</text>']

# ---- 4-4: drive_path() ----
pos=(0,0); hd=0; st=[]
for k,q in enumerate(PATH):
    want=dh(pos,q)
    st.append(('pause',1,f"Pass {k+1}: next_pos is {q}",f"desired_heading is {want}, {L[want]}",0.9))
    if want==hd:
        st.append(('hold',2,f"Pass {k+1}: turn_to()",f"already facing {NAME[hd]}: no turn",0.9))
    else:
        op='cw' if (hd+1)%4==want else 'ccw'
        st.append((op,2,f"Pass {k+1}: turn_to()",f"{NAME[hd]} to {NAME[want]}: now facing {L[want]}"))
        hd=want
    st.append(('track',3,f"Pass {k+1}: drive",f"track to the intersection at {q}"))
    st.append(('past',3,f"Pass {k+1}: drive",f"at {q}"))
    st.append(('pause',4,f"Pass {k+1}: current_position",f"is now {q}",0.6))
    pos=q
lines=[(0,"for next_pos in path:"),(1,"get_desired_heading(...)"),(1,"current_heading = turn_to(...)"),
       (1,"fake_track_to_intersection()"),(1,"current_position = next_pos"),(0,"return the pose")]
R=[dict(name="drive_path(path, (0, 0), 0)",start=(0,0),heading=0,lines=lines,steps=st,
        done=("return (2, 3), 0","the new pose: at (2, 3), facing North"))]
make(OUTDIR+'drive-path-steps.svg','drive_path() on Leg 1',g,R,
 ["One pass of the loop per intersection:","work out the heading, turn to face it,","drive there. Then the next pass starts","from there."],
 'A step-through animation of drive_path() on Leg 1 of the delivery run, seen from above on a 4 by 4 grid. The robot starts at (0, 0) facing North; the destination (2, 3) is ringed. Beside it, the drive_path() loop with the running line highlighted and a box naming the pass. Pass 1: next_pos is (1, 0), desired heading 1, East; the robot turns right to face East and drives to (1, 0). Pass 2: (2, 0), East again: no turn, drive. Pass 3: (2, 1), North: the robot turns left to face North and drives. Passes 4 and 5: (2, 2) and (2, 3), North: no turn, drive. drive_path() returns (2, 3) and heading 0.',
 panel_title="What drive_path() does",extra=extra,step_ops=('hold','cw','ccw','past'))

# ---- 4-5: turn_to() ----
pos=(0,0); hd=0; st=[]
for k,q in enumerate(PATH):
    want=dh(pos,q)
    if want==hd:
        st.append(('hold',0,f"turn_to({L[hd]}, {L[want]})",f"already facing {NAME[want]}: 0 turns",1.0))
    n=0
    while hd!=want:
        n+=1
        st.append(('pause',0,f"turn_to({L[(hd-n+1)%4] if False else L[hd]}, {L[want]})",f"{hd} is not {want}: keep turning",0.5))
        st.append(('cw',2,f"Turn {n}: ({hd} + 1) % 4",f"heading is now {(hd+1)%4}, {NAME[(hd+1)%4]}"))
        hd=(hd+1)%4
    st.append(('track',None,f"Drive to {q}",f"facing {NAME[hd]}"))
    st.append(('past',None,f"Drive to {q}",f"facing {NAME[hd]}"))
    pos=q
lines=[(0,"while current_heading !="),(2,"desired_heading:"),(1,"fake_turn_clockwise()"),
       (1,"current_heading ="),(2,"(current_heading + 1) % 4"),(0,"return current_heading")]
R=[dict(name="turn_to() on Leg 1",start=(0,0),heading=0,lines=lines,steps=st,
        done=("Leg 1 done","1, 0, 3, 0 and 0 turns: four in all"))]
make(OUTDIR+'turn-to-steps.svg','turn_to() on Leg 1',g,R,
 ["Each clockwise quarter turn adds 1,","and % 4 wraps 3 back to 0. East to","North takes three turns: East, South,","West, North."],
 'A step-through animation of the real turn_to() on Leg 1 of the delivery run, seen from above on a 4 by 4 grid. The robot starts at (0, 0) facing North. To face East it makes one clockwise quarter turn, heading 0 to 1, and drives to (1, 0). Already facing East, it makes no turn and drives to (2, 0). To face North it makes three clockwise quarter turns, East to South, South to West, West to North, heading 1 to 2, 2 to 3, and 3 wraps to 0, then drives to (2, 1). Already facing North, it drives to (2, 2) and (2, 3) with no turns. Beside it, the turn_to() loop with the running line highlighted and a box showing the heading after each turn.',
 panel_title="What turn_to() does",extra=extra,step_ops=('hold','cw','past'))
