import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys,math; from common import *
g=G(110,100,sp=110,n=3,pad=36)
b=['<text class="h" x="12" y="24">Which intersection is blocked?</text>']
b+=[e for e in g.base(axes=True,north=False) if 'x →' not in e and 'y →' not in e]
x,y=g.p(1,0); bx,by=g.p(2,0)
b.append(f'<rect x="{bx-22}" y="{by-22}" width="44" height="44" rx="4" fill="#C8A26B" stroke="#7A5C2E" stroke-width="2"/><path d="M {bx-22} {by-6} H {bx+22}" stroke="#7A5C2E" stroke-width="1.5"/>')
b.append(f'<use href="#pcXRP" transform="translate({x} {y}) rotate(90) scale(0.55)"/>')
fx=x+0.55*68
for i,r in enumerate((14,26,38)):
    b.append(f'<path d="M {fx+r*0.6} {y-r*0.8} A {r} {r} 0 0 1 {fx+r*0.6} {y+r*0.8}" fill="none" stroke="#4C8BF5" stroke-width="2.4" opacity="{0.9-i*0.2}"/>')
b.append(tag(x-74,y-64,"position (1, 0)",fill="#F1F3F5",stroke="#868E96",w=110))
b.append(tag(bx-14,by-64,"next_pos (2, 0)",fill="#FBE3E6",stroke="#D1182C",w=114))
b.append('<text class="n" x="12" y="404">After turn_to(), the robot faces next_pos,</text>')
b.append('<text class="n" x="12" y="421">so a reading under OBSTACLE_CM means next_pos is blocked.</text>')
# distance scale
X0,X1,Y=420,660,170; scale=lambda cm:X0+(X1-X0)*cm/60
b.append('<text class="h" x="420" y="60">The reading, in cm</text>')
b.append(f'<line x1="{X0}" y1="{Y}" x2="{X1}" y2="{Y}" stroke="#495057" stroke-width="2"/>')
for cm in (0,30,45,60):
    b.append(f'<line x1="{scale(cm)}" y1="{Y-5}" x2="{scale(cm)}" y2="{Y+5}" stroke="#495057" stroke-width="1.5"/><text class="sm" x="{scale(cm)}" y="{Y+20}" text-anchor="middle">{cm}</text>')
b.append(f'<rect x="{X0}" y="{Y-34}" width="{scale(15)-X0}" height="24" fill="#FBE3E6" stroke="#D1182C" stroke-width="1.2"/><text class="sm" x="{(X0+scale(15))/2}" y="{Y-18}" text-anchor="middle" style="fill:#D1182C;font-weight:700">blocked</text>')
b.append(f'<rect x="{scale(15)}" y="{Y-34}" width="{X1-scale(15)}" height="24" fill="#E1F0E3" stroke="#2E7D32" stroke-width="1.2"/><text class="sm" x="{(scale(15)+X1)/2}" y="{Y-18}" text-anchor="middle" style="fill:#2E7D32;font-weight:700">clear</text>')
b.append(f'<line x1="{scale(15)}" y1="{Y-44}" x2="{scale(15)}" y2="{Y+30}" stroke="#142D50" stroke-width="2.4" stroke-dasharray="5 3"/><text class="ms" x="{scale(15)}" y="{Y+46}" text-anchor="middle">OBSTACLE_CM = 15</text>')
for cm,lab,col in ((12,"box at the next intersection: ~12","#D1182C"),(50,"nothing there: ~50","#2E7D32")):
    b.append(f'<circle cx="{scale(cm)}" cy="{Y}" r="6" fill="{col}"/>')
b.append(f'<text class="sm" x="{X0}" y="{Y+76}" style="fill:#D1182C">● ~12 cm: a box on the next intersection</text>')
b.append(f'<text class="sm" x="{X0}" y="{Y+94}" style="fill:#2E7D32">● ~50 cm: nothing there</text>')
b.append(f'<text class="sm" x="{X0}" y="{Y+120}">Measure yours; set the cutoff between them.</text>')
open(OUTDIR+'rangefinder-ahead.svg','w').write(svg('Reading the intersection ahead',
 'Left: the XRP parked on intersection (1, 0), its position, turned to face east toward (2, 0), next_pos, the intersection to its right, where a box sits; sound waves go from the rangefinder toward the box. After turn_to(), the robot faces next_pos, so a reading under OBSTACLE_CM means next_pos is blocked. Right: a distance scale from 0 to 60 cm with a dashed cutoff at OBSTACLE_CM = 15: below it is blocked, above it clear. A box on the next intersection reads about 12 cm; nothing there reads about 50 cm. Measure yours and set the cutoff between them.',b,H=434))
