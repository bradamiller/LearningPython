import React, {useEffect, useState} from 'react';
import {useLocation} from '@docusaurus/router';

/**
 * Swizzled Root — wraps the whole app. Renders the floating toggles and keeps
 * their state in localStorage.
 *
 * Teacher mode: teacher content is hidden by default (CSS), and turning the
 * switch on sets html[data-teacher='on'], which reveals every <TeacherNote>
 * and teacher banner across the site.
 *
 * Show TODOs: authoring notes about things that still need fixing. The switch
 * appears on any page that has at least one, with a count of how many. It
 * defaults ON under `npm start` (you are there to fix things) and OFF on a built
 * site (a reader is not), and remembers whichever way you last set it.
 */

const TEACHER_KEY = 'xrp-teacher-mode';
const TODO_KEY = 'xrp-show-todos';

function Toggle({className, label, count, on, onClick, title}) {
  return (
    <button
      type="button"
      className={`teacherToggle ${className || ''}`}
      onClick={onClick}
      aria-pressed={on}
      title={title}>
      <span className="teacherToggle__label">{label}</span>
      {typeof count === 'number' && <span className="todoToggle__count">{count}</span>}
      <span className="teacherToggle__track">
        <span className="teacherToggle__thumb" />
      </span>
    </button>
  );
}

function TeacherToggle() {
  const [on, setOn] = useState(false);

  // Load persisted state after mount (avoids SSR/hydration mismatch).
  useEffect(() => {
    try {
      const saved = localStorage.getItem(TEACHER_KEY) === 'on';
      setOn(saved);
      document.documentElement.setAttribute('data-teacher', saved ? 'on' : 'off');
    } catch (e) {
      /* storage may be unavailable; default to off */
    }
  }, []);

  const toggle = () => {
    setOn((prev) => {
      const next = !prev;
      try {
        localStorage.setItem(TEACHER_KEY, next ? 'on' : 'off');
      } catch (e) {}
      document.documentElement.setAttribute('data-teacher', next ? 'on' : 'off');
      return next;
    });
  };

  return (
    <Toggle
      className="teacherToggle--teacher"
      label="Teacher mode"
      on={on}
      onClick={toggle}
      title="Show or hide teacher-only notes"
    />
  );
}

function TodoToggle() {
  // On while authoring, off for a reader — overridden by a remembered choice.
  const DEFAULT_ON = process.env.NODE_ENV !== 'production';
  const [on, setOn] = useState(DEFAULT_ON);
  const [count, setCount] = useState(0);
  const {pathname, hash} = useLocation();

  const apply = (next) => {
    setOn(next);
    try {
      localStorage.setItem(TODO_KEY, next ? 'on' : 'off');
    } catch (e) {}
    document.documentElement.setAttribute('data-todos', next ? 'on' : 'off');
  };

  useEffect(() => {
    try {
      const saved = localStorage.getItem(TODO_KEY);
      const next = saved === null ? DEFAULT_ON : saved === 'on';
      setOn(next);
      document.documentElement.setAttribute('data-todos', next ? 'on' : 'off');
    } catch (e) {
      document.documentElement.setAttribute('data-todos', DEFAULT_ON ? 'on' : 'off');
    }
  }, []);

  // Arriving from /todos with a #todo-N hash: switch the notes on and scroll to
  // the one that was clicked. Without this the browser has nothing to scroll to
  // — a hidden element has no position — and the link looks broken. Deliberately
  // persists the choice: you came here to read notes, so leave them on.
  useEffect(() => {
    if (!/^#todo-\d+$/.test(hash || '')) return;
    apply(true);
    const target = () => document.querySelector(hash);
    const scroll = () => {
      const el = target();
      if (el) el.scrollIntoView({block: 'center'});
    };
    // Two frames: one for the attribute to un-hide the note, one for layout.
    const id = requestAnimationFrame(() => requestAnimationFrame(scroll));
    return () => cancelAnimationFrame(id);
  }, [pathname, hash]);

  // Count what's on the page. Re-runs per navigation, and once more on the next
  // frame because Docusaurus swaps content after the route changes.
  useEffect(() => {
    const recount = () => setCount(document.querySelectorAll('.todo').length);
    recount();
    const id = requestAnimationFrame(recount);
    return () => cancelAnimationFrame(id);
  }, [pathname]);

  const toggle = () => apply(!on);

  // No switch on a page with nothing to show. (When they're hidden the nodes
  // are still in the DOM, so the count survives being switched off.)
  if (count === 0) return null;

  return (
    <Toggle
      className="todoToggle"
      label="Show TODOs"
      count={count}
      on={on}
      onClick={toggle}
      title="Authoring notes — things in this lesson that still need fixing."
    />
  );
}

export default function Root({children}) {
  return (
    <>
      {children}
      <TeacherToggle />
      <TodoToggle />
    </>
  );
}
