import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import math
src=open(ROBOT_SRC).read()
defs=src[src.index('<defs>'):src.index('</defs>')+7]
S=0.6; TW=12; H=130; W=325
def P(cx,cy,ang,lx,ly):
    a=math.radians(ang); x,y=lx*S,ly*S
    return (cx + x*math.cos(a) - y*math.sin(a), cy + x*math.sin(a) + y*math.cos(a))
def arc(cx,cy,r,a0,a1):
    p0=(cx+r*math.sin(math.radians(a0)), cy-r*math.cos(math.radians(a0)))
    p1=(cx+r*math.sin(math.radians(a1)), cy-r*math.cos(math.radians(a1)))
    return f'<path d="M {p0[0]:.1f} {p0[1]:.1f} A {r} {r} 0 0 1 {p1[0]:.1f} {p1[1]:.1f}" fill="none" stroke="#495057" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#ttArr)"/>'
out=[]; clips=[]
def scene(id,x,y,ang,prev=None,ghost=None,ring=None,spin=False,nxt=False):
    cx,cy=x+W/2-40,y+H/2
    clips.append(f'<clipPath id="{id}"><rect x="{x}" y="{y}" width="{W}" height="{H}" rx="6"/></clipPath>')
    g=[f'<g clip-path="url(#{id})">',
       f'<rect x="{x}" y="{y}" width="{W}" height="{H}" fill="#F3F4F6"/>',
       f'<rect x="{cx-TW/2}" y="{y}" width="{TW}" height="{H}" fill="#2B2B2B"/>',
       f'<rect x="{x}" y="{cy-TW/2}" width="{W}" height="{TW}" fill="#2B2B2B"/>']
    if ghost is not None:
        g.append(f'<use href="#pcGhost" transform="translate({cx} {cy}) rotate({ghost}) scale({S})"/>')
    g.append(f'<use href="#pcXRP" transform="translate({cx} {cy}) rotate({ang}) scale({S})" opacity="0.9"/>')
    if ring:
        for side,color in ring:
            px,py=P(cx,cy,ang,6.5*side,-60)
            g.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="6" fill="none" stroke="{color}" stroke-width="2.6"/>')
    if prev is not None:
        g.append(arc(cx,cy,68,prev+5,ang-3))
    if spin:
        g.append(f'<g transform="translate({cx} {cy})" fill="none" stroke="#22527B" stroke-width="2.2" marker-end="url(#ttArrB)">'
                 f'<path d="M 50 -42 A 66 66 0 0 1 66 -6"/><path d="M -50 42 A 66 66 0 0 1 -66 6"/></g>')
    if nxt:
        g.append(f'<line x1="{cx+66}" y1="{cy}" x2="{cx+150}" y2="{cy}" stroke="#2E7D32" stroke-width="3" stroke-dasharray="7 5" marker-end="url(#ttArrG)"/>')
        g.append(f'<text class="nx" x="{cx+108}" y="{cy-14}" text-anchor="middle">next: track</text>')
    g.append('</g>')
    g.append(f'<rect x="{x}" y="{y}" width="{W}" height="{H}" rx="6" fill="none" stroke="#DEE2E6"/>')
    out.append('\n    '.join(g))
cols=[12,343]; rows=[0,180]
panels=[
 ("Blind turn","# 1. blind turn, about 60 deg","both sensors are now off the old line",dict(ang=60,prev=0,ghost=0)),
 ("Keep spinning","# 2. keep spinning in place","motors stay on while the program goes on",dict(ang=70,spin=True)),
 ("Wait for a sensor","# 3. wait until a sensor sees the line","is_either_on_line() becomes True",dict(ang=82,ring=[(1,"#2E7D32")])),
 ("Stop","# 4. stop","facing the new line, ready to follow it",dict(ang=82,ring=[(1,"#2E7D32")],nxt=True)),
]
for i,(t,c,n,kw) in enumerate(panels):
    x=cols[i%2]; y=rows[i//2]
    out.append(f'<text class="h" x="{x}" y="{y+15}">{i+1} · {t}</text>')
    scene(f'tt{i}',x,y+24,**kw)
    out.append(f'<text class="note" x="{x}" y="{y+24+H+17}">{n}</text>')
fy=364
out.append(f'<text class="h" x="12" y="{fy+15}" style="fill:#D1182C">If the blind turn is the wrong size</text>')
scene('ttf0',12,fy+24,ang=10,prev=0,ghost=0,ring=[(-1,"#D1182C")])
scene('ttf1',343,fy+24,ang=120,prev=0,ghost=0)
by=fy+24+H
out.append(f'<text class="bad" x="12" y="{by+17}">Too small (10°): a sensor is still on the</text>')
out.append(f'<text class="bad" x="12" y="{by+33}">old line, so the wait ends at once.</text>')
out.append(f'<text class="bad" x="343" y="{by+17}">Too big (120°): the sensors already swung</text>')
out.append(f'<text class="bad" x="343" y="{by+33}">past the cross street; it keeps spinning.</text>')
Htot=by+42
mk=lambda i,c,sz: f'<marker id="{i}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="{sz}" markerHeight="{sz}" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'
extra='\n    '.join([mk('ttArr','#495057',5),mk('ttArrB','#22527B',5),mk('ttArrG','#2E7D32',4)]+clips)
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 {Htot}" width="680" height="{Htot}" role="img" aria-labelledby="ttTitle ttDesc">
  <title id="ttTitle">A sensor-ended turn in four steps</title>
  <desc id="ttDesc">Four top-down drawings of the XRP parked on an intersection, turning right onto the cross street.
    1, blind turn of about 60 degrees: both line sensors are now off the line it was following. 2, keep spinning in
    place: the motors stay on while the program goes on. 3, wait until a sensor sees the line: the leading sensor reaches
    the cross street and is_either_on_line() becomes True. 4, stop, facing the new line, ready to follow it. Below, two mistakes: a
    blind turn that is too small (10 degrees) leaves a sensor on the old line, so the wait ends at once; one that is too
    big (120 degrees) swings the sensors past the cross street, so the robot keeps spinning.</desc>
  <style>
    .h    {{ font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 700; fill: #22527B; }}
    .code {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 12px; font-weight: 600; fill: #142D50; }}
    .note {{ font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 12.5px; fill: #495057; }}
    .bad  {{ font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 12.5px; font-weight: 600; fill: #D1182C; }}
    .nx   {{ font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 12px; font-weight: 700; fill: #2E7D32; }}
  </style>
  {defs.replace('<defs>','<defs>'+chr(10)+'    '+extra)}
  <rect width="680" height="{Htot}" fill="#FFFFFF"/>
  {chr(10).join("  "+o for o in out)}
</svg>
'''
open(OUTDIR+'sensor-ended-turn.svg','w').write(svg); print(Htot)
