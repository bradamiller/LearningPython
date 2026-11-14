#!/usr/bin/env python3
"""Build the robot.py templates and the complete sample for the Module 4 test
(top-down trial), docs/test-module-04.

    python3 scripts/build_test_module_templates.py
    python3 scripts/build_test_module_templates.py --samples DIR   # + plain .py
    python3 scripts/build_test_module_templates.py --verify --xrplib DIR --scratch DIR

Run scripts/build_templates.py first: the trial forks from the end of Module 3,
so its base files are that script's robot-end-of-module-3.py (template) and,
for the complete sample, the same file with every body filled in (it writes it
with --samples; this script calls it for you).

Writes:
  static/templates/test-module-04/<track>/robot-after-4-<L>.py
      every skeleton through lesson 4-L pasted in, nothing written yet;
  docs/teacher-guide/sample-programs/_module-4-test-files.mdx
      the COMPLETE file at the end of the trial, both tracks, every line
      inside a <TeacherNote> (answers).
build_templates.py lists the template files on docs/templates.mdx.

How it reads the lessons. A lesson's code fences are split into top-level
units (a def, a class, a NAME = setting, or a `# =====` / `# ---` banner with
the comment lines under it). A template takes the lesson's student skeleton
fences; the sample takes its "Solution (teacher copy)" fences. Each unit
replaces the unit of the same name, or goes in after the unit before it in the
same fence, or at the lesson's anchor. The few edits a lesson states in prose
(4-3's two new comments, 4-4's heading letter, 4-6's two-line swap) are EDITS
below, each with text that must be found in the lesson, so a changed lesson
fails loudly instead of building a wrong file.

The class track is the same file grown on the class-track Module 3 base; its
only difference in these lessons is 4-6's swap, which calls tracker.
turn_clockwise() and tracker.track_to_intersection(). The optional Manhattan
and Navigator class extensions in 4-3 and 4-6 are not built into it.
"""

import argparse
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, 'docs', 'test-module-04')
OUT = os.path.join(ROOT, 'static', 'templates', 'test-module-04')
PARTIAL = os.path.join(ROOT, 'docs', 'teacher-guide', 'sample-programs',
                       '_module-4-test-files.mdx')
TRACKS = ('function', 'class')
LESSONS = [1, 2, 3, 4, 5, 6]


def fail(msg):
    sys.exit('build_test_module_templates: ' + msg)


def lesson_file(n):
    for f in sorted(os.listdir(DOCS)):
        if f.startswith('lesson-%02d-' % n) and f.endswith('.mdx'):
            return os.path.join(DOCS, f)
    fail('no lesson file for 4-%d' % n)


def lesson_title(n):
    m = re.search(r'^title: "Lesson 4-\d+ · (.*)"', open(lesson_file(n)).read(), re.M)
    return m.group(1)


def fences(n):
    """[(visibility, text)] for every ```python fence in lesson 4-n.
    visibility: student, reveal, teacher (a "Solution (teacher copy)" note),
    note (any other teacher note), ext (inside an optional extension)."""
    out, stack, buf, inside = [], [], None, False
    for line in open(lesson_file(n)).read().split('\n'):
        s = line.strip()
        if inside:
            if s == '```':
                vis = 'ext' if 'ext' in stack else (stack[-1] if stack else 'student')
                out.append((vis, '\n'.join(buf) + '\n'))
                inside = False
            else:
                buf.append(line)
            continue
        if s.startswith('```python'):
            inside, buf = True, []
        elif s.startswith('<OptionalExtension'):
            stack.append('ext')
        elif s.startswith('<Reveal'):
            stack.append('reveal')
        elif s.startswith('<TeacherNote'):
            stack.append('teacher' if 'Solution (teacher copy)' in s else 'note')
        elif s in ('</OptionalExtension>', '</Reveal>', '</TeacherNote>'):
            stack.pop()
    return out


def units(text):
    """Top-level units of a fence, [(key, text)], stopping at the RUN block."""
    out, cur = [], None
    lines = text.rstrip('\n').split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('# ===== RUN'):
            break
        key = None
        if line.startswith('def ') or line.startswith('class '):
            key = re.match(r'(?:def|class) (\w+)', line).group(1)
        elif re.match(r'[A-Z_][A-Z0-9_]* = ', line):
            key = line.split(' =')[0]
        elif line.startswith('# =====') or line.startswith('# ---'):
            key = 'banner:' + line.strip('# =-').strip()
        if key:
            if cur:
                out.append(cur)
            cur = [key, [line]]
        elif cur is not None and (line.startswith((' ', '\t', '#')) or (
                line == '' and i + 1 < len(lines) and lines[i + 1].startswith((' ', '\t')))):
            cur[1].append(line)
        elif line.strip() == '':
            if cur:
                out.append(cur)
                cur = None
        else:
            fail('unexpected top-level line: %r' % line)
        i += 1
    if cur:
        out.append(cur)
    return [(k, '\n'.join(l).rstrip('\n') + '\n') for k, l in out]


def skeleton_fences(n, must):
    """The student-visible fences of lesson 4-n that hold every name in `must`."""
    hits = [t for v, t in fences(n) if v == 'student' and all(m in t for m in must)]
    if not hits:
        fail('4-%d: no student fence with %r' % (n, must))
    return hits[0]


def teacher_fences(n):
    hits = [t for v, t in fences(n) if v == 'teacher']
    if not hits:
        fail('4-%d: no teacher copy' % n)
    return hits


# ---------------------------------------------------------------- the file model

class File:
    def __init__(self, base):
        head, run = base.split('# ===== RUN =====', 1)
        self.head = head.rstrip('\n') + '\n'
        self.run = '# ===== RUN =====' + run
        self.items = []          # [(key, text)]

    def index(self, key):
        for i, (k, _) in enumerate(self.items):
            if k == key:
                return i
        return None

    def upsert(self, fence_units, anchor=None):
        prev = None
        for key, text in fence_units:
            i = self.index(key)
            if i is not None:
                self.items[i] = (key, text)
            elif prev is not None:
                self.items.insert(self.index(prev) + 1, (key, text))
            elif anchor:
                where, name = anchor
                j = self.index(name)
                if j is None:
                    fail('anchor %s not in file' % name)
                self.items.insert(j if where == 'before' else j + 1, (key, text))
            else:
                self.items.append((key, text))
            prev = key

    def edit(self, key, old, new):
        i = self.index(key)
        if i is None or old not in self.items[i][1]:
            fail('edit %s: %r not found' % (key, old))
        self.items[i] = (key, self.items[i][1].replace(old, new))

    def text(self, header):
        body = '\n'.join(t for _, t in self.items)
        return header + '\n' + self.head + '\n' + body + '\n' + self.run


def evidence(n, text):
    if text not in open(lesson_file(n)).read():
        fail('4-%d no longer says %r: check the edit that relies on it' % (n, text))


# ---------------------------------------------------------------- the lessons

def apply_template(f, n, track):
    if n == 1:
        f.upsert(units(skeleton_fences(1, ['# ===== MANHATTAN PLANNER', 'def test_delivery'])))
    elif n == 2:
        f.upsert(units(skeleton_fences(2, ['def compute_manhattan_path', 'def test_planner'])))
    elif n == 3:
        west = '    # West: copy east, flip < to > and + to -'
        south = '    # South: copy north, flip < to > and + to -'
        evidence(3, west)
        evidence(3, south)
        f.edit('compute_manhattan_path', '    # North: copy east',
               west + '\n\n    # North: copy east')
        f.edit('compute_manhattan_path', '\n    return path', '\n' + south + '\n\n    return path')
        f.upsert(units(skeleton_fences(3, ['def run_test', 'def test_planner'])),
                 anchor=('after', 'compute_manhattan_path'))
    elif n == 4:
        f.upsert(units(skeleton_fences(4, ['HEADING_NAMES = ', 'def turn_to'])),
                 anchor=('before', 'drive_path'))
        f.upsert(units(skeleton_fences(4, ['def drive_path', '# 3. turn'])))
        evidence(4, 'HEADING_NAMES[robot_heading])')
        f.edit('test_delivery', '"heading:", robot_heading', '"heading:", HEADING_NAMES[robot_heading]')
    elif n == 5:
        f.upsert(units(skeleton_fences(5, ['def fake_turn_clockwise', 'def turn_to'])),
                 anchor=('after', 'fake_track_to_intersection'))
    elif n == 6:
        evidence(6, 'change `fake_turn_clockwise()` to `turn_clockwise()`')
        evidence(6, 'change `fake_track_to_intersection()` to `track_to_intersection()`')
        pre = 'tracker.' if track == 'class' else ''
        f.edit('turn_to', 'fake_turn_clockwise()', pre + 'turn_clockwise()')
        f.edit('drive_path', 'fake_track_to_intersection()', pre + 'track_to_intersection()')


def apply_sample(f, n, track):
    anchors = {4: ('before', 'drive_path'), 5: ('after', 'fake_track_to_intersection')}
    for t in teacher_fences(n):
        u = units(t)
        if n == 6 and track == 'class':
            u = [(k, x.replace('    turn_clockwise()', '    tracker.turn_clockwise()')
                       .replace('    track_to_intersection()', '    tracker.track_to_intersection()'))
                 for k, x in u]
        f.upsert(u, anchor=anchors.get(n))


# ---------------------------------------------------------------- build

def header(track, lesson, complete):
    if complete:
        return ('# robot.py, COMPLETE, as the teacher copies leave it after\n'
                '# Lesson 4-6 of the Module 4 test (%s track). Answers: not for students.\n' % track)
    return ('# robot.py after Lesson 4-%d of the Module 4 test (%s track):\n'
            '# every skeleton through Lesson 4-%d pasted in, nothing written yet.\n'
            % (lesson, track, lesson))


def strip_header(text):
    lines = text.split('\n')
    while lines and lines[0].startswith('#'):
        lines.pop(0)
    return '\n'.join(lines).lstrip('\n')


def build(samples_dir):
    m3 = os.path.join(samples_dir, '_m3')
    subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'build_templates.py'),
                    '--samples', m3], check=True, capture_output=True)
    rendered = {}
    for track in TRACKS:
        tbase = open(os.path.join(ROOT, 'static', 'templates', track,
                                  'robot-end-of-module-3.py')).read()
        sbase = open(os.path.join(m3, track, 'robot-end-of-module-3.py')).read()
        tf, sf = File(strip_header(tbase)), File(strip_header(sbase))
        for n in LESSONS:
            apply_template(tf, n, track)
            rendered[(track, n)] = tf.text(header(track, n, False))
            apply_sample(sf, n, track)
        rendered[(track, 'sample')] = sf.text(header(track, None, True))
    shutil.rmtree(OUT, ignore_errors=True)
    for (track, n), text in rendered.items():
        if n == 'sample':
            continue
        path = os.path.join(OUT, track, 'robot-after-4-%d.py' % n)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, 'w').write(text)
    open(PARTIAL, 'w').write(partial(rendered))
    for track in TRACKS:
        os.makedirs(os.path.join(samples_dir, track), exist_ok=True)
        open(os.path.join(samples_dir, track, 'robot-end-of-module-4-test.py'), 'w').write(
            rendered[(track, 'sample')])
    return rendered


def partial(rendered):
    out = ['{/* GENERATED by scripts/build_test_module_templates.py from the Module 4',
           '    test lessons: the complete robot.py at the end of the trial, both tracks.',
           '    Answers, so everything is inside a TeacherNote. Do not edit this file:',
           '    change the lessons (or the script) and re-run it. */}', '']
    for track in TRACKS:
        out += ['## %s track' % track.capitalize(), '',
                '<TeacherNote title="Module 4 test: complete robot.py (%s track)">' % track, '',
                '```python title="robot.py · %s track · end of the Module 4 test"' % track,
                rendered[(track, 'sample')].rstrip('\n'), '```', '', '</TeacherNote>', '']
    return '\n'.join(out)


# ---------------------------------------------------------------- verify

def run(scratch, name, text, xrplib, calls):
    d = os.path.join(scratch, name)
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d)
    shutil.copytree(xrplib, os.path.join(d, 'XRPLib'))
    open(os.path.join(d, 'robot.py'), 'w').write(text)
    open(os.path.join(d, 'runner.py'), 'w').write(
        'import runpy, sys\nns = runpy.run_path("robot.py", run_name="__main__")\n'
        'for n in sys.argv[1:]:\n    print("### calling", n)\n    ns[n]()\n')
    p = subprocess.run([sys.executable, 'runner.py'] + calls, cwd=d, capture_output=True,
                       text=True, timeout=60)
    return p.returncode, p.stdout, p.stderr


def verify(rendered, xrplib, scratch):
    problems = []
    for (track, n), text in sorted(rendered.items(), key=str):
        rc, out, err = run(scratch, 'm4t_%s_%s' % (track, n), text, xrplib, [])
        print('%-8s %-6s loads: %s' % (track, n, 'ok' if rc == 0 else 'FAILED'))
        if rc:
            problems.append(err)
    for track in TRACKS:
        text = rendered[(track, 'sample')]
        rc, out, err = run(scratch, 'm4t_%s_run' % track, text, xrplib,
                           ['test_planner', 'test_headings', 'test_delivery'])
        passes = out.count(' - PASS')
        last = [l for l in out.split('\n') if l.startswith('new position:')][-1:]
        print('%-8s sample: %d PASS, %d FAIL, ends %s' % (
            track, passes, out.count(' - FAIL'), last))
        if rc or passes != 5 or 'FAIL' in out or last != ['new position: (0, 0) heading: S']:
            problems.append('%s sample run wrong:\n%s\n%s' % (track, out[-800:], err[-800:]))
        moves = [l for l in out.split('\n')
                 if l.startswith(('turning clockwise', 'tracking to intersection', 'moving:'))]
        print('%-8s sample: %d moving/turning/tracking lines' % (track, len(moves)))
    if problems:
        fail('\n\n'.join(problems))
    print('all checks passed')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--samples', metavar='DIR')
    ap.add_argument('--verify', action='store_true')
    ap.add_argument('--xrplib', metavar='DIR')
    ap.add_argument('--scratch', metavar='DIR')
    a = ap.parse_args()
    import tempfile
    samples = a.samples or tempfile.mkdtemp()
    rendered = build(samples)
    print('wrote %d templates and %s' % (len(rendered) - 2, os.path.relpath(PARTIAL, ROOT)))
    if a.verify:
        if not (a.xrplib and a.scratch):
            ap.error('--verify needs --xrplib and --scratch')
        verify(rendered, a.xrplib, a.scratch)


if __name__ == '__main__':
    main()
