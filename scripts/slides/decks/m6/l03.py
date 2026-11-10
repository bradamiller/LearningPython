BFS_PENCIL = [
    '# for each neighbor of current:',
    '#     only if it has no entry yet:',
    '#         write where it came from',
    '#         put it on the END of the list',
]
DIJKSTRA_PENCIL = [
    '# for each neighbor of current:',
    '#     this way costs: current\'s cost',
    '#         + weight(current, neighbor)',
    '#     if no cost yet, OR this is cheaper:',
    '#         write the cost',
    '#         write where it came from',
    '#         put it on the list, if not on it',
]
# The lesson's <SideBySide>: the two pencil loops as two columns of one code block.
PENCIL = '\n'.join(
    (f'{l:<41}{r}').rstrip()
    for l, r in zip(['BFS (Module 5)', ''] + BFS_PENCIL + [''] * 3,
                    ['Dijkstra', ''] + DIJKSTRA_PENCIL))

DECK = {
    'module': 6, 'lesson': 3,
    'doc': 'module-06-dijkstra/lesson-03-from-bfs-to-dijkstra',
    'title': 'From BFS to Dijkstra',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Add the cost check to `run_all_tests()` as its seventh case',
             'Duplicate `compute_bfs_path()` as `compute_dijkstra_path()` and keep the parts that don\'t change',
             'Make change 1: take the **closest** intersection off `to_visit`, not the oldest',
             'Make change 2: add the segment\'s **weight**, and keep the cheaper total when an '
             'intersection is reached again',
             'Read a `print_grid()` of costs and explain each number',
             'Run Manhattan, BFS and Dijkstra through the same harness and say where they agree and disagree',
         ],
         'notes': '60 minutes. No robot needed. The lesson\'s shape is the point: a working thing, '
                  'copied, changed in two marked places, tested after each. Students who try to '
                  'write Dijkstra fresh get lost in to_visit bookkeeping; students who copy BFS and '
                  'change two lines have it working in twenty minutes and can explain both changes.'},

        {'kind': 'bullets', 'title': 'Not a new algorithm: your BFS, upgraded',
         'bullets': [
             'BFS fails the cost check because it **never looks at a weight**',
             'The fix is your BFS, **copied**, **renamed**, and changed in **two places** in the middle',
             'Everything else stays exactly as you wrote it in Module 5: the graph, `add_blocked()`, '
             'the `previous` dictionary, the walk-back',
             'The result is **Dijkstra\'s algorithm**',
         ],
         'callout': 'By the end of the lesson: three planners running through one harness',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Skeleton, paste above `RUN` (1 of 3)',
         'lead': 'It starts the DIJKSTRA PLANNER section: a helper, the planner, the function that '
                 'draws its costs, and one given printer.',
         'lead_h': 1.0,
         'code': '# ===== DIJKSTRA PLANNER =====\n'
                 '# The third planner, made by copying the BFS PLANNER\'s\n'
                 '# function and changing two things in the middle: take the\n'
                 '# CLOSEST waiting intersection, not the oldest, and add the\n'
                 '# WEIGHTED GRAPH\'s weight() instead of counting a step,\n'
                 '# keeping the cheaper total when a place is reached twice.\n'
                 '# Same shape, same promises; the 5-6 harness tests all three.\n'
                 '\n'
                 'def closest(intersections, distance):\n'
                 '    """Return the entry of intersections with the smallest\n'
                 '    value in distance: a plain find-the-minimum loop."""\n'
                 '    pass',
         'code_size': 17},

        {'kind': 'code', 'title': 'Skeleton (2 of 3): the planner\'s outline',
         'code': 'def compute_dijkstra_path(start, destination):\n'
                 '    """Cheapest path from start to destination around\n'
                 '    BLOCKED, by weight(), as the intersections to drive to."""\n'
                 '    # SETUP: as compute_bfs_path(), plus\n'
                 '    #    distance = {start: 0}      cheapest cost so far\n'
                 '    # SEARCH\n'
                 '    #    while to_visit is not empty:\n'
                 '    #       CHANGE 1: current = the closest() one; remove it\n'
                 '    #       if current is the destination: stop looking\n'
                 '    #       for each neighbor of current in the graph:\n'
                 '    #          CHANGE 2: new cost = distance to current\n'
                 '    #                    + weight(current, neighbor)\n'
                 '    #          if neighbor has no cost yet, or this is less:\n'
                 '    #              record the new cost and where it came from\n'
                 '    #              add it to to_visit if it is not already on\n'
                 '    # WALK-BACK: unchanged from compute_bfs_path()\n'
                 '    pass',
         'code_size': 16,
         'notes': 'The outline is only the two changes, and the walk-back is "unchanged": the BFS '
                  'body goes in first, and the comments are a checklist, not a second algorithm.'},

        {'kind': 'code', 'title': 'Skeleton (3 of 3): the cost map, the printer',
         'code': 'def dijkstra_distances(start):\n'
                 '    """Cheapest cost to every reachable intersection, as a\n'
                 '    dictionary -- the search with no break, like bfs_rings()."""\n'
                 '    pass\n'
                 '\n'
                 'def compare(start, destination):\n'
                 '    """Print BFS\'s and Dijkstra\'s answers for one trip:\n'
                 '    steps, cost and path, one line each."""\n'
                 '    for (name, planner) in [("BFS", compute_bfs_path),\n'
                 '                            ("Dijkstra", compute_dijkstra_path)]:\n'
                 '        path = planner(start, destination)\n'
                 '        print(" ", "{:<9}".format(name), "steps:", len(path),\n'
                 '              " cost:", path_cost(position, path), " ", path)',
         'code_size': 15,
         'callout': '`compare()` is given: a print, not a planner. Its `for` line unpacks each pair as '
                    'it loops (Lesson 4-2): a label, and the planner function to call with it.',
         'tone': 'teal',
         'notes': '"{:<9}".format(name) is "this name, left-aligned in nine spaces", the same trick as '
                  'print_grid()\'s "{:>3}".'},

        {'kind': 'code', 'title': 'First, the harness learns to count cost',
         'lead': 'Three edits to `run_all_tests()` in the BFS PLANNER section. None of them touches '
                 'the six cases it already runs.',
         'lead_h': 1.0,
         'code': '    clear_blocked()\n'
                 '    clear_slow_edges()                      # 1. open grid, no slow edges\n'
                 '    ...                                     #    the six cases, as they are\n'
                 '    clear_blocked()\n'
                 '    add_slow_edge((0, 1), (0, 2), 5)        # 2. the seventh case: slow grid\n'
                 '    path = planner((0, 0), (0, 3))\n'
                 '    if check_cost("slow grid: (0,0) to (0,3)", (0, 0), (0, 3), path, 5):\n'
                 '        passed = passed + 1\n'
                 '    clear_slow_edges()\n'
                 '    print(name + ":", passed, "of 7 passed")   # 3. seven now',
         'code_size': 17,
         'callout': 'Run Module 5\'s `test_harness()`: Manhattan drops to **4 of 7** and BFS to **6 of '
                    '7**, each failing the new case',
         'tone': 'orange',
         'notes': 'The slow edge is cleared at the start as well as the end for the same reason the '
                  'blocked list is: a harness has to set up its own grid, not trust whatever ran '
                  'before. The harness edit comes first deliberately: a copy that fails 6 of 7 '
                  'exactly as BFS does is the proof that the copy is faithful.'},

        {'kind': 'code', 'title': 'Start by copying',
         'lead': 'Copy the body of `compute_bfs_path()` into `compute_dijkstra_path()`, in place of '
                 '`pass` and under the comments: the comments are your checklist. Change nothing else '
                 'yet. Then `test_three_planners()`: Lesson 5-6\'s `test_harness()` with a third line.',
         'lead_h': 1.5,
         'code': 'run_all_tests("Manhattan", compute_manhattan_path)\n'
                 'run_all_tests("BFS",       compute_bfs_path)\n'
                 'run_all_tests("Dijkstra",  compute_dijkstra_path)',
         'code_size': 22,
         'callout': 'The copy passes everything BFS passes and fails the same cost check. Now you have '
                    'a **safe place** to make two changes.',
         'tone': 'teal',
         'notes': 'Set the run line to test_three_planners(). Identical code, identical results: '
                  'that is what students should expect, and see.'},

        {'kind': 'bullets', 'title': 'Change 1 · Closest first, not oldest first',
         'bullets': [
             'BFS takes intersections off `to_visit` in the order they went on: `to_visit.pop(0)`',
             'That works because every step costs the same: the oldest entry is always one of the closest',
             'With weights that is no longer true',
             'An intersection reached by a **cheap detour** may be closer, in cost, than one that went '
             'on the list earlier by a **slow road**',
         ],
         'callout': 'So Dijkstra takes the waiting intersection that is **cheapest so far**, whenever '
                    'it went on the list',
         'tone': 'orange'},

        {'kind': 'bullets', 'title': 'Change 1 · `distance` and `closest()`',
         'bullets': [
             'A second dictionary, `distance`: the cheapest cost found so far to each intersection',
             'It starts as `{start: 0}`, because the start costs nothing to reach',
             'Each time round the loop: `closest(to_visit, distance)`',
             ['Assume the first entry is best, loop over the rest, keep any entry whose `distance` is smaller',
              'Finding the biggest number in a list (Module 1), with the comparison turned round'],
         ],
         'callout': '`pop(0)` did two jobs, choosing **and** removing. `closest()` only chooses, so the '
                    'line after it has to `remove()` the chosen one from `to_visit`.',
         'tone': 'teal',
         'notes': 'closest() is a linear scan. Real implementations use a priority queue, and the old '
                  'version of this material taught one; don\'t. For a 4 by 4 grid the scan is '
                  'instant, and the queue is machinery that hides the two ideas. If a student asks: '
                  '"a priority queue is a faster way to do what closest() does" is the whole answer.'},

        {'kind': 'figure', 'title': 'The moment the two choices differ',
         'figure': '/img/lesson-m6-03/closest-vs-oldest-xy.svg',
         'caption': 'Taking the oldest would settle (0, 2) at 6; taking the closest leaves it waiting '
                    'long enough for a cheaper way to turn up.',
         'notes': 'Dijkstra partway through on the slow grid. to_visit holds (0, 2) at cost 6, the '
                  'oldest, then three intersections at cost 3. pop(0) would take (0, 2); closest() '
                  'takes (3, 0). Before (0, 2) comes up, (1, 2) reaches it for 4. (This slide uses a '
                  'copy of the lesson figure widened slightly so its right-hand notes are not cut off.)'},

        {'kind': 'check',
         'question': 'Why can BFS get away with taking the oldest intersection off `to_visit`, and '
                     'Dijkstra cannot?',
         'options': ['BFS lists are shorter',
                     'Every step costing 1 keeps the oldest among the closest; with weights, a later '
                     'entry reached cheaply can be closer than an earlier one reached by a slow road',
                     'Dijkstra uses a dictionary and BFS uses a list',
                     'It can; the change is only for speed'],
         'answer': 1,
         'explanation': 'BFS\'s rings are rings of steps and rings of cost at once. Weights break that: '
                        'cost no longer grows in step with order of discovery, so the planner has to '
                        'look up which waiting intersection is cheapest.'},

        {'kind': 'bullets', 'title': 'Change 2 · Add the weight, keep the cheaper way',
         'bullets': [
             'BFS marks a neighbor the **first** time it sees it and never reconsiders',
             'That is safe for BFS: the first way to reach it is always a shortest way, in steps',
             'Dijkstra adds the edge\'s **weight** to get the cost of reaching the neighbor **this** way',
             'If that beats what it already had, it **updates**',
         ],
         'callout': 'A neighbor reached again by a **cheaper** route gets a new cost and a new '
                    'came-from',
         'tone': 'teal',
         'notes': 'Lesson heading: "Change 2 · Add the weight, and keep the cheaper way". The next '
                  'slide compares the pencil versions of the two neighbor loops.'},

        {'kind': 'code', 'title': 'The two neighbor loops, in pencil',
         'code': PENCIL,
         'code_size': 18,
         'notes': 'On the lesson page these are two blocks side by side; the slide sets them in two '
                  'columns of one block.'},

        {'kind': 'bullets', 'title': 'Three things to notice',
         'bullets': [
             '"Has no entry yet" was `not in previous` in BFS. Now it is `not in distance`: `distance` '
             'says whether a cost has been found.',
             'The **or** is the whole of change 2: a neighbor that already has a cost is reconsidered, '
             'and loses its old cost and old came-from if this way is cheaper',
             '"If not on it" matters now: a neighbor can be reached a second time while still waiting '
             'on `to_visit`, and must not be listed twice',
         ],
         'callout': '`previous[neighbor] = current` still remembers the path, and the walk-back is '
                    'untouched. New: `previous` can be **overwritten** when a cheaper way turns up.',
         'tone': 'orange',
         'notes': 'The "if not on it" check is the line students skip. Without it the open-grid cases '
                  'still pass but to_visit fills with duplicates, so ask them why BFS never needed it.'},

        {'kind': 'check',
         'question': 'In Dijkstra, what happens when the planner reaches an intersection it has already '
                     'recorded, by a cheaper route?',
         'options': ['Nothing: the first way found is kept, as in BFS',
                     '`distance` and `previous` for that intersection are overwritten with the cheaper '
                     'total and the new way in',
                     'The planner stops and returns the path',
                     'The intersection is added to `BLOCKED`'],
         'answer': 1,
         'explanation': 'That is change 2. BFS never reconsiders because its first discovery is already '
                        'shortest in steps. Dijkstra may find a cheaper way later and must keep it, '
                        'including the previous pointer that the walk-back will follow.'},

        {'kind': 'steps', 'title': 'Activity · Make the two changes',
         'lead': 'Work on your copy, in order. Run `test_three_planners()` after each step, and don\'t '
                 'go on until the result matches.',
         'steps': [
             'Write `closest()`. Add `distance = {start: 0}` to the setup and swap `to_visit.pop(0)` '
             'for `closest()` + `remove()`. Harness: still **6 of 7**: the cost case still fails, '
             'because nothing adds a weight yet.',
             'Replace the neighbor loop with the weighted version. Harness: **7 of 7**. The cost check '
             'passes, with a five-step path where BFS printed three.',
             'Read all three planners\' results. Manhattan fails the two blocked cases and the cost '
             'case; BFS fails only cost on the slow grid; Dijkstra passes everything.',
         ],
         'size': 20,
         'notes': 'On the open grid with no slow edges, all three agree on every path length. Watching '
                  'the seventh case flip to PASS at step 2 is the lesson\'s payoff. Class track: if '
                  'you built the BFS class in Lesson 5-5, the copy is of the class. Lesson 6-5 is '
                  'this lesson\'s class-track version, with the same two changes inside '
                  'compute_path(), and can be done now in place of the function version.'},

        {'kind': 'code', 'title': 'Last test: `test_cost_grid()`',
         'lead': 'Add the slow segment and call `compare((0, 0), (0, 3))`:',
         'code': '  BFS       steps: 3  cost: 7   [(0, 1), (0, 2), (0, 3)]\n'
                 '  Dijkstra  steps: 5  cost: 5   [(1, 0), (1, 1), (1, 2), (0, 2), (0, 3)]',
         'code_size': 20,
         'callout': 'Your Dijkstra path may go round a different way, back left at `(0, 2)` or on to '
                    '`(1, 3)` first, and still be right. **Cost 5** is what matters.',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'On a grid with no blocked intersections and no slow edges, how do the three '
                     'planners\' paths compare?',
         'options': ['Dijkstra\'s paths are shorter',
                     'All three are the same length; the planners only disagree when a wall or a slow '
                     'segment gives them a reason to',
                     'Manhattan fails',
                     'BFS and Dijkstra return `[]`'],
         'answer': 1,
         'explanation': 'Without obstacles, every planner finds a shortest Manhattan route. Walls '
                        'separate Manhattan from the other two; weights separate BFS from Dijkstra. '
                        'Each upgrade earns its keep on exactly the grid that needs it.'},

        {'kind': 'code', 'title': 'The cost grid',
         'lead': '`dijkstra_distances()` is to `compute_dijkstra_path()` what `bfs_rings()` was to '
                 '`compute_bfs_path()` in Lesson 5-5: the setup and the search, with no `break` and no '
                 'walk-back, returning `distance` itself. Write it, then add one line to `test_cost_grid()`:',
         'lead_h': 1.5,
         'code': 'print_grid(ROWS, COLS, BLOCKED, dijkstra_distances((0, 0)))',
         'code_size': 22,
         'callout': 'Dijkstra\'s `distance` dictionary is a map of how far everything is, in cost, from '
                    'the start',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Read up the left edge, x = 0',
         'bullets': [
             '(0, 1) costs 1, then (0, 2) costs **4**, not 2',
             'The slow segment would make it 1 + 5 = 6',
             'Over to (1, 1), up to (1, 2) and back left costs 1 + 1 + 1 + 1 = 4, so 4 is kept',
             'That one cell is **change 2** doing its job',
             'Everywhere else, the numbers are Module 5\'s BFS rings',
         ],
         'split': 0.55,
         'code': ' 3 |   5  4  5  6\n'
                 ' 2 |   4  3  4  5\n'
                 ' 1 |   1  2  3  4\n'
                 ' 0 |   0  1  2  3\n'
                 '    -------------\n'
                 '       0  1  2  3',
         'code_size': 26,
         'notes': 'The cost grid is where the understanding shows. Ask students to point at the one '
                  'cell that differs from BFS and say why before they look at the explanation.'},

        {'kind': 'figure', 'title': 'Why (0, 2) is 4, not 2',
         'figure': '/img/lesson-m6-03/cost-grid-xy.svg',
         'caption': 'The one cell that is not a BFS ring, and the two ways of reaching it.'},

        {'kind': 'check',
         'question': 'In the cost grid, why is (0, 2) a 4 rather than a 2?',
         'options': ['A typo in the grid',
                     'Straight up the left edge costs 1 + 5 = 6 because of the slow segment; the '
                     'detour through x = 1 costs 4, and Dijkstra keeps the cheaper total',
                     'Because (0, 2) is blocked',
                     'Because the grid is 4 wide'],
         'answer': 1,
         'explanation': 'Every other cell matches the BFS ring numbers. (0, 2) is the one place the slow '
                        'segment is on the direct route, and the printed 4 is the cheaper way round it.'},

        {'kind': 'frames', 'title': 'A bigger grid: how the two searches spread',
         'figure': '/img/lesson-m6-03/fanout-bfs-vs-dijkstra.svg',
         'crop': (0.0, 0.1, 0.565, 1.0),
         'frames': [(0.415, '**BFS**, by steps: over the top, 9 steps, cost 17'),
                    (0.975, '**Dijkstra**, by cost: round the bottom, 15 steps, cost 15')],
         'callout': 'BFS spreads by steps, so the slow road looks like any other street. Dijkstra '
                    'spreads by cost, so its wave slows down where the road is slow.',
         'tone': 'teal',
         'notes': 'On the lesson page this is an animation with two buttons, on the 8 by 6 grid from '
                  'Lesson 5-3: a wall of four blocked intersections at x = 3, a slow road (5 per '
                  'block) across the top gap, S at (0, 4) and D at (7, 4). These are its two end '
                  'states: BFS finished and Dijkstra finished. Midway through the Dijkstra run the '
                  'wave has raced along the bottom to cost 11 while the slow road has only reached '
                  'the top middle, at 8. On the 4 by 4 floor grid one slow segment '
                  'changes one number; a bigger grid shows what change 1 does to the shape of the '
                  'search.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('History', '1956',
              'Edsger Dijkstra designed this in about twenty minutes, in his head, in a cafe, as a '
              'demonstration for a new computer. It is still the standard.'),
             ('Maps', 'Under every route',
              'Map apps run Dijkstra\'s algorithm (and descendants of it) over road networks with '
              'millions of weighted edges.'),
             ('Engineering', 'Upgrade by diff',
              'Changing two lines of tested code and re-running the tests is how most real '
              'improvements ship. The copy you kept is the rollback.'),
         ]},

        {'kind': 'wrapup',
         'questions': [
             'What are the two changes?',
             'What is `distance`?',
             'Where do the three planners disagree?',
         ],
         'next': 'the robot drives the slow grid twice, and the class times both runs',
         'notes': 'Answers: closest first; add the weight and keep the cheaper total. The cheapest cost '
                  'found so far to each intersection. Walls split off Manhattan; weights split BFS from '
                  'Dijkstra. Formative: point to the two changed regions in the copy; explain '
                  'closest(); explain one cell of the cost grid. Exit ticket: "Why does Dijkstra '
                  'sometimes overwrite previous[neighbor], when BFS never does?" Next: a BFS run and a '
                  'Dijkstra run on the slow grid, timed.'},
    ],
}
