DECK = {
    'module': 3, 'lesson': 2,
    'doc': 'module-03-grid-driving/lesson-02-driving-multiple-intersections',
    'title': 'Driving Multiple Intersections',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Drive through one intersection to reach the next',
             'Use a `for` loop to drive a chosen number of intersections',
             'Write `drive_intersections(count)` from its docstring, test it, and use it',
         ],
         'notes': '40 to 50 minutes. The loop itself is short: the heart of the lesson is tracing '
                  'where the robot is after each pass.'},

        {'kind': 'bullets', 'title': 'From the first intersection to the third',
         'bullets': [
             'Reaching the **first** intersection is easy',
             'Reaching the **third** is the same call, three times',
             'That is what a `for` loop is for',
             'Today "arrive at an intersection" becomes a building block you can repeat a chosen number of times',
         ],
         'callout': 'The first real **function** in the GRID DRIVING section',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Add to robot.py: this lesson\'s skeleton (1 of 2)',
         'lead': 'Paste it above `RUN`, at the end of the GRID DRIVING section. First, one function '
                 'outline:',
         'lead_h': 0.75,
         'code': '# --- Lesson 3-2: a run of intersections ---\n'
                 '# drive_intersections(count) is track_to_intersection() in a\n'
                 '# loop.\n'
                 '# It ends parked on the count-th intersection, so Lessons 3-3\n'
                 '# and 3-4 build every path out of it and the two turns.\n'
                 '\n'
                 'def drive_intersections(count):\n'
                 '    """Arrive at count intersections in a row, printing\n'
                 '    which one it is each time. Ends parked on the last one\n'
                 '    with the sensors past it, ready to turn or to go on."""\n'
                 '    pass',
         'code_size': 18,
         'notes': 'The skeleton on the lesson page is one block: this slide and the next split it '
                  'in two to fit.'},

        {'kind': 'code', 'title': 'Add to robot.py: this lesson\'s skeleton (2 of 2)',
         'lead': 'Then two tests, right under the function:',
         'lead_h': 0.7,
         'code': 'def test_two_by_hand():\n'
                 '    # track_to_intersection() written out twice, no loop: the\n'
                 '    # robot should end parked on the SECOND intersection\n'
                 '    pass\n'
                 '\n'
                 'def test_drive_run():\n'
                 '    # drive_intersections(3), then print that it is done\n'
                 '    pass',
         'code_size': 20,
         'callout': 'One function outline and two tests',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'A docstring, not step comments',
         'bullets': [
             'The function has a **docstring** (Lesson 1-12) instead of step comments',
             'The string under the `def` line says what the function does and what ends it',
             'That\'s all the help you get: the steps are yours to work out',
             'Keep the docstring when you write the body: it belongs to the function',
         ],
         'callout': 'This lesson tells you enough to write it',
         'tone': 'orange'},

        {'kind': 'bullets', 'title': 'Drive a set number with a `for` loop',
         'bullets': [
             'Two calls in a row reach two intersections: each one ends with the sensors **past** the tape (Lesson 2-8), so the next has a line to follow',
             'Writing the call out by hand for each intersection is repetitive, and wrong the moment you want a different number',
             'A `for` loop over `range(count)` repeats it a chosen number of times',
             'Same shape as `polygon()` in Module 1: a loop and a count, packaged into a function '
             'with the count as its parameter',
             'Nothing in the loop body changes from pass to pass. The loop variable is only good for the print ("Intersection 1 of 3"), and it starts at 0',
         ],
         'size': 23,
         'callout': 'No special case for the last intersection: each call ends with the robot\'s '
                    'center on the cross, exactly where you want to be',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'After two `track_to_intersection()` calls in a row, where is the robot?',
         'options': ['Halfway between the second and third intersections',
                     'Parked with its center on the second intersection, sensors just past it',
                     'On the first intersection',
                     'It depends on the battery'],
         'answer': 1,
         'explanation': 'Each call ends with the robot\'s center on the cross the sensors just found. '
                        'Two calls, two intersections, and the robot is sitting on the second one, '
                        'which is why there is no special case for the last intersection.',
         'notes': 'Answer: B. Older versions of this lesson taught a timed nudge after each '
                  'intersection, with an if i < count - 1 guard to skip it on the last one. '
                  'track_to_intersection() now ends with the robot\'s center on the cross, so there '
                  'is nothing to skip. Walk the loop with i = 0, 1, 2 on the board and have students '
                  'say where the robot is after each pass.'},

        {'kind': 'frames', 'title': 'Activity · Two by hand, then the helper',
         'tag': 'Activity',
         'figure': '/img/lesson-m3-02/drive-run.svg',
         'crop': (0.02, 0.09, 0.57, 1.0),
         'frames': [(0.35, '**Step 1:** two calls reach the second intersection'),
                    (0.95, '**Step 2:** `drive_intersections(3)` reaches the third')],
         'callout': 'Every step starts on a line segment, facing the next intersection, with at '
                    'least three intersections ahead',
         'tone': 'teal',
         'notes': 'On the lesson page this is one animation of both tests, with the step running '
                  'highlighted beside the grid. These are the end of each step.'},

        {'kind': 'steps', 'title': 'Step 1 · test_two_by_hand()',
         'steps': [
             'Write the body: `track_to_intersection()` twice, no loop, and a print at the end',
             'Set the run line to `test_two_by_hand()` and run',
             'It should end parked on the **second** intersection. Don\'t go on until it does',
         ],
         'notes': 'More support: step 1 already has students write two intersections by hand, two '
                  'calls, before the loop; some will need to trace it on the board with i = 0, 1, 2 '
                  'before they write the function.'},

        {'kind': 'steps', 'title': 'Step 2 · drive_intersections(count)',
         'steps': [
             'Write the function from its docstring: one parameter, a `for` loop over it, '
             '`track_to_intersection()` inside, and a print so you can follow along',
             'Write the body of `test_drive_run()`: one call, `drive_intersections(3)`, and a print',
             'Set the run line to `test_drive_run()` and run. It should arrive three times, '
             'printing each one, and end parked on the third intersection',
         ],
         'callout': 'Then `drive_intersections(4)` drives four segments in one clean line: the '
                    'building block of the next two lessons',
         'tone': 'green',
         'notes': 'The lesson has a closed reveal with the function; students write and test theirs '
                  'first. If a student\'s version has an if in it, ask what it is guarding against. '
                  'Class-track students call the tracker inside the helper; the helper itself stays '
                  'a plain function in this section. More challenge: a speed parameter that changes '
                  'BASE_EFFORT before the loop and restores it after (needs global, Lesson 2-7), or '
                  'a running count checked against the grid.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Elevators', 'Floor counting', 'An elevator counts floor sensors as it rises and stops '
                                             'on the Nth: same detect-and-count idea.'),
             ('Manufacturing', 'Indexing lines', 'Assembly lines advance a fixed number of steps '
                                                 'between stations, clearing each position.'),
             ('Transit', 'Counting stops', 'Automated shuttles track how many stops they\'ve passed '
                                           'to know when to pull over.'),
         ]},

        {'kind': 'wrapup',
         'questions': [
             'What loop drives a set number of segments?',
             'Where is the robot after the last pass?',
         ],
         'next': 'turns, and L-shaped paths across the grid',
         'notes': 'Answers: a for loop over range(count), with track_to_intersection() inside. '
                  'Parked on the last intersection: every track ends with the robot\'s center on '
                  'the cross. Formative: drive exactly N intersections with a loop. Exit ticket: '
                  '"Why is there no special case for the last intersection?" (every track ends with '
                  'the robot\'s center on the cross, not past it).'},
    ],
}
