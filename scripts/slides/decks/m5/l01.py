DECK = {
    'module': 5, 'lesson': 1,
    'doc': 'module-05-pathfinding/lesson-01-grid-as-a-graph',
    'title': 'The Grid as a Graph',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Define **node**, **edge** and **neighbor**',
             'Explain why a grid of intersections is a graph',
             'Remove a blocked node (and its edges) from a graph',
             'Find a shortest path by hand that detours around obstacles',
             'Explain why the Manhattan algorithm can\'t handle blocked intersections',
         ],
         'notes': '45 to 50 minutes, no coding: a mental model first, on paper and the physical '
                  'grid. This lesson is the why for the whole module, so spend real time on the '
                  'hook. Save the worksheets: they become test cases in Lessons 5-3 to 5-5.'},

        {'kind': 'bullets', 'title': 'What if the road is closed?',
         'bullets': [
             'Your usual route to school is closed for construction',
             'You don\'t give up: you find a detour, and your GPS reroutes you automatically',
             'The robot needs to do the same',
             'Manhattan only knows one strategy: **across first, then up or down**',
             'It has no idea of an obstacle, so it drives right into a blocked intersection',
         ],
         'callout': 'To route **around** things, we need a smarter way to think about the grid',
         'tone': 'teal',
         'notes': 'Show a blocked intersection sitting on Manhattan\'s route and let students '
                  'feel that the old algorithm is stuck before you offer anything new.'},

        {'kind': 'bullets', 'title': 'The same puzzle your phone solves',
         'lead': 'A city\'s streets form a graph. A closed road is blocked, heavy traffic makes '
                 'some streets slower.',
         'lead_h': 1.25,
         'bullets': [
             '**This module, breadth-first search**: a route around blocked intersections',
             '**Module 6, Dijkstra\'s algorithm**: the **fastest** route when some streets are slow',
             'Real apps use faster descendants of Dijkstra (A* is the best known), but the core '
             'idea is the one you\'ll write',
         ],
         'split': 0.5,
         'figure': '/img/lesson-m5-01/phone-route.svg',
         'crop': (0.22, 0.0, 0.94, 1.0),
         'notes': 'The figure: a maps app going around a closed road (this module\'s problem) and '
                  'avoiding a slow street (the next module\'s).'},

        {'kind': 'check',
         'question': 'Why can\'t the Manhattan algorithm route around a blocked intersection?',
         'options': ['It runs too slowly',
                     'It only knows one fixed strategy (across, then up or down) and has no '
                     'concept of obstacles',
                     'It can, if you turn it off and on again',
                     'The robot has no wheels'],
         'answer': 1,
         'explanation': 'Manhattan always follows the same L-shaped route. It never checks whether '
                        'an intersection is blocked, so it can\'t detour.'},

        {'kind': 'bullets', 'title': 'Nodes, edges, neighbors',
         'bullets': [
             'A **graph** is a collection of **nodes** (points) connected by **edges** (links)',
             'You already know graphs:',
             ['a road map: intersections and streets',
              'a social network: people and friendships',
              'airline routes: airports and flights'],
             'A graph captures **what connects to what**',
         ],
         'callout': 'In computer science a graph is a network of nodes and edges, not a bar chart',
         'tone': 'orange',
         'notes': 'Clear up the word "graph" immediately: in CS it is a network of nodes and '
                  'edges, not a bar chart.'},

        {'kind': 'bullets', 'title': 'Our grid is a graph',
         'bullets': [
             'Every intersection is a **node**, named by its coordinate, like `(1, 2)`',
             'Every line between two adjacent intersections is an **edge**',
             'The nodes an edge connects you to are that node\'s **neighbors**',
             'How many depends on where it sits:',
             ['a **corner** has 2', 'an **edge** node has 3', 'an **interior** node has 4'],
         ],
         'split': 0.52,
         'figure': '/img/lesson-m5-01/graph-3x3-xy.svg',
         'notes': '(0, 0) is the bottom-left, as in Module 4. Draw a big 3x3 graph on the board '
                  'and have students count the neighbors of a corner, an edge node and the center. '
                  'No diagonals.'},

        {'kind': 'check',
         'question': 'On a 3×3 grid, how many neighbors does the interior node (1,1) have?',
         'options': ['2', '3', '4', '8'],
         'answer': 2,
         'explanation': '(1,1) connects left, right, down, and up: (0,1), (2,1), (1,0), (1,2). '
                        'No diagonals, so four neighbors.'},

        {'kind': 'bullets', 'title': 'Blocking a node',
         'bullets': [
             'When an intersection is blocked, we **remove it from the graph entirely**',
             'The node **and** all its edges',
             'Block (1,1): every node that used to touch it, (0,1), (1,0), (1,2) and (2,1), '
             'has lost a neighbor',
         ],
         'split': 0.52,
         'figure': '/img/lesson-m5-01/graph-blocked-xy.svg',
         'callout': 'Blocking one node changes its neighbors too',
         'tone': 'teal',
         'notes': 'Have students come up to the board, cross out a blocked node and erase its '
                  'edges with their own hands.'},

        {'kind': 'check',
         'question': 'After (1,1) is blocked, how many neighbors does (0,1) have?',
         'options': ['3: nothing changed',
                     '2: it lost its connection to the right, to (1,1)',
                     '4', '0'],
         'answer': 1,
         'explanation': '(0,1) used to connect to (0,0), (0,2), and (1,1). With (1,1) removed, '
                        'only two neighbors remain.'},

        {'kind': 'figure', 'title': 'Activity · Finding a path around', 'tag': 'Activity',
         'figure': '/img/lesson-m5-01/detour-xy.svg',
         'caption': 'Block **(1,0)** instead. Find the shortest path from (0,0) to (2,0): trace a '
                    'way around with your finger and count the steps.',
         'notes': 'Manhattan would try (0,0) to (1,0) to (2,0), but (1,0) is blocked, so it '
                  'fails. Let students struggle to find the path by hand; that struggle is what '
                  'motivates a systematic method in Lesson 5-3. The answer is behind a reveal on '
                  'the lesson page: take answers from the room before opening it.'},

        {'kind': 'bullets', 'title': 'Obstacles make paths longer',
         'bullets': [
             'Without the obstacle, the Manhattan distance from (0,0) to (2,0) is only 2',
             'With obstacles, Manhattan distance is just a **lower bound**, not the real answer',
             'There\'s usually more than one shortest path',
             'Our grid is **unweighted**: every edge costs 1 step',
             'In a **weighted** graph, a highway edge might cost less than a side street',
         ],
         'callout': 'This module: the unweighted case. The optional Module 6: edges with different costs',
         'tone': 'teal',
         'notes': 'Ask for the length of the detour students found before this slide. If two '
                  'students found different routes of the same length, both are right.'},

        {'kind': 'check',
         'question': 'With (1,0) blocked, the shortest path from (0,0) to (2,0) is 4 steps, but '
                     'the Manhattan distance is 2. What does that tell you?',
         'options': ['The Manhattan distance is wrong',
                     'With obstacles, the real shortest path can be longer than the Manhattan distance',
                     'Obstacles always add exactly 2 steps',
                     'The destination is unreachable'],
         'answer': 1,
         'explanation': 'Manhattan distance is the shortest path with NO obstacles. Blocked nodes '
                        'can force a longer detour, so it becomes a lower bound.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Navigation', 'GPS & Waze', 'Roads are edges, intersections are nodes. Rerouting '
                                          'around a closure is exactly this graph problem.'),
             ('Social', 'Friend networks', 'People are nodes, friendships are edges. "Friends of '
                                           'friends" is a graph search.'),
             ('Internet', 'Network routing', 'Data hops between routers (nodes) over links '
                                             '(edges), picking a shortest path each time.'),
         ]},

        {'kind': 'wrapup',
         'questions': [
             'What are a node, an edge, and a neighbor?',
             'What happens to the graph when a node is blocked?',
             'Why can obstacles make a path longer than the Manhattan distance?',
         ],
         'next': 'store the graph in Python with a dictionary',
         'notes': 'Answers: a point, a link between adjacent points, and the points a node links '
                  'to. It is removed entirely, node and all its edges. You have to detour around '
                  'blocked nodes. Formative: identify nodes, edges and neighbors, remove a blocked '
                  'node cleanly, trace a detour, explain why Manhattan fails. Exit ticket: "On a '
                  '3x3 grid with (1,0) blocked, draw the shortest path from (0,0) to (2,0) and '
                  'count the steps." (4). Preview: next lesson stores the graph as a dictionary, '
                  '{(0,0): [(0,1),(1,0)], ...}.'},

        {'kind': 'check', 'tag': 'Wrap-up quiz',
         'question': 'In computer science, what does the word \'graph\' mean?',
         'options': ['A bar chart or scatter plot', 'A network of nodes connected by edges',
                     'A grid of pixels', 'A line showing data over time'],
         'answer': 1,
         'explanation': 'Same word, different field. In CS a graph is nodes and edges: the '
                        'structure behind maps, networks, and our grid.'},
    ],
}
