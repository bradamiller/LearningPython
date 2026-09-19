import React from 'react';

/**
 * A student-facing callout — the thing you reach for when a paragraph would be
 * skimmed past but the consequence of missing it is a mystified student.
 *
 * Use it sparingly: a page with five callouts has none. Good candidates are
 * physical gotchas whose symptom looks like a code bug (the IMU calibration in
 * Lesson 1 is the model).
 *
 *   <Callout>…</Callout>                       default: a "Watch out" warning
 *   <Callout title="Give it a moment">…</Callout>
 *   <Callout kind="tip" title="Shortcut">…</Callout>
 *
 * kind: 'warn' (amber, default) | 'tip' (blue) | 'note' (gray)
 *
 * NB: Docusaurus's ::: admonition syntax does not render on this site, so this
 * component is the supported way to do a callout. See CLAUDE.md §5.
 */
const ICONS = {warn: '⚠️', tip: '💡', note: 'ℹ️'};
const DEFAULT_TITLES = {warn: 'Watch out', tip: 'Tip', note: 'Note'};

export default function Callout({kind = 'warn', title, children}) {
  const k = ICONS[kind] ? kind : 'warn';
  return (
    <aside className={`callout callout--${k}`}>
      <div className="callout__title">
        <span className="callout__icon" aria-hidden="true">
          {ICONS[k]}
        </span>
        {title || DEFAULT_TITLES[k]}
      </div>
      <div className="callout__body">{children}</div>
    </aside>
  );
}
