#!/usr/bin/env python3
"""
Generate a Blockly function-call block PNG, with or without parameters.

The XRP Blockly dictionary has no call block, because Blockly builds one per
user-defined function name. This composes one that matches the dictionary
artwork: every SILHOUETTE is lifted from a real block's alpha channel and
stretched through a constant-profile row/column, so corner radii, the top notch,
the bottom tab, the input socket and their antialiasing are the real artwork's
and a generated block stacks pixel-perfectly against real ones. Only fill,
border and labels are drawn.

    # no parameters -> a plain one-row stack block reading "square"
    python3 scripts/make_call_block.py square static/img/blocks/call_square.png

    # parameters -> label row "polygon with:", then one row per parameter,
    # each with a real numeric_const block plugged into a socket
    python3 scripts/make_call_block.py polygon static/img/blocks/call_polygon_4_30.png \
        --param sides=4 --param side_length=30

Geometry and colors were measured from Brad's real XRP Code screenshot
(static/img/blocks/programs/square-function.png), which is at the same scale as
the dictionary artwork: 26px rows, the value block hanging off the right edge of
its input row.
"""
import argparse

import numpy as np
from PIL import Image, ImageDraw, ImageFont

BODY = 'static/img/blocks/wait_for_button_press.png'   # plain stack block
VALUE = 'static/img/blocks/numeric_const.png'          # the number block
FONT = '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
FONT_SIZE = 15
PAD = 11             # donor: text starts 10px in
ROW = 26             # one row of block body
GAP = 14             # space between a parameter name and its socket

FILL = (136, 84, 152)      # function_def.png body
BORDER = (106, 67, 119)    # function_def.png outline
HILITE = (170, 131, 182)   # function_def.png top highlight
TEXT = (255, 255, 255)

# Donor slices that must be kept intact when stretching.
BODY_LEFT, BODY_RIGHT, BODY_SEAM = 36, 30, 148   # columns
BODY_TOP, BODY_BOT, BODY_ROW = 13, 17, 12        # rows
VAL_TAB = 9          # numeric_const: the plug, columns 0..8
VAL_SEAM = 22        # a constant column inside its white field
VAL_FIELD = (14, 5, 31, 20)


def _stretch(a, keep_lo, keep_hi, seam, target, axis):
    """Widen/heighten an array by repeating one constant-profile line."""
    lo = a[:, :keep_lo] if axis else a[:keep_lo]
    hi = a[:, a.shape[1] - keep_hi:] if axis else a[a.shape[0] - keep_hi:]
    line = a[:, seam:seam + 1] if axis else a[seam:seam + 1]
    n = target - keep_lo - keep_hi
    if n <= 0:                      # the kept slices already meet the target
        return np.concatenate([lo, hi], axis=axis)
    return np.concatenate([lo, np.repeat(line, n, axis=axis), hi], axis=axis)


def body_silhouette(width, height):
    a = np.array(Image.open(BODY).convert('RGBA'))[:, :, 3]
    a = _stretch(a, BODY_LEFT, BODY_RIGHT, BODY_SEAM, width, 1)
    return _stretch(a, BODY_TOP, BODY_BOT, BODY_ROW, height + 4, 0)


def shade(mask):
    """Paint a silhouette: 1px border, 1px inner top highlight, flat fill.

    The border is derived from the mask, so any socket cut into the mask gets
    an outline for free.
    """
    h, w = mask.shape
    solid = mask > 128
    interior = solid.copy()
    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        interior &= np.roll(solid, (dy, dx), (0, 1))
    rgb = np.zeros((h, w, 3), np.uint8)
    rgb[solid] = BORDER
    rgb[interior] = FILL
    for x in range(w):
        col = np.flatnonzero(interior[:, x])
        if col.size:
            rgb[col[0], x] = HILITE
    return Image.fromarray(np.dstack([rgb, mask]), 'RGBA')


def value_block(text, font):
    """A numeric_const block widened to fit `text`, relabelled."""
    a = np.array(Image.open(VALUE).convert('RGBA'))
    fx0, fy0, fx1, fy1 = VAL_FIELD
    need = font.getbbox(text)[2] + 12          # digits + padding inside the field
    have = fx1 - fx0 + 1
    if need > have:
        a = _stretch(a, VAL_SEAM, a.shape[1] - VAL_SEAM, VAL_SEAM, a.shape[1] + need - have, 1)
        fx1 += need - have
    img = Image.fromarray(a, 'RGBA')
    draw = ImageDraw.Draw(img)
    # Repaint the field's interior (not its rounded edge), then centre the text.
    field = tuple(int(v) for v in np.array(Image.open(VALUE).convert('RGBA'))[10, VAL_SEAM][:3])
    draw.rectangle([fx0 + 1, fy0 + 1, fx1 - 1, fy1 - 1], fill=field)
    draw.text(((fx0 + fx1) / 2, (fy0 + fy1) / 2), text, font=font,
              fill=(0, 0, 0), anchor='mm')
    return img


def build(name, params, out_path):
    font = ImageFont.truetype(FONT, FONT_SIZE)
    if not params:
        width = font.getbbox(name)[2] + PAD * 2
        img = shade(body_silhouette(width, ROW))
        ImageDraw.Draw(img).text((PAD - 1, 4), name, font=font, fill=TEXT)
        img.save(out_path)
        print(f'{out_path}  {img.size[0]}x{img.size[1]}  "{name}"')
        return

    label = f'{name}  with:'
    values = [value_block(str(v), font) for _, v in params]
    name_w = max(font.getbbox(p)[2] for p, _ in params)
    width = max(font.getbbox(label)[2] + PAD * 2, PAD + name_w + GAP + VAL_TAB)
    height = ROW * (1 + len(params))

    mask = body_silhouette(width, height)
    # Cut a socket for each plug so the purple edge is concave, as Blockly draws
    # it. The socket is exactly the plug's own alpha, so the plug fills it with
    # no seam; shade() then outlines the new edge along with the rest.
    plugs = []
    for i, val in enumerate(values):
        top = ROW * (i + 1) + (ROW - val.height) // 2
        x = width - VAL_TAB
        tab = np.array(val)[:, :VAL_TAB, 3] > 128
        region = mask[top:top + val.height, x:x + VAL_TAB]
        mask[top:top + val.height, x:x + VAL_TAB] = np.where(tab, 0, region)
        plugs.append((val, x, top))

    img = shade(mask)
    canvas = Image.new('RGBA', (width + max(v.width for v in values) - VAL_TAB, img.height))
    canvas.alpha_composite(img)
    for val, x, top in plugs:
        canvas.alpha_composite(val, (x, top))
    draw = ImageDraw.Draw(canvas)
    draw.text((PAD - 1, 4), label, font=font, fill=TEXT)
    for i, (p, _) in enumerate(params):
        draw.text((PAD - 1, ROW * (i + 1) + 4), p, font=font, fill=TEXT)
    canvas.save(out_path)
    print(f'{out_path}  {canvas.size[0]}x{canvas.size[1]}  "{label}" {params}')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('name')
    ap.add_argument('out')
    ap.add_argument('--param', action='append', default=[],
                    metavar='NAME=VALUE', help='repeatable, in argument order')
    args = ap.parse_args()
    build(args.name, [tuple(p.split('=', 1)) for p in args.param], args.out)
