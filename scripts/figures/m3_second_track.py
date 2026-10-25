import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
src=open(ROBOT_SRC).read()
defs=src[src.index('<defs>'):src.index('</defs>')+7]
D='dur="12s" repeatCount="indefinite"'
S=0.65
def fade(): return f'<animate attributeName="opacity" values="1;1;0;0;1;1" keyTimes="0;.84;.88;.92;.96;1" {D}/>'
def show(t0,t1=.84): return f'<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;{t0};{t0+.01:.3f};{t1};{t1+.01:.3f};1" {D}/>'
def scene(x0,clip,values,kt,still_dy):
    cx=x0+60
    a=[f'<clipPath id="{clip}"><rect x="{x0}" y="52" width="120" height="300" rx="6"/></clipPath>',
       f'<g clip-path="url(#{clip})">',
       f'<rect x="{x0}" y="52" width="120" height="300" fill="#F3F4F6"/>',
       f'<rect x="{cx-6}" y="52" width="12" height="300" fill="#2B2B2B"/>',
       f'<rect x="{x0}" y="90" width="120" height="12" fill="#2B2B2B"/>',
       f'<rect x="{x0}" y="224" width="120" height="12" fill="#2B2B2B"/>',
       f'<g class="anim"><g transform="translate({cx} 335)">{fade()}<g><animateTransform attributeName="transform" type="translate" values="{values}" keyTimes="{kt}" {D}/><use href="#pcXRP" transform="scale({S})" opacity="0.92"/></g></g></g>',
       f'<g class="still"><use href="#pcXRP" transform="translate({cx} {335+still_dy}) scale({S})" opacity="0.92"/></g>',
       '</g>',
       f'<rect x="{x0}" y="52" width="120" height="300" rx="6" fill="none" stroke="#DEE2E6"/>']
    return '\n  '.join(a)
def code(x0,lines):
    bx=x0+132; out=[f'<rect x="{bx}" y="62" width="188" height="{20+24*len(lines)}" rx="6" fill="#F8F9FA" stroke="#DEE2E6"/>']
    for i,(txt,t0,t1,col) in enumerate(lines):
        y=86+24*i
        out.append(f'<rect x="{bx+4}" y="{y-15}" width="180" height="21" rx="4" fill="{col}" opacity="0"><animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;{t0};{t0+.01:.3f};{t1};{t1+.01:.3f};1" {D}/></rect>')
        out.append(f'<text class="code" x="{bx+10}" y="{y}">{txt}</text>')
    return '\n  '.join(out)
def notes(x0,y,lines,t0,cls,still=True):
    t=''.join(f'<text class="{cls}" x="{x0+132}" y="{y+16*i}">{l}</text>' for i,l in enumerate(lines))
    return f'<g class="anim" opacity="0">{show(t0)}{t}</g><g class="still">{t}</g>' if still else f'<g class="anim" opacity="0">{show(t0)}{t}</g>'
L=12; R=350
body=[
 '<text class="t" x="12" y="20">Track, then track again</text>',
 '<text class="sub" x="12" y="37">no drive-past in between</text>',
 '<text class="t" x="350" y="20">Track, drive past, track</text>',
 '<text class="sub" x="350" y="37">the arrival pair, twice</text>',
 scene(L,'c32L',"0 0;0 0;0 -66;0 -66;0 0;0 0","0;.04;.16;.88;.92;1",-66),
 scene(R,'c32R',"0 0;0 0;0 -66;0 -66;0 -105;0 -105;0 -200;0 -200;0 0;0 0","0;.34;.46;.48;.54;.56;.72;.88;.92;1",-200),
 code(L,[("track_to_intersection()",.04,.16,"#DCE8F3"),("track_to_intersection()",.18,.84,"#FBE3E6")]),
 code(R,[("track_to_intersection()",.34,.46,"#DCE8F3"),("drive_past_intersection()",.48,.54,"#DCE8F3"),("track_to_intersection()",.56,.84,"#E1F0E3")]),
 notes(L,150,["The sensors are still on the","cross, so is_at_cross() is","already True: the loop never","runs and the robot never moves."],.19,"note"),
 notes(R,174,["drive_past_intersection() put","the sensors past the tape, so","the second track has a line to","follow and a new cross to find."],.56,"note"),
 notes(L,268,["Stuck on the first","intersection ✗"],.2,"bad"),
 notes(R,268,["Parked on the next","intersection ✓"],.73,"ok"),
]
desc=('Two animated top-down drawings of the XRP driving up a taped line that crosses two other lines, each beside the code it runs. '
 'Left: track_to_intersection() then track_to_intersection() again. The first call follows the line until the sensors reach the first cross. '
 'The second call returns at once, because the sensors are still on the cross and is_at_cross() is already True, so the robot never moves past the first intersection. '
 'Right: track_to_intersection(), drive_past_intersection(), track_to_intersection(). The drive-past moves the robot 8.75 cm so its center of rotation is on the cross and its sensors are past the tape, '
 'and the second track follows the line to the next intersection. The animation repeats.')
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 362" width="680" height="362" role="img" aria-labelledby="t32 d32">
  <title id="t32">Why drive_past_intersection() comes between two tracks</title>
  <desc id="d32">{desc}</desc>
  <style>
    .t    {{ font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 700; fill: #22527B; }}
    .sub  {{ font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 12px; fill: #495057; }}
    .code {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 12px; font-weight: 600; fill: #142D50; }}
    .note {{ font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 12px; fill: #495057; }}
    .bad  {{ font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 13px; font-weight: 700; fill: #D1182C; }}
    .ok   {{ font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 13px; font-weight: 700; fill: #2E7D32; }}
    .still {{ display: none; }}
    @media (prefers-reduced-motion: reduce) {{ .anim {{ display: none; }} .still {{ display: inline; }} }}
  </style>
  {defs}
  <rect width="680" height="362" fill="#FFFFFF"/>
  {chr(10).join("  "+b for b in body)}
</svg>
'''
open(OUTDIR+'second-track.svg','w').write(svg)
