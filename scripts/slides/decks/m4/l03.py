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
                  'to PASS.'},

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
                  'get smaller.'},

        {'kind': 'code', 'title': 'Let the computer compare',
         'lead': '`==` works on tuples and on lists:',
         'code': 'print((1, 2) == (1, 2))                      # True\n'
                 'print((1, 2) == (2, 1))                      # False -- order matters\n'
                 'print([(1, 0), (2, 0)] == [(1, 0), (2, 0)])  # True\n'
                 'print([(1, 0), (2, 0)] == [(1, 0)])          # False -- one is shorter',
         'code_size': 18,
         'callout': 'Same items, same order, same number of them: one `==` checks a whole path',
         'tone': 'teal',
         'notes': 'Last lesson students checked three printed paths by eye. With five paths, and a '
                  're-run after every change, that gets slow and easy to get wrong.'},

        {'kind': 'check',
         'question': 'Does `(1, 3) == (3, 1)` evaluate to True?',
         'options': ['Yes: they contain the same numbers',
                     'No: the parts must match in order, and these are swapped',
                     'Yes: tuples ignore order',
                     'It causes an error'],
         'answer': 1,
         'explanation': '(1, 3) is x = 1, y = 3; (3, 1) is x = 3, y = 1. Different intersections, '
                        'so False.'},

        {'kind': 'code', 'title': 'This lesson\'s skeleton: run_test()',
         'code': 'def run_test(test_name, start, destination, expected):\n'
                 '    actual = compute_manhattan_path(start, destination)\n'
                 '    if actual == expected:\n'
                 '        print(test_name, "- PASS")\n'
                 '    else:\n'
                 '        print(test_name, "- FAIL")\n'
                 '        print("  Expected:", expected)\n'
                 '        print("  Actual:  ", actual)',
         'code_size': 18,
         'notes': 'Students paste run_test() below compute_manhattan_path(), replace last lesson\'s '
                  'test_planner() with the five-case version from the lesson page, and add the two '
                  'new comments inside the planner: west between east and north, south after '
                  'north. The slide leaves out the docstring to fit.'},

        {'kind': 'code', 'title': 'The tests use your answer key',
         'code': 'def test_planner():\n'
                 '    # expected = your answer key, traced by hand\n'
                 '    run_test("Leg 1",       (0, 0), (2, 3), [(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)])\n'
                 '    run_test("Leg 2",       (2, 3), (1, 0), [])   # your answer key\n'
                 '    run_test("Same column", (2, 0), (2, 3), [])   # your answer key\n'
                 '    run_test("Same row",    (0, 2), (3, 2), [])   # your answer key\n'
                 '    run_test("Same spot",   (1, 1), (1, 1), [])   # your answer key',
         'code_size': 14,
         'callout': 'Expected paths come from **your own tracing**, never from what the code prints',
         'tone': 'orange',
         'notes': 'Watch for the student who runs the code first and pastes its output into '
                  'expected: then the test only checks that the code agrees with itself.'},

        {'kind': 'steps', 'title': 'Step 1 · Run the tests first',
         'tag': 'Activity',
         'steps': [
             'Replace each `[]` with the path from your answer key (Same spot stays `[]`)',
             'Set the run line to `test_planner()` and run it, **before** you change the planner',
         ],
         'callout': 'Correct: four PASS and one FAIL. Leg 2 expected four steps; actual `[]`',
         'tone': 'green',
         'notes': 'Running the tests before the fix is deliberate: students see a FAIL that tells '
                  'them what to write, then watch it change. Each result sits under the planner\'s '
                  'own computing path line.'},

        {'kind': 'steps', 'title': 'Step 2 · West: copy and flip',
         'tag': 'Activity',
         'steps': [
             'Copy the east loop under the west comment',
             'Flip `<` to `>` and `+ 1` to `- 1`',
             'Run `test_planner()`: Leg 2 still fails, but now with `Actual: [(1, 3)]`',
         ],
         'tone': 'green',
         'notes': 'The step left is there; the steps down are not.'},

        {'kind': 'figure', 'title': 'Why two x loops can sit side by side',
         'figure': '/img/lesson-m4-03/one-x-loop-runs.svg',
         'caption': 'A while loop checks before its first trip. Going left, `x < dest_x` is False at '
                    'once, so only the west loop moves x.',
         'notes': 'For any trip, at most one of the two x loops runs. The same goes for the two y '
                  'loops, so no if/else is needed.'},

        {'kind': 'steps', 'title': 'Step 3 · South',
         'tag': 'Activity',
         'steps': [
             'South is the north loop, flipped the same way',
             'Run `test_planner()`',
         ],
         'callout': 'Correct: five PASS lines',
         'tone': 'green'},

        {'kind': 'check',
         'question': 'For a trip that goes up and to the right, how many of the four while loops '
                     'actually run?',
         'options': ['All four',
                     'Two: the east loop and the north loop',
                     'Just one',
                     'None: it needs if/else'],
         'answer': 1,
         'explanation': 'At most one x loop and one y loop run for any trip. The other two find their '
                        'condition False on the first check.'},

        {'kind': 'figure', 'title': 'Watch the four loops run',
         'figure': '/img/lesson-m4-03/four-loops-xy.svg',
         'caption': 'Each trip runs at most one x loop and one y loop. A False on the first check '
                    'means a loop never runs at all.',
         'notes': 'On the lesson page an animation of three trips is behind a reveal, opened after '
                  'the tests pass; the slide shows the still version.'},

        {'kind': 'steps', 'title': 'Step 4 · Run the main program',
         'tag': 'Activity',
         'steps': [
             'Set the run line back to `test_delivery()` and run it',
             'Leg 1 and Leg 2 match your answer key',
             'Every leg starts one step from where it began, goes across first, and ends at the '
             'destination',
         ],
         'callout': 'The driver is still a stub, so the heading is still 0',
         'tone': 'green',
         'notes': 'The full expected printout is behind a reveal on the lesson page.'},

        {'kind': 'steps', 'title': 'The planner\'s three promises',
         'tag': 'Remember',
         'steps': [
             'The path **never includes the start**: the robot is already there',
             'The path **ends at the destination**',
             'The path is **empty** if the robot is already at the destination',
         ],
         'notes': 'Every planner in this course keeps them. Promise 1 is the one that bites later: '
                  'a path that includes the start gives the driver a zero-length move in Lesson '
                  '4-4. Students reaching for if/else: steer them back. The four loops handle every '
                  'case, including same spot (all four skipped). Keep run_test() in the file: '
                  'Module 5 comes back to it.'},

        {'kind': 'code', 'title': 'When a test fails',
         'lead': 'Don\'t guess: watch it run. In each loop, right after the `append`:',
         'code': '        print("  added:", (x, y))',
         'code_size': 22,
         'callout': 'Try it: change one `+ 1` to `- 1`, watch a test catch it, then change it back. '
                    'Remove the debug prints when done.',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'A classmate gets `[(3, 3), (2, 3), (1, 2), (1, 1), (1, 0)]` for (3, 3) to '
                     '(1, 0). What went wrong?',
         'options': ['Nothing: that is a valid Manhattan path',
                     'The west loop appends before it subtracts 1, so the start is included and '
                     '(1, 3) is skipped: promise 1 is broken',
                     'The destination tuple is backwards',
                     'The south loop ran before the west loop'],
         'answer': 1,
         'explanation': 'Swapping the two lines inside a loop shifts that leg by one: the start '
                        'appears and the corner is missed. The first element should never equal '
                        'the start.'},

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
                  'do. Same positions, same order, same number of them. No start in the path; it '
                  'ends at the destination; [] when already there. Your own hand trace, before you '
                  'run the code.'},
    ],
}
