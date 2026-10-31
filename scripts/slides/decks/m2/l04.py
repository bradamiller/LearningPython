DECK = {
    'module': 2, 'lesson': 4,
    'doc': 'module-02-line-tracking/lesson-04-random-turns',
    'title': 'Random Turns',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Explain what a **module** is and use `import` to bring one in',
             'Generate random integers with `random.randint(a, b)`',
             'Say why always turning 180° traps the robot in a pattern',
             'Write a random-angle version of your bounce test, from an outline',
         ],
         'notes': '50 to 60 minutes. A short lesson with one new tool, randint, and one '
                  'one-line change to last lesson\'s test. Most of the time goes to the '
                  'experiment in step 2.'},

        {'kind': 'bullets', 'title': 'Your bounce robot has a flaw',
         'bullets': [
             'It turns **exactly 180°** every time',
             'So it retraces the same path back and forth',
             'It never explores the rest of the circle',
         ],
         'callout': 'The fix is **randomness**: turn a different amount each bounce',
         'tone': 'teal',
         'notes': 'Ask who noticed this at the end of Lesson 2-3. To get random numbers we '
                  'import one of Python\'s built-in toolboxes.'},

        {'kind': 'code', 'title': 'Modules and `import`',
         'lead': 'Python ships with thousands of ready-made tools grouped into **modules**. '
                 'Think of each as a **toolbox**. To use one, you `import` it at the top of '
                 'your file. You have done this already for the robot:',
         'lead_h': 1.2,
         'code': 'from XRPLib.reflectance import Reflectance',
         'code_size': 26,
         'callout': 'For random numbers you import Python\'s built-in `random`',
         'tone': 'teal'},

        {'kind': 'code', 'title': '`random.randint(a, b)`',
         'code': 'import random\n'
                 '\n'
                 'for i in range(5):\n'
                 '    number = random.randint(1, 10)\n'
                 '    print("Random number:", number)',
         'code_size': 24, 'width': 9,
         'callout': '`random.randint(1, 10)` hands back **one** random whole number from 1 to 10, '
                    '**including** both ends. Run it again and you will (usually) get a '
                    'different number.',
         'tone': 'teal',
         'notes': 'More support: have students run just this, with no robot, so randint is '
                  'concrete before it drives anything. Computer randomness is really '
                  '"pseudo-random": deterministic underneath, but plenty random for us.'},

        {'kind': 'check',
         'question': 'What can `random.randint(1, 6)` return?',
         'options': ['Any decimal between 1 and 6',
                     'Any whole number from 1 to 6, including 1 and 6',
                     'The numbers 1 through 5 only', 'Exactly six random numbers at once'],
         'answer': 1,
         'explanation': 'randint gives one integer, and the range is inclusive: 1, 2, 3, 4, 5, '
                        'or 6 (like rolling a die).'},

        {'kind': 'check',
         'question': 'Where do import statements belong?',
         'options': ['At the very top of the file', 'Inside the while loop, so they run every pass',
                     'Right before the robot moves', 'Anywhere: it makes no difference'],
         'answer': 0,
         'explanation': 'By convention imports go at the top. You import once; the tools are '
                        'then available everywhere below.'},

        {'kind': 'bullets', 'title': 'Random bounce driving',
         'bullets': [
             'The only change from Lesson 2-3 is in the `if` branch',
             'Instead of a fixed `turn(180)`, pick a **random angle** first',
             'Then turn by **that**',
             'Nothing else in the program moves',
         ],
         'callout': 'Same loop, same `is_either_on_line()`: only the turn changes',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Add to robot.py: `test_random_bounce()`',
         'lead': '`import random` goes at the top, with the other imports. Paste the test above `RUN`.',
         'code': 'import random          # at the top of robot.py, with the other imports\n'
                 '\n'
                 'def test_random_bounce():\n'
                 '    # a copy of test_bounce(), with the if branch becoming:\n'
                 '    #     stop\n'
                 '    #     pick a random whole number of degrees, 90 to 270\n'
                 '    #     print it, so you can see each choice\n'
                 '    #     turn by that many degrees\n'
                 '    pass',
         'code_size': 18,
         'callout': 'Keep `test_bounce()` as it is: by the end of the module your file is a '
                    'record of everything the robot has learned to do',
         'tone': 'teal',
         'notes': 'Students should copy test_bounce(), not edit it. The fixed-angle bounce is '
                  'part of the record the file keeps.'},

        {'kind': 'bullets', 'title': 'Why 90 to 270, and not 0 to 360?',
         'lead': 'Each bounce picks a fresh angle, so the robot fans out and covers the whole '
                 'circle. But it has to **meaningfully** change direction:',
         'lead_h': 1.3,
         'bullets': [
             'Near **0**: it barely turns, and drifts out of the circle',
             'Near **180**: it goes straight back the way it came',
             'The band in the middle is where exploring happens',
         ],
         'split': 0.52,
         'figure': '/img/lesson-m2-04/random-bounce-run.svg',
         'frame': 0.95,
         'crop': (0.0, 0.08, 0.61, 0.92),
         'notes': 'randint(90, 270) guarantees a real change of direction. A range that '
                  'includes very small angles can send the robot back across the line it just '
                  'hit, or barely turn it, so it drifts out of the circle. The figure is the '
                  'end of the lesson\'s animated run: the paths fan out across the circle. '
                  'The lesson worksheet has a range table for step 2.'},

        {'kind': 'check',
         'question': 'Why does always turning exactly 180° cause a problem?',
         'options': ['It drains the battery faster',
                     'The robot retraces the same path back and forth and never explores the rest',
                     '180° turns are inaccurate on hardware', 'It makes the robot leave the circle'],
         'answer': 1,
         'explanation': 'A 180° turn sends the robot straight back the way it came, so it '
                        'bounces between the same two points forever. Random angles break that.'},

        {'kind': 'figure', 'title': 'What step 1 should look like',
         'figure': '/img/lesson-m2-04/random-bounce-run.svg',
         'frame': 0.64,
         'caption': 'With `randint(90, 270)`. Your angles will be different every run, '
                    'which is the point.',
         'notes': 'One moment from the lesson\'s animation: bounce 4, where randint picked 221. '
                  'The outline on the right highlights the line of the test that is running, '
                  'and the box below shows the angle each bounce picked.'},

        {'kind': 'steps', 'title': 'Step 1 · The random turn',
         'steps': [
             'Add `import random` at the top of `robot.py`',
             'Copy the body of `test_bounce()` into `test_random_bounce()`, and change the '
             '`if` branch as outlined',
             'Set the run line to `test_random_bounce()` and run it',
         ],
         'callout': 'The printed angle should differ on (almost) every bounce, and the robot '
                    'should wander the whole circle instead of pacing one line',
         'tone': 'teal'},

        {'kind': 'table', 'title': 'Step 2 · Try three ranges', 'tag': 'Activity',
         'lead': 'Run each one and write down how the robot\'s coverage of the circle changes.',
         'headers': ['Range', 'How much of the circle does it cover?'],
         'widths': [1.2, 2],
         'rows': [
             ['`randint(170, 190)`', ''],
             ['`randint(90, 270)`', ''],
             ['`randint(45, 315)`', ''],
         ],
         'size': 24,
         'callout': 'Which one explores best, and **why**?',
         'notes': 'Let students see for themselves why a mid-range band explores best: 170 to '
                  '190 is nearly the old 180 pattern, and a wide range lets in small turns. '
                  'The lesson worksheet has the same range table.'},

        {'kind': 'steps', 'title': 'Step 3 · Challenge: random speed too',
         'steps': [
             '`randint()` only gives **whole numbers**, and `set_effort()` wants a value '
             'between 0 and 1',
             'Pick a whole number in a range you choose, and **divide** it to get an effort '
             'between 0.2 and 0.5',
             'Drive at that speed until the next bounce',
         ],
         'notes': 'Step 3 is hand-in work. The division is the part students have to find: '
                  'most try randint with decimals first and get an error. More challenge: a '
                  '"dance mode" victory spin every 10th bounce, or random.choice() from a few '
                  'set angles, a nice preview of lists.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Games', 'Procedural worlds', 'Games generate endless different levels, loot, and '
                                            'maps from random numbers.'),
             ('Cleaning', 'Robot vacuums', 'Simpler vacuums use semi-random turns to eventually '
                                           'cover a whole room, just like your bounce bot.'),
             ('Science', 'Simulations', 'Weather, traffic, and epidemic models run millions of '
                                        'random trials to predict outcomes.'),
         ],
         'notes': 'Randomness is a real engineering tool, not just chaos.'},

        {'kind': 'wrapup',
         'questions': [
             'What does `import` do?',
             'What does `random.randint(1, 6)` return?',
             'Why is a random turn better than a fixed 180° here?',
         ],
         'next': 'stop bouncing off the line and start following it',
         'notes': 'Answers: brings in a module\'s tools so you can use them. One whole number, '
                  '1 to 6 inclusive. It stops the robot retracing the same path. Formative: '
                  'correct use of import random and the inclusive range of randint. Exit '
                  'ticket: "What values could random.randint(90, 270) give?" (any integer from '
                  '90 to 270). Next lesson is the big one: proportional control.'},
    ],
}
