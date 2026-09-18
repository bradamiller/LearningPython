#!/usr/bin/env node
/**
 * Pull every <KnowledgeCheck> out of the lesson .mdx files into
 * src/data/checks.json, which the printable quiz sheets render from.
 *
 * The lesson file stays the SINGLE SOURCE OF TRUTH: edit a question where it is
 * taught, re-run this, and the printable sheet follows. Nothing is written back
 * into the lessons.
 *
 * Run by `npm start` / `npm run build` automatically (prestart / prebuild).
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const DOCS = path.join(ROOT, 'docs');
const OUT = path.join(ROOT, 'src', 'data', 'checks.json');

const MODULE_TITLES = {
  'module-01-driving': 'Module 1 · Learning to Drive',
  'module-02-line-tracking': 'Module 2 · Line Tracking',
  'module-03-grid-driving': 'Module 3 · Grid Driving',
  'module-04-manhattan': "Module 4 · Manhattan Navigation",
  'module-05-dijkstra': "Module 5 · Dijkstra's Algorithm",
};

/** Front matter value, e.g. title: "Lesson 1 · Meet the XRP" */
function frontMatter(src, key) {
  const m = src.match(new RegExp(`^${key}:\\s*"?(.*?)"?\\s*$`, 'm'));
  return m ? m[1] : null;
}

/**
 * The text of every <KnowledgeCheck ... /> element, in document order.
 *
 * Scanning for the closing "/>" needs a little JSX awareness: an attribute is
 * either "a double-quoted string" — where an apostrophe is just prose ("isn't")
 * — or {a braced expression}, where both quote characters are real string
 * delimiters and braces nest. Treating every apostrophe as a delimiter silently
 * swallows the following questions.
 */
function checkBlocks(src) {
  const blocks = [];
  let i = 0;
  while ((i = src.indexOf('<KnowledgeCheck', i)) !== -1) {
    let j = i + '<KnowledgeCheck'.length;
    let mode = 'tag';        // 'tag' | 'dq' | 'expr'
    let depth = 0;           // brace/bracket depth while in 'expr'
    let quote = null;        // active quote char while in 'expr'

    while (j < src.length) {
      const c = src[j];
      if (mode === 'dq') {
        if (c === '"') mode = 'tag';
      } else if (mode === 'expr') {
        if (quote) {
          if (c === '\\') j++;
          else if (c === quote) quote = null;
        } else if (c === '"' || c === "'") {
          quote = c;
        } else if (c === '{' || c === '[') {
          depth++;
        } else if (c === '}' || c === ']') {
          depth--;
          if (depth === 0) mode = 'tag';
        }
      } else if (c === '"') {
        mode = 'dq';
      } else if (c === '{') {
        mode = 'expr';
        depth = 1;
      } else if (c === '/' && src[j + 1] === '>') {
        break;
      }
      j++;
    }
    blocks.push(src.slice(i, j + 2));
    i = j + 2;
  }
  return blocks;
}

/** A quoted JSX attribute: prop="..." or prop={'...'} */
function stringProp(block, name) {
  const dq = block.match(new RegExp(`${name}="([^"]*)"`));
  if (dq) return dq[1];
  const expr = block.match(new RegExp(`${name}=\\{'((?:[^'\\\\]|\\\\.)*)'\\}`));
  if (expr) return expr[1].replace(/\\'/g, "'");
  return null;
}

/** options={[ {text: '…', correct: true}, … ]} — evaluated as the JS it is. */
function optionsProp(block) {
  const start = block.indexOf('options={');
  if (start === -1) return null;
  let i = start + 'options={'.length;
  let depth = 1;
  let quote = null;
  while (i < block.length && depth > 0) {
    const c = block[i];
    if (quote) {
      if (c === '\\') i++;
      else if (c === quote) quote = null;
    } else if (c === '"' || c === "'") quote = c;
    else if (c === '{' || c === '[') depth++;
    else if (c === '}' || c === ']') depth--;
    i++;
  }
  const literal = block.slice(start + 'options={'.length, i - 1);
  // eslint-disable-next-line no-new-func
  return new Function(`return ${literal}`)();
}

function lessonId(moduleDir, file) {
  return `${moduleDir}/${file.replace(/\.mdx$/, '')}`;
}

function main() {
  const data = {};
  let total = 0;
  const problems = [];

  for (const moduleDir of fs.readdirSync(DOCS).filter((d) => d.startsWith('module-')).sort()) {
    const files = fs
      .readdirSync(path.join(DOCS, moduleDir))
      .filter((f) => f.endsWith('.mdx'))
      .sort();

    for (const file of files) {
      const full = path.join(DOCS, moduleDir, file);
      const src = fs.readFileSync(full, 'utf8');
      const checks = [];

      for (const block of checkBlocks(src)) {
        const question = stringProp(block, 'question');
        const explanation = stringProp(block, 'explanation');
        const options = optionsProp(block);
        if (!question || !options || !options.length) {
          problems.push(`${moduleDir}/${file}: could not parse a KnowledgeCheck`);
          continue;
        }
        if (options.filter((o) => o.correct).length !== 1) {
          problems.push(`${moduleDir}/${file}: "${question.slice(0, 50)}…" needs exactly one correct option`);
        }
        checks.push({question, options, explanation});
      }

      if (!checks.length) continue;
      total += checks.length;
      data[lessonId(moduleDir, file)] = {
        module: moduleDir,
        moduleTitle: MODULE_TITLES[moduleDir] || moduleDir,
        lessonTitle: frontMatter(src, 'title') || file,
        sidebarLabel: frontMatter(src, 'sidebar_label') || '',
        docPath: `/${moduleDir}/${file.replace(/\.mdx$/, '')}`,
        checks,
      };
    }
  }

  if (problems.length) {
    console.error('Knowledge-check extraction problems:');
    problems.forEach((p) => console.error('  - ' + p));
    process.exitCode = 1;
  }

  fs.mkdirSync(path.dirname(OUT), {recursive: true});
  fs.writeFileSync(OUT, JSON.stringify(data, null, 2) + '\n');
  console.log(
    `extract_checks: ${total} knowledge checks from ${Object.keys(data).length} lessons → src/data/checks.json`
  );
}

main();
