DECK = {
    'module': 2, 'lesson': 2,
    'doc': 'module-02-line-tracking/lesson-02-drive-to-the-edge',
    'title': 'Drive to the Edge and Stop',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Write a `while` loop that repeats until a condition changes, and say how it differs from `for`',
             'Use comparison operators (`<`, `>`, `==`, `!=`, `<=`, `>=`)',
             'Drive the robot with `set_effort()` while checking a sensor each pass',
             'Write a drive-until-the-line test from a comment outline, in your `robot.py`',
             'Explain why the sensor must be re-read **inside** the loop',
         ],
         'notes': '50 to 60 minutes. The lesson has six objectives; the slide folds "how while '
                  'differs from for" into the first line. Expect a third of the room to write the '
                  'infinite loop on the first try: that is the lesson, and the infinite-loop '
                  'section comes after the activity on purpose.'},

        {'kind': 'bullets', 'title': 'Drive and watch at the same time',
         'bullets': [
             'Last lesson the robot read the sensor but sat still',
             'Today it rolls forward **until the sensor spots the line**, then stops',
             'The tool that makes this possible: the `while` **loop**',
         ],
         'callout': 'How do you repeat "drive and check" without knowing how many times?',
         'tone': 'teal',
         'notes': 'Take a couple of answers to the callout question before the next slide.'},

        {'kind': 'bullets', 'title': '`for` vs. `while`',
         'bullets': [
             'In Module 1 `for` repeated a **fixed** number of times: `for i in range(4)` draws '
             'four sides',
             '"Drive until you hit the line" has **no fixed count**: you don\'t know how many '
             'steps it will take',
             '`while` repeats **as long as a condition stays true**',
         ],
         'callout': 'A `while` loop repeats until a condition changes, however long that takes',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'A `while` loop',
         'lead': 'It keeps going while the sensor is on white:',
         'code': 'while left < THRESHOLD:\n'
                 '    # this runs over and over while the sensor is on white\n'
                 '    # the moment left >= THRESHOLD, the loop stops',
         'code_size': 22,
         'callout': 'The condition is checked before every pass. The first time it is `False`, the loop ends',
         'tone': 'teal',
         'notes': 'Same shape as a for loop: a colon after the condition, an indented body. The body here is only comments; '
                  'students write the real body in the activity.'},

        {'kind': 'code', 'title': 'Conditions: comparison operators',
         'lead': 'A `while` loop needs a **condition**: a test that is either `True` or `False`.',
         'code': '0.3 < 0.5    # True  (less than)\n'
                 '0.8 > 0.5    # True  (greater than)\n'
                 '0.5 == 0.5   # True  (equal to)\n'
                 '0.9 != 0.5   # True  (not equal to)',
         'code_size': 26,
         'callout': 'Two more: `<=` (less than or equal to) and `>=` (greater than or equal to)',
         'tone': 'teal',
         'notes': 'Point out that == is a comparison, not the = that stores a value. The lesson '
                  'lists <= and >= among the operators in its objectives.'},

        {'kind': 'check',
         'question': 'Which loop fits the task "drive until the robot detects a line"?',
         'options': ['A `for` loop: you know it takes exactly 4 steps',
                     'A `while` loop: you repeat until a condition changes, however long that takes',
                     'Neither: you cannot loop with sensors',
                     'Both work exactly the same here'],
         'answer': 1,
         'explanation': 'You don\'t know the number of steps in advance, so you loop while the '
                        'sensor says "no line": that\'s a while loop.'},

        {'kind': 'bullets', 'title': 'Driving inside a loop: `set_effort()`',
         'bullets': [
             '`straight()` and `turn()` **block**: they finish their distance before the next '
             'line runs, so you can\'t watch a sensor while they\'re going',
             '`set_effort(left, right)` sets the motor power and **returns immediately**',
             'The robot keeps rolling while your program goes on, so a loop can drive **and** '
             'check a sensor on every pass',
             'The motors stay on until something changes them: `drivetrain.stop()` turns them off',
         ],
         'callout': '`drivetrain.set_effort(0.3, 0.3)`: both motors at 30%, and come straight back',
         'tone': 'orange',
         'notes': 'Worth stating outright: straight() blocks, set_effort() returns instantly, '
                  'which is exactly what a sensor loop needs. Keep the speed low (0.3 or less): '
                  'at higher speeds momentum carries the robot past the line before it can stop.'},

        {'kind': 'code', 'title': 'Add to robot.py: `THRESHOLD`',
         'lead': 'The threshold you picked last lesson becomes a **setting** in the LINE SENSOR '
                 'section: right under the section\'s comment, above `get_left()`.',
         'lead_h': 1.25,
         'code': 'THRESHOLD = 0.5          # use YOUR value from Lesson 2-1',
         'code_size': 24,
         'callout': 'Capitals mean **this is a setting**, not a value that changes while the '
                    'program runs. Python doesn\'t enforce that; readers rely on it.',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Add to robot.py: `test_drive_to_line()`',
         'lead': 'Paste it above `RUN`. This time the test **is** the exercise: the outline is '
                 'inside it, and you write the body.',
         'code': 'def test_drive_to_line():\n'
                 '    # read the left sensor into a variable\n'
                 '    # while that reading says "white":\n'
                 '    #     drive forward\n'
                 '    #     read the sensor again\n'
                 '    # stop the motors\n'
                 '    # print the reading that ended the loop\n'
                 '    pass',
         'code_size': 20,
         'callout': 'You know everything it needs: `get_left()`, `THRESHOLD`, a `while` loop, and '
                    'driving inside one',
         'tone': 'teal',
         'notes': 'This lesson used to hand students the whole program. Now the setup is the file '
                  'they already have and the loop is theirs, because they have every piece by '
                  'this point. Do not show a finished body; the lesson page has a reveal for '
                  'checking after they run it.'},

        {'kind': 'frames', 'title': 'What step 1 should look like',
         'figure': '/img/lesson-m2-02/drive-to-line.svg',
         'frames': [(0.05, 'On white: **True**, the loop goes round again'),
                    (0.25, 'On the tape (`0.84`): **False**, the loop ends')],
         'callout': 'The loop checks the reading before every pass, and the first reading on the '
                    'tape ends it',
         'tone': 'teal',
         'notes': 'The figure on the lesson page is an animation; these are two moments of the '
                  'first run. In the animation the robot is then put back in the middle pointing '
                  'at a different part of the edge, and it stops at the line there too.'},

        {'kind': 'steps', 'title': 'Step 1 · Write it and run it',
         'steps': [
             'Turn the comments into code and set the run line to `test_drive_to_line()`',
             'Start the robot inside the taped circle, pointing at an edge, and press the button',
             'Watch it stop at the line',
         ],
         'callout': 'Stops as soon as you press the button? The sensor already read "black": '
                    'check your threshold. Never stops? Read on.',
         'tone': 'orange',
         'notes': 'More support: start with a non-robot counting loop (count = 0, while count < 5) '
                  'so the loop mechanics are clear before sensors enter, and give the first line '
                  'of the body. Use effort 0.2 so there is time to observe. More challenge: count '
                  'the loop passes before the line is found, or flash the LED on detection.'},

        {'kind': 'steps', 'title': 'Step 2 · Either sensor',
         'steps': [
             'Switch to `get_right()` and make sure it still works',
             'Make the loop keep going only while **both** sensors are still on white, so the '
             'robot stops when **either** one hits the line',
             'You\'ll need `and` between two conditions, and a second sensor read inside the loop',
         ],
         'callout': 'More on `and` and `or` next lesson',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Step 3 · Tidy it',
         'tag': 'Activity',
         'lead': 'Once step 2 works, try reading the sensors **in the condition itself**:',
         'code': 'while get_left() < THRESHOLD and get_right() < THRESHOLD:',
         'code_size': 24,
         'callout': 'No variable to remember to update: the sensors are read fresh every time the '
                    'condition is checked. The body shrinks to one line, and the two reads before '
                    'the loop go away.',
         'tone': 'green',
         'notes': 'Most sensor loops in this course are written this way. The variable version '
                  '(step 1) is the one that can fall into the trap, which is why students write '
                  'it first; the condition-read version is where they end up.'},

        {'kind': 'bullets', 'title': 'The infinite-loop trap',
         'bullets': [
             'Did your robot drive forever in step 1? Your loop is missing its most important line',
             'The sensor is read once **before** the loop and never again',
             'So the variable in the condition never changes, the condition never becomes false, '
             'and the robot drives until you catch it',
             'The most common bug in every sensor program you\'ll ever write',
         ],
         'callout': '**The rule:** always update the variable your `while` loop is checking, inside '
                    'the loop, or put the sensor call in the condition',
         'tone': 'orange',
         'notes': 'Read this section after it has happened in the room, not before. Students who '
                  'hit it remember it.'},

        {'kind': 'check',
         'question': 'A student\'s robot drives forward and never stops, even over the line. '
                     'What did they most likely forget?',
         'options': ['The `board.wait_for_button()` line',
                     'To re-read the sensor inside the loop, so the condition never changes',
                     'To import the drivetrain',
                     'To charge the battery'],
         'answer': 1,
         'explanation': 'Without updating left inside the loop, the condition stays true forever: '
                        'a classic infinite loop.'},

        {'kind': 'check',
         'question': '`THRESHOLD` is 0.5 and the sensor reads 0.3. Is `left < THRESHOLD` True or '
                     'False?',
         'options': ['True: 0.3 is less than 0.5', 'False: 0.3 is greater than 0.5',
                     'True: they are equal', 'It causes an error'],
         'answer': 0,
         'explanation': '0.3 < 0.5 is True, so the loop keeps running: the robot is still on white '
                        'and should keep driving.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Home', 'Thermostats', 'The furnace runs **while** the room is below the set '
                                     'temperature, then stops: a while loop in hardware.'),
             ('Software', 'Downloads', 'A download loops "grab the next chunk" while there\'s more '
                                       'file left to fetch.'),
             ('Games', 'Game loops', 'A game repeats "update and draw" while the game is still '
                                     'running.'),
         ]},

        {'kind': 'wrapup',
         'questions': [
             'When do you reach for `while` instead of `for`?',
             'What\'s the one line you must never forget in a sensor `while` loop?',
             'What does `set_effort()` do that `straight()` can\'t?',
         ],
         'next': 'add `if/else` so the robot turns around at the line: bounce driving',
         'notes': 'Answers: when you repeat until a condition changes, not a fixed count. '
                  'Re-reading the sensor inside the loop. It runs the motors without blocking, so '
                  'the loop can keep checking. Formative: correct while syntax, and explaining the '
                  'infinite-loop trap. Exit ticket: "What happens if you don\'t update the sensor '
                  'inside the loop?" (an infinite loop).'},
    ],
}
