import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math; from common import *
CX,CY,R=215,210,138; S=0.42; SENS=60*S; SPEED=95.0; TURNRATE=150.0
def fwd(r): a=math.radians(r); return (math.sin(a),-math.cos(a))
def make(out, title, heading0, angles, LINES, states, labelfn, note, desc, either=False):
    """states: dict name -> (first_line, last_line) to highlight."""
    frames=[]; t=0.0; segs=[]; hls=[]; reads=[]; labels=[]; rings=[]
    x,y,h=CX,CY,heading0
    def add(): frames.append((t,x,y,h))
    add(); t+=0.6; add()
    for bi,ang in enumerate(angles):
        ux,uy=fwd(h); px,py=x+SENS*ux-CX, y+SENS*uy-CY
        bq=px*ux+py*uy; cq=px*px+py*py-(R-3)**2
        d=-bq+math.sqrt(bq*bq-cq)
        assert d>20, (bi, d)
        dur=d/SPEED; t0=t
        hls.append((t0,t0+dur,'drive')); reads.append((t0,t0+dur,0.20,False))
        labels.append((t0,t0+dur,"Driving forward","no line yet: the else branch","#22527B"))
        x0,y0=x,y; x,y=x+ux*d,y+uy*d; t+=dur; add()
        segs.append((t0,t,x0,y0,x,y))
        sx,sy=x+SENS*ux,y+SENS*uy
        tb=t
        hls.append((t,t+0.35,'if')); t+=0.35
        hls.append((t,t+0.7,'stop')); t+=0.7; add()
        n=12; td=abs(ang)/TURNRATE; tt=t
        hls.append((t,t+td,'turn'))
        h0=h
        for i in range(1,n+1): t+=td/n; h=h0-ang*i/n; add()   # counterclockwise
        t+=0.25; add()
        reads.append((tb,t,0.84,True))
        rings.append((tb,tt+0.3,sx,sy))
        tl,sub=labelfn(bi,ang)
        labels.append((tb,t,tl,sub,"#D1182C"))
    T=t+0.4; t=T; add()
    keys=";".join(f"{f[0]/T:.4f}" for f in frames)
    tr=";".join(f"{f[1]:.1f} {f[2]:.1f}" for f in frames)
    ro=";".join(f"{f[3]:.1f}" for f in frames)
    DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
    def vis(t0,t1):
        a=max(t0/T,0.0001); b=min(t1/T,0.9999)
        return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{a:.4f};{b:.4f}" calcMode="discrete" {DUR}/>'
    b=[f'<text class="h" x="20" y="26">{title}</text>']
    b.append('<rect x="20" y="40" width="390" height="340" rx="10" fill="#F3F4F6" stroke="#DEE2E6"/>')
    b.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="#FFFFFF" stroke="#2B2B2B" stroke-width="10"/>')
    anim=[]; still=[]
    # trail: each segment draws itself while the robot drives it, and stays for the rest of the cycle
    for (a,c,x0,y0,x1,y1) in segs:
        L=math.hypot(x1-x0,y1-y0)
        anim.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="#4C8BF5" stroke-width="3" stroke-linecap="round" opacity="0.55" stroke-dasharray="{L:.1f} {L+10:.1f}" stroke-dashoffset="{L:.1f}">'
                    f'<animate attributeName="stroke-dashoffset" values="{L:.1f};{L:.1f};0;0" keyTimes="0;{a/T:.4f};{c/T:.4f};1" {DUR}/></line>')
        still.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="#4C8BF5" stroke-width="3" stroke-linecap="round" opacity="0.55"/>')
    for (t0,t1,sx,sy) in rings:
        anim.append(f'<g opacity="0">{vis(t0,t1)}<circle cx="{sx:.1f}" cy="{sy:.1f}" r="15" fill="none" stroke="#D1182C" stroke-width="3.2"/></g>')
    anim.append(f'<g><animateTransform attributeName="transform" type="translate" values="{tr}" keyTimes="{keys}" {DUR}/>'
                f'<g><animateTransform attributeName="transform" type="rotate" values="{ro}" keyTimes="{keys}" {DUR}/>'
                f'<use href="#pcXRP" transform="scale({S})"/></g></g>')
    X=430
    b.append(f'<text class="h" x="{X}" y="60">What your test does</text>')
    LY=lambda i: 86+i*21
    hlg=[]
    for name,(l0,l1) in states.items():
        iv=[(a,c) for (a,c,s) in hls if s==name]
        ks=[0.0]; vs=[0]
        for (a,c) in iv: ks+=[a/T,min(c/T,0.9999)]; vs+=[1,0]
        hlg.append(f'<rect x="{X-6}" y="{LY(l0)-15}" width="246" height="{20+21*(l1-l0)}" rx="4" fill="#FDECEE" stroke="#D1182C" stroke-width="1.2" opacity="0">'
                   f'<animate attributeName="opacity" values="{";".join(map(str,vs))}" keyTimes="{";".join(f"{k:.4f}" for k in ks)}" calcMode="discrete" {DUR}/></rect>')
    b.append('<g class="anim">'+''.join(hlg)+'</g>')
    for i,(ind,txt) in enumerate(LINES):
        b.append(f'<text class="ms" x="{X+4+ind*16}" y="{LY(i)}">{txt}</text>')
    BY=86+len(LINES)*21+4
    b.append(f'<rect x="{X-6}" y="{BY}" width="246" height="50" rx="8" fill="#F8F9FA" stroke="#ADB5BD"/>')
    for (t0,t1,v,on) in reads:
        col="#D1182C" if on else "#2E7D32"
        anim.append(f'<g opacity="0">{vis(t0,t1)}<text class="m" x="{X+6}" y="{BY+20}">{("left, right = "+format(v,".2f")+", "+format(0.2 if on else v,".2f")) if either else ("get_left() = "+format(v,".2f"))}</text>'
                    f'<text class="ms" x="{X+6}" y="{BY+40}">{"is_either_on_line():" if either else "sees the line?"} <tspan style="fill:{col};font-weight:700">{"True: bounce" if on else "False: drive"}</tspan></text></g>')
    LBY=BY+64
    for (t0,t1,txt,sub,col) in labels:
        anim.append(f'<g opacity="0">{vis(t0,t1)}<rect x="{X-6}" y="{LBY}" width="246" height="54" rx="10" fill="#FFFFFF" stroke="{col}" stroke-width="2"/>'
                    f'<text class="nb" x="{X+8}" y="{LBY+23}" style="fill:{col}">{txt}</text><text class="sm" x="{X+8}" y="{LBY+42}">{sub}</text></g>')
    for i,ln in enumerate(note):
        b.append(f'<text class="sm" x="{X-6}" y="{LBY+74+i*15}">{ln}</text>')
    still.append(f'<use href="#pcXRP" transform="translate({CX} {CY}) rotate({heading0}) scale({S})"/>')
    still.append(f'<rect x="{X-6}" y="{LBY}" width="246" height="54" rx="10" fill="#FFFFFF" stroke="#22527B" stroke-width="2"/><text class="nb" x="{X+8}" y="{LBY+23}">Drive, bounce, repeat</text><text class="sm" x="{X+8}" y="{LBY+42}">the blue lines are its path</text>')
    b.append('<g class="anim">'+''.join(anim)+'</g>')
    b.append('<g class="still">'+''.join(still)+'</g>')
    H=max(400,LBY+74+len(note)*15)
    style_extra='<style>.still{display:none} @media (prefers-reduced-motion: reduce){.anim{display:none}.still{display:inline}}</style>'
    o=svg(title,desc,b,H=H)
    o=o.replace('<rect width="680"',style_extra+'\n  <rect width="680"',1)
    open(out,'w').write(o)
    print(out, round(T,2), 'H', H)
