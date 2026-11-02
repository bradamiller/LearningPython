DECK = {
    'module': 3, 'lesson': 2,
    'doc': 'module-03-grid-driving/lesson-02-driving-multiple-intersections',
    'title': 'Driving Multiple Intersections',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Explain why `track_to_intersection()` called twice in a row would not move the robot '
             'without `drive_past_intersection()` between them',
             'Drive past one intersection to reach the next',
             'Use a `for` loop to drive a chosen number of intersections',
             'Write `drive_intersections(count)` from its docstring, test it, and use it',
         ],
         'notes': '40 to 50 minutes. The thought experiment at the top is the heart of the lesson; '
                  'the loop itself is short.'},

        {'kind': 'bullets', 'title': 'From the first intersection to the third',
         'bullets': [
             'Reaching the **first** intersection is easy',
             'Reaching the **third** is the same two calls, three times',
             'That is what a `for` loop is for',
             'Today "arrive at an intersection" becomes a building block you can repeat',
         ],
         'callout': 'The first real **function** in the GRID DRIVING section',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Add to robot.py: this lesson\'s skeleton (1 of 2)',
         'lead': 'Paste it above `RUN`, at the end of the GRID DRIVING section. First, one function '
                 'outline:',
         'lead_h': 0.75,
         'code': '# --- Lesson 3-2: a run of intersections ---\n'
                 '# drive_intersections(count) is the arrival pair in a loop.\n'
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
                 '    # the arrival pair written out twice, no loop: the robot\n'
                 '    # should end parked on the SECOND intersection\n'
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

        {'kind': 'code', 'title': 'Why the second call works: a thought experiment',
         'lead': 'Call `track_to_intersection()` twice in a row, with nothing in between. '
                 '**Where does the robot end up?**',
         'lead_h': 1.0,
         'code': 'track_to_intersection()\n'
                 'track_to_intersection()',
         'code_size': 26, 'width': 8,
         'callout': 'Predict before the next slide: does the second call drive anywhere?',
         'tone': 'orange',
         'notes': 'Trace the two calls on the board and have students say why the second one '
                  'returns at once before you show the figure. This is the lesson.'},

        {'kind': 'figure', 'title': 'Track twice, or track, drive past, track',
         'figure': '/img/lesson-m3-02/second-track.svg',
         'frame': 0.65,
         'caption': 'Without the drive-past, the second track starts with its sensors on the cross '
                    'and is finished before it begins. With it, there is a new cross ahead.',
         'notes': 'On the lesson page both runs animate side by side. This is the end: the left '
                  'robot is stuck on the first intersection, the right one is parked on the next.'},

        {'kind': 'bullets', 'title': 'The drive-past\'s second job',
         'bullets': [
             'The first call stops with **both sensors on the cross**',
             'The second call\'s loop condition, `not is_at_cross()`, is already `False`',
             'So the robot "arrives" without moving',
             'The drive-past parks the center of rotation on the intersection, **and** carries the '
             'sensors past the tape',
             'Then the next track has a line to follow and a new cross to find',
         ],
         'size': 24,
         'callout': 'Driving the grid is the arrival pair, repeated: **track, drive past, track, '
                    'drive past, ...**',
         'tone': 'teal',
         'notes': 'Lesson 2-9 mentioned this second job in passing. Because the drive-past parks '
                  'the robot on the intersection, it always ends up sitting on the last one, ready '
                  'to turn.'},

        {'kind': 'check',
         'question': 'Why would a second `track_to_intersection()` call right after the first do '
                     'nothing, without `drive_past_intersection()` between them?',
         'options': ['The function can only be called once',
                     'Sensors still on the cross: `is_at_cross()` is already True, so the loop exits',
                     'The battery needs a rest',
                     'You must call `turn_clockwise()` in between'],
         'answer': 1,
         'explanation': 'After stopping, both sensors are still on the cross. The follow loop only '
                        'runs while NOT at a cross, so it exits at once. `drive_past_intersection()` '
                        'moves the sensors onto plain line first.'},

        {'kind': 'check',
         'question': 'After track, drive past, track, drive past, where is the robot?',
         'options': ['Halfway between the second and third intersections',
                     'Parked with its wheels on the second intersection, sensors just past it',
                     'On the first intersection',
                     'It depends on the battery'],
         'answer': 1,
         'explanation': 'Each drive-past ends with the wheels over the cross the sensors just found. '
                        'Two pairs, two intersections, and the robot is sitting on the second one, '
                        'which is why there is no special case for the last intersection.'},

        {'kind': 'bullets', 'title': 'Drive a set number with a `for` loop',
         'bullets': [
             'Writing the pair out by hand is repetitive, and wrong the moment you want a different number',
             'A `for` loop over `range(count)` repeats the pair a chosen number of times',
             'Same shape as `polygon()` in Module 1: a loop and a count, packaged into a function '
             'with the count as its parameter',
             'Nothing in the loop body changes from pass to pass',
             'The loop variable is only good for the print ("Intersection 1 of 3"), and it starts at 0',
         ],
         'size': 23,
         'callout': 'No special case for the last intersection: the drive-past parks the robot on it',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'A student worries that `drive_past_intersection()` on the last loop pass will '
                     'carry the robot off the final intersection. Are they right?',
         'options': ['Yes: the last pass should skip it',
                     'No: it puts the wheels ONTO the last cross, so the robot ends parked there',
                     'Yes: it should be called twice on the last pass',
                     'It depends on the grid spacing'],
         'answer': 1,
         'explanation': 'The name says what the sensors do, not the wheels. The sensors end up past '
                        'the cross; the wheels end up on it. Every arrival ends the same way, last one '
                        'included.',
         'notes': 'Answer: B. Older versions of this lesson taught a timed nudge after each '
                  'intersection, with an if i < count - 1 guard to skip it on the last one. '
                  'drive_past_intersection() replaces both: a fixed distance that parks the wheels '
                  'on the cross, so there is nothing to skip. Spend the saved time on the thought '
                  'experiment, and walk the loop with i = 0, 1, 2, asking where the robot is after '
                  'each pass.'},

        {'kind': 'frames', 'title': 'Activity · Two by hand, then the helper',
         'tag': 'Activity',
         'figure': '/img/lesson-m3-02/drive-run.svg',
         'crop': (0.02, 0.09, 0.57, 1.0),
         'frames': [(0.35, '**Step 1:** four calls reach the second intersection'),
                    (0.95, '**Step 2:** `drive_intersections(3)` reaches the third')],
         'callout': 'Every step starts on a line segment, facing the next intersection, with at '
                    'least three intersections ahead',
         'tone': 'teal',
         'notes': 'On the lesson page this is one animation of both tests, with the step running '
                  'highlighted beside the grid. These are the end of each step.'},

        {'kind': 'steps', 'title': 'Step 1 · test_two_by_hand()',
         'steps': [
             'Write the body: the arrival pair, then the arrival pair again (four calls, no loop) '
             'and a print at the end',
             'Set the run line to `test_two_by_hand()` and run. It should end parked on the '
             '**second** intersection',
             'Now take out the first `drive_past_intersection()` and run again. Where does it stop? '
             'What does the second track do?',
             'Put the call back. Don\'t go on until the four-call version reaches the second '
             'intersection',
         ],
         'size': 20,
         'notes': 'This step proves the thought experiment on the floor. More support: some '
                  'students need to trace the pair, twice, on the board before they write the loop.'},

        {'kind': 'steps', 'title': 'Step 2 · drive_intersections(count)',
         'steps': [
             'Write the function from its docstring: one parameter, a `for` loop over it, the '
             'arrival pair inside, and a print so you can follow along',
             'Write the body of `test_drive_run()`: one call, `drive_intersections(3)`, and a print',
             'Set the run line to `test_drive_run()` and run. It should arrive three times, '
             'printing each one, and end parked on the third intersection',
         ],
         'callout': 'Then `drive_intersections(4)` drives four segments in one clean line: the '
                    'building block of the next two lessons',
         'tone': 'green',
         'notes': 'The lesson has a closed reveal with the function; students write and test theirs '
                  'first. If a student\'s version has an if in it, ask what it is guarding against, '
                  'and whether drive_past_intersection() actually drives the robot past anything. '
                  'Class-track students call the tracker inside the helper; the helper itself stays '
                  'a plain function in this section. More challenge: a speed parameter that changes '
                  'BASE_EFFORT before the loop and restores it after (needs global, Lesson 2-7), or '
                  'a running count checked against the grid.'},

        {'kind': 'check',
         'question': 'A student\'s `drive_intersections(count)` calls `track_to_intersection()` on '
                     'every pass but `drive_past_intersection()` only on the first. What happens '
                     'with count = 3?',
         'options': ['It works: only the first intersection needs clearing',
                     'Reaches the second, then the third track returns at once: it never gets to the third',
                     'The robot drives past all three',
                     'It turns instead of driving'],
         'answer': 1,
         'explanation': 'Pass 2 ends with the sensors on the second cross and no drive-past. Pass 3\'s '
                        'loop condition is already False, so the robot reports arriving at '
                        'intersection 3 while parked short of the second.'},

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
             'Why does `drive_past_intersection()` have to come between two tracks?',
             'What loop drives a set number of segments?',
             'Where is the robot after the last pass?',
         ],
         'next': 'turns, and L-shaped paths across the grid',
         'notes': 'Answers: the sensors are still on the cross, so the second track would return at '
                  'once. A for loop over range(count), with the arrival pair inside. Parked on the '
                  'last intersection: the drive-past puts the wheels on it. Formative: explain the '
                  'thought experiment, and drive exactly N intersections with a loop. Exit ticket: '
                  '"Why is there no special case for the last intersection?" (the drive-past parks '
                  'on it, not past it).'},
    ],
}
