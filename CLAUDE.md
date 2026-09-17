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
  Brad is now doing an evaluation pass to see what needs changing.
  `docs/module-01-driving/lesson-01-meet-the-xrp.mdx` is the canonical template.
- **Blockly vs. Python by module:** Module 1 is the Blockly→Python arc (lessons
  1–7 use real Blockly block images; 8–11 are Python). **Module 2 onward is
  all Python** — plain ```python code blocks, no block images. Handy: the
  block-screenshot workflow (§6) only matters for Module 1.

## 2. Source content (what we convert from)

The curriculum content lives in the **parent repo** (`../`, `IntoToPython`):

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
│   │   ├── Lesson.js      # LessonHeader, Objectives, TeacherBanner, CardGrid, InfoCard
│   │   ├── TeacherNote.js # gray teacher-only box
│   │   ├── KnowledgeCheck.js # interactive multiple-choice quiz
│   │   ├── Media.js       # Video, Figure (real src OR labeled placeholder)
│   │   └── Blocks.js      # Block (inline), BlockProgram (composed), BlockShot (real screenshot)
│   ├── theme/
│   │   ├── Root.js        # the floating Teacher-mode toggle + persistence
│   │   └── MDXComponents.js # registers all components globally (no imports needed in .mdx)
│   └── css/custom.css     # ALL styling + brand color tokens (top of file)
├── static/img/
│   ├── logo.svg
│   └── blocks/            # 91 real XRP Blockly block PNGs + programs/ real screenshots (see §6)
├── sidebars.js            # curriculum outline (modules → lessons)
├── docusaurus.config.js   # site config, navbar, Montserrat font, footer
├── netlify.toml           # deploy config (see §8)
└── README.md              # run + deploy instructions
```

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
| Light gray — section + teacher-note backgrounds | `#E9ECEF` / `#F8F9FA` |
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
    {text: 'The correct answer', correct: true},
    {text: 'Another wrong answer', feedback: 'Optional per-option hint'},
  ]}
  explanation="Shown after answering. Works for true/false too (just two options)." />

<Video placeholderLabel="Intro clip (1–2 min)" caption="..." />   {/* placeholder */}
<Video src="https://www.youtube.com/embed/XXXX" caption="..." />  {/* YouTube/Vimeo */}
<Video src="/videos/first-drive.mp4" mp4 caption="..." />         {/* local mp4 */}

<Figure placeholderLabel="Labeled diagram of the XRP" caption="..." />  {/* placeholder */}
<Figure src="/img/lesson-01/parts.png" alt="..." caption="..." />       {/* real image */}

<CardGrid>
  <InfoCard tag="Warehouses" title="Delivery robots">Real-world connection card.</InfoCard>
</CardGrid>
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
    {name: 'stop_motors'},
  ]}
  caption="A stacked program, like the real workspace." />
```

**Container / C-shaped blocks (Repeat, If, function def):** give the block a
`children` array. The component wraps those children in a colored C-bracket that
matches the block's category color (loops green, functions purple, if blue) — so
the contained blocks look genuinely *enclosed*, the way Blockly stretches a Repeat
to wrap its contents. Nest `children` inside `children` for a function that
contains a loop, etc. (Do NOT use a flat list with an `indent` field — that's the
old approach and it did not show enclosure.)

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

`static/img/blocks/programs/square-function.png` is the first real one (used in
Lesson 4). The composed `BlockProgram` remains in lessons 2, 3, 5, 7, 9 until real
screenshots replace them.

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
4. Add the page to `sidebars.js` (under its module category; replace the
   "Coming soon" placeholder as modules get built out).
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

(GitHub Pages also works but needs `baseUrl` = `/IntoToPython/` + a build workflow.)

## 9. Decisions already made (don't re-litigate without reason)

- **Framework:** Docusaurus (Brad had already started one; best fit for the interactive components).
- **Content model:** merge lesson plan + worksheet into one student page; teacher content in toggle-able gray boxes.
- **Branding:** XRP/Experiential palette + Montserrat (see §4), tokens in custom.css.
- **Blocks:** real images from the XRP User Guide, transparent + cropped; "Effort" not "power %". Prefer real `<BlockShot>` screenshots from Brad when available (§6).
- **Videos/graphics:** Brad produces them and hands them off; lessons use labeled placeholders until then.

**Open / unresolved (flag for Brad's evaluation pass):**
- **Module 1 naming is now STANDARDIZED (2026-09-15 review):** `draw_square(size)`,
  `draw_triangle(size)`, `draw_polygon(sides, size, effort)` — identical names and
  parameter order in Blockly (L3–5) and Python (L10–11), so the Phase C mapping is
  literally 1:1. (Previously drifted: L5 used `distance`, L10/11 used `num_sides`.)
  **Still pending:** the Lesson 4 hero screenshot
  (`static/img/blocks/programs/square-function.png`) shows `square(side_length)`;
  the lesson text bridges this in the caption for now. **Brad to re-shoot it as
  `draw_square(size)`**, then drop the parenthetical from the L4 caption.
- **Block screenshots pending:** Brad is supplying real XRP Code screenshots to
  replace the composed `BlockProgram`s in Module 1 lessons 1, 2, 3, 5, 7, 9
  (Lesson 4 already done, but see re-shoot note above). Whiten + drop into
  `static/img/blocks/programs/`. Note: L1's first program now begins with
  `wait_for_button_press` — screenshots should include it.
- **Lesson 0 · What Is a Robot? (added 2026-09-15):** a no-code discussion kickoff
  built from Brad's *WhatIsARobot.pdf* slide deck (WPI). Gallery of "is this a
  robot?" devices with answers hidden in TeacherNotes → 1979 RIA definition →
  WPI sense/think/act → where the XRP fits. Numbered 0 (not renumbered to 1) so
  the site stays aligned with the source repo's 01–11 lesson/slide/worksheet
  numbering; matches Module 4's lesson-00 precedent. **Media pending:** the 9
  Figure placeholders map 1:1, in order, to the deck's images (slides 3–11); the
  Video placeholder is the FIRST ball-shooter clip (slide 14). No matching
  lesson-plan .md exists in the source repo's `module-01-driving/lessons/` yet.
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
  starts with Wait for button press (programs auto-run on upload); Python editor is
  **VS Code + MicroPython extension** (per Brad's source), Blockly is XRP Code;
  student-facing "on paper first" step in L2 and "say it in English first" in L3;
  3–4 objectives per lesson. **Connecting (L1 Part 2, 2026-09-17):** XRP Code
  connects over **USB cable or Bluetooth** — every robot needs one USB connection
  first (that's how XRP Code installs/updates its MicroPython), after which it
  pairs wirelessly by its per-robot ID shown under the RUN button. Bluetooth needs
  a Chromium browser (Chrome/Edge); low battery kills Bluetooth first; a running
  program can block pairing (press reset). Don't describe uploading as USB-only.
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

## 10. Good next steps

- **Evaluation pass (current):** Brad is reviewing all 5 modules. Likely follow-ups:
  resolve the M4/M5 `compute_path` return-shape mismatch (above), standardize Module 1
  naming, and drop in real screenshots/videos as delivered.
- Swap the placeholder `logo.svg` if Brad provides an official XRP logo.
- Drop in real videos/graphics and block screenshots as Brad delivers them
  (replace `placeholderLabel` / add `src`; whiten screenshots per §6).
- Deploy the updated build to Netlify (drag `build/` to app.netlify.com/drop, or push
  to GitHub for auto-deploy).

**Per-module pattern reminder:** each module is a `docs/module-XX-name/` folder of
`lesson-NN-slug.mdx` files, added to its category in `sidebars.js`. Modules 2+ are all
Python. **MDX gotcha:** a bare `{...}` in prose (e.g. a dict literal like
`{(0,0): None}`) is parsed as a JSX expression and breaks the build — wrap it in
backticks (inline code) or put it in a fenced code block.

**To continue in a new session, a prompt like this is enough:**
"Continue the XRP curriculum site in `curriculum-site/`. Read CLAUDE.md." — all five
modules are built; work is now evaluation/refinement, not new conversion.

## 11. Videos & images (adding real media)

Media lives under `static/` and is referenced from the site root (drop the word
`static`, keep the leading slash): `static/img/module-01/x.jpg` → `/img/module-01/x.jpg`;
`static/videos/x.mp4` → `/videos/x.mp4`. Swap a placeholder by replacing
`placeholderLabel` with `src` (+ `alt` for images; `mp4` flag for local video):

```mdx
<Figure src="/img/module-01/mars-rover.jpg" alt="..." caption="..." />
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
