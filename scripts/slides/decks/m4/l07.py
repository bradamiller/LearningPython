DECK = {
    'module': 4, 'lesson': 7,
    'doc': 'module-04-manhattan/lesson-07-final-project',
    'title': 'Final Project',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Integrate the planner and the driving functions in one program: the last test function in `robot.py`',
             'Build the program in three tested steps: one leg, two legs, then a loop over a list of destinations',
             'Carry the robot\'s pose (`position` and `heading`) from one leg into the next by assigning from `drive_path()`',
             'Demonstrate a working multi-destination run on the XRP',
         ],
         'notes': 'Multi-day project. Keep the intro brief: this is a build-and-test day. For '
                  '50-minute periods plan two days: steps 1 and 2, then the full run.'},

        {'kind': 'bullets', 'title': 'The mission: a delivery drone on a city grid',
         'bullets': [
             'Start at home base, **(0,0)**, visit four destinations **in order**, and end back home',
             'Compute a fresh path for each leg, and drive it autonomously',
             '`compute_manhattan_path(position, dest)` returns the list of intersections',
             '`drive_path(path, position, heading)` turns and drives it',
         ],
         'callout': 'Your job: the **main program** that connects them. About ten lines, and like every '
                    'program in this course it is a test function at the bottom of `robot.py`.',
         'tone': 'teal',
         'notes': 'Everything comes together: students already built every piece.'},

        {'kind': 'bullets', 'title': 'Four destinations, four lists of single hops',
         'bullets': [
             '`DESTINATIONS` is the supplied list: four stops, each **several intersections** from the last',
             'The main program sends **one destination at a time** to `compute_manhattan_path()`',
             'Each call returns a list of **adjacent** intersections: 2, 3, 2 and 3 hops here',
             '`drive_path()` drives that list one hop at a time, then the next destination is planned '
             'from where it stopped',
         ],
         'callout': 'Destinations say where to go; each path says every intersection on the way',
         'tone': 'teal',
         'notes': 'Ask students to say the first path out loud before running: from (0, 0) to (2, 0) it '
                  'is [(1, 0), (2, 0)].'},

        {'kind': 'frames', 'title': 'The whole run, driven',
         'figure': '/img/lesson-m4-07/delivery-drive.svg',
         'crop': (0.0, 0.07, 0.6, 1.0),
         'frames': [(0.2, 'Leg 2 is planned from (2, 0), where leg 1 ended'),
                    (0.3, 'Three right turns to face North'),
                    (0.9, 'Leg 4 drives home')],
         'callout': '2, 3, 2 and 3 steps. Each leg is planned from where the last one ended. `turn_to()` only turns clockwise, '
                    'so most legs start with three right turns.',
         'tone': 'teal',
         'notes': 'On the lesson page this is an animation of the whole run, with Back, Step and '
                  'Play/Pause buttons and the main loop in plain '
                  'words beside it and the running line highlighted; these are three moments from it, '
                  'with the side panel cropped off. Leg 1 is one right turn and two steps east; legs '
                  '2, 3 and 4 each start with three right turns.'},

        {'kind': 'code', 'title': 'Add to robot.py: the delivery run',
         'lead': 'Paste above `RUN`, at the end of the NAVIGATOR section. No new function is defined: '
                 'one setting and the project\'s test, which you build in three steps.',
         'lead_h': 0.95,
         'code': '# --- Lesson 4-7: final project, the delivery run ---\n'
                 '# The module project: visit DESTINATIONS in order, planning\n'
                 '# each leg with the MANHATTAN PLANNER from wherever the last\n'
                 '# leg ended and driving it with the NAVIGATOR. Nothing new is\n'
                 '# defined; the two sections did the work. Built in three\n'
                 '# tested steps: one leg, two legs, then a loop.\n'
                 'DESTINATIONS = [(2, 0), (2, 3), (0, 3), (0, 0)]',
         'code_size': 18,
         'notes': 'The skeleton continues on the next slide with test_delivery(), the graded work.'},

        {'kind': 'code', 'title': 'Add to robot.py: test_delivery()',
         'code': 'def test_delivery():\n'
                 '    # position and heading start at home, facing North\n'
                 '    # plan the FIRST leg and print it; wait for the button\n'
                 '    # for each destination:\n'
                 '    #     compute the path from where the robot is\n'
                 '    #     print it\n'
                 '    #     drive it\n'
                 '    #     ... and keep position and heading up to date\n'
                 '    #     print where the robot arrived\n'
                 '    pass',
         'code_size': 21,
         'callout': 'The second leg decides whether the project works. What does the test know after the '
                    'first `drive_path()` finishes, and what doesn\'t it, unless you ask?',
         'callout_size': 20,
         'tone': 'orange',
         'notes': 'There is no student reveal for it; the solution is the teacher copy only. '
                  'The line nearly everyone gets half right: they call drive_path and throw the return '
                  'value away. Leg one works perfectly, and every later leg is planned from (0,0) facing '
                  'North. If a robot drives a sensible first route and then wanders, ask what position is '
                  'in their main program after leg 1.'},

        {'kind': 'bullets', 'title': 'Only the first leg is printed before the button',
         'bullets': [
             'Lesson 4-6\'s habit, plan, print, button, drive, with one limit',
             'The main program prints the path for **leg 1** before the button',
             'It can\'t print legs 2, 3 and 4 yet: each is planned from wherever the previous leg **actually** finished',
             'Instead, each leg is printed as it\'s planned, just before the robot drives it',
             'The heading carries over too: leg 1 ends facing East, so leg 2 starts facing East',
         ],
         'callout': 'In Module 5, where obstacles can appear mid-run, this becomes the only way it could work',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'Why does the program print the plan for leg 1 before the button, but not for legs 2 to 4?',
         'options': ['print() can only be called once before wait_for_button()',
                     'Later legs start where the previous leg ends, known only once the robot gets there',
                     'Leg 1 is the only one that uses compute_manhattan_path',
                     'To save battery'],
         'answer': 1,
         'explanation': 'Each leg is planned from the robot\'s current position. Leg 1 is the only one whose '
                        'starting position is known before the robot moves.'},

        {'kind': 'steps', 'title': 'Activity · Build it in three steps',
         'lead': 'All three steps are in `test_delivery()`. Test each one on the robot before you start the '
                 'next, starting the robot at (0, 0) facing North every time.',
         'lead_h': 0.9,
         'steps': [
             '**One leg.** Plan the path from (0, 0) to (2, 0), print it, wait for the button, drive it, '
             'print where the robot arrived: Lesson 4-6\'s `test_drive_path()` with (2, 0). Read the printed '
             'path, `[(1, 0), (2, 0)]`, then press. One right turn; it stops on (2, 0) facing East',
             '**Add the second leg** to the same function: plan to (2, 3), print, drive, print. It works only '
             'if `position` and `heading` were assigned from the first `drive_path()`. After (2, 0): three '
             'right turns to face North, then up to (2, 3)',
             '**A list and a loop.** The two legs are the same lines twice: replace them with one loop over '
             '`DESTINATIONS`, as the outline describes. The robot should visit all four destinations and '
             'finish at home, with legs of 2, 3, 2 and 3 steps',
         ],
         'size': 19,
         'notes': 'Push step-by-step testing hard: the students who write everything at once and can\'t '
                  'find the break are the ones who skipped the one-leg and two-leg steps. Watch battery '
                  'drain on long multi-turn runs and charge between attempts. For 50-minute periods, plan '
                  'two days: steps 1 and 2, then the full run.'},

        {'kind': 'check',
         'question': 'On the second leg the robot drives a clearly wrong path. What\'s the first thing to check?',
         'options': ['The battery voltage',
                     'Whether position and heading were assigned from drive_path after leg 1',
                     'The color of the grid lines', 'The HEADING_NAMES list'],
         'answer': 1,
         'explanation': 'A wrong path on leg 2 or later almost always means the return value was dropped, so '
                        'leg 2 was planned from (0,0) facing North. The printed path for leg 2 confirms it.'},

        {'kind': 'table', 'title': 'The rubric',
         'lead': 'You\'re graded on the whole system working together.',
         'headers': ['Category', 'Points', 'What it takes'],
         'widths': [2.4, 1.1, 8.0],
         'rows': [
             ['Planner', '10', '`compute_manhattan_path` correct for any position and destination; Lesson 4-4 tests pass'],
             ['Driving functions', '15', 'Correct `get_desired_heading`, `turn_to`, `drive_path`; parked on the cross at every arrival; position and heading returned'],
             ['Main program', '10', '`test_delivery()`: 4+ destinations, prints leg 1 before the button, drives each leg, assigns `position, heading` from `drive_path`'],
             ['Robot demo', '10', 'Physically visits all destinations with correct turns'],
             ['Planning & docs', '5', 'Planning worksheet, a hand-trace of one leg, testing checklist followed'],
         ],
         'size': 20,
         'notes': 'Class track: students who did the '
                  'extensions run the project on their objects, navigator.drive_path(path) and '
                  'planner.compute_path() if they built Manhattan. The step tests change the same way. '
                  'Same rubric.'},

        {'kind': 'bullets', 'title': 'If you finish early',
         'bullets': [
             'A round trip: destinations forward, then reversed',
             'Let the user type the destinations',
             'Count total intersections driven and turns made across the whole journey',
             'Or the Lesson 4-6 class extension: a `Navigator` object, so the main loop has nothing to pass back and forth',
         ],
         'notes': 'Class-track students drive with navigator.drive_path(path) and read navigator.position; '
                  'there is no return value to drop, which is the point of the Lesson 4-6 side-by-side. '
                  'It is the first time the encapsulation pays off in a whole program.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Logistics', 'Delivery routing', 'Warehouse and delivery robots compute a route to each stop, '
                                               'drive it, then re-plan from the new location: exactly this loop.'),
             ('Rideshare', 'Multi-stop trips', 'Navigation apps chain legs together, recomputing from your '
                                               'current position at each waypoint.'),
             ('Space', 'Rover missions', 'Planetary rovers plan a path to a target, execute carefully, and '
                                         're-plan, with the same separation of planning and driving.'),
         ],
         'height': 3.9,
         'notes': 'The plan-then-execute structure students just built is fundamental to real autonomous '
                  'systems.'},

        {'kind': 'wrapup',
         'questions': [
             'What\'s the one line that makes multi-leg journeys work?',
             'Why is only leg 1 printed before the button?',
             'What were the three steps?',
             'Where did problem decomposition pay off?',
         ],
         'next': 'Module 5: breadth-first search replaces the planner, and drive_path keeps driving',
         'notes': 'Answers: position, heading = drive_path(path, position, heading), for each leg. Later legs '
                  'are planned from where the robot actually ends up. One leg, two legs, then a loop over '
                  'a list. Each part was built and tested alone, so the main program that connects them is '
                  'about ten lines, and a printed path tells you which part to open when a run goes wrong. '
                  'When a robot finishes the whole sequence, let the class watch: it is the '
                  'payoff of eight lessons. Name what they built across Module 4: coordinates and tuples, '
                  'lists and iteration, algorithm design, a planner and a driver that know nothing about '
                  'each other, a testing discipline, hardware integration. In Module 5 BFS replaces the '
                  'Manhattan planner and drive_path keeps driving unchanged: the reward for keeping the '
                  'two concerns separate.'},
    ],
}
