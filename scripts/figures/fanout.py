import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
# Module 5 / 6: how the search fans out, on a grid bigger than the floor grid so the shape shows.
#   fanout-bfs.svg            (Lesson 5-3)  one button: BFS around a wall
#   fanout-bfs-vs-dijkstra.svg (Lesson 6-3) two buttons: same grid plus a slow road
# Both searches follow the course code exactly: neighbors in the order left, right, down, up;
# BFS numbers a neighbor when it is first reached and stops when the destination is taken off
# the list; Dijkstra takes closest() (first of the cheapest, in list order) and stops the same way.
import json; from common import *
COLS,ROWS=8,6
BLOCKED=[(3,1),(3,2),(3,3),(3,4)]
START,DEST=(0,4),(7,4)
SLOW={frozenset([(2,5),(3,5)]):5, frozenset([(3,5),(4,5)]):5}
SP=42; X0,Y0=52,80
def P(n): return (X0+n[0]*SP, Y0+(ROWS-1-n[1])*SP)
def graph():
    g={}
    for x in range(COLS):
        for y in range(ROWS):
            if (x,y) in BLOCKED: continue
            g[(x,y)]=[n for n in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] if 0<=n[0]<COLS and 0<=n[1]<ROWS and n not in BLOCKED]
    return g
def weight(a,b,slow): return SLOW.get(frozenset([a,b]),1) if slow else 1
def bfs():
    g=graph(); prev={START:None}; ring={START:0}; order=[(START,0)]; q=[START]
    while q:
        c=q.pop(0)
        if c==DEST: break
        for n in g[c]:
            if n not in prev: prev[n]=c; ring[n]=ring[c]+1; order.append((n,ring[n])); q.append(n)
    return prev,order
def dijkstra():
    g=graph(); prev={START:None}; dist={START:0}; q=[START]; done=[]
    while q:
        best=q[0]
        for n in q:
            if dist[n]<dist[best]: best=n
        c=best; q.remove(c); done.append((c,dist[c]))
        if c==DEST: break
        for n in g[c]:
            nd=dist[c]+weight(c,n,True)
            if n not in dist or nd<dist[n]:
                dist[n]=nd; prev[n]=c
                if n not in q: q.append(n)
    return prev,done
def path(prev):
    p=[DEST]
    while prev[p[-1]] is not None: p.append(prev[p[-1]])
    return p[::-1]
RAMP=["#DCEBFB","#C3DBF6","#A8C9F0","#8BB5E8","#6E9FDD","#548ACF","#3E76BF","#2D63AA","#215293","#18437D","#123667","#0E2B55","#0B2247","#091C3C","#071631","#061228","#050F22","#040C1C"]
UNIT=0.42
def build(out,modes_spec,slow,title,desc,panel):
    """modes_spec: list of (label, kind) with kind 'bfs' or 'dij'"""
    segs=[]; t=0.4
    for (label,kind) in modes_spec:
        prev,order=bfs() if kind=='bfs' else dijkstra()
        s0=t; ev=[(s0+0.3+v*UNIT,n,v) for (n,v) in order]
        tf=ev[-1][0]+0.5; pth=path(prev); te=tf+0.12*len(pth)+0.4
        segs.append(dict(label=label,kind=kind,s0=s0,ev=ev,tf=tf,te=te,path=pth,stop=te+1.2,steps=len(pth)-1,
                         cost=sum(weight(a,b,True) for a,b in zip(pth,pth[1:])),seen=len(order)))
        t=te+1.6
    T=t
    DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
    def vis(a,b): return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{max(a/T,0.0001):.5f};{min(b/T,0.9999):.5f}" calcMode="discrete" {DUR}/>'
    def first(b): return f'<animate attributeName="opacity" values="1;0" keyTimes="0;{b/T:.5f}" calcMode="discrete" {DUR}/>'
    b=[f'<text class="h" x="20" y="24">{title}</text>']
    L=(COLS-1)*SP; H=(ROWS-1)*SP
    b.append(f'<rect x="{X0-28}" y="{Y0-28}" width="{L+56}" height="{H+56}" rx="10" fill="#F3F4F6" stroke="#DEE2E6"/>')
    g=graph()
    for a in g:
        for n in g[a]:
            if a<n:
                (x1,y1),(x2,y2)=P(a),P(n)
                if slow and frozenset([a,n]) in SLOW:
                    # red wiggle
                    import math
                    pts=[]; k=14
                    for i in range(k+1):
                        f=i/k; px=x1+(x2-x1)*f; py=y1+(y2-y1)*f+(4*math.sin(f*math.pi*4) if y1==y2 else 0)
                        pts.append(f'{px:.1f},{py:.1f}')
                    b.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#D1182C" stroke-width="3.2"/>')
                else:
                    b.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#ADB5BD" stroke-width="3"/>')
    if slow:
        mx=(P((2,5))[0]+P((4,5))[0])/2
        b.append(f'<text class="sm" x="{mx}" y="{Y0-24}" text-anchor="middle" style="fill:#D1182C;font-weight:700">slow road: 5 per block</text>')
    for n in BLOCKED:
        x,y=P(n); b.append(f'<rect x="{x-11}" y="{y-11}" width="22" height="22" rx="4" fill="#495057"/><path d="M {x-6} {y-6} L {x+6} {y+6} M {x+6} {y-6} L {x-6} {y+6}" stroke="#FFFFFF" stroke-width="2.4"/>')
    for n in g:
        if n in BLOCKED: continue
        x,y=P(n); b.append(f'<circle cx="{x}" cy="{y}" r="11" fill="#FFFFFF" stroke="#ADB5BD" stroke-width="1.6"/>')
    for i in range(COLS): b.append(f'<text class="ax" x="{X0+i*SP}" y="{Y0+H+46}" text-anchor="middle">{i}</text>')
    for j in range(ROWS): b.append(f'<text class="ax" x="{X0-40}" y="{Y0+(ROWS-1-j)*SP+4}" text-anchor="middle">{j}</text>')
    anim=[]
    for sg in segs:
        end=sg['stop']+0.2
        for (te,n,v) in sg['ev']:
            x,y=P(n); col=RAMP[min(v,len(RAMP)-1)]; tc="#FFFFFF" if v>=5 else "#142D50"
            anim.append(f'<g opacity="0">{vis(te,end)}<circle cx="{x}" cy="{y}" r="12" fill="{col}" stroke="#22527B" stroke-width="1.2"/>'
                        f'<text class="ms" x="{x}" y="{y+4}" text-anchor="middle" style="fill:{tc};font-size:11px;font-weight:700">{v}</text></g>')
            # the moment it is reached: an orange ring for one beat
            anim.append(f'<g opacity="0">{vis(te,te+0.6)}<circle cx="{x}" cy="{y}" r="15" fill="none" stroke="#F2A900" stroke-width="3"/></g>')
        pts=[P(n) for n in sg['path']]; Lp=sum(((a[0]-c[0])**2+(a[1]-c[1])**2)**.5 for a,c in zip(pts,pts[1:]))
        pp=" ".join(f"{x},{y}" for x,y in pts[::-1])
        anim.append(f'<g opacity="0">{vis(sg["tf"],end)}<polyline points="{pp}" fill="none" stroke="#D1182C" stroke-width="5" stroke-linejoin="round" stroke-linecap="round" opacity="0.85" stroke-dasharray="{Lp:.0f} {Lp+20:.0f}">'
                    f'<animate attributeName="stroke-dashoffset" values="{Lp:.0f};{Lp:.0f};0;0" keyTimes="0;{sg["tf"]/T:.5f};{sg["te"]/T:.5f};1" {DUR}/></polyline></g>')
    for n,lab in [(START,"S"),(DEST,"D")]:
        x,y=P(n); b.append(f'<circle cx="{x}" cy="{y}" r="15" fill="none" stroke="#142D50" stroke-width="2.4"/><text class="nb" x="{x+(-24 if lab=="S" else 24)}" y="{y+5}" text-anchor="middle">{lab}</text>')
    X=440
    anim.append(f'<g opacity="0">{first(segs[0]["s0"]+0.3)}'+''.join(f'<text class="sm" x="{X}" y="{60+i*16}">{l}</text>' for i,l in enumerate(panel['intro']))+'</g>')
    for sg in segs:
        lines=panel[sg['kind']]
        body=''.join(f'<text class="{c}" x="{X}" y="{y}">{l}</text>' for (c,y,l) in lines)
        anim.append(f'<g opacity="0">{vis(sg["s0"]+0.3,sg["stop"]+0.2)}{body}</g>')
        res=(f'<text class="nb" x="{X}" y="262" style="fill:#D1182C">Path: {sg["steps"]} steps, cost {sg["cost"]}</text>' if slow else
             f'<text class="nb" x="{X}" y="262" style="fill:#D1182C">Path: {sg["steps"]} steps</text>')
        res+=f'<text class="sm" x="{X}" y="280">numbered {sg["seen"]} of {len(g)} intersections</text><text class="sm" x="{X}" y="296">before it could stop</text>'
        anim.append(f'<g opacity="0">{vis(sg["tf"],sg["stop"]+0.2)}{res}</g>')
    b.append('<g>'+''.join(anim)+'</g>')
    modes=[{"label":sg['label'],"start":round(sg['s0'],3),"stop":round(sg['stop'],3)} for sg in segs]
    o=svg(title,desc,b,W=680,H=350)
    attr=(" data-modes='"+json.dumps(modes)+"'") if len(segs)>1 else f' data-hold="{segs[0]["stop"]:.2f}"'
    o=o.replace('<svg xmlns="http://www.w3.org/2000/svg"','<svg xmlns="http://www.w3.org/2000/svg"'+attr,1)
    open(OUTDIR+out,'w').write(o)
    print(out,[(s['label'],s['steps'],s['cost'],s['seen'],round(s['stop'],1)) for s in segs])
bfs_panel=[('h',60,'Breadth-first search'),('n',84,'Numbers = steps from S.'),
           ('sm',108,'Every intersection one step out'),('sm',124,'gets its number before any two'),
           ('sm',140,'steps out does, so the search'),('sm',156,'spreads in even rings, like a'),
           ('sm',172,'ripple. The wall bends the'),('sm',188,'ripple around its end.'),
           ('sm',214,'Orange: just reached. Red: the'),('sm',230,'walk-back from D.')]
dij_panel=[('h',60,"Dijkstra's algorithm"),('n',84,'Numbers = cost from S.'),
           ('sm',108,'It always takes the cheapest'),('sm',124,'intersection next, so the wave'),
           ('sm',140,'spreads by cost, not by steps.'),('sm',156,'On the slow road each block'),
           ('sm',172,'costs 5, and the wave crawls'),('sm',188,'there while it races along'),
           ('sm',204,'the bottom.'),('sm',230,'Orange: just finished.')]
build('fanout-bfs.svg',[("Run BFS",'bfs')],False,'How breadth-first search spreads',
 'An animation of breadth-first search on a grid of 8 by 6 intersections, bigger than the floor grid so the shape shows, with (0, 0) at the bottom-left. A wall of four blocked intersections stands at x = 3 from y = 1 to y = 4, leaving gaps at the top and bottom. The search starts at S, (0, 4), and the destination D is (7, 4), on the other side of the wall. Each intersection lights up with its step count from S the moment the search first reaches it: 1 for the neighbors of S, then 2, then 3, so the numbers spread out from S in even rings, like a ripple. The ripple flows through the gap at the top of the wall and bends around it, and also around the bottom. When D is taken off the list the search stops, and the walk-back from D to S is drawn in red: up, along the top through the gap, and back down to D, 9 steps.',
 dict(intro=['Press Run BFS. The search starts at','S and has to find its way around','the wall to D.'],bfs=bfs_panel))
build('fanout-bfs-vs-dijkstra.svg',[("BFS: counts steps",'bfs'),("Dijkstra: counts cost",'dij')],True,'Steps or cost: how the two searches spread',
 'An animation on a grid of 8 by 6 intersections with (0, 0) at the bottom-left, bigger than the floor grid so the shape shows. A wall of four blocked intersections stands at x = 3 from y = 1 to y = 4, so the only ways past it are the gap along the top row, where the two blocks either side of x = 3 are a slow road costing 5 each, and the gap along the bottom row. S is (0, 4) and D is (7, 4). Two buttons. BFS: each intersection lights up with its step count, the ripple spreads evenly and crosses the slow road as if it were normal, and the path goes over the top: 9 steps, cost 17. Dijkstra: each intersection lights up with its cheapest cost when it is finished; the wave races along the bottom but crawls through the slow road, and reaches D first from below, so the path goes around the bottom: 15 steps, cost 15.',
 dict(intro=['Same grid, plus a slow road through','the top gap. Press each button and','watch how differently they spread.'],bfs=bfs_panel[:1]+[('n',84,'Numbers = steps from S.'),('sm',108,'BFS counts every block as one'),('sm',124,'step, so the slow road looks'),('sm',140,'like any other street. The'),('sm',156,'ripple spreads evenly and goes'),('sm',172,'straight over the top.')],dij=dij_panel))
