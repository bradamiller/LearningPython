"""4-2: a number is copied, a list is shared. Writes out/number-vs-list.svg.
Right panel is the hand-made two-names-one-list.svg, moved over."""
import os
from _paths import OUTDIR

def box(x, y, addr, value, name):
    return f'''  <g transform="translate({x},{y})">
    <rect width="150" height="88" rx="7" fill="#F8F9FA" stroke="#22527B" stroke-width="2"/>
    <rect width="150" height="24" rx="7" fill="#E9ECEF"/>
    <rect y="17" width="150" height="7" fill="#E9ECEF"/>
    <line x1="0" y1="24" x2="150" y2="24" stroke="#ADB5BD" stroke-width="1"/>
    <text class="addr" x="75" y="17" text-anchor="middle">{addr}</text>
    <text class="value" x="75" y="61" text-anchor="middle">{value}</text>
    <rect x="13" y="66" width="124" height="19" rx="4" fill="#fff" stroke="#D1182C" stroke-width="1.5"/>
    <text class="name" x="75" y="80" text-anchor="middle">{name}</text>
  </g>
'''

STYLE = '  <style>\n    .addr  { font-size: 11px; fill: #868E96; letter-spacing: .5px; }\n    .name  { font-size: 13px; font-weight: 700; fill: #D1182C; }\n    .value { font-size: 19px; font-weight: 700; fill: #343A40;\n             font-family: ui-monospace, Menlo, Consolas, monospace; }\n    .item  { font-size: 15px; font-weight: 700; fill: #343A40;\n             font-family: ui-monospace, Menlo, Consolas, monospace; }\n    .hdr   { font-size: 13px; font-weight: 700; fill: #22527B; letter-spacing: .6px; }\n    .cap   { font-size: 12.5px; fill: #495057; }\n    .capb  { font-size: 12.5px; fill: #495057; font-weight: 700; }\n  </style>\n\n  <defs>\n    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7"\n            orient="auto-start-reverse">\n      <path d="M 0 0 L 10 5 L 0 10 z" fill="#22527B"/>\n    </marker>\n  </defs>'
RIGHT = '  <text class="hdr" x="24" y="26">A LIST IS SHARED</text>\n\n  <!-- path -->\n  <g transform="translate(24,48)">\n    <rect width="150" height="88" rx="7" fill="#F8F9FA" stroke="#22527B" stroke-width="2"/>\n    <rect width="150" height="24" rx="7" fill="#E9ECEF"/>\n    <rect y="17" width="150" height="7" fill="#E9ECEF"/>\n    <line x1="0" y1="24" x2="150" y2="24" stroke="#ADB5BD" stroke-width="1"/>\n    <text class="addr" x="75" y="17" text-anchor="middle">2100</text>\n    <text class="value" x="75" y="61" text-anchor="middle">5120</text>\n    <rect x="13" y="66" width="124" height="19" rx="4" fill="#fff" stroke="#D1182C" stroke-width="1.5"/>\n    <text class="name" x="75" y="80" text-anchor="middle">path</text>\n  </g>\n\n  <!-- same_path -->\n  <g transform="translate(24,168)">\n    <rect width="150" height="88" rx="7" fill="#F8F9FA" stroke="#22527B" stroke-width="2"/>\n    <rect width="150" height="24" rx="7" fill="#E9ECEF"/>\n    <rect y="17" width="150" height="7" fill="#E9ECEF"/>\n    <line x1="0" y1="24" x2="150" y2="24" stroke="#ADB5BD" stroke-width="1"/>\n    <text class="addr" x="75" y="17" text-anchor="middle">2104</text>\n    <text class="value" x="75" y="61" text-anchor="middle">5120</text>\n    <rect x="13" y="66" width="124" height="19" rx="4" fill="#fff" stroke="#D1182C" stroke-width="1.5"/>\n    <text class="name" x="75" y="80" text-anchor="middle">same_path</text>\n  </g>\n\n  <!-- arrows -->\n  <path d="M 178 92 C 250 92, 250 140, 316 152" fill="none" stroke="#22527B" stroke-width="2.2"\n        marker-end="url(#arrow)"/>\n  <path d="M 178 212 C 250 212, 250 164, 316 152" fill="none" stroke="#22527B" stroke-width="2.2"\n        marker-end="url(#arrow)"/>\n\n  <!-- the list -->\n  <g transform="translate(324,92)">\n    <rect width="332" height="120" rx="9" fill="#fff" stroke="#22527B" stroke-width="2.5"/>\n    <rect width="332" height="26" rx="9" fill="#22527B"/>\n    <rect y="18" width="332" height="8" fill="#22527B"/>\n    <text x="166" y="18" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff"\n          letter-spacing=".5px">ADDRESS 5120 — ONE LIST LIVES HERE</text>\n\n    <rect x="22" y="46" width="128" height="34" rx="5" fill="#E9ECEF" stroke="#ADB5BD"/>\n    <text class="item" x="86" y="68" text-anchor="middle">(1, 0)</text>\n    <rect x="166" y="46" width="128" height="34" rx="5" fill="#E9ECEF" stroke="#ADB5BD"/>\n    <text class="item" x="230" y="68" text-anchor="middle">(2, 0)</text>\n\n    <text x="166" y="102" text-anchor="middle" font-size="11.5" fill="#868E96">room to grow, which a\n      fixed-size location does not have</text>\n  </g>\n\n'

LEFT = ('  <text class="hdr" x="24" y="26">A NUMBER IS COPIED</text>\n'
        + box(24, 48, 2108, 5, 'a') + box(24, 168, 2112, 5, 'b'))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 930 310" role="img"
     aria-labelledby="nvl-title nvl-desc" font-family="Montserrat, Helvetica, Arial, sans-serif">
  <title id="nvl-title">A number is copied; a list is shared</title>
  <desc id="nvl-desc">Left: after a = 5 and b = a, the locations named a and b each hold their own 5.
  Right: the locations named path and same_path each hold the number 5120, the address of one list,
  and arrows run from both to that list.</desc>
{STYLE}
{LEFT}
  <line x1="236" y1="14" x2="236" y2="262" stroke="#CED4DA" stroke-width="1.5" stroke-dasharray="5 5"/>
  <g transform="translate(250,0)">
{RIGHT}  </g>
  <text class="cap" x="24" y="290"><tspan class="capb">b = a</tspan> puts a second 5 in b.</text>
  <text class="cap" x="274" y="290"><tspan class="capb">same_path = path</tspan> copies the address, so appending through</text>
  <text class="cap" x="274" y="306">either variable changes the one list both lead to.</text>
</svg>
'''
open(os.path.join(OUTDIR, 'number-vs-list.svg'), 'w').write(svg)
