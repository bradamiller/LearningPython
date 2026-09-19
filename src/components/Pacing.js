import React, {useState} from 'react';
import Link from '@docusaurus/Link';
import useBaseUrl from '@docusaurus/useBaseUrl';
import pacing from '@site/src/data/pacing.json';

/**
 * The pacing guide at /pacing — generated from the lessons by
 * scripts/extract_pacing.js, so it cannot drift from the course.
 *
 * Every number here comes from the lesson files: the duration and phase chips
 * in <LessonHeader>, the "## Activity ·" headings, and the <KnowledgeCheck>
 * count. Nothing is authored twice. If a figure looks wrong, fix the lesson.
 *
 * The period length and periods-per-week controls are in-memory only — this is
 * a planning surface, not a saved document.
 */

const PERIOD_LENGTHS = [40, 45, 50, 55, 60, 90];
const PER_WEEK = [2, 3, 4, 5];
const PERIODS_PER_PROJECT = 2; // stated assumption for the multi-day capstones

function periods(minutes, periodLength) {
  return minutes / periodLength;
}

function fmt(n) {
  return Number.isInteger(n) ? String(n) : n.toFixed(1);
}

function range(lo, hi, unit) {
  const a = fmt(lo);
  const b = fmt(hi);
  return a === b ? `${a} ${unit}` : `${a}–${b} ${unit}`;
}

function Chip({children, tone = 'phase'}) {
  return <span className={`pacingChip pacingChip--${tone}`}>{children}</span>;
}

function LessonRow({lesson}) {
  const doc = useBaseUrl(lesson.docPath);
  const quiz = useBaseUrl(lesson.quizPath || '/');
  return (
    <tr>
      <td className="pacingCell--lesson">
        <Link to={doc}>{lesson.title}</Link>
      </td>
      <td className="pacingCell--time">
        {lesson.multiDay ? (
          <Chip tone="project">Multi-day</Chip>
        ) : (
          lesson.durationLabel
        )}
      </td>
      <td className="pacingCell--do">
        {lesson.activities.length + lesson.challenges.length === 0 ? (
          <span className="pacingMuted">—</span>
        ) : (
          <ul className="pacingActivities">
            {lesson.activities.map((a) => (
              <li key={a}>{a}</li>
            ))}
            {lesson.challenges.map((c) => (
              <li key={c}>
                <span className="pacingKind">Challenge</span> {c}
              </li>
            ))}
          </ul>
        )}
      </td>
      <td className="pacingCell--checks">
        {lesson.quizPath ? (
          <Link to={quiz}>{lesson.checks}</Link>
        ) : (
          lesson.checks || <span className="pacingMuted">—</span>
        )}
      </td>
    </tr>
  );
}

function ModuleTable({mod, periodLength}) {
  const t = mod.totals;
  const lo = periods(t.lo, periodLength);
  const hi = periods(t.hi, periodLength);
  return (
    <section className="pacingModule">
      <h2 id={mod.id}>{mod.title}</h2>
      <p className="pacingModule__summary">
        {t.lessons} lessons · {range(t.lo, t.hi, 'min')} ·{' '}
        <strong>{range(lo, hi, 'periods')}</strong>
        {t.multiDay > 0 && (
          <>
            {' '}
            + {t.multiDay} multi-day project
            {t.multiDay > 1 ? 's' : ''}
          </>
        )}{' '}
        · {t.activities + t.challenges} activities to hand in · {t.checks}{' '}
        knowledge checks
      </p>
      <table className="pacingTable">
        <thead>
          <tr>
            <th>Lesson</th>
            <th>Time</th>
            <th>Activities students turn in</th>
            <th>Checks</th>
          </tr>
        </thead>
        <tbody>
          {mod.lessons.map((l) => (
            <LessonRow key={l.id} lesson={l} />
          ))}
        </tbody>
      </table>
    </section>
  );
}

export default function PacingGuide() {
  const [periodLength, setPeriodLength] = useState(50);
  const [perWeek, setPerWeek] = useState(3);

  const t = pacing.totals;
  const basePeriodsLo = periods(t.lo, periodLength);
  const basePeriodsHi = periods(t.hi, periodLength);
  const projectPeriods = t.multiDay * PERIODS_PER_PROJECT;
  const totalLo = basePeriodsLo + projectPeriods;
  const totalHi = basePeriodsHi + projectPeriods;

  return (
    <div className="pacing">
      <div className="pacingControls">
        <label>
          Period length
          <select
            value={periodLength}
            onChange={(e) => setPeriodLength(Number(e.target.value))}
          >
            {PERIOD_LENGTHS.map((p) => (
              <option key={p} value={p}>
                {p} min
              </option>
            ))}
          </select>
        </label>
        <label>
          Periods per week
          <select value={perWeek} onChange={(e) => setPerWeek(Number(e.target.value))}>
            {PER_WEEK.map((p) => (
              <option key={p} value={p}>
                {p}
              </option>
            ))}
          </select>
        </label>
      </div>

      <div className="pacingSummary">
        <div className="pacingStat">
          <div className="pacingStat__value">{range(t.lo / 60, t.hi / 60, 'hours')}</div>
          <div className="pacingStat__label">of estimated class time</div>
        </div>
        <div className="pacingStat">
          <div className="pacingStat__value">{range(totalLo, totalHi, 'periods')}</div>
          <div className="pacingStat__label">
            at {periodLength} min, including {t.multiDay} multi-day projects at{' '}
            {PERIODS_PER_PROJECT} periods each
          </div>
        </div>
        <div className="pacingStat">
          <div className="pacingStat__value">
            {range(totalLo / perWeek, totalHi / perWeek, 'weeks')}
          </div>
          <div className="pacingStat__label">at {perWeek} periods per week</div>
        </div>
      </div>

      <p className="pacingNote">
        {t.lessons} lessons · {t.activities + t.challenges} activities students
        hand in ·{' '}
        {t.checks} knowledge checks. Times are the estimates written into each
        lesson header, so treat them as a plan, not a stopwatch — a class that
        discusses well will run long on the kickoff and short on the syntax
        lessons.
      </p>

      {pacing.modules.map((mod) => (
        <ModuleTable key={mod.id} mod={mod} periodLength={periodLength} />
      ))}
    </div>
  );
}
