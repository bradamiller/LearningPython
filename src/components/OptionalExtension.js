import React, {useState} from 'react';

/**
 * Optional Extension — the classes track, per student, per lesson.
 *
 * The course's required content is written with plain functions. Where a lesson
 * has a class version of the same working code, it goes in here: closed by
 * default, opened deliberately, and gated on the functions version working.
 * (See IntoToPython/teacher-guide/course-design-decisions.md, D1.)
 *
 *   <OptionalExtension title="The BFS class">
 *     <SideBySide left="Functions — what you have" right="Class — the extension">
 *       ```python … ```
 *       ```python … ```
 *     </SideBySide>
 *     …prose, knowledge checks, more code…
 *   </OptionalExtension>
 *
 * The header carries the standing rule so no page has to repeat it: do it after
 * the functions version works on the robot; it earns no extra credit. Override
 * with `gate="…"` when a lesson needs different wording. Closed content is not
 * printed.
 *
 * NO MARKDOWN HEADINGS INSIDE. Children are not rendered until the box is
 * opened, but Docusaurus builds the page outline from the source, so a `###`
 * in here becomes an outline entry that scrolls nowhere (2026-10-15, M2 L8).
 * Use **bold text** for sub-sections; scripts/check_extensions.js enforces it.
 */
export default function OptionalExtension({
  title,
  gate = 'Do this after your functions version works on the robot. It is not graded; it is for when there is time.',
  children,
}) {
  const [open, setOpen] = useState(false);
  return (
    <section className={'ext' + (open ? ' ext--open' : '')}>
      <button
        type="button"
        className="ext__button"
        aria-expanded={open}
        onClick={() => setOpen((v) => !v)}
      >
        <span className="ext__chip">Optional extension</span>
        <span className="ext__title">{title}</span>
        <span className="ext__chevron" aria-hidden="true">
          {open ? '▾' : '▸'}
        </span>
      </button>
      {gate && <div className="ext__gate">{gate}</div>}
      {open && <div className="ext__body">{children}</div>}
    </section>
  );
}

/**
 * Two code blocks side by side, the functions version on the left and the class
 * version on the right, same names aligned as far as the code allows. Expects
 * exactly two children (two fenced code blocks). Stacks on narrow screens.
 */
export function SideBySide({left = 'Functions', right = 'Class', children}) {
  const kids = React.Children.toArray(children);
  return (
    <div className="sbs">
      <div className="sbs__col">
        <div className="sbs__head">{left}</div>
        {kids[0]}
      </div>
      <div className="sbs__col">
        <div className="sbs__head">{right}</div>
        {kids[1]}
      </div>
    </div>
  );
}
