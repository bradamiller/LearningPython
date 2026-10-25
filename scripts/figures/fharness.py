import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from common import *
b=[]
def card(x,y,w,h,head,body,stroke,fill):
    o=[f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.8"/>',
       f'<text class="nb" x="{x+12}" y="{y+22}">{head}</text>']
    for i,l in enumerate(body): o.append(f'<text class="ms" x="{x+12}" y="{y+42+i*16}">{l}</text>')
    return o
b+=card(12,20,300,78,"You, on paper → expected",["trace (0, 0) → (2, 3) by hand:","[(1,0), (2,0), (2,1), (2,2), (2,3)]"],"#C77C02","#FFF8E8")
b+=card(12,118,300,78,"The code → actual",["compute_manhattan_path(","    (0, 0), (2, 3))"],"#22527B","#F1F6FB")
b.append('<path d="M 314 59 C 350 59, 352 108, 380 108" fill="none" stroke="#495057" stroke-width="2" marker-end="url(#aG)"/>')
b.append('<path d="M 314 157 C 350 157, 352 112, 380 112" fill="none" stroke="#495057" stroke-width="2" marker-end="url(#aG)"/>')
b.append('<path d="M 440 64 L 498 110 L 440 156 L 382 110 Z" fill="#FFFFFF" stroke="#142D50" stroke-width="1.8"/>')
b.append('<text class="ms" x="440" y="106" text-anchor="middle">actual ==</text><text class="ms" x="440" y="122" text-anchor="middle">expected?</text>')
b.append('<line x1="498" y1="100" x2="528" y2="66" stroke="#2E7D32" stroke-width="2" marker-end="url(#aGr)"/>')
b.append('<line x1="498" y1="120" x2="528" y2="154" stroke="#D1182C" stroke-width="2" marker-end="url(#aR)"/>')
b+=card(532,38,140,46,"PASS",[],"#2E7D32","#E1F0E3")
b+=card(532,134,140,62,"FAIL",["print both lists"],"#D1182C","#FBE3E6")
b.append('<text class="n" x="12" y="226">The expected list has to come from your own trace. Copy it from the program\'s</text>')
b.append('<text class="n" x="12" y="243">output and the test only proves the program agrees with itself.</text>')
open(OUTDIR+'test-harness.svg','w').write(svg('Expected versus actual',
 'Two inputs meet at a comparison. Expected comes from you, on paper: tracing (0, 0) to (2, 3) by hand gives [(1,0), (2,0), (2,1), (2,2), (2,3)]. Actual comes from the code: compute_manhattan_path((0, 0), (2, 3)). If actual equals expected the test prints PASS; if not, FAIL, printing both lists. The expected list has to come from your own trace; copied from the program, the test only proves the program agrees with itself.',b,H=256))
