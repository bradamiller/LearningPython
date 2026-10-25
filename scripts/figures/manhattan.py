import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import random
random.seed(7)
W,H=680,400
AV=[78,180,282,384,486,570]          # avenues, west -> east
AVN=["9th Ave","8th Ave","7th Ave","6th Ave","5th Ave","Madison"]
ST=[322,277,232,187,142,97]          # streets, south -> north
STN=["53rd St","54th St","55th St","56th St","57th St","58th St"]
PARK_Y=(36,72)                        # Central Park, north of 59th
S=[]
S.append(f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>')
# water and land
S.append('<rect x="0" y="28" width="680" height="324" fill="#9FD3F2"/>')
for i in range(6):
    y=48+i*52
    S.append(f'<path d="M 4 {y} q 6 -5 12 0 t 12 0" fill="none" stroke="#FFFFFF" stroke-width="1.6" opacity="0.8"/>')
    S.append(f'<path d="M 650 {y+20} q 6 -5 12 0 t 12 0" fill="none" stroke="#FFFFFF" stroke-width="1.6" opacity="0.8"/>')
S.append('<rect x="34" y="28" width="562" height="324" fill="#D9D4C7"/>')
S.append('<text class="riv" x="16" y="200" transform="rotate(-90 16 200)" text-anchor="middle">Hudson River</text>')
S.append('<text class="riv" x="668" y="200" transform="rotate(90 668 200)" text-anchor="middle">East River</text>')
# streets (asphalt)
SW=14
for y in ST+[PARK_Y[1]+7]:
    S.append(f'<rect x="34" y="{y-SW/2}" width="562" height="{SW}" fill="#5B6168"/>')
for x in AV:
    S.append(f'<rect x="{x-SW/2-2}" y="28" width="{SW+4}" height="324" fill="#5B6168"/>')
# lane dashes
for y in ST+[PARK_Y[1]+7]:
    S.append(f'<line x1="34" y1="{y}" x2="596" y2="{y}" stroke="#F2C14E" stroke-width="1.2" stroke-dasharray="6 6"/>')
for x in AV:
    S.append(f'<line x1="{x}" y1="28" x2="{x}" y2="352" stroke="#F2C14E" stroke-width="1.2" stroke-dasharray="6 6"/>')
# park
S.append(f'<rect x="{AV[1]+SW/2+2}" y="28" width="{AV[4]-AV[1]-SW-4}" height="{PARK_Y[1]-28}" fill="#7CC36E"/>')
S.append(f'<ellipse cx="{(AV[2]+AV[3])/2+60}" cy="48" rx="34" ry="11" fill="#9FD3F2"/>')
for i in range(30):
    x=AV[1]+16+i*10.2+random.uniform(-3,3); y=random.choice([40,50,60])+random.uniform(-3,3)
    if abs(x-((AV[2]+AV[3])/2+60))<42 and y<62: continue
    if x>AV[4]-SW/2-10: continue
    S.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{random.uniform(5,7):.1f}" fill="#4F9A45"/>')
S.append(f'<text class="park" x="{(AV[1]+AV[4])/2}" y="66" text-anchor="middle">CENTRAL PARK</text>')
# buildings in each block
COLS=["#E07A5F","#F2CC8F","#81B29A","#9DB4C0","#C9ADA7","#B5838D","#F4A261","#8D99AE"]
edges_x=[34]+AV+[596]; edges_y=[PARK_Y[1]+7]+sorted(ST)+[352]
for i in range(len(edges_x)-1):
    for j in range(len(edges_y)-1):
        x0=edges_x[i]+(SW/2+5); x1=edges_x[i+1]-(SW/2+5)
        y0=edges_y[j]+SW/2+3; y1=edges_y[j+1]-SW/2-3
        if i==0: x0=edges_x[0]+4
        if i==len(edges_x)-2: x1=edges_x[-1]-4
        if y1-y0<12 or x1-x0<12: continue
        x=x0
        while x<x1-8:
            w=min(random.choice([18,22,26,30]),x1-x)
            c=random.choice(COLS); h=y1-y0
            S.append(f'<rect x="{x:.1f}" y="{y0:.1f}" width="{w-2:.1f}" height="{h:.1f}" rx="2" fill="{c}" stroke="#5F4B3B" stroke-width="0.8"/>')
            S.append(f'<rect x="{x+2:.1f}" y="{y0+2:.1f}" width="{w-6:.1f}" height="4" rx="1" fill="#FFFFFF" opacity="0.35"/>')
            for wy in range(int(y0+10),int(y1-4),8):
                for wx in range(int(x+4),int(x+w-6),6):
                    S.append(f'<rect x="{wx}" y="{wy}" width="3" height="3" fill="#FFF6D5" opacity="0.9"/>')
            x+=w
# A and B
A=(AV[1],ST[1]); B=(AV[3],ST[4])
# diagonal (not allowed)
S.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{B[0]}" y2="{B[1]}" stroke="#D1182C" stroke-width="3.5" stroke-dasharray="8 6"/>')
mx,my=(A[0]+B[0])/2,(A[1]+B[1])/2
S.append(f'<g transform="translate({mx} {my})"><circle r="13" fill="#FFFFFF" stroke="#D1182C" stroke-width="3"/><path d="M -6 -6 L 6 6 M 6 -6 L -6 6" stroke="#D1182C" stroke-width="3.2" stroke-linecap="round"/></g>')
S.append(f'<text class="tag" x="{mx-18}" y="{my-16}" text-anchor="end" style="fill:#D1182C">no cutting through buildings</text>')
# taxi route: east along 54th, then north up 6th
S.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {A[1]} L {B[0]} {B[1]}" fill="none" stroke="#1F6FEB" stroke-width="6" stroke-linejoin="round" stroke-linecap="round" opacity="0.9"/>')
for k in range(1,3):
    x=A[0]+(B[0]-A[0])*(k-0.5)/2
    S.append(f'<text class="cnt" x="{x}" y="{A[1]+24}" text-anchor="middle">{k}</text>')
for k in range(1,4):
    y=A[1]+(B[1]-A[1])*(k-0.5)/3
    S.append(f'<text class="cnt" x="{B[0]+14}" y="{y+4}">{k+2}</text>')
# taxi
def taxi(x,y):
    return (f'<g transform="translate({x} {y})"><rect x="-15" y="-8" width="30" height="16" rx="5" fill="#FFC72C" stroke="#3A2E00" stroke-width="1.2"/>'
            f'<rect x="-6" y="-5" width="12" height="10" rx="2" fill="#6FA8DC" stroke="#3A2E00" stroke-width="0.8"/>'
            f'<rect x="-4" y="-11" width="8" height="4" rx="1" fill="#FFFFFF" stroke="#3A2E00" stroke-width="0.8"/>'
            f'<circle cx="-9" cy="9" r="3" fill="#222"/><circle cx="9" cy="9" r="3" fill="#222"/><circle cx="-9" cy="-9" r="3" fill="#222"/><circle cx="9" cy="-9" r="3" fill="#222"/>'
            f'<path d="M -15 0 h 4 M 11 0 h 4" stroke="#222" stroke-width="2" stroke-dasharray="2 2"/></g>')
S.append(taxi(A[0]-26,A[1]))
def pin(x,y,l,c):
    return (f'<g transform="translate({x} {y})"><path d="M 0 0 C -4 -10 -12 -14 -12 -22 A 12 12 0 1 1 12 -22 C 12 -14 4 -10 0 0 Z" fill="{c}" stroke="#FFFFFF" stroke-width="2"/>'
            f'<text class="pin" x="0" y="-18" text-anchor="middle">{l}</text></g>')
S.append(pin(*A,"A","#2E7D32")); S.append(pin(*B,"B","#D1182C"))
# street/avenue name signs
for x,n in zip(AV,AVN):
    S.append(f'<rect x="{x-28}" y="356" width="56" height="16" rx="3" fill="#1F7A3E"/><text class="sign" x="{x}" y="368" text-anchor="middle">{n}</text>')
for y,n in zip(ST+[PARK_Y[1]+7],STN+["59th St"]):
    S.append(f'<rect x="600" y="{y-8}" width="50" height="16" rx="3" fill="#1F7A3E" opacity="0.95"/><text class="sign" x="625" y="{y+4}" text-anchor="middle">{n}</text>')
S.append('<text class="note" x="340" y="392" text-anchor="middle">Avenues run north and south; streets run east and west. The taxi counts blocks: 2 across + 3 up = 5.</text>')
S.append('<text class="h" x="20" y="20">Manhattan, roughly (not to scale)</text>')
style='''<style>
 .h{font-family:Montserrat,Helvetica,Arial,sans-serif;font-size:14px;font-weight:700;fill:#22527B}
 .riv{font-family:Montserrat,Helvetica,Arial,sans-serif;font-size:11px;font-weight:700;fill:#1F5F8B;letter-spacing:1px}
 .park{font-family:Montserrat,Helvetica,Arial,sans-serif;font-size:12px;font-weight:800;fill:#1E5A1A;letter-spacing:2px}
 .tag{font-family:Montserrat,Helvetica,Arial,sans-serif;font-size:12px;font-weight:700;paint-order:stroke;stroke:#FFFFFF;stroke-width:4px;stroke-linejoin:round}
 .cnt{font-family:Montserrat,Helvetica,Arial,sans-serif;font-size:13px;font-weight:800;fill:#1F6FEB;paint-order:stroke;stroke:#FFFFFF;stroke-width:4px}
 .pin{font-family:Montserrat,Helvetica,Arial,sans-serif;font-size:13px;font-weight:800;fill:#FFFFFF}
 .sign{font-family:Montserrat,Helvetica,Arial,sans-serif;font-size:9.5px;font-weight:700;fill:#FFFFFF}
 .note{font-family:Montserrat,Helvetica,Arial,sans-serif;font-size:12px;fill:#343A40}
</style>'''
desc='A cartoon map of midtown Manhattan from above, not to scale. Between the Hudson River on the left and the East River on the right, long avenues run north and south (9th Ave, 8th Ave, 7th Ave, 6th Ave, 5th Ave, Madison) and shorter cross streets run east and west (53rd to 58th Street), with Central Park along the top. Every block between them is filled with buildings. A yellow taxi waits at A, the corner of 8th Avenue and 54th Street. A red dashed straight line from A to B, at 6th Avenue and 57th Street, is crossed out: no cutting through buildings. The taxi route in blue goes 2 blocks east along 54th Street, then 3 blocks north up 6th Avenue, numbered 1 to 5: 2 across plus 3 up is 5 blocks.'
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
<title id="t">Manhattan's street grid</title><desc id="d">{desc}</desc>
{style}
{chr(10).join(S)}
</svg>'''
open(OUTDIR+'manhattan-grid.svg','w').write(svg); print(len(svg))
