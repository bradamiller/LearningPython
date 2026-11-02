DECK = {
    'module': 4, 'lesson': 6,
    'doc': 'module-04-manhattan/lesson-06-testing-without-a-robot',
    'title': 'Testing Without a Robot',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Explain why testing on screen is faster than debugging on the robot',
             'Describe **separation of concerns**: planning (math) vs. driving (hardware)',
             'Hand-calculate an expected path, then compare it to the actual output',
             'Add a reusable `run_test()` helper to the MANHATTAN PLANNER section, and a test that runs six cases through it',
             'Debug a failing test with print statements',
         ],
         'notes': '50 minutes. The planner is pure math, so it can be proven correct before the robot '
                  'ever moves. Two non-negotiables today: expected paths are calculated by hand before '
                  'anything runs, and the suite covers every direction and edge case.'},

        {'kind': 'bullets', 'title': 'Pure math is a gift',
         'bullets': [
             'Your `compute_manhattan_path()` is pure math: **no motors, no sensors**',
             'You can prove it\'s correct on any computer **before the robot ever moves**',
             'Today: the habit real software engineers live by',
         ],
         'callout': '**Test on screen before you test on the floor.**',
         'tone': 'teal',
         'notes': 'Repeat the motto until it sticks. Five minutes of testing saves thirty minutes '
                  'chasing a robot.'},

        {'kind': 'bullets', 'title': 'Why test without the robot?',
         'bullets': [
             'Would a pilot fly a brand-new plane without testing the engines on the ground?',
             'A robot driving into a wall tells you **something** is wrong, but not **what** or **where**',
             'A failing test on screen tells you the **exact input** that produced the wrong output',
         ],
         'callout': 'Because the planner is just math, you can run it hundreds of times in seconds: '
                    'no grid, no batteries, no chasing a robot across the room',
         'tone': 'orange'},

        {'kind': 'table', 'title': 'Separation of concerns',
         'lead': '`compute_manhattan_path()` only **computes** a path; the driving functions (Lesson 4-8) '
                 '**drive** it. Each can be checked on its own.',
         'headers': ['Problem', 'Where it runs', 'What you test'],
         'widths': [3, 3, 4],
         'rows': [
             ['Computing the path', 'Any computer', 'Does the path make sense?'],
             ['Driving the path', 'On the robot', 'Does the robot follow it?'],
         ],
         'size': 24,
         'callout': 'The planner is handed the robot\'s position and never stores it (Lesson 4-5), so '
                    'there is nothing to set up before a test: tuples in, list out',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'What does \'separation of concerns\' let you do here?',
         'options': ['Run the robot faster',
                     'Test the path-planning math on its own, separately from the driving',
                     'Skip testing entirely',
                     'Combine planning and driving into one function'],
         'answer': 1,
         'explanation': 'Because the planner only computes paths and the driving functions only drive '
                        'them, you can verify the algorithm on any computer before hardware is ever '
                        'involved.'},

        {'kind': 'code', 'title': 'Expected vs. actual',
         'lead': 'Decide what the answer **should** be by hand, then check whether the code agrees. '
                 'Hand-trace (0,0) → (2,3): right 2, then up 3.',
         'lead_h': 1.15,
         'code': 'expected = [(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]\n'
                 '\n'
                 'actual = compute_manhattan_path((0, 0), (2, 3))\n'
                 '\n'
                 'if actual == expected:\n'
                 '    print("Test 1: PASS")\n'
                 'else:\n'
                 '    print("Test 1: FAIL")\n'
                 '    print("  Expected:", expected)\n'
                 '    print("  Actual:  ", actual)',
         'code_size': 19,
         'notes': 'This is the heart of testing. The block is on the lesson page as written; the next '
                  'slide is its picture.'},

        {'kind': 'figure', 'title': 'Two sources, one comparison',
         'figure': '/img/lesson-m4-06/test-harness.svg',
         'caption': 'The test is only worth something because the two sides were worked out '
                    'independently.'},

        {'kind': 'bullets', 'title': 'Expected comes from you',
         'bullets': [
             'The expected list has to come from **your own** tracing',
             'Copy whatever the code prints and call it "expected"?',
             ['You haven\'t tested anything', 'You\'ve **assumed** the code is right'],
         ],
         'callout': 'A test needs an **independent** source of truth: your trace',
         'tone': 'orange',
         'notes': 'Watch for the student who runs the code first and pastes the output into expected: '
                  'that student\'s suite will pass on day one and hide a real bug on day three.'},

        {'kind': 'check',
         'question': 'Where should the \'expected\' path come from?',
         'options': ['Whatever the code prints when you run it',
                     'Hand-calculated by you, before running the code',
                     'A random guess',
                     'The robot\'s actual movement'],
         'answer': 1,
         'explanation': 'Testing needs an independent source of truth. You trace the path by hand '
                        'first; the whole point is to catch the case where the code disagrees with '
                        'the correct answer.'},

        {'kind': 'code', 'title': 'Add to robot.py: the test harness',
         'lead': 'That compare-and-report pattern repeats for every case, so it becomes a function. '
                 'Paste this at the **end** of the MANHATTAN PLANNER section.',
         'lead_h': 1.15,
         'code': '# --- Lesson 4-6: the test harness ---\n'
                 '# run_test() asks the planner for a path and compares it\n'
                 '# with one you traced by hand, printing PASS or FAIL. A\n'
                 '# planner test from here on is a list of run_test() calls.\n'
                 '\n'
                 'def run_test(test_name, position, destination, expected):\n'
                 '    """Plan position -> destination and compare the result\n'
                 '    with expected; print test_name with PASS or FAIL."""\n'
                 '    pass',
         'code_size': 17,
         'callout': 'The body is the expected-vs-actual block with the four values coming in as '
                    'parameters. On a FAIL, print **both** lists.',
         'tone': 'teal',
         'notes': 'A harness is a function whose only job is to test another one. Class-track '
                  'students ask planner.compute_path(position, destination) for the path; the rest '
                  'is the same. The finished run_test() is behind a reveal on the lesson page.'},

        {'kind': 'code', 'title': 'Activity · A suite of cases',
         'tag': 'Activity',
         'lead': 'Write `test_planner()`: six `run_test()` calls, each case one line. One is worked out; '
                 'trace the other five, then fill them in.',
         'lead_h': 1.15,
         'code': 'run_test("Forward right", (0, 0), (2, 3), [(1,0), (2,0), (2,1), (2,2), (2,3)])\n'
                 'run_test("Backward left", (2, 3), (0, 0), [ ... ])   # trace it, then fill it in\n'
                 'run_test("Same column",   (1, 0), (1, 3), [ ... ])\n'
                 'run_test("Same row",      (0, 2), (3, 2), [ ... ])\n'
                 'run_test("Same spot",     (1, 1), (1, 1), [ ... ])\n'
                 'run_test("One step",      (0, 0), (0, 1), [ ... ])',
         'code_size': 17,
         'callout': '**Work each expected out by hand before you run anything.**',
         'tone': 'orange',
         'notes': 'Don\'t hand the expected values out: the hand-tracing is the lesson. Trace on the '
                  'Lesson 4-1 grid worksheet.'},

        {'kind': 'bullets', 'title': 'Six PASS lines, and why six',
         'bullets': [
             'A test whose expected came from the program\'s own output proves nothing except that the program **agrees with itself**',
             'If a test fails, one of two things is wrong: **your trace or your code**. Finding out which is the skill',
             'Set the run line to `test_planner()`. Six PASS lines is the goal; the robot does not move',
             'Only ever test (0,0) → (2,3), and a bug that only shows up going **backward** slips right past you',
         ],
         'callout': 'A good suite covers **every direction and every edge case**',
         'tone': 'teal',
         'notes': 'Celebrate the FAILs: reframe a failing test as the test doing its job. "The test '
                  'found a bug for you."'},

        {'kind': 'check',
         'question': 'Your test shows actual = `[(1,0),(2,0),(2,1)]` but expected = '
                     '`[(1,0),(2,0),(2,1),(2,2),(2,3)]`. What\'s the likely problem?',
         'options': ['The robot battery is low',
                     'The north (y) loop stops early or doesn\'t run fully: the moves up are missing',
                     'The test is wrong',
                     'Nothing: that output is fine'],
         'answer': 1,
         'explanation': 'The moves across are all there but the moves up are cut short. That points '
                        'straight at the north while loop: exactly the kind of pinpointing '
                        'screen-testing gives you.'},

        {'kind': 'code', 'title': 'Activity · Debug a failing test',
         'tag': 'Activity',
         'lead': 'When a test fails, don\'t guess: add print statements inside '
                 '`compute_manhattan_path` to watch the logic run. One at the top, and one inside each '
                 'loop right after the `append`:',
         'lead_h': 1.25,
         'code': '    print("Computing from", position, "to", destination)   # first line\n'
                 '    ...\n'
                 '        print("  added:", (x, y))                          # in each loop',
         'code_size': 18,
         'callout': 'The trace shows exactly which loop ran and what it appended',
         'tone': 'teal'},

        {'kind': 'steps', 'title': 'Try it: catch a bug on purpose',
         'steps': [
             'Change one `+ 1` to `- 1` in `compute_manhattan_path`',
             'Run `test_planner()` and watch a test **catch the bug**',
             'Change it back',
         ],
         'callout': 'Once you\'ve found and fixed a bug, **remove the debug prints** so the output '
                    'stays clean',
         'tone': 'orange'},

        {'kind': 'check',
         'question': 'After using print statements to fix a bug, what should you do with them?',
         'options': ['Leave them in: more output is always better',
                     'Remove or comment them out so the test output stays clean',
                     'Move them outside the function',
                     'Turn them into knowledge checks'],
         'answer': 1,
         'explanation': 'Debug prints are scaffolding. Once the bug is fixed, clear them so future test '
                        'runs are easy to read.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Software', 'Unit tests', '\nProfessional code ships with automated tests that check '
                                        'each function against known answers: a formal version of '
                                        'run_test().'),
             ('Aerospace', 'Simulation', '\nRockets and planes fly thousands of simulated missions '
                                         'before a real one, catching problems on screen.'),
             ('Cars', 'Digital twins', '\nSelf-driving systems test on virtual roads first: far '
                                       'cheaper and safer than a real crash.'),
         ],
         'height': 4.0,
         'notes': '"Verify before you deploy" is everywhere in engineering.'},

        {'kind': 'wrapup',
         'questions': [
             'Why test on screen before the robot?',
             'Where does the expected path come from?',
             'What makes a good test suite?',
         ],
         'next': 'turning, so the robot faces the right way at each step',
         'notes': 'Answers: faster, and it points to the exact broken input. Hand-calculation, before '
                  'you run the code. Every direction and edge case, not just one happy path. Exit '
                  'ticket: "Write a test for position (1,1), destination (3,2): what\'s the expected '
                  'path?" ([(2,1),(3,1),(3,2)]). The algorithm is proven correct; next lesson tackles '
                  'turning.'},
    ],
}
