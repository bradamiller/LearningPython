import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys; from common import *
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'g51.py')).read().split("b=['<text class=\"h\" x=\"20\" y=\"26\">The 3×3")[0])
from sim import bfs
rows=[("previous = {position: None}","came-from table; start came from nowhere"),
      ("to_visit = [position]","the to-visit list beside the grid"),
      ("current = to_visit.pop(0)","take the oldest one, from the front"),
      ("if neighbor not in previous:","it has no number yet: numbered once"),
      ("previous[neighbor] = current","write where it came from"),
      ("to_visit.append(neighbor)","add it to the end of the list"),
      ("while current != position:","walk back along came-from; stop at the start")]
b=['<text class="h" x="12" y="24">Code</text>','<text class="h" x="388" y="24">Pencil (Lesson 5-3)</text>']
for i,(c,p) in enumerate(rows):
    y=40+i*40
    b.append(f'<rect x="12" y="{y}" width="290" height="30" rx="6" fill="#F1F6FB" stroke="#22527B" stroke-width="1.4"/><text class="ms" x="22" y="{y+20}">{c}</text>')
    b.append(f'<line x1="304" y1="{y+15}" x2="384" y2="{y+15}" stroke="#ADB5BD" stroke-width="1.6" stroke-dasharray="4 3"/>')
    b.append(f'<rect x="388" y="{y}" width="280" height="30" rx="6" fill="#FFF8E8" stroke="#C77C02" stroke-width="1.4"/><text class="n" x="398" y="{y+20}" style="font-size:12px">{p}</text>')
open(OUTDIR+'code-pencil.svg','w').write(svg('Every line is a pencil step',
 'Seven lines of compute_bfs_path matched to the pencil method from Lesson 5-3. previous = {position: None} is the came-from table, where the start came from nowhere. to_visit = [position] is the to-visit list beside the grid. current = to_visit.pop(0) takes the oldest one, from the front. if neighbor not in previous means it has no number yet, so each intersection is numbered once. previous[neighbor] = current writes where it came from. to_visit.append(neighbor) adds it to the end of the list. while current != position walks back along came-from and stops at the start.',b,H=322))
# bfs vs dfs, Test 4
B=[(1,0),(1,1)]; pb=bfs((0,0),(3,0),B); pd=bfs((0,0),(3,0),B,dfs=True)
def panel(x0,title,path,col,note):
    sp=64; gx,gy=x0+40,74
    o=[f'<text class="h" x="{x0}" y="26">{title}</text>']
    P=lambda a,b:(gx+a*sp,gy+(3-b)*sp)
    pts=[(0,0)]+path
    d='M '+' L '.join(f'{P(*q)[0]} {P(*q)[1]}' for q in pts)
    g=graph(gx,gy,sp,4,blocked=B,deg=False,label=False)
    g=[e.replace('r="18"','r="10"').replace('M {0}','') for e in g]
    g=[e.replace('stroke-width="4"','stroke-width="3"') for e in g]
    o+=g
    o.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round" opacity="0.75"/>')
    for i,q in enumerate(path):
        x,y=P(*q); o.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{col}"/><text class="sm" x="{x}" y="{y+4}" text-anchor="middle" style="fill:#FFFFFF;font-weight:700;font-size:10px">{i+1}</text>')
    x,y=P(0,0); o.append(f'<circle cx="{x}" cy="{y}" r="11" fill="#142D50"/><text class="sm" x="{x}" y="{y+4}" text-anchor="middle" style="fill:#FFFFFF;font-weight:700">S</text>')
    o.append(f'<text class="nb" x="{x0}" y="{gy+3*sp+44}" style="fill:{col}">{note}</text>')
    return o
b=[]
b+=panel(12,"pop(0): oldest first (BFS)",pb,"#2E7D32",f"{len(pb)} steps, the shortest")
b+=panel(352,"pop(): newest first (depth-first)",pd,"#D1182C",f"{len(pd)} steps: it dove down one route")
open(OUTDIR+'bfs-vs-dfs.svg','w').write(svg('pop(0) versus pop()',
 f'Test 4 on the 4 by 4 grid with (0, 0) at the bottom-left, from (0, 0) to (3, 0) with (1, 0) and (1, 1) blocked. Left, with pop(0), oldest first, breadth-first search finds a {len(pb)}-step path: up to (0, 2), right along y = 2 to (3, 2), then down the right edge to (3, 0). Right, with pop(), newest first, the search dives down one route and returns a {len(pd)}-step path: all the way up to (0, 3), right to (2, 3), back down the column at x = 2 to (2, 0), then right to (3, 0).',b,H=346))
print(len(pb),len(pd))
