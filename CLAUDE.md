# XRP Python Curriculum — Website Project

Context for anyone (human or AI) continuing work on this site. This is a
Docusaurus web version of Brad's XRP Python curriculum, styled like the
VEX STEM Labs lessons. **Read this first before making changes.**

---

## 1. What this project is

Turn the existing markdown curriculum (`../` — the `IntoToPython` repo) into a
browsable, VEX STEM Labs-style **website**: multi-page lessons with a sidebar,
prev/next navigation, embedded videos and graphics, interactive knowledge
checks, and a teacher-notes toggle.

- **Reference we're matching:** VEX AIR virtual-flight curriculum on
  education.vex.com (clean layout, teacher-notes switch, knowledge checks,
  media-rich lessons).
- **Audience:** high school students (no prior programming); teachers use the
  same pages with teacher-only notes toggled on.
- **Status (current):** **ALL FIVE MODULES ARE BUILT.** Module 1 (12: kickoff
  lesson-00-what-is-a-robot + lessons 1–11), Module 2 (10), Module 3 (4),
  Module 4 (10: overview + lessons 1–9), Module 5 (9: lessons 1–9) — 45 lessons live. Site builds clean (`npm run build`).
  `docs/module-01-driving/lesson-01-meet-the-xrp.mdx` is the canonical template.
- **Evaluation pass in progress (Brad, since 2026-09-15).** Conversion is done;
  the work now is Brad reading lessons and correcting them. **Module 1 lessons 0–6
  have been through it** (see §9 for every rule that came out of it): Lesson 0
  written and fully illustrated, Lesson 1 given the parts diagram + Bluetooth,
  Lesson 2 rebuilt for discovery learning, Lessons 3–5 renamed and re-shot,
  Lesson 6 rebuilt from Brad's motor deck and re-framed. **Lessons 7–11 and
  Modules 2–5 have NOT been reviewed yet** — expect the same kinds of correction
  there, and apply §9's rules pre-emptively when touching them.
- **Blockly vs. Python by module:** Module 1 is the Blockly→Python arc (lessons
  1–7 are Blockly; 8–11 are Python, though L8 and L9 each still show one block
  figure as the bridge). **Module 2 onward is
  all Python** — plain ```python code blocks, no block images. Handy: the
  block-screenshot workflow (§6) only matters for Module 1.

## 2. Source content (what we convert from)

The curriculum content lives in the **parent repo** (`../`, `IntoToPython`) — on
Brad's machine. Note that a cloud sandbox usually holds a copy of
`curriculum-site/` ONLY, so `../module-01-driving/` may not resolve there; read the
source through the device bridge (§13) when you need it:

- `../module-01-driving/` … `../module-05-dijkstra/`, each with:
  - `lessons/NN-*.md` — teacher lesson plans (objectives, key concepts, lesson flow, exercises, misconceptions, assessment)
  - `worksheets/NN-*.md` — student worksheets (great source for knowledge-check questions)
  - `code/starter/` and `code/solutions/` — Python/Blockly code
  - `slides/` — slide outlines + generated .pptx

**Content model (important):** we picked the **VEX model** — merge the teacher
lesson plan and the student worksheet into **one student-facing lesson page**,
and put teacher-only material (timing, setup tips, differentiation, assessment)
into `<TeacherNote>` boxes that only show when teacher mode is on. See
`docs/module-01-driving/lesson-01-meet-the-xrp.mdx` for the worked example —
copy its structure for new lessons.

## 3. Tech stack & layout

Docusaurus (classic preset, JavaScript). Docs are served at the site root
(`routeBasePath: '/'`).

```
curriculum-site/
├── docs/
│   ├── index.mdx                         # welcome / landing page (slug: /)
│   ├── module-01-driving/                # lesson-00 kickoff + 11 lessons (Blockly→Python) — DONE
│   │   └── lesson-01-meet-the-xrp.mdx    # THE TEMPLATE lesson — copy its structure
│   ├── module-02-line-tracking/          # 10 lessons (all Python) — DONE
│   ├── module-03-grid-driving/           # 4 lessons — DONE
│   ├── module-04-manhattan/              # lesson-00-overview + lessons 1–9 — DONE
│   └── module-05-dijkstra/               # lessons 1–9 (no overview) — DONE
├── src/
│   ├── components/
│   │   ├── Lesson.js      # LessonHeader, Objectives, TeacherBanner, CardGrid, InfoCard, Decide
│   │   ├── TeacherNote.js # gray teacher-only box
│   │   ├── KnowledgeCheck.js # interactive multiple-choice quiz
│   │   ├── Media.js       # Video, Figure (real src OR labeled placeholder)
│   │   ├── Blocks.js      # Block (inline), BlockProgram (composed), BlockShot (real screenshot)
│   │   └── cblocks.json   # GENERATED geometry for C-shaped blocks (see §6) — don't hand-edit
│   ├── theme/
│   │   ├── Root.js        # the floating Teacher-mode toggle + persistence
│   │   └── MDXComponents.js # registers all components globally (no imports needed in .mdx)
│   └── css/custom.css     # ALL styling + brand color tokens (top of file)
├── scripts/
│   └── slice_c_blocks.py  # slices container block art into bar/spine/foot (§6)
├── static/
│   ├── img/
│   │   ├── logo.svg
│   │   ├── blocks/        # 91 real XRP Blockly block PNGs
│   │   │   ├── c/         # GENERATED slices of the C-shaped blocks (§6)
│   │   │   └── programs/  # real XRP Code screenshots of whole programs (§6)
│   │   ├── lesson-01/     # Lesson 0 robot gallery (8 JPGs) + xrp-parts.jpg (Lesson 1)
│   │   └── lesson-06/     # motor-motion stills + the two effort diagrams (§12)
│   ├── videos/            # gort.mp4, ballshooter.mp4, motors-*.mp4 (§12)
│   └── .nojekyll          # already there for GitHub Pages (§8)
├── sidebars.js            # curriculum outline (modules → lessons)
├── docusaurus.config.js   # site config, navbar, Montserrat font, footer
├── netlify.toml           # deploy config (see §8)
└── README.md              # run + deploy instructions
```

`.gitignore` excludes `static/videos/*.mov` — only transcoded MP4s get committed
(§12). Not listed above: `package.json`/`package-lock.json`, an empty
`src/pages/`, and leftover Docusaurus scaffold art in `static/img/`
(`docusaurus*.{png,jpg}`, `undraw_*.svg`). `img/favicon.ico` is also there and IS
referenced by `docusaurus.config.js`, so leave that one alone. Everything under `static/img/blocks/c/` and `src/components/cblocks.json` is
generated; re-run `python3 scripts/slice_c_blocks.py` instead of editing by hand.

MDX gotcha: don't put escaped double-quotes inside a JSX attribute string. For a
`KnowledgeCheck` question that must contain quotes (e.g. `print("hi")`), use a JS
expression: `question={'... print("hi") ...'}` — not `question="... \"hi\" ..."`.

## 4. Design system (XRP / Experiential Robotics brand)

Matched to **experiential.bot** (the official Experiential Robotics site). All
values are CSS tokens at the top of `src/css/custom.css` — change them there,
not inline.

| Role | Color |
|------|-------|
| Brand red — primary CTA, accents, links, knowledge-check badge, teacher toggle | `#D1182C` |
| Steel blue — navigation, lesson-header gradient start, section headings | `#22527B` |
| Deep navy — lesson-header gradient end | `#142D50` / `#0F2543` |
| Dark slate — body text, headings | `#343A40` |
| Light gray — section backgrounds | `#E9ECEF` / `#F8F9FA` |
| Teacher-note background / border | `--xrp-teacher-bg: #f1f3f5` / `--xrp-teacher-border: #adb5bd` |
| Success green (knowledge-check correct) | `#2E7D32` |

- **Font:** Montserrat (loaded via Google Fonts in `docusaurus.config.js`).
- **Lesson header:** blue→navy gradient band with red accent dots.
- **Shape language:** rounded corners (10–14px), generous whitespace, like VEX.
- Dark mode is supported (Docusaurus theme toggle) with a lighter blue primary.

## 5. Custom components (use these in lesson `.mdx`)

All are registered globally — **no import lines needed** in `.mdx` files.

```mdx
<LessonHeader
  eyebrow="Module 1 · Learning to Drive"
  title="Lesson 1 · Meet the XRP"
  meta={['50–60 min', 'Phase A · Blockly Foundation', 'No experience needed']} />

<TeacherBanner>Shown only in teacher mode — the "you're seeing teacher view" note.</TeacherBanner>

<Objectives>
- Bulleted learning objectives
</Objectives>

<TeacherNote title="Timing tip">
Gray box, hidden unless teacher mode is on. Teacher-only guidance.
</TeacherNote>

<KnowledgeCheck
  question="..."
  options={[
    {text: 'A wrong answer'},
    {text: 'The correct answer', correct: true, feedback: 'Optional nudge, shown when they answer WRONG'},
    {text: 'Another wrong answer'},
  ]}
  explanation="Shown after answering. Works for true/false too (just two options)." />
{/* NB: KnowledgeCheck reads `feedback` only from the CORRECT option — putting it
    on a wrong option does nothing. `title` is optional on TeacherNote (default
    "Teacher Note") and Objectives (default "Learning Objectives"). */}

<Video placeholderLabel="Intro clip (1–2 min)" caption="..." />   {/* placeholder */}
<Video src="https://www.youtube.com/embed/XXXX" caption="..." />  {/* YouTube/Vimeo */}
<Video src="/videos/first-drive.mp4" mp4 caption="..." />         {/* local mp4 */}

<Figure placeholderLabel="Labeled diagram of the XRP" caption="..." />  {/* placeholder */}
<Figure src="/img/lesson-01/xrp-parts.jpg" alt="..." caption="..." />   {/* real image */}

<CardGrid>
  <InfoCard tag="Warehouses" title="Delivery robots">Real-world connection card.</InfoCard>
</CardGrid>

{/* A per-item fill-in: Yes/No buttons + a "Why?" line. Lesson 0 uses one under
    each gallery picture so a class can answer on the projector without
    scrolling back to a table. State is in-memory only — a reload clears it. */}
<Decide device="Camera drone" />
<Decide device="Mars rover" prompt="Robot?" why="Why? — what makes it one?" />
```

**Teacher mode** (Root.js): a floating switch (bottom-right) sets
`html[data-teacher='on']` and saves to `localStorage['xrp-teacher-mode']`.
`.teacherNote` and `.teacherBanner` are `display:none` by default and revealed
by that attribute (pure CSS). Default = student view.

## 6. Blockly blocks (real block images)

`static/img/blocks/` holds **all 91 real XRP Blockly block images**, taken from
the XRP User Guide's Blockly Dictionary (repo `Open-STEM/XRPUsersGuide`,
`course/blocks/*.png`). They were post-processed: the dark `#1F1F1F` workspace
background was flood-filled to transparent and each image auto-cropped tight, so
they float on a light canvas and interlock when stacked.

Render them with:

```mdx
The <Block name="straight" /> block drives in a straight line.   {/* inline */}

<BlockProgram
  blocks={[
    {name: 'straight', note: 'forward — cm: 20, Effort: 0.5'},
    {name: 'straight', note: 'back — change cm to -20'},
  ]}
  caption="A stacked program, like the real workspace." />
```

**Container / C-shaped blocks (Repeat, If, function def):** give the block a
`children` array and the component draws a real, stretching C — not a bracket.
`scripts/slice_c_blocks.py` cuts each container image in `static/img/blocks/` into
four pieces in `static/img/blocks/c/`: `<name>-bar.png` (top bar + inner notch),
`<name>-do.png` (the spine slice carrying the "do" label), `<name>-fill.png` (a 1px
tileable spine slice) and `<name>-foot.png` (closing lip + bottom tab), plus the
geometry manifest `src/components/cblocks.json`. `CBlock` in `Blocks.js` stacks
bar → spine (do slice on top, fill tiled beneath, stretched by flexbox to the
children's height) → foot, so the container grows around its contents exactly like
XRP Code. Detection is automatic (a narrow left-aligned band with a wider bar above
and foot below), so re-running the script picks up any new container art:

```bash
python3 scripts/slice_c_blocks.py     # after adding/replacing block images
```

Nest `children` inside `children` for a function containing a loop — L3's
`square` renders as a purple function def wrapping a green repeat
(`lesson-03-introduction-to-functions.mdx`). (Do NOT use
a flat list with an `indent` field, and don't reintroduce the old CSS bracket; it
is kept only as a fallback for a container with no sliced art.)

```mdx
<BlockProgram
  blocks={[
    {name: 'wait_for_button_press'},
    {name: 'repeat', note: 'repeat 4 times', children: [
      {name: 'straight', note: 'cm: 30'},
      {name: 'turn', note: 'Deg: 90'},
    ]},
  ]}
  caption="The Straight and Turn blocks sit inside the Repeat." />
```

**Real XRP block vocabulary (use these exact terms — NOT invented syntax):**

- **Straight** — `cm:` (distance; negative = backward), `Effort:` (0–1, not "power %"). Image: `straight.png`
- **Turn** — `Deg:` (angle), `Effort:` (0–1). Image: `turn.png`
- **Sleep** — seconds. Image: `sleep.png`
- **Stop motors**. Image: `stop_motors.png`
- Many more in `static/img/blocks/` (set_effort, arcade, LED_on, if_do, repeat, count, print1, variables, functions, sensors: sonar/reflectance/gyro, etc.) — filenames match the dictionary.

**Preferred for whole programs — real screenshots (`<BlockShot>`):** the composed
`BlockProgram` is an approximation (default field values, bracket-drawn nesting).
When Brad supplies a real screenshot of a program from XRP Code, use it instead —
it shows correct values and exact nesting. Save the PNG under
`static/img/blocks/programs/` and reference it:

```mdx
<BlockShot src="/img/blocks/programs/square-function.png"
  alt="square(side_length) function with a call passing 35"
  maxWidth={520}                        {/* optional; default 480 */}
  caption="The square(side_length) function and a call." />
```

XRP Code screenshots have a dark (#222) workspace background; whiten it before
use with an edge flood-fill (preserves the dark digits inside input fields):

```python
from PIL import Image, ImageDraw
im = Image.open('shot.png').convert('RGB'); w,h = im.size
for s in [(0,0),(w-1,0),(0,h-1),(w-1,h-1),(w//2,0),(w//2,h-1),(0,h//2),(w-1,h//2)]:
    ImageDraw.floodfill(im, s, (255,255,255), thresh=60)
im.save('out.png')
```

Real screenshots so far: `square-function.png` (Lesson 4),
`repeat-square.png` (Lesson 2 Part 4) and `polygon-function.png` (Lesson 5 Part 1
— `polygon (sides, side_length)` with `360 ÷ sides` in the Turn slot), the last two
from Brad on 2026-09-17. **Heads-up on `repeat-square.png`:** it shows a Repeat block at
its default count of **10**, not the 4 a square needs, and it has no
`wait_for_button_press` on top; the caption covers both ("a new Repeat block starts
at 10, so change the count to 4"). Swap it if Brad re-shoots with 4.

**Composed `BlockProgram`s still in use — L1, L2, L3, L6, L7, L8, L9** (L2 has one
*and* a real screenshot: the eight-block square is composed, the Repeat reveal is
Brad's shot). Those are the candidates for replacement as more screenshots arrive.

**Composed-block limitation:** `BlockProgram` images show fixed field values
(e.g. `cm: 20`); use the `note` prop for a different intended value.

## 7. Authoring a new lesson (the repeatable process)

1. Read the source `lessons/NN-*.md` and `worksheets/NN-*.md` in the parent repo.
2. Create `docs/module-XX-name/lesson-NN-slug.mdx` with frontmatter:
   ```
   ---
   title: "Lesson N · Title"
   sidebar_label: "N · Short Title"
   sidebar_position: N
   ---
   ```
3. Follow the Lesson 1 structure: `LessonHeader` → `TeacherBanner` → intro →
   `Objectives` → content sections (with `Video`/`Figure` placeholders and real
   `BlockProgram`s for any code) → `KnowledgeCheck`s built from the worksheet
   questions → `TeacherNote`s for teacher-only material → real-world `CardGrid`
   → wrap-up → Resources.
4. Add the page to `sidebars.js` (under its module category — all 45 lessons are
   listed explicitly there now; no "Coming soon" placeholders remain).
5. Use **real block vocabulary** (§6) — Straight/Turn/Effort/Sleep, not power %.
6. `npm start` and eyeball it in both student and teacher mode.

## 8. Build, run, deploy

```bash
npm install     # first time
npm start       # dev server, live reload, http://localhost:3000
npm run build   # static site → build/
npm run serve   # preview the build
```

**Deploy: Netlify.** `netlify.toml` is set up. Two options:
- **Instant link:** `npm run build`, then drag `build/` onto app.netlify.com/drop.
- **Auto-deploy:** push this folder to GitHub, then in Netlify import the repo
  and set **Base directory = `curriculum-site`** (build command + publish path
  come from `netlify.toml`). Served at domain root, so `baseUrl` stays `/`.

**Switching to GitHub Pages (Brad asked 2026-09-16 — not done, recipe only).**
Three steps, because the site lives in a subfolder of the repo:
1. `docusaurus.config.js`: `baseUrl: '/'` → `baseUrl: '/IntoToPython/'` (project
   sites serve from a subpath; without this every `/img/...` and `/videos/...`
   path 404s). `url` and `organizationName`/`projectName` are already correct.
   Site would live at `https://bradamiller.github.io/IntoToPython/`.
2. Add `.github/workflows/deploy.yml` at the REPO root that checks out, runs
   `npm ci && npm run build` with `working-directory: curriculum-site`, uploads
   `curriculum-site/build` via `actions/upload-pages-artifact@v3`, and deploys
   with `actions/deploy-pages@v4` (permissions: `contents: read`, `pages: write`,
   `id-token: write`).
3. Repo → Settings → Pages → Source: **GitHub Actions**.

Caveats: the repo must be public for Pages on a free personal account; a custom
domain (e.g. `curriculum.experiential.bot`) would instead keep `baseUrl: '/'`,
set `url` to the domain and add a `CNAME` file in `static/`. Netlify and Pages
can't both be served correctly from one committed `baseUrl` — drive it from an
env var if both must run during a transition. (Google Cloud: Firebase Hosting
with public dir `curriculum-site/build` is the simple option; no advantage over
Pages for a static site.)

## 9. Decisions already made (don't re-litigate without reason)

- **Framework:** Docusaurus (Brad had already started one; best fit for the interactive components).
- **Content model:** merge lesson plan + worksheet into one student page; teacher content in toggle-able gray boxes.
- **Branding:** XRP/Experiential palette + Montserrat (see §4), tokens in custom.css.
- **Blocks:** real images from the XRP User Guide, transparent + cropped; "Effort" not "power %". Prefer real `<BlockShot>` screenshots from Brad when available (§6).
- **Videos/graphics:** Brad produces them and hands them off; lessons use labeled placeholders until then.

**Open / unresolved (flag for Brad's evaluation pass):**
- **MODULE 1 FUNCTION NAMING — current, settled 2026-09-17.** One set of names in
  **both** languages: **`square(side_length)`**, **`triangle(side_length)`**,
  **`polygon(sides, side_length)`** — bare names (no `draw_` prefix), `sides`
  first, and **no `effort` parameter on `polygon`** in Blockly or Python. Effort
  stays `0.5` in the blocks and appears only as an optional challenge (L4 Part 3,
  L10 Part 2 prose). This is what the lessons and Brad's real XRP Code screenshots
  now agree on; `grep -rn "draw_square\|draw_polygon\|draw square\|draw polygon" docs/`
  should stay empty (don't grep bare `size` — it's ordinary English all over the
  lessons). *(Caveat: only `square` and `polygon` exist in both languages — no Python
  lesson defines `triangle`.)*
  - *History, so nobody "restores" it:* the 2026-09-15 review had standardized on
    `draw_square(size)` / `draw_polygon(sides, size, effort)`. Brad's screenshots
    then showed `square(side_length)` and `polygon(sides, side_length)`, and on
    2026-09-17 he chose to follow the screenshots rather than re-shoot, and to
    align the Python lessons exactly. **The site is now ahead of Brad's SOURCE
    repo**, which still says `draw_square(size)` in
    `../module-01-driving/lessons/04-*.md` and `draw_square(distance)` in
    `../module-01-driving/code/solutions/lesson-10-functions.py`. Open question:
    whether to bring the source markdown/slides/solutions in line.
- **Block screenshots — done so far / still wanted:** real XRP Code shots are in
  for **L2** (`repeat-square.png`), **L4** (`square-function.png`) and **L5**
  (`polygon-function.png`). Composed `BlockProgram`s still stand in for
  **L1, L2, L3, L6, L7, L8 and L9** — whiten (§6) and drop into
  `static/img/blocks/programs/` as Brad supplies them. Two things a new shot
  should have: the program starts with `wait_for_button_press`, and no trailing
  `stop_motors`. (`repeat-square.png` predates that and is captioned around it.)
- **Lesson 0 · What Is a Robot? (added 2026-09-15):** a no-code discussion kickoff
  built from Brad's *WhatIsARobot.pdf* slide deck (WPI). Gallery of "is this a
  robot?" devices with answers hidden in TeacherNotes → 1979 RIA definition →
  WPI sense/think/act → where the XRP fits. Numbered 0 (not renumbered to 1) so
  the site stays aligned with the source repo's 01–11 lesson/slide/worksheet
  numbering; matches Module 4's lesson-00 precedent. No matching lesson-plan .md
  exists in the source repo's `module-01-driving/lessons/` yet — the site page is
  the only version.
  **Media is DONE (2026-09-15/17):** Part 1 plays `/videos/gort.mp4`, the Part 2
  gallery shows all eight devices from `/img/lesson-01/` (RadioControlledAirplane,
  Drone, ManualVacuum, RobotVacuum, RedCar, ClothesFolding, MarsRover,
  WashingMachine) and Part 4 plays `/videos/ballshooter.mp4`.
  **Discussion design — do not re-scaffold (Brad, 2026-09-15):** students must
  reach "sensors + acting on what was sensed" THEMSELVES. The student page gives
  only a neutral "Think about it" prompt per picture (most ask what happens if the
  person walks away); every answer lives in a `TeacherNote`. An earlier draft with
  Q1–Q4 prompts and a multi-column table was rejected for giving it away.
  **Answers are recorded per picture, not in a table (Brad, 2026-09-16):** each
  image is followed by `<Decide device="…" />` — Yes/No buttons plus one "Why?"
  line — so a class answers in place instead of scrolling to a table during a
  presentation. Keep that pattern if more devices are added.
- **EXPERIENTIAL LEARNING IS THE CORNERSTONE (Brad, 2026-09-15).** When a lesson
  introduces a new construct, students must build up to *needing* it (try → run →
  hit the limitation → discover/search for the construct) before it's named or the
  finished code is shown. Lesson 2 was rebuilt as the model (straight → turn →
  eight-block square → find Repeat; triangle fails at 90° → derive 360 ÷ sides).
  Lesson 1's square "challenge" no longer gives the recipe. Objectives/headings
  must not spoil the construct. Paper reasoning comes *after* the motivating
  attempt, not before all coding. **Apply this pattern when revisiting Lessons 3
  (functions), 4 (parameters), 5 (polygon), 9–10 (Python loops/functions).**
- **Module 1 style rules applied in the 2026-09-15 review** (keep enforcing):
  Phase chips A (1–5) / B · Driving Challenges (6–7) / C (8–11); every program
  starts with Wait for button press / `board.wait_for_button()` (programs auto-run
  on upload) — **⚠️ not yet true everywhere: none of the 11 Python examples in
  L8–L11 call `board.wait_for_button()`, and five of the nine composed Blockly
  programs omit the block (L3 ×2, L7, L8, L9 — L3's first one is the deliberate
  copy-paste "before" figure, so judge it on its own). Module 2 does it right (9
  of 10 lessons). Fix when those lessons get their review pass;** Python editor is
  **VS Code + MicroPython extension** (per Brad's source), Blockly is XRP Code;
  student-facing "on paper first" step in L2 and "say it in English first" in L3;
  3–4 objectives per lesson. **Connecting (L1 Part 2, 2026-09-17):** XRP Code
  connects over **USB cable or Bluetooth** — every robot needs one USB connection
  first (that's how XRP Code installs/updates its MicroPython), after which it
  pairs wirelessly by its per-robot ID shown under the RUN button. Bluetooth needs
  a Chromium browser (Chrome/Edge); low battery kills Bluetooth first; a running
  program can block pairing (press reset). Don't describe uploading as USB-only.
  **No trailing stop (Brad, 2026-09-17):** motors stop automatically when a
  program ends, so NO program ends with **Stop motors** / `drivetrain.stop()`.
  Keep stops only where they're functional mid-program (stop → turn; a
  `track_until_cross()` that ends its motion before returning).
- **FINISHING vs. NON-FINISHING BLOCKS — and don't teach timed driving (Brad,
  2026-09-17).** The distinction students need: `Straight`/`Turn` **finish** —
  they do the job and stop the motors themselves; `Set effort`/`Arcade` just
  **start** the motors, which run until something stops them (a Stop motors
  block, another Set effort, or the program ending). **Do NOT build a section
  around `Sleep`.** Timed driving teaches the wrong habit and gives different
  results with battery level, surface and load; students should almost always
  stop on a **sensor** (rangefinder distance, reflectance seeing the line,
  encoder count) instead. Sleep is fine as an occasional pause or as an
  explicitly-flagged stand-in before sensors exist — never a section heading or a
  knowledge-check answer that endorses it. **Brad went further on 2026-09-17: no
  Sleep at all outside L6.** L1 no longer lists Sleep among the starter blocks
  (its Part 5 "add a pause" step is now a change-the-effort experiment) and L3 no
  longer suggests a Sleep between calls. The only Sleeps left in Module 1 are the
  two flagged stand-ins in L6, where `Set effort` needs something to hold the
  program open, plus `time.sleep(1)` between shapes in L11's project skeleton. L6 Part 2 ("Blocks that finish vs. blocks that don't") is the model:
  measure the same timed program on two surfaces, then point at Module 2.
- **🚨 THE SITE IS NOW BEHIND THE SOURCE: classes became OPTIONAL (merged
  2026-09-18, branch `separate-classes`, 170 files).** Brad reshaped the source
  curriculum so **functions are the spine everywhere and classes are an "Optional
  Extension" at the end of selected lessons** — a course can be taught entirely
  without `class`/`self` and still reach the same capstones. Read
  `../teacher-guide/classes-optional.md` first; it has the full lesson-by-lesson
  table. The merge touched NO files under `curriculum-site/`, so **every Module
  2/4/5 page on the site still teaches the old class-first version.** The gap, by
  page:
  - **M2:** source renamed `08-introduction-to-classes` → `08-sensor-functions`
    and `09-object-composition` → `09-line-tracking-functions`; the site still has
    `lesson-08-introduction-to-classes.mdx` / `lesson-09-object-composition.mdx`
    (file names, sidebar labels and content all class-first). L10 combines them.
  - **M4:** L5 (`Manhattan` class) and L8 (`Navigator` class) are now
    `compute_manhattan_path` + `desired_heading`/`turn_to`/`drive_path` functions,
    with the class as the extension; L9's main program has a functions version
    that skips the `manhattan.position = navigator.position` sync step.
  - **M5:** L4–L5 build `build_dijkstra_graph`/`compute_dijkstra_path` as
    functions; L6's swap is a `compute_path(algorithm, ...)` dispatch function in
    the functions track, with true polymorphism as the extension; L7–L9 call the
    functions directly.
  - Site pages need the same primary/extension split, and probably a visual
    treatment for "Optional Extension" (a collapsible, or reuse of the
    `TeacherNote` pattern). **Ask Brad how he wants extensions shown before
    rewriting.** Note this also resolves how M4/M5 relate — see the
    `compute_path` bullet below, which the functions-first shape may settle on its
    own.
  - Also per that guide, still stale in the SOURCE (not the site): M2 L8–L9 slide
    outlines + `.pptx`, the root `generate_pptx_lesson*.py` scripts, and the
    `.html`/`.pdf` worksheet renders for M4–M5.
- **⚠️ Cross-module `compute_path` return-shape mismatch (M4 vs M5).** This is a
  real inconsistency in Brad's SOURCE curriculum, carried faithfully into the site:
  - **Module 4 `Manhattan`:** returned path **excludes** the start; `steps = len(path)`;
    same position → `[]`.
  - **Module 5 `Dijkstra`:** returned path **includes** the start (per M5 lessons
    4/5/9 reconstruction: `path[0] == self.position`); `steps = len(path) - 1`;
    same position → `[(start)]`.
  The M5 Lesson 6 "two-line swap into Navigator" narrative assumes drop-in
  compatibility, but the Module 4 `Navigator.drive_path` iterates the path driving
  to each node — so a Dijkstra path that includes the current position would try to
  "drive to" where it already is on the first step. **Decide during eval:** either
  make Dijkstra exclude the start (match Manhattan), or adjust `drive_path` to skip
  `path[0]`. Not changed yet — faithful conversion + flagged.
- **Module 5 source constructor drift (already normalized on the site).** M5 source
  lessons 4/5/9 use `Dijkstra(start, blocked)` + `compute_path(destination)` (matches
  the real Manhattan/Navigator interface); source lessons 6/7/8 drift to
  `Dijkstra(rows, cols, blocked)` + `compute_path(start, dest)`. The site standardizes
  ALL M5 lessons on the 4/5/9 signature (`Dijkstra(start, blocked)` /
  `compute_path(destination)`), incl. the reactive-recompute pattern in L7/L8
  (`Dijkstra(current_pos, blocked_list)`). If Brad prefers the other signature, it's
  a global find/replace across M5.
- **Module 4 uses a 10-page structure** (lesson-00-overview + 1–9) because its source
  had `00-module-overview.md`. **Module 5 has no overview page** (source starts at 01) —
  consider whether M5 wants a parallel "big picture" overview for consistency.

## 10. Where the evaluation pass has reached

What Brad has corrected so far, lesson by lesson — useful both as history and as a
signal of what he cares about when you touch an unreviewed lesson.

| Lesson | What changed |
|---|---|
| **M1 L0** | Written from *WhatIsARobot.pdf*; all media wired; scaffolding stripped twice (see §9); table → per-picture `<Decide>` boxes |
| **M1 L1** | Real `xrp-parts.jpg` diagram; **Bluetooth** added beside USB; square challenge de-spoiled (hands off to L2); trailing `stop_motors` removed; Sleep dropped from the block list and from Part 5 |
| **M1 L2** | Rebuilt as the discovery model (straight → turn → 8-block square → find Repeat; triangle fails before `360 ÷ sides`); real Repeat screenshot |
| **M1 L3** | Function renamed `square`; Sleep-between-calls suggestion removed |
| **M1 L4** | Parameter renamed `side_length` to match the screenshot; function renamed `square` |
| **M1 L5** | Rebuilt from Brad's screenshot: `polygon (sides, side_length)`, no effort parameter |
| **M1 L6** | Part 1 built from Brad's Keynote motor deck (stills + clips); "effort ≠ speed" section added; Part 2 re-framed to finishing vs. non-finishing blocks, timed driving demoted |
| **M1 L10–11** | Python aligned to the Blockly names/params (`square`, `polygon(sides, side_length)`) — naming only; these lessons have NOT had a full review (their examples still skip `board.wait_for_button()`) |
| **M2 L2/L7/L10** | Trailing `drivetrain.stop()` removed from end-of-program examples |
| **Not yet reviewed** | **M1 L7–L11** (L10–11 got the rename only) **and all of Modules 2–5** (beyond the stop() sweep) |
| **M2/M4/M5 site pages** | ⚠️ Now BEHIND the source — the `separate-classes` merge (2026-09-18) made classes optional in the source only. See §9. |

## 11. Good next steps

- **Push.** Commits are made here but **`git push` cannot run from the sandbox**
  (no GitHub credentials) — Brad pushes with `git push origin main` or VS Code
  Sync. Always tell him how many commits are waiting.
- **Continue the evaluation pass** with M1 L7–L11, then Modules 2–5 — applying §9's
  rules (experiential first, no trailing stop, sensor-based stopping, naming)
  rather than waiting for Brad to catch each one.
- **Decide the M4/M5 `compute_path` return-shape mismatch** (§9) — the one known
  correctness bug in the converted material.
- **Source-repo sync (open question).** The site is now ahead of
  `../module-01-driving/` on naming (`square(side_length)` vs the source's
  `draw_square(size)`), on Lesson 0 (no source lesson plan exists), and on the
  stop-motors and Bluetooth guidance. Ask Brad whether to bring the source
  markdown/slides/solutions in line.
- **Media still wanted:** real block screenshots for the lessons still on composed
  art — **L1, L3, L6, L7, L8, L9** (§6; L2 is half-done); an XRP-built
  re-shoot of the Lesson 6 motor photos, which currently show a VEX-style robot
  (§12); an official `logo.svg` if there is one; and a social/OG card image — the
  config used to point at an `img/social-card.png` that never existed, so that
  reference has been removed rather than left broken.
- Deploy: Netlify as configured, or switch to GitHub Pages with the recipe in §8.

**Per-module pattern reminder:** each module is a `docs/module-XX-name/` folder of
`lesson-NN-slug.mdx` files, added to its category in `sidebars.js`. Modules 2+ are all
Python. **MDX gotcha:** a bare `{...}` in prose (e.g. a dict literal like
`{(0,0): None}`) is parsed as a JSX expression and breaks the build — wrap it in
backticks (inline code) or put it in a fenced code block.

**To continue in a new session, a prompt like this is enough:**
"Continue the XRP curriculum site in `curriculum-site/`. Read CLAUDE.md." — all five
modules are built; work is now evaluation/refinement, not new conversion.

## 12. Videos & images (adding real media)

Media lives under `static/` and is referenced from the site root (drop the word
`static`, keep the leading slash): `static/img/lesson-06/x.jpg` → `/img/lesson-06/x.jpg`;
`static/videos/x.mp4` → `/videos/x.mp4`. Images are foldered **by lesson**
(`img/lesson-01/`, `img/lesson-06/`), not by module. Swap a placeholder by replacing
`placeholderLabel` with `src` (+ `alt` for images; `mp4` flag for local video):

```mdx
<Figure src="/img/lesson-01/MarsRover.jpg" alt="..." caption="..." />
<Video src="/videos/gort.mp4" mp4 caption="..." />
<Video src="https://www.youtube.com/embed/VIDEO_ID" caption="..." />   {/* embed URL, not watch URL */}
```

**Local video must be transcoded first.** Raw screen recordings (.mov, 60 fps,
10+ Mbps) are 100+ MB — GitHub rejects files over 100 MB and Netlify deploys
bloat. Recipe (ffmpeg is on Brad's Mac; ~10 MB per 90 s):

```bash
ffmpeg -i Input.mov -vf "scale=960:-2,fps=30" -c:v libx264 -preset fast -crf 26 \
  -pix_fmt yuv420p -movflags +faststart -c:a aac -b:a 96k output.mp4
```

`.gitignore` excludes `static/videos/*.mov` so originals never get committed.
Long or many videos → YouTube (unlisted) instead of local files. First real
video: `static/videos/gort.mp4` in Module 1 Lesson 0, Part 1.

**Keynote decks → lesson media.** Brad's Keynote "Publish to HTML" exports (an
`index.html` + `assets/<UUID>/` per slide) hide their content: each slide is a
multi-page PDF of *layers* (arrows and labels are vector overlays, NOT baked into
the photos — `pdfimages` returns the bare photo), and embedded clips are HEVC
`.mov`, which Chrome/Firefox won't play. What works:
- `assets/header.json` → `slideList` gives the true slide order.
- Flat slide images: serve the export (`npx serve`) and drive the player with
  Playwright (ArrowRight advances one *build*, not one slide; dedupe screenshots
  by hash). `deviceScaleFactor: 3` gives crisp vector text.
- Photo-only crops: `pdftoppm -r 150` the question slide, then crop the photo box.
- Videos: `ffmpeg -i in.mov -an -vf scale=960:-2 -c:v libx264 -crf 27 -movflags
  +faststart out.mp4` (HEVC→H.264; ~0.2–0.8 MB for 4–10 s).
First use: the motion deck → Module 1 Lesson 6 Part 1 (`static/img/lesson-06/`,
`static/videos/motors-*.mp4`).

**Heads-up:** the robot in those Lesson 6 photos/clips is a **VEX-style build,
not an XRP** — captions say "the robot" / "a two-motor robot" rather than naming
the XRP. Reshoot with an XRP if you want it on-brand.

**HEIF/HEIC from Brad's Mac won't render in a browser** — convert to JPG first.
On his machine ImageMagick handles it (`magick in.heif -background white -flatten
out.jpg`); in this sandbox install the decoder first:

```bash
pip install pillow-heif --break-system-packages
python3 -c "
import pillow_heif; pillow_heif.register_heif_opener()
from PIL import Image
im = Image.open('XRPParts.heif').convert('RGBA')
bg = Image.new('RGB', im.size, 'white'); bg.paste(im, mask=im.split()[3])
bg.save('static/img/lesson-01/xrp-parts.jpg', quality=90)"
```

That is where `xrp-parts.jpg` (Lesson 1's labeled kit diagram) came from.

## 13. Getting changes from this sandbox into Brad's repo

The cloud workspace is NOT his machine. The loop that works:

1. Edit and `npm run build` in the cloud copy (`/home/claude/xrp-curriculum`).
2. Eyeball it: serve `build/` (`npx serve -l 3055 build`) and screenshot with the
   bundled Playwright — `require('<site>/node_modules/playwright-core')`,
   `executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'`. Serve
   and shoot in ONE bash call. (That Chromium can't decode H.264, so local MP4s
   show `readyState 0` in a screenshot — expected, not a bug.)
3. `tar -czf /mnt/user-data/outputs/<name>.tgz <changed files>` → `SendUserFile` →
   `device_commit_files` into `…/IntoToPython/curriculum-site/` → on the device,
   `tar --overwrite -xzf <name>.tgz && rm -f <name>.tgz` (plain `tar` refuses to
   overwrite; the FUSE mount needs `--overwrite`).
4. `git add curriculum-site && git commit` on the device.

**`git push` does not work from here** — no GitHub credentials in the sandbox.
Brad pushes. Say how many commits are waiting when you finish.

**If git complains about `index.lock`:** the mount sometimes leaves stale locks
and `rm` is blocked until file deletion is granted for the session — call
`device_request_delete_permission` on `/Users/bradmiller/GitHub/IntoToPython`,
then `rm -f .git/index.lock .git/HEAD.lock` and re-commit. The grant lapses
between sessions, so expect to ask again.
