DECK = {
    'module': 5, 'lesson': 6,
    'doc': 'module-05-pathfinding/lesson-06-testing-and-swapping',
    'title': 'Testing and Swapping',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Explain why an exact-match test is wrong for BFS and right for Manhattan',
             'Name the **five properties** every correct path has, and write each as one `if`',
             'Explain why the walled-off case needs its own test',
             'Hand a function to another function, and explain what `planner(position, destination)` does in the harness',
             'Run one harness against Manhattan and BFS and explain every FAIL line',
             'Write a main program that works with either planner by changing **one name**',
         ],
         'notes': '50 to 60 minutes. The planner passes five tests; now test it properly. The '
                  'property-versus-exact idea outlasts this course, so say so. Then one small trick '
                  'points the same tests at Module 4\'s Manhattan planner, which fails on paper for '
                  'exactly the reason this module exists.'},

        {'kind': 'code', 'title': 'Two right answers',
         'lead': 'Compare your Lesson 5-5 Test 1 path with a classmate\'s. Different? Good. If not, here\'s '
                 'another correct one:',
         'lead_h': 1.2,
         'code': '[(1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)]   # yours, maybe\n'
                 '[(0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3)]   # also six steps, also right',
         'code_size': 20,
         'callout': 'Both go from `(0, 0)` to `(3, 3)` in six steps, and both are shortest',
         'tone': 'teal',
         'notes': 'Have pairs actually compare paths on screen before showing the slide.'},

        {'kind': 'code', 'title': '...and one test',
         'lead': 'Module 4\'s test from Lesson 4-5, still in your file as `run_test()`:',
         'lead_h': 0.8,
         'code': 'if actual == expected:\n'
                 '    print(test_name, "- PASS")',
         'code_size': 26, 'width': 8,
         'callout': 'One of those two correct paths gets marked **FAIL**. Fine for Manhattan, which has '
                    'exactly one answer. BFS doesn\'t.',
         'tone': 'orange',
         'notes': 'A different kind of test gets a different name. run_test() stays in the MANHATTAN '
                  'PLANNER section, doing the job it was written for. Reusing the name with a different '
                  'parameter list would silently replace it and break test_planner().'},

        {'kind': 'bullets', 'title': 'Test what must be true',
         'lead': 'Forget the exact list. What has to be true of **any** correct path from `(0, 0)` to `(3, 3)`?',
         'lead_h': 0.85,
         'bullets': [
             '**1.** The first step is next to the start',
             '**2.** The last step is the destination',
             '**3.** Every step is next to the one before it',
             '**4.** No step is a blocked intersection',
             '**5.** With nothing blocked, the number of steps is the Manhattan distance',
         ],
         'size': 26,
         'callout': 'A **property test**: check what must be true, not what you happened to expect',
         'tone': 'teal',
         'notes': 'Five one-line checks. Together they are stricter than an exact match: an exact match '
                  'cannot tell you a path is valid, only that it is the one you expected. And they allow '
                  'every correct answer.'},

        {'kind': 'figure', 'title': 'The five properties on the wall test',
         'figure': '/img/lesson-m5-06/path-properties-xy.svg',
         'caption': 'The checks never ask which shortest path you found, only whether it is a legal one '
                    'of the right length.',
         'notes': 'Left: the BFS path around the wall, 7 steps, properties 1 to 4 holding. Right: '
                  'Manhattan goes straight through blocked (1, 0) and fails property 4. The fifth '
                  'property is only checked on an open grid.'},

        {'kind': 'check',
         'question': 'Why are the five property checks stronger than comparing with one expected path?',
         'options': ['They check that a path is valid, and accept every correct answer instead of just one',
                     'They run faster',
                     'They do not need to know the destination',
                     'They are not stronger: an exact match is always better'],
         'answer': 0,
         'explanation': 'An exact match passes only the path you wrote down, even if your expectation was '
                        'wrong. The properties check validity directly, and any shortest path passes.'},

        {'kind': 'code', 'title': 'Add to robot.py: the property harness',
         'lead': 'At the end of the BFS PLANNER section. First the header and two helpers:',
         'lead_h': 0.7,
         'code': '# --- Lesson 5-6: the property harness ---\n'
                 '# Tests any planner by what must be true of its path, not by\n'
                 '# one expected list, because BFS has many right answers.\n'
                 '# run_all_tests() is handed a planner FUNCTION and runs the\n'
                 '# six cases through it: one program tests Manhattan and BFS.\n'
                 '# Module 4\'s run_test() stays; exact match is right there.\n'
                 '\n'
                 'def manhattan_distance(a, b):\n'
                 '    """Steps between a and b with nothing in the way."""\n'
                 '    pass\n'
                 '\n'
                 'def is_neighbor(a, b):\n'
                 '    """True when a and b are one step apart."""\n'
                 '    pass',
         'code_size': 17,
         'notes': 'The skeleton is one paste on the lesson page; the slides show it in four parts. The two '
                  'helpers and the checker are the students\' to write; run_all_tests() and navigate() are '
                  'given, because they are the "same program" in "same program, swap the planner".'},

        {'kind': 'code', 'title': 'The skeleton: the checker',
         'notes': "Students write this in Step 2. The outline's first line after problems = [] is the empty-path special case.",
         'code': 'def check_path(path, start, destination):\n'
                 '    """Return a list of everything wrong with path as a route\n'
                 '    from start to destination; [] means it is good."""\n'
                 '    # problems = []\n'
                 '    # an empty path is fine only if already there; return\n'
                 '    # 1. first step next to the start?\n'
                 '    # 2. last step the destination?\n'
                 '    # 3. every step next to the one before it?\n'
                 '    # 4. no step in BLOCKED?\n'
                 '    # return problems\n'
                 '    pass',
         'code_size': 19,
         'callout': 'Properties 1 to 4. The fifth, the step count, is checked by the test that calls it.',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'The skeleton: the two tests',
         'notes': 'Students write both in Step 3, after the idea of handing over a function. Each returns True on a pass so run_all_tests() can count.',
         'code': 'def run_path_test(test_name, planner, start, destination, expected_steps):\n'
                 '    """Ask planner for a path, check the five properties, print\n'
                 '    PASS or FAIL with the path; return True on a pass."""\n'
                 '    # path = planner(start, destination)\n'
                 '    # problems from check_path(), plus 5. the step count\n'
                 '    # no problems: print "  PASS ", test_name, "", path\n'
                 '    # otherwise: print "  FAIL " the same way, then each\n'
                 '    # problem on its own line, "          - " in front\n'
                 '    pass\n'
                 '\n'
                 'def run_no_path_test(test_name, planner, start, destination):\n'
                 '    """For a walled-off destination the only right answer is\n'
                 '    []; print PASS or FAIL and return True on a pass."""\n'
                 '    pass',
         'code_size': 18},

        {'kind': 'code', 'title': 'The skeleton: run_all_tests() is given',
         'lead': 'The suite. Each case is one `if`, and a pass adds one to `passed`. It starts like this:',
         'lead_h': 0.75,
         'code': 'def run_all_tests(name, planner):\n'
                 '    """The six cases, through whichever planner is handed in:\n'
                 '    four on the open grid, the wall, and walled off."""\n'
                 '    print("==========", name, "==========")\n'
                 '    passed = 0\n'
                 '    clear_blocked()\n'
                 '    if run_path_test("open (0, 0) to (3, 3)", planner, (0, 0), (3, 3), 6):\n'
                 '        passed = passed + 1',
         'code_size': 18,
         'callout': 'It ends by printing how many of the 6 passed',
         'tone': 'teal',
         'notes': 'The rest of run_all_tests() is five more cases in the same pattern (next slide), with '
                  'add_blocked() calls before the wall cases, then clear_blocked() and the count. '
                  'navigate() is the last given function; it comes up in the swap activity.'},

        {'kind': 'table', 'title': 'The six cases in run_all_tests()',
         'headers': ['Case', 'Trip', 'Blocked', 'Expect'],
         'widths': [2.6, 3.0, 3.4, 2.2],
         'rows': [
             ['open', '`(0, 0)` to `(3, 3)`', 'nothing', '6 steps'],
             ['open', '`(0, 0)` to `(0, 3)`', 'nothing', '3 steps'],
             ['open', '`(2, 1)` to `(0, 3)`', 'nothing', '4 steps'],
             ['open', '`(1, 1)` to `(1, 1)`', 'nothing', '0 steps'],
             ['wall', '`(0, 0)` to `(3, 0)`', '`(1, 0)`, `(1, 1)`', '7 steps'],
             ['walled off', '`(0, 0)` to `(3, 0)`', 'the whole column at x = 1', '`[]`'],
         ],
         'notes': 'The first five go through run_path_test(); the walled-off case goes through '
                  'run_no_path_test(). The harness blocks the wall itself with add_blocked() and clears '
                  'the list before and after.'},

        {'kind': 'steps', 'title': 'Step 1 · Two helpers',
         'steps': [
             '`manhattan_distance()` is the Lesson 5-1 count: the x difference plus the y difference, each made positive with `abs()`',
             '`is_neighbor()` asks whether that distance is **exactly 1**',
         ],
         'size': 24,
         'notes': 'Both are one line. is_neighbor() calls manhattan_distance(), the same one function '
                  'calling another idea as the sensor toolkit.'},

        {'kind': 'steps', 'title': 'Step 2 · check_path() returns a list of problems',
         'steps': [
             'One `if` per property, each appending a sentence to `problems` when it fails. An empty list means the path is good',
             'First the special case: an empty path is correct when `position == destination` and a problem otherwise. Either way there are no steps to check, so return at once',
             'Property 3 is a loop from the second step to the last, comparing each with the one before. Property 4 is a loop over every step',
         ],
         'size': 21,
         'notes': 'Returning problems rather than True or False is deliberate: see the next slide.'},

        {'kind': 'code', 'title': 'Make the sentences specific',
         'lead': 'Build each sentence with `+` and `str()`. Property 1\'s:',
         'lead_h': 0.8,
         'code': '"first step " + str(path[0]) + " is not next to the start " + str(position)',
         'code_size': 20,
         'callout': 'A test that says only FAIL is a test you\'ll ignore. "drives through blocked '
                    'intersection (1, 0)" tells you what to fix.',
         'tone': 'orange',
         'notes': 'The others follow the same pattern: name the step, say what is wrong with it.'},

        {'kind': 'bullets', 'title': 'One case check_path() can\'t judge',
         'notes': 'This is the third wrap-up question.',
         'bullets': [
             'An empty path when the destination is walled off is **correct**',
             'But `check_path` can\'t tell "walled off" from "forgot to look"',
             'So the walled-off case gets its own small test, `run_no_path_test()`, where the only right answer is `[]`',
         ],
         'callout': 'Lesson 5-5\'s Tests 3 and 5 both returned `[]`. Now the harness tells them apart.',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'A planner returns `[(0,1), (0,3)]` for `(0,0)` to `(0,3)`. Which property fails, '
                     'and what does the FAIL line say?',
         'options': ['Property 3: "step (0, 3) is not next to (0, 1)"',
                     'Property 1: the first step is not next to the start',
                     'Property 2: the last step is not the destination',
                     'Nothing fails: it reaches the destination'],
         'answer': 0,
         'explanation': '(0,1) and (0,3) are two apart. The first step is fine, the last step is the '
                        'destination, but the middle is a gap, and the step count (2 instead of 3) fails too.',
         'notes': 'Answer: A. This is the exit ticket.'},

        {'kind': 'code', 'title': 'Step 3 · Hand the harness its planner',
         'notes': 'Read the last two lines aloud: the name of the function, with no parentheses, goes in like any other value.',
         'lead': 'The one new Python idea in the lesson. Look at the last two lines:',
         'lead_h': 0.8,
         'code': 'def run_path_test(test_name, planner, start, destination, expected_steps):\n'
                 '    path = planner(start, destination)\n'
                 '    ...\n'
                 '\n'
                 'run_all_tests("Manhattan", compute_manhattan_path)\n'
                 'run_all_tests("BFS", compute_bfs_path)',
         'code_size': 20,
         'callout': '`compute_bfs_path` with **no parentheses** is the function itself, handed over the '
                    'way you\'d hand over a number or a list',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'A function in a parameter',
         'bullets': [
             '`run_all_tests` passes the function straight on to `run_path_test`',
             'There, `planner` holds that function, and `planner(position, destination)` calls **whichever one was handed in**',
             'Both planners have the same shape, so the harness never needs to know which one it has',
             'Try it at the prompt first: `f = compute_bfs_path`, then `f((0, 0), (3, 3))`',
         ],
         'size': 24,
         'notes': 'The prompt demo prevents most of the parentheses slips. Do it on the projector.'},

        {'kind': 'figure', 'title': 'A slot shaped like a planner call',
         'figure': '/img/lesson-m5-06/planner-slot.svg',
         'crop': (0.0, 0.0, 1.0, 0.87),
         'caption': 'The harness has a slot shaped like a planner call. Any function that fits can be handed in.',
         'notes': 'The figure on the lesson page has one more line at the bottom, "hand the harness a '
                  'function, no parentheses", which the slide renderer cuts off; the next slide says it.'},

        {'kind': 'bullets', 'title': 'No parentheses when you hand it over',
         'bullets': [
             '`run_all_tests("BFS", compute_bfs_path)` passes the function',
             '`run_all_tests("BFS", compute_bfs_path())` **calls** it first, with no arguments, and passes the result: an error',
         ],
         'size': 26,
         'callout': 'The parentheses are the difference between "here is the planner" and "here is what '
                    'the planner said"',
         'tone': 'orange',
         'notes': 'The parentheses slip in the run_all_tests call is the first of the two things to listen '
                  'for during the activity.'},

        {'kind': 'code', 'title': 'Write run_path_test() and run_no_path_test()',
         'notes': 'The second line is a FAIL with two problems, each on its own line with the dash in front. The wording of the problems can differ; what matters is that each names the step that broke the property.',
         'lead': 'Each returns `True` on a pass, so `run_all_tests()` can count. A PASS line and a FAIL line '
                 'should look like this:',
         'lead_h': 1.2,
         'code': '  PASS  open (0, 0) to (0, 3)  [(0, 1), (0, 2), (0, 3)]\n'
                 '  FAIL  wall at (1,0),(1,1): (0,0) to (3,0)  [(1, 0), (2, 0), (3, 0)]\n'
                 '          - drives through blocked intersection (1, 0)\n'
                 '          - expected 7 steps, got 3',
         'code_size': 20,
         'callout': 'The print format is in the outline',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'Inside run_path_test, what does `path = planner(position, destination)` do when '
                     'the harness was handed compute_bfs_path?',
         'notes': 'Answer: A. The lesson\'s question says the harness was called with '
                  'run_all_tests("BFS", compute_bfs_path); the slide shortens that to fit. planner is a '
                  'parameter holding a function, and calling it calls the function that was passed in.',
         'options': ['Calls `compute_bfs_path(start, destination)`: whichever planner was handed in',
                     'Calls every planner in the file',
                     'Looks up a planner named "BFS"',
                     'Causes an error, because `planner` is a parameter'],
         'answer': 0,
         'explanation': 'planner is a parameter holding a function. Calling it calls the function that was '
                        'passed in. Hand it compute_manhattan_path instead and the same line tests Manhattan.'},

        {'kind': 'steps', 'title': 'Activity · Run it against both',
         'steps': [
             'Write `test_harness()`: the two `run_all_tests()` lines. Set the run line to it',
             'BFS should pass **6 of 6**',
             'Then read Manhattan\'s lines **carefully**',
         ],
         'size': 24,
         'notes': 'Let students discover Manhattan\'s FAIL lines by running it, rather than telling them '
                  'in advance. "Run it against Manhattan and read what it says" lands harder than any '
                  'explanation.'},

        {'kind': 'code', 'title': 'Manhattan through the harness',
         'code': '========== Manhattan ==========\n'
                 '  PASS  open (0, 0) to (3, 3)  [(1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)]\n'
                 '  PASS  open (0, 0) to (0, 3)  [(0, 1), (0, 2), (0, 3)]\n'
                 '  PASS  open (2, 1) to (0, 3)  [(1, 1), (0, 1), (0, 2), (0, 3)]\n'
                 '  PASS  open (1, 1) to (1, 1)  []\n'
                 '  FAIL  wall at (1,0),(1,1): (0,0) to (3,0)  [(1, 0), (2, 0), (3, 0)]\n'
                 '          - drives through blocked intersection (1, 0)\n'
                 '          - expected 7 steps, got 3\n'
                 '  FAIL  walled off: (0,0) to (3,0)  [(1, 0), (2, 0), (3, 0)]\n'
                 '          - there is no way through, so the path should be empty\n'
                 'Manhattan: 4 of 6 passed',
         'code_size': 18,
         'callout': 'Manhattan isn\'t broken: across, then up or down, with no idea what a wall is. The '
                    'harness just showed **why this module exists**.',
         'tone': 'green',
         'notes': 'Manhattan is doing exactly what it was built to do in Module 4. The harness shows it '
                  'on paper, with the path printed.'},

        {'kind': 'code', 'title': 'The same swap in a main program',
         'lead': '`navigate()` is the skeleton\'s last function, given: it plans with whatever planner it\'s '
                 'handed, prints the path, and returns where the robot **would** be.',
         'lead_h': 1.2,
         'code': 'def navigate(planner, position, destination):\n'
                 '    """Plan with planner and print the path; return\n'
                 '    destination, where the robot would be after driving it."""\n'
                 '    path = planner(position, destination)\n'
                 '    print("  Path from", position, "to", destination, ":", path, " Steps:", len(path))\n'
                 '    return destination',
         'code_size': 18,
         'notes': 'Returning the destination is all a paper test needs: it is where the robot would be '
                  'after driving the path.'},

        {'kind': 'code', 'title': 'test_swap(): change one name',
         'notes': 'test_swap() runs each planner there and back: (0, 0) to (3, 3), then from position back to (0, 0). Manhattan drives through the wall at (2, 0); BFS goes around it.',
         'lead': 'Block `(2, 0)`, then run two trips, `(0, 0)` to `(3, 3)` and back, with each planner. '
                 'Only the planner\'s name changes:',
         'lead_h': 1.2,
         'code': 'position = navigate(compute_manhattan_path, (0, 0), (3, 3))   # through the wall\n'
                 'position = navigate(compute_bfs_path, (0, 0), (3, 3))         # around it',
         'code_size': 20,
         'callout': 'Same program, swap the planner',
         'tone': 'teal'},

        {'kind': 'steps', 'title': 'Break a property on purpose',
         'lead': 'Watch the harness catch it. Put each back before the next.',
         'lead_h': 0.65,
         'steps': [
             'Make `compute_bfs_path` return `path[1:]`: it drops the first step',
             'Then make it return `path + [destination]`',
             'Which property catches each?',
         ],
         'size': 24,
         'notes': 'Answers: dropping the first step fails property 1, "first step (2, 0) is not next to the '
                  'start (0, 0)". Appending the destination again fails property 3, "step (3, 3) is not '
                  'next to (3, 3)": an intersection is not its own neighbor. Both fail the step count too. '
                  'Challenge for early finishers: add a sixth property, "no intersection appears twice". '
                  'Can BFS ever fail it? Could a buggy planner?'},

        {'kind': 'bullets', 'title': 'Optional: the harness with planner objects',
         'tag': 'Optional extension',
         'bullets': [
             'With Lesson 5-5\'s classes, the harness is handed an **object** and calls its methods',
             'Both classes have `add_blocked()`, `clear_blocked()` and `compute_path()`, so the harness never needs to know which it holds',
             '`Manhattan.add_blocked()` does nothing, so `Manhattan()` fails the same two tests for the same reason: the correct result',
         ],
         'size': 20,
         'split': 0.45,
         'code': 'run_all_tests("Manhattan", Manhattan())\n'
                 'run_all_tests("BFS", BFS())\n'
                 '\n'
                 '# inside the harness:\n'
                 'path = planner.compute_path(start, destination)\n'
                 'block(planner, (1, 0))\n'
                 'clear(planner)',
         'code_size': 16,
         'notes': 'Optional extension for the class track. The four edits: run_path_test() and '
                  'run_no_path_test() call planner.compute_path(start, destination); run_all_tests() '
                  'calls block(planner, ...) and clear(planner); check_path()\'s property 4 reads '
                  'HARNESS_BLOCKED; test_harness() hands in Manhattan() and BFS(). test_swap() gets the '
                  'same treatment. Solution file: lesson-06-testing-class-addon.py.'},

        {'kind': 'code', 'title': 'Optional: the harness keeps its own record',
         'tag': 'Optional extension',
         'lead': 'Property 4 needs to know what\'s blocked, but the list now lives **inside** the planner. '
                 'Paste above `manhattan_distance()`:',
         'lead_h': 1.2,
         'code': '# class track: the harness\'s own record of what it blocked\n'
                 'HARNESS_BLOCKED = []\n'
                 '\n'
                 'def block(planner, intersection):\n'
                 '    """Tell planner about intersection AND note it in\n'
                 '    HARNESS_BLOCKED, so check_path() can see it."""\n'
                 '    pass\n'
                 '\n'
                 'def clear(planner):\n'
                 '    """Tell planner to forget its blocks, and forget ours."""\n'
                 '    pass',
         'code_size': 18,
         'notes': 'Why not read planner.blocked directly? Manhattan has no such attribute, and the harness '
                  'is not supposed to know what is inside a planner: it only uses the three shared '
                  'methods. That is the lesson\'s optional check question. The finished helpers are in a '
                  'reveal on the lesson page and are not shown here.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Software', 'Property-based testing', 'Professional test tools generate thousands of random '
                                                    'inputs and check properties, because most real programs '
                                                    'have no single expected answer.'),
             ('Design', 'Plug-in parts', 'Handing a function or object to code that doesn\'t know which one '
                                         'it got is how programs are built from swappable parts.'),
             ('Robotics', 'Test before you drive', 'Teams test the planner on a laptop: it\'s faster, and it '
                                                   'separates "the algorithm is wrong" from "the robot drove wrong".'),
         ],
         'height': 4.2,
         'notes': 'Sort orders, file formats and planners are all examples of swappable parts.'},

        {'kind': 'wrapup',
         'questions': [
             'Why not compare with one expected path?',
             'What are the five properties?',
             'Why does walled-off get its own test?',
             'What\'s passed in `run_all_tests("BFS", compute_bfs_path)`?',
             'Why does Module 4\'s `run_test()` keep its name and its job?',
         ],
         'next': 'the planner goes on the robot',
         'notes': 'Answers: BFS has many correct answers; the properties allow all of them and check '
                  'validity. Starts next to the start, ends at the destination, every step a neighbor, no '
                  'blocked step, Manhattan-distance length on an open grid. check_path can\'t tell it from '
                  'a broken planner\'s []. The function itself. Exact match is right for a planner with one '
                  'answer. Formative: the five properties from memory, the no-parentheses explanation, '
                  'Manhattan\'s FAIL lines read and explained. Next lesson the rangefinder loop calls '
                  'add_blocked() exactly as this harness did, so passing these tests means the robot will '
                  're-plan correctly. Module 6, if you do it, adds a third planner to this same harness.'},
    ],
}
