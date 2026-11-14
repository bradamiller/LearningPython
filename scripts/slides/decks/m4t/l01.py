"""Module 4 test (top-down trial), Lesson 4-1 · The Main Program."""

DECK = {
    'module': 4, 'lesson': 1, 'key': '4t-1', 'label': 'MODULE 4 TEST',
    'doc': 'test-module-04/lesson-01-the-main-program',
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
                  'tree from Lesson 4-0: the main program that sends the robot to every '
                  'destination on a list. The planner and the driver start as stubs, so the '
                  'program runs today. Tuples, lists and the for loop get about fifteen minutes, '
                  'on purpose: just enough to write the program. Don\'t expand them; append(), '
                  'indexing and the rest arrive in the lessons that need them, and Lesson 4-7 '
                  'pulls them together.'},

        {'kind': 'bullets', 'title': 'Today: the top of the tree',
         'bullets': [
             'The **main program** sends the robot to every destination on a list',
             'The planner and the driver don\'t exist yet, so they start as **stubs**',
             'The program **runs today**, and the robot never moves',
         ],
         'figure': '/img/lesson-m4t-00/decomposition-topdown-v2.svg',
         'split': 0.5,
         'size': 26},

        {'kind': 'figure', 'title': 'A position is one value',
         'figure': '/img/lesson-m4-01/coordinate-axes.svg',
         'caption': 'x increases to the right and y increases up, both from (0, 0), the corner '
                    'nearest you.',
         'notes': 'In Lesson 4-0 every intersection was a pair of numbers. x counts across to the '
                  'right, y counts away from you. The usual stumble is the order: x first.'},

        {'kind': 'code', 'title': 'A pair of numbers is a tuple',
         'lead': 'Python stores the pair as **one value**, written just as on the map:',
         'code': 'robot_position = (0, 0)\n'
                 'delivery_destination = (2, 3)',
         'code_size': 26,
         'callout': 'Parentheses, a comma, **x first**. `(2, 3)` and `(3, 2)` are different '
                    'intersections.',
         'tone': 'teal'},

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

        {'kind': 'code', 'title': 'Destinations are a list',
         'lead': 'Five stops would need five variables. A **list** holds them all, in order, in '
                 'one variable:',
         'code': 'DELIVERY_STOPS = [(2, 3), (1, 0), (3, 1), (2, 2), (0, 0)]',
         'code_size': 24,
         'callout': 'Square brackets, commas between the items. Each item is a tuple.',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Do something with every item',
         'code': 'for delivery_destination in DELIVERY_STOPS:\n'
                 '    print("Go to", delivery_destination)',
         'code_size': 24,
         'callout': 'Each time around, the next item is assigned to `delivery_destination`, '
                    'first to last',
         'tone': 'teal',
         'notes': 'It is the for loop from Lesson 1-10, with a list in place of range().'},

        {'kind': 'check',
         'question': 'How many lines does this print, and what is the last one? '
                     '`STOPS = [(1, 1), (0, 2), (3, 3)]` then '
                     '`for stop in STOPS: print("Go to", stop)`',
         'options': ['One line: `Go to [(1, 1), (0, 2), (3, 3)]`',
                     'Three lines; the last is `Go to (3, 3)`',
                     'Six lines, one for each number',
                     'Three lines; the last is `Go to 3`'],
         'answer': 1,
         'explanation': 'The loop runs once per item, and each item is a whole tuple. Three '
                        'items, three lines, in list order.'},

        {'kind': 'steps', 'title': 'The main program in words',
         'tag': 'Plan',
         'lead': 'The robot starts at (0, 0) facing North. For each destination on its list:',
         'steps': [
             '**Plan** the path from where it is now',
             '**Drive** the path, which leaves it somewhere new, facing a new way',
         ],
         'callout': 'Then plan the next leg from **there**',
         'tone': 'teal',
         'notes': 'So the program keeps track of two things: the robot\'s position, a tuple, in '
                  'robot_position, and its heading, a number from 0 to 3, in robot_heading. '
                  'Today all students need is that 0 means North; the rest comes in Lesson 4-4.'},

        {'kind': 'figure', 'title': 'Position and heading: the pose',
         'figure': '/img/lesson-m4t-01/pose-robot.svg',
         'caption': 'The pose ((1, 1), 1): at (1, 1), facing East. drive_path hands it back.',
         'notes': 'The planner will be compute_manhattan_path(start, destination), and the driver '
                  'drive_path(path, current_position, current_heading).'},

        {'kind': 'bullets', 'title': 'Stubs: run it before the parts exist',
         'bullets': [
             'A **stub** is a stand-in function: same name, same parameters, same kind of return '
             'value',
             'Only enough inside to let the program run',
             'Each stub **prints what the real function will print**',
             'So the printout shows the main program called it, and with what',
         ],
         'size': 26},

        {'kind': 'code', 'title': 'The two stubs',
         'code': 'def compute_manhattan_path(start, destination):\n'
                 '    print("computing path from:", start, "to:", destination)\n'
                 '    return [destination]\n'
                 '\n'
                 'def drive_path(path, current_position, current_heading):\n'
                 '    for next_pos in path:\n'
                 '        print("moving: from", current_position, "to:", next_pos)\n'
                 '        current_position = next_pos\n'
                 '    return current_position, current_heading',
         'code_size': 16,
         'callout': 'The planner stub\'s path is wrong, but it is a list of positions: all the '
                    'main program needs today',
         'tone': 'orange',
         'notes': 'The slide leaves out the docstrings to fit; the lesson page has them. A robot '
                  'can\'t jump three blocks, which is the right question for a student to ask: a '
                  'stub only has to keep the program running.'},

        {'kind': 'code', 'title': 'Handing back two values',
         'lead': '`return current_position, current_heading` hands back both at once. Give each '
                 'its own variable:',
         'code': 'robot_position, robot_heading = drive_path(\n'
                 '    path, robot_position, robot_heading)',
         'code_size': 22,
         'callout': 'That\'s **unpacking**: the first variable gets the first value, the second '
                    'gets the second',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Why it has to hand them back',
         'bullets': [
             'When the call runs, `current_position` starts with the value of `robot_position`',
             '`current_position = next_pos` changes only `drive_path()`\'s **own** variable',
             'The caller\'s `robot_position` is never touched (Lesson 2-7)',
             'So the **return value** is the only way the main program learns where the robot '
             'ended up',
         ],
         'size': 24},

        {'kind': 'code', 'title': 'This lesson\'s skeleton: the main program',
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
         'code_size': 16,
         'notes': 'Students paste the whole skeleton from the lesson page into robot.py above RUN, '
                  'after the Module 3 code: the two stubs, each under its comment banner, then '
                  'this. Copy it from the page; the slide shows only the part they write.'},

        {'kind': 'steps', 'title': 'Step 1 · The loop on its own',
         'tag': 'Activity',
         'steps': [
             'Write step 1 and the `for` line of step 2',
             'For now, one line inside the loop: `print("next stop:", delivery_destination)`',
             'Set the run line to `test_delivery()`, run it, and press the button',
         ],
         'callout': 'Correct: five lines, one per stop, in list order',
         'tone': 'green'},

        {'kind': 'steps', 'title': 'Step 2 · Plan and drive',
         'tag': 'Activity',
         'steps': [
             'Replace that `print` with the rest of step 2',
             'Run it. The robot stays on the desk',
         ],
         'callout': 'Correct: four lines per stop. Each `computing path from:` starts at the '
                    '`new position:` before it. The heading is 0 every time.',
         'tone': 'green',
         'notes': 'The four lines are what the planner was asked, the path, the move, and where '
                  'the robot is now. The driver stub never turns, so the heading stays 0. The '
                  'finished test_delivery() and its output are behind a reveal on the lesson page.'},

        {'kind': 'steps', 'title': 'Step 3 · Break it on purpose',
         'tag': 'Activity',
         'steps': [
             'Change the driving call to just `drive_path(path, robot_position, robot_heading)`, '
             'with nothing on the left',
             '**Predict:** what will each `computing path from:` line say?',
             'Run it. Then put `robot_position, robot_heading =` back',
         ],
         'tone': 'orange',
         'callout': 'Predict before you run',
         'notes': 'Every line says computing path from: (0, 0), and every new position is (0, 0). '
                  'drive_path() still worked out where the robot ended up, but nobody caught the '
                  'answer. This is the lesson\'s point: the dropped return value is the most '
                  'common Module 4 bug, and it normally surfaces on the floor, on leg 2. Here '
                  'students cause it on purpose, on screen, in two minutes.'},

        {'kind': 'check',
         'question': 'A student calls `drive_path(path, robot_position, robot_heading)` with '
                     'nothing on the left, then plans the next leg. What goes wrong?',
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
             'What does `for delivery_destination in DELIVERY_STOPS:` do?',
             'What is a stub for, and why does it print?',
             'Why must the main program write `robot_position, robot_heading = drive_path(...)`?',
         ],
         'next': 'the planner, part 1: a path that grows',
         'notes': 'Answers: a tuple, (x, y); a list of tuples. It runs the body once per item, '
                  'with delivery_destination set to each in turn. It lets the program run before '
                  'the real function exists; the print shows it was called, and with what. '
                  'Assigning to a parameter changes only the function\'s own variable; the return '
                  'value is the only way the new pose gets back.'},
    ],
}
