import React, {useState} from 'react';
import Link from '@docusaurus/Link';
import data from '@site/src/data/todos.json';

/**
 * The /todos page: every authoring note in the course, on one screen, each one
 * a link straight to the note in its lesson.
 *
 * The working loop it exists for: pick one, click it, land on the note in the
 * lesson, fix the lesson, delete the note in the same commit (see CLAUDE.md
 * §10b), come back. The "index" link in the corner of every note box is the
 * return leg.
 *
 * Grouping is by category rather than by module, because category is what
 * decides whether something is worth doing now — a bug a student can hit
 * outranks a convention drift in the same lesson. The module is on each card
 * for orientation, and the filter chips narrow to one category at a time.
 *
 * All of it comes from src/data/todos.json, which is generated on every
 * start/build. There is nothing to keep in sync by hand: fix a note and it
 * leaves this page by itself.
 */

const BLURBS = {
  bug: 'Wrong, and a student can hit it.',
  blocked: "Needs Brad's decision, or a robot, before it can be fixed.",
  answers: 'An answer is visible where it should not be.',
  convention: 'Drifts from a rule the course keeps elsewhere.',
  media: 'A placeholder or a stand-in image.',
};

const ICONS = {
  bug: '🐞',
  blocked: '⏳',
  answers: '🙈',
  convention: '📐',
  media: '📷',
};

function Card({item}) {
  return (
    <li className={`todoIndex__card todoIndex__card--${item.category}`}>
      <Link
        className="todoIndex__link"
        to={`${item.docPath}#${item.anchor}`}
        title={`${item.file}:${item.line}`}
      >
        <div className="todoIndex__where">
          <span className="todoIndex__lesson">{item.sidebarLabel}</span>
          <span className="todoIndex__module">{item.moduleTitle}</span>
        </div>
        <p className="todoIndex__text">{item.text}</p>
        <div className="todoIndex__meta">
          {item.cite && <span className="todoIndex__cite">{item.cite}</span>}
          <span className="todoIndex__file">
            {item.file.replace(/^docs\//, '')}:{item.line}
          </span>
        </div>
      </Link>
    </li>
  );
}

export default function TodoIndex() {
  const [only, setOnly] = useState(null);
  const {items, counts, categoryOrder, categoryLabels, total} = data;

  if (!total) {
    return (
      <p className="todoIndex__empty">
        No TODO notes in this build. Either the course is clean, or this site was
        built with <code>SHOW_TODOS=0</code>, which strips them out.
      </p>
    );
  }

  const shown = categoryOrder.filter((c) => counts[c] && (!only || c === only));

  return (
    <div className="todoIndex">
      <div className="todoIndex__filters">
        <button
          type="button"
          className={`todoIndex__chip${only === null ? ' todoIndex__chip--on' : ''}`}
          onClick={() => setOnly(null)}
        >
          All <span className="todoIndex__count">{total}</span>
        </button>
        {categoryOrder
          .filter((c) => counts[c])
          .map((c) => (
            <button
              key={c}
              type="button"
              className={`todoIndex__chip todoIndex__chip--${c}${
                only === c ? ' todoIndex__chip--on' : ''
              }`}
              onClick={() => setOnly(only === c ? null : c)}
            >
              <span aria-hidden="true">{ICONS[c]}</span> {categoryLabels[c]}{' '}
              <span className="todoIndex__count">{counts[c]}</span>
            </button>
          ))}
      </div>

      {shown.map((c) => (
        <section key={c} className="todoIndex__section">
          <h2 id={c} className={`todoIndex__heading todoIndex__heading--${c}`}>
            <span aria-hidden="true">{ICONS[c]}</span> {categoryLabels[c]}{' '}
            <span className="todoIndex__count">{counts[c]}</span>
          </h2>
          <p className="todoIndex__blurb">{BLURBS[c]}</p>
          <ul className="todoIndex__list">
            {items
              .filter((i) => i.category === c)
              .map((i) => (
                <Card key={i.n} item={i} />
              ))}
          </ul>
        </section>
      ))}
    </div>
  );
}
