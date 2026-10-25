import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math, json; from common import *
PXCM=5.5; BCM=15.5; S=BCM*PXCM/101.0
SX,SY=330,190
TURNS=[0.15,0.3,0.5,0.8]; STRAIGHT=0.5
def efforts(s,t):
    sc=max(abs(s),abs(t))/(abs(s)+abs(t))
    return (s-t)*sc,(s+t)*sc     # left, right: XRPLib arcade(), positive turn bends LEFT
runs=[]; t=0.6; frames=[(0.0,SX,SY,0.0)]; segs=[]; trails=[]; icc=[]
for tu in TURNS:
    l,r=efforts(STRAIGHT,tu); v=(l+r)/2
    Rcm=(BCM/2)*(l+r)/(r-l); R=Rcm*PXCM
    C=Rcm*2*math.pi; dur=max(1.4,(C/v)/(162/0.385)*5.0)
    s0=t; frames.append((s0-0.001,SX,SY,0.0)); frames.append((s0+0.3,SX,SY,0.0))
    n=72; pts=[]
    for i in range(n+1):
        a=2*math.pi*i/n; tt=s0+0.3+dur*i/n
        x=SX-R+R*math.cos(a); y=SY-R*math.sin(a)
        frames.append((tt,x,y,-math.degrees(a))); pts.append((x,y))
    e=s0+0.3+dur; frames.append((e+1.6,SX,SY,-360.0))
    segs.append((s0,e+1.6,tu,l,r,Rcm,dur)); trails.append((s0+0.3,e,pts,2*math.pi*R)); icc.append((SX-R,SY))
    t=e+1.6+0.5
T=t; frames.append((T,SX,SY,0.0)); frames.sort(key=lambda f:f[0])
DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
def first(b): return f'<animate attributeName="opacity" values="1;0" keyTimes="0;{b/T:.5f}" calcMode="discrete" {DUR}/>'
def vis(a,b): return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{max(a/T,0.0001):.5f};{min(b/T,0.9999):.5f}" calcMode="discrete" {DUR}/>'
keys=";".join(f"{f[0]/T:.5f}" for f in frames)
b=['<text class="h" x="20" y="24">Same Straight, different Turn</text>']
b.append('<rect x="20" y="36" width="450" height="306" rx="10" fill="#FFFFFF" stroke="#ADB5BD" stroke-width="2"/>')
b.append('<text class="sm" x="460" y="334" text-anchor="end">whiteboard panel, drawn to scale</text>')
b.append(f'<path d="M {SX-12} {SY} h 24 M {SX} {SY-12} v 24" stroke="#ADB5BD" stroke-width="2"/>')
anim=[]
for i,(s0,s1,tu,l,r,Rcm,dur) in enumerate(segs):
    a,e,pts,L=trails[i]
    pp=' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)
    anim.append(f'<g opacity="0">{vis(s0,s1)}<polyline points="{pp}" fill="none" stroke="#1F6FEB" stroke-width="3.5" stroke-linecap="round" stroke-dasharray="{L:.0f} {L+20:.0f}"><animate attributeName="stroke-dashoffset" values="{L:.0f};{L:.0f};0;0" keyTimes="0;{a/T:.5f};{e/T:.5f};1" {DUR}/></polyline>'
                f'<g transform="translate({icc[i][0]:.1f} {icc[i][1]:.1f})"><circle r="7" fill="#FFFFFF" stroke="#7B4FA0" stroke-width="2.6"/><path d="M -11 0 h 22 M 0 -11 v 22" stroke="#7B4FA0" stroke-width="2"/><circle r="2.5" fill="#7B4FA0"/></g></g>')
trs=";".join(f"{f[1]:.1f} {f[2]:.1f}" for f in frames); ros=";".join(f"{f[3]:.1f}" for f in frames)
anim.append(f'<g opacity="0.9"><animateTransform attributeName="transform" type="translate" values="{trs}" keyTimes="{keys}" {DUR}/><g><animateTransform attributeName="transform" type="rotate" values="{ros}" keyTimes="{keys}" {DUR}/><use href="#pcXRP" transform="scale({S:.3f})"/></g></g>')
X=490
b.append(f'<text class="h" x="{X}" y="60">The Arcade block</text>')
anim.append(f'<g opacity="0">{first(segs[0][0])}<text class="sm" x="{X}" y="86">Straight stays at 0.5.</text><text class="sm" x="{X}" y="102">Press a Turn value to</text><text class="sm" x="{X}" y="118">drive one full circle.</text></g>')
def ebar(y,label,val,col):
    w=58*abs(val); x0=X+73 if val>=0 else X+73-w
    return (f'<text class="nb" x="{X}" y="{y+13}">{label}</text><rect x="{X+15}" y="{y}" width="116" height="18" rx="4" fill="#E9ECEF" stroke="#ADB5BD"/>'
            f'<line x1="{X+73}" y1="{y-3}" x2="{X+73}" y2="{y+21}" stroke="#495057" stroke-width="1.5"/>'
            f'<rect x="{x0:.1f}" y="{y+3}" width="{w:.1f}" height="12" rx="3" fill="{col}"/><text class="ms" x="{X+137}" y="{y+13}">{val:+.2f}</text>')
for (s0,s1,tu,l,r,Rcm,dur) in segs:
    anim.append(f'<g opacity="0">{vis(s0,s1)}<text class="m" x="{X}" y="88">Straight 0.5  Turn {tu}</text>'
                f'<text class="sm" x="{X}" y="114">wheel efforts it works out:</text>'
                +ebar(126,"L",l,"#D1182C")+ebar(154,"R",r,"#D1182C")+
                f'<text class="sm" x="{X+15}" y="190">back</text><text class="sm" x="{X+73}" y="190" text-anchor="middle">0</text><text class="sm" x="{X+131}" y="190" text-anchor="end">forward</text>'
                f'<text class="nb" x="{X}" y="222">Circle: about {round(2*Rcm/5)*5:.0f} cm across</text>'
                f'<text class="sm" x="{X}" y="240">{"the left (inside) wheel runs backward" if l<0 else ("the left (inside) wheel stops" if abs(l)<1e-6 else "the left (inside) wheel runs slower")}</text></g>')
b+= [f'<text class="sm" x="{X}" y="282">Purple: the point it circles.</text>',
     f'<text class="sm" x="{X}" y="298">More Turn means a bigger gap</text>',
     f'<text class="sm" x="{X}" y="314">between the wheels, so a</text>',
     f'<text class="sm" x="{X}" y="330">tighter circle.</text>']
b.append('<g>'+''.join(anim)+'</g>')
modes=[{"label":f"Turn {s[2]}","start":round(s[0],3),"stop":round(s[1],3)} for s in segs]
o=svg('Arcade circles: same Straight, different Turn',
 'An animation of an XRP seen from above on a whiteboard panel, drawn to scale, with a marker in the hole between its wheels. Four buttons run Arcade with Straight 0.5 and Turn 0.15, 0.3, 0.5 or 0.8. Each drives one full circle from the same starting mark and draws it in blue, with a purple target at the point it circles, and a panel shows the two wheel efforts Arcade works out. Positive Turn bends left. Turn 0.15: both wheels forward, the left one slower, a circle about 50 cm across. Turn 0.3: about 25 cm across. Turn 0.5: the left wheel stops and the robot swings around it, about 15 cm across. Turn 0.8: the left wheel runs backward and the circle is about 10 cm across, smaller than the robot.',b,W=680,H=350)
o=o.replace('<svg xmlns="http://www.w3.org/2000/svg"',"<svg xmlns=\"http://www.w3.org/2000/svg\" data-modes='"+json.dumps(modes)+"'",1)
open(OUTDIR+'arcade-circles.svg','w').write(o)
print([ (s[2],round(s[3],3),round(s[4],3),round(2*s[5],1),round(s[6],1)) for s in segs], round(T,1))
