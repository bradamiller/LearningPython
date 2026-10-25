import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math; import common
src=open(REPO+'/static/img/lesson-06/earth-moon-path.svg').read()
D=common.DEFS[common.DEFS.index('<g id="pcXRP"'):common.DEFS.index('</defs>')]
# keep only the pcXRP group
g=D[:D.index('</g>\n\n')+4] if '</g>\n\n' in D else D
L1=82*math.sqrt(2); ARC=116*1.5*math.pi; L2=164*math.sqrt(2)
segs=[(L1,"1 · Straight out to the Moon","measured: a Straight block"),(ARC,"2 · Swing around the Moon","timed: Arcade + Sleep, bending right"),
      (L2,"3 · Straight across to the Earth","measured: a Straight block"),(ARC,"4 · Swing around the Earth","timed: Arcade + Sleep, bending left"),
      (L1,"5 · Straight home to the start","measured: a Straight block")]
TOT=sum(s[0] for s in segs); SPEED=95.0; HOLD0=1.0; HOLD1=2.0
T=HOLD0+TOT/SPEED+HOLD1
DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
def vis(a,b): return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{max(a/T,0.0001):.4f};{min(b/T,0.9999):.4f}" calcMode="discrete" {DUR}/>'
path="M 340 150 L 422 68 A 116 116 0 1 1 422 232 L 258 68 A 116 116 0 1 0 258 232 L 340 150"
kt=f"0;{HOLD0/T:.4f};{(HOLD0+TOT/SPEED)/T:.4f};1"
robot=(f'<g><animateMotion path="{path}" rotate="auto" keyPoints="0;0;1;1" keyTimes="{kt}" calcMode="linear" {DUR}/>'
       f'<g transform="rotate(90) scale(0.36)"><use href="#pcXRP"/></g></g>')
labels=[]; t=HOLD0
labels.append(f'<g opacity="0">{vis(0,HOLD0)}<text class="seg" x="340" y="22" text-anchor="middle">Ready at the crossing</text></g>')
for (l,a,b) in segs:
    d=l/SPEED
    labels.append(f'<g opacity="0">{vis(t,t+d)}<text class="seg" x="340" y="22" text-anchor="middle">{a}</text><text class="segs" x="340" y="38" text-anchor="middle">{b}</text></g>')
    t+=d
labels.append(f'<g opacity="0">{vis(t,T)}<text class="seg" x="340" y="22" text-anchor="middle" style="fill:#2E7D32">Mission complete</text><text class="segs" x="340" y="38" text-anchor="middle">back at the crossing, pointing the way it started</text></g>')
out=src.replace('\n        marker-start="url(#way)"/>','/>')
assert 'marker-start' not in out
out=out.replace('viewBox="0 0 680 300"','viewBox="0 -10 680 310"',1)
out=out.replace('<title id="em2-title">The Earth–Moon–Earth flight path</title>','<title id="em2-title">The Earth–Moon–Earth mission, flown</title>')
out=out.replace('robot starts and finishes.</desc>','robot starts and finishes. In this animated version a small XRP flies the mission: straight out to the Moon, three-quarters of the way around it bending right, straight back across to the Earth, three-quarters of the way around it bending left, and straight home to the crossing, while a line at the top names each move and the block that drives it.</desc>')
out=out.replace('    .part { font-size: 12px;','    .seg { font-size: 13px; font-weight: 800; fill: #142D50; }\n    .segs { font-size: 11.5px; fill: #495057; }\n    .part { font-size: 12px;')
out=out.replace('  </defs>','    '+g+'\n  </defs>',1)
out=out.replace('</svg>','  '+''.join(labels)+'\n  '+robot+'\n</svg>')
open(OUTDIR+'earth-moon-mission.svg','w').write(out); print(round(T,1))
