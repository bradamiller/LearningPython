import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
W,H=680,360
E=[("graph","nodes and edges"),("motor","turns a wheel"),("robot","senses and acts"),("sensor","measures the world")]
S=[f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>']
S.append('<text class="h" x="20" y="24">A dictionary looks things up by word</text>')
# book: cover, two pages
BX,BY,BW,BH=24,44,380,280
S.append(f'<rect x="{BX-8}" y="{BY+6}" width="{BW+16}" height="{BH+4}" rx="14" fill="#8C2A2A"/>')   # cover
S.append(f'<path d="M {BX} {BY+10} Q {BX+BW/4} {BY-4} {BX+BW/2} {BY+12} L {BX+BW/2} {BY+BH} Q {BX+BW/4} {BY+BH-12} {BX} {BY+BH} Z" fill="#FFFBF0" stroke="#C9B98F" stroke-width="1.5"/>')
S.append(f'<path d="M {BX+BW} {BY+10} Q {BX+3*BW/4} {BY-4} {BX+BW/2} {BY+12} L {BX+BW/2} {BY+BH} Q {BX+3*BW/4} {BY+BH-12} {BX+BW} {BY+BH} Z" fill="#FFF7E6" stroke="#C9B98F" stroke-width="1.5"/>')
S.append(f'<line x1="{BX+BW/2}" y1="{BY+12}" x2="{BX+BW/2}" y2="{BY+BH}" stroke="#B9A776" stroke-width="2"/>')
# page headers
S.append(f'<text class="ph" x="{BX+30}" y="{BY+36}">graph – motor</text>')
S.append(f'<text class="ph" x="{BX+BW-30}" y="{BY+36}" text-anchor="end">robot – sensor</text>')
# thumb tabs on right edge
for i,l in enumerate("ABCDEFGHIJKLMNOPQRS"[::2]):
    y=BY+30+i*24
    hl = l in "QS" if False else l=="S"
    fill="#FDECEE" if l=="S" else "#EFE6CF"
    S.append(f'<rect x="{BX+BW+2}" y="{y}" width="18" height="20" rx="4" fill="{fill}" stroke="#B9A776"/><text class="tab" x="{BX+BW+11}" y="{y+14}" text-anchor="middle">{l}</text>')
# entries: two per page
pos=[(BX+28,BY+70),(BX+28,BY+170),(BX+BW/2+22,BY+70),(BX+BW/2+22,BY+170)]
for (w,d),(x,y) in zip(E,pos):
    hl = w=="sensor"
    if hl: S.append(f'<rect x="{x-8}" y="{y-20}" width="166" height="70" rx="8" fill="#FFF3B0" opacity="0.9"/>')
    S.append(f'<text class="hw" x="{x}" y="{y}">{w}</text>')
    S.append(f'<text class="pos" x="{x+len(w)*10+8}" y="{y}">noun</text>')
    S.append(f'<text class="df" x="{x}" y="{y+22}">{d}</text>')
    S.append(f'<line x1="{x}" y1="{y+38}" x2="{x+140}" y2="{y+38}" stroke="#E2D6B5" stroke-width="1"/>')
# key/value labels on the highlighted entry
x,y=pos[3]
S.append(f'<path d="M {x+30} {y-28} C {x+40} {y-50} {x+70} {y-56} {x+96} {y-56}" fill="none" stroke="#D1182C" stroke-width="2" marker-end="url(#ar)"/>')
S.append(f'<text class="kv" x="{x+100}" y="{y-52}" style="fill:#D1182C">key</text>')
S.append(f'<path d="M {x+40} {y+30} C {x+36} {y+56} {x+20} {y+64} {x+6} {y+70}" fill="none" stroke="#22527B" stroke-width="2" marker-end="url(#ab)"/>')
S.append(f'<text class="kv" x="{x+14}" y="{y+84}" style="fill:#22527B">value</text>')
# magnifying glass (cartoon) over sensor
S.append(f'<g transform="translate({x+138} {y-8}) rotate(-20)"><circle r="18" fill="#D6ECFA" fill-opacity="0.35" stroke="#5F666D" stroke-width="4"/><rect x="-4" y="17" width="8" height="26" rx="3" fill="#5F666D"/></g>')
# python card
PX=424
S.append(f'<rect x="{PX}" y="{BY}" width="248" height="{BH+10}" rx="12" fill="#F8F9FA" stroke="#ADB5BD"/>')
S.append(f'<text class="ch" x="{PX+14}" y="{BY+26}">The same idea in Python</text>')
code=['glossary = {','  "graph": "nodes and edges",','  "motor": "turns a wheel",','  "robot": "senses and acts",','  "sensor": "measures the world",','}']
for i,l in enumerate(code):
    S.append(f'<text class="cd" x="{PX+14}" y="{BY+54+i*19}" style="white-space:pre">{l}</text>')
y0=BY+54+len(code)*19+18
S.append(f'<text class="cd" x="{PX+14}" y="{y0}">glossary["sensor"]</text>')
S.append(f'<text class="cd" x="{PX+14}" y="{y0+20}" style="fill:#22527B">  "measures the world"</text>')
# key/value legend under code
S.append(f'<text class="lg" x="{PX+14}" y="{y0+45}"><tspan style="fill:#D1182C;font-weight:700">key</tspan>: the word you look up</text>')
S.append(f'<text class="lg" x="{PX+14}" y="{y0+62}"><tspan style="fill:#22527B;font-weight:700">value</tspan>: what you find there</text>')
S.append(f'<text class="lg" x="{PX+14}" y="{y0+83}">No page-flipping: give the key,</text>')
S.append(f'<text class="lg" x="{PX+14}" y="{y0+98}">get the value straight back.</text>')
defs='''<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#D1182C"/></marker>
<marker id="ab" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#22527B"/></marker></defs>'''
style='''<style>
 .h{font-family:Montserrat,Helvetica,Arial,sans-serif;font-size:14px;font-weight:700;fill:#22527B}
 .ph{font-family:Georgia,'Times New Roman',serif;font-size:11px;font-style:italic;fill:#8A7A55}
 .hw{font-family:Georgia,'Times New Roman',serif;font-size:19px;font-weight:700;fill:#2B2B2B}
 .pos{font-family:Georgia,'Times New Roman',serif;font-size:12px;font-style:italic;fill:#8A7A55}
 .df{font-family:Georgia,'Times New Roman',serif;font-size:13.5px;fill:#343A40}
 .tab{font-family:Georgia,serif;font-size:11px;font-weight:700;fill:#5F4B3B}
 .kv{font-family:Montserrat,Helvetica,Arial,sans-serif;font-size:13px;font-weight:800}
 .ch{font-family:Montserrat,Helvetica,Arial,sans-serif;font-size:12.5px;font-weight:700;fill:#142D50}
 .cd{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:11px;font-weight:600;fill:#142D50}
 .lg{font-family:Montserrat,Helvetica,Arial,sans-serif;font-size:11.5px;fill:#343A40}
</style>'''
desc='A cartoon of an open printed dictionary with four entries, each a bold word with its definition: graph, nodes joined by edges; motor, turns a wheel; robot, senses, thinks, acts; sensor, measures the world. Letter tabs run down the edge, and a magnifying glass hovers over the highlighted entry for sensor, where the word is labeled key and the definition is labeled value. Beside it, the same entries as a Python dictionary called glossary, with words as keys and definitions as values, and glossary["sensor"] giving "measures the world".'
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d"><title id="t">A dictionary, in print and in Python</title><desc id="d">{desc}</desc>{defs}{style}{chr(10).join(S)}</svg>'''
open(OUTDIR+'word-dictionary.svg','w').write(svg)
