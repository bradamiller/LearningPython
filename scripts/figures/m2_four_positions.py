import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
src=open(ROBOT_SRC).read()
defs=src[src.index('<defs>'):src.index('</defs>')+7]
S=1.15; TW=16
cols=[("Both on white", None, False, (False,False)),
      ("Left sensor on tape", -7.5, False, (True,False)),
      ("Right sensor on tape", 7.5, False, (True,False)),
      ("On the cross", -7.5, True, (True,True))]
X0=170; CW=127; SW=117; SY=30; SH=140
out=[]; clips=[]
for i,(title,tape,cross,vals) in enumerate(cols):
    x=X0+i*CW; cx=x+SW/2; sy_sens=SY+56; cy=sy_sens+60*S
    clips.append(f'<clipPath id="fp{i}"><rect x="{x}" y="{SY}" width="{SW}" height="{SH}" rx="6"/></clipPath>')
    g=[f'<text class="h" x="{cx}" y="{SY-10}" text-anchor="middle">{title}</text>',
       f'<g clip-path="url(#fp{i})"><rect x="{x}" y="{SY}" width="{SW}" height="{SH}" fill="#F3F4F6"/>']
    if tape is None:
        g.append(f'<rect x="{cx-46}" y="{SY}" width="{TW}" height="{SH}" fill="#2B2B2B"/>')
    else:
        g.append(f'<rect x="{cx+tape-TW/2}" y="{SY}" width="{TW}" height="{SH}" fill="#2B2B2B"/>')
    if cross:
        g.append(f'<rect x="{x}" y="{sy_sens-TW/2}" width="{SW}" height="{TW}" fill="#2B2B2B"/>')
    g.append(f'<use href="#pcXRP" transform="translate({cx} {cy}) scale({S})" opacity="0.8"/>')
    for side in (-1,1):
        sx=cx+side*6.5*S
        on = cross or (tape is not None and abs(sx-(cx+tape))<TW/2)
        if on: g.append(f'<circle cx="{sx}" cy="{sy_sens}" r="7.5" fill="none" stroke="#2E7D32" stroke-width="3"/>')
    g.append('</g>')
    g.append(f'<rect x="{x}" y="{SY}" width="{SW}" height="{SH}" rx="6" fill="none" stroke="#DEE2E6"/>')
    for r,v in enumerate(vals):
        y=SY+SH+14+r*34
        fill,stroke,txt,cls=("#E1F0E3","#2E7D32","True","vt") if v else ("#F1F3F5","#ADB5BD","False","vf")
        g.append(f'<rect x="{cx-34}" y="{y}" width="68" height="24" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="1.4"/>')
        g.append(f'<text class="{cls}" x="{cx}" y="{y+16.5}" text-anchor="middle">{txt}</text>')
    out+=g
for r,(fn,sub) in enumerate([("is_either_on_line()","at least one dark (or)"),("is_at_cross()","both dark (and)")]):
    y=SY+SH+14+r*34
    out.append(f'<text class="fn" x="12" y="{y+12}">{fn}</text>')
    out.append(f'<text class="sm" x="12" y="{y+26}">{sub}</text>')
out.append(f'<text class="sm" x="12" y="{SY+40}">green ring = sensor</text>')
out.append(f'<text class="sm" x="12" y="{SY+55}">over black tape</text>')
out.append(f'<circle cx="140" cy="{SY+46}" r="5.8" fill="#FFD43B" stroke="#2E7D32" stroke-width="2.4"/>')
H=SY+SH+14+34+24+10
desc=('Four close-ups of the front of the XRP, where the two line sensors sit under the rangefinder, with what each sensor function returns. '
 'Both sensors on white: is_either_on_line() False, is_at_cross() False. Left sensor on the tape: True, False. Right sensor on the tape: True, False. '
 'On the cross, where a second taped line runs under both sensors: True, True.')
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 {H}" width="680" height="{H}" role="img" aria-labelledby="fpT fpD">
  <title id="fpT">What the two is_ functions return in four positions</title>
  <desc id="fpD">{desc}</desc>
  <style>
    .h  {{ font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 12px; font-weight: 700; fill: #22527B; }}
    .fn {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 12.5px; font-weight: 700; fill: #142D50; }}
    .sm {{ font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 11.5px; fill: #6C757D; }}
    .vt {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 12.5px; font-weight: 700; fill: #2E7D32; }}
    .vf {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 12.5px; font-weight: 600; fill: #868E96; }}
  </style>
  {defs.replace('<defs>','<defs>'+chr(10)+'    '+(chr(10)+'    ').join(clips))}
  <rect width="680" height="{H}" fill="#FFFFFF"/>
  {(chr(10)+'  ').join(out)}
</svg>
'''
open(OUTDIR+'four-positions.svg','w').write(svg); print(H)
