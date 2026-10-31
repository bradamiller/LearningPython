"""Sketch-style PowerPoint decks for the lessons.

Brad's pick (2026-10-31): one style for every deck, the hand-drawn "sketch"
look from the Module 3 trial (IntoToPython/templates/sketch-style-html-slides.md),
built as .pptx so teachers can edit it in PowerPoint or Google Slides.

A deck is a plain Python list of slide dicts (see decks/). This module turns
that list into a .pptx. The lesson page on the site is the source of truth:
a deck follows its lesson section by section, uses the lesson's own figures
(rendered from static/img/*.svg), and never shows a solution.

Text in any field may use `code` for Fira Mono and **bold**.

Fonts: Caveat (titles), Patrick Hand (body), Fira Mono (code), all Google
Fonts, so Google Slides has them built in; PowerPoint needs them installed
(the README in static/slides says where to get them).
"""

import os
import re

import cairosvg
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
STATIC = os.path.join(REPO, 'static')
CACHE = os.path.join(HERE, '.figcache')

# ---- palette (templates/sketch-style-html-slides.md) ----
TEAL = RGBColor(0x5B, 0x8F, 0xA8)
ORANGE = RGBColor(0xE8, 0xA8, 0x7C)
GREEN = RGBColor(0x5E, 0xA8, 0x64)
RED = RGBColor(0xC8, 0x4B, 0x4B)
DARK = RGBColor(0x2D, 0x34, 0x36)
MUTED = RGBColor(0x63, 0x6E, 0x72)
BORDER = RGBColor(0xB8, 0xC5, 0xD0)
PAPER = RGBColor(0xFD, 0xFC, 0xFA)
RULE = RGBColor(0xE6, 0xEE, 0xF3)
CODE_BG = RGBColor(0xF0, 0xED, 0xE8)
TEAL_BG = RGBColor(0xE4, 0xEF, 0xF4)
ORANGE_BG = RGBColor(0xFD, 0xF0, 0xE6)
GREEN_BG = RGBColor(0xE8, 0xF5, 0xE9)

TITLE_FONT = 'Caveat'
BODY_FONT = 'Patrick Hand'
CODE_FONT = 'Fira Mono'      # not Fira Code: its ligatures turn == into one glyph

W, H = Inches(13.333), Inches(7.5)
MARGIN = Inches(0.7)
TOP = Inches(1.45)          # first line under the title bar

TONES = {
    'teal': (TEAL, TEAL_BG),
    'orange': (ORANGE, ORANGE_BG),
    'green': (GREEN, GREEN_BG),
}


# ---------------------------------------------------------------- text runs

_RUN = re.compile(r'(`[^`]+`|\*\*[^*]+\*\*)')


def _runs(p, text, size, color=DARK, font=BODY_FONT, bold=False):
    """Fill paragraph p with text, honoring `code` and **bold**."""
    for part in _RUN.split(text):
        if not part:
            continue
        r = p.add_run()
        if part.startswith('`'):
            r.text = part[1:-1]
            r.font.name = CODE_FONT
            r.font.size = Pt(round(size * 0.86))
            r.font.color.rgb = DARK
            r.font.bold = bold
        elif part.startswith('**'):
            r.text = part[2:-2]
            r.font.name = font
            r.font.size = Pt(size)
            r.font.color.rgb = color
            r.font.bold = True
        else:
            r.text = part
            r.font.name = font
            r.font.size = Pt(size)
            r.font.color.rgb = color
            r.font.bold = bold


def _box(slide, left, top, width, height):
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.05)
    tf.margin_top = tf.margin_bottom = Inches(0.03)
    return tf


def text(slide, s, left, top, width, height, size=22, color=DARK,
         font=BODY_FONT, bold=False, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    tf = _box(slide, left, top, width, height)
    tf.vertical_anchor = anchor
    lines = s.split('\n')
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        _runs(p, line, size, color, font, bold)
    return tf


def _bullet(p, level, size):
    """A real hanging bullet, so a wrapped line lines up under the text."""
    from pptx.oxml.ns import qn
    from lxml import etree
    pPr = p._p.get_or_add_pPr()
    hang = int(Pt(size) * 0.9)
    pPr.set('marL', str(hang + int(Inches(0.45)) * level))
    pPr.set('indent', str(-hang))
    color = TEAL if level == 0 else MUTED
    clr = etree.SubElement(pPr, qn('a:buClr'))
    etree.SubElement(clr, qn('a:srgbClr')).set('val', str(color))
    etree.SubElement(pPr, qn('a:buFont')).set('typeface', BODY_FONT)
    etree.SubElement(pPr, qn('a:buChar')).set('char', '•' if level == 0 else '–')


def bullets(slide, items, left, top, width, height, size=22, gap=8):
    """A bullet list; an item that is a list is a sub-list of the one before."""
    tf = _box(slide, left, top, width, height)
    first = True

    def add(item, level):
        nonlocal first
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.space_after = Pt(gap)
        _bullet(p, level, size - 2 * level)
        _runs(p, item, size - 2 * level)

    for item in items:
        if isinstance(item, (list, tuple)):
            for sub in item:
                add(sub, 1)
        else:
            add(item, 0)
    return tf


# ---------------------------------------------------------------- shapes

def _shape(slide, kind, left, top, width, height, fill=None, line=None,
           weight=2.25, tilt=0.0):
    s = slide.shapes.add_shape(kind, left, top, width, height)
    if fill is None:
        s.fill.background()
    else:
        s.fill.solid()
        s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line
        s.line.width = Pt(weight)
    s.shadow.inherit = False
    if tilt:
        s.rotation = tilt
    if kind == MSO_SHAPE.ROUNDED_RECTANGLE:
        s.adjustments[0] = 0.08
    return s


def paper(slide):
    bg = slide.background.fill
    bg.solid()
    bg.fore_color.rgb = PAPER
    # faint notebook rules
    y = Inches(1.6)
    while y < H - Inches(0.2):
        _shape(slide, MSO_SHAPE.RECTANGLE, 0, y, W, Pt(0.75), fill=RULE)
        y += Inches(0.42)


def title_bar(slide, title, tag=None):
    _shape(slide, MSO_SHAPE.RECTANGLE, 0, 0, W, Inches(1.1), fill=TEAL_BG)
    _shape(slide, MSO_SHAPE.RECTANGLE, 0, Inches(1.1), W, Pt(3), fill=TEAL)
    text(slide, title, MARGIN, Inches(0.12), W - 2 * MARGIN - Inches(2.2), Inches(0.9),
         size=40, font=TITLE_FONT, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    if tag:
        text(slide, tag, W - MARGIN - Inches(2.4), Inches(0.3), Inches(2.4), Inches(0.5),
             size=16, color=TEAL, align=PP_ALIGN.RIGHT)


def callout(slide, s, left, top, width, height, tone='orange', size=22, tilt=-0.4,
            align=PP_ALIGN.CENTER, font=BODY_FONT):
    line, fill = TONES[tone]
    _shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height,
           fill=fill, line=line, tilt=tilt)
    return text(slide, s, left + Inches(0.25), top + Inches(0.08), width - Inches(0.5),
                height - Inches(0.16), size=size, align=align, font=font,
                anchor=MSO_ANCHOR.MIDDLE)


CODE_ADVANCE = 0.6          # Fira Mono: every glyph is 0.6 em wide


def code_fit(code, width, size):
    """The largest size <= size at which the widest line fits in width."""
    longest = max((len(l) for l in code.strip('\n').split('\n')), default=1) or 1
    room = (width - Inches(0.5)) / 12700          # points
    return max(10, min(size, int(room / (longest * CODE_ADVANCE) * 2) / 2))


def code_width(code, size):
    """The box width a block needs at size, padding included."""
    longest = max((len(l) for l in code.strip('\n').split('\n')), default=1)
    return Emu(int(longest * CODE_ADVANCE * size * 12700 + Inches(0.6)))


def code_block(slide, code, left, top, width, height=None, size=16):
    lines = code.strip('\n').split('\n')
    size = code_fit(code, width, size)
    line_h = Pt(size * 1.38)
    if height is None:
        height = Emu(int(line_h * len(lines) + Inches(0.4)))
    _shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height,
           fill=CODE_BG, line=BORDER)
    tf = _box(slide, left + Inches(0.25), top + Inches(0.15), width - Inches(0.4),
              height - Inches(0.25))
    tf.word_wrap = False
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(0)
        p.line_spacing = 1.0
        hash_at = _comment_start(line)
        parts = [(line, DARK)] if hash_at < 0 else [(line[:hash_at], DARK), (line[hash_at:], MUTED)]
        for chunk, color in parts:
            if not chunk:
                continue
            r = p.add_run()
            r.text = chunk
            r.font.name = CODE_FONT
            r.font.size = Pt(size)
            r.font.color.rgb = color
    return height


def _comment_start(line):
    """Index of a # that starts a comment (not one inside a string), or -1."""
    quote = None
    for i, ch in enumerate(line):
        if quote:
            if ch == quote:
                quote = None
        elif ch in '"\'':
            quote = ch
        elif ch == '#':
            return i
    return -1


def _num(v):
    return [float(x) for x in re.split(r'[\s,]+', v.strip()) if x]


def freeze_svg(svg_bytes, at):
    """Replace each SMIL animation by its value at fraction `at` of the longest
    animation, so a static render shows that moment instead of the first frame."""
    from lxml import etree
    root = etree.fromstring(svg_bytes)
    anims = [e for e in root.iter() if isinstance(e.tag, str)
             and etree.QName(e).localname in ('animate', 'animateTransform')]
    if not anims:
        return svg_bytes
    durs = [float(e.get('dur', '1s').rstrip('s')) for e in anims]
    t = max(durs) * at
    for e, dur in zip(anims, durs):
        vals = e.get('values', '').split(';')
        keys = [float(k) for k in e.get('keyTimes', '').split(';')] if e.get('keyTimes') \
            else [i / max(1, len(vals) - 1) for i in range(len(vals))]
        f = min(t / dur, 1.0) if e.get('repeatCount') != 'indefinite' else (t % dur) / dur
        if at >= 1.0:
            f = 1.0
        i = max(j for j, k in enumerate(keys) if k <= f + 1e-9)
        v = vals[i]
        if e.get('calcMode', 'linear') != 'discrete' and i + 1 < len(vals):
            a, b = _num(vals[i]), _num(vals[i + 1])
            span = keys[i + 1] - keys[i]
            u = (f - keys[i]) / span if span > 0 else 0
            if len(a) == len(b):
                v = ' '.join(f'{x + (y - x) * u:.3f}' for x, y in zip(a, b))
        parent = e.getparent()
        name = e.get('attributeName')
        if etree.QName(e).localname == 'animateTransform':
            v = f"{e.get('type', 'translate')}({v})"
        parent.set(name, v)
        parent.remove(e)
    return etree.tostring(root)


def figure(slide, src, left, top, max_w, max_h, frame=None, crop=None):
    """Place a site figure (path under static/, .svg or raster), fit and centered.
    frame: for an animated SVG, the moment to show, 0..1 of one run (default 0.5).
    crop: (x0, y0, x1, y1) as fractions of the figure, to show only part of it."""
    # '/img/...' is a site figure under static/; './...' is a slide-only copy
    # under scripts/slides/ (for a figure the slide renderer draws badly)
    path = os.path.join(HERE, src[2:]) if src.startswith('./') else \
        os.path.join(STATIC, src.lstrip('/'))
    if path.endswith('.svg'):
        os.makedirs(CACHE, exist_ok=True)
        at = 0.5 if frame is None else frame
        tag = f'@{at:.3f}' + ('' if not crop else '_' + '_'.join(f'{c:.2f}' for c in crop))
        png = os.path.join(CACHE, src.strip('./').replace('/', '__') + tag + '.png')
        if not os.path.exists(png) or os.path.getmtime(png) < os.path.getmtime(path):
            with open(path, 'rb') as fh:
                data = freeze_svg(fh.read(), at)
            cairosvg.svg2png(bytestring=data, write_to=png, output_width=2000)
            if crop:
                from PIL import Image
                im = Image.open(png)
                x0, y0, x1, y1 = crop
                im.crop((int(x0 * im.width), int(y0 * im.height),
                         int(x1 * im.width), int(y1 * im.height))).save(png)
        path = png
    pic = slide.shapes.add_picture(path, left, top)
    ratio = min(max_w / pic.width, max_h / pic.height)
    pic.width, pic.height = int(pic.width * ratio), int(pic.height * ratio)
    pic.left = int(left + (max_w - pic.width) / 2)
    pic.top = int(top + (max_h - pic.height) / 2)
    return pic


def notes(slide, s):
    if s:
        slide.notes_slide.notes_text_frame.text = s.strip()


# ---------------------------------------------------------------- slide kinds

def s_title(prs, d, deck):
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    paper(sl)
    robot = os.path.join(HERE, 'assets', 'xrp.png')
    if os.path.exists(robot):
        p = sl.shapes.add_picture(robot, 0, Inches(0.45), height=Inches(1.5))
        p.left = int((W - p.width) / 2)
    text(sl, f"MODULE {deck['module']}  ·  LESSON {deck['module']}-{deck['lesson']}",
         0, Inches(2.0), W, Inches(0.5), size=22, color=TEAL, align=PP_ALIGN.CENTER)
    text(sl, deck['title'], Inches(0.8), Inches(2.45), W - Inches(1.6), Inches(1.1),
         size=60, font=TITLE_FONT, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    _shape(sl, MSO_SHAPE.RECTANGLE, int(W / 2 - Inches(2)), Inches(3.6), Inches(4), Pt(4),
           fill=ORANGE, tilt=-0.6)
    if d.get('objectives'):
        text(sl, 'By the end of this lesson you can', Inches(1.3), Inches(3.95),
             Inches(10), Inches(0.5), size=26, font=TITLE_FONT, color=TEAL, bold=True)
        bullets(sl, d['objectives'], Inches(1.3), Inches(4.45), W - Inches(2.6),
                Inches(2.9), size=20, gap=4)
    notes(sl, d.get('notes'))


def s_bullets(prs, d, deck):
    """Title, bullets, and optionally a figure, a code block or a callout."""
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    paper(sl)
    title_bar(sl, d['title'], d.get('tag'))
    has_side = 'figure' in d or 'code' in d
    split = d.get('split', 0.5)
    tw = (W - 2 * MARGIN) * (split if has_side else 1) - (Inches(0.3) if has_side else 0)
    bottom = H - Inches(0.4)
    if d.get('callout'):
        bottom -= Inches(1.2)
    y = TOP
    if d.get('lead'):
        text(sl, d['lead'], MARGIN, y, tw, Inches(1.0), size=d.get('size', 24))
        y += Inches(d.get('lead_h', 0.9))
    if d.get('bullets'):
        n = sum(len(b) if isinstance(b, (list, tuple)) else 1 for b in d['bullets'])
        size = d.get('size') or (28 if (n <= 5 and not has_side) else 24)
        bullets(sl, d['bullets'], MARGIN, y, tw, bottom - y, size=size, gap=12 if size > 24 else 8)
    if has_side:
        sx = MARGIN + (W - 2 * MARGIN) * split
        sw = W - MARGIN - sx
        if 'figure' in d:
            figure(sl, d['figure'], sx, TOP, sw, bottom - TOP, d.get('frame'), d.get('crop'))
        else:
            code_block(sl, d['code'], sx, TOP, sw, size=d.get('code_size', 16))
    if d.get('callout'):
        callout(sl, d['callout'], MARGIN + Inches(0.5), H - Inches(1.45),
                W - 2 * MARGIN - Inches(1.0), Inches(0.95), tone=d.get('tone', 'orange'))
    notes(sl, d.get('notes'))


def s_figure(prs, d, deck):
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    paper(sl)
    title_bar(sl, d['title'], d.get('tag'))
    bottom = H - Inches(0.35)
    if d.get('caption'):
        bottom -= Inches(0.85)
    figure(sl, d['figure'], MARGIN, TOP, W - 2 * MARGIN, bottom - TOP, d.get('frame'), d.get('crop'))
    if d.get('caption'):
        text(sl, d['caption'], MARGIN, H - Inches(1.1), W - 2 * MARGIN, Inches(0.8),
             size=22, color=MUTED, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    notes(sl, d.get('notes'))


def s_frames(prs, d, deck):
    """One animated figure shown at several moments, side by side, each captioned.
    frames: [(moment 0..1, caption), ...]; crop as for figure."""
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    paper(sl)
    title_bar(sl, d['title'], d.get('tag'))
    frames = d['frames']
    gap = Inches(0.3)
    fw = int((W - 2 * MARGIN - gap * (len(frames) - 1)) / len(frames))
    bottom = H - Inches(0.35) - (Inches(1.15) if d.get('callout') else 0)
    fh = bottom - TOP - Inches(0.75)
    for i, (at, cap) in enumerate(frames):
        x = MARGIN + (fw + gap) * i
        figure(sl, d['figure'], x, TOP, fw, fh, at, d.get('crop'))
        text(sl, cap, x, TOP + fh + Inches(0.1), fw, Inches(0.6), size=20,
             align=PP_ALIGN.CENTER)
    if d.get('callout'):
        callout(sl, d['callout'], MARGIN + Inches(0.5), H - Inches(1.35),
                W - 2 * MARGIN - Inches(1.0), Inches(0.9), tone=d.get('tone', 'teal'))
    notes(sl, d.get('notes'))


def s_code(prs, d, deck):
    """Title, an optional lead line, a code block, an optional callout."""
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    paper(sl)
    title_bar(sl, d['title'], d.get('tag'))
    y = TOP
    if d.get('lead'):
        text(sl, d['lead'], MARGIN, y, W - 2 * MARGIN, Inches(0.9), size=d.get('size', 22))
        y += Inches(d.get('lead_h', 0.85))
    full = W - 2 * MARGIN
    cw = Inches(d['width']) if d.get('width') else \
        max(Inches(6), min(full, code_width(d['code'], d.get('code_size', 18))))
    cx = int((W - cw) / 2)
    h = code_block(sl, d['code'], cx, y, cw, size=d.get('code_size', 18))
    if d.get('callout'):
        cy = max(y + h + Inches(0.3), H - Inches(1.5))
        callout(sl, d['callout'], MARGIN + Inches(0.5), min(cy, H - Inches(1.3)),
                W - 2 * MARGIN - Inches(1.0), Inches(0.95), tone=d.get('tone', 'orange'),
                size=d.get('callout_size', 22))
    notes(sl, d.get('notes'))


def s_table(prs, d, deck):
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    paper(sl)
    title_bar(sl, d['title'], d.get('tag'))
    y = TOP
    if d.get('lead'):
        text(sl, d['lead'], MARGIN, y, W - 2 * MARGIN, Inches(0.9), size=22)
        y += Inches(0.85)
    headers, rows = d['headers'], d['rows']
    tw = W - 2 * MARGIN
    row_h = Inches(0.62)
    shape = sl.shapes.add_table(len(rows) + 1, len(headers), MARGIN, y, tw, row_h * (len(rows) + 1))
    tbl = shape.table
    widths = d.get('widths') or [1] * len(headers)
    for i, wt in enumerate(widths):
        tbl.columns[i].width = int(tw * wt / sum(widths))
    for c, h in enumerate(headers):
        cell = tbl.cell(0, c)
        cell.fill.solid()
        cell.fill.fore_color.rgb = TEAL_BG
        cell.text_frame.paragraphs[0].text = ''
        _runs(cell.text_frame.paragraphs[0], h, 22, TEAL, TITLE_FONT, True)
    for r, row in enumerate(rows, 1):
        for c, v in enumerate(row):
            cell = tbl.cell(r, c)
            cell.fill.solid()
            cell.fill.fore_color.rgb = PAPER
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.text_frame.paragraphs[0].text = ''
            _runs(cell.text_frame.paragraphs[0], str(v), d.get('size', 20))
    if d.get('callout'):
        callout(sl, d['callout'], MARGIN + Inches(0.5), H - Inches(1.45),
                W - 2 * MARGIN - Inches(1.0), Inches(0.95), tone=d.get('tone', 'orange'))
    notes(sl, d.get('notes'))


def _check_slide(prs, d, deck, reveal):
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    paper(sl)
    title_bar(sl, 'Check your understanding' if not reveal else 'Answer',
              d.get('tag'))
    text(sl, d['question'], MARGIN, TOP, W - 2 * MARGIN, Inches(1.2), size=28)
    y = TOP + Inches(1.35)
    letters = 'ABCDEF'
    oh = Inches(0.78)
    for i, opt in enumerate(d['options']):
        right = reveal and i == d['answer']
        line, fill = (GREEN, GREEN_BG) if right else (BORDER, PAPER)
        _shape(sl, MSO_SHAPE.ROUNDED_RECTANGLE, MARGIN + Inches(0.4), y,
               W - 2 * MARGIN - Inches(0.8), oh - Inches(0.12), fill=fill, line=line,
               weight=3 if right else 1.5)
        n = len(re.sub(r'[`*]', '', opt))     # a long option gets smaller text, not overflow
        osize = 22 if n <= 76 else 19 if n <= 92 else 17
        text(sl, f'{letters[i]}.   {opt}', MARGIN + Inches(0.7), y, W - 2 * MARGIN - Inches(1.4),
             oh - Inches(0.12), size=osize, color=DARK if (right or not reveal) else MUTED,
             anchor=MSO_ANCHOR.MIDDLE)
        y += oh
    if reveal and d.get('explanation'):
        callout(sl, d['explanation'], MARGIN + Inches(0.4), max(y + Inches(0.1), H - Inches(1.5)),
                W - 2 * MARGIN - Inches(0.8), Inches(1.1), tone='green', size=20, tilt=0,
                align=PP_ALIGN.LEFT)
    if not reveal:
        notes(sl, d.get('notes') or f"Answer: {letters[d['answer']]}. {d.get('explanation', '')}")
    else:
        notes(sl, d.get('notes'))


def s_check(prs, d, deck):
    """A knowledge check: the question, then the same slide with the answer."""
    _check_slide(prs, d, deck, reveal=False)
    _check_slide(prs, d, deck, reveal=True)


def s_steps(prs, d, deck):
    """An activity: numbered steps, each a sketch card."""
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    paper(sl)
    title_bar(sl, d['title'], d.get('tag') or 'Activity')
    y = TOP
    if d.get('lead'):
        text(sl, d['lead'], MARGIN, y, W - 2 * MARGIN, Inches(0.8), size=22)
        y += Inches(0.75)
    steps = d['steps']
    gap = Inches(0.18)
    bottom = H - Inches(0.35) - (Inches(1.15) if d.get('callout') else 0)
    sh = int((bottom - y - gap * (len(steps) - 1)) / len(steps))
    for i, st in enumerate(steps, 1):
        _shape(sl, MSO_SHAPE.ROUNDED_RECTANGLE, MARGIN, y, W - 2 * MARGIN, sh,
               fill=PAPER, line=TEAL, tilt=(-0.3 if i % 2 else 0.3))
        _shape(sl, MSO_SHAPE.OVAL, MARGIN + Inches(0.2), y + int(sh / 2) - Inches(0.3),
               Inches(0.6), Inches(0.6), fill=ORANGE)
        text(sl, str(i), MARGIN + Inches(0.2), y + int(sh / 2) - Inches(0.3), Inches(0.6),
             Inches(0.6), size=24, font=TITLE_FONT, bold=True, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE, color=RGBColor(0xFF, 0xFF, 0xFF))
        text(sl, st, MARGIN + Inches(1.05), y + Inches(0.05), W - 2 * MARGIN - Inches(1.3),
             sh - Inches(0.1), size=d.get('size', 21), anchor=MSO_ANCHOR.MIDDLE)
        y += sh + gap
    if d.get('callout'):
        callout(sl, d['callout'], MARGIN + Inches(0.5), H - Inches(1.35),
                W - 2 * MARGIN - Inches(1.0), Inches(0.9), tone=d.get('tone', 'orange'))
    notes(sl, d.get('notes'))


def s_cards(prs, d, deck):
    """Real-world connections: two to four cards side by side."""
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    paper(sl)
    title_bar(sl, d.get('title', 'Real-world connections'), d.get('tag'))
    cards = d['cards']
    gap = Inches(0.35)
    cw = int((W - 2 * MARGIN - gap * (len(cards) - 1)) / len(cards))
    ch = Inches(d.get('height', 3.6))
    top = int(TOP + (H - TOP - Inches(0.4) - ch) / 2)
    tones = ['teal', 'orange', 'green', 'teal']
    for i, (tag, head, body) in enumerate(cards):
        x = MARGIN + (cw + gap) * i
        line, fill = TONES[tones[i]]
        _shape(sl, MSO_SHAPE.ROUNDED_RECTANGLE, x, top, cw, ch, fill=fill, line=line,
               tilt=(-0.8, 0.6, -0.4, 0.7)[i])
        text(sl, tag.upper(), x + Inches(0.3), top + Inches(0.25), cw - Inches(0.6),
             Inches(0.4), size=16, color=MUTED)
        room = (cw - Inches(0.7)) / 12700
        hsize = max(22, min(32, int(room / (len(head) * 0.42))))
        text(sl, head, x + Inches(0.3), top + Inches(0.6), cw - Inches(0.6), Inches(0.8),
             size=hsize, font=TITLE_FONT, bold=True)
        text(sl, body, x + Inches(0.3), top + Inches(1.5), cw - Inches(0.6), ch - Inches(1.8),
             size=20)
    notes(sl, d.get('notes'))


def s_wrapup(prs, d, deck):
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    paper(sl)
    title_bar(sl, d.get('title', 'Wrap-up'), d.get('tag'))
    y = TOP + Inches(0.1)
    qs = d['questions']
    qh = int((H - Inches(1.9) - y) / max(len(qs), 1))
    qh = min(qh, Inches(1.3))
    for i, q in enumerate(qs):
        callout(sl, q, MARGIN + Inches(0.3), y, W - 2 * MARGIN - Inches(0.6), qh - Inches(0.2),
                tone='teal', size=24, tilt=(-0.4 if i % 2 else 0.4), align=PP_ALIGN.LEFT)
        y += qh
    if d.get('next'):
        text(sl, 'Next: ' + d['next'], MARGIN, H - Inches(1.2), W - 2 * MARGIN, Inches(0.7),
             size=24, color=TEAL, font=TITLE_FONT, bold=True, align=PP_ALIGN.CENTER)
    notes(sl, d.get('notes'))


KINDS = {
    'title': s_title, 'bullets': s_bullets, 'figure': s_figure, 'code': s_code,
    'table': s_table, 'check': s_check, 'steps': s_steps, 'cards': s_cards,
    'wrapup': s_wrapup, 'frames': s_frames,
}


def build(deck, out_path):
    prs = Presentation()
    prs.slide_width, prs.slide_height = W, H
    core = prs.core_properties
    core.title = f"Lesson {deck['module']}-{deck['lesson']} · {deck['title']}"
    core.author = 'XRP Python Curriculum'
    core.subject = 'XRP Python Curriculum slides, GNU GPL v3.0'
    for d in deck['slides']:
        KINDS[d['kind']](prs, d, deck)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    prs.save(out_path)
    return len(prs.slides)
