import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math; from common import *
def E(s): return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def make(out,title,scenes,note,desc,H=440,n=4,panel_title="In Python",cell=46):
    """scenes: list of dict(code=[lines], start=(a,b) or None, events=[dict(dur,line,vars,move,append,label)], name)"""
    g=G(92,66,sp=88,n=n,pad=36) if n==4 else G(80,70,sp=72,n=n,pad=34)
    P=g.p
    t=0.0; segs=[]   # timeline pieces
    hl=[]; varsv=[]; labels=[]; marker=[]; tags=[]; cells=[]; starts=[]; codes=[]; lens=[]
    for si,sc in enumerate(scenes):
        s0=t
        pos=sc.get('start')
        if pos: marker.append((t,)+P(*pos)); 
        k=0
        for ev in sc['events']:
            a=t; t+=ev.get('dur',1.0)
            if ev.get('line') is not None: hl.append((si,a,t,ev['line']))
            if ev.get('vars'): varsv.append((a,t,ev['vars']))
            if ev.get('label'): labels.append((a,t)+tuple(ev['label']))
            if ev.get('move'):
                marker.append((a+0.05,)+marker[-1][1:]); marker.append((a+min(0.6,ev.get('dur',1)*0.6),)+P(*ev['move']))
            if ev.get('append'):
                ap=ev['append']; tags.append((a+0.3,None,ap,k,si)); cells.append((a+0.3,None,ap,k,si)); k+=1
            lens.append((a,t,k,si))
        s1=t+ev.get('hold',0)
        t=s1+1.6
        if marker: marker.append((t-0.01,)+marker[-1][1:])
        codes.append((s0,t,sc))
        if pos: starts.append((s0,t,pos))
        # close tags/cells for this scene
        for L in (tags,cells):
            for i,x in enumerate(L):
                if x[4]==si and x[1] is None: L[i]=(x[0],t,x[2],x[3],x[4])
        if labels and labels[-1][1]<t and labels[-1][0]>=s0: labels[-1]=(labels[-1][0],t)+labels[-1][2:]
        if varsv and varsv[-1][0]>=s0: varsv[-1]=(varsv[-1][0],t,varsv[-1][2])
        if lens and lens[-1][0]>=s0: lens[-1]=(lens[-1][0],t,lens[-1][2],lens[-1][3])
    T=t
    DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
    def vis(t0,t1=None):
        t1=T if t1 is None else t1
        a=max(t0/T,0.0001); b=min(t1/T,0.9999)
        return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{a:.4f};{b:.4f}" calcMode="discrete" {DUR}/>'
    def Gv(t0,t1,inner): return f'<g opacity="0">{vis(t0,t1)}{inner}</g>'
    b=[f'<text class="h" x="20" y="22">{title}</text>']
    b+=g.base(axes=True,north=False)
    anim=[]
    for (a,c,pos) in starts:
        x,y=P(*pos); anim.append(Gv(a,c,f'<circle cx="{x}" cy="{y}" r="16" fill="none" stroke="#2E7D32" stroke-width="3"/><text class="ms halo" x="{x-20}" y="{y+28}" style="fill:#2E7D32">start {pos[0]}, {pos[1]}</text>'.replace(f'start {pos[0]}, {pos[1]}',f'start ({pos[0]}, {pos[1]})')))
    for (a,c,ap,k,si) in tags:
        x,y=P(*ap); anim.append(Gv(a,c,f'<circle cx="{x}" cy="{y}" r="11" fill="#22527B"/><text class="ms" x="{x}" y="{y+4}" text-anchor="middle" style="fill:#FFFFFF">{k}</text>'))
    # marker
    if marker:
        mk=sorted(marker,key=lambda m:m[0])
        if mk[0][0]>0: mk.insert(0,(0.0,)+mk[0][1:])
        mk.append((T,)+mk[-1][1:])
        keys=";".join(f"{m[0]/T:.5f}" for m in mk); vals=";".join(f"{m[1]:.1f} {m[2]:.1f}" for m in mk)
        anim.append(f'<g><animateTransform attributeName="transform" type="translate" values="{vals}" keyTimes="{keys}" {DUR}/><circle r="8" fill="#D1182C" stroke="#FFFFFF" stroke-width="2"/></g>')
    X=430
    b.append(f'<text class="h" x="{X}" y="58">{panel_title}</text>')
    CB=70
    maxl=max(len(sc['code']) for sc in scenes)
    CH=maxl*18+14
    b.append(f'<rect x="{X-6}" y="{CB}" width="246" height="{CH}" rx="8" fill="#F8F9FA" stroke="#ADB5BD"/>')
    hlg=[]
    for si,(a,c,sc) in enumerate(codes):
        for li in range(len(sc['code'])):
            iv=[(p,q) for (s,p,q,l) in hl if s==si and l==li]
            if not iv: continue
            ks=[0.0]; vs=[0]
            for (p,q) in iv: ks+=[p/T,min(q/T,0.9999)]; vs+=[1,0]
            hlg.append(f'<rect x="{X-3}" y="{CB+5+li*18}" width="240" height="18" rx="3" fill="#FDECEE" stroke="#D1182C" stroke-width="1" opacity="0"><animate attributeName="opacity" values="{";".join(map(str,vs))}" keyTimes="{";".join(f"{k:.5f}" for k in ks)}" calcMode="discrete" {DUR}/></rect>')
    b.append('<g class="anim">'+''.join(hlg)+'</g>')
    for (a,c,sc) in codes:
        inner=''.join(f'<text class="ms" x="{X+3}" y="{CB+18+i*18}" style="white-space:pre">{E(l)}</text>' for i,l in enumerate(sc['code']))
        anim.append(Gv(a,c,inner)) if len(codes)>1 else b.append(inner)
    VB=CB+CH+8
    for (a,c,v) in varsv:
        anim.append(Gv(a,c,f'<text class="m" x="{X}" y="{VB+14}" style="white-space:pre">{v}</text>'))
    LB=VB+26
    b.append(f'<text class="ms" x="{X}" y="{LB+14}">path =</text>')
    for (a,c,ap,k,si) in cells:
        cx=X+50+(k%5)*cell; cy=LB+(k//5)*44
        anim.append(Gv(a,c,f'<rect x="{cx}" y="{cy}" width="{cell-3}" height="22" rx="4" fill="#FFFFFF" stroke="#22527B" stroke-width="1.6"/><text class="ms" x="{cx+(cell-3)/2}" y="{cy+15}" text-anchor="middle">({ap[0]},{ap[1]})</text><text class="sm" x="{cx+(cell-3)/2}" y="{cy+35}" text-anchor="middle">[{k}]</text>'))
    for (a,c,k,si) in lens:
        if k==0: anim.append(Gv(a,c,f'<text class="ms" x="{X+50}" y="{LB+14}">[ ]  empty</text>'))
    RB=LB+92
    for (a,c,t1_,s1_,col) in labels:
        anim.append(Gv(a,c,f'<rect x="{X-6}" y="{RB}" width="246" height="52" rx="10" fill="#FFFFFF" stroke="{col}" stroke-width="2"/><text class="nb" x="{X+8}" y="{RB+22}" style="fill:{col}">{E(t1_)}</text><text class="sm" x="{X+8}" y="{RB+40}">{E(s1_)}</text>'))
    for i,ln in enumerate(note): b.append(f'<text class="sm" x="{X-6}" y="{RB+72+i*15}">{ln}</text>')
    b.append('<g class="anim">'+''.join(anim)+'</g>')
    still=''.join(f'<text class="ms" x="{X+3}" y="{CB+18+i*18}" style="white-space:pre">{E(l)}</text>' for i,l in enumerate(scenes[0]['code'])) if len(codes)>1 else ''
    b.append(f'<g class="still">{still}</g>')
    style_extra='<style>.halo{paint-order:stroke;stroke:#FFFFFF;stroke-width:5px;stroke-linejoin:round} .still{display:none} @media (prefers-reduced-motion: reduce){.anim{display:none}.still{display:inline}}</style>'
    H=max(H,RB+72+len(note)*15)
    o=svg(title,desc,b,H=H).replace('<rect width="680"',style_extra+'\n  <rect width="680"',1)
    open(out,'w').write(o); print(out,round(T,1),'H',H)
