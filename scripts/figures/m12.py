import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math; from common import *
S=0.6; SIDE=150.0
CX,CY=205,222
x,y,h=CX+SIDE/2,CY+SIDE/2,0.0
frames=[]; t=0.0; labels=[]; trail=[(x,y)]; tr_t=[(0.0,0.0)]  # (time, cumulative length)
L=0.0
def add(): frames.append((t,x,y,h))
add(); t+=1.0; add(); labels.append((0,t,"Waiting for the button","Wait for button press, first block","#6C757D"))
t0=t; t+=0.4; add(); labels.append((t0,t,"Button pressed","now the blocks run, in order","#22527B"))
for k in range(4):
    t0=t; ux,uy=math.sin(math.radians(h)),-math.cos(math.radians(h)); n=20
    for i in range(1,n+1):
        t+=2.0/n; x+=ux*SIDE/n; y+=uy*SIDE/n; L+=SIDE/n; add(); tr_t.append((t,L))
    trail.append((x,y))
    labels.append((t0,t,f"Side {k+1} of 4","Straight: drive 20 cm","#22527B"))
    t0=t; t+=0.25; add(); tr_t.append((t,L))
    for i in range(1,11): t+=1.0/10; h-=9; add()
    t+=0.25; add(); tr_t.append((t,L))
    labels.append((t0,t,f"Corner {k+1} of 4","Turn: 90 degrees","#D1182C"))
t0=t; t+=2.8; add(); T=t
labels.append((t0,T,"Back where it started","same spot, facing the same way","#2E7D32"))
DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
def vis(a,b):
    return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{max(a/T,0.0001):.4f};{min(b/T,0.9999):.4f}" calcMode="discrete" {DUR}/>'
keys=";".join(f"{f[0]/T:.5f}" for f in frames)
trs=";".join(f"{f[1]:.1f} {f[2]:.1f}" for f in frames)
ros=";".join(f"{f[3]:.1f}" for f in frames)
b=['<text class="h" x="20" y="26">Where you are headed</text>']
b.append('<rect x="20" y="40" width="390" height="350" rx="10" fill="#F3F4F6" stroke="#DEE2E6"/>')
sx,sy=CX+SIDE/2,CY+SIDE/2
b.append(f'<path d="M {sx-14} {sy} h 28 M {sx} {sy-14} v 28" stroke="#ADB5BD" stroke-width="2"/>')
b.append(f'<text class="sm" x="{sx+30}" y="{sy+50}" style="font-weight:700">start</text>')
# 20 cm dimension along first side
b.append(f'<line x1="{sx+52}" y1="{sy}" x2="{sx+52}" y2="{sy-SIDE}" stroke="#6C757D" stroke-width="1.4" marker-start="url(#aG)" marker-end="url(#aG)"/><text class="sm" x="{sx+58}" y="{sy-SIDE/2+4}">20 cm</text>')
anim=[]
pts=' '.join(f'{p[0]:.1f},{p[1]:.1f}' for p in trail)
Ltot=4*SIDE
ks=";".join(f"{a/T:.5f}" for a,_ in tr_t)+";1"; vs=";".join(f"{Ltot-l:.1f}" for _,l in tr_t)+";0"
anim.append(f'<polyline points="{pts}" fill="none" stroke="#1F6FEB" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="{Ltot:.0f} {Ltot+20:.0f}"><animate attributeName="stroke-dashoffset" values="{vs}" keyTimes="{ks}" {DUR}/></polyline>')
anim.append(f'<g><animateTransform attributeName="transform" type="translate" values="{trs}" keyTimes="{keys}" {DUR}/><g><animateTransform attributeName="transform" type="rotate" values="{ros}" keyTimes="{keys}" {DUR}/><use href="#pcXRP" transform="scale({S})"/></g></g>')
X=436
b.append(f'<text class="h" x="{X}" y="60">The goal</text>')
for i,l in enumerate(["Four sides the same length,","four corners the same size,","and back to the start","facing the same way."]):
    b.append(f'<text class="n" x="{X}" y="{84+i*19}">{l}</text>')
LB=170
for (a,c,tx,sub,col) in labels:
    anim.append(f'<g opacity="0">{vis(a,c)}<rect x="{X-6}" y="{LB}" width="236" height="54" rx="10" fill="#FFFFFF" stroke="{col}" stroke-width="2"/><text class="nb" x="{X+8}" y="{LB+23}" style="fill:{col}">{tx}</text><text class="sm" x="{X+8}" y="{LB+42}">{sub}</text></g>')
# side tally
b.append(f'<text class="sm" x="{X}" y="{LB+80}">sides drawn</text>')
for k in range(4):
    tk=[l for l in labels if l[2]==f"Side {k+1} of 4"][0][1]
    bx=X+80+k*26
    b.append(f'<rect x="{bx}" y="{LB+68}" width="18" height="18" rx="4" fill="#FFFFFF" stroke="#ADB5BD"/>')
    anim.append(f'<g opacity="0">{vis(tk,T)}<rect x="{bx}" y="{LB+68}" width="18" height="18" rx="4" fill="#1F6FEB"/><path d="M {bx+4} {LB+77} l 4 4 l 7 -8" stroke="#FFFFFF" stroke-width="2.4" fill="none"/></g>')
for i,l in enumerate(["A marker in the hole between the","wheels draws the path as it drives."]):
    b.append(f'<text class="sm" x="{X}" y="{LB+116+i*15}">{l}</text>')
still=[f'<polyline points="{pts}" fill="none" stroke="#1F6FEB" stroke-width="4" stroke-linejoin="round"/>',f'<use href="#pcXRP" transform="translate({sx} {sy}) scale({S})"/>']
b.append('<g class="anim">'+''.join(anim)+'</g>')
b.append('<g class="still">'+''.join(still)+'</g>')
style_extra='<style>.still{display:none} @media (prefers-reduced-motion: reduce){.anim{display:none}.still{display:inline}}</style>'
out=svg('Where you are headed: a square',
 'An animation, seen from above, of an XRP robot on a plain floor carrying a marker in the hole between its wheels. It waits for the button, then drives straight 20 cm, stops, and turns 90 degrees in place, drawing a blue line as it goes. It does that four times, drawing a square, and ends back on its start mark facing the way it began. Beside it, the goal in words, a box naming each side and corner as it happens, and four check boxes that fill in as the sides are drawn.',b,H=400)
out=out.replace('<rect width="680"',style_extra+'\n  <rect width="680"',1)
open(OUTDIR+'square-goal.svg','w').write(out); print(round(T,1),SIDE)
