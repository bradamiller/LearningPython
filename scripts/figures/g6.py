import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math; from common import *
O=OUTDIR+''
RED,GRN,BLU,NAVY,AMB,SL="#D1182C","#2E7D32","#22527B","#142D50","#C77C02","#343A40"
def wig(x1,x2,y,amp=20,waves=3,n=90):
    pts=[]
    for i in range(n+1):
        t=i/n; x=x1+(x2-x1)*t
        env=min(1,t*6,(1-t)*6)
        pts.append((round(x,1),round(y+amp*env*math.sin(2*math.pi*waves*t),1)))
    return pts
def wigseg(p1,p2,amp=20,waves=3,n=90):
    (x1,y1),(x2,y2)=p1,p2; L=((x2-x1)**2+(y2-y1)**2)**.5; nx,ny=-(y2-y1)/L,(x2-x1)/L
    pts=[]
    for i in range(n+1):
        t=i/n; env=min(1,t*6,(1-t)*6); o=amp*env*math.sin(2*math.pi*waves*t)
        pts.append((round(x1+(x2-x1)*t+nx*o,1),round(y1+(y2-y1)*t+ny*o,1)))
    return pts
def poly(pts): return 'M '+' L '.join(f'{x} {y}' for x,y in pts)
def floor(g,slow=((0,1),(0,2))):
    o=g.base(axes=True,north=False)
    (x,y1),(_,y2)=g.p(*slow[0]),g.p(*slow[1])
    o.append(f'<rect x="{x-g.tw/2-1}" y="{y2+g.tw/2}" width="{g.tw+2}" height="{y1-y2-g.tw}" fill="#F3F4F6"/>')
    o.append(f'<path d="{poly(wigseg((x,y1),(x,y2)))}" fill="none" stroke="#2B2B2B" stroke-width="{g.tw}" stroke-linejoin="round"/>')
    return o
def endpoints(g,s,d):
    o=[]
    for q,l,c in ((s,"S",NAVY),(d,"D",GRN)):
        x,y=g.p(*q); o.append(f'<circle cx="{x}" cy="{y}" r="11" fill="{c}" stroke="#FFFFFF" stroke-width="2"/><text class="sm" x="{x}" y="{y+4}" text-anchor="middle" style="fill:#FFFFFF;font-weight:700">{l}</text>')
    return o
def card(x,y,w,h,col,lines):
    o=[f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#FFFFFF" stroke="{col}" stroke-width="2"/>']
    for i,(cls,t) in enumerate(lines):
        st=f' style="fill:{col}"' if i==0 else ''
        o.append(f'<text class="{cls}" x="{x+14}" y="{y+24+i*20}"{st}>{t}</text>')
    return o

# ---------- 6-0 slow-road ----------
g=G(80,112,sp=80)
b=['<text class="h" x="20" y="26">One slow segment, two answers</text>']
b+=floor(g)
x0,y0=g.p(0,0); _,y1=g.p(0,1); _,y2=g.p(0,2); _,y3=g.p(0,3)
A=[(x0,y0),(x0,y1)]+wigseg((x0,y1),(x0,y2))+[(x0,y3)]
b.append(f'<path d="{poly([(x,y-0) for x,y in A])}" fill="none" stroke="{RED}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round" opacity="0.85"/>')
b.append(g.route([(0,0),(1,0),(1,1),(1,2),(0,2),(0,3)],GRN).replace('stroke-width="9"','stroke-width="6"'))
b+=endpoints(g,(0,0),(0,3))
b.append(tag(x0+40,(y1+y2)/2,"slow road",stroke=RED,cls="sm",w=72).replace('<text class="sm"','<text class="sm" style="fill:#D1182C;font-weight:700"'))
X=400
b+=card(X,92,262,92,RED,[("nb","BFS: fewest steps"),("n","straight up the left edge, x = 0"),("m","3 steps   cost 7")])
b+=card(X,202,262,92,GRN,[("nb","Dijkstra: least time"),("n","right, up through x = 1, back left"),("m","5 steps   cost 5")])
b+=[f'<text class="sm" x="{X}" y="322">cost = blocks\' worth of time; the slow road</text>',f'<text class="sm" x="{X}" y="338">costs 5, every other block costs 1</text>']
open(O+'slow-road.svg','w').write(svg('One slow segment, two answers',
 'A 4 by 4 grid of tape with (0, 0) at the bottom-left. On the left edge, x = 0, the segment between (0, 1) and (0, 2) winds back and forth instead of running straight. From S at (0, 0) to D at (0, 3), BFS goes straight up the left edge through the slow segment: 3 steps, cost 7. Dijkstra goes right to x = 1, up, and back left to the left edge: 5 steps, cost 5, and arrives first.',b,H=430))

# ---------- 6-1 floor vs graph ----------
ys=[350,260,170,80]   # y = 0 at the bottom
b=[]
def coltitle(x,t1,t2): return [f'<text class="h" x="{x}" y="26" text-anchor="middle">{t1}</text>',f'<text class="sm" x="{x}" y="44" text-anchor="middle">{t2}</text>']
# floor strip
FX=110
b+=coltitle(FX,"On the floor","the left edge, x = 0")
b.append(f'<rect x="{FX-36}" y="56" width="72" height="318" rx="8" fill="#F3F4F6" stroke="#DEE2E6"/>')
b.append(f'<rect x="{FX-4.5}" y="{ys[1]}" width="9" height="{374-ys[1]}" fill="#2B2B2B"/>')
b.append(f'<path d="{poly(wigseg((FX,ys[1]),(FX,ys[2]),amp=22,waves=4))}" fill="none" stroke="#2B2B2B" stroke-width="9" stroke-linejoin="round"/>')
b.append(f'<rect x="{FX-4.5}" y="56" width="9" height="{ys[2]-56}" fill="#2B2B2B"/>')
for i,y in enumerate(ys):
    b.append(f'<rect x="{FX-36}" y="{y-4.5}" width="72" height="9" fill="#2B2B2B"/>')
    b.append(f'<text class="ax" x="{FX-44}" y="{y+4}" text-anchor="end">(0, {i})</text>')
for i,(t,c,bold) in enumerate((("about 4 s","#6C757D",""),("about 20 s",RED,";font-weight:700"),("about 4 s","#6C757D",""))):
    b.append(f'<text class="sm" x="{FX+44}" y="{(ys[i]+ys[i+1])/2+4}" style="fill:{c}{bold}">{t}</text>')
def chain(cx,labels,colors,widths,title,sub,note):
    o=coltitle(cx,title,sub)
    for i in range(3):
        o.append(f'<line x1="{cx}" y1="{ys[i]}" x2="{cx}" y2="{ys[i+1]}" stroke="{colors[i]}" stroke-width="{widths[i]}"/>')
        o.append(tag(cx+46,(ys[i]+ys[i+1])/2,labels[i],stroke=colors[i] if colors[i]!="#495057" else BLU))
    for i,y in enumerate(ys):
        o.append(f'<circle cx="{cx}" cy="{y}" r="18" fill="#FFFFFF" stroke="{BLU}" stroke-width="2.4"/><text class="ms" x="{cx}" y="{y+4}" text-anchor="middle" style="font-size:10.5px">0,{i}</text>')
    for j,t in enumerate(note): o.append(f'<text class="n" x="{cx}" y="{398+j*17}" text-anchor="middle">{t}</text>')
    return o
b+=chain(350,["1 step"]*3,["#495057"]*3,[4,4,4],"To the Module 5 graph","every edge counts 1",["all the same"])
b+=chain(560,["1","5","1"],[BLU,RED,BLU],[4,7,4],"With a weight","on every edge",["20 ÷ 4 ≈ 5:","five blocks\' time"])
open(O+'floor-vs-graph.svg','w').write(svg('A slow segment, a step and a weight',
 'Three columns, each the left edge of the grid, x = 0, from (0, 0) at the bottom to (0, 3) at the top. On the floor: the tape from (0, 0) to (0, 1) and from (0, 2) to (0, 3) is straight and takes about 4 seconds; the tape from (0, 1) to (0, 2) winds back and forth and takes about 20 seconds. To the Module 5 graph: every edge is 1 step, so it cannot tell them apart. With a weight on every edge: the edges are 1, 5 and 1, because 20 divided by 4 is about 5 blocks of time.',b,H=440))

# ---------- 6-1 break-even ----------
g=G(70,80,sp=84,n=2)
def mini(gx,gy):
    gg=G(gx,gy,sp=84,n=2,pad=24)
    return gg
b=['<text class="h" x="20" y="26">The slow edge, or the three blocks around it</text>']
gg=G(90,92,sp=90,n=2,pad=26)
L=gg.sp
o=[f'<rect x="{gg.x0-26}" y="{gg.y0-26}" width="{L+52}" height="{L+52}" rx="8" fill="#F3F4F6" stroke="#DEE2E6"/>']
(ax,ay),(bx,by),(cx,cy),(dx,dy)=gg.p(0,0),gg.p(0,1),gg.p(1,0),gg.p(1,1)
o.append(f'<path d="{poly(wigseg((ax,ay),(bx,by),amp=16,waves=3))}" fill="none" stroke="{RED}" stroke-width="6" stroke-linejoin="round"/>')
o.append(f'<path d="M {ax} {ay} L {cx} {cy} L {dx} {dy} L {bx} {by}" fill="none" stroke="{GRN}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>')
for (x,y),l in (((ax,ay),"0,1"),((bx,by),"0,2"),((cx,cy),"1,1"),((dx,dy),"1,2")):
    o.append(f'<circle cx="{x}" cy="{y}" r="17" fill="#FFFFFF" stroke="{BLU}" stroke-width="2.4"/><text class="ms" x="{x}" y="{y+4}" text-anchor="middle" style="font-size:10.5px">{l}</text>')
o+=[f'<text class="nb" x="20" y="{by-40}" style="fill:{RED}">slow edge (left): weight w</text>',
    f'<text class="nb" x="20" y="{ay+50}" style="fill:{GRN}">around it: 1 + 1 + 1 = 3</text>']
b+=o
X=330; rows=[("w = 2","the slow edge is cheaper",RED),("w = 3","a tie: 3 and 3",AMB),("w = 4 or more","going around is cheaper",GRN)]
b.append(f'<text class="h" x="{X}" y="74">Compare w with 3</text>')
for i,(a,t,c) in enumerate(rows):
    y=100+i*48
    b.append(f'<rect x="{X}" y="{y}" width="320" height="38" rx="8" fill="#FFFFFF" stroke="{c}" stroke-width="2"/>')
    b.append(f'<text class="m" x="{X+14}" y="{y+24}">{a}</text><text class="n" x="{X+132}" y="{y+24}" style="fill:{c};font-weight:700">{t}</text>')
b+=[f'<text class="sm" x="{X}" y="264">Only w = 4 or more makes the two</text>',f'<text class="sm" x="{X}" y="280">planners in this module disagree.</text>']
open(O+'break-even.svg','w').write(svg('Why a weight of three is not enough',
 'Two neighboring intersections on the left edge, (0, 1) and (0, 2) above it, joined by a slow edge of weight w. The way around it goes right to (1, 1), up to (1, 2) and back left: three normal blocks, cost 3. If w is 2 the slow edge is cheaper; if w is 3 the two tie; only if w is 4 or more is going around cheaper.',b,H=300))

# ---------- 6-2 path-cost ----------
b=['<text class="h" x="20" y="26">path_cost((0, 0), [(0, 1), (0, 2), (0, 3)])</text>']
xs=[80,240,400,560]; y=110
labels=["(0, 0)","(0, 1)","(0, 2)","(0, 3)"]
b.append(f'<rect x="{xs[1]-56}" y="{y-60}" width="{xs[3]-xs[1]+112}" height="86" rx="10" fill="#F1F6FB" stroke="{BLU}" stroke-width="1.6" stroke-dasharray="6 4"/>')
b.append(f'<text class="sm" x="{xs[3]+52}" y="{y-44}" text-anchor="end" style="fill:{BLU};font-weight:700">path: what the planner returns</text>')
b.append(f'<text class="sm" x="{xs[0]}" y="{y-44}" text-anchor="middle" style="fill:{NAVY};font-weight:700">position</text>')
for i,(x,l) in enumerate(zip(xs,labels)):
    fill=NAVY if i==0 else "#FFFFFF"; tc="#FFFFFF" if i==0 else NAVY
    b.append(f'<rect x="{x-44}" y="{y-18}" width="88" height="36" rx="8" fill="{fill}" stroke="{NAVY}" stroke-width="2"/><text class="m" x="{x}" y="{y+5}" text-anchor="middle" style="fill:{tc}">{l}</text>')
w=[1,5,1]; tot=[1,6,7]
for i in range(3):
    xa,xb=xs[i]+46,xs[i+1]-46; c=RED if w[i]==5 else BLU
    b.append(f'<line x1="{xa}" y1="{y}" x2="{xb-4}" y2="{y}" stroke="{c}" stroke-width="3" marker-end="url(#a{"R" if c==RED else "B"})"/>')
    b.append(tag((xa+xb)/2,y+46+0,f"weight {w[i]}",stroke=c))
    b.append(f'<text class="n" x="{(xa+xb)/2}" y="{y+90}" text-anchor="middle">total = <tspan class="m">{tot[i]}</tspan></text>')
    b.append(f'<text class="sm" x="{(xa+xb)/2}" y="{y+110}" text-anchor="middle">here moves to {labels[i+1]}</text>')
b.append(f'<text class="sm" x="20" y="{y+90}">total</text><text class="sm" x="20" y="{y+106}">starts 0</text>')
yb=y+150
b.append(f'<rect x="20" y="{yb}" width="640" height="56" rx="10" fill="#FDECEE" stroke="{RED}" stroke-width="1.6"/>')
b.append(f'<text class="nb" x="36" y="{yb+23}" style="fill:{RED}">Start the loop at path[0] instead of position</text>')
b.append(f'<text class="n" x="36" y="{yb+43}">and the first segment, (0, 0) to (0, 1), is never added: 6 instead of 7.</text>')
open(O+'path-cost.svg','w').write(svg('Adding up a route',
 'path_cost from position (0, 0) along the path (0, 1), (0, 2), (0, 3). The position is not part of the path, but the first segment starts there. Segment weights are 1, 5 and 1; the running total goes 1, 6, 7 as here moves along the path. A warning: starting the loop at path[0] instead of position misses the first segment and gives 6 instead of 7.',b,H=330))

# ---------- 6-3 closest vs oldest ----------
sp=72; gx,gy=70,92
P=lambda a,b:(gx+a*sp,gy+(3-b)*sp)
done={(0,0):0,(1,0):1,(0,1):1,(2,0):2,(1,1):2}
wait=[((0,2),6),((3,0),3),((2,1),3),((1,2),3)]
b=['<text class="h" x="20" y="26">Halfway through the search</text>']
for r in range(4):
    for c in range(4):
        for dr,dc in ((0,1),(1,0)):
            r2,c2=r+dr,c+dc
            if r2>3 or c2>3: continue
            (x1,y1),(x2,y2)=P(r,c),P(r2,c2)
            if {(r,c),(r2,c2)}=={(0,1),(0,2)}:
                b.append(f'<path d="{poly(wigseg((x1,y1),(x2,y2),amp=12,waves=3))}" fill="none" stroke="{RED}" stroke-width="3.5"/>')
                b.append(tag(x1-30,(y1+y2)/2,"5",stroke=RED))
            else: b.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#ADB5BD" stroke-width="3"/>')
wd=dict(wait)
for r in range(4):
    for c in range(4):
        x,y=P(r,c)
        if (r,c) in done: f,s,t,tc=(BLU,BLU,str(done[(r,c)]),"#FFFFFF")
        elif (r,c) in wd: f,s,t,tc=("#FFF0D1",AMB,str(wd[(r,c)]),NAVY)
        else: f,s,t,tc=("#FFFFFF","#CED4DA","","")
        b.append(f'<circle cx="{x}" cy="{y}" r="16" fill="{f}" stroke="{s}" stroke-width="2.4"/>')
        if t: b.append(f'<text class="m" x="{x}" y="{y+4.5}" text-anchor="middle" style="fill:{tc}">{t}</text>')
ly=gy+3*sp+42
b+=[f'<circle cx="34" cy="{ly}" r="8" fill="{BLU}"/><text class="sm" x="48" y="{ly+4}">done</text>',
    f'<circle cx="108" cy="{ly}" r="8" fill="#FFF0D1" stroke="{AMB}" stroke-width="2"/><text class="sm" x="122" y="{ly+4}">on to_visit, with its cost so far</text>']
X=362
b.append(f'<text class="h" x="{X}" y="64">to_visit, oldest first</text>')
for i,((r,c),d) in enumerate(wait):
    y=82+i*42; hl=(r,c)==(3,0); old=i==0
    st=GRN if hl else (RED if old else AMB)
    b.append(f'<rect x="{X}" y="{y}" width="150" height="34" rx="7" fill="#FFFFFF" stroke="{st}" stroke-width="{2.6 if (hl or old) else 1.6}"/>')
    b.append(f'<text class="m" x="{X+14}" y="{y+22}">({r}, {c})</text><text class="ms" x="{X+138}" y="{y+22}" text-anchor="end">cost {d}</text>')
b.append(f'<path d="M {X+156} 99 L {X+180} 99" stroke="{RED}" stroke-width="2.4" marker-start="url(#aR)"/>')
b+=[f'<text class="nb" x="{X+186}" y="96" style="fill:{RED}">pop(0): the oldest</text>',f'<text class="sm" x="{X+186}" y="112">cost 6, by the slow road</text>']
b.append(f'<path d="M {X+156} 141 L {X+180} 141" stroke="{GRN}" stroke-width="2.4" marker-start="url(#aGr)"/>')
b+=[f'<text class="nb" x="{X+186}" y="138" style="fill:{GRN}">closest(): cheapest</text>',f'<text class="sm" x="{X+186}" y="154">first of the cost-3 entries</text>']
b+=[f'<text class="n" x="{X}" y="276">(0, 2) waits. Before its turn comes,</text>',
    f'<text class="n" x="{X}" y="295">(1, 2) reaches it for 3 + 1 = <tspan class="m">4</tspan>, and</text>',
    f'<text class="n" x="{X}" y="314">change 2 replaces the 6.</text>']
open(O+'closest-vs-oldest.svg','w').write(svg('Closest first, not oldest first',
 'Dijkstra from (0, 0), the bottom-left, on the 4 by 4 grid with the slow edge between (0, 1) and (0, 2) at weight 5, partway through. Five intersections are done, with costs 0, 1, 1, 2 and 2. Four are waiting on to_visit, oldest first: (0, 2) at cost 6, reached by the slow road, then (3, 0), (2, 1) and (1, 2) at cost 3. pop(0) would take (0, 2), the oldest; closest() takes (3, 0), the first of the cheapest. (0, 2) waits, and before its turn (1, 2) reaches it for 4, which replaces the 6.',b,H=372))

# ---------- 6-3 cost grid ----------
cost=[[0,1,4,5],[1,2,3,4],[2,3,4,5],[3,4,5,6]]
sp=74; gx,gy=70,80
P=lambda a,b:(gx+a*sp,gy+(3-b)*sp)
b=['<text class="h" x="20" y="26">dijkstra_distances((0, 0))</text>']
for r in range(4):
    for c in range(4):
        for dr,dc in ((0,1),(1,0)):
            r2,c2=r+dr,c+dc
            if r2>3 or c2>3: continue
            (x1,y1),(x2,y2)=P(r,c),P(r2,c2)
            if {(r,c),(r2,c2)}=={(0,1),(0,2)}:
                b.append(f'<path d="{poly(wigseg((x1,y1),(x2,y2),amp=12,waves=3))}" fill="none" stroke="{RED}" stroke-width="3.5" opacity="0.8"/>')
            else: b.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#CED4DA" stroke-width="3"/>')
pts=[P(*q) for q in [(0,0),(1,0),(1,1),(1,2),(0,2)]]
b.append(f'<path d="{poly(pts)}" fill="none" stroke="{GRN}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round" opacity="0.55"/>')
for r in range(4):
    for c in range(4):
        x,y=P(r,c); hl=(r,c)==(0,2)
        b.append(f'<circle cx="{x}" cy="{y}" r="{19 if hl else 17}" fill="{"#E8F5E9" if hl else "#FFFFFF"}" stroke="{GRN if hl else BLU}" stroke-width="{3 if hl else 2.2}"/>')
        b.append(f'<text class="m" x="{x}" y="{y+5}" text-anchor="middle" style="font-size:14px">{cost[r][c]}</text>')
X=380
b.append(f'<text class="h" x="{X}" y="64">Why (0, 2) is 4, not 2</text>')
b+=card(X,82,280,60,RED,[("nb","By the slow road"),("m","1 + 5 = 6")])
b+=card(X,160,280,60,GRN,[("nb","Right, up, back left"),("m","1 + 1 + 1 + 1 = 4")])
b+=[f'<text class="n" x="{X}" y="250">4 is cheaper, so 4 is kept.</text>',
    f'<text class="sm" x="{X}" y="276">Every other number is the step count:</text>',
    f'<text class="sm" x="{X}" y="292">Module 5\'s BFS rings.</text>']
open(O+'cost-grid.svg','w').write(svg('Reading the cost grid',
 'The 4 by 4 grid with (0, 0) at the bottom-left, each intersection labeled by its cheapest cost from (0, 0). Read row by row from the far side: y = 3 is 5, 4, 5, 6; y = 2 is 4, 3, 4, 5; y = 1 is 1, 2, 3, 4; y = 0 is 0, 1, 2, 3. The slow edge between (0, 1) and (0, 2), on the left edge, is drawn as a red wiggle. (0, 2) is highlighted: by the slow road it would cost 1 + 5 = 6, but right to x = 1, up and back left costs 1 + 1 + 1 + 1 = 4, so 4 is kept. Every other number equals the step count, the Module 5 BFS rings.',b,H=340))

# ---------- 6-4 cost predicts seconds ----------
b=['<text class="h" x="20" y="26">Predict the stopwatch from the cost</text>']
b.append(f'<text class="sm" x="20" y="46">With Lesson 6-1\'s example times: one normal block about 4.1 s. Use your own.</text>')
rows=[("BFS",3,7,RED),("Dijkstra",5,5,GRN)]
X0=150; unit=56
for i,(n,st,c,col) in enumerate(rows):
    y=86+i*96
    b.append(f'<text class="nb" x="20" y="{y+6}" style="fill:{col}">{n}</text>')
    b.append(f'<text class="sm" x="20" y="{y+24}">{st} steps</text>')
    if n=="BFS": segs=[1,5,1]
    else: segs=[1,1,1,1,1]
    x=X0
    for wv in segs:
        wd=wv*unit
        b.append(f'<rect x="{x}" y="{y-12}" width="{wd-4}" height="28" rx="5" fill="{"#FDECEE" if wv==5 else "#F1F6FB"}" stroke="{RED if wv==5 else BLU}" stroke-width="1.6"/>')
        b.append(f'<text class="ms" x="{x+(wd-4)/2}" y="{y+6}" text-anchor="middle">{wv}</text>')
        x+=wd
    b.append(f'<text class="n" x="{X0}" y="{y+40}">cost {c} × 4.1 s ≈ <tspan class="m" style="fill:{col}">{int(c*4.1+0.5)} s</tspan></text>')
b.append(f'<line x1="{X0+5*unit}" y1="60" x2="{X0+5*unit}" y2="250" stroke="{GRN}" stroke-width="1.6" stroke-dasharray="4 4"/>')
b.append(f'<line x1="{X0+7*unit}" y1="60" x2="{X0+7*unit}" y2="250" stroke="{RED}" stroke-width="1.6" stroke-dasharray="4 4"/>')
b.append(f'<text class="sm" x="{X0}" y="274">one box = one segment; its width is its weight, so the bar\'s length is the drive\'s time</text>')
open(O+'cost-to-seconds.svg','w').write(svg('Cost predicts the stopwatch',
 'Two bars made of segments whose widths are their weights. BFS: 3 steps with weights 1, 5 and 1, cost 7, about 29 seconds at 4.1 seconds a block. Dijkstra: 5 steps of weight 1, cost 5, about 21 seconds. More steps, shorter bar. The times use Lesson 6-1\'s example; students use their own.',b,H=290))

# ---------- 6-5 three planners ----------
b=[]
b.append('<rect x="150" y="20" width="380" height="104" rx="12" fill="#F1F6FB" stroke="#22527B" stroke-width="2"/>')
b.append('<text class="m" x="340" y="46" text-anchor="middle">run_all_tests(name, planner)</text>')
b.append('<text class="sm" x="340" y="64" text-anchor="middle">seven cases; never names a class</text>')
b.append('<rect x="186" y="76" width="308" height="34" rx="8" fill="#FFFFFF" stroke="#22527B" stroke-width="2" stroke-dasharray="6 4"/>')
b.append('<text class="ms" x="340" y="98" text-anchor="middle">planner.compute_path(position, destination)</text>')
meth=["compute_path()","add_blocked()","clear_blocked()","add_slow_edge()","clear_slow_edges()"]
cols=[("Manhattan()",AMB,[1,0,0,0,0],"4 of 7"),("BFS()",BLU,[1,1,1,0,0],"6 of 7"),("Dijkstra()",GRN,[1,1,1,1,1],"7 of 7")]
for k,(n,col,use,res) in enumerate(cols):
    x=20+k*222; y=170
    b.append(f'<path d="M {x+100} {y-2} C {x+100} {y-30}, 340 {y-20}, 340 116" fill="none" stroke="{col}" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#aG)"/>')
    b.append(f'<rect x="{x}" y="{y}" width="200" height="164" rx="10" fill="#FFFFFF" stroke="{col}" stroke-width="2"/>')
    b.append(f'<text class="m" x="{x+100}" y="{y+24}" text-anchor="middle" style="fill:{col}">{n}</text>')
    for j,m in enumerate(meth):
        yy=y+50+j*22
        if use[j]: b.append(f'<text class="ms" x="{x+14}" y="{yy}">{m}</text>')
        else: b.append(f'<text class="ms" x="{x+14}" y="{yy}" style="fill:#ADB5BD">{m}</text><text class="sm" x="{x+188}" y="{yy}" text-anchor="end" style="font-style:italic">pass</text>')
    b.append(f'<text class="nb" x="{x+100}" y="{y+192}" text-anchor="middle" style="fill:{col}">{res} passed</text>')
b.append('<text class="sm" x="340" y="390" text-anchor="middle">Same five method names on all three. Gray ones accept the call and do nothing.</text>')
open(O+'three-planners.svg','w').write(svg('One harness, three planners',
 'The run_all_tests harness at the top calls planner.compute_path and never names a class. Below, three objects plug into it: Manhattan, BFS and Dijkstra, each with the same five methods: compute_path, add_blocked, clear_blocked, add_slow_edge and clear_slow_edges. Manhattan only really uses compute_path, and its other four are pass; BFS ignores the two slow-edge methods; Dijkstra uses all five. Results: Manhattan 4 of 7, BFS 6 of 7, Dijkstra 7 of 7.',b,H=404))
