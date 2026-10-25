import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'g51.py')).read().split("b=['<text class=\"h\" x=\"20\" y=\"26\">The 3×3")[0])
HL={(1,1):("#4C8BF5","#22527B"),(0,1):("#DCE8F3","#22527B"),(2,1):("#DCE8F3","#22527B"),(1,0):("#DCE8F3","#22527B"),(1,2):("#DCE8F3","#22527B"),(0,0):("#FFF0D1","#C77C02")}
b=['<text class="h" x="20" y="26">graph = {node: [neighbors]}</text>']
b+=graph(60,80,90,3,deg=False,mark=HL)
X=300
b.append(f'<text class="nb" x="{X}" y="64">key</text><text class="nb" x="{X+96}" y="64">value: a list of neighbors</text>')
rows=[("(0, 0)","[(1, 0), (0, 1)]","#FFF0D1","#C77C02"),("(0, 1)","[(1, 1), (0, 0), (0, 2)]","#F8F9FA","#ADB5BD"),("(1, 1)","[(0, 1), (2, 1), (1, 0), (1, 2)]","#DCE8F3","#22527B"),("…","…","#F8F9FA","#ADB5BD")]
for i,(k,v,f,s) in enumerate(rows):
    y=80+i*42
    b.append(f'<rect x="{X}" y="{y}" width="80" height="30" rx="6" fill="{f}" stroke="{s}" stroke-width="1.6"/><text class="m" x="{X+40}" y="{y+20}" text-anchor="middle">{k}</text>')
    b.append(f'<line x1="{X+82}" y1="{y+15}" x2="{X+94}" y2="{y+15}" stroke="#495057" stroke-width="2" marker-end="url(#aG)"/>')
    b.append(f'<rect x="{X+96}" y="{y}" width="272" height="30" rx="6" fill="#FFFFFF" stroke="{s}" stroke-width="1.4"/><text class="ms" x="{X+106}" y="{y+20}">{v}</text>')
b+=[f'<text class="n" x="{X}" y="270"><tspan class="m">graph[(1, 1)]</tspan> jumps straight to the blue list:</text>',
    f'<text class="n" x="{X}" y="288">no searching, no counting positions.</text>',
    f'<text class="sm" x="{X}" y="314">Neighbors are listed left, right, down, up.</text>']
open(OUTDIR+'graph-dict.svg','w').write(svg('A graph stored as a dictionary',
 'Left: the 3 by 3 graph, (0, 0) at the bottom-left, with (1, 1) highlighted blue, its four neighbors light blue, and (0, 0) orange. Right: the dictionary as key and value rows. Key (0, 0) maps to [(1, 0), (0, 1)]; key (0, 1) maps to [(1, 1), (0, 0), (0, 2)]; key (1, 1) maps to [(0, 1), (2, 1), (1, 0), (1, 2)]. graph[(1, 1)] jumps straight to that list. Neighbors are listed left, right, down, up.',b,H=330))
# bounds
def checks(cx,cy,title,res,node):
    o=[f'<text class="h" x="{cx}" y="30" text-anchor="middle">{title}</text>',f'<circle cx="{cx}" cy="{cy}" r="20" fill="#DCE8F3" stroke="#22527B" stroke-width="2.4"/><text class="ms" x="{cx}" y="{cy+4}" text-anchor="middle">{node}</text>']
    for (dx,dy,lab,ok) in res:
        col="#2E7D32" if ok else "#D1182C"
        x2,y2=cx+dx*130,cy+dy*62
        o.append(f'<line x1="{cx+dx*24}" y1="{cy+dy*24}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="3" {"" if ok else "stroke-dasharray=\"5 4\""} marker-end="url({"#aGr" if ok else "#aR"})"/>')
        if dx==0: tx,ty,anc=cx,cy+dy*84+4,"middle"
        else: tx,ty,anc=cx+dx*(88 if dx>0 else 68),cy-14,"middle"
        o.append(f'<text class="ms" x="{tx}" y="{ty}" text-anchor="{anc}" style="fill:{col}">{lab} {"✓" if ok else "✗"}</text>')
    return o
b=[]
b+=checks(170,170,"Corner (0, 0): 2 neighbors",[(0,-1,"y &lt; rows - 1",True),(0,1,"y &gt; 0",False),(-1,0,"x &gt; 0",False),(1,0,"x &lt; cols - 1",True)],"0,0")
b+=checks(510,170,"Interior (1, 1): 4 neighbors",[(0,-1,"y &lt; rows - 1",True),(0,1,"y &gt; 0",True),(-1,0,"x &gt; 0",True),(1,0,"x &lt; cols - 1",True)],"1,1")
b.append('<text class="n" x="340" y="316" text-anchor="middle">Each check guards one direction. A failed check means that neighbor would be off the grid.</text>')
open(OUTDIR+'bounds-checks.svg','w').write(svg('The four bounds checks',
 'Two nodes with an arrow for each direction. The bottom-left corner (0, 0): left, x &gt; 0, fails; down, y &gt; 0, fails; right, x &lt; cols - 1, passes; up, y &lt; rows - 1, passes; so it gets 2 neighbors. The interior node (1, 1): all four checks pass, so it gets 4 neighbors. A failed check means that neighbor would be off the grid.',b,H=330))
