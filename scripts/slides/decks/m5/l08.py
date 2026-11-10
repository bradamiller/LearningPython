DECK = {
    'module': 5, 'lesson': 8,
    'doc': 'module-05-pathfinding/lesson-08-building-experience',
    'title': 'Building Experience',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Write `navigate_with_detection()`: Lesson 5-7\'s step inside a `while` loop that runs until the robot **arrives**',
             'Explain why remembering obstacles improves navigation',
             'Start a run with obstacles **already known**, so the planner avoids them from the first path',
             'Compare Run 1 and Run 2 with **metrics** (steps, reroutes)',
             'Explain the GPS/Waze analogy for crowd-sourced obstacle data',
         ],
         'notes': '50 minutes. Better data, same algorithm: the robot learns. Spend the first '
                  'fifteen minutes on the while loop. The rerouted flag is the only new Python '
                  'idea in the lesson, which is why the outline spells the loop out: the shape '
                  'is the lesson, the typing is theirs.'},

        {'kind': 'bullets', 'title': 'Two things are missing',
         'lead': 'In Lesson 5-7 the robot found one obstacle, re-planned once, and the loop stopped '
                 'with a `break`.',
         'lead_h': 1.05,
         'bullets': [
             'The robot should **keep going**: follow the new path, and if it finds another wall, '
             're-plan again, until it arrives',
             'It rediscovers every obstacle **from scratch** each run, like being surprised by the '
             'same construction zone every morning',
         ],
         'callout': 'Today: a function that re-plans until arrival, and a way to start Run 2 '
                    'knowing what Run 1 found out',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Add to robot.py: this lesson\'s skeleton',
         'lead': 'At the end of the OBSTACLES section, under `test_detect_once()`. One setting, and '
                 'the one function the capstone is built from.',
         'lead_h': 0.95,
         'code': '# --- Lesson 5-8: re-plan until you arrive ---\n'
                 '# navigate_with_detection() is the 5-7 loop inside a while:\n'
                 '# plan, follow, and if something got in the way, plan again\n'
                 '# from here, until a whole path is driven with no reroute. It\n'
                 '# hands back position and heading, as drive_path() does, plus\n'
                 '# the step and reroute counts. KNOWN_OBSTACLES is what the\n'
                 '# last run found, typed in by you: memory between runs.\n'
                 'KNOWN_OBSTACLES = []     # what the last run printed; empty on Run 1\n'
                 '\n'
                 'def navigate_with_detection(position, heading, destination, rangefinder, obstacle_cm):\n'
                 '    """Drive from position (facing heading) to destination,\n'
                 '    re-planning around every obstacle the rangefinder finds;\n'
                 '    return (position, heading, step_count, reroute_count)."""',
         'code_size': 17,
         'notes': 'The function\'s outline, which is the rest of the skeleton, is on the next slide.'},

        {'kind': 'code', 'title': 'The outline of navigate_with_detection()',
         'code': '    # step_count = 0 ; reroute_count = 0\n'
                 '    # arrived = False\n'
                 '    # while not arrived:\n'
                 '    #     plan from position; print the path\n'
                 '    #     if the path is empty: say "No path"; return the four\n'
                 '    #     rerouted = False\n'
                 '    #     for each next_pos in path:          -- Lesson 5-7\n'
                 '    #         face it\n'
                 '    #         look ahead with rangefinder.distance()\n'
                 '    #         if closer than obstacle_cm:\n'
                 '    #             add_blocked(next_pos); count the reroute\n'
                 '    #             rerouted = True ; break\n'
                 '    #         else:\n'
                 '    #             arrive; position = next_pos; count the step\n'
                 '    #     if not rerouted: arrived = True\n'
                 '    # return position, heading, step_count, reroute_count\n'
                 '    pass',
         'code_size': 17,
         'notes': 'Under the docstring from the previous slide. Trace it on the board with a path '
                  'that hits one wall, so students see the for break, rerouted go True, and the '
                  'while plan again from the new position.'},

        {'kind': 'bullets', 'title': 'From break to "until you arrive"',
         'bullets': [
             'Put Lesson 5-7\'s whole `for` loop inside a `while`',
             'The `while` ends only when the `for` ran **all the way through** without a reroute',
             'The inner `for` is Lesson 5-7 unchanged, except that the re-plan happens at the **top** '
             'of the `while`, not inside the `if`',
             'So the `break` only has to get out of the `for`',
         ],
         'callout': 'Read the shape, not the lines: **plan, follow, and if something got in the '
                    'way, plan again from here**',
         'tone': 'teal'},

        {'kind': 'figure', 'title': 'Plan, follow, plan again',
         'figure': '/img/lesson-m5-08/until-arrive.svg',
         'caption': 'Plan, follow, and if something got in the way, plan again from here.',
         'notes': 'Plan from here with compute_bfs_path(position, dest). Follow it, looking ahead '
                  'before each step. Something ahead: add_blocked(next_pos), set rerouted, break out '
                  'of the for, and the while plans again. Every step followed with nothing ahead: '
                  'arrived, return position, heading and the counts.'},

        {'kind': 'bullets', 'title': 'The rerouted flag, and what comes back',
         'bullets': [
             'The `rerouted` flag is how the `while` finds out whether the `for` **finished** or '
             '**broke out** early',
             ['Set it `False` before the `for`', 'Set it `True` in the obstacle branch',
              'After the `for`, "not rerouted" means "drove the whole path": **arrived**'],
             'The function returns the robot\'s new pose (`position` and `heading`)',
             ['The caller needs them to plan the **next** trip: Lesson 5-9 strings several of these together'],
         ],
         'size': 24,
         'notes': 'Class track: if students built the Navigator class in Lesson 4-7, this function '
                  'wants to be a method of it. position and heading become self.position and '
                  'self.heading and drop out of the parameters and the return; the driving calls go '
                  'through self.line_track. and self.desired_heading() / self.turn_to(); the planner '
                  'calls are planner.add_blocked() and planner.compute_path(). It returns only the '
                  'two counts, and the caller reads navigator.position afterwards, as in Lesson 4-8.'},

        {'kind': 'bullets', 'title': 'Two parameters that look odd',
         'bullets': [
             '`rangefinder` and `obstacle_cm` are already in the file, as a global and a setting',
             'Passing them in means the function **says** what it depends on: read the `def` line '
             'and you know it needs a sensor and a cutoff',
             'And a test can hand in a different cutoff **without editing** the function',
         ],
         'callout': 'The simulated sensor is a function of `next_pos`, not an object with a '
                    '`distance()` method: for the dry run, swap the one look-ahead line, as in Lesson 5-7',
         'tone': 'orange'},

        {'kind': 'bullets', 'title': 'Why check for an empty path?',
         'bullets': [
             'It matters now in a way it didn\'t on paper',
             'If the robot gets **boxed in**, `compute_bfs_path()` returns `[]` (Lesson 5-5)',
             'Without the check, the `for` loop runs **zero times**',
             '`rerouted` stays `False`, and the robot declares itself **arrived** at the wrong intersection',
         ],
         'callout': 'So: if the path is empty, say "No path" and return the four values',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'In `navigate_with_detection()`, what makes the `while` loop finally stop?',
         'options': ['A fixed number of iterations',
                     'The `for` loop finishes without a reroute, so `rerouted` stays `False` and `arrived` becomes `True`',
                     'The rangefinder returns 0',
                     '`compute_bfs_path` returns the same path twice'],
         'answer': 1,
         'explanation': 'Each pass plans a path and tries to follow it. If a wall turns up, the `for` '
                        'loop breaks with `rerouted = True` and the `while` plans again from the new '
                        'position. Only a complete, uninterrupted pass sets `arrived`.'},

        {'kind': 'check',
         'question': 'Why does the function return the pose (`position` and `heading`), not just the step counts?',
         'options': ['Python requires functions to return at least two values',
                     'So the next trip is planned from where the robot actually ended up, facing the way it faces',
                     'To reset them to (0, 0) and 0',
                     'For the print statement only'],
         'answer': 1,
         'explanation': 'The pose, `position` and `heading`, is local to the function. The caller '
                        'only learns the new pose if the function hands it back, and Lesson 5-9 '
                        'needs them to chain several destinations.'},

        {'kind': 'table', 'title': 'Why memory matters',
         'lead': 'The BFS planner doesn\'t change between runs. The driving functions don\'t change. '
                 'Only the **input** changes:',
         'headers': ['Run', 'Blocked list at the start', 'What happens', 'Result'],
         'widths': [1.3, 3.2, 3.8, 2.4],
         'rows': [
             ['Run 1', 'empty', 'discover obstacles the hard way', 'many reroutes'],
             ['Run 2', 'pre-loaded', 'plan around known obstacles', 'few or no reroutes'],
         ],
         'size': 22,
         'callout': '**Better data leads to better performance.** Run 2 runs the **same** algorithm '
                    'on better information.',
         'tone': 'teal',
         'notes': 'Frame memory with Waze: students get it instantly. "What if Waze forgot every '
                  'traffic report when you closed the app?"'},

        {'kind': 'figure', 'title': 'Run 1 and Run 2',
         'figure': '/img/lesson-m5-08/run1-run2-xy.svg',
         'caption': 'One example with three boxes. Your numbers will depend on your grid; the shape '
                    'of the difference won\'t.',
         'notes': 'S at (0, 0) to D at (3, 3), boxes at (2, 0), (2, 2) and (3, 1). Run 1 starts '
                  'empty and finds each box only when it faces it: 8 steps, 3 reroutes, backing up '
                  'once. Run 2 starts with the three typed in: 6 steps, 0 reroutes.'},

        {'kind': 'check',
         'question': 'Why does the robot navigate better on Run 2?',
         'options': ['It learns a smarter algorithm',
                     'Same algorithm, but the blocked list starts with Run 1\'s obstacles, so it plans around them',
                     'Its motors get faster',
                     'It skips destinations'],
         'answer': 1,
         'explanation': 'Same BFS, better data. Pre-loading Run 1\'s discoveries means Run 2 plans '
                        'around those obstacles immediately instead of rediscovering them.'},

        {'kind': 'steps', 'title': 'Activity · Step 1 · Dry run',
         'steps': [
             'Write the body from the outline, with `simulate_rangefinder(next_pos)` in the '
             'look-ahead line for now',
             'Write `test_navigate()`: hand every entry of `KNOWN_OBSTACLES` to `add_blocked()` (a '
             '`for` loop, two lines). Position `(0, 0)`, heading `0`, destination `(3, 3)`',
             'Plan the path and print it; wait for the button',
             'Call the function, **assign all four return values**, then print where it arrived, the '
             'step and reroute counts, and on its own line `"All known obstacles:"` and `BLOCKED`',
         ],
         'size': 20,
         'notes': 'The dry run proves the loop with Lesson 5-7\'s simulate_rangefinder() before any '
                  'box goes on the grid.'},

        {'kind': 'code', 'title': 'Assign all four return values',
         'lead': 'In `test_navigate()`, the call hands back **four** values. Catch every one:',
         'lead_h': 0.8,
         'code': '    position, heading, steps, reroutes = navigate_with_detection(\n'
                 '        position, heading, destination, rangefinder, OBSTACLE_CM\n'
                 '    )',
         'code_size': 20,
         'callout': 'With `SIMULATED_OBSTACLES` still `[(2, 0), (2, 2)]`: reaches `(1, 0)`, "sees" '
                    '`(2, 0)`, prints a new path, **takes it**, and arrives at `(3, 3)` with one reroute',
         'tone': 'green',
         'notes': 'Robot at (0, 0) facing North on an empty grid, run line set to test_navigate(), '
                  'both presses. Compare with Lesson 5-7, which stopped at the reroute.'},

        {'kind': 'steps', 'title': 'Step 2 · The real sensor',
         'steps': [
             'Change the look-ahead line to `rangefinder.distance()`',
             'Put two boxes on the grid, on intersections the printed path crosses, and run again',
             'It should reroute around the first, reroute again if the new path meets the second, '
             'and arrive',
             'Write down the last line it prints: the **blocked list**',
         ],
         'notes': 'Set up the grid so Run 1 has 2 to 3 reroutes; the contrast with a zero-reroute '
                  'Run 2 is the "aha." The lesson page has a closed reveal with a finished '
                  'navigate_with_detection() to check against; it is not on the slides. If a '
                  'student\'s version re-plans at the bottom of the for instead of the top of the '
                  'while and still arrives, keep theirs, but check that a boxed-in robot prints '
                  '"No path" rather than claiming to have arrived.'},

        {'kind': 'bullets', 'title': 'Carry it into the next run',
         'bullets': [
             'Within one program run, `BLOCKED` persists between function calls: that\'s why the '
             '`while` loop works',
             'But close the program and it\'s **gone**: Python variables don\'t survive a restart',
             'So how does Run 2 begin already knowing what Run 1 found out?',
         ],
         'callout': '**You tell it.**',
         'tone': 'orange',
         'tag': 'Activity'},

        {'kind': 'code', 'title': 'Type Run 1\'s list into KNOWN_OBSTACLES',
         'lead': 'Your test already prints `All known obstacles: [(1, 2), (2, 2), (3, 0)]` at the '
                 'end of the run. Type that list in at the top of the Lesson 5-8 part of the file:',
         'lead_h': 1.2,
         'code': 'KNOWN_OBSTACLES = [(1, 2), (2, 2), (3, 0)]      # what Run 1 discovered',
         'code_size': 20,
         'callout': 'Run it again: it plans around all three from its very first path. Find a fourth, '
                    'and the printed list has four, ready for Run 3.',
         'tone': 'teal',
         'notes': 'The first two lines of test_navigate() hand each intersection to the planner the '
                  'same way everything else reaches it.'},

        {'kind': 'bullets', 'title': 'You are the memory',
         'bullets': [
             'The robot found the obstacles, **you** carried them from one run to the next, and the '
             'algorithm never changed',
             'The planner has now been told about walls three ways:',
             ['by a test in 5-6', 'by the rangefinder in 5-7', 'by you, here'],
             'Every one of them was a call to `add_blocked()`',
         ],
         'callout': 'A real system writes the list somewhere and reads it back itself. **What** gets '
                    'carried across, and what it\'s worth, is exactly what you just did by hand.',
         'tone': 'teal',
         'notes': 'Carrying the list by hand is the point, not a shortcut: it makes "same algorithm, '
                  'better data" something students do with their own fingers, and keeps the lesson '
                  'about navigation instead of file formats. If someone asks why the robot can\'t '
                  'save it itself: good question, that is what a real one does, and it changes '
                  'nothing about what is carried.'},

        {'kind': 'check',
         'question': 'Run 1 finishes and prints [(1,2), (2,2)]. What has to happen for Run 2 to start '
                     'out knowing about those two obstacles?',
         'options': ['Nothing: the robot remembers them automatically',
                     'Hand the list to `add_blocked()` at the start of Run 2: a variable doesn\'t outlive the program',
                     'Run 2 has to drive the same route as Run 1',
                     '`compute_bfs_path` has to be rewritten'],
         'answer': 1,
         'explanation': 'A list lives only while the program runs. Run 2 starts out knowing exactly '
                        'what it is handed, which is why you print the list at the end of one run '
                        'and type it into `KNOWN_OBSTACLES` at the start of the next.'},

        {'kind': 'table', 'title': 'Activity · Measure the improvement',
         'lead': '"It seemed faster" isn\'t evidence: **measure**. Your test prints the steps and '
                 'reroutes; write them down for each run.',
         'headers': ['Metric', 'Run 1', 'Run 2'],
         'widths': [4, 3, 3],
         'rows': [
             ['Starting obstacles', '0', '(from Run 1)'],
             ['Reroutes', '____', '____'],
             ['Total steps', '____', '____'],
         ],
         'size': 24,
         'callout': 'Fill it in from your own two runs: the numbers are the evidence, and they\'ll '
                    'differ with your grid and where the obstacles sit',
         'tone': 'teal',
         'notes': 'Insist on recorded numbers: the quantitative comparison convinces far more than '
                  '"it felt faster."'},

        {'kind': 'check',
         'question': 'Run 1 took 12 steps with 3 reroutes; Run 2 took 8 steps with 0 reroutes. Why '
                     'the change?',
         'options': ['The battery was fuller',
                     'Run 2 started knowing the obstacles, so it planned around them and never had to reroute',
                     'The grid got smaller',
                     'Random luck'],
         'answer': 1,
         'explanation': 'With obstacles pre-loaded, Run 2\'s initial paths already avoid them: no '
                        'mid-run surprises, so zero reroutes and fewer steps.'},

        {'kind': 'bullets', 'title': 'Could Run 2 still find new obstacles?',
         'bullets': [
             '**Yes.** Run 2 avoids everything it **already** knows',
             'But its smarter route may pass intersections Run 1 never visited, and one of those could be blocked',
             'So Run 3 would start with even more knowledge',
             'Eventually the robot knows every relevant obstacle, and its paths are right from the start',
         ],
         'callout': 'That is **convergence**',
         'tone': 'teal',
         'notes': 'Be honest about limits: what if an obstacle moves? Real systems need to forget '
                  'stale data, not just accumulate it. Good discussion for advanced students.'},

        {'kind': 'check',
         'question': 'Can Run 2 discover an obstacle Run 1 never found?',
         'options': ['No: Run 2 knows everything already',
                     'Yes: Run 2 may take a different route and encounter obstacles Run 1 never drove past',
                     'No: obstacles never change',
                     'Only if the grid grows'],
         'answer': 1,
         'explanation': 'The robot only discovers obstacles it drives toward. A new route can reach '
                        'intersections Run 1 skipped, so Run 2 can still find something new, feeding '
                        'Run 3 even better data.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Maps', 'Waze traffic', 'One driver hits traffic; the app warns everyone behind them. '
                                      'Shared, remembered data.'),
             ('AI', 'Learning from data', 'Machine-learning systems improve as they accumulate '
                                          'examples: the same "better data, better results" idea.'),
             ('Apps', 'Saved state', 'Games, editors and browsers store your progress before '
                                     'closing: the automatic version of carrying your blocked list '
                                     'across by hand.'),
         ],
         'height': 3.9,
         'notes': 'Connect lightly to machine learning: accumulate data, make better decisions.'},

        {'kind': 'wrapup',
         'questions': [
             'What turns Lesson 5-7\'s single reroute into "drive until you arrive"?',
             'What actually changes between Run 1 and Run 2?',
             'How do you show Run 2 is better?',
             'What has to happen between runs for the robot to keep what it learned?',
         ],
         'next': 'the capstone, one complete autonomous system',
         'notes': 'Answers: a while not arrived loop around the for, with a rerouted flag. The data '
                  '(the blocked list), not the algorithm. Measure steps and reroutes. The list has '
                  'to be handed back to add_blocked(): a variable doesn\'t survive the program '
                  'ending. The wrap-up quiz question follows.'},

        {'kind': 'check',
         'question': 'What is "convergence" in this context?',
         'options': ['The robot running out of battery',
                     'After enough runs it knows all relevant obstacles, so its paths are right from the start',
                     'Two robots meeting at an intersection',
                     'The grid shrinking over time'],
         'answer': 1,
         'explanation': 'Each run can add knowledge until there\'s nothing new to learn. At that '
                        'point paths are right immediately: the robot\'s map has converged.',
         'notes': 'The lesson\'s wrap-up quiz. Answer: B. Formative: trace the while loop through '
                  'one reroute; pre-load a blocked list; articulate the Waze analogy. Exit ticket: '
                  '"Run 1 took 12 steps and 3 reroutes; Run 2 took 8 steps and 0 reroutes. Explain '
                  'why." Preview: the capstone chains navigate_with_detection() across several '
                  'destinations, and demonstrates Run 1 vs. Run 2.'},
    ],
}
