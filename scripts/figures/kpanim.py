import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math; from common import *
from kpsim import sim, CX, CY, R, S, SENS
PLAY=1.4; SIMT=8.4; GAP=0.9
RUNS=[(0.2,"KP = 0.2: too low","too gentle: it drifts off the line","#D1182C"),
      (0.5,"KP = 0.5: about right","small corrections, holds the edge","#2E7D32"),
      (1.0,"KP = 1.0: too high","over-corrects: it weaves","#D1182C")]
frames=[]; trails=[]; reads=[]; labels=[]; opac=[]
t=0.0
for ri,(kp,ttl,sub,col) in enumerate(RUNS):
    o=sim(kp,T=(6.2 if kp<0.3 else SIMT),K=6,tau=0.12,delay=0.10)
    t0=t
    pts=[]
    for k,(st,x,y,rot,r,e,c) in enumerate(o):
        if k%5==0:
            frames.append((t0+st/PLAY,x,y,rot)); pts.append((x,y))
    t1=t0+o[-1][0]/PLAY
    # readouts every 0.25 sim seconds
    step=25
    for k in range(0,len(o),step):
        st,x,y,rot,r,e,c=o[k]
        a=t0+st/PLAY; b=t0+min(o[-1][0],st+step*0.01)/PLAY
        reads.append([a,b,r,e,c])
    reads[-1][1]=t1+GAP-0.36
    trails.append((t0,t1,pts))
    labels.append((t0,t1+GAP,ttl,sub,col,kp))
    t=t1+GAP
    if ri<len(RUNS)-1:
        frames.append((t-0.35,pts[-1][0],pts[-1][1],frames[-1][3]))
        opac.append((t-0.35,t-0.01))
T=t
frames.append((T,frames[-1][1],frames[-1][2],frames[-1][3]))
frames.sort(key=lambda f:f[0])
keys=";".join(f"{f[0]/T:.5f}" for f in frames)
tr=";".join(f"{f[1]:.1f} {f[2]:.1f}" for f in frames)
ro=";".join(f"{f[3]:.1f}" for f in frames)
DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
def vis(t0,t1):
    a=max(t0/T,0.0001); b=min(t1/T,0.9999)
    return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{a:.5f};{b:.5f}" calcMode="discrete" {DUR}/>'
b=['<text class="h" x="20" y="26">Tuning KP, from above</text>']
b.append('<rect x="20" y="40" width="390" height="350" rx="10" fill="#F3F4F6" stroke="#DEE2E6"/>')
b.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="#2B2B2B" stroke-width="10"/>')
b.append(f'<text class="sm" x="{CX}" y="{CY+4}" text-anchor="middle" style="font-weight:700">the left sensor follows</text>')
b.append(f'<text class="sm" x="{CX}" y="{CY+20}" text-anchor="middle" style="font-weight:700">the outside edge of the tape</text>')
anim=[]; still=[]
for (t0,t1,pts) in trails:
    L=sum(math.hypot(pts[i][0]-pts[i-1][0],pts[i][1]-pts[i-1][1]) for i in range(1,len(pts)))
    d=' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)
    anim.append(f'<g opacity="0">{vis(t0,t1+GAP-0.05)}<polyline points="{d}" fill="none" stroke="#4C8BF5" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" opacity="0.7" stroke-dasharray="{L:.0f} {L+20:.0f}" stroke-dashoffset="{L:.0f}">'
                f'<animate attributeName="stroke-dashoffset" values="{L:.0f};{L:.0f};0;0" keyTimes="0;{t0/T:.5f};{t1/T:.5f};1" {DUR}/></polyline></g>')
# robot, fading between runs
ok=[0.0]; ov=["1"]
for (a,c) in opac:
    ok+=[a/T,c/T,c/T+0.004,(c+0.35)/T]; ov+=["1","0","0","1"]
ok.append(1.0); ov.append("1")
opa=f'<animate attributeName="opacity" values="{";".join(ov)}" keyTimes="{";".join(f"{k:.5f}" for k in ok)}" {DUR}/>'
anim.append(f'<g>{opa}<animateTransform attributeName="transform" type="translate" values="{tr}" keyTimes="{keys}" {DUR}/>'
            f'<g><animateTransform attributeName="transform" type="rotate" values="{ro}" keyTimes="{keys}" {DUR}/>'
            f'<use href="#pcXRP" transform="scale({S})"/></g></g>')
X=430
b.append(f'<text class="h" x="{X}" y="60">The same loop, three KP values</text>')
LINES=[(0,"loop forever:"),(1,"error = get_error()"),(1,"correction = error x KP"),(1,"arcade(BASE_EFFORT, correction)")]
for i,(ind,txt) in enumerate(LINES):
    b.append(f'<text class="ms" x="{X+4+ind*16}" y="{86+i*21}">{txt}</text>')
BY=86+4*21+2
for (t0,t1,ttl,sub,col,kp) in labels:
    anim.append(f'<g opacity="0">{vis(t0,t1)}<rect x="{X-6}" y="{BY}" width="246" height="54" rx="10" fill="#FFFFFF" stroke="{col}" stroke-width="2"/>'
                f'<text class="nb" x="{X+8}" y="{BY+23}" style="fill:{col}">{ttl}</text><text class="sm" x="{X+8}" y="{BY+42}">{sub}</text></g>')
RY=BY+68
b.append(f'<rect x="{X-6}" y="{RY}" width="246" height="72" rx="8" fill="#F8F9FA" stroke="#ADB5BD"/>')
for (a,c,r,e,cc) in reads:
    anim.append(f'<g opacity="0">{vis(a,c)}<text class="ms" x="{X+6}" y="{RY+20}">left reading  {r:.2f}</text>'
                f'<text class="ms" x="{X+6}" y="{RY+40}">error         {e:+.2f}</text>'
                f'<text class="ms" x="{X+6}" y="{RY+60}">correction    {cc:+.2f}</text></g>')
NY=RY+92
for i,ln in enumerate(["Nothing changes between the three runs","but one number. Too low and the robot","can't steer hard enough for the curve;","too high and every small error turns","into a big swerve past the edge."]):
    b.append(f'<text class="sm" x="{X-6}" y="{NY+i*15}">{ln}</text>')
still.append(f'<rect x="{X-6}" y="{BY}" width="246" height="54" rx="10" fill="#FFFFFF" stroke="#22527B" stroke-width="2"/><text class="nb" x="{X+8}" y="{BY+23}">Low drifts off, high weaves</text><text class="sm" x="{X+8}" y="{BY+42}">the right KP holds the edge</text>')
o=sim(0.5,T=0.01); x,y,rot=o[0][1],o[0][2],o[0][3]
still.append(f'<use href="#pcXRP" transform="translate({x:.1f} {y:.1f}) rotate({rot:.1f}) scale({S})"/>')
b.append('<g class="anim">'+''.join(anim)+'</g>')
b.append('<g class="still">'+''.join(still)+'</g>')
style_extra='<style>.still{display:none} @media (prefers-reduced-motion: reduce){.anim{display:none}.still{display:inline}}</style>'
H=max(400,NY+5*15+5)
out=svg('Tuning KP, from above',
 'An animation, seen from above, of the same line-following program run three times on a taped circle, with a different KP each time. The robot follows the outside edge of the tape with its left sensor, driving clockwise, and a blue line traces its path. With KP = 0.2 the correction is too small for the curve: the robot drifts outward and leaves the line. With KP = 0.5 it holds the edge with small corrections. With KP = 1.0 it over-corrects, swerving back and forth across the edge. Beside it, the three lines of the loop, and a box showing the left reading, the error and the correction as the robot drives.',b,H=H)
out=out.replace('<rect width="680"',style_extra+'\n  <rect width="680"',1)
open(OUTDIR+'kp-tuning.svg','w').write(out)
print(round(T,2),H)
