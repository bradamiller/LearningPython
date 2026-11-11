import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR
# Lesson 4-3: going left, the east loop's first check is False, so only west runs.
INK,MUTE,RED,GRN="#343A40","#868E96","#D1182C","#2E7D32"
o=[]
T=lambda x,y,t,cls,col=INK,anc="start": f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anc}" fill="{col}" xml:space="preserve">{t}</text>'
o.append(T(24,30,"GOING LEFT: x = 3, dest_x = 1","hdr","#22527B"))
def box(y,lines,stroke,fill,txtcol,verdict,vcol,dash=""):
    h=24*len(lines)+26
    s=[f'<rect x="24" y="{y}" width="330" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="2.5" {dash}/>']
    for i,l in enumerate(lines): s.append(T(40,y+30+24*i,l,"c",txtcol))
    for k,v in enumerate(verdict): s.append(T(380,y+28+22*k,v,"v" if k==0 else "w",vcol if k==0 else INK))
    return s,h
s,h=box(48,["# East","while x &lt; dest_x:","    x = x + 1","    path.append((x, y))"],"#ADB5BD","#F8F9FA",MUTE,
        ["3 &lt; 1 is False","on the first check,","so this loop never runs."],RED,'stroke-dasharray="7 6"'); o+=s
y2=48+h+22
s,h2=box(y2,["# West","while x &gt; dest_x:","    x = x - 1","    path.append((x, y))"],GRN,"#E8F3E9",INK,
        ["3 &gt; 1 is True,","so this loop runs twice:","x goes 3, 2, 1."],GRN); o+=s
H=y2+h2+50; W=640
o.append(T(24,H-18,"For any trip, at most one of the two x loops runs. The same goes for the two y loops.","cap","#495057"))
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="sk-t sk-d" font-family="Montserrat, Helvetica, Arial, sans-serif">
  <title id="sk-t">Only one x loop runs</title>
  <desc id="sk-d">Going left, with x = 3 and dest_x = 1. The east loop, while x &lt; dest_x, is grayed out: 3 &lt; 1 is False on the first check, so it never runs. The west loop, while x &gt; dest_x, is highlighted: 3 &gt; 1 is True, so it runs twice and x goes 3, 2, 1. For any trip, at most one of the two x loops runs, and the same goes for the two y loops.</desc>
  <style>
    .hdr {{ font-size: 13px; font-weight: 700; letter-spacing: .6px; }}
    .c {{ font-size: 16px; font-family: ui-monospace, Menlo, Consolas, monospace; }}
    .v {{ font-size: 15px; font-weight: 700; font-family: ui-monospace, Menlo, Consolas, monospace; }}
    .w {{ font-size: 14px; }}
    .cap {{ font-size: 13px; }}
  </style>
{chr(10).join("  "+x for x in o)}
</svg>
'''
open(OUTDIR+'one-x-loop-runs.svg','w').write(svg)
