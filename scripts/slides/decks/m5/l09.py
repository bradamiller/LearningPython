DECK = {
    'module': 5, 'lesson': 9,
    'doc': 'module-05-pathfinding/lesson-09-capstone-project',
    'title': 'Capstone Project',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Integrate the BFS planner, Module 4\'s driving toolkit and rangefinder detection into **one program**',
             'Visit four or more destinations while detecting and avoiding obstacles',
             'Start a run from the obstacles a previous run discovered, and report what this one found',
             'Demonstrate learning: Run 2 outperforms Run 1, **with numbers** to prove it',
             'Debug integration issues where individually-working parts don\'t cooperate',
         ],
         'notes': 'Multi-day: for 50-minute periods this spans 2 to 3 days (assembly and simulation, '
                  'robot testing, demos). This is the module\'s graduation project.'},

        {'kind': 'bullets', 'title': 'Every piece, one system',
         'bullets': [
             'The robot visits **several destinations**, plans with BFS, senses obstacles with the '
             'rangefinder, and reroutes on the fly',
             'It starts the next run knowing what this one found',
             'You won\'t write much new code. The challenge is **integration**: making working parts '
             'work together',
         ],
         'callout': 'That\'s exactly what real software engineers do',
         'tone': 'teal',
         'notes': 'Students underestimate how hard connecting working parts is. Say so up front.'},

        {'kind': 'bullets', 'title': 'The mission',
         'lead': 'Your robot is an **autonomous delivery vehicle**. It visits four or more grid '
                 'destinations in sequence. For each leg:',
         'lead_h': 1.05,
         'bullets': [
             'plan a path',
             'drive it while watching for obstacles',
             'reroute whenever the rangefinder finds one',
         ],
         'callout': 'Everything you need already exists in `robot.py`. Today you **connect** it.',
         'tone': 'teal',
         'notes': 'Where each piece came from: the planner (Lessons 5-4 and 5-5) and its paper tests '
                  '(5-6), detection (5-7), the drive-until-you-arrive function and carrying '
                  'knowledge between runs (5-8).'},

        {'kind': 'bullets', 'title': 'Two runs',
         'bullets': [
             '**Run 1** starts with an empty blocked list, discovers obstacles the hard way, and '
             'prints what it found',
             '**Run 2** starts with that list typed in, so it plans around them and reroutes less',
         ],
         'callout': 'The drop in step count between runs **is** the learning',
         'tone': 'green'},

        {'kind': 'check',
         'question': 'What is the main challenge of the capstone?',
         'options': ['Inventing a new pathfinding algorithm',
                     'Integrating components you already built so they work together as one system',
                     'Building a new robot from parts',
                     'Rewriting BFS from scratch'],
         'answer': 1,
         'explanation': 'Every component already exists and was tested in earlier lessons. The '
                        'capstone is about connecting them correctly: integration, not new algorithms.'},

        {'kind': 'code', 'title': 'Add to robot.py: this lesson\'s skeleton',
         'lead': 'At the end of the OBSTACLES section, above `RUN`. No new function is defined: one '
                 'setting, a paper test, and the project itself.',
         'lead_h': 0.95,
         'code': '# --- Lesson 5-9: capstone, the delivery run ---\n'
                 '# The module project: visit CAPSTONE_DESTINATIONS in order,\n'
                 '# each leg with navigate_with_detection(), starting from what\n'
                 '# the last run found (KNOWN_OBSTACLES) and printing what this\n'
                 '# run found for the next one. Nothing new is defined; the\n'
                 '# sections above did the work, and this test connects them.\n'
                 'CAPSTONE_DESTINATIONS = [(1, 3), (3, 3), (3, 0), (0, 0)]\n'
                 '\n'
                 'def test_capstone_paper():\n'
                 '    # no robot: hand KNOWN_OBSTACLES to add_blocked(), then\n'
                 '    # from (0, 0) plan each leg with the BFS planner, print it\n'
                 '    # with its step count, and move position on to that\n'
                 '    # destination for the next leg\n'
                 '    pass',
         'code_size': 16,
         'notes': 'The name is CAPSTONE_DESTINATIONS because DESTINATIONS is already in the file: '
                  'Lesson 4-9\'s delivery run still reads it, and a finished section is not edited '
                  'from another one. test_capstone() is the rest of the skeleton, on the next slide.'},

        {'kind': 'code', 'title': 'The project is a test: test_capstone()',
         'lead': 'Like every program in this course, it is a test function. The outline is the whole '
                 'program\'s shape:',
         'lead_h': 0.95,
         'code': 'def test_capstone():\n'
                 '    # 1. hand KNOWN_OBSTACLES to add_blocked()\n'
                 '    #    (empty on Run 1, last run\'s list on Run 2)\n'
                 '    # 2. position (0, 0), heading 0; both totals at 0\n'
                 '    # 3. print the plan for leg 1; wait for the button\n'
                 '    # 4. for each destination, with its leg number:\n'
                 '    #        navigate_with_detection() -- plan, follow,\n'
                 '    #        re-plan until arrived (Lesson 5-8)\n'
                 '    #        ... keeping position and heading up to date\n'
                 '    #        add its steps and reroutes to the totals\n'
                 '    # 5. print the blocked list -- what you type in next run\n'
                 '    # 6. print the totals: steps, reroutes\n'
                 '    pass',
         'code_size': 17},

        {'kind': 'bullets', 'title': 'The blocked list is the thread',
         'bullets': [
             'Step 1 **fills** it',
             'The planner **reads** it on every call',
             'Detection **adds** to it',
             'Step 5 **hands** it to the next run',
         ],
         'callout': 'Every one of those goes through `add_blocked()`. The planner never knows which.',
         'tone': 'teal'},

        {'kind': 'figure', 'title': 'One list, leg by leg',
         'figure': '/img/lesson-m5-09/capstone-thread-xy.svg',
         'caption': 'The dry run with `SIMULATED_OBSTACLES = [(1, 0), (2, 2), (3, 1)]`. One list '
                    'grows across the run and starts the next.',
         'notes': 'Left: the robot at home, the four destinations numbered in order, and the three '
                  'pretend boxes. Right: leg 1 adds (1, 0); leg 3 adds (3, 1) and (2, 2). Run 1 '
                  'totals 20 steps and 3 reroutes and prints the list; Run 2 starts with all three '
                  'and takes 18 steps with 0 reroutes. Useful numbers to have when a team\'s dry run '
                  'looks off.'},

        {'kind': 'check',
         'question': 'What single data structure connects the start of the run, pathfinding, '
                     'detection, and what you carry into the next run?',
         'options': ['The previous dictionary',
                     'The blocked list: filled at the start, planned from, added to on detection, then printed',
                     'The to_visit list',
                     'The heading number'],
         'answer': 1,
         'explanation': '`BLOCKED` flows through every stage: start, planner, detection, the next run. '
                        'If it doesn\'t flow correctly, the whole system breaks.'},

        {'kind': 'code', 'title': 'The destination loop',
         'lead': '`navigate_with_detection()` already handles one trip. The new code is the loop that '
                 'calls it **once per destination**, feeding each trip\'s end position and heading '
                 'into the next:',
         'lead_h': 1.25,
         'code': '        position, heading, steps, reroutes = navigate_with_detection(\n'
                 '            position, heading, dest, rangefinder, OBSTACLE_CM\n'
                 '        )',
         'code_size': 20,
         'callout': 'The call from your Lesson 5-8 test, with the leg\'s destination `dest` in place '
                    'of a fixed one',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Two details that are easy to get wrong',
         'bullets': [
             '`position` and `heading` must be **assigned from the return value**',
             ['Forget the `position, heading, ... =` part and leg 2 plans from (0, 0) while the robot '
              'sits somewhere else'],
             'Only the **first** leg is printed before the button',
             ['Later legs are planned from wherever the robot actually ends up, including around '
              'obstacles it hasn\'t found yet'],
         ],
         'size': 26,
         'notes': 'Class track: with the Navigator class there is no position, heading line to get '
                  'wrong. navigate_with_detection() is a method that updates navigator.position '
                  'and navigator.heading itself and returns the two counts. With the BFS class, the '
                  'planner calls are planner.compute_path() and planner.add_blocked(), and the list '
                  'printed at the end is planner.blocked.'},

        {'kind': 'check',
         'question': 'Why can the program print the plan for leg 1 before the button, but not for '
                     'legs 2 to 4?',
         'options': ['`compute_bfs_path` only works once per program',
                     'Later legs depend on where leg 1 ends and what it finds on the way: neither is known yet',
                     'Printing more than one path would overflow the screen',
                     'The button only allows one print'],
         'answer': 1,
         'explanation': 'Each leg is planned when it starts, from the robot\'s real position and the '
                        'current `BLOCKED` list. Leg 1 is the only one whose inputs are known before '
                        'the robot moves.'},

        {'kind': 'check',
         'question': 'A team\'s robot drives leg 1 correctly, then on leg 2 turns the wrong way and '
                     'tracks off the grid. The most likely cause?',
         'options': ['The rangefinder threshold is too low',
                     'They didn\'t assign the returned `position` and `heading`, so leg 2 was planned from the start',
                     'BFS found a non-shortest path',
                     'The destinations list is too long'],
         'answer': 1,
         'explanation': 'If `position` and `heading` are not updated from the return value, the '
                        'planner thinks the robot is still at (0, 0) facing north. The path it '
                        'produces is right for that spot and wrong for where the robot is.'},

        {'kind': 'steps', 'title': 'Activity · Test in three levels',
         'lead': 'Do **not** jump straight to the full run on the robot. One test on the run line at a time:',
         'lead_h': 0.65,
         'steps': [
             '**Planner alone (no robot).** Write `test_capstone_paper()`: the four paths on screen, with '
             'their step counts. Then type a pretend `KNOWN_OBSTACLES` list and watch the legs bend around it',
             '**Dry run on the grid.** Write `test_capstone()` with the simulated sensor and '
             '`SIMULATED_OBSTACLES = [(1, 0), (2, 2), (3, 1)]`. No boxes. Does the blocked list grow '
             'across all four legs?',
             '**The real thing.** Back to `rangefinder.distance()`, boxes on the grid. Run 1 with '
             '`KNOWN_OBSTACLES = []`, then Run 2 with the printed list typed in',
         ],
         'size': 20,
         'notes': 'If something breaks in the full run, you won\'t know which piece. Level 1 is Lesson '
                  '4-9\'s paper test on today\'s destinations with the BFS planner; with nothing '
                  'blocked the four legs are 4, 2, 3 and 3 steps (the page has that in a closed '
                  'reveal). Level 2: the simulated sensor goes in navigate_with_detection()\'s '
                  'look-ahead line (Lesson 5-8, step 1); verify paths compute, pretend obstacles '
                  'register, and the list printed at the end is the one to start the next run with. '
                  'Insist everyone gets the dry run working before a box touches the grid: logic '
                  'first, hardware second.'},

        {'kind': 'bullets', 'title': 'Watch for the classic integration bugs',
         'bullets': [
             'The blocked list **reset** between destinations',
             ['One `BLOCKED` for the whole run: never call `clear_blocked()` between legs'],
             '`position` and `heading` **not assigned** from the return value',
             'A destination that is itself in `KNOWN_OBSTACLES`',
             ['The planner returns `[]` and the leg is skipped with "No path"'],
         ],
         'size': 26,
         'callout': 'Check these first when parts that worked on their own don\'t cooperate',
         'tone': 'orange'},

        {'kind': 'check',
         'question': 'Which is a classic capstone integration bug to watch for?',
         'options': ['Using too few comments',
                     'Resetting the blocked list between destinations, so the robot forgets obstacles mid-run',
                     'Naming the robot',
                     'Printing the path'],
         'answer': 1,
         'explanation': '`BLOCKED` must persist across all destinations in a run. Clearing it for each '
                        'leg throws away everything learned so far. (Also common: not assigning '
                        '`position` and `heading` from the return value.)',
         'notes': 'Answer: B. test_capstone() is the graded work, and there is no student reveal '
                  'for it; the teacher copy of the solution is for unsticking a team, not a handout.'},

        {'kind': 'table', 'title': 'The rubric',
         'lead': 'You\'re graded on the integrated system, component by component:',
         'lead_h': 0.7,
         'headers': ['Category', 'Points', 'What it takes'],
         'widths': [2.6, 1.1, 6.3],
         'rows': [
             ['BFS pathfinding', '10', 'Correct shortest paths; the Lesson 5-6 tests pass'],
             ['Driving integration', '10', 'Robot physically drives the computed paths, leg after leg'],
             ['Obstacle detection', '10', 'Rangefinder detects and `add_blocked()` updates the list'],
             ['Re-planning', '10', 'Reroutes correctly around discovered obstacles'],
             ['Experience', '10', 'Run 1 prints what it found; Run 2 starts from that list'],
             ['Demonstration', '5', 'Run 1 discovers & reroutes; Run 2 avoids known obstacles'],
             ['Code quality', '5', 'Readable, uses functions, meaningful comments'],
         ],
         'size': 20,
         'notes': 'Use the rubric as a self-assessment checklist: each row maps to a lesson. '
                  'Students who did the class extensions run the capstone with their Navigator and '
                  'BFS objects; nothing in the rubric changes.'},

        {'kind': 'bullets', 'title': 'The demo, and finished early?',
         'lead': 'Run twice and have your numbers ready:',
         'lead_h': 0.6,
         'bullets': [
             '"Run 1 took X steps with Y reroutes; Run 2 took A steps with B reroutes."',
             '**Finished early?** Try an extension:',
             ['visit the nearest destination next',
              'obstacle expiration: re-check old obstacles after a few runs',
              'a `print_grid()` map of the rings after each leg',
              'a `Navigator` object that owns `position` and `heading` (if you did the class extensions)'],
         ],
         'size': 24,
         'notes': 'At the demo, ask why Run 2 is better and listen for "better data," not "the robot '
                  'is smarter." With a Navigator object the destination loop has nothing to pass '
                  'back and forth.'},

        {'kind': 'check',
         'question': 'In the demo, what evidence shows the robot "learned"?',
         'options': ['It drives faster',
                     'Run 2 has fewer reroutes and/or steps, because it started out knowing the obstacles',
                     'It makes a sound at each intersection',
                     'Run 2 visits fewer destinations'],
         'answer': 1,
         'explanation': 'The measurable improvement from Run 1 to Run 2 (fewer reroutes and steps) is '
                        'the evidence. Same algorithm, better data to start from.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Robotics', 'SLAM', 'Real robots build and reuse maps of their environment: the '
                                  'grown-up version of your obstacle memory.'),
             ('Vehicles', 'Self-driving', 'Sense, plan, act, and learn from fleet data: the same '
                                          'loop at massive scale.'),
             ('Engineering', 'System integration', 'Connecting tested components into a reliable '
                                                   'whole is the core of professional software work.'),
         ],
         'notes': 'You\'ve built, in miniature, what real autonomous systems do.'},

        {'kind': 'wrapup',
         'questions': [
             'What connects all the components?',
             'Why test in simulation before the robot?',
             'What proves the robot learned?',
         ],
         'next': 'Module 6 · Dijkstra\'s Algorithm (optional)',
         'notes': 'Answers: the blocked list (filled at the start, planned from, added to on '
                  'detection, printed for the next run); to separate logic bugs from hardware bugs; '
                  'Run 2\'s measured improvement over Run 1. Course wrap-up: take a moment to trace '
                  'the arc. Module 1 Python foundations, Module 2 sensors and functions, Module 3 '
                  'the grid, Module 4 Manhattan pathfinding and turning at intersections, Module 5 '
                  'graphs, BFS, sensing and learning, and one file, robot.py, that grew a section '
                  'at a time from Lesson 2-1. The plan-vs-drive split and the shared planner '
                  'interface are ideas they will meet again in any serious software work. From '
                  '"Hello, World" to an autonomous robot that navigates, senses and learns is a '
                  'real accomplishment. If there is time, Module 6 adds Dijkstra\'s algorithm as a '
                  'third planner behind the same interface.'},
    ],
}
