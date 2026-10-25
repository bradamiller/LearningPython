import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
# Lesson 2-8: track_to_intersection() -- follow the circle until both sensors are on the cross.
import math; from common import *
S=0.7; TW=9*S; SX=6.5*S; SF=60*S; SPOT=2.6*S
CX,CY,R=215,208,130
CROSS_A=math.radians(-62); CL=46          # cross strip: radial, centered on the line
def on_tape(px,py):
    d=math.hypot(px-CX,py-CY)
    if abs(d-R)<=TW/2: return True
    a=math.atan2(py-CY,px-CX)
    ux,uy=math.cos(CROSS_A),math.sin(CROSS_A)
    along=(px-CX)*ux+(py-CY)*uy; perp=-(px-CX)*uy+(py-CY)*ux
    return abs(along-R)<=CL/2 and abs(perp)<=TW/2
def cover(px,py):
    n=0
    for i in range(7):
        for j in range(7):
            n+=on_tape(px-SPOT+2*SPOT*(i+.5)/7, py-SPOT+2*SPOT*(j+.5)/7)
    return n/49
def sensors(x,y,r):
    a=math.radians(r); fx,fy=math.sin(a),-math.cos(a); rx,ry=math.cos(a),math.sin(a)
    L=(x+SF*fx-SX*rx, y+SF*fy-SX*ry); Rr=(x+SF*fx+SX*rx, y+SF*fy+SX*ry)
    return 0.2+0.6*cover(*L), 0.2+0.6*cover(*Rr)
# start: sensors on the line near the bottom, heading along it (counterclockwise on screen)
a0=math.radians(100)
px,py=CX+R*math.cos(a0),CY+R*math.sin(a0)
tx,ty=math.sin(a0),-math.cos(a0)                 # tangent, counterclockwise on screen
r=math.degrees(math.atan2(tx,-ty))+3             # a small initial misalignment so it weaves a bit
x,y=px-SF*tx, py-SF*ty
V=62.0; K=230.0; dt=0.02; t=0.0
frames=[(0.0,x,y,r)]; samples=[]
t=1.2; frames.append((t,x,y,r))                  # waiting for the button
stopped=None
while t<20:
    l,rr=sensors(x,y,r)
    samples.append((t,l,rr))
    if l>0.5 and rr>0.5: stopped=t; break
    om=-K*(l-rr)                                  # left sensor high -> line to the left -> turn left
    r+=om*dt; a=math.radians(r); x+=V*math.sin(a)*dt; y-=V*math.cos(a)*dt; t+=dt
    if len(samples)%3==0: frames.append((t,x,y,r))
frames.append((t,x,y,r))
tstop=t; T=tstop+4.0; frames.append((T,x,y,r))
DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
def first(b): return f'<animate attributeName="opacity" values="1;0" keyTimes="0;{b/T:.5f}" calcMode="discrete" {DUR}/>'
def vis(a,b): return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{max(a/T,0.0001):.5f};{min(b/T,0.9999):.5f}" calcMode="discrete" {DUR}/>'
keys=";".join(f"{f[0]/T:.5f}" for f in frames); trs=";".join(f"{f[1]:.1f} {f[2]:.1f}" for f in frames); ros=";".join(f"{f[3]:.1f}" for f in frames)
b=['<text class="h" x="20" y="26">Follow until the cross</text>']
b.append('<rect x="20" y="40" width="390" height="350" rx="10" fill="#F3F4F6" stroke="#DEE2E6"/>')
b.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="#FFFFFF" stroke="#2B2B2B" stroke-width="{TW:.1f}"/>')
ux,uy=math.cos(CROSS_A),math.sin(CROSS_A); deg=math.degrees(CROSS_A)
b.append(f'<rect x="{R-CL/2:.1f}" y="{-TW/2:.1f}" width="{CL}" height="{TW:.1f}" fill="#2B2B2B" transform="translate({CX} {CY}) rotate({deg:.1f})"/>')
la=CROSS_A-0.10; lx,ly=CX+(R+22)*math.cos(la),CY+(R+16)*math.sin(la)
b.append(f'<text class="sm" x="{lx:.0f}" y="{ly:.0f}" text-anchor="end" style="font-weight:700">the cross</text>')
anim=[]
anim.append(f'<g><animateTransform attributeName="transform" type="translate" values="{trs}" keyTimes="{keys}" {DUR}/><g><animateTransform attributeName="transform" type="rotate" values="{ros}" keyTimes="{keys}" {DUR}/><use href="#pcXRP" transform="scale({S})"/></g></g>')
# ring on the sensors once stopped
l,rr=sensors(x,y,r); a=math.radians(r)
sx,sy=x+SF*math.sin(a),y-SF*math.cos(a)
anim.append(f'<g opacity="0">{vis(tstop,T)}<circle cx="{sx:.1f}" cy="{sy:.1f}" r="14" fill="none" stroke="#D1182C" stroke-width="3"/></g>')
X=436
b.append(f'<text class="h" x="{X}" y="60">track_to_intersection()</text>')
LINES=[(0,"while not is_at_cross():"),(1,"follow: steer by the error"),(0,"stop the motors")]
LY=lambda i: 86+i*21
def bar(li,ivs):
    ks=[0.0]; vs=[0]
    for (p,q) in ivs: ks+=[p/T,min(q/T,0.9999)]; vs+=[1,0]
    return f'<rect x="{X-6}" y="{LY(li)-15}" width="236" height="20" rx="4" fill="#FDECEE" stroke="#D1182C" stroke-width="1.2" opacity="0"><animate attributeName="opacity" values="{";".join(map(str,vs))}" keyTimes="{";".join(f"{k:.5f}" for k in ks)}" calcMode="discrete" {DUR}/></rect>'
b.append('<g class="anim">'+bar(0,[(1.2,tstop)])+bar(1,[(1.2,tstop)])+bar(2,[(tstop,tstop+0.8)])+'</g>')
for i,(ind,txt) in enumerate(LINES): b.append(f'<text class="ms" x="{X+4+ind*18}" y="{LY(i)}">{txt}</text>')
BY=158
b.append(f'<rect x="{X-6}" y="{BY}" width="236" height="70" rx="8" fill="#F8F9FA" stroke="#ADB5BD"/>')
# readings box, sampled every ~0.24 s
step=12; pts=samples[::step]+[samples[-1]]
def tf(v): return f'<tspan style="fill:{"#2E7D32" if v else "#D1182C"};font-weight:700">{v}</tspan>'
def box(l,rr,c): return (f'<text class="ms" x="{X+6}" y="{BY+20}">Left:  {l:.2f}</text><text class="ms" x="{X+120}" y="{BY+20}">Right: {rr:.2f}</text>'
                         f'<text class="ms" x="{X+6}" y="{BY+42}">is_at_cross(): {tf(c)}</text>'
                         f'<text class="sm" x="{X+6}" y="{BY+60}">{"both above 0.5" if c else "needs BOTH above 0.5"}</text>')
anim.append(f'<g opacity="0">{first(1.2)}{box(*sensors(*frames[0][1:]),False)}</g>')
for i in range(len(pts)-1):
    t0,l0,r0=pts[i]; t1=pts[i+1][0] if i<len(pts)-2 else tstop
    anim.append(f'<g opacity="0">{vis(t0,t1)}{box(l0,r0,False)}</g>')
anim.append(f'<g opacity="0">{vis(tstop,T)}{box(l,rr,True)}</g>')
LB=246
labs=[(0,1.2,"Waiting for the button","robot on the circle, pointed along it","#6C757D"),
      (1.2,tstop,"Following the circle","one sensor high at a time: keep going","#22527B"),
      (tstop,T,"Stopped on the cross","both sensors on tape at once","#2E7D32")]
for (p,q,tx,sub,col) in labs:
    anim.append(f'<g opacity="0">{vis(p,q) if p>0 else first(q)}'
                f'<rect x="{X-6}" y="{LB}" width="236" height="54" rx="10" fill="#FFFFFF" stroke="{col}" stroke-width="2"/><text class="nb" x="{X+8}" y="{LB+23}" style="fill:{col}">{tx}</text><text class="sm" x="{X+8}" y="{LB+42}">{sub}</text></g>')
for i,ln in enumerate(["The loop line does the looking; the","body only steers. Nothing inside","the loop mentions the cross."]):
    b.append(f'<text class="sm" x="{X-6}" y="{LB+76+i*15}">{ln}</text>')
still=[f'<use href="#pcXRP" transform="translate({x:.1f} {y:.1f}) rotate({r:.1f}) scale({S})"/>',box(l,rr,True)]
b.append('<g class="anim">'+''.join(anim)+'</g>')
b.append('<g class="still">'+''.join(still)+'</g>')
style_extra='<style>.still{display:none} @media (prefers-reduced-motion: reduce){.anim{display:none}.still{display:inline}}</style>'
out=svg('Follow until the cross',
 'An animation, seen from above, of test_track() from Lesson 2-8. A taped circle has a short cross strip across it near the top right. The robot starts on the circle near the bottom, pointed along the line, waits for the button, then follows the line counterclockwise, weaving slightly as it steers by the error. Beside it, the outline of track_to_intersection(): while not is_at_cross, follow; then stop the motors. A box shows the live left and right readings and is_at_cross(): while following, at most one sensor reads high and is_at_cross() stays False. When both sensors reach the cross strip both read about 0.8, is_at_cross() becomes True, the loop ends and the robot stops with its sensors on the cross.',b,H=400)
out=out.replace('<rect width="680"',style_extra+'\n  <rect width="680"',1)
open(OUTDIR+'track-to-cross.svg','w').write(out)
print(round(tstop,2),round(T,2),len(frames),[round(v,2) for v in (l,rr)])
