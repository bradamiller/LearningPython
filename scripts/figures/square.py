import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math; from common import *
S=0.42; SENS=60*S; SPEED=120.0
g=G(100,100,sp=110,n=3,pad=62)
def P(a,b): return g.p(a,b)
frames=[]; t=0.0
def add(x,y,r): frames.append((t,x,y,r))
def move(p0,p1,r):
    global t
    (x0,y0),(x1,y1)=p0,p1; d=math.hypot(x1-x0,y1-y0); n=max(2,int(d/6)); dur=d/SPEED
    for i in range(1,n+1):
        t+=dur/n; add(x0+(x1-x0)*i/n, y0+(y1-y0)*i/n, r)
def hold(p,r,d):
    global t; t+=d; add(p[0],p[1],r)
def spin(p,r0,r1,d):
    global t; n=10
    for i in range(1,n+1): t+=d/n; add(p[0],p[1],r0+(r1-r0)*i/n)
labels=[]; flashes=[]
dirs=[(0,1,0),(1,0,90),(0,-1,180),(-1,0,270)]   # (dx, dy, screen rotation)
pos=(0,0); rot=0
add(*P(*pos),0); hold(P(*pos),0,0.9)
labels.append((0,t,"Ready","parked on the start corner, facing away"))
for side,(dx,dy,_) in enumerate(dirs):
    for k in range(2):
        t0=t
        nxt=(pos[0]+dx,pos[1]+dy)
        (x0,y0),(x1,y1)=P(*pos),P(*nxt)
        ux,uy=(x1-x0)/g.sp,(y1-y0)/g.sp
        stop=(x1-ux*SENS, y1-uy*SENS)
        move((x0,y0),stop,rot)          # track_to_intersection()
        tf=t; hold(stop,rot,0.35); flashes.append((tf,t+0.9,nxt))
        move(stop,(x1,y1),rot)          # drive_past_intersection()
        hold((x1,y1),rot,0.15)
        labels.append((t0,t,f"Side {side+1} of 4",f"arriving at intersection {k+1} of SIDE = 2"))
        pos=nxt
    t0=t
    hold(P(*pos),rot,0.2); spin(P(*pos),rot,rot+60,0.45); spin(P(*pos),rot+60,rot+90,0.4); hold(P(*pos),rot+90,0.3)
    rot+=90
    labels.append((t0,t,"Turning right...","turn_clockwise() at the corner"))
t0=t; hold(P(*pos),rot,2.8); T=t
labels.append((t0,T,"Square complete!","back at start, facing the way it began"))
kt=lambda x: f"{x/T:.4f}"
keys=";".join(kt(f[0]) for f in frames)
tr=";".join(f"{f[1]:.1f} {f[2]:.1f}" for f in frames)
ro=";".join(f"{f[3]:.1f}" for f in frames)
DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
def vis(t0,t1):
    a=max(t0/T,0.0001); b=min(t1/T,0.9999)
    return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{a:.4f};{b:.4f}" calcMode="discrete" {DUR}/>'
b=['<text class="h" x="20" y="26">The square, from above</text>']
b+=g.base(axes=False,north=False)
# faint route
pts=[(0,0),(0,2),(2,2),(2,0),(0,0)]
b.append('<path d="M '+' L '.join(f'{P(*q)[0]} {P(*q)[1]}' for q in pts)+'" fill="none" stroke="#4C8BF5" stroke-width="5" opacity="0.35" stroke-dasharray="2 9" stroke-linecap="round"/>')
x,y=P(0,0); b.append(f'<text class="sm" x="{x}" y="{y+84}" text-anchor="middle" style="font-weight:700">start, nearest you</text>')
anim=[]; still=[]
for (t0,t1,q) in flashes:
    x,y=P(*q)
    anim.append(f'<g opacity="0">{vis(t0,t1)}<circle cx="{x:.1f}" cy="{y:.1f}" r="17" fill="none" stroke="#D1182C" stroke-width="3.2"/></g>')
anim.append(f'<g><animateTransform attributeName="transform" type="translate" values="{tr}" keyTimes="{keys}" {DUR}/>'
            f'<g><animateTransform attributeName="transform" type="rotate" values="{ro}" keyTimes="{keys}" {DUR}/>'
            f'<use href="#pcXRP" transform="scale({S})"/></g></g>')
X=420
b+=[f'<text class="h" x="{X}" y="60">What your program does</text>',
    f'<text class="n" x="{X}" y="84">4 times:</text>',
    f'<text class="n" x="{X+16}" y="104">drive SIDE intersections</text>',
    f'<text class="n" x="{X+16}" y="124">turn right</text>',
    f'<text class="n" x="{X}" y="144">then print "Square complete!"</text>']
for (t0,t1,txt,sub) in labels:
    col="#2E7D32" if txt.startswith("Square") else ("#D1182C" if txt.startswith("Turning") else "#22527B")
    anim.append(f'<g opacity="0">{vis(t0,t1)}<rect x="{X}" y="180" width="244" height="58" rx="10" fill="#FFFFFF" stroke="{col}" stroke-width="2"/>'
                f'<text class="nb" x="{X+14}" y="204" style="fill:{col}">{txt}</text><text class="sm" x="{X+14}" y="224">{sub}</text></g>')
b+=[f'<text class="sm" x="{X}" y="272">Each side is two arrivals: the sensors</text>',
    f'<text class="sm" x="{X}" y="288">reach the intersection, then the</text>',
    f'<text class="sm" x="{X}" y="304">robot drives on to park its wheels on</text>',
    f'<text class="sm" x="{X}" y="320">it. Four right turns make 360 degrees,</text>',
    f'<text class="sm" x="{X}" y="336">so it ends facing the way it started.</text>']
still.append(f'<use href="#pcXRP" transform="translate({P(0,0)[0]} {P(0,0)[1]}) scale({S})"/>')
still.append(f'<rect x="{X}" y="180" width="244" height="58" rx="10" fill="#FFFFFF" stroke="#22527B" stroke-width="2"/><text class="nb" x="{X+14}" y="204">Four sides, four right turns</text><text class="sm" x="{X+14}" y="224">back to the start corner</text>')
b.append('<g class="anim">'+''.join(anim)+'</g>')
b.append('<g class="still">'+''.join(still)+'</g>')
style_extra='<style>.still{display:none} @media (prefers-reduced-motion: reduce){.anim{display:none}.still{display:inline}}</style>'
out=svg('The square, from above',
 'An animation, seen from above, of the Module 3 final project on a 3 by 3 taped grid. The robot starts parked on the bottom-left intersection, the corner nearest you, facing away from you. It drives up the left side: its sensors reach the first intersection, it drives on to park its wheels there, then does the same at the second, the top-left corner. It turns right and drives along the top two intersections, turns right and drives down the right side, turns right and drives along the bottom back to the start, and turns right once more, ending facing the way it began. A panel beside it names each stage: side 1 to 4, arriving at intersection 1 or 2, turning right, and square complete.',b,H=440)
out=out.replace('<rect width="680"',style_extra+'\n  <rect width="680"',1)
open(OUTDIR+'square-run.svg','w').write(out)
print(round(T,2))
