import React from 'react';

/**
 * An authoring note about something in this lesson that still needs fixing.
 *
 *   <Todo kind="bug">loop_count is defined nowhere in this module …</Todo>
 *
 * DEVELOPMENT ONLY. This renders `null` in a production build, so the text
 * never reaches the deployed site — not even hidden in the page source. That
 * matters: several of these notes say *where the answers are visible*, which
 * is the last thing to ship to students. Run `npm start` to see them.
 *
 * The "Show TODOs" switch beside Teacher mode hides and shows them while you
 * read; the switch only appears when there is something to switch.
 *
 * Categories, in the order they are worth attention:
 *   bug         wrong, and a student can hit it
 *   blocked     needs a decision or a robot before it can be fixed
 *   answers     an answer is visible where it should not be
 *   convention  drifts from a rule the course keeps elsewhere
 *   media       a placeholder or a stand-in image
 */

const KINDS = {
  bug: {label: 'Bug', icon: '🐞'},
  blocked: {label: 'Blocked', icon: '⏸'},
  answers: {label: 'Answer leak', icon: '🙈'},
  convention: {label: 'Convention', icon: '📐'},
  media: {label: 'Media', icon: '📷'},
};

export default function Todo({kind = 'bug', children}) {
  if (process.env.NODE_ENV === 'production') return null;
  const k = KINDS[kind] ? kind : 'bug';
  const {label, icon} = KINDS[k];
  return (
    <aside className={`todo todo--${k}`} data-todo={k}>
      <div className="todo__tag">
        <span className="todo__icon" aria-hidden="true">
          {icon}
        </span>
        TODO · {label}
      </div>
      <div className="todo__body">{children}</div>
    </aside>
  );
}
