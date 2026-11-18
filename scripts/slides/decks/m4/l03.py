"""Module 4, Lesson 4-3 · The Planner: Every Direction."""

DECK = {
    'module': 4, 'lesson': 3,
    'doc': 'module-04-manhattan/lesson-03-the-planner-every-direction',
    'title': 'The Planner: Every Direction',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Compare two tuples, or two lists, with `==`',
             'Test a function with `run_test()` against paths you traced by hand',
             'Write the west and south loops, with no `if/else`',
             'State the planner\'s three promises',
         ],
         'notes': '50 to 60 minutes, robot on the desk. Last lesson\'s delivery run fell apart on '
                  'Leg 2: the planner can only go right and up. Today students write tests that say '
                  'exactly what\'s wrong, then add the two missing loops and watch the tests turn '
                  'to PASS. Every step of the activity is predict, run, compare: students write '
                  'down what they expect before each run.'},

        {'kind': 'table', 'title': 'Activity · Make your answer key',
         'tag': 'Activity',
         'lead': 'Trace each path by hand: across first, then up or down. Then: what is different '
                 'about **Leg 2**?',
         'headers': ['Test', 'From, to', 'Expected path'],
         'widths': [2, 2.4, 5.6],
         'rows': [['Leg 1', '(0, 0) to (2, 3)', ''],
                  ['Leg 2', '(2, 3) to (1, 0)', ''],
                  ['Same column', '(2, 0) to (2, 3)', ''],
                  ['Same row', '(0, 2) to (3, 2)', ''],
                  ['Same spot', '(1, 1) to (1, 1)', '']],
         'row_h': 0.5,
         'notes': 'About 10 minutes on a big grid. Check the sheets before students go on: a wrong '
                  'key sends them hunting for a bug that isn\'t there. Answers: Leg 1 [(1, 0), '
                  '(2, 0), (2, 1), (2, 2), (2, 3)]; Leg 2 [(1, 3), (1, 2), (1, 1), (1, 0)]; same '
                  'column [(2, 1), (2, 2), (2, 3)]; same row [(1, 2), (2, 2), (3, 2)]; same spot []. '
                  'Leg 1 goes right and up, so x and y get bigger; Leg 2 goes left and down, so they '
                  'get smaller. Same spot is empty because the robot is already there.'},

        # Step 1
        {'kind': 'code', 'title': 'Step 1 · Let the computer compare', 'tag': 'Activity',
         'lead': '`==` works on tuples and on lists. Type these into the shell:',
         'code': 'print((1, 2) == (1, 2))\n'
                 'print((1, 2) == (2, 1))\n'
                 'print([(1, 0), (2, 0)] == [(1, 0), (2, 0)])\n'
                 'print([(1, 0), (2, 0)] == [(1, 0)])',
         'code_size': 22,
         'callout': '**Predict:** what does each line print?',
         'tone': 'teal',
         'notes': 'Last lesson students checked printed paths by eye. With five paths, and a re-run '
                  'after every change, that gets slow. Answer on the next slide.'},

        {'kind': 'code', 'title': 'Step 1 · Check your output', 'tag': 'Activity',
         'code': 'True\n'
                 'False\n'
                 'True\n'
                 'False',
         'code_size': 24,
         'callout': 'Equal means equal items, in the same order, and the same number of them. One '
                    '`==` checks a whole path.',
         'tone': 'green'},

        {'kind': 'check',
         'question': 'Does `(1, 3) == (3, 1)` evaluate to True?',
         'options': ['Yes: they contain the same numbers',
                     'No: the parts must match in order, and these are swapped',
                     'Yes: tuples ignore order',
                     'It causes an error'],
         'answer': 1,
         'explanation': '(1, 3) is x = 1, y = 3; (3, 1) is x = 3, y = 1. Different intersections, '
                        'so False.'},

        # Step 2
        {'kind': 'code', 'title': 'Step 2 · Run the tests first', 'tag': 'Activity',
         'lead': 'Add `run_test()` below `compute_manhattan_path()`:',
         'code': 'def run_test(test_name, start, destination, expected):\n'
                 '    actual = compute_manhattan_path(start, destination)\n'
                 '    if actual == expected:\n'
                 '        print(test_name, "- PASS")\n'
                 '    else:\n'
                 '        print(test_name, "- FAIL")\n'
                 '        print("  Expected:", expected)\n'
                 '        print("  Actual:  ", actual)',
         'code_size': 20,
         'notes': 'The slide leaves out the docstring to fit; students copy the block from the '
                  'lesson page.'},

        {'kind': 'code', 'title': 'Step 2 · Run the tests first', 'tag': 'Activity',
         'lead': 'Replace last lesson\'s `test_planner()`. Each `[]` becomes the path from your '
                 'answer key (Same spot stays `[]`).',
         'code': 'def test_planner():\n'
                 '    # expected = your answer key, traced by hand\n'
                 '    run_test("Leg 1",       (0, 0), (2, 3), [(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)])\n'
                 '    run_test("Leg 2",       (2, 3), (1, 0), [])   # your answer key\n'
                 '    run_test("Same column", (2, 0), (2, 3), [])   # your answer key\n'
                 '    run_test("Same row",    (0, 2), (3, 2), [])   # your answer key\n'
                 '    run_test("Same spot",   (1, 1), (1, 1), [])   # your answer key',
         'code_size': 16,
         'callout': 'Run line: `test_planner()`. **Predict:** with only east and north written, '
                    'which tests will pass?',
         'tone': 'teal',
         'notes': 'The expected lists must come from the students\' own tracing. Watch for the '
                  'student who runs the code first and pastes its output into expected: then the '
                  'test only checks that the code agrees with itself.'},

        {'kind': 'code', 'title': 'Step 2 · Check your output', 'tag': 'Activity',
         'code': 'computing path from: (0, 0) to: (2, 3)\n'
                 'Leg 1 - PASS\n'
                 'computing path from: (2, 3) to: (1, 0)\n'
                 'Leg 2 - FAIL\n'
                 '  Expected: [(1, 3), (1, 2), (1, 1), (1, 0)]\n'
                 '  Actual:   []\n'
                 'computing path from: (2, 0) to: (2, 3)\n'
                 'Same column - PASS\n'
                 'computing path from: (0, 2) to: (3, 2)\n'
                 'Same row - PASS\n'
                 'computing path from: (1, 1) to: (1, 1)\n'
                 'Same spot - PASS',
         'code_size': 18,
         'callout': 'The one FAIL says exactly what\'s missing: the steps left and down',
         'tone': 'green',
         'notes': 'Running the tests before the fix is deliberate: students see a FAIL that tells '
                  'them what to write, then watch it change. That\'s the habit to build.'},

        # Step 3
        {'kind': 'code', 'title': 'Step 3 · West: copy and flip', 'tag': 'Activity',
         'lead': 'Add this comment between the east loop and the north loop. Under it, copy the '
                 'east loop and flip `<` to `>` and `+ 1` to `- 1`.',
         'lead_h': 1.2,
         'code': '    # West: copy east, flip < to > and + to -',
         'code_size': 24,
         'callout': '**Predict:** run `test_planner()`. What will Leg 2\'s `Actual:` be now?',
         'tone': 'teal',
         'notes': 'The comment goes between east and north so the path still goes across first. '
                  'Answer: Leg 2 still fails, but Actual: is now [(1, 3)]. The step left is there; '
                  'the steps down are not.'},

        {'kind': 'figure', 'title': 'Step 3 · Check your output', 'tag': 'Activity',
         'figure': '/img/lesson-m4-03/one-x-loop-runs.svg',
         'caption': 'Leg 2\'s `Actual:` is now `[(1, 3)]`. Going left, `x < dest_x` is False on '
                    'the first check, so the east loop never runs.',
         'notes': 'The step left is there; the steps down are not. Two x loops can sit next to '
                  'each other because a while loop checks its condition before its first trip. For '
                  'any trip, at most one of the two x loops runs, and the same goes for the two y '
                  'loops. Students reaching for if x < dest_x ... elif: steer them back. The four '
                  'loops handle every case, including same spot (all four skipped, []).'},

        # Step 4
        {'kind': 'code', 'title': 'Step 4 · South', 'tag': 'Activity',
         'lead': 'After the north loop, before `return path`, add this comment and write the '
                 'south loop the same way:',
         'lead_h': 1.2,
         'code': '    # South: copy north, flip < to > and + to -',
         'code_size': 24,
         'callout': 'Run `test_planner()`: five PASS lines. Same column, same row and same spot '
                    'need no code of their own.',
         'tone': 'green',
         'notes': 'A loop with nothing to do never runs.'},

        {'kind': 'code', 'title': 'Step 4 · Check your loops', 'tag': 'Activity',
         'code': '    # West: copy east, flip < to > and + to -\n'
                 '    while x > dest_x:\n'
                 '        x = x - 1\n'
                 '        path.append((x, y))\n'
                 '\n'
                 '    # South: copy north, flip < to > and + to -\n'
                 '    while y > dest_y:\n'
                 '        y = y - 1\n'
                 '        path.append((x, y))',
         'code_size': 22,
         'callout': 'Laid out differently and passes all five tests? Keep yours.',
         'tone': 'green'},

        {'kind': 'figure', 'title': 'Three trips, the same four loops',
         'figure': '/img/lesson-m4-03/four-loops-run.svg',
         'caption': 'A False on the first check means a loop never runs at all.',
         'notes': 'Trip one, (0, 0) to (2, 3): east and north run. Trip two, (3, 3) to (1, 0): '
                  'west and south run. Trip three, (1, 1) to (1, 1): all four are skipped and the '
                  'path is empty.'},

        {'kind': 'check',
         'question': 'For a trip that goes up and to the right, how many of the four while loops '
                     'actually run?',
         'options': ['All four',
                     'Two: the east loop and the north loop',
                     'Just one',
                     'None: it needs if/else'],
         'answer': 1,
         'explanation': 'At most one x loop (east OR west) and one y loop (north OR south) run for '
                        'any trip. The other two find their condition False on the first check.'},

        {'kind': 'steps', 'title': 'The planner\'s three promises',
         'tag': 'Remember',
         'steps': [
             'The path **never includes the start**',
             'The path **ends at the destination**',
             'The path is **empty** if the robot is already there',
         ],
         'notes': 'Every planner in this course keeps them. Keep run_test() in the file: Module 5 '
                  'comes back to it.'},

        # Step 5
        {'kind': 'code', 'title': 'Step 5 · Break it on purpose', 'tag': 'Activity',
         'lead': 'In the west loop, swap the two lines so the `append` comes **before** '
                 '`x = x - 1`:',
         'code': '    while x > dest_x:\n'
                 '        path.append((x, y))\n'
                 '        x = x - 1',
         'code_size': 24,
         'callout': '**Predict:** which tests fail, and what is Leg 2\'s `Actual:`? Then run '
                    '`test_planner()`.',
         'tone': 'teal',
         'notes': 'This breaks promise 1 on purpose because it\'s the one that bites later: a path '
                  'that includes the start gives the driver a zero-length move in Lesson 4-4. '
                  'Don\'t let students "break it" by flipping a + 1 in the east or north loop '
                  'instead: that loop never ends.'},

        {'kind': 'code', 'title': 'Step 5 · What happened?', 'tag': 'Activity',
         'code': 'Leg 2 - FAIL\n'
                 '  Expected: [(1, 3), (1, 2), (1, 1), (1, 0)]\n'
                 '  Actual:   [(2, 3), (1, 2), (1, 1), (1, 0)]',
         'code_size': 22,
         'callout': 'The other four pass. Appending first records where the robot **was**: the '
                    'start sneaks in and (1, 3) is lost. Promise 1 is broken.',
         'tone': 'orange',
         'notes': 'The other four pass because the west loop doesn\'t run for them.'},

        {'kind': 'code', 'title': 'Step 5 · Watch the function run', 'tag': 'Activity',
         'lead': 'When a test fails, don\'t guess. In every loop, right after the `append`, add:',
         'code': '        print("  added:", (x, y))',
         'code_size': 24,
         'callout': 'Run it: the first `added:` is `(2, 3)`, the start. Swap the lines back, run '
                    'until all five pass, then **remove the debug prints**.',
         'tone': 'teal',
         'notes': 'The added: lines show which loop ran and what it added. Removing them keeps the '
                  'output clean for the next step.'},

        {'kind': 'check',
         'question': 'A classmate gets `[(3, 3), (2, 3), (1, 2), (1, 1), (1, 0)]` for (3, 3) to '
                     '(1, 0). What went wrong?',
         'options': ['Nothing: that is a valid Manhattan path',
                     'The west loop appends before it subtracts 1 from x, so the start is '
                     'included and (1, 3) is skipped: promise 1 is broken',
                     'The destination tuple is backwards',
                     'The south loop ran before the west loop'],
         'answer': 1,
         'explanation': 'Swapping the two lines inside a loop (append first, then change x) shifts '
                        'that leg by one: the start appears and the corner is missed. The first '
                        'element should never equal the start.'},

        # Step 6
        {'kind': 'code', 'title': 'Step 6 · Run the main program', 'tag': 'Activity',
         'lead': 'Set the run line back to:',
         'code': 'test_delivery()',
         'code_size': 26,
         'callout': '**Predict:** where does Leg 3 start, and what heading does every line show?',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Step 6 · Check your output', 'tag': 'Activity',
         'code': 'computing path from: (0, 0) to: (2, 3)\n'
                 '[(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]\n'
                 'moving: from (0, 0) to: (1, 0)\n'
                 '...\n'
                 'new position: (2, 3) heading: 0\n'
                 'computing path from: (2, 3) to: (1, 0)\n'
                 '[(1, 3), (1, 2), (1, 1), (1, 0)]\n'
                 '...\n'
                 'new position: (1, 0) heading: 0\n'
                 'computing path from: (1, 0) to: (3, 1)\n'
                 '...',
         'code_size': 18,
         'callout': 'Leg 3 starts at (1, 0), where Leg 2 ended. The driver is still a stub, so the '
                    'heading is still 0.',
         'tone': 'green',
         'notes': 'Trimmed; the full printout is in the reveal on the lesson page. Every path '
                  'starts one step from where its leg began, goes across first, and ends at the '
                  'destination. Legs 3 to 5: [(2, 0), (3, 0), (3, 1)], [(2, 1), (2, 2)], '
                  '[(1, 2), (0, 2), (0, 1), (0, 0)]; the run ends new position: (0, 0) '
                  'heading: 0.'},

        {'kind': 'bullets', 'title': 'Optional: unit tests and the Manhattan class',
         'tag': 'Optional',
         'bullets': [
             '`test_planner()` is a set of **unit tests**: each checks one function on its own, '
             'against an answer worked out separately',
             'The planner only computes, so it can be tested on any computer: **separation of '
             'concerns**',
             'Students who did the Module 2 class extensions can write the planner as a '
             '`Manhattan` class with a `compute_path()` method',
         ],
         'size': 22,
         'notes': 'Both extensions are optional and nothing later depends on them. The class holds '
                  'no state; it exists only so it has the same shape as the Module 5 and 6 planners. '
                  'From then on, class-track students write planner.compute_path(robot_position, '
                  'delivery_destination). The lesson page has the skeleton and the reveal.'},

        {'kind': 'wrapup',
         'questions': [
             'Why four while loops instead of `if/else`?',
             'When are two paths equal with `==`?',
             'What are the planner\'s three promises?',
             'Where does a test\'s expected path come from?',
         ],
         'next': 'the driver',
         'notes': 'Answers: a loop whose condition starts False never runs, so only the right ones '
                  'do. Same positions, in the same order, and the same number of them. No start in '
                  'the path; it ends at the destination; [] when already there. Your own hand '
                  'trace, before you run the code.'},
    ],
}
