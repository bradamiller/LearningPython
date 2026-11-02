"""Run: python3 scripts/slides/decks/m1/fig/make_l06_cases.py <repo root>

Compose Lesson 1-6's four motor cases into 2x2 sheets for the slides:
one at the start (predict) and one mid-drive (drive it)."""
import io, os, sys
REPO = sys.argv[1]
sys.path.insert(0, os.path.join(REPO, 'scripts/slides'))
import sketchdeck, cairosvg
from PIL import Image, ImageDraw, ImageFont
OUT = os.path.join(REPO, 'scripts/slides/decks/m1/fig')
cases = [('straight', 0.6, 'Case 1', 'Left: forward   ·   Right: forward, same speed'),
         ('curve', 0.6, 'Case 2', 'Left: forward, fast   ·   Right: forward, slow'),
         ('pivot', 0.5, 'Case 3', 'Left: stopped   ·   Right: forward'),
         ('spin', 0.5, 'Case 4', 'Left: backward   ·   Right: forward')]
big = ImageFont.truetype(os.path.expanduser('~/.fonts/Caveat-Bold.ttf'), 70)
body = ImageFont.truetype(os.path.expanduser('~/.fonts/PatrickHand-Regular.ttf'), 50)
W = 1400
for name, mode in (('l06-cases-predict.png', 'predict'), ('l06-cases-drive.png', 'drive')):
    panels = []
    for case, at, label, sides in cases:
        src = os.path.join(REPO, f'static/img/lesson-06/motors-{case}-drive.svg')
        data = sketchdeck.freeze_svg(open(src, 'rb').read(), 0.0 if mode == 'predict' else at)
        png = cairosvg.svg2png(bytestring=data, output_width=W)
        im = Image.open(io.BytesIO(png)).convert('RGBA')
        x0, x1 = int(0.045 * im.width), int(0.955 * im.width)
        y0, y1 = int(0.205 * im.height), int(0.965 * im.height)
        im = im.crop((x0, y0, x1, y1))
        # paint the panel's own background over the cropped edge, as a rounded card
        card = Image.new('RGBA', im.size, (0, 0, 0, 0))
        ImageDraw.Draw(card).rounded_rectangle((0, 0, im.width - 1, im.height - 1), 24,
                                               fill=(243, 244, 246, 255),
                                               outline=(206, 212, 218, 255), width=3)
        mask = Image.new('L', im.size, 0)
        ImageDraw.Draw(mask).rounded_rectangle((3, 3, im.width - 4, im.height - 4), 22, fill=255)
        card.paste(im, (0, 0), mask)
        head = 96
        p = Image.new('RGBA', (card.width, card.height + head), (0, 0, 0, 0))
        d = ImageDraw.Draw(p)
        d.text((8, head - 18), label, font=big, fill=(91, 143, 168, 255), anchor='ls')
        lw = d.textlength(label, font=big)
        d.text((8 + lw + 40, head - 20), sides, font=body, fill=(45, 52, 54, 255), anchor='ls')
        p.alpha_composite(card, (0, head))
        panels.append(p)
    pw, ph = panels[0].size
    gap = 60
    sheet = Image.new('RGBA', (pw * 2 + gap, ph * 2 + gap), (0, 0, 0, 0))
    for i, p in enumerate(panels):
        sheet.alpha_composite(p, ((i % 2) * (pw + gap), (i // 2) * (ph + gap)))
    sheet.save(os.path.join(OUT, name))
    print(name, sheet.size, round(sheet.width / sheet.height, 2))
