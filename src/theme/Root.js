import React, {useEffect, useState} from 'react';

/**
 * Swizzled Root — wraps the whole app. Renders the floating "Teacher mode"
 * toggle and keeps its state in localStorage. Teacher content is hidden by
 * default (CSS), and turning the switch on sets html[data-teacher='on'],
 * which reveals every <TeacherNote> and teacher banner across the site.
 */

const STORAGE_KEY = 'xrp-teacher-mode';

function TeacherToggle() {
  const [on, setOn] = useState(false);

  // Load persisted state after mount (avoids SSR/hydration mismatch).
  useEffect(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEY) === 'on';
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
        localStorage.setItem(STORAGE_KEY, next ? 'on' : 'off');
      } catch (e) {}
      document.documentElement.setAttribute('data-teacher', next ? 'on' : 'off');
      return next;
    });
  };

  return (
    <button
      type="button"
      className="teacherToggle"
      onClick={toggle}
      aria-pressed={on}
      title="Show or hide teacher-only notes">
      <span className="teacherToggle__label">Teacher mode</span>
      <span className="teacherToggle__track">
        <span className="teacherToggle__thumb" />
      </span>
    </button>
  );
}

export default function Root({children}) {
  return (
    <>
      {children}
      <TeacherToggle />
    </>
  );
}
