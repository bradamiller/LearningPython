# Lesson slide decks

Sketch-style PowerPoint decks, one per lesson, built from Python.

```
python3 scripts/slides/build.py          # every deck
python3 scripts/slides/build.py 2-5      # one lesson
```

- `sketchdeck.py` is the look (palette, fonts, slide kinds). Its docstring and
  each `s_*` function list the keys a slide takes.
- `decks/m<module>/l<lesson>.py` holds one deck: a `DECK` dict whose `slides`
  list follows the lesson page section by section. The lesson page is the
  source of truth; a deck never shows a solution, and teacher notes go in each
  slide's `notes`.
- Figures come from `static/img/`. SVGs are rendered with cairosvg into
  `.figcache/` (ignored by git). An animated SVG is frozen at `frame` (0 to 1
  of one run, default 0.5); `crop` keeps part of the figure.
- Output: `static/slides/<module folder>/module-<N>-<lesson page>.pptx`, and `src/data/slides.json`, which the
  lesson header reads to show its **Slides (PowerPoint)** link.

Fonts: Caveat (titles), Patrick Hand (body) and Fira Mono (code), all on Google
Fonts. To preview the decks locally (for example with LibreOffice), install
them first. Teachers get the same note on the "How this course works" page.

Licensed with the rest of the course under the GNU GPL v3.0.
