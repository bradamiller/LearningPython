#!/usr/bin/env node
/**
 * List the TODO markers embedded in the lessons.
 *
 *   npm run todos               — everything, grouped by module
 *   npm run todos -- bug        — only one category
 *   npm run todos -- --count    — just the tallies
 *   npm run todos -- --compact  — one line each, for the VS Code task
 *
 * A TODO is an MDX comment, so it never reaches a rendered page:
 *
 *   {\/* TODO-CATEGORY: what is wrong — what to do about it. [REVIEW §N] *\/}
 *
 * Categories, in the order they're worth attention:
 *   bug         something is wrong and a student can hit it
 *   blocked     needs a decision or a robot before it can be fixed
 *   answers     an answer is visible where it shouldn't be
 *   convention  drifts from a rule the course follows elsewhere
 *   media       a placeholder or a stand-in image
 */
const fs = require('fs');
const path = require('path');

const DOCS = path.join(__dirname, '..', 'docs');
const ORDER = ['bug', 'blocked', 'answers', 'convention', 'media'];
const LABEL = {
  bug: 'BUG        ',
  blocked: 'BLOCKED    ',
  answers: 'ANSWERS    ',
  convention: 'CONVENTION ',
  media: 'MEDIA      ',
};

function walk(dir) {
  return fs.readdirSync(dir, {withFileTypes: true}).flatMap((e) => {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) return walk(p);
    return e.name.endsWith('.mdx') && !e.name.startsWith('_') ? [p] : [];
  });
}

const found = [];
for (const file of walk(DOCS).sort()) {
  const lines = fs.readFileSync(file, 'utf8').split('\n');
  lines.forEach((line, i) => {
    const m = line.match(/\{\/\*\s*TODO-([A-Z]+):\s*([\s\S]*?)\s*\*\/\}/);
    if (m) {
      found.push({
        file: path.relative(path.join(__dirname, '..'), file),
        line: i + 1,
        category: m[1].toLowerCase(),
        text: m[2].replace(/\s+/g, ' '),
      });
    }
  });
}

const args = process.argv.slice(2);
if (args.includes('--compact')) {
  // One line per TODO: "path:line: CATEGORY: message".
  // The VS Code task's problemMatcher parses exactly this shape.
  for (const t of found) {
    console.log(`${t.file}:${t.line}: ${t.category.toUpperCase()}: ${t.text}`);
  }
  process.exit(0);
}
const [filter] = args;
const counts = {};
for (const t of found) counts[t.category] = (counts[t.category] || 0) + 1;

if (filter === '--count') {
  for (const c of ORDER) if (counts[c]) console.log(`${LABEL[c]} ${counts[c]}`);
  console.log(`${'TOTAL      '} ${found.length}`);
  process.exit(0);
}

const shown = filter ? found.filter((t) => t.category === filter) : found;
if (filter && !shown.length) {
  console.log(`No TODOs in category "${filter}". Known: ${ORDER.join(', ')}`);
  process.exit(0);
}

let lastModule = null;
// Most-urgent category first, then by file so a lesson's TODOs stay together.
shown.sort(
  (a, b) =>
    ORDER.indexOf(a.category) - ORDER.indexOf(b.category) ||
    a.file.localeCompare(b.file) ||
    a.line - b.line,
);
let lastCategory = null;
for (const t of shown) {
  if (t.category !== lastCategory) {
    console.log(`\n=== ${LABEL[t.category].trim()} ===`);
    lastCategory = t.category;
    lastModule = null;
  }
  const mod = path.dirname(t.file);
  if (mod !== lastModule) {
    console.log(`\n  ${mod}`);
    lastModule = mod;
  }
  const name = path.basename(t.file);
  console.log(`    ${name}:${t.line}`);
  // Wrap the body so a long note stays readable in a terminal.
  const words = t.text.split(' ');
  let out = '     ';
  for (const w of words) {
    if ((out + ' ' + w).length > 94) {
      console.log(out);
      out = '     ';
    }
    out += ' ' + w;
  }
  if (out.trim()) console.log(out);
}

console.log('\n' + '-'.repeat(60));
for (const c of ORDER) if (counts[c]) console.log(`${LABEL[c]} ${counts[c]}`);
console.log(`${'TOTAL      '} ${found.length}   (details in REVIEW-2026-09-21.md)`);
