import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR
# Lesson 4-3: the trace table's rows become two loops.
XC,YC,INK,MUTE="#D1182C","#2E7D32","#343A40","#868E96"
XB,YB="#FDECEE","#E8F3E9"
rows=[("1","x + 1","(1, 0)"),("2","x + 1","(2, 0)"),("3","y + 1","(2, 1)"),("4","y + 1","(2, 2)"),("5","y + 1","(2, 3)")]
o=[]
T=lambda x,y,t,cls="t",anc="start",col=INK: f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anc}" fill="{col}">{t}</text>'
tx,ty,rh=24,56,40; cw=[70,110,140]; tw=sum(cw)
o.append(T(tx,30,"YOUR TRACE TABLE: (0, 0) TO (2, 3)","hdr"))
o.append(f'<rect x="{tx}" y="{ty}" width="{tw}" height="{rh}" fill="#22527B" rx="6"/>')
cx=tx
for w,h in zip(cw,["Step","Action","New position"]):
    o.append(T(cx+w/2,ty+26,h,"th","middle","#fff")); cx+=w
for i,(s,a,p) in enumerate(rows):
    y=ty+rh*(i+1); col,bg=(XC,XB) if i<2 else (YC,YB)
    o.append(f'<rect x="{tx}" y="{y}" width="{tw}" height="{rh}" fill="{bg}" stroke="#fff" stroke-width="2"/>')
    vals=[(s,INK),(a,col),(p,INK)]; cx=tx
    for w,(v,c) in zip(cw,vals):
        o.append(T(cx+w/2,y+26,v,"m","middle",c)); cx+=w
# brackets
bx=tx+tw+14
def bracket(y1,y2,col):
    return f'<path d="M{bx},{y1+4} h10 V{y2-4} h-10" fill="none" stroke="{col}" stroke-width="3"/>'
y1a,y2a=ty+rh,ty+rh*3; y1b,y2b=ty+rh*3,ty+rh*6
o.append(bracket(y1a,y2a,XC)); o.append(bracket(y1b,y2b,YC))
# code boxes
kx=bx+90; kw=360
def code(y,lines,col,bg,label):
    h=24*len(lines)+44
    s=[f'<rect x="{kx}" y="{y}" width="{kw}" height="{h}" rx="8" fill="{bg}" stroke="{col}" stroke-width="2.5"/>',
       T(kx+14,y+24,label,"lab","start",col)]
    for i,l in enumerate(lines):
        s.append(f'<text class="c" x="{kx+14}" y="{y+52+24*i}" xml:space="preserve" fill="{INK}">{l}</text>')
    return s,h
la=["while x &lt; dest_x:","    x = x + 1","    path.append((x, y))"]
lb=["while y &lt; dest_y:","    y = y + 1","    path.append((x, y))"]
ka=ty+8; s,ha=code(ka,la,XC,XB,"Loop 1 · rows 1 and 2: add 1 to x"); o+=s
kb=ka+ha+24; s,hb=code(kb,lb,YC,YB,"Loop 2 · rows 3 to 5: add 1 to y"); o+=s
def arrow(y0,y1,col,mk):
    return f'<path d="M{bx+12},{y0} C{bx+50},{y0} {kx-40},{y1} {kx-4},{y1}" fill="none" stroke="{col}" stroke-width="2.5" marker-end="url(#{mk})"/>'
o.append(arrow((y1a+y2a)/2,ka+ha/2,XC,"mx")); o.append(arrow((y1b+y2b)/2,kb+hb/2,YC,"my"))
H=max(ty+rh*6,kb+hb)+46; W=kx+kw+24
o.append(T(tx,H-16,"Each row is one trip around a loop: add 1, then append the new position.","cap","start","#495057"))
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" role="img" aria-labelledby="tl-t tl-d" font-family="Montserrat, Helvetica, Arial, sans-serif">
  <title id="tl-t">From the trace table to two loops</title>
  <desc id="tl-d">The trace table for (0, 0) to (2, 3) has five rows. Rows 1 and 2, in red, say x + 1 and reach (1, 0) and (2, 0); a red bracket points to loop 1: while x &lt; dest_x, x = x + 1, path.append((x, y)). Rows 3 to 5, in green, say y + 1 and reach (2, 1), (2, 2) and (2, 3); a green bracket points to loop 2, the same loop for y. Each row is one trip around a loop: add 1, then append the new position.</desc>
  <style>
    .hdr {{ font-size: 13px; font-weight: 700; fill: #22527B; letter-spacing: .6px; }}
    .th {{ font-size: 13px; font-weight: 700; }}
    .m, .c {{ font-family: ui-monospace, Menlo, Consolas, monospace; }}
    .m {{ font-size: 15px; font-weight: 700; }}
    .c {{ font-size: 16px; }}
    .lab {{ font-size: 13.5px; font-weight: 700; }}
    .cap {{ font-size: 13px; }}
  </style>
  <defs>
    <marker id="mx" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{XC}"/></marker>
    <marker id="my" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{YC}"/></marker>
  </defs>
  {chr(10).join("  "+x for x in o)}
</svg>
'''
open(OUTDIR+'trace-to-loops.svg','w').write(svg)
