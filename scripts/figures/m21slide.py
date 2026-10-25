import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
# Lesson 2-1: test_sensors() printing while the robot is slid by hand across the tape.
import math; from common import *
S=0.85; LX=215.0; TW=13*S; SPOT=4*S; SY=-60*S; SX=6.5*S
ROBOT_Y=300
def cover(px):
    n=0
    for i in range(15):
        x=px-SPOT+2*SPOT*(i+0.5)/15; n+=abs(x-LX)<=TW/2
    return n/15
def readings(x): return 0.2+0.6*cover(x-SX)+0.01*math.sin(x*1.7), 0.2+0.6*cover(x+SX)+0.01*math.cos(x*1.3)
# path: start right of the tape, slide left across it, pause, slide back
PRINT=0.24                      # seconds of animation per printed line
path=[(LX+70,0.0)]
def leg(x1,dur):
    x0,t0=path[-1]; path.append((x1,t0+dur))
leg(LX+70,1.4); leg(LX+24,1.0); leg(LX-24,4.6); leg(LX-70,1.0); leg(LX-70,1.2)
leg(LX-24,1.0); leg(LX+24,4.6); leg(LX+70,1.0); leg(LX+70,1.4)
T=path[-1][1]
def xat(t):
    for (x0,t0),(x1,t1) in zip(path,path[1:]):
        if t0<=t<=t1: return x0+(x1-x0)*(t-t0)/(t1-t0) if t1>t0 else x1
    return path[-1][0]
prints=[]; t=0.0
while t<T-1e-6:
    l,r=readings(xat(t)); prints.append((t,l,r)); t+=PRINT
DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
def vis(a,b): return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{max(a/T,0.0001):.5f};{min(b/T,0.9999):.5f}" calcMode="discrete" {DUR}/>'
def first(b): return f'<animate attributeName="opacity" values="1;0" keyTimes="0;{b/T:.5f}" calcMode="discrete" {DUR}/>'
b=['<text class="h" x="20" y="26">Sliding the robot across the tape</text>']
b.append('<rect x="20" y="40" width="390" height="340" rx="10" fill="#F3F4F6" stroke="#DEE2E6"/>')
b.append(f'<rect x="{LX-TW/2:.1f}" y="40" width="{TW:.1f}" height="340" fill="#2B2B2B"/>')
b.append('<text class="sm" x="32" y="60">motors off: you slide the robot</text>')
b.append(f'<text class="sm" x="{LX+14}" y="372" style="font-weight:700">black tape</text>')
keys=";".join(f"{q/T:.5f}" for _,q in path); trs=";".join(f"{x:.1f} {ROBOT_Y}" for x,_ in path)
anim=[f'<g><animateTransform attributeName="transform" type="translate" values="{trs}" keyTimes="{keys}" {DUR}/><use href="#pcXRP" transform="scale({S})"/>'
      f'<text class="ax" x="{-SX-8:.1f}" y="{SY-12:.1f}" text-anchor="end" style="fill:#D1182C">L</text><text class="ax" x="{SX+8:.1f}" y="{SY-12:.1f}" style="fill:#D1182C">R</text></g>']
# hand-slide arrows
b.append(f'<path d="M {LX-60} 96 H {LX+60}" stroke="#ADB5BD" stroke-width="2" marker-start="url(#aG)" marker-end="url(#aG)"/>')
X=430; BY=48; NL=11; LH=19
b.append(f'<text class="h" x="{X}" y="34">The shell, as it prints</text>')
b.append(f'<rect x="{X-6}" y="{BY}" width="246" height="{NL*LH+18}" rx="8" fill="#FFFFFF" stroke="#ADB5BD"/>')
def line(i,l,r,y):
    def v(val): return f'<tspan style="fill:{"#142D50" if val>0.5 else "#6C757D"};font-weight:{700 if val>0.5 else 500}">{val:.2f}</tspan>'
    return f'<text class="ms" x="{X+4}" y="{y}">Left: {v(l)}   Right: {v(r)}</text>'
for k,(tk,l,r) in enumerate(prints):
    t1=prints[k+1][0] if k+1<len(prints) else T
    shown=prints[max(0,k-NL+1):k+1]
    inner=''.join(line(j,pl,pr,BY+22+j*LH) for j,(_,pl,pr) in enumerate(shown))
    anim.append(f'<g opacity="0">{vis(tk,t1) if tk>0 else first(t1)}{inner}</g>')
NY=BY+NL*LH+42
for i,ln in enumerate(["About 0.2 on the white floor, about 0.8","on the black tape. Each sensor climbs as","it moves onto the tape and drops as it","leaves, and the left one gets there first","on the way across."]):
    b.append(f'<text class="sm" x="{X-6}" y="{NY+i*15}">{ln}</text>')
b.append('<g class="anim">'+''.join(anim)+'</g>')
still=[f'<use href="#pcXRP" transform="translate({LX} {ROBOT_Y}) scale({S})"/>']
lc,rc=readings(LX)
still.append(line(0,0.21,0.20,BY+22)+line(1,lc,rc,BY+22+LH)+line(2,0.20,0.21,BY+22+2*LH))
b.append('<g class="still">'+''.join(still)+'</g>')
style_extra='<style>.still{display:none} @media (prefers-reduced-motion: reduce){.anim{display:none}.still{display:inline}}</style>'
out=svg('Sliding the robot across the tape',
 'An animation, close up and seen from above, of the Lesson 2-1 test. A strip of black tape runs up the picture. With the motors off, the robot is slid by hand from the right of the tape, across it to the left, and back again, while test_sensors() prints a line about every tenth of a second. Beside it, the shell scrolls those lines: Left and Right both about 0.20 on the white floor; as the robot crosses, the left sensor reaches the tape first and climbs to about 0.80 while the right still reads 0.20, then both read about 0.5 with the tape between them, then the right one reads 0.80 as the left one leaves, and both fall back to about 0.20 once the robot is past.',b,H=390)
out=out.replace('<rect width="680"',style_extra+'\n  <rect width="680"',1)
open(OUTDIR+'slide-across-tape.svg','w').write(out)
print(round(T,1),len(prints),[tuple(round(v,2) for v in readings(x)) for x in (LX+70,LX+SX,LX,LX-SX,LX-70)])
