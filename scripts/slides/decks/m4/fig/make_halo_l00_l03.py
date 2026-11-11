"""Slide-only copies of Module 4 figures whose text uses a halo
(paint-order: stroke). cairosvg ignores paint-order, so the white halo stroke
is drawn on top of the letters and hides them. Each copy draws the halo as a
separate text underneath, then the letters with no stroke. cairosvg also
ignores CSS white-space:pre, which drops the indentation of code lines, so
those texts get xml:space="preserve".

    python3 scripts/slides/decks/m4/fig/make_halo_l00_l03.py
"""
import copy
import os
import re

from lxml import etree

HERE = os.path.dirname(os.path.abspath(__file__))
STATIC = os.path.join(HERE, '..', '..', '..', '..', '..', 'static')
FIGS = ['lesson-m4-00/manhattan-grid', 'lesson-m4-01/coordinates-xy',
        'lesson-m4-01/naming-intersections', 'lesson-m4-01/tuple-on-grid',
        'lesson-m4-02/build-path']


def _props(css):
    return dict((k.strip(), v.strip()) for k, v in
                (p.split(':', 1) for p in css.split(';') if ':' in p))


def fix(svg):
    root = etree.fromstring(svg)
    css = ''.join(e.text or '' for e in root.iter() if isinstance(e.tag, str)
                  and etree.QName(e).localname == 'style')
    halo_classes = {}
    for name, body in re.findall(r'\.([\w-]+)\s*\{([^}]*)\}', css):
        p = _props(body)
        if p.get('paint-order') == 'stroke':
            halo_classes[name] = p
    texts = [e for e in root.iter() if isinstance(e.tag, str)
             and etree.QName(e).localname == 'text']
    for t in texts:
        if 'white-space:pre' in (t.get('style') or '').replace(' ', ''):
            t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    for t in texts:
        inline = _props(t.get('style', ''))
        p = {}
        for c in (t.get('class') or '').split():
            p.update(halo_classes.get(c, {}))
        p.update(inline)
        if p.get('paint-order') != 'stroke':
            continue
        stroke = p.get('stroke', '#FFFFFF')
        width = p.get('stroke-width', '4px')
        halo = copy.deepcopy(t)
        extra = f';fill:{stroke};stroke:{stroke};stroke-width:{width};stroke-linejoin:round'
        halo.set('style', (halo.get('style') or '') + extra)
        for sub in halo.iter():
            if not isinstance(sub.tag, str):
                continue
            name = etree.QName(sub).localname
            if name == 'tspan':
                sub.set('style', (sub.get('style') or '') + extra)
            elif name in ('animate', 'set') and sub.get('attributeName') in ('fill', 'stroke'):
                sub.getparent().remove(sub)
        t.addprevious(halo)
        t.set('style', (t.get('style') or '') + ';stroke:none')
    return etree.tostring(root)


if __name__ == '__main__':
    for f in FIGS:
        with open(os.path.join(STATIC, 'img', f + '.svg'), 'rb') as fh:
            out = fix(fh.read())
        dest = os.path.join(HERE, f.split('/')[1] + '.svg')
        with open(dest, 'wb') as fh:
            fh.write(out)
        print(dest)
