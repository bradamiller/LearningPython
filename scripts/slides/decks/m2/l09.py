DECK = {
    'module': 2, 'lesson': 9,
    'doc': 'module-02-line-tracking/lesson-09-line-tracking-functions',
    'title': 'Line-Tracking Functions',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Say what **ends** each of the three driving functions, and why none of them is a timer',
             'Write `turn_clockwise()` and `turn_counterclockwise()` as **sensor-ended** turns: a blind start, then spin until `is_either_on_line()`',
             'Drive a follow, turn, follow course with **three function calls**, from a test function in your one file',
         ],
         'notes': '60 minutes. This lesson finishes the driving toolkit. The rule to say out loud: '
                  'nothing here stops because a clock ran out. The names learned today are used '
                  'through Module 5.'},

        {'kind': 'bullets', 'title': 'Finish the driving toolkit',
         'bullets': [
             'Last lesson the robot followed the line to a cross and stopped with its **center on it**',
             'Today: two turns that **spin on the cross** until a sensor finds the next line',
             'Built on the five sensor functions from Lesson 2-7, written one at a time, each tested before the next',
         ],
         'callout': 'With `track_to_intersection()`, that\'s three driving functions. They drive every '
                    'robot program for the rest of the course.',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Add to robot.py: one setting, two outlines',
         'code': 'TURN_EFFORT = 0.25       # spin speed during a turn\n'
                 '\n'
                 'def turn_clockwise():\n'
                 '    # 1. blind turn, about 60 deg: get BOTH sensors off this line\n'
                 '    # 2. keep spinning in place (no forward speed, only turn)\n'
                 '    # 3. wait until a sensor sees a line\n'
                 '    # 4. stop\n'
                 '    pass\n'
                 '\n'
                 'def turn_counterclockwise():\n'
                 '    # the mirror image: same four moves, opposite direction\n'
                 '    pass',
         'code_size': 15,
         'notes': 'Paste the whole skeleton above RUN, at the end of the LINE TRACKING section. It '
                  'opens with a section comment: track_to_intersection() stops with the robot\'s '
                  'center on the cross, and the two turns spin there until a LINE SENSOR function '
                  'sees the next line, so no turn depends on a timer. The slide leaves that comment '
                  'out to fit; the tests are on the next slide and on the Step 4 slide.'},

        {'kind': 'code', 'title': 'Add to robot.py: the tests',
         'lead': 'Also in the skeleton, under the outlines (`test_course()` comes in Step 4). One more '
                 'change, in the LINE TRACKING settings: raise `BASE_EFFORT` to **0.4**.',
         'lead_h': 1.15,
         'code': 'def test_turn():\n'
                 '    # follow to the cross, then turn until a sensor finds a\n'
                 '    # line: on the circle, that is all the way around\n'
                 '    track_to_intersection()\n'
                 '    turn_clockwise()',
         'code_size': 18,
         'notes': 'BASE_EFFORT goes up because the steering is now tuned and the robot can go a little '
                  'faster. If a robot weaves at 0.4, drop it back (Step 1 checks this).'},

        {'kind': 'table', 'title': 'Three functions, and what ends each one',
         'lead': 'For each: what it does, and what makes it **stop**. The design is the lesson; the typing is yours.',
         'headers': ['Function', 'What it does', 'What ends it'],
         'widths': [3.6, 4.2, 2.2],
         'rows': [
             ['`track_to_intersection()`', 'follows the line, then puts its center on the cross (you have it)', 'a **cross**, then a **distance**'],
             ['`turn_clockwise()`', 'spins until a sensor finds a line', 'a **line**'],
             ['`turn_counterclockwise()`', 'the mirror image', 'a **line**'],
         ],
         'size': 20,
         'callout': 'Each one ends on something the robot can **sense** or measure. None is a timer.',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'The one you have: following the line',
         'bullets': [
             '`track_to_intersection()` is the control loop with `is_at_cross()` as the **exit condition**',
             'Until you\'re at a cross, steer toward the line; then stop',
             'All the sensor arithmetic is behind `get_error()` and `is_at_cross()`',
             'Nothing in the function reads the hardware directly',
         ],
         'callout': 'Its loop ends on a **cross**, and a measured 8.75 cm puts the robot\'s center on '
                    'it. The two turns also end on something the robot can sense.',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Turning until a sensor says stop',
         'bullets': [
             'How far should a turn go?',
             ['On the grid in Module 3: a **quarter turn**, onto the cross street',
              'On your circle the cross is too short for the sensors to touch while the robot spins, '
              'so the next line is the **circle behind**: all the way around'],
             'You could time either one, and it would be right **until the battery dropped**',
             'Instead, turn until the sensors **find the next line**, wherever it is',
         ],
         'callout': '`turn_counterclockwise()` is the mirror image: swap the sign on **both** the blind '
                    'turn and the spin',
         'tone': 'teal'},

        {'kind': 'figure', 'title': 'The four moves of turn_clockwise()',
         'figure': '/img/lesson-m2-09/sensor-ended-turn.svg',
         'crop': (0.0, 0.0, 1.0, 0.665),
         'caption': 'Drawn on a grid intersection. On your circle the same four moves carry on round '
                    'to the circle behind. A sensor, not a clock, ends the turn.',
         'notes': 'Walk the four panels in order: the blind turn clears the old line, the motors '
                  'stay on while the program goes on, is_either_on_line() becomes True, stop.'},

        {'kind': 'bullets', 'title': 'Why a blind turn, and why pass?',
         'bullets': [
             'The turn starts with the sensors **on** the line: without the blind turn, `is_either_on_line()` is already `True` and the wait ends before the robot moves',
             'Move 2 is `arcade()` with **no forward speed**, only a turn value',
             'The waiting loop has nothing to do: the motors are already running. Python needs something in the body, so you write `pass`',
         ],
         'split': 0.5,
         'code': 'def turn_clockwise():\n'
                 '    # 1. blind turn, about 60 deg:\n'
                 '    #    get BOTH sensors off this line\n'
                 '    # 2. keep spinning in place\n'
                 '    #    (no forward speed, only turn)\n'
                 '    # 3. wait until a sensor sees a line\n'
                 '    # 4. stop\n'
                 '    pass',
         'code_size': 16,
         'notes': 'pass is the same word as in the outlines, with the same meaning: nothing to do '
                  'here. The outline comments are wrapped onto two lines on this slide to fit.'},

        {'kind': 'figure', 'title': 'Why 60° and not 90°?',
         'figure': '/img/lesson-m2-09/sensor-ended-turn.svg',
         'crop': (0.0, 0.665, 1.0, 1.0),
         'caption': 'The sensor finishes the turn, so the blind part only has to **clear the old line**. '
                    'Too small: the wait ends at once. Too big: the sensors swing past the new line.',
         'notes': 'The bottom row of the lesson figure. Not so little that a sensor is still on the old '
                  'line, not so much that the sensors swing past the new one. The two functions are '
                  'mirror images: swap the sign on both the blind turn and the spin, and the direction '
                  'swaps.'},

        {'kind': 'check',
         'question': 'Why does `turn_clockwise()` start with a blind 60-degree turn before the while loop?',
         'options': ['To make the turn faster',
                     'Both sensors start on the old line, so `is_either_on_line()` is already `True`',
                     'Because 60 + 30 = 90',
                     'To recharge the battery'],
         'answer': 1,
         'explanation': 'The sensor-ended loop needs a moment when neither sensor is on tape. The blind '
                        'turn provides it; the loop then finishes the turn on the next line it finds.'},

        {'kind': 'check',
         'question': 'What does `pass` do inside the while loop?',
         'options': ['Skips the turn',
                     'Nothing: a placeholder; the loop re-checks `is_either_on_line()` while the motors run',
                     'Pauses the program',
                     'Passes the robot to the next line'],
         'answer': 1,
         'explanation': '`pass` is a do-nothing statement. The motors were already told to spin; the '
                        'loop\'s body has nothing to add, and Python needs something there.'},

        {'kind': 'steps', 'title': 'Step 1 · track_to_intersection(), at the new speed',
         'lead': 'Every step: robot on the circle-with-cross, pointed along the circle. The run block waits for the button.',
         'steps': [
             'Nothing to write, but the speed went up: set the run call to `test_track()`',
             'It should follow the line and stop with its **center on the cross**',
             'If it weaves at the new speed, drop `BASE_EFFORT` back to 0.3',
         ],
         'callout': 'Don\'t go on until the function you\'re building on works',
         'tone': 'orange',
         'notes': 'Expect the class to spread out: some pairs will be tuning a turn while others are '
                  'still on the first follow. Nothing in one pair\'s step depends on a neighbor\'s. The '
                  'cross must be clearly perpendicular to the circle and short, about 10 cm: long '
                  'enough for both sensors at once, short enough that they swing clear when the '
                  'robot spins on it.'},

        {'kind': 'steps', 'title': 'Step 2 · turn_clockwise()',
         'steps': [
             'Write the four moves, with `TURN_EFFORT` at 0.25 to start, and run `test_turn()`',
             'Watch the blind part: it should carry **both sensors clear** of the circle',
             'Then the spin carries on until a sensor meets the circle again, the robot **facing back** the way it came',
         ],
         'notes': 'The check on the lesson page is a closed reveal; students write and test both '
                  'functions before opening it. If theirs differs and still works, they keep it; if '
                  'it differs and does not, compare the two signs in each turn first.'},

        {'kind': 'table', 'title': 'Step 2 · Two things to fix',
         'headers': ['What you see', 'Why', 'Fix'],
         'widths': [3.6, 4.2, 2.4],
         'rows': [
             ['The turn **stops at once**, barely moving',
              'The blind part was too small: a sensor was still on the old line', 'Increase the 60°'],
             ['The turn stops **a quarter of the way round**, facing along the cross',
              'The cross is too long: the sensors found it during the spin', 'Trim it to about 10 cm'],
         ],
         'size': 22},

        {'kind': 'steps', 'title': 'Step 3 · turn_counterclockwise()',
         'steps': [
             'Mirror step 2: same four moves, **both signs flipped**',
             'Change `test_turn()` to call it instead, and run it from the cross',
             'Confirm it also turns all the way around, this time **the other way**',
         ]},

        {'kind': 'code', 'title': 'Step 4 · Three lines to drive a course',
         'lead': 'With all three working, run `test_course()`. The part that actually **drives** is three calls.',
         'code': 'def test_course():\n'
                 '    # follow, turn around, follow the circle back to the\n'
                 '    # cross: the whole lesson in three calls\n'
                 '    track_to_intersection()\n'
                 '    turn_clockwise()\n'
                 '    track_to_intersection()\n'
                 '    print("Done!")',
         'code_size': 20,
         'callout': 'All the sensor reading and motor control lives in the sections above. Compare it '
                    'to the wall of code this was back in Lesson 2-6.',
         'tone': 'green'},

        {'kind': 'bullets', 'title': 'Challenge: turn_around()',
         'bullets': [
             'Add `turn_around()` to the section, and a `test_turn_around()` for it',
             'On your circle its body is **one call**: `turn_clockwise()` already ends facing back the way it came',
             'Why write a function for one call?',
             ['The **name** says what you mean',
              'On a grid, turning around takes two calls: `turn_around()` is the one place that would change'],
         ],
         'notes': 'More support: give the finished sensor toolkit and have students write only the '
                  'two turns. More challenge: a '
                  'timeout so a turn that never finds a line gives up (count loop passes, not '
                  'seconds), or a track_for_distance() using the drivetrain encoders rather than a '
                  'timer.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Robots', 'Skill stacks', '\nPerception feeds motion feeds planning: each layer built on '
                                        'the one below, as driving is built on sensing.'),
             ('Cars', 'Sensor-ended actions', '\nParking assist stops when the sensors say the space '
                                              'is reached, not after a set number of seconds.'),
             ('Software', 'Libraries on libraries', '\nAlmost every library is built on another one, '
                                                    'calling its functions rather than re-reading the hardware.'),
         ],
         'height': 4.0,
         'notes': 'Layered toolkits are how robot software is organized.'},

        {'kind': 'wrapup',
         'questions': [
             'What ends each of the three driving functions?',
             'Why the blind 60° at the start of a turn?',
         ],
         'next': 'the final project: lap the circle, reversing at the cross',
         'notes': 'Answers: a cross and then a distance, a line, a line. To get the sensors off the '
                  'old line so the loop can end on the new one. Exit ticket: "Write '
                  'track_and_turn_clockwise() that follows to a cross and turns."'},

        {'kind': 'bullets', 'title': 'Optional: the LineTrack class',
         'tag': 'Optional extension',
         'bullets': [
             'Built `LineSensor` in Lesson 2-7? The driving toolkit can become a class too',
             'A car **has an** engine. `LineTrack` **has a** `LineSensor` and **has a** drivetrain, and coordinates them: **composition**',
             'Same three methods, same names, with `tracker.` in front',
             '**From here on, use your class.** Lesson 3-1 says `track_to_intersection()`: you write `tracker.track_to_intersection()`',
         ],
         'split': 0.55,
         'code': 'tracker = LineTrack()\n'
                 '\n'
                 'tracker.track_to_intersection()\n'
                 'tracker.turn_clockwise()\n'
                 'tracker.track_to_intersection()',
         'code_size': 16,
         'notes': 'Optional extension, for students who built the LineSensor class. The lessons ahead '
                  'are written with the function names; class-track students use the same names with '
                  'tracker. in front. LineTrack makes the LineSensor it uses, so the separate '
                  'sensor = LineSensor() line is no longer needed; keep it for test_sensors() or '
                  'delete it. Solution file: lesson-09-linetrack-class-addon.py.'},

        {'kind': 'code', 'title': 'Optional: move your three bodies in',
         'tag': 'Optional extension',
         'lead': 'Put `self.` in front of every sensor call, drivetrain call and setting: '
                 '`get_error()` becomes `self.sensor.get_error()`, `KP` becomes `self.kp`.',
         'lead_h': 0.95,
         'code': 'class LineTrack:\n'
                 '    def __init__(self):\n'
                 '        self.sensor = LineSensor()           # has-a LineSensor\n'
                 '        self.drivetrain = DifferentialDrive.get_default_differential_drive()\n'
                 '        self.base_effort = 0.4\n'
                 '        self.kp = 0.5\n'
                 '        self.turn_effort = 0.25\n'
                 '\n'
                 '    def track_to_intersection(self):\n'
                 '        # your function, with self. in front of the sensor,\n'
                 '        # the drivetrain and the settings\n'
                 '        pass\n'
                 '\n'
                 '    # turn_clockwise() and turn_counterclockwise():\n'
                 '    # the same, each with self\n'
                 'tracker = LineTrack()',
         'code_size': 14,
         'notes': 'The class-track skeleton replaces the section\'s settings and three functions; the '
                  'test functions stay. On the lesson page all three methods are pass outlines and '
                  'there is a header comment; the slide folds the last two methods into one comment '
                  'to fit. __init__ is the new idea, so it is given. Each test call gets tracker. in '
                  'front, and test_course() is the check that nothing else changed. The finished '
                  'methods are behind a reveal on the lesson page and are not shown here.'},
    ],
}
