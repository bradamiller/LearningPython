import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from common import *
b=[]
def box(x,y,w,h,t1,t2,stroke,fill,c1="m"):
    return [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.8"/>',
            f'<text class="{c1}" x="{x+w/2}" y="{y+21}" text-anchor="middle">{t1}</text>',f'<text class="sm" x="{x+w/2}" y="{y+39}" text-anchor="middle">{t2}</text>']
srcs=[("a paper test","Lesson 5-6"),("the rangefinder","Lesson 5-7"),("you, typing in","Lesson 5-8")]
for i,(a,c) in enumerate(srcs):
    y=40+i*66
    b+=box(12,y,150,48,a,c,"#ADB5BD","#F8F9FA",c1="nb")
    b.append(f'<path d="M 164 {y+24} C 200 {y+24}, 200 120, 226 120" fill="none" stroke="#495057" stroke-width="1.8" marker-end="url(#aG)"/>')
b+=box(230,96,150,48,"add_blocked(x)","appends once","#22527B","#F1F6FB")
b.append('<line x1="382" y1="120" x2="420" y2="120" stroke="#495057" stroke-width="2" marker-end="url(#aG)"/>')
b.append('<rect x="424" y="88" width="244" height="64" rx="10" fill="#FFF8E8" stroke="#C77C02" stroke-width="2"/>')
b.append('<text class="m" x="436" y="112">BLOCKED</text><text class="ms" x="436" y="134">[(2, 0), (2, 2)]</text>')
b.append('<text class="sm" x="546" y="80" text-anchor="middle">one list, top of GRID GRAPH</text>')
b.append('<path d="M 546 154 L 546 196" fill="none" stroke="#495057" stroke-width="2" marker-end="url(#aG)"/>')
b+=box(424,200,244,52,"compute_bfs_path()","builds the graph from BLOCKED every call","#2E7D32","#F2F8F2")
b.append('<text class="n" x="12" y="262">Every way of learning about a wall goes through the</text>')
b.append('<text class="n" x="12" y="279">same call, and every plan reads the list fresh, so a</text>')
b.append('<text class="n" x="12" y="296">wall found a moment ago is already out of the graph.</text>')
open(OUTDIR+'blocked-list.svg','w').write(svg('One blocked list, three ways in',
 'Three sources, a paper test in Lesson 5-6, the rangefinder in Lesson 5-7 and you typing in a list in Lesson 5-8, all call add_blocked(x), which appends to one list, BLOCKED, at the top of the GRID GRAPH section. compute_bfs_path() builds the graph from BLOCKED on every call, so a wall found a moment ago is already out of the graph.',b,H=310))
# append vs assign
b=[]
def panel(x0,title,code,ok):
    o=[f'<text class="h" x="{x0}" y="26">{title}</text>',f'<rect x="{x0}" y="38" width="310" height="34" rx="6" fill="#F8F9FA" stroke="#DEE2E6"/><text class="ms" x="{x0+10}" y="60">{code}</text>']
    o.append(f'<rect x="{x0}" y="96" width="98" height="34" rx="6" fill="#FFF8E8" stroke="#C77C02" stroke-width="1.6"/><text class="m" x="{x0+49}" y="118" text-anchor="middle">BLOCKED</text>')
    o.append(f'<line x1="{x0+100}" y1="113" x2="{x0+146}" y2="113" stroke="#495057" stroke-width="2" marker-end="url(#aG)"/>')
    if ok:
        o.append(f'<rect x="{x0+150}" y="96" width="156" height="34" rx="6" fill="#FFFFFF" stroke="#495057" stroke-width="1.6"/><text class="ms" x="{x0+160}" y="118">[(2,0), <tspan fill="#2E7D32" font-weight="800">(1,1)</tspan>]</text>')
        o.append(f'<text class="n" x="{x0}" y="160" style="fill:#2E7D32">Same list, one more item. The name</text>')
        o.append(f'<text class="n" x="{x0}" y="177" style="fill:#2E7D32">was never reassigned: no global.</text>')
    else:
        o.append(f'<rect x="{x0+150}" y="96" width="156" height="34" rx="6" fill="#FFFFFF" stroke="#495057" stroke-width="1.6"/><text class="ms" x="{x0+160}" y="118">[(2,0)]</text>')
        o.append(f'<rect x="{x0}" y="146" width="98" height="34" rx="6" fill="#F1F3F5" stroke="#868E96" stroke-width="1.6" stroke-dasharray="4 3"/><text class="m" x="{x0+49}" y="168" text-anchor="middle" style="fill:#495057">BLOCKED</text>')
        o.append(f'<line x1="{x0+100}" y1="163" x2="{x0+146}" y2="163" stroke="#868E96" stroke-width="2" marker-end="url(#aG)"/>')
        o.append(f'<rect x="{x0+150}" y="146" width="60" height="34" rx="6" fill="#FFFFFF" stroke="#868E96" stroke-width="1.6"/><text class="ms" x="{x0+180}" y="168" text-anchor="middle">[]</text>')
        o.append(f'<text class="sm" x="{x0+218}" y="160">a new local,</text><text class="sm" x="{x0+218}" y="174">gone at return</text>')
        o.append(f'<text class="n" x="{x0}" y="204" style="fill:#D1182C">Assigning makes a new local name; the</text>')
        o.append(f'<text class="n" x="{x0}" y="221" style="fill:#D1182C">real list is untouched. That needs global.</text>')
    return o
b+=panel(12,"append: changes the list","BLOCKED.append((1, 1))",True)
b+=panel(358,"= inside a function: a new name","BLOCKED = []",False)
open(OUTDIR+'append-vs-assign.svg','w').write(svg('Why append needs no global',
 'Two panels. Left, BLOCKED.append((1, 1)): the name BLOCKED still points at the same list, which now has one more item; the name was never reassigned, so no global is needed. Right, BLOCKED = [] inside a function: this makes a new local name BLOCKED pointing at a new empty list, gone when the function returns, while the real BLOCKED list is untouched; that is the case that needs global.',b,H=236))
