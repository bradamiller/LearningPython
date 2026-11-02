DECK = {
    'module': 3, 'lesson': 4,
    'doc': 'module-03-grid-driving/lesson-04-final-project',
    'title': 'Final Project',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Design a test function that drives a closed **square** path on the grid',
             'Use a `for` loop to repeat a drive-and-turn sequence',
             'Test and tune a real robot until the path closes',
             'Verify the robot returns to its starting position',
         ],
         'notes': '50 to 60 minutes. The capstone of Module 3 and its summative assessment. Treat it '
                  'as plan, build, test, present.'},

        {'kind': 'bullets', 'title': 'Tie the module together',
         'bullets': [
             'Your robot will drive a complete **square** on the grid',
             'Two intersections per side, a right turn at each corner, four times',
             'It ends up right back where it started',
             'Same `robot.py`, no new Python: just your sections, put to work',
         ],
         'callout': 'Everything you need is already in the file',
         'tone': 'teal'},

        {'kind': 'frames', 'title': 'The mission',
         'figure': '/img/lesson-m3-04/square-run.svg',
         'crop': (0.02, 0.07, 0.585, 0.875),
         'frames': [(0.2, '**Side 1 done:** turning right at the corner'),
                    (0.5, '**Side 3 of 4**'),
                    (0.95, '**Square complete:** back at the start')],
         'callout': 'Each side is two arrivals at an intersection; each corner is one right turn',
         'tone': 'teal',
         'notes': 'On the lesson page this is one animation of the whole run, with a panel naming '
                  'each step: Ready, Side N of 4, Turning right, Square complete. The robot starts '
                  'parked on the bottom-left corner, nearest you, facing away, and ends there facing '
                  'the way it began.'},

        {'kind': 'bullets', 'title': 'Your program must',
         'bullets': [
             'Use the LINE TRACKING section and `drive_intersections()` **unchanged**',
             'Drive the square with a `for` loop (not four copied blocks)',
             'Print progress',
             'Return to start',
         ],
         'callout': 'These four are what the project is graded on',
         'tone': 'orange',
         'notes': 'A 50-point rubric works well: using the earlier sections unchanged, using a loop, '
                  'completing four sides, returning to start, and progress prints.'},

        {'kind': 'code', 'title': 'Add to robot.py: this lesson\'s skeleton',
         'lead': 'Paste it above `RUN`, at the end of GRID DRIVING. One setting and two tests; the '
                 'second test is the project.',
         'lead_h': 0.7,
         'code': '# --- Lesson 3-4: final project, the square ---\n'
                 '# The module project: four sides of SIDE intersections with a\n'
                 '# right turn at every corner, back to the start. Built from\n'
                 '# drive_intersections() and one turn; nothing new is defined.\n'
                 'SIDE = 2                 # intersections per side\n'
                 '\n'
                 'def test_one_side():\n'
                 '    # one side of the square: drive SIDE intersections, then\n'
                 '    # turn right\n'
                 '    pass\n'
                 '\n'
                 'def test_square():\n'
                 '    # the project. A for loop that runs one side per pass,\n'
                 '    # printing which side it is on; then the finish message\n'
                 '    pass',
         'code_size': 17,
         'notes': '`SIDE` is a setting, in capitals like the others, so the size of the square is '
                  'one number at the top of the sub-section and not a literal buried in a loop.'},

        {'kind': 'bullets', 'title': 'One loop, four sides',
         'bullets': [
             'The whole square is a **four-iteration loop**: each pass drives one side, then turns '
             'the corner',
             'The piece that drives a side is `drive_intersections(count)`, built and tested in '
             'Lesson 3-2',
             'Sketch the loop body in English first: what happens **once per side**?',
             'The loop body is two calls and a print or two. If yours is longer, ask what the extra '
             'lines are for',
         ],
         'size': 24,
         'callout': 'Nothing goes between the drive and the turn: the helper leaves the robot parked '
                    'on the corner, and the turn ends on the next side\'s line',
         'tone': 'teal',
         'notes': 'The teacher copy of the solution is on the lesson page, to unstick a team. The '
                  'loop is the graded work, and there is no student reveal for it. Class-track '
                  'students call the turn on the tracker.'},

        {'kind': 'bullets', 'title': 'Four right turns',
         'bullets': [
             'Each right turn is 90°',
             'Four of them add up to a full **360°**',
             'That is why the robot comes back to its starting **heading** as well as its starting '
             'intersection',
         ],
         'callout': 'Back on the start corner, facing the way it began',
         'tone': 'green'},

        {'kind': 'check',
         'question': 'The square loop runs `turn_clockwise()` once per side, four times. How many '
                     'total degrees does the robot turn?',
         'options': ['90°', '180°', '360°', '270°'],
         'answer': 2,
         'explanation': 'Four right turns × 90° each = 360°: one full rotation, which is why a '
                        'four-sided loop returns the robot to its starting heading.'},

        {'kind': 'steps', 'title': 'Activity · Test one side at a time',
         'lead': 'Don\'t run all four sides first. Build up, one test at a time:',
         'lead_h': 0.65,
         'steps': [
             '**One side.** Write `test_one_side()` and set the run line to it. It should drive `SIDE` '
             'intersections, pivot on the corner, and stop facing along the next side. Don\'t go on '
             'until it does',
             '**Two sides.** Write `test_square()` with `range(2)` for now. What shape should that '
             'give you? Predict, then run',
             '**Full square.** Change it to `range(4)`. Does it close back to the start?',
         ],
         'notes': 'The lesson has a closed reveal with an animation of what each test should look '
                  'like; it is left off the slides because it shows the loop running. Insist on '
                  'incremental testing: one side, then two, then four.'},

        {'kind': 'check',
         'question': 'A student wrote `for leg in range(3):` and added a second '
                     '`drive_past_intersection()` just before the turn. What are the two bugs?',
         'options': ['Nothing is wrong',
                     '`range(3)` makes only 3 sides (needs 4), and the extra drive-past carries the '
                     'wheels 8.75 cm past the corner',
                     '`turn_clockwise()` should be `turn_counterclockwise()`, and sides should be 4',
                     'The loop should be a while loop, and print is missing'],
         'answer': 1,
         'explanation': 'A square needs `range(4)`. And `drive_intersections()` already ends with the '
                        'wheels on the corner; a second drive-past moves them off it, so the turn '
                        'pivots in the wrong place.',
         'notes': 'Answer: B. The common fixes are all tuning: turns that aren\'t quite 90° (the '
                  'blind part of the turn too long, or TURN_EFFORT too high, so the sensor-ended '
                  'finish spins past the line), a drive_past_intersection() distance that doesn\'t '
                  'match the robot\'s sensor-to-axle gap, or too much BASE_EFFORT. Frame that as real '
                  'engineering. Returning approximately to start is success; a perfectly closed '
                  'square on real tape is a bonus. Two clean sides already show mastery.'},

        {'kind': 'table', 'title': 'Activity · Extend it',
         'tag': 'Activity',
         'lead': 'Once the square works, try a variation:',
         'headers': ['Variation', 'What to try'],
         'widths': [3.2, 8],
         'rows': [
             ['**Bigger:** 3-per-side square', 'Set `SIDE = 3` for a larger square. Does it still close?'],
             ['**Rectangle:** alternating legs', 'Write `test_rectangle()`: a list `[2, 3, 2, 3]` '
                                                 'indexed by the loop variable, so opposite sides differ'],
             ['**Mirror:** left-turn square', 'Swap in `turn_counterclockwise()` to drive the square '
                                              'the other way around'],
         ],
         'size': 20,
         'callout': 'Each variation changes one thing',
         'tone': 'teal',
         'notes': 'For teams whose square works. On the lesson page these are three cards; the slide '
                  'makes them a table so the function names fit on one line.'},

        {'kind': 'frames', 'title': 'The three extensions',
         'tag': 'Activity',
         'figure': '/img/lesson-m3-04/extensions.svg',
         'crop': (0.02, 0.09, 0.57, 1.0),
         'frames': [(0.35, '**Bigger:** `SIDE = 3`'),
                    (0.6, '**Rectangle:** 2, 3, 2, 3'),
                    (0.8, '**Mirror:** left turns')],
         'callout': 'Each changes one thing, and still closes on its start corner',
         'tone': 'teal',
         'notes': 'On the lesson page this is one animation of the three runs. The mirror square '
                  'starts from the bottom-right corner and goes round counterclockwise.'},

        {'kind': 'wrapup', 'title': 'Activity · Reflect',
         'questions': [
             'What was hardest to get working, and how did you fix it?',
             'Why is the `for` loop better than copying the side code four times?',
             'How is this different from the polygon function in Module 1?',
         ],
         'notes': 'Demo the square, then reflect. On the polygon question: there you set distances '
                  'and angles; here you count intersections and follow real lines.'},

        {'kind': 'bullets', 'title': 'Nice work: Module 3 done',
         'bullets': [
             'You reused functions you wrote weeks ago on a brand-new surface',
             'You learned to count intersections, and sequenced drives and turns into real paths',
             '`robot.py` grew a GRID DRIVING section with one function and a record of every test it '
             'passed',
         ],
         'callout': 'Every route here was one **you** planned and hard-coded. That\'s about to change.',
         'tone': 'green',
         'notes': 'Coming in Module 4, Manhattan Navigation: instead of students hard-coding the path, '
                  'the computer calculates it. "Go to (2, 3)" means two across and three up from the '
                  'corner nearest you, and the robot works out the drives and turns itself, using '
                  'coordinates, tuples and lists, in new sections of the same file. Reward the '
                  'tuning process in the assessment.'},
    ],
}
