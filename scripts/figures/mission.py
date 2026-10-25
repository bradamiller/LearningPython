import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math; from common import *
CX,CY,R=215,200,128; S=0.42; SENS=60*S; DELTA=math.degrees(SENS/R)
SPEED=210.0   # px per second along the circle
def pos(th): t=math.radians(th); return (CX+R*math.cos(t), CY+R*math.sin(t))
frames=[]   # (time, x, y, rot)
events=[]   # (t_start, t_end, label_id)
t=0.0
def add(th,rot): frames.append((t,)+pos(th)+(rot,))
def travel(th0,th1,off):     # rot = th + off  (off 0 when th decreasing, 180 when increasing)
    global t
    n=max(2,int(abs(th1-th0)/3))
    dur=math.radians(abs(th1-th0))*R/SPEED
    for i in range(1,n+1):
        th=th0+(th1-th0)*i/n; t0=t; t=t0+dur/n; add(th,th+off); t=t
    return
def hold(th,rot,d):
    global t; t+=d; add(th,rot)
def spin(th,r0,r1,d):
    global t; n=8
    for i in range(1,n+1): t+=d/n; add(th,r0+(r1-r0)*i/n)
labels=[]
add(90,90); hold(90,90,0.8)
legs=[(90,0,-1),(0,360,1),(360,0,-1),(0,360,1)]
rot=90; flashes=[]
for i,(a_,b_,d) in enumerate(legs):
    off = 0 if d<0 else 180
    base = rot - (a_+off)
    t_leg = 0.0 if i==0 else t
    stop = b_ - d*DELTA
    travel(a_,stop,off+base)
    t_flash=t
    hold(stop,stop+off+base,0.45)
    labels.append((t_leg,t_flash,f"Leg {i+1}","following to the cross"))
    flashes.append((t_flash,t,b_))
    travel(stop,b_,off+base)
    r=b_+off+base
    hold(b_,r,0.25); spin(b_,r,r+60,0.45); spin(b_,r+60,r+180,0.95); hold(b_,r+180,0.3)
    labels.append((t_flash,t,"Cross! Reversing...",f"reversal {i+1}: park, one clockwise turn"))
    rot=r+180
t_done=t
hold(360,rot,2.6)
T=t
labels.append((t_done,T,"Done! 4 reversals complete.","the robot stops"))
kt=lambda x: f"{x/T:.4f}"
keys=";".join(kt(f[0]) for f in frames)
tr=";".join(f"{f[1]:.1f} {f[2]:.1f}" for f in frames)
ro=";".join(f"{f[3]:.1f}" for f in frames)
DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
def vis(t0,t1):
    a=max(t0/T,0.0001); b=min(t1/T,0.9999)
    return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{a:.4f};{b:.4f}" calcMode="discrete" {DUR}/>'
b=['<text class="h" x="20" y="26">The mission, from above</text>']
# floor, circle tape, strip
b.append(f'<rect x="20" y="40" width="390" height="330" rx="10" fill="#F3F4F6" stroke="#DEE2E6"/>')
b.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="#2B2B2B" stroke-width="10"/>')
XC=CX+R; SL=26
b.append(f'<rect x="{XC-SL/2}" y="{CY-5}" width="{SL}" height="10" fill="#2B2B2B"/>')
x,y=pos(0); b.append(f'<text class="sm" x="{x-34}" y="{y+4}" text-anchor="end" style="font-weight:700">the cross</text>')
x,y=pos(90); b.append(f'<text class="sm" x="{x}" y="{y+40}" text-anchor="middle" style="font-weight:700">start</text>')
anim=[]; still=[]
for (t0,t1,th) in flashes:
    x,y=pos(th)
    anim.append(f'<g opacity="0">{vis(t0,t1+1.4)}<circle cx="{x:.1f}" cy="{y:.1f}" r="20" fill="none" stroke="#D1182C" stroke-width="3.5"/></g>')
robot=(f'<g><animateTransform attributeName="transform" type="translate" values="{tr}" keyTimes="{keys}" {DUR}/>'
       f'<g><animateTransform attributeName="transform" type="rotate" values="{ro}" keyTimes="{keys}" {DUR}/>'
       f'<use href="#pcXRP" transform="scale({S})"/></g></g>')
anim.append(robot)
X=440
b+=[f'<text class="h" x="{X}" y="60">What your program does</text>',
    f'<text class="n" x="{X}" y="84">1. Follow the circle to the cross</text>',
    f'<text class="n" x="{X}" y="104">2. Park on it and turn around</text>',
    f'<text class="n" x="{X}" y="124">3. Follow the other way</text>',
    f'<text class="n" x="{X}" y="144">4. Four reversals, then stop</text>']
for (t0,t1,txt,sub) in labels:
    col="#2E7D32" if txt.startswith("Done") else ("#D1182C" if txt.startswith("Cross") else "#22527B")
    anim.append(f'<g opacity="0">{vis(t0,t1)}<rect x="{X}" y="180" width="230" height="58" rx="10" fill="#FFFFFF" stroke="{col}" stroke-width="2"/>'
                f'<text class="nb" x="{X+14}" y="204" style="fill:{col}">{txt}</text><text class="sm" x="{X+14}" y="224">{sub}</text></g>')
b+=[f'<text class="sm" x="{X}" y="272">The cross is one short strip: long</text>',
    f'<text class="sm" x="{X}" y="288">enough for both sensors to see it,</text>',
    f'<text class="sm" x="{X}" y="304">too short to stop the turn. So one</text>',
    f'<text class="sm" x="{X}" y="320">clockwise turn carries on to the</text>',
    f'<text class="sm" x="{X}" y="336">circle behind, and the robot meets</text>',
    f'<text class="sm" x="{X}" y="352">the cross once a lap.</text>']
# still version for reduced motion: robot at start, arrows
still.append(f'<use href="#pcXRP" transform="translate({pos(90)[0]:.1f} {pos(90)[1]:.1f}) rotate(90) scale({S})"/>')
for th in (0,):
    x,y=pos(th); still.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="20" fill="none" stroke="#D1182C" stroke-width="3.5"/>')
still.append(f'<rect x="{X}" y="180" width="230" height="58" rx="10" fill="#FFFFFF" stroke="#22527B" stroke-width="2"/><text class="nb" x="{X+14}" y="204">Reverse at each cross</text><text class="sm" x="{X+14}" y="224">four times, then stop</text>')
b.append('<g class="anim">'+''.join(anim)+'</g>')
b.append('<g class="still">'+''.join(still)+'</g>')
style_extra='<style>.still{display:none} @media (prefers-reduced-motion: reduce){.anim{display:none}.still{display:inline}}</style>'
out=svg('The final project, from above',
 'An animation, seen from above, of the Module 2 final project. A taped circle has one short strip of tape across its line on the right-hand side: the cross, about half as long as the robot is wide. The robot starts at the bottom of the circle and follows it to the cross. Its sensors reach the cross first and it stops; it drives forward to park its wheels on the cross, then turns clockwise in place; the cross is too short for the sensors to touch, so the turn carries on until they find the circle behind, facing the other way. It follows the circle all the way round the other way and meets the cross again from the other side, and reverses there the same way. Four reversals, and it stops. A panel beside it names each stage: following to the cross, cross detected and reversing, and done.',b,H=390)
out=out.replace('<rect width="680"',style_extra+'\n  <rect width="680"',1)
open(OUTDIR+'final-project-mission.svg','w').write(out)
print(round(T,2),'s')
