DECK = {
    'module': 2, 'lesson': 8,
    'doc': 'module-02-line-tracking/lesson-08-detecting-intersections',
    'title': 'Detecting Intersections',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Test `is_at_cross()` on a **moving** robot, with no line following in the program',
             'Write `track_to_intersection()`: follow the line **until** `is_at_cross()` says stop, then drive the robot\'s center onto the cross',
             'Explain why the robot drives **8.75 cm** after the sensors reach the cross',
             'Explain why the cross is detected in the **loop condition**, not inside the loop body',
             'Program a response to the cross (stop, turn around, follow back)',
         ],
         'notes': '50 to 60 minutes. Students finished the sensor toolkit last lesson and tested it '
                  'by hand. Today the robot drives on it. The big idea is a sensor-ended loop: '
                  'the loop condition does the looking, the body does the following.'},

        {'kind': 'bullets', 'title': 'A reason to stop',
         'bullets': [
             'Last lesson you tested all five sensor functions by **sliding the robot by hand**',
             'Your follower in `test_follow()` runs **forever**',
             'This lesson gives it a reason to stop: **the cross**',
             'First `is_at_cross()` gets one more test, with the robot moving. Then it goes in charge of the follower\'s loop',
         ],
         'callout': 'The stopping is done by a function you already trust',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Add to robot.py: this lesson\'s skeleton',
         'lead': 'Paste it above `RUN`, at the end of LINE TRACKING. The loop\'s body is the body '
                 'of `test_follow()`: what\'s new is the `while` line and the drive after the loop.',
         'lead_h': 1.15,
         'code': '# --- Lesson 2-8: follow to a cross ---\n'
                 '# track_to_intersection() is the follower from test_follow()\n'
                 '# with a reason to stop: it follows until is_at_cross() says\n'
                 '# the sensors are on a crossing line, then drives on until\n'
                 '# the robot\'s center is on it. Lesson 2-9 adds the turns.\n'
                 '\n'
                 'def track_to_intersection():\n'
                 '    # until is_at_cross():\n'
                 '    #     correction = get_error() * KP\n'
                 '    #     steer with arcade(BASE_EFFORT, correction)\n'
                 '    # then stop the motors\n'
                 '    # then drive straight 8.75 cm: the robot\'s center onto\n'
                 '    # the cross\n'
                 '    pass',
         'code_size': 15,
         'notes': 'The same paste also holds three test functions: test_cross_moving(), test_track() '
                  'and test_reverse(). The next slides show each one where it is used. This is the '
                  'first real driving function, placed next to the test that has been doing the job '
                  'so far.'},

        {'kind': 'code', 'title': 'One more test, moving this time',
         'lead': 'Sliding by hand showed `is_at_cross()` reads the tape. Does a **driving** robot get '
                 'a clean reading when both sensors arrive on the strip?',
         'lead_h': 1.2,
         'code': 'def test_cross_moving():\n'
                 '    # robot 20-30 cm from a straight line, square on: drive\n'
                 '    # until the cross check fires\n'
                 '    while not is_at_cross():\n'
                 '        drivetrain.set_effort(0.3, 0.3)\n'
                 '    drivetrain.stop()\n'
                 '    print("Cross!")',
         'code_size': 20,
         'callout': 'It is Lesson 2-2\'s drive-to-the-edge program with the condition swapped for a '
                    'function call. No line following in it yet.',
         'tone': 'teal'},

        {'kind': 'table', 'title': 'Reading the moving test',
         'headers': ['What the robot does', 'What it means'],
         'widths': [3.4, 6.6],
         'rows': [
             ['Stops with **both sensors on the tape**',
              '`is_at_cross()` works at driving speed. Anything that goes wrong later is not its fault'],
             ['Drives **straight through**',
              'The sensors crossed the tape faster than the loop read them (drop the effort to 0.2), or the threshold is too high'],
             ['Stops **before** the tape',
              'Something lighter than the floor counted as black'],
         ],
         'size': 22},

        {'kind': 'check',
         'question': 'Why test `is_at_cross()` with a straight drive before using it in the line follower?',
         'options': ['Because line following cannot be tested on a cross',
                     'So that if the test fails, the only thing that can be wrong is the cross check',
                     'Because `set_effort()` is faster than `arcade()`',
                     'It makes no difference; either order is the same'],
         'answer': 1,
         'explanation': 'One new piece at a time. With only `is_at_cross()` and a straight drive, a '
                        'failure points at exactly one place. Inside the follower, it could be in either.'},

        {'kind': 'bullets', 'title': 'Follow until the cross',
         'bullets': [
             '`test_follow()` is `while True:`, so it follows forever',
             'Change the **condition**: the looking is done by the loop condition, the following is done inside the loop',
             'The body is the two lines you already have',
             'When both sensors reach the cross, `is_at_cross()` returns `True`, the loop ends, and the robot stops',
         ],
         'callout': 'Read the `while` line as a sentence: **while not at a cross, follow**',
         'tone': 'teal',
         'notes': 'An earlier version of this lesson did the cross check and the following in one '
                  'if/else inside a while True. Students got it working but could not say which half '
                  'was broken when it was not. Now the sensor functions arrive tested, and '
                  'track_to_intersection() is test_follow()\'s loop with the condition replaced. Keep '
                  'that separation visible: every function in Lesson 2-9 follows it.'},

        {'kind': 'figure', 'title': 'test_track() from above: following',
         'figure': '/img/lesson-m2-08/track-to-cross.svg',
         'frame': 0.36,
         'crop': (0.0, 0.08, 1.0, 1.0),
         'caption': 'Watch the `is_at_cross()` line: following the line only ever puts one sensor on '
                    'the tape at a time, so it stays `False` the whole way round.',
         'notes': 'On the lesson page this is one animation of test_track(); these two slides are two '
                  'moments of it. The readout shows the live left and right readings: at most one is '
                  'high while following.'},

        {'kind': 'figure', 'title': 'test_track() from above: the cross',
         'figure': '/img/lesson-m2-08/track-to-cross.svg',
         'frame': 0.8,
         'crop': (0.0, 0.08, 1.0, 1.0),
         'caption': 'Both sensors reach the cross strip and read high: `is_at_cross()` becomes `True`, '
                    'the loop ends, the robot stops. Then it drives 8.75 cm, center on the cross.',
         'notes': 'The robot stops with its sensors on the cross, then drives straight 8.75 cm and '
                  'stops with its center on the cross; the next section explains that drive. On tight '
                  'curves both sensors can briefly go high (a false positive); a wide, crisp taped '
                  'cross and a little tuning handle it.'},

        {'kind': 'check',
         'question': 'What makes `track_to_intersection()` stop?',
         'options': ['A fixed number of loop passes',
                     '`is_at_cross()` becoming `True`: both sensors see the cross',
                     'The error reaching exactly zero',
                     'A timer'],
         'answer': 1,
         'explanation': 'The while condition is `not is_at_cross()`. The moment both sensors see the '
                        'tape of a cross, the loop ends and the robot stops, however long that took.'},

        {'kind': 'check',
         'question': 'In `track_to_intersection()`, where is the intersection detected?',
         'options': ['In an if/else inside the loop body',
                     'In the while condition: the body only steers',
                     'After the loop, by checking the last error',
                     'In `arcade()`'],
         'answer': 1,
         'explanation': 'The loop condition asks `is_at_cross()` every pass. The body reads, computes, '
                        'steers. Each part has one job, which makes each one testable.'},

        {'kind': 'bullets', 'title': 'Arriving: the center on the cross',
         'bullets': [
             'When the loop ends, the **sensors** are on the cross',
             'They sit at the very **front** of the robot',
             'The robot turns about its **center of rotation**: the hole between the drive wheels where a pen goes, **8.75 cm** further back',
             'So `track_to_intersection()` ends with one more move: drive straight **8.75 cm**. Now the robot\'s center is on the cross',
         ],
         'split': 0.55,
         'figure': '/img/lesson-m2-09/park-turn-left-then-right.svg',
         'frame': 0.0,
         'crop': (0.0, 0.0, 0.5, 0.9),
         'notes': 'The figure is the left panel of the animation two slides on, at its first moment: '
                  'the robot stopped with its sensors on the cross. The 8.75 cm drive is built into '
                  'track_to_intersection() so it is taught once. From here to Module 6, "track to the '
                  'next intersection" means the robot is there, center on the cross, ready to turn, '
                  'and no later lesson repeats it. The 8.75 cm is sensor-to-axle on an XRP; measure '
                  'it if the robot\'s mounting differs.'},

        {'kind': 'bullets', 'title': 'One move, two jobs',
         'bullets': [
             '**Turns spin on the cross.** Turn from where the sensors stopped and the robot swings about a point short of the cross. Turn from the center and the sensors come down on the new line',
             '**The next track starts clean.** The sensors end up past the tape, so the next `track_to_intersection()` has a line to follow instead of stopping at once',
         ]},

        {'kind': 'figure', 'title': 'Turn now, or drive 8.75 cm first?',
         'figure': '/img/lesson-m2-09/park-turn-left-then-right.svg',
         'frame': 0.75,
         'caption': 'Both stopped with their sensors on the cross. Left: turns right away and swings '
                    'about a point short of it. Right: drives 8.75 cm first, spins on the cross, and '
                    'its sensors find the new line.',
         'notes': 'On the lesson page both robots animate side by side from the same start. This is '
                  'the end state: the left robot\'s sensors land beside the new line, the right '
                  'robot\'s land on it.'},

        {'kind': 'bullets', 'title': 'A distance, not a time',
         'bullets': [
             'It\'s a **distance**, not a `time.sleep()`, on purpose',
             'Eight and three-quarter centimeters is the same with a full battery or a flat one; half a second is not',
         ],
         'callout': 'You know the drivetrain call that drives a distance: you\'ve used it since Lesson 1-8.',
         'tone': 'orange'},

        {'kind': 'check',
         'question': 'Why does `track_to_intersection()` end by driving 8.75 cm rather than driving for '
                     'half a second?',
         'options': ['`straight()` is easier to spell',
                     'A distance is the same with a full or flat battery and on any floor; a time needs re-tuning',
                     '`time.sleep()` cannot be used with motors',
                     'Because 8.75 is a magic number'],
         'answer': 1,
         'explanation': 'The course avoids timing-based movement everywhere. Distances and sensor '
                        'readings describe the world; a duration describes a guess about the motors.'},

        {'kind': 'code', 'title': 'The two tests that drive it',
         'lead': 'Both are in the skeleton. The run block still waits for the button before every test.',
         'code': 'def test_track():\n'
                 '    # robot on the circle, pointed along it: follow to the\n'
                 '    # cross and stop\n'
                 '    track_to_intersection()\n'
                 '    print("Done!")\n'
                 '\n'
                 'def test_reverse():\n'
                 '    # follow to the cross, turn around on it, follow back\n'
                 '    track_to_intersection()\n'
                 '    drivetrain.turn(180)\n'
                 '    track_to_intersection()\n'
                 '    print("Done!")',
         'code_size': 19},

        {'kind': 'steps', 'title': 'Step 1 · is_at_cross(), moving',
         'steps': [
             'Set the run call to `test_cross_moving()`',
             'Robot 20 to 30 cm from a straight line, **square on**. It should stop with both sensors on the tape',
             'Try it from **three distances**',
         ],
         'callout': 'Don\'t go on until it does',
         'tone': 'orange'},

        {'kind': 'steps', 'title': 'Step 2 · track_to_intersection()',
         'steps': [
             'Write the body: start by copying the loop out of `test_follow()`',
             'Set the run call to `test_track()`. Put the robot on the circle, pointed along it',
             'It should follow the line around and stop with its **center on the cross**: put a finger on the tape beside the robot, and the pen hole between the wheels should sit over it',
         ],
         'callout': 'Weaves? Same gain you tuned in Lesson 2-6. Stops somewhere else? Step 1 already '
                    'cleared the cross check, so look at where the follower put the sensors.',
         'tone': 'orange',
         'notes': 'The check on the lesson page is a closed reveal; do not show it before students '
                  'have tested their own on the circle. If theirs reads the error a different way '
                  'and passes the test, they keep theirs. Class-track students write '
                  'track_to_intersection() as a plain function this lesson, calling their sensor '
                  'object (sensor.is_at_cross(), sensor.get_error()); the LineTrack class comes in '
                  'Lesson 2-9\'s extension.'},

        {'kind': 'steps', 'title': 'Step 3 · Follow, reverse, follow',
         'steps': [
             'Set the run call to `test_reverse()`',
             'The robot follows to the cross, **turns around on it**, and follows the circle back the other way to the same cross',
         ]},

        {'kind': 'steps', 'title': 'Step 4 · Challenge: count the crossings',
         'steps': [
             'Write `test_count()`: the robot reverses at the cross **four times** and stops',
             'At each cross, print the count: "Cross # 1", "Cross # 2", and so on, then "Done!"',
             'You know a loop that runs a **fixed number of times**',
         ],
         'callout': 'This is a direct preview of the Module 2 final project',
         'tone': 'teal',
         'notes': 'test_count() is hand-in work; the solution is in the teacher copy only. '
                  'More support: have the straight-drive test print get_left() and get_right() each '
                  'pass, so students see both readings climb as the tape arrives. More challenge: '
                  'turn 90 degrees to take the perpendicular path; give different crossings different '
                  'behaviors (beep on 1, blink on 2); or write track_for_crosses(n) that follows '
                  'through n crossings before stopping.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Transit', 'Rail junctions', '\nTrains detect track sensors at switches to decide '
                                           'which way to route.'),
             ('Factories', 'Conveyor triggers', '\nA sensor spots each item passing a point and '
                                                'triggers a sort, stamp, or count.'),
             ('Wearables', 'Step & tap detection', '\nYour watch watches a constant sensor stream for '
                                                   'the pattern that means "a step" or "a tap."'),
         ],
         'height': 4.0,
         'notes': 'The common thread: watching a continuous stream for a specific event.'},

        {'kind': 'wrapup',
         'questions': [
             'Why test `is_at_cross()` with a straight drive first?',
             'Where does `track_to_intersection()` look for the cross?',
             'What ends `track_to_intersection()`\'s loop?',
             'Why drive 8.75 cm after the loop?',
         ],
         'next': 'two turns that spin on the cross until a sensor finds the next line',
         'notes': 'Answers: so a failure can only be the cross check. In the while condition; the '
                  'body only steers. Both sensors on the cross, not a timer, not a count. The sensors '
                  'reach the cross first; the robot\'s center, which it turns about, is 8.75 cm behind '
                  'them. Exit ticket: "Write track_to_intersection() from memory using the toolkit '
                  'functions." Lesson 2-9 adds the two turns, which spin on the cross until a sensor '
                  'finds the next line: the toolkit the rest of the course drives on.'},
    ],
}
