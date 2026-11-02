DECK = {
    'module': 6, 'lesson': 0,
    'doc': 'module-06-dijkstra/lesson-00-overview',
    'title': 'The Same Algorithm, One Upgrade',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Measure a slow segment and turn it into a number: its **weight**',
             'Add a cost check to the Module 5 test harness, and show BFS failing it',
             'Turn your `compute_bfs_path()` into `compute_dijkstra_path()` by making two changes to a copy',
             'Read a cost grid and explain every number on it',
             'Run three planners through one harness and say exactly where they agree and disagree',
         ],
         'notes': '15 to 20 minutes. Optional module, 1 to 2 weeks, after Module 5. The course is '
                  'complete at the end of Module 5 and nothing later depends on this, so it can be '
                  'dropped cleanly. It needs a physical change to the grid: one segment has to be '
                  'genuinely slow, something students can time. The leading candidate is a winding '
                  'tape detour between two adjacent intersections; try it on your grid before '
                  'scheduling the module. Pacing: weeks 19 to 20 of an 18-week course, or a second '
                  'semester.'},

        {'kind': 'bullets', 'title': 'Fewest steps, or least time?',
         'bullets': [
             'Module 5 ended with a robot that finds its own way around blocked intersections',
             'It uses **breadth-first search**, which finds the path with the **fewest steps**',
             'On a grid where every block takes the same time, that is also the **fastest** path',
             'But suppose one segment takes a long, winding detour, so that driving it takes as long '
             'as **five** ordinary blocks',
             'The map still says it is one step. BFS will happily send the robot down it, because BFS '
             'only counts steps.',
         ],
         'callout': '**Dijkstra\'s algorithm** is your BFS with two changes. It finds the path that '
                    'takes the least **time**, not the fewest steps.',
         'tone': 'orange'},

        {'kind': 'figure', 'title': 'The same trip, two planners',
         'figure': '/img/lesson-m6-00/slow-road-xy.svg',
         'caption': 'BFS counts steps and takes the slow road; Dijkstra adds up time and goes around it.',
         'notes': 'BFS goes straight up the left edge, x = 0, through the slow segment between '
                  '(0, 1) and (0, 2): 3 steps, cost 7. Dijkstra goes right, up through x = 1 and '
                  'back left: 5 steps, cost 5. Cost here means blocks\' worth of time.'},

        {'kind': 'bullets', 'title': 'What this module is not',
         'bullets': [
             'It is not a new kind of programming: there is **no new Python syntax** in it',
             'The graph, `add_blocked()`, the `previous` dictionary, the walk-back and the harness '
             'are all the ones you built in Module 5, in the same `robot.py`',
             'The harness gains **one case**',
             'The file gains two sections above `RUN`: **WEIGHTED GRAPH** and **DIJKSTRA PLANNER**',
         ],
         'callout': 'The two changes are in the middle of **one function**',
         'tone': 'teal'},

        {'kind': 'cards', 'title': 'The two changes',
         'height': 3.4,
         'cards': [
             ('Change 1', 'Closest, not oldest',
              'Take the **closest** intersection off the to-visit list instead of the oldest one.'),
             ('Change 2', 'Add the weight',
              'Add the segment\'s **weight** instead of counting one step, and keep the cheaper '
              'total if you reach the same place a second time.'),
         ],
         'notes': 'That\'s it. The rest of the module is about seeing why those two changes matter.'},

        {'kind': 'table', 'title': 'The lessons',
         'headers': ['Lesson', 'What happens'],
         'widths': [3.4, 8],
         'size': 17,
         'rows': [
             ['**6-1 · When Fewest Steps Isn\'t Fastest**',
              'Time a normal block and the slow segment with a stopwatch. Work out, on paper, which '
              'of two routes is really faster.'],
             ['**6-2 · Weights in the Graph**',
              'Start WEIGHTED GRAPH: the slow list, `weight()`, `path_cost()` and a cost check. Run '
              'the check on BFS, and watch it fail.'],
             ['**6-3 · From BFS to Dijkstra**',
              'Start DIJKSTRA PLANNER: copy your BFS, rename it, make the two changes. Print the cost '
              'grid. Run Manhattan, BFS and Dijkstra through the same harness.'],
             ['**6-4 · Drive It**',
              'The robot on the slow-segment grid: a BFS run, then a Dijkstra run, one test and one '
              'changed name.'],
             ['**6-5 · Three Planners, One Harness** (optional extension)',
              'The `Dijkstra` class, and all three planners as objects through the Module 5 class '
              'harness.'],
         ],
         'notes': 'Lesson 6-5 is for students on the class track (the Manhattan and BFS classes '
                  'from Lessons 4-5 and 5-5).'},

        {'kind': 'check',
         'question': 'On a grid where every segment takes the same time, how do BFS and Dijkstra\'s '
                     'algorithm compare?',
         'options': ['Dijkstra finds a shorter path',
                     'They find paths of the same length: Dijkstra only differs when segments have '
                     'different costs',
                     'BFS finds a shorter path',
                     'Dijkstra cannot run on a grid'],
         'answer': 1,
         'explanation': 'With every segment costing 1, fewest steps and least cost are the same thing, '
                        'so the two agree on every test. The slow segment is what separates them.'},

        {'kind': 'wrapup',
         'questions': [
             'What does BFS find, and when is that also the fastest path?',
             'What are the two changes that turn BFS into Dijkstra?',
             'What stays the same from Module 5?',
         ],
         'next': 'time the slow segment, and turn it into a weight',
         'notes': 'Answers: the fewest steps, which is the fastest path only when every block takes '
                  'the same time. Closest first instead of oldest first; add the weight instead of '
                  'counting one step, and keep the cheaper total. The graph, add_blocked(), the previous dictionary, the walk-back, the harness and robot.py itself. Before Lesson 6-1, re-tape the '
                  'slow segment on the grid.'},
    ],
}
