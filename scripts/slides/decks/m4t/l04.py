"""Module 4 test (top-down trial), Lesson 4-4 · The Driver."""

DECK = {
    'module': 4, 'lesson': 4, 'key': '4t-4', 'label': 'MODULE 4 TEST',
    'doc': 'test-module-04/lesson-04-the-driver',
    'title': 'The Driver',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Break driving a path into two steps at each intersection: turn, then drive',
             'Read one item of a list or one part of a tuple by its index, counting from 0',
             'Write `get_desired_heading(position, next_pos)`: a one-step move becomes a heading',
             'Write the real `drive_path()` loop, with stubs for turning and driving',
         ],
         'notes': '55 to 65 minutes, robot on the desk. The planner is real; now the driver stub '
                  'goes. At each intersection the robot turns to face the next one, then drives to '
                  'it. Turning and driving stay stubs, so every move shows up as printed lines. '
                  'Indexing is new here. Optional: raising an error when a function is asked '
                  'something it can\'t answer.'},

        {'kind': 'figure', 'title': 'Today: the driver\'s half of the tree',
         'figure': './decks/m4t/fig/topdown-decomp-4.svg',
         'caption': 'drive_path() and get_desired_heading() today. Turning is Lesson 4-5; driving '
                    'on the tape is 4-6.'},

        {'kind': 'table', 'title': 'Heading is a number',
         'lead': 'Since Lesson 4-1 the program has carried a `robot_heading` that never changed. '
                 'Numbered clockwise from North:',
         'headers': ['Heading', '0', '1', '2', '3'],
         'widths': [2, 1.5, 1.5, 1.5, 1.5],
         'rows': [['Direction', 'North', 'East', 'South', 'West']],
         'row_h': 0.6,
         'callout': 'Easy to do arithmetic on (a clockwise turn adds 1), but `0` in a printout is '
                    'hard to read',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Picking one item: indexing',
         'code': 'HEADING_NAMES = ["N", "E", "S", "W"]\n'
                 '\n'
                 'print(HEADING_NAMES[0])    # N\n'
                 'print(HEADING_NAMES[2])    # S\n'
                 'heading = 3\n'
                 'print(HEADING_NAMES[heading])    # W',
         'code_size': 22,
         'callout': 'Every item has an **index**, counting from 0. A heading **is** the index of its '
                    'own letter.',
         'tone': 'teal',
         'notes': 'The heading-is-its-own-index trick is worth saying out loud. Try HEADING_NAMES[4] '
                  'once in the shell so IndexError isn\'t a surprise later.'},

        {'kind': 'code', 'title': 'A tuple is indexed the same way',
         'code': 'next_pos = (2, 3)\n'
                 'print(next_pos[0])    # 2 -> x\n'
                 'print(next_pos[1])    # 3 -> y',
         'code_size': 24,
         'callout': 'For a position you usually want both numbers, so this program keeps '
                    '**unpacking**. Indexing picks one item out of many.',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'What does this print? `path = [(1, 0), (2, 0), (2, 1)]`, then '
                     '`last = path[2]`, then `print(last[1])`',
         'options': ['`(2, 0)`', '`1`', '`2`', 'An IndexError'],
         'answer': 1,
         'explanation': 'Indexes count from 0, so path[2] is the third item, (2, 1). Then last[1] is '
                        'its second part, y: 1.'},

        {'kind': 'figure', 'title': 'Which way to face?',
         'figure': './decks/m4/fig/l05-headings-xy.svg',
         'caption': 'Between adjacent intersections, x or y changes by one. **North is away from '
                    'you**, so moving North makes y bigger.',
         'notes': 'Four cases: y + 1 is North (0), x + 1 East (1), y - 1 South (2), x - 1 West (3). '
                  'The grid orientation is the number one confusion: x comes first in the tuple, but '
                  'North and South change the second number. Draw it, point at it, quiz it.'},

        {'kind': 'check',
         'question': 'The robot moves from (2, 3) to (3, 3). Which direction is that, and what '
                     'heading?',
         'options': ['North, heading 0', 'South, heading 2', 'East, heading 1', 'West, heading 3'],
         'answer': 2,
         'explanation': 'x went 2 to 3 and y stayed 3. Increasing x is moving right, East: '
                        'heading 1.'},

        {'kind': 'bullets', 'title': 'get_desired_heading(position, next_pos)',
         'bullets': [
             'Unpack both positions, as the planner did',
             'Find the **one number that changed**',
             'Four `if` lines, one per row of the table',
             ['`next_y > y`: North', '`next_x > x`: East', 'the same with **smaller** for South and '
              'West'],
         ],
         'size': 26,
         'notes': 'No subtraction and no and: the function trusts the planner\'s promise, already '
                  'tested in 4-3, that every step is to a neighbor.'},

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
         'code_size': 14,
         'notes': 'These go above the drive_path() function, with the two stubs on the next slide. '
                  'The slide leaves out the docstring to fit; students copy the block from the '
                  'lesson page.'},

        {'kind': 'code', 'title': 'This lesson\'s skeleton (2 of 2): two new stubs',
         'code': 'def turn_to(current_heading, desired_heading):\n'
                 '    print("turning: from", HEADING_NAMES[current_heading],\n'
                 '          "to:", HEADING_NAMES[desired_heading])\n'
                 '    return desired_heading\n'
                 '\n'
                 'def fake_track_to_intersection():\n'
                 '    print("tracking to intersection")',
         'code_size': 18,
         'callout': 'Stubs print what the real function will do: turning is Lesson 4-5, the tape '
                    'is 4-6',
         'tone': 'orange'},

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
         'code_size': 15,
         'callout': 'Also: the `new position:` print in `test_delivery()` now shows '
                    '`HEADING_NAMES[robot_heading]`',
         'tone': 'teal',
         'notes': 'turn_to() hands back the new heading, so step 3 keeps current_heading up to date '
                  'the same way the main program keeps robot_position up to date.'},

        {'kind': 'steps', 'title': 'Step 1 · get_desired_heading()',
         'tag': 'Activity',
         'steps': [
             'Work out the four answers from the table first: (1, 1) to (0, 1), (1, 2), (2, 1) and '
             '(1, 0)',
             'Write the body from the outline',
             'Set the run line to `test_headings()` and run it',
         ],
         'callout': 'Correct: four lines whose numbers and letters match your answers',
         'tone': 'green',
         'notes': 'The answers come out 3, 0, 1, 2: W, N, E, S. (0, 1) is one step left, so it\'s '
                  'West. The finished function is behind a reveal on the lesson page.'},

        {'kind': 'steps', 'title': 'Step 2 · The drive_path() loop',
         'tag': 'Activity',
         'steps': [
             'Fill in steps 1 to 4 of the loop',
             'Set the run line to `test_delivery()` and run it',
         ],
         'callout': 'Correct: one `moving:` line per step, then `turning:` and `tracking to '
                    'intersection`. Leg 1 is E, E, N, N, N. The run ends heading S.',
         'tone': 'green',
         'notes': 'Each turning: line starts from the heading the one before it ended on. A student '
                  'whose every turning: line starts from N forgot current_heading = turn_to(...): '
                  'the same dropped return as Lesson 4-1, one level down. The full printout is '
                  'behind a reveal on the lesson page.'},

        {'kind': 'check',
         'question': 'Going from (1, 3) to (1, 2), what does `get_desired_heading()` return?',
         'options': ['0 (North)', '1 (East)', '2 (South)', '3 (West)'],
         'answer': 2,
         'explanation': 'x is unchanged; y went 3 to 2. Decreasing y is moving toward you: South, '
                        'heading 2.'},

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
