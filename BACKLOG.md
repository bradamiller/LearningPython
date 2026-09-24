# Backlog — deferred work

Things worth doing that are deliberately **not** being done yet, with enough
detail that picking one up later doesn't mean redoing the research.

Defects are not here — those live in `REVIEW-2026-09-21.md`, and the ones still
open are flagged in the lessons themselves as `<Todo>` notes (`npm run todos`).
This file is for features and decisions.

---

## 1. Site search

**Brad, 2026-09-23: wanted, but after the course is closer to finished.**

Docusaurus ships **no search**. It's a plugin choice, and there are three routes.

**Algolia DocSearch** is the official one, free for developer-documentation
sites, and it's an application-and-approval process with a hosted crawler that
needs the site publicly reachable. Good service; it puts a third party and a
queue between us and a working search box.

**A local plugin** builds the index at build time and ships it inside the site.
`@easyops-cn/docusaurus-search-local` is the mature one for Docusaurus 3. No
account, no approval, no external service, works on GitHub Pages unchanged — and
it keeps working once a page has loaded on bad classroom wifi, which matters more
here than on most docs sites. 46 lessons is a small index.

**Typesense DocSearch** is the self-hosted middle ground; more infrastructure
than this site justifies.

**Recommendation: the local plugin.**

### The thing that must not be missed

Search indexes the **rendered page**, and this site deliberately ships content
students aren't meant to read:

- **Teacher notes** are in the HTML, hidden only by CSS. Un-filtered, a student
  searching a distinctive phrase gets hits inside teacher-only guidance.
- **`<Todo>` notes** are in the HTML on the same terms (see `CLAUDE.md` §10b).
- **Answer keys** at `/checks/…-key` are already public URLs but unlinked and
  undiscoverable. Indexing them changes "public if you guess the URL" into
  "first hit for the word *answer*." That's a real change in exposure, not a
  cosmetic one.

The plugin has the hooks for all three:

| Option | Use it for |
|---|---|
| `ignoreCssSelectors` | drop `.teacherNote`, `.teacherBanner`, `.todo` from the index |
| `ignoreFiles` | keep the `/checks/…-key` routes out entirely |
| `searchContextByPaths` | if a second, teacher-facing search context is wanted |

**Open question for Brad:** should teachers get a *second* search that does reach
teacher notes? `searchContextByPaths` is the mechanism. It would be
obfuscation, not security — the same bargain teacher mode already makes.

**Acceptance check when this is built:** build the site, search for a phrase that
exists only inside a `<TeacherNote>`, and get no result. Then search a phrase from
a lesson body and get the right lesson.

---

## 2. PDF export — lesson, module, whole curriculum

**Brad, 2026-09-23: wanted, but after the course is closer to finished.**

Docusaurus has **no PDF export**.

**What already works, with no code:** `Cmd+P` on any lesson. The print styling is
already in place — closed `<Reveal>` blocks stay closed, and `.todo` is
`display: none` in `@media print`. Worth knowing so nobody thinks PDFs are
blocked on this backlog item.

**What not to use:** `docusaurus-prince-pdf` is the common recommendation, but it
depends on **Prince XML**, a licensed commercial renderer. Its pricing page lists
only paid licences (academic is $1,900 one-time). Prince has historically also
offered a free non-commercial build that stamps a watermark on the first page —
**verify current terms before relying on that**, because the purchase page doesn't
mention it. Either way it's a dependency this repo doesn't need.

**What to build instead:** a generator beside the existing ones — `npm run pdf` —
using the Chromium already installed for the Playwright checks
(`/opt/pw-browsers/chromium-*/chrome-linux/chrome`, `PLAYWRIGHT_BROWSERS_PATH` is
already set; don't run `playwright install`).

Sketch:

1. `npm run build`, serve `build/` locally.
2. Read the lesson order from `sidebars.js` — it's the explicit `items` list, so
   it's already the authoritative order, same source the pacing guide uses.
3. For each lesson, `page.pdf()` to `pdf/lessons/<module>/<lesson>.pdf`.
4. Merge per module and once for the whole course (`pdf-lib`, or `pypdf`).
5. Generate a contents page from the same `sidebars.js` order, with the
   `module-lesson` numbering.

Two things this gets that a print dialog can't:

- **Student and teacher editions of the same lesson.** Set
  `document.documentElement.setAttribute('data-teacher', 'on')` before printing
  for the teacher edition. Everything else is identical, so it's one extra pass,
  not a second pipeline.
- **A real table of contents**, and stable file names that can be handed out.

Build it with `SHOW_TODOS=0` (see `CLAUDE.md` §10b) so authoring notes can't reach
a printed handout.

**Watch for:** lazy-loaded images (wait for `networkidle` and scroll the page
before printing), code blocks breaking across pages, and the two floating toggle
switches — hide `.teacherToggle` in print CSS or they'll appear on every page.

---

## 3. Decisions parked elsewhere

Not duplicated here — this is the index so nothing gets lost.

| What | Where it's written up |
|---|---|
| `turn_right()` doesn't clear the intersection — needs a robot on a grid | `REVIEW-2026-09-21.md` §1.2, and a `TODO-BLOCKED` in L3-3 |
| `base_effort` drifting 0.3 → 0.4 between L2-5 and L2-9/L2-10 | `REVIEW` §4, `TODO-CONVENTION` in L2-9. (The `Kp` vs `kp` half of this was settled 2026-09-24: `Kp` everywhere, with the engineering-notation exception explained in L2-5.) |
| Whether Module 5 should end with a program that actually drives the grid | `REVIEW` §2 (the rest of which was settled 2026-09-24 — obstacles moved to `set_blocked_intersections`, so the two planners are now created identically), `TODO-BUG` in L5-9 |
| Answer-leak pass across Modules 2–5 | `REVIEW` §3, seven `TODO-ANSWERS` notes |
| Whether `abs()` belongs in L4-4's distance work | Brad, 2026-09-24. L4-4 handles negative distances with four `while` loops and explicitly rejects `abs()`. L4-2's teacher note used to promise `abs()` was coming, which was simply wrong, so the promise is gone. If `abs()` is later brought into L4-4, put the preview back in that note. |
| A separate teacher guide instead of teacher mode | discussed 2026-09-20; Brad thinking about it |
| Whiteboard panel recommendations for the materials list | Brad to supply |
| Source-repo sync — `IntoToPython` is behind on naming, Lesson 0, stop-motors | `CLAUDE.md` §11 |
| Real block screenshots for the lessons still on composed art | `CLAUDE.md` §11 |
