"""Module 4, Lesson 4-2 · The Planner: A Path That Grows.

The discussion "Where does the path go?" runs one slide per question, then one
slide with the answer, as in Lesson 5-1. Each question slide's notes hold that
step of the lesson's teacher notes. Grids: scripts/figures/m4discuss.py.
"""

FIG = '/img/lesson-m4-discuss/'


def ask(n, total, question, figure=None, notes=None):
    s = {'kind': 'bullets', 'title': f'Question {n} of {total}', 'tag': 'Discuss',
         'bullets': question, 'size': 28}
    if figure:
        s.update(figure=figure if figure.startswith('/') else FIG + figure + '.svg', split=0.55)
    if notes:
        s['notes'] = notes
    return s


def answer(n, total, points, rule=None, figure=None, notes=None):
    s = {'kind': 'bullets', 'title': f'Answer {n} of {total}', 'tag': 'Discuss',
         'bullets': points, 'size': 28}
    if figure:
        s.update(figure=figure if figure.startswith('/') else FIG + figure + '.svg', split=0.55)
    if rule:
        s.update(callout=rule, tone='green')
    if notes:
        s['notes'] = notes
    return s


DECK = {
    'module': 4, 'lesson': 2,
    'doc': 'module-04-manhattan/lesson-02-a-path-that-grows',
    'title': 'The Planner: A Path That Grows',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Work out the planner\'s rule: change one number by 1 until it matches the '
             'destination\'s',
             'Build a path by hand with `append()`, across first, then up',
             'Start with an empty list, add to it with `append()`, and count it with `len()`',
             'Unpack a tuple into `x` and `y`, and make a new tuple from them',
             'Build a path inside a `while` loop, one step per trip around',
             'Explain what happens when two names refer to the same list',
         ],
         'notes': '60 to 75 minutes, robot on the desk. It opens with a 10 to 15 minute discussion in which the class works out the planner\'s rule. The planner stub hands back one jump; '
                  'today it starts to build real paths, for any trip that goes right and up. Left '
                  'and down are Lesson 4-3. "Empty list, append inside a loop" is the pattern the '
                  'rest of the course builds paths with. Scope: [], append(), len(), unpacking. '
                  'No indexing yet (4-4), and no insert, pop or slicing at all.'},

        {'kind': 'bullets', 'title': 'The stub hands back one jump',
         'bullets': [
             'Right now `compute_manhattan_path()` returns `[destination]`',
             'A real path lists **every** intersection on the way',
             'Today the stub starts to go: by the end, real paths for trips that go **right and up**',
         ],
         'callout': 'Left and down come in Lesson 4-3',
         'tone': 'teal', 'size': 28},

        # --- Discuss · Where does the path go? ---
        {'kind': 'bullets', 'title': 'Where does the path go?', 'tag': 'Discuss',
         'bullets': [
             'Draw a 4×4 grid: S at (0,0), D at (2,3)',
             'That\'s Leg 1 of the delivery run',
             'Answer each question before you go on to the next',
         ],
         'split': 0.55,
         'figure': FIG + 'm4d-42-grid.svg',
         'notes': 'Leading the discussion, 10 to 15 minutes. Draw the grid big on the board and '
                  'mark the intersections as the class names them. The goal is that they say the '
                  'rule; your job is to ask the next question. Keep the robot out of it: turning '
                  'and driving are Lesson 4-4\'s discussion. Today the driver stays a stub.'},

        ask(1, 8, ['What is the **fewest** number of blocks the robot can drive from S to D?',
                   'Is there only one route that short?'], 'm4d-42-grid',
            notes='Have a few students trace different 5-block routes on the board. Then ask: '
                  '"Which one is easiest to explain to someone over the phone?" Steer to across '
                  'first, then up, the rule from Lesson 4-0.'),
        answer(1, 8, ['**5 blocks**: 2 across and 3 up',
                      '**No**, there are several',
                      'We pick the easiest to describe: all the way **east**, then all the way '
                      '**north**'], figure='m4d-42-routes'),

        ask(2, 8, ['List, in order, every intersection the robot drives to on that route',
                   'Does S go on the list?'], 'm4d-42-route',
            notes='Write the list on the board as a list of tuples, the way DELIVERY_STOPS is '
                  'written, and leave it there: Step 1 types it in. If someone starts with (0,0), '
                  'ask: "Does the robot drive to (0,0)?"'),
        answer(2, 8, ['(1,0), (2,0), (2,1), (2,2), (2,3)',
                      '**S doesn\'t**: the robot is already there'],
               rule='This list is the path the planner has to hand back', figure='m4d-42-path'),

        ask(3, 8, ['From one intersection on the list to the next, **what changes**?'],
            'm4d-42-path',
            notes='Point at neighbors on the board list, (1,0) then (2,0), (2,1) then (2,2), and '
                  'ask each time: "Which number changed? By how much?"'),
        answer(3, 8, ['**One number, by exactly 1**',
                      'x on the way across, then y on the way up',
                      'Never both: that would be a diagonal'],
               figure='/img/lesson-m4-03/one-step.svg'),

        ask(4, 8, ['On the way across, how does the planner know when to **stop** going east?'],
            'm4d-42-path',
            notes='Questions 3 and 4 are the heart of it. Write the rule on the board and '
                  'underline it. "Until it matches" is a loop that keeps going while x is less '
                  'than D\'s x: Step 2 writes it.'),
        answer(4, 8, ['**When x equals D\'s x**',
                      'Then the same with y'],
               rule='**Add 1 to x until it matches D\'s x, then add 1 to y until it matches '
                    'D\'s y.**'),

        ask(5, 8, ['Leg 2 goes from (2,3) to (1,0). What is different?',
                   'How does the planner know **which way** to go?'], 'm4d-42-leg2-q',
            notes='Draw Leg 2 on a fresh grid. If someone says "subtract", ask "subtract what '
                  'from what?" and steer back to comparing.'),
        answer(5, 8, ['**Both numbers get smaller**: one step west, then three south',
                      'Compare where you are with D, one number at a time',
                      'x smaller than D\'s x: east. Bigger: west. Same with y: north or south'],
               rule='Four directions. East and north today; west and south in Lesson 4-3',
               figure='m4d-42-leg2'),

        ask(6, 8, ['What if x already matches D\'s x at the start?',
                   'What if S and D are the **same** intersection?'],
            notes='If anyone wants a special case, ask: "Does the rule already do the right '
                  'thing?" Walk it through (2,0) to (2,3): x already matches, so there are no '
                  'steps across. Lesson 4-3 tests both cases.'),
        answer(6, 8, ['**No steps across**: the robot only goes up or down',
                      '**S is D: the path is empty**. The robot is already there'],
               rule='The rule handles both with nothing extra'),

        ask(7, 8, ['Without listing the path, can you tell **how many** intersections are on '
                   'it?'],
            notes='Steps across is how far apart the two x\'s are; steps up or down is how far '
                  'apart the two y\'s are. Don\'t name it yet: Lesson 5-1 calls it the '
                  'Manhattan distance.'),
        answer(7, 8, ['**Steps across plus steps up or down**',
                      'Leg 1: 2 + 3 = 5',
                      'Leg 2: 1 + 3 = 4'],
               rule='A quick check on any path the planner prints'),

        ask(8, 8, ['Does it matter that we go **across first**?'], 'm4d-42-routes',
            notes='Leave this one open. In Module 5 an intersection can be blocked, and then '
                  'which intersections you drive through is exactly what matters.'),
        answer(8, 8, ['**Not for the length**: up first is 5 blocks too',
                      '**It does change which intersections** the robot drives through'],
               figure='m4d-42-routes'),

        # --- Step 1 ---
        {'kind': 'code', 'title': 'Step 1 · A list can grow',
         'tag': 'Activity',
         'lead': 'The planner doesn\'t know the path until it works it out. So it starts **empty** '
                 'and adds to the **end**:',
         'code': 'path = []\n'
                 'path.append((1, 0))\n'
                 'path.append((2, 0))\n'
                 'print(path)          # [(1, 0), (2, 0)]\n'
                 'print(len(path))     # 2',
         'code_size': 22,
         'callout': 'Double parentheses: the outer pair is `append()`, the inner pair is the tuple',
         'tone': 'teal',
         'notes': 'len() counts the items. Take real time on the double parentheses.'},

        {'kind': 'steps', 'title': 'Step 1 · Leg 1, by hand',
         'tag': 'Activity',
         'lead': 'Leg 1: (0, 0) to (2, 3), right twice, then up three times. The start is **not** '
                 'in the path. In `compute_manhattan_path()`, keep the `print` line. Replace '
                 '`return [destination]` with:',
         'steps': [
             '`path = []`',
             'Five `append()` lines, one per move, each followed by `print(path)`. The first is '
             '`path.append((1, 0))`',
             '`return path`. Then run `test_delivery()`',
         ],
         'callout': '**Predict:** the five lists Leg 1 prints, and Leg 2\'s path',
         'tone': 'orange',
         'notes': 'Answer: the list grows by one tuple per append, on the end. Leg 2 gets the same '
                  'five steps, starting with a jump from (2, 3) to (1, 0), and so does every leg: '
                  'the function never looks at start or destination. Deliberately clumsy; keep it '
                  'to ten minutes.'},

        {'kind': 'code', 'title': 'Step 1 · Check: Leg 1',
         'tag': 'Activity',
         'code': 'computing path from: (0, 0) to: (2, 3)\n'
                 '[(1, 0)]\n'
                 '[(1, 0), (2, 0)]\n'
                 '[(1, 0), (2, 0), (2, 1)]\n'
                 '[(1, 0), (2, 0), (2, 1), (2, 2)]\n'
                 '[(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]',
         'code_size': 20,
         'callout': 'Leg 1 is right. But Leg 2 gets **the same five steps**: the function hands back '
                    'what you typed.',
         'tone': 'green'},

        {'kind': 'bullets', 'title': 'Step 1 · Could you just type more?',
         'tag': 'Activity',
         'bullets': [
             'How many `append()` lines would Leg 2 need?',
             'All five legs?',
             'Corner to corner on a 10 x 10 grid?',
         ],
         'callout': 'A planner has to **work the path out** from where the robot is and where it\'s going',
         'tone': 'orange', 'size': 26,
         'notes': 'Leg 2 needs 4; all five legs need 18 between them, but one function has only one '
                  'set of lines, so typed lines are right for one trip at most. Corner to corner on '
                  'a 10 x 10 grid is 18 by itself.'},

        {'kind': 'check',
         'question': 'What does this print? `stops = []`, then `stops.append((0, 1))`, '
                     '`stops.append((0, 2))`, `stops.append((1, 2))`, then '
                     '`print(len(stops), stops)`',
         'options': ['`3 [(1, 2), (0, 2), (0, 1)]`',
                     '`3 [(0, 1), (0, 2), (1, 2)]`',
                     '`6 [0, 1, 0, 2, 1, 2]`',
                     '`1 [(1, 2)]`'],
         'answer': 1,
         'explanation': 'append() adds to the end, so the items stay in the order they were added. '
                        'Three appends, three tuples, so len() is 3.'},

        # --- Step 2 ---
        {'kind': 'figure', 'title': 'Step 2 · A loop appends',
         'tag': 'Activity',
         'figure': '/img/lesson-m4-03/appends-to-loops.svg',
         'caption': 'Each append is one trip around a loop.'},

        {'kind': 'code', 'title': 'Step 2 · Take the tuples apart',
         'tag': 'Activity',
         'lead': 'To add 1 to x, the function needs x on its own. **Unpacking** (Lesson 4-1):',
         'code': 'x, y = start              # where the plan is now\n'
                 'dest_x, dest_y = destination   # where it is going',
         'code_size': 22,
         'callout': 'After each move, `(x, y)` puts them back together as a **new tuple** for the '
                    'path',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Step 2 · The new planner',
         'tag': 'Activity',
         'code': 'def compute_manhattan_path(start, destination):\n'
                 '    print("computing path from:", start, "to:", destination)\n'
                 '    path = []\n'
                 '    x, y = start              # where the plan is now\n'
                 '    dest_x, dest_y = destination   # where it is going\n'
                 '\n'
                 '    # East: keep stepping right until x matches dest_x\n'
                 '    while x < dest_x:\n'
                 '        x = x + 1             # one step right\n'
                 '        path.append((x, y))   # record the new spot\n'
                 '\n'
                 '    # North: copy east, but step y until it matches dest_y\n'
                 '\n'
                 '    return path',
         'code_size': 18,
         'notes': 'The slide leaves out the docstring to fit; students paste the whole block from '
                  'the lesson page.'},

        {'kind': 'code', 'title': 'Step 2 · Paper test, then run',
         'tag': 'Activity',
         'lead': 'Add this under it. On paper, write the full path for each trip:',
         'code': 'def test_planner():\n'
                 '    print(compute_manhattan_path((0, 0), (2, 3)))\n'
                 '    print(compute_manhattan_path((0, 2), (3, 2)))\n'
                 '    print(compute_manhattan_path((2, 0), (2, 3)))',
         'code_size': 22,
         'callout': '**Predict:** with only the east loop, what will each print? Then run '
                    '`test_planner()`.',
         'tone': 'orange'},

        {'kind': 'code', 'title': 'Step 2 · Check your output',
         'tag': 'Activity',
         'code': 'computing path from: (0, 0) to: (2, 3)\n'
                 '[(1, 0), (2, 0)]\n'
                 'computing path from: (0, 2) to: (3, 2)\n'
                 '[(1, 2), (2, 2), (3, 2)]\n'
                 'computing path from: (2, 0) to: (2, 3)\n'
                 '[]',
         'code_size': 22,
         'callout': 'Right two, then stop. The second needs no move up. The third only goes up, '
                    'so nothing is appended.',
         'tone': 'green'},

        # --- Step 3 ---
        {'kind': 'steps', 'title': 'Step 3 · Break it on purpose',
         'tag': 'Activity',
         'steps': [
             'Move `path.append((x, y))` one indent to the left, so it lines up with `while`',
             '**Predict** the first path, then run it',
             'Put the indent back',
         ],
         'callout': 'Predict before you run',
         'tone': 'orange',
         'notes': 'The indentation bug is the most common list bug there is; here it costs one '
                  'keystroke to cause and to fix.'},

        {'kind': 'code', 'title': 'Step 3 · What happened?',
         'tag': 'Activity',
         'code': 'computing path from: (0, 0) to: (2, 3)\n'
                 '[(2, 0)]\n'
                 'computing path from: (0, 2) to: (3, 2)\n'
                 '[(3, 2)]\n'
                 'computing path from: (2, 0) to: (2, 3)\n'
                 '[(2, 0)]',
         'code_size': 22,
         'callout': 'Indentation decides what\'s inside the loop. `append()` now runs **once, '
                    'after** the loop.',
         'tone': 'green',
         'notes': 'Only the last position is recorded. The third path is worse: the loop never '
                  'ran, so the function appended the start itself.'},

        # --- Step 4 ---
        {'kind': 'steps', 'title': 'Step 4 · Write north',
         'tag': 'Activity',
         'steps': [
             'Under the north comment, **copy the east loop**',
             'Compare `y` with `dest_y`, and step `y` instead of `x`',
             'Leave `path.append((x, y))` as it is: it records the whole position',
             'Run `test_planner()`. All three paths should match your paper test',
         ],
         'tone': 'green'},

        {'kind': 'code', 'title': 'Step 4 · Check your north loop',
         'tag': 'Activity',
         'code': '    # North: copy east, but step y until it matches dest_y\n'
                 '    while y < dest_y:\n'
                 '        y = y + 1             # one step up\n'
                 '        path.append((x, y))',
         'code_size': 22},

        {'kind': 'code', 'title': 'Step 4 · Check your output',
         'tag': 'Activity',
         'code': 'computing path from: (0, 0) to: (2, 3)\n'
                 '[(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]\n'
                 'computing path from: (0, 2) to: (3, 2)\n'
                 '[(1, 2), (2, 2), (3, 2)]\n'
                 'computing path from: (2, 0) to: (2, 3)\n'
                 '[(2, 1), (2, 2), (2, 3)]',
         'code_size': 22,
         'callout': 'All three match the paper test',
         'tone': 'green'},

        # --- Step 5 ---
        {'kind': 'code', 'title': 'Step 5 · A tuple can\'t change',
         'tag': 'Activity',
         'lead': 'Could the loop just add to one tuple instead of making new ones? Type these into the shell:',
         'code': 'spot = (2, 3)\n'
                 'spot.append(4)',
         'code_size': 26,
         'callout': '**Predict:** what happens?',
         'tone': 'orange'},

        {'kind': 'code', 'title': 'Step 5 · What happened?',
         'tag': 'Activity',
         'lead': 'A tuple **can\'t be changed** once it\'s made, so the loop makes a new one every '
                 'step:',
         'code': 'AttributeError: \'tuple\' object has no attribute \'append\'',
         'code_size': 22,
         'callout': '**Tuple:** one thing with a fixed number of parts, like a position. '
                    '**List:** any number of things in order, like the stops on a route.',
         'tone': 'teal',
         'notes': 'That\'s right for a position: (2, 3) should always mean the same intersection. '
                  'A list is the opposite: it can grow.'},

        {'kind': 'check',
         'question': 'A program adds every obstacle the robot finds, as it drives. What should it '
                     'store them in?',
         'options': ['One tuple, with `append()`',
                     'A list of tuples: each obstacle is an (x, y) tuple, and the list grows',
                     'A tuple of lists',
                     'Two separate variables, `x` and `y`'],
         'answer': 1,
         'explanation': 'Each position is a fixed pair, so a tuple. The collection grows as the '
                        'robot drives, so a list. That is exactly what Module 5 does.'},

        # --- Step 6 ---
        {'kind': 'code', 'title': 'Step 6 · Two names, one list',
         'tag': 'Activity',
         'lead': 'A list can grow, so it lives elsewhere. The variable holds its **address**: a '
                 '**reference**.',
         'code': 'a = 5\n'
                 'b = a\n'
                 'b = b + 1\n'
                 'print(a, b)\n'
                 '\n'
                 'path = [(1, 0)]\n'
                 'same_path = path\n'
                 'same_path.append((2, 0))\n'
                 'print(path)',
         'code_size': 20,
         'callout': '**Predict** both printouts, then run it in the shell',
         'tone': 'orange',
         'notes': 'This adds to Lesson 1-9; it doesn\'t correct it. A variable is still a named '
                  'memory location, and = still stores there. The new fact is what the stored '
                  'value is for a list: a location is a fixed size, so the list lives somewhere '
                  'else. A demo that lands: two students hold slips with the same post office box '
                  'number; one puts something in the box, and the other finds it there.'},

        {'kind': 'figure', 'title': 'Step 6 · What happened?',
         'tag': 'Activity',
         'figure': '/img/lesson-m4-02/number-vs-list.svg',
         'caption': 'Prints 5 6, then [(1, 0), (2, 0)]. b = a makes a second 5. same_path = path '
                    'makes a second arrow to the same list.',
         'notes': 'b = a copied the value: two separate 5s. same_path = path copied the address: '
                  'still one list, so appending through either name changes what both see. Don\'t '
                  'teach copy() or slicing: nothing in this course needs a separate copy, and '
                  'Module 5\'s BLOCKED list relies on the sharing.'},

        {'kind': 'code', 'title': 'Step 6 · Same for a parameter',
         'tag': 'Activity',
         'lead': '**Predict** both printouts, then run it:',
         'code': 'def move(spot):\n'
                 '    spot = (9, 9)             # assigns a new value\n'
                 '\n'
                 'def extend(steps):\n'
                 '    steps.append((9, 9))      # changes the list itself\n'
                 '\n'
                 'here = (1, 1)\n'
                 'move(here)\n'
                 'print(here)\n'
                 '\n'
                 'route = [(1, 1)]\n'
                 'extend(route)\n'
                 'print(route)',
         'code_size': 17},

        {'kind': 'code', 'title': 'Step 6 · What happened?',
         'tag': 'Activity',
         'code': '(1, 1)\n'
                 '[(1, 1), (9, 9)]',
         'code_size': 26,
         'callout': '`=` stores a new value in the function\'s own variable (4-1). '
                    '`append()` goes to the list itself, and there is only one list.',
         'tone': 'green',
         'notes': 'The caller never sees the =. Module 5 relies on the append: a planner sees '
                  'every obstacle you add to your list.'},

        {'kind': 'check',
         'question': 'What does `scores` hold after these three lines? `scores = [10, 20]`, '
                     '`backup = scores`, `backup.append(30)`',
         'options': ['`[10, 20]`: backup is a separate copy',
                     '`[10, 20, 30]`: both variables refer to the same list',
                     '`[30]`',
                     'An error: you cannot assign a list to another name'],
         'answer': 1,
         'explanation': 'backup = scores stores the address that was in scores, not a copy of the '
                        'list, so both variables lead to one list.'},

        {'kind': 'check',
         'question': 'A function is handed a list, `blocked`, and runs `blocked.append((2, 2))`. '
                     'What does the caller\'s list hold after?',
         'options': ['What it held before: functions cannot change the caller\'s variables',
                     'The old items plus (2, 2): the function and the caller refer to the same '
                     'list',
                     'Only (2, 2)',
                     'Nothing: the list is emptied when the function ends'],
         'answer': 1,
         'explanation': 'The parameter holds the list\'s address, so append() changes the one list '
                        'both sides share. Only assigning with = inside the function would leave '
                        'the caller\'s list alone.'},

        # --- Step 7 ---
        {'kind': 'steps', 'title': 'Step 7 · Run the main program',
         'tag': 'Activity',
         'steps': [
             'Set the run line back to `test_delivery()`',
             '**Predict:** will Leg 2, (2, 3) to (1, 0), work?',
             'Run it',
         ],
         'tone': 'orange'},

        {'kind': 'code', 'title': 'Step 7 · Check: Legs 1 and 2',
         'tag': 'Activity',
         'code': 'computing path from: (0, 0) to: (2, 3)\n'
                 '[(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]\n'
                 'moving: from (0, 0) to: (1, 0)\n'
                 'moving: from (1, 0) to: (2, 0)\n'
                 'moving: from (2, 0) to: (2, 1)\n'
                 'moving: from (2, 1) to: (2, 2)\n'
                 'moving: from (2, 2) to: (2, 3)\n'
                 'new position: (2, 3) heading: 0\n'
                 'computing path from: (2, 3) to: (1, 0)\n'
                 '[]\n'
                 'new position: (2, 3) heading: 0',
         'code_size': 18,
         'callout': 'Leg 2\'s path is empty, so the robot never leaves (2, 3). Every leg after it '
                    'goes wrong.',
         'tone': 'orange',
         'notes': 'The hook for Lesson 4-3: let students say what\'s missing. The rest of the '
                  'printout is on the lesson page: Leg 3 is [(3, 3)], and Legs 4 and 5 are [].'},

        {'kind': 'check',
         'question': 'Why is the path for Leg 2, (2, 3) to (1, 0), empty?',
         'options': ['`append()` only works once per program',
                     'Both while conditions are False from the start (2 is not < 1, 3 is not < 0), '
                     'so neither loop runs',
                     'The start and destination are the same',
                     'The driver is still a stub'],
         'answer': 1,
         'explanation': 'East and north only handle x and y getting bigger, and a while loop whose '
                        'condition starts False does nothing. Lesson 4-3 adds left and down.'},

        {'kind': 'wrapup',
         'questions': [
             'How does the planner build a path?',
             'Why is a position a tuple and a path a list?',
             'If two names refer to the same list and you append through one, what does the '
             'other see?',
             'What still doesn\'t work?',
         ],
         'next': 'the planner, part 2: every direction',
         'notes': 'Answers: start with [] and append() one position on every trip around a loop. '
                  'A position is a fixed pair that shouldn\'t change; a path grows one step at a '
                  'time. The change: there is only one list. Trips that go left or down: both '
                  'loops are skipped.'},
    ],
}
