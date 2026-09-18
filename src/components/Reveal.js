import React, {useState} from 'react';

/**
 * Click-to-reveal answer box.
 *
 * The course's cornerstone is that students work things out themselves, so a
 * lesson must not hand over the answer in the paragraph after asking for it.
 * Anything a student *may* look at once they've genuinely tried — a worked
 * result, a finished program, the rule behind a pattern — goes in here, closed
 * by default, so opening it is a deliberate act.
 *
 * Anything a student HANDS IN (filled tables, challenge solutions, project code)
 * does NOT go here — that belongs in a <TeacherNote>, which students can't open.
 *
 *   <Reveal>…</Reveal>                                  "Check your work"
 *   <Reveal title="Stuck? Open this after you've tried a guess.">…</Reveal>
 *
 * Closed content is not printed, which is what you want on a handout.
 */
export default function Reveal({title = 'Check your work', hint = 'try it first', children}) {
  const [open, setOpen] = useState(false);

  return (
    <div className={'reveal' + (open ? ' reveal--open' : '')}>
      <button
        type="button"
        className="reveal__button"
        aria-expanded={open}
        onClick={() => setOpen((v) => !v)}
      >
        <span className="reveal__chevron" aria-hidden="true">
          {open ? '▾' : '▸'}
        </span>
        <span className="reveal__title">{title}</span>
        {!open && hint && <span className="reveal__hint">{hint}</span>}
      </button>
      {open && <div className="reveal__body">{children}</div>}
    </div>
  );
}
