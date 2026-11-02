DECK = {
    'module': 5, 'lesson': 7,
    'doc': 'module-05-pathfinding/lesson-07-obstacle-detection',
    'title': 'Obstacle Detection',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Add the XRP **rangefinder** to the start of `robot.py` and read a distance',
             'Explain how an ultrasonic rangefinder measures distance',
             'Use a **threshold** to decide whether the intersection ahead is blocked',
             'Say which intersection a reading refers to, and why the path already tells you',
             'Write a driving test: Module 4\'s `drive_path()` loop plus **one rangefinder check**',
         ],
         'notes': '60 minutes, robot required. The planner was tested on paper in Lesson 5-6 and '
                  'nothing about it changes today. The only new thing is detection: look before '
                  'you drive, and if something is there, call add_blocked() and ask for a new '
                  'path. The last objective on the page also says: re-plan when it fires, first '
                  'with a simulated sensor, then the real one.'},

        {'kind': 'bullets', 'title': 'The robot fills in the blocked list',
         'bullets': [
             'Until now the blocked list was filled in **by hand**: by you, in a test',
             'Today the robot fills it in itself, with the **ultrasonic rangefinder**',
             'The planner does not change. The only new thing is **detection**: look before you drive',
             'If something is there, call `add_blocked()` (the exact call your tests made) and ask for a new path',
         ],
         'callout': 'This opens the last section of `robot.py`: **OBSTACLES**',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'The robot gets eyes',
         'bullets': [
             'The rangefinder sends out a **sound pulse**, too high for us to hear',
             'It times the **echo** bouncing back',
             'The round-trip time tells it how far away an object is',
             'It returns that distance in **centimeters**',
         ],
         'callout': 'The sensor does the physics internally. You just read a number.',
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
         'notes': 'Putting rangefinder in the start block means every function below can use it '
                  'the way they use drivetrain. It is the first new object in the start block '
                  'since Lesson 2-1 (the only other change was import random in 2-4).'},

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
             'Readings have **noise**: they vary a little each time',
             'So don\'t check for an exact distance: use a **threshold**',
             'Measure with the next intersection **blocked** (say ~12 cm) and **clear** (say ~50 cm)',
             'Pick a cutoff **between** them',
         ],
         'split': 0.52,
         'code': 'if distance < OBSTACLE_CM:\n'
                 '    print("OBSTACLE DETECTED")\n'
                 'else:\n'
                 '    print("Path is clear")',
         'code_size': 20,
         'callout': 'Why `OBSTACLE_CM` and not `THRESHOLD`? The file already has a `THRESHOLD` '
                    '(the reflectance one from Lesson 2-2). Two settings with one name is a bug '
                    'waiting to happen.',
         'notes': 'Calibrate the threshold ahead of class and have a value ready: it depends on grid '
                  'spacing, obstacle material and the sensor. Soft or angled surfaces read '
                  'inconsistently, which is a good real-world-sensor talking point.'},

        {'kind': 'check',
         'question': 'Why use a threshold instead of checking for an exact distance?',
         'options': ['Exact distances are illegal',
                     'Sensor readings vary slightly (noise), so a cutoff is more reliable than an exact match',
                     'To make the robot slower',
                     'Thresholds use less memory'],
         'answer': 1,
         'explanation': 'Ultrasonic readings fluctuate with angle, surface, and noise. A threshold '
                        '("closer than 15 cm = blocked") absorbs that variation; an exact-match '
                        'check would fail constantly.'},

        {'kind': 'code', 'title': 'Add to robot.py: the OBSTACLES section',
         'lead': 'Paste it above `RUN`, after the BFS PLANNER section. Like the NAVIGATOR, it '
                 'drives, so its tests wait for the button **twice**.',
         'lead_h': 0.95,
         'code': '# ===== OBSTACLES =====\n'
                 '# The robot fills BLOCKED itself. Before each step of a path\n'
                 '# the rangefinder looks at the intersection ahead; if there is\n'
                 '# something, add_blocked() tells the BFS PLANNER (the call the\n'
                 '# 5-6 harness made) and a new path is planned from where the\n'
                 '# robot stands. Facing and driving are the NAVIGATOR\'s job.\n'
                 'OBSTACLE_CM = 15                         # closer than this = blocked\n'
                 'SIMULATED_OBSTACLES = [(2, 0), (2, 2)]   # pretend boxes, for a dry run\n'
                 '\n'
                 'def simulate_rangefinder(next_pos):\n'
                 '    """Stand-in for rangefinder.distance(): 8.0 if next_pos is\n'
                 '    in SIMULATED_OBSTACLES, otherwise 50.0."""\n'
                 '    pass',
         'code_size': 17,
         'notes': 'It is the file\'s last section. Two tests go under it, both the students\' to '
                  'write: test_rangefinder() in Step 1, and test_detect_once(), whose outline is '
                  'two slides on.'},

        {'kind': 'code', 'title': 'Which intersection is blocked?',
         'lead': 'The one **directly in front** of the robot, and you already know which one that '
                 'is. Look at Module 4\'s `drive_path()` loop:',
         'lead_h': 0.95,
         'code': 'for next_pos in path:\n'
                 '    needed = desired_heading(position, next_pos)\n'
                 '    heading = turn_to(heading, needed)\n'
                 '    track_to_intersection()\n'
                 '    drive_past_intersection()\n'
                 '    position = next_pos',
         'code_size': 22,
         'callout': 'After `turn_to()`, the robot is **facing** `next_pos`. A short reading right '
                    'then means `next_pos` is blocked: the path already told you.',
         'tone': 'teal',
         'notes': 'Facing next_pos is what turning to the needed heading means, so no new code is '
                  'needed to know which intersection is blocked. "Which intersection is blocked" '
                  'used to confuse students when it was computed from the heading. Demonstrate the '
                  'new reasoning physically: stand on an intersection, turn to face the next one on '
                  'the path, point at it.'},

        {'kind': 'figure', 'title': 'Parked, and facing next_pos',
         'figure': '/img/lesson-m5-07/rangefinder-ahead-xy.svg',
         'caption': 'The robot is parked and facing `next_pos`, so a short reading can only mean '
                    '`next_pos`.',
         'notes': 'Left: the robot on (1, 0), turned east toward next_pos (2, 0), where a box sits. '
                  'Right: the reading scale with the cutoff at OBSTACLE_CM = 15. A box on the next '
                  'intersection reads about 12 cm, nothing there about 50 cm.'},

        {'kind': 'check',
         'question': 'The robot is at (2,1), has just turned to face the next step on its path, '
                     '(1,1), and the rangefinder reads 8 cm. Which intersection is blocked?',
         'options': ['(2,1): where the robot is',
                     '(1,1): the next step on the path, which the robot is now facing',
                     '(3,1)',
                     'It depends on the heading number'],
         'answer': 1,
         'explanation': '`turn_to(heading, needed)` pointed the robot at `next_pos`. Whatever the '
                        'sensor sees now is at `next_pos`. The robot sits on a clear intersection; '
                        'the obstacle is the one it faces.'},

        {'kind': 'code', 'title': 'The loop: Module 4\'s, plus one check',
         'code': 'def test_detect_once():\n'
                 '    # robot at (0, 0) facing North; destination (3, 3)\n'
                 '    # plan the path, print it, wait for the button\n'
                 '    # for each next_pos in path:\n'
                 '    #     face it: desired_heading(), then turn_to()\n'
                 '    #     NEW: look ahead -- distance = simulate_rangefinder(\n'
                 '    #          next_pos) for now; rangefinder.distance() later\n'
                 '    #     print position, HEADING_NAMES[heading], the distance\n'
                 '    #     if distance < OBSTACLE_CM:\n'
                 '    #         tell the planner: add_blocked(next_pos); say so\n'
                 '    #         new path from HERE: compute_bfs_path(position,\n'
                 '    #             destination); print it; then break\n'
                 '    #     else:\n'
                 '    #         arrive: track_to_intersection(), then\n'
                 '    #         drive_past_intersection(); position = next_pos\n'
                 '    # print the blocked list\n'
                 '    pass',
         'code_size': 16,
         'notes': 'Students write it as test_detect_once() under the skeleton. Today\'s driving test is drive_path()\'s loop with exactly one step added, '
                  'between turning and driving: look ahead. Everything else is Lesson 4-8.'},

        {'kind': 'code', 'title': 'The new branch',
         'lead': 'The one piece that isn\'t Lesson 4-8:',
         'lead_h': 0.65,
         'code': '        if distance < OBSTACLE_CM:\n'
                 '            add_blocked(next_pos)\n'
                 '            print("Obstacle at", next_pos, "! Rerouting...")\n'
                 '            path = compute_bfs_path(position, destination)\n'
                 '            print("New path:", path)\n'
                 '            break      # Lesson 5-8 keeps going instead',
         'code_size': 20,
         'callout': 'The `break` ends the `for` loop as soon as a new path is planned: today the '
                    'robot re-plans **once** and stops',
         'tone': 'teal',
         'notes': 'Lesson 5-8 replaces that break with "follow the new path, and keep going until '
                  'you arrive."'},

        {'kind': 'bullets', 'title': 'Three things to notice',
         'bullets': [
             '`add_blocked(next_pos)` is **the same call** your Lesson 5-6 harness made',
             ['The planner can\'t tell a test script from a sensor: passing the paper tests means it will re-plan correctly'],
             'Re-planning is **one line**, from where the robot is: `compute_bfs_path(position, destination)`',
             ['Rule 1 from Lesson 5-4. The planner rebuilds its graph from `BLOCKED` every call, so there is no "rebuild the graph" step to forget'],
             'The robot is **parked** when it re-plans',
             ['`drive_past_intersection()` runs after every track, so the wheels are still over the intersection it re-planned from'],
         ],
         'size': 24,
         'notes': 'Nothing moves the robot during a re-plan. Class track: if students built the '
                  'LineTrack or Navigator class, the driving calls are tracker. or '
                  'navigator.line_track. calls, as in Lesson 4-8, and the planner calls are '
                  'planner.add_blocked() and planner.compute_path().'},

        {'kind': 'check',
         'question': 'When the robot detects a new obstacle, what does it do to reroute?',
         'options': ['Stops permanently',
                     'Calls `add_blocked(next_pos)`, then `compute_bfs_path(position, destination)` from where it is',
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
         'lead': 'The first two lines of the outline are the Lesson 4-8 habit: plan and **print** '
                 'the path before the robot moves.',
         'lead_h': 0.95,
         'code': '    path = compute_bfs_path(position, destination)\n'
                 '    print("Planned path:", path)\n'
                 '\n'
                 '    board.wait_for_button()',
         'code_size': 22,
         'callout': 'Printed path right, but the robot still goes wrong? The bug is in the '
                    '**driving**, not the planner.',
         'tone': 'teal',
         'notes': 'Read it before pressing the button: is it what you expected? This is the Lesson '
                  '5-6 paper test built into every run, and the first diagnostic. As in Module 4, '
                  'that makes two presses per driving test: the one in RUN starts the test and '
                  'prints the plan; the one in the test is go.'},

        {'kind': 'steps', 'title': 'Step 1 · The sensor',
         'steps': [
             'Add the import and the object to the **start block**',
             'Write `test_rangefinder()`: print `rangefinder.distance()` fifty times, a tenth of a '
             'second apart, the way `test_sensors()` did in Lesson 2-1',
             'Set the run line to it. Hold a box in front of the robot at the distance of the next '
             'intersection, then take it away',
             'Write both readings down. Check that `OBSTACLE_CM` sits **between** them; change it if not',
         ],
         'size': 20,
         'notes': 'Have your own calibrated value ready to compare against.'},

        {'kind': 'steps', 'title': 'Step 2 · Simulate the sensor',
         'steps': [
             'Write `simulate_rangefinder()`: one line, `8.0` if `next_pos` is in '
             '`SIMULATED_OBSTACLES`, otherwise `50.0`',
             'Write `test_detect_once()` from the outline, with the **simulated** sensor in the '
             'look-ahead line',
             'Robot at `(0, 0)` facing North on an **empty** grid, run line set to it. Read the planned '
             'path before the second press: `(2, 0)` is on it',
             'It should face East, drive to `(1, 0)`, face `(2, 0)`, "see" the pretend box, print the new '
             'path, and stop',
         ],
         'size': 20,
         'callout': 'Confirm on screen: the blocked list has **grown**, and the new path goes **around**',
         'tone': 'teal',
         'notes': 'Only the sensor is simulated. The planner needs no simulation: it was tested in '
                  'Lesson 5-6. Have everyone run this before touching a box: the robot still '
                  'drives, but the obstacle is pretend, so a wrong reroute is a logic bug and '
                  'nothing else. Separating software bugs from hardware bugs saves enormous '
                  'frustration.'},

        {'kind': 'steps', 'title': 'Step 3 · The real sensor',
         'steps': [
             'Change the look-ahead line to `rangefinder.distance()`',
             'Put a box on one intersection of the printed path: `(2, 0)` again is a good choice',
             'Press the button. Watch the robot stop, print "Rerouting...", print the new path, and stop',
         ],
         'callout': 'Taking the new path is next lesson',
         'tone': 'teal',
         'notes': 'Place real obstacles on the printed path so the reroute is visible and dramatic. '
                  'Hardware note: the driving functions are Module 4\'s, unchanged. If the robot '
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
         'explanation': 'A simulated sensor lets you confirm the detection logic on screen. Once '
                        'that\'s solid, real-sensor problems are clearly hardware, not logic, and '
                        'the planner itself was already proven in Lesson 5-6.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Cars', 'Self-driving', 'Radar and LIDAR detect obstacles; the planner reroutes in '
                                      'real time, just like this loop.'),
             ('Warehouses', 'Fulfillment robots', 'Robots sense blocked aisles and replan paths '
                                                  'on the fly to keep goods moving.'),
             ('Space', 'Mars rovers', 'Rovers scan the terrain ahead and reroute around rocks they '
                                      'can\'t cross.'),
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
