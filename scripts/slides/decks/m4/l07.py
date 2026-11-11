DECK = {
    'module': 4, 'lesson': 7,
    'doc': 'module-04-manhattan/lesson-07-driving-the-path',
    'title': 'Driving the Path',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Name the four Module 2 functions the driving code is built on, and what each does',
             'Explain why the robot must `drive_past_intersection()` after every `track_to_intersection()`',
             'Write `turn_to()` and `drive_path()` from their outlines, and test them one at a time',
             'Keep the robot\'s pose (`position` and `heading`) up to date by assigning from what `drive_path()` returns',
             'Plan, **print the path**, wait for the button, then drive',
         ],
         'notes': '60 minutes, Python plus robot. The two paper designs from Lesson 4-6 become real '
                  'code, built on the Module 2 line-tracking functions with no motor code rewritten. '
                  'Testing goes on screen first, then one leg, then a path.'},

        {'kind': 'bullets', 'title': 'Time to make the robot move',
         'bullets': [
             'The two functions you designed on paper join `desired_heading()` in the NAVIGATOR section',
             'Together they drive **any** Manhattan path on the grid',
             'They call the **line-tracking functions you built in Module 2**: no motor code to rewrite',
             'One wrinkle the paper design didn\'t care about: **where** the robot actually turns',
         ],
         'callout': 'That\'s the payoff of building a toolkit',
         'tone': 'teal'},

        {'kind': 'table', 'title': 'The toolkit you already have',
         'lead': 'Module 2 ended with four functions in the LINE TRACKING section. Module 3 drove the '
                 'whole grid with them.',
         'headers': ['Function', 'What it does', 'Ends when'],
         'widths': [4.2, 3.2, 3.6],
         'rows': [
             ['`track_to_intersection()`', 'Follows the line forward', 'both sensors see the cross'],
             ['`turn_clockwise()`', 'Pivots right', 'the sensors find the next line'],
             ['`turn_counterclockwise()`', 'Pivots left', 'the sensors find the next line'],
             ['`drive_past_intersection()`', 'Drives straight 8.75 cm', 'the distance is done'],
         ],
         'size': 21,
         'callout': 'No coordinates, headings or paths: they follow tape and have no idea where the robot '
                    'is. Today\'s three functions sit between them and the planner.',
         'tone': 'teal',
         'notes': 'The split from Lesson 4-0 again: the planner doesn\'t know how to drive, and the '
                  'driving functions don\'t know what a path is. Class-track students with LineTrack '
                  'write tracker. in front of each.'},

        {'kind': 'check',
         'question': 'Which of these does `track_to_intersection()` know about?',
         'options': ['The robot\'s x and y coordinates',
                     'Only the reflectance sensors and the motors: it follows tape until both sensors see a cross',
                     'The heading number', 'The path list'],
         'answer': 1,
         'explanation': 'Module 2\'s functions are about tape, not grids. That makes them reusable: the '
                        'same track_to_intersection() drove the Module 3 square and drives paths here.'},

        {'kind': 'code', 'title': 'Arriving: the same pair as Module 3',
         'lead': '`track_to_intersection()` stops the moment both **sensors** see the cross, but the robot '
                 'turns about its **center of rotation**, 8.75 cm behind them. You met this in Lesson 3-1, '
                 'and the fix is the same here.',
         'lead_h': 1.75, 'size': 27,
         'code': 'track_to_intersection()        # sensors reach the cross\n'
                 'drive_past_intersection()      # center of rotation on the cross; sensors past it',
         'code_size': 18,
         'callout': '`drive_path()` arrives at **every** intersection with the pair, whichever way it turns '
                    'next: turns spin on the cross, and the next track starts clean.',
         'callout_size': 20,
         'tone': 'teal',
         'notes': 'The two-robot animation in Lesson 3-1 shows what goes wrong if you turn early. The '
                  '8.75 cm is the gap between the reflectance sensors and the center of rotation (the '
                  'pen hole between the drive wheels) on an XRP; if a class has a robot with a '
                  'different mounting, measure it. Doing the drive-past after every track removes '
                  'the straight-ahead special case the old lesson had.'},

        {'kind': 'check',
         'question': 'Why does the robot call `drive_past_intersection()` after every '
                     '`track_to_intersection()`, even when it is going straight on?',
         'options': ['To speed up the run',
                     'Moves the center of rotation onto the cross: turns pivot there, next track starts clean',
                     'Only turns need it; going straight it is skipped',
                     'To recharge the battery'],
         'answer': 1,
         'explanation': 'The sensors lead the center of rotation. Parking it on the cross makes every turn '
                        'pivot on the intersection, and moves the sensors off the tape so the next '
                        'line-follow starts clean. Doing it every time means no special cases.'},

        {'kind': 'code', 'title': 'Add to robot.py: turn_to()',
         'lead': 'Paste at the end of the NAVIGATOR section, under `desired_heading()`.',
         'lead_h': 0.7,
         'code': '# --- Lesson 4-7: turn to a heading, drive a path ---\n'
                 '# turn_to() turns a quarter turn at a time, with the LINE\n'
                 '# TRACKING turns, until the robot faces the heading it\n'
                 '# needs. drive_path() is the loop: for each\n'
                 '# intersection, face it, arrive with the track-then-drive-past\n'
                 '# pair, and record the new position. Both hand back what they\n'
                 '# changed, because the caller keeps the only record.\n'
                 '\n'
                 'def turn_to(heading, desired):\n'
                 '    """Turn clockwise a quarter turn at a time until heading\n'
                 '    is desired; return the new heading."""\n'
                 '    # while heading is not desired:\n'
                 '    #     one turn_clockwise()\n'
                 '    #     heading goes up by 1, wrapping 3 back to 0\n'
                 '    # return heading\n'
                 '    pass',
         'code_size': 16,
         'notes': 'The two outlines are the Lesson 4-6 designs. The skeleton continues on the next '
                  'slide with drive_path(), whose step 3 has grown the wrinkle.'},

        {'kind': 'code', 'title': 'Add to robot.py: drive_path()',
         'lead': 'Right under `turn_to()`. Step 3 has grown the wrinkle: arrive with the pair.',
         'lead_h': 0.7,
         'code': 'def drive_path(path, position, heading):\n'
                 '    """Turn and drive through every intersection in path, from\n'
                 '    position facing heading; return the final (position, heading)."""\n'
                 '    # for each next_pos in path:\n'
                 '    #     1. needed = desired_heading(position, next_pos)\n'
                 '    #     2. heading = turn_to(heading, needed)\n'
                 '    #     3. arrive: track_to_intersection(), then\n'
                 '    #        drive_past_intersection()\n'
                 '    #     4. position = next_pos -- the robot is there now\n'
                 '    # return position, heading\n'
                 '    pass',
         'code_size': 19,
         'notes': 'Class-track students who built LineTrack in Lesson 2-9 write tracker.turn_clockwise(), '
                  'tracker.track_to_intersection() and so on: the same names with the object in front.'},

        {'kind': 'bullets', 'title': 'Read the two assignments carefully',
         'bullets': [
             '`heading = turn_to(heading, needed)`: the turn function hands back the new heading, and the loop keeps it',
             '`position = next_pos`: the robot has arrived, so its position is the intersection it just drove to',
             'The function returns both at the end, so whoever called it can keep its own record straight',
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

        {'kind': 'bullets', 'title': 'One tuple, unpacked',
         'bullets': [
             '`return position, heading` looks like returning two things, but it is **one**: two values with a comma make a tuple',
             'That tuple is the robot\'s **pose**, say `((1, 1), 0)`',
             'The left-hand side unpacks it, exactly like `x, y = position` in Lesson 4-2',
             'First variable gets the position, second gets the heading',
         ],
         'callout': 'Forget the left-hand side and the robot drives fine, **once**. The next path gets '
                    'planned from where the robot was.',
         'tone': 'orange'},

        {'kind': 'figure', 'title': 'The robot\'s pose',
         'figure': './decks/m4/fig/l07-pose.svg',
         'caption': 'Where the robot is and which way it faces, as one tuple. drive_path takes the '
                    'pose and hands back the new one.',
         'notes': 'Position says where the robot is; heading says which way it faces. Together they '
                  'are its pose. From here on, "pass the pose" and "return the pose" mean the '
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
         'tone': 'teal',
         'notes': 'The two presses need saying once; after that students like it, because the first '
                  'press is when they read the path.'},

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
                        'desired_heading, turn_to, drive_path or the Module 2 functions.'},

        {'kind': 'bullets', 'title': 'Plan, then drive: connect the parts',
         'bullets': [
             'This test connects the two halves from Lesson 4-0',
             'Each part was built and tested on its own, so connecting them takes **three '
             'lines**: plan, print, drive',
             'It is that short because both parts agreed from the start on what passes between '
             'them: **a list of intersections**',
         ],
         'callout': 'When a run goes wrong, the printed path tells you which part to open',
         'tone': 'teal'},

        {'kind': 'steps', 'title': 'Activity · Trace it, then integrate',
         'lead': 'Before running anything, trace `[(1,0), (1,1)]` from (0,0) heading 0 (N) on paper. '
                 'For each step write down:',
         'lead_h': 0.9,
         'steps': [
             'The next intersection, and the heading needed',
             'The headings the turning loop steps through',
             'What the robot does',
         ],
         'callout': 'Then build it in stages, one function per step. Don\'t go on until each works.',
         'tone': 'orange',
         'notes': 'The trace and its grid figure are a closed reveal on the lesson page ("paper '
                  'first"). Point out step 2 when students check: facing East and needing North, '
                  'the loop goes three quarters of the way round.'},

        {'kind': 'steps', 'title': 'Step 1 · The logic, on screen',
         'steps': [
             'Write the body of `turn_to()` from its outline',
             'Write `test_turns_paper()`: walk `[(1, 0), (1, 1)]` from `(0, 0)` heading 0 the way '
             '`drive_path()` will, but **print** instead of turning',
             'Each step: print the intersection and heading needed, then run the same `while` loop, '
             'with a `print` of the new heading where `turn_clockwise()` would be. Update `position`',
             'Set the run line to it and compare with your trace: E for the first step, then S, W, N. '
             'Nothing moves.',
         ],
         'size': 20,
         'notes': 'This paper test is the old "desktop mode" without editing the Module 2 functions: '
                  'it prints what the robot would do, and it is where most logic bugs get caught. '
                  'Write and test one function at a time, never the whole section at once.'},

        {'kind': 'steps', 'title': 'Step 2 · One leg',
         'steps': [
             'Write the body of `drive_path()`',
             'Write `test_one_leg()`: drive the one-element path `[(1, 0)]` from `(0, 0)` heading 0, '
             'and print where it arrived',
             'Robot at (0, 0) facing North, run line set to it, both presses',
             'One clockwise turn, one track, one drive-past. Does the robot stop with its '
             '**center of rotation** on the intersection?',
         ],
         'size': 20,
         'notes': 'The check for turn_to() and drive_path() is a closed reveal on the lesson page. If a '
                  'leg goes wrong, the first two things to compare are the return heading and the '
                  'position = next_pos. A student version that differs and drives the path parked on '
                  'every cross is fine.'},

        {'kind': 'steps', 'title': 'Step 3 · A real path',
         'steps': [
             'Add `test_drive_path()` and run it: `(0, 0)` to `(2, 3)`',
             'Read the printed path before the second press',
             'Watch each arrival: center of rotation on the cross, turns pivoting on it',
             'Watch the corner where the path bends from East to North: **count the turns**',
         ],
         'notes': 'The clockwise-only loop spins 270 degrees at that corner: correct behavior, and the '
                  'optional challenge is there for students who want to fix it. Usual bugs, most '
                  'frequent first: not assigning position, heading from drive_path\'s return; the '
                  'start sneaking into the path (desired_heading raises, which is the lesson working); '
                  'a turn_to that forgets to return heading. Turns end on the sensors, not a timer, so '
                  'they tolerate battery and friction; if a turn overshoots, shorten the blind first '
                  'part of Module 2\'s turn_clockwise().'},

        {'kind': 'figure', 'title': 'Challenge (optional): the short way round',
         'tag': 'Optional challenge',
         'figure': '/img/lesson-m4-07/turn-shortcut-xy.svg',
         'caption': 'At the corner the robot turned right three times to face what was a quarter turn '
                    'to its left. One counterclockwise turn does the same.'},

        {'kind': 'bullets', 'title': 'Challenge (optional): fewer turns',
         'tag': 'Optional challenge',
         'bullets': [
             'Make `turn_to()` turn whichever way takes **fewer** turns',
             'First, on paper: when is counterclockwise actually shorter? Try every pair of headings, or just the four starting from North',
             'Change `turn_to()` to turn counterclockwise in exactly those cases, clockwise in the rest',
             'Keep `heading` up to date either way, and still return it',
             'Run `test_drive_path()` again and count the turns at the corner',
         ],
         'callout': 'Nothing else in the file has to change, because nothing else knows how `turn_to()` '
                    'does its job.',
         'tone': 'green',
         'notes': 'The answer is in the lesson\'s teacher copy, not here. Hints if needed: with four '
                  'headings there is exactly one case where counterclockwise wins; turning around is a '
                  'tie. Students who compute (desired - heading) % 4 are also right, but it needs % '
                  'on a negative number (-1 % 4 is 3), worth showing in the REPL if it comes up. Watch '
                  'for a version that turns left and then also loops because it forgot to update '
                  'heading.'},

        {'kind': 'check',
         'question': 'The path is [(1,0),(2,0),(2,1)]. How many times does drive_path call '
                     'track_to_intersection(), and how many times drive_past_intersection()?',
         'options': ['Three and zero',
                     'Three and three: one pair per intersection in the path',
                     'Four and four: including the start',
                     'It depends on the turns'],
         'answer': 1,
         'explanation': 'drive_path loops once per element in the path, and every pass ends with the '
                        'track-then-drive-past pair. Three elements, three pairs. The start is not in the path.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Software', 'Libraries', 'You call a graphics or networking library instead of rewriting '
                                       'it, exactly how drive_path calls track_to_intersection.'),
             ('Robotics', 'Motor controllers', 'High-level planners send "go to X"; a lower-level '
                                               'controller handles the motors, just like this split.'),
             ('Cars', 'Drive-by-wire', 'The steering software sets a target; a separate actuator '
                                       'system does the physical turning.'),
         ],
         'notes': 'Building on a well-tested lower layer is how real systems scale. Hammer the reuse '
                  'point: the Module 2 functions drove the Module 3 square and now drive grid paths '
                  'unchanged.'},

        {'kind': 'wrapup',
         'questions': [
             'What four Module 2 functions does the driving code use?',
             'Why `drive_past_intersection()` after every track?',
             'What does `drive_path` return, and why?',
             'What do you do before pressing the button?',
         ],
         'next': 'the final project: a delivery run to several destinations',
         'notes': 'Answers: track_to_intersection, turn_clockwise, turn_counterclockwise, '
                  'drive_past_intersection. To put the center of rotation on the cross, so turns pivot '
                  'there and the next track starts clean. The robot\'s pose, so the caller plans '
                  'the next path from the right place. Read the printed path. Exit ticket: "At (1,2) '
                  'heading 1 (E), next is (1,1): heading needed, headings turn_to() steps through, '
                  'and what the robot does?" (2 (S), since y goes down by 1; E, S: one clockwise turn, '
                  'then track and drive past.)'},

        {'kind': 'bullets', 'title': 'Optional: what self really is',
         'tag': 'Optional extension',
         'bullets': [
             'Lesson 2-7: the class is a blueprint, the objects are houses. Now every house has an **address**',
             '`elm.paint()` means "paint the house at 48 Elm". Inside `paint()`, `self` is that address',
             'A method is a **work order** written once, with a blank for the address: `self` is first '
             'in the `def`, and Python fills it in from the object you called it on',
         ],
         'size': 22, 'split': 0.42,
         'figure': '/img/lesson-m4-07/house-address.svg',
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
                 '    def desired_heading(self, next_pos):\n'
                 '        pass\n'
                 '\n'
                 '    def turn_to(self, desired):\n'
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
                  'Lesson 4-8 says drive_path(path, position, heading). Full file: '
                  'lesson-08-navigator-class-addon.py in the Module 4 solutions. The finished methods '
                  'are behind a reveal on the lesson page and are not shown here.'},
    ],
}
