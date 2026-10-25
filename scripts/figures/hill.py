import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys, math, json; from common import *
X0,X1=40,450; BASE=300; HH=85
def hy(x):
    # flat, cosine up, flat top, cosine down, flat
    a,b,c,d=105,215,265,375
    if x<a: return 0.0
    if x<b: return HH*(1-math.cos(math.pi*(x-a)/(b-a)))/2
    if x<c: return HH
    if x<d: return HH*(1+math.cos(math.pi*(x-c)/(d-c)))/2
    return 0.0
def slope(x,e=0.5): return (hy(x+e)-hy(x-e))/(2*e)   # dy/dx, + = uphill
def sim(mode,dt=0.02):
    x=X0+20; out=[]; t=0.0
    while x<X1-15:
        s=slope(x); th=math.atan(s); sn=math.sin(th)
        if mode=='effort':
            eff=0.5; v=max(12.0,60*(1-0.95*sn))          # px/s along ground
        else:
            v=42.0; eff=min(1.0,max(0.05,0.5*(1+1.6*sn)))
        out.append((t,x,BASE-hy(x),math.degrees(-th),eff,v))
        x+=v*math.cos(th)*dt; t+=dt
        if t>60: break
    out.append((t,x,BASE-hy(x),0.0,out[-1][4],out[-1][5]))
    return out
runs={'effort':sim('effort'),'speed':sim('speed')}
GAP=0.6; t0=0.4
seg={}; frames=[]
cur=t0
frames.append((0.0,X0+20,BASE,0.0,0,0))
for m in ('effort','speed'):
    r=runs[m]; s0=cur
    frames.append((s0-0.001 if s0>0.001 else 0.0001,X0+20,BASE,0.0,0,0))
    for f in r[::3]+[r[-1]]: frames.append((s0+f[0],)+f[1:])
    e=s0+r[-1][0]; frames.append((e+1.2,)+r[-1][1:]); seg[m]=(round(s0,3),round(e+1.2,3)); cur=e+1.2+GAP
T=cur
frames.append((T,)+frames[-1][1:]) if False else None
frames.sort(key=lambda f:f[0]); frames.append((T,)+frames[-1][1:])
DUR=f'dur="{T:.2f}s" repeatCount="indefinite"'
def kt(L): return ";".join(f"{f[0]/T:.5f}" for f in L)
keys=kt(frames)
def first(b): return f'<animate attributeName="opacity" values="1;0" keyTimes="0;{b/T:.5f}" calcMode="discrete" {DUR}/>'
def vis(a,b): return f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{max(a/T,0.0001):.5f};{min(b/T,0.9999):.5f}" calcMode="discrete" {DUR}/>'
b=['<text class="h" x="20" y="24">Same hill, two ways to drive</text>']
b.append('<rect x="20" y="36" width="450" height="300" rx="10" fill="#EAF4FB" stroke="#DEE2E6"/>')
pts=[(x,BASE-hy(x)) for x in range(20,471,3)]
d="M 20 336 L "+" L ".join(f"{x} {y:.1f}" for x,y in pts)+" L 470 336 Z"
b.append(f'<path d="{d}" fill="#B9D99B" stroke="#6E9B4A" stroke-width="2.5"/>')
b.append(f'<text class="sm" x="160" y="250" text-anchor="middle" style="font-weight:700">uphill</text><text class="sm" x="240" y="203" text-anchor="middle" style="font-weight:700">flat top</text><text class="sm" x="335" y="250" text-anchor="middle" style="font-weight:700">downhill</text>')
anim=[]
# breadcrumb dots every 0.35 s of each run
for m in ('effort','speed'):
    s0,s1=seg[m]; r=runs[m]; col="#D1182C" if m=='effort' else "#1F6FEB"
    k=0
    for f in r:
        if f[0]>=k*0.35:
            anim.append(f'<g opacity="0">{vis(s0+f[0],s1)}<circle cx="{f[1]:.1f}" cy="{f[2]-2:.1f}" r="3.6" fill="{col}"/></g>'); k+=1
# side-view XRP, origin at ground under the drive wheel, facing right
XRP='''<g>
 <rect x="-30" y="-30" width="62" height="18" rx="5" fill="#D3D7DB" stroke="#5F666D" stroke-width="1.5"/>
 <rect x="-14" y="-38" width="26" height="9" rx="2" fill="#D1182C"/>
 <rect x="26" y="-36" width="9" height="10" rx="2" fill="#B5172A"/>
 <circle cx="31" cy="-6" r="5" fill="#C3C8CD" stroke="#5F666D" stroke-width="1.3"/>
 <circle cx="0" cy="-14" r="14" fill="#2B2B2B"/><circle cx="0" cy="-14" r="5" fill="#9AA1A8"/>
</g>'''
trs=";".join(f"{f[1]:.1f} {f[2]:.1f}" for f in frames); ros=";".join(f"{f[3]:.1f}" for f in frames)
anim.append(f'<g><animateTransform attributeName="transform" type="translate" values="{trs}" keyTimes="{keys}" {DUR}/><g><animateTransform attributeName="transform" type="rotate" values="{ros}" keyTimes="{keys}" {DUR}/>{XRP}</g></g>')
# panel
X=492
b.append(f'<text class="h" x="{X}" y="60">The gauges</text>')
def bar(y,label,col,idx):
    b.append(f'<text class="nb" x="{X}" y="{y}">{label}</text>')
    b.append(f'<rect x="{X}" y="{y+8}" width="170" height="18" rx="9" fill="#E9ECEF" stroke="#ADB5BD"/>')
    vals=";".join(f"{max(0.0,min(1.0,f[idx]/(1.0 if idx==4 else 115.0)))*170:.1f}" for f in frames)
    anim.append(f'<rect x="{X}" y="{y+8}" width="0" height="18" rx="9" fill="{col}"><animate attributeName="width" values="{vals}" keyTimes="{keys}" {DUR}/></rect>')
bar(92,"Effort: how hard it works","#D1182C",4)
bar(150,"Speed: how fast it goes","#1F6FEB",5)
labs={'effort':("Effort control","same effort the whole way,","so the hill sets the speed","#D1182C"),
      'speed':("Speed control","same speed the whole way,","so the hill sets the effort","#1F6FEB")}
for m in ('effort','speed'):
    s0,s1=seg[m]; t1,l1,l2,col=labs[m]
    anim.append(f'<g opacity="0">{vis(s0,s1)}<rect x="{X-6}" y="200" width="182" height="72" rx="10" fill="#FFFFFF" stroke="{col}" stroke-width="2"/><text class="nb" x="{X+6}" y="222" style="fill:{col}">{t1}</text><text class="sm" x="{X+6}" y="242">{l1}</text><text class="sm" x="{X+6}" y="258">{l2}</text></g>')
anim.append(f'<g opacity="0">{first(seg["effort"][0])}<text class="sm" x="{X}" y="226">Press a button to drive the</text><text class="sm" x="{X}" y="242">same hill under each kind</text><text class="sm" x="{X}" y="258">of control.</text></g>')
b.append(f'<text class="sm" x="{X}" y="300">Dots are dropped at equal</text><text class="sm" x="{X}" y="316">time steps: far apart means</text><text class="sm" x="{X}" y="332">fast, close together slow.</text>')
b.append('<g>'+''.join(anim)+'</g>')
modes=[{"label":"Effort control","start":seg['effort'][0],"stop":seg['effort'][1]},{"label":"Speed control","start":seg['speed'][0],"stop":seg['speed'][1]}]
o=svg('Effort control and speed control on a hill',
 'An animation of an XRP, seen from the side, driving over a hill: flat ground, an uphill slope, a flat top and a downhill slope. Two buttons choose how it is controlled. Effort control: the effort gauge stays at the same level the whole way, and the robot crawls up the slope, speeds up on the flat top and goes fastest down the other side; red dots dropped at equal time steps bunch together uphill and spread out downhill. Speed control: the speed gauge stays the same the whole way while the effort gauge climbs high going uphill, drops to medium on the top and falls low going downhill; blue dots are evenly spaced.',b,W=680,H=350)
o=o.replace('<svg xmlns="http://www.w3.org/2000/svg"',"<svg xmlns=\"http://www.w3.org/2000/svg\" data-modes='"+json.dumps(modes)+"'",1)
open(OUTDIR+'effort-vs-speed-hill.svg','w').write(o); print(seg,round(T,1))
