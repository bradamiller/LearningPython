import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from common import *
b=[]
def box(x,y,w,h,title,sub,stroke="#22527B",fill="#FFFFFF",op=1):
    return [f'<g opacity="{op}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.8"/>',
            f'<text class="m" x="{x+w/2}" y="{y+22}" text-anchor="middle">{title}</text>',
            f'<text class="sm" x="{x+w/2}" y="{y+40}" text-anchor="middle">{sub}</text></g>']
def arrow(x1,y,x2,label=None,color="#495057"):
    o=[f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color}" stroke-width="2" marker-end="url(#aG)"/>']
    if label: o.append(tag((x1+x2)/2,y-16,label,fill="#F1F3F5",stroke="#ADB5BD"))
    return o
# Row 1: without raise
b.append('<text class="h" x="12" y="24">Without the raise</text>')
b+=box(12,40,190,52,"desired_heading()","(1, 1) to (2, 2): no match")
b+=arrow(204,66,268,"None")
b+=box(272,40,190,52,"turn_to(heading, None)","perfectly correct code")
b+=arrow(464,66,500)
b.append('<rect x="504" y="40" width="164" height="52" rx="8" fill="#FBE3E6" stroke="#D1182C" stroke-width="1.8"/>')
b.append('<text class="m" x="586" y="62" text-anchor="middle" style="fill:#D1182C">TypeError</text>')
b.append('<text class="sm" x="586" y="80" text-anchor="middle">NoneType and int</text>')
b.append('<path d="M 586 94 C 586 130, 107 130, 107 96" fill="none" stroke="#D1182C" stroke-width="1.6" stroke-dasharray="5 4" marker-end="url(#aR)"/>')
b.append('<text class="n" x="346" y="140" text-anchor="middle" style="fill:#D1182C">The error points at turn_to(). The mistake was back here.</text>')
# Row 2: with raise
b.append('<text class="h" x="12" y="184">With the raise</text>')
b+=box(12,200,190,52,"desired_heading()","(1, 1) to (2, 2): no match",stroke="#2E7D32")
b+=arrow(204,226,240)
b.append('<rect x="244" y="200" width="250" height="52" rx="8" fill="#FBE3E6" stroke="#D1182C" stroke-width="1.8"/>')
b.append('<text class="m" x="369" y="221" text-anchor="middle" style="fill:#D1182C">ValueError</text>')
b.append('<text class="sm" x="369" y="239" text-anchor="middle">(1, 1) and (2, 2) are not one step apart</text>')
b+=box(512,200,156,52,"turn_to()","never runs",stroke="#ADB5BD",op=0.45)
b.append('<text class="n" x="346" y="282" text-anchor="middle" style="fill:#2E7D32">The program stops on the line that noticed, and names both positions.</text>')
open(OUTDIR+'raise.svg','w').write(svg('Where the error shows up, with and without raise',
 'Two rows. Without the raise: desired_heading is asked for the heading from (1, 1) to (2, 2), matches none of its four cases, and silently returns None; turn_to receives None and fails with a TypeError about NoneType and int, so the error points at turn_to, which is correct code, while the mistake was back in the call to desired_heading. With the raise: desired_heading stops immediately with a ValueError saying (1, 1) and (2, 2) are not one step apart, and turn_to never runs.',b,H=296))
