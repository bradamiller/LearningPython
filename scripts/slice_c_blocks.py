#!/usr/bin/env python3
"""
Slice the real XRP Blockly C-shaped block images (Repeat, If, function def, …)
into three pieces so the web version can *stretch* like the real editor does:

    <name>-bar.png    the top bar + the inner top notch  (full width)
    <name>-do.png     the spine slice that carries the "do" label
    <name>-fill.png   a 1px-tall clean slice of the spine, tiled to any height
    <name>-foot.png   the closing lip + the bottom connector tab

A C-block image has a distinctive profile: a full-width top bar, then a narrow
band (the left spine, ~38px), then a full-width foot. This finds that narrow
band automatically, so any container block in the dictionary is handled.

Writes the pieces to static/img/blocks/c/ and a manifest the React component
imports (src/components/cblocks.json) with each piece's pixel geometry.
"""

import json
import os
from PIL import Image

BLOCKS_DIR = os.path.join(os.path.dirname(__file__), '..', 'static', 'img', 'blocks')
OUT_DIR = os.path.join(BLOCKS_DIR, 'c')
MANIFEST = os.path.join(os.path.dirname(__file__), '..', 'src', 'components', 'cblocks.json')

ALPHA = 40          # opacity threshold for "this pixel is part of the block"
SPINE_SLACK = 3     # rows within this many px of the narrowest count as spine


def row_extents(im):
    """For each row: (min_x, max_x) of opaque pixels, or None for an empty row."""
    w, h = im.size
    px = im.load()
    out = []
    for y in range(h):
        xs = [x for x in range(w) if px[x, y][3] > ALPHA]
        out.append((min(xs), max(xs)) if xs else None)
    return out


def find_spine(im, extents):
    """
    The left spine: a tall run of left-aligned rows, clearly narrower than the
    block, with a wider bar above it and a wider foot below. Candidate runs are
    scored so the real spine wins over look-alikes such as the bottom connector
    tab (too short, not left-aligned) or an input notch (no foot beneath it).
    """
    w, h = im.size
    widths = [(e[1] - e[0] + 1) if e else 10 ** 6 for e in extents]
    left0 = [bool(e) and e[0] == 0 for e in extents]

    candidates = []
    y = 0
    while y < h:
        if widths[y] <= w * 0.6 and left0[y]:
            y1 = y
            while (y1 + 1 < h and left0[y1 + 1]
                   and abs(widths[y1 + 1] - widths[y]) <= SPINE_SLACK):
                y1 += 1
            candidates.append((y, y1, widths[y]))
            y = y1 + 1
        else:
            y += 1

    for y0, y1, narrow in sorted(candidates, key=lambda c: c[0] - c[1]):
        if y1 - y0 + 1 < 8:                     # a spine is a tall band
            continue
        above = [widths[i] for i in range(0, y0) if extents[i]]
        below = [widths[i] for i in range(y1 + 1, h) if extents[i]]
        if not above or not below:
            continue
        if y0 < 12 or max(above) < narrow + 10 or max(below) < narrow + 4:
            continue
        if not 6 <= (h - y1 - 1) <= 40:          # plausible closing lip + tab
            continue
        return y0, y1, narrow
    return None


def cleanest_row(im, y0, y1):
    """The spine row with the fewest distinct colors — i.e. no label glyphs on it."""
    px = im.load()
    spine_w = None
    best_y, best_n = y0, 10 ** 6
    for y in range(y0, y1 + 1):
        row = [px[x, y][:3] for x in range(im.size[0]) if px[x, y][3] > ALPHA]
        n = len(set(row))
        if n <= best_n:        # <= so ties take the lower row
            best_y, best_n, spine_w = y, n, len(row)
    return best_y, spine_w


def is_container(im, extents, spine):
    """A real C-block: full-width bar above the spine and a foot below it."""
    if spine is None:
        return False
    y0, y1, narrow = spine
    w, h = im.size
    if y0 < 4 or y1 > h - 5:
        return False                      # nothing above or below — not a C
    if narrow > w * 0.75:
        return False                      # spine isn't meaningfully narrower
    above = max((e[1] - e[0] + 1) for e in extents[:y0] if e)
    below = max((e[1] - e[0] + 1) for e in extents[y1 + 1:] if e)
    return above > narrow + 8 and below > narrow + 4


def slice_block(name, path):
    im = Image.open(path).convert('RGBA')
    w, h = im.size
    extents = row_extents(im)
    spine = find_spine(im, extents)
    if not is_container(im, extents, spine):
        return None

    y0, y1, narrow = spine
    # Trim any flare where the spine starts widening back out into the foot, so
    # a stretched spine stays perfectly straight.
    while y1 > y0 and (extents[y1][1] - extents[y1][0] + 1) > narrow + 1:
        y1 -= 1
    fill_y, spine_w = cleanest_row(im, y0, y1)

    bar = im.crop((0, 0, w, y0))                     # top bar + inner notch taper
    do = im.crop((0, y0, spine_w, y1 + 1))           # spine slice carrying "do"
    fill = im.crop((0, fill_y, spine_w, fill_y + 1))  # 1px tileable spine slice
    foot = im.crop((0, y1 + 1, w, h))                # closing lip + bottom tab

    os.makedirs(OUT_DIR, exist_ok=True)
    bar.save(os.path.join(OUT_DIR, f'{name}-bar.png'))
    do.save(os.path.join(OUT_DIR, f'{name}-do.png'))
    fill.save(os.path.join(OUT_DIR, f'{name}-fill.png'))
    foot.save(os.path.join(OUT_DIR, f'{name}-foot.png'))

    return {
        'barW': bar.size[0], 'barH': bar.size[1],
        'spineW': spine_w, 'doH': do.size[1],
        'footW': foot.size[0], 'footH': foot.size[1],
    }


def main():
    manifest = {}
    for fn in sorted(os.listdir(BLOCKS_DIR)):
        if not fn.endswith('.png'):
            continue
        name = fn[:-4]
        geo = slice_block(name, os.path.join(BLOCKS_DIR, fn))
        if geo:
            manifest[name] = geo
            print(f'{name:28s} bar {geo["barW"]}x{geo["barH"]}  '
                  f'spine {geo["spineW"]}x{geo["doH"]}  foot {geo["footW"]}x{geo["footH"]}')
    with open(MANIFEST, 'w') as f:
        json.dump(manifest, f, indent=2, sort_keys=True)
        f.write('\n')
    print(f'\n{len(manifest)} container blocks sliced → {OUT_DIR}')


if __name__ == '__main__':
    main()
