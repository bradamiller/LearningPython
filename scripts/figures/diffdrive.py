import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math; from common import *
S=0.75; B=101*S; VMAX=70.0
CASES={
 'straight':dict(l=1.0,r=1.0,start=(340,290),h=0,dur=2.2,desc="both sides forward at the same speed",
                 txt=("Left side: forward","Right side: forward, same speed")),
 'curve':dict(l=1.0,r=0.4,start=(250,240),h=0,dur=4.2,desc="both sides forward, the left side much faster than the right",
                 txt=("Left side: forward, fast","Right side: forward, slow")),
 'pivot':dict(l=0.0,r=1.0,start=(380,230),h=0,dur=3.8,desc="the right side driving forward and the left side stopped",
                 txt=("Left side: stopped","Right side: forward")),
 'spin':dict(l=-1.0,r=1.0,start=(340,195),h=0,dur=2.8,desc="the left side driving backward and the right side forward",
                 txt=("Left side: backward","Right side: forward")),
}
STY_ARROW='fill="#FFFFFF" stroke="#D1182C" stroke-width="3" stroke-linejoin="round"'
def arrow(x,eff):
    """block arrow drawn in robot-local units (before scale) beside a wheel at x; up = forward"""
    if eff==0:
        return f'<g transform="translate({x} 0)"><rect x="-13" y="-13" width="26" height="26" rx="4" fill="#FFFFFF" stroke="#D1182C" stroke-width="3"/><path d="M -7 0 h 14" stroke="#D1182C" stroke-width="4"/></g>'
    L=70*abs(eff); sgn=-1 if eff>0 else 1   # forward is -y
    tip=sgn*(L/2+20); base=-sgn*L/2
    w=9; hw=20
    d=f"M {-w} {base} L {-w} {sgn*L/2} L {-hw} {sgn*L/2} L 0 {tip} L {hw} {sgn*L/2} L {w} {sgn*L/2} L {w} {base} Z"
    return f'<g transform="translate({x} 0)"><path d="{d}" {STY_ARROW}/></g>'
def robot_with_arrows(c):
    # arrows outside the wheels (wheels at +-50.5)
    return f'<use href="#pcXRP"/>{arrow(-80,c["l"])}{arrow(80,c["r"])}'
def floor(b):
    b.append('<rect x="20" y="40" width="640" height="300" rx="10" fill="#F3F4F6" stroke="#DEE2E6"/>')
def static(name):
    c=CASES[name]; b=[f'<text class="h" x="20" y="26">Which way will it drive?</text>']; floor(b)
    b.append(f'<g transform="translate(340 200) scale({S*1.1})">{robot_with_arrows(c)}</g>')
    b.append(f'<text class="nb" x="40" y="70">{c["txt"][0]}</text><text class="nb" x="640" y="70" text-anchor="end">{c["txt"][1]}</text>')
    b.append(f'<text class="sm" x="340" y="326" text-anchor="middle">Seen from above, front at the top. Longer arrow = faster.</text>')
    o=svg('Motor arrows: '+name, f'An XRP seen from above, front at the top, with a red-outlined arrow beside each drive wheel showing what that side is doing: {c["desc"]}. Longer arrows mean faster.',b,W=680,H=350)
    open(OUTDIR+f'motors-{name}-arrows.svg','w').write(o)
def anim(name):
    c=CASES[name]; x,y=c['start']; h=math.radians(c['h'])
    vl,vr=c['l']*VMAX,c['r']*VMAX; v=(vl+vr)/2; w=(vr-vl)/B   # +w = counterclockwise
    frames=[]; t=0.0; trail=[(x,y)]
    frames.append((t,x,y,math.degrees(h))); t+=0.9; frames.append((t,x,y,math.degrees(h)))
    n=60; dt=c['dur']/n
    for i in range(n):
        # integrate (exact for constant v,w)
        if abs(w)<1e-9:
            x+=v*dt*math.sin(h); y-=v*dt*math.cos(h)
        else:
            h2=h-w*dt
            x+= (v/w)*(math.cos(h2)-math.cos(h))*-1 if False else 0
            # simple midpoint integration
            hm=h-w*dt/2; x+=v*dt*math.sin(hm); y-=v*dt*math.cos(hm); h=h2
        t+=dt; frames.append((t,x,y,math.degrees(h))); trail.append((x,y))
    t+=1.6; frames.append((t,x,y,math.degrees(h)))
    fo=t; t+=0.3; frames.append((t,x,y,math.degrees(h))); T=t+0.01
    frames.append((T,)+frames[0][1:])
    DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
    keys=";".join(f"{f[0]/T:.5f}" for f in frames); trs=";".join(f"{f[1]:.1f} {f[2]:.1f}" for f in frames); ros=";".join(f"{f[3]:.1f}" for f in frames)
    b=[f'<text class="h" x="20" y="26">Which way will it drive?</text>']; floor(b)
    hid=[]
    sx,sy=c['start']
    b.append(f'<g opacity="0.22" transform="translate({sx} {sy}) rotate({c["h"]}) scale({S})"><use href="#pcXRP"/></g>')
    if name in ("straight","curve"): hid.append(f'<text class="sm" x="{sx-52}" y="{sy+4}" text-anchor="end" style="font-weight:700">start</text>')
    vv=(c['l']+c['r'])/2*VMAX; ww=(c['r']-c['l'])*VMAX/B
    icc=None
    if abs(ww)>1e-9:
        lat=(vv/abs(ww))*(1 if ww<0 else -1)   # + = to the robot's right
        icc=(sx+lat,sy)
        R=abs(lat)
        if R>1: hid.append(f'<circle cx="{icc[0]:.1f}" cy="{icc[1]:.1f}" r="{R:.1f}" fill="none" stroke="#1F6FEB" stroke-width="1.5" stroke-dasharray="3 6" opacity="0.6"/>')
    spoke=''
    if icc:
        lx=(icc[0]-sx)/S
        if abs(lx)>1: spoke=f'<line x1="0" y1="0" x2="{lx:.1f}" y2="0" stroke="#7B4FA0" stroke-width="{3.2/S:.1f}" stroke-dasharray="{7/S:.1f} {5/S:.1f}" opacity="0">SPOKEANIM</line>'

    L=sum(math.hypot(trail[i][0]-trail[i-1][0],trail[i][1]-trail[i-1][1]) for i in range(1,len(trail)))
    if L>2:
        pts=' '.join(f'{p[0]:.1f},{p[1]:.1f}' for p in trail)
        t0=0.9/T; t1=(0.9+c['dur'])/T
        b.append(f'<polyline points="{pts}" fill="none" stroke="#1F6FEB" stroke-width="4" stroke-linecap="round" stroke-dasharray="{L:.0f} {L+20:.0f}"><animate attributeName="stroke-dashoffset" values="{L:.0f};{L:.0f};0;0;{L:.0f}" keyTimes="0;{t0:.4f};{t1:.4f};{fo/T:.4f};1" {DUR}/></polyline>')
    op=f'<animate attributeName="opacity" values="1;1;0;0;1" keyTimes="0;{fo/T:.4f};{(fo+0.3)/T:.4f};{(fo+0.31)/T:.4f};1" {DUR}/>'
    b.append(f'<g>{op}<animateTransform attributeName="transform" type="translate" values="{trs}" keyTimes="{keys}" {DUR}/><g><animateTransform attributeName="transform" type="rotate" values="{ros}" keyTimes="{keys}" {DUR}/><g transform="scale({S})">{robot_with_arrows(c)}{spoke.replace('SPOKEANIM',f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{0.9/T:.4f};{(fo+0.3)/T:.4f}" calcMode="discrete" {DUR}/>')}</g></g></g>')
    if icc:
        ix,iy=icc
        hid.append(f'<g><circle cx="{ix:.1f}" cy="{iy:.1f}" r="9" fill="#FFFFFF" stroke="#7B4FA0" stroke-width="3"/><path d="M {ix-14:.1f} {iy:.1f} h 28 M {ix:.1f} {iy-14:.1f} v 28" stroke="#7B4FA0" stroke-width="2.4"/><circle cx="{ix:.1f}" cy="{iy:.1f}" r="3" fill="#7B4FA0"/></g>')
        lab={'curve':'turning center, off the robot','pivot':'turning center: the stopped wheel','spin':'turning center: the pen hole, midway between the wheels'}[name]
        ty=312
        hid.append(f'<text class="nb halo" x="{ix:.1f}" y="{ty:.1f}" text-anchor="middle" style="fill:#7B4FA0">{lab}</text>')
    else:
        hid.append('<text class="nb" x="520" y="200" text-anchor="middle" style="fill:#7B4FA0">no turning center:</text><text class="nb" x="520" y="218" text-anchor="middle" style="fill:#7B4FA0">it never turns</text>')
    hid.append(f'<text class="sm" x="340" y="330" text-anchor="middle">Blue: the path of the point midway between the wheels. Purple: the point it turns around.</text>')
    va=f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{0.9/T:.4f};{(fo+0.3)/T:.4f}" calcMode="discrete" {DUR}/>'
    b.append('<g opacity="0">'+va+''.join(hid)+'</g>')
    b.append(f'<text class="nb" x="40" y="70">{c["txt"][0]}</text><text class="nb" x="640" y="70" text-anchor="end">{c["txt"][1]}</text>')
    o=svg('Motor case: '+name, f'An animation, seen from above, of an XRP with {c["desc"]}, shown by arrows beside the wheels that ride along with it. A faded copy marks where it started, and a blue line traces the path of the point midway between its wheels. A purple target marks the point it turns around, joined to the robot by a dashed line: '+{'straight':'there is none, since it drives straight.','curve':'here it is off the robot, beyond the slower right side, and the robot circles it.','pivot':'here it is the stopped left wheel, and the robot swings around it.','spin':'here it is the pen hole in the chassis, midway between the wheels, so the robot turns on the spot.'}[name],b,W=680,H=350)
    o=o.replace('<rect width="680"','<style>.halo{paint-order:stroke;stroke:#F3F4F6;stroke-width:5px;stroke-linejoin:round}</style><rect width="680"',1)
    o=o.replace('<svg xmlns="http://www.w3.org/2000/svg"',f'<svg xmlns="http://www.w3.org/2000/svg" data-hold="{fo:.2f}"',1)
    open(OUTDIR+f'motors-{name}-drive.svg','w').write(o)
for n in CASES: static(n); anim(n)
print('ok')
