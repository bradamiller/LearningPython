#!/usr/bin/env node
/**
 * Build src/data/pacing.json — the data behind the /pacing teacher guide.
 *
 * Everything here is already written in the lessons: the duration and phase
 * chips in <LessonHeader meta={[...]}/>, the "## Activity ·" and
 * "## Challenge ·" headings, and the <KnowledgeCheck> count. Nothing is
 * authored twice, so the pacing guide cannot drift from the course — same
 * contract as extract_checks.js.
 *
 * Run automatically by `npm start` / `npm run build` (prestart / prebuild).
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const DOCS = path.join(ROOT, 'docs');
const OUT = path.join(ROOT, 'src', 'data', 'pacing.json');

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

function frontMatter(src, key) {
  const m = src.match(new RegExp(`^${key}:\\s*"?(.*?)"?\\s*$`, 'm'));
  return m ? m[1] : null;
}

/** The quoted strings inside <LessonHeader … meta={[ … ]} />. */
function metaChips(src) {
  const header = src.match(/<LessonHeader([\s\S]*?)\/>/);
  if (!header) return [];
  const meta = header[1].match(/meta=\{\[([\s\S]*?)\]\}/);
  if (!meta) return [];
  return [...meta[1].matchAll(/'([^']*)'|"([^"]*)"/g)].map((m) => m[1] ?? m[2]);
}

/**
 * A chip like "50–60 min" or "90 min" becomes [lo, hi] minutes. "Multi-day"
 * (the capstones) has no honest minute value, so it is flagged instead of
 * guessed at — the guide reports those projects separately.
 */
function duration(chips) {
  const chip = chips.find((c) => /\bmin\b|\bhour/i.test(c));
  if (!chip) {
    const multi = chips.find((c) => /multi-?day|project day/i.test(c));
    return {minutes: null, multiDay: Boolean(multi), label: multi || null};
  }
  const nums = (chip.match(/\d+/g) || []).map(Number);
  if (!nums.length) return {minutes: null, multiDay: false, label: chip};
  const scale = /hour/i.test(chip) ? 60 : 1;
  return {
    minutes: [nums[0] * scale, nums[nums.length - 1] * scale],
    multiDay: false,
    label: chip,
  };
}

/**
 * "## Activity · Name" and "## Challenge 2 · Name" — the numbered form is real
 * (Lesson 7 has Challenge 1 and Challenge 2), so the number is optional here.
 */
function headings(src, word) {
  return [
    ...src.matchAll(new RegExp(`^##\\s+${word}(?:\\s+\\d+)?\\s*·\\s*(.+?)\\s*$`, 'gm')),
  ].map((m) => m[1]);
}

function main() {
  const modules = [];
  const problems = [];
  let totals = {lo: 0, hi: 0, lessons: 0, activities: 0, challenges: 0, checks: 0, multiDay: 0};

  const dirs = fs
    .readdirSync(DOCS, {withFileTypes: true})
    .filter((d) => d.isDirectory() && !d.name.startsWith('_')) // docs/_partials/ is shared MDX, not lessons
    .map((d) => d.name)
    .sort((a, b) => {
      const ia = MODULE_ORDER.indexOf(a);
      const ib = MODULE_ORDER.indexOf(b);
      return (ia === -1 ? 99 : ia) - (ib === -1 ? 99 : ib);
    });

  for (const dir of dirs) {
    const files = fs
      .readdirSync(path.join(DOCS, dir))
      .filter((f) => f.endsWith('.mdx') && !f.startsWith('_'))
      .sort();
    if (!files.length) continue;

    const lessons = [];
    for (const file of files) {
      const src = fs.readFileSync(path.join(DOCS, dir, file), 'utf8');
      const chips = metaChips(src);
      if (!chips.length) problems.push(`${dir}/${file}: no LessonHeader meta chips`);

      const dur = duration(chips);
      if (!dur.minutes && !dur.multiDay) {
        problems.push(`${dir}/${file}: no duration chip (add one like '50–60 min')`);
      }

      const slug = file.replace(/\.mdx$/, '');
      const activities = headings(src, 'Activity');
      const challenges = headings(src, 'Challenge');
      const checks = (src.match(/<KnowledgeCheck/g) || []).length;

      lessons.push({
        id: `${dir}/${slug}`,
        title: frontMatter(src, 'title') || slug,
        sidebarLabel: frontMatter(src, 'sidebar_label') || '',
        position: Number(frontMatter(src, 'sidebar_position') || 99),
        docPath: `/${dir}/${slug}`,
        quizPath: src.includes('<QuizLink') ? `/checks/${dir}/${slug}` : null,
        minutes: dur.minutes,
        multiDay: dur.multiDay,
        durationLabel: dur.label,
        phase: chips.find((c) => /phase/i.test(c)) || null,
        chips,
        activities,
        challenges,
        checks,
      });

      totals.lessons += 1;
      totals.activities += activities.length;
      totals.challenges += challenges.length;
      totals.checks += checks;
      if (dur.minutes) {
        totals.lo += dur.minutes[0];
        totals.hi += dur.minutes[1];
      }
      if (dur.multiDay) totals.multiDay += 1;
    }

    lessons.sort((a, b) => a.position - b.position);
    const timed = lessons.filter((l) => l.minutes);
    modules.push({
      id: dir,
      title: MODULE_TITLES[dir] || dir,
      lessons,
      totals: {
        lessons: lessons.length,
        lo: timed.reduce((s, l) => s + l.minutes[0], 0),
        hi: timed.reduce((s, l) => s + l.minutes[1], 0),
        multiDay: lessons.filter((l) => l.multiDay).length,
        activities: lessons.reduce((s, l) => s + l.activities.length, 0),
        challenges: lessons.reduce((s, l) => s + l.challenges.length, 0),
        checks: lessons.reduce((s, l) => s + l.checks, 0),
      },
    });
  }

  if (problems.length) {
    console.error('Pacing extraction problems:');
    problems.forEach((p) => console.error('  - ' + p));
    process.exitCode = 1;
  }

  fs.mkdirSync(path.dirname(OUT), {recursive: true});
  fs.writeFileSync(OUT, JSON.stringify({modules, totals}, null, 2) + '\n');
  console.log(
    `extract_pacing: ${totals.lessons} lessons, ${totals.lo}–${totals.hi} min ` +
      `(+${totals.multiDay} multi-day), ${totals.activities} activities → src/data/pacing.json`
  );
}

main();
