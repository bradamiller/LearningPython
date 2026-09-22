# XRP Python Curriculum — Web Site

A VEX STEM Labs-style web version of the XRP Python curriculum, built with
[Docusaurus](https://docusaurus.io/). The source curriculum this was converted
from — the teacher lesson plans, student worksheets, starter/solution code and
slide decks — lives in a separate repo, `IntoToPython`. This repo is the website
only. **All five modules are built — 46 lessons:**
Module 1 · Learning to Drive (kickoff lesson 0 + 12), Module 2 · Line Tracking (10), Module 3 · Grid
Driving (4), Module 4 · Manhattan Navigation (overview + 9), and Module 5 ·
Dijkstra's Algorithm (9). See `CLAUDE.md` for the full project spec, conventions,
and open items.

**Review status.** Building the lessons and *reviewing* them are separate jobs, and
only the first is finished. Module 1 has been through Brad's evaluation pass
lesson by lesson; Modules 2–5 were converted and have had only mechanical sweeps
(activity headings, trailing `stop()`), not a content read. Treat prose, code and
claims in Modules 2–5 as unverified until they get that pass.

## What the site provides

- **Sidebar + breadcrumb + prev/next navigation** across modules and lessons
- **Colored lesson header** band with duration / topic metadata
- **Teacher-mode toggle** — the floating switch (bottom-right). Off = student
  view; on = reveals gray Teacher Notes and the teacher banner. The choice is
  remembered in the browser.
- **Knowledge checks** — interactive multiple-choice / true-false questions with
  instant color-coded feedback and a "try again" reset
- **Printable knowledge checks** — every lesson links to a one-page handout of its
  questions (with a teacher answer key) that prints cleanly from the browser; the
  full list is at `/checks`. The questions still live in the lesson files, so the
  sheets can't drift out of date
- **Video and image placeholders** — labeled drop-in spots; add a `src` to embed
  the real media later
- **Real XRP Blockly block images** — Module 1 sample programs are built from the
  actual block graphics (from the XRP User Guide); Modules 2–5 are all Python
- **Generated pacing guide** at `/pacing` — per-module tables of time, activities
  and checks, with period-length and per-week selectors, plus the required
  materials list. Built from the lesson files on every build, so it can't drift
- **"How this course works"** (`docs/how-this-course-works.mdx`, first in the
  sidebar) — the course philosophy, structure, big ideas, the three places the
  course can be cut short, and the materials needed to deliver it

## Style conventions (enforced across lessons)

- **Lesson numbering is `module-lesson`:** "Lesson 1-7", "Lesson 5-3", in titles,
  sidebar labels and every cross-reference.
- **The middle header chip names the topic** — "Blockly Foundation", "while loops",
  "Python data", "Capstone". In Module 1 that chip also marks the arc: Blockly
  Foundation (1-1 to 1-5), Driving Challenges (1-6, 1-7), Transition to Python
  (1-8 to 1-12), with 1-0 a no-code kickoff discussion.
- **Function names carry from Blockly to Python unchanged:** `square(side_length)`,
  `triangle(side_length)`, `polygon(sides, side_length)`. The Blockly and Python
  versions of a function have the same name and the same parameters, in the same
  order — the names match the real XRP Code screenshots in the lessons. Effort is
  not a parameter; it stays at `0.5` in the blocks (it appears only as an optional
  challenge).
- **Real XRP block vocabulary:** Straight (cm, Effort 0–1), Turn (Deg, Effort),
  Sleep (seconds), Stop motors, Wait for button press — never "power %".
- **Every robot program starts with Wait for button press** (programs run the
  moment they upload).
- **No stop block at the end.** The robot stops its motors when the program
  ends, so programs never finish with **Stop motors** / `drivetrain.stop()`.
  Stopping is only shown *mid*-program, where the motors must quit while the
  program keeps running (e.g. stop, then turn).
- **Finishing vs. non-finishing blocks:** `Straight`/`Turn` finish the job and
  stop the motors themselves; `Set effort`/`Arcade` start the motors and leave
  them running. Lessons teach that distinction — and stop motion on a **sensor**
  (distance, line, encoder), not a timer. `Sleep` appears only as a pause or a
  clearly-flagged stand-in before sensors are introduced.
- **One tool throughout:** XRP Code in the browser — Blockly first, then
  MicroPython files in the same editor from Module 1 Lesson 8 on. No local
  install, Chrome or Edge only.
- **Experience before explanation (the cornerstone):** when a lesson introduces a
  new construct (a loop, a function, a parameter, an angle rule…), students build
  up to *needing* it through a short guided sequence — try something → run it →
  see the limitation → discover or search for the construct — before it is named
  or shown finished. Never open with the working solution. Lesson 2 is the model:
  drive straight → add a turn → make a square with what you have (eight blocks) →
  notice the repetition → find the Repeat block. Teacher notes say what to hold
  back and when to reveal.
- **Paper reasoning follows the experiment:** the "on paper first" step (angle
  table, pseudocode in English) comes *after* a quick hands-on attempt has
  motivated it — e.g. let the triangle fail at 90° before deriving 360 ÷ sides.
- **Objectives and headings don't spoil the discovery:** phrase them as outcomes
  ("find a shorter way to repeat…") rather than naming the construct up front.
- **3–4 learning objectives per lesson.**
- **Student work is `## Activity · <name>`** — that exact heading gets the red
  DO THIS badge and is what the pacing guide counts. Don't use "Part 3" or
  "Exercise".
- **Answers are hidden according to whether they're handed in.** Something a
  student checks *after trying* — a worked result, the rule behind a pattern —
  goes in `<Reveal>` (collapsed, and not printed when closed), always with a
  `hint` like "try it first". Anything handed in — filled tables, challenge
  solutions, project code, expected test values — goes in `<TeacherNote>`, which
  students can't open at all. Never answer a question in the paragraph below it.
- **Variables are `snake_case`; Capitalized means a class.** `rangefinder` is your
  variable, `Rangefinder` is the class it came from. Taught in Lesson 1-9.
- **Python is introduced with its own vocabulary lesson.** Lesson 1-9 covers what
  `=` actually does, naming, expressions and operator precedence before loops and
  functions use them.

## Finding what still needs work

Known problems are flagged in the lessons as `<Todo>` components, which render as
coloured boxes **on the dev server only**:

```bash
npm start                  # then use the "Show TODOs" switch, above Teacher mode
```

The switch shows a count for the current page and is on by default. Nothing about
them reaches a production build — the component renders null *and* a remark plugin
strips the nodes before compiling, so neither the markup nor the text is in the
deployed site or its JavaScript. That matters, because several of the notes say
where a lesson's answers are visible.

From the terminal:

```bash
npm run todos              # everything, grouped by category
npm run todos -- bug       # just one category
npm run todos -- --count   # tallies only
```

Categories, most urgent first: `bug` (wrong, and a student can hit it), `blocked`
(needs a decision or a robot first), `answers` (an answer is visible where it
shouldn't be), `convention` (drifts from a rule kept elsewhere), `media`
(placeholder art). `REVIEW-2026-09-21.md` has the full reasoning behind each one.

When you fix something, delete its `<Todo>` in the same commit. Never put one
inside a code fence — it becomes literal text in the code block.

## Gotchas worth knowing before you edit

- **`:::note` / `:::tip` / `:::caution` admonitions DO NOT RENDER** on this site —
  they appear as literal `:::` text in the page. Use `<Callout kind="warn|tip|note"
  title="...">` instead. This one has bitten the site more than once.
- **A bare `{...}` in prose breaks the build.** MDX parses it as a JSX expression,
  so a dict literal like `{(0,0): None}` must be inside backticks or a fenced code
  block.
- **Any component taking a `src` must run it through `useBaseUrl`**, or the asset
  404s if the site ever moves to a subpath.
- **Wide tables overflow.** The content column is about 570px, so a table with 3+
  prose columns is unreadable on a laptop and worse on a phone. Prefer code blocks
  or card grids.
- **SVG diagrams must be drawn for that same ~570px column.** A 900-wide viewBox
  renders its labels at about 9px. 680×300 is a good starting size.

## Run it locally

```bash
npm install     # first time only
npm start       # dev server with live reload at http://localhost:3000
```

To make a production build (static files in `build/`):

```bash
npm run build
npm run serve   # preview the build locally
```

## Where things live

- `docs/` — the curriculum content, one folder per module, one `.mdx` file per
  lesson. `docs/index.mdx` is the welcome page.
- `sidebars.js` — the curriculum outline shown in the left sidebar.
- `src/components/` — the custom pieces (TeacherNote, KnowledgeCheck, Video,
  Figure, LessonHeader, etc.).
- `src/theme/Root.js` — the teacher-mode toggle switch and its persistence.
- `src/theme/MDXComponents.js` — registers the components globally so lessons can
  use `<TeacherNote>`, `<KnowledgeCheck>`, etc. with no import lines.
- `src/css/custom.css` — all styling and the VEX-style color palette.
- `src/pages/` — the non-lesson pages: `/checks` (printable knowledge checks) and
  `/pacing` (the teacher pacing guide).
- `static/img/` and `static/videos/` — where graphics and videos go. Images are
  foldered by lesson (`img/lesson-01/`), except block art, which lives in
  `static/img/blocks/`.
- `scripts/` — the generators. `extract_checks.js` + `generate_quiz_pages.js` build
  the printable checks; `extract_pacing.js` builds the pacing data; both run
  automatically via `prestart`/`prebuild` and their output is gitignored, so the
  lesson files stay the single source of truth. `slice_c_blocks.py` cuts container
  block art; `make_call_block.py` generates Blockly function-call block images,
  which the block dictionary doesn't provide.

## Authoring a lesson

Each lesson is plain Markdown with a few custom tags. See
`docs/module-01-driving/lesson-01-meet-the-xrp.mdx` for a complete worked
example. The available tags:

```mdx
<LessonHeader eyebrow="Module 1 · Learning to Drive" title="Lesson 1-1 · Meet the XRP"
  meta={['50–60 min', 'Blockly Foundation', 'No experience needed']} />

<Objectives> ...bulleted list... </Objectives>

<QuizLink id="module-01-driving/lesson-01-meet-the-xrp" />   {/* = the file path */}

<TeacherNote title="Timing tip"> ...teacher-only guidance... </TeacherNote>

<Callout kind="warn" title="Watch out">   {/* ::: admonitions do NOT render */}
...the thing to watch out for...
</Callout>

<Reveal title="Check your answer" hint="try it first"> ...worked result... </Reveal>

<KnowledgeCheck
  question="..."
  options={[
    {text: 'A wrong answer'},
    {text: 'The right answer', correct: true},
  ]}
  explanation="Shown after answering." />

<Video placeholderLabel="Intro clip (1–2 min)" caption="..." />
<Video src="https://www.youtube.com/embed/XXXX" caption="..." />
<Video src="/videos/first-drive.mp4" mp4 caption="..." />

<Figure placeholderLabel="Labeled diagram of the XRP" caption="..." />
<Figure src="/img/lesson-01/parts.png" alt="..." caption="..." />

{/* Blockly: a composed program, or a real XRP Code screenshot (preferred) */}
<BlockProgram blocks={[{name: 'wait_for_button_press'}, {name: 'call_square'}]}
  caption="..." />
<BlockShot src="/img/blocks/programs/square-function.png" alt="..." caption="..." />

<CardGrid><InfoCard tag="Games" title="...">...</InfoCard></CardGrid>
```

Adding a lesson means four things: the `.mdx` file with `sidebar_position`, an
entry in `sidebars.js`, a duration chip in `meta` (the pacing guide reads it), and
a `<QuizLink id="...">` matching the file path. Inserting one mid-module also means
renumbering everything after it — file names, titles, `QuizLink` ids and prose
cross-references — plus re-pointing the previous lesson's "next lesson" preview.

## Deploying (GitHub Pages)

The site publishes itself. `.github/workflows/deploy.yml` builds on every push to
`main` and deploys the result to GitHub Pages. The live site is at

**https://learningpython.bradhouse.com/**

served from its own subdomain rather than a path, so `baseUrl` is plain `/`.

### How the domain is wired

- DNS: a CNAME record for `learningpython` under `bradhouse.com`, pointing at
  `bradamiller.github.io`.
- GitHub: the `LearningPython` repo's Settings → Pages → Custom domain is set to
  `learningpython.bradhouse.com`, and "Enforce HTTPS" once the certificate is
  issued.
- `static/CNAME` holds the same domain, so every deploy re-asserts it. If the
  domain ever changes, change it in **three** places: that file, `url` and
  `baseUrl` in `docusaurus.config.js`, and the repo setting.

Media paths in lessons are written site-absolute (`/img/...`, `/videos/...`), and
the `<Figure>`, `<Video>`, `<Block>` and `<BlockShot>` components run them through
Docusaurus's `useBaseUrl` — which is what let the site move between a subpath and
a domain root without touching a single lesson. New components that take a `src`
must do the same.

### Checking a build locally

```bash
npm run build
npm run serve     # http://localhost:3000
```

### A throwaway link, without deploying

`npm run build`, then drag the `build/` folder onto https://app.netlify.com/drop
for a temporary URL.
