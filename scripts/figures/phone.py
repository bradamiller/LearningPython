import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
W,H=680,440
PX,PY,PW,PH=170,14,230,412
SX,SY,SW_,SH=PX+12,PY+40,PW-24,PH-80
S=[f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>']
S.append('<defs><clipPath id="scr"><rect x="%d" y="%d" width="%d" height="%d" rx="6"/></clipPath></defs>'%(SX,SY,SW_,SH))
# phone body
S.append(f'<rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" rx="30" fill="#1E2328" stroke="#0B0E11" stroke-width="2"/>')
S.append(f'<rect x="{PX+PW/2-30}" y="{PY+14}" width="60" height="10" rx="5" fill="#0B0E11"/>')
S.append(f'<rect x="{PX+PW/2-40}" y="{PY+PH-22}" width="80" height="5" rx="2.5" fill="#5B6168"/>')
# map
M=[]
M.append(f'<rect x="{SX}" y="{SY}" width="{SW_}" height="{SH}" fill="#EEF0E8"/>')
M.append(f'<path d="M {SX} {SY+250} C {SX+60} {SY+230} {SX+110} {SY+300} {SX+SW_} {SY+280} L {SX+SW_} {SY+SH} L {SX} {SY+SH} Z" fill="#AFD4F0"/>')
M.append(f'<rect x="{SX+120}" y="{SY+64}" width="70" height="56" rx="4" fill="#BFE3B0"/>')
# streets: grid
xs=[SX+20+i*40 for i in range(6)]; ys=[SY+40+i*36 for i in range(7)]
for y in ys: M.append(f'<rect x="{SX}" y="{y-4}" width="{SW_}" height="8" fill="#FFFFFF" stroke="#D6D8D0" stroke-width="0.8"/>')
for x in xs: M.append(f'<rect x="{x-4}" y="{SY}" width="8" height="{SH}" fill="#FFFFFF" stroke="#D6D8D0" stroke-width="0.8"/>')
# a highway
M.append(f'<path d="M {SX} {SY+190} L {SX+SW_} {SY+150}" stroke="#F6C85F" stroke-width="9"/>')
# heavy traffic segment (red) on a street
TRA=(xs[4],ys[2],xs[4],ys[5])
M.append(f'<line x1="{TRA[0]}" y1="{TRA[1]}" x2="{TRA[2]}" y2="{TRA[3]}" stroke="#D93025" stroke-width="7" stroke-linecap="round"/>')
M.append(f'<line x1="{xs[4]}" y1="{ys[5]}" x2="{xs[4]}" y2="{ys[6]}" stroke="#F29900" stroke-width="7" stroke-linecap="round"/>')
# road closure on a column
CX_,CY_=(xs[1]+xs[2])/2,ys[1]
# route: start bottom-left, around
st=(xs[0],ys[5]); en=(xs[4],ys[1])
route=[st,(xs[0],ys[2]),(xs[3],ys[2]),(xs[3],ys[1]),en]
d="M "+" L ".join(f"{x} {y}" for x,y in route)
M.append(f'<path d="{d}" fill="none" stroke="#174EA6" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>')
M.append(f'<path d="{d}" fill="none" stroke="#4285F4" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>')
# hmm route passes x2 between y2 - closure is at x2 between ys1-ys2 (north of route), fine
M.append(f'<g transform="translate({CX_} {CY_})"><rect x="-11" y="-7" width="22" height="14" rx="2" fill="#FFFFFF" stroke="#D93025" stroke-width="1.6"/><path d="M -9 5 L -3 -5 M -3 5 L 3 -5 M 3 5 L 9 -5" stroke="#D93025" stroke-width="2.4"/></g>')
M.append(f'<circle cx="{st[0]}" cy="{st[1]}" r="9" fill="#4285F4" opacity="0.25"/><circle cx="{st[0]}" cy="{st[1]}" r="5.5" fill="#1A73E8" stroke="#FFFFFF" stroke-width="2"/>')
M.append(f'<g transform="translate({en[0]} {en[1]})"><path d="M 0 0 C -3 -8 -10 -11 -10 -18 A 10 10 0 1 1 10 -18 C 10 -11 3 -8 0 0 Z" fill="#D93025" stroke="#FFFFFF" stroke-width="1.5"/><circle cx="0" cy="-18" r="3.5" fill="#FFFFFF"/></g>')
# top card
M.append(f'<rect x="{SX+8}" y="{SY+8}" width="{SW_-16}" height="22" rx="11" fill="#FFFFFF" stroke="#D6D8D0"/><text class="ph" x="{SX+20}" y="{SY+23}">Your location → School</text>')
# bottom sheet
BY=SY+SH-70
M.append(f'<rect x="{SX}" y="{BY}" width="{SW_}" height="70" rx="12" fill="#FFFFFF" stroke="#D6D8D0"/>')
M.append(f'<text class="phb" x="{SX+14}" y="{BY+24}" style="fill:#188038">14 min</text><text class="ph" x="{SX+70}" y="{BY+24}">(3.2 km)</text>')
M.append(f'<text class="phs" x="{SX+14}" y="{BY+40}">Fastest route · avoids a closed road</text>')
M.append(f'<rect x="{SX+14}" y="{BY+47}" width="60" height="18" rx="9" fill="#1A73E8"/><text class="phw" x="{SX+44}" y="{BY+60}" text-anchor="middle">Start</text>')
S.append('<g clip-path="url(#scr)">'+''.join(M)+'</g>')
# status bar
S.append(f'<text class="phw" x="{PX+28}" y="{PY+30}">9:41</text>')
# callouts
def call(x1,y1,x2,y2,l1,l2,col):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="1.6"/><circle cx="{x1}" cy="{y1}" r="3" fill="{col}"/>'
            f'<text class="cb" x="{x2+6}" y="{y2-2}" style="fill:{col}">{l1}</text><text class="cs" x="{x2+6}" y="{y2+14}">{l2}</text>')
S.append(call(CX_+12,CY_,440,120,"Road closed","an obstacle: Module 5","#D93025"))
S.append(call(xs[4]+4,(ys[3]+ys[4])/2,440,210,"Heavy traffic","a slow street: Module 6","#C26401"))
S.append(call(xs[0]+4,ys[4],440,300,"The route goes around both","planned on a graph of streets","#174EA6"))
style='''<style>
 .ph{font-family:Helvetica,Arial,sans-serif;font-size:10px;fill:#3C4043}
 .phs{font-family:Helvetica,Arial,sans-serif;font-size:9px;fill:#5F6368}
 .phb{font-family:Helvetica,Arial,sans-serif;font-size:15px;font-weight:700}
 .phw{font-family:Helvetica,Arial,sans-serif;font-size:10px;font-weight:700;fill:#FFFFFF}
 .cb{font-family:Montserrat,Helvetica,Arial,sans-serif;font-size:13px;font-weight:700}
 .cs{font-family:Montserrat,Helvetica,Arial,sans-serif;font-size:11.5px;fill:#495057}
</style>'''
desc='A drawing of a smartphone running a generic maps app. The map shows a grid of city streets, a park, a river and a highway. A blue route runs from the blue dot of your location to a red pin at school. One street has a road-closed barrier, labeled as an obstacle, Module 5; another is colored red for heavy traffic, labeled as a slow street, Module 6. The blue route turns along the streets to go around both. A card at the bottom reads 14 min, fastest route, avoids a closed road, with a Start button.'
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d"><title id="t">A maps app routing around trouble</title><desc id="d">{desc}</desc>{style}{chr(10).join(S)}</svg>'''
open(OUTDIR+'phone-route.svg','w').write(svg)
