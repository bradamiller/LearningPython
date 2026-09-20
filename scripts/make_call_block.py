#!/usr/bin/env python3
"""
Generate a Blockly "call <function>" stack block PNG.

The XRP Blockly dictionary has no image for a function-call block, because the
block is generated per user-defined function name. This composes one that matches
the dictionary artwork: the SILHOUETTE (corner radii, top notch, bottom tab, and
its antialiasing) is lifted from a real block's alpha channel, so a generated
block stacks pixel-perfectly against real ones in <BlockProgram>. Only the fill,
border and label are drawn.

    python3 scripts/make_call_block.py square static/img/blocks/call_square.png

Colors are sampled from function_def.png so the block reads as the same
(purple) Functions category as the definition block it pairs with.
"""
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

DONOR = 'static/img/blocks/wait_for_button_press.png'
FONT = '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
FONT_SIZE = 15
PAD = 11               # donor: text starts 10px in, ends 13px from the right

FILL = (136, 84, 152)      # function_def.png body
BORDER = (106, 67, 119)    # function_def.png outline
HILITE = (170, 131, 182)   # function_def.png top highlight
TEXT = (255, 255, 255)

LEFT = 36    # columns carrying the left corners + top notch
RIGHT = 30   # columns carrying the right corners
SEAM = 148   # a constant-profile column to tile across the middle


def silhouette(width):
    """Donor alpha, widened to `width` by tiling a constant-profile column."""
    a = np.array(Image.open(DONOR).convert('RGBA'))[:, :, 3]
    h, w = a.shape
    mid_cols = max(width - LEFT - RIGHT, 1)
    mid = np.repeat(a[:, SEAM:SEAM + 1], mid_cols, axis=1)
    return np.concatenate([a[:, :LEFT], mid, a[:, w - RIGHT:]], axis=1)


def shade(mask):
    """Paint the silhouette: 1px border, 1px inner top highlight, flat fill."""
    h, w = mask.shape
    solid = mask > 128
    # A pixel is interior when all four neighbours are solid; the rest is outline.
    interior = solid.copy()
    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        interior &= np.roll(solid, (dy, dx), (0, 1))
    rgb = np.zeros((h, w, 3), np.uint8)
    rgb[solid] = BORDER
    rgb[interior] = FILL
    # Highlight the topmost interior pixel of each column, as the artwork does.
    for x in range(w):
        col = np.flatnonzero(interior[:, x])
        if col.size:
            rgb[col[0], x] = HILITE
    out = np.dstack([rgb, mask])
    return Image.fromarray(out, 'RGBA')


def build(label, out_path):
    font = ImageFont.truetype(FONT, FONT_SIZE)
    width = font.getbbox(label)[2] + PAD * 2
    img = shade(silhouette(width))
    draw = ImageDraw.Draw(img)
    # Anchor on the ascender line, not the glyph bounding box, so every label
    # shares one baseline: a word without capitals or descenders must not float.
    # The donor's cap-tops sit at y=7, which is 3px below its ascender line.
    draw.text((PAD - 1, 4), label, font=font, fill=TEXT)
    img.save(out_path)
    print(f'{out_path}  {img.size[0]}x{img.size[1]}  "{label}"')


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2])
