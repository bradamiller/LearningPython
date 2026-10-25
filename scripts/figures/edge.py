import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math, random; from common import *
random.seed(4)
CX,CY,R=215,210,138; S=0.42; SENS=60*S; SPEED=46.0; STEP=0.22
frames=[]; t=0.0; robot_vis=[]   # robot fades between runs
def add(x,y,r): frames.append((t,x,y,r))
hl=[]        # (t0,t1,line)
reads=[]     # (t0,t1,value)
labels=[]    # (t0,t1,title,sub,color)
rings=[]     # (t0,t1,x,y)
runs=[0,128]
def fwd(r): a=math.radians(r); return (math.sin(a),-math.cos(a))
for ri,rot in enumerate(runs):
    ux,uy=fwd(rot)
    dist=R-3-SENS
    if ri==0: add(CX,CY,rot)
    t0run=t
    # read the left sensor
    v=round(random.uniform(0.18,0.23),2)
    hl.append((t,t+0.5,0)); reads.append([t,None,v]); t+=0.5; add(CX,CY,rot)
    drive_time=dist/SPEED; k=max(2,math.ceil(drive_time/(3*STEP)))
    tstart=None
    for i in range(k):
        hl.append((t,t+STEP,1)); t+=STEP
        if tstart is None: tstart=t; add(CX,CY,rot)
        hl.append((t,t+STEP,2)); t+=STEP
        hl.append((t,t+STEP,3)); t+=STEP
        last=(i==k-1)
        v=0.84 if last else round(random.uniform(0.18,0.23),2)
        reads[-1][1]=t-STEP; reads.append([t-STEP,None,v])
    tend=t-STEP
    # robot motion from tstart to tend: sample
    n=20
    frames.append((tstart,CX,CY,rot))
    for j in range(1,n+1):
        f=j/n; frames.append((tstart+(tend-tstart)*f, CX+ux*dist*f, CY+uy*dist*f, rot))
    xe,ye=CX+ux*dist,CY+uy*dist
    labels.append((t0run,tend,f"Run {ri+1}: on white","the loop keeps driving","#22527B"))
    hl.append((t,t+0.55,1)); t+=0.55       # while -> False
    hl.append((t,t+0.45,4)); t+=0.45       # stop
    hl.append((t,t+2.2,5)); tp=t; t+=2.2   # print
    reads[-1][1]=t
    sx,sy=xe+ux*SENS,ye+uy*SENS
    rings.append((tend,t,sx,sy))
    labels.append((tend,t,"Line detected!","Sensor value: 0.84","#2E7D32"))
    frames.append((t,xe,ye,rot))
    if ri<len(runs)-1:
        robot_vis.append((t,t+0.35)); t+=0.35; frames.append((t,xe,ye,rot))
        t+=0.01; frames.append((t,CX,CY,runs[ri+1]))
        labels.append((t-0.36,t+0.35,"Back to the middle","pointing at a new edge","#6C757D"))
        robot_vis.append((t,t+0.35)); t+=0.35; frames.append((t,CX,CY,runs[ri+1]))
T=t
frames.sort(key=lambda f:f[0])
# dedupe identical times (keep last)
fr=[]
for f in frames:
    if fr and abs(fr[-1][0]-f[0])<1e-6: fr[-1]=f
    else: fr.append(f)
frames=fr
keys=";".join(f"{f[0]/T:.4f}" for f in frames)
tr=";".join(f"{f[1]:.1f} {f[2]:.1f}" for f in frames)
ro=";".join(f"{f[3]:.1f}" for f in frames)
DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
def vis(t0,t1):
    a=max(t0/T,0.0001); b=min(t1/T,0.9999)
    return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{a:.4f};{b:.4f}" calcMode="discrete" {DUR}/>'
b=['<text class="h" x="20" y="26">Drive until the line, from above</text>']
b.append('<rect x="20" y="40" width="390" height="340" rx="10" fill="#F3F4F6" stroke="#DEE2E6"/>')
b.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="#FFFFFF" stroke="#2B2B2B" stroke-width="10"/>')
b.append(f'<text class="sm" x="{CX}" y="{CY+62}" text-anchor="middle" style="font-weight:700">white inside the taped circle</text>')
anim=[]; still=[]
for (t0,t1,x,y) in rings:
    anim.append(f'<g opacity="0">{vis(t0,t1)}<circle cx="{x:.1f}" cy="{y:.1f}" r="15" fill="none" stroke="#D1182C" stroke-width="3.2"/></g>')
# robot opacity: fade out/in
ok=["0","1"]; ov=["1","1"]
for (a,c) in robot_vis:
    pass
op_k=[0.0]; op_v=[1]
for i,(a,c) in enumerate(robot_vis):
    tgt=0 if i%2==0 else 1
    op_k+= [a/T, c/T]; op_v+=[op_v[-1], tgt]
op_k.append(1.0); op_v.append(op_v[-1])
opa=f'<animate attributeName="opacity" values="{";".join(map(str,op_v))}" keyTimes="{";".join(f"{k:.4f}" for k in op_k)}" {DUR}/>'
anim.append(f'<g>{opa}<animateTransform attributeName="transform" type="translate" values="{tr}" keyTimes="{keys}" {DUR}/>'
            f'<g><animateTransform attributeName="transform" type="rotate" values="{ro}" keyTimes="{keys}" {DUR}/>'
            f'<use href="#pcXRP" transform="scale({S})"/></g></g>')
X=436
b.append(f'<text class="h" x="{X}" y="60">What your test does</text>')
LINES=[(0,"read the left sensor"),(0,'while it says "white":'),(1,"drive forward"),(1,"read it again"),(0,"stop the motors"),(0,"print the reading")]
LY=lambda i: 86+i*21
# highlight bars (one element per line, many intervals)
hlg=[]
for li in range(len(LINES)):
    iv=[(a,c) for (a,c,l) in hl if l==li]
    ks=[0.0]; vs=[0]
    for (a,c) in iv: ks+=[a/T,c/T]; vs+=[1,0]
    ks=[max(0.0,min(k,0.9999)) for k in ks]
    hlg.append(f'<rect x="{X-6}" y="{LY(li)-15}" width="236" height="20" rx="4" fill="#FDECEE" stroke="#D1182C" stroke-width="1.2" opacity="0">'
                f'<animate attributeName="opacity" values="{";".join(map(str,vs))}" keyTimes="{";".join(f"{k:.4f}" for k in ks)}" calcMode="discrete" {DUR}/></rect>')
b.append('<g class="anim">'+''.join(hlg)+'</g>')
for i,(ind,txt) in enumerate(LINES):
    b.append(f'<text class="ms" x="{X+4+ind*18}" y="{LY(i)}">{txt}</text>')
# live reading box
BY=226
b.append(f'<rect x="{X-6}" y="{BY}" width="236" height="50" rx="8" fill="#F8F9FA" stroke="#ADB5BD"/>')
for (t0,t1,v) in reads:
    yes=v<0.5; col="#2E7D32" if yes else "#D1182C"
    anim.append(f'<g opacity="0">{vis(t0,t1)}<text class="m" x="{X+6}" y="{BY+20}">left = {v:.2f}</text>'
                f'<text class="ms" x="{X+6}" y="{BY+40}">left &lt; THRESHOLD (0.5): <tspan style="fill:{col};font-weight:700">{"True" if yes else "False"}</tspan></text></g>')
for (t0,t1,txt,sub,col) in labels:
    anim.append(f'<g opacity="0">{vis(t0,t1)}<rect x="{X-6}" y="292" width="236" height="54" rx="10" fill="#FFFFFF" stroke="{col}" stroke-width="2"/>'
                f'<text class="nb" x="{X+8}" y="315" style="fill:{col}">{txt}</text><text class="sm" x="{X+8}" y="334">{sub}</text></g>')
b+=[f'<text class="sm" x="{X-6}" y="366">The loop checks before every pass. The</text>',
    f'<text class="sm" x="{X-6}" y="381">first False reading ends it, wherever</text>',
    f'<text class="sm" x="{X-6}" y="396">the edge happens to be.</text>']
still.append(f'<use href="#pcXRP" transform="translate({CX} {CY}) scale({S})"/>')
still.append(f'<line x1="{CX}" y1="{CY-40}" x2="{CX}" y2="{CY-R+16}" stroke="#22527B" stroke-width="3" stroke-dasharray="6 5" marker-end="url(#aB)"/>')
still.append(f'<rect x="{X-6}" y="292" width="236" height="54" rx="10" fill="#FFFFFF" stroke="#22527B" stroke-width="2"/><text class="nb" x="{X+8}" y="315">Drive while on white</text><text class="sm" x="{X+8}" y="334">stop at the first line reading</text>')
b.append('<g class="anim">'+''.join(anim)+'</g>')
b.append('<g class="still">'+''.join(still)+'</g>')
style_extra='<style>.still{display:none} @media (prefers-reduced-motion: reduce){.anim{display:none}.still{display:inline}}</style>'
out=svg('Drive until the line, from above',
 'An animation, seen from above, of the Lesson 2-2 activity. The robot starts in the middle of a taped circle, pointing at the edge. Beside it, the test outline: read the left sensor; while it says white, drive forward and read it again; stop the motors; print the reading. A highlight steps through the outline as the program runs, and a box shows each reading: about 0.2 on white, so left is less than THRESHOLD and the loop goes round again while the robot creeps forward. When the sensor reaches the tape the reading jumps to 0.84, the comparison is False, the loop ends, the robot stops with its sensor on the line, and it prints the reading. The robot is put back in the middle pointing at a different part of the edge, and the same program stops it at the line there too.',b,H=410)
out=out.replace('<rect width="680"',style_extra+'\n  <rect width="680"',1)
open(OUTDIR+'drive-to-line.svg','w').write(out)
print(round(T,2))
