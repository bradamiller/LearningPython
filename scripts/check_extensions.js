#!/usr/bin/env node
/**
 * Fail the build if a markdown heading sits inside an <OptionalExtension>.
 *
 * Why this exists
 * ---------------
 * Found by Docusaurus's broken-anchor check on 2026-10-15. An OptionalExtension
 * is closed by default and does not render its children until clicked, but
 * Docusaurus builds the right-hand "On this page" outline from the MDX source —
 * so a `###` heading inside an extension puts an entry in the outline that
 * scrolls nowhere until the box is open. Three dead links on M2 L8, invisible
 * in the source, visible to every student who clicks them.
 *
 * The rule: **inside an extension, use bold text for sub-sections, never a
 * markdown heading.** The extension's own title is its heading.
 *
 * Runs from prestart/prebuild next to check_code_ascii.js.
 */

const fs = require('fs');
const path = require('path');

const DOCS = path.join(__dirname, '..', 'docs');

function walk(dir, out = []) {
  for (const e of fs.readdirSync(dir, {withFileTypes: true})) {
    if (e.name.startsWith('_')) continue;
    const full = path.join(dir, e.name);
    if (e.isDirectory()) walk(full, out);
    else if (e.name.endsWith('.mdx')) out.push(full);
  }
  return out;
}

const problems = [];

for (const file of walk(DOCS)) {
  const rel = path.relative(path.join(__dirname, '..'), file);
  let depth = 0, inFence = false;
  fs.readFileSync(file, 'utf8').split('\n').forEach((line, idx) => {
    const t = line.trimStart();
    if (t.startsWith('```')) { inFence = !inFence; return; }
    if (inFence) return;
    if (/<OptionalExtension\b/.test(t)) depth++;
    if (/<\/OptionalExtension>/.test(t)) depth = Math.max(0, depth - 1);
    if (depth > 0 && /^#{1,6}\s/.test(t)) {
      problems.push(`${rel}:${idx + 1}\n    ${t}`);
    }
  });
}

if (problems.length) {
  console.error(
    `\nMarkdown heading(s) inside an <OptionalExtension> (${problems.length}).\n` +
    `The page outline links to them, but a closed extension has no such anchor —\n` +
    `the link is dead until the box is opened. Use **bold text** instead.\n\n` +
    problems.join('\n\n') + '\n');
  process.exit(1);
}

console.log('No headings inside optional extensions.');
