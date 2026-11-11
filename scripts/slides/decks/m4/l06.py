DECK = {
    'module': 4, 'lesson': 6,
    'doc': 'module-04-manhattan/lesson-06-the-challenge-of-turning',
    'title': 'The Challenge of Turning',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Break driving a path into two steps, turn then drive, as in Lesson 4-0',
             'Write `desired_heading(position, next_pos)`: coordinate change to heading 0 to 3',
             'Raise an error when a function cannot answer, and say why',
             'Design a turn: clockwise quarter turns, `(heading + 1) % 4`',
             'Describe how `drive_path` uses both to drive a whole path',
         ],
         'notes': '35 minutes, design on paper. Only one function is written today, '
                  'desired_heading(), and it runs on the desk. turn_to() and drive_path() are '
                  'designed here and written in Lesson 4-7. Resist jumping to the driving code.'},

        {'kind': 'figure', 'title': 'Decompose further, like 4-0',
         'figure': './decks/m4/fig/l06-decomp-1.svg',
         'caption': 'The whole problem, as in Lesson 4-0. What are its parts?',
         'notes': 'Four slides, one level each: click through as the class answers. Ask what the '
                  'parts are before each click.'},

        {'kind': 'figure', 'title': 'Decompose further, like 4-0',
         'figure': './decks/m4/fig/l06-decomp-2.svg',
         'caption': 'Lesson 4-0\'s split: the planner is built and tested. Now the driver.',
         'notes': 'Recap of 4-0. The planner is small enough to build and test in one go; the driver '
                  'still needs breaking down.'},

        {'kind': 'figure', 'title': 'Decompose further, like 4-0',
         'figure': './decks/m4/fig/l06-decomp-3.svg',
         'caption': 'Driving a planned path breaks into two steps at each intersection: turn to face '
                    'the next one, then drive to it.',
         'notes': 'Same move as 4-0, one level down. The robot has a heading and only drives forward, '
                  'so it has to turn to face each next intersection before it drives. Driving is '
                  'Module 2 line tracking, already built.'},

        {'kind': 'figure', 'title': 'Decompose further, like 4-0',
         'figure': './decks/m4/fig/l06-decomp-4.svg',
         'caption': 'And turning breaks into two: work out which way to face, then turn until facing it.',
         'notes': 'Today: write desired_heading() and test it on screen; design turn_to() and '
                  'drive_path() on paper. Lesson 4-7 writes them.'},

        {'kind': 'table', 'title': 'One change, four directions',
         'lead': 'Between **adjacent** intersections, either x changes by one **or** y changes by one. '
                 'Never both: that would be a diagonal.',
         'headers': ['Coordinate change', 'Direction', 'Heading number'],
         'widths': [4, 2.5, 2.5],
         'rows': [
             ['y +1 (up, away from you)', 'North', '0'],
             ['x +1 (right)', 'East', '1'],
             ['y −1 (down, toward you)', 'South', '2'],
             ['x −1 (left)', 'West', '3'],
         ],
         'size': 22,
         'callout': 'x increases by one, so the robot moves **East**: desired heading **1**. '
                    'Four `if` statements find which value changed and set the heading.',
         'tone': 'teal',
         'notes': 'The grid orientation (x first in the tuple, but North is +y, away from you) is the '
                  'number one confusion of this lesson. Draw it, point at it, quiz it. Read the callout as '
                  'the bridge to desired_heading(): one if per row of this table.'},

        {'kind': 'figure', 'title': 'Four neighbors, four headings',
         'figure': './decks/m4/fig/l06-headings-xy.svg',
         'caption': 'The coordinate change that reaches each neighbor, and its heading number. '
                    'Clockwise adds 1.',
         'notes': 'The lesson figure, with its card labels redrawn as plain text: the slide renderer '
                  'overlapped the bold letter and the "= 0" in the original. Get students standing '
                  'and turning clockwise a quarter at a time, calling out 0, 1, 2, 3, 0. The '
                  'kinesthetic bit cements the wrap. Odometer analogy: "...3, and one more is 0, not 4."'},

        {'kind': 'check',
         'question': 'The robot moves from (2,3) to (3,3). Which direction is that, and what heading number?',
         'options': ['North, heading 0', 'South, heading 2', 'East, heading 1', 'West, heading 3'],
         'answer': 2,
         'explanation': 'x went 2 → 3 (x +1) and y stayed 3. Increasing x means moving right across '
                        'the grid, which is East: heading 1.'},

        {'kind': 'code', 'title': 'Add to robot.py: the NAVIGATOR section',
         'lead': 'The last section of the file. Paste it above `RUN`, after the MANHATTAN PLANNER '
                 'section: the heading names, then the one function you write today.',
         'lead_h': 1.2,
         'code': '# ===== NAVIGATOR =====\n'
                 '# Drives a planned path. The MANHATTAN PLANNER section says\n'
                 '# WHERE to go (a list of intersections); this section works\n'
                 '# out which way to face at each one and does the driving with\n'
                 '# the LINE TRACKING functions. It is the only code that knows\n'
                 '# the robot\'s position and heading, and it hands both back.\n'
                 'HEADING_NAMES = ["N", "E", "S", "W"]    # HEADING_NAMES[2] -> "S"',
         'code_size': 19,
         'notes': 'The section comment sets up the whole module\'s split: the planner says where, the '
                  'navigator works out which way to face and drives. The function outline is on the '
                  'next slide; it goes straight under HEADING_NAMES.'},

        {'kind': 'code', 'title': 'Add to robot.py: desired_heading()',
         'code': 'def desired_heading(position, next_pos):\n'
                 '    """Return the heading (0-3) that points from position to\n'
                 '    next_pos, which must be one step away; raise if it is not."""\n'
                 '    # 1. x_diff and y_diff: next_pos minus position\n'
                 '    # 2. one if per direction, from the table above; each\n'
                 '    #    checks BOTH differences, because the other one is 0\n'
                 '    # 3. none matched: raise ValueError, naming both positions\n'
                 '    pass',
         'code_size': 19,
         'callout': 'Step 2 is the table as four `if` lines. North means y went up by one **and** '
                    'x didn\'t move at all: the "one change at a time" rule, written down.',
         'tone': 'teal',
         'notes': 'Why both differences: a version that checks only one (if y_diff == 1: '
                  'return 0) looks equivalent and is not. From (2,1) to (3,3), x_diff is 1, so it '
                  'returns East and never reaches the raise. A check with a hole in it is worse than '
                  'no check. Good thing to show a fast finisher.'},

        {'kind': 'check',
         'question': 'Going from (1,3) to (1,2), what does `desired_heading` return?',
         'options': ['0 (North)', '1 (East)', '2 (South)', '3 (West)'],
         'answer': 2,
         'explanation': 'x is unchanged; y went 3 → 2 (y −1). Decreasing y is moving toward you, '
                        'which is South: heading 2.'},

        {'kind': 'code', 'title': 'Say so when you can\'t answer',
         'lead': 'None of the four matched? Then the positions aren\'t one step apart (diagonal, '
                 'identical, or across the map), and no heading answers that. `raise` is new: it '
                 'stops the program on the spot and prints your message.',
         'lead_h': 1.6, 'size': 25,
         'code': 'raise ValueError("what went wrong, in words")',
         'code_size': 26,
         'callout': '`ValueError` is Python\'s name for "the values I was given make no sense". The '
                    'message is yours: name both positions, with `str(position)` to turn a tuple into text.',
         'tone': 'teal',
         'notes': 'This is the debugging lesson, not a Python lesson. raise needs nothing beyond '
                  '"the program stops and prints your message"; students never write try/except to '
                  'benefit from it. Don\'t turn this into a detour on exception handling.'},

        {'kind': 'figure', 'title': 'Same bad input, two programs',
         'figure': '/img/lesson-m4-06/raise-spin.svg',
         'caption': 'Without the raise the program never even stops; with it, it stops where the '
                    'mistake is.',
         'notes': 'Top row: no match, the function silently returns None, turn_to waits forever for a '
                  'heading of None, and the robot spins with no message. Bottom row: ValueError at '
                  'desired_heading, turn_to never runs. Worth a few minutes: ask the class to predict '
                  'what they would see without the raise, and where they would look first (turn_to, '
                  'the one piece of code that is right).'},

        {'kind': 'bullets', 'title': 'Stop it at the door',
         'bullets': [
             'A wrong value that gets returned doesn\'t stay put',
             'It travels into the next function, and the next',
             'By the time anything visibly breaks, you\'re a long way from the mistake',
             'Every check like this shortens the distance between where a bug **shows up** '
             'and where it **actually is**',
         ],
         'callout': 'When a function is asked something it cannot answer, say so immediately and loudly.',
         'tone': 'green',
         'notes': 'First time the course asks students to write a line whose only job is to make a '
                  'future problem easier to find. Can the error actually happen? With '
                  'compute_manhattan_path feeding it, no: the planner only produces adjacent steps. '
                  'It becomes reachable when students call desired_heading themselves (the diagonal '
                  'call in test_headings does, on purpose) or in their own project in Lesson 4-8.'},

        {'kind': 'check',
         'question': 'Why does `desired_heading` end with `raise`, instead of just letting Python return `None`?',
         'options': ['Because None uses more memory',
                     'To stop at the line that found the problem, not break later somewhere else',
                     'Because every Python function has to end with raise',
                     'To make the robot turn faster'],
         'answer': 1,
         'explanation': 'Without it, desired_heading hands back None, turn_to waits forever for a '
                        'heading of None, and the robot spins in correct code with nothing printed. '
                        'Raising reports the problem where it was found.'},

        {'kind': 'steps', 'title': 'Activity · Write it, then ask it the four questions',
         'steps': [
             'Write the body of `desired_heading()` from the outline',
             'Write a paper test, `test_headings()`, that prints the heading from `(1, 1)` to each '
             'neighbor: `(0, 1)`, `(1, 2)`, `(2, 1)` and `(1, 0)`',
             'Work out the four answers from the table **before** you run it',
             'Print `HEADING_NAMES[...]` of each result next to the number. Set the run line to '
             '`test_headings()`: the robot stays on the desk',
         ],
         'size': 20,
         'notes': 'The check for desired_heading is a closed reveal on the lesson page; students run '
                  'test_headings() first. Push them to predict all four on paper before running.'},

        {'kind': 'steps', 'title': 'Activity · Then ask it a question it can\'t answer',
         'start': 5,
         'steps': [
             'Add one more call at the **end** of the test: `(1, 1)` to `(2, 2)`, a diagonal',
             'Run it again. The four answers print, then the program **stops** with your message',
             'Read the message: does it name **both** positions?',
         ],
         'callout': 'Why the diagonal goes last: nothing after the raise runs',
         'tone': 'teal',
         'notes': 'This is the raise doing its job, on purpose, in a test.'},

        {'kind': 'code', 'title': 'Turning until you face it',
         'lead': 'Like every sensor loop in Module 2: keep doing something until a condition is true. '
                 'One clockwise quarter turn, until you face the heading you want.',
         'lead_h': 1.2,
         'code': '# while heading is not desired:\n'
                 '#     one turn_clockwise()\n'
                 '#     heading goes up by 1, wrapping 3 back to 0\n'
                 '\n'
                 'heading = (heading + 1) % 4',
         'code_size': 24, 'width': 10,
         'callout': '`%` is the remainder (Lesson 2-5). For 1, 2 and 3 the remainder is the number '
                    'itself; `4 % 4` is 0, so after West comes North, never a heading 4.',
         'tone': 'teal',
         'notes': 'The top three lines are the loop design; the last line is the wrap, the odometer '
                  'in one expression.'},

        {'kind': 'table', 'title': 'Trace it: from South (2) to East (1)',
         'headers': ['Pass', 'Heading before', 'Turn', 'Heading after, `(h + 1) % 4`', 'Facing East?'],
         'widths': [1, 2.2, 1.8, 3.4, 2.6],
         'rows': [
             ['1', '2 (S)', 'clockwise', '3 (W)', 'no'],
             ['2', '3 (W)', 'clockwise', '0 (N)', 'no'],
             ['3', '0 (N)', 'clockwise', '1 (E)', 'yes, the loop ends'],
         ],
         'size': 22,
         'callout': 'Three passes. The loop never asks which way is shorter: from South it spins three '
                    'quarters round to face what is a quarter turn to its **left**.',
         'tone': 'orange',
         'notes': 'The long way round is on purpose: it is the simplest turn that always works. In '
                  'Lesson 4-7 students watch the robot spin 270 degrees, and an optional challenge '
                  'there makes it turn whichever way is fewer turns. If someone spots the problem '
                  'today, agree and point them at that challenge. An earlier version taught '
                  'turns = (desired - heading) % 4, which leans on % with a negative number '
                  '(-1 % 4 is 3) and surprises nearly everyone.'},

        {'kind': 'bullets', 'title': 'The design of turn_to(heading, desired)',
         'bullets': [
             'Already facing the right way? The condition is false on the first check, so the loop '
             'does nothing: **no special case**',
             '`turn_clockwise()` is the Module 2 function that turns until the sensors find the next line',
             'It returns `heading` at the end, which by then equals `desired`',
             'So the caller writes `heading = turn_to(heading, needed)` and keeps its own record up to date',
         ],
         'callout': 'You write it next lesson.',
         'tone': 'teal',
         'notes': 'Three sensor-ended turns take three times as long as one and give the line sensors '
                  'three chances to miss. That is the reason the optional challenge in 4-7 is worth '
                  'doing for those who want it.'},

        {'kind': 'check',
         'question': 'The robot faces West (3) and makes one clockwise turn. What does `(heading + 1) % 4` give?',
         'options': ['4', '0, North: 4 % 4 is 0, so the heading wraps around',
                     '3, because West is the last heading', 'An error, because there is no heading 4'],
         'answer': 1,
         'explanation': '3 + 1 is 4, and the remainder of 4 divided by 4 is 0. One clockwise turn from '
                        'West faces North, and the heading never becomes 4.'},

        {'kind': 'code', 'title': 'Preview · drive_path, next lesson',
         'lead': 'For each intersection: work out the heading, turn to it, drive one, update position.',
         'lead_h': 0.7,
         'code': 'def drive_path(path, position, heading):\n'
                 '    """Turn and drive through every intersection in path, from\n'
                 '    position facing heading; return the final (position, heading)."""\n'
                 '    # for each next_pos in path:\n'
                 '    #     1. needed = desired_heading(position, next_pos)\n'
                 '    #     2. heading = turn_to(heading, needed)\n'
                 '    #     3. drive to the next intersection (LINE TRACKING)\n'
                 '    #     4. position = next_pos -- the robot is there now\n'
                 '    # return position, heading\n'
                 '    pass',
         'code_size': 19,
         'callout': '`position` and `heading` update every step. Otherwise the next `desired_heading` '
                    'compares against the wrong spot.',
         'tone': 'teal',
         'notes': 'A preview, not an activity: students trace and write it in Lesson 4-7. '
                  'Step 3 is track_to_intersection(), the Module 2 function that follows the line '
                  'until both sensors hit a crossing: the robot drives exactly one intersection '
                  'without measuring distance. It returns position and heading because the caller '
                  'will plan the next path from wherever the robot ended up. Lesson 4-7 adds one '
                  'real-world wrinkle to step 3.'},

        {'kind': 'check',
         'question': 'Why must `drive_path` update `position` after each step?',
         'options': ['To make the robot faster',
                     'So the next desired_heading() compares against the correct current position',
                     'To reset the heading to North',
                     'It doesn\'t matter: position is never used again'],
         'answer': 1,
         'explanation': 'desired_heading works from the difference between current and next. If '
                        'position isn\'t updated, every step after the first computes the wrong direction.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Aviation', 'Compass headings', 'Pilots fly numbered headings (0 to 360°). "Turn to '
                                              'heading 090" is exactly this idea at finer resolution.'),
             ('Games', 'Facing and rotation', 'Game characters store a facing direction and rotate '
                                              'toward targets, often with the same wrap-around math.'),
             ('Robotics', 'Rovers and drones', 'Every autonomous vehicle tracks its heading to know '
                                               'which way "forward" actually points.'),
         ],
         'notes': 'Tracking heading and turning to a target direction is core to real navigation.'},

        {'kind': 'wrapup',
         'questions': [
             'Between adjacent intersections, what can change, and how many cases result?',
             'Why store heading as a number?',
             'How does `turn_to` know when to stop?',
         ],
         'next': 'driving the path: turn_to() and drive_path() become real code',
         'notes': 'Answers: x or y, four cases. Each clockwise turn adds 1, and % 4 wraps 4 back to 0. '
                  'Its loop runs until the heading equals the one it wants; already facing it means '
                  'zero turns. Exit ticket: "Heading 3 '
                  '(W), desired 1 (E): which headings does the loop step through, and how many '
                  'turns?" (W, N, E: two clockwise turns, a turn-around.)'},
    ],
}
