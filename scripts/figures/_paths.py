"""Shared paths for the figure generators (see README.md).

OUTDIR   where every generator writes its SVG (gitignored; copy the result
         into static/img/<lesson>/ yourself -- README.md says where each goes).
ROBOT_SRC the SVG whose <defs> hold the top-down XRP drawing (#pcXRP) that
         almost every figure reuses. It is the L2-9 turn animation.
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
OUTDIR = os.path.join(HERE, 'out') + os.sep
ROBOT_SRC = os.path.join(REPO, 'static', 'img', 'lesson-m2-09', 'park-turn-left-then-right.svg')
os.makedirs(OUTDIR, exist_ok=True)
