import React from 'react';

/**
 * A gray "Teacher Note" box, VEX-style. Hidden unless teacher mode is on
 * (the floating toggle sets html[data-teacher='on']; visibility is CSS-driven).
 *
 * Usage in MDX:
 *   <TeacherNote>
 *   Timing tip: in a 50-minute class, skip Exercise 2.
 *   </TeacherNote>
 *
 * Optional `title` overrides the default "Teacher Note" label.
 */
export default function TeacherNote({children, title = 'Teacher Note'}) {
  return (
    <aside className="teacherNote" role="note">
      <span className="teacherNote__label">{title}</span>
      <div className="teacherNote__body">{children}</div>
    </aside>
  );
}
