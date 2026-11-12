DECK = {
    'module': 4, 'lesson': 4,
    'doc': 'module-04-manhattan/lesson-04-naming-and-testing-the-planner',
    'title': 'Testing the Planner',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'State the function\'s three promises and record them in a docstring',
             'Say what a **unit test** is, and why testing on screen beats debugging on the robot (**separation of concerns**)',
             'Hand-calculate an expected path, then compare it to the actual output',
             'Add a reusable `run_test()` helper to the MANHATTAN PLANNER section, and a test '
             'that runs a suite of six cases through it',
             'Debug a failing test with print statements',
         ],
         'notes': '55 to 70 minutes. Not a line inside the planner changes: it gets its promises '
                  'written down, and unit tests prove them on screen. Two '
                  'non-negotiables: expected paths are calculated by hand before anything runs, and '
                  'the suite covers every direction and edge case.'},

        {'kind': 'bullets', 'title': 'Same function, written promises',
         'bullets': [
             'Last lesson you wrote `compute_manhattan_path()` and it worked',
             'Today you write down what it promises and prove those promises with **unit tests**, '
             'before the robot ever moves',
         ],
         'callout': '**Test on screen before you test on the floor.**',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'What the function promises: a docstring',
         'lead': 'A function is a contract: give me these inputs, and I guarantee this output. Write '
                 'the guarantee in a **docstring**: a string in triple quotes, right under the `def` '
                 'line, that Python keeps attached to the function.',
         'lead_h': 1.25,
         'code': 'def compute_manhattan_path(start, destination):\n'
                 '    """Compute a Manhattan path from start to destination.\n'
                 '\n'
                 '    start:       an (x, y) tuple -- where the robot is now\n'
                 '    destination: an (x, y) tuple -- where it needs to go\n'
                 '\n'
                 '    Returns a list of (x, y) tuples the robot should move to,\n'
                 '    not including the start itself.\n'
                 '    """\n'
                 '    path = []\n'
                 '    ...',
         'code_size': 18,
         'notes': 'Docstrings are new. Show that help(compute_manhattan_path) prints it, and that '
                  'the first line is a one-sentence summary by convention. Don\'t go further than '
                  'that. The last sentence is the one people get wrong: check it against the code. '
                  'The first thing appended to path is the position after the first step, never '
                  'the start itself.'},

        {'kind': 'bullets', 'title': 'The three promises',
         'bullets': [
             'The path **never includes the start**',
             'The path **ends at the destination**',
             'The path is **empty** if you\'re already there: every `while` loop is skipped',
         ],
         'callout': 'Every planner in this course makes the same three promises',
         'tone': 'teal',
         'notes': 'Promise 1 matters because each element is a place to drive to, and the robot '
                  'already stands on the start. It bites in Lesson 4-6: a path that includes the start '
                  'makes the first get_desired_heading() call see a zero move and return None.'},

        {'kind': 'check',
         'question': 'A classmate\'s version returns `[(0, 0), (1, 0), (2, 0)]` for start (0, 0), '
                     'destination (2, 0). Which promise did it break, and why does it matter?',
         'options': ['Promise 2: the path does not end at the destination',
                     'Promise 1: it includes the start, so the robot is told to drive where it already is',
                     'Promise 3: the path should be empty',
                     'No promise was broken; this is also correct'],
         'answer': 1,
         'explanation': 'The path is a list of places to drive TO. The robot is already at (0, 0); '
                        'listing it as a step gives the driving code a zero-length move and a turn '
                        'it cannot work out.'},

        {'kind': 'bullets', 'title': 'In robot.py',
         'bullets': [
             'Replace the one-line docstring with the full one',
             'Run `test_paper_paths()`: same output as last lesson',
         ]},

        {'kind': 'bullets', 'title': 'Unit testing',
         'bullets': [
             'A **unit test** checks one function on its own: inputs you chose, an answer you worked out',
             'Professional software runs thousands on every change, catching a mistake minutes after it is made',
             'A robot driving into a wall says **something** is wrong; a failing test shows the **exact input**',
         ],
         'callout': 'Your planner is an ideal unit: tuples in, list out',
         'tone': 'teal',
         'notes': 'Five minutes of testing saves thirty minutes chasing a robot.'},

        {'kind': 'table', 'title': 'Separation of concerns',
         'lead': '`compute_manhattan_path()` only **computes** a path; the driving functions (Lesson 4-6) '
                 '**drive** it. Each can be checked on its own.',
         'headers': ['Problem', 'Where it runs', 'What you test'],
         'widths': [3, 3, 4],
         'rows': [
             ['Computing the path', 'Any computer', 'Does the path make sense?'],
             ['Driving the path', 'On the robot', 'Does the robot follow it?'],
         ],
         'size': 24,
         'callout': 'The planner is handed the robot\'s position as a parameter, so there is nothing '
                    'to set up before a test: tuples in, list out',
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
         'figure': '/img/lesson-m4-04/test-harness.svg',
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
         'code': '# --- Lesson 4-4: the test harness ---\n'
                 '# run_test() asks the planner for a path and compares it\n'
                 '# with one you traced by hand, printing PASS or FAIL. A\n'
                 '# planner test from here on is a list of run_test() calls.\n'
                 '\n'
                 'def run_test(test_name, start, destination, expected):\n'
                 '    """Plan start -> destination and compare the result\n'
                 '    with expected; print test_name with PASS or FAIL."""\n'
                 '    pass',
         'code_size': 17,
         'callout': 'The body is the expected-vs-actual block with the four values coming in as '
                    'parameters. On a FAIL, print **both** lists.',
         'tone': 'teal',
         'notes': 'A harness is a function whose only job is to test another one. Class-track '
                  'students ask planner.compute_path(start, destination) for the path; the rest '
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
         'code': '    print("Computing from", start, "to", destination)   # first line\n'
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
         'question': 'A classmate runs `compute_manhattan_path((3, 3), (1, 0))` and gets '
                     '`[(3, 3), (2, 3), (1, 2), (1, 1), (1, 0)]`. What went wrong?',
         'options': ['Nothing: that is a valid Manhattan path',
                     'The west loop appends before it subtracts 1, so the start is in and (1, 3) is skipped',
                     'The destination tuple is backwards',
                     'The south loop ran before the west loop'],
         'answer': 1,
         'explanation': 'Swapping the two lines inside a loop (append first, then change x) shifts that '
                        'leg by one: the start appears and the corner is missed. Promise 1 spots it '
                        'fastest: the first element should never equal the start.',
         'notes': 'Answer: B. The append-before-update bug is the one students actually make. '
                  'Promise 1 is broken, and the corner (1, 3) is missing.'},

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
             ('Maps', 'Routing engines', '\nA map app\'s router is handed your location every time '
                                         'you ask. Swap in a bike router and the app does not change.'),
             ('Aerospace', 'Simulation', '\nRockets and planes fly thousands of simulated missions '
                                         'before a real one, catching problems on screen.'),
         ],
         'height': 4.0,
         'notes': '"Verify before you deploy" is everywhere in engineering.'},

        {'kind': 'wrapup',
         'questions': [
             'What are the three promises?',
             'Why test on screen before the robot?',
             'Where does the expected path come from?',
             'What makes a good test suite?',
         ],
         'next': 'turning, so the robot faces the right way at each step',
         'notes': 'Answers: No start in the path; ends at the destination; [] when already there. Faster, and it points to the exact broken input. Hand-calculation, before '
                  'you run the code. Every direction and edge case, not just one happy path. Exit '
                  'ticket: "Write a test for start (1,1), destination (3,2): what\'s the expected '
                  'path?" ([(2,1),(3,1),(3,2)]). The algorithm is proven correct; next lesson tackles '
                  'turning.'},

        {'kind': 'code', 'title': 'Optional: the Manhattan class',
         'tag': 'Optional extension',
         'lead': 'Did the class extensions in Module 2? Here is the same planner as a class. It holds '
                 '**no state**: `compute_path()` is told the robot\'s position every call.',
         'lead_h': 1.2,
         'code': 'path = compute_manhattan_path((0, 0), (2, 3))\n'
                 '\n'
                 'planner = Manhattan()\n'
                 'path = planner.compute_path((0, 0), (2, 3))',
         'code_size': 24,
         'callout': 'Why bother? So it has the **same shape** as the Module 5 and 6 planners (BFS, '
                    'Dijkstra): one main program and one test harness work with any of them by '
                    'changing one name.',
         'tone': 'teal',
         'notes': 'Optional extension, for students who built classes in Module 2. The code is the '
                  'lesson\'s side-by-side: the function call, then the same call on the class. '
                  'From here on, class-track students use their class: when a lesson says '
                  'compute_manhattan_path(position, destination), they write '
                  'planner.compute_path(position, destination), in the test harness, in the final '
                  'project, everywhere.'},

        {'kind': 'code', 'title': 'Optional: the class skeleton',
         'tag': 'Optional extension',
         'lead': 'Paste it in place of `compute_manhattan_path()` (keep your tests), and move the four '
                 'loops into the method. In your tests, `compute_manhattan_path(` becomes '
                 '`planner.compute_path(`.',
         'lead_h': 1.1,
         'code': 'class Manhattan:\n'
                 '    def __init__(self):\n'
                 '        pass        # nothing to set up\n'
                 '\n'
                 '    def compute_path(self, start, destination):\n'
                 '        # your compute_manhattan_path(), unchanged: nothing in\n'
                 '        # it needs self., because the planner holds nothing\n'
                 '        pass\n'
                 '\n'
                 'planner = Manhattan()',
         'code_size': 16,
         'callout': 'No start position in `__init__`, no `self.position`: the planner is still told '
                    'where the robot is',
         'tone': 'teal',
         'notes': 'On the lesson page the skeleton also has a section comment and a docstring (the '
                  '"why bother" from the previous slide); the slide leaves them out to fit. Run '
                  'test_planner() again: six PASS lines. The __init__ is empty because '
                  'Manhattan has nothing to set up; BFS in Module 5 uses its __init__ to hold the '
                  'list of blocked intersections, and that is when the class earns its keep. The '
                  'finished method is behind a reveal on the lesson page and is not shown here. '
                  'Solution file: lesson-05-manhattan-class-addon.py.'},
    ],
}
