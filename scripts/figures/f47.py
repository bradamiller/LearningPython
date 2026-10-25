import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math; from common import *
def pt(cx,cy,r,a): a=math.radians(a); return (cx+r*math.sin(a), cy-r*math.cos(a))
# ---------- headings ----------
b=[]; cx,cy=190,182; D=96
b.append(f'<rect x="20" y="20" width="340" height="324" rx="8" fill="#F3F4F6" stroke="#DEE2E6"/>')
b.append(f'<rect x="{cx-4.5}" y="20" width="9" height="324" fill="#2B2B2B"/><rect x="20" y="{cy-4.5}" width="340" height="9" fill="#2B2B2B"/>')
b.append(f'<use href="#pcXRP" transform="translate({cx} {cy}) scale(0.42)"/>')
# clockwise arcs between directions
for a0 in (0,90,180,270):
    p0=pt(cx,cy,62,a0+14); p1=pt(cx,cy,62,a0+76)
    b.append(f'<path d="M {p0[0]:.1f} {p0[1]:.1f} A 62 62 0 0 1 {p1[0]:.1f} {p1[1]:.1f}" fill="none" stroke="#4C8BF5" stroke-width="3" marker-end="url(#aB)"/>')
    m=pt(cx,cy,80,a0+45); b.append(f'<text class="nb" x="{m[0]:.1f}" y="{m[1]+4:.1f}" text-anchor="middle" style="fill:#22527B">+1</text>')
dirs=[("N",0,"y + 1",0),("E",1,"x + 1",90),("S",2,"y − 1",180),("W",3,"x − 1",270)]
for L,n,ch,a in dirs:
    x,y=pt(cx,cy,D+30,a)
    b.append(f'<circle cx="{pt(cx,cy,D+30,a)[0] if False else pt(cx,cy,D+30-0,a)[0]:.1f}" cy="{y:.1f}" r="0"/>')
    px,py=pt(cx,cy,118,a)
    w=74; h=40
    if a in (90,270): px=cx+(1 if a==90 else -1)*120
    b.append(f'<rect x="{px-w/2:.1f}" y="{py-h/2:.1f}" width="{w}" height="{h}" rx="7" fill="#FFFFFF" stroke="#22527B" stroke-width="1.6"/>')
    b.append(f'<text class="nb" x="{px:.1f}" y="{py-3:.1f}" text-anchor="middle"><tspan style="font-size:15px">{L}</tspan> = {n}</text>')
    b.append(f'<text class="ms" x="{px:.1f}" y="{py+13:.1f}" text-anchor="middle">{ch}</text>')
X=385
b+=[f'<text class="h" x="{X}" y="52">Heading as a number</text>',
    f'<text class="n" x="{X}" y="74">0 = N, 1 = E, 2 = S, 3 = W, counted</text>',
    f'<text class="n" x="{X}" y="91">clockwise. Each clockwise turn adds 1;</text>',
    f'<text class="n" x="{X}" y="108">past 3 it wraps back to 0, like an</text>',
    f'<text class="n" x="{X}" y="125">odometer rolling over.</text>',
    f'<text class="h" x="{X}" y="170">Which way is the next step?</text>',
    f'<text class="n" x="{X}" y="192">Between neighbors only x <tspan font-weight="700">or</tspan> y</text>',
    f'<text class="n" x="{X}" y="209">changes, by one. The change</text>',
    f'<text class="n" x="{X}" y="226">names the direction (the cards).</text>',
    f'<text class="h" x="{X}" y="272">(0, 0) is the near corner</text>',
    f'<text class="n" x="{X}" y="294">North is away from you, up the page,</text>',
    f'<text class="n" x="{X}" y="311">so y + 1 is North and x + 1 is East.</text>']
open(OUTDIR+'headings.svg','w').write(svg('Headings as numbers 0 to 3',
 'The robot at an intersection facing north, with a card at each neighbor. North is heading 0, y goes up by 1. East is 1, x goes up by 1. South is 2, y goes down by 1. West is 3, x goes down by 1. Curved arrows between them, each marked +1, show that every clockwise turn adds 1, wrapping from 3 back to 0. (0, 0) is the corner nearest you and north is away from you, so y plus 1 is north and x plus 1 is east.',b,H=360))
# ---------- short way ----------
b=[]
def panel(x0,title,ok):
    cx,cy=x0+150,140
    o=[f'<text class="h" x="{x0}" y="24">{title}</text>',
       f'<rect x="{x0}" y="36" width="300" height="200" rx="8" fill="#F3F4F6" stroke="#DEE2E6"/>',
       f'<rect x="{cx-4.5}" y="36" width="9" height="200" fill="#2B2B2B"/><rect x="{x0}" y="{cy-4.5}" width="300" height="9" fill="#2B2B2B"/>',
       f'<use href="#pcXRP" transform="translate({cx} {cy}) rotate(90) scale(0.42)" opacity="0.45"/>',
       f'<use href="#pcXRP" transform="translate({cx} {cy}) rotate(180) scale(0.42)"/>']
    r=70
    if ok:
        p0=pt(cx,cy,r,172); p1=pt(cx,cy,r,98)
        o.append(f'<path d="M {p0[0]:.1f} {p0[1]:.1f} A {r} {r} 0 0 0 {p1[0]:.1f} {p1[1]:.1f}" fill="none" stroke="#2E7D32" stroke-width="4" marker-end="url(#aGr)"/>')
        o.append(f'<text class="nb" x="{x0+150}" y="258" text-anchor="middle" style="fill:#2E7D32">1 counterclockwise turn: 90° ✓</text>')
    else:
        for a0,a1 in ((188,262),(278,352),(368,442)):
            p0=pt(cx,cy,r,a0); p1=pt(cx,cy,r,a1)
            o.append(f'<path d="M {p0[0]:.1f} {p0[1]:.1f} A {r} {r} 0 0 1 {p1[0]:.1f} {p1[1]:.1f}" fill="none" stroke="#D1182C" stroke-width="4" stroke-dasharray="7 4" marker-end="url(#aR)"/>')
        o.append(f'<text class="nb" x="{x0+150}" y="258" text-anchor="middle" style="fill:#D1182C">3 clockwise turns: 270° ✗</text>')
    o.append(f'<text class="sm" x="{x0+10}" y="54">facing S (2), wants E (1)</text>')
    return o
b+=panel(20,"The long way round",False)+panel(360,"The short way round",True)
b+=['<text class="ms" x="340" y="290" text-anchor="middle" style="font-size:12.5px">turns = (desired − heading) % 4 = (1 − 2) % 4 = 3</text>',
    '<text class="n" x="340" y="312" text-anchor="middle">Same finish, a quarter of the spinning: when the answer is 3, turn counterclockwise once.</text>']
open(OUTDIR+'short-way.svg','w').write(svg('Three clockwise turns or one counterclockwise',
 'Two drawings of the robot at an intersection facing south, needing to face east (shown faded). Left, the long way round: three dashed clockwise quarter turns, 270 degrees. Right, the short way round: one counterclockwise quarter turn, 90 degrees. Below: turns = (desired − heading) % 4 = (1 − 2) % 4 = 3; same finish, a quarter of the spinning: when the answer is 3, turn counterclockwise once.',b,H=326))
