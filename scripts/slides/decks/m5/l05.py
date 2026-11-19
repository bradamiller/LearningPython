"""Module 5, Lesson 5-5 · Implementing compute_bfs_path().

Same order as the lesson page: the two outlines, every line a pencil step, then the two
stages (the numbers, then the walk downhill), each a slide to predict on and a slide to
check against, the five paper tests, and the break-it activity. Teacher notes from the
page are in the slide notes.
"""


def step(title, bullets, predict, notes=None, size=24):
    s = {'kind': 'bullets', 'title': title, 'tag': 'Activity', 'bullets': bullets,
         'size': size, 'callout': '**Predict:** ' + predict, 'tone': 'orange'}
    if notes:
        s['notes'] = notes
    return s


def check(title, output, says, notes=None, size=20):
    s = {'kind': 'code', 'title': title, 'tag': 'Activity', 'code': output,
         'code_size': size, 'callout': says, 'tone': 'green'}
    if notes:
        s['notes'] = notes
    return s


DECK = {
    'module': 5, 'lesson': 5,
    'doc': 'module-05-pathfinding/lesson-05-compute-bfs-path',
    'title': 'compute_bfs_path()',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Match each line of `bfs_distances()` and `compute_bfs_path()` to a step of the '
             'paper method',
             'Explain why `to_visit.pop(0)` (oldest first) matters, and what `pop()` would do',
             'Explain why `if neighbor not in distance` is the whole "numbered once" rule',
             'Write the walk downhill so the path leaves the start out, and return `[]` when the '
             'start can\'t be reached',
         ],
         'notes': '50 to 60 minutes. The heart of Module 5: the algorithm reviewed at the end of '
                  'Lesson 5-2 becomes about twenty lines of Python, each a step students have done '
                  'with a pencil. Have their Lesson 5-1 and 5-2 traces on the desk.'},

        {'kind': 'bullets', 'title': 'From pencil to Python',
         'bullets': [
             'Lesson 5-2\'s two parts become two functions:',
             ['`bfs_distances()` **numbers the grid** from the destination',
              '`compute_bfs_path()` **walks downhill** from the start'],
             'Build and test them **in that order**',
         ],
         'size': 28,
         'callout': 'Every test prints. The robot stays on the desk.',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Skeleton, part 1: the numbers',
         'lead': 'In BFS PLANNER, replace the placeholder with two outlines. The first:',
         'lead_h': 0.7,
         'code': 'def bfs_distances(destination):\n'
                 '    """Steps from every reachable intersection to\n'
                 '    destination, as a dictionary: the wave of numbers."""\n'
                 '    # Program only, not a step of the algorithm: build the\n'
                 '    # graph from BLOCKED; return {} if destination is not in it.\n'
                 '    #\n'
                 '    # Number the grid from the destination (Lesson 5-2):\n'
                 '    #  1. Write 0 on the destination.\n'
                 '    #  2. Put the destination on the to-visit list.\n'
                 '    #  3. While the to-visit list is not empty:\n'
                 '    #  4.     Take the oldest one off the front. Call it current.\n'
                 '    #  5.     For each open neighbor of current:\n'
                 '    #  6.         If that neighbor has no number yet:\n'
                 '    #  7.             Give it one more than current\'s number.\n'
                 '    #  8.             Add it to the end of the to-visit list.\n'
                 '    #  9. Return the numbers.\n'
                 '    pass',
         'code_size': 14,
         'notes': 'The outlines are deliberately the longest in the module: this is the one place '
                  'in Module 5 where students need the hand-holding. The comments are the steps of '
                  'Lesson 5-2\'s review, numbered, not the code. Point a stuck student at the step, '
                  'not at the answer.'},

        {'kind': 'code', 'title': 'Skeleton, part 2: the walk downhill',
         'code': 'def compute_bfs_path(start, destination):\n'
                 '    """Shortest path from start to destination around\n'
                 '    BLOCKED, as the list of intersections to drive to."""\n'
                 '    # Program only: build the graph from BLOCKED.\n'
                 '    #\n'
                 '    # Walk downhill from the start (Lesson 5-2):\n'
                 '    #  1. Number the grid: call bfs_distances(destination).\n'
                 '    #  2. If the start has no number, there is no path.\n'
                 '    #  3. Start with an empty path, standing on the start.\n'
                 '    #  4. Until you are standing on the destination:\n'
                 '    #  5.     Find the open neighbor whose number is one less\n'
                 '    #  6.     and step onto it.\n'
                 '    #  7.     Add where you are standing to the path.\n'
                 '    #  8. That path is the answer.\n'
                 '    pass',
         'code_size': 15},

        {'kind': 'bullets', 'title': 'Skeleton, part 3: print_grid()',
         'bullets': [
             'Formatting, not pathfinding: given, and **Module 6 uses it unchanged**',
             '**Far row first**, so the picture lies like the grid in front of you',
             '`"{:>3}".format(cell)`: right-aligned in three spaces',
             'Blocked shows `X`; no entry shows `.`',
         ],
         'size': 20,
         'split': 0.45,
         'code_size': 17,
         'code': '    for i in range(rows):\n'
                 '        y = rows - 1 - i\n'
                 '        line = " " + str(y) + " | "\n'
                 '        for x in range(cols):\n'
                 '            if (x, y) in blocked:\n'
                 '                cell = "X"\n'
                 '            elif (x, y) in numbers:\n'
                 '                cell = numbers[(x, y)]\n'
                 '            else:\n'
                 '                cell = "."\n'
                 '            line = line + "{:>3}".format(cell)\n'
                 '        print(line)',
         'notes': 'print_grid(rows, cols, blocked, numbers). The slide shows the loop that draws the '
                  'rows; five more lines after it print the dashed line and the x numbers along the '
                  'bottom. Students paste the whole function from the lesson page.'},

        {'kind': 'bullets', 'title': 'Every line is a pencil step',
         'bullets': [
             'Under each numbered comment, write the Python for that step: usually one line',
             'Names from Lesson 5-3: `distance` for the numbers, `to_visit` for the list',
             'Step 1 makes `distance` with one entry: the destination, numbered 0',
         ],
         'size': 26},

        {'kind': 'figure', 'title': 'Code on the left, pencil on the right',
         'figure': '/img/lesson-m5-05/code-pencil-downhill.svg',
         'caption': 'Nothing in the code is new: each line is a step you already did with a pencil.'},

        {'kind': 'bullets', 'title': 'Before you type',
         'bullets': [
             'A key in `distance` = **has a number**',
             ['So `if neighbor not in distance` is the whole **numbered-once** rule'],
             'The list is a **queue**',
             ['`append()` adds to the end, `pop(0)` takes from the front',
              'So the wave front moves out one step at a time'],
         ],
         'size': 24,
         'notes': 'An intersection gets an entry in distance only when the wave reaches it. Both '
                  'points come straight back in the break-it activity: pop() instead of pop(0), and '
                  'deleting the not-in-distance line.'},

        {'kind': 'check',
         'question': 'In `bfs_distances()`, what does `if neighbor not in distance:` mean in pencil '
                     'terms?',
         'options': ['"Only if this intersection has no number yet"',
                     '"Only if this intersection is not blocked"',
                     '"Only if this intersection is the destination"',
                     '"Only if we have not visited the current intersection"'],
         'answer': 0,
         'explanation': 'An intersection gets an entry in distance the first time the wave reaches '
                        'it, so not-in-distance means not-yet-numbered. Blocked intersections never '
                        'come up at all: they aren\'t in the graph.'},

        # --- Stage 1: the numbers ---
        step('Step 1 · The numbers',
             ['Write `bfs_distances()`',
              'Write `test_distances()`: clear the blocked list, block `(1, 0)` and `(1, 1)`, then:',
              ['`print_grid(ROWS, COLS, BLOCKED, bfs_distances((3, 0)))`'],
              'Set the run line to it'],
             'the grid it prints. You numbered it in Lesson 5-1.',
             notes='The numbers come first on purpose: test_distances() prints a grid students have '
                   'already drawn by hand, so a wrong number is found before there is a walk to '
                   'blame. Students who type the whole thing and then debug lose the mapping to the '
                   'paper method, which is the point.'),
        check('Step 1 · Check your grid',
              ' 3 |   6  5  4  3\n'
              ' 2 |   5  4  3  2\n'
              ' 1 |   6  X  2  1\n'
              ' 0 |   7  X  1  0\n'
              '    -------------\n'
              '       0  1  2  3',
              'A wrong number? The bug is in `bfs_distances()`: there\'s no walk yet to blame',
              size=24),

        # --- Stage 2: the walk downhill ---
        {'kind': 'bullets', 'title': 'Step 2 · The walk downhill', 'tag': 'Activity',
         'bullets': [
             'Write `compute_bfs_path()`',
             'Start has no number? The wave never reached it: **no path**',
             ['One check covers a blocked start, a blocked destination and a wall between'],
             'Add an intersection to the path only **after** stepping onto it',
         ],
         'size': 24,
         'callout': 'So the start never goes in, and already there is `[]` for free',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Step 2 · A loop inside a loop', 'tag': 'Activity',
         'bullets': [
             'The outer `while`: keep walking until you\'re on the destination',
             'The inner `for`: look through the neighbors for one with a number **one less**',
             'Found it? Step onto it, and `break` to stop looking',
             'Check it has a number first: `neighbor in distance and ...`',
         ],
         'size': 24,
         'notes': 'The for with a break inside the while is the one genuinely new shape. Walk '
                  'through it once on the board with the 3x3 numbers from Lesson 5-2.'},

        {'kind': 'check',
         'question': 'A classmate\'s walk adds current to the path BEFORE stepping. Their test, '
                     '(0,0) to (0,3), prints Steps: 3, but the path is [(0, 0), (0, 1), (0, 2)]. '
                     'What\'s wrong?',
         'options': ['The start is in the path and the destination is missing',
                     'Nothing: 3 steps is right',
                     'The path goes the wrong way',
                     'A blocked intersection got into the path'],
         'answer': 0,
         'explanation': 'Adding before stepping writes down where you were, not where you went. The '
                        'step count is right, which is why a test should check the list, not just '
                        'its length.',
         'notes': 'This is the exit ticket.'},

        # --- The five paper tests ---
        step('Run the five paper tests',
             ['`test_bfs_open()`: start with `clear_blocked()`, then plan',
              ['(0,0) to (3,3), (0,0) to (0,3), (2,2) to (2,2)'],
              '`test_bfs_walls()`: block (1,0) and (1,1), plan (0,0) to (3,0)',
              ['then block the rest of the column at x = 1 and plan again'],
              'Print each path, its `len()`, and the step count you expect'],
             'the step count of each. They\'re all grids you traced by hand.',
             size=22,
             notes='clear_blocked() first, so the test means the same whatever ran before it. '
                   'Print the blocked list before each wall test.'),
        check('Tests 1 to 3 · Check your output',
              '=== Test 1: no obstacles, (0,0) to (3,3) ===\n'
              'Path: [(1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)]\n'
              'Steps: 6 (expect 6)\n'
              '\n'
              '=== Test 2: straight line, (0,0) to (0,3) ===\n'
              'Path: [(0, 1), (0, 2), (0, 3)]\n'
              'Steps: 3 (expect 3)\n'
              '\n'
              '=== Test 3: already there, (2,2) to (2,2) ===\n'
              'Path: []\n'
              'Steps: 0 (expect 0)',
              'Step counts must match. The exact path may differ from yours and still be right',
              size=16),
        check('Tests 4 and 5 · Check your output',
              '=== Test 4: wall across the grid, (0,0) to (3,0) ===\n'
              'Blocked: [(1, 0), (1, 1)]\n'
              'Path: [(0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (3, 1), (3, 0)]\n'
              'Steps: 7 (expect 7 -- around the wall)\n'
              '\n'
              '=== Test 5: destination walled off ===\n'
              'Blocked: [(1, 0), (1, 1), (1, 2), (1, 3)]\n'
              'Path: []\n'
              'Steps: 0 (expect 0 -- no way through)',
              'Tests 3 and 5 both return `[]`: already there, and the start never got a number',
              notes='Next lesson\'s harness tells the two empty paths apart. The finished functions '
                    'are behind the "Check your two functions" reveal on the lesson page.',
              size=16),

        # --- Break it on purpose ---
        step('Break it 1 · `pop(0)` becomes `pop()`',
             ['Once all five pass, change `pop(0)` to `pop()` in `bfs_distances()`',
              'Run Test 4'],
             'more steps, fewer, or the same?',
             notes='The break-it activity is not optional: seeing pop() give a longer path is what '
                   'makes "oldest first" stick.'),
        {'kind': 'figure', 'title': 'Break it 1 · Check: 9 steps, not 7', 'tag': 'Activity',
         'figure': '/img/lesson-m5-05/bfs-vs-dfs-downhill-xy.svg',
         'caption': '`pop()` takes the newest, so the numbers stop being shortest distances. The '
                    'walk is only as good as its numbers.',
         'notes': 'Have them run test_distances() too and compare the grid with theirs. On Test 1\'s '
                  'open grid, pop() happens to give 6 steps too: a test can pass by luck, which is '
                  'why you keep more than one case. Put pop(0) back before the next break.'},

        {'kind': 'check',
         'question': 'You change `pop(0)` to `pop()` and Test 4 prints Steps: 9 instead of 7. What '
                     'changed?',
         'options': ['Newest-first writes numbers that are not shortest distances, and the walk '
                     'follows them on a longer route',
                     'The graph lost some neighbors',
                     'The walk downhill went the wrong way',
                     'Nothing: 9 is also a shortest path'],
         'answer': 0,
         'explanation': 'Oldest first (a queue) moves the wave out one step at a time, so each number '
                        'is the fewest steps. Newest first (a stack) numbers along whatever route it '
                        'dives down.'},

        step('Break it 2 · Delete one line',
             ['Delete `if neighbor not in distance:`',
              'Keep the two lines under it, one indent level out',
              'Run Test 1'],
             'what happens?'),
        {'kind': 'bullets', 'title': 'Break it 2 · Check: it hangs', 'tag': 'Activity',
         'bullets': [
             'Every neighbor goes back on the list **every time**',
             'So the list never empties. Press **Ctrl-C**',
         ],
         'size': 28,
         'callout': 'That one line is the numbered-once rule',
         'tone': 'green',
         'notes': 'Seeing the program hang is what makes "numbered once" stick. Put the line back. '
                  'Keep 999999 and "closest first" out of the room; a student who asks about roads '
                  'that take longer gets "Module 6."'},

        # --- Optional extension ---
        {'kind': 'bullets', 'title': 'Optional: the BFS class',
         'tag': 'Optional extension',
         'bullets': [
             '`BFS` has setup to hold: grid size and blocked list',
             '`Manhattan` got a class in Lesson 4-3 **only** to have the same shape, so one main '
             'program and one test harness work with either: that is **the swap**',
             'Neither remembers the robot\'s position (Rule 1)',
             '**From here on, use your class**',
         ],
         'size': 24,
         'callout': '`compute_bfs_path(...)` becomes `planner.compute_path(...)`',
         'tone': 'teal',
         'notes': 'Optional extension. In code: planner = BFS(), then planner.add_blocked((1, 1)), '
                  'then path = planner.compute_path((0, 0), (3, 3)). The same four changes as every '
                  'extension so far: functions move inside class BFS and gain self; shared variables '
                  'move into __init__ as self.rows, self.cols, self.blocked; inside methods they gain '
                  'self.; outside, calls go through the object. Manhattan also gets add_blocked() '
                  'and clear_blocked() methods that deliberately do nothing, so next lesson\'s '
                  'harness can call them on either planner. Delete the planner = Manhattan() line '
                  'and change Lesson 4-3\'s run_test() to call Manhattan().compute_path(...). Then '
                  'test_two_planners(): BFS goes around the wall, Manhattan drives straight through.'},

        {'kind': 'code', 'title': 'Optional: the class-track skeleton',
         'tag': 'Optional extension',
         'code': 'class BFS:\n'
                 '    def __init__(self, rows=4, cols=4):\n'
                 '        self.rows = rows\n'
                 '        self.cols = cols\n'
                 '        self.blocked = []\n'
                 '\n'
                 '    def add_blocked(self, intersection):\n'
                 '        # your function, with self.blocked for BLOCKED\n'
                 '        pass\n'
                 '\n'
                 '    def clear_blocked(self):\n'
                 '        # self.blocked = []  -- no global, no pop loop\n'
                 '        pass\n'
                 '\n'
                 '    def bfs_distances(self, destination):\n'
                 '        # your function, with\n'
                 '        # build_graph(self.rows, self.cols, self.blocked)\n'
                 '        pass\n'
                 '\n'
                 '    def compute_path(self, start, destination):\n'
                 '        # your compute_bfs_path(), with the same graph line\n'
                 '        # and self.bfs_distances(destination)\n'
                 '        pass\n'
                 '\n'
                 'planner = BFS()',
         'code_size': 12,
         'notes': 'Paste it in place of the BFS PLANNER banner, bfs_distances() and '
                  'compute_bfs_path(), and delete BLOCKED, add_blocked() and clear_blocked() from '
                  'GRID GRAPH: they live inside the object now. Tests change the usual way: '
                  'planner.add_blocked(, planner.clear_blocked(), planner.compute_path(, '
                  'planner.bfs_distances(, and planner.blocked where they read BLOCKED. The finished '
                  'methods are in a reveal on the lesson page.'},

        {'kind': 'wrapup',
         'questions': [
             'Which line is "take the oldest one"? What would `pop()` do?',
             'Which line is "numbered once"?',
             'Why add an intersection only after stepping onto it?',
             'Two cases return `[]`. What are they?',
         ],
         'next': 'test it properly, and swap in Manhattan',
         'notes': 'Answers: to_visit.pop(0); pop() is newest first, not shortest. if neighbor not in '
                  'distance. So the start is never in the path: Rule 2. Already there, and the start '
                  'never got a number. Formative: the line-to-pencil mapping, the grid and five '
                  'tests passing in order, the two breakages explained, not just observed. Next '
                  'lesson: on an open grid there are many shortest paths, so the harness checks what '
                  'must be true of any correct answer, then runs against Manhattan, which fails the '
                  'wall tests on screen.'},
    ],
}
