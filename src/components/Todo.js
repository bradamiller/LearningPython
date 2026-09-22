import React from 'react';

/**
 * An authoring note about something in this lesson that still needs fixing.
 *
 *   <Todo kind="bug">loop_count is defined nowhere in this module …</Todo>
 *
 * These ship with the site and are hidden behind the "Show TODOs" switch beside
 * Teacher mode — the same arrangement teacher notes use. The switch defaults ON
 * under `npm start` and OFF on a built site, and only appears on a page that has
 * at least one note.
 *
 * That means the text IS in the page source of the deployed site, exactly as
 * teacher notes and answer keys already are. To ship a build where the notes
 * cannot be found at all, build with SHOW_TODOS=0 — a remark plugin then deletes
 * the nodes before MDX compiles them, so neither markup nor text is emitted.
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
