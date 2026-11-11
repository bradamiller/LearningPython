DECK = {
    'module': 6, 'lesson': 2,
    'doc': 'module-06-dijkstra/lesson-02-weights-in-the-graph',
    'title': 'Weights in the Graph',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Store slow segments as `(a, b, cost)` entries and add one with `add_slow_edge()`',
             'Write `weight(a, b)` so it returns the slow cost in either direction and 1 otherwise',
             'Write `path_cost(position, path)` by walking the path and summing weights',
             'Write `check_cost()`, the cost check, and explain what its FAIL line means',
             'State BFS\'s limitation precisely: it minimizes steps, and cost is not steps',
         ],
         'notes': '50 minutes. No robot needed: every test today is a paper test. Students need '
                  'the weight they measured in Lesson 6-1.'},

        {'kind': 'bullets', 'title': 'You have a weight. Now the program needs it.',
         'bullets': [
             'A new section of `robot.py`: a list of **slow segments** next to the blocked list',
             '`weight()` answers "what does this edge cost?"',
             '`path_cost()` adds a route up',
             'Then **cost** becomes one more thing the Module 5 harness checks',
             'BFS, unchanged, **fails** that check: on paper, with the path printed, before any robot is involved',
         ],
         'callout': 'That failure is the reason the next lesson exists',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Skeleton, paste above `RUN` (1 of 2)',
         'code': '# ===== WEIGHTED GRAPH =====\n'
                 '# The grid with a cost on every edge. A normal block costs 1;\n'
                 '# a slow segment costs what you measured in Lesson 6-1. The\n'
                 '# slow list is kept the way GRID GRAPH keeps BLOCKED, and\n'
                 '# weight() is the one question every planner asks of it.\n'
                 '# path_cost() adds a route up; check_cost() is a sixth\n'
                 '# property for the BFS PLANNER\'s harness, and BFS fails it.\n'
                 'SLOW_EDGES = []          # (a, b, cost), one per slow segment\n'
                 '\n'
                 'def add_slow_edge(a, b, cost):\n'
                 '    """Record the segment between a and b as costing cost."""\n'
                 '    pass\n'
                 '\n'
                 'def clear_slow_edges():\n'
                 '    """Empty SLOW_EDGES in place, as clear_blocked() does."""\n'
                 '    pass',
         'code_size': 16,
         'notes': 'It starts the WEIGHTED GRAPH section: one list, five function outlines, no tests '
                  'yet. One paste: the skeleton is split over two slides to fit. Students write the '
                  'tests as they go, as in Module 5.'},

        {'kind': 'code', 'title': 'Skeleton, paste above `RUN` (2 of 2)',
         'code': 'def weight(a, b):\n'
                 '    """Cost of driving from a to b: the slow cost if that\n'
                 '    segment is in SLOW_EDGES, in either order; otherwise 1."""\n'
                 '    pass\n'
                 '\n'
                 'def path_cost(position, path):\n'
                 '    """Total cost of driving path from position: the weight\n'
                 '    of every segment, starting with position to path[0]."""\n'
                 '    pass\n'
                 '\n'
                 'def check_cost(test_name, start, destination, path, expected_cost):\n'
                 '    """Print PASS if path costs expected_cost, else FAIL with\n'
                 '    the cost and the path; return True on a pass."""\n'
                 '    pass',
         'code_size': 17},

        {'kind': 'bullets', 'title': 'A second list, next to `BLOCKED`',
         'bullets': [
             'Module 5 kept what the planner knows about the grid in `BLOCKED`, fed through '
             '`add_blocked()` and emptied by `clear_blocked()`',
             'Slow segments get the same treatment: `SLOW_EDGES`, fed through `add_slow_edge()`, '
             'emptied by `clear_slow_edges()`',
             'Both are one-liners shaped like their Module 5 twins',
             'A slow segment belongs to the **edge** between two intersections, not to either one, so '
             'each entry holds both ends and the weight you measured',
         ],
         'callout': '`add_slow_edge((0, 1), (0, 2), 5)` appends the tuple `((0, 1), (0, 2), 5)`',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': '`weight(a, b)`: in either order',
         'bullets': [
             'The one question every planner will ask',
             'It loops over `SLOW_EDGES` looking for the pair, and returns 1 if it never finds it',
             'The robot might drive the segment from (0, 1) to (0, 2) **or** from (0, 2) to (0, 1), '
             'and it is slow both ways',
             'So the test inside the loop matches the pair **either way round**: an `or` of two comparisons',
         ],
         'callout': 'Anything not in the list costs 1: a normal block',
         'tone': 'orange',
         'notes': 'The or in weight() is easy to drop, and then the check passes or fails depending '
                  'on which way the robot happens to drive the segment. A good bug to plant.'},

        {'kind': 'check',
         'question': '`SLOW_EDGES` holds `((0, 1), (0, 2), 5)`. What do `weight((0, 2), (0, 1))` and '
                     '`weight((1, 1), (1, 2))` return?',
         'options': ['5 and 5',
                     '5 and 1: the slow segment matches in either order; a segment not in the list '
                     'is a normal block',
                     '1 and 1',
                     'An error, because the first pair is backwards'],
         'answer': 1,
         'explanation': 'The or in the if makes the match direction-free; the final return 1 is the '
                        'default for every ordinary segment.'},

        {'kind': 'bullets', 'title': 'Adding up a route',
         'bullets': [
             'A path from the planner is the intersections to drive to, **not including the start**',
             'Its cost is the weight of every segment driven: start to the first step, that step to '
             'the next, and so on',
             '`path_cost()` keeps a running total and a `here` that starts at the robot\'s position '
             'and moves forward one step each pass',
             'Same shape as `drive_path()`\'s `position = next_pos`',
         ],
         'callout': 'For `[(0, 1), (0, 2), (0, 3)]` from (0, 0), with the slow edge at 5: 1 + 5 + 1 = 7',
         'tone': 'teal'},

        {'kind': 'figure', 'title': 'Why `path_cost()` is handed position',
         'figure': '/img/lesson-m6-02/path-cost.svg',
         'caption': 'The path leaves out the start, but the first segment begins there.',
         'notes': 'path_cost() must start from position, not from path[0]. Students who start at '
                  'path[0] miss the first segment and get costs one too small; step 2 of the '
                  'activity is written to catch exactly that.'},

        {'kind': 'check',
         'question': 'Why does `path_cost()` need the `position` parameter, when the path is right there?',
         'options': ['It does not; position is unused',
                     'The path excludes the start (Lesson 4-4\'s promise 1), so the first segment runs from '
                     'position to path[0], and only the caller knows position',
                     'To check the path is not empty',
                     'Because `weight()` requires three arguments'],
         'answer': 1,
         'explanation': 'Every planner in the course returns the intersections to drive TO. The segment '
                        'from where the robot is to the first of those is part of the trip, and its '
                        'weight counts.'},

        {'kind': 'bullets', 'title': 'The sixth property',
         'bullets': [
             'The Module 5 harness checks **five** properties of a path. Add a sixth: the path\'s cost '
             'equals the **cheapest possible**',
             'For now you work out the cheapest by hand, trace the routes and add them up, and type '
             'the number in. The next lesson writes the planner that finds it.',
             '`check_cost()` is shaped like Lesson 5-6\'s `run_no_path_test()`: a PASS or FAIL line in '
             'the same format, and `True` on a pass, so the harness can count it',
             'One difference: it is handed the **path**, not the planner, so you can point it at any '
             'planner\'s answer',
         ],
         'notes': 'check_cost() prints in the 5-6 format and returns True for a reason: next lesson it '
                  'becomes the seventh case inside run_all_tests(), and the count line becomes "of 7". '
                  'clear_slow_edges() exists for the same reason: the harness has to run its open-grid '
                  'cases with no slow edges.'},

        {'kind': 'code', 'title': 'A PASS line and a FAIL line',
         'lead': 'As they should look:',
         'code': '  PASS  open grid  [(0, 1), (0, 2), (0, 3)]  cost: 3\n'
                 '  FAIL  slow grid  [(0, 1), (0, 2), (0, 3)]  cost: 7\n'
                 '          - the cheapest route costs 5',
         'code_size': 22,
         'callout': 'The FAIL line prints the path and its cost, then the cost it should have had',
         'tone': 'teal'},

        {'kind': 'steps', 'title': 'Activity · Build it, then watch BFS fail',
         'lead': 'Every test today is a paper test: the robot stays on the desk.',
         'steps': [
             '**The list and** `weight()`**.** Write `add_slow_edge()`, `clear_slow_edges()` and '
             '`weight()`. Then write `test_weights()`: clear the slow list, add your segment from '
             'Lesson 6-1, and print `weight()` for the slow pair in both orders and for one ordinary '
             'pair. Run it: your weight, your weight, 1.',
             '`path_cost()`**.** Write the body, and add two lines to `test_weights()`: the cost of '
             'Route A and Route B from Lesson 6-1, from `(0, 0)`, typed in as lists. Expect 7 and 5 '
             'with a weight of 5. Route A one too small? Your loop started at `path[0]` instead of '
             '`position`.',
         ],
         'notes': 'Make students write the expected cost by hand before they run the check; if they '
                  'let the program tell them what to expect, the test tests nothing (Lesson 4-4\'s '
                  'point).'},

        {'kind': 'bullets', 'title': 'Step 3 · `check_cost()`, against BFS',
         'tag': 'Activity',
         'bullets': [
             'Write `check_cost()`',
             'Then a second test, `test_cost_check()`, that runs it against BFS twice:',
             ['**Open grid:** clear the blocked list **and** the slow list, plan `(0, 0)` to `(0, 3)` '
              'with `compute_bfs_path()`, and check it against a cost of 3',
              '**Slow grid:** add the slow segment at weight 5, plan the same trip, and check it '
              'against 5, the cost of the detour you added up in Lesson 6-1'],
         ],
         'callout': 'Built the `BFS` class? Plan with `planner.compute_path()` and clear with '
                    '`planner.clear_blocked()`. The slow list is this section\'s own.',
         'tone': 'teal',
         'notes': 'Class track: add_slow_edge() and clear_slow_edges() are called as written, '
                  'because the slow list belongs to the WEIGHTED GRAPH section, not to the planner.'},

        {'kind': 'code', 'title': 'Step 3 · There it is',
         'lead': 'Set the run line to `test_cost_check()`:',
         'code': '  PASS  open grid  [(0, 1), (0, 2), (0, 3)]  cost: 3\n'
                 '  FAIL  slow grid  [(0, 1), (0, 2), (0, 3)]  cost: 7\n'
                 '          - the cheapest route costs 5',
         'code_size': 22,
         'callout': 'Not a crash, not a wrong turn on the floor: a FAIL line with the path printed. '
                    'BFS drove the slow road, because it counts steps and 3 is less than 5.',
         'tone': 'orange',
         'notes': 'This is Lesson 5-6\'s idea doing its job: the failure is found at a desk, not a '
                  'robot taking the long way while everyone wonders.'},

        {'kind': 'check',
         'question': 'BFS passes every Module 5 property on the slow grid and fails only the cost '
                     'check. What does that tell you?',
         'options': ['BFS is broken and must be rewritten from scratch',
                     'BFS does exactly what it promises, fewest steps, and cost is a different thing '
                     'it was never asked to minimize',
                     'The harness is wrong',
                     'The slow segment should be blocked instead'],
         'answer': 1,
         'explanation': 'A property test tells you precisely which promise failed. The path is valid, '
                        'connected, unblocked and shortest in steps. It is not cheapest, and nothing '
                        'in BFS ever looks at a weight.',
         'notes': 'Name the limitation exactly: BFS minimizes steps; it never looks at a weight. '
                  'Don\'t say BFS is wrong. Next lesson keeps 90% of it.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Maps', 'Edge attributes',
              'Road networks store a speed, a length and a toll on every edge: exactly a weight '
              'table, far larger than yours.'),
             ('Testing', 'A new requirement, a new test',
              'When "fewest steps" became "least time", the first move was a test, not a rewrite. '
              'Working code failing a new test is how software grows.'),
             ('Networks', 'Symmetric links',
              'Most links cost the same both ways, which is what the `or` in `weight()` encodes. '
              'One-way streets are the exception.'),
         ],
         'notes': 'One-way streets are a good extension question: how would weight() change?'},

        {'kind': 'wrapup',
         'questions': [
             'Where does a slow segment live, and how does it get there?',
             'What does `weight(a, b)` return for an ordinary segment?',
             'Why does `path_cost()` take `position`?',
             'What exactly did BFS fail?',
         ],
         'next': 'copy your BFS, change two places, and the FAIL becomes a PASS',
         'notes': 'Answers: in SLOW_EDGES, via add_slow_edge(a, b, cost). 1. The path excludes the '
                  'start. The cost check: it minimized steps, as promised. Formative: write weight() '
                  'with the or; trace path_cost() on a three-step path; read a FAIL line and say what '
                  'BFS did. Exit ticket: "Why does BFS pass the open-grid cost check and fail the '
                  'slow one?" Next: the cost check goes into run_all_tests() as case seven; then '
                  'copy compute_bfs_path, rename it, change two places.'},
    ],
}
