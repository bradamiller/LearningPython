"""Lesson 4-6: the robot's pose is its position and its heading, together.

The robot at (1, 1) facing East; beside it the pose as Python holds it,
((1, 1), 1), with each half labeled.

Output: out/pose.svg -> static/img/lesson-m4-06/pose.svg
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR
from common import *

BLUE, RED = "#22527B", "#D1182C"
g = G(70, 50, sp=60, pad=30)
b = g.base(axes=True, north=True)

rx, ry = g.p(1, 1)
b.append(f'<use href="#pcXRP" transform="translate({rx} {ry}) rotate(90) scale(0.36)"/>')
b.append(f'<line x1="{rx+30}" y1="{ry}" x2="{rx+56}" y2="{ry}" stroke="{RED}" stroke-width="3" marker-end="url(#aR)"/>')

X = 330
b.append(f'<text class="h" x="{X}" y="70">The robot\'s pose</text>')
b.append(f'<text class="n" x="{X}" y="92">Where it is, and which way it faces.</text>')
# the tuple, big, one character per fixed slot so the labels line up in any font
MONO = "font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 26px; font-weight: 700"
ADV = 15
chars = "((1, 1), 1)"
for k, ch in enumerate(chars):
    color = BLUE if 1 <= k <= 6 else RED if k == 9 else "#142D50"
    if ch != " ":
        b.append(f'<text x="{X + k*ADV + ADV/2}" y="150" text-anchor="middle" style="{MONO}; fill: {color}">{ch}</text>')
pos_l, pos_r = X + 1*ADV + 2, X + 7*ADV - 2
pos_mid = (pos_l + pos_r) / 2
head_mid = X + 9*ADV + ADV/2
b.append(f'<line x1="{pos_l}" y1="160" x2="{pos_r}" y2="160" stroke="{BLUE}" stroke-width="2.4"/>')
b.append(f'<line x1="{head_mid-8}" y1="160" x2="{head_mid+8}" y2="160" stroke="{RED}" stroke-width="2.4"/>')
b.append(f'<line x1="{pos_mid}" y1="160" x2="{pos_mid}" y2="184" stroke="{BLUE}" stroke-width="1.6"/>')
b.append(f'<line x1="{head_mid}" y1="160" x2="{head_mid}" y2="212" stroke="{RED}" stroke-width="1.6"/>')
b.append(f'<text class="nb" x="{pos_mid}" y="200" text-anchor="middle" style="fill:{BLUE}">position</text>')
b.append(f'<text class="nb" x="{head_mid}" y="228" text-anchor="middle" style="fill:{RED}">heading: 1 = East</text>')
b.append(f'<text class="m" x="{X}" y="278">position, heading = drive_path(...)</text>')
b.append(f'<text class="sm" x="{X}" y="296">drive_path hands back the pose.</text>')

open(OUTDIR + 'pose.svg', 'w').write(svg(
    'The robot\'s pose: its position and its heading',
    'A 4 by 4 grid with (0, 0) at the bottom-left. The robot sits at (1, 1) facing East, '
    'shown by a red arrow. Beside it: the robot\'s pose, where it is and which way it '
    'faces, written ((1, 1), 1). The (1, 1) is labeled position; the final 1 is labeled '
    'heading, 1 = East. Below: position, heading = drive_path(...), drive_path hands back the pose.',
    b, W=640, H=320))

# Module 4 test (top-down trial), Lesson 4-1: the same figure with the trial's
# variable names, robot_position and robot_heading. -> static/img/lesson-m4t-01/pose-robot.svg
robot = open(OUTDIR + 'pose.svg').read()
old_code = f'<text class="m" x="{X}" y="278">position, heading = drive_path(...)</text>'
old_note = f'<text class="sm" x="{X}" y="296">drive_path hands back the pose.</text>'
assert old_code in robot and old_note in robot
robot = robot.replace(old_code,
    f'<text class="m" x="{X}" y="266">robot_position, robot_heading =</text>'
    f'<text class="m" x="{X + 24}" y="284">drive_path(...)</text>')
robot = robot.replace(old_note, f'<text class="sm" x="{X}" y="304">drive_path hands back the pose.</text>')
robot = robot.replace('Below: position, heading = drive_path(...)', 'Below: robot_position, robot_heading = drive_path(...)')
open(OUTDIR + 'pose-robot.svg', 'w').write(robot)
