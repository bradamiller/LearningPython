import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math; from common import *
S=0.85; LX=215.0; TW=6.5*2*S; SPOT=4*S; SY=-60*S; SX=6.5*S
CROSS_Y=118; CROSS_L=56
def cover(px,py):
    # fraction of a square spot of half-width SPOT at (px,py) on tape (vertical line or cross strip)
    def ov1(a,b,lo,hi): return max(0,min(b,hi)-max(a,lo))
    n=0; tot=0
    for i in range(9):
        for j in range(9):
            x=px-SPOT+2*SPOT*(i+0.5)/9; y=py-SPOT+2*SPOT*(j+0.5)/9
            on=abs(x-LX)<=TW/2 or (abs(y-CROSS_Y)<=TW/2 and abs(x-LX)<=CROSS_L/2)
            n+=on; tot+=1
    return n/tot
def readings(x,y):
    l=0.2+0.6*cover(x-SX,y+SY); r=0.2+0.6*cover(x+SX,y+SY); return l,r
frames=[]; t=0.0; samples=[]; labels=[]
x,y=LX+0.25,312.0
def add(): frames.append((t,x,y))
def hold(d):
    global t; samples.append((t,x,y)); t+=d; add()
def slide(nx,ny,d):
    global t,x,y
    x0,y0=x,y; n=max(4,int(d/0.1))
    for i in range(1,n+1):
        samples.append((t,x,y)); t+=d/n; x=x0+(nx-x0)*i/n; y=y0+(ny-y0)*i/n; add()
add()
s=t; hold(2.6); labels.append((s,t,"1. On the line","each sensor sits on an edge of the tape","#22527B"))
s=t; slide(LX+8,312,0.9); hold(2.4); labels.append((s,t,"2. Off to one side","only the left sensor is on the tape","#22527B"))
s=t; slide(LX+46,312,0.9); hold(2.4); labels.append((s,t,"3. Completely off","both sensors on white","#22527B"))
s=t; slide(LX+0.25,312,0.9); slide(LX+0.25,CROSS_Y-SY,2.4); hold(3.0); labels.append((s,t,"4. Slide along to the cross","Cross: False until both sensors reach it","#2E7D32"))
s=t; slide(LX+0.25,312,1.2); hold(0.4); T=t
labels.append((s,T,"Back to the start","","#6C757D"))
keys=";".join(f"{f[0]/T:.5f}" for f in frames)
tr=";".join(f"{f[1]:.1f} {f[2]:.1f}" for f in frames)
DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
def vis(t0,t1):
    a=max(t0/T,0.0001); b=min(t1/T,0.9999)
    return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{a:.5f};{b:.5f}" calcMode="discrete" {DUR}/>'
b=['<text class="h" x="20" y="26">Testing the toolkit by hand, close up</text>']
b.append('<rect x="20" y="40" width="390" height="350" rx="10" fill="#F3F4F6" stroke="#DEE2E6"/>')
b.append(f'<rect x="{LX-TW/2:.1f}" y="40" width="{TW:.1f}" height="350" fill="#2B2B2B"/>')
b.append(f'<rect x="{LX-CROSS_L/2:.1f}" y="{CROSS_Y-TW/2:.1f}" width="{CROSS_L}" height="{TW:.1f}" fill="#2B2B2B"/>')
b.append(f'<text class="sm" x="{LX-62}" y="{CROSS_Y+4}" text-anchor="end" style="font-weight:700">the cross</text>')
b.append(f'<text class="sm" x="{LX-14}" y="380" text-anchor="end" style="font-weight:700">a stretch of your circle&apos;s line</text>')
b.append(f'<text class="sm" x="32" y="58">motors off: you slide the robot</text>')
anim=[]; still=[]
anim.append(f'<g><animateTransform attributeName="transform" type="translate" values="{tr}" keyTimes="{keys}" {DUR}/>'
            f'<use href="#pcXRP" transform="scale({S})"/></g>')
X=430
b.append(f'<text class="h" x="{X}" y="60">What test_sensors() prints</text>')
BY=74
b.append(f'<rect x="{X-6}" y="{BY}" width="246" height="112" rx="8" fill="#F8F9FA" stroke="#ADB5BD"/>')
samples.append((T,x,y))
for i in range(len(samples)-1):
    t0,sx,sy=samples[i]; t1=samples[i+1][0]
    l,r=readings(sx,sy); e=l-r; on=l>0.5 or r>0.5; cr=l>0.5 and r>0.5
    def tf(v): return f'<tspan style="fill:{"#2E7D32" if v else "#D1182C"};font-weight:700">{v}</tspan>'
    anim.append(f'<g opacity="0">{vis(t0,t1)}'
      f'<text class="ms" x="{X+6}" y="{BY+22}">Left:  {l:.2f}</text>'
      f'<text class="ms" x="{X+6}" y="{BY+42}">Right: {r:.2f}</text>'
      f'<text class="ms" x="{X+6}" y="{BY+62}">Error: {e:+.2f}</text>'
      f'<text class="ms" x="{X+6}" y="{BY+82}">On line: {tf(on)}</text>'
      f'<text class="ms" x="{X+6}" y="{BY+102}">Cross:   {tf(cr)}</text></g>')
LBY=BY+128
for (t0,t1,ttl,sub,col) in labels:
    anim.append(f'<g opacity="0">{vis(t0,t1)}<rect x="{X-6}" y="{LBY}" width="246" height="54" rx="10" fill="#FFFFFF" stroke="{col}" stroke-width="2"/>'
                f'<text class="nb" x="{X+8}" y="{LBY+23}" style="fill:{col}">{ttl}</text><text class="sm" x="{X+8}" y="{LBY+42}">{sub}</text></g>')
NY=LBY+76
for i,ln in enumerate(["THRESHOLD is 0.5. On line asks whether","either reading is above it; Cross asks","whether both are. Only the cross makes","both readings high at once."]):
    b.append(f'<text class="sm" x="{X-6}" y="{NY+i*15}">{ln}</text>')
still.append(f'<use href="#pcXRP" transform="translate({LX} {CROSS_Y-SY}) scale({S})"/>')
still.append(f'<text class="ms" x="{X+6}" y="{BY+22}">Left:  0.80</text><text class="ms" x="{X+6}" y="{BY+42}">Right: 0.80</text><text class="ms" x="{X+6}" y="{BY+62}">Error: +0.00</text><text class="ms" x="{X+6}" y="{BY+82}">On line: True</text><text class="ms" x="{X+6}" y="{BY+102}">Cross:   True</text>')
b.append('<g class="anim">'+''.join(anim)+'</g>')
b.append('<g class="still">'+''.join(still)+'</g>')
style_extra='<style>.still{display:none} @media (prefers-reduced-motion: reduce){.anim{display:none}.still{display:inline}}</style>'
out=svg('Testing the toolkit by hand',
 'An animation, close up and seen from above, of the Lesson 2-7 activity. A stretch of the circle&apos;s tape runs up the picture, with the short cross strip across it near the top. With the motors off, the robot is slid by hand to four positions while a panel shows what test_sensors() prints. On the line, each sensor sits on an edge of the tape and reads about 0.5: on line True, cross False. Off to one side, only the left sensor is on the tape: left 0.80, right 0.20, error +0.60, on line True, cross False. Completely off the line, both read 0.20: both False. Then it is slid along the line to the cross: cross stays False until both sensors are on the strip, where both read 0.80 and both answers are True.',b,H=400)
out=out.replace('<rect width="680"',style_extra+'\n  <rect width="680"',1)
open(OUTDIR+'toolkit-by-hand.svg','w').write(out)
print(round(T,2)); 
for p in [(LX+0.25,312),(LX+8,312),(LX+46,312),(LX+0.25,CROSS_Y-SY)]: print([round(v,2) for v in readings(*p)])
