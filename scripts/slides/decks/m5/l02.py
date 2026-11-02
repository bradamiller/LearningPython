DECK = {
    'module': 5, 'lesson': 2,
    'doc': 'module-05-pathfinding/lesson-02-dictionaries',
    'title': 'Dictionaries',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Explain what a dictionary is: a collection of key-value pairs',
             'Create a dictionary, add pairs, and look up a value by key',
             'Check whether a key exists with the `in` keyword',
             'Represent a grid graph as `{node: [neighbors]}`',
             'Open the GRID GRAPH section of `robot.py` with `build_grid_graph()` and '
             '`remove_blocked()`, each with a paper test',
         ],
         'notes': '50 minutes. You drew the grid graph on paper in Lesson 5-1; today it goes into '
                  'Python. The last objective on the lesson page names the full signatures, '
                  'build_grid_graph(rows, cols) and remove_blocked(graph, blocked_nodes); the slide '
                  'shortens them. Show a plain dictionary like {"name": "Alice"} before the '
                  'tuple-keyed graph.'},

        {'kind': 'bullets', 'title': 'What is a dictionary?',
         'bullets': [
             'A **dictionary** stores **key-value pairs** in curly braces',
             'A real dictionary maps words to definitions',
             'A phone book maps names to numbers',
             'A Python dictionary maps any key to any value',
         ],
         'callout': 'Today: store the Lesson 5-1 graph in a dictionary, ready for the search in '
                    'Lesson 5-3',
         'tone': 'teal'},

        {'kind': 'figure', 'title': 'The key and the value',
         'figure': '/img/lesson-m5-02/word-dictionary.svg',
         'caption': 'The word you look up is the **key**; what\'s printed beside it is the '
                    '**value**. Python\'s dictionary works the same way.'},

        {'kind': 'bullets', 'title': 'Why a dictionary is fast: hashing',
         'bullets': [
             'A printed dictionary is in alphabetical order, so you flip straight to the right page',
             'A Python dictionary is organized for speed too, though not alphabetically',
             'Storing: Python turns the key into a number that says where to keep it',
             'Looking up: it does the same arithmetic and goes straight there',
             'That trick is **hashing**: a lookup is just as fast with four thousand entries as with four',
         ],
         'callout': 'So a key must be something that can\'t change, like a number or a tuple',
         'tone': 'orange',
         'notes': 'If the key could change, Python would be looking in the wrong place. Tuples '
                  'can be dictionary keys, lists cannot: keys must be immutable.'},

        {'kind': 'code', 'title': 'Dictionaries in code',
         'lead': 'Snippets like these are for trying out in a scratch file or at the Python '
                 'prompt, not for keeping in `robot.py`:',
         'lead_h': 1.2,
         'code': 'scores = {"Alice": 95, "Bob": 87}\n'
                 'graph = {}                         # empty, ready to fill\n'
                 'graph[(0, 0)] = [(0, 1), (1, 0)]   # node (0,0) -> its neighbor list',
         'code_size': 22,
         'callout': 'For our graph, the **keys are node tuples** and the **values are lists of '
                    'neighbor tuples**',
         'tone': 'teal',
         'notes': 'Why not just a list? Because we look things up by content ("what are the '
                  'neighbors of (1,1)?"), not by position. A dictionary jumps straight to the '
                  'answer.'},

        {'kind': 'figure', 'title': 'The graph as a dictionary',
         'figure': '/img/lesson-m5-02/graph-dict-xy.svg',
         'caption': 'One entry per node: the node is the key, its neighbor list is the value.',
         'notes': 'Have students open their Lesson 5-1 drawings and translate each node into a '
                  'key-value pair: it makes the paper-to-code jump concrete. The snippets in this '
                  'part of the lesson are for trying out in a scratch file or at the Python '
                  'prompt, as with tuples in Lesson 4-2. Only the two functions in the skeleton '
                  'go into robot.py.'},

        {'kind': 'check',
         'question': 'In our graph dictionary, what are the keys and what are the values?',
         'options': ['Keys are numbers; values are strings',
                     'Keys are (x, y) node tuples; values are lists of neighbor tuples',
                     'Keys are lists; values are tuples',
                     'Both are single integers'],
         'answer': 1,
         'explanation': 'Each node is a tuple key, and its value is the list of nodes it connects '
                        'to: the Python version of the paper graph.'},

        {'kind': 'code', 'title': 'Access and the `in` keyword',
         'lead': 'Look up a value with square brackets, and check whether a key exists with `in`:',
         'code': 'graph = {(0, 0): [(0, 1), (1, 0)], (0, 1): [(0, 0), (0, 2), (1, 1)]}\n'
                 '\n'
                 'print(graph[(0, 0)])       # [(0, 1), (1, 0)]\n'
                 'print(len(graph[(0, 0)]))  # 2  -- number of neighbors\n'
                 '\n'
                 'print((0, 0) in graph)     # True\n'
                 'print((2, 2) in graph)     # False -- not added',
         'code_size': 20,
         'callout': '**A blocked node simply isn\'t in the graph**, so `(1, 1) in graph` tells '
                    'you whether that intersection is reachable',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Missing keys, and deleting one',
         'bullets': [
             'Accessing a **missing** key, like `graph[(9, 9)]`, raises a `KeyError`',
             'So check with `in` first',
             '`del graph[(1, 1)]` removes the pair whose key is `(1, 1)`',
             'Afterwards, `(1, 1) in graph` is `False`',
         ],
         'callout': 'You\'ll need `del` for blocking a node later in this lesson',
         'tone': 'orange'},

        {'kind': 'check',
         'question': 'Given `graph = {(0,0): [(0,1)]}`, what does `(0,0) in graph` return?',
         'options': ['True', 'False', '[(0,1)]', 'A KeyError'],
         'answer': 0,
         'explanation': '`in` checks whether a key exists. (0,0) is a key, so it returns True. '
                        '(Accessing a missing key with [] would raise KeyError, which is why we '
                        'use `in`.)'},

        {'kind': 'code', 'title': 'Add to robot.py: GRID GRAPH (1 of 3)',
         'lead': 'A new kind of data gets a new section. Paste it above `RUN`, after the '
                 'NAVIGATOR section. Nothing in it drives.',
         'lead_h': 1.2,
         'code': '# ===== GRID GRAPH =====\n'
                 '# The grid as a graph, in a dictionary: every intersection is\n'
                 '# a key, and its value is the list of neighbors it is joined\n'
                 '# to. The BFS PLANNER searches this graph. Starts with the\n'
                 '# open grid; Lesson 5-4 adds the blocked list, so a blocked\n'
                 '# intersection is neither a key nor anyone\'s neighbor.\n'
                 'ROWS = 4                 # the grid is ROWS x COLS intersections\n'
                 'COLS = 4',
         'code_size': 18,
         'callout': '`ROWS` and `COLS` are the size of your taped grid',
         'tone': 'teal',
         'notes': 'Like the MANHATTAN PLANNER, nothing here drives: two functions that take '
                  'numbers and lists and return a dictionary. The functions take the size as '
                  'parameters rather than reading the settings, so a test can build a 3x3 while '
                  'the settings say 4x4.'},

        {'kind': 'code', 'title': 'Add to robot.py: GRID GRAPH (2 of 3)',
         'code': 'def build_grid_graph(rows, cols):\n'
                 '    """Return the open grid as a dictionary: every (x, y)\n'
                 '    maps to the list of its on-grid neighbors."""\n'
                 '    # 1. graph = {}\n'
                 '    # 2. for every x, for every y:\n'
                 '    #       neighbors = []\n'
                 '    #       left, right, down, up: append each one that is\n'
                 '    #       still on the grid (a bounds check for each)\n'
                 '    #       graph[(x, y)] = neighbors\n'
                 '    # 3. return graph\n'
                 '    pass',
         'code_size': 18,
         'callout': 'The build-in-a-loop pattern from Lesson 4-3, with two loops, one inside the '
                    'other, and a value that is itself a list you build',
         'tone': 'teal',
         'callout_size': 20,
         'notes': 'It goes under the ROWS and COLS settings. The outline is longer than Module 4\'s because this is the first time students '
                  'build a dictionary inside a function: start empty, add one entry per pass. In '
                  'Lesson 5-4 this function is rewritten with the blocked list folded in; the '
                  'tests students write today will tell them whether that rewrite broke '
                  'anything. Every student needs a working copy.'},

        {'kind': 'code', 'title': 'Add to robot.py: GRID GRAPH (3 of 3)',
         'lead': 'Right under `build_grid_graph()`:',
         'code': 'def remove_blocked(graph, blocked_nodes):\n'
                 '    """Take every node in blocked_nodes out of graph: delete\n'
                 '    its key AND drop it from every other node\'s neighbors."""\n'
                 '    # 1. for each blocked node that is in graph: del its key\n'
                 '    # 2. for each node still in graph: replace its neighbor\n'
                 '    #    list with one that leaves the blocked nodes out\n'
                 '    # 3. return graph\n'
                 '    pass',
         'code_size': 19,
         'callout': 'Two numbered steps: delete the key, then clean every neighbor list',
         'tone': 'orange',
         'notes': 'remove_blocked() is deleted in Lesson 5-4, the way SETPOINT went in Lesson '
                  '2-6, when the blocked list is folded into the graph builder.'},

        {'kind': 'bullets', 'title': 'Activity · Build the graph automatically', 'tag': 'Activity',
         'bullets': [
             'Typing all 9 nodes of a 3×3 grid by hand is tedious; a 10×10 grid has 100',
             'So `build_grid_graph()` generates the graph for any size',
             'For each node, check left, right, down and up, and add only the ones that are on the grid',
             'That means a **bounds check** before each `append`:',
             ['left only if you\'re not on the left edge: `x > 0`',
              'right only if you\'re not on the right edge: `x < cols - 1`',
              'the same two checks for `y`, against the bottom and top rows'],
         ],
         'callout': 'The four checks are what give corners 2 neighbors and interior nodes 4',
         'tone': 'teal'},

        {'kind': 'figure', 'title': 'Four bounds checks', 'tag': 'Activity',
         'figure': '/img/lesson-m5-02/bounds-checks-xy.svg',
         'caption': 'A failed check is a neighbor that would be off the grid, so it is never '
                    'appended.'},

        {'kind': 'steps', 'title': 'Step 1 · Test `build_grid_graph()`',
         'steps': [
             'Write the body of `build_grid_graph()` from its outline',
             'Write a test, say `test_grid_graph()`, that builds the 4×4 graph and prints '
             '`len(graph)`, the neighbors of `(1, 1)` and the neighbors of `(0, 0)`',
             'Before you run it, write down what each should be from your Lesson 5-1 drawing',
             'Set the run line to it. The robot stays on the desk',
         ],
         'notes': 'The expected output is behind a reveal on the lesson page; let students '
                  'predict and run first. The order inside a neighbor list depends on the order '
                  'the four directions are checked; left, right, down, up is the order the search '
                  'in Lesson 5-5 will use.'},

        {'kind': 'check',
         'question': 'In `build_grid_graph`, why is each neighbor guarded by an if (like `if x > 0`)?',
         'options': ['To make the code shorter',
                     'To keep neighbors inside the grid: a corner or edge node has no neighbor '
                     'off the grid',
                     'To skip blocked nodes',
                     'It has no effect'],
         'answer': 1,
         'explanation': 'The bounds checks prevent adding neighbors that fall off the edge of the '
                        'grid, so corners get 2 neighbors and interior nodes get 4.'},

        {'kind': 'bullets', 'title': 'Activity · Removing blocked nodes', 'tag': 'Activity',
         'bullets': [
             'Blocking a node is a **two-step** job:',
             ['delete its key', '**and** remove it from every other node\'s neighbor list'],
             'Forget step 2 and other nodes still think they can reach a blocked intersection',
             'Step 2, one way: start a new empty list, loop over the old neighbors, append each '
             'one that is `not in blocked_nodes`',
             'Then assign the new list back to `graph[node]`',
         ],
         'callout': 'Those are the outline\'s two numbered steps',
         'tone': 'orange',
         'notes': 'Spend extra time here: forgetting to clean the neighbor lists is the number '
                  'one bug in later lessons. A plain loop-and-append is the version to expect '
                  'from most students, and it is fine.'},

        {'kind': 'steps', 'title': 'Step 2 · Test `remove_blocked()`',
         'steps': [
             'Write the body of `remove_blocked()` from its outline',
             'Write a test, `test_remove_blocked()`, that builds a **3×3** graph and removes '
             '`(1, 1)`',
             'Print how many intersections are left, `(1, 1) in graph`, and the neighbors of '
             '`(0, 1)`. Predict all three first',
             'Don\'t go on until both tests print what you predicted',
         ],
         'notes': 'The finished bodies and the expected output are behind a reveal on the lesson '
                  'page, and the full section is in the teacher solution file '
                  'lesson-02-dictionaries.py in the Module 5 solutions. The reveal uses a list '
                  'comprehension, which is new; students who wrote the loop keep the loop.'},

        {'kind': 'check',
         'question': 'To block node (1,1), what two things must happen to the graph dictionary?',
         'options': ['Just delete the key (1,1)',
                     'Delete the key (1,1) AND remove (1,1) from every other node\'s neighbor list',
                     'Set graph[(1,1)] to an empty list',
                     'Nothing: blocked nodes are ignored automatically'],
         'answer': 1,
         'explanation': 'Deleting only the key leaves dangling references: neighbors still list '
                        '(1,1). You must also clean it out of every neighbor list.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Web', 'User profiles', 'A username maps to a profile object: look up any user '
                                      'instantly by their key.'),
             ('Games', 'Inventories', 'Item name maps to quantity; the game jumps straight to '
                                      '"how many potions?" without searching.'),
             ('Data', 'Caches & indexes', 'Databases and caches use key lookups so huge datasets '
                                          'stay fast to search.'),
         ]},

        {'kind': 'wrapup',
         'questions': [
             'How is a dictionary different from a list?',
             'Why are tuples the keys and lists the values in our graph?',
             'What are the two steps to block a node?',
         ],
         'next': 'breadth-first search, on paper',
         'notes': 'Answers: looked up by key, not by position. A node is a fixed pair; its '
                  'neighbors are a changing collection. Delete its key; remove it from all '
                  'neighbor lists.'},
    ],
}
