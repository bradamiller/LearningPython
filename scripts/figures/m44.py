import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from pathanim import *
B="#22527B"; R="#D1182C"; GR="#2E7D32"; GY="#6C757D"
code=["path = [], unpack start and end","east:  while x < end_x: x + 1","west:  while x > end_x: x - 1","north: while y < end_y: y + 1","south: while y > end_y: y - 1","return path"]
def trip(s,e):
    x,y=s; ex,ey=e; ev=[dict(dur=1.2,line=0,vars=f"x, y = {x}, {y}    end = ({ex}, {ey})",label=(f"({x}, {y}) to ({ex}, {ey})","path = [ ]",B))]
    for li,(nm,cmp,dx,dy) in enumerate([("East","<",1,0),("West",">",-1,0),("North","<",0,1),("South",">",0,-1)],start=1):
        v,ev_ = (x,ex) if dx else (y,ey)
        ok = v<ev_ if cmp=="<" else v>ev_
        if not ok:
            ev.append(dict(dur=1.3,line=li,vars=f"x, y = {x}, {y}",label=(f"{nm}: skipped",f"{'x' if dx else 'y'} {cmp} {ev_} is {v} {cmp} {ev_}: False at the first check",GY)))
            continue
        while (x<ex if (dx==1) else x>ex if dx==-1 else y<ey if dy==1 else y>ey):
            x+=dx; y+=dy
            ev.append(dict(dur=0.9,line=li,vars=f"x, y = {x}, {y}",move=(x,y),append=(x,y),label=(f"{nm} runs",f"step to ({x}, {y}) and append it",R)))
        ev.append(dict(dur=0.7,line=li,vars=f"x, y = {x}, {y}",label=(f"{nm} stops",f"{'x' if dx else 'y'} now matches the end",B)))
    n=len([e_ for e_ in ev if e_.get('append')])
    ev.append(dict(dur=2.2,line=5,vars=f"x, y = {x}, {y}",label=(f"return: {n} steps" if n else "return: [ ]",f"|{ex}-{s[0]}| + |{ey}-{s[1]}| = {n}" if n else "already there: zero steps",GR)))
    return dict(code=code,start=s,events=ev)
make(OUTDIR+'four-loops-run.svg','The four loops, one trip at a time',
 [trip((0,0),(2,3)),trip((3,3),(1,0)),trip((1,1),(1,1))],
 ["At most one x loop and one y loop run;","the others find their condition False on","the first check and do nothing."],
 'An animation of compute_path() on a 4 by 4 grid, with the four loops listed beside it. Trip one, (0, 0) to (2, 3): east runs twice, appending (1, 0) and (2, 0); west is skipped; north runs three times, appending (2, 1), (2, 2) and (2, 3); south is skipped; five steps. Trip two, (3, 3) to (1, 0): east is skipped; west runs twice, (2, 3) and (1, 3); north is skipped; south runs three times, (1, 2), (1, 1), (1, 0); five steps. Trip three, (1, 1) to (1, 1): all four loops are skipped and the path is empty. A red dot steps along each move and each appended spot is numbered by its index.',cell=39)
