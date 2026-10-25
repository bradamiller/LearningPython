import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math; from common import *
g=G(92,66,sp=88,n=4,pad=36); P=g.p
L=3*g.sp; BOT=g.y0+L+g.pad
SC=[(0,4.5),(4.5,9.5),(9.5,14.5),(14.5,20.5),(20.5,26.5),(26.5,34.0)]
T=SC[-1][1]
DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
def vis(t0,t1=None):
    t1=T if t1 is None else t1
    a=max(t0/T,0.0001); b=min(t1/T,0.9999)
    return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{a:.4f};{b:.4f}" calcMode="discrete" {DUR}/>'
def G_(t0,t1,inner): return f'<g opacity="0">{vis(t0,t1)}{inner}</g>'
def pill(x,y,text,col="#22527B",fill="#FFFFFF"):
    w=len(text)*7.4+10
    return f'<rect x="{x-w/2:.1f}" y="{y-10:.1f}" width="{w:.1f}" height="20" rx="6" fill="{fill}" stroke="{col}" stroke-width="1.8"/><text class="ms" x="{x:.1f}" y="{y+4:.1f}" text-anchor="middle" style="fill:{col}">{text}</text>'
def seg(p0,p1,col,ta,tb,t1,off=0,w=5):
    (x0,y0),(x1,y1)=p0,p1
    if y0==y1: y0+=off; y1+=off
    else: x0+=off; x1+=off
    Ln=math.hypot(x1-x0,y1-y0)
    return G_(ta,t1,f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="{col}" stroke-width="{w}" stroke-linecap="round" opacity="0.85" stroke-dasharray="{Ln:.0f} 999" stroke-dashoffset="{Ln:.0f}"><animate attributeName="stroke-dashoffset" values="{Ln:.0f};{Ln:.0f};0;0" keyTimes="0;{ta/T:.4f};{tb/T:.4f};1" {DUR}/></line>')
b=['<text class="h" x="20" y="22">A tuple names one intersection</text>']
b+=g.base(axes=True,north=False)
anim=[]
X=430
b.append(f'<text class="h" x="{X}" y="58">In Python</text>')
# code box
CB=70
b.append(f'<rect x="{X-6}" y="{CB}" width="246" height="66" rx="8" fill="#F8F9FA" stroke="#ADB5BD"/>')
def code(t0,t1,lines):
    return G_(t0,t1,''.join(f'<text class="m" x="{X+6}" y="{CB+22+i*20}" style="white-space:pre">{l}</text>' for i,l in enumerate(lines)))
# tuple diagram area
TB=158
def tup(t0,t1,name,a,bb,col="#22527B",hl=None,y=TB,strike=False):
    cells=''
    for i,v in enumerate((a,bb)):
        cx=X+70+i*52
        fill="#FDECEE" if hl==i else "#FFFFFF"
        cells+=f'<rect x="{cx}" y="{y}" width="48" height="36" rx="5" fill="{fill}" stroke="{col}" stroke-width="2"/><text class="m" x="{cx+24}" y="{y+23}" text-anchor="middle" style="font-size:16px;fill:{col}">{v}</text>'
        cells+=f'<text class="sm" x="{cx+24}" y="{y+50}" text-anchor="middle">[{i}] {"x" if i==0 else "y"}</text>'
    inner=f'<text class="ms" x="{X+60}" y="{y+23}" text-anchor="end" style="fill:{col}">{name} =</text>'+cells
    if strike: inner+=f'<line x1="{X+66}" y1="{y-4}" x2="{X+178}" y2="{y+40}" stroke="#D1182C" stroke-width="3"/>'
    return G_(t0,t1,inner)
RB=286
def res(t0,t1,l1,l2="",col="#142D50"):
    return G_(t0,t1,f'<rect x="{X-6}" y="{RB}" width="246" height="56" rx="10" fill="#FFFFFF" stroke="{col}" stroke-width="2"/><text class="nb" x="{X+8}" y="{RB+23}" style="fill:{col}">{l1}</text><text class="sm" x="{X+8}" y="{RB+42}">{l2}</text>')
R="#D1182C"; GR="#2E7D32"; B="#22527B"
# scene 1: make a tuple
s0,s1=SC[0]
anim.append(code(s0,s1,["position = (2, 3)"]))
anim.append(tup(s0+0.6,s1,"position",2,3))
anim.append(G_(s0+1.2,s1,pill(*P(2,3),"(2, 3)",B)))
anim.append(res(s0+1.2,s1,"One value, two numbers","the tuple names the spot (2, 3)"))
# scene 2: index
s0,s1=SC[1]
anim.append(code(s0,s1,["position[0]   # 2","position[1]   # 3"]))
anim.append(tup(s0,s0+2.5,"position",2,3,hl=0)); anim.append(tup(s0+2.5,s1,"position",2,3,hl=1))
anim.append(G_(s0,s1,pill(*P(2,3),"(2, 3)",B)))
anim.append(seg(P(0,0),P(2,0),R,s0+0.4,s0+1.4,s1,off=-5))
anim.append(G_(s0+1.2,s1,f'<text class="ms halo" x="{(P(0,0)[0]+P(2,0)[0])/2}" y="{P(0,0)[1]-20}" text-anchor="middle" style="fill:{R}">[0] = 2 across</text>'))
anim.append(seg(P(2,0),P(2,3),R,s0+2.7,s0+3.9,s1,off=-5))
anim.append(G_(s0+3.7,s1,f'<text class="ms halo" x="{P(2,1.5)[0]-20}" y="{P(2,1.5)[1]+4}" text-anchor="end" style="fill:{R}">[1] = 3 away</text>'))
anim.append(res(s0,s1,"Index 0 is x, index 1 is y","Python counts from zero, like the grid"))
# scene 3: immutable
s0,s1=SC[2]
anim.append(code(s0,s1,["position[0] = 5","# TypeError"]))
anim.append(tup(s0,s1,"position",2,3,hl=0,strike=True))
anim.append(G_(s0,s1,pill(*P(2,3),"(2, 3)",B)))
anim.append(res(s0+0.8,s1,"TypeError","a tuple can't be changed once made",R))
# scene 4: new tuple
s0,s1=SC[3]
anim.append(code(s0,s1,["old_position = (2, 3)","new_position = (2, 4)?"]))
SC4=["old_position = (2, 3)","new_position = (2, 3) ..."]
anim[-1]=code(s0,s1,["old_position = (2, 3)","new_position = (3, 3)"])
anim.append(tup(s0,s1,"old",2,3,col="#6C757D"))
anim.append(tup(s0+1.0,s1,"new",3,3,col=GR,y=TB+64))
anim.append(seg(P(2,3),P(3,3),GR,s0+1.0,s0+1.8,s1,off=0,w=6))
anim.append(G_(s0,s1,pill(*P(2,3),"(2, 3)","#6C757D")))
anim.append(G_(s0+1.8,s1,pill(*P(3,3),"(3, 3)",GR)))
anim.append(res(s0+1.8,s1,"Moving means a new tuple","one step east: x + 1, a new value",GR))
# scene 5: compare
s0,s1=SC[4]
anim.append(code(s0,s1,["(1, 2) == (1, 2)   # True","(1, 2) == (2, 1)   # False"]))
anim.append(G_(s0,s1,pill(*P(1,2),"(1, 2)",B)))
anim.append(G_(s0+0.4,s0+2.8,f'<circle cx="{P(1,2)[0]}" cy="{P(1,2)[1]}" r="20" fill="none" stroke="{GR}" stroke-width="3"/>'))
anim.append(res(s0+0.4,s0+2.8,"True","both parts match, in order: same spot",GR))
anim.append(G_(s0+2.8,s1,pill(*P(2,1),"(2, 1)",R)))
anim.append(res(s0+2.8,s1,"False","same numbers, swapped: another spot",R))
# scene 6: distance
s0,s1=SC[5]
anim.append(code(s0,s1,["x_distance = 2 - 0      # 2","y_distance = 3 - 0      # 3","total_steps = 2 + 3    # 5"]))
anim.append(G_(s0,s1,pill(*P(0,0),"(0, 0)",B)+pill(*P(2,3),"(2, 3)",R)))
anim.append(seg(P(0,0),P(2,0),R,s0+0.6,s0+1.8,s1,off=-5))
anim.append(seg(P(2,0),P(2,3),R,s0+2.2,s0+3.8,s1,off=-5))
for k,(a_,b_) in enumerate([(0.5,0),(1.5,0),(2,0.5),(2,1.5),(2,2.5)]):
    tt=s0+0.9+k*0.65 if k<2 else s0+2.5+(k-2)*0.6
    x,y=P(a_,b_)
    anim.append(G_(tt,s1,f'<circle cx="{x+( -5 if b_==0 else -5)}" cy="{y+(-5 if b_==0 else 0)}" r="10" fill="#FFFFFF" stroke="{R}" stroke-width="2"/><text class="ms" x="{x-5}" y="{y+(-5 if b_==0 else 0)+4}" text-anchor="middle" style="fill:{R}">{k+1}</text>'))
anim.append(res(s0+4.0,s1,"5 steps","start (0, 0) to destination (2, 3)",R))
# scene list
STEPS=["make","index","change?","new one","compare","distance"]
LB=360
for i,(st,(a,c)) in enumerate(zip(STEPS,SC)):
    xx=X-6+(i%3)*84; yy=LB+(i//3)*28
    b.append(f'<rect class="anim" x="{xx}" y="{yy}" width="80" height="22" rx="11" fill="#FDECEE" stroke="#D1182C" stroke-width="1.2" opacity="0">{vis(a,c)}</rect>')
    b.append(f'<text class="sm" x="{xx+40}" y="{yy+15}" text-anchor="middle">{st}</text>')
still=[pill(*P(2,3),"(2, 3)",B), code(0,T,["position = (2, 3)"]).replace('opacity="0"','opacity="1"',1)]
b.append('<g class="anim">'+''.join(anim)+'</g>')
b.append('<g class="still"><text class="m" x="'+str(X+6)+'" y="'+str(CB+22)+'">position = (2, 3)</text>'+pill(*P(2,3),"(2, 3)",B)+'</g>')
style_extra='<style>.halo{paint-order:stroke;stroke:#FFFFFF;stroke-width:5px;stroke-linejoin:round} .still{display:none} @media (prefers-reduced-motion: reduce){.anim{display:none}.still{display:inline}}</style>'
out=svg('A tuple names one intersection',
 'An animation of a 4 by 4 grid, x numbered 0 to 3 along the bottom and y 0 to 3 up the left, with Python beside it. position = (2, 3) makes a tuple of two boxes, 2 at index 0 and 3 at index 1, and labels that intersection. position[0] is 2, drawn as 2 across; position[1] is 3, drawn as 3 away. position[0] = 5 is crossed out with a TypeError: a tuple cannot be changed. Moving one step east makes a new tuple, (3, 3), beside the old (2, 3). (1, 2) == (1, 2) is True, the same spot; (1, 2) == (2, 1) is False, a different spot. Finally the distance from (0, 0) to (2, 3): 2 across plus 3 away, 5 steps, each step numbered on the grid.',b,H=430)
out=out.replace('<rect width="680"',style_extra+'\n  <rect width="680"',1)
open(OUTDIR+'tuple-on-grid.svg','w').write(out); print('ok')
