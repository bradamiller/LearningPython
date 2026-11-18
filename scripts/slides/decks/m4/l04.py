"""Module 4, Lesson 4-4 · The Driver."""

DECK = {
    'module': 4, 'lesson': 4,
    'doc': 'module-04-manhattan/lesson-04-the-driver',
    'title': 'The Driver',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Break driving a path into two steps at each intersection: turn, then drive',
             'Read one item of a list or one part of a tuple by its index, counting from 0',
             'Loop over a list\'s indexes with `range(len(...))`',
             'Write `get_desired_heading(position, next_pos)`, which turns a one-step move into a '
             'heading (0 = N, 1 = E, 2 = S, 3 = W)',
             'Write the real `drive_path()` loop, with stubs for turning and driving',
             '(Optional) Catch a mistake early by raising an error when a function is asked '
             'something it can\'t answer',
         ],
         'notes': '55 to 65 minutes, robot on the desk. The planner is real; now the driver stub '
                  'goes. At each intersection the robot turns to face the next one, then drives to '
                  'it. Turning and driving stay stubs, so every move shows up as printed lines. '
                  'Indexing and range(len(...)) are new here; Module 5 numbers the legs of a run '
                  'with the same loop. Every step of the activity is predict, run, compare.'},

        {'kind': 'figure', 'title': 'Today: the driver\'s half of the tree',
         'figure': './decks/m4/fig/topdown-decomp-4.svg',
         'caption': 'drive_path() and get_desired_heading() today. Turning is Lesson 4-5; driving '
                    'on the tape is 4-6.'},

        {'kind': 'table', 'title': 'Heading is a number',
         'lead': 'Since Lesson 4-1 the program has carried a `robot_heading` that never changed. '
                 'Numbered clockwise from North:',
         'headers': ['Heading', '0', '1', '2', '3'],
         'widths': [2, 1.5, 1.5, 1.5, 1.5],
         'rows': [['Direction', 'North', 'East', 'South', 'West']],
         'row_h': 0.6,
         'callout': 'Easy to do arithmetic on (a clockwise quarter turn adds 1), but `0` in a '
                    'printout is hard to read',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'This lesson\'s skeleton (1 of 2)',
         'code': 'HEADING_NAMES = ["N", "E", "S", "W"]    # HEADING_NAMES[2] -> "S"\n'
                 '\n'
                 'def get_desired_heading(position, next_pos):\n'
                 '    # 1. unpack position into x, y and next_pos into\n'
                 '    #    next_x, next_y\n'
                 '    # 2. one if per row of the table, each returning its\n'
                 '    #    heading. North is: if next_y > y: return 0\n'
                 '    # 3. (optional) none matched: raise ValueError, naming\n'
                 '    #    both positions -- see "Catching mistakes early"\n'
                 '    pass\n'
                 '\n'
                 'def test_headings():\n'
                 '    for next_pos in [(0, 1), (1, 2), (2, 1), (1, 0)]:\n'
                 '        heading = get_desired_heading((1, 1), next_pos)\n'
                 '        print("(1, 1) to", next_pos, ":", heading, HEADING_NAMES[heading])',
         'code_size': 18,
         'notes': 'These go above the drive_path() function, with the two stubs on the next slide. '
                  'The slide leaves out the docstring to fit; students copy the block from the '
                  'lesson page.'},

        {'kind': 'code', 'title': 'This lesson\'s skeleton (2 of 2)',
         'code': 'def turn_to(current_heading, desired_heading):\n'
                 '    print("turning: from", HEADING_NAMES[current_heading],\n'
                 '          "to:", HEADING_NAMES[desired_heading])\n'
                 '    return desired_heading\n'
                 '\n'
                 'def fake_track_to_intersection():\n'
                 '    print("tracking to intersection")',
         'code_size': 20,
         'callout': 'Stubs print what the real function will do: turning is Lesson 4-5, the tape '
                    'is 4-6',
         'tone': 'orange',
         'notes': 'Two new stubs, shown without their docstrings.'},

        {'kind': 'code', 'title': 'Fill in drive_path()',
         'code': 'def drive_path(path, current_position, current_heading):\n'
                 '    for next_pos in path:\n'
                 '        # 1. desired_heading: which way to face next_pos\n'
                 '        # 2. print("moving: from", current_position, "to:", next_pos,\n'
                 '        #          "heading:", HEADING_NAMES[desired_heading])\n'
                 '        # 3. turn: current_heading = turn_to(...)\n'
                 '        # 4. drive there: fake_track_to_intersection()\n'
                 '        current_position = next_pos     # the robot is there now\n'
                 '    return current_position, current_heading',
         'code_size': 17,
         'callout': 'Also: the `new position:` print in `test_delivery()` now shows '
                    '`HEADING_NAMES[robot_heading]`',
         'tone': 'teal',
         'notes': 'The loop gets four new steps, and the docstring changes (on the lesson page; '
                  'left out here to fit). Students fill the steps in during Step 3.'},

        # Step 1
        {'kind': 'code', 'title': 'Step 1 · A heading\'s letter, by index', 'tag': 'Activity',
         'lead': 'Every item in a list has an **index**, counting from **0**. Square brackets '
                 'after the name pick one item out. Type these into the shell:',
         'lead_h': 1.2,
         'code': 'HEADING_NAMES = ["N", "E", "S", "W"]\n'
                 'print(HEADING_NAMES[0])\n'
                 'print(HEADING_NAMES[2])\n'
                 'heading = 3\n'
                 'print(HEADING_NAMES[heading])',
         'code_size': 22,
         'callout': '**Predict:** what does each `print` show?',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Step 1 · Check your output', 'tag': 'Activity',
         'code': 'N\n'
                 'S\n'
                 'W',
         'code_size': 24,
         'callout': 'The headings were numbered 0 to 3 so that a heading **is** the index of its '
                    'own letter',
         'tone': 'green',
         'notes': 'The heading-is-its-own-index trick is worth saying out loud.'},

        {'kind': 'code', 'title': 'Step 1 · Every index, in order', 'tag': 'Activity',
         'lead': '`len()` is how many items there are; `range()` counts from 0 up to one less:',
         'code': 'for i in range(len(HEADING_NAMES)):\n'
                 '    print(i, HEADING_NAMES[i])',
         'code_size': 24,
         'callout': '**Predict:** what does it print?',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Step 1 · Check your output', 'tag': 'Activity',
         'code': '0 N\n'
                 '1 E\n'
                 '2 S\n'
                 '3 W',
         'code_size': 24,
         'callout': 'Four items, indexes 0 to 3. Now try `HEADING_NAMES[4]`: there is no fifth '
                    'item, so Python stops with an `IndexError`.',
         'tone': 'green',
         'notes': 'Have students actually try HEADING_NAMES[4] in the shell so IndexError isn\'t a '
                  'surprise later.'},

        {'kind': 'bullets', 'title': 'A tuple is indexed the same way',
         'bullets': [
             'For a position, `next_pos[0]` is x and `next_pos[1]` is y',
             'This program still **unpacks** positions, as the planner does, because it usually '
             'wants both numbers',
         ],
         'size': 28},

        {'kind': 'check',
         'question': 'What does this print? `path = [(1, 0), (2, 0), (2, 1)]`, then '
                     '`last = path[2]`, then `print(last[1])`',
         'options': ['`(2, 0)`', '`1`', '`2`', 'An IndexError'],
         'answer': 1,
         'explanation': 'Indexes count from 0, so path[2] is the third item, (2, 1). Then last[1] is '
                        'its second part, y: 1.'},

        # Step 2
        {'kind': 'figure', 'title': 'Step 2 · Which way to face?', 'tag': 'Activity',
         'figure': './decks/m4/fig/l05-headings-xy.svg',
         'caption': 'Between adjacent intersections, x or y changes by one. **North is away from '
                    'you**, so moving North makes y bigger.',
         'notes': 'Four cases: y + 1 is North (0), x + 1 East (1), y - 1 South (2), x - 1 West (3). '
                  'The grid orientation is the number one confusion: x comes first in the tuple, but '
                  'North and South change the second number. Draw it, point at it, quiz it.'},

        {'kind': 'steps', 'title': 'Step 2 · get_desired_heading()',
         'tag': 'Activity',
         'steps': [
             'Write the body from its outline: one `if` per row of the table',
             '**Predict:** the four headings `test_headings()` prints, from (1, 1) to (0, 1), '
             '(1, 2), (2, 1) and (1, 0)',
             'Set the run line to `test_headings()` and run it',
         ],
         'notes': 'The four if lines trust the planner\'s promise that every step is to a neighbor, '
                  'which test_planner() already checked.'},

        {'kind': 'code', 'title': 'Step 2 · Check your output', 'tag': 'Activity',
         'code': '(1, 1) to (0, 1) : 3 W\n'
                 '(1, 1) to (1, 2) : 0 N\n'
                 '(1, 1) to (2, 1) : 1 E\n'
                 '(1, 1) to (1, 0) : 2 S',
         'code_size': 24,
         'callout': '(0, 1) is one step left of (1, 1), so it\'s West',
         'tone': 'green'},

        {'kind': 'code', 'title': 'Step 2 · Check your function', 'tag': 'Activity',
         'code': 'def get_desired_heading(position, next_pos):\n'
                 '    x, y = position\n'
                 '    next_x, next_y = next_pos\n'
                 '    if next_y > y: return 0   # North\n'
                 '    if next_x > x: return 1   # East\n'
                 '    if next_y < y: return 2   # South\n'
                 '    if next_x < x: return 3   # West',
         'code_size': 22,
         'notes': 'The slide leaves out the docstring. Laid out differently and printing the same '
                  'four lines is fine.'},

        {'kind': 'check',
         'question': 'The robot moves from (2, 3) to (3, 3). Which direction is that, and what '
                     'heading?',
         'options': ['North, heading 0', 'South, heading 2', 'East, heading 1', 'West, heading 3'],
         'answer': 2,
         'explanation': 'x went 2 to 3 (x +1) and y stayed 3. Increasing x is moving right, East: '
                        'heading 1.'},

        # Step 3
        {'kind': 'figure', 'title': 'Step 3 · The drive_path() loop', 'tag': 'Activity',
         'figure': '/img/lesson-m4-04/drive-path-steps.svg',
         'caption': 'Leg 1, one pass per intersection: work out the heading, turn to face it, '
                    'drive there.',
         'notes': 'Pass 1: (1, 0), East: turn and drive. Pass 2: (2, 0), East again: no turn. '
                  'Pass 3: (2, 1), North: turn and drive. Passes 4 and 5: North, no turn. '
                  'drive_path() returns (2, 3) and heading 0. The animation draws each turn the '
                  'short way; the turn_to() stub just hands back the heading it was asked for, and '
                  'how the robot really gets there is Lesson 4-5.'},

        {'kind': 'steps', 'title': 'Step 3 · The drive_path() loop',
         'tag': 'Activity',
         'steps': [
             'Fill in steps 1 to 4 of the loop. `turn_to()` hands back the new heading, so step 3 '
             'keeps `current_heading` up to date.',
             'Leg 1\'s letters are E, E, N, N, N. **Predict:** Leg 2\'s letters, from (2, 3) to '
             '(1, 0), and the last line of the run',
             'Set the run line to `test_delivery()` and run it',
         ],
         'notes': 'Step 3 of the loop keeps current_heading up to date the same way the main '
                  'program keeps robot_position up to date.'},

        {'kind': 'code', 'title': 'Step 3 · Check your drive_path()', 'tag': 'Activity',
         'code': 'def drive_path(path, current_position, current_heading):\n'
                 '    for next_pos in path:\n'
                 '        desired_heading = get_desired_heading(current_position, next_pos)\n'
                 '        print("moving: from", current_position, "to:", next_pos,\n'
                 '              "heading:", HEADING_NAMES[desired_heading])\n'
                 '        current_heading = turn_to(current_heading, desired_heading)\n'
                 '        fake_track_to_intersection()\n'
                 '        current_position = next_pos     # the robot is there now\n'
                 '    return current_position, current_heading',
         'code_size': 18,
         'notes': 'The slide leaves out the docstring.'},

        {'kind': 'code', 'title': 'Step 3 · Check your output', 'tag': 'Activity',
         'code': 'computing path from: (2, 3) to: (1, 0)\n'
                 '[(1, 3), (1, 2), (1, 1), (1, 0)]\n'
                 'moving: from (2, 3) to: (1, 3) heading: W\n'
                 'turning: from N to: W\n'
                 'tracking to intersection\n'
                 'moving: from (1, 3) to: (1, 2) heading: S\n'
                 'turning: from W to: S\n'
                 'tracking to intersection\n'
                 '...\n'
                 'new position: (0, 0) heading: S',
         'code_size': 18,
         'callout': 'Leg 2 is W, S, S, S. Each `turning:` starts from the heading the one before '
                    'ended on.',
         'tone': 'green',
         'notes': 'Trimmed to Leg 2 and the last line; the full printout is in the reveal on the '
                  'lesson page. Leg 1 ends new position: (2, 3) heading: N, so Leg 2\'s first turn '
                  'is from N. The last move of the run goes South.'},

        {'kind': 'check',
         'question': 'Going from (1, 3) to (1, 2), what does `get_desired_heading()` return?',
         'options': ['0 (North)', '1 (East)', '2 (South)', '3 (West)'],
         'answer': 2,
         'explanation': 'x is unchanged; y went 3 to 2 (y -1). Decreasing y is moving toward you: '
                        'South, heading 2.'},

        # Step 4
        {'kind': 'code', 'title': 'Step 4 · Break it on purpose', 'tag': 'Activity',
         'lead': 'In `drive_path()`, drop `current_heading =`, so the line is just:',
         'code': 'turn_to(current_heading, desired_heading)',
         'code_size': 24,
         'callout': '**Predict:** what will every `turning:` line start from? Then run it.',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Step 4 · What happened?', 'tag': 'Activity',
         'bullets': [
             'Every line says `turning: from N`, and every `new position:` line says `heading: N`',
             '`turn_to()` hands back the new heading, and nobody caught it: the dropped return '
             'from Lesson 4-1, one level down',
             'On the floor, the robot would think it still faced North and turn the wrong amount '
             'at every corner',
         ],
         'size': 24,
         'callout': 'Put `current_heading =` back and run it again',
         'tone': 'green'},

        {'kind': 'bullets', 'title': 'Optional: catching mistakes early',
         'tag': 'Optional',
         'bullets': [
             'If `next_pos` is the same spot as `position`, **none** of the four `if` lines is true',
             'That only happens with a planner bug: a path that includes the start',
             'Without a check the function returns `None`, and the program stops one line later with '
             'a confusing `TypeError`',
             'With `raise ValueError(...)` it stops **where the mistake was noticed**, naming both '
             'positions',
         ],
         'size': 22,
         'notes': 'raise needs no more teaching than "the program stops and prints your message"; '
                  'don\'t detour into try/except. The check catches a move that goes nowhere. A '
                  'diagonal or a two-block jump still gets a heading, because the four if lines only '
                  'ask which number changed; the planner\'s own tests rule those out. Try it: add '
                  'get_desired_heading((1, 1), (1, 1)) at the end of test_headings().'},

        {'kind': 'wrapup',
         'questions': [
             'What two steps happen at each intersection?',
             'Between adjacent intersections, what can change?',
             'What does `HEADING_NAMES[heading]` do?',
             'Why does `drive_path()` write `current_heading = turn_to(...)`?',
         ],
         'next': 'turning',
         'notes': 'Answers: turn to face the next one, then drive to it. x or y, by one: four cases, '
                  'four headings. It picks the item at that index, counting from 0: the heading\'s '
                  'letter. turn_to() hands back the new heading; assigning it is the only way '
                  'drive_path() keeps it.'},
    ],
}
