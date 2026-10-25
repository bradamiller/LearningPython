import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
# Lesson 1-5: one polygon function, four calls. A PlayFigure with a button per call.
import math, json; from common import *
S=0.48; PX=5.8
SX,SY=352,262
CALLS=[(4,30),(3,30),(6,20),(8,15)]
NAMES={3:"triangle",4:"square",6:"hexagon",8:"octagon"}
frames=[(0.0,SX,SY,0.0)]; segs=[]; t=0.6
for (n,side) in CALLS:
    s0=t; x,y,h=SX,SY,0.0
    frames.append((s0-0.001,x,y,h)); t=s0+0.3; frames.append((t,x,y,h))
    pts=[(x,y)]; tl=[(s0,0.0),(t,0.0)]; L=0.0; ang=360/n
    for k in range(n):
        d=side*PX; ux,uy=math.sin(math.radians(h)),-math.cos(math.radians(h)); m=10; dur=0.9*side/20
        for i in range(1,m+1):
            t+=dur/m; x+=ux*d/m; y+=uy*d/m; L+=d/m; frames.append((t,x,y,h)); tl.append((t,L))
        pts.append((x,y)); m=6
        for i in range(1,m+1): t+=(0.25+0.35*ang/90)/m; h-=ang/m; frames.append((t,x,y,h))
        tl.append((t,L))
    e=t; t+=1.2; frames.append((t,SX,SY,h)); tl.append((t,L))
    segs.append((s0,e,n,side,pts,tl,L)); t+=0.4
T=t; frames.append((T,SX,SY,0.0)); frames.sort(key=lambda f:f[0])
DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
def first(b): return f'<animate attributeName="opacity" values="1;0" keyTimes="0;{b/T:.5f}" calcMode="discrete" {DUR}/>'
def vis(a,b): return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{max(a/T,0.0001):.5f};{min(b/T,0.9999):.5f}" calcMode="discrete" {DUR}/>'
keys=";".join(f"{f[0]/T:.5f}" for f in frames); trs=";".join(f"{f[1]:.1f} {f[2]:.1f}" for f in frames); ros=";".join(f"{f[3]:.1f}" for f in frames)
b=['<text class="h" x="20" y="24">One function, four calls</text>']
b.append('<rect x="20" y="36" width="420" height="300" rx="10" fill="#F3F4F6" stroke="#DEE2E6"/>')
b.append(f'<path d="M {SX-14} {SY} h 28 M {SX} {SY-14} v 28" stroke="#ADB5BD" stroke-width="2"/><text class="sm" x="{SX+18}" y="{SY+26}" style="font-weight:700">start</text>')
anim=[]
for (s0,e,n,side,pts,tl,L) in segs:
    pp=' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)
    ks="0;"+";".join(f"{q/T:.5f}" for q,_ in tl)+";1"; vs=f"{L:.1f};"+";".join(f"{L-l:.1f}" for _,l in tl)+";0"
    seg_end=tl[-1][0]+0.35
    anim.append(f'<g opacity="0">{vis(s0,seg_end)}<polyline points="{pp}" fill="none" stroke="#1F6FEB" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="{L:.0f} {L+20:.0f}"><animate attributeName="stroke-dashoffset" values="{vs}" keyTimes="{ks}" {DUR}/></polyline></g>')
anim.append(f'<g><animateTransform attributeName="transform" type="translate" values="{trs}" keyTimes="{keys}" {DUR}/><g><animateTransform attributeName="transform" type="rotate" values="{ros}" keyTimes="{keys}" {DUR}/><use href="#pcXRP" transform="scale({S})"/></g></g>')
X=460
b.append(f'<text class="h" x="{X}" y="58">The call</text>')
anim.append(f'<g opacity="0">{first(segs[0][0])}<text class="sm" x="{X}" y="84">Press a call to run it. The</text><text class="sm" x="{X}" y="100">function inside never changes:</text><text class="sm" x="{X}" y="116">only the two numbers do.</text></g>')
for (s0,e,n,side,pts,tl,L) in segs:
    a=360/n; at=f"{a:g}"
    anim.append(f'<g opacity="0">{vis(s0,tl[-1][0]+0.35)}'
        f'<text class="m" x="{X}" y="84">polygon ({n}, {side})</text>'
        f'<text class="n" x="{X}" y="114">sides = <tspan style="font-weight:700">{n}</tspan></text>'
        f'<text class="n" x="{X}" y="134">side_length = <tspan style="font-weight:700">{side}</tspan> cm</text>'
        f'<text class="sm" x="{X}" y="164">Repeat {n} times:</text>'
        f'<text class="sm" x="{X+12}" y="182">Straight {side} cm</text>'
        f'<text class="sm" x="{X+12}" y="200">Turn 360 ÷ {n} = <tspan style="font-weight:700;fill:#D1182C">{at}°</tspan></text>'
        f'<text class="nb" x="{X}" y="232">{"An" if NAMES[n][0] in "aeiou" else "A"} {NAMES[n]}</text></g>')
b+= [f'<text class="sm" x="{X}" y="282">The turns always add up to</text>',
     f'<text class="sm" x="{X}" y="298">360°, so every shape ends</text>',
     f'<text class="sm" x="{X}" y="314">back on its start mark.</text>']
b.append('<g>'+''.join(anim)+'</g>')
modes=[{"label":f"polygon ({s[2]}, {s[3]})","start":round(s[0],3),"stop":round(s[5][-1][0],3)} for s in segs]
o=svg('One polygon function, four calls',
 'An animation of an XRP seen from above with a marker in the hole between its wheels. Four buttons run the four calls from the lesson: polygon (4, 30), polygon (3, 30), polygon (6, 20) and polygon (8, 15). Each starts from the same mark, facing up, and draws its shape in blue, turning left at each corner, while a panel shows the call, the values sides and side_length take, and the turn the function works out: 360 divided by 4 is 90 degrees, a square; 360 divided by 3 is 120, a triangle; 360 divided by 6 is 60, a hexagon; 360 divided by 8 is 45, an octagon. Every shape ends back on its start mark, because the turns add up to 360 degrees.',b,W=680,H=350)
o=o.replace('<svg xmlns="http://www.w3.org/2000/svg"',"<svg xmlns=\"http://www.w3.org/2000/svg\" data-modes='"+json.dumps(modes)+"'",1)
open(OUTDIR+'polygon-calls.svg','w').write(o); print(round(T,1),modes)
