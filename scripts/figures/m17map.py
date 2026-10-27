import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import math; from common import *
# Lesson 1-7, Challenge 1: the delivery course, drawn to scale from above.
K=1.35                       # px per cm
OX,OY=74,352                 # screen position of the start mark (course origin)
def P(x,y): return (OX+x*K, OY-y*K)        # course cm (x right, y up the page) -> screen
c45=math.cos(math.radians(45))
pts=[(0,0),(0,150),(100,150),(100+50*c45,150+50*c45)]
S=[P(*q) for q in pts]
RED='#D1182C'; GRAY='#6C757D'
b=['<text class="h" x="20" y="26">The delivery course</text>']
# floor panel with a faint 10 cm grid, so the map can be measured
PX0,PY0,PX1,PY1=20,40,330,398
b.append(f'<rect x="{PX0}" y="{PY0}" width="{PX1-PX0}" height="{PY1-PY0}" rx="10" fill="#F3F4F6" stroke="#DEE2E6"/>')
g=[]
for i in range(-4,18):
    x=OX+i*10*K
    if PX0+4<x<PX1-4: g.append(f'M {x:.1f} {PY0+4} V {PY1-4}')
for j in range(-3,23):
    y=OY-j*10*K
    if PY0+4<y<PY1-4: g.append(f'M {PX0+4} {y:.1f} H {PX1-4}')
b.append(f'<path d="{" ".join(g)}" stroke="#E2E5E9" stroke-width="1"/>')
# target stop zone (under the tape)
tx,ty=S[3]
b.append(f'<circle cx="{tx:.1f}" cy="{ty:.1f}" r="{30*K:.1f}" fill="#D1182C" fill-opacity="0.07" stroke="{RED}" stroke-width="1.8" stroke-dasharray="6 4"/>')
# the tape
d='M '+' L '.join(f'{x:.1f} {y:.1f}' for x,y in S)
b.append(f'<path d="{d}" fill="none" stroke="#2B2B2B" stroke-width="7" stroke-linejoin="round" stroke-linecap="butt"/>')
# start bar across the tape
sx,sy=S[0]
b.append(f'<line x1="{sx-16}" y1="{sy}" x2="{sx+16}" y2="{sy}" stroke="#2B2B2B" stroke-width="5"/>')
b.append(f'<text class="nb" x="{sx}" y="{sy+24}" text-anchor="middle">START</text>')
# target bullseye
b.append(f'<circle cx="{tx:.1f}" cy="{ty:.1f}" r="9" fill="#FFFFFF" stroke="{RED}" stroke-width="3"/><circle cx="{tx:.1f}" cy="{ty:.1f}" r="3.5" fill="{RED}"/>')
b.append(f'<text class="nb" x="{tx:.1f}" y="{ty-30*K-8:.1f}" text-anchor="middle" style="fill:{RED}">TARGET</text>')
# leg lengths
def dim(a,bb,off,label,anchor='middle',dx=0,dy=0):
    (x1,y1),(x2,y2)=a,bb; L=math.hypot(x2-x1,y2-y1); nx,ny=-(y2-y1)/L*off,(x2-x1)/L*off
    o=f'<line x1="{x1+nx:.1f}" y1="{y1+ny:.1f}" x2="{x2+nx:.1f}" y2="{y2+ny:.1f}" stroke="{GRAY}" stroke-width="1.4" marker-start="url(#aG)" marker-end="url(#aG)"/>'
    mx,my=(x1+x2)/2+nx,(y1+y2)/2+ny
    return o+tag(mx+dx,my+dy,label,stroke=GRAY)
b.append(dim(S[0],S[1],-18,'150 cm'))
b.append(dim(S[1],S[2],18,'100 cm'))
b.append(dim(S[2],S[3],-14,'50 cm',dx=-26,dy=-14))
# turns: dashed line straight on, arc from straight-on to the new leg
def turn(c,h_in,h_out,label,lx,ly,rc=18):
    cx,cy=c; o=[]
    ex,ey=cx+28*K*math.sin(math.radians(h_in)),cy-28*K*math.cos(math.radians(h_in))
    o.append(f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="#ADB5BD" stroke-width="2" stroke-dasharray="4 4"/>')
    r=rc*K; a0,a1=math.radians(h_in),math.radians(h_out)
    x0,y0=cx+r*math.sin(a0),cy-r*math.cos(a0); x1,y1=cx+r*math.sin(a1),cy-r*math.cos(a1)
    sweep=1 if h_out>h_in else 0
    o.append(f'<path d="M {x0:.1f} {y0:.1f} A {r:.1f} {r:.1f} 0 0 {sweep} {x1:.1f} {y1:.1f}" fill="none" stroke="{RED}" stroke-width="2.2" marker-end="url(#aR)"/>')
    o.append(tag(lx,ly,label,stroke=RED))
    return ''.join(o)
b.append(turn(S[1],0,90,'right 90°',S[1][0]-8,S[1][1]-46))
b.append(turn(S[2],90,45,'left 45°',S[2][0]+62,S[2][1]+28,rc=15))
# the robot on its start mark, facing up the first leg (center of rotation on the mark)
b.append(f'<use href="#pcXRP" transform="translate({sx} {sy}) scale(0.2)"/>')
# scale bar
b.append(f'<line x1="{PX1-20-50*K:.1f}" y1="{PY1-16}" x2="{PX1-20}" y2="{PY1-16}" stroke="{GRAY}" stroke-width="2"/>'
         f'<path d="M {PX1-20-50*K:.1f} {PY1-21} v 10 M {PX1-20} {PY1-21} v 10" stroke="{GRAY}" stroke-width="2"/>'
         f'<text class="sm" x="{PX1-20-25*K:.1f}" y="{PY1-25}" text-anchor="middle">50 cm</text>')
# key
X=356
b.append(f'<text class="h" x="{X}" y="60">Reading the map</text>')
y=86
def key(sym,lines):
    global y
    o=[sym(X+14,y)]
    for i,l in enumerate(lines): o.append(f'<text class="n" x="{X+38}" y="{y+4+i*17}">{l}</text>')
    y+=17*len(lines)+20; return ''.join(o)
b.append(key(lambda x,yy:f'<line x1="{x-12}" y1="{yy}" x2="{x+12}" y2="{yy}" stroke="#2B2B2B" stroke-width="7"/>',
             ['Tape on the floor: the route.']))
b.append(key(lambda x,yy:f'<use href="#pcXRP" transform="translate({x} {yy+6}) scale(0.16)"/>',
             ['Start with the center of rotation','on the mark, facing up the first leg.']))
b.append(key(lambda x,yy:f'<path d="M {x-11} {yy+4} A 14 14 0 0 1 {x+9} {yy-6}" fill="none" stroke="{RED}" stroke-width="2.2" marker-end="url(#aR)"/>',
             ['A turn is measured from the way','the robot is already facing','(the dashed line).']))
b.append(key(lambda x,yy:f'<circle cx="{x}" cy="{yy}" r="12" fill="#D1182C" fill-opacity="0.07" stroke="{RED}" stroke-width="1.8" stroke-dasharray="5 3"/><circle cx="{x}" cy="{yy}" r="3" fill="{RED}"/>',
             ['Stop zone: finish within 30 cm','of the target, then signal.']))
b.append(f'<text class="sm" x="{X}" y="{y+6}">Drawn to scale. Each faint square is 10 cm.</text>')
out=svg('The delivery course',
 'A to-scale map, seen from above, of a route taped on the floor. From the start mark, where an XRP sits facing up the page, the tape runs 150 cm straight ahead, turns right 90 degrees, runs 100 cm, turns left 45 degrees, and runs 50 cm to a red target. A dashed red circle 30 cm around the target marks the stop zone. Each turn is drawn as a red arc from a dashed line that continues the way the robot was facing. Beside the map, a key explains the tape, the start, how turns are measured, and the stop zone.',b,H=410)
open(OUTDIR+'course-map.svg','w').write(out); print('ok')
