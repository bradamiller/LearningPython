#!/usr/bin/env python3
"""
Rewrite the value in a Blockly block's editable field.

    python3 scripts/relabel_block.py straight straight_cm30 0 30
    python3 scripts/relabel_block.py repeat   repeat_4      0 4
    python3 scripts/relabel_block.py function_def function_def_square 0 square

    <source name>  <output name>  <field index, left to right>  <new text>

Why this exists
---------------
`BlockProgram` composes figures out of the dictionary's block art, and that art
carries whatever value the block has when you first drag it out — `cm: 20`,
`repeat 10 times`, `to do something`. Lessons had been papering over that with a
note beside the block ("← cm: 30"), which means a figure whose whole job is to
say "this Blockly equals that Python" shows four numbers that disagree with the
Python next to it. Students compare pictures; they do not read the apology.

So: repaint the field instead. Everything except the glyphs is the real
artwork — same approach as `make_call_block.py`, which lifts its silhouettes
from real blocks rather than drawing them.

What it does NOT do
-------------------
Resize. A field keeps its original width, so replacing wide text with narrow
text leaves a roomy box. That is what Blockly itself looks like mid-edit, so it
reads fine; but text WIDER than the field would overflow, and the script refuses
rather than producing something misleading. If you need that, widen the field by
stretching a constant-profile column the way make_call_block.py does.
"""

import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage

FONT = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
BLOCKS = 'static/img/blocks'

# A field's outer shell is the light lavender plug; the part you type into is
# the brighter paper inside it.
SHELL_MIN = 150
PAPER_MIN = 225


def find_fields(rgb, alpha):
    """Editable fields, left to right, as (x0, y0, x1, y1) of the shell."""
    light = (alpha > 200) & (rgb.min(axis=2) > SHELL_MIN)
    lab, _ = ndimage.label(light)
    out = []
    for i, sl in enumerate(ndimage.find_objects(lab)):
        h, w = sl[0].stop - sl[0].start, sl[1].stop - sl[1].start
        if h >= 14 and w >= 20:                      # not a letter of a label
            out.append((sl[1].start, sl[0].start, sl[1].stop, sl[0].stop))
    return sorted(out)


def paper_area(rgb, alpha, field):
    """The bright rectangle inside a field where the value is drawn."""
    x0, y0, x1, y1 = field
    sub_rgb, sub_a = rgb[y0:y1, x0:x1], alpha[y0:y1, x0:x1]
    paper = (sub_a > 200) & (sub_rgb.min(axis=2) > PAPER_MIN)
    if paper.sum() < 40:                             # a flat-tinted field
        paper = (sub_a > 200) & (sub_rgb.min(axis=2) > SHELL_MIN)
    ys, xs = np.where(paper)
    return (x0 + xs.min(), y0 + ys.min(), x0 + xs.max() + 1, y0 + ys.max() + 1)


def relabel(src, dst, index, text):
    im = Image.open(f'{BLOCKS}/{src}.png').convert('RGBA')
    arr = np.asarray(im).astype(int)
    rgb, alpha = arr[..., :3], arr[..., 3]

    fields = find_fields(rgb, alpha)
    if not fields:
        sys.exit(f'{src}: no editable field found')
    if index >= len(fields):
        sys.exit(f'{src}: only {len(fields)} field(s), asked for #{index}')

    fx0, fy0, fx1, fy1 = fields[index]
    px0, py0, px1, py1 = paper_area(rgb, alpha, fields[index])
    # A numeric field has a distinctly brighter pill inside its plug; a text
    # field is one flat tone, so its "paper" IS the whole field. The flat kind
    # has no inner rounded edge to protect, so the clear can run a row lower.
    flat = (px1 - px0) >= (fx1 - fx0) - 2
    # paper_area bounds the BRIGHT pixels, so a descender that dips into the
    # field's lower edge falls outside it and survives the clear as a stray
    # stub. Reach one pixel further, still inside the field shell.
    py0, py1 = max(fy0 + 1, py0 - 1), min(fy1 - 1, py1 + 1)
    px0, px1 = max(fx0 + 1, px0 - 1), min(fx1 - 1, px1 + 1)
    patch = rgb[py0:py1, px0:px1].reshape(-1, 3)
    dark = patch[patch.max(axis=1) < 120]
    ink = tuple(np.percentile(dark, 12, axis=0).astype(int)) if len(dark) else (0, 0, 0)

    # Erase the OLD VALUE ONLY — not the field. Repainting the whole paper
    # rectangle squares off its rounded corners and, if you tile a row to get the
    # tone right, that row's corners smear across it. So: take the paper's own
    # dominant colour, and recolour just the pixels darker than it, inside a
    # 2px inset that keeps the corners out of reach.
    inner = rgb[py0 + 2:py1 - 2, px0 + 2:px1 - 2].reshape(-1, 3)
    # Relative, not a fixed threshold: a numeric field's paper is near-white but
    # the function-name field is a flat lavender, and both are "the light tone
    # in this field" relative to their own ink.
    cutoff = inner.min(axis=1).max() - 15
    bright = inner[inner.min(axis=1) >= cutoff]
    if len(bright) < 20:
        sys.exit(f'{src}: cannot read the paper colour of field #{index}')
    colours, counts = np.unique(bright, axis=0, return_counts=True)
    paper_rgb = colours[counts.argmax()]


    # Size the text to the paper height, the way the original glyphs are.
    size = max(9, int((py1 - py0) * 0.82))
    font = ImageFont.truetype(FONT, size)
    while font.getbbox(text)[2] > (px1 - px0) - 4 and size > 8:
        size -= 1
        font = ImageFont.truetype(FONT, size)
    if font.getbbox(text)[2] > (px1 - px0) - 2:
        sys.exit(f'{src}: "{text}" is wider than the field; widen the art instead')

    out = np.asarray(im).astype(np.uint8).copy()
    # 1px inset, not 2: a descender ("do something" has a g) reaches the bottom
    # row of the paper, and leaving it behind puts a stray tail next to the new
    # value. One pixel is enough to keep the field's own rounded edge.
    region = out[py0 + 1:py1 if flat else py1 - 1, px0 + 1:px1 - 1, :3]
    # Anything that isn't the paper colour is old value — including the pale
    # antialiasing around a glyph and the tail of a descender. A brightness
    # cutoff misses both; distance from the paper does not.
    off = np.abs(region.astype(int) - paper_rgb.astype(int)).max(axis=2)
    region[off > 12] = paper_rgb
    # A descender can be drawn PAST the bottom of its field, onto the block body
    # ("do something" has a g that does exactly this). Those pixels are outside
    # the field, so clearing the field leaves a stub under the new value. Sweep a
    # few rows below, recolouring anything dark with the body colour beside it.
    # Flat fields only: a pill field's bottom edge sits in exactly those rows and
    # is not a descender, and repainting it leaves a pale scar under the value.
    for r in (range(py1, min(py1 + 3, out.shape[0])) if flat else []):
        row = out[r, :, :3]
        outside = np.concatenate([row[max(0, px0 - 12):px0], row[px1:px1 + 12]])
        outside = outside[outside.max(axis=1) > 60]
        if not len(outside):
            continue
        body = np.median(outside, axis=0).astype(np.uint8)
        seg = out[r, px0:px1, :3]
        seg[np.abs(seg.astype(int) - body.astype(int)).max(axis=1) > 45] = body

    im = Image.fromarray(out)
    draw = ImageDraw.Draw(im)
    bb = draw.textbbox((0, 0), text, font=font)
    draw.text((((px0 + px1) - (bb[2] - bb[0])) / 2 - bb[0],
               ((py0 + py1) - (bb[3] - bb[1])) / 2 - bb[1]),
              text, font=font, fill=ink + (255,))

    im.save(f'{BLOCKS}/{dst}.png')
    print(f'{src}.png field #{index} -> "{text}"  ->  {dst}.png')


if __name__ == '__main__':
    if len(sys.argv) != 5:
        sys.exit(__doc__.strip().split('\n\n')[1])
    relabel(sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4])
