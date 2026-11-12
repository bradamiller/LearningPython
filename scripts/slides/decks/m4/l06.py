DECK = {
    'module': 4, 'lesson': 6,
    'doc': 'module-04-manhattan/lesson-06-driving-the-path',
    'title': 'Driving the Path',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Name the three Module 2 functions the driving code is built on, and what each does',
             'Write `turn_to()` and `drive_path()` from their outlines, and test them on a whole path',
             'Keep the robot\'s pose (`position` and `heading`) up to date by assigning from what `drive_path()` returns',
             'Plan, **print the path**, wait for the button, then drive, and use the printed path as the '
             'first diagnostic',
         ],
         'notes': '50 minutes, Python plus robot. The turn_to() paper design from Lesson 4-5 and '
                  'drive_path(), which pulls planning and turning together, become real code, built on the Module 2 line-tracking functions with no motor code rewritten. '
                  'Students write both, then test them on a whole path.'},

        {'kind': 'bullets', 'title': 'Time to make the robot move',
         'bullets': [
             '`turn_to()`, designed on paper in Lesson 4-5, and `drive_path()` join `get_desired_heading()` in the NAVIGATOR section',
             'Together they drive **any** Manhattan path on the grid',
             'They call the **line-tracking functions you built in Module 2**: no motor code to rewrite',
         ],
         'callout': 'That\'s the payoff of building a toolkit',
         'tone': 'teal'},

        {'kind': 'table', 'title': 'The toolkit you already have',
         'lead': 'Module 2 ended with three functions in the LINE TRACKING section. Module 3 drove the '
                 'whole grid with them.',
         'headers': ['Function', 'What it does', 'Ends when'],
         'widths': [4.2, 3.2, 3.6],
         'rows': [
             ['`track_to_intersection()`', 'Follows the line forward', 'the robot\'s center is on the cross'],
             ['`turn_clockwise()`', 'Pivots right', 'the sensors find the next line'],
             ['`turn_counterclockwise()`', 'Pivots left', 'the sensors find the next line'],
         ],
         'size': 21,
         'callout': 'No coordinates, headings or paths: they follow tape and have no idea where the robot '
                    'is. Today\'s three functions sit between them and the planner.',
         'callout_size': 20,
         'tone': 'teal',
         'notes': 'The split from Lesson 4-0 again: the planner doesn\'t know how to drive, and the '
                  'driving functions don\'t know what a path is. Class-track students with LineTrack '
                  'write tracker. in front of each.'},

        {'kind': 'code', 'title': 'Add to robot.py: turn_to()',
         'lead': 'Paste at the end of the NAVIGATOR section, under `get_desired_heading()`.',
         'lead_h': 0.7,
         'code': '# --- Lesson 4-6: turn to a heading, drive a path ---\n'
                 '# turn_to() turns a quarter turn at a time, with the LINE\n'
                 '# TRACKING turns, until the robot faces the heading it\n'
                 '# needs. drive_path() is the loop: for each\n'
                 '# intersection, face it, arrive with track_to_intersection(),\n'
                 '# and record the new position. Both hand back what they\n'
                 '# changed, because the caller keeps the only record.\n'
                 '\n'
                 'def turn_to(current_heading, desired_heading):\n'
                 '    """Turn clockwise a quarter turn at a time until\n'
                 '    current_heading is desired_heading; return the new\n'
                 '    heading."""\n'
                 '    # while current_heading is not desired_heading:\n'
                 '    #     one turn_clockwise()\n'
                 '    #     current_heading goes up by 1, wrapping 3 back to 0\n'
                 '    # return current_heading\n'
                 '    pass',
         'code_size': 15,
         'notes': 'turn_to() is the Lesson 4-5 design. The skeleton continues on the next '
                  'slide with drive_path(), the loop that uses it.'},

        {'kind': 'code', 'title': 'Add to robot.py: drive_path()',
         'lead': 'Right under `turn_to()`: the loop that uses it.',
         'lead_h': 0.7,
         'code': 'def drive_path(path, position, heading):\n'
                 '    """Turn and drive through every intersection in path, from\n'
                 '    position facing heading; return the final (position, heading)."""\n'
                 '    # for each next_pos in path:\n'
                 '    #     1. desired_heading = get_desired_heading(position, next_pos)\n'
                 '    #     2. heading = turn_to(heading, desired_heading)\n'
                 '    #     3. arrive: track_to_intersection()\n'
                 '    #     4. position = next_pos -- the robot is there now\n'
                 '    # return position, heading\n'
                 '    pass',
         'code_size': 19,
         'notes': 'Class-track students who built LineTrack in Lesson 2-9 write tracker.turn_clockwise(), '
                  'tracker.track_to_intersection() and so on: the same names with the object in front.'},

        {'kind': 'bullets', 'title': 'Keeping the pose',
         'bullets': [
             '`heading = turn_to(heading, desired_heading)` keeps the new heading',
             '`position = next_pos` records the intersection the robot just reached',
             'It returns both as one tuple, the robot\'s **pose**, and the caller unpacks it like `x, y = position` in Lesson 4-1',
         ],
         'callout': '`position, heading = drive_path(path, position, heading)`',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Why one track per entry is enough',
         'bullets': [
             'A destination can be many intersections away, but `drive_path()` never sees it',
             'It gets the planner\'s list, where every entry is **adjacent** to the one before',
             'So each pass of the loop is **one hop**: one turn (maybe none), then '
             '`track_to_intersection()` to the very next intersection',
             'A three-block leg is just three passes of the same loop',
         ],
         'callout': 'The planner breaks the trip into single hops; the driver only ever drives one block',
         'tone': 'teal',
         'notes': 'This is why the planner returns every intersection instead of only the destination. '
                  'If the list skipped intersections, track_to_intersection() would stop at the first '
                  'one and position would be wrong.'},

        {'kind': 'figure', 'title': 'The robot\'s pose',
         'figure': './decks/m4/fig/l06-pose.svg',
         'caption': 'Where the robot is and which way it faces, as one tuple. drive_path takes the '
                    'pose and hands back the new one.',
         'notes': 'Forget the left-hand side and the robot drives fine, once: the next path gets '
                  'planned from where the robot was. Position and heading together are its pose. From here on, "pass the pose" and "return the pose" mean the '
                  'position and heading together.'},

        {'kind': 'check',
         'question': 'A student writes `drive_path(path, position, heading)` on its own line, then plans '
                     'the next path with `compute_manhattan_path(position, dest)`. What goes wrong?',
         'options': ['Nothing: drive_path updates position for them',
                     'The caller\'s position and heading never changed: next path planned from the old spot',
                     'Python raises an error about an unused return value',
                     'The robot drives the path twice'],
         'answer': 1,
         'explanation': 'position and heading inside drive_path are the function\'s own variables. The '
                        'caller only learns the new values by assigning from the return. This is the '
                        'single most common Module 4 bug.'},

        {'kind': 'code', 'title': 'Plan, print, button, drive',
         'lead': 'The test that puts the planner and the navigator together: the shape of every driving '
                 'program from here on. Note the order.',
         'lead_h': 0.9,
         'code': 'def test_drive_path():\n'
                 '    position = (0, 0)\n'
                 '    heading = 0                   # facing North\n'
                 '    destination = (2, 3)\n'
                 '\n'
                 '    path = compute_manhattan_path(position, destination)\n'
                 '    print("Path:", path)\n'
                 '\n'
                 '    board.wait_for_button()       # read the path, THEN press\n'
                 '\n'
                 '    position, heading = drive_path(path, position, heading)\n'
                 '    print("Arrived at:", position, "facing", HEADING_NAMES[heading])',
         'code_size': 17,
         'notes': 'The path is planned and printed before the button. This habit costs two lines.'},

        {'kind': 'bullets', 'title': 'Read the path, then press',
         'bullets': [
             'Is the printed path what you expect? **Then** press the button',
             'Path right, robot wrong? The bug is in the **driving**, not the planner, and you know which half of the file to open',
             'Two button presses per run, both useful:',
             ['The one in the `RUN` block **starts** the test: the path prints and the robot sits still while you read it',
              'The one in the test is **go**'],
         ],
         'callout': 'A test that drives is the only kind that waits twice',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'The printed path is correct, but the robot turns left at the second intersection '
                     'when it should go straight. Where is the bug?',
         'options': ['In compute_manhattan_path',
                     'In the driving code: the planner has been shown to be right',
                     'In the print statement',
                     'In the destination tuple'],
         'answer': 1,
         'explanation': 'Printing the path before the button splits the program in two for debugging. A '
                        'correct printed path clears the planner; whatever went wrong is downstream of it: '
                        'get_desired_heading, turn_to, drive_path or the Module 2 functions.'},

        {'kind': 'steps', 'title': 'Activity · Write it, then drive it',
         'steps': [
             '**Write the code.** Write the bodies of `turn_to()` and `drive_path()` from their outlines',
             '**Run the test.** Add `test_drive_path()` from above, set the run line to it, and put the '
             'robot on (0, 0) facing North. Press once and read the printed path, then press again to '
             'drive to (2, 3). Watch each arrival: the robot\'s center on the cross, turns pivoting on it. '
             'And watch the corner where the path bends from East to North: **count the turns**',
         ],
         'size': 21,
         'notes': 'The check for turn_to() and drive_path() is a closed reveal on the lesson page. If a '
                  'leg goes wrong, the first two things to compare are the return current_heading and the '
                  'position = next_pos. A student version that differs and drives the path parked on '
                  'every cross is fine. Usual bugs, most frequent first: not assigning position, heading '
                  'from drive_path\'s return; the start sneaking into the path (get_desired_heading '
                  'raises if the student did the optional check in 4-5, and otherwise the robot spins in '
                  'place); a turn_to that forgets to return heading. Turns end on the sensors, not a '
                  'timer, so they tolerate battery and friction; if a turn overshoots, shorten the blind '
                  'first part of Module 2\'s turn_clockwise().'},

        {'kind': 'figure', 'title': 'Challenge (optional): the short way round',
         'tag': 'Optional challenge',
         'figure': '/img/lesson-m4-06/turn-shortcut-xy.svg',
         'caption': 'At the corner the robot turned right three times to face what was a quarter turn '
                    'to its left. One counterclockwise turn does the same.'},

        {'kind': 'bullets', 'title': 'Challenge (optional): fewer turns',
         'tag': 'Optional challenge',
         'bullets': [
             'Make `turn_to()` turn whichever way takes **fewer** turns',
             'First, on paper: when is counterclockwise actually shorter? Try every pair of headings, or just the four starting from North',
             'Change `turn_to()` to turn counterclockwise in exactly those cases, clockwise in the rest',
             'Keep `current_heading` up to date either way, and still return it',
             'Run `test_drive_path()` again and count the turns at the corner',
         ],
         'callout': 'Nothing else in the file has to change, because nothing else knows how `turn_to()` '
                    'does its job.',
         'tone': 'green',
         'notes': 'The answer is in the lesson\'s teacher copy, not here. Hints if needed: with four '
                  'headings there is exactly one case where counterclockwise wins; turning around is a '
                  'tie. Students who compute (desired_heading - current_heading) % 4 are also right, but it needs % '
                  'on a negative number (-1 % 4 is 3), worth showing in the REPL if it comes up. Watch '
                  'for a version that turns left and then also loops because it forgot to update '
                  'current_heading.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Software', 'Libraries', 'You call a graphics or networking library instead of rewriting '
                                       'it, exactly how drive_path calls track_to_intersection.'),
             ('Robotics', 'Motor controllers', 'High-level planners send "go to X"; a lower-level '
                                               'controller handles the motors, just like this split.'),
             ('Cars', 'Drive-by-wire', 'The steering software sets a target; a separate actuator '
                                       'system does the physical turning.'),
         ],
         'notes': 'Building on a well-tested lower layer is how real systems scale.'},

        {'kind': 'wrapup',
         'questions': [
             'What three Module 2 functions does the driving code use?',
             'What does `drive_path` return, and why?',
             'What do you do before pressing the button?',
         ],
         'next': 'the final project: a delivery run to several destinations',
         'notes': 'Answers: track_to_intersection, turn_clockwise, turn_counterclockwise. '
                  'The robot\'s pose, so the caller plans '
                  'the next path from the right place. Read the printed path. Exit ticket: "At (1,2) '
                  'heading 1 (E), next is (1,1): heading needed, headings turn_to() steps through, '
                  'and what the robot does?" (desired heading 2 (S), since y goes down by 1; E, S: one '
                  'clockwise turn, then track.)'},

        {'kind': 'bullets', 'title': 'Optional: what self really is',
         'tag': 'Optional extension',
         'bullets': [
             'Lesson 2-7: the class is a blueprint, the objects are houses. Now every house has an **address**',
             '`elm.paint()` means "paint the house at 48 Elm". Inside `paint()`, `self` is that address',
             'A method is a **work order** written once, with a blank for the address: `self` is first '
             'in the `def`, and Python fills it in from the object you called it on',
         ],
         'size': 22, 'split': 0.42,
         'figure': '/img/lesson-m4-06/house-address.svg',
         'notes': 'Optional extension, for students who did the Module 2 class extensions. Navigator is '
                  'the first class in the course whose constructor takes real parameters. Two errors '
                  'become easy to read: def paint(): with no self gives "takes 0 positional arguments '
                  'but 1 was given" (no address blank); color instead of self.color gives a NameError '
                  '(a color with no address). Navigator((0, 0), 0) and Navigator((3, 3), 2) are two '
                  'objects from one plan with different numbers on the door.'},

        {'kind': 'code', 'title': 'Optional: the Navigator class',
         'tag': 'Optional extension',
         'lead': 'Replaces the three functions (keep `HEADING_NAMES` and your tests). Move your bodies into '
                 'the methods. The caller writes `navigator.drive_path(path)` and reads `navigator.position`: '
                 'nothing to pass back, so nothing to forget.',
         'lead_h': 1.25,
         'code': 'class Navigator:\n'
                 '    def __init__(self, start, heading):\n'
                 '        self.position = start\n'
                 '        self.heading = heading\n'
                 '        self.line_track = LineTrack()        # has-a LineTrack\n'
                 '\n'
                 '    def get_desired_heading(self, next_pos):\n'
                 '        pass\n'
                 '\n'
                 '    def turn_to(self, desired_heading):\n'
                 '        pass\n'
                 '\n'
                 '    def drive_path(self, path):\n'
                 '        pass\n'
                 '\n'
                 'navigator = Navigator((0, 0), 0)',
         'code_size': 14,
         'notes': 'Shortened from the lesson\'s class-track skeleton: the section header comment and each '
                  'method\'s outline comments are left off to fit. Those comments say position becomes '
                  'self.position, heading becomes self.heading, turns get self.line_track. in front, '
                  'and turn_to and drive_path store instead of return. __init__ is the new idea, so it '
                  'is given. The signatures shrank because the object already knows position and '
                  'heading. From here on class-track students use navigator.drive_path(path) wherever '
                  'Lesson 4-7 says drive_path(path, position, heading). Full file: '
                  'lesson-08-navigator-class-addon.py in the Module 4 solutions. The finished methods '
                  'are behind a reveal on the lesson page and are not shown here.'},
    ],
}
