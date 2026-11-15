"""Module 4, Lesson 4-2 · The Planner: A Path That Grows."""

DECK = {
    'module': 4, 'lesson': 2,
    'doc': 'module-04-manhattan/lesson-02-a-path-that-grows',
    'title': 'The Planner: A Path That Grows',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Trace a path by hand: across first, then up',
             'Start with an empty list and add to it with `append()`',
             'Unpack a tuple into `x` and `y`, and make a new tuple from them',
             'Build a path inside a `while` loop, one step per trip around',
         ],
         'notes': '50 to 60 minutes, robot on the desk. The planner stub hands back one jump; '
                  'today it starts to build real paths, for any trip that goes right and up. Left '
                  'and down are Lesson 4-3. Scope: [], append(), len(), unpacking. No indexing yet '
                  '(4-4), and no insert, pop or slicing at all.'},

        {'kind': 'bullets', 'title': 'The stub hands back one jump',
         'bullets': [
             'Right now `compute_manhattan_path()` returns `[destination]`',
             'A real path lists **every** intersection on the way',
             'Today the stub starts to go: by the end, real paths for trips that go **right and up**',
         ],
         'callout': 'Left and down come in Lesson 4-3',
         'tone': 'teal', 'size': 28},

        {'kind': 'figure', 'title': 'One step at a time',
         'figure': '/img/lesson-m4-03/one-step.svg',
         'caption': 'One step changes x or y by 1, never both. Both would be a diagonal, and the '
                    'robot can\'t drive one.',
         'notes': 'The Manhattan rule from Lesson 4-0: step across until x is right, then step up '
                  'or down until y is right.'},

        {'kind': 'table', 'title': 'Activity · Trace it on paper',
         'tag': 'Activity',
         'lead': 'Trace **Leg 1**, (0, 0) → (2, 3), one row per move. Then write the whole path as '
                 'a Python list.',
         'headers': ['Step', 'Action', 'New position'],
         'widths': [1, 1.6, 2.2],
         'rows': [['1', 'x + 1', '(1, 0)'], ['2', '', ''], ['3', '', ''], ['4', '', ''],
                  ['5', '', '']],
         'row_h': 0.5,
         'notes': 'The filled-in trace is behind a reveal on the lesson page. Check traces before '
                  'Step 2\'s run: a wrong trace sends a student hunting for a bug that isn\'t there. '
                  'Answer: x + 1 to (2, 0), then y + 1 three times to (2, 1), (2, 2), (2, 3).'},

        {'kind': 'figure', 'title': 'The start is not in the path',
         'figure': '/img/lesson-m4-02/path-list-xy.svg',
         'caption': 'One tuple per intersection the robot drives to, in order. The robot is already '
                    'standing on the start.'},

        {'kind': 'code', 'title': 'A list can grow',
         'lead': 'A planner doesn\'t know the path until it works it out. So it starts **empty** '
                 'and adds to the **end**:',
         'code': 'path = []\n'
                 'path.append((1, 0))\n'
                 'path.append((2, 0))\n'
                 'print(path)          # [(1, 0), (2, 0)]\n'
                 'print(len(path))     # 2',
         'code_size': 22,
         'callout': 'Double parentheses: the outer pair is `append()`, the inner pair is the tuple',
         'tone': 'teal',
         'notes': 'len() counts the items. Take real time on the double parentheses.'},

        {'kind': 'check',
         'question': 'What does this print? `stops = []`, then `stops.append((0, 1))`, '
                     '`stops.append((0, 2))`, `stops.append((1, 2))`, then '
                     '`print(len(stops), stops)`',
         'options': ['`3 [(1, 2), (0, 2), (0, 1)]`',
                     '`3 [(0, 1), (0, 2), (1, 2)]`',
                     '`6 [0, 1, 0, 2, 1, 2]`',
                     '`1 [(1, 2)]`'],
         'answer': 1,
         'explanation': 'append() adds to the end, so the items stay in the order they were added. '
                        'Three appends, three tuples, so len() is 3.'},

        {'kind': 'steps', 'title': 'Step 1 · Leg 1, by hand',
         'tag': 'Activity',
         'lead': 'In `compute_manhattan_path()`, keep the `print` line. Replace `return [destination]` '
                 'with:',
         'steps': [
             'Assign an empty list to a variable named `path`',
             'Append the five positions from your trace to `path`, one line each. The first is '
             '`path.append((1, 0))`',
             'Return `path`. Then run `test_delivery()`',
         ],
         'callout': 'Correct: Leg 1 matches your trace, and every other leg gets the same path',
         'tone': 'green',
         'notes': 'Deliberately clumsy, about five minutes: five typed appends make students want '
                  'the loop. Every leg is the same because the function never looks at start or '
                  'destination: it hands back the path they typed. A planner has to work the path '
                  'out.'},

        {'kind': 'figure', 'title': 'Step 2 · Let a loop do the appending',
         'tag': 'Activity',
         'figure': '/img/lesson-m4-03/trace-to-loops.svg',
         'caption': 'Each row is one trip around a loop: add 1 to x, record the spot, until x is '
                    'right.'},

        {'kind': 'code', 'title': 'Take the tuples apart',
         'lead': 'To add 1 to x, the function needs x on its own. **Unpacking** (Lesson 4-1):',
         'code': 'x, y = start                     # start is (0, 0): x is 0, y is 0\n'
                 'dest_x, dest_y = destination     # (2, 3): dest_x is 2, dest_y is 3',
         'code_size': 20,
         'callout': 'After each move, `(x, y)` makes a **new tuple** for the path',
         'tone': 'teal',
         'notes': 'x and y are where the plan has got to. They start as the start and change by 1 '
                  'on every move.'},

        {'kind': 'code', 'title': 'Replace the function with this',
         'tag': 'Activity',
         'code': 'def compute_manhattan_path(start, destination):\n'
                 '    print("computing path from:", start, "to:", destination)\n'
                 '    path = []\n'
                 '    x, y = start              # where the plan is now\n'
                 '    dest_x, dest_y = destination   # where it is going\n'
                 '\n'
                 '    # East: keep stepping right until x matches dest_x\n'
                 '    while x < dest_x:\n'
                 '        x = x + 1             # one step right\n'
                 '        path.append((x, y))   # record the new spot\n'
                 '\n'
                 '    # North: copy east, but step y until it matches dest_y\n'
                 '\n'
                 '    return path',
         'code_size': 15,
         'notes': 'The slide leaves out the docstring to fit. The lesson page has the whole block '
                  'plus test_planner(), which prints three trips: (0, 0) to (2, 3), (0, 2) to '
                  '(3, 2), and (2, 0) to (2, 3). Students paste it from the page.'},

        {'kind': 'steps', 'title': 'Run the east loop',
         'tag': 'Activity',
         'steps': [
             'Trace the three trips in `test_planner()` on paper first: a **paper test**, the right answer worked out by hand',
             'Set the run line to `test_planner()` and run it',
             'Only the east loop exists: the first trip goes right two and stops; the second is '
             'already complete; the third comes back `[]`',
         ],
         'tone': 'green',
         'notes': 'Expected: [(1, 0), (2, 0)], then [(1, 2), (2, 2), (3, 2)], then [], each under '
                  'its computing path from: line. The second trip needs no move up; the third only '
                  'goes up.'},

        {'kind': 'steps', 'title': 'Step 3 · Break it on purpose',
         'tag': 'Activity',
         'steps': [
             'Move `path.append((x, y))` one indent to the left, so it lines up with `while`',
             '**Predict** the first path, then run it',
             'Put the indent back',
         ],
         'callout': 'Indentation decides what is inside the loop',
         'tone': 'orange',
         'notes': 'The append runs once, after the loop: [(2, 0)], [(3, 2)], and [(2, 0)] for the '
                  'third trip, where the loop never ran and the start itself was appended. The '
                  'indentation bug is the most common list bug there is; here it costs one keystroke '
                  'to cause and to fix.'},

        {'kind': 'check',
         'question': 'A loop is meant to build a path, but the list ends up holding only the last '
                     'position. What\'s wrong?',
         'options': ['`append()` is broken',
                     'The `append()` line is outside the loop, so it runs only once',
                     'The path should have been a tuple',
                     'The loop ran too many times'],
         'answer': 1,
         'explanation': 'If append() isn\'t indented inside the loop, it runs a single time after '
                        'the loop ends and records just the final position.'},

        {'kind': 'steps', 'title': 'Step 4 · Write north',
         'tag': 'Activity',
         'steps': [
             'Under the north comment, **copy the east loop**',
             'Compare `y` with `dest_y`, and step `y` instead of `x`',
             'Leave `path.append((x, y))` as it is: it records the whole position',
             'Run `test_planner()`',
         ],
         'callout': 'Correct: all three paths match your paper traces',
         'tone': 'green',
         'notes': 'The north loop is behind a reveal on the lesson page.'},

        {'kind': 'steps', 'title': 'Step 5 · Run the main program',
         'tag': 'Activity',
         'steps': [
             'Set the run line back to `test_delivery()` and run it',
             'Leg 1 is right, and the driver stub now moves **one step at a time**',
             'Leg 2 is not: its path is **empty**, so the robot never leaves (2, 3)',
         ],
         'tone': 'orange',
         'callout': 'What is missing?',
         'notes': 'The broken run is the hook for Lesson 4-3. Let students say what\'s missing: '
                  'loops for going left and down. The full expected printout is behind a reveal on '
                  'the lesson page.'},

        {'kind': 'check',
         'question': 'Why is the path for Leg 2, (2, 3) to (1, 0), empty?',
         'options': ['`append()` only works once per program',
                     'Both while conditions are False from the start (2 is not < 1, 3 is not < 0), '
                     'so neither loop runs',
                     'The start and destination are the same',
                     'The driver is still a stub'],
         'answer': 1,
         'explanation': 'East and north only handle x and y getting bigger. A while loop whose '
                        'condition starts False does nothing. Going left or down needs two more '
                        'loops: Lesson 4-3.'},

        {'kind': 'code', 'title': 'Why a new tuple every step',
         'lead': 'Could the loop just change the x inside one tuple? Try it in the shell:',
         'code': 'spot = (2, 3)\n'
                 'spot[0] = 5      # TypeError: \'tuple\' object does not support item assignment',
         'code_size': 20,
         'callout': 'A tuple **can\'t change**: right for a position. A list can grow: right for a '
                    'path.',
         'tone': 'teal',
         'notes': '(2, 3) should always mean the same intersection, however many lists it is in. So '
                  'a position is a tuple, and a path is a list of tuples.'},

        {'kind': 'check',
         'question': 'Which is true?',
         'options': ['A tuple can grow with `append()`; a list cannot',
                     'A list can grow and change; a tuple stays as it was made',
                     'Lists and tuples are the same thing with different brackets',
                     'A list can only hold numbers'],
         'answer': 1,
         'explanation': 'Lists use square brackets and can change, which suits a path built step by '
                        'step. Tuples use parentheses and can\'t change, which suits a position.'},

        {'kind': 'wrapup',
         'questions': [
             'How does the planner build a path?',
             'What does `x, y = start` do?',
             'Why isn\'t the start in the path?',
             'What still doesn\'t work?',
         ],
         'next': 'the planner, part 2: every direction, and tests',
         'notes': 'Answers: start with [] and append() one position on every trip around a loop. It '
                  'unpacks the tuple: x gets the first number, y the second. The robot is already '
                  'there; the path lists where it drives to. Trips that go left or down: both loops '
                  'are skipped.'},
    ],
}
