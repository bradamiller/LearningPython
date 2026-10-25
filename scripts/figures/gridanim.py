import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math; from common import *
S=0.42; SENS=60*S; SPEED=90.0; PAUSE=1.0
def make(out, title, g, runs, note, desc, H=410, panel_title="What your test does", extra=None):
    """runs: list of dict(start=(a,b), heading=deg, lines=[(indent,text)], steps=[(op,line,label,sub)], name=str)
       op: 'track','past','cw','ccw','hold'"""
    marks={}
    frames=[]; t=0.0; hls=[]; labels=[]; flashes=[]; trails=[]; fades=[]; panels=[]
    def P(a,b): return g.p(a,b)
    for ri,run in enumerate(runs):
        x,y=P(*run['start']); h=run['heading']
        if ri==0: frames.append((0.0,x,y,h))
        else:
            fades.append((t,t+0.3)); t+=0.3; frames.append((t,frames[-1][1],frames[-1][2],frames[-1][3]))
            t+=0.01; frames.append((t,x,y,h)); t+=0.3; frames.append((t,x,y,h))
        tr0=t; trail=[(x,y)]
        t+=0.6; frames.append((t,x,y,h))
        run_t0=t
        for st in run['steps']:
            op,li,lab=st[0],st[1],st[2]; sub=st[3] if len(st)>3 else ''
            hd=st[4] if len(st)>4 else (sub if isinstance(sub,(int,float)) else 0.9)
            t0=t
            ux,uy=math.sin(math.radians(h)),-math.cos(math.radians(h))
            if op=='track':
                # distance until sensors reach next intersection ahead
                sx,sy=x+SENS*ux,y+SENS*uy
                best=None
                for a in range(-1,g.n+1):
                    for b in range(-1,g.n+1):
                        if not (0<=a<g.n and 0<=b<g.n): continue
                        ix,iy=P(a,b); d=(ix-sx)*ux+(iy-sy)*uy
                        perp=abs((ix-sx)*uy-(iy-sy)*ux)
                        if d>4 and perp<3 and (best is None or d<best): best=d
                n=max(3,int(best/6)); dur=best/SPEED
                for i in range(1,n+1):
                    t+=dur/n; frames.append((t,x+ux*best*i/n,y+uy*best*i/n,h))
                x,y=x+ux*best,y+uy*best; trail.append((x,y))
                flashes.append((t,t+0.8*PAUSE,x+SENS*ux,y+SENS*uy)); t+=0.35*PAUSE; frames.append((t,x,y,h))
            elif op=='past':
                n=6; dur=SENS/SPEED
                for i in range(1,n+1):
                    t+=dur/n; frames.append((t,x+ux*SENS*i/n,y+uy*SENS*i/n,h))
                x,y=x+ux*SENS,y+uy*SENS; trail.append((x,y)); t+=0.2*PAUSE; frames.append((t,x,y,h))
            elif op in ('cw','ccw'):
                s=1 if op=='cw' else -1
                t+=0.2*PAUSE; frames.append((t,x,y,h))
                for i in range(1,7): t+=0.45*PAUSE/6; frames.append((t,x,y,h+s*60*i/6))
                for i in range(1,5): t+=0.4*PAUSE/4; frames.append((t,x,y,h+s*(60+30*i/4)))
                h+=s*90; t+=0.3*PAUSE; frames.append((t,x,y,h))
            elif op=='mark':
                marks[lab]=t; continue
            elif op=='hold':
                t+=hd; frames.append((t,x,y,h))
            if li is not None: hls.append((ri,t0,t,li))
            if lab: labels.append((t0,t,lab,sub if isinstance(sub,str) else "",run.get('col',"#22527B")))
        done=run.get('done',("Done","",""))
        t0=t; t+=2.2; frames.append((t,x,y,h))
        labels.append((t0,t,done[0],done[1],"#2E7D32"))
        trails.append((run_t0,t,trail))
        panels.append((tr0,t,run))
    T=t
    keys=";".join(f"{f[0]/T:.5f}" for f in frames)
    trs=";".join(f"{f[1]:.1f} {f[2]:.1f}" for f in frames)
    ros=";".join(f"{f[3]:.1f}" for f in frames)
    DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
    def vis(t0,t1):
        a=max(t0/T,0.0001); b=min(t1/T,0.9999)
        return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{a:.5f};{b:.5f}" calcMode="discrete" {DUR}/>'
    b=[f'<text class="h" x="20" y="26">{title}</text>']
    b+=g.base(axes=False,north=False)
    anim=[]; still=[]
    if extra: anim+=extra(vis,P,marks,T)
    # trails: polyline drawn progressively, visible for its run
    for (t0,t1,pts) in trails:
        # times: approximate even reveal across run
        L=sum(math.hypot(pts[i][0]-pts[i-1][0],pts[i][1]-pts[i-1][1]) for i in range(1,len(pts)))
        if L<1: continue
        d=' '.join(f'{p[0]:.1f},{p[1]:.1f}' for p in pts)
        # reveal tied to robot distance: sample frames within run
        fr=[f for f in frames if t0<=f[0]<=t1]
        acc=0; ks=[0.0]; vs=[L]; prev=None
        for f in fr:
            if prev: acc+=math.hypot(f[1]-prev[1],f[2]-prev[2])
            prev=f; ks.append(f[0]/T); vs.append(max(0,L-acc))
        ks.append(1.0); vs.append(vs[-1])
        anim.append(f'<g opacity="0">{vis(t0,t1)}<polyline points="{d}" fill="none" stroke="#4C8BF5" stroke-width="5" stroke-linejoin="round" stroke-linecap="round" opacity="0.6" stroke-dasharray="{L:.0f} {L+20:.0f}">'
                    f'<animate attributeName="stroke-dashoffset" values="{";".join(f"{v:.0f}" for v in vs)}" keyTimes="{";".join(f"{k:.5f}" for k in ks)}" {DUR}/></polyline></g>')
    for (t0,t1,sx,sy) in flashes:
        anim.append(f'<g opacity="0">{vis(t0,t1)}<circle cx="{sx:.1f}" cy="{sy:.1f}" r="15" fill="none" stroke="#D1182C" stroke-width="3.2"/></g>')
    ok=[0.0]; ov=["1"]
    for (a,c) in fades: ok+=[a/T,c/T,(c+0.01)/T,(c+0.31)/T]; ov+=["1","0","0","1"]
    ok.append(1.0); ov.append("1")
    opa=f'<animate attributeName="opacity" values="{";".join(ov)}" keyTimes="{";".join(f"{k:.5f}" for k in ok)}" {DUR}/>'
    anim.append(f'<g>{opa}<animateTransform attributeName="transform" type="translate" values="{trs}" keyTimes="{keys}" {DUR}/>'
                f'<g><animateTransform attributeName="transform" type="rotate" values="{ros}" keyTimes="{keys}" {DUR}/>'
                f'<use href="#pcXRP" transform="scale({S})"/></g></g>')
    X=430
    b.append(f'<text class="h" x="{X}" y="60">{panel_title}</text>')
    named=any(r.get('name') for r in runs)
    LY=(lambda i: 108+i*21) if named else (lambda i: 86+i*21)
    maxlines=max(len(r['lines']) for r in runs)
    hlg=[]; txt=[]
    for ri,(t0,t1,run) in enumerate(panels):
        for li in range(len(run['lines'])):
            iv=[(a,c) for (r,a,c,l) in hls if r==ri and l==li]
            if not iv: continue
            ks=[0.0]; vs=[0]
            for (a,c) in iv: ks+=[a/T,min(c/T,0.9999)]; vs+=[1,0]
            hlg.append(f'<rect x="{X-6}" y="{LY(li)-15}" width="246" height="20" rx="4" fill="#FDECEE" stroke="#D1182C" stroke-width="1.2" opacity="0">'
                       f'<animate attributeName="opacity" values="{";".join(map(str,vs))}" keyTimes="{";".join(f"{k:.5f}" for k in ks)}" calcMode="discrete" {DUR}/></rect>')
        inner=''.join(f'<text class="ms" x="{X+4+ind*16}" y="{LY(i)}">{tx}</text>' for i,(ind,tx) in enumerate(run['lines']))
        head=f'<text class="ms" x="{X-6}" y="82" style="fill:#D1182C">{run["name"]}</text>' if run.get('name') else ''
        if len(panels)==1: txt.append(head+inner)
        else: txt.append(f'<g opacity="0">{vis(t0,t1)}{head}{inner}</g>')
    b.append('<g class="anim">'+''.join(hlg)+'</g>')
    if len(panels)==1: b.append(txt[0])
    else: anim.append(''.join(txt))
    LBY=LY(maxlines)+8
    for (t0,t1,tx,sub,col) in labels:
        anim.append(f'<g opacity="0">{vis(t0,t1)}<rect x="{X-6}" y="{LBY}" width="246" height="54" rx="10" fill="#FFFFFF" stroke="{col}" stroke-width="2"/>'
                    f'<text class="nb" x="{X+8}" y="{LBY+23}" style="fill:{col}">{tx}</text><text class="sm" x="{X+8}" y="{LBY+42}">{sub}</text></g>')
    for i,ln in enumerate(note):
        b.append(f'<text class="sm" x="{X-6}" y="{LBY+76+i*15}">{ln}</text>')
    r0=runs[0]; sx,sy=P(*r0['start'])
    still.append(f'<use href="#pcXRP" transform="translate({sx:.1f} {sy:.1f}) rotate({r0["heading"]}) scale({S})"/>')
    if len(panels)>1: still.append(''.join(f'<text class="ms" x="{X+4+ind*16}" y="{LY(i)}">{tx}</text>' for i,(ind,tx) in enumerate(r0['lines'])))
    b.append('<g class="anim">'+''.join(anim)+'</g>')
    b.append('<g class="still">'+''.join(still)+'</g>')
    style_extra='<style>.still{display:none} @media (prefers-reduced-motion: reduce){.anim{display:none}.still{display:inline}}</style>'
    H=max(H,LBY+76+len(note)*15)
    o=svg(title,desc,b,H=H)
    o=o.replace('<rect width="680"',style_extra+'\n  <rect width="680"',1)
    open(out,'w').write(o); print(out,round(T,2),'H',H)
