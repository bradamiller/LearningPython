import React from 'react';
import Link from '@docusaurus/Link';
import useBaseUrl from '@docusaurus/useBaseUrl';
import CHECKS from '@site/src/data/checks.json';

/**
 * Printable knowledge-check sheets.
 *
 * The questions live in the lesson .mdx files (as <KnowledgeCheck>, which is what
 * students click through on the page). `scripts/extract_checks.js` copies them
 * into src/data/checks.json, and these components render that same content as a
 * sheet a teacher can print and a student can fill in by hand.
 *
 *   <QuizSheet id="module-01-driving/lesson-01-meet-the-xrp" />        student copy
 *   <QuizSheet id="…" answers />                                       teacher key
 *   <QuizLink id="…" />                                                link on the lesson page
 */

const LETTERS = 'ABCDEFGH';

function sheetUrl(id, answers) {
  return `/checks/${id}${answers ? '-key' : ''}`;
}

export function QuizSheet({id, answers = false}) {
  const lesson = CHECKS[id];
  if (!lesson) {
    return <p>No knowledge checks found for <code>{id}</code>.</p>;
  }
  const {moduleTitle, lessonTitle, checks, docPath} = lesson;

  return (
    <div className={'quizSheet' + (answers ? ' quizSheet--key' : '')}>
      <header className="quizSheet__head">
        <div className="quizSheet__eyebrow">{moduleTitle}</div>
        <h1 className="quizSheet__title">
          {lessonTitle} — Knowledge Checks
          {answers && <span className="quizSheet__keyTag">Answer key</span>}
        </h1>
        {answers ? (
          <p className="quizSheet__meta">
            Correct answers are marked and the explanation follows each question.
          </p>
        ) : (
          <div className="quizSheet__nameRow">
            <span>Name <span className="quizSheet__rule" /></span>
            <span>Date <span className="quizSheet__ruleShort" /></span>
          </div>
        )}
      </header>

      <ol className="quizSheet__list">
        {checks.map((c, i) => (
          <li className="quizSheet__item" key={i}>
            <p className="quizSheet__q">{c.question}</p>
            <ol className="quizSheet__options">
              {c.options.map((o, j) => (
                <li
                  className={
                    'quizSheet__option' +
                    (answers && o.correct ? ' quizSheet__option--correct' : '')
                  }
                  key={j}
                >
                  <span className="quizSheet__letter">{LETTERS[j]}.</span>
                  <span>{o.text}</span>
                  {answers && o.correct && <span className="quizSheet__tick">✓</span>}
                </li>
              ))}
            </ol>
            {answers ? (
              c.explanation && <p className="quizSheet__why">{c.explanation}</p>
            ) : (
              <p className="quizSheet__answerLine">
                Answer <span className="quizSheet__box" /> Why?
                <span className="quizSheet__rule" />
              </p>
            )}
          </li>
        ))}
      </ol>

      <footer className="quizSheet__foot">
        <Link to={useBaseUrl(docPath)}>Back to the lesson</Link>
        {!answers && (
          <>
            {' · '}
            <Link to={useBaseUrl(sheetUrl(id, true))}>Answer key (teachers)</Link>
          </>
        )}
      </footer>
    </div>
  );
}

/**
 * The callout on a lesson page pointing at its printable sheet. The answer-key
 * link is inside a .teacherNote wrapper, so students don't see it.
 */
export function QuizLink({id}) {
  const sheet = useBaseUrl(sheetUrl(id, false));
  const key = useBaseUrl(sheetUrl(id, true));
  const lesson = CHECKS[id];
  const count = lesson ? lesson.checks.length : 0;

  return (
    <div className="quizLink">
      <span className="quizLink__icon" aria-hidden="true">📄</span>
      <div>
        <Link to={sheet}>
          <strong>Printable knowledge checks</strong>
        </Link>{' '}
        — the {count} questions from this lesson on one page, with room to write.
        <span className="teacherNote teacherNote--inline">
          {' '}
          Teachers: <Link to={key}>answer key</Link>.
        </span>
      </div>
    </div>
  );
}

/** One page listing every lesson's sheet and key, grouped by module. */
export function QuizIndex() {
  const byModule = {};
  for (const [id, lesson] of Object.entries(CHECKS)) {
    (byModule[lesson.moduleTitle] = byModule[lesson.moduleTitle] || []).push({id, lesson});
  }
  return (
    <div className="quizSheet quizIndex">
      <header className="quizSheet__head">
        <div className="quizSheet__eyebrow">XRP Python Curriculum</div>
        <h1 className="quizSheet__title">Printable Knowledge Checks</h1>
        <p className="quizSheet__meta">
          Every lesson's questions as a one-page handout. Open a sheet and print it
          (Cmd/Ctrl-P) — the navigation and colors drop away automatically.
        </p>
      </header>
      {Object.entries(byModule).map(([moduleTitle, lessons]) => (
        <section key={moduleTitle} className="quizIndex__module">
          <h2>{moduleTitle}</h2>
          <ul className="quizIndex__list">
            {lessons.map(({id, lesson}) => (
              <li key={id}>
                <Link to={useBaseUrl(sheetUrl(id, false))}>{lesson.lessonTitle}</Link>{' '}
                <span className="quizIndex__count">({lesson.checks.length} questions)</span>{' '}
                <Link className="quizIndex__key" to={useBaseUrl(sheetUrl(id, true))}>
                  answer key
                </Link>
              </li>
            ))}
          </ul>
        </section>
      ))}
    </div>
  );
}

export default QuizSheet;
