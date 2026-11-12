DECK = {
    'module': 4, 'lesson': 5,
    'doc': 'module-04-manhattan/lesson-05-the-challenge-of-turning',
    'title': 'The Challenge of Turning',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Break driving a path into two steps, turn then drive, as in Lesson 4-0',
             'Write `get_desired_heading(position, next_pos)`: coordinate change to heading 0 to 3, '
             'and test it on screen',
             '(Optional) Catch a mistake early by raising an error when a function cannot answer',
             'Design a turn: clockwise quarter turns, `(heading + 1) % 4`',
         ],
         'notes': '30 minutes, design on paper. Only one function is written today, '
                  'get_desired_heading(), and it runs on the desk. turn_to() is designed here; '
                  'Lesson 4-6 writes it and drive_path(). Resist jumping to the driving code.'},

        {'kind': 'bullets', 'title': 'Facing the right way',
         'bullets': [
             'The robot drives over a list of intersections, one to the next',
             'Somewhere in that list the path turns: that\'s the corner of the "L"',
             'So before it drives from one intersection to the next, the robot has to be '
             '**facing the right way**',
         ],
         'callout': 'That\'s what this lesson is about.',
         'tone': 'teal',
         'notes': 'The lesson opens here: the planner hands the driver a list of intersections, and '
                  'the path bends at the corner of the L, so the robot has to face each next '
                  'intersection before it drives to it.'},

        {'kind': 'figure', 'title': 'Decompose further, like 4-0',
         'figure': './decks/m4/fig/l05-decomp-1.svg',
         'caption': 'The whole problem, as in Lesson 4-0. What are its parts?',
         'notes': 'Four slides, one level each: click through as the class answers. Ask what the '
                  'parts are before each click.'},

        {'kind': 'figure', 'title': 'Decompose further, like 4-0',
         'figure': './decks/m4/fig/l05-decomp-2.svg',
         'caption': 'Lesson 4-0\'s split: the planner is built and tested. Now the driver.',
         'notes': 'Recap of 4-0. The planner is small enough to build and test in one go; the driver '
                  'still needs breaking down.'},

        {'kind': 'figure', 'title': 'Decompose further, like 4-0',
         'figure': './decks/m4/fig/l05-decomp-3.svg',
         'caption': 'Driving a planned path breaks into two steps at each intersection: turn to face '
                    'the next one, then drive to it.',
         'notes': 'Same move as 4-0, one level down. The robot has a heading and only drives forward, '
                  'so it has to turn to face each next intersection before it drives. Driving is '
                  'Module 2 line tracking, already built.'},

        {'kind': 'figure', 'title': 'Decompose further, like 4-0',
         'figure': './decks/m4/fig/l05-decomp-4.svg',
         'caption': 'And turning breaks into two: work out which way to face, then turn until facing it.',
         'notes': 'Today: write get_desired_heading() and test it on screen; design turn_to() on paper. '
                  'Lesson 4-6 writes it and drive_path().'},

        {'kind': 'bullets', 'title': 'Where we are',
         'bullets': [
             'The robot has an `(x, y)` position and a **heading** (0 = North, 1 = East, 2 = South, '
             '3 = West). Together they are the robot\'s **pose**',
             'The robot only moves in the direction it is facing, and only one intersection at a time',
             'Every clockwise turn adds one to the heading, and every counterclockwise turn subtracts '
             'one. If the heading hits 4, it wraps around to 0; if it goes below 0, it wraps around to 3',
         ],
         'notes': 'A recap before the new work: position plus heading is the pose, the robot moves one '
                  'intersection at a time in the direction it faces, and the heading wraps both ways.'},

        {'kind': 'bullets', 'title': 'One change at a time',
         'bullets': [
             'We need a function that gives the **desired heading** to reach the next intersection: '
             '`get_desired_heading()`. You write it in this lesson',
             'For every move, the robot has to decide which way to go',
             'That decision depends on its **current position** and the desired, or **next**, '
             'position on the path',
         ],
         'notes': 'This sets up the function students write today, before the table that defines it.'},

        {'kind': 'table', 'title': 'One change, four directions',
         'lead': 'Between **adjacent** intersections, either x changes by one **or** y changes by one. '
                 'Never both: that would be a diagonal.',
         'headers': ['Coordinate change', 'Desired heading', 'Heading number'],
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
                  'the bridge to get_desired_heading(): one if per row of this table.'},

        {'kind': 'figure', 'title': 'Four neighbors, four headings',
         'figure': './decks/m4/fig/l05-headings-xy.svg',
         'caption': 'The coordinate change that reaches each neighbor, and its heading number. '
                    'Clockwise adds 1.',
         'notes': 'The lesson figure, with its card labels redrawn as plain text: the slide renderer '
                  'overlapped the bold letter and the "= 0" in the original. Get students standing '
                  'and turning clockwise a quarter at a time, calling out 0, 1, 2, 3, 0. The '
                  'kinesthetic bit cements the wrap. The numbers count clockwise from North, so each '
                  'clockwise turn adds 1. Adding 1 isn\'t enough from West to North: 3 + 1 is 4, and 4 '
                  'isn\'t a heading. It has to wrap back to 0.'},

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

        {'kind': 'code', 'title': 'Add to robot.py: get_desired_heading()',
         'code': 'def get_desired_heading(position, next_pos):\n'
                 '    """Return the heading (0-3) that points from position to\n'
                 '    next_pos, which must be one step away."""\n'
                 '    # 1. x_diff and y_diff: next_pos minus position\n'
                 '    # 2. one if per direction, from the table above; each\n'
                 '    #    checks BOTH differences, because the other one is 0\n'
                 '    # 3. (optional) none matched: raise ValueError, naming\n'
                 '    #    both positions -- see "Catching mistakes early"\n'
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
         'question': 'Going from (1,3) to (1,2), what does `get_desired_heading` return?',
         'options': ['0 (North)', '1 (East)', '2 (South)', '3 (West)'],
         'answer': 2,
         'explanation': 'x is unchanged; y went 3 → 2 (y −1). Decreasing y is moving toward you, '
                        'which is South: heading 2.'},

        {'kind': 'bullets', 'title': 'Optional: catching mistakes early',
         'tag': 'Optional extension',
         'bullets': [
             'A good program catches its own mistakes early',
             '`get_desired_heading()` only makes sense when the next intersection is **adjacent** '
             'to the current one, one step away',
             'If none of the four `if` lines matched, the two positions aren\'t neighbors and there '
             'is no right answer',
         ],
         'callout': '**When would that happen?** Make a guess first.',
         'tone': 'teal',
         'notes': 'Optional: open it if you have time. Nothing later depends on it. Answer to the '
                  'question (a closed reveal on the page): only when there\'s a bug in the planner. A '
                  'correct planner only ever lists adjacent steps, so a pair that isn\'t adjacent means '
                  'the path itself is wrong.'},

        {'kind': 'code', 'title': 'Optional: stop at once, and say why',
         'tag': 'Optional extension',
         'lead': 'Without a check, `get_desired_heading()` quietly returns `None`, `turn_to` waits forever '
                 'for a heading of `None`, and the robot spins with no message. With a check, the program '
                 'stops at once and says which two positions caused it:',
         'lead_h': 1.6, 'size': 23,
         'code': 'raise ValueError(str(position) + " and " + str(next_pos) + " are not neighbors")',
         'code_size': 18,
         'callout': '`raise` stops the program on the spot and prints your message. `ValueError` is Python\'s '
                    'name for "the values I was given make no sense". `str(position)` turns a tuple into text.',
         'callout_size': 19,
         'tone': 'teal',
         'notes': 'raise is new here, but nothing about it needs teaching beyond "the program stops and '
                  'prints your message"; students never write try/except to benefit from it. Don\'t turn '
                  'this into a detour on exception handling. The code that\'s spinning without the check '
                  'isn\'t even the code that\'s wrong.'},

        {'kind': 'figure', 'title': 'Same bad input, two programs',
         'tag': 'Optional extension',
         'figure': '/img/lesson-m4-05/raise-spin.svg',
         'caption': 'Without the raise the program never even stops; with it, it stops where the '
                    'mistake is.',
         'notes': 'Top row: no match, the function silently returns None, turn_to waits forever for a '
                  'heading of None, and the robot spins with no message. Bottom row: ValueError at '
                  'get_desired_heading, turn_to never runs. Worth ten minutes: ask the class to predict '
                  'what they would see without the raise, and how they would go about finding the cause '
                  '("a robot spinning forever, and the first place you\'d look is the one piece of code '
                  'that\'s right"). This is the first time the course asks students to write a line whose '
                  'only job is to make a future problem easier to find.'},

        {'kind': 'check',
         'question': 'Why end `get_desired_heading` with `raise`, instead of just letting Python return `None`?',
         'options': ['Because None uses more memory',
                     'To stop at the line that found the problem, not break later somewhere else',
                     'Because every Python function has to end with raise',
                     'To make the robot turn faster'],
         'answer': 1,
         'explanation': 'Without it, get_desired_heading hands back None, turn_to waits forever for a '
                        'heading of None, and the robot spins in correct code with nothing printed. '
                        'Raising reports the problem where it was found.'},

        {'kind': 'steps', 'title': 'Optional · Try it',
         'tag': 'Optional extension',
         'steps': [
             'Add step 3 to `get_desired_heading()`',
             'Add one more call at the **end** of `test_headings()`: `(1, 1)` to `(2, 2)`, a diagonal',
             'Run it. The four answers print as before, then the program **stops** with your message, '
             'naming both positions',
         ],
         'callout': 'Why the diagonal goes last: nothing after it runs',
         'tone': 'teal',
         'notes': 'This is the raise doing its job, on purpose, in a test.'},

        {'kind': 'steps', 'title': 'Activity · Write it, then ask it the four questions',
         'steps': [
             'Write the body of `get_desired_heading()` from the outline',
             'Write a paper test, `test_headings()`. It calls `get_desired_heading()` from `(1, 1)` to '
             'each neighbor, `(0, 1)`, `(1, 2)`, `(2, 1)` and `(1, 0)`, and prints one line for each: the '
             'neighbor, the heading number, and its name from `HEADING_NAMES`',
             'Work out the four answers from the table **first**',
             'Set the run line to `test_headings()` and run it with the robot on the desk. Correct '
             'output is four lines that match your four answers',
         ],
         'size': 20,
         'notes': 'The check for get_desired_heading is a closed reveal on the lesson page; students run '
                  'test_headings() first. Push them to predict all four on paper before running.'},

        {'kind': 'code', 'title': 'Turning until you face it',
         'lead': 'Now we know both the current heading and the desired heading. So the robot can simply '
                 'turn clockwise, adding one to the heading for each turn, while it isn\'t facing the '
                 'desired heading.',
         'lead_h': 1.4,
         'code': '# while current_heading is not desired_heading:\n'
                 '#     one turn_clockwise()\n'
                 '#     current_heading goes up by 1, wrapping 3 back to 0\n'
                 '\n'
                 'heading = (heading + 1) % 4',
         'code_size': 24, 'width': 10,
         'callout': 'West (3) to North (0): the remainder `%` (Lesson 2-5) makes it easy. For 1, 2 and 3 '
                    'the remainder is the number itself; `4 % 4` is 0, so after West comes North.',
         'callout_size': 19,
         'tone': 'teal',
         'notes': 'The top three lines are the loop design; the last line is the wrap: when the robot '
                  'is facing West (3) and turns clockwise to North (0), % makes it easy, and the '
                  'heading is never 4.'},

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
                  'Lesson 4-6 students watch the robot spin 270 degrees, and an optional challenge '
                  'there makes it turn whichever way is fewer turns. If someone spots the problem '
                  'today, agree and point them at that challenge. An earlier version taught '
                  'turns = (desired_heading - current_heading) % 4, which leans on % with a negative number '
                  '(-1 % 4 is 3) and surprises nearly everyone.'},

        {'kind': 'bullets', 'title': 'The design of turn_to()',
         'bullets': [
             'Already facing the right way? The condition is false on the first check, so the loop '
             'does nothing: **no special case**',
             '`turn_clockwise()` is the Module 2 function that turns until the sensors find the next line',
             'It returns `current_heading` at the end, which by then equals `desired_heading`',
             'So the caller writes `heading = turn_to(heading, desired_heading)` and keeps its own '
             'record up to date',
         ],
         'callout': '`turn_to(current_heading, desired_heading)`: you write it next lesson.',
         'tone': 'teal',
         'notes': 'Three sensor-ended turns take three times as long as one and give the line sensors '
                  'three chances to miss. That is the reason the optional challenge in 4-6 is worth '
                  'doing for those who want it.'},

        {'kind': 'check',
         'question': 'The robot faces West (3) and makes one clockwise turn. What does `(heading + 1) % 4` give?',
         'options': ['4', '0, North: 4 % 4 is 0, so the heading wraps around',
                     '3, because West is the last heading', 'An error, because there is no heading 4'],
         'answer': 1,
         'explanation': '3 + 1 is 4, and the remainder of 4 divided by 4 is 0. One clockwise turn from '
                        'West faces North, and the heading never becomes 4.'},

        {'kind': 'bullets', 'title': 'Next: the whole problem',
         'bullets': [
             'You have the planner, a way to pick a heading, and a design for the turn',
             'Next lesson pulls the turning and planning code together',
             'Result: drive from the start to a destination, on its own',
         ],
         'tone': 'teal'},

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
