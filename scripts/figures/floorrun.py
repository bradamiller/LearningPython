import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math; from common import *
def make(out,title,runs,note,desc,start=(205,262),side=150.0,S=0.6,panel_title="Your program",H=400):
    """runs: list of dict(name, blocks=[(text, op, val)] or None, cmds=[(op,val,label,sub)], done=(t,sub,col))"""
    frames=[]; t=0.0; labels=[]; hls=[]; trails=[]; fades=[]; names=[]
    for ri,run in enumerate(runs):
        x,y=start; h=0.0
        if ri==0: frames.append((0.0,x,y,h))
        else:
            fades.append(t); t+=0.3; frames.append((t,)+frames[-1][1:]); t+=0.01; frames.append((t,x,y,h)); t+=0.3; frames.append((t,x,y,h))
        r0=t; pts=[(x,y)]; tl=[(t,0.0)]; L=0.0
        t0=t; t+=1.0; frames.append((t,x,y,h)); labels.append((t0,t,"Waiting for the button","press it to start","#6C757D")); hls.append((ri,t0,t,0))
        for bi,(op,val,lab,sub) in enumerate(run['cmds']):
            t0=t
            if op=='S':
                d=side*val/20.0; ux,uy=math.sin(math.radians(h)),-math.cos(math.radians(h)); n=20; dur=2.0*val/20
                for i in range(1,n+1):
                    t+=dur/n; x+=ux*d/n; y+=uy*d/n; L+=d/n; frames.append((t,x,y,h)); tl.append((t,L))
                pts.append((x,y)); col="#22527B"
            else:
                t+=0.2; frames.append((t,x,y,h)); tl.append((t,L)); n=10
                for i in range(1,n+1): t+=abs(val)/90/n; h-=val/n; frames.append((t,x,y,h))
                t+=0.2; frames.append((t,x,y,h)); tl.append((t,L)); col="#D1182C"
            labels.append((t0,t,lab,sub,col)); hls.append((ri,t0,t,run.get('hl',{}).get(bi,bi+1)))
        t0=t; t+=2.6; frames.append((t,x,y,h)); tl.append((t,L))
        labels.append((t0,t)+tuple(run['done']))
        trails.append((r0,t,pts,tl,L)); names.append((r0,t,run))
    T=t
    DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
    def vis(a,b): return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{max(a/T,0.0001):.4f};{min(b/T,0.9999):.4f}" calcMode="discrete" {DUR}/>'
    keys=";".join(f"{f[0]/T:.5f}" for f in frames); trs=";".join(f"{f[1]:.1f} {f[2]:.1f}" for f in frames); ros=";".join(f"{f[3]:.1f}" for f in frames)
    b=[f'<text class="h" x="20" y="26">{title}</text>','<rect x="20" y="40" width="390" height="350" rx="10" fill="#F3F4F6" stroke="#DEE2E6"/>']
    sx,sy=start
    b.append(f'<path d="M {sx-14} {sy} h 28 M {sx} {sy-14} v 28" stroke="#ADB5BD" stroke-width="2"/><text class="sm" x="{sx+30}" y="{sy+50}" style="font-weight:700">start</text>')
    anim=[]
    for (a,c,pts,tl,L) in trails:
        if L<1: continue
        pp=' '.join(f'{p[0]:.1f},{p[1]:.1f}' for p in pts)
        ks=";".join(f"{q/T:.5f}" for q,_ in tl); vs=";".join(f"{L-l:.1f}" for _,l in tl)
        ks="0;"+ks+";1"; vs=f"{L:.1f};"+vs+f";{0:.1f}"
        anim.append(f'<g opacity="0">{vis(a,c)}<polyline points="{pp}" fill="none" stroke="#1F6FEB" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="{L:.0f} {L+20:.0f}"><animate attributeName="stroke-dashoffset" values="{vs}" keyTimes="{ks}" {DUR}/></polyline></g>')
    ok=[0.0]; ov=["1"]
    for a in fades: ok+=[a/T,(a+0.3)/T,(a+0.31)/T,(a+0.61)/T]; ov+=["1","0","0","1"]
    ok.append(1.0); ov.append("1")
    opa=f'<animate attributeName="opacity" values="{";".join(ov)}" keyTimes="{";".join(f"{k:.5f}" for k in ok)}" {DUR}/>'
    anim.append(f'<g>{opa}<animateTransform attributeName="transform" type="translate" values="{trs}" keyTimes="{keys}" {DUR}/><g><animateTransform attributeName="transform" type="rotate" values="{ros}" keyTimes="{keys}" {DUR}/><use href="#pcXRP" transform="scale({S})"/></g></g>')
    X=436
    b.append(f'<text class="h" x="{X}" y="60">{panel_title}</text>')
    LY=lambda i: 108+i*22
    for ri,(a,c,run) in enumerate(names):
        inner=f'<text class="ms" x="{X-6}" y="82" style="fill:#D1182C">{run["name"]}</text>'
        hl=''
        if run.get('blocks'):
            for li,bt in enumerate(run['blocks']):
                iv=[(p,q) for (r,p,q,l) in hls if r==ri and l==li]
                if iv:
                    ks=[0.0]; vs=[0]
                    for (p,q) in iv: ks+=[p/T,min(q/T,0.9999)]; vs+=[1,0]
                    hl+=f'<rect x="{X-6}" y="{LY(li)-15}" width="236" height="20" rx="4" fill="#FDECEE" stroke="#D1182C" stroke-width="1.2" opacity="0"><animate attributeName="opacity" values="{";".join(map(str,vs))}" keyTimes="{";".join(f"{k:.5f}" for k in ks)}" calcMode="discrete" {DUR}/></rect>'
            inner+=''.join(f'<text class="ms" x="{X+4}" y="{LY(i)}">{bt}</text>' for i,bt in enumerate(run['blocks']))
        anim.append(f'<g opacity="0">{vis(a,c)}{hl}{inner}</g>')
    nb=max(len(r.get('blocks') or []) for r in runs)
    LB=LY(nb)+6 if nb else 100
    for (a,c,tx,sub,col) in labels:
        anim.append(f'<g opacity="0">{vis(a,c)}<rect x="{X-6}" y="{LB}" width="236" height="54" rx="10" fill="#FFFFFF" stroke="{col}" stroke-width="2"/><text class="nb" x="{X+8}" y="{LB+23}" style="fill:{col}">{tx}</text><text class="sm" x="{X+8}" y="{LB+42}">{sub}</text></g>')
    for i,l in enumerate(note): b.append(f'<text class="sm" x="{X-6}" y="{LB+76+i*15}">{l}</text>')
    b.append('<g class="anim">'+''.join(anim)+'</g>')
    b.append(f'<g class="still"><use href="#pcXRP" transform="translate({sx} {sy}) scale({S})"/></g>')
    style_extra='<style>.still{display:none} @media (prefers-reduced-motion: reduce){.anim{display:none}.still{display:inline}}</style>'
    o=svg(title,desc,b,H=max(H,LB+76+len(note)*15)).replace('<rect width="680"',style_extra+'\n  <rect width="680"',1)
    open(out,'w').write(o); print(out,round(T,1))
