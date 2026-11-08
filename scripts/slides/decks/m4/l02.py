
DECK = {
    'module': 4, 'lesson': 2,
    'doc': 'module-04-manhattan/lesson-02-tuples',
    'title': 'Tuples',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Create a tuple to hold an `(x, y)` coordinate',
             'Read its parts: the x coordinate of the tuple is `position[0]`, and the y '
             'coordinate is `position[1]`; or unpack both at once',
             'Explain **immutability** and why it suits coordinates',
             'Compare positions with `==` and compute a Manhattan distance in code',
             'Write a function that takes two positions as tuples',
         ],
         'notes': '50 minutes. This is where Module 4 turns into code, but scratch code: '
                  'students try the snippets in a scratch file or at the Python prompt and '
                  'throw them away. Nothing goes into robot.py until Lesson 4-4.'},

        {'kind': 'bullets', 'title': 'From the grid to Python',
         'bullets': [
             'You can name any grid spot with `(x, y)`',
             'Now you\'ll store one in Python, using a **tuple**: a single value that packages '
             'two numbers',
             'Scratch code, this lesson and the next: a scratch file or the Python prompt',
             'The file gets its next section in Lesson 4-4, once there is a function worth '
             'keeping',
         ],
         'callout': 'Nothing here goes into `robot.py`',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'One value, two numbers',
         'lead': 'You **could** use two variables, `x = 2` and `y = 3`, but ten positions would '
                 'need twenty variables. A **tuple** packs both into one value, written with '
                 'parentheses:',
         'lead_h': 1.25,
         'code': 'position = (2, 3)\n'
                 'start = (0, 0)\n'
                 'destination = (3, 2)',
         'code_size': 26, 'width': 7.5},

        {'kind': 'code', 'title': 'Pull the pieces out by index',
         'lead': 'Python counts from zero, just like our grid: index `0` is x and index `1` is y.',
         'code': 'position = (2, 3)\n'
                 'print(position[0])   # 2  -> x, across\n'
                 'print(position[1])   # 3  -> y, away from you',
         'code_size': 24,
         'callout': 'The x coordinate is `position[0]`; the y coordinate is `position[1]`',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'Given position = (3, 1), what does position[0] return?',
         'options': ['1', '3', '(3, 1)', 'An error'],
         'answer': 1,
         'explanation': 'Index 0 is the first element, x, so position[0] is 3. position[1] '
                        'would be y, 1.'},

        {'kind': 'code', 'title': 'Unpacking: both numbers at once',
         'lead': 'Indexing pulls out one part at a time. Often you want both, as ordinary '
                 'variables, in one line:',
         'code': 'position = (2, 3)\n'
                 'x, y = position      # x is 2, y is 3',
         'code_size': 26, 'width': 9,
         'callout': 'That\'s **tuple unpacking**: the first name gets index 0, the second gets '
                    'index 1',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'It does exactly what two lines do',
         'bullets': [
             'The names are yours to choose: `dest_x, dest_y = destination` works the same way',
             'There must be **exactly as many names as parts**',
             'Two names and a three-part tuple, or three names and a two-part tuple: Python '
             'stops with a `ValueError`',
         ],
         'split': 0.58,
         'code': 'x = position[0]\n'
                 'y = position[1]',
         'code_size': 22},

        {'kind': 'check',
         'question': 'After start = (3, 2) and then a, b = start, what is b?',
         'options': ['3', '2', '(3, 2)', 'An error'],
         'answer': 1,
         'explanation': 'The names take the parts in order: a gets index 0, which is 3, and b '
                        'gets index 1, which is 2. The names don\'t have to be x and y.'},

        {'kind': 'code', 'title': 'Tuples don\'t change (and that\'s good)',
         'lead': 'Try to modify a tuple and Python stops you:',
         'code': 'position = (2, 3)\n'
                 'position[0] = 5      # TypeError: \'tuple\' object does not support item '
                 'assignment',
         'code_size': 20,
         'callout': 'Tuples are **immutable**: once made, they can\'t be altered',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'A new spot is a new tuple',
         'lead': 'That\'s right for a coordinate: `(2, 3)` should **always** mean x = 2, y = 3. '
                 'To represent a new spot, you make a new tuple:',
         'lead_h': 1.2,
         'code': 'old_position = (2, 3)\n'
                 'new_position = (3, 3)    # one step east -- a brand-new tuple',
         'code_size': 22,
         'callout': 'Like a street address: move, and you get a **new** address. You don\'t edit '
                    'the old one.',
         'notes': 'Expect [0] versus [1] confusion for a few exercises: post "the x coordinate is '
                  'position[0], the y coordinate is position[1]" on the wall. Flag the bracket rule early: tuples are made with parentheses; '
                  'square brackets are only for indexing (and, next lesson, for lists). The '
                  'immutability payoff is not obvious yet; the street-address analogy is enough '
                  'for now. It really pays off once tuples live inside lists and the algorithm.'},

        {'kind': 'check',
         'question': 'What happens when you run position[0] = 5 on a tuple?',
         'options': ['x changes to 5', 'You get a TypeError: tuples cannot be modified',
                     'It creates a new tuple automatically', 'Nothing happens'],
         'answer': 1,
         'explanation': 'Tuples are immutable, so item assignment raises a TypeError. To '
                        '"change" a position, create a new tuple.'},

        {'kind': 'code', 'title': 'Comparing positions',
         'lead': '`==` checks whether two tuples are the **same** position: both parts must '
                 'match, in order.',
         'code': 'current = (1, 2)\n'
                 'target  = (1, 2)\n'
                 'print(current == target)   # True\n'
                 '\n'
                 'other = (2, 1)\n'
                 'print(current == other)    # False -- order matters!',
         'code_size': 22,
         'callout': 'Later the algorithm asks "have we reached the destination yet?" by '
                    'comparing tuples',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'Does (1, 3) == (3, 1) evaluate to True?',
         'options': ['Yes: they contain the same numbers',
                     'No: the parts must match in order, and these are swapped',
                     'Yes: tuples ignore order', 'It causes an error'],
         'answer': 1,
         'explanation': 'Two tuples are equal only if every element matches in order. (1, 3) is '
                        '1 for x and 3 for y; (3, 1) is 3 for x and 1 for y: different, so '
                        'False.'},

        {'kind': 'code', 'title': 'Activity · Manhattan distance in code', 'tag': 'Activity',
         'lead': 'The paper counting from Lesson 4-1 becomes simple arithmetic on tuple parts:',
         'code': 'start = (0, 0)\n'
                 'destination = (2, 3)\n'
                 '\n'
                 'x_distance = destination[0] - start[0]     # 2\n'
                 'y_distance = destination[1] - start[1]     # 3\n'
                 'total_steps = x_distance + y_distance      # 5\n'
                 'print("Total steps:", total_steps)',
         'code_size': 22},

        {'kind': 'check',
         'question': 'Using this method, what\'s the Manhattan distance from (0, 1) to (3, 3)?',
         'options': ['7', '5', '3', '2'],
         'answer': 1,
         'explanation': '(3 − 0) across + (3 − 1) up = 3 + 2 = 5 steps.'},

        {'kind': 'steps', 'title': 'Try it: write compute_distance()',
         'lead': 'A program, not paper. New MICROPYTHON file in XRP Code; it only prints, '
                 'so the robot won\'t move. Scratch work: not in robot.py.',
         'steps': [
             'Write compute_distance(start, end): print both tuples, then print the '
             'Manhattan distance between them',
             'Put the test from the next slide under it: five calls. Run the program',
             'Check the shell against the output shown. If a distance is off, count it on '
             'your Lesson 4-1 grid and find the wrong part: x or y',
         ],
         'notes': 'More support: a reference card ("the x coordinate is position[0], the y coordinate is position[1]"), the interactive shell '
                  'for instant feedback, and starting with just creating and printing tuples. '
                  'More challenge: an (x, y, heading) three-tuple (what does [2] give?), or '
                  'tuples built from input. Watch for: subtracting a bigger start from a smaller '
                  'destination gives a negative distance. Acknowledge it is real and say Lesson '
                  '4-4 deals with it; for now keep destinations up and to the right of the '
                  'start.'},

        {'kind': 'code', 'title': 'The outline and the test', 'tag': 'Activity',
         'code': 'def compute_distance(start, end):\n'
                 '    # 1. Print start and end\n'
                 '    # 2. Work out the x distance and the y distance\n'
                 '    # 3. Print the total: the Manhattan distance\n'
                 '    pass\n'
                 '\n'
                 '# Test: five calls to compute_distance()\n'
                 'compute_distance((0, 0), (2, 3))\n'
                 'compute_distance((1, 1), (3, 2))\n'
                 'compute_distance((0, 0), (3, 3))\n'
                 'compute_distance((2, 0), (2, 3))\n'
                 'compute_distance((0, 2), (1, 3))',
         'code_size': 18,
         'notes': 'Every end is up and to the right of its start, so no distance comes out '
                  'negative; Lesson 4-4 deals with the other directions. The teacher copy '
                  'is on the Module 4 sample programs page.'},

        {'kind': 'code', 'title': 'What the test prints', 'tag': 'Activity',
         'lead': 'When your function works, the shell shows this:',
         'code': 'From (0, 0) to (2, 3)\n'
                 'Manhattan distance: 5\n'
                 'From (1, 1) to (3, 2)\n'
                 'Manhattan distance: 3\n'
                 'From (0, 0) to (3, 3)\n'
                 'Manhattan distance: 6\n'
                 'From (2, 0) to (2, 3)\n'
                 'Manhattan distance: 3\n'
                 'From (0, 2) to (1, 3)\n'
                 'Manhattan distance: 2',
         'code_size': 18},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Graphics', 'Points & colors',
              'Screen points (x, y) and colors (r, g, b) are stored exactly like coordinate '
              'tuples.'),
             ('Data', 'Records',
              'A row of a dataset, (name, age, score), is a fixed bundle, just like a '
              'coordinate.'),
             ('Maps', 'Lat/long pairs',
              'Every mapped location is a two-value pair passed around as one unit.'),
         ]},

        {'kind': 'wrapup',
         'questions': [
             'How do you get x and y out of a tuple?',
             'What does immutable mean, and why is it good for coordinates?',
             'Why is `(2, 3) == (3, 2)` False?',
         ],
         'next': 'a whole path, many tuples, in a list',
         'notes': 'Answers: the x coordinate is position[0] and the y coordinate is position[1], or unpack both. It can\'t change; a position should stay fixed. The '
                  'elements must match in order. Formative: correct tuple syntax, the right '
                  'index for x versus y, and reading ==. Exit ticket: "Manhattan distance from '
                  '(1,0) to (3,3), show your work" (5).'},
    ],
}
