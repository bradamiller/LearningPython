DECK = {
    'module': 4, 'lesson': 4,
    'doc': 'module-04-manhattan/lesson-04-the-manhattan-algorithm',
    'title': 'The Manhattan Algorithm',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Explain **Manhattan distance**, and why it is named after Manhattan, NYC',
             'Describe the "across first, then up or down" strategy and hand-trace a path on paper',
             'Write `compute_path(start, end)` in the MANHATTAN PLANNER section, with while loops that build a list',
             'Extend it from 2 loops (east/north) to 4 loops (all directions), with no `if/else`',
             'Test it on screen against your paper traces, edge cases included',
         ],
         'notes': '60 minutes. Coordinates (4-1), tuples (4-2) and lists (4-3) come together: '
                  'a function that computes a whole path from a start and a destination. Paper '
                  'first for 8 to 10 minutes, then the bulk of the lesson is writing and testing '
                  'compute_path().'},

        {'kind': 'bullets', 'title': 'Coordinates, tuples, lists: together',
         'bullets': [
             'Today you write the function that **computes a whole path** automatically',
             'Give it a start and a destination; it hands back the **list of intersections** to drive',
             'Trace it on paper first, then build it in **two stages**',
             'It goes in a new section of `robot.py`, the first one that **never touches the robot**',
         ],
         'callout': 'Tuples in, a list out. The robot can stay on the desk all lesson.',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Why "Manhattan"?',
         'bullets': [
             'Picture the streets of Manhattan in New York',
             'You can\'t cut diagonally through the buildings: you walk along the **streets and avenues**',
             'The distance is the blocks across **plus** the blocks up or down',
             'Taxi drivers know it too: it is also called **taxicab distance**',
             'Our robot is in the same spot: it drives along grid lines, never diagonally',
         ],
         'callout': 'Manhattan distance = steps across + steps up or down, the idea you computed '
                    'by hand in Lesson 4-1',
         'tone': 'teal',
         'notes': 'If you can, show an actual map of Manhattan for the hook: the name sticks when '
                  'it is tied to real streets.'},

        {'kind': 'bullets', 'title': 'The strategy: across first, then up or down',
         'bullets': [
             'The simplest strategy that always works:',
             ['Move **across** until x is right', 'Then move **up or down** until y is right'],
             'That always traces an **L-shaped** path',
             'Or a straight line, if x or y is already correct',
         ],
         'size': 26,
         'split': 0.5,
         'figure': '/img/lesson-m4-04/four-loops-xy.svg',
         'crop': (0.49, 0.03, 0.83, 0.82),
         'notes': 'The figure is the right half of the lesson\'s four-loops figure: the trip from '
                  '(1, 3) to (3, 0), across two, then down three. The whole figure comes back in '
                  'Step 2.'},

        {'kind': 'check',
         'question': 'Why can\'t the robot use a straight diagonal to shorten the trip?',
         'options': ['Diagonals are slower than straight lines',
                     'The robot follows grid lines, so it can only move along rows and columns',
                     'The grid is too small',
                     'It can: the Manhattan algorithm just chooses not to'],
         'answer': 1,
         'explanation': 'Like walking Manhattan\'s streets, the robot can\'t cut through the middle '
                        'of a block, only along the lines. That is why the distance is steps '
                        'across + steps up or down.'},

        {'kind': 'table', 'title': 'Activity · Trace it on paper first',
         'tag': 'Activity',
         'lead': 'Take **(0, 0) → (2, 3)**: right first, then up. The robot is **already** at the '
                 'start, so the path lists only the spots it moves **to**. Fill in a row per move.',
         'lead_h': 1.2,
         'headers': ['Step', 'Action', 'New position', 'Path so far'],
         'widths': [1, 1.6, 2.2, 5],
         'rows': [
             ['1', 'x +1', '(1, 0)', '`[(1,0)]`'],
             ['2', '', '', ''],
             ['3', '', '', ''],
             ['4', '', '', ''],
             ['5', '', '', ''],
         ],
         'notes': 'Hand out a big grid and markers: one color for moves across, another for moves '
                  'up and down. Keep it short and targeted; the goal is intuition, not mastery. '
                  'Then ask how many steps it took, and check that against the Manhattan distance, '
                  '|2−0| + |3−0|. The finished table is behind a reveal on the lesson page.'},

        {'kind': 'bullets', 'title': 'Now try the same spot',
         'bullets': [
             'Trace **(1, 1) → (1, 1)**',
             'No moves across, no moves up or down',
             'The path is `[]`: an **empty list**, zero steps',
         ],
         'callout': 'That\'s not a bug: the robot is already there',
         'tone': 'green'},

        {'kind': 'check',
         'question': 'Hand-tracing (2,0) → (2,3), what path do you get?',
         'options': ['`[(2,0), (2,1), (2,2), (2,3)]`', '`[(2,1), (2,2), (2,3)]`',
                     '`[(2,3)]`', '`[]`'],
         'answer': 1,
         'explanation': 'Same x, so no moves across, only three moves up. The start (2,0) is not '
                        'included, so the path is [(2,1), (2,2), (2,3)]: three steps.'},

        {'kind': 'code', 'title': 'Add to robot.py: MANHATTAN PLANNER',
         'code': '# ===== MANHATTAN PLANNER =====\n'
                 '# Plans a route across the grid: given where the robot is and\n'
                 '# where it should go, returns the list of (x, y) tuples to\n'
                 '# drive to, across first and then up or down. Pure arithmetic --\n'
                 '# nothing in here touches a sensor or a motor, so every test\n'
                 '# in this section runs on screen with the robot sitting still.\n'
                 '\n'
                 'def compute_path(start, end):\n'
                 '    """Return the (x, y) steps from start to end, across\n'
                 '    first, then up or down. The start itself is not in the list."""\n'
                 '    # 1. path = [] ; unpack start and end into x and y numbers\n'
                 '    # 2. east loop: while x is short of the end x,\n'
                 '    #    step x by one and append the new position\n'
                 '    # 3. north loop: the same for y\n'
                 '    # 4. return path\n'
                 '    pass',
         'code_size': 16,
         'notes': 'Paste it into robot.py above RUN, after the GRID DRIVING section. It is the first '
                  'section in the file with no driving in it at all: a function that takes two tuples '
                  'and returns a list.'},

        {'kind': 'bullets', 'title': 'Two things are new about this skeleton',
         'bullets': [
             'The **outline is shorter** than Module 2\'s',
             ['You just traced the algorithm by hand, so the comments name the pieces instead of '
              'spelling them out'],
             'There is **no test function** in it',
             ['From this module on, the lesson says what a test should show, and you write it, name and all'],
             'These are **paper tests**: they print a path, you compare it with your trace, nothing moves',
         ],
         'notes': 'The hint level drops again here. The outline names the pieces (unpack, two loops, '
                  'return) because the trace table just did the algorithm by hand. Expect two or three '
                  'print lines per test; the habit is what matters, because every planner test from '
                  'here to Module 6 is written this way. Students who want the Module 2 scaffolding '
                  'back can be pointed at their own trace table: it is the outline.'},

        {'kind': 'code', 'title': 'Step 1 · East and north only',
         'tag': 'Activity',
         'lead': 'Start with just the two "positive" directions, right and up: steps 1 to 4 of the '
                 'outline. Step 1 uses **tuple unpacking** from Lesson 4-2: one line pulls both '
                 'numbers out of a tuple into two variables.',
         'lead_h': 1.3,
         'code': 'x, y = start     # start is (0, 0): x is 0, y is 0',
         'code_size': 26,
         'callout': 'Do the same for `end`, and the loops compare plain numbers',
         'tone': 'teal',
         'notes': 'Build it in two stages: get the easy half working and run it before you '
                  'generalize. A half-finished algorithm you have tested beats a whole one you '
                  'haven\'t. Check that tuple unpacking from 4-2 stuck.'},

        {'kind': 'bullets', 'title': 'Step 1 · The two loops',
         'tag': 'Activity',
         'bullets': [
             'Each loop is the **build-in-a-loop** pattern from Lesson 4-3, with a `while` instead of a `for`',
             'As long as x is still **short of** the destination x, step it by one and append the new `(x, y)`',
             'The north loop does the same for y',
         ],
         'callout': 'The double parentheses in `append((...))`: the outer pair is the function call, '
                    'the inner pair is the tuple',
         'tone': 'orange',
         'notes': 'Take real time on the double parentheses in append((x, y)): the outer pair is the '
                  'function call, the inner pair is the tuple.'},

        {'kind': 'steps', 'title': 'Step 1 · Test it against your trace',
         'steps': [
             'Write a test, say `test_paper_paths()`, that prints `compute_path((0, 0), (2, 3))` '
             'and `compute_path((1, 1), (3, 4))`',
             'Set the run line to it and run it',
             'Compare with your paper traces: both should give exactly the hand-traced lists, **5 steps each**',
         ],
         'callout': 'Don\'t go on until they match',
         'tone': 'orange'},

        {'kind': 'bullets', 'title': 'Now find the limit',
         'bullets': [
             'Add `compute_path((3, 3), (1, 0))` to the test and run it again',
             'An **empty list!**',
             '`3 < 1` is False and `3 < 0` is False, so **neither** loop runs',
             'Going left or down, this version does nothing',
         ],
         'callout': 'We need west and south too',
         'tone': 'orange'},

        {'kind': 'check',
         'question': 'Why does the stage-1 function return `[]` for (3,3) → (1,0)?',
         'options': ['`append()` is broken',
                     'Both while conditions start False (3 is not < 1, 3 is not < 0), so neither loop runs',
                     'The start and end are the same',
                     'It runs forever'],
         'answer': 1,
         'explanation': 'Stage 1 only handles increasing x and y. Moving left or down needs the two '
                        'decreasing loops we add next.'},

        {'kind': 'bullets', 'title': 'Step 2 · All four directions',
         'tag': 'Activity',
         'bullets': [
             'The fix: **add two more while loops**, west (x decreases) and south (y decreases)',
             'Each is the **mirror** of the loop it sits next to: the comparison flips and the step goes the other way',
             'No `if/else` needed: for any trip, at most **one x loop and one y loop** run',
             'Keep the two x loops together, **before** the two y loops, so the path always goes across first',
         ],
         'notes': 'This is the lesson\'s big idea: a while loop whose condition starts False simply '
                  'does nothing. Students who have seen conditionals will try to wrap this in '
                  'if x < dest_x ... elif x > dest_x. Steer them back: the four loops are simpler and '
                  'handle every case, including the same position (all four skipped, so []).'},

        {'kind': 'figure', 'title': 'Four loops, one per direction',
         'figure': '/img/lesson-m4-04/four-loops-xy.svg',
         'caption': 'Every trip runs at most one x loop and one y loop. The other two find their '
                    'condition False on the first check and never run.',
         'notes': 'Walk the right half: (1, 3) to (3, 0). East runs twice, west and north are '
                  'skipped, south runs three times. Five steps, matching |3−1| + |0−3|.'},

        {'kind': 'steps', 'title': 'Step 2 · Trace it, then run it',
         'steps': [
             'Trace **(3, 3) → (1, 0)** on paper',
             'Say which of the four loops run: the robot has to go **left** and **down**, so two of them stay idle',
             'Run `test_paper_paths()` again and compare with your trace',
         ],
         'notes': 'The finished trace is behind a reveal on the lesson page. The page also has an '
                  'animation of the four loops running three trips, in a reveal for students whose '
                  'tests already match; it is not on these slides because it shows the traced '
                  'answers.'},

        {'kind': 'check',
         'question': 'For a trip that goes up and to the right, how many of the four while loops '
                     'actually run?',
         'options': ['All four', 'Two: the north loop and the east loop', 'Just one',
                     'None: it needs if/else'],
         'answer': 1,
         'explanation': 'At most one x loop (east OR west) and one y loop (north OR south) run for any '
                        'trip. Up-and-right means north + east; the other two are skipped.'},

        {'kind': 'steps', 'title': 'Activity · The edge cases',
         'lead': 'Good algorithms handle the awkward inputs without special code. Write a second '
                 'test, `test_edge_cases()`, with three calls:',
         'lead_h': 1.0,
         'steps': [
             '**Same column**: `(2, 0)` to `(2, 3)`',
             '**Same row**: `(0, 2)` to `(3, 2)`',
             '**Same spot**: `(1, 1)` to `(1, 1)`',
         ],
         'callout': 'Trace all three on paper and write your prediction as a comment next to each '
                    'call **before** you set the run line to it',
         'tone': 'teal',
         'notes': 'The predicted outputs, and a finished compute_path(), are in reveals on the lesson '
                  'page. Nothing special is written for these cases: the loops just don\'t run when '
                  'there is no distance to cover.'},

        {'kind': 'check',
         'question': 'What does `compute_path((2, 2), (2, 2))` return, and why?',
         'options': ['`[(2, 2)]`: the current position',
                     '`[]`: all four loop conditions are False, so nothing is appended',
                     'An error', '`0`'],
         'answer': 1,
         'explanation': 'Start equals destination, so every while condition is False from the start. '
                        'No loop runs, the path stays empty, and len(path) is 0: the robot is '
                        'already there.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Games', 'Grid movement', '\nTurn-based and tile games measure moves in Manhattan '
                                        'steps: no diagonal shortcuts.'),
             ('AI', 'Pathfinding heuristics', '\nManhattan distance is a classic "how far, roughly?" '
                                              'estimate that guides search algorithms like A*.'),
             ('Data', 'Clustering', '\nSome machine-learning methods group points by Manhattan '
                                    '(taxicab) distance instead of straight-line distance.'),
         ],
         'height': 4.0,
         'notes': '"Move one axis, then the other" and Manhattan distance show up all over computing.'},

        {'kind': 'wrapup',
         'questions': [
             'What does "across first, then up or down" produce?',
             'Why four while loops instead of `if/else`?',
             'Why isn\'t the starting position in the path?',
         ],
         'next': 'the same function gets its real name, and a written promise',
         'notes': 'Answers: an L-shaped path, predictable and always valid. Only the relevant loops '
                  'run; a False condition just skips. The robot is already there, so len(path) is the '
                  'number of steps. Exit ticket: "What does compute_path((0,0),(2,3)) return, and how '
                  'many steps is that?" ([(1,0),(2,0),(2,1),(2,2),(2,3)], 5). Next lesson the '
                  'function becomes compute_manhattan_path(position, destination), with a docstring; '
                  'the algorithm does not change at all.'},
    ],
}
