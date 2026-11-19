"""Module 4, Lesson 4-1 · The Main Program."""

DECK = {
    'module': 4, 'lesson': 1,
    'doc': 'module-04-manhattan/lesson-01-the-main-program',
    'title': 'The Main Program',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Write a position as a tuple, `(x, y)`',
             'Use stubs so a program runs before the functions it calls are written',
             'Return two values from a function, and unpack them where it is called',
             'Keep several destinations in a list, and run the same code for each one with a '
             '`for` loop',
         ],
         'notes': '50 to 60 minutes, robot on the desk all lesson. Students write the top of the '
                  'tree from Lesson 4-0: the main program. The planner and the driver start as '
                  'stubs, so the whole program runs in the first coding lesson, and every later '
                  'lesson swaps one stub for the real thing. Tuples and unpacking get a sentence or two '
                  'each, inside the step that uses them. The list and the for loop arrive in '
                  'Step 4, as the fix for copying one delivery five times. Don\'t expand them: '
                  'append() arrives in 4-2, == in 4-3, indexing in 4-4.'},

        {'kind': 'bullets', 'title': 'Today: the top of the tree',
         'bullets': [
             'The **main program** sends the robot on its deliveries',
             'The planner and the driver don\'t exist yet, so they start as **stubs**',
             'The program **runs today**, and the robot never moves',
         ],
         'figure': '/img/lesson-m4t-00/decomposition-topdown-v2.svg',
         'split': 0.5,
         'size': 26},

        {'kind': 'steps', 'title': 'The main program in words',
         'tag': 'Plan',
         'lead': 'The robot starts at (0, 0) facing North. To make a delivery:',
         'steps': [
             '**Plan** the path from where it is now',
             '**Drive** the path, which leaves it somewhere new, facing a new way',
         ],
         'callout': 'The next delivery is planned from **there**',
         'tone': 'teal',
         'notes': 'So the program keeps track of the robot\'s position and its heading. Today all '
                  'students need is that 0 means North; the rest comes in Lesson 4-4.'},

        {'kind': 'code', 'title': 'The skeleton: two stubs',
         'code': 'def compute_manhattan_path(start, destination):\n'
                 '    print("computing path from:", start, "to:", destination)\n'
                 '    return [destination]\n'
                 '\n'
                 'def drive_path(path, current_position, current_heading):\n'
                 '    for next_pos in path:\n'
                 '        print("moving: from", current_position, "to:", next_pos)\n'
                 '        current_position = next_pos\n'
                 '    return current_position, current_heading',
         'code_size': 18,
         'notes': 'Students paste the whole skeleton from the lesson page into robot.py above RUN, '
                  'after the Module 3 code. The slide leaves out the comment banners and '
                  'docstrings to fit. Step 1 says what a stub is.'},

        {'kind': 'code', 'title': 'The skeleton: the main program',
         'code': 'def test_delivery():\n'
                 '    # 1. robot_position starts at (0, 0); robot_heading\n'
                 '    #    starts at 0, North\n'
                 '    # 2. plan the path from robot_position to (2, 3),\n'
                 '    #    and print it\n'
                 '    # 3. drive it, and assign the pose it hands back\n'
                 '    # 4. print "new position:", robot_position,\n'
                 '    #          "heading:", robot_heading\n'
                 '    pass',
         'code_size': 20,
         'callout': 'Each step prints something. **Predict** before every run, then compare.',
         'tone': 'teal',
         'notes': 'Set the run line to test_delivery(). Students fill in the outline over Steps 1 '
                  'and 2, copy it for a second delivery in Step 3, and turn it into a loop in '
                  'Step 4.'},

        # --- Step 1 ---
        {'kind': 'figure', 'title': 'Step 1 · A position is one value',
         'tag': 'Activity',
         'figure': '/img/lesson-m4-01/coordinate-axes.svg',
         'caption': 'x increases to the right and y increases up, both from (0, 0), the corner '
                    'nearest you.'},

        {'kind': 'bullets', 'title': 'Step 1 · A tuple, and a stub',
         'tag': 'Activity',
         'bullets': [
             '`(0, 0)` is a **tuple**: parentheses, a comma, **x first**',
             '`(2, 3)` and `(3, 2)` are different intersections',
             'A **stub** is a stand-in function: same name, same parameters, same kind of '
             'return value',
             'It **prints what the real function will print**, so you see it was called, and '
             'with what',
         ],
         'size': 24,
         'notes': 'The planner stub returns a pretend path that jumps straight to the '
                  'destination. A robot can\'t jump three blocks. If someone asks why the stub '
                  'returns a wrong path, that\'s the right question: a stub only has to keep the '
                  'program running.'},

        {'kind': 'check',
         'question': 'The robot is 3 across and 1 up from the corner nearest you. Which line '
                     'stores that?',
         'options': ['`robot_position = (1, 3)`',
                     '`robot_position = (3, 1)`',
                     '`robot_position = 3, 1, 0`',
                     '`robot_position = (0, 0) + (3, 1)`'],
         'answer': 1,
         'explanation': 'x comes first: 3 across, then y: 1 up. Both numbers count from 0, so the '
                        'corner itself is (0, 0).'},

        {'kind': 'code', 'title': 'Step 1 · One plan',
         'tag': 'Activity',
         'lead': 'Replace `pass` with outline steps 1 and 2:',
         'code': '    robot_position = (0, 0)\n'
                 '    robot_heading = 0               # facing North\n'
                 '    path = compute_manhattan_path(robot_position, (2, 3))\n'
                 '    print(path)',
         'code_size': 22,
         'callout': '**Predict:** what two lines will print?',
         'tone': 'orange'},

        {'kind': 'code', 'title': 'Step 1 · Check your output',
         'tag': 'Activity',
         'code': 'computing path from: (0, 0) to: (2, 3)\n'
                 '[(2, 3)]',
         'code_size': 24,
         'callout': 'The stub prints the first line; your `print(path)` prints the second',
         'tone': 'green',
         'notes': 'The square brackets hold the path\'s positions, here just one. Step 4 shows '
                  'how to make a list like that.'},

        # --- Step 2 ---
        {'kind': 'figure', 'title': 'Step 2 · The pose',
         'tag': 'Activity',
         'figure': '/img/lesson-m4t-01/pose-robot.svg',
         'caption': 'The pose ((1, 1), 1): at (1, 1), facing East.'},

        {'kind': 'code', 'title': 'Step 2 · Drive, and catch the pose',
         'tag': 'Activity',
         'lead': '`return current_position, current_heading` hands back both at once. Give each '
                 'its own variable:',
         'code': '    robot_position, robot_heading = drive_path(\n'
                 '        path, robot_position, robot_heading)\n'
                 '    print("new position:", robot_position, "heading:", robot_heading)',
         'code_size': 20,
         'callout': '**Unpacking:** the first variable gets the first value, the second gets the '
                    'second. One variable per value, or `ValueError`.',
         'tone': 'teal',
         'notes': 'A comma between two values makes a tuple, so the return hands back both '
                  'together. Predict before running: what will the two new lines say?'},

        {'kind': 'code', 'title': 'Step 2 · Check your output',
         'tag': 'Activity',
         'code': 'computing path from: (0, 0) to: (2, 3)\n'
                 '[(2, 3)]\n'
                 'moving: from (0, 0) to: (2, 3)\n'
                 'new position: (2, 3) heading: 0',
         'code_size': 22,
         'callout': 'One delivery, four lines. The heading stays 0: the driver stub never turns.',
         'tone': 'green'},

        # --- Step 3 ---
        {'kind': 'bullets', 'title': 'Step 3 · A second delivery',
         'tag': 'Activity',
         'bullets': [
             'Copy your four delivery lines: plan, print, drive, print',
             'Paste the copy under them',
             'In the copy, change `(2, 3)` to `(1, 0)`',
         ],
         'callout': '**Predict:** where will the second `computing path from:` start? Why there?',
         'tone': 'orange',
         'size': 26},

        {'kind': 'code', 'title': 'Step 3 · Check your output',
         'tag': 'Activity',
         'code': 'computing path from: (0, 0) to: (2, 3)\n'
                 '[(2, 3)]\n'
                 'moving: from (0, 0) to: (2, 3)\n'
                 'new position: (2, 3) heading: 0\n'
                 'computing path from: (2, 3) to: (1, 0)\n'
                 '[(1, 0)]\n'
                 'moving: from (2, 3) to: (1, 0)\n'
                 'new position: (1, 0) heading: 0',
         'code_size': 20,
         'callout': 'Leg 2 starts at (2, 3), where leg 1 ended, though the copy never says (2, 3)',
         'tone': 'green'},

        {'kind': 'bullets', 'title': 'Question', 'tag': 'Discuss',
         'bullets': ['Which line put (2, 3) into `robot_position`?'],
         'size': 28,
         'notes': 'Seeing the pose carry over matters now: in Step 4 the loop hides it. Let a '
                  'few students answer before the next slide.'},

        {'kind': 'bullets', 'title': 'Answer', 'tag': 'Discuss',
         'bullets': [
             'The drive line: `robot_position, robot_heading = drive_path(...)`',
             'Inside `drive_path()`, `current_position = next_pos` changes only the '
             'function\'s own variable',
         ],
         'callout': 'The return value is the only way the new pose gets back',
         'tone': 'green',
         'size': 26,
         'notes': 'Same idea as Lesson 2-7. A student who drops the left side sees leg 2 start '
                  'from (0, 0); on the floor, the robot drives leg 1 right and plans every later '
                  'leg from home.'},

        {'kind': 'check',
         'question': 'A student drops `robot_position, robot_heading =` from the driving call. '
                     'What goes wrong?',
         'options': ['Nothing: `drive_path()` updates `robot_position` for them',
                     '`robot_position` and `robot_heading` never changed, so the next leg is '
                     'planned from the old spot',
                     'Python raises an error about an unused return value',
                     'The robot drives the path twice'],
         'answer': 1,
         'explanation': 'current_position inside drive_path() is the function\'s own variable. The '
                        'main program only learns the new pose by assigning from the return.'},

        # --- Step 4 ---
        {'kind': 'bullets', 'title': 'Step 4 · Now five. Or fifty?', 'tag': 'Activity',
         'bullets': [
             'Three more stops: (3, 1), (2, 2), then home to (0, 0)',
             'Before you paste three more copies...',
         ],
         'size': 28},

        {'kind': 'bullets', 'title': 'Question 1 of 2', 'tag': 'Discuss',
         'bullets': ['How many lines would five deliveries take?', 'Fifty?'],
         'size': 28,
         'notes': 'Let pairs count before the next slide.'},

        {'kind': 'bullets', 'title': 'Answer 1 of 2', 'tag': 'Discuss',
         'bullets': ['Four lines per delivery', '**20** lines for five, **200** for fifty'],
         'size': 28},

        {'kind': 'bullets', 'title': 'Question 2 of 2', 'tag': 'Discuss',
         'bullets': ['From one copy to the next, what is different?'],
         'size': 28,
         'notes': 'After the answer, ask: if only one value changes, what would you want '
                  'instead of copies? Lead to: one copy of the code, and the destinations kept '
                  'together. If someone suggests range(5), that\'s a good instinct: it repeats, '
                  'but it gives numbers, not stops.'},

        {'kind': 'bullets', 'title': 'Answer 2 of 2', 'tag': 'Discuss',
         'bullets': ['Only the destination', 'And each copy is one more place to forget a change'],
         'callout': 'Keep the values together, and write the code once',
         'tone': 'green',
         'size': 28},

        {'kind': 'code', 'title': 'Step 4 · A list, and a for loop',
         'tag': 'Activity',
         'lead': 'A **list**: square brackets, commas between the items, in order. Put it above '
                 '`def test_delivery():`',
         'code': 'DELIVERY_STOPS = [(2, 3), (1, 0), (3, 1), (2, 2), (0, 0)]\n'
                 '\n'
                 '    for delivery_destination in DELIVERY_STOPS:',
         'code_size': 20,
         'callout': 'A `for` loop runs its body **once per item**, first to last; the loop '
                    'variable holds that item',
         'tone': 'teal',
         'notes': 'Capitals because it is a setting for the whole file. It is the for loop from '
                  'Lesson 1-10, with a list in place of range().'},

        {'kind': 'bullets', 'title': 'Step 4 · Rewrite test_delivery()', 'tag': 'Activity',
         'bullets': [
             'Keep the two starting lines',
             'Add the `for` line',
             'Indent **one** copy of the delivery under it, with `delivery_destination` in '
             'place of `(2, 3)`',
             'Delete the second copy',
         ],
         'callout': '**Predict:** how many lines will print, and what will the last one say?',
         'tone': 'orange',
         'size': 26},

        {'kind': 'code', 'title': 'Step 4 · Check: the whole loop',
         'tag': 'Activity',
         'code': 'def test_delivery():\n'
                 '    robot_position = (0, 0)\n'
                 '    robot_heading = 0               # facing North\n'
                 '    for delivery_destination in DELIVERY_STOPS:\n'
                 '        path = compute_manhattan_path(robot_position, delivery_destination)\n'
                 '        print(path)\n'
                 '        robot_position, robot_heading = drive_path(\n'
                 '            path, robot_position, robot_heading)\n'
                 '        print("new position:", robot_position, "heading:", robot_heading)',
         'code_size': 18,
         'callout': '20 lines: five stops, four each. The last: `new position: (0, 0) heading: 0`',
         'tone': 'green',
         'notes': 'The full printout is behind a reveal on the lesson page. Fifty stops would '
                  'need a longer list and no more code.'},

        {'kind': 'check',
         'question': 'You add a sixth stop, (3, 3), to the end of `DELIVERY_STOPS`. What else has '
                     'to change in `test_delivery()`?',
         'options': ['Nothing: the loop runs once more, for the new item',
                     'Add a sixth copy of the delivery lines',
                     'Change the `for` line to say 6',
                     'Set `robot_position` to (3, 3) before the loop'],
         'answer': 0,
         'explanation': 'A for loop over a list runs once per item, however many there are. '
                        'Adding a stop means adding to the list.'},

        {'kind': 'wrapup',
         'questions': [
             'How does Python store a position?',
             'What is a stub for, and why does it print?',
             'Why must the main program write `robot_position, robot_heading = drive_path(...)`?',
             'Why a list and a `for` loop instead of copies?',
         ],
         'next': 'the planner, part 1: a path that grows',
         'notes': 'Answers: a tuple, (x, y): parentheses, a comma, x first. It lets the '
                  'program run before the real function is written; the print shows it was '
                  'called, and with what. Assigning inside a function changes only its own '
                  'variable; the return value is the only way the new pose gets back, so the '
                  'next leg starts in the right place. Only the destination changes: the loop '
                  'writes the delivery once, and a new stop is one more item in the list.'},
    ],
}
