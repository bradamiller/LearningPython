import React, {useState} from 'react';

/**
 * Lesson header band — the colored title block at the top of a lesson,
 * like the VEX lesson pages. `meta` is a list of small facts (duration,
 * module, etc.) shown as a dotted row.
 */
export function LessonHeader({eyebrow, title, meta = []}) {
  return (
    <header className="lessonHeader">
      {eyebrow && <div className="eyebrow">{eyebrow}</div>}
      <h1>{title}</h1>
      {meta.length > 0 && (
        <div className="lessonMeta">
          {meta.map((m, i) => (
            <span key={i}>{m}</span>
          ))}
        </div>
      )}
    </header>
  );
}

/** Learning-objectives callout box. */
export function Objectives({children, title = 'Learning Objectives'}) {
  return (
    <section className="objectives">
      <h4>{title}</h4>
      {children}
    </section>
  );
}

/** A dashed banner that only appears when teacher mode is on. */
export function TeacherBanner({children}) {
  return (
    <div className="teacherBanner">
      <span>👩‍🏫</span>
      <span>{children}</span>
    </div>
  );
}

/** Simple responsive card grid for real-world connections / choice boards. */
export function CardGrid({children}) {
  return <div className="cardGrid">{children}</div>;
}

export function InfoCard({tag, title, children}) {
  return (
    <div className="infoCard">
      {tag && <div className="infoCard__tag">{tag}</div>}
      {title && <h4>{title}</h4>}
      <div>{children}</div>
    </div>
  );
}

/**
 * Decide — a compact "Robot? yes/no + why" fill-in that sits directly under a
 * gallery picture (Lesson 0). Interactive so a teacher can record the class's
 * answer live on the projector; state is in-memory only.
 */
export function Decide({device, prompt = 'Robot?', why = 'Why? — what makes it a robot, or keeps it from being one?'}) {
  const [choice, setChoice] = useState(null);
  return (
    <div className="decide">
      <div className="decide__row">
        {device && <span className="decide__device">{device}</span>}
        <span className="decide__prompt">{prompt}</span>
        {['Yes', 'No'].map((v) => (
          <button
            key={v}
            type="button"
            className={'decide__btn' + (choice === v ? ' decide__btn--on' : '')}
            onClick={() => setChoice(choice === v ? null : v)}
          >
            {v}
          </button>
        ))}
      </div>
      <input className="decide__why" type="text" placeholder={why} aria-label={why} />
    </div>
  );
}
