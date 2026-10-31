DECK = {
    'module': 2, 'lesson': 6,
    'doc': 'module-02-line-tracking/lesson-06-two-sensor-following',
    'title': 'Two-Sensor Line Following',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Explain why two sensors track better than one',
             'Compute error with two sensors: `error = left − right`',
             'Predict the sign of the error from the robot\'s position',
             'Rewrite `get_error()` for two sensors and see that the loop barely changes',
             'Explain why this follower needs no minus sign in `arcade(BASE_EFFORT, correction)`',
         ],
         'notes': '50 to 60 minutes. The code gets simpler this lesson, but the idea is subtle: '
                  'the meaning of a positive error changes, so the minus sign from Lesson 2-5 '
                  'comes out. Budget real time for that.'},

        {'kind': 'bullets', 'title': 'From one edge to the center',
         'bullets': [
             'Last lesson the robot followed one **edge** of the line with a single sensor',
             'Now you use **both** sensors together, and the code actually gets simpler',
             'The robot **straddles** the line and follows its **center**',
         ],
         'callout': 'Two sensors give smoother, more reliable tracking',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'The difference is the error',
         'bullets': [
             'With two sensors straddling the line, you **don\'t need a setpoint** anymore',
             'Just subtract one reading from the other',
             'Both read the same: the difference is zero, and the robot drives straight',
             'One drifts onto the line: the difference says **how much** and **which way**',
         ],
         'callout': 'error = left − right',
         'tone': 'teal',
         'notes': 'Contrast with Lesson 2-5: there the error was SETPOINT minus one reading. '
                  'Here equal readings already mean zero, so there is nothing to aim for but '
                  'balance.'},

        {'kind': 'bullets', 'title': 'Work out the direction, don\'t memorise it',
         'bullets': [
             'A **high** reading means **that sensor** is over the line',
             'If the **left** sensor is on the line, the line is off to the robot\'s left',
             'So the **robot** has wandered to the **right** of it',
         ],
         'callout': 'The sensor that finds the line points back toward where the robot should be',
         'tone': 'orange',
         'notes': 'Have students reason it out rather than learn the table by heart. Stand at the '
                  'front and act it out: "the line is on my left, so I must be to its right."'},

        {'kind': 'table', 'title': 'Reading the two-sensor error',
         'headers': ['Position', 'left', 'right', 'error = L − R', 'Which way to steer'],
         'widths': [2.4, 1, 1, 1.8, 3.6],
         'rows': [
             ['Centered', '0.5', '0.5', '`0.0`', 'drive straight'],
             ['Drifted right', '0.8', '0.2', '`+0.6`', 'steer left, back toward the line'],
             ['Drifted left', '0.2', '0.8', '`−0.6`', 'steer right, back toward the line'],
             ['Both on white', '0.1', '0.1', '`0.0`', 'straight (lost line)'],
             ['Both on black', '0.9', '0.9', '`0.0`', 'straight (an intersection!)'],
         ],
         'callout': 'Zero error can mean centered, lost, or at a crossing line',
         'tone': 'teal',
         'notes': 'The last two rows both give zero error for very different reasons. Point at '
                  'the bottom row: both sensors on black is a crossing line, and next lesson '
                  'gets a function that detects it.'},

        {'kind': 'figure', 'title': 'Two sensors straddle the line',
         'figure': '/img/lesson-m2-06/two-sensor-error.svg',
         'caption': 'The sensor that finds the tape is on the side the line is on, so the robot '
                    'has drifted the other way, and steers back toward the high reading.'},

        {'kind': 'check',
         'question': 'The left sensor reads 0.8 and the right reads 0.2. What is the error, and '
                     'which way has the robot drifted?',
         'options': ['error +0.6, drifted right', 'error +0.6, drifted left',
                     'error 0.0, centered', 'error 1.0, at an intersection'],
         'answer': 0,
         'explanation': 'error = 0.8 − 0.2 = +0.6. The high reading is on the LEFT, so the line is '
                        'off to the robot\'s left: the robot has drifted right of the line and '
                        'needs to steer left to get back.'},

        {'kind': 'bullets', 'title': 'The payoff for a one-line function',
         'bullets': [
             '`test_follow()` reads `get_error()`, scales it, steers',
             'Switching to two sensors means **rewriting** `get_error()`',
             'The loop that calls it barely notices',
             'Two changes to `robot.py`, both **in place**',
         ],
         'callout': 'This is why the error went behind a function last lesson',
         'tone': 'teal',
         'notes': 'Say this out loud now and again after step 2: the loop did not change, only '
                  'the function did. It is the first time the course shows why a one-line '
                  'function is worth having.'},

        {'kind': 'code', 'title': 'Change 1 · The LINE SENSOR section',
         'lead': 'Replace the body of `get_error()` so it returns `get_left() - get_right()`, '
                 'and **delete** `SETPOINT`: two sensors don\'t need one.',
         'lead_h': 1.2,
         'code': 'def get_error():\n'
                 '    # return the left reading minus the right reading\n'
                 '    pass',
         'code_size': 24,
         'callout': 'Same name, new body: everything that calls `get_error()` keeps working',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Change 2 · The minus sign comes out',
         'lead': 'In `test_follow()`, the **minus sign** in front of the correction comes out.',
         'code': '# Lesson 2-5, one sensor:\n'
                 'drivetrain.arcade(BASE_EFFORT, -correction)\n'
                 '\n'
                 '# Lesson 2-6, two sensors:\n'
                 'drivetrain.arcade(BASE_EFFORT, correction)',
         'code_size': 24, 'width': 10,
         'callout': 'That\'s the only change to the loop. Why? A positive error now means something different.',
         'tone': 'orange',
         'notes': 'Do not let this slide pass as a typo fix. The next slide is the reason, and '
                  'it is the subtle point of the lesson.'},

        {'kind': 'bullets', 'title': 'Why no minus now?',
         'bullets': [
             'A **positive** error now means the robot drifted **right** of the line',
             'So it must steer **left** to get back',
             'In `arcade()`, a **positive** turn steers **left**',
             'The math already lines up with the robot, so there\'s nothing to flip',
         ],
         'callout': 'In Lesson 2-5 a positive error meant "drifted onto white, steer **right**". '
                    'The meaning of a positive error changed, so the sign changed.',
         'tone': 'orange',
         'notes': 'Spend real time here. Walk both cases: one sensor, positive error, needs a '
                  'right steer, which is a negative turn, hence the minus. Two sensors, positive '
                  'error, needs a left steer, which is already a positive turn.'},

        {'kind': 'check',
         'question': 'Why does the minus sign from Lesson 2-5 come out of `arcade()` here?',
         'options': ['The meaning of a positive error flipped, so the steer direction has to flip too',
                     'Two sensors never need a sign change', 'It makes the robot go faster',
                     'It fixes a bug in `arcade()`'],
         'answer': 0,
         'explanation': 'In Lesson 2-5 a positive error meant "drifted onto white, steer right", a '
                        'negative turn, so the correction was negated. Now a positive error means '
                        '"drifted right, steer left", already a positive turn in `arcade()`.'},

        {'kind': 'steps', 'title': 'Step 1 · Explore the error by hand',
         'steps': [
             'Rewrite `get_error()` first, and test it before anything drives',
             'Add `" Error:", round(get_error(), 2)` to the print in `test_sensors()`, and set the '
             'run line to `test_sensors()`',
             'Slide the robot across the line by hand. Watch the error go positive, then zero, then '
             'negative',
             'Say out loud which way the robot has drifted each time, and check against the table',
         ],
         'notes': 'Do not skip this step. Sliding the robot by hand while the error goes positive, '
                  'zero and negative is the physical intuition that makes the sign change click.'},

        {'kind': 'steps', 'title': 'Step 2 · Run the follower',
         'steps': [
             'Take the minus sign out of `test_follow()` and set the run line back to it',
             'Put the robot with the line running **between** the sensors, press the button, '
             'and watch it track the circle',
             'Steers **away** from the line as soon as it drifts? The sign is backwards: go back to '
             'step 1 and work out which way a positive error should steer',
         ],
         'callout': 'The loop is the same three lines it was with one sensor. The function '
                    'changed; its caller didn\'t.',
         'tone': 'teal',
         'notes': 'Expect to re-tune KP: the two-sensor error has a different range from the '
                  'one-sensor version.'},

        {'kind': 'steps', 'title': 'Step 3 · Compare with one sensor',
         'steps': [
             'Temporarily put the one-sensor `get_error()` back (and `SETPOINT`), with its minus sign',
             'Run `test_follow()` again right after. Which is smoother? Which handles the curves '
             'and higher speeds better?',
             'Restore the two-sensor version: that\'s the one the rest of the course uses',
         ]},

        {'kind': 'steps', 'title': 'Step 4 · Challenge: push the speed',
         'tag': 'Challenge',
         'steps': [
             'Turn `BASE_EFFORT` up to 0.4 to 0.5 for both versions and watch what happens to each',
             'Which one degrades first?',
             'What does that tell you about how much information one sensor gives the robot?',
         ],
         'notes': 'One sensor only knows "more white" or "more black"; it cannot tell which side '
                  'of the line it lost. Two sensors always know which way back is.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Audio', 'Stereo & hearing', 'You locate a sound from the tiny difference between '
                                           'your two ears: the same differential idea.'),
             ('Navigation', 'Differential GPS', 'Comparing two receivers cancels error and pins '
                                                'a position down to centimeters.'),
             ('Robotics', 'Sensor arrays', 'Advanced line followers use 5 to 8 sensors, but the '
                                           'principle is the one you just learned.'),
         ]},

        {'kind': 'wrapup',
         'questions': [
             'What\'s the two-sensor error formula, and why no setpoint?',
             'Positive error means the robot drifted which way?',
             'Why did the minus sign come out?',
         ],
         'next': 'finish the sensor toolkit with `is_at_cross()`',
         'notes': 'Answers: left − right, since equal readings already mean zero. Right: the left '
                  'sensor found the line, so the line is left of the robot. A positive error now '
                  'needs a left steer, already a positive turn in arcade(). Exit ticket: "Both '
                  'sensors read 0.9: what is the error, and what might it physically mean?" '
                  '(about 0; an intersection). Next lesson adds is_at_cross(), which detects '
                  'that intersection.'},
    ],
}
