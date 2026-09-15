# XRP Python Curriculum — Web Site

A VEX STEM Labs-style web version of the XRP Python curriculum, built with
[Docusaurus](https://docusaurus.io/). **All five modules are built — 44 lessons:**
Module 1 · Learning to Drive (11), Module 2 · Line Tracking (10), Module 3 · Grid
Driving (4), Module 4 · Manhattan Navigation (overview + 9), and Module 5 ·
Dijkstra's Algorithm (9). See `CLAUDE.md` for the full project spec, conventions,
and open items.

## What the site provides

- **Sidebar + breadcrumb + prev/next navigation** across modules and lessons
- **Colored lesson header** band with duration / phase metadata
- **Teacher-mode toggle** — the floating switch (bottom-right). Off = student
  view; on = reveals gray Teacher Notes and the teacher banner. The choice is
  remembered in the browser.
- **Knowledge checks** — interactive multiple-choice / true-false questions with
  instant color-coded feedback and a "try again" reset
- **Video and image placeholders** — labeled drop-in spots; add a `src` to embed
  the real media later
- **Real XRP Blockly block images** — Module 1 sample programs are built from the
  actual block graphics (from the XRP User Guide); Modules 2–5 are all Python

## Style conventions (enforced across lessons)

- **Phases (Module 1):** A · Blockly Foundation (lessons 1–5), B · Driving
  Challenges (6–7), C · Transition to Python (8–11) — shown in each lesson header.
- **Function names carry from Blockly to Python unchanged:** `draw_square(size)`,
  `draw_triangle(size)`, `draw_polygon(sides, size, effort)`. The Blockly and Python
  versions of a function have the same name and the same parameters, in the same
  order.
- **Real XRP block vocabulary:** Straight (cm, Effort 0–1), Turn (Deg, Effort),
  Sleep (seconds), Stop motors, Wait for button press — never "power %".
- **Every robot program starts with Wait for button press** (programs run the
  moment they upload).
- **Python editor:** VS Code with the MicroPython extension (Blockly is XRP Code in
  the browser).
- **Paper before code:** each lesson that introduces an idea has a short
  student-facing "on paper first" / "say it in English first" step before building.
- **3–4 learning objectives per lesson.**

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
- `static/img/` and `static/videos/` — where your graphics and videos go.

## Authoring a lesson

Each lesson is plain Markdown with a few custom tags. See
`docs/module-01-driving/lesson-01-meet-the-xrp.mdx` for a complete worked
example. The available tags:

```mdx
<LessonHeader eyebrow="Module 1 · Learning to Drive" title="Lesson 1 · Meet the XRP"
  meta={['50–60 min', 'Phase A', 'No experience needed']} />

<Objectives> ...bulleted list... </Objectives>

<TeacherNote title="Timing tip"> ...teacher-only guidance... </TeacherNote>

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
```

## Deploying (Netlify)

The site builds to static HTML in `build/`, so it hosts free on Netlify. Two ways:

### A. Instant link (no account setup, throwaway URL)

```bash
npm install      # first time only
npm run build
```

Then drag the `build/` folder onto **https://app.netlify.com/drop**. Netlify
gives you a public URL (e.g. `something.netlify.app`) to share immediately. To
update it, re-run the build and drag again.

### B. Auto-deploy on every push (recommended for ongoing review)

1. Commit and push this `curriculum-site` folder to GitHub:
   ```bash
   git add curriculum-site
   git commit -m "Add curriculum website"
   git push
   ```
2. In Netlify: **Add new site → Import an existing project → GitHub**, pick the
   `IntoToPython` repo.
3. Set **Base directory** to `curriculum-site`. The build command
   (`npm run build`) and publish path (`build`) come from `netlify.toml`
   automatically.
4. Deploy. Every push to GitHub now rebuilds the live site.

The site is served at the domain root, so `baseUrl` stays `/` (no change needed).
Once you know the final URL you can set `url` in `docusaurus.config.js` to it (only
affects SEO/sitemap metadata).

### Other hosts

Vercel and Cloudflare Pages work the same way — connect the repo, set the root/base
directory to `curriculum-site`. For **GitHub Pages**, change `baseUrl` to
`/IntoToPython/` first (project sites serve from a subpath) and add a build
workflow.
