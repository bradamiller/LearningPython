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
 * Show TODOs: authoring notes about things that still need fixing. These exist
 * only on the dev server — <Todo> renders null in a production build — so this
 * switch is only rendered under `npm start`, and only on a page that actually
 * has one, with a count of how many.
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
      label="Teacher mode"
      on={on}
      onClick={toggle}
      title="Show or hide teacher-only notes"
    />
  );
}

function TodoToggle() {
  const [on, setOn] = useState(true);       // default ON — that's the point of them
  const [count, setCount] = useState(0);
  const {pathname} = useLocation();

  // Default to on, but remember a deliberate "off".
  useEffect(() => {
    try {
      const saved = localStorage.getItem(TODO_KEY);
      const next = saved === null ? true : saved === 'on';
      setOn(next);
      document.documentElement.setAttribute('data-todos', next ? 'on' : 'off');
    } catch (e) {
      document.documentElement.setAttribute('data-todos', 'on');
    }
  }, []);

  // Count what's on the page. Re-runs per navigation, and once more on the next
  // frame because Docusaurus swaps content after the route changes.
  useEffect(() => {
    const recount = () => setCount(document.querySelectorAll('.todo').length);
    recount();
    const id = requestAnimationFrame(recount);
    return () => cancelAnimationFrame(id);
  }, [pathname]);

  const toggle = () => {
    setOn((prev) => {
      const next = !prev;
      try {
        localStorage.setItem(TODO_KEY, next ? 'on' : 'off');
      } catch (e) {}
      document.documentElement.setAttribute('data-todos', next ? 'on' : 'off');
      return next;
    });
  };

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
      title="Authoring notes — things in this lesson that still need fixing. Dev server only."
    />
  );
}

export default function Root({children}) {
  return (
    <>
      {children}
      <TeacherToggle />
      {process.env.NODE_ENV !== 'production' && <TodoToggle />}
    </>
  );
}
