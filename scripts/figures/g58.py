import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from common import *
BOX=[(2,0),(2,2),(3,1)]
run1=[(0,0),(1,0),(1,1),(2,1),(1,1),(1,2),(1,3),(2,3),(3,3)]
run2=[(0,0),(1,0),(1,1),(1,2),(1,3),(2,3),(3,3)]
def mp(x0,title,route,col,known,sub,rr=()):
    g=G(x0+44,74,sp=60,pad=26)
    o=[f'<text class="h" x="{x0}" y="24">{title}</text>',f'<text class="sm" x="{x0}" y="42">{sub}</text>']
    o+=[e for e in g.base(axes=False,north=False)]
    for q in BOX:
        x,y=g.p(*q); o.append(f'<rect x="{x-14}" y="{y-14}" width="28" height="28" rx="3" fill="#C8A26B" stroke="#7A5C2E" stroke-width="1.6"/>')
        if q in known: o.append(f'<text class="sm" x="{x}" y="{y+4}" text-anchor="middle" style="fill:#3B2A12;font-weight:700">known</text>'.replace('>known<','>✓<'))
    seen=set(); segs=[]
    for a,b2 in zip(route,route[1:]):
        key=frozenset((a,b2)); off=6 if key in seen else 0; seen.add(key)
        (x1,y1),(x2,y2)=g.p(*a),g.p(*b2)
        dx,dy=(x2-x1),(y2-y1); L=(dx*dx+dy*dy)**.5; nx,ny=-dy/L*off,dx/L*off
        o.append(f'<line x1="{x1+nx}" y1="{y1+ny}" x2="{x2+nx}" y2="{y2+ny}" stroke="{col}" stroke-width="6" stroke-linecap="round" opacity="0.85"/>')
        mx,my=(x1+x2)/2+nx,(y1+y2)/2+ny
        o.append(f'<line x1="{mx-dx/L*5}" y1="{my-dy/L*5}" x2="{mx+dx/L*4}" y2="{my+dy/L*4}" stroke="#FFFFFF" stroke-width="2.4" marker-end="url(#aW)"/>')
    for i,(p,n) in enumerate(rr):
        (x1,y1),(x2,y2)=g.p(*p),g.p(*n); mx,my=(x1*0.45+x2*0.55),(y1*0.45+y2*0.55)
        o.append(f'<circle cx="{mx}" cy="{my}" r="9" fill="#D1182C"/><text class="sm" x="{mx}" y="{my+4}" text-anchor="middle" style="fill:#FFFFFF;font-weight:700">{i+1}</text>')
    x,y=g.p(0,0); o.append(f'<circle cx="{x}" cy="{y}" r="10" fill="#142D50"/><text class="sm" x="{x}" y="{y+4}" text-anchor="middle" style="fill:#FFFFFF;font-weight:700">S</text>')
    x,y=g.p(3,3); o.append(f'<circle cx="{x}" cy="{y}" r="10" fill="#2E7D32"/><text class="sm" x="{x}" y="{y+4}" text-anchor="middle" style="fill:#FFFFFF;font-weight:700">D</text>')
    return o
b=[]
b+=mp(12,"Run 1: KNOWN_OBSTACLES = []",run1,"#C77C02",[],"finds each box when it faces it",rr=[((1,0),(2,0)),((2,1),(3,1)),((2,1),(2,2))])
b+=mp(352,"Run 2: the list typed in",run2,"#2E7D32",BOX,"plans around all three from the start")
b+=['<text class="nb" x="12" y="328" style="fill:#C77C02">8 steps, 3 reroutes (backs up once)</text>','<text class="nb" x="352" y="328" style="fill:#2E7D32">6 steps, 0 reroutes</text>',
    '<text class="n" x="340" y="358" text-anchor="middle">Same planner, same driving code. Only the blocked list it started with changed.</text>']
open(OUTDIR+'run1-run2.svg','w').write(svg('Run 1 and Run 2',
 'Two runs from S at (0, 0), the bottom-left, to D at (3, 3), the far top-right, with boxes at (2, 0), (2, 2) and (3, 1). Run 1 starts with an empty list and finds each box only when it faces it: it reroutes at (1, 0) on seeing (2, 0), then twice at (2, 1) on seeing (3, 1) and (2, 2), backs up to (1, 1), and goes up the column at x = 1 and right along the top row: 8 steps and 3 reroutes. Run 2 starts with the three boxes typed in and plans around them from the start, up the column at x = 1 and right along the top row: 6 steps and 0 reroutes. Same planner, same driving code; only the blocked list it started with changed.',b,H=370))
# loop flow
b=[]
def bx(x,y,w,h,t,s,col,fill):
    return [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{col}" stroke-width="1.8"/>',f'<text class="nb" x="{x+w/2}" y="{y+22}" text-anchor="middle">{t}</text>',f'<text class="ms" x="{x+w/2}" y="{y+40}" text-anchor="middle" style="font-size:11px">{s}</text>']
b+=bx(12,40,214,52,"Plan from here","compute_bfs_path(position, dest)","#22527B","#F1F6FB")
b.append('<line x1="228" y1="66" x2="242" y2="66" stroke="#495057" stroke-width="2" marker-end="url(#aG)"/>')
b+=bx(244,40,214,52,"Follow it, looking ahead","turn, look, track, drive past","#22527B","#F1F6FB")
b.append('<line x1="460" y1="66" x2="478" y2="66" stroke="#495057" stroke-width="2" marker-end="url(#aG)"/>')
b.append('<path d="M 560 30 L 640 66 L 560 102 L 480 66 Z" fill="#FFFFFF" stroke="#142D50" stroke-width="1.8"/><text class="nb" x="560" y="62" text-anchor="middle">something</text><text class="nb" x="560" y="78" text-anchor="middle">ahead?</text>')
b.append('<path d="M 560 104 L 560 140" stroke="#D1182C" stroke-width="2" marker-end="url(#aR)"/><text class="sm" x="568" y="126" style="fill:#D1182C;font-weight:700">yes</text>')
b+=bx(440,144,230,52,"Tell the planner","add_blocked(next_pos); rerouted","#D1182C","#FDF2F3")
b.append('<path d="M 440 170 C 300 170, 119 170, 119 96" fill="none" stroke="#D1182C" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#aR)"/>')
b.append('<text class="sm" x="290" y="194" text-anchor="middle" style="fill:#D1182C">break out of the for; the while plans again</text>')
b.append('<path d="M 642 66 L 668 66 L 668 236 L 560 236" fill="none" stroke="#2E7D32" stroke-width="2" marker-end="url(#aGr)"/><text class="sm" x="652" y="216" text-anchor="end" style="fill:#2E7D32;font-weight:700">no, every step</text>')
b+=bx(340,212,216,52,"Arrived","return position, heading, ...","#2E7D32","#F2F8F2")
b.append('<text class="n" x="20" y="232">The while ends only when a whole path was</text>')
b.append('<text class="n" x="20" y="249">followed with no reroute: that means arrived.</text>')
open(OUTDIR+'until-arrive.svg','w').write(svg('Drive until you arrive',
 'A loop. Plan from here with compute_bfs_path(position, dest). Follow it, looking ahead before each step: turn, look, track, drive past. If something is ahead: tell the planner with add_blocked(next_pos), set rerouted, break out of the for loop, and the while loop plans again from where the robot is. If every step was followed with nothing ahead, the robot has arrived and the function returns position, heading and the counts. The while ends only when a whole path was followed with no reroute.',b,H=280))
