DECK = {
    'module': 4, 'lesson': 4,
    'doc': 'module-04-manhattan/lesson-04-the-manhattan-algorithm',
    'title': 'The Manhattan Algorithm',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Use **Manhattan distance**, steps across plus steps up or down, to check a path\'s length',
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

        {'kind': 'figure', 'title': 'One step: x or y, never both',
         'figure': '/img/lesson-m4-04/one-step.svg',
         'caption': 'One step changes x or y by 1, never both. Both would be a diagonal, and the '
                    'robot can\'t drive one.',
         'notes': 'Make this solid before the trace: every row of the trace table changes '
                  'exactly one coordinate by 1. Ask for the four neighbors of (2, 2), then ask '
                  'why (3, 3) is not one of them.'},

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
                  'Step 3.'},

        {'kind': 'table', 'title': 'Activity · Trace it on paper',
         'tag': 'Activity',
         'lead': '**Path 1, move by move:** trace (0, 0) → (2, 3), one row per move. The start is '
                 'never in the path.',
         'lead_h': 1.0,
         'headers': ['Step', 'Action', 'New position'],
         'widths': [1, 1.6, 2.2],
         'rows': [
             ['1', 'x + 1', '(1, 0)'],
             ['2', '', ''],
             ['3', '', ''],
             ['4', '', ''],
             ['5', '', ''],
         ],
         'row_h': 0.5,
         'callout_size': 18,
         'callout': 'Printable worksheet: [learningpython.bradhouse.com/printables/lesson-4-4-trace-worksheet.pdf]'
                    '(https://learningpython.bradhouse.com/printables/lesson-4-4-trace-worksheet.pdf)',
         'tone': 'teal',
         'notes': 'One paper activity, about 15 minutes: this table, then all six paths, then the '
                  'path 3 question. Big grid and markers: one color for moves across, another for '
                  'moves up and down. The sheet becomes their answer key for the coding steps. '
                  'Check the sheets before students go on: a wrong key sends them hunting for a bug '
                  'that is not there. The filled-in key is behind a reveal on the lesson page.'},

        {'kind': 'table', 'title': 'Activity · All six paths',
         'tag': 'Activity',
         'lead': 'Write each expected path and its steps. Path 1 is the one you just traced. '
                 'Steps should equal the Manhattan distance.',
         'lead_h': 1.2,
         'headers': ['#', 'From → to', 'Expected path', 'Steps'],
         'widths': [0.5, 2.6, 6, 1],
         'rows': [
             ['1', '(0, 0) → (2, 3)', '', ''],
             ['2', '(0, 1) → (3, 3)', '', ''],
             ['3', '(3, 3) → (1, 0)', '', ''],
             ['4', '(2, 0) → (2, 3)', '', ''],
             ['5', '(0, 2) → (3, 2)', '', ''],
             ['6', '(1, 1) → (1, 1)', '', ''],
         ],
         'row_h': 0.42,
         'callout': 'Then: what is different about **path 3** compared with paths 1 and 2?',
         'tone': 'teal',
         'notes': 'Paths 1 to 3 are test_paper_paths(), paths 4 to 6 are test_edge_cases(). '
                  'Answer to the question: paths 1 and 2 go right and up, so x and y get bigger; '
                  'path 3 goes left and down, so they get smaller. It sets up Step 2: the first '
                  'version only handles x and y getting bigger, so path 3 comes back empty. Path 6 '
                  'is [] because the robot is already there.'},

        {'kind': 'bullets', 'title': 'From the trace table to a loop',
         'bullets': [
             'Write the code the way you worked out each new position',
             '`x` and `y` are the robot\'s **current position**: `x, y = start`',
             '`dest_x` and `dest_y` are the destination: `dest_x, dest_y = end`',
             'Loop 1: keep adding 1 to x while x is less than `dest_x`',
             'Loop 2: do the same for y',
             'Inside each loop, **append** the new current position `(x, y)` to the path',
         ],
         'size': 26},

        {'kind': 'figure', 'title': 'Each row is one trip around a loop',
         'figure': '/img/lesson-m4-04/trace-to-loops.svg',
         'caption': 'Going left or down, the same loops subtract 1 instead: that\'s Step 3.',
         'notes': 'x and y are the robot\'s current position; they change by 1 each trip. When x '
                  'reaches dest_x the condition is False and the loop stops, just as students '
                  'stopped writing x + 1 rows once they reached x = 2. The inner parentheses in '
                  'path.append((x, y)) make the tuple; the outer pair is the call to append().'},

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
                 '        path.append((x, y))   # record the new spot\n'
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
         'callout': 'Paper tests: they print a path, you compare it with your answer key, nothing moves',
         'tone': 'teal',
         'notes': 'More hints than usual, on purpose: this is the first while loop that builds a '
                  'list and the first section with no robot in it. The step down to writing tests '
                  'themselves comes in Lesson 4-5, once the algorithm is theirs. Students who stall '
                  'on a loop can be pointed at their own trace table: each row is one trip around a '
                  'loop.'},

        {'kind': 'bullets', 'title': 'Plan first: the planner on its own',
         'bullets': [
             'Lesson 4-0 split the problem into **planning** and **driving**',
             'The planner is the first part; this lesson and the next two build and test it alone',
             'What it takes in and hands back is already decided: **two tuples in, a list of '
             'intersections out**',
             'Nothing else in the file has to work for it to work',
         ]},

        {'kind': 'steps', 'title': 'Step 1 · Paste in the skeleton',
         'tag': 'Activity',
         'steps': [
             'Copy the MANHATTAN PLANNER skeleton shown earlier: the function and both tests',
             'Paste it into `robot.py` in the editor, **above `RUN`**, after the GRID DRIVING section',
             'Save the file',
         ],
         'notes': 'The skeleton is on the "Add to robot.py: MANHATTAN PLANNER" and "The two tests '
                  'come with it" slides, and on the lesson page under This lesson\'s skeleton.'},

        {'kind': 'steps', 'title': 'Step 2 · Run the east loop',
         'tag': 'Activity',
         'steps': [
             'Set the run line to `test_paper_paths()` and run it **before you write anything**',
             'The first line prints `[(1, 0), (2, 0)]`: the first two spots of path 1 in your answer key',
             'Then it stops short: nothing moves it up yet',
         ],
         'callout': 'Build it one loop at a time, and run it after each one',
         'tone': 'orange',
         'notes': 'A half-finished algorithm you have tested beats a whole one you haven\'t. Check '
                  'that tuple unpacking from 4-2 (x, y = start) stuck.'},

        {'kind': 'bullets', 'title': 'Step 2 · Write north by copying east',
         'tag': 'Activity',
         'bullets': [
             'Under the north comment, **copy the east loop**',
             'Compare `y` with `dest_y`, and step `y` instead of `x`',
             'Leave `path.append((x, y))` as it is: it always records the whole position',
             'Run it again and check the first two lines against **paths 1 and 2** of your answer key',
         ],
         'callout': 'Don\'t go on until both match',
         'tone': 'orange',
         'notes': 'The north loop is in a reveal on the lesson page. Students with a wrong line '
                  'should check their key first, then their code: one of the two is wrong.'},

        {'kind': 'bullets', 'title': 'Now find the limit',
         'bullets': [
             'Look at the third line: `(3, 3)` to `(1, 0)` gives an **empty list!**',
             'Your answer key says path 3 has five steps: it goes left and down',
             '`3 < 1` is False and `3 < 0` is False, so **neither** loop runs',
             'Going left or down, this version does nothing',
         ],
         'callout': 'That is what the west and south comments are for',
         'tone': 'orange'},

        {'kind': 'check',
         'question': 'Why does the Step 2 version (east and north only) return `[]` for (3,3) → (1,0)?',
         'options': ['`append()` is broken',
                     'Both while conditions start False (3 is not < 1, 3 is not < 0), so neither loop runs',
                     'The start and end are the same',
                     'It runs forever'],
         'answer': 1,
         'explanation': 'East and north only handle increasing x and y. Moving left or down needs the '
                        'two flipped loops you add next.'},

        {'kind': 'bullets', 'title': 'Step 3 · West and south: copy and flip',
         'tag': 'Activity',
         'bullets': [
             'The fix: **two more while loops**, and you already have both, backwards',
             '**West** is the east loop flipped: `<` becomes `>`, `+ 1` becomes `- 1`',
             '**South** is the north loop, flipped the same way',
         ],
         'notes': 'This is the lesson\'s big idea: a while loop whose condition starts False simply '
                  'does nothing. Students who have seen conditionals will try to wrap this in '
                  'if x < dest_x ... elif x > dest_x. Steer them back: the four loops are simpler and '
                  'handle every case, including the same position (all four skipped, so []).'},

        {'kind': 'figure', 'title': 'Only one x loop runs',
         'figure': '/img/lesson-m4-04/one-x-loop-runs.svg',
         'caption': 'A while loop checks its condition first. Going left, east\'s first check is '
                    'False, so it never runs. Same for the two y loops: no `if/else` needed.',
         'notes': 'Ask: going right, which x loop never runs? (West: x > dest_x is False from the '
                  'start.) Then: going up, which y loop never runs? (South.)'},

        {'kind': 'figure', 'title': 'Four loops, one per direction',
         'figure': '/img/lesson-m4-04/four-loops-xy.svg',
         'caption': 'Every trip runs at most one x loop and one y loop. The other two find their '
                    'condition False on the first check and never run.',
         'notes': 'Walk the right half: (1, 3) to (3, 0). East runs twice, west and north are '
                  'skipped, south runs three times. Five steps, matching |3−1| + |0−3|.'},

        {'kind': 'steps', 'title': 'Step 3 · Check it against your key',
         'steps': [
             'Look at path 3 in your answer key, **(3, 3) → (1, 0)**',
             'Say which of the four loops run: the robot has to go **left** and **down**, so two of them stay idle',
             'Run `test_paper_paths()` again: all three lines should match your key',
         ],
         'notes': 'Which loops run is behind a reveal on the lesson page. The page also has an '
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
         'callout': 'They are paths 4 to 6 in your answer key. Set the run line to `test_edge_cases()` '
                    'and check all three lines against it',
         'tone': 'teal',
         'notes': 'A finished compute_path() is in a reveal on the lesson page. Nothing special is written for these cases: the loops just don\'t run when '
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
