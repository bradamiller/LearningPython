"""Module 5, Lesson 5-3 · From Pencil to Program.

Same order as the lesson page. Both discussions ("Where does the program keep the
numbers?" and "Where does the program keep the neighbors?") run one question per slide,
then its answer; the slide notes hold that step of the lesson's teacher note. Each
activity step is a slide to predict on, then a slide to check against. Grids:
fig/make_discuss_grids.py.
"""
FIG = './decks/m5/fig/'


def ask(n, total, question, figure=None, notes=None):
    s = {'kind': 'bullets', 'title': f'Question {n} of {total}', 'tag': 'Discuss',
         'bullets': question, 'size': 28}
    if figure:
        s.update(figure=figure, split=0.55)
    if notes:
        s['notes'] = notes
    return s


def answer(n, total, points, rule=None, figure=None, notes=None):
    s = {'kind': 'bullets', 'title': f'Answer {n} of {total}', 'tag': 'Discuss',
         'bullets': points, 'size': 28}
    if figure:
        s.update(figure=figure, split=0.55)
    if rule:
        s.update(callout=rule, tone='green')
    if notes:
        s['notes'] = notes
    return s


def step(title, code, predict, notes=None, lead=None, size=20):
    s = {'kind': 'code', 'title': title, 'tag': 'Activity', 'code': code, 'code_size': size,
         'callout': '**Predict:** ' + predict, 'tone': 'orange'}
    if lead:
        s.update(lead=lead, lead_h=1.0)
    if notes:
        s['notes'] = notes
    return s


def check(title, output, says, notes=None, size=20):
    s = {'kind': 'code', 'title': title, 'tag': 'Activity', 'code': output, 'code_size': size,
         'callout': says, 'tone': 'green'}
    if notes:
        s['notes'] = notes
    return s


GRAPH_3X3 = '/img/lesson-m5-01/graph-3x3-xy.svg'
BLOCKED_3X3 = '/img/lesson-m5-01/graph-blocked-xy.svg'

DECK = {
    'module': 5, 'lesson': 3,
    'doc': 'module-05-pathfinding/lesson-03-pencil-to-program',
    'title': 'From Pencil to Program',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Explain why the program keeps the numbers in a **dictionary**, not a list',
             'Create a dictionary, store and look up a value by key, and check for a key with '
             '`in`',
             'Explain why the program works out every intersection\'s neighbors **once**, before '
             'the search',
             'Describe the grid as a graph: nodes, edges and neighbors',
             'Build `build_grid_graph(rows, cols)` one printed step at a time',
         ],
         'notes': '65 to 75 minutes, robot on the desk. Two discussions, each ending in a '
                  'dictionary: first for the numbers, then for the neighbors. Nothing arrives '
                  'unasked for. The second dictionary is quick because they already know the '
                  'tool.'},

        {'kind': 'bullets', 'title': 'From paper to program',
         'bullets': [
             'Lesson 5-2 ended with the algorithm in plain words',
             'The program has to keep what you kept on paper:',
             ['the **number** on every intersection',
              'which intersections are **next to each other**'],
         ],
         'size': 28},

        # --- Discuss · Where does the program keep the numbers? ---
        {'kind': 'bullets', 'title': 'Where do the numbers go?', 'tag': 'Discuss',
         'bullets': [
             'You wrote a number on every intersection: its steps to D',
             'The program has to keep those numbers too',
         ],
         'split': 0.55, 'size': 26,
         'figure': FIG + 'dc-full.svg',
         'notes': 'Leading the discussion, 10 minutes. Put Lesson 5-2\'s open 4×4 grid, numbered '
                  'from D, back on the board. The dictionary should arrive as the answer to a '
                  'problem they can see, not as a new topic.'},

        ask(1, 2, ['The program is visiting (2,3) and needs its number',
                   'Where could it keep the numbers so it can find the one for (2,3)?'],
            FIG + 'dc-full.svg',
            notes='Someone will suggest a list. Ask: "Which position in the list is (2,3)\'s '
                  'number?" There isn\'t a good answer; that\'s the problem.'),
        answer(1, 2, ['**In something it can look up by intersection**',
                      'Give it (2,3), get back 1',
                      'A list finds things by **position**, like `path[0]`, so it would search '
                      'the whole list every time']),

        ask(2, 2, ['Where in real life do you look something up by **name**, and read what\'s '
                   'written beside it?'],
            notes='A phone\'s contacts work too: a name gets you a number.'),
        answer(2, 2, ['**A dictionary**: look up a word, read its definition',
                      'Python has one too, also called a **dictionary**',
                      'Look up a **key**, get its **value**'],
               figure='/img/lesson-m5-02/word-dictionary.svg'),

        {'kind': 'code', 'title': 'Python\'s dictionary',
         'lead': 'For the numbers, the key is an intersection and the value is its steps to D:',
         'lead_h': 0.9,
         'code': 'distance = {}              # an empty dictionary\n'
                 'distance[(3, 3)] = 0       # store: key (3, 3), value 0\n'
                 'print(distance[(3, 3)])    # look up: 0',
         'code_size': 22,
         'callout': 'A key can\'t change, like a number or a tuple, so an `(x, y)` tuple works',
         'tone': 'teal'},

        {'kind': 'figure', 'title': 'The numbers in a dictionary',
         'figure': FIG + 'd53-distance.svg',
         'caption': 'The numbers on the grid, in a dictionary called distance.'},

        # --- Activity · The numbers in a dictionary ---
        {'kind': 'code', 'title': 'Try it: try_distance()', 'tag': 'Activity',
         'lead': 'Above `RUN` in `robot.py`. Set the run line to `try_distance()`. The robot '
                 'stays on the desk.',
         'lead_h': 1.0,
         'code': 'def try_distance():\n'
                 '    distance = {}\n'
                 '    distance[(3, 3)] = 0\n'
                 '    distance[(2, 3)] = 1\n'
                 '    distance[(3, 2)] = 1',
         'code_size': 22,
         'notes': 'Practice only: students delete it at the end of the lesson. Lesson 5-5 writes '
                  'the real distance dictionary.'},

        step('Step 1 · Store and look up',
             '    print(distance[(2, 3)])\n'
             '    print(len(distance))\n'
             '    print(distance)',
             'the three lines it prints',
             lead='Add to the end of `try_distance()`:', size=22),
        check('Step 1 · Check your output',
              '1\n3\n{(3, 3): 0, (2, 3): 1, (3, 2): 1}',
              '`len()` counts the keys, as it counts the items in a list', size=22),

        step('Step 2 · One more than a neighbor',
             '    distance[(2, 2)] = distance[(2, 3)] + 1\n'
             '    print(distance[(2, 2)])',
             'what it prints',
             lead='Visiting (2,3) gives its neighbor (2,2) one more than (2,3)\'s number. Add:',
             size=22),
        check('Step 2 · Check your output', '2',
              'That one line is how BFS writes a number. You\'ll use it in Lesson 5-5', size=24),

        step('Step 3 · Does it have a number yet?',
             '    print((2, 2) in distance)\n'
             '    print((0, 0) in distance)\n'
             '    print(distance[(0, 0)])',
             'each line',
             lead='`in` asks whether a key is there. Add:', size=22,
             notes='The KeyError is meant to happen.'),
        check('Step 3 · Check your output',
              'True\nFalse\nKeyError: (0, 0)',
              '(0,0) has no number yet. Check with `in` before you look up a key that might be '
              'missing',
              notes='Delete the third line once they\'ve seen the error. "Does this neighbor have '
                    'a number yet?" is one in. When done, delete try_distance(); Lesson 5-5 writes '
                    'the real distance, and the to-visit list beside it, a plain list called '
                    'to_visit.', size=22),

        {'kind': 'check',
         'question': 'Given `distance = {(2,2): 0, (1,2): 1}`, what does `(1,2) in distance` return, '
                     'and what does it mean?',
         'options': ['True: (1,2) already has a number',
                     'False: (1,2) is blocked',
                     '1: its number',
                     'A KeyError'],
         'answer': 0,
         'explanation': 'in checks whether a key exists. (1,2) is a key, so it returns True: it '
                        'already has a number, and must not get another.'},

        # --- Discuss · Where does the program keep the neighbors? ---
        {'kind': 'bullets', 'title': 'Where do the neighbors go?', 'tag': 'Discuss',
         'bullets': [
             'To visit an intersection, the program needs its **open neighbors**',
             'On paper you just looked',
             'A 3×3 grid with the middle, (1,1), blocked',
         ],
         'split': 0.55, 'size': 26,
         'figure': BLOCKED_3X3,
         'notes': 'Leading the discussion, 10 minutes. The goal is the second dictionary, and the '
                  'reason to build it before the search. Make the case with blocked '
                  'intersections, not speed: on a 4×4 grid nobody can feel the time.'},

        ask(1, 3, ['The program is visiting (0,1)',
                   'How could it work out (0,1)\'s open neighbors?'], BLOCKED_3X3,
            notes='Let them say the two checks out loud: on the grid, and not blocked. Both have '
                  'to be right every time the search visits anything.'),
        answer(1, 3, ['**Try all four directions**: left, right, down, up',
                      'Keep each one on the grid and **not blocked**',
                      'Left is off the grid, (1,1) is blocked: (0,0) and (0,2)'],
               figure=BLOCKED_3X3),

        ask(2, 3, ['The search visits every intersection, and does those checks every time',
                   'Could the program do them **once** instead, before the search starts?']),
        answer(2, 3, ['**Yes: work out every intersection\'s open neighbors once**',
                      'Leave out anything off the grid **and anything blocked**',
                      'The search just reads the list'],
               rule='**The search never checks for a blocked intersection again.**',
               notes='The win is one place for the blocked check instead of one inside the '
                     'search. A search that forgets it steps into the wall; a list that never had '
                     'the wall in it can\'t. Lesson 5-4 builds the blocked intersections into the '
                     'list.'),

        ask(3, 3, ['How should the program save each intersection\'s neighbors, so the search '
                   'can look up (0,1)\'s later?'],
            notes='This time they should get there fast: same tool, and the value is a list '
                  'instead of a number.'),
        answer(3, 3, ['**Another dictionary**',
                      'The key is the intersection',
                      'The value is its list of open neighbors'],
               rule='`graph[(0, 1)] = [(0, 0), (0, 2)]`'),

        # --- The grid as a graph ---
        {'kind': 'bullets', 'title': 'The grid as a graph',
         'bullets': [
             'Every point and the points it\'s joined to: a **graph**',
             'Every intersection is a **node**, named like `(1, 2)`',
             'Every line between neighbors is an **edge**',
             'A node\'s **neighbors** are the nodes its edges lead to',
         ],
         'split': 0.55, 'size': 24,
         'figure': GRAPH_3X3,
         'notes': 'A road map is a graph (intersections and streets), so is a social network '
                  '(people and friendships). In computer science, "graph" never means a bar '
                  'chart. A corner has 2 neighbors, an edge node 3, an interior node 4.'},

        {'kind': 'check',
         'question': 'On a 3×3 grid, how many neighbors does the interior node (1,1) have?',
         'options': ['2', '3', '4', '8'],
         'answer': 2,
         'explanation': '(1,1) connects left, right, down and up. No diagonals, so four.'},

        {'kind': 'bullets', 'title': 'Blocking removes a node',
         'bullets': [
             'A blocked intersection is **removed**: the node and all its edges',
             '(0,1), (1,0), (1,2) and (2,1) each lose a neighbor',
             'An edge left into (1,1) lets the search step into the wall',
         ],
         'split': 0.55, 'size': 24,
         'figure': BLOCKED_3X3,
         'callout': 'Today: the open grid. Lesson 5-4 takes the blocked ones out.',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'After (1,1) is blocked, how many neighbors does (0,1) have?',
         'options': ['3: nothing changed', '2: it lost (1,1)', '4', '0'],
         'answer': 1,
         'explanation': '(0,1) used to connect to (0,0), (0,2) and (1,1). With (1,1) removed, two '
                        'remain.'},

        # --- Skeleton and the graph activity ---
        {'kind': 'code', 'title': 'Add to robot.py: GRID GRAPH',
         'lead': 'Above `RUN`, after the NAVIGATOR section. Nothing in it drives.',
         'lead_h': 0.7,
         'code': '# ===== GRID GRAPH =====\n'
                 '# The grid as a graph, in a dictionary: every intersection is\n'
                 '# a key, and its value is the list of neighbors it is joined\n'
                 '# to. The BFS PLANNER searches this graph. Starts with the\n'
                 '# open grid; Lesson 5-4 adds the blocked list, so a blocked\n'
                 '# intersection is neither a key nor anyone\'s neighbor.\n'
                 'ROWS = 4                 # the grid is ROWS x COLS intersections\n'
                 'COLS = 4\n'
                 '\n'
                 'def build_grid_graph(rows, cols):\n'
                 '    """Return the open grid as a dictionary: every (x, y)\n'
                 '    maps to the list of its on-grid neighbors."""\n'
                 '    pass',
         'code_size': 15,
         'notes': 'ROWS and COLS are the size of the taped grid. The function takes the size as '
                  'parameters, so students can build a small 3×3 while the settings say 4×4. '
                  'While they work, the run line is build_grid_graph(3, 3).'},

        step('Step 1 · Visit every intersection',
             'for x in range(cols):\n'
             '    for y in range(rows):\n'
             '        print((x, y))',
             'how many lines, and which changes fastest, x or y?',
             lead='Replace `pass`. Run line: `build_grid_graph(3, 3)`', size=22),
        check('Step 1 · Check your output',
              '(0, 0)\n(0, 1)\n(0, 2)\n(1, 0)\n(1, 1)\n(1, 2)\n(2, 0)\n(2, 1)\n(2, 2)',
              'Nine lines. `y` changes fastest: up the first column, then the next', size=16),

        {'kind': 'bullets', 'title': 'Step 2 · List every neighbor', 'tag': 'Activity',
         'bullets': [
             'Inside the inner loop, make an empty list `neighbors`',
             'Append the four next to `(x, y)`: **left, right, down, up**',
             'Print the intersection, then its list',
         ],
         'size': 26,
         'callout': '**Predict:** what will `(0, 0)` print?',
         'tone': 'orange',
         'notes': 'Left, right, down, up is the order the paper traces used, so the program\'s '
                  'paths will match the paper ones.'},
        check('Step 2 · Check your output',
              '(0, 0) [(-1, 0), (1, 0), (0, -1), (0, 1)]\n'
              '(0, 1) [(-1, 1), (1, 1), (0, 0), (0, 2)]\n'
              '(0, 2) [(-1, 2), (1, 2), (0, 1), (0, 3)]\n'
              '(1, 0) [(0, 0), (2, 0), (1, -1), (1, 1)]\n'
              '(1, 1) [(0, 1), (2, 1), (1, 0), (1, 2)]\n'
              '...',
              'A corner has only 2 neighbors. **Circle** every one that isn\'t really there',
              notes='Wrong on purpose. The moment they circle (-1, 0) is the moment they need the '
                    'bounds checks.', size=18),

        {'kind': 'bullets', 'title': 'Step 3 · Drop the off-grid ones', 'tag': 'Activity',
         'bullets': [
             'Off the grid: a number below 0, or past the last row or column',
             'Put an `if` in front of each `append`',
             'Each direction gets its own test; each test compares **one number**',
         ],
         'size': 26,
         'callout': '**Predict:** how many neighbors for a corner, an edge, the middle?',
         'tone': 'orange',
         'notes': 'Let them write the four tests before anyone sees the answer.'},
        check('Step 3 · Check your output',
              '(0, 0) [(1, 0), (0, 1)]\n'
              '(0, 1) [(1, 1), (0, 0), (0, 2)]\n'
              '(0, 2) [(1, 2), (0, 1)]\n'
              '(1, 0) [(0, 0), (2, 0), (1, 1)]\n'
              '(1, 1) [(0, 1), (2, 1), (1, 0), (1, 2)]\n'
              '...',
              'Corners 2, edges 3, the middle 4. These tests are **bounds checks**', size=18),
        {'kind': 'figure', 'title': 'Step 3 · Bounds checks', 'tag': 'Activity',
         'figure': '/img/lesson-m5-02/bounds-checks-xy.svg',
         'caption': 'A failed check is a neighbor that would be off the grid, so it is never '
                    'appended.'},

        {'kind': 'bullets', 'title': 'Step 4 · Keep them in a dictionary', 'tag': 'Activity',
         'bullets': [
             'Make `graph = {}` before the loops',
             'Replace the print inside the loop: store `neighbors` under the key `(x, y)`',
             'After the loops: print `len(graph)`, then the neighbors of `(1, 1)`, then of '
             '`(0, 0)`',
         ],
         'size': 24,
         'callout': '**Predict:** the three lines it prints',
         'tone': 'orange'},
        check('Step 4 · Check your output',
              '9\n[(0, 1), (2, 1), (1, 0), (1, 2)]\n[(1, 0), (0, 1)]',
              'Got 1 instead of 9? `graph = {}` is inside a loop, so it starts over each pass',
              size=22),
        {'kind': 'figure', 'title': 'What you just built',
         'figure': '/img/lesson-m5-02/graph-dict-xy.svg',
         'caption': 'One entry per node: the node is the key, its neighbor list is the value.'},

        {'kind': 'check',
         'question': 'In our graph dictionary, what are the keys and what are the values?',
         'options': ['Keys are numbers; values are strings',
                     'Keys are (x, y) node tuples; values are lists of neighbor tuples',
                     'Keys are lists; values are tuples',
                     'Both are single integers'],
         'answer': 1,
         'explanation': 'Each node is a tuple key, and its value is the list of nodes it connects '
                        'to.'},

        {'kind': 'code', 'title': 'Step 5 · Return it and test it', 'tag': 'Activity',
         'lead': 'Delete the three prints, end with `return graph`, and write the test. Run line: '
                 '`test_grid_graph()`',
         'lead_h': 1.0,
         'code': 'def test_grid_graph():\n'
                 '    graph = build_grid_graph(ROWS, COLS)\n'
                 '    print("Intersections:", len(graph))\n'
                 '    print("Neighbors of (1, 1):", graph[(1, 1)])\n'
                 '    print("Neighbors of (0, 0):", graph[(0, 0)])\n'
                 '    for node in graph:\n'
                 '        print(node, graph[node])',
         'code_size': 20,
         'callout': '**Predict:** which of the first three lines change on a 4×4? How many have '
                    'exactly 2 neighbors?',
         'tone': 'orange',
         'notes': 'A for loop over a dictionary hands you each key in turn, and the key looks up '
                  'its value.'},
        check('Step 5 · Check your output',
              'Intersections: 16\n'
              'Neighbors of (1, 1): [(0, 1), (2, 1), (1, 0), (1, 2)]\n'
              'Neighbors of (0, 0): [(1, 0), (0, 1)]\n'
              '(0, 0) [(1, 0), (0, 1)]\n'
              '(0, 1) [(1, 1), (0, 0), (0, 2)]\n'
              '...\n'
              '(3, 3) [(2, 3), (3, 2)]',
              'Only the count changes. Four corners with 2, eight edges with 3, four in the '
              'middle with 4',
              notes='The finished build_grid_graph() is behind the Step 5 reveal on the lesson '
                    'page. Every student needs a working copy: Lesson 5-4 rewrites it as '
                    'build_graph() with the blocked check folded in.', size=18),

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Navigation', 'Road maps',
              'Streets as a graph: intersections are nodes, roads are edges, and a closed road '
              'is an edge taken out.'),
             ('Web', 'User profiles', 'A username maps to a profile, found instantly by key.'),
             ('Games', 'Inventories', 'Item name maps to quantity: "how many potions?" with no '
              'searching.'),
         ]},

        {'kind': 'wrapup',
         'questions': [
             'Why does the program keep the numbers in a dictionary, not a list?',
             'What does `(2, 2) in distance` ask?',
             'Why work out every intersection\'s neighbors before the search?',
             'What does blocking a node remove?',
         ],
         'next': 'the blocked list, and the BFS PLANNER opens',
         'notes': 'Answers: it looks them up by intersection, not by position. Does (2,2) have a '
                  'number yet? Blocked intersections are left out once, so the search never has '
                  'to check for them. The node and all its edges. Exit ticket: write a dictionary '
                  'with two entries: (3, 3) is 0 steps from the destination, and (3, 2) is 1 '
                  'step.'},
    ],
}
