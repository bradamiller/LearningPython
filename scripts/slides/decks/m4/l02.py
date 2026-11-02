FIG = './decks/m4/fig/tuple-on-grid.svg'

DECK = {
    'module': 4, 'lesson': 2,
    'doc': 'module-04-manhattan/lesson-02-tuples',
    'title': 'Tuples',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Create a tuple to hold an `(x, y)` coordinate',
             'Read its parts with `position[0]` (x) and `position[1]` (y), or unpack both at '
             'once',
             'Explain **immutability** and why it suits coordinates',
             'Compare positions with `==` and compute a Manhattan distance in code',
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
         'callout': '`[0]` = x,  `[1]` = y',
         'tone': 'teal'},

        {'kind': 'figure', 'title': 'A tuple names one intersection',
         'figure': FIG, 'frame': 0.22,
         'caption': '`position[0]` is 2, drawn as 2 across; `position[1]` is 3, drawn as 3 away.',
         'notes': 'The lesson figure is one animation that runs through the whole lesson: make '
                  'a tuple, index it, fail to change it, make a new one, compare two, and count '
                  'the steps between them. This deck shows its moments section by section. '
                  '(The slides use a copy of the figure with its text halos redrawn for the '
                  'slide renderer.)'},

        {'kind': 'check',
         'question': 'Given position = (3, 5), what does position[0] return?',
         'options': ['5', '3', '(3, 5)', 'An error'],
         'answer': 1,
         'explanation': 'Index 0 is the first element, x, so position[0] is 3. position[1] '
                        'would be y, 5.'},

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
         'code_size': 22,
         'callout': 'Lesson 4-4\'s planner starts by unpacking where the robot is and where it\'s '
                    'going',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'After start = (4, 1) and then a, b = start, what is b?',
         'options': ['4', '1', '(4, 1)', 'An error'],
         'answer': 1,
         'explanation': 'The names take the parts in order: a gets index 0, which is 4, and b '
                        'gets index 1, which is 1. The names don\'t have to be x and y.'},

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
                 'new_position = (2, 4)    # one step north -- a brand-new tuple',
         'code_size': 22,
         'callout': 'Like a street address: move, and you get a **new** address. You don\'t edit '
                    'the old one.',
         'notes': 'Expect [0] versus [1] confusion for a few exercises: post "[0] = x, [1] = y" '
                  'on the wall. Flag the bracket rule early: tuples are made with parentheses; '
                  'square brackets are only for indexing (and, next lesson, for lists). The '
                  'immutability payoff is not obvious yet; the street-address analogy is enough '
                  'for now. It really pays off once tuples live inside lists and the algorithm.'},

        {'kind': 'figure', 'title': 'Can\'t change it, so make a new one',
         'figure': FIG, 'frame': 0.55,
         'caption': 'A tuple can\'t be changed, so one step east makes a new tuple, `(3, 3)`, '
                    'beside the old one.'},

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

        {'kind': 'figure', 'title': 'Same spot, or a different one?',
         'figure': FIG, 'frame': 0.72,
         'caption': '`(1, 2) == (1, 2)` is True, the same spot. `(1, 2) == (2, 1)` is False, a '
                    'different spot.'},

        {'kind': 'check',
         'question': 'Does (1, 4) == (4, 1) evaluate to True?',
         'options': ['Yes: they contain the same numbers',
                     'No: the parts must match in order, and these are swapped',
                     'Yes: tuples ignore order', 'It causes an error'],
         'answer': 1,
         'explanation': 'Two tuples are equal only if every element matches in order. (1, 4) is '
                        '1 for x and 4 for y; (4, 1) is 4 for x and 1 for y: different, so '
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

        {'kind': 'figure', 'title': 'Counting the steps',
         'figure': FIG, 'frame': 0.95,
         'caption': 'From (0, 0) to (2, 3): 2 across plus 3 away, 5 steps.'},

        {'kind': 'check',
         'question': 'Using this method, what\'s the Manhattan distance from (1, 1) to (4, 3)?',
         'options': ['7', '5', '3', '2'],
         'answer': 1,
         'explanation': '(4 − 1) across + (3 − 1) up = 3 + 2 = 5 steps.'},

        {'kind': 'steps', 'title': 'Try it',
         'steps': [
             'Store five of your grid positions as tuples',
             'Print each one\'s x and y',
             'Compute a couple of distances',
         ],
         'notes': 'More support: a reference card ("[0] = x, [1] = y"), the interactive shell '
                  'for instant feedback, and starting with just creating and printing tuples. '
                  'More challenge: an (x, y, heading) three-tuple (what does [2] give?), or '
                  'tuples built from input. Watch for: subtracting a bigger start from a smaller '
                  'destination gives a negative distance. Acknowledge it is real and say Lesson '
                  '4-4 deals with it; for now keep destinations up and to the right of the '
                  'start.'},

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
         'notes': 'Answers: [0] and [1]. It can\'t change; a position should stay fixed. The '
                  'elements must match in order. Formative: correct tuple syntax, the right '
                  'index for x versus y, and reading ==. Exit ticket: "Manhattan distance from '
                  '(1,1) to (4,3), show your work" (5).'},
    ],
}
