"""Module 4, Lesson 4-2 · The Planner: A Path That Grows."""

DECK = {
    'module': 4, 'lesson': 2,
    'doc': 'module-04-manhattan/lesson-02-a-path-that-grows',
    'title': 'The Planner: A Path That Grows',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Build a path by hand with `append()`, across first, then up',
             'Start with an empty list, add to it with `append()`, and count it with `len()`',
             'Unpack a tuple into `x` and `y`, and make a new tuple from them',
             'Build a path inside a `while` loop, one step per trip around',
             'Explain what happens when two names refer to the same list',
         ],
         'notes': '50 to 60 minutes, robot on the desk. The planner stub hands back one jump; '
                  'today it starts to build real paths, for any trip that goes right and up. Left '
                  'and down are Lesson 4-3. "Empty list, append inside a loop" is the pattern the '
                  'rest of the course builds paths with. Scope: [], append(), len(), unpacking. '
                  'No indexing yet (4-4), and no insert, pop or slicing at all.'},

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
                  'or down until y is right. Each step below prints something: students predict '
                  'before every run, then compare.'},

        # --- Step 1 ---
        {'kind': 'code', 'title': 'Step 1 · A list can grow',
         'tag': 'Activity',
         'lead': 'The planner doesn\'t know the path until it works it out. So it starts **empty** '
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

        {'kind': 'steps', 'title': 'Step 1 · Leg 1, by hand',
         'tag': 'Activity',
         'lead': 'Leg 1: (0, 0) to (2, 3), right twice, then up three times. The start is **not** '
                 'in the path. In `compute_manhattan_path()`, keep the `print` line. Replace '
                 '`return [destination]` with:',
         'steps': [
             '`path = []`',
             'Five `append()` lines, one per move, each followed by `print(path)`. The first is '
             '`path.append((1, 0))`',
             '`return path`. Then run `test_delivery()`',
         ],
         'callout': '**Predict:** the five lists Leg 1 prints, and Leg 2\'s path',
         'tone': 'orange',
         'notes': 'Answer: the list grows by one tuple per append, on the end. Leg 2 gets the same '
                  'five steps, starting with a jump from (2, 3) to (1, 0), and so does every leg: '
                  'the function never looks at start or destination. Deliberately clumsy; keep it '
                  'to ten minutes.'},

        {'kind': 'code', 'title': 'Step 1 · Check: Leg 1',
         'tag': 'Activity',
         'code': 'computing path from: (0, 0) to: (2, 3)\n'
                 '[(1, 0)]\n'
                 '[(1, 0), (2, 0)]\n'
                 '[(1, 0), (2, 0), (2, 1)]\n'
                 '[(1, 0), (2, 0), (2, 1), (2, 2)]\n'
                 '[(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]',
         'code_size': 20,
         'callout': 'Leg 1 is right. But Leg 2 gets **the same five steps**: the function hands back '
                    'what you typed.',
         'tone': 'green'},

        {'kind': 'bullets', 'title': 'Step 1 · Could you just type more?',
         'tag': 'Activity',
         'bullets': [
             'How many `append()` lines would Leg 2 need?',
             'All five legs?',
             'Corner to corner on a 10 x 10 grid?',
         ],
         'callout': 'A planner has to **work the path out** from where the robot is and where it\'s going',
         'tone': 'orange', 'size': 26,
         'notes': 'Leg 2 needs 4; all five legs need 18 between them, but one function has only one '
                  'set of lines, so typed lines are right for one trip at most. Corner to corner on '
                  'a 10 x 10 grid is 18 by itself.'},

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

        # --- Step 2 ---
        {'kind': 'figure', 'title': 'Step 2 · A loop appends',
         'tag': 'Activity',
         'figure': '/img/lesson-m4-03/appends-to-loops.svg',
         'caption': 'Each append is one trip around a loop.'},

        {'kind': 'code', 'title': 'Step 2 · Take the tuples apart',
         'tag': 'Activity',
         'lead': 'To add 1 to x, the function needs x on its own. **Unpacking** (Lesson 4-1):',
         'code': 'x, y = start              # where the plan is now\n'
                 'dest_x, dest_y = destination   # where it is going',
         'code_size': 22,
         'callout': 'After each move, `(x, y)` puts them back together as a **new tuple** for the '
                    'path',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Step 2 · The new planner',
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
         'code_size': 18,
         'notes': 'The slide leaves out the docstring to fit; students paste the whole block from '
                  'the lesson page.'},

        {'kind': 'code', 'title': 'Step 2 · Paper test, then run',
         'tag': 'Activity',
         'lead': 'Add this under it. On paper, write the full path for each trip:',
         'code': 'def test_planner():\n'
                 '    print(compute_manhattan_path((0, 0), (2, 3)))\n'
                 '    print(compute_manhattan_path((0, 2), (3, 2)))\n'
                 '    print(compute_manhattan_path((2, 0), (2, 3)))',
         'code_size': 22,
         'callout': '**Predict:** with only the east loop, what will each print? Then run '
                    '`test_planner()`.',
         'tone': 'orange'},

        {'kind': 'code', 'title': 'Step 2 · Check your output',
         'tag': 'Activity',
         'code': 'computing path from: (0, 0) to: (2, 3)\n'
                 '[(1, 0), (2, 0)]\n'
                 'computing path from: (0, 2) to: (3, 2)\n'
                 '[(1, 2), (2, 2), (3, 2)]\n'
                 'computing path from: (2, 0) to: (2, 3)\n'
                 '[]',
         'code_size': 22,
         'callout': 'Right two, then stop. The second needs no move up. The third only goes up, '
                    'so nothing is appended.',
         'tone': 'green'},

        # --- Step 3 ---
        {'kind': 'steps', 'title': 'Step 3 · Break it on purpose',
         'tag': 'Activity',
         'steps': [
             'Move `path.append((x, y))` one indent to the left, so it lines up with `while`',
             '**Predict** the first path, then run it',
             'Put the indent back',
         ],
         'callout': 'Predict before you run',
         'tone': 'orange',
         'notes': 'The indentation bug is the most common list bug there is; here it costs one '
                  'keystroke to cause and to fix.'},

        {'kind': 'code', 'title': 'Step 3 · What happened?',
         'tag': 'Activity',
         'code': 'computing path from: (0, 0) to: (2, 3)\n'
                 '[(2, 0)]\n'
                 'computing path from: (0, 2) to: (3, 2)\n'
                 '[(3, 2)]\n'
                 'computing path from: (2, 0) to: (2, 3)\n'
                 '[(2, 0)]',
         'code_size': 22,
         'callout': 'Indentation decides what\'s inside the loop. `append()` now runs **once, '
                    'after** the loop.',
         'tone': 'green',
         'notes': 'Only the last position is recorded. The third path is worse: the loop never '
                  'ran, so the function appended the start itself.'},

        # --- Step 4 ---
        {'kind': 'steps', 'title': 'Step 4 · Write north',
         'tag': 'Activity',
         'steps': [
             'Under the north comment, **copy the east loop**',
             'Compare `y` with `dest_y`, and step `y` instead of `x`',
             'Leave `path.append((x, y))` as it is: it records the whole position',
             'Run `test_planner()`. All three paths should match your paper test',
         ],
         'tone': 'green'},

        {'kind': 'code', 'title': 'Step 4 · Check your north loop',
         'tag': 'Activity',
         'code': '    # North: copy east, but step y until it matches dest_y\n'
                 '    while y < dest_y:\n'
                 '        y = y + 1             # one step up\n'
                 '        path.append((x, y))',
         'code_size': 22},

        {'kind': 'code', 'title': 'Step 4 · Check your output',
         'tag': 'Activity',
         'code': 'computing path from: (0, 0) to: (2, 3)\n'
                 '[(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]\n'
                 'computing path from: (0, 2) to: (3, 2)\n'
                 '[(1, 2), (2, 2), (3, 2)]\n'
                 'computing path from: (2, 0) to: (2, 3)\n'
                 '[(2, 1), (2, 2), (2, 3)]',
         'code_size': 22,
         'callout': 'All three match the paper test',
         'tone': 'green'},

        # --- Step 5 ---
        {'kind': 'code', 'title': 'Step 5 · A tuple can\'t change',
         'tag': 'Activity',
         'lead': 'Could the loop just add to one tuple instead of making new ones? Type these into the shell:',
         'code': 'spot = (2, 3)\n'
                 'spot.append(4)',
         'code_size': 26,
         'callout': '**Predict:** what happens?',
         'tone': 'orange'},

        {'kind': 'code', 'title': 'Step 5 · What happened?',
         'tag': 'Activity',
         'lead': 'A tuple **can\'t be changed** once it\'s made, so the loop makes a new one every '
                 'step:',
         'code': 'AttributeError: \'tuple\' object has no attribute \'append\'',
         'code_size': 22,
         'callout': '**Tuple:** one thing with a fixed number of parts, like a position. '
                    '**List:** any number of things in order, like the stops on a route.',
         'tone': 'teal',
         'notes': 'That\'s right for a position: (2, 3) should always mean the same intersection. '
                  'A list is the opposite: it can grow.'},

        {'kind': 'check',
         'question': 'A program adds every obstacle the robot finds, as it drives. What should it '
                     'store them in?',
         'options': ['One tuple, with `append()`',
                     'A list of tuples: each obstacle is an (x, y) tuple, and the list grows',
                     'A tuple of lists',
                     'Two separate variables, `x` and `y`'],
         'answer': 1,
         'explanation': 'Each position is a fixed pair, so a tuple. The collection grows as the '
                        'robot drives, so a list. That is exactly what Module 5 does.'},

        # --- Step 6 ---
        {'kind': 'code', 'title': 'Step 6 · Two names, one list',
         'tag': 'Activity',
         'lead': 'A list can grow, so it lives elsewhere. The variable holds its **address**: a '
                 '**reference**.',
         'code': 'a = 5\n'
                 'b = a\n'
                 'b = b + 1\n'
                 'print(a, b)\n'
                 '\n'
                 'path = [(1, 0)]\n'
                 'same_path = path\n'
                 'same_path.append((2, 0))\n'
                 'print(path)',
         'code_size': 20,
         'callout': '**Predict** both printouts, then run it in the shell',
         'tone': 'orange',
         'notes': 'This adds to Lesson 1-9; it doesn\'t correct it. A variable is still a named '
                  'memory location, and = still stores there. The new fact is what the stored '
                  'value is for a list: a location is a fixed size, so the list lives somewhere '
                  'else. A demo that lands: two students hold slips with the same post office box '
                  'number; one puts something in the box, and the other finds it there.'},

        {'kind': 'figure', 'title': 'Step 6 · What happened?',
         'tag': 'Activity',
         'figure': '/img/lesson-m4-02/number-vs-list.svg',
         'caption': 'Prints 5 6, then [(1, 0), (2, 0)]. b = a makes a second 5. same_path = path '
                    'makes a second arrow to the same list.',
         'notes': 'b = a copied the value: two separate 5s. same_path = path copied the address: '
                  'still one list, so appending through either name changes what both see. Don\'t '
                  'teach copy() or slicing: nothing in this course needs a separate copy, and '
                  'Module 5\'s BLOCKED list relies on the sharing.'},

        {'kind': 'code', 'title': 'Step 6 · Same for a parameter',
         'tag': 'Activity',
         'lead': '**Predict** both printouts, then run it:',
         'code': 'def move(spot):\n'
                 '    spot = (9, 9)             # assigns a new value\n'
                 '\n'
                 'def extend(steps):\n'
                 '    steps.append((9, 9))      # changes the list itself\n'
                 '\n'
                 'here = (1, 1)\n'
                 'move(here)\n'
                 'print(here)\n'
                 '\n'
                 'route = [(1, 1)]\n'
                 'extend(route)\n'
                 'print(route)',
         'code_size': 17},

        {'kind': 'code', 'title': 'Step 6 · What happened?',
         'tag': 'Activity',
         'code': '(1, 1)\n'
                 '[(1, 1), (9, 9)]',
         'code_size': 26,
         'callout': '`=` stores a new value in the function\'s own variable (4-1). '
                    '`append()` goes to the list itself, and there is only one list.',
         'tone': 'green',
         'notes': 'The caller never sees the =. Module 5 relies on the append: a planner sees '
                  'every obstacle you add to your list.'},

        {'kind': 'check',
         'question': 'What does `scores` hold after these three lines? `scores = [10, 20]`, '
                     '`backup = scores`, `backup.append(30)`',
         'options': ['`[10, 20]`: backup is a separate copy',
                     '`[10, 20, 30]`: both variables refer to the same list',
                     '`[30]`',
                     'An error: you cannot assign a list to another name'],
         'answer': 1,
         'explanation': 'backup = scores stores the address that was in scores, not a copy of the '
                        'list, so both variables lead to one list.'},

        {'kind': 'check',
         'question': 'A function is handed a list, `blocked`, and runs `blocked.append((2, 2))`. '
                     'What does the caller\'s list hold after?',
         'options': ['What it held before: functions cannot change the caller\'s variables',
                     'The old items plus (2, 2): the function and the caller refer to the same '
                     'list',
                     'Only (2, 2)',
                     'Nothing: the list is emptied when the function ends'],
         'answer': 1,
         'explanation': 'The parameter holds the list\'s address, so append() changes the one list '
                        'both sides share. Only assigning with = inside the function would leave '
                        'the caller\'s list alone.'},

        # --- Step 7 ---
        {'kind': 'steps', 'title': 'Step 7 · Run the main program',
         'tag': 'Activity',
         'steps': [
             'Set the run line back to `test_delivery()`',
             '**Predict:** will Leg 2, (2, 3) to (1, 0), work?',
             'Run it',
         ],
         'tone': 'orange'},

        {'kind': 'code', 'title': 'Step 7 · Check: Legs 1 and 2',
         'tag': 'Activity',
         'code': 'computing path from: (0, 0) to: (2, 3)\n'
                 '[(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]\n'
                 'moving: from (0, 0) to: (1, 0)\n'
                 'moving: from (1, 0) to: (2, 0)\n'
                 'moving: from (2, 0) to: (2, 1)\n'
                 'moving: from (2, 1) to: (2, 2)\n'
                 'moving: from (2, 2) to: (2, 3)\n'
                 'new position: (2, 3) heading: 0\n'
                 'computing path from: (2, 3) to: (1, 0)\n'
                 '[]\n'
                 'new position: (2, 3) heading: 0',
         'code_size': 18,
         'callout': 'Leg 2\'s path is empty, so the robot never leaves (2, 3). Every leg after it '
                    'goes wrong.',
         'tone': 'orange',
         'notes': 'The hook for Lesson 4-3: let students say what\'s missing. The rest of the '
                  'printout is on the lesson page: Leg 3 is [(3, 3)], and Legs 4 and 5 are [].'},

        {'kind': 'check',
         'question': 'Why is the path for Leg 2, (2, 3) to (1, 0), empty?',
         'options': ['`append()` only works once per program',
                     'Both while conditions are False from the start (2 is not < 1, 3 is not < 0), '
                     'so neither loop runs',
                     'The start and destination are the same',
                     'The driver is still a stub'],
         'answer': 1,
         'explanation': 'East and north only handle x and y getting bigger, and a while loop whose '
                        'condition starts False does nothing. Lesson 4-3 adds left and down.'},

        {'kind': 'wrapup',
         'questions': [
             'How does the planner build a path?',
             'Why is a position a tuple and a path a list?',
             'If two names refer to the same list and you append through one, what does the '
             'other see?',
             'What still doesn\'t work?',
         ],
         'next': 'the planner, part 2: every direction',
         'notes': 'Answers: start with [] and append() one position on every trip around a loop. '
                  'A position is a fixed pair that shouldn\'t change; a path grows one step at a '
                  'time. The change: there is only one list. Trips that go left or down: both '
                  'loops are skipped.'},
    ],
}
