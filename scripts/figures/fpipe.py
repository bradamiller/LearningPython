import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from common import *
b=[]
def box(x,y,w,h,head,code,sub,stroke,fill):
    return [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="2"/>',
            f'<text class="h" x="{x+w/2}" y="{y+24}" text-anchor="middle">{head}</text>',
            f'<text class="ms" x="{x+w/2}" y="{y+46}" text-anchor="middle">{code}</text>',
            f'<text class="sm" x="{x+w/2}" y="{y+66}" text-anchor="middle">{sub}</text>']
b+=box(12,40,236,80,"The planner","compute_manhattan_path()","plans the route; never drives","#22527B","#F1F6FB")
b+=box(432,40,236,80,"The driver","drive_path()","drives the route; never plans","#D1182C","#FDF2F3")
b.append('<line x1="250" y1="80" x2="428" y2="80" stroke="#495057" stroke-width="2.2" marker-end="url(#aG)"/>')
b.append(tag(340,62,"path",fill="#FFFFFF",stroke="#ADB5BD",cls="nb",w=50))
b.append('<text class="ms" x="340" y="102" text-anchor="middle">[(1,0), (2,0)]</text>')
b.append('<path d="M 550 122 C 550 190, 130 190, 130 124" fill="none" stroke="#495057" stroke-width="2.2" stroke-dasharray="6 4" marker-end="url(#aG)"/>')
b.append(tag(340,170,"position, heading",fill="#FFFFFF",stroke="#ADB5BD",cls="nb",w=150))
b.append('<text class="sm" x="340" y="196" text-anchor="middle">where the robot ended up, handed to the next plan</text>')
b.append('<text class="nb" x="130" y="24" text-anchor="middle">position, destination in</text>')
b.append('<line x1="130" y1="28" x2="130" y2="38" stroke="#495057" stroke-width="2" marker-end="url(#aG)"/>')
open(OUTDIR+'two-halves.svg','w').write(svg('The planner and the driver',
 'Two boxes. The planner, compute_manhattan_path(), takes a position and destination, plans the route and never drives. It hands a path, such as [(1,0), (2,0)], to the driver, drive_path(), which drives the route and never plans. The driver hands back position and heading, where the robot ended up, which go into the next plan.',b,H=212))
