DECK = {
    'module': 5, 'lesson': 4,
    'doc': 'module-05-pathfinding/lesson-04-pathfinding-functions',
    'title': 'The Pathfinding Functions',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Write `add_blocked(intersection)`: recorded **once**, even if told twice',
             'Rewrite `build_grid_graph()` as `build_graph(rows, cols, blocked)`',
             'State the **two planner rules**: the position is passed in; the path leaves the start out',
             'Explain why the blocked list is shared, and why the graph is rebuilt on every call',
         ],
         'notes': '45 minutes. The concept from Lesson 5-3 turns into code, in stages. Today the GRID '
                  'GRAPH section becomes a toolkit like Module 2\'s sensor code: a shared blocked list, '
                  'a function that adds to it, and build_graph() built around it. A new BFS PLANNER '
                  'section opens with a placeholder that Lesson 5-5 fills in.'},

        {'kind': 'bullets', 'title': 'Where do obstacles go?', 'tag': 'Discuss',
         'bullets': [
             'Lesson 5-7: the robot sees a box **while driving**',
             'It has to plan around it',
             'Where does it write down that the box is there?',
         ],
         'size': 28,
         'notes': 'Most students say "pass the list to the function". Agree that it is half right, then '
                  'ask when the robot finds out about each obstacle: one at a time, in the middle of '
                  'driving.'},

        {'kind': 'bullets', 'title': 'Answer', 'tag': 'Discuss',
         'bullets': [
             '"Pass the list in" is **half right**',
             'Obstacles arrive **one at a time**, while driving',
             'So the list has to last **between** one path and the next',
         ],
         'size': 28,
         'callout': 'One list at the top of the section, where every function can see it',
         'tone': 'green'},

        {'kind': 'code', 'title': 'One list at the top of the section',
         'lead': 'At the top of GRID GRAPH, where every function can see it, like `ROWS` and `COLS`:',
         'lead_h': 1.2,
         'code': 'BLOCKED = []     # intersections the robot must not drive through',
         'code_size': 24,
         'callout': 'Capitals, like `THRESHOLD`: it is a setting. It grows only through **one function**.',
         'tone': 'teal',
         'notes': 'A variable at the top of the section that every function can see is the same idea '
                  'students used for the sensor toolkit in Module 2 (reflectance and THRESHOLD at the '
                  'top of LINE SENSOR). Capitals because it is a setting, not something that changes '
                  'in the middle of a calculation.'},

        {'kind': 'figure', 'title': 'One list, three ways in, one way out',
         'figure': '/img/lesson-m5-04/blocked-list.svg',
         'caption': 'Every plan builds its graph from BLOCKED as it stands right now.',
         'notes': 'Point at the three sources: a paper test in Lesson 5-6, the rangefinder in Lesson 5-7, '
                  'and the student typing in a list in Lesson 5-8. All three call add_blocked(), and '
                  'compute_bfs_path() reads the list fresh on every call.'},

        {'kind': 'bullets', 'title': 'Two rules we will never break',
         'bullets': [
             '**Rule 1: the planner is told where the robot is**',
             ['It never remembers the position: the driving code owns it'],
             '**Rule 2: the path is the intersections to drive to**',
             ['No start: `len(path)` is the steps; "already there" is `[]`'],
         ],
         'size': 24,
         'callout': 'Module 4\'s planner follows both: from `(0, 0)` to `(0, 2)` it returns '
                    '`[(0, 1), (0, 2)]`',
         'tone': 'teal',
         'notes': 'Every planner looks like compute_something_path(start, destination). One owner. '
                  'Rule 1: the driving code already knows where the robot is. If the planner kept its '
                  'own copy, the two could disagree, and the planner would plan from the wrong place. '
                  'Rule 2: two steps, no start. Keep these two rules on the board all module. Nothing '
                  'later breaks them, including the class versions and Module 6.'},

        {'kind': 'check',
         'question': 'Why must a planner be TOLD the robot\'s position instead of remembering it?',
         'options': ['So the planner and the driving code can never disagree about where the robot is',
                     'Because functions cannot store values between calls',
                     'To make the path shorter',
                     'Because the position changes while the path is being computed'],
         'answer': 0,
         'explanation': 'The driving code owns the position. Two copies of the same fact is how a planner '
                        'ends up planning from an intersection the robot left three steps ago.'},

        {'kind': 'code', 'title': 'Add to robot.py: the blocked list',
         'lead': 'At the end of GRID GRAPH, under your Lesson 5-3 test:',
         'lead_h': 0.7,
         'code': '# --- Lesson 5-4: the blocked list ---\n'
                 '# BLOCKED is the one record of where the robot must not go.\n'
                 '# add_blocked() is the one way in: tests, the rangefinder and\n'
                 '# you all use it. build_graph() builds AROUND the list, so a\n'
                 '# blocked intersection is never a key and never a neighbor.\n'
                 'BLOCKED = []             # intersections the robot must not drive through\n'
                 '\n'
                 'def add_blocked(intersection):\n'
                 '    """Record intersection in BLOCKED, once, even if told twice."""\n'
                 '    pass\n'
                 '\n'
                 'def clear_blocked():\n'
                 '    """Empty BLOCKED in place, so a test can start fresh."""\n'
                 '    pass',
         'code_size': 18,
         'notes': 'Two pastes today and one rewrite. This is the first paste. Both bodies are written '
                  'in Step 1.'},

        {'kind': 'code', 'title': 'Add to robot.py: BFS PLANNER',
         'lead': 'After GRID GRAPH, above `RUN`. The placeholder body is given: Lesson 5-5 replaces it.',
         'lead_h': 0.7,
         'code': '# ===== BFS PLANNER =====\n'
                 '# The second planner. compute_bfs_path(start, destination)\n'
                 '# has the same shape as the MANHATTAN PLANNER\'s function and\n'
                 '# keeps the same two promises (told the position; the path\n'
                 '# leaves the start out), but it numbers the GRID GRAPH as a\n'
                 '# wave from the destination, so it routes AROUND whatever\n'
                 '# is in BLOCKED. Pure\n'
                 '# dictionary work: every test here runs with the robot still.\n'
                 '\n'
                 'def compute_bfs_path(start, destination):\n'
                 '    """Shortest path from start to destination around\n'
                 '    BLOCKED, as the list of intersections to drive to."""\n'
                 '    graph = build_graph(ROWS, COLS, BLOCKED)      # rebuilt every call\n'
                 '    print("compute_bfs_path is not written yet!")\n'
                 '    return []',
         'code_size': 18,
         'notes': 'A planner is a different kind of work from a graph, so it gets its own section. The '
                  'placeholder is given because it is not the function yet.'},

        {'kind': 'bullets', 'title': 'Activity · Build the toolkit',
         'bullets': [
             '**Step 1:** write `add_blocked()` and `clear_blocked()`',
             '**Step 2:** rewrite `build_grid_graph()` as `build_graph(rows, cols, blocked)`',
             ['Change **every call** as well as the definition'],
             '**Step 3:** read the placeholder; test with a wall',
         ],
         'callout': 'All paper tests: the robot stays on the desk',
         'tone': 'teal',
         'notes': 'The rewrite is the step most likely to go wrong. Budget the most time for Step 2.'},

        {'kind': 'steps', 'title': 'Step 1 · add_blocked()',
         'notes': 'Why the if: the robot may see the same wall twice. (2, 0) in the list twice is '
                  'harmless but untidy, and it makes the printed grid confusing. Students write both '
                  'bodies now and test them in Step 2. If anyone asks why there is no global, hold it '
                  'for the next slide.',
         'lead': 'The one way to tell the planner about an obstacle.',
         'lead_h': 0.65,
         'steps': [
             'An `if` and an `append`: add it **only if not already there**',
             'The robot may see the same wall twice',
             '`clear_blocked()`: `pop()` until empty, **in place**',
         ],
         'callout': 'Write both bodies. Step 2 tests them.',
         'tone': 'orange'},

        {'kind': 'code', 'title': 'Does it need `global`?',
         'lead': 'In Lesson 2-7, `set_threshold()` needed `global THRESHOLD`. What does each do to the name?',
         'lead_h': 1.2,
         'code': '    THRESHOLD = new_value              # Lesson 2-7: REASSIGNS the name -- needs global\n'
                 '    BLOCKED.append(intersection)       # today: CHANGES the list -- no global needed',
         'code_size': 18,
         'callout': '`global` is only for **reassigning** a name. `append` changes the list '
                    '`BLOCKED` already names.',
         'tone': 'teal',
         'notes': 'append reassigns nothing: BLOCKED still names the same list, which just has one more '
                  'thing in it. clear_blocked() is the same idea the other way. Writing BLOCKED = [] '
                  'inside it would reassign the name and need global; popping does not. This is the '
                  'exit ticket question, so give it time.'},

        {'kind': 'figure', 'title': 'Change the list, or the name?',
         'figure': '/img/lesson-m5-04/append-vs-assign.svg',
         'caption': '`append` changes the list the name points at. `=` points a name at something else, '
                    'and inside a function that name is a new local.',
         'notes': 'Right side: BLOCKED = [] inside a function makes a new local name pointing at a new '
                  'empty list, gone when the function returns. The real BLOCKED is untouched. That is '
                  'the case that needs global.'},

        {'kind': 'check',
         'question': 'Why does `add_blocked()` not need `global BLOCKED`, when `set_threshold()` in '
                     'Lesson 2-7 needed `global THRESHOLD`?',
         'options': ['`append` changes the list in place; `set_threshold` reassigns the name',
                     'Lists are always global',
                     '`BLOCKED` is in capital letters',
                     'It does need it: the code above is wrong'],
         'answer': 0,
         'explanation': '`global` is needed only to reassign a module-level name. Appending to a list changes '
                        'the list that BLOCKED already names; the name itself is untouched.'},

        {'kind': 'code', 'title': 'Step 2 · build_graph()', 'tag': 'Activity',
         'lead': 'Lesson 5-3 built the open grid. Now it leaves out the blocked intersections. '
                 'In GRID GRAPH, change the `def` line to:',
         'lead_h': 1.2,
         'code': 'def build_graph(rows, cols, blocked):\n'
                 '    """Return the grid as a dictionary, leaving out every\n'
                 '    intersection in blocked: not a key, not anyone\'s neighbor."""',
         'code_size': 22,
         'callout': 'Then two changes to the body you already have',
         'tone': 'teal',
         'notes': 'This rewrite is in place, in the GRID GRAPH section, where build_grid_graph() was.'},

        {'kind': 'bullets', 'title': 'Step 2 · Two `in blocked` checks',
         'bullets': [
             '**1.** `(x, y)` in `blocked`? Skip it: never a key',
             '**2.** Each neighbor check also needs the neighbor **not** in `blocked`',
             'Keep the order **left, right, down, up** (Lesson 5-1\'s trace)',
         ],
         'size': 24,
         'callout': 'Miss check 2 and the graph has **edges into the wall**',
         'tone': 'orange',
         'notes': 'Both checks are needed: the second keeps a blocked intersection out of every other '
                  'intersection\'s neighbor list. The order matters because it is why the Lesson 5-1 '
                  'trace\'s printed path matched the table. A build_graph that drops blocked keys but '
                  'still lists them as neighbors is the single most common bug in the module, and it '
                  'only shows up in Lesson 5-5 as a search that walks into a wall. Catch it today.'},

        {'kind': 'steps', 'title': 'Step 2 · Tidy up, then test',
         'notes': 'The old name is gone, the way SETPOINT disappeared in Lesson 2-6. Every call to '
                  'build_grid_graph() has to change, not only the definition. A NameError at this '
                  'point usually means a call was missed.',
         'steps': [
             'The old name is gone, the way `SETPOINT` went in Lesson 2-6',
             'Fix `test_grid_graph()` to build with `build_graph(ROWS, COLS, BLOCKED)`',
             'Run it. Nothing blocked: **16**, four neighbors, two neighbors, then the whole graph',
         ],
         'callout': 'Don\'t go on until it matches Lesson 5-3',
         'tone': 'orange'},

        {'kind': 'check',
         'question': '(1,1) is blocked. Someone wrote `build_graph` with the first `in blocked` check but '
                     'forgot the second. What is wrong with the result?',
         'options': ['(1,1) is not a key, but it is still in its neighbors\' lists: edges into the wall',
                     '(1,1) is a key with an empty neighbor list',
                     'Nothing: the first check is enough',
                     'The graph has 16 keys instead of 15'],
         'answer': 0,
         'explanation': 'The first check removes (1,1) as a key. Only the second check removes it from the '
                        'lists of (0,1), (1,0), (1,2) and (2,1). Without it, a search could step into the wall.'},

        {'kind': 'bullets', 'title': 'Step 3 · Why rebuild every call?',
         'notes': 'The placeholder compute_bfs_path() builds the graph itself, from BLOCKED, every time '
                  'it is called, rather than once at the top of the file. Rebuilding every call means '
                  'there is no "forgot to rebuild" bug to have, and on a 4x4 grid it visits sixteen '
                  'intersections: no time worth measuring. This is the third wrap-up question. Point '
                  'back at the blocked-list figure: one way in, and every plan reads the list fresh.',
         'lead': 'Why rebuild from `BLOCKED` on **every** call, not once?',
         'lead_h': 1.0,
         'bullets': [
             'A wall found at step 3 must be **gone** when planning step 4',
             'Automatic: no "forgot to rebuild" bug',
             'On a 4×4 grid it costs nothing',
         ],
         'callout': 'Every plan uses the list **as it stands right now**',
         'tone': 'teal'},

        {'kind': 'steps', 'title': 'Step 3 · test_blocked_graph()',
         'notes': 'The lesson page describes the test in words; students write it. It exercises all '
                  'three functions. The expected output is on the next slide.',
         'lead': 'Write it, and set the run line to it.',
         'lead_h': 0.65,
         'steps': [
             'Block `(1, 1)`; build the graph',
             'Print the blocked list, intersection count, `(1, 1) in graph`, and `(0, 1)`\'s neighbors',
             'Block `(1, 1)` again; print the list',
             'Print `compute_bfs_path((0, 0), (3, 3))`',
         ]},

        {'kind': 'code', 'title': 'Step 3 · Check your output', 'tag': 'Activity',
         'code': 'Blocked: [(1, 1)]\n'
                 'Number of intersections: 15\n'
                 '(1,1) in graph? False\n'
                 'Neighbors of (0,1): [(0, 0), (0, 2)]\n'
                 'Blocked after adding (1,1) again: [(1, 1)]\n'
                 'compute_bfs_path is not written yet!\n'
                 'Path: []',
         'code_size': 22, 'width': 9,
         'callout': 'Check: **15** keys, `(1, 1)` neither a key nor `(0, 1)`\'s neighbor, list still '
                    '**one** entry long',
         'tone': 'green',
         'notes': 'The neighbors-of-(0,1) line is the one that catches the missing second in-blocked '
                  'check. The empty path is the placeholder: for now, the right answer to nothing.'},

        {'kind': 'bullets', 'title': 'Before you leave',
         'lead': 'What should these return once Lesson 5-5 is done, with nothing blocked?',
         'lead_h': 1.5,
         'bullets': [
             '`compute_bfs_path((0, 0), (0, 2))`',
             '`compute_bfs_path((2, 2), (2, 2))`',
         ],
         'size': 32,
         'callout': 'Use the two rules: what is in the path, and what is left out?',
         'tone': 'teal',
         'notes': 'Answers: [(0, 1), (0, 2)] and [], Rule 2 both times. Challenge for early finishers: '
                  'block (1, 0) and (1, 1), rebuild, and print the whole graph. Which intersections in '
                  'the left column (x = 0) can still reach the column at x = 2, and through what? Then: '
                  'using only build_graph and the wave idea, write is_reachable(a, b). They will '
                  'write most of Lesson 5-5 a day early, which is fine.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'notes': 'Rule 1 and the shared list are the same idea at any scale: one owner for each fact. '
                  'A navigation app keeps one shared list of closed roads and rebuilds its routing '
                  'graph from it: this toolkit at city scale.',
         'cards': [
             ('Maps', 'Closures', 'One shared list of closed roads; the routing graph is '
                                       'rebuilt from it.'),
             ('Software', 'One owner', 'Keep one copy of each fact and tell everything '
                                                'else. Copies drift apart.'),
             ('Robotics', 'Vacuums', 'A robot vacuum\'s map fills in as it bumps walls: '
                                            'a huge BLOCKED list.'),
         ],
         'height': 4.0},

        {'kind': 'wrapup',
         'questions': [
             'What are the two planner rules?',
             'Who calls `add_blocked()`?',
             'Why is the graph rebuilt on every call?',
             'Why no `global` in `add_blocked()`?',
         ],
         'next': 'the placeholder becomes real: compute_bfs_path()',
         'notes': 'Answers: told the position, and the path excludes the start. A paper test in 5-6, the '
                  'rangefinder in 5-7, and you in 5-8, typing in what the last run found. So a '
                  'just-found obstacle is already missing from it. Appending changes the list; it does '
                  'not reassign the name. Formative: the two rules from memory, the second in-blocked bug '
                  'caught, the global explanation. Exit ticket: "Why doesn\'t add_blocked() need global?" '
                  'Next lesson: the wave of numbers from the destination and the walk downhill from Lesson '
                  '5-2, in about twenty lines.'},
    ],
}
