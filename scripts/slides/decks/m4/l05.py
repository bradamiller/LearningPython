"""Module 4, Lesson 4-5 · Turning."""

DECK = {
    'module': 4, 'lesson': 5,
    'doc': 'module-04-manhattan/lesson-05-turning',
    'title': 'Turning',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Design a turn as a loop: one clockwise quarter turn at a time until the heading '
             'matches',
             'Wrap the heading from 3 back to 0 with `(heading + 1) % 4`',
             'Write the real `turn_to()` and count its turns in the delivery run\'s printout',
         ],
         'notes': '40 to 50 minutes, robot on the desk. Right now turn_to() is a stub: the robot '
                  'faces whichever way it\'s told, instantly. A real robot turns a quarter turn at a '
                  'time with the Module 2 turn_clockwise(). Today students write the real turn_to(), '
                  'with one more stub standing in for the turn itself, so every quarter turn shows '
                  'up as a printed line.'},

        {'kind': 'code', 'title': 'This lesson\'s skeleton',
         'code': 'def fake_turn_clockwise():\n'
                 '    print("turning clockwise")\n'
                 '\n'
                 'def turn_to(current_heading, desired_heading):\n'
                 '    # while current_heading is not desired_heading:\n'
                 '    #     fake_turn_clockwise()\n'
                 '    #     current_heading goes up by 1, wrapping 3 back to 0\n'
                 '    # return current_heading\n'
                 '    pass',
         'code_size': 18,
         'notes': 'Replace the turn_to() stub with this, and put the new stub next to '
                  'fake_track_to_intersection(). The slide leaves out the docstrings to fit; '
                  'students copy the block from the lesson page.'},

        {'kind': 'steps', 'title': 'Step 1 · Predict the turns',
         'tag': 'Activity',
         'lead': 'Every step: write down what you expect, run it, compare.',
         'steps': [
             'The robot starts facing North and turns only **clockwise**, a quarter turn at a time',
             'How many turns before each of Leg 1\'s five moves: **E, E, N, N, N**?',
         ],
         'notes': 'Answer: 1, 0, 3, 0, 0. North to East is one turn. East to East is none: the loop '
                  'doesn\'t run. East to North is three: South, West, North.'},

        {'kind': 'figure', 'title': 'Step 1 · Check your prediction',
         'tag': 'Activity',
         'figure': '/img/lesson-m4-05/turn-to-steps.svg',
         'caption': '1, 0, 3, 0, 0. The loop never asks which way is shorter.',
         'notes': 'One clockwise quarter turn at a time: heading 1 to 2, 2 to 3, and 3 wraps to 0 '
                  'at the third move. On the lesson page students can step through it.'},

        {'kind': 'code', 'title': 'Step 2 · Wrap 3 back to 0',
         'tag': 'Activity',
         'lead': 'West is 3, and 3 + 1 is 4: not a heading. `%` from Lesson 2-5 wraps it. Predict '
                 'the four lines, then run this in the shell:',
         'lead_h': 1.1,
         'code': 'for h in range(4):\n'
                 '    print(h, (h + 1) % 4)',
         'code_size': 28,
         'notes': 'Output: 0 1, 1 2, 2 3, 3 0 (one pair per line). For 1, 2 and 3, the remainder '
                  'after dividing by 4 is the number itself. 4 % 4 is 0, so after West comes North. '
                  'Get students standing and turning clockwise a quarter at a time, calling out 0, '
                  '1, 2, 3, 0: the kinesthetic bit cements the wrap.'},

        {'kind': 'check',
         'question': 'The robot faces West (3) and makes one clockwise turn. What does '
                     '`(heading + 1) % 4` give?',
         'options': ['4', '0, North: 4 % 4 is 0, so the heading wraps around',
                     '3, because West is the last heading',
                     'An error, because there is no heading 4'],
         'answer': 1,
         'explanation': '3 + 1 is 4, and the remainder of 4 divided by 4 is 0. One clockwise turn '
                        'from West faces North.'},

        {'kind': 'steps', 'title': 'Step 3 · Write it and run it',
         'tag': 'Activity',
         'steps': [
             'Write `turn_to()` from its outline, using `(current_heading + 1) % 4`',
             'Predict: how many `turning clockwise` lines will Leg 2 print, from (2, 3) to (1, 0)?',
             'Run `test_delivery()` and compare',
         ],
         'callout': 'Already facing the right way? The condition is False on the first check: no '
                    'special case needed',
         'tone': 'teal',
         'notes': 'Each turning: line from last lesson becomes zero to three turning clockwise '
                  'lines. Leg 2 prints six: three to face West, three more to face South. The run '
                  'still ends with new position: (0, 0) heading: S. The finished turn_to() and the '
                  'full printout are behind a reveal on the lesson page.'},

        {'kind': 'steps', 'title': 'Step 4 · Break it on purpose',
         'tag': 'Activity',
         'steps': [
             'Change the update line to `current_heading = current_heading + 1`, with no `% 4`',
             'Predict what happens at Leg 1\'s third move, East to North',
             'Run it, and press **Stop** when you\'ve seen enough',
             'Put `% 4` back and run it again',
         ],
         'notes': 'turning clockwise scrolls forever. The heading goes 1, 2, 3, 4, 5... and never '
                  'comes back to 0, so the loop\'s condition never becomes False. On the floor, '
                  'that\'s a robot spinning in place, and the screen version is much easier to stop '
                  'and read. Show students where Stop is before they run it.'},

        {'kind': 'check',
         'question': 'A student\'s printout shows `turning clockwise` forever after the first move. '
                     'What\'s the likely bug?',
         'options': ['The planner returned the wrong path',
                     '`turn_to()` never changes `current_heading` inside the loop, so the '
                     'condition never becomes False',
                     '`HEADING_NAMES` is in the wrong order',
                     'The robot is not on the grid'],
         'answer': 1,
         'explanation': 'The loop ends only when current_heading equals desired_heading. If the '
                        'heading never changes, or counts past 3 without wrapping, it never matches '
                        'and the loop never ends.'},

        {'kind': 'wrapup',
         'questions': [
             'How does `turn_to()` know when to stop?',
             'Why `(heading + 1) % 4`?',
             'Why does the robot sometimes turn three times?',
         ],
         'next': 'the stubs out, the robot on the grid',
         'notes': 'Answers: its loop runs until the heading equals the one it wants; already facing '
                  'it means zero turns. Each clockwise turn adds 1, and % 4 wraps 4 back to 0. The '
                  'loop always turns clockwise, so a quarter turn left takes three quarter turns '
                  'right. The long way round is on purpose: it is the simplest turn that always '
                  'works. Students will spot the three-turn corners; agree, and point them at the '
                  'optional challenge in Lesson 4-6. Three sensor-ended turns take three times as '
                  'long as one and give the line sensors three chances to miss.'},
    ],
}
