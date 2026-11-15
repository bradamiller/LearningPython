"""Module 4, Lesson 4-6 · On the Robot."""

DECK = {
    'module': 4, 'lesson': 6,
    'doc': 'module-04-manhattan/lesson-06-on-the-robot',
    'title': 'On the Robot',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Name the Module 2 functions the driving code is built on, and what each does',
             'Swap the two stubs for the real functions and drive the delivery run on the grid',
             'Tell an algorithm bug from a robot problem by comparing the robot with the printout',
             'Demonstrate a working multi-destination run on the XRP',
         ],
         'notes': 'Multi-day; for 50-minute periods, plan two. The whole delivery already runs on '
                  'screen. Today the last two stubs come out, the real Module 2 functions go in, and '
                  'the robot drives it. Keep the intro short: this is a run-and-fix day.'},

        {'kind': 'table', 'title': 'The toolkit you already have',
         'lead': 'Module 2 built these in the LINE TRACKING section; Module 3 drove the grid with '
                 'them:',
         'headers': ['Function', 'What it does', 'Ends when'],
         'widths': [3.6, 2.8, 3.8],
         'rows': [['`track_to_intersection()`', 'Follows the line forward',
                   'the robot\'s center is on the cross'],
                  ['`turn_clockwise()`', 'Pivots right', 'the sensors find the next line'],
                  ['`turn_counterclockwise()`', 'Pivots left', 'the sensors find the next line']],
         'size': 20,
         'callout': 'They only follow tape. The planner doesn\'t know how to drive; these don\'t '
                    'know what a path is. The NAVIGATOR sits between them.',
         'tone': 'teal'},

        {'kind': 'steps', 'title': 'Step 1 · Swap two lines',
         'tag': 'Activity',
         'steps': [
             'In `turn_to()`, change `fake_turn_clockwise()` to `turn_clockwise()`',
             'In `drive_path()`, change `fake_track_to_intersection()` to `track_to_intersection()`',
             'That\'s all. Leave the two fake functions in the file',
         ],
         'callout': 'Class track: `tracker.turn_clockwise()` and `tracker.track_to_intersection()`',
         'tone': 'teal',
         'notes': 'The fakes stay because they are handy for checking a new run on screen first.'},

        {'kind': 'steps', 'title': 'Step 2 · Drive it',
         'tag': 'Activity',
         'steps': [
             'Put the robot on (0, 0) facing North',
             'Run `test_delivery()` and press the button',
             'Count the turns at each corner against the printout',
         ],
         'callout': 'Correct: exactly what the printout said, in order. One right turn at the start, '
                    'three at (2, 0). Ends on (0, 0) facing South.',
         'tone': 'green',
         'notes': 'The moving: lines still print as it goes. Charge between runs: the delivery run '
                  'has a lot of turns. When a robot finishes the whole run, let the class watch.'},

        {'kind': 'check',
         'question': 'Yesterday\'s printout was right, but today the robot turns one too few times '
                     'at a corner. Where is the problem?',
         'options': ['In `compute_manhattan_path()`',
                     'On the robot side: a turn that missed or doubled up a line, the tape, or the '
                     'battery',
                     'In the print statements',
                     'In `DELIVERY_STOPS`'],
         'answer': 1,
         'explanation': 'The planner, get_desired_heading() and turn_to() were tested on screen and '
                        'didn\'t change. Only the two real calls are new.',
         'notes': 'If a robot wanders, ask for the printout first. If the printout is wrong, it was '
                  'wrong yesterday too, and the fix is in the code; if it\'s right, it\'s the robot. '
                  'Turns end when the sensors find the next line, so they tolerate battery and '
                  'friction; if a turn overshoots, shorten the blind first part of '
                  'turn_clockwise().'},

        {'kind': 'figure', 'title': 'Challenge · The short way round (optional)',
         'tag': 'Optional',
         'figure': '/img/lesson-m4-06/turn-shortcut-xy.svg',
         'caption': 'At (2, 0) the robot turned right three times to face a quarter turn to its '
                    'left. Make `turn_to()` take whichever way is fewer turns.',
         'notes': 'Work out on paper first when counterclockwise is shorter. Answer: only when '
                  'desired_heading == (current_heading + 3) % 4; turn counterclockwise once and set '
                  'current_heading, and the loop then has nothing to do. Turning around is a tie. '
                  'Other versions are right if the turn counts match; -1 % 4 is 3, so '
                  '(current_heading - 1) % 4 also works. '
                  'Watch for a version that turns left and forgets to update current_heading. '
                  'Check it on screen first with a fake_turn_counterclockwise().'},

        {'kind': 'table', 'title': 'The rubric',
         'headers': ['Category', 'Points', 'What it takes'],
         'widths': [2.4, 1.2, 7.6],
         'rows': [['Planner', '10', '`compute_manhattan_path()` correct for any start and '
                   'destination; `test_planner()` passes'],
                  ['Driving functions', '15', '`get_desired_heading()`, `turn_to()`, `drive_path()`; '
                   'parked on the cross; pose returned'],
                  ['Main program', '10', '`test_delivery()`: 4+ destinations, assigns '
                   '`robot_position, robot_heading`'],
                  ['Screen run', '5', 'Full run checked on screen with the stubs first'],
                  ['Robot demo', '10', 'Visits all destinations with the turns the printout '
                   'predicted']],
         'size': 18,
         'notes': 'Early finishers: a round trip (the stops forward, then reversed); let the user '
                  'type destinations; count intersections driven and turns made; or the Navigator '
                  'class extension.'},

        {'kind': 'bullets', 'title': 'Optional: the Navigator class, and what self is',
         'tag': 'Optional',
         'figure': '/img/lesson-m4-06/house-address.svg',
         'split': 0.5,
         'bullets': [
             'A class is the plan; each object is a house built from it, with an **address**',
             '`self` is the address of the one object this call is about',
             'A `Navigator` stores its own position and heading, so nothing is passed back',
         ],
         'size': 22,
         'notes': 'For students who did the Module 2 class extensions. The constructor takes the '
                  'start position and heading; the methods read and update self.position and '
                  'self.heading, which is why the signatures shrink and nothing is returned. Two '
                  'errors become easy to read: a method with no self ("takes 0 positional arguments '
                  'but 1 was given"), and a name with no self. in front (NameError). The skeleton '
                  'and the finished methods are on the lesson page.'},

        {'kind': 'wrapup',
         'questions': [
             'What changed today?',
             'If the robot goes wrong but the printout was right, where do you look?',
             'Where did top-down pay off?',
         ],
         'next': 'tuples and lists: what you now know',
         'notes': 'Answers: two lines, the fake turn and the fake track became the real Module 2 '
                  'functions. The robot side: turns, tape, battery. The whole run worked on screen '
                  'before the robot moved, and every step was checked as it was added. Name what '
                  'students built: a main program first, a planner and a driver that know nothing '
                  'about each other, a test for every step, and the hardware last. In Module 5, '
                  'breadth-first search replaces the planner and drive_path() keeps driving.'},
    ],
}
