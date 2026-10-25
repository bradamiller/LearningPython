import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
# Lesson 1-10: the nested-loop program, first two squares only (the activity is left to the student).
import math; from common import *
S=0.5; PX=6.0                     # px per cm
SX0,SY0=318,338
COLORS=["#1F6FEB","#7B4FA0"]
x,y,h=SX0,SY0,0.0; t=0.0
frames=[(0.0,x,y,h)]; trails=[]; hls=[]; vars_=[]; labels=[]
t=1.0; frames.append((t,x,y,h)); labels.append((0,t,"Waiting for the button","board.wait_for_button()","#6C757D"))
for sq in range(2):
    size=20+sq*5
    t0=t; t+=0.5; frames.append((t,x,y,h)); hls.append((t0,t,0)); vars_.append((t0,t,sq,None,None))
    t0=t; t+=0.6; frames.append((t,x,y,h)); hls.append((t0,t,1)); vars_.append((t0,t,sq,size,None))
    pts=[(x,y)]; tl=[(t,0.0)]; L=0.0; tstart=t
    for side in range(4):
        t0=t; t+=0.3; frames.append((t,x,y,h)); tl.append((t,L)); hls.append((t0,t,2)); vars_.append((t0,t,sq,size,side))
        t0=t; d=size*PX; ux,uy=math.sin(math.radians(h)),-math.cos(math.radians(h)); n=12; dur=1.0*size/20
        for i in range(1,n+1):
            t+=dur/n; x+=ux*d/n; y+=uy*d/n; L+=d/n; frames.append((t,x,y,h)); tl.append((t,L))
        pts.append((x,y)); hls.append((t0,t,3)); vars_.append((t0,t,sq,size,side))
        t0=t; n=8
        for i in range(1,n+1): t+=0.55/n; h-=90/n; frames.append((t,x,y,h))
        tl.append((t,L)); hls.append((t0,t,4)); vars_.append((t0,t,sq,size,side))
    trails.append((tstart,pts,tl,L,COLORS[sq],size))
    labels.append((tstart,t,f"Square {sq+1}: {size} cm","the inner loop draws four sides","#22527B"))
t0=t; t+=4.0; frames.append((t,x,y,h)); T=t
labels.append((t0,T,"Two squares in, two to go","the next passes use 30 and 35","#2E7D32"))
vars_.append((t0,T,1,25,3))
DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
def vis(a,b): return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{max(a/T,0.0001):.5f};{min(b/T,0.9999):.5f}" calcMode="discrete" {DUR}/>'
def first(b): return f'<animate attributeName="opacity" values="1;0" keyTimes="0;{b/T:.5f}" calcMode="discrete" {DUR}/>'
keys=";".join(f"{f[0]/T:.5f}" for f in frames); trs=";".join(f"{f[1]:.1f} {f[2]:.1f}" for f in frames); ros=";".join(f"{f[3]:.1f}" for f in frames)
b=['<text class="h" x="20" y="26">A loop inside a loop: the first two squares</text>']
b.append('<rect x="20" y="40" width="390" height="340" rx="10" fill="#F3F4F6" stroke="#DEE2E6"/>')
b.append(f'<path d="M {SX0-14} {SY0} h 28 M {SX0} {SY0-14} v 28" stroke="#ADB5BD" stroke-width="2"/><text class="sm" x="{SX0+18}" y="{SY0+26}" style="font-weight:700">start</text>')
anim=[]
for (a,pts,tl,L,col,size) in trails:
    pp=' '.join(f'{p[0]:.1f},{p[1]:.1f}' for p in pts)
    ks="0;"+";".join(f"{q/T:.5f}" for q,_ in tl)+";1"; vs=f"{L:.1f};"+";".join(f"{L-l:.1f}" for _,l in tl)+";0"
    anim.append(f'<polyline points="{pp}" fill="none" stroke="{col}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="{L:.0f} {L+20:.0f}"><animate attributeName="stroke-dashoffset" values="{vs}" keyTimes="{ks}" {DUR}/></polyline>')
    # size tag on the first side, once drawn
    ty=SY0-size*PX+(16 if size==20 else -8); tx=SX0-size*PX/2
    anim.append(f'<g opacity="0">{vis(tl[6][0],T)}<text class="sm" x="{tx:.0f}" y="{ty:.0f}" text-anchor="middle" style="fill:{col};font-weight:700">{size} cm</text></g>')
anim.append(f'<g><animateTransform attributeName="transform" type="translate" values="{trs}" keyTimes="{keys}" {DUR}/><g><animateTransform attributeName="transform" type="rotate" values="{ros}" keyTimes="{keys}" {DUR}/><use href="#pcXRP" transform="scale({S})"/></g></g>')
X=430
b.append(f'<text class="h" x="{X}" y="26">The program</text>')
CODE=[(0,"for square in range(4):"),(1,"size = 20 + square * 5"),(1,"for side in range(4):"),(2,"drivetrain.straight(size)"),(2,"drivetrain.turn(90)")]
LY=lambda i: 52+i*21
hlg=[]
for li in range(len(CODE)):
    ks=[0.0]; vs=[0]
    for (p,q,l) in hls:
        if l==li: ks+=[p/T,min(q/T,0.9999)]; vs+=[1,0]
    hlg.append(f'<rect x="{X-6}" y="{LY(li)-15}" width="244" height="20" rx="4" fill="#FDECEE" stroke="#D1182C" stroke-width="1.2" opacity="0"><animate attributeName="opacity" values="{";".join(map(str,vs))}" keyTimes="{";".join(f"{k:.5f}" for k in ks)}" calcMode="discrete" {DUR}/></rect>')
b.append('<g class="anim">'+''.join(hlg)+'</g>')
for i,(ind,txt) in enumerate(CODE): b.append(f'<text class="ms" x="{X+2+ind*16}" y="{LY(i)}">{txt}</text>')
VY=170
b.append(f'<rect x="{X-6}" y="{VY}" width="244" height="64" rx="8" fill="#F8F9FA" stroke="#ADB5BD"/>')
b.append(f'<text class="sm" x="{X+4}" y="{VY+18}">the counters, right now</text>')
def vbox(sq,size,side):
    f=lambda v:'-' if v is None else str(v)
    return (f'<text class="m" x="{X+4}" y="{VY+42}">square = {f(sq)}</text><text class="m" x="{X+128}" y="{VY+42}">side = {f(side)}</text>'
            f'<text class="m" x="{X+4}" y="{VY+58}">size = {f(size)}</text>')
anim.append(f'<g opacity="0">{first(1.0)}{vbox(None,None,None)}</g>')
for (p,q,sq,size,side) in vars_: anim.append(f'<g opacity="0">{vis(p,q)}{vbox(sq,size,side)}</g>')
LB=252
for (p,q,tx,sub,col) in labels:
    anim.append(f'<g opacity="0">{vis(p,q) if p>0 else first(q)}<rect x="{X-6}" y="{LB}" width="244" height="54" rx="10" fill="#FFFFFF" stroke="{col}" stroke-width="2"/><text class="nb" x="{X+8}" y="{LB+23}" style="fill:{col}">{tx}</text><text class="sm" x="{X+8}" y="{LB+42}">{sub}</text></g>')
for i,ln in enumerate(["size changes once per square; side","counts 0 to 3 inside every square."]):
    b.append(f'<text class="sm" x="{X-6}" y="{LB+76+i*15}">{ln}</text>')
b.append('<g class="anim">'+''.join(anim)+'</g>')
still=[f'<polyline points="{" ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in tr[1])}" fill="none" stroke="{tr[4]}" stroke-width="4" stroke-linejoin="round"/>' for tr in trails]
still.append(f'<use href="#pcXRP" transform="translate({SX0} {SY0}) scale({S})"/>'+vbox(1,25,3))
b.append('<g class="still">'+''.join(still)+'</g>')
style_extra='<style>.still{display:none} @media (prefers-reduced-motion: reduce){.anim{display:none}.still{display:inline}}</style>'
out=svg('A loop inside a loop: the first two squares',
 'An animation, seen from above, of the first two passes of the nested-loop program from Lesson 1-10. Beside the robot, the five lines of the program, with the one running highlighted, and a box showing the counters square, side and size. On the first pass of the outer loop, square is 0 and size works out to 20; the inner loop then runs four times, side counting 0 to 3, and the robot draws a 20 cm square in blue and ends back on its start mark. On the second pass square is 1 and size is 25, and the robot draws a 25 cm square in purple from the same corner, around the first one. The animation stops there; the remaining two passes would draw 30 and 35 cm squares the same way.',b,H=390)
out=out.replace('<rect width="680"',style_extra+'\n  <rect width="680"',1)
open(OUTDIR+'nest-two-squares.svg','w').write(out); print(round(T,1))
