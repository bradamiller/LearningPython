#!/usr/bin/env node
/**
 * Fail the build if any fenced code block contains a non-ASCII character.
 *
 * Why this exists
 * ---------------
 * Brad hit this on 2026-09-29: a `←` sitting in a comment inside a ```python
 * block in M2 L2. It renders beautifully on the page, so nothing looked wrong —
 * but a student's job is to COPY that block into XRP Code, and the editor
 * rejected the character. A whole class can lose ten minutes to a bug that is
 * invisible to whoever wrote it.
 *
 * A sweep found 86 such lines across 27 lessons: arrows, em dashes, middots,
 * `×`, `÷`, `≠`, `≈`, `°` and a Unicode minus sign. Every one had been typed
 * because it looked nicer in prose — and prose is exactly where it belongs.
 *
 * The rule: **inside a code fence, ASCII only.** Write `<-` and `->` for arrows,
 * `--` for a dash, `!=` for not-equal, `x` for times, `deg` for degrees. Save
 * the real typography for the paragraphs around the block, where nobody is
 * going to paste it into an editor.
 *
 * This runs from prestart/prebuild, so a bad character can never reach the
 * deployed site.
 */

const fs = require('fs');
const path = require('path');

const DOCS = path.join(__dirname, '..', 'docs');

// The replacements we settled on, so the error message can suggest one rather
// than leaving the author to guess.
const SUGGEST = {
  '←': '<-', '→': '->', '—': '--', '–': '-',
  '·': '-',  '×': 'x',  '≠': '!=', '÷': '/',
  '−': '-',  '≈': '~',  '°': ' deg', '…': '...',
  '“': '"',  '”': '"',  '‘': "'",  '’': "'",
};

function walk(dir, out = []) {
  for (const e of fs.readdirSync(dir, {withFileTypes: true})) {
    if (e.name.startsWith('_')) continue;            // partials, like the extractors
    const full = path.join(dir, e.name);
    if (e.isDirectory()) walk(full, out);
    else if (e.name.endsWith('.mdx')) out.push(full);
  }
  return out;
}

const problems = [];

for (const file of walk(DOCS)) {
  const rel = path.relative(path.join(__dirname, '..'), file);
  let inFence = false;
  fs.readFileSync(file, 'utf8').split('\n').forEach((line, idx) => {
    if (line.trimStart().startsWith('```')) { inFence = !inFence; return; }
    if (!inFence) return;
    const bad = [...new Set([...line].filter((c) => c.charCodeAt(0) > 127))];
    if (bad.length) {
      const fixes = bad
        .map((c) => `${JSON.stringify(c)} (U+${c.codePointAt(0).toString(16).toUpperCase().padStart(4, '0')})`
                    + (SUGGEST[c] ? ` -> write ${JSON.stringify(SUGGEST[c])}` : ''))
        .join(', ');
      problems.push(`${rel}:${idx + 1}\n    ${line.trim()}\n    ${fixes}`);
    }
  });
}

if (problems.length) {
  console.error(
    `\nNon-ASCII characters inside code fences (${problems.length} line${problems.length > 1 ? 's' : ''}).\n` +
    `Students copy these blocks into XRP Code, and the editor rejects them.\n` +
    `Use the ASCII spelling in code; keep the real typography for the prose.\n\n` +
    problems.join('\n\n') + '\n');
  process.exit(1);
}

console.log('Code fences are ASCII-clean.');
