# XRP Python Curriculum — Website Project

Context for anyone (human or AI) continuing work on this site. This is a
Docusaurus web version of Brad's XRP Python curriculum, styled like the
VEX STEM Labs lessons. **Read this first before making changes.**

**This repo is `LearningPython` — the website only.** It was split out of the
`IntoToPython` repo on 2026-09-18, carrying its full history with it (§16). The
source curriculum it was converted from still lives in `IntoToPython`.

---

## 1. What this project is

Turn the existing markdown curriculum (the separate `IntoToPython` repo — see §2)
into a browsable, VEX STEM Labs-style **website**: multi-page lessons with a sidebar,
prev/next navigation, embedded videos and graphics, interactive knowledge
checks, and a teacher-notes toggle.

- **Reference we're matching:** VEX AIR virtual-flight curriculum on
  education.vex.com (clean layout, teacher-notes switch, knowledge checks,
  media-rich lessons).
- **Audience:** high school students (no prior programming); teachers use the
  same pages with teacher-only notes toggled on.
- **Status (current):** **ALL FIVE MODULES ARE BUILT.** Module 1 (13: kickoff
  lesson-00-what-is-a-robot + lessons 1–12), Module 2 (10), Module 3 (4),
  Module 4 (10: overview + lessons 1–9), Module 5 (9: lessons 1–9) — 46 lessons live. Site builds clean (`npm run build`).
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

The curriculum content lives in a **separate repo**, `IntoToPython` — on Brad's
machine at `/Users/bradmiller/GitHub/IntoToPython`, and on GitHub at
`bradamiller/IntoToPython`. It is NOT a parent directory of this repo any more
(it was until the 2026-09-18 split, which is why older notes say `../`). A cloud
sandbox holds a copy of THIS repo only, so reach the source through the device
bridge (§13) — it has to be a connected folder before you can read it:

- `<IntoToPython>/module-01-driving/` … `<IntoToPython>/module-05-dijkstra/`, each with:
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
LearningPython/                            # repo root — the site itself
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
│   │   ├── Quiz.js        # QuizSheet, QuizLink, QuizIndex — printable checks (§14)
│   │   ├── Callout.js     # student-facing callout box (:::admonitions don't work — §5)
│   │   ├── Reveal.js      # click-to-reveal answer box (§15)
│   │   └── cblocks.json   # GENERATED geometry for C-shaped blocks (see §6) — don't hand-edit
│   ├── data/checks.json   # GENERATED question data (§14) — gitignored
│   ├── pages/checks/      # GENERATED printable sheets + keys (§14) — gitignored
│   ├── theme/
│   │   ├── Root.js        # the floating Teacher-mode toggle + persistence
│   │   └── MDXComponents.js # registers all components globally (no imports needed in .mdx)
│   └── css/custom.css     # ALL styling + brand color tokens (top of file)
├── scripts/
│   ├── slice_c_blocks.py       # slices container block art into bar/spine/foot (§6)
│   ├── extract_checks.js       # lessons → src/data/checks.json (§14)
│   └── generate_quiz_pages.js  # checks.json → src/pages/checks/*.mdx (§14)
├── static/
│   ├── img/
│   │   ├── logo.svg
│   │   ├── blocks/        # 91 real XRP Blockly block PNGs
│   │   │   ├── c/         # GENERATED slices of the C-shaped blocks (§6)
│   │   │   └── programs/  # real XRP Code screenshots of whole programs (§6)
│   │   ├── lesson-01/     # Lesson 0 robot gallery (8 JPGs) + xrp-parts.png (Lesson 1)
│   │   ├── lesson-04/     # gear-icon walkthrough stills, cut from the screencast (§12)
│   │   ├── lesson-08/     # library-shelf.svg — hand-drawn diagram (§12)
│   │   ├── lesson-m2-01/  # reflectance-sensor.svg — hand-drawn diagram (§12)
│   │   └── lesson-06/     # motor-motion stills + the two effort diagrams (§12)
│   ├── videos/            # gort.mp4, ballshooter.mp4, motors-*.mp4, l4-square-parameter.mp4 (§12)
│   ├── CNAME              # the custom domain, re-asserted on every deploy (§8)
│   └── .nojekyll          # already there for GitHub Pages (§8)
├── .github/workflows/
│   └── deploy.yml         # build + publish to GitHub Pages on push to main (§8)
├── sidebars.js            # curriculum outline (modules → lessons)
├── docusaurus.config.js   # site config, navbar, Montserrat font, footer
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
  meta={['50–60 min', 'Blockly Foundation', 'No experience needed']} />

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
<Figure src="/img/lesson-01/xrp-parts.png" alt="..." caption="..." />   {/* real image */}

<CardGrid>
  <InfoCard tag="Warehouses" title="Delivery robots">Real-world connection card.</InfoCard>
</CardGrid>

{/* A per-item fill-in: Yes/No buttons + a "Why?" line. Lesson 0 uses one under
    each gallery picture so a class can answer on the projector without
    scrolling back to a table. State is in-memory only — a reload clears it. */}
<Decide device="Camera drone" />
<Decide device="Mars rover" prompt="Robot?" why="Why? — what makes it one?" />

{/* Printable knowledge checks (§14). The QuizLink goes right after </Objectives>
    in every lesson; the sheet pages are generated, so you never write those by
    hand. */}
<QuizLink id="module-01-driving/lesson-01-meet-the-xrp" />
<QuizSheet id="module-01-driving/lesson-01-meet-the-xrp" />        {/* student sheet */}
<QuizSheet id="module-01-driving/lesson-01-meet-the-xrp" answers /> {/* answer key */}
<QuizIndex />                                                       {/* all sheets, by module */}

{/* Click-to-reveal answer box (§15). Closed by default, so opening it is a
    deliberate act — and closed content doesn't print, which is what you want on
    a handout. Never put anything students HAND IN in here. */}
<Reveal>Default title is "Check your work".</Reveal>
<Reveal title="Check your trace" hint="fill the table in first">…</Reveal>

{/* Student-facing callout. Use sparingly — a page with five callouts has none.
    kind: warn (amber, default) | tip (blue) | note (gray). */}
<Callout title="Give the robot a few seconds of stillness">…</Callout>
<Callout kind="tip" title="Proof of concept">…</Callout>
```

**⚠️ Docusaurus `:::` admonitions DO NOT RENDER on this site** — they come out as
literal `:::tip` text. That bit us twice: the home page shipped a literal
`:::tip Proof of concept` for weeks, and a Lesson 1 callout written that way did
the same on 2026-09-19. Root cause not chased; `<Callout>` exists precisely so
nobody has to. If you ever fix the directive parsing, the component can stay —
it's styled to match the course, prints as a bordered box, and takes MDX
children (leave blank lines inside the tags so markdown is parsed).

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

**Function-call blocks are generated, not from the dictionary (2026-09-20).** The
dictionary has no call block, because Blockly builds one per user-defined function
name. `scripts/make_call_block.py` synthesizes one, with or without parameters:

```bash
python3 scripts/make_call_block.py square static/img/blocks/call_square.png
python3 scripts/make_call_block.py polygon static/img/blocks/call_polygon_4_30.png \
    --param sides=4 --param side_length=30
```

Every **silhouette is lifted from a real block's alpha channel** and stretched
through one constant-profile row/column, so corner radii, the top notch, the
bottom tab, the input socket and their antialiasing are the real artwork's and a
generated block stacks pixel-perfectly against real ones. Only fill `#885498`,
border `#6A4377`, highlight `#AA83B6` (sampled from `function_def.png`, so it
reads as the Functions category) and the labels are drawn. Two details that were
bugs before they were rules: the label is anchored on the **ascender line**, not
the glyph bbox (bbox anchoring floats a word with no capitals or descenders), and
the socket is cut with the plug's **exact** alpha, not a dilated one, or a 1px
transparent seam shows between block and plug.

With parameters the block gets a `name  with:` label row plus one 26px row per
parameter, each with a real `numeric_const.png` widened through its own field and
relabelled, plugged into a socket cut in the right edge — the external-input
layout XRP Code actually uses, confirmed against Brad's `square-function.png`
screenshot (which is at dictionary scale, so measurements transfer 1:1).

Existing: `call_square.png` (L1-3), `call_square_{20,35,60}.png` (L1-4),
`call_polygon_{4_30,3_30,6_20,8_15}.png` (L1-5).

**A ```text fence showing block calls is a bug** — use these images. The
exception is genuine plain-English pseudocode, e.g. L1-12's planning step, which
is explicitly "not Python" and should stay a text fence.

A no-parameter call block is labelled with **just the function name** — no "call"
prefix. That's inferred from Brad's real L1-4 screenshot, where a call *with* a
parameter reads `square with: side_length`. If XRP Code actually shows something
else for the no-parameter case, regenerate with the right label and fix the L1-3
prose that points this out.

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
4. Add the page to `sidebars.js` (under its module category — all 46 lessons are
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

**Deploy: GitHub Pages, automatically (set up 2026-09-18).** Netlify was never
connected and its config is gone; `.github/workflows/deploy.yml` builds on every
push to `main` and publishes to Pages. Live site:
**https://learningpython.bradhouse.com/**. The workflow runs `npm ci && npm run
build` on Node 20 (so the `prebuild` hook regenerates the printable checks, §14),
uploads `build/` with `actions/upload-pages-artifact@v3` and deploys with
`actions/deploy-pages@v4`; permissions `contents: read`, `pages: write`,
`id-token: write`, and a `pages` concurrency group so deploys queue instead of
racing. Repo setting, done once: **Settings → Pages → Source: GitHub Actions**
(Pages also needs a public repo on a free personal account).

**The domain, and the three places it lives (settled 2026-09-18).** The site is
served at the root of its own subdomain: DNS has a `learningpython` CNAME under
`bradhouse.com` pointing at `bradamiller.github.io`, and the **`LearningPython`
repo's** Settings → Pages custom domain is `learningpython.bradhouse.com`. Because
it's a root, `baseUrl` is `/` and `url` is the subdomain. `static/CNAME` carries
the domain into every deploy. **Change the domain and you change three things:**
`static/CNAME`, `url` + `baseUrl` in `docusaurus.config.js`, and the repo setting.

History worth knowing, because it was an hour of confusion: the site first went up
as a project site at `bradamiller.github.io/LearningPython/` with
`baseUrl: '/LearningPython/'`. It 404'd, because the **user-site** repo
`bradamiller.github.io` had a `CNAME` of `bradhouse.com` — a user site's custom
domain applies account-wide, so every project site is served at
`bradhouse.com/<repo>/` and the github.io address 301-redirects there. Deleting
that CNAME restored the github.io URL (and Safari cached the 301, which needed
Develop → Empty Caches plus a restart). Then the subdomain replaced it. Two rules
fall out: a custom domain on the **user-site** repo means project sites live at
`<domain>/<repo>/`; a custom domain on **this** repo means the root of that
domain. Only the second is in play now.

**⚠️ Any component that takes a `src` MUST pass it through `useBaseUrl`.** A raw
`/img/...` string works at a domain root and breaks under a subpath — and the site
has now been both. `Media.js` (`Video`, `Figure`) was fixed for this on
2026-09-18; `Blocks.js` (`Block`, `BlockShot`, the C-block slices) and `Quiz.js`
already did it. Lessons keep writing site-absolute paths; components resolve them.
That discipline is why moving from `/LearningPython/` to `/` touched no lesson
file.

**Verifying a build locally** — `npm run build && npm run serve` is enough now
that the site is served at a root. If it is ever moved back under a subpath,
verify it one directory deep instead, because a server at the root hides subpath
mistakes:

```bash
mkdir -p /tmp/pub/<subpath> && cp -r build/* /tmp/pub/<subpath>/
npx serve /tmp/pub    # NOT `serve -s`, which shows a directory listing
```

Then check for 4xx responses and images with `naturalWidth === 0`.

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
- **ACTIVITY HEADINGS, NOT PART NUMBERS (Brad, 2026-09-18).** Lessons are short
  enough that "Part 3" earned nothing, and it never told a student whether to read
  or to do. **All five modules are converted** (M1 first, then M2–M5) — 55
  activities across the 46 lessons; `grep -rn "^## Part " docs/` stays empty. The
  scheme:
  - A section that is student work is `## Activity · <title>`; everything else is
    just `## <title>` with no number. Lesson 7's `## Challenge 1 · …` headings
    count as activities too.
  - The **DO THIS** badge is pure CSS in `custom.css`, matched on the heading id
    Docusaurus derives from the text (`h2[id^='activity']`, `h2[id^='challenge']`),
    so activities stay ordinary markdown headings — still in the right-hand
    contents (where they also get a red dot), still linkable, no wrapper
    component. Nothing to remember when authoring beyond the heading text.
  - **A long build-up is ONE activity with `### Step N · …` subheadings**, not one
    activity per step (Brad, 2026-09-18) — L2's drive-straight → add-a-turn →
    make-a-square sequence is the model.
  - Cross-references must name the section ("when they hunt for the Repeat block"),
    never "see Part 4". `grep -rn "Part [0-9]" docs/module-01-driving/` stays empty.
  - Every lesson should have at least one activity. Two M1 lessons had none and got
    new ones on 2026-09-18: **L6 · Drive a figure-eight** (two mirrored Arcade
    curves — the shape `Straight`/`Turn` cannot draw) and **L9 · Draw a nest of
    squares**, which needed a new teaching section first (**A loop inside a loop**,
    nested `for` loops where the outer counter sets each square's size — Brad's
    design). **The one lesson still without an activity is M2 L8
    (Introduction to Classes)** — pure concept teaching, and due for rewrite when
    the classes-optional reshape reaches the site, so nothing was invented for it.
  - Staged builds in M4/M5 follow the same one-activity-many-steps rule: the
    Manhattan algorithm (2 steps), the Manhattan class (3), the Dijkstra class (3)
    and `compute_path` (5 — the whole lesson is one activity). Each opens with a
    sentence saying what the steps add up to. **Watch for duplicated wording** when
    grouping: titles that already began "Step 1 — …" or "stage 1 —" had to be
    trimmed, or the heading renders "Step 1 · Step 1 — …".
  - For a final-project lesson, "The mission" and "The rubric" stay plain — they're
    the brief, not the work; the planning/testing/reflecting sections carry the
    badge.
- **LESSON NUMBERING IS `module-lesson` (Brad, 2026-09-20).** Every lesson is
  "Lesson 1-7", "Lesson 5-3" — module number, hyphen, lesson number — in the
  frontmatter `title`, the `sidebar_label` (without the word "Lesson"), the
  `<LessonHeader title>`, and every cross-reference in prose. **Cross-references
  are always fully qualified now**, so "see Lesson 1-2" reads the same from any
  module; there is no such thing as a bare "Lesson 2" any more. Ranges read
  "Lessons 5-4 and 5-5" (adjacent) or "Lessons 2-1 through 2-6" (wider) — an
  en-dash range like "5-4–5-5" is unreadable next to the hyphens. Edge cases:
  Module 1's kickoff is **1-0**, Module 4's overview is **4-0** (its title stays
  "Module Overview · The Big Picture"), and the final-project titles dropped the
  redundant "Module N" — "Lesson 2-10 · Final Project". File names are
  `lesson-NN-slug.mdx` with NN matching the lesson number.
- **MID-MODULE INSERTION IS ALLOWED NOW (Brad, 2026-09-21).** The site's lesson
  numbers used to be pinned to the source repo's 01–11 slide/worksheet numbering
  (that's why the kickoff is `lesson-00`, not a renumber of 1–11). Brad has
  dropped that constraint: "I don't think there is any reason to have the section
  numbers relate to the prior version of the course any more." So a new lesson
  goes in at its right place and everything after it shifts. The renumber touches
  five things, and missing any one of them breaks the build or a link:
  file name, `sidebar_position`, frontmatter `title` + `sidebar_label`,
  `<LessonHeader title>`, the `<QuizLink id>` (it is the file path, so it MUST
  change with the file name), `sidebars.js`'s explicit `items` list, and prose
  cross-references anywhere in `docs/`. Rename highest-number-first so the moves
  never collide. `src/data/*.json` and `src/pages/checks/**` are generated — leave
  them alone, they regenerate. Also re-point the **preview line** in the teacher
  note of the lesson *before* the insertion: it names what comes next, and an
  insertion silently makes it wrong.
  Printable checks and the pacing guide read titles from frontmatter, so both
  followed automatically.
- **Module 1 style rules applied in the 2026-09-15 review** (keep enforcing):
  the middle header chip names the TOPIC, matching Modules 2–5 ("while loops",
  "Python data"). Module 1's reads "Blockly Foundation" (1-1 to 1-5), "Driving
  Challenges" (1-6, 1-7) or "Transition to Python" (1-8 to 1-12) — **the "Phase A ·
  / B · / C ·" prefixes were dropped 2026-09-20** (Brad: only Module 1 had phases,
  so the letters implied a course-wide scheme that doesn't exist; the grouping
  labels stay because Module 1 really does change tools partway through).
  **WAIT FOR BUTTON — ON PROGRAMS STUDENTS RUN, NOT ON EVERY SNIPPET (Brad,
  2026-09-23).** A program students type in and press RUN on starts driving the
  instant it uploads, so it opens with Wait for button press /
  `board.wait_for_button()`. An *illustrative* snippet — a three-line
  block-to-Python comparison, a `def` shown on its own, a loop body with no
  imports, a deliberately broken fragment to debug — does **not** get one: it is
  never run as printed, and the extra lines bury the one idea the snippet exists
  to show. Judge by "would a student paste this and press RUN?", not by whether
  the text contains a drive call. Applied to M1 L8 (its Activity got the wait; its
  four teaching snippets deliberately did not) and M1 L12 (the project skeleton,
  inside `main()`); M1 L10's only complete program already had it, and M1 L11 is
  all definitions and fragments, so neither needed anything. Same judgement was
  used for the M3–M5 sweep on 2026-09-22, where two fragments were left alone on
  purpose. **⚠️ Still open:** five of the nine composed Blockly programs omit the
  block (L3 ×2, L7, L8, L10 — L3's first one is the deliberate copy-paste "before"
  figure, so judge it on its own). Python editor is
  **XRP Code for everything** — Blockly first, then MicroPython files in the same
  browser editor (`File → New File` → MICROPYTHON; filesystem left, editor middle,
  shell bottom; green RUN button). **Corrected 2026-09-19:** earlier notes and
  four lessons said VS Code + the MicroPython extension, which came from the
  source repo and is not what the course uses. If you see VS Code anywhere, it's
  a leftover;
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
- **M2-L6 DRIFT DIRECTION (fixed 2026-09-22).** With black = 0.8, the sensor reading
  high is the side the LINE is on, so the robot is on the **other** side: left sensor
  high → the robot drifted **right** → steer left. The lesson had this inverted in six
  places (including the teacher's reference card) while the code was correct, so
  nothing failed and the explanation was still wrong. If you touch two-sensor
  material, derive the direction; don't copy a remembered table.
- **DIJKSTRA TAKES A GRID SIZE (fixed 2026-09-22).** `Dijkstra.__init__` is
  `(self, start, blocked, rows=4, cols=4)` and `build_graph` reads `self.rows` /
  `self.cols`. The defaults keep `Dijkstra((0,0), [])` working, and the 3×3 that L5-3
  traces by hand is now reachable — which L5-5 has always instructed students to test
  against. Verified by running the assembled class: 16/15/14 nodes on the 4×4, 8 on
  the 3×3, 6 steps across a clear 4×4, and the 3×3 route matches L5-3's hand trace
  with the start dropped. `Manhattan` still takes only `start`; that constructor
  difference is real and is the open question in REVIEW's section 2.
- **`Kp` KEEPS ITS CAPITAL — the one exception to snake_case (Brad, 2026-09-24).** The
  proportional gain is `Kp` everywhere: L2-5, L2-6, L2-7, and as `self.Kp` in L2-9 and
  L2-10, which previously used `self.kp` and made the course disagree with itself. It is
  the ONLY name in the course that departs from L1-9's rule, and a `<Callout kind="note">`
  at its first use in L2-5 says why rather than leaving students to notice the
  contradiction: every control-systems text, datasheet and paper writes the proportional
  gain as K-sub-p, so `kp` would be more Pythonic while quietly cutting the link to
  everything a student will ever read about PID tuning. The rule as stated there: *name
  your own variables the Python way; when a name comes from the engineering world rather
  than from you, keep the engineering spelling.* If a second such name ever appears, it
  joins that sentence — don't start a second explanation somewhere else. L1-9 is
  deliberately left alone; the exception is explained where it is met, not pre-empted.
- **OBSTACLES ARE TOLD TO THE PLANNER, NOT PASSED TO IT (Brad, 2026-09-24).** `Dijkstra`
  is `__init__(self, start, rows=4, cols=4)` with `self.blocked = []`, plus
  `set_blocked_intersections(blocked)`, which stores the list **and rebuilds the graph**.
  Both lines matter: `build_graph` builds *around* the blocked nodes in one pass (it does
  not build-then-prune, and L5-4 argues for that), so storing a new list without rebuilding
  leaves routes through a node you just blocked.
  **Why:** `Manhattan(start)` and `Dijkstra(start)` are now created identically, so the
  L5-6 swap really is one word — the interchangeability the philosophy page has promised
  since Module 4. The deeper reason is that obstacles are something a planner *discovers*
  while driving, not part of what it is; `start` is identity, `blocked` is knowledge.
  **Rejected:** giving `Manhattan` optional `rows`/`cols` to make the signatures match
  character for character (Brad proposed it). Manhattan's arithmetic works on any grid and
  would never read them, so they would be parameters that lie about what the class needs;
  the call sites already match, which is the only place matching matters. If Manhattan ever
  gains an off-grid `raise` (the L4-7 convention) they become real — a separate decision.
  **Touched:** L5-4 (constructor comparison flipped to "the same", the setter section, both
  knowledge checks, Step 3, the InfoCard pair, wrap-up, exit ticket), L5-6 (both test
  snippets, the swap activity), L5-7 and L5-9 (reactive loops now tell the existing planner
  rather than building a new one each time). `grep -rn "Dijkstra(" docs/` should show no
  call passing a blocked list positionally.
  **The subtlety that is now taught rather than tripped over:** the planner holds a
  *reference* to your blocked list (L4-3), so appending to yours updates `self.blocked`
  immediately — but `self.graph` was computed earlier and nothing rebuilds it by itself.
  That is exactly why the setter exists, and L5-4's teacher note stages the mistake
  deliberately.
  **Verified** by assembling the class with L5-5's `compute_path` and running it: 16/15/14
  nodes, 8 on the 3×3 from L5-3's hand trace, the setter replacing rather than accumulating,
  Dijkstra matching Manhattan's 6 steps on a clear 4×4, the L5-6 obstacle test avoiding both
  blocked nodes, and a mid-journey reroute going around a newly discovered obstacle.
- **FAIL WHERE THE PROBLEM IS — `raise` on impossible input (Brad, 2026-09-24).** A
  function that cannot answer the question it was asked ends with a `raise`, not an
  implicit fall-off-the-end. Three places do this and they are the whole set:
  `desired_heading` in **L4-7** and again in **L4-8**, and `get_next_intersection` in
  **M5 L7**. All three were silently returning `None`, which then travelled — `None`
  into `turn_to` spins the robot forever (`self.heading` is only ever 0–3), and `None`
  into `blocked_list` corrupts the graph the planner reasons about without crashing
  anything.
  **L4-7 owns the teaching**, in a section called "Say so when you can't answer"; the
  other two cite it in a sentence. The point Brad asked for, and the one to keep if this
  is ever rewritten: *checking for failure conditions puts the error where the problem
  is, which is what makes it findable.* The worked example is that the symptom of the
  missing check appears in `turn_to`, which is completely correct — so a student hunting
  the bug reads the one piece of code that isn't wrong. Implicit `None` on fall-through
  is named explicitly there too; it is a beginner trap and that is the place it bites.
  **The four conditions now test BOTH differences** (`col_diff == 0 and row_diff == -1`
  …). The original one-sided form looked equivalent and wasn't: (2,1) → (3,3) has
  `row_diff` of 1, so it returned South and never reached the `raise` for a pair that is
  plainly not a step apart. A check with a hole in it is worse than none, since the
  section's whole claim is that the error lands where the problem is. It also writes down
  the lesson's own "one change at a time" premise. Verified against every case the lesson
  states, including the four knowledge-check pairs.
  **Deliberately NOT taught:** `try`/`except`. Students never catch these — they read the
  message. (The course's only `try` is M5 L8's `load_obstacles`, and it stays a one-off.)
  Don't turn L4-7 into an exceptions lesson; its teacher note says so.
  **Rejected alternative:** returning a sentinel like `-1`. It reproduces the same bug —
  `turn_to(-1)` loops forever exactly as `turn_to(None)` does — so it only helps at call
  sites that remember to check, and it puts error-handling noise into the very lessons
  whose point is that the main program reads as a list of intentions.
  **Unverified:** an uncaught exception mid-drive leaves the motors running until the
  program dies. §9's "motors stop when a program ends" rule should cover it, but that
  rule was written about normal termination — worth one check on a real robot.
- **VARIABLES, EXPRESSIONS AND SCOPE (Brad, 2026-09-21).** Before this, nothing in
  the course explained what a variable is: the first assignment students met was
  `drivetrain = …` in L1-8, presented only as "make an instance", and `snake_case`
  appeared nowhere in the repo. **L1-9 · Variables & Expressions** now owns it —
  **the memory-location model (Brad, 2026-09-23)** — memory is a bank of
  **locations**, each holding one value and each carrying a number called its
  **address**; a variable is one of those locations with a **name** you chose; `=`
  works out the right side and *stores* the result there; reassigning *overwrites*
  what was there. The picture is a wall of **post office boxes** (Brad's, and it is
  load-bearing — see below), with the **processor as the clerk**: nothing goes into
  a location or comes out of one except through it. That is what makes
  `count = count + 1` explainable — the processor reads the location, adds one,
  writes it back, same location twice in one line.
  **Two framings that were tried and rejected, in order:** "a name attached to a
  value" (Brad, 2026-09-21 — confusing, and it makes `count = count + 1` unexplainable)
  and then "a labelled box" (Brad, 2026-09-23 — accurate enough but it has to be
  *retracted* in L4-3, where the box turns out not to contain the list). Don't
  restore either.
  **Why post office boxes specifically:** the number is printed on the front and is
  separate from the contents, so the address is visible from L1-9 onward without
  being used. That makes L4-3 an **extension** rather than an amendment — no sentence
  from L1-9 becomes false when references arrive, which is the whole reason for the
  model. So: L1-9 shows the addresses on the figure and says in one sentence that
  they exist and aren't needed yet; L4-3 is where they do work. Don't teach addresses
  in Module 1, and don't hide them from the diagram either.
  **The honest caveat, for whoever edits this next:** in MicroPython *every* variable
  holds a reference, integers included. "Numbers live in the location, lists live
  elsewhere" is itself a simplification — it is safe only because ints are immutable,
  so no student experiment can catch it out. It was chosen over the fully accurate
  version because it never needs taking back. Do not "correct" L1-9 into a lecture on
  object identity.
  **Figures — three, and they do different jobs.** L1-9 opens with
  `static/img/lesson-09/memory-post-office.png`, Brad's illustration of a post office
  wall, which carries the *analogy*; then
  `static/img/lesson-09/memory-locations.svg` carries the *mechanism* (a bank of five
  locations drawn as box doors: address plate on top, value inside, red name card at
  the bottom; two unnamed). L4-3 has
  `static/img/lesson-m4-03/two-names-one-list.svg` (`path` and `same_path` both
  holding `5120`, arrows to one list). The two SVGs are hand-drawn in the course
  palette per §12.
  **The PNG was repaired before use and the original is not usable as supplied.** It
  is AI-generated, and every box label came out as garbled squiggles — fatal for a
  figure whose subject is *the boxes have numbers*. The plates were detected as
  near-neutral rectangles, refilled with their own sampled tone and repainted with
  real numbers (101–105, 111–113, 121–125, …, one series per column), then the
  leftover garbled marks sitting directly on the box fronts were inpainted with the
  surrounding tan. If it is ever regenerated or replaced, that pass has to be redone —
  check at the rendered width (~549 px), not at full size, and in particular check for
  stray glyphs *above* a plate rather than on it.
  **The rest of the lesson covers:** reassignment including
  `count = count + 1`, snake_case, the Capitalized-class / lowercase-instance
  convention (which had been living in a teacher note only), arithmetic operators,
  precedence and parentheses, and one note on `/` always giving a float. Its
  examples are deliberately real lines from later lessons — `size = 20 + square * 5`
  (L1-10) and the threshold midpoint `(white + black) / 2` (L2-1) — because a
  precedence mistake raises no error, it just produces a wrong number.
  **Deliberately NOT in it:** comparison operators (`<`, `==`, …) stay in L2-2
  where a `while` condition first needs them, and `//` and `**` are never used
  anywhere in the course so teaching them would be padding. **`%` is the exception
  and the note here used to be wrong:** it appears exactly once, in M2 L5's
  throttled-print line (`i % 50 == 0`), and until 2026-09-24 nothing anywhere had
  said what it does. It is now explained in one sentence *at that line* rather than
  taught in L1-9, because one use does not earn a section — but if a second use ever
  appears, move it into L1-9's operator list. The activity is
  robot-free (predict, then `print()`), which makes it the lesson to reach for when
  hardware or batteries are unavailable.
  **Scope lives in L1-11,** rewritten the same day. The old lesson asserted "local"
  in an objective and discharged it with a single quiz question — while its own
  example called `drivetrain` from inside a function, which flatly contradicts the
  naive reading. The rule taught is **local first, then look outward**: locals and
  parameters die when the function returns, a function *can read* an outer name
  (this is why one `drivetrain` at the top serves every function), and *assigning*
  to an outer name makes a new local instead — which is the gap `self.` closes in
  Module 2. Don't simplify this back to "functions can't see outside themselves",
  and keep `global` out of the course; it is needed nowhere.
- **BLOCKLY FUNCTIONS: NO RETURN VALUE (Brad, 2026-09-20).** The Functions palette
  offers two definition blocks — plain **"to do something"** and a version with a
  **return** socket. Module 1 uses the plain one only. The return version's call
  block is a rounded value block, so it will not snap into the program stack, and
  students who grab it think they've broken something. L1-3 calls this out with a
  Callout, a knowledge check on the rounded-call-block symptom, and a teacher note.
  `return` is introduced later, in **L1-11**, in Python, for functions that compute
  an answer (`360 / sides`) — don't frame return as wrong, only as not applicable
  to functions that drive the robot.
- **XRP CODE URL AND BROWSER (Brad, 2026-09-18).** The IDE students use is
  **https://xrpcode.wpi.edu/staging**, and it works **only in Google Chrome or
  Microsoft Edge** — the serial and Bluetooth APIs it needs to reach a robot exist
  only in Chromium browsers, so Safari and Firefox load the page, build programs
  fine, and then fail at CONNECT with the robot simply absent from the list. L1
  says this where students are first told to open the tool, with a knowledge check
  on the symptom. Deeper how-to lives in the **XRPCode chapter of the XRP User
  Guide** (`https://xrpusersguide.readthedocs.io/en/latest/course/XRPCode.html` —
  panels, USB connection, troubleshooting); link there rather than re-documenting
  the IDE. **Propagated site-wide (Brad, 2026-09-20):** every link to the IDE now
  carries `/staging` — the navbar and footer entries in `docusaurus.config.js` and
  all eight remaining lesson Resources lists. There is no bare
  `https://xrpcode.wpi.edu/` link left in the site; new links must include
  `/staging` too.
- **IMU CALIBRATION: PUT THE ROBOT DOWN BEFORE POWER-ON (Brad, 2026-09-19).** For
  the first few seconds after power-on or reset, the XRP calibrates its IMU, and
  the calibration assumes the robot is completely still. Held in a hand — or
  bumped — it calibrates against a moving reference and **every later turn is off
  by an unpredictable amount**, with no error reported. The sequence students
  learn: robot down → power on (or reset) → wait a few seconds, hands off → press
  the User button to release **Wait for button press**. That's the practical
  justification for the wait-for-button block beyond "don't drive off the table."
  Lesson 1's "Put the robot down *before* you switch it on" `<Callout>` and its
  knowledge check are the canonical treatment; the same symptom is the first
  troubleshooting entry for any turn that misbehaves in later lessons.
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
    `TeacherNote` pattern). **DO NOT start this yet — Brad is deliberately
    deferring it (2026-09-18): he wants the course's overall structure settled
    first, then he'll come back to the class-first question.** When he does, the
    open decision is how an Optional Extension should look on a page.** Note this also resolves how M4/M5 relate — see the
    `compute_path` bullet below, which the functions-first shape may settle on its
    own.
  - Also per that guide, still stale in the SOURCE (not the site): M2 L8–L9 slide
    outlines + `.pptx`, the root `generate_pptx_lesson*.py` scripts, and the
    `.html`/`.pdf` worksheet renders for M4–M5.
- **✅ `compute_path` return shape — SETTLED 2026-09-19: both planners EXCLUDE the
  start.** `compute_path` returns only the intersections the robot drives *to*, so
  `steps = len(path)` in both modules and "already there" is `[]`. Brad's call;
  it makes the Manhattan→Dijkstra swap real, which the philosophy page (§18) now
  promises publicly.
  - Previously M4 excluded the start and M5 **included** it (the source curriculum
    disagreed with itself), so a Dijkstra path fed to `Navigator.drive_path` would
    have driven to the robot's own position on every first step.
  - What changed on the site: M5 L5's reconstruction now ends `return path[1:]`
    with the reasoning spelled out; step counts moved from `len(path) - 1` to
    `len(path)` in L5 and L6; L6's interface note explains that the agreement has
    to be exact down to the first element; L9's capstone loop iterates
    `for next_stop in path` instead of `range(len(path) - 1)` / `path[i + 1]`;
    L3 (hand-tracing) still reconstructs the whole route — correct for tracing —
    but now says the code drops the first entry.
  - **The source repo still has the old M5 shape.** If lessons are ever re-converted
    from `IntoToPython`, this correction must be re-applied.
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
| **M1 L1** | Real `xrp-parts.png` diagram; **Bluetooth** added beside USB; square challenge de-spoiled (hands off to L2); trailing `stop_motors` removed; Sleep dropped from the block list and from Part 5 |
| **M1 L2** | Rebuilt as the discovery model (straight → turn → 8-block square → find Repeat; triangle fails before `360 ÷ sides`); real Repeat screenshot |
| **M1 L3** | Function renamed `square`; Sleep-between-calls suggestion removed |
| **M1 L4** | Parameter renamed `side_length` to match the screenshot; function renamed `square` |
| **M1 L5** | Rebuilt from Brad's screenshot: `polygon (sides, side_length)`, no effort parameter |
| **M1 L6** | Built from Brad's Keynote motor deck (stills + clips); "effort ≠ speed" section added; re-framed to finishing vs. non-finishing blocks, timed driving demoted; **figure-eight activity added** (2026-09-18) |
| **M1 L9** | **New "A loop inside a loop" section + nest-of-squares activity** (2026-09-18) — nested `for` loops, outer counter sets the size; objectives and wrap-up updated |
| **All 46 lessons** | Part numbers dropped; student-work sections relabelled `Activity · …` with a DO THIS badge — M1 then M2–M5 (2026-09-18). This was a *labelling* pass on M2–M5, not a content review: their prose still hasn't had Brad's eye. |
| **M1 L10–11** | Python aligned to the Blockly names/params (`square`, `polygon(sides, side_length)`) — naming only; these lessons have NOT had a full review (their examples still skip `board.wait_for_button()`) |
| **M2 L2/L7/L10** | Trailing `drivetrain.stop()` removed from end-of-program examples |
| **Not yet reviewed** | **M1 L7–L11** (L10–11 got the rename only) **and all of Modules 2–5** (beyond the stop() sweep) |
| **M2/M4/M5 site pages** | ⚠️ Now BEHIND the source — the `separate-classes` merge (2026-09-18) made classes optional in the source only. See §9. |

## 10b. TODO notes in the lessons (added 2026-09-22, reworked 2026-09-23)

Known-broken or unfinished things are flagged **in the lesson itself**, as a
`<Todo>` component that renders a coloured box on the page:

```mdx
<Todo kind="bug">
loop_count is defined nowhere in this module, so a student who pastes this in
gets a NameError. [REVIEW §1.7]
</Todo>
```

**They ship with the site, behind a switch** — the same arrangement teacher notes
already use. A **"Show TODOs"** toggle sits above Teacher mode with a count for the
page; it appears only where there is something to show, defaults **on** under
`npm start` and **off** on a built site, and remembers whichever way it was last
set. So the notes are readable on the deployed site by flipping the switch, and a
reader who never touches it sees nothing.

This was **dev-server-only until 2026-09-23** and that was the wrong call — Brad
could not see them where he actually reads the course. The honest tradeoff of the
current arrangement: the note text is in the deployed page source, exactly as
teacher notes and the public answer-key pages already are (§15). If that ever
matters, one build strips them completely:

```bash
SHOW_TODOS=0 npm run build     # markup and text both gone, verified
```

`plugins/remark-strip-todos.js` does that by deleting the nodes before MDX
compiles them. Deleting at the *remark* stage is the only thing that works: a
component returning null still leaves its children compiled into the JS bundle,
so the words shipped anyway — which is how this was first written, and was wrong.

Categories, most urgent first: **bug** (wrong, and a student can hit it),
**blocked** (needs Brad's decision or a robot), **answers** (an answer is visible
where it shouldn't be), **convention** (drifts from a rule kept elsewhere),
**media** (placeholder or stand-in art). As of 2026-09-24: 2 bug, 3 blocked,
7 answers, 6 convention, 2 media — 20 total. `npm run todos` lists them from the
terminal; `REVIEW-2026-09-21.md` carries the reasoning each cites.

### The /todos index (added 2026-09-24)

Every note on one page, grouped by category, each card linking straight to the
note in its lesson — and an **index** link in the corner of every note box for the
way back. That loop is the point: pick one, click it, fix the lesson, delete the
note, return. Generated like the checks and the pacing guide, so a fixed note
leaves the page by itself:

```
docs/**/lesson-*.mdx  --scripts/extract_todos.js-->  src/data/todos.json
                      --src/components/TodoIndex.js-->  /todos
```

**The navbar tab is gated on the switch** — `.navbar__item--todos` is
`display:none` unless `html[data-todos='on']`. A tab advertising everything wrong
with the course is not for students. Consequence worth knowing: the tab only
appears once TODOs are switched on, which under `npm start` is the default, and on
the built site happens the moment Brad flips the switch on any lesson that has
notes. The page itself stays reachable at its URL either way, like the answer keys.

**Three things that had to be got right, and will break quietly if changed:**

- **The anchors are numbered by a remark plugin, not by hand.**
  `plugins/remark-number-todos.js` stamps `index` on each `<Todo>` in document
  order and the component renders `id="todo-N"`; `extract_todos.js` counts the same
  way over the same source. **Change how either one counts and every link lands one
  note off.** Numbering runs in every build, before the strip plugin.
- **`<Todo>` calls `useBrokenLinks().collectAnchor(id)`**, the same API headings
  use. Docusaurus only knows about anchors a component registers, so without it
  every card on /todos is reported as a broken anchor — 29 false warnings per
  build, which is exactly how a real one gets missed.
- **Landing on a hidden note needed two fixes.** Root.js watches for a `#todo-N`
  hash and switches TODOs on before scrolling (a hidden element has no position, so
  the browser has nothing to scroll to and the link looks broken), and `.todo` has
  `scroll-margin-top: 5rem` so the note clears the sticky navbar.

`SHOW_TODOS=0` empties the index too — otherwise the one page listing every
unfinished thing in the course would survive a strip that removed the notes.

Four rules when writing one, each learned the hard way:
- **Never inside a code fence.** A `<Todo>` between fence markers is literal text
  in the code block, visible to students. Seven were placed that way and had to be
  moved out (2026-09-23). Put it *above* the fence.
- **No braces or backticks in the body** — a bare brace in MDX is a JSX expression
  and breaks the build; angle brackets break it too.
- **Never inside a JSX element's attribute list** — put it on the line above.
- **Delete the note in the same commit that fixes the thing.**

## 11. Good next steps

**Deferred feature work lives in `BACKLOG.md`** — site search and PDF export are
both written up there with the research already done (which plugin, which config
options, and the trap in each). Brad asked for both on 2026-09-23 but wants them
after the course is closer to finished. `BACKLOG.md` also indexes the parked
decisions so none of them are only in a chat log.

- **Push.** Commits are made here but **`git push` cannot run from the sandbox**
  (no GitHub credentials) — Brad pushes with `git push origin main`. Always tell him how many commits are waiting.
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
- Deploy: GitHub Pages, automatic on push to `main` (§8). Live at
  https://learningpython.bradhouse.com/.

**Per-module pattern reminder:** each module is a `docs/module-XX-name/` folder of
`lesson-NN-slug.mdx` files, added to its category in `sidebars.js`. Modules 2+ are all
Python. **MDX gotcha:** a bare `{...}` in prose (e.g. a dict literal like
`{(0,0): None}`) is parsed as a JSX expression and breaks the build — wrap it in
backticks (inline code) or put it in a fenced code block.

**To continue in a new session, a prompt like this is enough:**
"Continue the XRP curriculum site in the `LearningPython` repo. Read CLAUDE.md." —
all five modules are built; work is now evaluation/refinement, not new conversion.

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
10+ Mbps) are 100+ MB — GitHub rejects files over 100 MB, and every megabyte is
re-fetched by each Pages build. Recipe (ffmpeg is on Brad's Mac; ~10 MB per 90 s):

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
**Hand-drawn SVG diagrams.** Two exist so far: `lesson-08/library-shelf.svg`
(XRPLib as a shelf of books) and `lesson-m2-01/reflectance-sensor.svg` (LED +
phototransistor over white vs. black, with the ≈0.2 / ≈0.8 readings that match the
lesson's convention — higher means darker). Note the folder naming: Module 1
lessons use `lesson-NN/`, so anything outside Module 1 needs a module-qualified
name like `lesson-m2-01/`.

**Hand-drawn SVG diagrams.** Where a photo doesn't exist and a stock image would
only be decorative, draw it: `static/img/lesson-08/library-shelf.svg` (XRPLib as a
shelf of books, with DifferentialDrive taken down) is the worked example. Inline
the styles, use the brand palette from §4, and give it `<title>`/`<desc>` for
screen readers. **Size it for the content column, which is only ~570 px wide** —
the first version had a 900-wide viewBox, so its 15px labels rendered at 9px and
were unreadable. A viewBox around 680×300 scales to roughly 0.83 and stays legible;
check by screenshotting the figure as rendered, not the file on its own.

**Stills pulled from a screencast.** Lesson 4's three step images were cut from
Brad's own XRP Code recording rather than shot separately: find a sharp frame
(CleanShot's zoom-ins are upscales of a 894×500 capture, so they're soft — the
*un*-zoomed frames are the sharp ones; rank candidates by variance-of-Laplacian),
crop tight around the blocks in native coordinates, then upscale 1.5–2× with
Lanczos and save JPEG q88 into `static/img/lesson-NN/`. That keeps a 365 px-wide
crop legible in a ~720 px content column. `scripts/` has no helper for this; it was
a one-off ffmpeg + Pillow pass.

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

That is where the FIRST version of Lesson 1's labeled kit diagram came from.

**Superseded 2026-09-21.** Brad supplied a new kit diagram and it is now
`static/img/lesson-01/xrp-parts.png` — PNG, not JPEG, because the labels are
black text on white and JPEG rings around them. Processing: trimmed the uneven
white margin to a uniform 24px (the component caps a figure at 520px tall, so
margin is wasted height), then quantized to a 256-colour palette — 218KB instead
of 530KB, with no visible loss at render size. The labels are Wheels and tires,
Batteries, Drive Motor, Controller, Rangefinder, Reflectance and Castor wheel;
lesson prose must match those, and the old image's *Line Follower* wording has
been removed. Note the image spells it "Castor"; the prose uses "caster".

## 13. Getting changes from this sandbox into Brad's repo

The cloud workspace is NOT his machine. The repo lives at
`/Users/bradmiller/GitHub/LearningPython`; it must be a **connected folder** for
this session before any of this works (ask with `device_request_folder_access` if
the `device_*` tools can't see it). The loop that works:

1. Edit and `npm run build` in the cloud copy (`/home/claude/xrp-curriculum`).
2. Eyeball it: serve `build/` (`npx serve -l 3055 build`) and screenshot with the
   bundled Playwright — `require('<site>/node_modules/playwright-core')`,
   `executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'`. Serve
   and shoot in ONE bash call. (That Chromium can't decode H.264, so local MP4s
   show `readyState 0` in a screenshot — expected, not a bug.)
3. `tar -czf /mnt/user-data/outputs/<name>.tgz <changed files>` → `SendUserFile` →
   `device_commit_files` into `…/GitHub/LearningPython/` → on the device,
   `tar --overwrite -xzf <name>.tgz && rm -f <name>.tgz` (plain `tar` refuses to
   overwrite; the FUSE mount needs `--overwrite`). Paths in the tarball are now
   repo-root-relative — before the split they were relative to `curriculum-site/`.
4. `git add -A && git commit` on the device.

**`git push` does not work from here** — no GitHub credentials in the sandbox.
Brad pushes. Say how many commits are waiting when you finish.

**If git complains about `index.lock`:** the mount sometimes leaves stale locks
and `rm` is blocked until file deletion is granted for the session — call
`device_request_delete_permission` on `/Users/bradmiller/GitHub/LearningPython`,
then `rm -f .git/index.lock .git/HEAD.lock` and re-commit. The grant lapses
between sessions, so expect to ask again. Anything that writes git's own
temporary state (rebase, cherry-pick) needs that grant too, and git needs an
identity in the repo — the mount has none, so `git config user.name/user.email`
locally or every commit fails with "unable to auto-detect email address".

## 14. Printable knowledge checks

Added 2026-09-18 at Brad's request: teachers can print the questions and students
fill them in by hand, **without losing the interactive versions** on the lesson
pages (he chose to keep both).

**Where the questions live:** in the lesson `.mdx`, as `<KnowledgeCheck>` — exactly
as before. That is the single source of truth. Nothing is duplicated.

**The pipeline** (`npm run checks`, run automatically by `prestart`/`prebuild`):

```
docs/**/lesson-*.mdx  --scripts/extract_checks.js-->  src/data/checks.json
                      --scripts/generate_quiz_pages.js-->  src/pages/checks/**.mdx
```

- `extract_checks.js` parses every `<KnowledgeCheck>` (174 of them across the 45
  lessons) into JSON, with the lesson title, module title and doc path. It fails
  loudly if a question can't be parsed or doesn't have exactly one `correct: true`,
  so a malformed check can't silently vanish from a sheet.
- `generate_quiz_pages.js` writes 91 stub pages — a student sheet and an answer key
  per lesson, plus an index at `/checks` — each three lines long, rendering
  `<QuizSheet>`/`<QuizIndex>` from the JSON. It wipes the folder first, so renamed
  or deleted lessons can't leave stale sheets behind.
- Both outputs are **gitignored**; the build regenerates them. Don't commit them,
  and don't hand-edit them — edit the lesson.

**Pages** live under `src/pages/` (not `docs/`), so a sheet has no sidebar,
breadcrumb or prev/next — it's a handout, not a lesson. URLs:
`/checks/<module>/<lesson>`, `…-key` for the answer key, `/checks` for the index.

**Titles** identify the lesson, per Brad's ask: the module in small caps above,
then "Lesson N · Title — Knowledge Checks", plus a red ANSWER KEY chip on the key.
The student sheet adds Name/Date rules, lettered options, and an "Answer ___ Why?"
line under each question. The key marks the correct option and prints the
explanation that was already written for the interactive version.

**Printing** is plain browser print (Cmd/Ctrl-P): `@media print` in `custom.css`
hides the navbar, footer, sidebar, TOC and the teacher-mode toggle, forces black
on white, and keeps a question from splitting across a page break.

**On each lesson page**, `<QuizLink id="…" />` sits **immediately after the
`</Objectives>` block** — near the top, where a teacher planning the lesson will
see it. (It was first placed just before `## Resources`; Brad couldn't find it
down there, so it moved up on 2026-09-18. Keep it near the top.) Its answer-key
link is wrapped in `.teacherNote teacherNote--inline`, so students don't see it
unless teacher mode is on. The navbar also has a **Printable Checks** entry
pointing at `/checks`, so the whole set is reachable from any page.

**If you add or edit a question:** edit the `<KnowledgeCheck>` in the lesson and
rebuild — the sheet follows. **If you add a lesson:** the sheet and key are
generated automatically; just add a `<QuizLink>` after its `</Objectives>`.

**If the links don't appear while you're working:** restart `npm start`. Component
registration (`src/theme/MDXComponents.js`) is read at server start, so a dev
server that was already running when `QuizLink` was added renders nothing for it.

## 15. Where answers may and may not appear

Added 2026-09-18. Brad flagged that the Drawing Shapes lesson handed students the
answers to the very problems it had just asked them to solve, and asked for that to
be fixed throughout. The rule now has two tiers, and which tier something falls into
depends on **whether the student turns it in**:

| The thing | Where it goes | Student can open it? |
|---|---|---|
| Worked result, finished program, the rule behind a pattern — something they may check *after trying* | `<Reveal>` | Yes, by clicking |
| Anything they hand in: filled tables, challenge solutions, project code, expected test values | `<TeacherNote>` | No |

`<Reveal>` (`src/components/Reveal.js`) is closed by default, so opening it is a
deliberate act rather than something the eye catches while scrolling. Closed content
isn't printed either, which matters because these pages get printed as handouts.
`<TeacherNote>` is the existing teacher-mode box — invisible to students entirely.

Conventions that came out of the pass:

- **Never answer in the next paragraph.** If a section asks "what do you predict?",
  the paragraph after it must not say. Put the answer behind a `<Reveal>`.
- **Blank the givens.** Tables with a worked example: leave exactly one row filled as
  a model and blank the rest, then a `<Reveal>` with the completed table. Lesson 2's
  angle table and M5 L3's Dijkstra trace are the references.
- **Videos are answers too.** Where a video shows the outcome of a prediction, the
  caption says "press play once you've committed to a prediction" rather than
  describing what happens (M1 L6).
- **Don't demonstrate on the same data they just traced.** M5 L3 teaches path
  reconstruction on a throwaway 1×3 strip, then sends students back to their own
  table. Reuse of the activity's own numbers is a spoiler even when it reads like
  teaching.
- **Reference programs are teacher copies.** M4 L9's main program, M4 L6's expected
  `run_test` values and M2 L10's complete program are `<TeacherNote title="… (teacher
  copy)">`; the student page keeps a comment-only skeleton describing the shape.
- **Reveals get a hint.** The `hint` prop ("try it first", "fill the table in
  first") prints next to the closed title and is the thing that actually stops a
  student opening it reflexively.

**Lessons touched by this pass:** M1 L2, L3, L5, L6, L7, L9; M2 L4, L6, L10; M3 L4;
M4 L1, L4, L6, L8, L9; M5 L1, L3, L8. If you write a new lesson, apply the table
above as you go — it's much cheaper than another audit.

**Known remaining softness:** M4 L1's "Map it" activity and the knowledge check
below it are close enough that a student can read one off the other; the coordinates
were changed so they no longer coincide, but the two are still adjacent.

## 16. The 2026-09-18 repo split (how this repo came to exist)

The site started as `curriculum-site/` inside `IntoToPython`, alongside the source
curriculum. Brad split it out once it was clearly its own project.

**What was done, in case it ever needs repeating or explaining:**

```bash
# in IntoToPython — extract the 35 commits that touched curriculum-site,
# rewritten so its files sit at the repo root
git subtree split --prefix=curriculum-site -b curriculum-site-only

# in the new, empty LearningPython repo (which had one stub "first commit")
git fetch <path-to-IntoToPython> curriculum-site-only:imported
git rebase --onto main --root imported -X theirs   # -X theirs: site README wins
git checkout main && git merge --ff-only imported && git branch -d imported
```

Result: linear history, Brad's `first commit` at the root, then all 35 site
commits on top, and a push that fast-forwards (no force-push needed). The
resulting tree hash matched `IntoToPython`'s `HEAD:curriculum-site` exactly, so
nothing was lost or altered in the move.

**What deliberately did NOT come along** (it stays in `IntoToPython`): the source
markdown (`module-01-driving/` … `module-05-dijkstra/` with lesson plans,
worksheets, starter/solution code and slides), the `generate_pptx_*.py` deck
scripts, `course-outline.md`, `Module 1 Content Roadmap.md`, the
`student-guide/`, `teacher-guide/`, `templates/` and `tools/` folders, and
`XRPLib_API_Reference.md`. §2 of this file says where to find them; several are
worth reading when a lesson's source intent is in question.

**Still standing open after the split:**

- `curriculum-site/` is still present in `IntoToPython` (Brad chose to leave it
  until the new repo is proven). Once he's happy, it should be deleted there in
  its own commit with a pointer to this repo, so the two copies can't drift.
- The `curriculum-site-only` branch is still in `IntoToPython` too; it's disposable
  (`git branch -D curriculum-site-only`).
- ~~Netlify was never connected~~ — settled 2026-09-18: publishing goes through
  GitHub Pages instead, `netlify.toml` deleted, and the site is live at its own
  subdomain (§8).
- `IntoToPython` commits with a local identity of `Brad Miller <brad@example.com>`,
  which doesn't link to Brad's GitHub account. This repo is set to
  `bradamiller <brad@bradhouse.com>` to match his own first commit. The imported
  commits keep their original author (`brad@example.com`); only the committer is
  the new identity.

## 17. The pacing guide (/pacing)

Added 2026-09-19. A teacher-facing planning page, generated from the lessons the
same way the printable checks are — nothing is authored twice, so it can't drift.

```
docs/**/lesson-*.mdx  --scripts/extract_pacing.js-->  src/data/pacing.json
                      --src/components/Pacing.js-->   /pacing
```

**What it reads out of each lesson:** the chips in `<LessonHeader meta={[...]}/>`
(the duration and the phase), the `## Activity ·` and `## Challenge N ·`
headings, whether there's a `<QuizLink>`, and the `<KnowledgeCheck>` count. The
page is `src/pages/pacing.mdx` — a hand-written intro (materials, robot ratios,
where the natural pauses are) around a `<PacingGuide />`. `pacing.json` is
gitignored; `npm run pacing` regenerates it and `prestart`/`prebuild` run it.

**Numbers as of 2026-09-21** (L1-9 added): 46 lessons, 2295–2525 minutes of
estimated class time (38–42 hours), 60 hand-in activities, 189 knowledge checks.
At 50-minute periods that's 50–54 periods including the two multi-day capstones
at an assumed 2 periods each — about 17–18 weeks at three periods a week, which
is where the home page's "18 weeks" comes from. These are regenerated on every
build; don't hand-edit them, re-read `extract_pacing`'s output.

**Conventions the extractor depends on** (break these and the guide goes wrong,
loudly — it exits non-zero and names the file):

- Every lesson has a duration chip in its header meta: `'50–60 min'`, `'90 min'`,
  or `'Multi-day'` for a capstone. A range becomes lo–hi; `Multi-day` is counted
  separately rather than given invented minutes.
- Hand-in work is an `h2` of the form `## Activity · Name` or
  `## Challenge 1 · Name`. That's the same convention the DO THIS badge keys on
  (§9), so one rule serves both.

**It doubles as a coverage report.** Lessons with no hand-in activity show a dash
in the table, which is how M2 L8 (introduction-to-classes) and M1 L7 stand out —
L7 turned out to have challenges rather than activities, and the extractor was
fixed to count those. M4's overview page legitimately has none.

**If you add a module,** add it to `MODULE_ORDER` and `MODULE_TITLES` at the top
of `scripts/extract_pacing.js` (the same pair exists in `extract_checks.js`).

## 18. The "How this course works" page

Added 2026-09-19 (Brad's philosophy + materials). `docs/how-this-course-works.mdx`
sits at the TOP of the sidebar, above Module 1 — student-visible on purpose:
Brad's call was that none of it is harmful to share, and the experiential
principle in particular works better as a contract with students than as a
technique applied to them.

**The big ideas it states, in Brad's words (2026-09-19) — these are course
design intent, not decoration, so don't contradict them in a lesson:**

1. **Reuse is the spine.** Each module's code is reused by the next: Module 1's
   driving → Module 2's line tracking → Module 3's intersection-to-intersection
   driving → Module 4's navigator → Module 5's planner swap. The end state is a
   complex program nobody wrote in one go. Writing reusable code is presented as
   a real programming skill, and the practical payoff is that every step stays
   small.
2. **Each reusable part is an object** — and that's as far as the OOP goes. This
   is NOT an OOP course; the aim is a feel for how a program can be structured.
3. **The swap is the payoff.** `Manhattan` and `Dijkstra` answer the same request,
   so the navigator doesn't care which it holds: get Manhattan working, then hand
   it a Dijkstra with almost no other change. The site keeps this promise as of
   2026-09-19 — both planners exclude the start from the path they return (§9).
4. **Planners are testable without a robot** — they're arithmetic that returns a
   list of intersections. M4 L6 is the worked example.

**Three stated cut points** (also in §9 terms): skip classes and write the same
components as functions (loses the planner swap, keeps everything else); stop
after Manhattan; or teach Dijkstra without the drive-time blocked-intersection
discovery. Note the site currently teaches the class route only — the
functions-first material exists in the source repo and is the deferred rework in
§9, so the page describes the choice as design intent rather than promising
parallel pages.

**Materials list contents** are Brad's (2026-09-19): robots and ratios, browsers,
data USB cables and the first USB pass, floor space, **whiteboard panels** from a
hardware store (a driving surface that works on the floor or across tables, and
the surface the robot draws on with a marker — **Brad is supplying specific panel
recommendations, still TBD**), **dry-erase markers** that fit the robot's marker
holder, tape for floor line courses, and **rechargeable AAs with a charger bank
and two boxes** (charged / needs charging) so a flat robot is a swap, not a lost
period.

**Shared materials list.** `docs/_partials/materials.mdx` is imported by BOTH
this page and `src/pages/pacing.mdx` — one file, two renderings, so they can't
drift. Docusaurus ignores `docs/_partials/`, and an `@site/docs/_partials/…`
import works from `src/pages` as well as from a docs page (verified). Both
extractors now skip `_`-prefixed files and folders; before that, `extract_pacing`
counted the partial as a 46th lesson and failed the build.
