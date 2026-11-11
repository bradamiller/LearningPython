DECK = {
    'module': 6, 'lesson': 5,
    'doc': 'module-06-dijkstra/lesson-05-three-planners-one-harness',
    'title': 'Three Planners, One Harness',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Write the `Dijkstra` class by copying `BFS` and making the same two changes as Lesson 6-3',
             'Give it `add_slow_edge()`, `clear_slow_edges()` and `weight()` as methods, with the slow '
             'list inside the object',
             'Run `Manhattan()`, `BFS()` and `Dijkstra()` through one harness and read the results',
             'Explain why the harness can treat three different classes the same way',
         ],
         'notes': '45 minutes. Optional extension, class track only: for students who built the '
                  'Manhattan and BFS classes in Lessons 4-4 and 5-5. Everything is Lesson 6-3 with '
                  'self. in front; students who did 6-3 carefully finish this in half an hour.'},

        {'kind': 'bullets', 'title': 'The third class',
         'bullets': [
             'You built the `Manhattan` and `BFS` classes in Lessons 4-4 and 5-5',
             'Today: the third one, `Dijkstra`, and all three as objects through the Module 5 class harness',
             'The harness **never finds out** which one it is holding',
             'That property has a name: **polymorphism**',
         ],
         'callout': 'Did 6-3 as a function? This replaces that function with the class. Skipped ahead '
                    'from 6-3? This is where you write it.',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Where the skeleton goes',
         'bullets': [
             'Paste it **in place of** the DIJKSTRA PLANNER banner and `compute_dijkstra_path()`',
             '`closest()` sits under the new banner',
             '`dijkstra_distances()`, `compare()`, the Lesson 6-4 part and your tests stay where they are',
             'Move your Lesson 6-3 body into `compute_path()`',
         ],
         'callout': 'WEIGHTED GRAPH stays too. From today it is the **harness\'s** record of the slow '
                    'edges, the way `HARNESS_BLOCKED` is its record of the blocks.',
         'tone': 'orange'},

        {'kind': 'code', 'title': 'Skeleton (1 of 3): the banner and `__init__`',
         'code': '# ===== DIJKSTRA PLANNER (class version) =====\n'
                 '# One Dijkstra object holds the grid size, ITS OWN blocked\n'
                 '# list and ITS OWN slow list, and plans by cost around both:\n'
                 '# the BFS class with the slow-list methods added and the two\n'
                 '# Lesson 6-3 changes inside compute_path(). Same names as the\n'
                 '# function version, with planner. in front; the 5-6 class\n'
                 '# harness tests all three planners without naming one.\n'
                 'class Dijkstra:\n'
                 '    def __init__(self, rows=4, cols=4):\n'
                 '        self.rows = rows\n'
                 '        self.cols = cols\n'
                 '        self.blocked = []\n'
                 '        self.slow_edges = []       # NEW: lives inside the planner',
         'code_size': 18},

        {'kind': 'code', 'title': 'Skeleton (2 of 3): blocked and slow methods',
         'code': '    def add_blocked(self, intersection):\n'
                 '        # as in BFS\n'
                 '        pass\n'
                 '\n'
                 '    def clear_blocked(self):\n'
                 '        pass\n'
                 '\n'
                 '    def add_slow_edge(self, a, b, cost):\n'
                 '        # your function, with self.slow_edges for SLOW_EDGES\n'
                 '        pass\n'
                 '\n'
                 '    def clear_slow_edges(self):\n'
                 '        pass',
         'code_size': 18},

        {'kind': 'code', 'title': 'Skeleton (3 of 3): the last two methods',
         'code': '    def weight(self, a, b):\n'
                 '        # your function, reading self.slow_edges\n'
                 '        pass\n'
                 '\n'
                 '    def compute_path(self, start, destination):\n'
                 '        # your compute_dijkstra_path(), with\n'
                 '        # build_graph(self.rows, self.cols, self.blocked)\n'
                 '        # and self.weight(); closest() stays a function\n'
                 '        pass\n'
                 '\n'
                 'planner = Dijkstra()',
         'code_size': 20},

        {'kind': 'bullets', 'title': 'A copy of `BFS`, with one more list',
         'bullets': [
             '`BFS` holds its blocked list in `self.blocked` and has `add_blocked()`, '
             '`clear_blocked()` and `compute_path(start, destination)`',
             '`Dijkstra` is a copy of it with **one more list** and the **two changes**',
             'Same shape as the other two: told the position every call, returning a path that '
             'excludes the start',
             'The slow list is the planner\'s own data, as the blocked list already was: nothing '
             'outside the object reaches in to change it',
         ]},

        {'kind': 'bullets', 'title': 'One object called `planner`',
         'bullets': [
             'The Lesson 5-5 rule: one object called `planner`, and it is your **newest** planner',
             'Delete `planner = BFS()`',
             'Everything in Module 5 that said `planner.` now plans by cost',
             'On a grid with no slow edges it gives the same answers as before: prove it by running any '
             'Module 5 test',
         ],
         'callout': 'The one trap: `planner = BFS()` left in the file **below** the Dijkstra one '
                    'silently puts the old planner back',
         'tone': 'orange'},

        {'kind': 'check',
         'question': 'Where does the slow-edge list live in the class version, and why?',
         'options': ['In a global `SLOW_EDGES`, as in Lesson 6-2',
                     'Inside the Dijkstra object as `self.slow_edges`, like `self.blocked`: the '
                     'planner\'s own knowledge, reached only through `add_slow_edge()`',
                     'Inside the harness',
                     'In the Navigator'],
         'answer': 1,
         'explanation': 'A class keeps its data with the methods that use it. The blocked list moved '
                        'inside BFS in Lesson 5-5 for the same reason; the slow list follows it.'},

        {'kind': 'code', 'title': 'One harness, three objects',
         'lead': 'The Lesson 5-6 class harness is handed an object and calls its methods:',
         'code': 'run_all_tests("Manhattan", Manhattan())\n'
                 'run_all_tests("BFS",       BFS())\n'
                 'run_all_tests("Dijkstra",  Dijkstra())',
         'code_size': 24,
         'callout': 'Inside, every line is `planner.compute_path(...)`, `block(planner, ...)` or '
                    '`clear(planner)`. **Nothing in the harness names a class.**',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'One more helper: `slow()`',
         'lead': 'The seventh case needs a helper of the `block()` kind. `slow(planner, a, b, cost)` '
                 'tells the planner about a slow edge **and** records it in `SLOW_EDGES`, so '
                 '`path_cost()` adds up the true weights, whichever planner is being tested.',
         'lead_h': 1.5,
         'code': 'def slow(planner, a, b, cost):\n'
                 '    """Tell planner about the slow edge AND note it in\n'
                 '    SLOW_EDGES, so path_cost() can see it."""\n'
                 '    pass',
         'code_size': 22,
         'callout': 'Paste it under `clear()` in the 5-6 part of the file. `clear()` has to forget the '
                    'slow edges as well as the blocks, on **both** sides.',
         'tone': 'teal'},

        {'kind': 'steps', 'title': 'Three edits to the harness',
         'tag': 'Harness',
         'steps': [
             '`clear(planner)` also calls `planner.clear_slow_edges()` and `clear_slow_edges()`.',
             'In `run_all_tests()`, the seventh case: `slow(planner, (0, 1), (0, 2), 5)` where it said '
             '`add_slow_edge(...)`, `planner.compute_path(...)` for the plan, and `clear(planner)` for '
             'both clears.',
             '`compare()` makes a fresh `BFS()` and a fresh `Dijkstra()`, and a fresh object knows '
             'nothing: before it plans, tell each one every entry in `SLOW_EDGES` with '
             '`p.add_slow_edge(a, b, cost)`. Two lines, and `BFS` ignores them.',
         ],
         'size': 20,
         'notes': 'compare()\'s two new lines make the polymorphism point from the other side: a '
                  'planner that cannot use the slow list is still told it, and nothing checks which '
                  'one it is.'},

        {'kind': 'code', 'title': 'Manhattan and BFS accept the call too',
         'lead': '`slow()` and `clear()` call these on any planner, so `Manhattan` and `BFS` need them, '
                 'even though they ignore them, exactly as `Manhattan.add_blocked()` did nothing in Module 5:',
         'lead_h': 1.25,
         'code': 'class BFS:\n'
                 '    # ...\n'
                 '    def add_slow_edge(self, a, b, cost):\n'
                 '        pass        # BFS does not plan by cost; it accepts the call and ignores it\n'
                 '\n'
                 '    def clear_slow_edges(self):\n'
                 '        pass',
         'code_size': 19,
         'notes': 'The add_slow_edge() that does nothing is the teaching moment. Ask why it has to '
                  'exist, and let students find the "if planner is BFS" they would otherwise need in '
                  'the harness.'},

        {'kind': 'code', 'title': 'Functions (6-3), then objects (6-5)',
         'code': '# Functions (6-3)\n'
                 'run_all_tests("Dijkstra", compute_dijkstra_path)\n'
                 '\n'
                 'path = planner(position, destination)\n'
                 'add_slow_edge((0, 1), (0, 2), 5)\n'
                 '\n'
                 '# Objects (6-5)\n'
                 'run_all_tests("Dijkstra", Dijkstra())\n'
                 '\n'
                 'path = planner.compute_path(start, destination)\n'
                 'slow(planner, (0, 1), (0, 2), 5)',
         'code_size': 20,
         'notes': 'On the lesson page these are two blocks side by side; the slide stacks them.'},

        {'kind': 'bullets', 'title': 'That is polymorphism',
         'bullets': [
             'Three classes, one set of method names, one harness that works on any of them',
             'Code written against a **shape**, the names a planner answers to, rather than against '
             'one particular class',
             'You have used it since Lesson 5-6, where the harness was handed a function',
             'Objects make the shape explicit: it is the **list of methods**',
         ],
         'notes': 'The word is introduced here because students have now done the thing three times: '
                  'the Lesson 5-6 function swap, the Lesson 5-6 class extension, and this. Name it, '
                  'point at the harness, and move on; a lecture on OOP terminology would undo the '
                  'lightness that made the class track work.'},

        {'kind': 'figure', 'title': 'One shape, three classes',
         'figure': '/img/lesson-m6-05/three-planners.svg',
         'caption': 'The methods a planner cannot use are still there, doing nothing, so the harness '
                    'can call them on any of the three.'},

        {'kind': 'check',
         'question': 'Why must `BFS` have an `add_slow_edge()` method that does nothing?',
         'options': ['Python requires every class to have the same methods',
                     'So the harness can call it on whichever planner it holds without checking which: '
                     'the reason `Manhattan` has an `add_blocked()` that does nothing',
                     'Because BFS secretly uses weights',
                     'It does not; the harness skips BFS'],
         'answer': 1,
         'explanation': 'The harness is written against the shape. A planner that cannot use a piece of '
                        'information still has to accept it, or the harness would need an if for every '
                        'class, which is exactly what polymorphism avoids.'},

        {'kind': 'steps', 'title': 'Activity · Build it, test it, read the results',
         'steps': [
             'Fill in the `Dijkstra` methods: the two blocked ones as in `BFS`, the three slow ones from '
             'WEIGHTED GRAPH with `self.slow_edges` for `SLOW_EDGES`, and `compute_path()` from your '
             '6-3 body. Delete `planner = BFS()`.',
             'Give `Manhattan` and `BFS` the two methods that do nothing.',
             'Write `slow()` and make the three harness edits. `test_three_planners()` hands in '
             '`Manhattan()`, `BFS()` and `Dijkstra()`; `test_cost_grid()` says `slow(planner, ...)` '
             'and draws `planner.blocked`. Run `test_three_planners()`.',
         ],
         'size': 19,
         'notes': 'In step 3, dijkstra_distances() also changes: it reads planner.blocked and '
                  'planner.weight().'},

        {'kind': 'code', 'title': 'Expected, on the slow grid',
         'tag': 'Activity',
         'code': '=== Manhattan ===   blocked cases FAIL, cost FAIL     4 of 7\n'
                 '=== BFS ===         blocked cases PASS, cost FAIL     6 of 7\n'
                 '=== Dijkstra ===    everything PASS                   7 of 7',
         'code_size': 20,
         'callout': 'Each planner fails exactly the tests that describe what it cannot do, in the '
                    'harness you wrote in Lesson 5-6, with one case added',
         'tone': 'green'},

        {'kind': 'bullets', 'title': 'Step 4 · The swap on the floor',
         'tag': 'Activity',
         'bullets': [
             'In `test_drive_slow_grid()`, `PLANNER_NAME` now chooses an **object**: '
             '`planner = Dijkstra()` or `planner = BFS()`',
             'It is told the slow segment with `slow(planner, ...)`, and asked for the path with '
             '`planner.compute_path()`',
             'With the `Navigator` class, the drive is `navigator.drive_path(path)`',
             'Run both planners as in Lesson 6-4',
         ],
         'callout': 'Same test program. The only line that changes is the **class name**.',
         'tone': 'teal'},

        {'kind': 'wrapup',
         'questions': [
             'What does `Dijkstra` add to `BFS`?',
             'Why can one harness test three classes?',
             'What is that called?',
         ],
         'next': 'the end of the course: one robot.py, three planners, swapped by one name',
         'notes': 'Answers: a slow list with three methods, and the two changes. They answer to the '
                  'same method names. Polymorphism. Formative: the three-planner harness output; an '
                  'explanation of the empty add_slow_edge(). Exit ticket: "What would the harness need '
                  'if BFS lacked add_slow_edge()?" (An if per class, the thing polymorphism removes.) '
                  'This is the last lesson in the course: a robot that follows lines, drives a grid, '
                  'plans around obstacles and now plans by time, with three planners swappable by one '
                  'name, in one robot.py that has grown since Lesson 2-1.'},
    ],
}
