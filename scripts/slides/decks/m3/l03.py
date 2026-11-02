DECK = {
    'module': 3, 'lesson': 3,
    'doc': 'module-03-grid-driving/lesson-03-turning-on-the-grid',
    'title': 'Turning on the Grid',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Sequence drive and turn operations into a **path**',
             'Turn at intersections with `turn_clockwise()` and `turn_counterclockwise()`, and say '
             'why the turn pivots on the intersection',
             'Navigate an **L-shaped path**, as a test function written from a description',
             'Plan a path on paper before you write the code',
         ],
         'notes': '40 to 50 minutes. Sequencing and planning. There is no new function this lesson: '
                  'a path is calls to what students already have.'},

        {'kind': 'bullets', 'title': 'Turning corners',
         'bullets': [
             'You can drive straight along the grid',
             'Now you\'ll turn corners, sequencing drives and turns to trace an **L-shaped path**',
             'Any route across a grid is really just a sequence of "drive some segments, turn, drive '
             'some more"',
         ],
         'callout': 'A path is a list of drives and turns',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Add to robot.py: this lesson\'s skeleton',
         'lead': 'Paste it above `RUN`, at the end of GRID DRIVING. No new function this time: two tests.',
         'lead_h': 0.7,
         'code': '# --- Lesson 3-3: turning on the grid ---\n'
                 '# No new function: a path is drive_intersections(), a turn,\n'
                 '# drive_intersections() again. The turn works because the\n'
                 '# helper leaves the wheels parked on the intersection.\n'
                 '\n'
                 'def test_l_shape():\n'
                 '    # drive 2 intersections, turn right, drive 2 more, then\n'
                 '    # print that the L is complete\n'
                 '    pass\n'
                 '\n'
                 'def test_my_path():\n'
                 '    # the path you planned on paper, one leg per line\n'
                 '    pass',
         'code_size': 18},

        {'kind': 'bullets', 'title': 'Drive, turn, drive',
         'bullets': [
             'Turning a corner on the grid is just like walking city streets',
             'Go to the intersection, then turn',
             'In code: `drive_intersections()`, then a turn, then `drive_intersections()` again',
         ],
         'callout': 'Three lines for an L: one per leg or corner',
         'tone': 'teal'},

        {'kind': 'figure', 'title': 'An L-shape',
         'figure': '/img/lesson-m3-03/l-path-xy.svg',
         'caption': 'Two intersections, a right turn, two more. The plan beside it is the paper '
                    'sketch from Step 2.',
         'notes': 'The robot starts parked on the bottom-left intersection, the corner nearest you, '
                  'facing away from you. The numbers are the intersections it arrives at: it turns '
                  'parked on 2 and ends parked on 4.'},

        {'kind': 'check',
         'question': 'Which sequence drives an L-shape: two segments, a right turn, then two more '
                     'segments?',
         'options': ['First `turn_clockwise()`, then `drive_intersections(2)`, then '
                     '`drive_intersections(2)`',
                     'First `drive_intersections(2)`, then `turn_clockwise()`, then '
                     '`drive_intersections(2)`',
                     '`drive_intersections(4)`',
                     '`turn_clockwise(); turn_clockwise()`'],
         'answer': 1,
         'explanation': 'Drive to the corner, turn, then continue: the drive/turn/drive order is what '
                        'makes the L.',
         'notes': 'Answer: B. The lesson writes the first two options as one line of calls separated '
                  'by semicolons; the slide spells them out with "then" so they fit.'},

        {'kind': 'bullets', 'title': 'Why the turn lands on the new line',
         'bullets': [
             '`drive_intersections()` leaves the robot parked with its **wheels over** the last '
             'intersection, sensors just past it',
             'That is exactly the position a turn needs',
             'The robot pivots about its center of rotation (Lesson 3-1), so it spins **on** the '
             'intersection',
             'The blind 60° plus the sensor-ended finish from Lesson 2-9 bring the sensors down on '
             'the crossing line',
         ],
         'size': 24,
         'callout': 'After the turn, the next `drive_intersections()` starts with a line to follow: '
                    'no extra step in between',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'After `turn_clockwise()`, what has to happen before the next '
                     '`drive_intersections()`?',
         'options': ['A `drive_past_intersection()` to clear the cross',
                     'Nothing: the turn ends with a sensor on the new line, and the next track '
                     'follows it',
                     'A short `time.sleep()`',
                     'A second turn to straighten up'],
         'answer': 1,
         'explanation': 'The turn finishes when `is_either_on_line()` sees the crossing line. The '
                        'robot is on the intersection, facing the new direction, with a sensor on '
                        'tape: ready to track.'},

        {'kind': 'check',
         'question': 'A student calls `turn_clockwise()` right after `track_to_intersection()`, '
                     'skipping `drive_past_intersection()`. What goes wrong?',
         'options': ['Nothing: the turn works the same',
                     'The wheels are short of the intersection, so it pivots in front of it and the '
                     'sensors miss the new line',
                     'The robot turns the wrong way',
                     'The turn takes twice as long'],
         'answer': 1,
         'explanation': 'The sensors reach the cross before the wheels do. Turning before the '
                        'drive-past spins the robot around a point short of the intersection; the '
                        'sensor-ended turn then hunts for a line that is not where it expects.',
         'notes': 'Answer: B. Two rules trip students up. The robot must be parked on an '
                  'intersection to turn: you cannot turn mid-segment, and drive_intersections() '
                  'always leaves it parked. And the arrival pair is track then drive past, every '
                  'time. Students who hand-write the pair sometimes drop the second half; '
                  'drive_intersections() exists partly so they can\'t.'},

        {'kind': 'frames', 'title': 'Activity · The L, then a path of your own',
         'tag': 'Activity',
         'figure': '/img/lesson-m3-03/l-and-plan.svg',
         'crop': (0.02, 0.09, 0.57, 1.0),
         'frames': [(0.42, '**Step 1:** the L, parked on the fourth intersection'),
                    (0.8, '**Step 2 example:** three, a left turn, one more')],
         'callout': 'Your own plan in Step 2 will draw something else',
         'tone': 'teal',
         'notes': 'On the lesson page this is one animation: the L from step 1, then the example plan '
                  'from step 2 from a different start. These are the end of each run.'},

        {'kind': 'steps', 'title': 'Step 1 · test_l_shape()',
         'steps': [
             'Write the body from its comment: three calls and a print',
             'Start the robot on a line segment with at least two intersections ahead and room to the '
             'right. Set the run line to `test_l_shape()` and run',
             'It should drive two segments, pivot on the second intersection, drive two more, and '
             'stop parked on the fourth. Don\'t go on until it does',
         ],
         'notes': 'The lesson has a closed reveal with the L; students run theirs first. '
                  'Class-track students call the turns on the tracker; the helper call is the same '
                  'for everyone.'},

        {'kind': 'steps', 'title': 'Step 2 · Plan on paper, then test_my_path()',
         'lead': 'A plan reads like directions: **leg 1:** three segments; **corner:** left; '
                 '**leg 2:** one segment.',
         'lead_h': 0.7,
         'steps': [
             'Sketch the path: mark the start, the direction the robot faces, how many segments each '
             'leg is, and where the turns go',
             'Translate it into `test_my_path()`, one leg or corner per line, with a comment saying '
             'which is which',
             'Set the run line to `test_my_path()` and run. Did the robot end where your sketch says?',
         ],
         'callout': 'If not, the sketch and the code disagree somewhere: find the line',
         'tone': 'orange',
         'notes': 'test_my_path() is the student\'s own, so there is nothing to check it against but '
                  'their sketch. Planning on paper first prevents most sequencing mistakes. More '
                  'support: give students a drawn path and have them write the matching sequence. '
                  'More challenge: a test_u_turn() (drive, turn right, drive one, turn right, '
                  'drive), a good reminder that two right turns only reverse direction if you drive '
                  'a segment between them.'},

        {'kind': 'check',
         'question': 'Starting at the bottom-left corner facing away from you, the robot runs: '
                     '`drive_intersections(3)`, `turn_clockwise()`, `drive_intersections(2)`. '
                     'Where does it end up?',
         'options': ['Back at the start',
                     '3 intersections up from the start, then 2 intersections to the right from there',
                     '2 up, then 3 to the right',
                     'It never turns'],
         'answer': 1,
         'explanation': 'It drives 3 up, away from you, turns right (now facing right), and drives 2 '
                        'to the right: an L ending 3 up and 2 across.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Maps', 'Turn-by-turn directions', '"Go 3 blocks, turn right, go 2 blocks" is the same '
                                                 'drive/turn sequence you just wrote.'),
             ('Warehouses', 'Pick routes', 'A warehouse robot\'s route is a list of segment-drives and '
                                           'turns between shelf intersections.'),
             ('Manufacturing', 'Toolpaths', 'CNC and pick-and-place machines follow planned sequences '
                                            'of moves and direction changes.'),
         ]},

        {'kind': 'wrapup',
         'questions': [
             'What\'s the basic shape of any grid path?',
             'What has to come before a turn?',
             'What comes after a turn?',
         ],
         'next': 'the final project: four drive-and-turn legs in a loop, a complete square',
         'notes': 'Answers: a sequence of drives and turns. The arrival pair: the robot parked on the '
                  'intersection. The next drive: a sensor is already on the new line. Formative: '
                  'sequence drives and turns for a described path, and explain why the turn must '
                  'wait for the drive-past. Exit ticket: "Write the calls for drive 2, turn left, '
                  'drive 1."'},
    ],
}
