DECK = {
    'module': 4, 'lesson': 3,
    'doc': 'module-04-manhattan/lesson-03-lists',
    'title': 'Lists',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Create a list with `[]` and see how it differs from a tuple',
             'Add items with `append()` and count them with `len()`',
             'Loop through a list with a `for` loop',
             'Build a list step by step inside a loop, and store a path as a list of tuples',
             'Explain what a variable holds when the value is a list, and what happens when two '
             'names refer to the same one',
         ],
         'notes': '50 minutes. Scratch work again, like Lesson 4-2: a scratch file or the Python '
                  'prompt, not robot.py. The build-in-a-loop pattern practiced here is what next '
                  'lesson\'s planner function is made of; that function is what goes in the '
                  'file.'},

        {'kind': 'bullets', 'title': 'A path is many positions',
         'bullets': [
             'A tuple stores **one** position',
             'A **path** is many positions in order, and for that you need a **list**',
             'By the end you\'ll represent a route as a list of coordinate tuples, like '
             '`[(1,0), (2,0), (2,1), (2,2), (2,3)]`',
             'And build one up step by step: exactly what the Manhattan algorithm does next '
             'lesson',
         ],
         'callout': 'Scratch work again: a scratch file or the Python prompt, not `robot.py`',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'The start is not in the path',
         'bullets': [
             'That example is the route from `(0,0)` to `(2,3)`',
             'The robot\'s own starting intersection **isn\'t in it**',
             'A path lists the places the robot **drives to**',
             'It\'s already standing on the start: putting it in the list would mean "drive to '
             'where you already are"',
         ],
         'callout': 'Every path in this module and the next works that way',
         'tone': 'orange'},

        {'kind': 'figure', 'title': 'One tuple per intersection it drives to',
         'figure': '/img/lesson-m4-03/path-list-xy.svg',
         'caption': 'In order. The start is where it already is, so it is not in the list, and '
                    '`len(path)` is the number of steps.'},

        {'kind': 'code', 'title': 'List vs. tuple',
         'lead': 'A **list** is an ordered collection written with square brackets, and unlike '
                 'a tuple it\'s **mutable**: it can grow and change.',
         'lead_h': 1.2,
         'code': 'numbers = [1, 2, 3, 4, 5]\n'
                 'print(numbers[0])     # 1   -- indexing works like tuples\n'
                 'print(len(numbers))   # 5   -- how many items',
         'code_size': 22},

        {'kind': 'table', 'title': 'Which one, when?',
         'headers': ['', 'Tuple', 'List'],
         'widths': [2, 2, 2],
         'rows': [
             ['Brackets', '`( )`', '`[ ]`'],
             ['Can change?', 'No (immutable)', 'Yes (mutable)'],
             ['Best for', 'a fixed position', 'a growing path'],
         ],
         'size': 24,
         'callout': 'So a **coordinate** is a tuple; a **path** is a list of tuples',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'Which is true about lists compared to tuples?',
         'options': ['Lists use () and cannot change',
                     'Lists use [] and CAN change (they are mutable)',
                     'Lists and tuples are identical',
                     'Lists can only hold numbers'],
         'answer': 1,
         'explanation': 'Lists use square brackets and are mutable, so they can grow: perfect for '
                        'a path that\'s built up step by step.'},

        {'kind': 'code', 'title': 'Growing a list with `append()`',
         'lead': '`append()` adds an item to the **end** of a list. Start empty and build up:',
         'code': 'path = []\n'
                 'path.append((1, 0))\n'
                 'path.append((2, 0))\n'
                 'path.append((3, 0))\n'
                 'print(path)        # [(1, 0), (2, 0), (3, 0)]\n'
                 'print(len(path))   # 3',
         'code_size': 22,
         'callout': 'A robot at `(0,0)` driving three intersections to the right: three places to '
                    'drive to, so `len(path)` is 3, the number of steps',
         'callout_size': 21,
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Loop through it with `for`',
         'code': 'for step in path:\n'
                 '    print("Visit:", step, " x:", step[0], " y:", step[1])',
         'code_size': 22,
         'callout': 'Each pass, `step` is one tuple from the list, in order',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'Given path = [(1, 0), (2, 0), (3, 0)], what does path[2] return?',
         'options': ['(2, 0)', '(3, 0)', '2', 'An IndexError'],
         'answer': 1,
         'explanation': 'Indexing starts at 0, so path[2] is the third item: the tuple (3, 0).'},

        {'kind': 'check',
         'question': 'For that same path, what does path[2][1] return?',
         'options': ['3', '0', '(3, 0)', 'An error'],
         'answer': 1,
         'explanation': 'path[2] is (3, 0); then [1] takes its y, 0. Two indexes: which step, '
                        'then which part of that step.'},

        {'kind': 'code', 'title': 'Activity · Build a path in a loop', 'tag': 'Activity',
         'lead': 'The pattern the whole module depends on: **start empty, append inside a '
                 'loop.**',
         'code': 'path = []\n'
                 'for x in range(1, 5):            # start at 1, not 0 -- the robot is already '
                 'at x = 0\n'
                 '    path.append((x, 0))\n'
                 'print(path)        # [(1, 0), (2, 0), (3, 0), (4, 0)]',
         'code_size': 20,
         'callout': '`range(1, 5)` counts 1, 2, 3, 4: it starts where you tell it to, so the '
                    'first intersection you append is the first one the robot drives to',
         'callout_size': 21,
         'tone': 'teal'},

        {'kind': 'steps', 'title': 'Trace it, then change it',
         'steps': [
             'Trace the loop: the list grows by **one** each pass',
             'Change the loop to vary **y** instead, and you build a vertical path',
             'Combine a "go right" loop and a "go up" loop, and you\'ve basically written the '
             'Manhattan algorithm',
         ],
         'notes': 'This is make-or-break: Lesson 4-4\'s algorithm relies entirely on "empty '
                  'list, append inside a loop." Spend real time here with a trace table. Demo '
                  'the classic bug live: put append() outside the loop (wrong indentation) so '
                  'only the last item lands, then fix the indentation. Keep scope tight: [], '
                  'append(), len(), indexing and for. No insert, pop, slicing or comprehensions '
                  'yet.'},

        {'kind': 'figure', 'title': 'The pattern, traced',
         'figure': './decks/m4/fig/build-path.svg', 'frame': 0.35,
         'caption': 'One append per pass, so the list grows by one each time. Drawn on a 4 by 4 '
                    'grid, so the loop stops at x = 3.',
         'notes': 'The lesson figure is an animation: the loop appends (1, 0), (2, 0), (3, 0) one '
                  'pass at a time, and the start (0, 0) is never added. This is the end of that '
                  'part. (The slides use a copy of the figure with its text halos redrawn for '
                  'the slide renderer.)'},

        {'kind': 'figure', 'title': 'Then a go-right loop and a go-up loop',
         'figure': './decks/m4/fig/build-path.svg', 'frame': 0.88,
         'caption': 'Two loops, one after the other: the path from (0, 0) to (2, 3), five steps.',
         'notes': 'The second half of the same animation. Students do not write the general '
                  'version yet: that is next lesson.'},

        {'kind': 'bullets', 'title': 'What the variable actually holds',
         'bullets': [
             'Back in Lesson 1-9, a variable was a **named location in memory**, and `=` stored '
             'a value there',
             'That\'s still true, and for a number it\'s the whole story: `side_length = 30` puts '
             'a `30` in that location',
             'Remember the numbers on those locations, the **addresses**? Here is what they\'re '
             'for.',
         ],
         'size': 26},

        {'kind': 'bullets', 'title': 'A list can\'t fit in a location',
         'bullets': [
             'A list **grows**: `append()` makes it longer',
             'A memory location is a **fixed size**, so none is guaranteed big enough',
             'So the list lives somewhere else in memory, in as much room as it needs',
             'What goes in `path`\'s location is that area\'s **address**: the number that says '
             'where to find it',
         ],
         'callout': 'An address stored in a variable is called a **reference**',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Two names, one address',
         'lead': 'That sounds like a technicality until two names hold the same address:',
         'code': 'path = []\n'
                 'path.append((1, 0))\n'
                 '\n'
                 'same_path = path          # copies the ADDRESS, not the list\n'
                 'same_path.append((2, 0))\n'
                 '\n'
                 'print(path)               # [(1, 0), (2, 0)]  <- path changed too',
         'code_size': 21,
         'callout': '`same_path = path` works out the right side, an address, and stores it. '
                    'Nothing copied the list.',
         'callout_size': 21,
         'tone': 'orange'},

        {'kind': 'figure', 'title': 'Two names, one list',
         'figure': '/img/lesson-m4-03/two-names-one-list.svg',
         'caption': 'Two locations, the same address in each, one list at the end of both '
                    'arrows.'},

        {'kind': 'code', 'title': 'Compare: a number is copied',
         'lead': 'There is only **one list** above: appending through either name changes it. '
                 'A number is small and fixed in size, so it really is stored in the location:',
         'lead_h': 1.2,
         'code': 'a = 5\n'
                 'b = a                     # copies the VALUE\n'
                 'b = b + 1\n'
                 'print(a)                  # 5  <- unchanged',
         'code_size': 22,
         'callout': 'If a list were copied on assignment, `path` would still be one item long. '
                    'It isn\'t.',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'After scores = [10, 20], then backup = scores, then backup.append(30), '
                     'what does scores hold?',
         'options': ['[10, 20]: backup is a separate copy',
                     '[10, 20, 30]: both names refer to the same list',
                     '[30]',
                     'An error: you cannot assign a list to another name'],
         'answer': 1,
         'explanation': 'backup = scores stores the address that was in scores, not a copy of '
                        'the list, so both names lead to one list. Appending through either name '
                        'changes what both see. To get an independent copy you would have to make '
                        'a new list.'},

        {'kind': 'bullets', 'title': 'Not a trap: a mechanism',
         'bullets': [
             'This is the mechanism the rest of the course relies on',
             'In **Module 5** you\'ll build a list of blocked intersections and hand it to a '
             'planner object',
             'You keep adding to it as the robot discovers obstacles',
             'The planner sees every new obstacle precisely **because** it holds the address of '
             'your list, not a frozen copy of it',
         ],
         'notes': 'Be explicit: this section adds to Lesson 1-9, it does not correct it. A '
                  'variable is still a named memory location, and = still works out the right '
                  'side and stores the result. The only new fact is what the stored value is '
                  'for a list: the address that was printed on the location all along. If asked '
                  'why the address exists, the physical reason is the honest one: a location is '
                  'a fixed size, a list can grow. A demo that lands: two students each hold a '
                  'slip with the same post office box number. One puts something in the box. '
                  'The other one\'s slip has not changed, but what they find in the box has. Then '
                  'ask what would have to be different for them to have separate boxes. Don\'t '
                  'teach copy() or slicing: nothing in the course needs an independent copy, and '
                  'the aliasing is load-bearing in Module 5.'},

        {'kind': 'code', 'title': 'The most common list bug',
         'lead': 'Indentation decides what\'s inside the loop. Get it wrong and only the last '
                 'item is added:',
         'code': '# WRONG -- append is outside the loop\n'
                 'path = []\n'
                 'for x in range(1, 4):\n'
                 '    position = (x, 0)\n'
                 'path.append(position)     # only runs once -> [(3, 0)]\n'
                 '\n'
                 '# CORRECT -- append is inside the loop\n'
                 'path = []\n'
                 'for x in range(1, 4):\n'
                 '    position = (x, 0)\n'
                 '    path.append(position)  # runs each pass -> [(1, 0), (2, 0), (3, 0)]',
         'code_size': 18},

        {'kind': 'check',
         'question': 'A student\'s loop ends with a list holding only the LAST coordinate '
                     'instead of all of them. What\'s wrong?',
         'options': ['append() is broken',
                     'append() is outside the loop (wrong indentation), so it runs only once',
                     'They used a tuple instead of a list',
                     'range() is the wrong size'],
         'answer': 1,
         'explanation': 'If append() isn\'t indented inside the loop, it runs a single time after '
                        'the loop ends, capturing just the final value.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Apps', 'Feeds & playlists',
              'A playlist or a feed is a list you add to and iterate through, item by item.'),
             ('Navigation', 'Route waypoints',
              'A GPS route is a list of waypoints the app walks through in order.'),
             ('Data', 'Records & logs',
              'Programs collect results into a list, then loop over them to summarize or '
              'display.'),
         ]},

        {'kind': 'wrapup',
         'questions': [
             'Tuple vs list: which is for a position, which for a path?',
             'What does `append()` do?',
             'What\'s the pattern for building a path?',
             'Two names refer to the same list and you append through one. What does the other '
             'see?',
         ],
         'next': 'computing a path automatically: the Manhattan algorithm',
         'notes': 'Answers: tuple = position, list = path. Adds an item to the end. Start with '
                  '[], append() inside a loop. The change: there\'s only one list, and both names '
                  'hold its address. Formative: create a list, append() in a loop, index into a '
                  'list of tuples (path[3][1]), and spot the indentation bug. Exit ticket: '
                  '"Given path = [(1,0),(2,0),(3,0)], what is path[2][1]?" (0). Next lesson '
                  'starts on paper.'},
    ],
}
