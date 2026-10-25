import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math; from common import *
def pt(cx,cy,r,a): a=math.radians(a); return (cx+r*math.sin(a), cy-r*math.cos(a))
# ---------- short way ----------
b=[]
def panel(x0,title,ok):
    cx,cy=x0+150,140
    o=[f'<text class="h" x="{x0}" y="24">{title}</text>',
       f'<rect x="{x0}" y="36" width="300" height="200" rx="8" fill="#F3F4F6" stroke="#DEE2E6"/>',
       f'<rect x="{cx-4.5}" y="36" width="9" height="200" fill="#2B2B2B"/><rect x="{x0}" y="{cy-4.5}" width="300" height="9" fill="#2B2B2B"/>',
       f'<use href="#pcXRP" transform="translate({cx} {cy}) rotate(0) scale(0.42)" opacity="0.45"/>',
       f'<use href="#pcXRP" transform="translate({cx} {cy}) rotate(90) scale(0.42)"/>']
    r=70
    if ok:
        p0=pt(cx,cy,r,82); p1=pt(cx,cy,r,8)
        o.append(f'<path d="M {p0[0]:.1f} {p0[1]:.1f} A {r} {r} 0 0 0 {p1[0]:.1f} {p1[1]:.1f}" fill="none" stroke="#2E7D32" stroke-width="4" marker-end="url(#aGr)"/>')
        o.append(f'<text class="nb" x="{x0+150}" y="258" text-anchor="middle" style="fill:#2E7D32">1 counterclockwise turn: 90° ✓</text>')
    else:
        for a0,a1 in ((98,172),(188,262),(278,352)):
            p0=pt(cx,cy,r,a0); p1=pt(cx,cy,r,a1)
            o.append(f'<path d="M {p0[0]:.1f} {p0[1]:.1f} A {r} {r} 0 0 1 {p1[0]:.1f} {p1[1]:.1f}" fill="none" stroke="#D1182C" stroke-width="4" stroke-dasharray="7 4" marker-end="url(#aR)"/>')
        o.append(f'<text class="nb" x="{x0+150}" y="258" text-anchor="middle" style="fill:#D1182C">3 clockwise turns: 270° ✗</text>')
    o.append(f'<text class="sm" x="{x0+10}" y="54">facing E (1), wants N (0)</text>')
    return o
b+=panel(20,"The loop: always clockwise",False)+panel(360,"Turning the short way",True)
b+=['<text class="n" x="340" y="296" text-anchor="middle">Same place, a third of the turning: three clockwise steps around the compass</text>',
    '<text class="n" x="340" y="314" text-anchor="middle">land where one counterclockwise turn does.</text>']
open(OUTDIR+'turn-shortcut.svg','w').write(svg('The long way and the short way round',
 'Two drawings of the robot at an intersection facing east, needing to face north (shown faded). Left, the loop alone, always clockwise: three dashed clockwise quarter turns, 270 degrees. Right, turning the short way: one counterclockwise quarter turn, 90 degrees. Same place, a third of the turning.',b,H=326))
