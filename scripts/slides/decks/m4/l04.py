DECK = {
    'module': 4, 'lesson': 4,
    'doc': 'module-04-manhattan/lesson-04-the-manhattan-algorithm',
    'title': 'The Manhattan Algorithm',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Explain **Manhattan distance**, and why it is named after Manhattan, NYC',
             'Describe the "across first, then up or down" strategy and hand-trace a path on paper',
             'Read each row of your trace table as one trip around a loop, and match the given east loop to it',
             'Write north by copying east, then west and south by copying and flipping: four loops, no `if/else`',
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
             'Trace it on paper first, then build it **one loop at a time**',
             'It goes in a new section of `robot.py`, the first one that **never touches the robot**',
         ],
         'callout': 'Tuples in, a list out. The robot can stay on the desk all lesson.',
         'tone': 'teal'},

        {'kind': 'figure', 'title': 'What goes in, what comes back',
         'figure': './decks/m4/fig/destinations-hops.svg',
         'caption': 'Handed one destination, possibly many intersections away. Hands back a list of '
                    'adjacent intersections, one hop each, ending at the destination.',
         'notes': 'The main program supplies the destinations list from Lesson 4-0. The function you '
                  'write today handles one destination at a time: the main loop calls it once per '
                  'destination. Every entry in the list it returns is one block from the entry before '
                  'it, and the first is one block from the start.'},

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
         'row_h': 0.5,
         'callout_size': 18,
         'callout': 'Printable worksheet: [learningpython.bradhouse.com/printables/lesson-4-4-trace-worksheet.pdf]'
                    '(https://learningpython.bradhouse.com/printables/lesson-4-4-trace-worksheet.pdf)',
         'tone': 'teal',
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

        {'kind': 'table', 'title': 'From the trace table to a loop',
         'lead': '**Each row of your trace is one trip around a loop.** In plain words, the east '
                 'loop says: keep stepping right until your x matches the end x.',
         'lead_h': 1.2,
         'headers': ['In your trace table', 'In the code'],
         'widths': [1, 1.3],
         'rows': [
             ['Action: x +1', '`x = x + 1`'],
             ['New position', '`next_spot = (x, y)`'],
             ['Path so far', '`path.append(next_spot)`'],
         ],
         'callout': '"Until x matches" is `while x < dest_x`: as long as x is short, take another step',
         'tone': 'teal',
         'notes': 'Rows 1 and 2 of the trace both say x +1: that is one loop going around twice, '
                  'stepping east. Rows 3 to 5 are a second loop going around three times, stepping '
                  'north. dest_x and dest_y come from unpacking the end tuple, as in Lesson 4-2. When '
                  'x reaches dest_x the condition is False and the loop stops, just as students '
                  'stopped writing x +1 rows once they reached x = 2.'},

        {'kind': 'code', 'title': 'Add to robot.py: MANHATTAN PLANNER',
         'code': '# ===== MANHATTAN PLANNER =====\n'
                 '\n'
                 'def compute_path(start, end):\n'
                 '    """Return the (x, y) steps from start to end, across\n'
                 '    first, then up or down. The start itself is not in the list."""\n'
                 '    path = []\n'
                 '    x, y = start              # where the robot is now\n'
                 '    dest_x, dest_y = end      # where it is going\n'
                 '\n'
                 '    # East: keep stepping right until x matches dest_x\n'
                 '    while x < dest_x:\n'
                 '        x = x + 1             # one step right\n'
                 '        next_spot = (x, y)    # the spot it just stepped to\n'
                 '        path.append(next_spot)\n'
                 '\n'
                 '    # West: copy east, flip < to > and + to -\n'
                 '    # North: copy east, but step y until it matches dest_y\n'
                 '    # South: copy north, flip < to > and + to -\n'
                 '\n'
                 '    return path',
         'code_size': 14,
         'notes': 'Paste it into robot.py above RUN, after the GRID DRIVING section. The lesson page '
                  'has the whole block, with the section comment, blank lines between the three '
                  'comments for the loops to come, and the two tests: copy it from '
                  'there. The east loop is given finished; the other three loops are the students\' '
                  'work, and each one is a copy of the east loop with a small change.'},

        {'kind': 'code', 'title': 'The two tests come with it',
         'code': 'def test_paper_paths():\n'
                 '    print(compute_path((0, 0), (2, 3)))   # your trace table\n'
                 '    print(compute_path((0, 1), (3, 3)))\n'
                 '    print(compute_path((3, 3), (1, 0)))   # left and down\n'
                 '\n'
                 'def test_edge_cases():\n'
                 '    print(compute_path((2, 0), (2, 3)))   # same column\n'
                 '    print(compute_path((0, 2), (3, 2)))   # same row\n'
                 '    print(compute_path((1, 1), (1, 1)))   # same spot',
         'code_size': 18,
         'callout': 'Paper tests: they print a path, you compare it with your trace, nothing moves',
         'tone': 'teal',
         'notes': 'More hints than usual, on purpose: this is the first while loop that builds a '
                  'list and the first section with no robot in it. The step down to writing tests '
                  'themselves comes in Lesson 4-5, once the algorithm is theirs. Students who stall '
                  'on a loop can be pointed at their own trace table: each row is one trip around a '
                  'loop.'},

        {'kind': 'bullets', 'title': 'Decomposition: one part at a time',
         'bullets': [
             'Step 3 of the method from Lesson 4-0: **build and test each part on its own**',
             'The planner is the first part; this lesson and the next two build and test it alone',
             'What it takes in and hands back is already decided: **two tuples in, a list of '
             'intersections out**',
             'Nothing else in the file has to work for it to work',
         ]},

        {'kind': 'steps', 'title': 'Step 1 · Run the east loop',
         'tag': 'Activity',
         'steps': [
             'Set the run line to `test_paper_paths()` and run it **before you write anything**',
             'The first line prints `[(1, 0), (2, 0)]`: rows 1 and 2 of your trace',
             'Then it stops short: nothing moves it up yet',
         ],
         'callout': 'Build it one loop at a time, and run it after each one',
         'tone': 'orange',
         'notes': 'A half-finished algorithm you have tested beats a whole one you haven\'t. Check '
                  'that tuple unpacking from 4-2 (x, y = start) stuck.'},

        {'kind': 'code', 'title': 'Step 1 · Write north by copying east',
         'tag': 'Activity',
         'lead': 'Under the north comment, copy the east loop: compare `y` with `dest_y` and step '
                 '`y` instead of `x`. Leave `next_spot = (x, y)` as it is. Run it again:',
         'lead_h': 1.3,
         'code': '[(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]\n'
                 '[(1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]\n'
                 '[]',
         'code_size': 22,
         'callout': 'The first line is your trace table. Don\'t go on until both match',
         'tone': 'orange',
         'notes': 'next_spot = (x, y) always records the whole position, so it does not change when '
                  'the loop is copied. The tuple is built on its own line and appended on the next, '
                  'so there are no double parentheses to untangle. The north loop is in a reveal on '
                  'the lesson page.'},

        {'kind': 'bullets', 'title': 'Now find the limit',
         'bullets': [
             'Look at the third line: `(3, 3)` to `(1, 0)` gives an **empty list!**',
             '`3 < 1` is False and `3 < 0` is False, so **neither** loop runs',
             'Going left or down, this version does nothing',
         ],
         'callout': 'That is what the west and south comments are for',
         'tone': 'orange'},

        {'kind': 'check',
         'question': 'Why does the Step 1 version (east and north only) return `[]` for (3,3) → (1,0)?',
         'options': ['`append()` is broken',
                     'Both while conditions start False (3 is not < 1, 3 is not < 0), so neither loop runs',
                     'The start and end are the same',
                     'It runs forever'],
         'answer': 1,
         'explanation': 'East and north only handle increasing x and y. Moving left or down needs the '
                        'two flipped loops you add next.'},

        {'kind': 'bullets', 'title': 'Step 2 · West and south: copy and flip',
         'tag': 'Activity',
         'bullets': [
             'The fix: **two more while loops**, and you already have both, backwards',
             '**West** is the east loop flipped: `<` becomes `>`, `+ 1` becomes `- 1`',
             '**South** is the north loop, flipped the same way',
             'No `if/else` needed: for any trip, at most **one x loop and one y loop** run',
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
         'lead': 'Good algorithms handle the awkward inputs without special code. The second test '
                 'in your skeleton, `test_edge_cases()`, has three:',
         'lead_h': 1.0,
         'steps': [
             '**Same column**: `(2, 0)` to `(2, 3)`',
             '**Same row**: `(0, 2)` to `(3, 2)`',
             '**Same spot**: `(1, 1)` to `(1, 1)`',
         ],
         'callout': 'Trace all three on paper and add your prediction to the comment on each call '
                    '**before** you set the run line to it',
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
