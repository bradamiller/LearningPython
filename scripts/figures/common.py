import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
src=open(ROBOT_SRC).read()
DEFS=src[src.index('<defs>'):src.index('</defs>')+7]
STY='''<style>
    .h   { font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 700; fill: #22527B; }
    .n   { font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 12.5px; fill: #343A40; }
    .nb  { font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 12.5px; font-weight: 700; fill: #142D50; }
    .sm  { font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 11.5px; fill: #6C757D; }
    .ax  { font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 12px; font-weight: 700; fill: #6C757D; }
    .m   { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 12.5px; font-weight: 700; fill: #142D50; }
    .ms  { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 11.5px; font-weight: 600; fill: #343A40; }
  </style>'''
MK='''<marker id="aB" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#22527B"/></marker>
    <marker id="aW" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#FFFFFF"/></marker>
    <marker id="aG" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6C757D"/></marker>
    <marker id="aR" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#D1182C"/></marker>
    <marker id="aGr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#2E7D32"/></marker>'''
class G:
    def __init__(s,x0,y0,sp=70,n=4,tw=9,pad=32):
        s.x0,s.y0,s.sp,s.n,s.tw,s.pad=x0,y0,sp,n,tw,pad
    def p(s,a,b): return (s.x0+a*s.sp, s.y0+(s.n-1-b)*s.sp)   # (x, y): x across, y up the page
    def base(s,axes=True,north=True):
        x0,y0,sp,n,tw,pad=s.x0,s.y0,s.sp,s.n,s.tw,s.pad
        L=(n-1)*sp; o=[f'<rect x="{x0-pad}" y="{y0-pad}" width="{L+2*pad}" height="{L+2*pad}" rx="8" fill="#F3F4F6" stroke="#DEE2E6"/>']
        for i in range(n):
            o.append(f'<rect x="{x0+i*sp-tw/2}" y="{y0-pad}" width="{tw}" height="{L+2*pad}" fill="#2B2B2B"/>')
            o.append(f'<rect x="{x0-pad}" y="{y0+i*sp-tw/2}" width="{L+2*pad}" height="{tw}" fill="#2B2B2B"/>')
        if axes:
            for i in range(n):
                o.append(f'<text class="ax" x="{x0+i*sp}" y="{y0+L+pad+16}" text-anchor="middle">{i}</text>')
                o.append(f'<text class="ax" x="{x0-pad-10}" y="{y0+(n-1-i)*sp+4}" text-anchor="end">{i}</text>')
            o.append(f'<text class="ax" x="{x0+L/2}" y="{y0+L+pad+32}" text-anchor="middle" style="fill:#22527B">x →</text>')
            o.append(f'<text class="ax" x="{x0-pad-24}" y="{y0+L/2}" text-anchor="middle" transform="rotate(-90 {x0-pad-24} {y0+L/2})" style="fill:#22527B">y →</text>')
        if north:
            nx=x0+L+pad+22; ny=y0-pad+4
            o.append(f'<line x1="{nx}" y1="{ny+30}" x2="{nx}" y2="{ny+4}" stroke="#495057" stroke-width="2" marker-end="url(#aG)"/>')
            o.append(f'<text class="ax" x="{nx}" y="{ny+44}" text-anchor="middle">N</text>')
        return o
    def route(s,pts,color="#4C8BF5"):
        d='M '+' L '.join(f'{x} {y}' for x,y in (s.p(*q) for q in pts))
        return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="9" stroke-linejoin="round" stroke-linecap="round" opacity="0.85"/>'
    def dot(s,r,c,fill="#FFFFFF",stroke="#22527B",rad=7):
        x,y=s.p(r,c); return f'<circle cx="{x}" cy="{y}" r="{rad}" fill="{fill}" stroke="{stroke}" stroke-width="2.4"/>'
def tag(x,y,text,fill="#FFFFFF",stroke="#22527B",cls="ms",w=None):
    w=w or (len(text)*7+12)
    return f'<rect x="{x-w/2}" y="{y-11}" width="{w}" height="20" rx="5" fill="{fill}" stroke="{stroke}" stroke-width="1.4"/><text class="{cls}" x="{x}" y="{y+3.5}" text-anchor="middle">{text}</text>'
def svg(title,desc,body,W=680,H=380,extra=''):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="fT fD">
  <title id="fT">{title}</title>
  <desc id="fD">{desc}</desc>
  {STY}
  {DEFS.replace('<defs>','<defs>'+chr(10)+'    '+MK+extra)}
  <rect width="{W}" height="{H}" fill="#FFFFFF"/>
  {(chr(10)+'  ').join(body)}
</svg>
'''
