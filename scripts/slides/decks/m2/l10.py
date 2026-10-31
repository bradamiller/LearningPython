DECK = {
    'module': 2, 'lesson': 10,
    'doc': 'module-02-line-tracking/lesson-10-final-project',
    'title': 'Final Project',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Combine both sections of `robot.py` into one complete, working program',
             'Write a short, readable project function that is mostly **calls to your own functions**',
             'Test and debug a real robot behavior **systematically**',
             'Explain and demonstrate your design',
         ],
         'notes': 'Multi-day capstone. Treat it as an arc: plan, build, test, present. The final '
                  'project is the summative assessment for Module 2.'},

        {'kind': 'bullets', 'title': 'Put it all together',
         'bullets': [
             '`robot.py` has two finished sections',
             ['**LINE SENSOR** reads the tape', '**LINE TRACKING** drives on it'],
             'This project is the first program built **entirely** out of them',
             'Follow the taped circle, detect the cross, reverse direction, repeat four times, then stop',
         ],
         'callout': 'The capstone of Module 2: sensors, control loops, decisions, and functions built '
                    'on functions',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'The mission',
         'lead': 'Your robot must:',
         'lead_h': 0.6,
         'bullets': [
             'Follow the taped circle with `track_to_intersection()`',
             'Detect the cross intersection',
             'Reverse direction',
             'Keep following, and repeat for **4 total reversals**',
             'Stop and print a completion message',
         ],
         'size': 24,
         'split': 0.56,
         'figure': '/img/lesson-m2-10/final-project-reverse.svg',
         'frame': 0.0,
         'crop': (0.0, 0.08, 0.6, 1.0),
         'callout': 'Built the classes? Use `tracker.track_to_intersection()` wherever the list says '
                    '`track_to_intersection()`',
         'tone': 'teal'},

        {'kind': 'frames', 'title': 'What the finished project looks like',
         'figure': '/img/lesson-m2-10/final-project-reverse.svg',
         'crop': (0.0, 0.08, 0.6, 1.0),
         'frames': [(0.09, '**At the cross:** park, one clockwise turn'),
                    (0.18, '**Next leg:** following the other way'),
                    (0.91, '**Done:** four reversals, it stops')],
         'callout': 'The cross is too short to stop a turn, so one clockwise turn reverses the robot, '
                    'and it meets the cross once a lap',
         'tone': 'teal',
         'notes': 'On the lesson page this is an animation of the whole run, with a panel naming '
                  'each stage. The cross is one short strip, about half as long as the robot is '
                  'wide: long enough for both sensors to see it, too short to stop the turn.'},

        {'kind': 'cards', 'title': 'Pick your option',
         'cards': [
             ('Option A', 'Standard', 'The mission, using your two sections unchanged. Focus on a '
                                      'clean project function and solid debugging.'),
             ('Option B', 'Enhanced', 'Use a `turn_around()` function (the Lesson 2-9 challenge; '
                                      'write it now if not), count each leg, and flash the LED or '
                                      'beep at every reversal.'),
             ('Option C', 'Advanced', 'Add line-loss recovery, or speed up on later laps. Invent your '
                                      'own twist (teacher-approved).'),
         ],
         'height': 3.9},

        {'kind': 'code', 'title': 'Add to robot.py: this lesson\'s skeleton',
         'lead': 'Paste it above `RUN`, at the end of LINE TRACKING. Two tests, and the second one **is** the project.',
         'lead_h': 0.75,
         'code': 'def test_reversal():\n'
                 '    # park on the cross, turn around (one clockwise turn\n'
                 '    # does it here), then follow back to the cross\n'
                 '    pass\n'
                 '\n'
                 'def test_final_project():\n'
                 '    # the mission: follow to the cross, park on it, reverse,\n'
                 '    # four times in all; then stop and print "Done!"\n'
                 '    # write your plan here as comments first, then the code\n'
                 '    pass',
         'code_size': 17,
         'callout': 'Both bodies are yours. The outline is short on purpose: the plan is the first '
                    'part of the project.',
         'tone': 'orange',
         'notes': 'There are no new driving functions in this lesson. The skeleton on the lesson page opens with a section comment: the module project '
                  'laps the circle, reversing at the cross, four times, then stops; nothing new is '
                  'defined for it; it is a list of calls to the four driving functions, because the '
                  'sections did the work and the project assembles them. The slide leaves that '
                  'comment out to fit.'},

        {'kind': 'steps', 'title': 'Activity · Plan before you build',
         'steps': [
             'Pseudocode `test_final_project()` first, in **plain English**, before you type any Python',
             'Write your plan as `#` comments inside the function, **one step per line**',
             'It will be shorter than you expect: the two sections do the heavy lifting, so each line of the plan is close to one line of code',
         ],
         'callout': 'When you\'re done, each comment will have its line of code under it',
         'tone': 'teal',
         'notes': 'The lesson page has a closed reveal with one possible plan; students write theirs '
                  'first. If a plan has many more steps, ask: what work are you doing by hand that a '
                  'function in LINE TRACKING already does? The button wait is not part of the plan: '
                  'the RUN block does that before every test.'},

        {'kind': 'check',
         'question': 'For the final project, do you need to rewrite the sensor and driving logic from scratch?',
         'options': ['Yes: copy it all into the project function',
                     'No: reuse the tested LINE SENSOR and LINE TRACKING sections of `robot.py`',
                     'Yes: functions cannot be reused in a new program',
                     'Only the sensor part'],
         'answer': 1,
         'explanation': 'That\'s the whole point of building the file one tested function at a time: '
                        'the project is a handful of calls to functions you already trust.'},

        {'kind': 'steps', 'title': 'Build it in pieces',
         'lead': 'You have every part already. Build in this order, and don\'t go on until each step works:',
         'steps': [
             '**Park on the cross.** Run `test_park()` from Lesson 2-9 once more. Wheels on the cross?',
             '**One turn.** Run `test_turn()`. Does the turn find the line again?',
             '**One full reversal.** Write the body of `test_reversal()` and run it: park, one clockwise turn, follow back to the same cross',
             '**The loop.** Write `test_final_project()` under your plan comments and set the run line to it',
         ],
         'size': 20,
         'tag': 'Activity',
         'notes': 'Insist on incremental testing. If a student did the Lesson 2-9 challenge, '
                  'test_turn_around() is test_reversal() already. The teacher copy of the solution '
                  'is for unsticking a team, not a handout: the assembly and tuning is the graded '
                  'work, and there is no student reveal for it.'},

        {'kind': 'steps', 'title': 'Activity · Test, tune, present',
         'lead': 'Work up in stages, and keep a note of what you tuned:',
         'steps': [
             'Does `test_park()` follow and stop at the cross, with the wheels left on it?',
             'Does one turn in `test_turn()` find the line again?',
             'Does `test_reversal()` work end to end?',
             'Do all four reversals in `test_final_project()` run and stop?',
         ],
         'size': 20,
         'notes': 'The common fixes are all tuning: THRESHOLD (cross not detected), the blind part '
                  'of the turn or TURN_EFFORT (the loop ends on the old line, or spins past the new '
                  'one), and BASE_EFFORT (overshoots the cross). Frame that tuning as the real '
                  'engineering, not failure. Two successful reversals already show mastery; four is '
                  'the goal.'},

        {'kind': 'check',
         'question': 'Your robot follows the line but blows past the cross without stopping. '
                     'What\'s the best first thing to try?',
         'options': ['Rewrite both toolkits',
                     'Lower `BASE_EFFORT` (and/or check `THRESHOLD`) so it detects the cross in time',
                     'Delete the turn methods',
                     'Increase Kp to 5'],
         'answer': 1,
         'explanation': 'Overshooting is usually too much speed or a threshold that\'s too high. Slow '
                        'down and re-check calibration before touching anything else.'},

        {'kind': 'bullets', 'title': 'You built a robot that thinks',
         'bullets': [
             'You started Module 2 reading **a single sensor value**',
             'You finish it with two cooperating sections of one file that follow a line, detect intersections, and navigate a course',
             'Sensing and driving cleanly separated, each built on the layer below, each function tested the lesson it was written',
         ],
         'callout': 'That is exactly how professional robot code is structured, and the next module '
                    'adds a section on top of it',
         'tone': 'green',
         'notes': 'Students who did the class extensions have the same thing as LineSensor and '
                  'LineTrack objects, and that is the version they should have used for the project.'},

        {'kind': 'wrapup', 'title': 'Demo and reflect',
         'questions': [
             'What was hardest?',
             'How did building the file one tested function at a time make the project easier?',
             'What would you add with more time?',
         ],
         'next': 'Module 3 · Grid Driving',
         'notes': 'The final project is the summative assessment: a 50-point rubric across code '
                  'organization, functionality, testing and debugging, and presentation works well. '
                  'Reward process and tuning, not just a flawless demo. Module 3 adds a GRID DRIVING '
                  'section to robot.py: track_to_intersection() and drive_past_intersection() become '
                  'the way the robot drives from one intersection to the next.'},
    ],
}
