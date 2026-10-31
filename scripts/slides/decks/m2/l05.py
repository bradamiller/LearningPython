DECK = {
    'module': 2, 'lesson': 5,
    'doc': 'module-02-line-tracking/lesson-05-proportional-control',
    'title': 'Proportional Control',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Explain a **setpoint**, and why the edge of the line (about 0.5) is ours',
             'Compute **error** as setpoint − reading, and read its sign',
             'Turn error into a steering **correction** with a gain, Kp',
             'Write `get_error()` and the control loop in `robot.py`',
             'Tune Kp by watching the robot',
         ],
         'notes': '60+ minutes. This is the first control loop, and the hardest shift in the '
                  'module: from "do this, then that" to "constantly read and adjust". Lean on '
                  'the car-steering analogy.'},

        {'kind': 'bullets', 'title': 'Bouncing is not following',
         'bullets': [
             'Bounce driving kept the robot inside the circle, but it **reacted after** hitting the line',
             'Following means **constantly adjusting** so you never leave it',
             'Like nudging the steering wheel around a gentle curve, instead of stopping to turn',
         ],
         'callout': 'Today: your first **control loop**, one of the most important ideas in the course',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Steer while you drive: `arcade()`',
         'lead': '`arcade(speed, turn)` sets a forward speed and a steering amount in one call, '
                 'and it does not stop the program.',
         'lead_h': 1.25,
         'bullets': [
             'A **positive** turn steers **left** (counterclockwise)',
             'A **negative** turn steers **right**',
             'Zero drives straight',
             'Same rule as Lesson 1-6\'s Arcade block',
         ],
         'split': 0.48,
         'code': 'drivetrain.arcade(speed, turn)\n'
                 '# works like:\n'
                 'drivetrain.set_effort(speed - turn,\n'
                 '                      speed + turn)\n'
                 '# then XRPLib scales both so the\n'
                 '# faster wheel gets the larger of\n'
                 '# speed and turn',
         'code_size': 17,
         'callout': '`arcade(0.3, 0.15)` slows the left wheel, speeds up the right: it curves **left**'},

        {'kind': 'check',
         'question': 'What does `arcade(0.3, -0.15)` do?',
         'options': ['Drives forward, curving right', 'Drives forward, curving left',
                     'Drives backward', 'Spins in place'],
         'answer': 0,
         'explanation': 'The speed is positive, so it drives forward. The turn is negative, so the '
                        'left wheel speeds up, the right slows down, and the robot curves right.'},

        {'kind': 'bullets', 'title': 'Setpoint and error',
         'bullets': [
             'The **setpoint** is the reading we want the sensor to hold',
             'Following the **edge** of the line, that is about `0.5`: halfway between white and black',
             '**Error** is how far off we are',
         ],
         'callout': 'error = setpoint − sensor_reading',
         'tone': 'teal',
         'notes': 'Hammer this: the setpoint is the edge (about 0.5), not white (0.0). The robot '
                  'rides the boundary. Encourage students to use their own edge value from '
                  'Lesson 2-1 rather than assuming exactly 0.5.'},

        {'kind': 'table', 'title': 'The sign says which way, the size says how far',
         'headers': ['Where the robot is', 'Reading', 'error = 0.5 − reading', 'Meaning'],
         'widths': [3, 1.4, 2.6, 3],
         'rows': [
             ['On the edge (perfect)', '0.5', '`0.0`', 'no correction'],
             ['Drifted onto white', '0.2', '`+0.3`', 'steer toward the line'],
             ['Drifted onto black', '0.8', '`−0.3`', 'steer back off the line'],
             ['Far onto white', '0.1', '`+0.4`', 'steer hard toward the line'],
         ]},

        {'kind': 'figure', 'title': 'Reading the error',
         'figure': '/img/lesson-m2-05/error-sign.svg',
         'caption': 'Positive error steers toward the line, negative steers back off it. '
                    'The sign picks the direction, so the loop needs no if/else.'},

        {'kind': 'check',
         'question': 'The setpoint is 0.5 and the sensor reads 0.2. What is the error?',
         'options': ['−0.3', '+0.3', '0.7', '0.2'],
         'answer': 1,
         'explanation': 'error = 0.5 − 0.2 = +0.3. The positive sign says the robot drifted onto '
                        'white and should steer toward the line.'},

        {'kind': 'bullets', 'title': 'From error to steering: the gain Kp',
         'bullets': [
             'We scale the error by a **proportional gain**, Kp, to set how strongly the robot reacts',
             'With Kp = 0.5, an error of +0.3 gives a correction of +0.15',
             'Bigger error → bigger correction → sharper steer',
             'Error 0 → correction 0 → drive straight',
         ],
         'callout': 'correction = error × Kp',
         'tone': 'teal',
         'notes': 'Kp breaks the lowercase naming rule on purpose: every control-systems text '
                  'writes the proportional gain as Kp. In robot.py it is a file-level setting, '
                  'so it is written in capitals, KP, like THRESHOLD.'},

        {'kind': 'code', 'title': 'Why the minus sign?',
         'lead': 'We steer with the correction, with a **minus sign** in front of it:',
         'code': 'drivetrain.arcade(BASE_EFFORT, -correction)',
         'code_size': 26, 'width': 9.5,
         'callout': 'Positive error = drifted onto white, so steer **right**. In `arcade()` a '
                    'positive turn steers **left**. The minus lines the math up with the robot.',
         'callout_size': 22,
         'notes': 'No if/else anywhere: the sign of the error does the deciding. Next lesson the '
                  'error is measured differently, and the minus sign comes out again.'},

        {'kind': 'check',
         'question': 'If Kp = 0.6 and the error is 0.3, what is the correction?',
         'options': ['0.9', '0.18', '0.3', '0.5'],
         'answer': 1,
         'explanation': 'correction = error × Kp = 0.3 × 0.6 = 0.18.'},

        {'kind': 'code', 'title': 'Add to robot.py: the LINE SENSOR section',
         'lead': '`SETPOINT` goes under `THRESHOLD`. `get_error()` goes under `get_right()`.',
         'code': 'SETPOINT = 0.5           # the reading at the edge of the line\n'
                 '\n'
                 'def get_error():\n'
                 '    # return SETPOINT minus the left reading\n'
                 '    pass',
         'code_size': 22,
         'callout': 'The error is a sensor question: how far off the edge am I?',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Add to robot.py: a new LINE TRACKING section',
         'lead': 'Paste it above `RUN`. The loop\'s outline is inside the test.',
         'code': '# ===== LINE TRACKING =====\n'
                 'BASE_EFFORT = 0.3        # forward speed while following\n'
                 'KP = 0.5                 # proportional gain -- tune this!\n'
                 '\n'
                 'def test_follow():\n'
                 '    # loop forever:\n'
                 '    #     error = get_error()\n'
                 '    #     correction = error times KP\n'
                 '    #     steer: arcade() with BASE_EFFORT and minus the correction\n'
                 '    #     time.sleep(0.01), so the loop doesn\'t flood the processor\n'
                 '    pass',
         'code_size': 18,
         'notes': 'The section comment in the lesson is longer (it says the section grows over '
                  'the module); the slide shortens it. The time.sleep(0.01) only keeps the loop '
                  'from flooding the processor.'},

        {'kind': 'steps', 'title': 'Step 1 · Write the loop and run it',
         'steps': [
             'Write `get_error()`, and turn the comments in `test_follow()` into code',
             'Set the run line to `test_follow()`. Put the left sensor on the edge of the line, press the button',
             'It should hold the edge, nudging left and right as the line curves',
         ],
         'callout': 'Drives straight off? Check the sign of your error and the minus in front of the '
                    'correction. Spins in place? Check the order of the two arguments to `arcade()`.',
         'tone': 'orange'},

        {'kind': 'steps', 'title': 'Step 2 · Tune Kp',
         'steps': [
             'Run the test with `KP = 0.2` and write down what the robot does on a curve',
             'Run it again with `KP = 0.5`, then with `KP = 1.0`',
             'Decide: which is too high, which too low, and what does each one **look** like?',
         ],
         'notes': 'There is no single right Kp: it depends on the surface, the tape and the base '
                  'speed. The goal is the relationship, not a magic number. Start everyone at '
                  'BASE_EFFORT = 0.3 or lower so the robot is observable.'},

        {'kind': 'frames', 'title': 'What too low, about right and too high look like',
         'figure': '/img/lesson-m2-05/kp-tuning-v2.svg',
         'crop': (0.0, 0.07, 0.6, 1.0),
         'frames': [(0.25, '**Too low** (KP = 0.2): drifts off the curve'),
                    (0.6, '**About right** (KP = 0.5): holds the edge'),
                    (0.95, '**Too high** (KP = 1.0): weaves and over-corrects')],
         'callout': 'No single correct number: it depends on your surface, tape and speed',
         'tone': 'teal',
         'notes': 'Show this after the class has tried all three values. The figure on the '
                  'lesson page is an animation of the three runs; these are its three end '
                  'states. Too low: the robot cannot steer hard enough for the curve. Too '
                  'high: every small error turns into a big swerve.'},

        {'kind': 'check',
         'question': 'Your robot follows the line but weaves back and forth rapidly, never '
                     'settling. What should you do to Kp?',
         'options': ['Increase it: it needs to react harder', 'Decrease it: it is over-correcting',
                     'Set it to 0', 'Leave KP and increase BASE_EFFORT instead'],
         'answer': 1,
         'explanation': 'Rapid weaving is over-correction: Kp is too high. Lower it for gentler, '
                        'smoother steering.'},

        {'kind': 'code', 'title': 'Print every 50th pass: `%`',
         'lead': 'The loop runs hundreds of times a second. `a % b` is the **remainder** after '
                 'dividing a by b (nothing to do with percent).',
         'lead_h': 1.2,
         'code': '7 % 3        # 1   (3 goes into 7 twice, remainder 1)\n'
                 '10 % 5       # 0   (5 goes into 10 exactly)\n'
                 '50 % 50      # 0\n'
                 '51 % 50      # 1\n'
                 '100 % 50     # 0\n'
                 '149 % 50     # 49\n'
                 '150 % 50     # 0',
         'code_size': 20, 'width': 9,
         'callout': '`i % 50 == 0` is true on pass 0, 50, 100 ... and false in between',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'What is `120 % 50`, and would a print inside `if i % 50 == 0:` happen on pass 120?',
         'options': ['2.4, and yes', '20, and no: 120 is not a multiple of 50', '0, and yes',
                     '70, and no'],
         'answer': 1,
         'explanation': '50 goes into 120 twice (100) with 20 left over, so 120 % 50 is 20. Only '
                        'passes whose remainder is 0 (multiples of 50) print.'},

        {'kind': 'code', 'title': 'Watch the sign flip: `test_sweep()`',
         'lead': 'No motors. Slide the robot **by hand** so the left sensor goes from white, '
                 'across the edge, onto black.',
         'lead_h': 1.2,
         'code': 'def test_sweep():\n'
                 '    # no motors: sweep the robot across the line BY HAND\n'
                 '    for i in range(500):\n'
                 '        error = get_error()\n'
                 '        correction = error * KP\n'
                 '        if i % 50 == 0:\n'
                 '            print(f"i={i}  error={error:.2f}  correction={correction:.2f}")\n'
                 '        time.sleep(0.02)',
         'code_size': 18,
         'callout': 'At the edge the error falls to zero and goes **negative**: the steering '
                    'changes direction with no if/else',
         'tone': 'green',
         'notes': 'This is the moment to make the sign flip physical: motors off, robot in hand, '
                  'the printed error crossing zero as the sensor crosses the edge. If the error '
                  'never changes sign, the sensor did not cross the edge, or SETPOINT is not '
                  'their edge value from Lesson 2-1.'},

        {'kind': 'steps', 'title': 'Step 3 · Put it in your own loop',
         'lead': 'Your loop is a `while True:`, so there is no `i`. Make your own counter:',
         'steps': [
             'Set a counter to zero **before** the loop',
             'At the end of the loop body, add one to it (`count = count + 1`, from Lesson 1-9)',
             'Print the error and correction only when the counter is a multiple of 50',
         ],
         'callout': 'Tune KP again, reading the numbers: too high shows up as a correction that '
                    'flips sign on nearly every printed line',
         'tone': 'teal'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Cars', 'Cruise control', 'The further you are below the set speed, the harder it '
                                        'presses the throttle: error × gain.'),
             ('Flight', 'Drone stabilization', 'Drones hold level by constantly correcting in '
                                               'proportion to how far they have tilted.'),
             ('Driving', 'Lane-keeping', 'Lane assist steers in proportion to how far the car has '
                                         'drifted from center.'),
         ]},

        {'kind': 'wrapup',
         'questions': [
             'What is the setpoint for edge-following, and why?',
             'What do the sign and the size of the error each tell you?',
             'The robot oscillates. Is Kp too high or too low?',
         ],
         'next': 'two sensors, a simpler error, smoother tracking',
         'notes': 'Answers: about 0.5, the boundary between white and black. Sign = which way to '
                  'steer, size = how hard. Too high: decrease it. Exit ticket: "setpoint 0.5, '
                  'sensor 0.2: error and steer direction?" (+0.3, toward the line).'},
    ],
}
