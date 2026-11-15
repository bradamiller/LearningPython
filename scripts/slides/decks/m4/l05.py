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
                  'with one more stub standing in for the turn itself.'},

        {'kind': 'code', 'title': 'Turning until you face it',
         'lead': 'Each clockwise quarter turn adds 1 to the heading. So: turn clockwise while it '
                 'isn\'t facing the right way.',
         'lead_h': 1.1,
         'code': '# while current_heading is not desired_heading:\n'
                 '#     one clockwise quarter turn\n'
                 '#     current_heading goes up by 1, wrapping 3 back to 0',
         'code_size': 22,
         'notes': 'Get students standing and turning clockwise a quarter at a time, calling out 0, '
                  '1, 2, 3, 0: the kinesthetic bit cements the wrap.'},

        {'kind': 'code', 'title': 'West to North: the wrap',
         'lead': '3 + 1 is 4, and 4 isn\'t a heading. The remainder `%` from Lesson 2-5 wraps it:',
         'code': 'heading = (heading + 1) % 4',
         'code_size': 28,
         'callout': 'For 1, 2 and 3 the remainder is the number itself; `4 % 4` is 0, so after West '
                    'comes North',
         'tone': 'teal'},

        {'kind': 'table', 'title': 'Trace it: from South (2) to East (1)',
         'headers': ['Pass', 'Heading before', 'Heading after, `(h + 1) % 4`', 'Facing East?'],
         'widths': [1, 2.4, 3.6, 2.8],
         'rows': [
             ['1', '2 (S)', '3 (W)', 'no'],
             ['2', '3 (W)', '0 (N)', 'no'],
             ['3', '0 (N)', '1 (E)', 'yes, the loop ends'],
         ],
         'size': 22,
         'callout': 'Three passes: it always goes clockwise, so a quarter turn **left** takes three '
                    'turns right',
         'tone': 'orange',
         'notes': 'The long way round is on purpose: it is the simplest turn that always works. '
                  'Lesson 4-6 has an optional challenge to make it turn whichever way is fewer '
                  'turns. Already facing the right way? The condition is False on the first check '
                  'and the loop does nothing, with no special case. At the end the function returns '
                  'current_heading, which by then equals desired_heading.'},

        {'kind': 'check',
         'question': 'The robot faces West (3) and makes one clockwise turn. What does '
                     '`(heading + 1) % 4` give?',
         'options': ['4', '0, North: 4 % 4 is 0, so the heading wraps around',
                     '3, because West is the last heading',
                     'An error, because there is no heading 4'],
         'answer': 1,
         'explanation': '3 + 1 is 4, and the remainder of 4 divided by 4 is 0. One clockwise turn '
                        'from West faces North.'},

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

        {'kind': 'steps', 'title': 'Step 1 · Predict',
         'tag': 'Activity',
         'lead': 'The robot starts facing North. How many clockwise turns before each of Leg 1\'s '
                 'five moves?',
         'steps': [
             'The moves face **E, E, N, N, N**',
             'Write down a number for each move',
         ],
         'callout': 'Predict before you write any code',
         'tone': 'orange',
         'notes': 'Answer: 1, 0, 3, 0, 0. North to East is one turn. East to East is none: the loop '
                  'doesn\'t run. East to North is three: East, South, West, North.'},

        {'kind': 'steps', 'title': 'Step 2 · Write it and run it',
         'tag': 'Activity',
         'steps': [
             'Write `turn_to()` from its outline',
             'Run `test_delivery()`',
         ],
         'callout': 'Correct: each `turning:` line becomes zero to three `turning clockwise` lines. '
                    'Leg 1 matches your prediction. Still ends heading S.',
         'tone': 'green',
         'notes': 'Every turn count should be three or fewer. The finished turn_to() and the full '
                  'printout are behind a reveal on the lesson page.'},

        {'kind': 'check',
         'question': 'A student\'s printout shows `turning clockwise` forever after the first move. '
                     'What\'s the likely bug?',
         'options': ['The planner returned the wrong path',
                     '`turn_to()` never changes `current_heading` inside the loop, so the '
                     'condition never becomes False',
                     '`HEADING_NAMES` is in the wrong order',
                     'The robot is not on the grid'],
         'answer': 1,
         'explanation': 'The loop ends only when current_heading equals desired_heading. On screen '
                        'that\'s a scrolling printout; on the floor it would be a robot spinning in '
                        'place.'},

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
                  'right. An endless turning clockwise printout usually means the heading isn\'t '
                  'updated in the loop, or is updated without the wrap.'},
    ],
}
