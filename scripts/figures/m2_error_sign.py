import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
src=open(ROBOT_SRC).read()
defs=src[src.index('<defs>'):src.index('</defs>')+7]
S=1.15; TW=16
# (title, tape left-edge offset from left sensor, reading, error, steer, turn)
cases=[("Drifted onto white",9,"0.2","+0.3","steer right, toward the line",1),
       ("On the edge",0,"0.5","0.0","drive straight",0),
       ("Drifted onto black",-8,"0.8","−0.3","steer left, back off the line",-1)]
W=205; SW=190; SY=34; SH=150
out=[]; clips=[]
for i,(t,off,rd,er,st,turn) in enumerate(cases):
    x=12+i*(W+8); cx=x+SW/2; sy=SY+70; cy=sy+60*S
    lsx=cx-6.5*S
    clips.append(f'<clipPath id="es{i}"><rect x="{x}" y="{SY}" width="{SW}" height="{SH}" rx="6"/></clipPath>')
    g=[f'<text class="h" x="{x}" y="{SY-12}">{t}</text>',
       f'<g clip-path="url(#es{i})"><rect x="{x}" y="{SY}" width="{SW}" height="{SH}" fill="#FFFFFF"/>',
       f'<rect x="{lsx+off}" y="{SY}" width="{TW*2.2}" height="{SH}" fill="#2B2B2B"/>',
       f'<use href="#pcXRP" transform="translate({cx} {cy}) scale({S})" opacity="0.8"/>',
       f'<circle cx="{cx+6.5*S}" cy="{sy}" r="4.6" fill="#ADB5BD" stroke="#868E96"/>',
       f'<circle cx="{lsx}" cy="{sy}" r="8" fill="none" stroke="#D1182C" stroke-width="2.6"/>']
    # steering arrow from front
    fx,fy=cx,SY+18
    if turn==0: g.append(f'<line x1="{cx}" y1="{sy-22}" x2="{cx}" y2="{SY+10}" stroke="#2E7D32" stroke-width="3.4" marker-end="url(#esA)"/>')
    else: g.append(f'<path d="M {cx} {sy-22} Q {cx} {SY+14} {cx+turn*48} {SY+12}" fill="none" stroke="#2E7D32" stroke-width="3.4" marker-end="url(#esA)"/>')
    g.append('</g>')
    g.append(f'<rect x="{x}" y="{SY}" width="{SW}" height="{SH}" rx="6" fill="none" stroke="#ADB5BD"/>')
    g.append(f'<text class="m" x="{x}" y="{SY+SH+20}">left reads {rd}</text>')
    g.append(f'<text class="me" x="{x}" y="{SY+SH+38}">error = 0.5 − {rd} = {er}</text>')
    g.append(f'<text class="st" x="{x}" y="{SY+SH+57}">{st}</text>')
    out+=g
out.append(f'<text class="sm" x="12" y="{SY+SH+82}">Red ring: the left sensor, the one this follower reads. The robot rides the line\'s left edge.</text>')
H=SY+SH+92
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 {H}" width="680" height="{H}" role="img" aria-labelledby="esT esD">
  <title id="esT">The sign of the error says which way to steer</title>
  <desc id="esD">Three close-ups of the XRP's front following the left edge of a black line with its left sensor. Drifted onto white: the left sensor reads 0.2, error = 0.5 − 0.2 = +0.3, steer right, toward the line. On the edge: it reads 0.5, error 0.0, drive straight. Drifted onto black: it reads 0.8, error = 0.5 − 0.8 = −0.3, steer left, back off the line.</desc>
  <style>
    .h  {{ font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 13.5px; font-weight: 700; fill: #22527B; }}
    .m  {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 12.5px; font-weight: 600; fill: #343A40; }}
    .me {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 12.5px; font-weight: 700; fill: #D1182C; }}
    .st {{ font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 12.5px; font-weight: 700; fill: #2E7D32; }}
    .sm {{ font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 11.5px; fill: #6C757D; }}
  </style>
  {defs.replace('<defs>','<defs>'+chr(10)+'    <marker id="esA" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#2E7D32"/></marker>'+chr(10)+'    '+(chr(10)+'    ').join(clips))}
  <rect width="680" height="{H}" fill="#FFFFFF"/>
  {(chr(10)+'  ').join(out)}
</svg>
'''
open(OUTDIR+'error-sign.svg','w').write(svg); print(H)
