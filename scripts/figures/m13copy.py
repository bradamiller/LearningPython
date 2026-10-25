import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
# Lesson 1-3: why a function -- change the side length in a copy-pasted program vs. in a function.
from common import *
GREEN,GREEN_D="#5BA55B","#3F7D3F"; BLUE,BLUE_D="#4C97FF","#3373CC"; PURP,PURP_D="#885498","#6A4377"
T=14.0
DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
def vis(a,b=None):
    b=T if b is None else b
    return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{max(a/T,0.0001):.4f};{min(b/T,0.9999):.4f}" calcMode="discrete" {DUR}/>'
def until(b): return f'<animate attributeName="opacity" values="1;0" keyTimes="0;{b/T:.4f}" calcMode="discrete" {DUR}/>'
def flash(a): return f'<animate attributeName="opacity" values="0;0;1;0;0" keyTimes="0;{a/T:.4f};{(a+0.15)/T:.4f};{(a+1.0)/T:.4f};1" {DUR}/>'
b=[]; anim=[]
def stack(x,y,label,val_t,w=170):
    """a Straight block with a cm field whose value changes at val_t (None: never)"""
    o=f'<rect x="{x}" y="{y}" width="{w}" height="22" rx="4" fill="{BLUE}" stroke="{BLUE_D}"/><text class="nb" x="{x+8}" y="{y+15}" style="fill:#FFFFFF">Straight  cm:</text>'
    fx=x+104
    o+=f'<rect x="{fx}" y="{y+3}" width="34" height="16" rx="8" fill="#FFFFFF"/>'
    if val_t is None:
        o+=f'<text class="ms" x="{fx+17}" y="{y+15}" text-anchor="middle">30</text>'
    else:
        anim.append(f'<g opacity="0">{until(val_t)}<text class="ms" x="{fx+17}" y="{y+15}" text-anchor="middle">30</text></g>')
        anim.append(f'<g opacity="0">{vis(val_t)}<text class="ms" x="{fx+17}" y="{y+15}" text-anchor="middle" style="fill:#D1182C;font-weight:700">40</text></g>')
        anim.append(f'<g opacity="0">{flash(val_t)}<rect x="{fx-4}" y="{y-1}" width="42" height="24" rx="10" fill="none" stroke="#F2B705" stroke-width="3"/></g>')
    return o
def turn(x,y,w=170):
    return f'<rect x="{x}" y="{y}" width="{w}" height="22" rx="4" fill="{BLUE}" stroke="{BLUE_D}"/><text class="nb" x="{x+8}" y="{y+15}" style="fill:#FFFFFF">Turn  Deg:</text><rect x="{x+104}" y="{y+3}" width="34" height="16" rx="8" fill="#FFFFFF"/><text class="ms" x="{x+121}" y="{y+15}" text-anchor="middle">90</text>'
def repeat(x,y,val_t,w=200):
    pts=[(x,y),(x+w,y),(x+w,y+26),(x+16,y+26),(x+16,y+76),(x+w*0.6,y+76),(x+w*0.6,y+88),(x,y+88)]
    o=(f'<polygon points="{" ".join(f"{a:.0f},{c:.0f}" for a,c in pts)}" fill="{GREEN}" stroke="{GREEN_D}" stroke-linejoin="round"/>'
       f'<text class="nb" x="{x+8}" y="{y+17}" style="fill:#FFFFFF">repeat 4 times</text>')
    o+=stack(x+18,y+28,"",val_t)+turn(x+18,y+52)
    return o, 92
# ---- left: copy-paste
LX=34
b.append('<text class="h" x="20" y="26">Copy-paste</text>')
b.append('<rect x="20" y="36" width="310" height="306" rx="10" fill="#F8F9FA" stroke="#DEE2E6"/>')
y=48; edits=[3.2,4.4,None]
for i,et in enumerate(edits):
    o,hgt=repeat(LX,y,et); b.append(o)
    b.append(f'<text class="sm" x="{LX+214}" y="{y+18}">square #{i+1}</text>')
    if et is None:
        anim.append(f'<g opacity="0">{vis(5.6)}<circle cx="{LX+18+121}" cy="{y+28+11}" r="20" fill="none" stroke="#D1182C" stroke-width="3"/><text class="nb" x="{LX+214}" y="{y+44}" style="fill:#D1182C">missed</text><text class="nb" x="{LX+214}" y="{y+60}" style="fill:#D1182C">this one</text></g>')
    y+=hgt+6
# ---- right: function
RX=364
b.append('<text class="h" x="350" y="26">A function</text>')
b.append('<rect x="350" y="36" width="310" height="306" rx="10" fill="#F8F9FA" stroke="#DEE2E6"/>')
dy=48
pts=[(RX,dy),(RX+220,dy),(RX+220,dy+26),(RX+14,dy+26),(RX+14,dy+122),(RX+130,dy+122),(RX+130,dy+134),(RX,dy+134)]
b.append(f'<polygon points="{" ".join(f"{a:.0f},{c:.0f}" for a,c in pts)}" fill="{PURP}" stroke="{PURP_D}" stroke-linejoin="round"/>'
         f'<text class="nb" x="{RX+8}" y="{dy+17}" style="fill:#FFFFFF">to square</text>')
o,_=repeat(RX+14,dy+30,3.2,w=196); b.append(o)
b.append(f'<text class="sm" x="{RX+228}" y="{dy+17}">defined</text><text class="sm" x="{RX+228}" y="{dy+31}">once</text>')
cy=dy+148
b.append(f'<rect x="{RX}" y="{cy}" width="150" height="22" rx="4" fill="#E6A23C" stroke="#B27A20"/><text class="nb" x="{RX+8}" y="{cy+15}" style="fill:#FFFFFF">Wait for button press</text>')
for k in range(3):
    yy=cy+26+k*26
    b.append(f'<rect x="{RX}" y="{yy}" width="74" height="22" rx="4" fill="{PURP}" stroke="{PURP_D}"/><text class="nb" x="{RX+10}" y="{yy+15}" style="fill:#FFFFFF">square</text>')
    # arrow from call up to the definition
    ax=RX+82; d=f'M {ax} {yy+11} C {ax+150-k*8} {yy+11}, {RX+270} {dy+110}, {RX+234} {dy+80}'
    b.append(f'<path d="{d}" fill="none" stroke="#ADB5BD" stroke-width="1.6" stroke-dasharray="4 4" marker-end="url(#aG)"/>')
    anim.append(f'<g opacity="0">{flash(3.6+k*0.25)}<path d="{d}" fill="none" stroke="#D1182C" stroke-width="2.4" marker-end="url(#aR)"/></g>')
b.append(f'<text class="sm" x="{RX+82}" y="{cy+110}">called three times</text>')
# ---- the change, and what the robot draws
anim.append(f'<g opacity="0">{until(2.6)}<text class="nb" x="340" y="364" text-anchor="middle">Both programs draw three 30 cm squares.</text></g>')
anim.append(f'<g opacity="0">{vis(2.6,7.0)}<text class="nb" x="340" y="364" text-anchor="middle" style="fill:#D1182C">Change of plan: make the squares 40 cm.</text></g>')
anim.append(f'<g opacity="0">{vis(7.0)}<text class="nb" x="340" y="364" text-anchor="middle">What the robot draws now</text></g>')
def squares(cx,sizes,col):
    o=''
    for s in sorted(set(sizes),reverse=True):
        p=s*1.25; o+=f'<rect x="{cx-p:.0f}" y="{410-p:.0f}" width="{p:.0f}" height="{p:.0f}" fill="none" stroke="{col}" stroke-width="3"/>'
    return o
anim.append(f'<g opacity="0">{vis(7.6)}{squares(200,[40,40,30],"#1F6FEB")}<text class="sm" x="210" y="384">two 40 cm squares</text><text class="sm" x="210" y="399" style="fill:#D1182C;font-weight:700">and one 30 cm square</text></g>')
anim.append(f'<g opacity="0">{vis(7.6)}{squares(520,[40,40,40],"#1F6FEB")}<text class="sm" x="530" y="384">three 40 cm squares,</text><text class="sm" x="530" y="399">drawn on top of each other</text></g>')
anim.append(f'<g opacity="0">{vis(3.2,7.0)}<text class="sm" x="175" y="364" text-anchor="middle"> </text></g>')
b.append('<g class="anim">'+''.join(anim)+'</g>')
still=f'<text class="nb" x="340" y="364" text-anchor="middle">Change 30 to 40: three edits on the left, one on the right.</text>'
b.append(f'<g class="still">{still}</g>')
style_extra='<style>.still{display:none} @media (prefers-reduced-motion: reduce){.anim{display:none}.still{display:inline}}</style>'
out=svg('Copy-paste versus a function',
 'An animation comparing two Blockly programs that each draw three 30 cm squares. On the left, copy-paste: three identical Repeat 4 times loops, each with Straight cm 30 and Turn 90. On the right, a function: one definition, to square, holding the same loop, and a main program of Wait for button press and three square call blocks, with arrows from each call to the definition. Then the plan changes: make the squares 40 cm. On the left the 30 is changed to 40 in the first loop, then the second, and the third is missed, circled in red. On the right the 30 is changed once, in the definition, and the arrows light up from all three calls. Below, what each robot now draws: the copy-paste program draws two 40 cm squares and one 30 cm square; the function program draws three 40 cm squares on top of each other.',b,H=420)
out=out.replace('<rect width="680"',style_extra+'\n  <rect width="680"',1)
open(OUTDIR+'copy-paste-vs-function.svg','w').write(out); print('ok')
