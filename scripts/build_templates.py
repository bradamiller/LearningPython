#!/usr/bin/env python3
"""Build the robot.py templates (and the complete samples) from the
lessons.

    python3 scripts/build_templates.py                 # templates + page
    python3 scripts/build_templates.py --samples DIR   # + complete files
    python3 scripts/build_templates.py --verify --xrplib DIR --scratch DIR

Students keep ONE file, robot.py, from Lesson 2-1 to the end of
the course (CLAUDE.md section 15c). Every lesson hands out a
skeleton to paste above the `# ===== RUN =====` block. This script
reads the lesson .mdx files and writes, for every lesson that
changes the file and for both tracks:

  static/templates/<track>/robot-after-<L>.py
      the file as a student who pasted every skeleton through
      lesson L but wrote NOTHING yet would have it (no answers);
  static/templates/<track>/robot-end-of-module-<N>.py
      a byte-identical copy of the module's last lesson file;
  docs/templates.mdx
      the download page, with one table per module;
  <samples>/<track>/robot-end-of-module-<N>.py   (--samples only)
      the COMPLETE file with every body filled in from the Reveal
      and teacher-copy fences. These are answers: never put them
      in the site.

Design: the CONTENT comes from the lessons, the STRUCTURE from the
recipe below. Nothing in a template is typed here except the two
header lines and, on the class track, the few test bodies that the
lessons describe only in prose (CLASS_OVERRIDES, each one cited).

THE RECIPE FORMAT
-----------------
RECIPE is an ordered list of (lesson, [op, op, ...]). Lessons are
"M-L" strings in course order. Every op has `tracks`, a tuple
drawn from ("function", "class"); the default is both. The class
track applies the same ops as the function track plus its own,
and class ops read the lesson's <OptionalExtension> fences
(ext=True) unless told otherwise. Ops:

  Start(lesson)
      the start block: imports, the objects and the RUN block, from
      the lesson's fence that contains `# ===== RUN =====`.
  AddImport(lesson, prefix, after_prefix=None)
  AddObject(lesson, name)
      one more import / object line, pulled from the lesson.
  Banner(key, lesson, match, ext=False, after=/before=)
      a `# =====` section banner or `# ---` sub-banner plus the
      comment lines under it. `match` is text found in the banner
      line; `key` is how later ops refer to it ("banner:KEY").
  Setting(name, lesson, ext=False, after=/before=)
      the `NAME = value` line from the lesson's skeleton fence.
  SetValue(name, lesson, value, evidence)
      an in-place edit the lesson states in prose (2-9 raises
      BASE_EFFORT). `evidence` is a regex that must match the
      lesson text, so a changed lesson fails loudly.
  Func(name, lesson, full=False, pick=0, replace=False, ext=None,
       after=/before=)
      a function. OUTLINE = the student-visible skeleton fence in
      that lesson that defines the name (the first outline-like
      one, or the `pick`-th match when full=True). BODY = the
      latest Reveal / "Solution (teacher copy)" fence in any lesson
      up to the file's lesson that defines it with a real body.
      full=True marks a function the lesson gives in full (see
      GIVEN_IN_FULL). replace=True rewrites an existing function
      in place (2-6 get_error).
  Rename(old, new, lesson)
      in-place rename: the new def line and docstring come from
      the lesson's fence defining `new`; the outline comments stay.
  Refresh(name, lesson, kind, ext=False, full=True)
      re-pull a given-in-full function from a later fence
      (6-3's run_all_tests, from the teacher copy).
  Invent(name, lesson, body=None, after=/before=)
      a test the lesson asks the student to name and write (not
      in templates; in samples, body from the teacher copy, or
      the given text when the lesson has none).
  Delete(name)  /  Delete("banner:KEY")
  Class(name, lesson, methods, after=/before=)
      a class skeleton from an extension: header and __init__ as
      given, the listed methods as outlines; bodies from the
      extension's Reveal.
  AddMethods(cls, lesson, names, kind, full=True)
      methods added to an existing class (5-5's no-ops).
  AddMethodText(cls, name, outline, body)
      a method the lesson describes only in prose (5-8).
  Object(name, lesson, after=)
      the `name = Class(...)` line under a class.

Positions: ops append at the end (above RUN) unless `after=` or
`before=` names an item ("get_right", "banner:LINE SENSOR").

CLASS_RULES are regex substitutions the class track applies to
function text from a given lesson on ("each call gets sensor. in
front"); scoped rules name the functions they apply to.
"""

import argparse
import ast
import copy
import glob
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
OUT = os.path.join(ROOT, "static", "templates")
PAGE = os.path.join(DOCS, "templates.mdx")

MODULE_DIRS = {
    2: "module-02-line-tracking",
    3: "module-03-grid-driving",
    4: "module-04-manhattan",
    5: "module-05-pathfinding",
    6: "module-06-dijkstra",
}
MODULE_NAMES = {
    2: "Module 2 · Line Tracking",
    3: "Module 3 · Grid Driving",
    4: "Module 4 · Manhattan Navigation",
    5: "Module 5 · Pathfinding Around Obstacles",
    6: "Module 6 · Dijkstra's Algorithm (optional)",
}
TRACKS = ("function", "class")
COMMENT_MAX = 62


class BuildError(Exception):
    pass


def fail(msg):
    raise BuildError(msg)


def lkey(lesson):
    m, l = lesson.split("-")
    return (int(m), int(l))


# ---------------------------------------------------------------
# Lesson files: fences and their Python chunks
# ---------------------------------------------------------------

def lesson_path(lesson):
    m, l = lkey(lesson)
    pat = os.path.join(DOCS, MODULE_DIRS[m], "lesson-%02d-*.mdx" % l)
    hits = glob.glob(pat)
    if len(hits) != 1:
        fail("lesson %s: expected one file for %s, found %r" % (lesson, pat, hits))
    return hits[0]


def lesson_title(lesson):
    text = open(lesson_path(lesson), encoding="utf-8").read()
    m = re.search(r'^title: "(.*)"', text, re.M)
    if not m:
        fail("lesson %s: no title" % lesson)
    title = m.group(1)
    return title.split(" · ", 1)[-1]


class Fence:
    def __init__(self, lesson, index, line, vis, ext, sbs, text):
        self.lesson = lesson
        self.index = index
        self.line = line
        self.vis = vis          # student | reveal | teacher | other
        self.ext = ext          # inside <OptionalExtension>
        self.sbs = sbs          # inside <SideBySide>
        self.text = text
        self.chunks = parse_chunks(text)

    def __repr__(self):
        return "<fence %s:%d %s%s%s>" % (
            self.lesson, self.line, self.vis,
            " ext" if self.ext else "", " sbs" if self.sbs else "")


_LESSON_CACHE = {}


def lesson_fences(lesson):
    if lesson in _LESSON_CACHE:
        return _LESSON_CACHE[lesson]
    lines = open(lesson_path(lesson), encoding="utf-8").read().split("\n")
    fences = []
    depth = {"reveal": 0, "teacher": 0, "ext": 0, "sbs": 0}
    teacher_solution = False
    in_fence = False
    buf = []
    indent = 0
    lang = ""
    start = 0
    for i, raw in enumerate(lines, 1):
        s = raw.lstrip()
        if in_fence:
            if s.startswith("```"):
                in_fence = False
                if lang == "python":
                    if depth["teacher"]:
                        vis = "teacher" if teacher_solution else "other"
                    elif depth["reveal"]:
                        vis = "reveal"
                    else:
                        vis = "student"
                    fences.append(Fence(lesson, len(fences), start, vis,
                                        depth["ext"] > 0, depth["sbs"] > 0,
                                        "\n".join(buf)))
            else:
                if raw[:indent].strip() == "":
                    buf.append(raw[indent:])
                else:
                    buf.append(s)
            continue
        if s.startswith("```"):
            in_fence = True
            indent = len(raw) - len(s)
            lang = s[3:].strip()
            buf = []
            start = i
            continue
        for tag, key in (("Reveal", "reveal"), ("TeacherNote", "teacher"),
                         ("OptionalExtension", "ext"), ("SideBySide", "sbs")):
            if re.search(r"<%s(\s|>)" % tag, s):
                depth[key] += 1
                if tag == "TeacherNote":
                    teacher_solution = 'title="Solution' in s
            if "</%s>" % tag in s:
                depth[key] -= 1
    if in_fence:
        fail("lesson %s: unterminated code fence from line %d" % (lesson, start))
    _LESSON_CACHE[lesson] = fences
    return fences


DEF_RE = re.compile(r"^def (\w+)\(")
METHOD_RE = re.compile(r"^    def (\w+)\(self")
CLASS_RE = re.compile(r"^class (\w+)\b")
SETTING_RE = re.compile(r"^([A-Z][A-Z0-9_]*) = ")
OBJECT_RE = re.compile(r"^([a-z_]\w*) = [A-Z]\w*(\.\w+)?\(")
IMPORT_RE = re.compile(r"^(import |from )")
BANNER_RE = re.compile(r"^# (=====|---) ")


class Chunk:
    def __init__(self, kind, name, lines):
        self.kind = kind    # banner|def|method|class|setting|object|import
        self.name = name
        self.lines = lines

    @property
    def text(self):
        return "\n".join(self.lines)


def parse_chunks(text):
    lines = text.rstrip("\n").split("\n")
    chunks = []
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if METHOD_RE.match(line):
            # a bare, indented method (a Reveal of "the methods")
            j = i + 1
            while j < n and (not lines[j].strip()
                             or lines[j].startswith("        ")
                             or (lines[j].startswith("    ")
                                 and lines[j].strip().startswith("#"))):
                j += 1
            body = [l[4:] if l.startswith("    ") else l for l in lines[i:j]]
            while body and not body[-1].strip():
                body.pop()
            chunks.append(Chunk("method", METHOD_RE.match(line).group(1), body))
            i = j
            continue
        if line.startswith((" ", "\t")):
            i += 1
            continue
        if BANNER_RE.match(line):
            j = i
            while j < n and lines[j].startswith("#"):
                j += 1
            chunks.append(Chunk("banner", line, lines[i:j]))
            i = j
            continue
        if line.startswith("#"):
            i += 1
            continue
        m = DEF_RE.match(line) or CLASS_RE.match(line)
        if m:
            j = i + 1
            while j < n and (not lines[j].strip() or lines[j].startswith((" ", "\t"))):
                j += 1
            body = lines[i:j]
            while body and not body[-1].strip():
                body.pop()
            kind = "class" if line.startswith("class") else "def"
            chunks.append(Chunk(kind, m.group(1), body))
            i = j
            continue
        if IMPORT_RE.match(line):
            chunks.append(Chunk("import", line.split("#")[0].strip(), [line.split("#")[0].rstrip()]))
            i += 1
            continue
        m = SETTING_RE.match(line)
        if m:
            chunks.append(Chunk("setting", m.group(1), [line]))
            i += 1
            continue
        m = OBJECT_RE.match(line)
        if m:
            chunks.append(Chunk("object", m.group(1), [line]))
            i += 1
            continue
        i += 1
    return chunks


def is_outline(lines):
    """True when a def's body is only a docstring, comments, pass."""
    try:
        tree = ast.parse("\n".join(lines))
    except SyntaxError:
        return False
    if len(tree.body) != 1 or not isinstance(tree.body[0], ast.FunctionDef):
        return False
    for st in tree.body[0].body:
        if isinstance(st, ast.Pass):
            continue
        if (isinstance(st, ast.Expr) and isinstance(st.value, ast.Constant)
                and isinstance(st.value.value, str)):
            continue
        return False
    return True


def split_def(lines):
    """-> (def line, docstring lines, the rest)."""
    head, rest = lines[0], lines[1:]
    doc = []
    if rest and rest[0].strip().startswith('"""'):
        doc.append(rest[0])
        if rest[0].strip().count('"""') < 2:
            k = 1
            while k < len(rest):
                doc.append(rest[k])
                if '"""' in rest[k]:
                    break
                k += 1
        rest = rest[len(doc):]
    return head, doc, rest


def parse_class(lines):
    """-> (header lines, [(method name, dedented lines)])."""
    header = []
    methods = []
    i = 0
    while i < len(lines) and not METHOD_RE.match(lines[i]):
        header.append(lines[i])
        i += 1
    while header and not header[-1].strip():
        header.pop()
    while i < len(lines):
        m = METHOD_RE.match(lines[i])
        if not m:
            i += 1
            continue
        j = i + 1
        while j < len(lines) and not METHOD_RE.match(lines[j]):
            j += 1
        body = [l[4:] if l.startswith("    ") else l for l in lines[i:j]]
        while body and not body[-1].strip():
            body.pop()
        methods.append((m.group(1), body))
        i = j
    return header, methods


# ---------------------------------------------------------------
# Fence lookups
# ---------------------------------------------------------------

ALL_LESSONS = []   # filled from RECIPE


def fences_for(lesson, vis, ext=None):
    out = []
    for f in lesson_fences(lesson):
        if f.sbs:
            continue
        if vis == "answer" and f.vis not in ("reveal", "teacher"):
            continue
        if vis != "answer" and f.vis != vis:
            continue
        if ext is not None and f.ext != ext:
            continue
        out.append(f)
    return out


def find_def_outline(name, lesson, ext, full, pick):
    hits = []
    for f in fences_for(lesson, "student", ext):
        for c in f.chunks:
            if c.kind == "def" and c.name == name:
                if full or is_outline(c.lines):
                    hits.append((f, c))
    if len(hits) <= pick:
        fail("lesson %s: no %s skeleton fence defines %s() (%s)" % (
            lesson, "extension" if ext else "student", name,
            "match %d of %d" % (pick + 1, len(hits))))
    return hits[pick]


def find_def_body(name, upto, track):
    """The latest answer fence (<= upto) that defines name in full."""
    best = None
    for lesson in ALL_LESSONS:
        if lkey(lesson) > lkey(upto):
            break
        ext = None if track == "class" else False
        for f in fences_for(lesson, "answer", ext):
            for c in f.chunks:
                if c.kind == "def" and c.name == name and not is_outline(c.lines):
                    best = (f, c)
    return best


def find_chunk(lesson, vis, ext, kind, name, pick=0):
    hits = []
    for f in fences_for(lesson, vis, ext):
        for c in f.chunks:
            if c.kind == kind and (name is None or c.name == name):
                hits.append((f, c))
    if len(hits) <= pick:
        fail("lesson %s: no %s fence has %s %s" % (lesson, vis, kind, name))
    return hits[pick]


def find_method_body(cls, mname, lesson, ext):
    best = None
    for f in fences_for(lesson, "answer", ext):
        for c in f.chunks:
            if c.kind == "method" and c.name == mname and not is_outline(c.lines):
                best = c.lines
            if c.kind == "class" and c.name == cls:
                for n, body in parse_class(c.lines)[1]:
                    if n == mname and not is_outline(body):
                        best = body
    return best


# ---------------------------------------------------------------
# The model of one robot.py
# ---------------------------------------------------------------

class Item:
    def __init__(self, kind, name, lesson, **kw):
        self.kind = kind          # banner|setting|func|class|object
        self.name = name
        self.lesson = lesson
        self.lines = kw.get("lines")       # banner, setting, object
        self.outline = kw.get("outline")   # func
        self.body = kw.get("body")         # func (sample)
        self.full = kw.get("full", False)
        self.invented = kw.get("invented", False)
        self.header = kw.get("header")     # class
        self.methods = kw.get("methods")   # class: list of Method
        self.ext = kw.get("ext", False)

    def key(self):
        return "banner:" + self.name if self.kind == "banner" else self.name


class Method:
    def __init__(self, name, outline, body, full):
        self.name = name
        self.outline = outline
        self.body = body
        self.full = full


class Model:
    def __init__(self):
        self.imports = []
        self.objects = []
        self.run = []
        self.items = []

    def find(self, key):
        for it in self.items:
            if it.key() == key:
                return it
        return None

    def index(self, key):
        for i, it in enumerate(self.items):
            if it.key() == key:
                return i
        fail("no item %r in the file" % key)

    def insert(self, item, after=None, before=None):
        if after:
            self.items.insert(self.index(after) + 1, item)
        elif before:
            self.items.insert(self.index(before), item)
        else:
            self.items.append(item)

    def delete(self, key):
        self.items.pop(self.index(key))


# ---------------------------------------------------------------
# Ops
# ---------------------------------------------------------------

class Op:
    tracks = TRACKS

    def __init__(self, *a, **kw):
        self.tracks = kw.pop("tracks", TRACKS)
        self.after = kw.pop("after", None)
        self.before = kw.pop("before", None)
        self.setup(*a, **kw)

    def setup(self):
        pass

    def ext_for(self, track):
        if self.ext is not None:
            return self.ext
        return track == "class" and self.tracks == ("class",)


class Start(Op):
    def setup(self, lesson):
        self.lesson = lesson

    def apply(self, model, track):
        for f in fences_for(self.lesson, "student", False):
            if "# ===== RUN =====" in f.text:
                model.imports = [c.lines[0] for c in f.chunks if c.kind == "import"]
                model.objects = [c.lines[0] for c in f.chunks if c.kind == "object"]
                lines = f.text.split("\n")
                k = lines.index("# ===== RUN =====")
                model.run = lines[k:]
                return
        fail("lesson %s: no start block fence with the RUN banner" % self.lesson)


class AddImport(Op):
    def setup(self, lesson, prefix, after_prefix=None):
        self.lesson, self.prefix, self.after_prefix = lesson, prefix, after_prefix

    def apply(self, model, track):
        for f in fences_for(self.lesson, "student", False):
            for c in f.chunks:
                if c.kind == "import" and c.name.startswith(self.prefix):
                    line = c.lines[0]
                    if self.after_prefix:
                        idx = max(i for i, l in enumerate(model.imports)
                                  if l.startswith(self.after_prefix))
                        model.imports.insert(idx + 1, line)
                    else:
                        model.imports.append(line)
                    return
        fail("lesson %s: no import line starting %r" % (self.lesson, self.prefix))


class AddObject(Op):
    def setup(self, lesson, name):
        self.lesson, self.name = lesson, name

    def apply(self, model, track):
        f, c = find_chunk(self.lesson, "student", False, "object", self.name)
        model.objects.append(c.lines[0])


class Banner(Op):
    def setup(self, key, lesson, match, ext=None):
        self.key, self.lesson, self.match, self.ext = key, lesson, match, ext

    def apply(self, model, track):
        ext = self.ext_for(track)
        for f in fences_for(self.lesson, "student", ext):
            for c in f.chunks:
                if c.kind == "banner" and self.match in c.lines[0]:
                    model.insert(Item("banner", self.key, self.lesson, lines=c.lines),
                                 self.after, self.before)
                    return
        fail("lesson %s: no banner matching %r" % (self.lesson, self.match))


class Setting(Op):
    def setup(self, name, lesson, ext=None):
        self.name, self.lesson, self.ext = name, lesson, ext

    def apply(self, model, track):
        # prefer the skeleton fence (the one with a banner) over a
        # prose snippet that shows the same line
        hits = []
        for f in fences_for(self.lesson, "student", self.ext_for(track)):
            kinds = {c.kind for c in f.chunks}
            for c in f.chunks:
                if c.kind == "setting" and c.name == self.name:
                    hits.append(("banner" in kinds, c))
        if not hits:
            fail("lesson %s: no skeleton fence has the setting %s" % (self.lesson, self.name))
        hits.sort(key=lambda h: h[0])
        model.insert(Item("setting", self.name, self.lesson, lines=hits[-1][1].lines),
                     self.after, self.before)


class SetValue(Op):
    def setup(self, name, lesson, value, evidence):
        self.name, self.lesson, self.value, self.evidence = name, lesson, value, evidence

    def apply(self, model, track):
        text = open(lesson_path(self.lesson), encoding="utf-8").read()
        if not re.search(self.evidence, text):
            fail("lesson %s no longer says %r" % (self.lesson, self.evidence))
        it = model.find(self.name)
        if it is None:
            fail("lesson %s edits %s, which is not in the file" % (self.lesson, self.name))
        line = it.lines[0]
        m = re.match(r"^(%s = )(\S+)(.*)$" % self.name, line)
        it.lines = [m.group(1) + self.value + m.group(3)]
        it.lesson = self.lesson


class Func(Op):
    def setup(self, name, lesson, full=False, pick=0, replace=False, ext=None):
        self.name, self.lesson, self.full, self.pick = name, lesson, full, pick
        self.replace, self.ext = replace, ext

    def apply(self, model, track):
        f, c = find_def_outline(self.name, self.lesson, self.ext_for(track), self.full, self.pick)
        if self.replace:
            it = model.find(self.name)
            if it is None:
                fail("lesson %s rewrites %s(), which is not in the file" % (self.lesson, self.name))
            it.outline, it.lesson, it.full = c.lines, self.lesson, self.full
        else:
            if model.find(self.name) is not None:
                fail("lesson %s: %s() is already in the file" % (self.lesson, self.name))
            model.insert(Item("func", self.name, self.lesson, outline=c.lines, full=self.full),
                         self.after, self.before)


class Rename(Op):
    def setup(self, old, new, lesson):
        self.old, self.new, self.lesson = old, new, lesson

    def apply(self, model, track):
        it = model.find(self.old)
        if it is None:
            fail("lesson %s renames %s, which is not in the file" % (self.lesson, self.old))
        # the first student fence that defines the new name WITH a
        # docstring (4-5 also shows the bare def line as a diff)
        for f in fences_for(self.lesson, "student", False):
            for c in f.chunks:
                if c.kind == "def" and c.name == self.new and split_def(c.lines)[1]:
                    break
            else:
                continue
            break
        else:
            fail("lesson %s: no fence gives %s() with a docstring" % (self.lesson, self.new))
        head, doc, _ = split_def(c.lines)
        _, _, rest = split_def(it.outline)
        it.outline = [head] + doc + rest
        it.name, it.lesson = self.new, self.lesson


class Refresh(Op):
    def setup(self, name, lesson, kind="teacher", ext=False, full=True):
        self.name, self.lesson, self.kind, self.ext, self.full = name, lesson, kind, ext, full

    def apply(self, model, track):
        it = model.find(self.name)
        if it is None:
            fail("lesson %s edits %s(), which is not in the file" % (self.lesson, self.name))
        f, c = find_chunk(self.lesson, self.kind, self.ext, "def", self.name)
        if self.full:
            it.outline, it.full = c.lines, True
        else:
            head, doc, _ = split_def(c.lines)
            _, _, rest = split_def(it.outline)
            it.outline = [head] + doc + rest
        it.lesson = self.lesson


class Invent(Op):
    def setup(self, name, lesson, body=None):
        self.name, self.lesson, self.body = name, lesson, body

    def apply(self, model, track):
        body = self.body.strip("\n").split("\n") if self.body else None
        model.insert(Item("func", self.name, self.lesson, outline=None, body=body, invented=True),
                     self.after, self.before)


class Delete(Op):
    def setup(self, key):
        self.key = key

    def apply(self, model, track):
        model.delete(self.key)


class Class(Op):
    def setup(self, name, lesson, methods, ext=True):
        self.name, self.lesson, self.methods, self.ext = name, lesson, methods, ext

    def apply(self, model, track):
        for f in fences_for(self.lesson, "student", self.ext):
            for c in f.chunks:
                if c.kind != "class" or c.name != self.name:
                    continue
                header, methods = parse_class(c.lines)
                names = [n for n, _ in methods]
                if any(m not in names for m in self.methods):
                    continue
                if any(not is_outline(b) for n, b in methods if n != "__init__"):
                    continue
                ms = []
                for n, body in methods:
                    if n == "__init__":
                        ms.append(Method(n, body, body, True))
                    else:
                        real = find_method_body(self.name, n, self.lesson, self.ext)
                        if real is None:
                            fail("lesson %s: no Reveal gives %s.%s()" % (self.lesson, self.name, n))
                        ms.append(Method(n, body, real, False))
                model.insert(Item("class", self.name, self.lesson, header=header, methods=ms),
                             self.after, self.before)
                return
        fail("lesson %s: no extension skeleton defines class %s with %r" % (
            self.lesson, self.name, self.methods))


class AddMethods(Op):
    def setup(self, cls, lesson, names, kind="student", ext=True, full=True):
        self.cls, self.lesson, self.names, self.kind, self.ext, self.full = (
            cls, lesson, names, kind, ext, full)

    def apply(self, model, track):
        it = model.find(self.cls)
        if it is None or it.kind != "class":
            fail("lesson %s adds methods to %s, which is not a class here" % (self.lesson, self.cls))
        for n in self.names:
            found = None
            for f in fences_for(self.lesson, self.kind, self.ext):
                for c in f.chunks:
                    if c.kind == "method" and c.name == n and found is None:
                        found = c.lines
                    if c.kind == "class" and c.name == self.cls:
                        for mn, body in parse_class(c.lines)[1]:
                            if mn == n and found is None:
                                found = body
                if found:
                    break
            if found is None:
                fail("lesson %s: no %s fence gives method %s()" % (self.lesson, self.kind, n))
            it.methods.append(Method(n, found, found, self.full))


class AddMethodText(Op):
    def setup(self, cls, name, outline, body):
        self.cls, self.name = cls, name
        self.outline = outline.strip("\n").split("\n")
        self.body = body.strip("\n").split("\n")

    def apply(self, model, track):
        it = model.find(self.cls)
        if it is None or it.kind != "class":
            fail("%s is not a class in the file" % self.cls)
        it.methods.append(Method(self.name, self.outline, self.body, False))


class Object(Op):
    def setup(self, name, lesson, ext=True):
        self.name, self.lesson, self.ext = name, lesson, ext

    def apply(self, model, track):
        # prefer the line in the skeleton fence (the one with the
        # class) over an earlier teaching snippet
        hits = []
        for f in fences_for(self.lesson, "student", self.ext):
            kinds = {c.kind for c in f.chunks}
            for c in f.chunks:
                if c.kind == "object" and c.name == self.name:
                    hits.append(("class" in kinds, c))
        if not hits:
            fail("lesson %s: no fence creates the object %s" % (self.lesson, self.name))
        hits.sort(key=lambda h: h[0])
        model.insert(Item("object", self.name, self.lesson, lines=hits[-1][1].lines),
                     self.after, self.before)


C = ("class",)   # class-track-only ops

# ---------------------------------------------------------------
# Class-track test bodies the lessons give only in prose
# ---------------------------------------------------------------
# Each entry: the lesson it takes effect from, the outline a
# template shows (None = the function outline with CLASS_RULES
# applied), the body a sample shows, and the sentence(s) of the
# lesson that specify it. Comment lines stay <= 62 characters.

CLASS_OVERRIDES = {
    # 4-8 extension: "drive_path([(1, 0)], (0, 0), 0) becomes
    # navigator.drive_path([(1, 0)]), and the print afterwards reads
    # navigator.position and navigator.heading. The planner call in
    # test_drive_path() is handed navigator.position."
    "test_drive_path": dict(frm="4-8", outline='''
def test_drive_path():
    destination = (2, 3)

    path = planner.compute_path(navigator.position, destination)
    print("Path:", path)

    board.wait_for_button()       # read the path, THEN press

    navigator.drive_path(path)
    print("Arrived at:", navigator.position, "facing", HEADING_NAMES[navigator.heading])
'''),
    "test_one_leg": dict(frm="4-8", outline=None, body='''
def test_one_leg():
    navigator.drive_path([(1, 0)])
    print("Arrived at:", navigator.position, "facing", HEADING_NAMES[navigator.heading])
'''),
    # 4-8: desired_heading(self, next_pos) "has lost its position
    # parameter ... the object already knows both"; the 4-7 test
    # asks from (1, 1), so it builds a navigator standing there.
    "test_headings": dict(frm="4-8", outline=None, body='''
def test_headings():
    nav = Navigator((1, 1), 0)
    for next_pos in [(0, 1), (1, 2), (2, 1), (1, 0)]:
        heading = nav.desired_heading(next_pos)
        print("(1, 1) ->", next_pos, ":", heading, HEADING_NAMES[heading])
    # nav.desired_heading((2, 2))   # diagonal: stops here
'''),
    "test_turns_paper": dict(frm="4-8", outline=None, body='''
def test_turns_paper():
    for next_pos in [(1, 0), (1, 1)]:
        needed = navigator.desired_heading(next_pos)
        print("to", next_pos, ": need", HEADING_NAMES[needed],
              "turns:", (needed - navigator.heading) % 4)
        navigator.heading = needed
        navigator.position = next_pos
'''),
    # 4-9 teacher copy: "test_delivery() is handed navigator.position
    # by the planner call, drives with navigator.drive_path(path),
    # and prints navigator.position -- there is no
    # position, heading = ... line to get half right."
    "test_delivery": dict(frm="4-9", outline='''
def test_delivery():
    # the navigator starts at home, facing North
    # plan the FIRST leg and print it; wait for the button
    # for each destination:
    #     compute the path from navigator.position
    #     print it
    #     navigator.drive_path(path) -- it keeps the record
    #     print where the navigator arrived
    pass
''', body='''
def test_delivery():
    print("Planned path for leg 1:",
          planner.compute_path(navigator.position, DESTINATIONS[0]))
    board.wait_for_button()

    for dest in DESTINATIONS:
        print("--- Navigating to", dest, "---")
        path = planner.compute_path(navigator.position, dest)
        print("Path:", path)
        navigator.drive_path(path)
        print("Arrived at:", navigator.position, "facing", HEADING_NAMES[navigator.heading])
'''),
    # 5-5 extension: "one more test -- test_two_planners() -- that
    # runs the wall case against both objects: create a Manhattan()
    # and a BFS(), tell each add_blocked((1, 0)) and
    # add_blocked((1, 1)), and print each one's
    # compute_path((0, 0), (3, 0))."
    "test_two_planners": dict(frm="5-5", outline=None, body='''
def test_two_planners():
    manhattan = Manhattan()
    bfs = BFS()
    for p in [manhattan, bfs]:
        p.add_blocked((1, 0))
        p.add_blocked((1, 1))
    print("Manhattan:", manhattan.compute_path((0, 0), (3, 0)))   # straight through
    print("BFS:      ", bfs.compute_path((0, 0), (3, 0)))         # around
'''),
    # 5-6 extension: "test_harness() hands in Manhattan() and BFS()";
    # "test_swap() gets the same treatment: navigate() calls
    # planner.compute_path(...), and the test hands it Manhattan()
    # and your planner."
    "test_harness": dict(frm="5-6", outline=None, body='''
def test_harness():
    run_all_tests("Manhattan", Manhattan())
    run_all_tests("BFS", BFS())
'''),
    "test_swap": dict(frm="5-6", outline=None, body='''
def test_swap():
    planner.clear_blocked()
    planner.add_blocked((2, 0))
    print("Manhattan:")
    position = navigate(Manhattan(), (0, 0), (3, 3))   # through the wall
    position = navigate(Manhattan(), position, (0, 0))
    print("BFS:")
    position = navigate(planner, (0, 0), (3, 3))        # around it
    position = navigate(planner, position, (0, 0))
'''),
    # 5-7: "the driving calls in the outline are tracker. or
    # navigator.line_track. calls, as in Lesson 4-8, and the planner
    # calls are planner.add_blocked() and planner.compute_path()."
    "test_detect_once": dict(frm="5-7", outline='''
def test_detect_once():
    # the navigator at (0, 0) facing North; destination (3, 3)
    # plan the path, print it, wait for the button
    # for each next_pos in path:
    #     face it: navigator.desired_heading(), then
    #         navigator.turn_to()
    #     NEW: look ahead -- distance = simulate_rangefinder(
    #          next_pos) for now; rangefinder.distance() later
    #     print navigator.position, its heading, the distance
    #     if distance < OBSTACLE_CM:
    #         tell the planner: planner.add_blocked(next_pos)
    #         new path from HERE: planner.compute_path(
    #             navigator.position, destination); print it;
    #             then break
    #     else:
    #         arrive: navigator.line_track.
    #             track_to_intersection(), then
    #             drive_past_intersection()
    #         navigator.position = next_pos
    # print the blocked list, planner.blocked
    pass
''', body='''
def test_detect_once():
    destination = (3, 3)

    path = planner.compute_path(navigator.position, destination)
    print("Planned path:", path)
    board.wait_for_button()

    for next_pos in path:
        needed = navigator.desired_heading(next_pos)
        navigator.turn_to(needed)

        distance = simulate_rangefinder(next_pos)     # rangefinder.distance() on the robot
        print("At", navigator.position, "facing", HEADING_NAMES[navigator.heading],
              "- ahead:", distance, "cm")

        if distance < OBSTACLE_CM:
            planner.add_blocked(next_pos)
            print("Obstacle at", next_pos, "! Rerouting...")
            path = planner.compute_path(navigator.position, destination)
            print("New path:", path)
            break      # Lesson 5-8 keeps going instead
        else:
            navigator.line_track.track_to_intersection()
            navigator.line_track.drive_past_intersection()
            navigator.position = next_pos
            print("Drove to", navigator.position)
    print("All known obstacles:", planner.blocked)
'''),
    # 5-8: the function "wants to be a method of [Navigator] ... It
    # returns only the two counts; the caller reads
    # navigator.position afterwards, as in Lesson 4-9."
    "test_navigate": dict(frm="5-8", outline=None, body='''
def test_navigate():
    for intersection in KNOWN_OBSTACLES:
        planner.add_blocked(intersection)
    destination = (3, 3)

    print("Planned path:", planner.compute_path(navigator.position, destination))
    board.wait_for_button()

    steps, reroutes = navigator.navigate_with_detection(
        destination, rangefinder, OBSTACLE_CM
    )
    print("Arrived at:", navigator.position, "facing", HEADING_NAMES[navigator.heading])
    print("Steps:", steps, " Reroutes:", reroutes)
    print("All known obstacles:", planner.blocked)
'''),
    # 5-9 teacher copy: "the loop body is steps, reroutes =
    # navigator.navigate_with_detection(dest, rangefinder,
    # OBSTACLE_CM) and the final line prints planner.blocked".
    "test_capstone": dict(frm="5-9", outline='''
def test_capstone():
    # 1. hand KNOWN_OBSTACLES to planner.add_blocked()
    #    (empty on Run 1, last run's list on Run 2)
    # 2. the navigator starts at (0, 0) heading 0; totals at 0
    # 3. print the plan for leg 1; wait for the button
    # 4. for each destination, with its leg number:
    #        navigator.navigate_with_detection() -- plan,
    #        follow, re-plan until arrived (Lesson 5-8); the
    #        navigator keeps position and heading itself
    #        add its steps and reroutes to the totals
    # 5. print planner.blocked -- what you type in next run
    # 6. print the totals: steps, reroutes
    pass
''', body='''
def test_capstone():
    for intersection in KNOWN_OBSTACLES:
        planner.add_blocked(intersection)
    total_steps = 0
    total_reroutes = 0

    print("Planned path for leg 1:",
          planner.compute_path(navigator.position, CAPSTONE_DESTINATIONS[0]))
    board.wait_for_button()

    for i in range(len(CAPSTONE_DESTINATIONS)):
        dest = CAPSTONE_DESTINATIONS[i]
        print("--- Leg", i + 1, ": Heading to", dest, "---")

        steps, reroutes = navigator.navigate_with_detection(
            dest, rangefinder, OBSTACLE_CM
        )

        total_steps = total_steps + steps
        total_reroutes = total_reroutes + reroutes
        print("  Arrived at", dest)

    print("=== FINAL REPORT ===")
    print("Total steps:", total_steps)
    print("Total reroutes:", total_reroutes)
    print("Obstacles discovered:", planner.blocked)
'''),
    # 6-4: "drive_path() is navigator.drive_path(path) ... the plans
    # are made from navigator.position"; 6-5: "PLANNER_NAME chooses
    # an object -- planner = Dijkstra() or planner = BFS() -- which
    # is told the slow segment with slow(planner, ...) and asked for
    # the path with planner.compute_path()"; its teacher copy: "the
    # three driving lines are navigator = Navigator(position,
    # heading) before the button and navigator.drive_path(path)
    # between the two times".
    "test_drive_slow_grid": dict(frm="6-4", outline='''
def test_drive_slow_grid():
    # 1. clear the slow list; add SLOW_SEGMENT to it
    # 2. position (0, 0), heading 0, destination (0, 3)
    # 3. planner = the planner PLANNER_NAME names
    # 4. compare() both plans, so the choice is on screen
    # 5. plan with planner; navigator = Navigator(position,
    #    heading); then board.wait_for_button()
    # 6. note the time; navigator.drive_path(path); note the
    #    time again
    # 7. print PLANNER_NAME, the seconds and the step count
    pass
''', body_frm="6-5", body='''
def test_drive_slow_grid():
    if PLANNER_NAME == "Dijkstra":
        planner = Dijkstra()
    else:
        planner = BFS()
    clear(planner)
    slow(planner, SLOW_SEGMENT[0], SLOW_SEGMENT[1], SLOW_SEGMENT[2])
    position = (0, 0)
    heading = 0
    destination = (0, 3)

    compare(position, destination)
    path = planner.compute_path(position, destination)
    navigator = Navigator(position, heading)
    board.wait_for_button()

    start_time = time.time()
    navigator.drive_path(path)
    elapsed = time.time() - start_time
    print(PLANNER_NAME, "took", round(elapsed, 1), "seconds for", len(path), "steps")
'''),
}

# 5-8: "If you built the Navigator class in Lesson 4-8, this
# function wants to be a method of it: position and heading become
# self.position and self.heading and drop out of the parameter list
# and the return, the four driving calls go through self.line_track.
# and self.desired_heading() / self.turn_to(), and the planner calls
# are planner.add_blocked() and planner.compute_path(). It returns
# only the two counts".
NAVIGATE_METHOD_OUTLINE = '''
def navigate_with_detection(self, destination, rangefinder, obstacle_cm):
    """Drive from self.position (facing self.heading) to
    destination, re-planning around every obstacle the
    rangefinder finds; return (step_count, reroute_count)."""
    # the 5-8 function as a method: self.position and
    # self.heading replace the parameters; the driving
    # goes through self.line_track, self.desired_heading()
    # and self.turn_to(); planner calls stay on planner
    # step_count = 0 ; reroute_count = 0
    # arrived = False
    # while not arrived:
    #     plan from self.position; print the path
    #     if the path is empty: say "No path"; return both
    #     rerouted = False
    #     for each next_pos in path:      -- Lesson 5-7
    #         face it
    #         look ahead with rangefinder.distance()
    #         if closer than obstacle_cm:
    #             planner.add_blocked(next_pos); count it
    #             rerouted = True ; break
    #         else:
    #             arrive; self.position = next_pos; count
    #     if not rerouted: arrived = True
    # return step_count, reroute_count
    pass
'''
NAVIGATE_METHOD_BODY = '''
def navigate_with_detection(self, destination, rangefinder, obstacle_cm):
    """Drive from self.position (facing self.heading) to
    destination, re-planning around every obstacle the
    rangefinder finds; return (step_count, reroute_count)."""
    step_count = 0
    reroute_count = 0

    arrived = False
    while not arrived:
        path = planner.compute_path(self.position, destination)
        print("  Path from", self.position, ":", path)

        if len(path) == 0:
            print("No path to", destination, "!")
            return step_count, reroute_count

        rerouted = False
        for next_pos in path:
            needed = self.desired_heading(next_pos)
            self.turn_to(needed)

            distance = rangefinder.distance()          # look before driving
            if distance < obstacle_cm:
                planner.add_blocked(next_pos)
                print("  OBSTACLE at", next_pos, "! Rerouting...")
                reroute_count = reroute_count + 1
                rerouted = True
                break
            else:
                self.line_track.track_to_intersection()
                self.line_track.drive_past_intersection()
                self.position = next_pos
                step_count = step_count + 1

        if not rerouted:
            arrived = True

    return step_count, reroute_count
'''

# ---------------------------------------------------------------
# Class-track substitutions: (from lesson, only these names or
# None, pattern, replacement). Scoped rules run first.
# ---------------------------------------------------------------
NOT_ATTR = r"(?<![\w.])"
CLASS_RULES = [
    # 2-7: "each sensor call in them gets sensor. in front"
    ("2-7", None, NOT_ATTR + r"(get_left|get_right|get_error|is_either_on_line|is_at_cross)\(",
     r"sensor.\1("),
    # 2-7: "THRESHOLD stop[s] being [a] global ... self.threshold";
    # the lesson does not say what 2-2's test_drive_to_line() reads
    # once THRESHOLD is gone -- the object's attribute is the only
    # faithful reading.
    ("2-7", None, NOT_ATTR + r"THRESHOLD\b", "sensor.threshold"),
    # 2-9: "each call in them gets tracker. in front"; "the settings
    # moved from file-level capitals into self. attributes"
    ("2-9", None, NOT_ATTR + r"(track_to_intersection|drive_past_intersection|"
     r"turn_clockwise|turn_counterclockwise)\(", r"tracker.\1("),
    ("2-9", None, NOT_ATTR + r"KP\b", "tracker.kp"),
    ("2-9", None, NOT_ATTR + r"BASE_EFFORT\b", "tracker.base_effort"),
    ("2-9", None, NOT_ATTR + r"TURN_EFFORT\b", "tracker.turn_effort"),
    # 4-5: "each compute_manhattan_path( in them becomes
    # planner.compute_path("
    ("4-5", None, NOT_ATTR + r"compute_manhattan_path\(", "planner.compute_path("),
    # 5-5: "in Lesson 4-6's run_test() change planner.compute_path(...)
    # to Manhattan().compute_path(...)"
    ("5-5", {"run_test"}, r"planner\.compute_path\(", "Manhattan().compute_path("),
    # 5-6 extension: the four edits
    ("5-6", {"run_all_tests"}, NOT_ATTR + r"add_blocked\(", "block(planner, "),
    ("5-6", {"run_all_tests"}, NOT_ATTR + r"clear_blocked\(\)", "clear(planner)"),
    ("5-6", {"check_path"}, NOT_ATTR + r"BLOCKED\b", "HARNESS_BLOCKED"),
    ("5-6", {"run_path_test", "run_no_path_test", "navigate", "run_all_tests"},
     NOT_ATTR + r"planner\(", "planner.compute_path("),
    # 5-5: "add_blocked( becomes planner.add_blocked(, clear_blocked()
    # becomes planner.clear_blocked(), compute_bfs_path( becomes
    # planner.compute_path(, and where a test or bfs_rings() reads
    # BLOCKED it reads planner.blocked"
    ("5-5", None, NOT_ATTR + r"compute_bfs_path\b", "planner.compute_path"),
    ("5-5", None, NOT_ATTR + r"add_blocked\(", "planner.add_blocked("),
    ("5-5", None, NOT_ATTR + r"clear_blocked\(\)", "planner.clear_blocked()"),
    ("5-5", None, NOT_ATTR + r"BLOCKED\b", "planner.blocked"),
]


def apply_rules(name, lines, lesson):
    text = "\n".join(lines)
    for frm, only, pat, repl in CLASS_RULES:
        if lkey(frm) > lkey(lesson):
            continue
        if only is not None and name not in only:
            continue
        text = re.sub(pat, repl, text)
    return text.split("\n")


# ---------------------------------------------------------------
# Functions the lessons give in full (allowed real bodies in a
# TEMPLATE). name -> (why, lesson range or None)
# ---------------------------------------------------------------
GIVEN_IN_FULL = {
    "test_sensors": ("2-1: the first test, given in full (Module 2 gives tests in full)", None),
    "test_sweep": ("2-5: the no-motor % demo, given in full in required text", None),
    "test_cross_moving": ("2-8: Module 2 test, given in full in the skeleton", None),
    "test_track": ("2-8: Module 2 test, given in full in the skeleton", None),
    "test_reverse": ("2-8: Module 2 test, given in full in the skeleton", None),
    "test_park": ("2-9: Module 2 test, given in full in the skeleton", None),
    "test_turn": ("2-9: Module 2 test, given in full in the skeleton", None),
    "test_course": ("2-9: Module 2 test, given in full in the skeleton", None),
    "set_threshold": ("2-7: the global-keyword demo; its body is the lesson text", None),
    "test_drive_path": ("4-8: the plan, print, button, drive shape, given in full", None),
    "compute_bfs_path": ("5-4: the placeholder body is given ('it isn't the function yet')", ("5-4", "5-4")),
    "print_grid": ("5-5: 'print_grid() is given -- it's formatting, not pathfinding'", None),
    "run_all_tests": ("5-6: the suite is given ('the same program'); 6-3/6-5 edit it", None),
    "navigate": ("5-6: given with run_all_tests as the swap demo", None),
    "compare": ("6-3: 'compare() is given -- it's a print, not a planner'", None),
    "Manhattan.add_blocked": ("5-5: deliberate no-op, given", None),
    "Manhattan.clear_blocked": ("5-5: deliberate no-op, given", None),
    "Manhattan.add_slow_edge": ("6-5: deliberate no-op, given", None),
    "Manhattan.clear_slow_edges": ("6-5: deliberate no-op, given", None),
    "BFS.add_slow_edge": ("6-5: deliberate no-op, given", None),
    "BFS.clear_slow_edges": ("6-5: deliberate no-op, given", None),
}

# ---------------------------------------------------------------
# THE RECIPE
# ---------------------------------------------------------------
RECIPE = [
    ("2-1", [
        Start("2-1"),
        Banner("LINE SENSOR", "2-1", "===== LINE SENSOR ====="),
        Func("get_left", "2-1"),
        Func("get_right", "2-1"),
        Func("test_sensors", "2-1", full=True),
    ]),
    ("2-2", [
        Setting("THRESHOLD", "2-2", after="banner:LINE SENSOR"),
        Func("test_drive_to_line", "2-2"),
    ]),
    ("2-3", [
        Func("is_either_on_line", "2-3", after="get_right"),
        Func("test_bounce", "2-3"),
    ]),
    ("2-4", [
        AddImport("2-4", "import random"),
        Func("test_random_bounce", "2-4"),
    ]),
    ("2-5", [
        Setting("SETPOINT", "2-5", after="THRESHOLD"),
        # "Add both under THRESHOLD": SETPOINT goes with the
        # settings; get_error() sits after get_right(), where every
        # later teacher copy shows it.
        Func("get_error", "2-5", after="get_right"),
        Banner("LINE TRACKING", "2-5", "===== LINE TRACKING ====="),
        Setting("BASE_EFFORT", "2-5"),
        Setting("KP", "2-5"),
        Func("test_follow", "2-5"),
        Func("test_sweep", "2-5", full=True),
    ]),
    ("2-6", [
        Func("get_error", "2-6", replace=True),
        Delete("SETPOINT"),
    ]),
    ("2-7", [
        Func("is_at_cross", "2-7", after="is_either_on_line"),
        Func("set_threshold", "2-7", full=True, pick=1, after="is_at_cross"),
        # class track: "Paste it in place of the LINE SENSOR
        # functions (keep THRESHOLD out -- it's self.threshold now)"
        Delete("banner:LINE SENSOR", tracks=C),
        Delete("THRESHOLD", tracks=C),
        Delete("get_left", tracks=C), Delete("get_right", tracks=C),
        Delete("get_error", tracks=C), Delete("is_either_on_line", tracks=C),
        Delete("is_at_cross", tracks=C), Delete("set_threshold", tracks=C),
        Banner("LINE SENSOR", "2-7", "LINE SENSOR (Lesson 2-7, class version)",
               before="test_sensors", tracks=C),
        Class("LineSensor", "2-7", ["get_left", "get_right", "get_error",
                                    "is_at_cross", "is_either_on_line"],
              after="banner:LINE SENSOR", tracks=C),
        Object("sensor", "2-7", after="LineSensor", tracks=C),
    ]),
    ("2-8", [
        Banner("L2-8", "2-8", "--- Lesson 2-8:"),
        Func("track_to_intersection", "2-8"),
        Func("test_cross_moving", "2-8", full=True),
        Func("test_track", "2-8", full=True),
        Func("test_reverse", "2-8", full=True),
        Invent("test_count", "2-8"),
    ]),
    ("2-9", [
        Banner("L2-9", "2-9", "--- Lesson 2-9:"),
        Setting("TURN_EFFORT", "2-9"),
        Func("drive_past_intersection", "2-9"),
        Func("turn_clockwise", "2-9"),
        Func("turn_counterclockwise", "2-9"),
        Invent("turn_around", "2-9"),
        Func("test_park", "2-9", full=True),
        Func("test_turn", "2-9", full=True),
        Func("test_course", "2-9", full=True),
        Invent("test_turn_around", "2-9"),
        SetValue("BASE_EFFORT", "2-9", "0.4", r"raise `BASE_EFFORT` to \*\*0\.4\*\*"),
        # class track: "Paste it in place of the section's settings
        # and four functions (keep the test functions)"
        Delete("banner:LINE TRACKING", tracks=C),
        Delete("BASE_EFFORT", tracks=C), Delete("KP", tracks=C),
        Delete("banner:L2-8", tracks=C), Delete("track_to_intersection", tracks=C),
        Delete("banner:L2-9", tracks=C), Delete("TURN_EFFORT", tracks=C),
        Delete("drive_past_intersection", tracks=C),
        Delete("turn_clockwise", tracks=C), Delete("turn_counterclockwise", tracks=C),
        Banner("LINE TRACKING", "2-9", "LINE TRACKING (class version)",
               before="test_follow", tracks=C),
        Class("LineTrack", "2-9", ["track_to_intersection", "drive_past_intersection",
                                   "turn_clockwise", "turn_counterclockwise"],
              after="banner:LINE TRACKING", tracks=C),
        Object("tracker", "2-9", after="LineTrack", tracks=C),
    ]),
    ("2-10", [
        Banner("L2-10", "2-10", "--- Lesson 2-10:"),
        Func("test_reversal", "2-10"),
        Func("test_final_project", "2-10"),
    ]),
    ("3-1", [
        Banner("GRID DRIVING", "3-1", "===== GRID DRIVING ====="),
        Func("test_first_intersection", "3-1"),
        Func("test_arrive_and_turn", "3-1"),
    ]),
    ("3-2", [
        Banner("L3-2", "3-2", "--- Lesson 3-2:"),
        Func("drive_intersections", "3-2"),
        Func("test_two_by_hand", "3-2"),
        Func("test_drive_run", "3-2"),
    ]),
    ("3-3", [
        Banner("L3-3", "3-3", "--- Lesson 3-3:"),
        Func("test_l_shape", "3-3"),
        Func("test_my_path", "3-3"),
    ]),
    ("3-4", [
        Banner("L3-4", "3-4", "--- Lesson 3-4:"),
        Setting("SIDE", "3-4"),
        Func("test_one_side", "3-4"),
        Func("test_square", "3-4"),
    ]),
    ("4-4", [
        Banner("MANHATTAN PLANNER", "4-4", "===== MANHATTAN PLANNER ====="),
        Func("compute_path", "4-4"),
        Invent("test_paper_paths", "4-4"),
        Invent("test_edge_cases", "4-4"),
    ]),
    ("4-5", [
        Rename("compute_path", "compute_manhattan_path", "4-5"),
        Invent("test_from_everywhere", "4-5"),
        # class track: "Paste it in place of the
        # compute_manhattan_path() function (keep your tests)"
        Delete("banner:MANHATTAN PLANNER", tracks=C),
        Delete("compute_manhattan_path", tracks=C),
        Banner("MANHATTAN PLANNER", "4-5", "MANHATTAN PLANNER (class version)",
               before="test_paper_paths", tracks=C),
        Class("Manhattan", "4-5", ["compute_path"], after="banner:MANHATTAN PLANNER", tracks=C),
        Object("planner", "4-5", after="Manhattan", tracks=C),
    ]),
    ("4-6", [
        Banner("L4-6", "4-6", "--- Lesson 4-6:"),
        Func("run_test", "4-6"),
        Invent("test_planner", "4-6"),
    ]),
    ("4-7", [
        Banner("NAVIGATOR", "4-7", "===== NAVIGATOR ====="),
        Setting("HEADING_NAMES", "4-7"),
        Func("desired_heading", "4-7"),
        Invent("test_headings", "4-7"),
    ]),
    ("4-8", [
        Banner("L4-8", "4-8", "--- Lesson 4-8:"),
        Func("turn_to", "4-8"),
        Func("drive_path", "4-8"),
        Invent("test_turns_paper", "4-8"),
        Invent("test_one_leg", "4-8"),
        Func("test_drive_path", "4-8", full=True),
        # class track: "paste it in place of the three functions
        # (keep HEADING_NAMES and your tests)"
        Delete("banner:NAVIGATOR", tracks=C),
        Delete("desired_heading", tracks=C),
        Delete("banner:L4-8", tracks=C),
        Delete("turn_to", tracks=C), Delete("drive_path", tracks=C),
        Banner("NAVIGATOR", "4-8", "NAVIGATOR (class version)", before="HEADING_NAMES", tracks=C),
        Class("Navigator", "4-8", ["desired_heading", "turn_to", "drive_path"],
              after="HEADING_NAMES", tracks=C),
        Object("navigator", "4-8", after="Navigator", tracks=C),
    ]),
    ("4-9", [
        Banner("L4-9", "4-9", "--- Lesson 4-9:"),
        Setting("DESTINATIONS", "4-9"),
        Func("test_delivery_paper", "4-9"),
        Func("test_delivery", "4-9"),
    ]),
    ("5-2", [
        Banner("GRID GRAPH", "5-2", "===== GRID GRAPH ====="),
        Setting("ROWS", "5-2"),
        Setting("COLS", "5-2"),
        Func("build_grid_graph", "5-2"),
        Func("remove_blocked", "5-2"),
        Invent("test_grid_graph", "5-2"),
        Invent("test_remove_blocked", "5-2"),
    ]),
    ("5-4", [
        Rename("build_grid_graph", "build_graph", "5-4"),
        Delete("remove_blocked"),
        Delete("test_remove_blocked"),
        Banner("L5-4", "5-4", "--- Lesson 5-4:"),
        Setting("BLOCKED", "5-4"),
        Func("add_blocked", "5-4"),
        Func("clear_blocked", "5-4"),
        Invent("test_blocked_graph", "5-4"),
        Banner("BFS PLANNER", "5-4", "===== BFS PLANNER ====="),
        Func("compute_bfs_path", "5-4", full=True),
    ]),
    ("5-5", [
        Func("compute_bfs_path", "5-5", replace=True),
        Func("bfs_rings", "5-5"),
        Func("print_grid", "5-5", full=True),
        Invent("test_bfs_open", "5-5"),
        Invent("test_bfs_walls", "5-5"),
        Invent("test_rings", "5-5"),
        # class track: "Paste it in place of the BFS PLANNER banner
        # and compute_bfs_path(), and delete BLOCKED, add_blocked()
        # and clear_blocked() from the Lesson 5-4 part of GRID
        # GRAPH"; "Delete the Manhattan line -- one object called
        # planner"; the Manhattan no-ops; test_two_planners().
        Delete("banner:L5-4", tracks=C), Delete("BLOCKED", tracks=C),
        Delete("add_blocked", tracks=C), Delete("clear_blocked", tracks=C),
        Delete("banner:BFS PLANNER", tracks=C), Delete("compute_bfs_path", tracks=C),
        Delete("planner", tracks=C),
        Banner("BFS PLANNER", "5-5", "BFS PLANNER (class version)", before="bfs_rings", tracks=C),
        Class("BFS", "5-5", ["add_blocked", "clear_blocked", "compute_path"],
              after="banner:BFS PLANNER", tracks=C),
        Object("planner", "5-5", after="BFS", tracks=C),
        AddMethods("Manhattan", "5-5", ["add_blocked", "clear_blocked"], tracks=C),
        Invent("test_two_planners", "5-5", after="test_rings", tracks=C),
    ]),
    ("5-6", [
        Banner("L5-6", "5-6", "--- Lesson 5-6:"),
        Func("manhattan_distance", "5-6"),
        Func("is_neighbor", "5-6"),
        Func("check_path", "5-6"),
        Func("run_path_test", "5-6"),
        Func("run_no_path_test", "5-6"),
        Func("run_all_tests", "5-6", full=True),
        Func("navigate", "5-6", full=True),
        Invent("test_harness", "5-6"),
        Invent("test_swap", "5-6"),
        # class track: "paste it at the top of the Lesson 5-6 part
        # of the file, above manhattan_distance()"
        Setting("HARNESS_BLOCKED", "5-6", after="banner:L5-6", tracks=C),
        Func("block", "5-6", after="HARNESS_BLOCKED", tracks=C),
        Func("clear", "5-6", after="block", tracks=C),
    ]),
    ("5-7", [
        AddImport("5-7", "from XRPLib.rangefinder", after_prefix="from XRPLib"),
        AddObject("5-7", "rangefinder"),
        Banner("OBSTACLES", "5-7", "===== OBSTACLES ====="),
        Setting("OBSTACLE_CM", "5-7"),
        Setting("SIMULATED_OBSTACLES", "5-7"),
        Func("simulate_rangefinder", "5-7"),
        Invent("test_rangefinder", "5-7"),
        Func("test_detect_once", "5-7"),
    ]),
    ("5-8", [
        Banner("L5-8", "5-8", "--- Lesson 5-8:"),
        Setting("KNOWN_OBSTACLES", "5-8"),
        Func("navigate_with_detection", "5-8", tracks=("function",)),
        AddMethodText("Navigator", "navigate_with_detection",
                      NAVIGATE_METHOD_OUTLINE, NAVIGATE_METHOD_BODY, tracks=C),
        Invent("test_navigate", "5-8"),
    ]),
    ("5-9", [
        Banner("L5-9", "5-9", "--- Lesson 5-9:"),
        Setting("CAPSTONE_DESTINATIONS", "5-9"),
        Func("test_capstone_paper", "5-9"),
        Func("test_capstone", "5-9"),
    ]),
    ("6-2", [
        Banner("WEIGHTED GRAPH", "6-2", "===== WEIGHTED GRAPH ====="),
        Setting("SLOW_EDGES", "6-2"),
        Func("add_slow_edge", "6-2"),
        Func("clear_slow_edges", "6-2"),
        Func("weight", "6-2"),
        Func("path_cost", "6-2"),
        Func("check_cost", "6-2"),
        Invent("test_weights", "6-2"),
        Invent("test_cost_check", "6-2"),
    ]),
    ("6-3", [
        # "Three edits to run_all_tests() ... seven now": the edited
        # suite is given code, pulled from the teacher copy.
        Refresh("run_all_tests", "6-3", kind="teacher"),
        Banner("DIJKSTRA PLANNER", "6-3", "===== DIJKSTRA PLANNER ====="),
        Func("closest", "6-3"),
        Func("compute_dijkstra_path", "6-3"),
        Func("dijkstra_distances", "6-3"),
        Func("compare", "6-3", full=True),
        Invent("test_three_planners", "6-3"),
        Invent("test_cost_grid", "6-3"),
    ]),
    ("6-4", [
        Banner("L6-4", "6-4", "--- Lesson 6-4:"),
        Setting("SLOW_SEGMENT", "6-4"),
        Setting("PLANNER_NAME", "6-4"),
        Func("test_drive_slow_grid", "6-4"),
    ]),
    ("6-5", [
        # class track only: "Paste it in place of the section's
        # banner and compute_dijkstra_path() -- closest() sits under
        # the new banner"; "Delete planner = BFS()"; the no-ops;
        # slow() "under clear()"; the three harness edits.
        Delete("banner:DIJKSTRA PLANNER", tracks=C),
        Delete("compute_dijkstra_path", tracks=C),
        Delete("planner", tracks=C),
        # (6-5 is a class-track lesson with no <OptionalExtension>
        # wrapper, so its fences are read with ext=False.)
        Banner("DIJKSTRA PLANNER", "6-5", "DIJKSTRA PLANNER (class version)",
               before="closest", ext=False, tracks=C),
        Class("Dijkstra", "6-5", ["add_blocked", "clear_blocked", "add_slow_edge",
                                  "clear_slow_edges", "weight", "compute_path"],
              after="closest", ext=False, tracks=C),
        Object("planner", "6-5", after="Dijkstra", ext=False, tracks=C),
        AddMethods("Manhattan", "6-5", ["add_slow_edge", "clear_slow_edges"],
                   kind="teacher", ext=False, tracks=C),
        AddMethods("BFS", "6-5", ["add_slow_edge", "clear_slow_edges"],
                   kind="teacher", ext=False, tracks=C),
        Func("slow", "6-5", after="clear", ext=False, tracks=C),
        Refresh("clear", "6-5", kind="reveal", ext=False, full=False, tracks=C),
        Refresh("run_all_tests", "6-5", kind="teacher", ext=False, tracks=C),
        Refresh("compare", "6-5", kind="teacher", ext=False, tracks=C),
    ]),
]
ALL_LESSONS[:] = [l for l, _ in RECIPE]


# ---------------------------------------------------------------
# Building and rendering
# ---------------------------------------------------------------

def build_models(track):
    """-> ordered list of (lesson, model after that lesson)."""
    model = Model()
    out = []
    for lesson, ops in RECIPE:
        changed = False
        for op in ops:
            if track in op.tracks:
                op.apply(model, track)
                changed = True
        if changed:
            out.append((lesson, copy.deepcopy(model)))
    return out


def override_for(track, name, lesson, which):
    if track != "class" or name not in CLASS_OVERRIDES:
        return None
    o = CLASS_OVERRIDES[name]
    frm = o.get("body_frm", o["frm"]) if which == "body" else o["frm"]
    if lkey(lesson) < lkey(frm):
        return None
    text = o.get(which)
    if text is None and which == "body":
        text = o.get("outline")      # given in full: outline is body
    if text is None:
        return None
    return text.strip("\n").split("\n")


def func_lines(item, track, lesson, sample):
    if sample:
        ov = override_for(track, item.name, lesson, "body")
        if ov:
            return ov
        if item.body:
            lines = item.body
        else:
            hit = find_def_body(item.name, lesson, track)
            lines = hit[1].lines if hit else item.outline
        if lines is None:
            fail("no body anywhere for %s() (lesson %s, %s track)" % (item.name, lesson, track))
    else:
        ov = override_for(track, item.name, lesson, "outline")
        if ov:
            return ov
        lines = item.outline
    if track == "class":
        lines = apply_rules(item.name, lines, lesson)
    return lines


def class_lines(item, sample):
    out = list(item.header)
    for i, m in enumerate(item.methods):
        if i > 0 or len(item.header) > 1:   # a docstring, then a blank
            out.append("")
        src = m.body if sample else m.outline
        out.extend("    " + l if l.strip() else "" for l in src)
    return out


def render(model, track, lesson, sample):
    lines = []
    if sample:
        lines.append("# robot.py, COMPLETE, as the teacher copies leave it after")
        lines.append("# Lesson %s (%s track). Answers: not for students." % (lesson, track))
    else:
        lines.append("# robot.py after Lesson %s (%s track): every skeleton" % (lesson, track))
        lines.append("# through Lesson %s pasted in, nothing written yet." % lesson)
    lines.append("")
    lines.extend(model.imports)
    lines.append("")
    lines.extend(model.objects)
    prev = None
    for it in model.items:
        if it.kind == "func" and it.invented and not sample:
            continue
        if it.kind == "banner":
            lines.extend(["", ""] if it.lines[0].startswith("# =====") else [""])
            lines.extend(it.lines)
        elif it.kind == "setting":
            if prev is None or prev.kind not in ("banner", "setting"):
                lines.append("")
            lines.extend(it.lines)
        elif it.kind == "object":
            lines.append("")
            lines.extend(it.lines)
        elif it.kind == "func":
            lines.append("")
            lines.extend(func_lines(it, track, lesson, sample))
        elif it.kind == "class":
            lines.append("")
            lines.extend(class_lines(it, sample))
        prev = it
    lines.append("")
    lines.extend(model.run)
    return "\n".join(lines) + "\n"


def changing_lessons(models):
    return [l for l, _ in models]


def last_lesson_of_module(models, module):
    return [l for l, _ in models if lkey(l)[0] == module][-1]


def write_file(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def build_all(samples_dir=None):
    written = []
    rendered = {}     # (track, lesson, sample) -> text
    for track in TRACKS:
        models = build_models(track)
        for lesson, model in models:
            text = render(model, track, lesson, False)
            rendered[(track, lesson, False)] = text
            path = os.path.join(OUT, track, "robot-after-%s.py" % lesson)
            write_file(path, text)
            written.append(path)
            rendered[(track, lesson, True)] = render(model, track, lesson, True)
        for module in sorted(MODULE_DIRS):
            last = last_lesson_of_module(models, module)
            path = os.path.join(OUT, track, "robot-end-of-module-%d.py" % module)
            write_file(path, rendered[(track, last, False)])
            written.append(path)
            if samples_dir:
                path = os.path.join(samples_dir, track, "robot-end-of-module-%d.py" % module)
                write_file(path, rendered[(track, last, True)])
                written.append(path)
    write_file(PAGE, render_page(rendered))
    written.append(PAGE)
    return written, rendered


# ---------------------------------------------------------------
# docs/templates.mdx
# ---------------------------------------------------------------

PAGE_HEAD = '''---
title: robot.py templates
sidebar_label: robot.py templates
sidebar_position: 1
---

{/* GENERATED by scripts/build_templates.py from the lessons.
    Edit the script's page text, not this file. */}

<LessonHeader
  eyebrow="Reference · Modules 2 to 6"
  title="robot.py templates"
  meta={['One file for the course', 'Two tracks', 'Pick up at any lesson']}
/>

From Lesson 2-1 to the end of the course you keep **one program file**,
`robot.py`. Every lesson hands you a *skeleton* to paste into it: a banner naming
the section, a few comment lines saying what the section does, its settings in
capitals, the outlines of the functions you are about to write, and that
lesson's test functions. The file grows a section at a time, and by Module 5 the
banner comments are its table of contents.

Two rules keep it working all year. **New code goes above the `RUN` block, never
below it** — Python runs a file top to bottom, so the run block has to be the
last thing in the file and everything it calls has to be defined above it. And
**the run block calls one test function at a time**: change the call, don't stack
them.

## What a template is

Each file below is `robot.py` as a student who has pasted **every skeleton
through that lesson, and written nothing yet**, would have it: all the banners,
settings and test functions, and every function outline ending in `pass`. None
of the bodies you are asked to write are in it. If you join the course late, lost
your file, or want a clean start for a lesson, download the file for the
*previous* lesson, rename it `robot.py`, and go on from there. The end-of-module
file is the same as the module's last lesson.

Two tracks, because the course has two. The **function track** is the course
everyone does: each section is plain functions and settings. The **class track**
is for students who take every *optional extension* — `LineSensor` (2-7),
`LineTrack` (2-9), `Manhattan` (4-5), `Navigator` (4-8), `BFS` (5-5), the class
harness (5-6) and `Dijkstra` (6-5). On that track a class skeleton replaces the
function section, the object is created right under its class, and the tests
call the object (`tracker.track_to_intersection()`,
`planner.compute_path(...)`). Up to Lesson 2-6 the two files are identical. If
you have built a class, stay on the class track; if you have not, use the
function track.

<Callout kind="tip" title="Saving a template">

The links open the file as plain text. Use **Save link as** (right-click the
link) or copy the whole page into a new file, and name it `robot.py`. Then
set the run line to the test you are working on.

</Callout>

<TeacherNote title="Where the complete files are">

These pages hold outlines only. The complete `robot.py` for any lesson is the
`Solution (teacher copy)` note at the end of that lesson's activity, which you
see with teacher mode on; the files are generated from those copies and the
student skeletons by `scripts/build_templates.py`, so they stay in step with the
lessons.

</TeacherNote>
'''


def render_page(rendered):
    out = [PAGE_HEAD]
    for module in sorted(MODULE_DIRS):
        out.append("\n## %s\n" % MODULE_NAMES[module])
        out.append("| After lesson | Function track | Class track |")
        out.append("|---|---|---|")
        lessons = sorted({l for (t, l, s) in rendered if lkey(l)[0] == module and not s},
                         key=lkey)
        for lesson in lessons:
            f = ("function", lesson, False) in rendered
            c = ("class", lesson, False) in rendered
            same = f and c and rendered[("function", lesson, False)].replace(
                "(function track)", "") == rendered[("class", lesson, False)].replace(
                "(class track)", "")
            label = "%s · %s" % (lesson, lesson_title(lesson))
            out.append("| %s | %s | %s |" % (
                label,
                link("function", "robot-after-%s.py" % lesson) if f else "no change",
                (link("class", "robot-after-%s.py" % lesson) + (" (identical)" if same else ""))
                if c else "no change"))
        out.append("| End of Module %d | %s | %s |" % (
            module,
            link("function", "robot-end-of-module-%d.py" % module),
            link("class", "robot-end-of-module-%d.py" % module)))
    out.append("")
    return "\n".join(out)


def link(track, name):
    return "[%s](pathname:///templates/%s/%s)" % (name, track, name)


# ---------------------------------------------------------------
# Verification
# ---------------------------------------------------------------

def top_names(text):
    tree = ast.parse(text)
    names = set()
    for st in tree.body:
        if isinstance(st, (ast.FunctionDef, ast.ClassDef)):
            names.add(st.name)
        elif isinstance(st, ast.Assign):
            for t in st.targets:
                if isinstance(t, ast.Name):
                    names.add(t.id)
    return names


def check_outlines(text, lesson, label):
    """Every def in a template is comments/docstring/pass, except
    GIVEN_IN_FULL. -> list of problems."""
    problems = []
    tree = ast.parse(text)

    def ok(fn, qual):
        for st in fn.body:
            if isinstance(st, ast.Pass):
                continue
            if (isinstance(st, ast.Expr) and isinstance(st.value, ast.Constant)
                    and isinstance(st.value.value, str)):
                continue
            return False
        return True

    def allowed(qual):
        if qual.endswith(".__init__"):
            return True
        if qual not in GIVEN_IN_FULL:
            return False
        rng = GIVEN_IN_FULL[qual][1]
        return rng is None or lkey(rng[0]) <= lkey(lesson) <= lkey(rng[1])

    for st in tree.body:
        if isinstance(st, ast.FunctionDef):
            if not ok(st, st.name) and not allowed(st.name):
                problems.append("%s: %s() has a real body" % (label, st.name))
        elif isinstance(st, ast.ClassDef):
            for m in st.body:
                if isinstance(m, ast.FunctionDef):
                    q = st.name + "." + m.name
                    if not ok(m, q) and not allowed(q):
                        problems.append("%s: %s() has a real body" % (label, q))
    return problems


def run_python(scratch, name, text, xrplib, runner=None, args=()):
    d = os.path.join(scratch, name)
    if os.path.isdir(d):
        shutil.rmtree(d)
    os.makedirs(d)
    shutil.copytree(xrplib, os.path.join(d, "XRPLib"),
                    ignore=shutil.ignore_patterns("__pycache__"))
    write_file(os.path.join(d, "robot.py"), text)
    cmd = [sys.executable, "robot.py"]
    if runner:
        write_file(os.path.join(d, "runner.py"), runner)
        cmd = [sys.executable, "runner.py"] + list(args)
    p = subprocess.run(cmd, cwd=d, capture_output=True, text=True, timeout=60)
    return p.returncode, p.stdout, p.stderr


RUNNER = '''
import runpy, sys
ns = runpy.run_path("robot.py", run_name="__main__")
for name in sys.argv[1:]:
    print("### calling", name)
    ns[name]()
'''

# Every test in a module-end sample that terminates against the
# stubs (no while True, no long sleeps), called in order in one
# process: a smoke run for the bodies, the class-track ones above
# all.
SMOKE = {
    2: ["test_drive_to_line", "test_cross_moving", "test_track", "test_reverse",
        "test_count", "test_park", "test_turn", "test_course", "test_turn_around",
        "test_reversal", "test_final_project"],
    3: ["test_first_intersection", "test_arrive_and_turn", "test_two_by_hand",
        "test_drive_run", "test_l_shape", "test_my_path", "test_one_side", "test_square"],
    4: ["test_paper_paths", "test_edge_cases", "test_from_everywhere", "test_planner",
        "test_headings", "test_turns_paper", "test_one_leg", "test_drive_path",
        "test_delivery_paper", "test_delivery"],
    5: ["test_grid_graph", "test_blocked_graph", "test_bfs_open", "test_bfs_walls",
        "test_rings", "test_harness", "test_swap", "test_detect_once", "test_navigate",
        "test_capstone_paper", "test_capstone"],
    6: ["test_weights", "test_cost_check", "test_three_planners", "test_cost_grid",
        "test_drive_slow_grid"],
}
SMOKE_CLASS_EXTRA = {5: ["test_two_planners"]}

PAPER = {
    4: ("test_planner", ["Forward right - PASS", "Backward left - PASS", "Same row - PASS",
                         "Same column - PASS", "Same spot - PASS", "One step - PASS"], ["FAIL"]),
    5: ("test_harness", ["Manhattan: 4 of 6 passed", "BFS: 6 of 6 passed"], []),
    6: ("test_three_planners", ["Manhattan: 4 of 7 passed", "BFS: 6 of 7 passed",
                                "Dijkstra: 7 of 7 passed"], []),
}


def verify(rendered, xrplib, scratch, base_dir=None):
    report = []
    problems = []
    # 1. py_compile every written file
    files = sorted(glob.glob(os.path.join(OUT, "*", "*.py")))
    for f in files:
        compile(open(f, encoding="utf-8").read(), f, "exec")   # no __pycache__
    for key, text in rendered.items():
        compile(text, "%s-%s%s" % (key[0], key[1], "-sample" if key[2] else ""), "exec")
    report.append("compiles: %d files under static/templates, %d rendered texts" % (
        len(files), len(rendered)))
    # 2. templates load; 3. outlines; 5. name sets
    loads = 0
    long_comments = {}
    for track in TRACKS:
        invented_so_far = set()
        for lesson in ALL_LESSONS:
            key = (track, lesson, False)
            if key not in rendered:
                continue
            text = rendered[key]
            rc, out, err = run_python(scratch, "tmpl_%s_%s" % (track, lesson), text, xrplib)
            if rc != 0:
                problems.append("template %s %s failed to run:\n%s" % (track, lesson, err[-800:]))
            else:
                loads += 1
            problems.extend(check_outlines(text, lesson, "template %s %s" % (track, lesson)))
            for n, line in enumerate(text.split("\n"), 1):
                if line.strip().startswith("#") and len(line) > COMMENT_MAX:
                    long_comments.setdefault(line.strip(), "%s %s:%d" % (track, lesson, n))
            # name sets
            sample = rendered[(track, lesson, True)]
            tnames = top_names(text)
            snames = top_names(sample)
            model = dict(build_models(track))[lesson]
            invented = {it.name for it in model.items if it.kind == "func" and it.invented}
            if tnames != snames - invented:
                problems.append("names differ for %s %s: template-only %r, sample-only %r" % (
                    track, lesson, sorted(tnames - (snames - invented)),
                    sorted((snames - invented) - tnames)))
    report.append("templates run to completion against the stubs: %d of %d" % (
        loads, sum(1 for k in rendered if not k[2])))
    if long_comments:
        report.append("comment lines over %d chars (all copied from the lessons):" % COMMENT_MAX)
        for text, where in sorted(long_comments.items(), key=lambda kv: kv[1]):
            report.append("  %s  <- first at %s" % (text, where))
    # 4. samples: paper tests
    for track in TRACKS:
        models = build_models(track)
        for module in sorted(MODULE_DIRS):
            last = last_lesson_of_module(models, module)
            text = rendered[(track, last, True)]
            if module in PAPER:
                fn, musts, mustnots = PAPER[module]
                rc, out, err = run_python(scratch, "sample_%s_m%d" % (track, module), text,
                                          xrplib, RUNNER, [fn])
                if rc != 0:
                    problems.append("sample %s M%d %s() crashed:\n%s" % (track, module, fn, err[-800:]))
                    continue
                for m in musts:
                    if m not in out:
                        problems.append("sample %s M%d: %s() output lacks %r" % (track, module, fn, m))
                for m in mustnots:
                    if m in out:
                        problems.append("sample %s M%d: %s() output contains %r" % (track, module, fn, m))
                summary = [l for l in out.split("\n") if " of " in l or "PASS" in l or "FAIL" in l]
                report.append("sample %s M%d %s():\n    %s" % (track, module, fn, "\n    ".join(summary)))
            else:
                rc, out, err = run_python(scratch, "sample_%s_m%d" % (track, module), text, xrplib)
                if rc != 0:
                    problems.append("sample %s M%d failed to load:\n%s" % (track, module, err[-800:]))
                else:
                    report.append("sample %s M%d loads" % (track, module))
            tests = SMOKE[module] + (SMOKE_CLASS_EXTRA.get(module, []) if track == "class" else [])
            rc, out, err = run_python(scratch, "smoke_%s_m%d" % (track, module), text,
                                      xrplib, RUNNER, tests)
            if rc != 0:
                problems.append("sample %s M%d smoke run crashed:\n%s" % (track, module, err[-1200:]))
            else:
                report.append("sample %s M%d smoke run: %d tests called without error" % (
                    track, module, len(tests)))
    # 6. function samples vs the base files
    if base_dir:
        models = build_models("function")
        for module in (4, 5, 6):
            base = os.path.join(base_dir, "robot_m%d_base.py" % module)
            if not os.path.exists(base):
                continue
            mine = [st.name for st in ast.parse(rendered[("function", last_lesson_of_module(models, module), True)]).body
                    if isinstance(st, (ast.FunctionDef, ast.ClassDef))]
            theirs = [st.name for st in ast.parse(open(base).read()).body
                      if isinstance(st, (ast.FunctionDef, ast.ClassDef))]
            common = [n for n in mine if n in theirs]
            order_ok = common == [n for n in theirs if n in mine]
            report.append("M%d vs %s: only in generated %r; only in base %r; shared order %s" % (
                module, os.path.basename(base), [n for n in mine if n not in theirs],
                [n for n in theirs if n not in mine], "same" if order_ok else "DIFFERS"))
    return report, problems


# ---------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--samples", metavar="DIR", help="also write the complete files here")
    ap.add_argument("--verify", action="store_true", help="run the checks (needs --xrplib, --scratch)")
    ap.add_argument("--xrplib", metavar="DIR", help="stub XRPLib package to run against")
    ap.add_argument("--scratch", metavar="DIR", help="scratch directory for the runs")
    ap.add_argument("--base-dir", metavar="DIR", help="dir with robot_m4_base.py etc. to compare")
    a = ap.parse_args()
    try:
        written, rendered = build_all(a.samples)
        print("wrote %d files" % len(written))
        if a.verify:
            if not (a.xrplib and a.scratch):
                ap.error("--verify needs --xrplib and --scratch")
            report, problems = verify(rendered, a.xrplib, a.scratch, a.base_dir)
            print("\n".join(report))
            if problems:
                print("\nPROBLEMS:")
                print("\n".join(problems))
                sys.exit(1)
            print("\nall checks passed")
    except BuildError as e:
        print("build_templates: " + str(e), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
