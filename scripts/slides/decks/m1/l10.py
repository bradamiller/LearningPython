SQUARE_BLOCKS = [
    {'name': 'repeat_4', 'alt': 'repeat 4 times', 'children': [
        {'name': 'straight_cm30', 'alt': 'Straight cm 30'},
        {'name': 'turn', 'alt': 'Turn Deg 90'},
    ]},
]

DECK = {
    'module': 1, 'lesson': 10,
    'doc': 'module-01-driving/lesson-10-python-loops',
    'title': 'Python Loops',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Write a Python `for` loop and use it to repeat robot commands',
             'Explain what `range(n)` produces and why counting starts at `0`',
             'Apply the last two of Python\'s five syntax rules, **colons** and **indentation**, '
             'to say exactly what\'s inside the loop',
             'Nest one loop inside another, using the outer counter to change what the inner '
             'loop draws',
         ],
         'notes': '50 to 60 minutes. The logic is identical to the Repeat block; only the syntax '
                  'changed. This lesson also delivers the two syntax rules Lesson 1-8 promised, '
                  'because a loop is the first thing students have written that has an inside.'},

        {'kind': 'bullets', 'title': 'The Repeat block, in text',
         'lead': 'Here\'s the square you drew in Lesson 1-2 as a Blockly Repeat.',
         'bullets': [
             'Remember how much shorter the Repeat block made shapes?',
             'Python has the same tool: the `for` loop',
             'Same logic, only the syntax changed',
             'Later today: put a loop **inside** another loop, something Blockly made awkward',
         ],
         'split': 0.5,
         'figure': SQUARE_BLOCKS,
         'notes': 'Put the blocks next to the Python on the projector and let students match each '
                  'block to its line before showing the next slide.'},

        {'kind': 'bullets', 'title': 'The same square in Python',
         'lead': 'Breaking down that first line:',
         'lead_h': 0.7,
         'bullets': [
             '`for`: the keyword that starts a loop',
             '`i`: a counter variable (you can use it or ignore it)',
             '`range(4)`: produces the numbers `0, 1, 2, 3`, four of them',
             '`:` the colon, required. More on that in a moment.',
         ],
         'split': 0.5,
         'code': 'for i in range(4):\n'
                 '    drivetrain.straight(30)\n'
                 '    drivetrain.turn(90)',
         'code_size': 24,
         'notes': 'The same square as the Lesson 1-2 Repeat block: Repeat N times becomes '
                  'for i in range(N):, and the blocks inside become the indented lines.'},

        {'kind': 'bullets', 'title': 'The two syntax rules you were promised',
         'bullets': [
             'Lesson 1-8 said there were **five** syntax rules, then showed three',
             'The other two answer a question a flat list of one-line instructions never raised: '
             '**which lines belong to which?**',
             'The `for` loop is the first thing in this course that has an **inside**',
         ],
         'callout': 'Rule 4 is the **colon**. Rule 5 is **indentation**.',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Rules 4 and 5: colons and indentation',
         'bullets': [
             '**4. Colons:** a `:` ends any line that opens a block',
             ['`for i in range(4):` promises that lines belonging to the loop follow',
              '`if` and `def` do the same, as you\'ll see soon enough'],
             '**5. Indentation:** the spaces at the start of a line say what\'s **inside**',
             ['Indented means in; back at the margin means out'],
         ],
         'split': 0.56,
         'code': 'for i in range(4):\n'
                 '    drivetrain.straight(30)\n'
                 '    drivetrain.turn(90)',
         'code_size': 22,
         'callout': 'Python took away the braces `{ }` and made indentation the rule, so a stray '
                    'space is a genuine error, not a style nitpick',
         'tone': 'orange',
         'notes': 'Most languages use curly braces for this and treat indentation as a courtesy. '
                  'In Python the shape of the code on the page and what the code does can never '
                  'disagree. Demonstrate the broken (un-indented) version and the correct one so '
                  'students see the error message.'},

        {'kind': 'check',
         'question': 'What\'s wrong with this line?  `for i in range(4)`',
         'options': ['`range` should be capitalized',
                     'It is missing the colon at the end: `for i in range(4):`',
                     'It needs quotes around the 4', 'Nothing is wrong'],
         'answer': 1,
         'explanation': 'Rule 4: a line that opens a block must end with a colon. for, if and def '
                        'all follow it.'},

        {'kind': 'check',
         'question': 'What numbers does `range(4)` produce?',
         'options': ['1, 2, 3, 4', '0, 1, 2, 3', '0, 1, 2, 3, 4', '4, 3, 2, 1'],
         'answer': 1,
         'explanation': 'range(n) counts from 0 and stops BEFORE n, so range(4) is 0, 1, 2, 3: four '
                        'numbers, which is why the loop runs 4 times.',
         'notes': 'Answer: B. Two things trip nearly everyone: counting from 0 (range(4) is '
                  '0, 1, 2, 3, not 1, 2, 3, 4), and indentation as syntax.'},

        {'kind': 'code', 'title': 'Indentation decides what repeats',
         'lead': 'Rule 5 in action. The only difference is where one line starts:',
         'code': 'for i in range(4):\n'
                 '    drivetrain.straight(30)\n'
                 '    drivetrain.turn(90)\n'
                 'print("Square complete!")     # NOT indented -> runs once, after the loop',
         'code_size': 22,
         'callout': 'The two indented lines repeat four times. The `print` runs once at the end, '
                    'because it\'s not indented.',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'In the code above, how many times does `print("Square complete!")` run?',
         'options': ['Four times: once per loop', 'Once, after the loop finishes', 'Never',
                     'It causes an error'],
         'answer': 1,
         'explanation': 'Because it isn\'t indented, print is outside the loop body: it runs a '
                        'single time once the loop is done.'},

        {'kind': 'code', 'title': 'Use the counter',
         'lead': 'The loop variable isn\'t just for counting: you can **use** it. `print()` takes '
                 'several things at once, separated by commas:',
         'lead_h': 1.2,
         'code': 'for i in range(5):\n'
                 '    print("Drawing side", i + 1, "of 5")\n'
                 '    drivetrain.straight(20)\n'
                 '    drivetrain.turn(72)',
         'code_size': 24,
         'callout': 'Prints `Drawing side 1 of 5`, `Drawing side 2 of 5` ... with a space between '
                    'items. `i + 1` because `range(5)` counts from 0, but people count from 1.',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'The same message, as an f-string',
         'code': 'for i in range(5):\n'
                 '    print(f"Drawing side {i + 1} of 5")\n'
                 '    drivetrain.straight(20)\n'
                 '    drivetrain.turn(72)',
         'code_size': 26,
         'callout': 'The output is identical. An **f-string** (f for **formatted**) is one piece of '
                    'text with a slot in it, where Python drops in the value of `i + 1`.',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'The rules for f-strings',
         'bullets': [
             'Put an `f` right before the opening quote: `f"…"`, with no space between them',
             'Curly braces `{ }` mark a **slot**. Python works out what\'s inside and puts the '
             'answer in the text: `{i}`, `{i + 1}`, `{360 / 5}`',
             'Everything outside the braces is printed **exactly** as you typed it. Python adds '
             'nothing.',
             'Use as many slots as you like: `f"Side {i + 1}: drive {length} cm, turn {angle} degrees"`',
         ],
         'size': 24,
         'callout': 'Forget the `f` and the braces stop working: Python prints them literally. '
                    'Curly braces in your output? Look for a missing `f`.',
         'tone': 'orange'},

        {'kind': 'check',
         'question': '`i` is 2. What does `print("Side {i + 1}")` show?',
         'options': ['Side 3', 'Side 2', 'Side {i + 1}', 'An error'],
         'answer': 2,
         'explanation': 'There is no f before the quote, so it is ordinary text and the braces are '
                        'just characters. Add the f, as in f"Side {i + 1}", and it shows Side 3.'},

        {'kind': 'code', 'title': 'Why bother? 1 · You can read it',
         'lead': 'For a short message the two are interchangeable. As the message grows, an '
                 'f-string looks like the line it will print; the comma version is chopped into '
                 'pieces.',
         'lead_h': 1.2,
         'code': 'print("Side", i + 1, "- drive", length, "cm, turn", angle, "degrees")\n'
                 'print(f"Side {i + 1} - drive {length} cm, turn {angle} degrees")',
         'code_size': 22,
         'callout': 'With commas, you have to assemble the message in your head',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Why bother? 2 · You control the spacing',
         'lead': 'Commas **always** put a space between items, whether you want one or not. Try '
                 'printing a fraction like `1/5`:',
         'lead_h': 1.2,
         'code': 'print("Side", i + 1, "/", 5)     # Side 1 / 5\n'
                 'print(f"Side {i + 1}/5")         # Side 1/5',
         'code_size': 26,
         'callout': 'No way to make the comma version print `1/5`. In an f-string, the only spaces '
                    'are the ones you typed.',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Why bother? 3 · It\'s a value, not just a printout',
         'lead': 'Commas only mean "several things" inside `print()`. An f-string is a complete '
                 'piece of text you can store in a variable and use later:',
         'lead_h': 1.2,
         'code': 'message = f"Drawing side {i + 1} of 5"\n'
                 'print(message)',
         'code_size': 26,
         'callout': 'Later in the course: more f-string tricks, like rounding a long sensor reading '
                    'to two decimal places as you print it',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'You want a loop to run 6 times to draw a hexagon. What goes in the range?',
         'options': ['`range(5)`', '`range(6)`', '`range(7)`', '`range(60)`'],
         'answer': 1,
         'explanation': 'range(6) gives 0 to 5, which is six passes: one per side of the hexagon '
                        '(turning 360 ÷ 6 = 60° each time).'},

        {'kind': 'steps', 'title': 'Try these',
         'steps': [
             'Write a loop to draw a **triangle**: `range(3)`, turn 120',
             'Write a loop to draw a **pentagon**: `range(5)`, turn 72',
             'Add a `print()` inside each loop so you can watch the progress',
         ],
         'notes': 'More support: practice loops that only print numbers before touching the robot '
                  '(for i in range(3): print(i)), and predict output before running. More '
                  'challenge: a loop with an if that changes the side length on alternating '
                  'passes, a preview of Lessons 1-11 and 1-12.'},

        {'kind': 'bullets', 'title': 'A loop inside a loop',
         'lead': 'New problem: draw **four squares, each bigger than the last**: 20 cm, then 25, '
                 'then 30, then 35.',
         'lead_h': 1.2,
         'bullets': [
             'You already know how to draw one square with a loop',
             'You could write that loop four times, changing one number in each copy...',
             'In Lesson 1-2, the answer to "the same thing, over and over" was a loop. It still is.',
         ],
         'callout': 'The difference this time: the thing being repeated **is itself a loop**',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Four squares, one program',
         'code': 'from XRPLib.defaults import *\n'
                 '\n'
                 'board.wait_for_button()\n'
                 '\n'
                 'for square in range(4):          # outer loop -- one pass per square\n'
                 '    size = 20 + square * 5       # 20, 25, 30, 35\n'
                 '    for side in range(4):        # inner loop -- one pass per side\n'
                 '        drivetrain.straight(size)\n'
                 '        drivetrain.turn(90)',
         'code_size': 22,
         'callout': 'Before you run it, predict: how many sides will the robot drive in total?',
         'tone': 'orange',
         'notes': 'size = 20 + square * 5 is straight out of Lesson 1-9\'s precedence section.'},

        {'kind': 'bullets', 'title': 'Read it from the inside out',
         'bullets': [
             'The **inner** loop is the square you already wrote: four sides, four corners',
             'The **outer** loop runs that entire square four times',
             '`square` counts `0, 1, 2, 3`, so `20 + square * 5` gives a different size on every pass',
             '`size` is indented **once**: outer loop, recalculated once per square',
             'The `drivetrain` lines are indented **twice**: inner loop, four times per square, '
             'sixteen sides in all',
         ],
         'size': 24,
         'callout': 'A square finishes where it started, so each new square sets off from the same '
                    'corner and the four nest inside each other',
         'tone': 'teal'},

        {'kind': 'figure', 'title': 'Pass 1 of the outer loop: `square = 0`',
         'figure': '/img/lesson-10/nest-two-squares.svg',
         'frame': 0.3, 'crop': (0.0, 0.085, 1.0, 1.0),
         'caption': '`size` is 20, and `side` counts 0 to 3 as the inner loop draws the first square.',
         'notes': 'On the lesson page this is an animation of the first two passes, with the '
                  'running line highlighted and the counters shown. This slide and the next are '
                  'two moments from it. Trace it out loud together: square = 0, size 20, four '
                  'sides; square = 1, size 25, four sides.'},

        {'kind': 'figure', 'title': 'Pass 2 of the outer loop: `square = 1`',
         'figure': '/img/lesson-10/nest-two-squares.svg',
         'frame': 0.95, 'crop': (0.0, 0.085, 1.0, 1.0),
         'caption': 'Watch which counter changes when: `size` once per square, `side` four times '
                    'inside every square.',
         'notes': 'size was worked out again at the top of the pass: 25. The 25 cm square starts '
                  'from the same corner, around the first. The animation stops after two squares; '
                  'the program goes on to 30 and 35.'},

        {'kind': 'check',
         'question': 'In the nested program, how many times does `drivetrain.straight()` run in '
                     'total?',
         'options': ['Four times: once per square',
                     'Sixteen times: four sides in each of four squares',
                     'Eight times', 'Once, because it is inside two loops'],
         'answer': 1,
         'explanation': 'The inner loop runs four times per pass of the outer loop, and the outer '
                        'loop runs four times: 4 × 4 = 16 sides.',
         'notes': 'Answer: B. Have students predict the total before running; 16 surprises people '
                  'who expect 8. The slippery idea is not the syntax, it is that the outer loop\'s '
                  'body is a whole loop.'},

        {'kind': 'check',
         'question': 'What happens if you indent the `size` line twice, so it lines up with the '
                     '`drivetrain` lines?',
         'options': ['Nothing changes', 'The program will not run at all',
                     'Every square comes out the same size', 'The robot draws only one square'],
         'answer': 0,
         'explanation': 'It still computes the same value, just four times per square instead of '
                        'once: wasteful, but harmless. Indentation changes WHEN a line runs. (Move '
                        'it ABOVE the outer loop, though, and every square would be the same size.)',
         'notes': 'This is deliberately a near-miss. Say out loud that moving size deeper does not '
                  'break anything, because students often believe any indentation change breaks a '
                  'program. The change that does matter is moving it above the outer loop.'},

        {'kind': 'steps', 'title': 'Activity · Draw a nest of squares',
         'steps': [
             'Type the nested-loop program and run it. **Before** you press the button, write down '
             'two predictions: the **total distance** the robot will drive, and how many **turns** '
             'it will make. Check them against what you see.',
             'Change it to draw **six** squares. What did you have to change, and what stayed the '
             'same?',
             '**Challenge:** make the squares **shrink** instead of grow, so the largest is drawn '
             'first. There are two ways: change the arithmetic, or count down.',
         ],
         'notes': 'Step 1 predictions, for the teacher: 4 × (20 + 25 + 30 + 35) = 440 cm and 16 '
                  'turns. Less than 440 cm on the floor is wheel slip and corner error, and the '
                  'biggest square rarely closes perfectly: that is the encoder and wheel-slip '
                  'reality, not a bug. Step 2 is the real check: only the outer range changes; '
                  'the inner loop and the size formula are untouched, which is the payoff of '
                  'nesting. The two range(4)s mean different things: one counts squares, the '
                  'other counts sides. Step 3 is for groups that finish early; both the '
                  'arithmetic answer and counting down are right.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Web', 'Feeds & lists', 'A social feed loops over posts, drawing each one with the '
                                      'same code.'),
             ('Data', 'Processing records', 'Analyzing a million rows is one loop that runs a '
                                            'million times, with no extra code.'),
             ('Robotics', 'Sensor polling', 'Robots loop constantly: read sensors, decide, act, '
                                            'repeat, thousands of times a second.'),
         ],
         'notes': 'Loops are how software handles "do this for every..." without endless '
                  'copy-paste.'},

        {'kind': 'wrapup',
         'questions': [
             'What does `range(4)` produce, and how many times does the loop run?',
             'What decides which lines are inside the loop?',
             'In a nested loop, which loop runs more often: the inner one or the outer one?',
             'How did the outer loop change the size of each square?',
         ],
         'next': 'Python functions with parameters, the text version of Lessons 1-3 to 1-5',
         'notes': 'Answers: 0, 1, 2, 3, so four times. Indentation. The inner one, once per side, '
                  'per square. Its counter was used in the arithmetic that set size. Formative: '
                  'correct for syntax, the right range for a shape, correct reading of '
                  'indentation, and whether a student can say which loop a line belongs to and '
                  'why. Exit ticket: "Write a loop to draw a hexagon" (look for range(6) and a '
                  '60 degree turn); stretch: three hexagons of different sizes. Next lesson, the '
                  'nested squares program is crying out to become square(side_length) called '
                  'from a loop.'},
    ],
}
