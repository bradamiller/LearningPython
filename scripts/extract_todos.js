#!/usr/bin/env node
/**
 * Build src/data/todos.json — the data behind the /todos index page.
 *
 * Same contract as extract_checks.js and extract_pacing.js: the notes are
 * authored once, in the lessons, and everything else is derived. Nothing is
 * written twice, so the index cannot drift from the course.
 *
 * Each note gets a number within its own lesson, and the SAME numbering is
 * stamped onto the rendered element by plugins/remark-number-todos.js, which
 * walks the file in document order exactly as this does. That shared ordering
 * is what makes /todos → #todo-N land on the right note. If you change how
 * either one counts, change both.
 *
 * Run automatically by `npm start` / `npm run build` (prestart / prebuild).
 *
 * SHOW_TODOS=0 builds a site with the notes stripped out of the lessons
 * entirely, so this emits an empty index to match — otherwise the one page
 * that lists every unfinished thing in the course would survive the strip.
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const DOCS = path.join(ROOT, 'docs');
const OUT = path.join(ROOT, 'src', 'data', 'todos.json');

const STRIPPED = process.env.SHOW_TODOS === '0';

const MODULE_ORDER = [
  'module-01-driving',
  'module-02-line-tracking',
  'module-03-grid-driving',
  'module-04-manhattan',
  'module-05-dijkstra',
];

const MODULE_TITLES = {
  'module-01-driving': 'Module 1 · Learning to Drive',
  'module-02-line-tracking': 'Module 2 · Line Tracking',
  'module-03-grid-driving': 'Module 3 · Grid Driving',
  'module-04-manhattan': 'Module 4 · Manhattan Navigation',
  'module-05-dijkstra': "Module 5 · Dijkstra's Algorithm",
};

/** Most urgent first — the order the index and the counts are shown in. */
const CATEGORY_ORDER = ['bug', 'blocked', 'answers', 'convention', 'media'];

const CATEGORY_LABELS = {
  bug: 'Bug',
  blocked: 'Blocked',
  answers: 'Answer leak',
  convention: 'Convention',
  media: 'Media',
};

function frontMatter(src, key) {
  const m = src.match(new RegExp(`^${key}:\\s*"?(.*?)"?\\s*$`, 'm'));
  return m ? m[1] : null;
}

/** Lesson files only: `_`-prefixed files are partials (docs/_partials). */
function lessonFiles(dir) {
  const full = path.join(DOCS, dir);
  if (!fs.existsSync(full)) return [];
  return fs
    .readdirSync(full)
    .filter((f) => f.endsWith('.mdx') && !f.startsWith('_'))
    .sort();
}

const items = [];
const counts = {};

if (!STRIPPED) {
  for (const dir of MODULE_ORDER) {
    for (const file of lessonFiles(dir)) {
      const src = fs.readFileSync(path.join(DOCS, dir, file), 'utf8');
      const slug = file.replace(/\.mdx$/, '');
      const lessonTitle = frontMatter(src, 'title') || slug;
      const sidebarLabel = frontMatter(src, 'sidebar_label') || lessonTitle;

      const rx = /<Todo\s+kind="([a-z]+)"\s*>([\s\S]*?)<\/Todo>/g;
      let m;
      let onPage = 0;
      while ((m = rx.exec(src)) !== null) {
        onPage += 1;
        const category = CATEGORY_LABELS[m[1]] ? m[1] : 'bug';
        const raw = m[2].replace(/\s+/g, ' ').trim();
        // "… fix this. [REVIEW §2]" — pull the citation out so the card can
        // show it as a chip instead of trailing it in the sentence.
        const cite = raw.match(/\s*\[(REVIEW[^\]]*)\]\s*$/);
        items.push({
          n: items.length + 1,
          indexOnPage: onPage,
          anchor: `todo-${onPage}`,
          category,
          categoryLabel: CATEGORY_LABELS[category],
          text: cite ? raw.slice(0, cite.index).trim() : raw,
          cite: cite ? cite[1] : null,
          module: dir,
          moduleTitle: MODULE_TITLES[dir],
          lessonTitle,
          sidebarLabel,
          docPath: `/${dir}/${slug}`,
          file: `docs/${dir}/${file}`,
          line: src.slice(0, m.index).split('\n').length,
        });
        counts[category] = (counts[category] || 0) + 1;
      }
    }
  }
}

const data = {
  generatedAt: new Date().toISOString(),
  stripped: STRIPPED,
  total: items.length,
  categoryOrder: CATEGORY_ORDER,
  categoryLabels: CATEGORY_LABELS,
  counts,
  items,
};

fs.mkdirSync(path.dirname(OUT), {recursive: true});
fs.writeFileSync(OUT, JSON.stringify(data, null, 2) + '\n');

const tally = CATEGORY_ORDER.filter((c) => counts[c])
  .map((c) => `${counts[c]} ${c}`)
  .join(', ');
console.log(
  STRIPPED
    ? 'extract_todos: SHOW_TODOS=0 — empty index written → src/data/todos.json'
    : `extract_todos: ${items.length} notes (${tally}) → src/data/todos.json`,
);
