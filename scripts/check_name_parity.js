#!/usr/bin/env node
/**
 * Fail the build if a class method in an <OptionalExtension> has no function of
 * the same name, with the same parameters minus `self`, in the same lesson's
 * primary content.
 *
 * Why this exists
 * ---------------
 * Decision D8 in IntoToPython/teacher-guide/course-design-decisions.md (Brad,
 * 2026-10-14). Classes are optional: the functions track is the lesson, and the
 * class version lives in an OptionalExtension whose methods are named exactly
 * like the functions (LineSensor.get_left() <-> get_left()), so a student can
 * move between tracks without relearning names. Drift between the two copies
 * is the real ongoing cost of the extensions, and this check is cheaper than
 * catching it in class.
 *
 * What it compares: every `def name(self, ...)` inside an <OptionalExtension>
 * against every `def name(...)` in a ```python fence outside one, anywhere in
 * the course (students keep one growing robot.py, so a function is often written
 * a lesson or two before its method appears). Parameter NAMES are compared, in
 * order; default values are ignored. Teacher copies count as primary content.
 * Dunder methods (`__init__` and friends) have no function twin and are skipped.
 *
 * The two differences D2/D3 make on purpose, and nothing else, are allowed:
 *   - State the class owns. A function parameter may be missing from the method
 *     when the class keeps it as `self.<name>` (Navigator owns position and
 *     heading, so drive_path(path, position, heading) is drive_path(self, path)).
 *     That is the "shared variables move into __init__ as self.x" step of the
 *     side-by-side.
 *   - The planner swap. Every planner class has compute_path(self, position,
 *     destination), and its function twin is named for the planner:
 *     compute_manhattan_path, compute_bfs_path, compute_dijkstra_path.
 *
 * Runs from prestart/prebuild next to check_code_ascii.js and check_extensions.js.
 */

const fs = require('fs');
const path = require('path');

const DOCS = path.join(__dirname, '..', 'docs');

function walk(dir, out = []) {
  for (const e of fs.readdirSync(dir, {withFileTypes: true})) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p, out);
    else if (/\.mdx?$/.test(e.name)) out.push(p);
  }
  return out;
}

// Split a file into text inside <OptionalExtension ...>...</OptionalExtension>
// and text outside it.
function split(src) {
  const inside = [], outside = [];
  const re = /<OptionalExtension\b[\s\S]*?<\/OptionalExtension>/g;
  let last = 0, m;
  while ((m = re.exec(src))) {
    outside.push(src.slice(last, m.index));
    inside.push(m[0]);
    last = m.index + m[0].length;
  }
  outside.push(src.slice(last));
  return {inside: inside.join('\n'), outside: outside.join('\n')};
}

// Every `def name(params)` in the python fences of a chunk of MDX.
function defs(text) {
  const out = [];
  const fence = /```python[^\n]*\n([\s\S]*?)```/g;
  let f;
  while ((f = fence.exec(text))) {
    const d = /^\s*def\s+([A-Za-z_]\w*)\s*\(([^)]*)\)/gm;
    let m;
    while ((m = d.exec(f[1]))) {
      const params = m[2].split(',').map(s => s.trim()).filter(Boolean)
        .map(s => s.split(/[=:]/)[0].trim());
      out.push({name: m[1], params});
    }
  }
  return out;
}

const files = walk(DOCS);
const funcs = [];
for (const file of files) funcs.push(...defs(split(fs.readFileSync(file, 'utf8')).outside).filter(d => d.params[0] !== 'self'));
const problems = [];
for (const file of files) {
  const src = fs.readFileSync(file, 'utf8');
  if (!src.includes('<OptionalExtension')) continue;
  const {inside} = split(src);
  const owned = new Set([...inside.matchAll(/\bself\.([A-Za-z_]\w*)/g)].map(m => m[1]));
  for (const m of defs(inside)) {
    if (m.params[0] !== 'self' || /^__.*__$/.test(m.name)) continue;
    const want = m.params.slice(1).join(', ');
    const twins = funcs.filter(f => f.name === m.name ||
      (m.name === 'compute_path' && /^compute_\w+_path$/.test(f.name)));
    const matches = f => f.params.filter(p => !(owned.has(p) && !m.params.includes(p))).join(', ') === want;
    const rel = path.relative(path.join(__dirname, '..'), file);
    if (!twins.length) {
      problems.push(`${rel}: method ${m.name}(self${want ? ', ' + want : ''}) has no function ${m.name}(${want}) anywhere in the course`);
    } else if (!twins.some(matches)) {
      problems.push(`${rel}: method ${m.name}(self${want ? ', ' + want : ''}) but the function is ${twins[0].name}(${twins[0].params.join(', ')})`);
    }
  }
}

if (problems.length) {
  console.error('check_name_parity: class methods and functions have drifted apart (D8):\n');
  for (const p of [...new Set(problems)]) console.error('  ' + p);
  console.error('\nRename one side so each method matches a function of the same name and parameters (minus self).');
  process.exit(1);
}
console.log('check_name_parity: every extension method has a matching function');
