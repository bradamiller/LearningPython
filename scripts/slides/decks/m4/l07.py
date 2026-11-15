"""Module 4, Lesson 4-7 · Tuples and Lists: What You Now Know."""

DECK = {
    'module': 4, 'lesson': 7,
    'doc': 'module-04-manhattan/lesson-07-tuples-and-lists',
    'title': 'Tuples and Lists: What You Now Know',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Say when to use a tuple and when to use a list',
             'Create, unpack, index, compare and loop over them without looking it up',
             'Predict what a few lines of tuple and list code print',
             'Explain what happens when two variables refer to the same list',
         ],
         'notes': '45 to 55 minutes, no robot. Students never had a lesson on tuples or lists: they '
                  'picked them up a piece at a time, because the delivery program needed them. This '
                  'lesson lays the pieces side by side, checks them away from the robot, and adds '
                  'references, which Module 5 depends on. If time is short, do the activity and '
                  '"What the variable actually holds", and skip the tables.'},

        {'kind': 'table', 'title': 'Where you used each piece',
         'lead': 'Every line is from your own `robot.py`:',
         'headers': ['What it does', 'From your program', 'Lesson'],
         'widths': [2.6, 6.4, 1.4],
         'rows': [['Make a tuple', '`robot_position = (0, 0)`', '4-1'],
                  ['Make a list', '`DELIVERY_STOPS = [(2, 3), (1, 0), ...]`', '4-1'],
                  ['Loop over a list', '`for delivery_destination in DELIVERY_STOPS:`', '4-1'],
                  ['Unpack', '`x, y = start`', '4-1, 4-2'],
                  ['Start empty, grow', '`path = []` and `path.append((x, y))`', '4-2'],
                  ['Compare', '`if actual == expected:`', '4-3'],
                  ['Pick one by index', '`HEADING_NAMES[robot_heading]`', '4-4']],
         'size': 18, 'row_h': 0.5},

        {'kind': 'code', 'title': 'Looping by index',
         'code': 'for i in range(len(path)):\n'
                 '    print("step", i, "is", path[i])',
         'code_size': 22,
         'callout': '`len(path)` is how many items; `range()` counts 0 up to one less: exactly '
                    'the indexes',
         'tone': 'teal',
         'notes': '`for next_pos in path:` hands you each item. Loop over the indexes when you '
                  'also need the item\'s place in the list. Module 5 uses this to number the '
                  'legs of a run.'},

        {'kind': 'code', 'title': 'Unpacking in a for line',
         'code': 'for x, y in path:\n'
                 '    print("x is", x, "and y is", y)',
         'code_size': 22,
         'callout': 'Each pass splits the tuple: the same as `for next_pos in path:` then '
                    '`x, y = next_pos`',
         'tone': 'teal'},

        {'kind': 'table', 'title': 'Tuple or list?',
         'headers': ['', 'Tuple', 'List'],
         'widths': [3.6, 3.2, 3.6],
         'rows': [['Written with', '`( )`', '`[ ]`'],
                  ['Can it change?', 'No', 'Yes: grow, or replace an item'],
                  ['Index, unpack, `==`, `for`, `len()`', 'Yes', 'Yes'],
                  ['`append()`', 'No', 'Yes'],
                  ['In your program', 'a position, a pose', 'a path, the stops, the letters']],
         'size': 20, 'row_h': 0.55,
         'callout': 'A **tuple** is one thing with a fixed number of parts. A **list** is any '
                    'number of things in order.',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'A program must remember every intersection where the robot found an obstacle, '
                     'adding to it as the robot drives. What should it use?',
         'options': ['One tuple, with `append()`',
                     'A list of tuples: each obstacle is an (x, y) tuple, and the list grows',
                     'A tuple of lists',
                     'Two separate variables, x and y'],
         'answer': 1,
         'explanation': 'Each position is a fixed pair, so a tuple. The collection grows as the '
                        'robot drives, so a list. That is exactly what Module 5 does.'},

        {'kind': 'code', 'title': 'Activity · Predict, then run',
         'tag': 'Activity',
         'code': 'path = [(1, 0), (2, 0), (2, 1)]\n'
                 'print(len(path))                               # 1\n'
                 'print(path[0])                                 # 2\n'
                 'print(path[2][1])                              # 3\n'
                 'x, y = path[1]\n'
                 'print(x + y)                                   # 4\n'
                 'path.append((2, 2))\n'
                 'print(len(path), path[3])                      # 5\n'
                 'print(path == [(1, 0), (2, 0), (2, 1)])        # 6\n'
                 'path[0] = (0, 1)\n'
                 'print(path)                                    # 7\n'
                 'path[0][0] = 5                                 # 8',
         'code_size': 15,
         'callout': 'In a **new file**. Write all eight predictions, then run it. One line is an '
                    'error: which, and why?',
         'tone': 'orange',
         'notes': 'This is the module\'s check on the Python: collect the written predictions '
                  'before anyone runs it. Answers: 3; (1, 0); 1; 2; 4 (2, 2); False, the list has '
                  'four items now; [(0, 1), (2, 0), (2, 1), (2, 2)], a list item can be replaced; '
                  'line 8 is a TypeError, because path[0] is a tuple and a tuple can\'t change. A '
                  'student who gets lines 3, 6 and 8 right has the tuples and '
                  'lists that Module 5 builds on.'},

        {'kind': 'check',
         'question': 'After these lines, what is `total`? `legs = [(2, 3), (1, 0)]`, `total = 0`, '
                     'then `for leg in legs:` `x, y = leg` and `total = total + x + y`',
         'options': ['2', '6', '4', 'An error: a tuple cannot be unpacked inside a loop'],
         'answer': 1,
         'explanation': 'First pass: x is 2, y is 3, total becomes 5. Second pass: x is 1, y is 0, '
                        'total becomes 6.'},

        {'kind': 'check',
         'question': 'Given `path = [(1, 0), (2, 0), (3, 0)]`, which gives the y of the last '
                     'position?',
         'options': ['`path[3][1]`', '`path[2][1]`', '`path[1][2]`', '`path(2, 1)`'],
         'answer': 1,
         'explanation': 'Three items have indexes 0, 1 and 2, so the last is path[2]. Its y is index '
                        '1. path[3] would be an IndexError.'},

        {'kind': 'code', 'title': 'What the variable actually holds',
         'code': 'a = 5\n'
                 'b = a                     # copies the VALUE: two 5s\n'
                 '\n'
                 'path = [(1, 0)]\n'
                 'same_path = path          # copies the ADDRESS: still one list\n'
                 'same_path.append((2, 0))\n'
                 'print(path)               # [(1, 0), (2, 0)]  <- path changed too',
         'code_size': 18,
         'callout': 'A list lives elsewhere in memory; the variable holds its **address**, a '
                    '**reference**',
         'tone': 'teal',
         'notes': 'This adds to Lesson 1-9, it doesn\'t correct it: a variable is still a named '
                  'memory location. The only new fact is what the stored value is for a list. Why: a '
                  'location is a fixed size and a list can grow, so the list lives somewhere with '
                  'room and the location keeps the number that says where. Demo: two students hold '
                  'slips with the same post office box number; one puts something in the box; the '
                  'other\'s slip hasn\'t changed, but what they find in the box has.'},

        {'kind': 'figure', 'title': 'Two names, one list',
         'figure': '/img/lesson-m4-02/number-vs-list.svg',
         'caption': '`b = a` makes a second 5. `same_path = path` makes a second arrow to the same '
                    'list.'},

        {'kind': 'check',
         'question': 'What does `scores` hold after `scores = [10, 20]`, `backup = scores`, '
                     '`backup.append(30)`?',
         'options': ['`[10, 20]`: backup is a separate copy',
                     '`[10, 20, 30]`: both variables refer to the same list',
                     '`[30]`',
                     'An error: you cannot assign a list to another name'],
         'answer': 1,
         'explanation': 'backup = scores stores the address that was in scores, not a copy, so both '
                        'variables lead to one list.'},

        {'kind': 'code', 'title': 'Assigning versus changing',
         'code': 'def move(spot):\n'
                 '    spot = (9, 9)             # ASSIGNS: spot now holds something else\n'
                 '\n'
                 'def extend(steps):\n'
                 '    steps.append((9, 9))      # CHANGES the list steps refers to\n'
                 '\n'
                 'here = (1, 1)\n'
                 'move(here)\n'
                 'print(here)                   # (1, 1)  -- untouched\n'
                 '\n'
                 'route = [(1, 1)]\n'
                 'extend(route)\n'
                 'print(route)                  # [(1, 1), (9, 9)]  -- changed',
         'code_size': 15,
         'callout': '`=` stays in the function (Lesson 4-1). `append()` goes to the one list both '
                    'sides share.',
         'tone': 'teal',
         'notes': 'Run move() and extend() live: the two printouts side by side do more than the '
                  'explanation. A tuple can\'t be changed at all, so a function can never alter a '
                  'position you hand it. This isn\'t a trap; the course relies on it: in Module 5 '
                  'a planner sees each obstacle you add because it holds the list\'s address. Don\'t '
                  'teach copy() or slicing.'},

        {'kind': 'check',
         'question': 'A function is handed a list called `blocked` and runs '
                     '`blocked.append((2, 2))`. After it returns, what does the caller\'s list hold?',
         'options': ['What it held before: functions cannot change the caller\'s variables',
                     'The old items plus (2, 2): the function and the caller refer to the same list',
                     'Only (2, 2)',
                     'Nothing: the list is emptied when the function ends'],
         'answer': 1,
         'explanation': 'The parameter holds the list\'s address, so append() changes the one list '
                        'both sides share. Only assigning with = inside the function would leave the '
                        'caller\'s list alone.'},

        {'kind': 'wrapup',
         'questions': [
             'Tuple or list: which for a position, which for a path, and why?',
             'Name three things you can do with both',
             'What can a list do that a tuple can\'t?',
             'Two variables refer to the same list and you append through one. What does the other '
             'see?',
         ],
         'next': 'Module 5: obstacles on the grid',
         'notes': 'Exit ticket: write the line that makes an empty list called seen, the line that '
                  'adds the position 3 across and 1 up, and the line that prints its y. (seen = [], '
                  'seen.append((3, 1)), print(seen[0][1]).) Module 5 puts obstacles on the grid: the '
                  'planner changes; drive_path() and the main program don\'t.'},
    ],
}
