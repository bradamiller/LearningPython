"""Module 4, Lesson 4-1 · The Main Program."""

DECK = {
    'module': 4, 'lesson': 1,
    'doc': 'module-04-manhattan/lesson-01-the-main-program',
    'title': 'The Main Program',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Write a position as a tuple, `(x, y)`, and several destinations as a list',
             'Run the same code for every item in a list with a `for` loop',
             'Use stubs so a program runs before the functions it calls are written',
             'Return two values from a function, and unpack them where it is called',
         ],
         'notes': '50 to 60 minutes, robot on the desk all lesson. Students write the top of the '
                  'tree from Lesson 4-0: the main program. The planner and the driver start as '
                  'stubs, so the whole program runs in the first coding lesson, and every later '
                  'lesson swaps one stub for the real thing. Tuples, lists and the for loop get a '
                  'sentence or two each, inside the step that uses them. Don\'t expand them: '
                  'append() arrives in 4-2, == in 4-3, indexing in 4-4.'},

        {'kind': 'bullets', 'title': 'Today: the top of the tree',
         'bullets': [
             'The **main program** sends the robot to every destination on a list',
             'The planner and the driver don\'t exist yet, so they start as **stubs**',
             'The program **runs today**, and the robot never moves',
         ],
         'figure': '/img/lesson-m4t-00/decomposition-topdown-v2.svg',
         'split': 0.5,
         'size': 26},

        {'kind': 'steps', 'title': 'The main program in words',
         'tag': 'Plan',
         'lead': 'The robot starts at (0, 0) facing North. For each destination on its list:',
         'steps': [
             '**Plan** the path from where it is now',
             '**Drive** the path, which leaves it somewhere new, facing a new way',
         ],
         'callout': 'Then plan the next leg from **there**',
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
                  'docstrings to fit. Step 2 says what a stub is.'},

        {'kind': 'code', 'title': 'The skeleton: the main program',
         'code': 'DELIVERY_STOPS = [(2, 3), (1, 0), (3, 1), (2, 2), (0, 0)]\n'
                 '\n'
                 'def test_delivery():\n'
                 '    # 1. robot_position starts at (0, 0); robot_heading\n'
                 '    #    starts at 0, North\n'
                 '    # 2. for each delivery_destination in DELIVERY_STOPS:\n'
                 '    #      plan the path from robot_position, and print it\n'
                 '    #      drive it, and assign the pose it hands back\n'
                 '    #      print "new position:", robot_position,\n'
                 '    #            "heading:", robot_heading\n'
                 '    pass',
         'code_size': 20,
         'callout': 'Each step prints something. **Predict** before every run, then compare.',
         'tone': 'teal',
         'notes': 'Set the run line to test_delivery(). Students fill in the outline over Steps 1 '
                  'to 3.'},

        # --- Step 1 ---
        {'kind': 'figure', 'title': 'Step 1 · A position is one value',
         'tag': 'Activity',
         'figure': '/img/lesson-m4-01/coordinate-axes.svg',
         'caption': 'x increases to the right and y increases up, both from (0, 0), the corner '
                    'nearest you.'},

        {'kind': 'bullets', 'title': 'Step 1 · A tuple, and a list of them',
         'tag': 'Activity',
         'bullets': [
             '`(0, 0)` is a **tuple**: parentheses, a comma, **x first**',
             '`(2, 3)` and `(3, 2)` are different intersections',
             '`DELIVERY_STOPS` is a **list**: square brackets, commas between the items',
             '`for delivery_destination in DELIVERY_STOPS:` runs its body once per item, first '
             'to last',
         ],
         'size': 26,
         'notes': 'It is the for loop from Lesson 1-10, with a list in place of range().'},

        {'kind': 'check',
         'question': 'The robot is 3 across and 1 up from the corner nearest you. Which line '
                     'stores that?',
         'options': ['`robot_position = (1, 3)`',
                     '`robot_position = (3, 1)`',
                     '`robot_position = 3, 1, 0`',
                     '`robot_position = [3] + [1]`'],
         'answer': 1,
         'explanation': 'x comes first: 3 across, then y: 1 up. Both numbers count from 0, so the '
                        'corner itself is (0, 0).'},

        {'kind': 'code', 'title': 'Step 1 · Write it',
         'tag': 'Activity',
         'lead': 'Replace `pass` with outline step 1, the `for` line, and one line in the loop:',
         'code': 'def test_delivery():\n'
                 '    robot_position = (0, 0)\n'
                 '    robot_heading = 0               # facing North\n'
                 '    for delivery_destination in DELIVERY_STOPS:\n'
                 '        print("next stop:", delivery_destination)',
         'code_size': 22,
         'callout': '**Predict:** how many lines will print, and what is the first one?',
         'tone': 'orange'},

        {'kind': 'code', 'title': 'Step 1 · Check your output',
         'tag': 'Activity',
         'code': 'next stop: (2, 3)\n'
                 'next stop: (1, 0)\n'
                 'next stop: (3, 1)\n'
                 'next stop: (2, 2)\n'
                 'next stop: (0, 0)',
         'code_size': 24,
         'callout': 'Five items, five lines, in list order. Each item is a whole tuple.',
         'tone': 'green'},

        # --- Step 2 ---
        {'kind': 'bullets', 'title': 'Step 2 · Plan with a stub',
         'tag': 'Activity',
         'bullets': [
             'A **stub** is a stand-in function: same name, same parameters, same kind of return '
             'value',
             'Just enough inside to let the program run',
             'It **prints what the real function will print**, so you see it was called, and '
             'with what',
             'The planner stub returns `[destination]`: a wrong path, but a list of positions',
         ],
         'size': 24,
         'notes': 'A robot can\'t jump three blocks. If someone asks why the stub returns a wrong '
                  'path, that\'s the right question: a stub only has to keep the program running.'},

        {'kind': 'code', 'title': 'Step 2 · Call the planner',
         'tag': 'Activity',
         'lead': 'Replace the `print` in the loop with:',
         'code': '        path = compute_manhattan_path(robot_position, delivery_destination)\n'
                 '        print(path)',
         'code_size': 20,
         'callout': '**Predict:** the first two lines. Where will every `computing path from:` '
                    'start?',
         'tone': 'orange'},

        {'kind': 'code', 'title': 'Step 2 · Check your output',
         'tag': 'Activity',
         'code': 'computing path from: (0, 0) to: (2, 3)\n'
                 '[(2, 3)]\n'
                 'computing path from: (0, 0) to: (1, 0)\n'
                 '[(1, 0)]\n'
                 'computing path from: (0, 0) to: (3, 1)\n'
                 '[(3, 1)]\n'
                 'computing path from: (0, 0) to: (2, 2)\n'
                 '[(2, 2)]\n'
                 'computing path from: (0, 0) to: (0, 0)\n'
                 '[(0, 0)]',
         'code_size': 18,
         'callout': 'Every leg starts from (0, 0): nothing drives yet, so `robot_position` never '
                    'changes',
         'tone': 'green'},

        # --- Step 3 ---
        {'kind': 'figure', 'title': 'Step 3 · The pose',
         'tag': 'Activity',
         'figure': '/img/lesson-m4t-01/pose-robot.svg',
         'caption': 'The pose ((1, 1), 1): at (1, 1), facing East.'},

        {'kind': 'code', 'title': 'Step 3 · Drive, and catch the pose',
         'tag': 'Activity',
         'lead': '`return current_position, current_heading` hands back both at once. Give each '
                 'its own variable:',
         'code': '        robot_position, robot_heading = drive_path(\n'
                 '            path, robot_position, robot_heading)',
         'code_size': 22,
         'callout': '**Unpacking:** the first variable gets the first value, the second gets the '
                    'second. One variable per value, or `ValueError`.',
         'tone': 'teal',
         'notes': 'A comma between two values makes a tuple, so the return hands back both '
                  'together.'},

        {'kind': 'code', 'title': 'Step 3 · The whole loop',
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
         'callout': '**Predict:** what will the second `computing path from:` line say now?',
         'tone': 'orange'},

        {'kind': 'code', 'title': 'Step 3 · Check: first two stops',
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
         'callout': 'Four lines per stop; each leg starts where the last ended. The heading stays '
                    '0: the driver stub never turns.',
         'tone': 'green',
         'notes': 'The full printout is behind a reveal on the lesson page. The last stop ends '
                  'with: new position: (0, 0) heading: 0.'},

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

        {'kind': 'wrapup',
         'questions': [
             'How does Python store a position, and several destinations?',
             'What is a stub for, and why does it print?',
             'Why must the main program write `robot_position, robot_heading = drive_path(...)`?',
         ],
         'next': 'the planner, part 1: a path that grows',
         'notes': 'Answers: a tuple, (x, y); a list of tuples, in square brackets. It lets the '
                  'program run before the real function is written; the print shows it was '
                  'called, and with what. Assigning inside a function changes only its own '
                  'variable; the return value is the only way the new pose gets back.'},
    ],
}
