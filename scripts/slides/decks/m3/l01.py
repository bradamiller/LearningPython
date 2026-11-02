DECK = {
    'module': 3, 'lesson': 1,
    'doc': 'module-03-grid-driving/lesson-01-introduction-to-the-grid',
    'title': 'Introduction to the Grid',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Describe how a grid is built from lines and **intersections**',
             'Explain how a grid intersection is just the "cross" from Module 2',
             'Use `track_to_intersection()` and `drive_past_intersection()` to arrive at the next intersection',
             'Start the GRID DRIVING section of `robot.py`, and write its first two tests from a description',
             'Place the robot on the grid and reach the first intersection',
         ],
         'notes': '40 to 50 minutes. The big idea of Module 3 is not a new Python concept, it is '
                  'reuse: the exact same functions running on a new course. Say it out loud early, '
                  'because students expect a new problem to need new code.'},

        {'kind': 'bullets', 'title': 'From the circle to the grid',
         'bullets': [
             'In Module 2 the robot learned to follow a line and detect a cross',
             'Now a whole **grid** of lines goes on the floor',
             'The LINE TRACKING section of `robot.py` already knows how to drive it',
             'No new driving code: this lesson opens a new section and fills it with **tests**',
         ],
         'callout': 'Same tape, same surface, same functions, new course',
         'tone': 'teal'},

        {'kind': 'figure', 'title': 'A grid is just a lot of intersections',
         'figure': '/img/lesson-m3-01/grid.svg',
         'caption': 'Rows and columns of tape. Every place they cross is an **intersection**: a spot '
                    'the robot can stop and turn.',
         'notes': 'To the robot\'s two sensors, an intersection looks exactly like the taped cross '
                  'from Module 2: both sensors go high at once. A segment is the stretch of line '
                  'from one intersection to the next.'},

        {'kind': 'bullets', 'title': 'You already built the whole toolkit',
         'lead': 'The LINE TRACKING section you finished in Lesson 2-9 has the four functions that '
                 'drive a grid:',
         'lead_h': 1.0,
         'bullets': [
             '`track_to_intersection()`: follow the line to the next intersection and stop',
             '`drive_past_intersection()`: put the wheels on the intersection, sensors past it',
             '`turn_clockwise()`: turn onto the perpendicular line to the right',
             '`turn_counterclockwise()`: turn onto the perpendicular line to the left',
         ],
         'size': 24,
         'callout': 'A grid intersection is the Module 2 cross, so the toolkit works **unchanged**',
         'tone': 'teal',
         'notes': 'The grid is the same color surface with the same tape the circle was made from, '
                  'so there is nothing to re-measure and nothing to re-tune: both sections of '
                  'robot.py come across untouched.'},

        {'kind': 'bullets', 'title': 'Built the LineTrack class? Use it',
         'bullets': [
             'Your LINE TRACKING section is the class, with `tracker = LineTrack()` right under it',
             'The skeletons in this module use the function names; yours is the same name on your object',
             'Where an outline says "arrive at the intersection", your body calls the tracker',
             'No threshold constant, no sensor to hand in, nothing shared through `global`',
         ],
         'size': 22,
         'split': 0.56,
         'code': 'tracker.track_to_intersection()\n'
                 'tracker.drive_past_intersection()',
         'code_size': 16,
         'callout': 'The tracker brought its sensor and its settings with it. That is what the class '
                    'bought you.',
         'tone': 'green',
         'notes': 'Only for students who built the LineTrack class in Module 2. The helper they '
                  'write in Lesson 3-2 calls the tracker the same way.'},

        {'kind': 'check',
         'question': 'Do you need to change your driving toolkit to drive on the grid?',
         'options': ['Yes: grids need a whole new set of functions',
                     'No: a grid intersection looks just like the Module 2 cross, so the toolkit '
                     'works unchanged',
                     'Yes: you must rewrite `track_to_intersection()`',
                     'Only the sensor functions change'],
         'answer': 1,
         'explanation': 'An intersection reads the same to the sensors as the circle\'s cross did, so '
                        'the same functions navigate the grid with no changes. That\'s code reuse.',
         'notes': 'Sell the reuse: it is the point of the module. That is how professionals work: a '
                  'well-designed toolkit outlives the problem it was written for.'},

        {'kind': 'code', 'title': 'Add to robot.py: a new GRID DRIVING section',
         'lead': 'Paste it above `RUN`, after the whole LINE TRACKING section. No functions yet, '
                 'only tests.',
         'lead_h': 0.7,
         'code': '# ===== GRID DRIVING =====\n'
                 '# Drives the taped grid one intersection at a time, using only\n'
                 '# the LINE TRACKING functions: a grid intersection is the\n'
                 '# cross from Module 2. To ARRIVE at an intersection is\n'
                 '# track_to_intersection() then drive_past_intersection(); a\n'
                 '# turn happens parked on one. Nothing here touches a sensor.\n'
                 '\n'
                 'def test_first_intersection():\n'
                 '    # from a line, arrive at the next intersection and say so\n'
                 '    pass\n'
                 '\n'
                 'def test_arrive_and_turn():\n'
                 '    # arrive at the intersection, then turn right onto the\n'
                 '    # crossing line\n'
                 '    pass',
         'code_size': 16,
         'notes': 'A new kind of driving gets a new section. It starts with no functions of its '
                  'own because there is nothing new to write yet.'},

        {'kind': 'bullets', 'title': 'Two things are different this module',
         'bullets': [
             'The tests have **no bodies**: the comment says what the test should do, and you write it',
             'From here on, that is how every test arrives',
             '`pass` holds the place, as it did in Lesson 2-1, so the file runs before you\'ve written anything',
         ],
         'callout': 'Read the comment, write the body, run the test',
         'tone': 'teal',
         'notes': 'The hint level drops this module. Module 2 gave the test functions in full; from '
                  'here the skeleton gives the def line and a comment, and the body is the '
                  'student\'s: test-driven development, lightly. The bodies in this lesson are two '
                  'to five calls they have made before, so it is the right place to start that '
                  'habit.'},

        {'kind': 'bullets', 'title': 'Drive to the first intersection',
         'lead': 'Place the robot centered on a line, facing toward the next intersection. The '
                 'first test is two calls:',
         'lead_h': 1.0,
         'bullets': [
             '`track_to_intersection()` follows the line right up to the cross',
             '`drive_past_intersection()` rolls forward so the wheels are over the intersection',
             'Exactly as `test_park()` did in Lesson 2-9',
         ],
         'callout': 'Those two calls together are the **arrival pair**: what "arrive at an '
                    'intersection" means for the rest of the course',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Where the robot turns',
         'bullets': [
             'When `track_to_intersection()` stops, the **sensors** are on the cross',
             'But the sensors sit at the very front of the robot',
             'The robot turns about its **center of rotation**: the pen hole between the drive '
             'wheels, **8.75 cm** further back',
             'Turn from where the track stopped, and the robot swings around a point short of the '
             'intersection',
         ],
         'callout': 'On the grid, the second call of the pair matters more than it did on the circle',
         'tone': 'orange'},

        {'kind': 'figure', 'title': 'Turn now, or drive past first?',
         'figure': '/img/lesson-m2-09/park-turn-left-then-right.svg',
         'frame': 0.8,
         'caption': 'Left: turns right away, and its sensors miss the cross street. Right: drives '
                    'past first, spins on the intersection, and lands on the new line.',
         'notes': 'Both robots start where track_to_intersection() left them. On the lesson page '
                  'this is an animation; the slide shows the end state.'},

        {'kind': 'bullets', 'title': 'Why every arrival is the pair',
         'bullets': [
             '`drive_past_intersection()` drives forward exactly that **8.75 cm**',
             'The center of rotation ends up where the sensors were: right on the intersection',
             'Any turn from there spins the robot **in place** on the cross',
             'The sensors come down on the crossing line',
         ],
         'callout': 'Every arrival is the pair, never the track alone, even when the robot is about '
                    'to go straight on',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'Which function drives the robot from where it is to the next intersection?',
         'options': ['`turn_clockwise()`', '`track_to_intersection()`',
                     '`drive_past_intersection()`', '`get_error()`'],
         'answer': 1,
         'explanation': '`track_to_intersection()` follows the line and stops when both sensors hit '
                        'the intersection: one grid segment per call. `drive_past_intersection()` '
                        'then parks the wheels on it.'},

        {'kind': 'check',
         'question': 'Why drive past the intersection before turning, instead of turning where '
                     '`track_to_intersection()` stops?',
         'options': ['To save battery',
                     'The robot turns about its center of rotation, 8.75 cm behind the sensors, so '
                     'turning early pivots short of the intersection and the sensors miss the new line',
                     'Because `turn_clockwise()` only works while the robot is moving',
                     'It does not matter; both land on the new line'],
         'answer': 1,
         'explanation': 'The sensors arrive first. Driving the 8.75 cm puts the center of rotation on '
                        'the cross, so the turn spins on the intersection and the sensors come down '
                        'on the crossing line.'},

        {'kind': 'frames', 'title': 'Activity · Reach it, then turn',
         'tag': 'Activity',
         'figure': '/img/lesson-m3-01/reach-and-turn.svg',
         'crop': (0.02, 0.09, 0.565, 1.0),
         'frames': [(0.35, '**Step 1:** parked on the intersection'),
                    (0.95, '**Step 2:** turned onto the crossing line')],
         'callout': 'The arrival pair parks the wheels on the intersection, and from there one turn '
                    'lands on the crossing line',
         'tone': 'teal',
         'notes': 'On the lesson page this is one animation of both tests, with the step running '
                  'highlighted beside the grid. These are the end of each step.'},

        {'kind': 'steps', 'title': 'Step 1 · test_first_intersection()',
         'steps': [
             'Write the body: a print saying what it\'s about to do, the arrival pair, and a print '
             'saying it got there',
             'Set the run line to `test_first_intersection()`. Put the robot on a line segment facing '
             'the next intersection, and run',
             'It should stop with its wheels on the intersection. Try a few starting spots. Don\'t go '
             'on until it does',
         ],
         'notes': 'More support: have students get test_first_intersection() reliable before writing '
                  'the turn test.'},

        {'kind': 'steps', 'title': 'Step 2 · test_arrive_and_turn()',
         'steps': [
             'Write the body: the arrival pair, then `turn_clockwise()`, with a print before the turn '
             'and one after',
             'Set the run line to `test_arrive_and_turn()` and run',
             'It should arrive, pivot on the intersection, and stop facing along the crossing line '
             'with a sensor on the tape',
         ],
         'callout': 'Detects an intersection **immediately**? It started on one: nudge it back '
                    'onto the line.',
         'tone': 'orange',
         'notes': 'The lesson has a closed reveal with both tests; students write and run theirs '
                  'first. Prints can say anything; the calls and their order are what matter. '
                  'Common snags: starting on an intersection (detects instantly), a threshold that '
                  'needs re-calibrating for the grid surface, or the robot not centered before a '
                  'turn. More challenge: a test_two_segments() that arrives, turns, and arrives '
                  'again, previewing Lesson 3-2.'},

        {'kind': 'check',
         'question': 'You run the program and the robot reports "Intersection reached!" instantly '
                     'without moving. Why?',
         'options': ['The battery is dead',
                     'It started sitting on an intersection, so both sensors were already high',
                     '`track_to_intersection()` is broken',
                     'The threshold is too low'],
         'answer': 1,
         'explanation': 'If it starts on a cross, `is_at_cross()` is already true and the follow loop '
                        'exits at once. Back it onto a plain line segment to start.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Warehouses', 'Fulfillment robots', 'Warehouse robots roll along floor grids, stopping '
                                                  'at labeled intersections to pick shelves.'),
             ('Cities', 'Street navigation', 'Self-driving cars think in intersections and blocks: '
                                             'drive to the next junction, then decide.'),
             ('Games', 'Grid worlds', 'Countless games move characters on a grid, one tile at a '
                                      'time, exactly like this.'),
         ]},

        {'kind': 'wrapup',
         'questions': [
             'What is a grid intersection, to the robot?',
             'Which function drives one segment to the next intersection?',
             'Why didn\'t you have to write any new driving code?',
         ],
         'next': 'drive through intersections, with a loop and counting',
         'notes': 'Answers: the same both-sensors-high cross from Module 2. track_to_intersection(), '
                  'then drive_past_intersection() to park on it. LINE TRACKING already handles lines '
                  'and crosses: reuse, and only the tests are new. Formative: explain why LINE '
                  'TRACKING works unchanged, and drive to the first intersection reliably. Exit '
                  'ticket: "Which function turns the robot onto the crossing line?" '
                  '(turn_clockwise() or turn_counterclockwise()). Next lesson the GRID DRIVING '
                  'section gets its first function.'},
    ],
}
