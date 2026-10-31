DECK = {
    'module': 2, 'lesson': 3,
    'doc': 'module-02-line-tracking/lesson-03-bounce-driving',
    'title': 'Bounce Driving',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Write `if/else` statements that choose between two actions',
             'Combine `while True`, `if/else` and a sensor read for continuous decisions',
             'Use `and`, `or` and `not`, and write `is_either_on_line()` around the `or`',
             'Write the bounce as a test function in `robot.py`, from a pseudocode outline',
         ],
         'notes': '50 to 60 minutes. The new idea is the decision: the robot checks the sensor '
                  'every moment and picks one of two actions. Everything else (the sensor read, '
                  'the threshold, the drive commands) students already have from Lessons 2-1 '
                  'and 2-2.'},

        {'kind': 'bullets', 'title': 'From stopping to bouncing',
         'bullets': [
             'Lesson 2-2: drive to the line, **stop**, done',
             'Today: keep going, bouncing off each edge like a ball in a box',
             'That needs a **decision** every moment: **if** I see the line, turn around; '
             '**otherwise**, keep driving',
         ],
         'callout': 'The tool for that decision is the `if/else` statement',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Making a decision with `if/else`',
         'lead': 'An `if/else` runs one block when a condition is true and a different block '
                 'when it is false.',
         'lead_h': 1.25,
         'bullets': [
             'The condition is checked once',
             '**True**: the `if` block runs',
             '**False**: the `else` block runs',
             'Never both',
         ],
         'split': 0.5,
         'code': 'if condition:\n'
                 '    # runs when the condition is True\n'
                 'else:\n'
                 '    # runs when the condition is False',
         'code_size': 18,
         'callout': 'Indentation shows which lines belong to which block, the same as in a loop',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'A non-robot example',
         'lead': 'The shape is easiest to see away from the robot:',
         'code': 'temperature = 85\n'
                 'if temperature > 80:\n'
                 '    print("It\'s hot outside!")\n'
                 'else:\n'
                 '    print("It\'s comfortable.")',
         'code_size': 24, 'width': 8.5,
         'callout': '`85 > 80` is True, so only the first print runs. Change the temperature to '
                    '70 and only the second one does.',
         'notes': 'Ask the class to predict the output before revealing it, then change the '
                  'number to 70 and predict again. Also ask what happens at exactly 80 (False, '
                  'so "It\'s comfortable.").'},

        {'kind': 'check',
         'question': 'When an if/else runs, how many of the two blocks execute?',
         'options': ['Both, top to bottom', 'Exactly one: whichever matches the condition',
                     'Neither, unless you call them', 'It depends on the sensor'],
         'answer': 1,
         'explanation': 'An if/else always runs exactly one branch: the if-block when the '
                        'condition is True, the else-block when it is False.'},

        {'kind': 'code', 'title': 'The bounce algorithm',
         'lead': 'The behavior in plain English:',
         'code': 'loop forever:\n'
                 '    read the sensor\n'
                 '    if the sensor sees the line:\n'
                 '        stop, then turn around\n'
                 '    else:\n'
                 '        keep driving forward',
         'code_size': 24, 'width': 8.5,
         'callout': '"Loop forever" is `while True:`',
         'tone': 'teal',
         'notes': 'Walk the loop by hand with a student as the robot: read, decide, act, '
                  'repeat. The decision happens on every pass, many times a second.'},

        {'kind': 'bullets', 'title': '`while True:` loops forever',
         'bullets': [
             'Its condition is `True`, which is always true',
             'So it runs until you power the robot off or stop it',
             'That is completely normal in robotics',
             'Real robots run a loop like this the whole time they are on',
         ],
         'callout': 'Read the sensor, decide, act, and go round again',
         'tone': 'teal',
         'notes': 'Students sometimes think while True will crash the program. Reassure them it '
                  'is the standard control-loop pattern, and the way out is the robot\'s stop '
                  'button or power. The drivetrain.stop() before the turn just makes a cleaner '
                  'pivot. On real hardware the 180 degrees will not be exact: that is expected, '
                  'and Lesson 2-4 turns it into a feature.'},

        {'kind': 'check',
         'question': 'What does `while True:` do?',
         'options': ['Runs the loop once',
                     'Loops forever, until the robot is powered off or stopped',
                     'Causes a syntax error', 'Runs the loop only if a sensor is True'],
         'answer': 1,
         'explanation': 'The condition True is always true, so the loop repeats endlessly: the '
                        'standard pattern for continuous robot control.'},

        {'kind': 'bullets', 'title': 'Combining conditions',
         'bullets': [
             'One sensor can **miss** the line if the robot hits it at an angle',
             'Checking **both** sensors is safer',
             '`or` is true if **either** side is true',
         ],
         'callout': '`get_left() > THRESHOLD or get_right() > THRESHOLD` means '
                    '**at least one sensor sees the line**',
         'tone': 'teal'},

        {'kind': 'table', 'title': 'The three logical operators',
         'headers': ['Operator', 'True when', 'Where you see it'],
         'widths': [1.4, 3.2, 3.6],
         'rows': [
             ['`and`', 'both sides are true', 'Lesson 2-2'],
             ['`or`', 'at least one side is true', 'today: either sensor on the line'],
             ['`not`', 'flips True to False, False to True', 'whenever you need the opposite'],
         ],
         'callout': '`and` needs both. `or` needs only one.',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'The function that asks',
         'lead': 'Its name: `is_either_on_line()`',
         'lead_h': 0.75,
         'bullets': [
             'The `or` question, **is either sensor on a line?**, gets asked by this bounce, next '
             'lesson\'s random bounce, and the turns in Lesson 2-9',
             'So it becomes the next function in your **LINE SENSOR** section',
             'It returns `True` or `False`: a **Boolean** is a value like any other, and '
             '`return` hands one back just as it handed back a number in Lesson 1-11',
             'The name starts with `is_` because it answers a **yes/no** question',
         ],
         'size': 24,
         'notes': 'The is_ naming convention shows up in every function like it from here on. '
                  'Point out that returning True or False is no different from returning a '
                  'number: the caller uses the answer, here as an if condition.'},

        {'kind': 'check',
         'question': 'left is 0.2 and right is 0.9 (THRESHOLD 0.5). Is '
                     '`left > THRESHOLD or right > THRESHOLD` True?',
         'options': ['False: the left sensor is on white',
                     'True: the right sensor is over the line, and or needs only one side',
                     'False: you need both sensors on the line', 'It causes an error'],
         'answer': 1,
         'explanation': 'or is true when at least one side is true. Right (0.9 > 0.5) is true, '
                        'so the whole condition is true: bounce.'},

        {'kind': 'code', 'title': 'Add to robot.py: the LINE SENSOR section',
         'lead': '`is_either_on_line()` goes under `get_right()`.',
         'code': 'def is_either_on_line():\n'
                 '    # return True when AT LEAST ONE reading is above THRESHOLD\n'
                 '    pass',
         'code_size': 22,
         'callout': 'A sensor question with a yes/no answer, so it lives with the sensor functions',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Add to robot.py: `test_bounce()`',
         'lead': 'Paste it above `RUN`. The pseudocode is inside it as comments.',
         'code': 'def test_bounce():\n'
                 '    # loop forever:\n'
                 '    #     if the left sensor sees the line:\n'
                 '    #         stop, print a message, turn around\n'
                 '    #     else:\n'
                 '    #         drive forward\n'
                 '    pass',
         'code_size': 22,
         'notes': 'The test is the exercise: students turn each comment into a line of code. '
                  'Step 1 uses the left sensor only; step 2 swaps in is_either_on_line().'},

        {'kind': 'figure', 'title': 'What step 1 should look like',
         'figure': '/img/lesson-m2-03/bounce-run.svg',
         'frame': 0.18,
         'caption': 'Every bounce is exactly 180 degrees, so the robot paces one line. '
                    'Lesson 2-4 fixes that.',
         'notes': 'The lesson page shows this as an animation of the whole run; this is the '
                  'moment of the first bounce. The outline on the right highlights the line of '
                  'the test that is running: while the sensor reads white (about 0.20) the else '
                  'branch drives forward, and when it reads the tape (0.84) the if branch stops '
                  'and turns 180.'},

        {'kind': 'steps', 'title': 'Step 1 · One sensor',
         'steps': [
             'Turn the comments in `test_bounce()` into code, with `get_left() > THRESHOLD` as '
             'the condition',
             'Set the run line to `test_bounce()`. Start the robot inside the circle and press '
             'the button',
             'Watch it bounce back and forth',
         ],
         'callout': 'Drives through the line? Check which way your comparison points: the sensor '
                    'reads **high** on the line.',
         'notes': 'More support: start with just an if (stop on the line) before adding the else '
                  'and the turn. More challenge: try turn(90) and observe, or add an elif for a '
                  'third case.'},

        {'kind': 'steps', 'title': 'Step 2 · Either sensor',
         'steps': [
             'Write the body of `is_either_on_line()`',
             'Check it first: add `" On line:", is_either_on_line()` to the print in '
             '`test_sensors()`, run that, and slide the robot by hand',
             'Then change the condition in `test_bounce()` to call it',
         ],
         'callout': '`True` with either sensor on tape, `False` with both off. Then the robot '
                    'bounces whichever sensor hits first.',
         'tone': 'teal',
         'notes': 'Insist on the hand test before the robot drives: it separates a wrong '
                  'function from a wrong loop.'},

        {'kind': 'steps', 'title': 'Step 3 · Challenge: count the bounces',
         'steps': [
             'Add a `bounce_count` variable that goes up by one each bounce',
             'Print it, so you can watch the count climb',
         ],
         'callout': 'You will build on counters like this later',
         'tone': 'teal',
         'notes': 'Step 3 is hand-in work. The counter pattern is the one from Lesson 1-9.'},

        {'kind': 'frames', 'title': 'Notice anything?',
         'figure': '/img/lesson-m2-03/bounce-run.svg',
         'crop': (0.0, 0.08, 0.61, 0.95),
         'frames': [(0.18, 'Bounce 1'), (0.36, 'Bounce 2'), (0.64, 'Bounce 3')],
         'callout': 'It bounces between the **same two points** and never explores the rest of '
                    'the circle',
         'tone': 'orange',
         'notes': 'Plant the seed for Lesson 2-4: that predictability is the problem randomness '
                  'will fix next. Ask the class what would make it cover the whole circle.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Driving', 'Self-driving cars', '"If an obstacle is ahead, brake; otherwise keep '
                                              'going": millions of these checks per second.'),
             ('Safety', 'Smoke alarms', 'If smoke is over the threshold, sound the alarm; '
                                        'else stay quiet.'),
             ('Apps', 'Form validation', 'If the password is too short, show an error; '
                                         'otherwise let you continue.'),
         ],
         'notes': 'if/else decisions are the backbone of anything that reacts.'},

        {'kind': 'wrapup',
         'questions': [
             'How many branches of an `if/else` run each time?',
             'What does `while True` mean, and how do you stop it?',
             'What is the difference between `and` and `or`?',
         ],
         'next': 'random turns, so the robot explores the whole circle',
         'notes': 'Answers: exactly one. Loop forever; stop the robot. and needs both true, or '
                  'needs at least one. Formative: correct if/else syntax, knowing only one '
                  'branch runs, reading and/or. Exit ticket: "What happens if you remove '
                  'drivetrain.stop() before the turn?" (a sloppier pivot; the motors were still '
                  'driving).'},
    ],
}
