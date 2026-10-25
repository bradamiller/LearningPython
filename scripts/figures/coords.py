import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math; from common import *
g=G(92,66,sp=88,n=4,pad=36)
P=g.p
T=27.0
DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
def vis(t0,t1=None):
    t1=T if t1 is None else t1
    a=max(t0/T,0.0001); b=min(t1/T,0.9999)
    return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{a:.4f};{b:.4f}" calcMode="discrete" {DUR}/>'
b=['<text class="h" x="20" y="22">Naming the intersections</text>']
b+=g.base(axes=False,north=False)
L=3*g.sp; BOT=g.y0+L+g.pad
# you
b.append(f'<text class="nb" x="{g.x0+L/2}" y="{BOT+50}" text-anchor="middle">YOU stand here, at the near edge</text>')
b.append(f'<line x1="{g.x0+L/2}" y1="{BOT+36}" x2="{g.x0+L/2}" y2="{BOT+8}" stroke="#495057" stroke-width="2" marker-end="url(#aG)"/>')
anim=[]
def pill(x,y,text,col="#22527B",fill="#FFFFFF",w=None):
    w=w or len(text)*7.4+10
    return f'<rect x="{x-w/2:.1f}" y="{y-10:.1f}" width="{w:.1f}" height="20" rx="6" fill="{fill}" stroke="{col}" stroke-width="1.6"/><text class="ms" x="{x:.1f}" y="{y+4:.1f}" text-anchor="middle" style="fill:{col}">{text}</text>'
# stage times
S=[(0,3.0),(3.0,7.0),(7.0,11.0),(11.0,15.5),(15.5,20.0),(20.0,T)]
# stage 1: origin ring
x,y=P(0,0)
anim.append(f'<g opacity="0">{vis(0.3,3.0)}<circle cx="{x}" cy="{y}" r="16" fill="none" stroke="#D1182C" stroke-width="3.5"/></g>')
anim.append(f'<g opacity="0">{vis(0.8,20.0)}{pill(x,y,"(0, 0)","#D1182C")}</g>')
# stage 2: x labels
for i in range(4):
    tx,ty=P(i,0); t0=3.3+i*0.8
    anim.append(f'<g opacity="0">{vis(t0)}<text class="ax" x="{tx}" y="{BOT+16}" text-anchor="middle" style="fill:#22527B;font-size:14px">{i}</text></g>')
    if i>0: anim.append(f'<g opacity="0">{vis(t0,7.0)}<circle cx="{tx}" cy="{ty}" r="13" fill="none" stroke="#22527B" stroke-width="3"/></g>')
anim.append(f'<g opacity="0">{vis(6.2)}<text class="ax" x="{g.x0+L+g.pad+8}" y="{BOT+16}" style="fill:#22527B;font-size:13px">x →</text></g>')
# stage 3: y labels
for i in range(4):
    tx,ty=P(0,i); t0=7.3+i*0.8
    anim.append(f'<g opacity="0">{vis(t0)}<text class="ax" x="{g.x0-g.pad-10}" y="{ty+5}" text-anchor="end" style="fill:#22527B;font-size:14px">{i}</text></g>')
    if i>0: anim.append(f'<g opacity="0">{vis(t0,11.0)}<circle cx="{tx}" cy="{ty}" r="13" fill="none" stroke="#22527B" stroke-width="3"/></g>')
anim.append(f'<g opacity="0">{vis(10.2)}<text class="ax" x="{g.x0-g.pad-10}" y="{g.y0-g.pad+6}" text-anchor="end" style="fill:#22527B;font-size:13px">y ↑</text></g>')
# stages 4,5: walk to (2,3) and (3,2)
def walk(t0,a,bb,col,off):
    # marker: across then up; drawn arrows
    out=[]
    x0,y0=P(0,0); x1,y1=P(a,0); x2,y2=P(a,bb)
    lx0,ly0,lx1,ly1,lx2,ly2=x0,y0+off,x1+off,y1+off,x2+off,y2
    ta=t0+0.4; tb=ta+0.5*a; tc=tb+0.4; td=tc+0.5*bb
    out.append(f'<g opacity="0">{vis(ta,S[5][0])}<line x1="{lx0}" y1="{ly0}" x2="{lx1}" y2="{ly1}" stroke="{col}" stroke-width="5" stroke-linecap="round" opacity="0.8" stroke-dasharray="{x1-x0} 999" stroke-dashoffset="{x1-x0}"><animate attributeName="stroke-dashoffset" values="{x1-x0};{x1-x0};0;0" keyTimes="0;{ta/T:.4f};{tb/T:.4f};1" {DUR}/></line></g>')
    out.append(f'<g opacity="0">{vis(tc,S[5][0])}<line x1="{lx1}" y1="{ly1}" x2="{lx2}" y2="{ly2}" stroke="{col}" stroke-width="5" stroke-linecap="round" opacity="0.8" stroke-dasharray="{y1-y2} 999" stroke-dashoffset="{y1-y2}"><animate attributeName="stroke-dashoffset" values="{y1-y2};{y1-y2};0;0" keyTimes="0;{tc/T:.4f};{td/T:.4f};1" {DUR}/></line></g>')
    out.append(f'<g opacity="0">{vis(tb-0.1,S[5][0])}<text class="ms halo" x="{(x0+x1)/2}" y="{y0+(26 if off>0 else -12)}" text-anchor="middle" style="fill:{col}">across {a}</text></g>')
    out.append(f'<g opacity="0">{vis(td-0.1,S[5][0])}<text class="ms halo" x="{x2-12}" text-anchor="end" y="{P(a, bb/2 + (0.5 if bb%2==0 else 0))[1]+4}" style="fill:{col}">away {bb}</text></g>')
    out.append(f'<g opacity="0">{vis(td+0.1,S[5][0])}{pill(x2,y2,f"({a}, {bb})",col,"#FFFFFF")}</g>')
    return out
anim+=walk(11.0,2,3,"#D1182C",-5)
anim+=walk(15.5,3,2,"#2E7D32",5)
x,y=P(0,0); anim.append(f'<g opacity="0">{vis(0.8,20.0)}{pill(x,y,"(0, 0)","#D1182C")}</g>')
# stage 6: all labels
k=0
for yy in range(4):
    for xx in range(4):
        x,y=P(xx,yy); t0=20.2+k*0.22; k+=1
        anim.append(f'<g opacity="0">{vis(t0)}{pill(x,y,f"({xx}, {yy})")}</g>')
# panel
X=450
b.append(f'<text class="h" x="{X}" y="58">How to name a spot</text>')
STEPS=["(0, 0) is the corner nearest you","x counts across, to the right","y counts away from you","(2, 3): across 2, then away 3","(3, 2) is a different place","every intersection has a name"]
for i,(st,(a,c)) in enumerate(zip(STEPS,S)):
    yy=84+i*24
    b.append(f'<rect class="anim" x="{X-6}" y="{yy-16}" width="222" height="22" rx="4" fill="#FDECEE" stroke="#D1182C" stroke-width="1.2" opacity="0">{vis(a,c)}</rect>')
    b.append(f'<text class="n" x="{X}" y="{yy}"><tspan style="font-weight:700">{i+1}.</tspan> {st}</text>')
notes=[(0,3,"Count from zero, starting at","the corner closest to you."),
       (3,7,"x is the first number: how far","across from the left edge."),
       (7,11,"y is the second number: how far","away from the near edge."),
       (11,15.5,"Across first, then away, like a","graph in math class."),
       (15.5,20,"Same two numbers, other order:","another intersection entirely."),
       (20,T,"A 4 by 4 grid has 16 names,","(0, 0) up to (3, 3).")]
BY=84+6*24+4
for (a,c,l1,l2) in notes:
    anim.append(f'<g opacity="0">{vis(a,c)}<rect x="{X-6}" y="{BY}" width="222" height="54" rx="10" fill="#FFFFFF" stroke="#22527B" stroke-width="2"/>'
                f'<text class="n" x="{X+8}" y="{BY+22}">{l1}</text><text class="n" x="{X+8}" y="{BY+40}">{l2}</text></g>')
# still: all labels and axes
still=[]
for yy in range(4):
    for xx in range(4):
        x,y=P(xx,yy); still.append(pill(x,y,f"({xx}, {yy})"))
for i in range(4):
    still.append(f'<text class="ax" x="{P(i,0)[0]}" y="{BOT+16}" text-anchor="middle" style="fill:#22527B;font-size:14px">{i}</text>')
    still.append(f'<text class="ax" x="{g.x0-g.pad-10}" y="{P(0,i)[1]+5}" text-anchor="end" style="fill:#22527B;font-size:14px">{i}</text>')
b.append('<g class="anim">'+''.join(anim)+'</g>')
b.append('<g class="still">'+''.join(still)+'</g>')
style_extra='<style>.halo{paint-order:stroke;stroke:#FFFFFF;stroke-width:5px;stroke-linejoin:round} .still{display:none} @media (prefers-reduced-motion: reduce){.anim{display:none}.still{display:inline}}</style>'
out=svg('Naming the intersections',
 'An animation of a 4 by 4 grid of taped lines, seen from above, with you standing at the near (bottom) edge. First the bottom-left intersection, the one nearest you, is ringed and labeled (0, 0). Then x is counted 0, 1, 2, 3 along the bottom, left to right, and y is counted 0, 1, 2, 3 up the left side, away from you. Then a red line goes across 2 and away 3 to reach (2, 3), and a green line goes across 3 and away 2 to reach (3, 2), a different intersection. Finally every intersection is labeled in turn, from (0, 0) in the near corner to (3, 3) in the far corner. A panel beside it lists the six ideas, highlighting the one being shown.',b,H=460)
out=out.replace('<rect width="680"',style_extra+'\n  <rect width="680"',1)
open(OUTDIR+'naming-intersections.svg','w').write(out); print('ok')
