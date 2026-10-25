import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
src=open(ROBOT_SRC).read()
defs=src[src.index('<defs>'):src.index('</defs>')+7]
S=0.5; TW=11
gx=[75,185,295]; gy=[75,185,295]
STY='''<style>
    .h   { font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 700; fill: #22527B; }
    .n   { font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 12.5px; fill: #343A40; }
    .nb  { font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 12.5px; font-weight: 700; fill: #142D50; }
    .num { font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 11px; font-weight: 700; fill: #22527B; }
    .pl  { font-family: "Comic Sans MS", "Chalkboard SE", "Marker Felt", Montserrat, sans-serif; font-size: 14px; fill: #142D50; }
  </style>'''
EXTRA='''<marker id="gA" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#FFFFFF"/></marker>
    <marker id="gL" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#495057"/></marker>'''
def base():
    g=['<rect x="20" y="20" width="330" height="330" rx="8" fill="#F3F4F6" stroke="#DEE2E6"/>']
    for x in gx: g.append(f'<rect x="{x-TW/2}" y="20" width="{TW}" height="330" fill="#2B2B2B"/>')
    for y in gy: g.append(f'<rect x="20" y="{y-TW/2}" width="330" height="{TW}" fill="#2B2B2B"/>')
    return g
def robot(x,y,ang,op=0.95): return f'<use href="#pcXRP" transform="translate({x} {y}) rotate({ang}) scale({S})" opacity="{op}"/>'
def route(pts):
    d='M '+' L '.join(f'{x} {y}' for x,y in pts)
    return f'<path d="{d}" fill="none" stroke="#4C8BF5" stroke-width="10" stroke-linejoin="round" stroke-linecap="round" opacity="0.85"/>'
def arrows(pts):
    out=[]
    for (x1,y1),(x2,y2) in zip(pts,pts[1:]):
        mx,my=(x1+x2)/2,(y1+y2)/2; dx,dy=(x2-x1),(y2-y1); L=(dx*dx+dy*dy)**.5; ux,uy=dx/L,dy/L
        out.append(f'<line x1="{mx-ux*8:.1f}" y1="{my-uy*8:.1f}" x2="{mx+ux*6:.1f}" y2="{my+uy*6:.1f}" stroke="#FFFFFF" stroke-width="3" marker-end="url(#gA)"/>')
    return out
def badge(x,y,n,dx=15,dy=-15):
    return f'<circle cx="{x+dx}" cy="{y+dy}" r="9" fill="#FFFFFF" stroke="#22527B" stroke-width="1.6"/><text class="num" x="{x+dx}" y="{y+dy+4}" text-anchor="middle">{n}</text>'
def turnmark(x,y,dx=22,dy=22):
    return (f'<path d="M {x+dx-10} {y+dy-12} A 11 11 0 1 1 {x+dx-11} {y+dy+5}" fill="none" stroke="#D1182C" stroke-width="2.2" marker-end="url(#gR)"/>')
def svg(title,desc,body,H=370):
    ex=EXTRA+'\n    <marker id="gR" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#D1182C"/></marker>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 {H}" width="680" height="{H}" role="img" aria-labelledby="gT gD">
  <title id="gT">{title}</title>
  <desc id="gD">{desc}</desc>
  {STY}
  {defs.replace('<defs>','<defs>'+chr(10)+'    '+ex)}
  <rect width="680" height="{H}" fill="#FFFFFF"/>
  {(chr(10)+'  ').join(body)}
</svg>
'''
# ---------- 3-1 grid ----------
b=base()
for x in gx:
    for y in gy: b.append(f'<circle cx="{x}" cy="{y}" r="15" fill="none" stroke="#2E7D32" stroke-width="2.4" stroke-dasharray="5 3"/>')
b.append(robot(110,185,90))
b.append(f'<rect x="200" y="{185-TW/2-4}" width="0" height="0"/>')
# annotations
b+= ['<text class="h" x="380" y="70">Intersection</text>',
     '<text class="n" x="380" y="90">where two lines cross. To the</text>',
     '<text class="n" x="380" y="107">sensors it looks just like the</text>',
     '<text class="n" x="380" y="124">cross from Module 2.</text>',
     '<path d="M 376 78 C 330 70, 320 75, 302 77" fill="none" stroke="#495057" stroke-width="1.4" marker-end="url(#gL)"/>',
     '<text class="h" x="380" y="175">Segment</text>',
     '<text class="n" x="380" y="195">the stretch of line from one</text>',
     '<text class="n" x="380" y="212">intersection to the next.</text>',
     '<path d="M 376 183 C 320 200, 270 210, 245 190" fill="none" stroke="#495057" stroke-width="1.4" marker-end="url(#gL)"/>',
     '<text class="h" x="380" y="275">The robot</text>',
     '<text class="n" x="380" y="295">on a segment, facing the next</text>',
     '<text class="n" x="380" y="312">intersection: track_to_intersection()</text>',
     '<text class="n" x="380" y="329">takes it there.</text>',
     '<path d="M 376 283 C 250 300, 150 260, 130 214" fill="none" stroke="#495057" stroke-width="1.4" marker-end="url(#gL)"/>']
open(OUTDIR+'grid.svg','w').write(svg('A 3×3 taped grid',
 'A grid of three vertical and three horizontal taped lines. The nine places where they cross are circled: intersections. The XRP sits on the middle row between the first and second intersections, facing the next one. Labels: an intersection is where two lines cross and looks to the sensors just like the cross from Module 2; a segment is the stretch of line from one intersection to the next; the robot on a segment, facing the next intersection, is taken there by track_to_intersection().',b))
# ---------- 3-3 L ----------
# Geometry is the old drawing turned a quarter turn counterclockwise, so the
# robot starts on the corner nearest the student (bottom-left) facing away.
def T(x,y): return (185+(y-185), 185-(x-185))
def TO(dx,dy): return (dy,-dx)
pts=[T(*q) for q in [(75,75),(295,75),(295,295)]]
b=base(); b.append(route(pts)); b+=arrows([T(*q) for q in [(75,75),(185,75),(295,75)]])+arrows([T(*q) for q in [(295,75),(295,185),(295,295)]])
for i,(x,y) in enumerate([(185,75),(295,75),(295,185),(295,295)]):
    dx,dy=((42 if y==295 else 17) if x==295 else 0, 0 if x==295 else -18)
    X,Y=T(x,y); DX,DY=TO(dx,dy); b.append(badge(X,Y,i+1,dx=DX,dy=DY))
X,Y=T(295,75); b.append(turnmark(X,Y,*TO(22,22)))
X,Y=T(295,295); b.append(robot(X,Y,90,0.35)); X,Y=T(75,75); b.append(robot(X,Y,0))
b+=['<text class="nb" x="104" y="336">start</text>','<text class="nb" x="226" y="62">end</text>',
    '<text class="h" x="390" y="70">The plan, on paper</text>',
    '<rect x="390" y="84" width="260" height="128" rx="6" fill="#FFFCEB" stroke="#E9D9A6"/>',
    '<text class="pl" x="404" y="112">leg 1: 2 intersections</text>',
    '<text class="pl" x="404" y="142">corner: turn right</text>',
    '<text class="pl" x="404" y="172">leg 2: 2 intersections</text>',
    '<text class="pl" x="404" y="199" style="font-size:12px;fill:#6C757D">one line of code per line</text>',
    '<text class="n" x="390" y="246">Numbers are the intersections the</text>',
    '<text class="n" x="390" y="263">robot arrives at. It turns parked on</text>',
    '<text class="n" x="390" y="280">②, and ends parked on ④.</text>',
    f'<path d="M 386 136 C 300 130, 160 100, 98 82" fill="none" stroke="#D1182C" stroke-width="1.4" marker-end="url(#gR)"/>']
open(OUTDIR+'l-path.svg','w').write(svg('An L-shaped path on the grid',
 'The 3×3 grid with an L-shaped route. The robot starts parked on the bottom-left intersection, the corner nearest you, facing away from you. Leg 1 arrives at two intersections, numbered 1 and 2, up the left-hand column; at 2 it turns right; leg 2 arrives at intersections 3 and 4 along the top row, and it ends parked on 4 facing right. Beside it, the plan as written on paper: leg 1: 2 intersections; corner: turn right; leg 2: 2 intersections.',b))
# ---------- 3-4 square ----------
corners=[T(*q) for q in [(75,75),(295,75),(295,295),(75,295),(75,75)]]
b=base(); b.append(route(corners))
for a_,c in zip(corners,corners[1:]):
    mid=((a_[0]+c[0])/2,(a_[1]+c[1])/2); b+=arrows([a_,mid,c])
stops=[(185,75),(295,75),(295,185),(295,295),(185,295),(75,295),(75,185),(75,75)]
offs={(185,75):(0,-17),(295,75):(17,-17),(295,185):(18,0),(295,295):(17,17),(185,295):(0,18),(75,295):(-17,17),(75,185):(-18,0),(75,75):(0,-45)}
for i,(x,y) in enumerate(stops):
    X,Y=T(x,y); b.append(badge(X,Y,i+1,*TO(*offs[(x,y)])))
for (x,y),(dx,dy) in [((295,75),(-26,26)),((295,295),(-26,-26)),((75,295),(26,-26)),((75,75),(36,40))]:
    X,Y=T(x,y); b.append(turnmark(X,Y,*TO(dx,dy)))
X,Y=T(75,75); b.append(robot(X,Y,0))
b+=['<text class="nb" x="104" y="262">start = end</text>',
    '<text class="h" x="390" y="70">One side per pass</text>',
    '<rect x="390" y="84" width="260" height="104" rx="6" fill="#FFFCEB" stroke="#E9D9A6"/>',
    '<text class="pl" x="404" y="112">4 times:</text>',
    '<text class="pl" x="420" y="142">drive SIDE intersections</text>',
    '<text class="pl" x="420" y="172">turn right</text>',
    '<text class="n" x="390" y="222">SIDE = 2. Four sides, four right</text>',
    '<text class="n" x="390" y="239">turns (360°): the robot is back on</text>',
    '<text class="n" x="390" y="256">the corner it started on, facing</text>',
    '<text class="n" x="390" y="273">the way it started.</text>',
    '<text class="n" x="390" y="305" style="fill:#6C757D">Numbers are the intersections it</text>',
    '<text class="n" x="390" y="322" style="fill:#6C757D">arrives at; 8 is the start corner.</text>']
open(OUTDIR+'square-path.svg','w').write(svg('A square path on the grid',
 'The 3×3 grid with a square route around its outside. The robot starts parked on the bottom-left corner, nearest you, facing away from you. Each side arrives at two intersections, and there is a right turn at each corner; the intersections are numbered 1 to 8, and 8 is the corner it started on, so start and end are the same. Beside it, the loop in plain words: 4 times, drive SIDE intersections, turn right. SIDE is 2; four right turns make 360 degrees, so the robot ends facing the way it started.',b))
