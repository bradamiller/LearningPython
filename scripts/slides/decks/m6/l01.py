DECK = {
    'module': 6, 'lesson': 1,
    'doc': 'module-06-dijkstra/lesson-01-fewest-steps-isnt-fastest',
    'title': 'When Fewest Steps Isn\'t Fastest',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Explain why the shortest path in steps is not always the fastest in time',
             'Time a normal block and the slow segment, and turn the ratio into a **weight**',
             'Add up the cost of a route by hand, with and without the slow segment',
             'Predict which of two routes BFS will choose, and whether it is the faster one',
             'Say why a slow segment that costs exactly three blocks is not slow enough to matter',
         ],
         'notes': '45 minutes. Stopwatch and paper. Set the grid up before class: re-tape one '
                  'segment between two adjacent intersections as a winding detour that takes at '
                  'least four normal blocks\' time to drive (five is better). Same tape width, '
                  'gentle curves, and test it with track_to_intersection() before students arrive. '
                  'Both intersections must still read as crosses. Between (0, 1) and (0, 2) on a '
                  '4 by 4 grid, with trips up the left edge (x = 0), works well.'},

        {'kind': 'bullets', 'title': 'Today one block is different',
         'bullets': [
             'Module 5\'s planner finds the path with the **fewest steps**',
             'So far that has always been the fastest path too: every block took the same time',
             'Your teacher has changed one segment so the tape takes a **long detour** between two '
             'neighboring intersections',
             'The map still says one step. The robot will take a lot longer than one step to drive it.',
         ],
         'callout': 'Today: measure that, and turn it into a **number the planner can use**',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'The grid has a slow road',
         'bullets': [
             'One segment winds back and forth before it arrives',
             'Line following still works on it: the sensors don\'t care that the tape wiggles',
             'But the robot has to drive the **whole length** of the wiggle',
             'To the Module 5 graph it is still one edge: `(0, 1)` is a neighbor of `(0, 2)`, full stop',
             '`build_graph()` has no way to say "this neighbor is far"',
         ],
         'callout': '`compute_bfs_path()` counts edges, so from (0, 0) to (0, 3) it picks the straight '
                    'run up the left edge, three steps, along the slow road, every time',
         'tone': 'orange'},

        {'kind': 'figure', 'title': 'The floor and the graph disagree',
         'figure': '/img/lesson-m6-01/floor-vs-graph-xy.svg',
         'caption': 'The graph needs a number on each edge that says how long it takes, and the '
                    'stopwatch is where that number comes from.',
         'notes': 'Left: the left edge of the floor, x = 0, with two straight blocks of about 4 '
                  'seconds and the winding one of about 20. Middle: the Module 5 graph calls every '
                  'edge 1 step. Right: with weights, the edges are 1, 5 and 1.'},

        {'kind': 'check',
         'question': 'Why does `compute_bfs_path()` choose the slow road without hesitation?',
         'options': ['It has a bug',
                     'It counts steps, and the slow road is one step like any other: the graph has '
                     'no way to say an edge is long',
                     'It prefers rows to columns',
                     'It always chooses the first neighbor in the list'],
         'answer': 1,
         'explanation': 'BFS finds the path with the fewest edges. Nothing in the graph or the planner '
                        'knows one edge takes longer to drive than another. That information does '
                        'not exist yet: this module adds it.'},

        {'kind': 'steps', 'title': 'Activity · Measure it',
         'lead': 'A planner needs a number, not "it\'s slow." Get one with a stopwatch:',
         'steps': [
             'Time the robot driving one **normal** block, intersection to intersection, with '
             '`track_to_intersection()`. Do it three times and average.',
             'Time the robot driving the **slow** segment the same way, three times, and average.',
             'Divide: slow time ÷ normal time. That ratio is the segment\'s **weight**: how many '
             'normal blocks\' worth of time it costs.',
         ],
         'notes': 'The stopwatch activity is the heart of the lesson. The weight has to come from a '
                  'measurement students made, or the module is just arithmetic. Three timings each '
                  'and an average also quietly revisits why we measure more than once.'},

        {'kind': 'code', 'title': 'From two averages to a weight',
         'code': 'Normal block:   4.1 s   4.0 s   4.2 s    average 4.1 s\n'
                 'Slow segment:  19.8 s  20.5 s  20.1 s    average 20.1 s\n'
                 '\n'
                 'weight = 20.1 / 4.1 = 4.9  -> call it 5',
         'code_size': 24,
         'callout': 'Round to a whole number: the planner needs to know this edge is about five '
                    'times worse. **Write your weight down.** Lesson 6-2 types it into the program.',
         'tone': 'teal',
         'notes': 'The planner does not need two decimal places. Make sure every group leaves with '
                  'its own weight written down.'},

        {'kind': 'check',
         'question': 'A normal block takes 4 seconds and the slow segment takes 16. What is its weight?',
         'options': ['16',
                     '4: it costs four normal blocks\' worth of time',
                     '12',
                     '0.25'],
         'answer': 1,
         'explanation': 'weight = slow time / normal time = 16 / 4 = 4. A weight is measured in '
                        'blocks, not seconds, so the same number works whatever speed the robot '
                        'drives at.'},

        {'kind': 'code', 'title': 'Cost on paper',
         'lead': 'From (0, 0) to (0, 3) on a 4×4 grid, slow segment between (0, 1) and (0, 2) at '
                 'weight 5. A route\'s **cost** is the sum of its edge weights.',
         'lead_h': 1.0,
         'code': 'Route A, straight up the left edge (x = 0):\n'
                 '  (0,0) -> (0,1) -> (0,2) -> (0,3)\n'
                 '  cost =    1   +    5   +    1    = 7       (3 steps)\n'
                 '\n'
                 'Route B, right, up through x = 1, and back:\n'
                 '  (0,0) -> (1,0) -> (1,1) -> (1,2) -> (1,3) -> (0,3)\n'
                 '  cost =    1   +    1   +    1   +    1   +    1    = 5       (5 steps)',
         'code_size': 18,
         'callout': 'Route A has fewer steps. Route B is faster. **BFS picks A.**',
         'tone': 'orange'},

        {'kind': 'check',
         'question': 'With the slow segment at weight 5, which route does BFS choose from (0,0) to '
                     '(0,3), and what does it cost?',
         'options': ['Route B, cost 5: BFS finds the cheapest path',
                     'Route A, cost 7: BFS finds the fewest steps, and A has 3 steps to B\'s 5',
                     'Route A, cost 3',
                     'Neither; it reports no path'],
         'answer': 1,
         'explanation': 'BFS compares 3 steps against 5 steps and takes 3. It never sees the 7, '
                        'because cost is not something it computes. The robot pays the extra time '
                        'on the floor.'},

        {'kind': 'bullets', 'title': 'Why three isn\'t enough',
         'bullets': [
             'Try the same comparison with the slow segment at weight **3**',
             'Route A costs 1 + 3 + 1 = 5. Route B still costs 5. **They tie.**',
             'Going round one segment on an open grid always takes exactly **three** normal blocks',
             'So weight 3 is the break-even point',
         ],
         'callout': 'For the two planners to **disagree**, the slow segment needs a weight of **4 or '
                    'more**. If your stopwatch gave you 3, ask your teacher to make the detour longer.',
         'tone': 'orange',
         'notes': 'If your detour comes out at exactly weight 3, the module falls flat. Lengthen it.'},

        {'kind': 'figure', 'title': 'The slow edge, or the three blocks around it',
         'figure': '/img/lesson-m6-01/break-even-xy.svg',
         'caption': 'Going around one segment always costs 3. The slow segment has to cost more than '
                    'that before going around wins.'},

        {'kind': 'check',
         'question': 'The slow segment measures weight 3. From (0,0) to (0,3), what happens?',
         'options': ['The detour is faster by 2',
                     'Straight costs 1+3+1 = 5 and the detour costs 5: a tie, so the slow road is '
                     'not slow enough to change the answer',
                     'The straight route is faster by 2',
                     'BFS reports no path'],
         'answer': 1,
         'explanation': 'Going round one segment costs three normal blocks on an open grid, so weight '
                        '3 exactly breaks even. The module needs the slow segment to be worse than that.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Maps', 'Fastest, not shortest',
              'A map app\'s route is rarely the fewest turns or the fewest miles; it is the least '
              'time, with each road weighted by its speed.'),
             ('Networks', 'Link costs',
              'Internet routers weight links by bandwidth and delay; more hops over fast links beat '
              'a short path over a slow one.'),
             ('Logistics', 'Toll roads and traffic',
              'Delivery routing adds tolls, traffic and loading time to distance. The cheapest '
              'route has the smallest total.'),
         ],
         'notes': 'Every real router works in time or cost, not hops.'},

        {'kind': 'wrapup',
         'questions': [
             'What does a weight mean?',
             'How do you get one?',
             'What is a route\'s cost?',
             'Why isn\'t weight 3 enough?',
         ],
         'next': 'the weight goes into the program, and BFS fails a new test',
         'notes': 'Answers: how many normal blocks\' worth of time a segment costs. Time the slow '
                  'segment, divide by a normal block, round. The sum of its edge weights. The '
                  'detour around one segment is 3 blocks, so it ties. Formative: compute a weight '
                  'from two timings; add up two routes by hand; say which BFS picks. Exit ticket: '
                  '"Weight 4, from (0,0) to (0,3): cost of each route, and which is faster?" '
                  '(A: 6, B: 5; B.) Next lesson the weight goes into the program, the harness '
                  'learns to add up cost, and BFS fails the new test on screen.'},
    ],
}
