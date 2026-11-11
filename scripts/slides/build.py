#!/usr/bin/env python3
"""Build the lesson slide decks.

    python3 scripts/slides/build.py            # every deck
    python3 scripts/slides/build.py 2-5 2-6    # just these lessons

Each deck is scripts/slides/decks/m<module>/l<lesson>.py defining DECK (see
sketchdeck.py). Output goes to static/slides/<module folder>/module-<N>-<lesson
page>.pptx, for example
static/slides/module-04-manhattan/module-4-lesson-03-the-manhattan-algorithm.pptx,
and src/data/slides.json maps each lesson's doc id to its deck so the lesson
page can link it.
"""

import glob
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sketchdeck  # noqa: E402

REPO = sketchdeck.REPO
MANIFEST = os.path.join(REPO, 'src', 'data', 'slides.json')


def load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.DECK


def main(only):
    decks = sorted(glob.glob(os.path.join(HERE, 'decks', 'm*', 'l*.py')))
    manifest = {}
    for path in decks:
        deck = load(path)
        key = f"{deck['module']}-{deck['lesson']}"
        doc = deck['doc']
        if not os.path.exists(os.path.join(REPO, 'docs', doc + '.mdx')):
            sys.exit(f'{path}: no lesson page docs/{doc}.mdx')
        folder, page = os.path.split(doc)
        # the module number goes in the file name, so a downloaded deck says where it belongs
        url = f"/slides/{folder}/module-{deck['module']}-{page}.pptx"
        manifest[doc] = url
        if only and key not in only:
            continue
        n = sketchdeck.build(deck, os.path.join(REPO, 'static', url.lstrip('/')))
        print(f'{key:>5}  {n:3d} slides  static{url}')
    os.makedirs(os.path.dirname(MANIFEST), exist_ok=True)
    with open(MANIFEST, 'w') as f:
        json.dump(manifest, f, indent=2, sort_keys=True)
        f.write('\n')


if __name__ == '__main__':
    main(set(sys.argv[1:]))
