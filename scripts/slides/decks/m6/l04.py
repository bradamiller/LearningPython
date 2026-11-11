DECK = {
    'module': 6, 'lesson': 4,
    'doc': 'module-06-dijkstra/lesson-04-drive-it',
    'title': 'Drive It',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Type a measured slow segment into the program as a setting and hand it to `add_slow_edge()`',
             'Swap the planner by changing one name, and print both planners\' paths and costs before the button',
             'Time two runs and relate the seconds to the costs the program printed',
             'Explain why the driving functions did not change',
         ],
         'notes': '50 minutes. Robot required, on the slow-segment grid. Students need their measured '
                  'weight from Lesson 6-1 and the per-block time.'},

        {'kind': 'bullets', 'title': 'Two planners, one grid, one trip',
         'bullets': [
             'The robot drives from (0, 0) to (0, 3) planned by **BFS**',
             'Then the same trip planned by **Dijkstra**, and the class times both',
             'BFS takes **fewer steps**. Dijkstra **arrives first**.',
         ],
         'callout': 'Nothing about the driving changes: it is Module 4\'s `drive_path()`, with the '
                    'planner\'s name the only Module 6 line in the test',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Skeleton (1 of 2): two settings',
         'lead': 'Paste this at the end of the DIJKSTRA PLANNER section.',
         'code': '# --- Lesson 6-4: drive it ---\n'
                 '# The slow grid on the floor. One test, run twice:\n'
                 '# PLANNER_NAME picks BFS or Dijkstra, both plans are printed\n'
                 '# before the button, and the NAVIGATOR\'s drive_path() drives\n'
                 '# whichever was picked while the program times it. Nothing\n'
                 '# that drives changed: a path is a list, whoever planned it.\n'
                 'SLOW_SEGMENT = ((0, 1), (0, 2), 5)   # what you measured in 6-1\n'
                 'PLANNER_NAME = "BFS"                  # or "Dijkstra"',
         'code_size': 19},

        {'kind': 'code', 'title': 'Skeleton (2 of 2): the driving test\'s outline',
         'code': 'def test_drive_slow_grid():\n'
                 '    # 1. clear the slow list; add SLOW_SEGMENT to it\n'
                 '    # 2. position (0, 0), heading 0, destination (0, 3)\n'
                 '    # 3. planner = the function PLANNER_NAME names\n'
                 '    # 4. compare() both plans, so the choice is on screen\n'
                 '    # 5. plan with planner, then board.wait_for_button()\n'
                 '    # 6. note the time; drive_path(); note the time again\n'
                 '    # 7. print PLANNER_NAME, the seconds and the step count\n'
                 '    pass',
         'code_size': 20},

        {'kind': 'code', 'title': 'One name changes',
         'lead': '`SLOW_SEGMENT` is one tuple: the two ends and the weight. Type it once, hand it to '
                 '`add_slow_edge()` as `SLOW_SEGMENT[0]`, `SLOW_SEGMENT[1]`, `SLOW_SEGMENT[2]` (Lesson '
                 '4-1\'s indexing). Then the test chooses its planner by name:',
         'lead_h': 1.5,
         'code': '    if PLANNER_NAME == "Dijkstra":\n'
                 '        planner = compute_dijkstra_path\n'
                 '    else:\n'
                 '        planner = compute_bfs_path',
         'code_size': 22,
         'callout': '`planner = compute_dijkstra_path` is the Lesson 5-6 swap: a function handed around '
                    'by name, with **no parentheses**',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'From that line on',
         'bullets': [
             '`planner(position, destination)` is whichever one was chosen',
             '`drive_path()` is handed the list it returns, with **no idea** which planner produced it',
             'Before the button, the test calls `compare()`, so both plans are on the screen before '
             'either run happens',
             'The timing: `time.time()` just before `drive_path()` and just after. The difference is '
             'the seconds the drive took: a check on the stopwatch.',
         ],
         'notes': 'Navigator class: drive_path() is navigator.drive_path(path), with no "position, '
                  'heading =" to get wrong, and the plans are made from navigator.position. Planner '
                  'classes plus Lesson 6-5: PLANNER_NAME chooses between BFS() and Dijkstra(); see '
                  'that lesson.'},

        {'kind': 'code', 'title': 'Both plans, before the button',
         'code': '  BFS       steps: 3  cost: 7   [(0, 1), (0, 2), (0, 3)]\n'
                 '  Dijkstra  steps: 5  cost: 5   [(1, 0), (1, 1), (1, 2), (0, 2), (0, 3)]',
         'code_size': 20,
         'callout': 'The usual two presses: the one in `RUN` starts the test and prints the plans; the '
                    'one in the test is **go**',
         'tone': 'orange'},

        {'kind': 'figure', 'title': 'Predict the stopwatch from the cost',
         'figure': '/img/lesson-m6-04/cost-to-seconds.svg',
         'caption': 'Cost is time in blocks, so multiplying by one block\'s time predicts the stopwatch. '
                    'Write your prediction down before either run.',
         'notes': 'The figure uses Lesson 6-1\'s example time of 4.1 seconds a block: BFS cost 7 is '
                  'about 29 seconds, Dijkstra cost 5 about 21. Students should use their own '
                  'per-block time.'},

        {'kind': 'check',
         'question': 'How much of the driving code changes between the BFS run and the Dijkstra run?',
         'options': ['`drive_path()` needs a weight parameter',
                     'None of it: the planner returns a list of intersections either way, and '
                     '`drive_path()` drives lists',
                     '`turn_to()` has to know about the slow segment',
                     '`track_to_intersection()` runs slower on purpose'],
         'answer': 1,
         'explanation': 'The plan-versus-drive split from Lesson 4-0 pays off a third time. The driving '
                        'functions never knew what a path meant, so a path chosen for cost instead of '
                        'steps is just another list.'},

        {'kind': 'steps', 'title': 'Activity · Two runs, one stopwatch',
         'steps': [
             'Write `test_drive_slow_grid()` from the outline, type your segment into `SLOW_SEGMENT`, '
             'and run it on the desk. Check the printed costs match your paper from 6-1. **Don\'t press '
             'the second button yet.**',
             '`PLANNER_NAME = "BFS"`. Robot at (0, 0) facing North. Run, read the path, press the '
             'button, start a stopwatch with the robot. Record the time. Watch it take the slow road.',
             '`PLANNER_NAME = "Dijkstra"`. Same start, same destination. Record the time. Watch it go round.',
             'Fill in the table: steps, cost and seconds for each planner.',
         ],
         'size': 19,
         'notes': 'Make it a class event: run the two trips back to back with the whole class watching '
                  'and one student on a stopwatch. The robot visibly choosing the long way round and '
                  'arriving sooner is the module\'s payoff; let it land before the discussion. Before '
                  'the button, have students read both plans aloud and predict the two times from the '
                  'costs and their per-block time. If the two plans match, the slow segment is missing '
                  'or too light: fix the setup, not the code.'},

        {'kind': 'code', 'title': 'Step 4 · Fill in the table',
         'tag': 'Activity',
         'code': 'Planner    steps   cost   seconds\n'
                 'BFS         ___    ___     ___\n'
                 'Dijkstra    ___    ___     ___',
         'code_size': 28,
         'callout': 'The program\'s own elapsed time is a check on your stopwatch. The two should tell '
                    'the same story: **more steps, fewer seconds**.',
         'tone': 'teal',
         'notes': 'Discrepancies are a good conversation: turns cost time too (the detour has more of '
                  'them), which is why the predicted gap is usually a little bigger than the measured '
                  'one. It is also a fair place to mention what the course left out: a planner that '
                  'weights turns needs to know the heading, and that is a bigger change than two lines.'},

        {'kind': 'check',
         'question': 'A team\'s Dijkstra run takes 5 steps and 21 seconds; their BFS run takes 3 steps '
                     'and 29 seconds. A normal block is about 4 seconds. Do the numbers make sense?',
         'options': ['No: more steps must take more time',
                     'Yes: 5 normal blocks is about 20 s; 2 normal blocks plus a weight-5 segment is '
                     'about 28 s',
                     'No: BFS should always be faster',
                     'Only if the battery was changed between runs'],
         'answer': 1,
         'explanation': 'Cost predicts time: 5 blocks\' worth against 7 blocks\' worth, at about 4 '
                        'seconds a block. The stopwatch agreeing with the cost column is the point of '
                        'the lesson.'},

        {'kind': 'check',
         'question': 'Both runs produce the same path and the same time. What is the most likely cause?',
         'options': ['Dijkstra is broken',
                     '`SLOW_SEGMENT` was not typed in (or its weight is 3 or less), so the two planners '
                     'have no reason to disagree',
                     'The robot is too fast',
                     '`drive_path()` ignores the planner'],
         'answer': 1,
         'explanation': 'The printed plans before the button show this at once. With no slow edge, or a '
                        'weight that ties with the detour, Dijkstra and BFS agree, as they should.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Maps', 'The long way that\'s quicker',
              'A map app routing you onto the highway for three extra miles is this run, at scale: '
              'more distance, less time.'),
             ('Testing', 'Predict, then measure',
              'Writing down the expected time before the run, from the cost, is the same discipline '
              'as writing the expected path before a test.'),
             ('Robotics', 'Swappable planners',
              'Real robot stacks run several planners behind one interface and switch by '
              'configuration, not by rewriting the driver.'),
         ]},

        {'kind': 'wrapup',
         'questions': [
             'What is the one Module 6 line in the driving test?',
             'What predicted the stopwatch?',
             'Why did the robot\'s driving code not change?',
         ],
         'next': 'optional, class track: the Dijkstra class and three planners as objects',
         'notes': 'Answers: which planner planner is set to. The cost column. It drives lists; it '
                  'never knew what a path meant. Formative: the two-run table filled in, with costs and '
                  'times that agree. Exit ticket: "In one sentence, why did the 5-step route win?" '
                  'Lesson 6-5 is an optional extension for students who did the class track. For '
                  'everyone else, the course ends here, with a robot that plans by time and a robot.py '
                  'that is the record of everything it learned.'},
    ],
}
