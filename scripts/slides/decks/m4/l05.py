DECK = {
    'module': 4, 'lesson': 5,
    'doc': 'module-04-manhattan/lesson-05-manhattan-function',
    'title': 'A Reusable Planner Function',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Rename `compute_path()` to `compute_manhattan_path(position, destination)`, update every call, and say why each part of the name matters',
             'State the function\'s **three promises**',
             'Write a **docstring** that records those promises',
             'Explain why the planner takes the robot\'s position as a **parameter** instead of storing it',
             'Write a paper test that calls the planner from several positions, and check each result by hand',
         ],
         'notes': '50 minutes. A small lesson on purpose: students own the algorithm from 4-4, so '
                  'keep the load on the contract. Not a line inside the function changes.'},

        {'kind': 'bullets', 'title': 'Same function, its real name',
         'bullets': [
             'Last lesson you wrote `compute_path()` and it worked',
             'Today **not a single line inside it changes**',
             'You give it its real name and **write down exactly what it promises**',
             'And you settle one design rule the rest of the course depends on',
         ],
         'callout': '**The planner is told where the robot is. It never remembers.**',
         'tone': 'teal',
         'notes': 'Small lesson, big consequences: Module 5 swaps in a completely different planner '
                  'behind this same function shape, and nothing else has to change.'},

        {'kind': 'code', 'title': 'A rename with a reason',
         'lead': 'The whole change to the function\'s first line, in the MANHATTAN PLANNER section:',
         'code': '# Lesson 4-4\n'
                 'def compute_path(start, end):\n'
                 '\n'
                 '# Lesson 4-5\n'
                 'def compute_manhattan_path(position, destination):',
         'code_size': 24,
         'callout': 'Nothing is pasted in this lesson: it\'s an edit to a function you already have, '
                    'the same way Lesson 2-6 rewrote `get_error()`',
         'tone': 'teal'},

        {'kind': 'table', 'title': 'Three words changed, each on purpose',
         'headers': ['Word', 'Why'],
         'widths': [2.8, 8],
         'rows': [
             ['`manhattan`', 'Says **which** algorithm. In Module 5 you write a second planner, '
                             '`compute_bfs_path()`, and the two must not collide.'],
             ['`position`, not `start`', 'Where the robot is **right now**. After it drives to '
                                         '(2, 3), the next path is planned from (2, 3).'],
             ['`destination`, not `end`', '`end` is a vague word, and a worse one next to `start`. '
                                          'The path ends at the destination; so does the robot.'],
         ],
         'size': 22,
         'callout': 'A path isn\'t always planned from the robot\'s starting corner',
         'tone': 'teal',
         'notes': 'Right now it is the only planner, so "manhattan" feels redundant. A path is not '
                  'always planned from the robot\'s starting corner, which is why "start" is the '
                  'wrong word for the first parameter.'},

        {'kind': 'check',
         'question': 'Why does the function\'s name include \'manhattan\' when it is the only planner '
                     'in the course so far?',
         'options': ['Python requires function names to have three parts',
                     'Module 5 adds `compute_bfs_path()`, and both must exist in one program without colliding',
                     'Because it is faster to type',
                     'It is a convention for while loops'],
         'answer': 1,
         'explanation': 'A name that says which algorithm it is costs nothing now and saves a rename '
                        'later. compute_manhattan_path() and compute_bfs_path() will sit side by '
                        'side in Module 5.'},

        {'kind': 'code', 'title': 'What the function promises: a docstring',
         'lead': 'A function is a contract: give me these inputs, and I guarantee this output. Write '
                 'the guarantee in a **docstring**: a string in triple quotes, right under the `def` '
                 'line, that Python keeps attached to the function.',
         'lead_h': 1.25,
         'code': 'def compute_manhattan_path(position, destination):\n'
                 '    """Compute a Manhattan path from position to destination.\n'
                 '\n'
                 '    position:    an (x, y) tuple -- where the robot is now\n'
                 '    destination: an (x, y) tuple -- where it needs to go\n'
                 '\n'
                 '    Returns a list of (x, y) tuples the robot should move to,\n'
                 '    not including position itself.\n'
                 '    """\n'
                 '    path = []\n'
                 '    ...',
         'code_size': 18,
         'notes': 'Docstrings are new. Show that help(compute_manhattan_path) prints it, and that '
                  'the first line is a one-sentence summary by convention. Don\'t go further than '
                  'that. The last sentence is the one people get wrong: check it against the code. '
                  'The first thing appended to path is the position after the first step, never '
                  'position itself.'},

        {'kind': 'table', 'title': 'The three promises',
         'headers': ['The path...', 'Example'],
         'widths': [3.2, 7],
         'rows': [
             ['1. **never includes the start**',
              '`compute_manhattan_path((0, 0), (2, 0))` is `[(1, 0), (2, 0)]`'],
             ['2. **ends at the destination**', 'the last element is always `destination`'],
             ['3. is **empty** if you\'re already there',
              '`compute_manhattan_path((1, 1), (1, 1))` is `[]`: every loop is skipped'],
         ],
         'size': 20,
         'callout': 'Every planner in this course, Manhattan now, BFS and Dijkstra later, makes the '
                    'same three promises',
         'tone': 'teal',
         'notes': 'Promise 1: the path for (0, 0) to (2, 0) is not [(0, 0), (1, 0), (2, 0)]. Have '
                  'students write the promises in the docstring and say them out loud.'},

        {'kind': 'bullets', 'title': 'Why promise 1 matters',
         'bullets': [
             'The robot is going to **drive this list**',
             'Each element is an intersection to drive **to**',
             'The robot is already standing on `position`',
             'Telling it to drive there means driving **zero distance**, and getting confused about which way to turn',
         ],
         'callout': 'A path is a list of places to go, never the place you are',
         'tone': 'orange',
         'notes': 'This is the promise that bites later. In Lesson 4-8 the driving loop is '
                  'for next_pos in path, and a path that includes the start makes the first '
                  'desired_heading() call see a zero move and return None.'},

        {'kind': 'check',
         'question': 'What does `compute_manhattan_path((2, 1), (2, 1))` return, and why?',
         'options': ['`[(2, 1)]`: the destination is always included',
                     '`[]`: the robot is already there, so every while condition is false',
                     'An error, because position equals destination',
                     '`[(2, 1), (2, 1)]`'],
         'answer': 1,
         'explanation': 'Promise 3. With x == dest_x and y == dest_y, none of the four loops run, '
                        'and path stays empty. That is the right answer: there is nowhere to go.'},

        {'kind': 'check',
         'question': 'A classmate\'s version returns `[(0, 0), (1, 0), (2, 0)]` for position (0, 0), '
                     'destination (2, 0). Which promise did it break, and why does it matter?',
         'options': ['Promise 2: the path does not end at the destination',
                     'Promise 1: it includes the start, so the robot is told to drive where it already is',
                     'Promise 3: the path should be empty',
                     'No promise was broken; this is also correct'],
         'answer': 1,
         'explanation': 'The path is a list of places to drive TO. The robot is already at (0, 0); '
                        'listing it as a step gives the driving code a zero-length move and a turn '
                        'it cannot work out.'},

        {'kind': 'code', 'title': 'The planner is told, it doesn\'t remember',
         'lead': 'Look at how the same function is used three times in a row:',
         'code': 'path1 = compute_manhattan_path((0, 0), (2, 3))     # plan from the corner\n'
                 'path2 = compute_manhattan_path((2, 3), (0, 3))     # robot drove there; plan from there\n'
                 'path3 = compute_manhattan_path((0, 3), (0, 0))     # and again',
         'code_size': 18,
         'callout': 'Every call is handed the robot\'s position. The planner never stores it.',
         'tone': 'teal',
         'notes': 'The "told, not remembered" rule is Module 5\'s foundation, so give it the full ten '
                  'minutes.'},

        {'kind': 'figure', 'title': 'Three legs, three positions',
         'figure': '/img/lesson-m4-05/told-not-remembered-xy.svg',
         'caption': 'The first argument changes every time, because the robot has moved. The planner '
                    'never has to know that; it is told.'},

        {'kind': 'bullets', 'title': 'One owner for the robot\'s position',
         'bullets': [
             'Only **one piece of code** is in charge of knowing where the robot is: the **driving code**, in Lesson 4-8',
             'It updates its `position` variable after every intersection, and hands the current value to the planner',
             'If the planner also kept a copy, you\'d have **two variables that are supposed to agree**',
             'The first time one is updated and the other isn\'t, the robot plans from a place it isn\'t',
         ],
         'callout': 'A planner has no memory: tuples in, list out. That\'s also why you can test it '
                    'with no robot attached, next lesson.',
         'tone': 'teal',
         'notes': 'The bug it prevents is concrete: in the old class version of this lesson, the '
                  'planner stored self.position and the driving code stored its own, and every '
                  'student program needed a line to keep them in sync. Nobody misses that line. '
                  'The easiest way to never have the bug is to never have the second copy.'},

        {'kind': 'check',
         'question': 'Why does `compute_manhattan_path()` take position as a parameter every call, '
                     'instead of remembering where the robot started?',
         'options': ['Functions cannot store values between calls',
                     'So only the driving code tracks the robot; a copy in the planner would drift from it',
                     'Because the start is always (0, 0)',
                     'To make the function slower and more careful'],
         'answer': 1,
         'explanation': 'One owner for the robot\'s position. The driving code updates it after every '
                        'intersection; the planner is handed the current value and does arithmetic '
                        'with it. No second copy, no disagreement.'},

        {'kind': 'steps', 'title': 'Step 1 · The rename',
         'steps': [
             'In MANHATTAN PLANNER, change the `def` line and replace the one-line docstring with the full one',
             'Set the run line to `test_paper_paths()`, run it, and **read the error**: your Lesson 4-4 '
             'tests still call `compute_path()`, which no longer exists',
             'Update both tests and run them again: same output as yesterday',
         ],
         'callout': 'A rename changes every **call** as well as the definition. That\'s why names in '
                    'this file are chosen carefully and changed almost never.',
         'tone': 'orange'},

        {'kind': 'code', 'title': 'Step 2 · A test from everywhere',
         'tag': 'Activity',
         'lead': 'Write `test_from_everywhere()` with these four calls. Before you run it, trace each '
                 'answer by hand on the grid and write what you expect as a comment.',
         'lead_h': 1.2,
         'code': 'print(compute_manhattan_path((0, 0), (2, 3)))   # east, then north\n'
                 'print(compute_manhattan_path((0, 0), (3, 1)))\n'
                 'print(compute_manhattan_path((3, 3), (1, 0)))   # west, then south\n'
                 'print(compute_manhattan_path((2, 0), (2, 4)))   # same column: north only',
         'code_size': 18,
         'callout': 'Set the run line to it. Check each result against the promises, then add a '
                    '**fifth call** where position equals destination.',
         'tone': 'teal',
         'notes': 'The traced answers are behind a reveal on the lesson page. Reading their own '
                  'output against the three promises is the habit Lesson 4-6 builds on.'},

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
                        'fastest: the first element should never equal position.',
         'notes': 'Answer: B. The append-before-update bug is the one students actually make. '
                  'Promise 1 is broken, and the corner (1, 3) is missing.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Maps', 'Routing engines', '\nA map app\'s router is handed your location every time '
                                         'you ask. Swap in a bike router and the app does not change.'),
             ('Software', 'Pure functions', '\nInputs in, output out, nothing stored: the easiest '
                                            'code to test and the hardest to get subtly wrong.'),
             ('Teams', 'Interfaces', '\nWrite down what a function promises and two people can work '
                                     'on either side of it without talking every hour.'),
         ],
         'height': 4.0,
         'notes': 'A function with a written promise, no memory, and the same shape as its '
                  'alternatives is how big systems stay swappable.'},

        {'kind': 'wrapup',
         'questions': [
             'Why `compute_manhattan_path` and not `compute_path`?',
             'What are the three promises?',
             'Who knows where the robot is?',
         ],
         'next': 'testing the planner systematically, on screen',
         'notes': 'Answers: Module 5 adds compute_bfs_path, and the name says which. No start in the '
                  'path; ends at the destination; [] when already there. The driving code, and only '
                  'it: the planner is told. Exit ticket: "Your partner\'s planner stores the start '
                  'position inside it. Describe one bug that could cause." Next lesson adds a '
                  'run_test() helper, possible only because the planner is pure arithmetic.'},

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
                  'From here on, class-track students use their class: when Lesson 4-6 says '
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
                 '    def compute_path(self, position, destination):\n'
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
                  'test_from_everywhere() again: same five lists. The __init__ is empty because '
                  'Manhattan has nothing to set up; BFS in Module 5 uses its __init__ to hold the '
                  'list of blocked intersections, and that is when the class earns its keep. The '
                  'finished method is behind a reveal on the lesson page and is not shown here. '
                  'Solution file: lesson-05-manhattan-class-addon.py.'},
    ],
}
