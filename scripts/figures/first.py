import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math; from common import *
S=0.6; PXCM=118*S/18.0
SX,SY=165,300; D=30*PXCM
LINES=["# setup: two imports, drivetrain, board","board.wait_for_button()",'print("Driving forward...")',"drivetrain.straight(30)",'print("Driving backward...")',"drivetrain.straight(-30)",'print("Done!")']
ev=[]; t=0.0; frames=[(0.0,SX,SY)]; shell=[]
def hold(li,d,lab=None):
    global t; ev.append((t,t+d,li)); t+=d; frames.append((t,frames[-1][1],frames[-1][2]))
hold(0,0.8)
hold(1,2.0)                    # waiting for the button
tb=t
hold(2,0.7); shell.append((t-0.35,"Driving forward..."))
a=t; dur=2.2
for i in range(1,21): frames.append((a+dur*i/20,SX,SY-D*i/20))
ev.append((a,a+dur,3)); t=a+dur
hold(4,0.7); shell.append((t-0.35,"Driving backward..."))
a=t
for i in range(1,21): frames.append((a+dur*i/20,SX,SY-D+D*i/20))
ev.append((a,a+dur,5)); t=a+dur
hold(6,0.7); shell.append((t-0.35,"Done!"))
t+=2.5; frames.append((t,SX,SY)); T=t
DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
def vis(a,b): return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{max(a/T,0.0001):.4f};{min(b/T,0.9999):.4f}" calcMode="discrete" {DUR}/>'
keys=";".join(f"{f[0]/T:.5f}" for f in frames); trs=";".join(f"{f[1]:.1f} {f[2]:.1f}" for f in frames)
b=['<text class="h" x="20" y="24">Your first program, running</text>']
b.append('<rect x="20" y="36" width="280" height="330" rx="10" fill="#F3F4F6" stroke="#DEE2E6"/>')
b.append(f'<path d="M {SX-14} {SY} h 28 M {SX} {SY-14} v 28" stroke="#ADB5BD" stroke-width="2"/><text class="sm" x="{SX-48}" y="{SY+4}" text-anchor="end" style="font-weight:700">start</text>')
b.append(f'<line x1="{SX+60}" y1="{SY}" x2="{SX+60}" y2="{SY-D:.1f}" stroke="#6C757D" stroke-width="1.4" marker-start="url(#aG)" marker-end="url(#aG)"/><text class="sm" x="{SX+66}" y="{SY-D/2+4:.1f}">30 cm</text>')
anim=[]
anim.append(f'<g opacity="0">{vis(0.8,tb)}<text class="nb" x="{SX}" y="{SY+52}" text-anchor="middle" style="fill:#D1182C">waiting for you to press the button</text></g>')
anim.append(f'<g><animateTransform attributeName="transform" type="translate" values="{trs}" keyTimes="{keys}" {DUR}/><use href="#pcXRP" transform="scale({S})"/></g>')
X=318
b.append(f'<text class="h" x="{X}" y="58">lesson_1_8_first_drive.py</text>')
LY=lambda i: 84+i*21
hl=[]
for li in range(len(LINES)):
    iv=[(p,q) for (p,q,l) in ev if l==li]
    ks=[0.0]; vs=[0]
    for (p,q) in iv: ks+=[p/T,min(q/T,0.9999)]; vs+=[1,0]
    hl.append(f'<rect x="{X-6}" y="{LY(li)-15}" width="352" height="20" rx="4" fill="#FDECEE" stroke="#D1182C" stroke-width="1.2" opacity="0"><animate attributeName="opacity" values="{";".join(map(str,vs))}" keyTimes="{";".join(f"{k:.5f}" for k in ks)}" calcMode="discrete" {DUR}/></rect>')
b.append('<g>'+''.join(hl)+'</g>')
for i,l in enumerate(LINES):
    style=' style="fill:#6C757D;white-space:pre"' if i==0 else ' style="white-space:pre"'
    b.append(f'<text class="ms" x="{X}" y="{LY(i)}"{style}>{l.replace("<","&lt;")}</text>')
SH=LY(len(LINES))+12
b.append(f'<text class="nb" x="{X}" y="{SH}">Shell</text>')
b.append(f'<rect x="{X-6}" y="{SH+8}" width="352" height="84" rx="8" fill="#1E2328"/>')
for k,(ts,txt) in enumerate(shell):
    anim.append(f'<g opacity="0">{vis(ts,T-0.01)}<text class="ms" x="{X+6}" y="{SH+30+k*22}" style="fill:#E9ECEF">{txt}</text></g>')
b.append('<g>'+''.join(anim)+'</g>')
o=svg('Your first program, running',
 'An animation of the Lesson 1-8 program running. On the left an XRP sits on the floor on its start mark. On the right, the program, with the line that is running highlighted, and the shell below it. First the program waits at board.wait_for_button() until the button is pressed. Then the shell prints Driving forward..., the robot drives 30 cm forward, the shell prints Driving backward..., the robot drives 30 cm back to its start mark, and the shell prints Done!',b,W=680,H=380)
open(OUTDIR+'first-drive.svg','w').write(o); print(round(T,1))
