"""One-off edit of the Lesson 4-1 Map it worksheet (its generator was not kept):
question 3 no longer asks for the total number of steps (Brad, 2026-11-11: Manhattan
distance is no longer taught in 4-1). Rewrites the page's own drawing commands, so the
text is gone, not covered. Needs pypdf. Safe to run twice."""
import os
from pypdf import PdfReader, PdfWriter
from pypdf.generic import ContentStream, NameObject

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PDF = os.path.join(ROOT, 'static', 'printables', 'lesson-4-1-blank-grid.pdf')

r = PdfReader(PDF)
w = PdfWriter(clone_from=r)
page = w.pages[0]
d = page.get_contents().get_data().decode('latin-1')
d = d.replace('how many up or down, how many total steps?) Tj', 'how many up or down?) Tj')
d = d.replace('BT 1 0 0 1 324 83 Tm (Total:) Tj T* ET\n.333333 .333333 .333333 RG\n.7 w\nn 362 81 m 402 81 l S\n', '')
assert 'total steps' not in d and '(Total:)' not in d
cs = ContentStream(None, w)
cs.set_data(d.encode('latin-1'))
page[NameObject('/Contents')] = w._add_object(cs)
with open(PDF, 'wb') as f:
    w.write(f)
