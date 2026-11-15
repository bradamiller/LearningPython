DECK = {
    'module': 5, 'lesson': 5,
    'doc': 'module-05-pathfinding/lesson-05-compute-bfs-path',
    'title': 'Implementing compute_bfs_path()',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Match each line of `compute_bfs_path()` to a step of the paper method',
             'Explain why `to_visit.pop(0)` (oldest first) matters, and what `pop()` would do',
             'Explain why `if neighbor not in previous` is the "numbered once" rule',
             'Write the walk-back so the path leaves the start out; say why "already there" gives `[]`',
             'Return `[]` when the destination is walled off',
             'Write `bfs_rings()` and use `print_grid()` to draw what the search found',
         ],
         'notes': '50 to 60 minutes. The heart of Module 5: the Lesson 5-3 hand trace becomes working '
                  'Python. Build it in three stages and run a paper test after each. Students who type '
                  'the whole thing and then debug lose the mapping to the paper method, which is the '
                  'point.'},

        {'kind': 'bullets', 'title': 'From pencil to Python',
         'bullets': [
             'About **twenty lines**, each a step you did with a pencil in Lesson 5-3',
             'Build it in **three stages**, with a paper test after each',
             'Then the program **draws its ring numbers**, to compare with yours',
         ],
         'callout': 'Check each printed line against your Lesson 5-3 trace',
         'tone': 'teal',
         'notes': 'A paper test prints paths and step counts; the robot stays on the desk. Have students '
                  'get out their Lesson 5-3 traces, the came-from table and the wall grid. They compare '
                  'against both today.'},

        {'kind': 'code', 'title': 'Skeleton, part 1: setup and search',
         'code': 'def compute_bfs_path(start, destination):\n'
                 '    """Shortest path from start to destination around\n'
                 '    BLOCKED, as the list of intersections to drive to."""\n'
                 '    # SETUP\n'
                 '    # 1. graph = build_graph(ROWS, COLS, BLOCKED)\n'
                 '    # 2. guard: if start or destination is not in the\n'
                 '    #    graph, there is nothing to search -- return []\n'
                 '    # 3. previous = {start: None}      the came-from table\n'
                 '    #    to_visit = [start]           the list beside the grid\n'
                 '    # SEARCH\n'
                 '    # 4. while to_visit is not empty:\n'
                 '    #       take the OLDEST one off the FRONT -> current\n'
                 '    #       if current is the destination: stop looking\n'
                 '    #       for each neighbor of current in the graph:\n'
                 '    #           only if it has no number yet (not in previous)\n'
                 '    #               write where it came from\n'
                 '    #               add it to the END of to_visit',
         'code_size': 16,
         'notes': 'In the BFS PLANNER section, this outline replaces the placeholder compute_bfs_path(). '
                  'It is the Lesson 5-3 method step by step: the comments are the pencil steps, not the '
                  'code. It is deliberately the longest outline in the module, the one place students '
                  'need the hand-holding. The outline continues on the next slide.'},

        {'kind': 'code', 'title': 'Skeleton, part 2: the walk-back',
         'notes': 'Same function as the previous slide: these lines finish the outline of compute_bfs_path().',
         'lead': 'The outline ends with the walk-back, then `pass`:',
         'lead_h': 0.75,
         'code': '    # WALK-BACK\n'
                 '    # 5. if destination never got an entry: return []\n'
                 '    # 6. path = [] ; current = destination\n'
                 '    #    while current is not start:\n'
                 '    #        append current; current = where it came from\n'
                 '    # 7. reverse path and return it\n'
                 '    pass',
         'code_size': 22,
         'callout': 'Seven pencil steps: SETUP is 1 to 3, SEARCH is 4, WALK-BACK is 5 to 7',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Skeleton, part 3: bfs_rings()',
         'lead': 'Under `compute_bfs_path()`, paste the two functions for the picture. The first is an '
                 'outline:',
         'lead_h': 1.2,
         'code': 'def bfs_rings(start):\n'
                 '    """Ring number of every intersection reachable from\n'
                 '    start, as a dictionary -- the search with no break."""\n'
                 '    # the SETUP and SEARCH of compute_bfs_path, with two\n'
                 '    # changes: never stop early, and instead of came-from,\n'
                 '    # write the ring number: one more than current\'s\n'
                 '    pass',
         'code_size': 20,
         'notes': 'bfs_rings() is written at the end of the lesson, after all five paper tests pass.'},

        {'kind': 'bullets', 'title': 'Skeleton, part 4: print_grid() is given',
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
         'notes': 'print_grid(rows, cols, blocked, numbers). It prints the far row first, so y counts '
                  'down the page. The slide shows the loop that draws the rows. On the lesson page it sits under '
                  'the def line and a docstring (top line is the far row, y = 0 is the bottom line, X '
                  'for blocked, . for no entry), and five more lines after it print the dashed line and '
                  'the x numbers along the bottom. Students paste the whole function from the lesson page.'},

        {'kind': 'bullets', 'title': 'Every line is a pencil step',
         'bullets': [
             '`previous`: the **came-from table**; the start came from nowhere',
             '`to_visit`: the **list beside the grid**',
             'The loop: **take the oldest one; every neighbor with no number gets the next number**',
             'But you write **where it came from**, not a number',
         ],
         'size': 24,
         'callout': 'Keep your Lesson 5-3 trace beside you',
         'tone': 'teal',
         'notes': 'previous starts with its first row filled in: the start came from nowhere. to_visit '
                  'starts with the start on it. The loop is the rule students said out loud in Lesson '
                  '5-3: take the oldest one I haven\'t looked around yet. Read the SEARCH part of the '
                  'outline against the trace, one comment at a time, before anyone types.'},

        {'kind': 'figure', 'title': 'Code on the left, pencil on the right',
         'figure': '/img/lesson-m5-05/code-pencil.svg',
         'caption': 'Nothing in the function is new: each line is a step you already did with a pencil.',
         'notes': 'Seven lines of the finished function matched to the pencil method. These single lines '
                  'appear on the lesson page in the open, outside the reveal.'},

        {'kind': 'bullets', 'title': 'Two things to notice before you type',
         'notes': 'An intersection only gets an entry in previous when it is reached, so being a key '
                  'means having a number. The 0 in pop(0) is the index of the front. Both points come '
                  'straight back in the break-it activity: pop() instead of pop(0), and deleting the not-in-previous line.',
         'bullets': [
             '`previous` does **double duty**',
             ['A key in `previous` = **has a number**',
              'So `if neighbor not in previous` is the **numbered-once rule**'],
             'The list is a **queue**',
             ['`append()` onto the end, `pop(0)` off the front',
              'Each ring finishes before the next starts'],
         ],
         'size': 26},

        {'kind': 'check',
         'question': 'In the search loop, what does `if neighbor not in previous:` mean in pencil terms?',
         'options': ['"Only if this intersection has no number yet"',
                     '"Only if this intersection is not blocked"',
                     '"Only if this intersection is the destination"',
                     '"Only if we have not visited the current intersection"'],
         'answer': 0,
         'explanation': 'An intersection gets an entry in previous the first time it\'s reached, so '
                        'not-in-previous means not-yet-numbered. Blocked intersections never come up at '
                        'all: they aren\'t in the graph.'},

        {'kind': 'steps', 'title': 'Step 1 · Setup and the guard',
         'notes': 'The three cases: (0, 0) to (3, 3), (0, 0) to (0, 3), (2, 2) to (2, 2). clear_blocked() '
                  'first, so the test means the same thing whatever ran before it. Run after every stage. '
                  'Empty paths are right for now: the function ends with return [] until Step 3.',
         'steps': [
             'Steps 1 to 3 of the outline; end with `return []` for now',
             'The guard: blocked start or destination? Not in the graph: return `[]`',
             '`test_bfs_open()`: Tests 1 to 3, open grid; print each path and `len(path)` beside the expected count',
             'Start it with `clear_blocked()`. Run it',
         ],
         'size': 20,
         'callout': 'Three empty paths, three wrong counts, no errors',
         'tone': 'green'},

        {'kind': 'steps', 'title': 'Step 2 · The search',
         'notes': 'test_came_from() clears the blocked list first. The dictionary should match keys in '
                  'the same order. The test can stay. Step 3 uses the walled-off fact. '
                  'The 3 by 3 grid with (1, 1) blocked is the Lesson 5-3 trace, so the printed dictionary can be checked line by line against the table students wrote.',
         'steps': [
             'Add step 4, the loop, and a temporary `print(previous)` after it',
             '`test_came_from()`: block only `(1, 1)`; plan `(0, 0)` to `(2, 2)`',
             'Set `ROWS` and `COLS` to 3 and run: does it match your came-from table **exactly**?',
             'Set them back to 4; remove the print',
         ],
         'size': 20,
         'callout': 'Walled off? `to_visit` empties and `destination` never gets into `previous`',
         'tone': 'teal'},

        {'kind': 'steps', 'title': 'Step 3 · The walk-back',
         'notes': "The outline's step 5 (return [] if the destination never got an entry) comes first; it is the walled-off case from the previous slide.",
         'lead': 'Steps 5 to 7 of the outline.',
         'lead_h': 0.65,
         'steps': [
             'From the destination, follow `previous` back to the start, appending as you go',
             'Then **reverse**: you collected it backwards. `reverse()` works in place',
             'Run `test_bfs_open()` again: the step counts should match',
         ]},

        {'kind': 'bullets', 'title': 'Why stop at `start`, and not at `None`?',
         'notes': 'Both conditions would end the loop. Stopping at the start means the start is never '
                  'appended, which is Rule 2 from Lesson 5-4 with no trimming afterwards. When position '
                  '== destination the loop never runs and the path is []. The check on the next slide '
                  'is the exit ticket.',
         'lead': '`while current != start`, not `while current is not None`:',
         'lead_h': 1.0,
         'bullets': [
             'The start is never appended: **Rule 2**, no trimming',
             '"Already there" is free: the loop never runs, so the path is `[]`',
         ],
         'size': 26,
         'callout': 'The robot is already on the start',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'A classmate writes the walk-back as `while current is not None:` and their '
                     'straight-line test prints Steps: 4 instead of 3. What is in their path that shouldn\'t be?',
         'options': ['The start: the loop ran one extra time and appended it',
                     'The destination: it should be left out',
                     'A blocked intersection',
                     'Nothing: 4 is correct'],
         'answer': 0,
         'explanation': 'Running until None appends the start before stopping. Rule 2 says the path is the '
                        'intersections to drive TO; the robot is already on the start.',
         'notes': 'Answer: A. This is the exit ticket. Running until None appends the start before '
                  'stopping; Rule 2 says the robot is already on the start.'},

        {'kind': 'table', 'title': 'Run the five paper tests',
         'lead': 'Tests 1 to 3 are in `test_bfs_open()`. Write `test_bfs_walls()` for Tests 4 and 5.',
         'headers': ['Test', 'Trip', 'Blocked', 'Steps'],
         'widths': [3.4, 2.6, 3.4, 1.2],
         'rows': [
             ['1 · no obstacles', '`(0,0)` to `(3,3)`', 'nothing', '6'],
             ['2 · straight line', '`(0,0)` to `(0,3)`', 'nothing', '3'],
             ['3 · already there', '`(2,2)` to `(2,2)`', 'nothing', '0'],
             ['4 · wall across the grid', '`(0,0)` to `(3,0)`', '`(1, 0)`, `(1, 1)`', '7'],
             ['5 · destination walled off', '`(0,0)` to `(3,0)`', 'the whole column at x = 1', '0'],
         ],
         'callout': 'Step counts must match; the exact path may differ and still be right',
         'tone': 'orange',
         'notes': 'All five are grids students traced by hand in Lesson 5-3. test_bfs_walls() '
                  'add_blocked()s the two wall intersections and plans (0, 0) to (3, 0), then blocks the '
                  'rest of the column at x = 1 and plans it again, printing the blocked list before each.'},

        {'kind': 'code', 'title': 'Tests 4 and 5: what to look for',
         'code': '=== Test 4: wall across the grid, (0,0) to (3,0) ===\n'
                 'Blocked: [(1, 0), (1, 1)]\n'
                 'Path: [(0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (3, 1), (3, 0)]\n'
                 'Steps: 7 (expect 7 -- around the wall)\n'
                 '\n'
                 '=== Test 5: destination walled off ===\n'
                 'Blocked: [(1, 0), (1, 1), (1, 2), (1, 3)]\n'
                 'Path: []\n'
                 'Steps: 0 (expect 0 -- no way through)',
         'code_size': 20,
         'callout': 'Tests 3 and 5 both return `[]`: the walk-back never ran, or the destination was '
                    'never reached',
         'tone': 'teal',
         'notes': 'Next lesson the test harness tells those two apart. The lesson page also shows the '
                  'expected output for Tests 1 to 3; the step counts are in the table on the previous '
                  'slide.'},

        {'kind': 'steps', 'title': 'Activity · Break it on purpose',
         'lead': 'Once all five pass, break it two ways. Undo each before the next.',
         'lead_h': 0.65,
         'steps': [
             'Change `pop(0)` to `pop()`. Run **Test 4** and count the steps',
             'Delete `if neighbor not in previous:` (keep the two lines under it, one level out). '
             'Run **Test 1**. Hangs? Ctrl-C',
         ],
         'size': 22,
         'callout': 'Watch what happens, then explain it',
         'tone': 'orange',
         'notes': 'Not optional. With pop() the search takes the newest intersection, dives down one path '
                  'before finishing the ring, and the first route it finds is not necessarily shortest: '
                  'depth-first search, a fine algorithm for other jobs but not this one. Without the '
                  'not-in-previous line, intersections get their came-from overwritten by later, longer '
                  'routes, and the walk-back can chase its own tail forever. Seeing pop() give a longer '
                  'path is what makes "oldest first" stick; seeing the hang is what makes "numbered '
                  'once" stick. The lesson page has a figure of what pop() did to Test 4 inside a '
                  'reveal; it is left off the slides.'},

        {'kind': 'check',
         'question': 'You change `pop(0)` to `pop()` and Test 4, the wall test, prints Steps: 9 instead '
                     'of 7. What changed?',
         'options': ['It takes the newest intersection first, diving down one route before finishing the ring',
                     'The graph lost some neighbors',
                     'The walk-back went the wrong way',
                     'Nothing: 9 is also a shortest path'],
         'answer': 0,
         'explanation': 'Oldest-first (a queue) finishes each ring before the next. Newest-first (a stack) '
                        'is depth-first search: it finds a path, but not necessarily a shortest one.',
         'notes': 'Answer: A. On the open grid in Test 1, pop() happens to land on a 6-step path too, which '
                  'is why the wall test is the one to run. A test that passes by luck is the reason to '
                  'keep more than one case.'},

        {'kind': 'bullets', 'title': 'The picture: bfs_rings()',
         'bullets': [
             'The same search with **no `break`**: it runs until every reachable intersection has a number',
             'It records the **ring number**, not came-from',
             ['Start: 0', 'Each new neighbor: `current`\'s number + 1'],
             '`print_grid()` draws the result',
         ],
         'size': 24,
         'notes': 'The dictionary it returns is the grid of numbers students wrote in Lesson 5-3. '
                  'Students write the body from the outline: the SETUP and SEARCH of compute_bfs_path() '
                  'with a rings dictionary in place of previous.'},

        {'kind': 'code', 'title': 'test_rings(): your wall grid, drawn by the program',
         'lead': 'Block `(1, 0)` and `(1, 1)`, then call:\n`print_grid(ROWS, COLS, BLOCKED, bfs_rings((0, 0)))`',
         'lead_h': 1.2,
         'code': ' 3 |   3  4  5  6\n'
                 ' 2 |   2  3  4  5\n'
                 ' 1 |   1  X  5  6\n'
                 ' 0 |   0  X  6  7\n'
                 '    -------------\n'
                 '       0  1  2  3',
         'code_size': 24, 'width': 6.5,
         'callout': 'Your Lesson 5-3 wall grid. Test 4\'s path is one route down these numbers, 1, 2, '
                    '3 ... to the 7.',
         'tone': 'green',
         'notes': 'Write the body of bfs_rings() first, then test_rings(). Ask students to trace Test 4\'s '
                  'path on the printed grid with a finger.'},

        {'kind': 'bullets', 'title': 'Optional: the BFS class',
         'tag': 'Optional extension',
         'bullets': [
             '`BFS` has setup to hold: grid size and blocked list',
             '`Manhattan` got a class in Lesson 4-3 **only** to have the same shape, so one main program and one test harness work with either: that is **the swap**',
             'Neither remembers the robot\'s position (Rule 1)',
             '**From here on, use your class**',
         ],
         'size': 24,
         'callout': '`compute_bfs_path(...)` becomes `planner.compute_path(...)`',
         'tone': 'teal',
         'notes': 'Optional extension. In code: planner = BFS(), then planner.add_blocked((1, 1)), then '
                  'path = planner.compute_path((0, 0), (3, 3)). The same four changes as every extension so far: functions move '
                  'inside class BFS and gain self; shared variables move into __init__ as self.rows, '
                  'self.cols, self.blocked; inside methods they gain self.; outside, calls go through the '
                  'object. Manhattan also gets add_blocked() and clear_blocked() methods that deliberately '
                  'do nothing, so next lesson\'s harness can call them on either planner. Delete the '
                  'planner = Manhattan() line and change Lesson 4-3\'s run_test() to call '
                  'Manhattan().compute_path(...). Then test_two_planners(): BFS goes around the wall, '
                  'Manhattan drives straight through. The lesson\'s check: why give Manhattan an '
                  'add_blocked() that does nothing? So every planner has the same shape and the harness '
                  'never has to know which one it holds.'},

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
                 '        # self.blocked = []  -- a method assigns to an\n'
                 '        # attribute freely; no global, no pop loop\n'
                 '        pass\n'
                 '\n'
                 '    def compute_path(self, start, destination):\n'
                 '        # your compute_bfs_path(), with\n'
                 '        # build_graph(self.rows, self.cols, self.blocked)\n'
                 '        pass\n'
                 '\n'
                 'planner = BFS()',
         'code_size': 13,
         'notes': 'Paste it in place of the BFS PLANNER banner and compute_bfs_path(), and delete BLOCKED, '
                  'add_blocked() and clear_blocked() from GRID GRAPH: they live inside the object now. '
                  'The lesson\'s skeleton opens with a five-line header comment, left off the slide to '
                  'fit: one BFS object holds the grid size and its own blocked list, builds the graph '
                  'from self.blocked on every call, and holds no position (Rule 1). Tests change the '
                  'usual way: planner.add_blocked(, planner.clear_blocked(), planner.compute_path(, and '
                  'planner.blocked where they read BLOCKED. The finished methods are in a reveal on the '
                  'lesson page and are not shown here.'},

        {'kind': 'wrapup',
         'questions': [
             'Which line is "take the oldest one"? What would `pop()` do?',
             'Which line is "numbered once"?',
             'Why does the walk-back stop at `start`?',
             'Two cases return `[]`. What are they?',
         ],
         'next': 'test it properly, and swap in Manhattan',
         'notes': 'Answers: to_visit.pop(0); pop() is newest first, depth-first, not shortest. if neighbor '
                  'not in previous. So the start is never appended: Rule 2. Already there, and walled off. '
                  'Formative: the line-to-pencil mapping, five tests passing in order, the two breakages '
                  'explained, not just observed. Keep distances, 999999 and "closest first" out of the '
                  'room; a student who asks about roads that take longer gets "Module 6, and it\'s two '
                  'changes to this function." Next lesson: on an open grid there are many shortest '
                  'paths, so the harness checks what must be true of any correct answer.'},
    ],
}
