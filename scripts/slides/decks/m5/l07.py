DECK = {
    'module': 5, 'lesson': 7,
    'doc': 'module-05-pathfinding/lesson-07-obstacle-detection',
    'title': 'Obstacle Detection',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Add the **rangefinder** to the start of `robot.py` and read a distance',
             'Explain how an ultrasonic rangefinder measures distance',
             'Use a **threshold** to decide whether the intersection ahead is blocked',
             'Say which intersection a reading refers to, and why the path already tells you',
             'Write a driving test: Module 4\'s `drive_path()` loop plus **one rangefinder check** that re-plans',
         ],
         'notes': '60 minutes, robot required. The planner was tested on screen in Lesson 5-6 and '
                  'nothing about it changes today. The only new thing is detection: look before '
                  'you drive, and if something is there, call add_blocked() and ask for a new '
                  'path. The last objective on the page adds: first with a simulated sensor, then '
                  'the real one.'},

        {'kind': 'bullets', 'title': 'The robot fills in the blocked list',
         'bullets': [
             'Until now you filled it in **by hand**, in a test',
             'Today the robot does it, with the **ultrasonic rangefinder**',
             'Look before you drive. Something there? Call `add_blocked()` and re-plan',
             'The planner doesn\'t change',
         ],
         'callout': 'New, last section of `robot.py`: **OBSTACLES**',
         'tone': 'teal',
         'notes': 'add_blocked() is the same call the students\' tests made. The only new thing '
                  'today is detection.'},

        {'kind': 'bullets', 'title': 'The robot gets eyes',
         'bullets': [
             'Sends a **sound pulse**, too high for us to hear',
             'Times the **echo**',
             'Round-trip time gives the distance, in **centimeters**',
         ],
         'callout': 'The sensor does the physics. You just read a number.',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Reading it takes three lines',
         'code': 'from XRPLib.rangefinder import Rangefinder\n'
                 '\n'
                 'rangefinder = Rangefinder.get_default_rangefinder()\n'
                 'distance = rangefinder.distance()      # float, in cm',
         'code_size': 24,
         'callout': 'The first two lines go in the **start block**: the import under the other '
                    '`XRPLib` imports, the object under `board = ...`',
         'tone': 'teal',
         'notes': 'Putting rangefinder in the start block means every function can use it the way '
                  'it uses drivetrain. It is the first new object in the start block since Lesson '
                  '2-1 (the only other change was import random in 2-4).'},

        {'kind': 'check',
         'question': 'How does an ultrasonic rangefinder measure distance?',
         'options': ['It uses a camera to estimate size',
                     'It sends a sound pulse and times how long the echo takes to return',
                     'It counts wheel rotations',
                     'It reads a GPS signal'],
         'answer': 1,
         'explanation': 'Sound pulse out, echo back, time it: that round-trip time converts to a '
                        'distance. The XRP returns it in centimeters.'},

        {'kind': 'bullets', 'title': 'Choosing a threshold',
         'bullets': [
             'Readings are **noisy**, so use a **threshold**, not an exact distance',
             'Measure **blocked** (~12 cm) and **clear** (~50 cm)',
             'Pick a cutoff **between** them',
         ],
         'split': 0.52,
         'code': 'if distance < OBSTACLE_CM:\n'
                 '    print("OBSTACLE DETECTED")\n'
                 'else:\n'
                 '    print("Path is clear")',
         'code_size': 20,
         'callout': 'Not `THRESHOLD`: the file already has the reflectance one (Lesson 2-2)',
         'notes': 'Two settings with one name is a bug waiting to happen. Calibrate the threshold ahead of class and have a value ready: it depends on grid '
                  'spacing, obstacle material and the sensor. Soft or angled surfaces read '
                  'inconsistently, which is a good real-world-sensor talking point.'},

        {'kind': 'check',
         'question': 'Why use a threshold instead of checking for an exact distance?',
         'options': ['Exact distances are illegal',
                     'Sensor readings vary slightly (noise), so a cutoff is more reliable than an exact match',
                     'To make the robot slower',
                     'Thresholds use less memory'],
         'answer': 1,
         'explanation': 'Readings vary with angle, surface and noise. A threshold ("closer than '
                        '15 cm = blocked") absorbs that; an exact match would fail constantly.'},

        {'kind': 'code', 'title': 'Add to robot.py: the OBSTACLES section',
         'lead': 'Above `RUN`, after the BFS PLANNER section. It drives, so its tests wait for '
                 'the button **twice**.',
         'lead_h': 0.95,
         'code': '# ===== OBSTACLES =====\n'
                 '# The robot fills BLOCKED itself. Before each step of a path\n'
                 '# the rangefinder looks at the intersection ahead; if there is\n'
                 '# something, add_blocked() tells the BFS PLANNER (the call the\n'
                 '# 5-6 harness made) and a new path is planned from where the\n'
                 '# robot stands. Facing and driving are the NAVIGATOR\'s job.\n'
                 'OBSTACLE_CM = 15                         # closer than this = blocked\n'
                 'SIMULATED_OBSTACLES = [(2, 0), (2, 2)]   # pretend obstacles, for a dry run\n'
                 '\n'
                 'def simulate_rangefinder(next_pos):\n'
                 '    """Stand-in for rangefinder.distance(): 8.0 if next_pos is\n'
                 '    in SIMULATED_OBSTACLES, otherwise 50.0."""\n'
                 '    pass',
         'code_size': 17,
         'notes': 'It is the file\'s last section. Like the NAVIGATOR, it drives. Two tests go under it, both the students\' to '
                  'write: test_rangefinder() in Step 1, and test_detect_once(), whose outline is '
                  'two slides on.'},

        {'kind': 'code', 'title': 'Which intersection is blocked?',
         'lead': 'The one **directly in front** of the robot, and the loop already knows it:',
         'lead_h': 0.95,
         'code': 'for next_pos in path:\n'
                 '    desired_heading = get_desired_heading(current_position, next_pos)\n'
                 '    current_heading = turn_to(current_heading, desired_heading)\n'
                 '    track_to_intersection()\n'
                 '    current_position = next_pos',
         'code_size': 22,
         'callout': 'After `turn_to()`, the robot **faces** `next_pos`. A short reading then means '
                    '`next_pos` is blocked.',
         'tone': 'teal',
         'notes': 'This is Module 4\'s drive_path() loop. The path already told you which '
                  'intersection is blocked. Facing next_pos is what turning to the desired heading '
                  'means, so no new code is needed to know which intersection is blocked. "Which intersection is blocked" '
                  'used to confuse students when it was computed from the heading. Demonstrate the '
                  'new reasoning physically: stand on an intersection, turn to face the next one on '
                  'the path, point at it.'},

        {'kind': 'figure', 'title': 'Parked, and facing next_pos',
         'figure': '/img/lesson-m5-07/rangefinder-ahead-xy-v2.svg',
         'caption': 'The robot is parked and facing `next_pos`, so a short reading can only mean '
                    '`next_pos`.',
         'notes': 'Left: the robot on (1, 0), turned east toward next_pos (2, 0), where an obstacle sits. '
                  'Right: the reading scale with the cutoff at OBSTACLE_CM = 15. An obstacle on the next '
                  'intersection reads about 12 cm, nothing there about 50 cm.'},

        {'kind': 'check',
         'question': 'The robot is at (2,1), has just turned to face the next step on its path, '
                     '(1,1), and the rangefinder reads 8 cm. Which intersection is blocked?',
         'options': ['(2,1): where the robot is',
                     '(1,1): the next step on the path, which the robot is now facing',
                     '(3,1)',
                     'It depends on the heading number'],
         'answer': 1,
         'explanation': '`turn_to(current_heading, desired_heading)` pointed the robot at `next_pos`. Whatever the '
                        'sensor sees now is at `next_pos`. The robot sits on a clear intersection; '
                        'the obstacle is the one it faces.'},

        {'kind': 'code', 'title': 'The loop: Module 4\'s, plus one check',
         'code': 'def test_detect_once():\n'
                 '    # robot at (0, 0) facing North; destination (3, 3)\n'
                 '    # plan the path, print it, wait for the button\n'
                 '    # for each next_pos in path:\n'
                 '    #     face it: get_desired_heading(), then turn_to()\n'
                 '    #     NEW: look ahead -- distance = simulate_rangefinder(\n'
                 '    #          next_pos) for now; rangefinder.distance() later\n'
                 '    #     print current_position, HEADING_NAMES[current_heading], the distance\n'
                 '    #     if distance < OBSTACLE_CM:\n'
                 '    #         tell the planner: add_blocked(next_pos); say so\n'
                 '    #         new path from HERE: compute_bfs_path(current_position,\n'
                 '    #             destination); print it; then break\n'
                 '    #     else:\n'
                 '    #         arrive: track_to_intersection();\n'
                 '    #         current_position = next_pos\n'
                 '    # print the blocked list\n'
                 '    pass',
         'code_size': 16,
         'notes': 'Students write it as test_detect_once() under the skeleton. Today\'s driving test is drive_path()\'s loop with exactly one step added, '
                  'between turning and driving: look ahead. Everything else is Module 4\'s drive_path().'},

        {'kind': 'code', 'title': 'The new branch',
         'lead': 'The one piece that isn\'t Module 4\'s `drive_path()`:',
         'lead_h': 0.65,
         'code': '        if distance < OBSTACLE_CM:\n'
                 '            add_blocked(next_pos)\n'
                 '            print("Obstacle at", next_pos, "! Rerouting...")\n'
                 '            path = compute_bfs_path(current_position, destination)\n'
                 '            print("New path:", path)\n'
                 '            break      # Lesson 5-8 keeps going instead',
         'code_size': 20,
         'callout': 'The `break` ends the loop: today the robot re-plans **once** and stops',
         'tone': 'teal',
         'notes': 'Lesson 5-8 replaces that break with "follow the new path, and keep going until '
                  'you arrive."'},

        {'kind': 'bullets', 'title': 'Three things to notice',
         'bullets': [
             '`add_blocked(next_pos)` is **the same call** as the Lesson 5-6 harness',
             ['Pass those tests, and it re-plans correctly'],
             'Re-planning is **one line**, from where the robot is',
             ['The planner rebuilds its graph from `BLOCKED` every call'],
             'The robot is **parked** when it re-plans',
         ],
         'size': 24,
         'notes': 'The planner can\'t tell a test script from a sensor. The re-plan is '
                  'compute_bfs_path(current_position, destination), Rule 1 from Lesson 5-4, and there is no '
                  '"rebuild the graph" step to forget. Every track ends with the robot\'s center on '
                  'the cross, so the robot is still on the intersection it re-planned from. '
                  'Nothing moves the robot during a re-plan. Class track: if students built the '
                  'LineTrack or Navigator class, the driving calls are tracker. or '
                  'navigator.line_track. calls, as in Lesson 4-6, and the planner calls are '
                  'planner.add_blocked() and planner.compute_path().'},

        {'kind': 'check',
         'question': 'When the robot detects a new obstacle, what does it do to reroute?',
         'options': ['Stops permanently',
                     'Calls `add_blocked(next_pos)`, then `compute_bfs_path(current_position, destination)` from where it is',
                     'Reverses back to the start',
                     'Ignores it and drives through'],
         'answer': 1,
         'explanation': 'Detecting an obstacle means reroute, not stop. `add_blocked` tells the '
                        'planner; `compute_bfs_path` from the current position returns a path around '
                        'it, because the planner rebuilds its graph from `BLOCKED` on every call.'},

        {'kind': 'check',
         'question': 'Why does the robot not need a separate "rebuild the graph" step after '
                     '`add_blocked()`?',
         'options': ['Because `compute_bfs_path` builds the graph from `BLOCKED` every time it is called',
                     'Because the graph is never rebuilt: obstacles are checked while driving',
                     'Because `add_blocked` rebuilds the graph itself',
                     'It does need one: the code above is missing it'],
         'answer': 0,
         'explanation': 'Lesson 5-4 put `build_graph()` inside the planner precisely so that a wall '
                        'found at step 3 is already missing from the graph used at step 4.'},

        {'kind': 'code', 'title': 'Print the plan before the button',
         'lead': 'A new habit: plan and **print** the path, then wait for the button before the '
                 'robot moves.',
         'lead_h': 0.95,
         'code': '    path = compute_bfs_path(current_position, destination)\n'
                 '    print("Planned path:", path)\n'
                 '\n'
                 '    board.wait_for_button()',
         'code_size': 22,
         'callout': 'Path right, robot wrong? The bug is in the **driving**.',
         'tone': 'teal',
         'notes': 'Read it before pressing the button: is it what you expected? Printing the plan '
                  'before you drive is a paper test built into every run, and the first diagnostic. '
                  'That makes two presses per driving test: the one in RUN starts the test and '
                  'prints the plan; the one in the test is go.'},

        {'kind': 'steps', 'title': 'Step 1 · The sensor',
         'steps': [
             'Add the import and the object to the **start block**',
             'Write `test_rangefinder()`: print `rangefinder.distance()` 50 times, 0.1 s apart',
             'Run it. Hold an obstacle at the next intersection\'s distance, then remove it',
             'Check `OBSTACLE_CM` sits **between** the readings',
         ],
         'size': 20,
         'notes': 'test_rangefinder() works the way test_sensors() did in Lesson 2-1. Students '
                  'write both readings down and change OBSTACLE_CM if it is not between them. Have '
                  'your own calibrated value ready to compare against.'},

        {'kind': 'steps', 'title': 'Step 2 · Simulate the sensor',
         'steps': [
             'Write `simulate_rangefinder()`: `8.0` if `next_pos` is in `SIMULATED_OBSTACLES`, else `50.0`',
             'Write `test_detect_once()`, with the **simulated** sensor',
             'Robot at `(0, 0)` facing North, **empty** grid',
             'It should drive to `(1, 0)`, "see" `(2, 0)`, re-plan, and stop',
         ],
         'size': 20,
         'callout': 'Check: the blocked list **grew**; the new path goes **around**',
         'tone': 'teal',
         'notes': 'Before the second press, check that (2, 0) is on the planned path. The robot '
                  'faces East, drives to (1, 0), faces (2, 0), sees the pretend obstacle, prints the new '
                  'path, and stops. Only the sensor is simulated. The planner needs no simulation: it was tested in '
                  'Lesson 5-6. Have everyone run this before touching an obstacle: the robot still '
                  'drives, but the obstacle is pretend, so a wrong reroute is a logic bug and '
                  'nothing else. Separating software bugs from hardware bugs saves enormous '
                  'frustration.'},

        {'kind': 'steps', 'title': 'Step 3 · The real sensor',
         'steps': [
             'Change the look-ahead line to `rangefinder.distance()`',
             'Put an obstacle on the printed path: `(2, 0)` again works',
             'Press the button. It should stop, print "Rerouting..." and the new path',
         ],
         'callout': 'Taking the new path is next lesson',
         'tone': 'teal',
         'notes': 'Place real obstacles on the printed path so the reroute is visible and dramatic. '
                  'Hardware note: the driving functions are Module 4\'s, unchanged: turns end on a sensor, '
                  'and track_to_intersection() parks the robot\'s center on each intersection. If the robot '
                  'overshoots or misses a turn here, it did in Module 4 too; tune there. The lesson '
                  'page has a closed reveal with a finished test_detect_once() for students to '
                  'check against after they run it; it is not on the slides.'},

        {'kind': 'check',
         'question': 'Why test with a simulated rangefinder before using the real one?',
         'options': ['The real sensor never works',
                     'To verify the reroute logic in software first, separating code bugs from hardware bugs',
                     'Simulation is required by Python',
                     'To avoid writing the loop'],
         'answer': 1,
         'explanation': 'A simulated sensor proves the detection logic on screen. After that, '
                        'real-sensor problems are hardware, not logic. The planner was already '
                        'proven in Lesson 5-6.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Cars', 'Self-driving', 'Radar and LIDAR detect obstacles; the planner reroutes in '
                                      'real time.'),
             ('Warehouses', 'Fulfillment robots', 'Robots sense blocked aisles and replan on the fly.'),
             ('Space', 'Mars rovers', 'Rovers scan the terrain ahead and reroute around rocks.'),
         ],
         'notes': 'Sense, decide, act is the loop behind every autonomous machine.'},

        {'kind': 'wrapup',
         'questions': [
             'What three lines read the rangefinder?',
             'Which intersection does an obstacle reading refer to?',
             'What is the one line that tells the planner?',
             'Why is there no "rebuild the graph" step?',
         ],
         'next': 'keep going until you arrive, and remember what you found',
         'notes': 'Answers: the import, get_default_rangefinder(), .distance(). next_pos: the robot '
                  'just turned to face it. add_blocked(next_pos), the same call the tests used. '
                  'The planner rebuilds from BLOCKED on every call. Exit ticket: "Why can the '
                  'planner not tell a sensor from a test script?" (Both call add_blocked().) '
                  'Preview: the break becomes a while loop that keeps re-planning until the robot '
                  'arrives, and the robot prints what it found so the next run starts out knowing it.'},
    ],
}
