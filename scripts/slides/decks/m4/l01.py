DECK = {
    'module': 4, 'lesson': 1,
    'doc': 'module-04-manhattan/lesson-01-coordinates-and-tuples',
    'title': 'Coordinates and Tuples',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Name any intersection with an `(x, y)` pair, and tell x (across) from y (away from you)',
             'Create a tuple to hold an `(x, y)` coordinate',
             'Read its parts: the x coordinate is `position[0]`, the y coordinate is '
             '`position[1]`; or unpack both at once',
             'Explain **immutability** and why it suits coordinates',
             'Compare positions with `==`',
         ],
         'notes': '60 to 70 minutes: the grid on paper first, then tuples in Python. Practice '
                  'code goes in a new file; nothing goes into robot.py until Lesson 4-3. When '
                  'students ask "when do we code?" during the paper part, answer "once you can '
                  'name every spot: that is the map the code will use."'},

        {'kind': 'bullets', 'title': 'A name for every spot',
         'bullets': [
             'To tell the robot **where to go**, you need a way to name every spot on the grid',
             'Today: that system, **(x, y) coordinates**',
             'On paper first, then stored in Python as a **tuple**',
         ],
         'callout': 'A solid mental model here makes tuples, lists and the Manhattan algorithm '
                    'click later',
         'tone': 'teal'},

        {'kind': 'figure', 'title': 'Two numbers name any spot',
         'figure': '/img/lesson-m4-01/coordinate-axes.svg',
         'caption': 'x increases to the right and y increases up.',
         'notes': 'One paragraph on the page: like Battleship ("B4") or a spreadsheet cell '
                  '("A1"), two numbers name every intersection, counted from (0, 0), the corner '
                  'nearest you. x counts across to the right, y counts up, away from you, both '
                  'from zero. Order matters: (2, 3) and (3, 2) are different spots. Getting x '
                  'and y in the right order is the number one stumble; what is new for most '
                  'students is counting from zero, so name why: Python indexes from 0. If you can, '
                  'have students stand at the near edge, walk the grid and call out their '
                  'coordinates.'},

        {'kind': 'check',
         'question': 'In the coordinate (2, 3), what does the 2 mean?',
         'options': ['The y: 2 steps away from you',
                     'The x: 2 steps right from the left edge',
                     'The total number of steps',
                     'Nothing: the order is flexible'],
         'answer': 1,
         'explanation': 'x comes first. (2, 3) means x = 2 (two right), y = 3 (three away from '
                        'you, up the page).'},

        {'kind': 'steps', 'title': 'Activity · Map it',
         'lead': 'Grab a blank grid and label every intersection with its `(x, y)`. Check '
                 'yourself: the top-right of a 4×4 grid, the far corner, should be `(3, 3)`. '
                 'Then answer:',
         'lead_h': 1.2,
         'steps': [
             'What\'s the bottom-right corner\'s coordinate?',
             'If the robot is at `(2, 1)`, what\'s directly to its left? Directly below it, '
             'toward you?',
             'From `(1, 1)` to `(3, 0)`: how many steps across, how many up or down?',
         ],
         'callout': 'Printable worksheet, grid and questions: [learningpython.bradhouse.com/printables/lesson-4-1-blank-grid.pdf]'
                    '(https://learningpython.bradhouse.com/printables/lesson-4-1-blank-grid.pdf)',
         'tone': 'teal',
         'notes': 'The answers are in the lesson\'s "Check your answers" box; students answer '
                  'all three first. More support: start on a 3×3 grid, color-code each column, '
                  'or hand out a partially filled grid. More challenge: an 8×8 grid; how many '
                  'intersections on an N×N grid; and the teaser, how many different shortest '
                  'paths from (0,0) to (2,3)? There are many equal-length paths; the Manhattan '
                  'algorithm will pick one specific route, across first, then up or down.'},

        {'kind': 'check',
         'question': 'The robot is at (3, 1) and needs to get to (3, 3). Which way does it go?',
         'options': ['Two steps east, to the right',
                     'Two steps north, away from you',
                     'Two steps south, toward you',
                     'It is already there'],
         'answer': 1,
         'explanation': 'x is the same, so it doesn\'t move across at all. y goes from 1 to 3, '
                        'so it moves 2 steps away from you, which is north.'},

        {'kind': 'bullets', 'title': 'From the grid to Python',
         'bullets': [
             'You can name any grid spot with `(x, y)`',
             'Now you\'ll store one in Python, using a **tuple**: a single value that packages '
             'two numbers',
         ],
         'callout': 'Try this lesson\'s code in a new file, not `robot.py`',
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
         'callout': 'That\'s **tuple unpacking**: the first variable gets index 0, the second gets '
                    'index 1',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'It does exactly what two lines do',
         'bullets': [
             'The variable names are yours to choose: `dest_x, dest_y = destination` works the same way',
             'There must be **exactly as many variables as parts**',
             'Two variables and a three-part tuple, or three variables and a two-part tuple: Python '
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
         'explanation': 'The variables take the parts in order: a gets index 0, which is 3, and b '
                        'gets index 1, which is 2. The variables don\'t have to be called x and y.'},

        {'kind': 'code', 'title': 'Tuples can\'t change',
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

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Navigation', 'GPS & maps',
              'Latitude and longitude are two numbers naming any spot on Earth, passed around '
              'as one unit.'),
             ('Computers', 'Screens & spreadsheets',
              'Every pixel and every cell is addressed by a row/column pair, counted from '
              'zero.'),
             ('Graphics', 'Colors',
              'Colors (r, g, b) and screen points (x, y) are stored exactly like coordinate '
              'tuples.'),
         ]},

        {'kind': 'wrapup',
         'questions': [
             'Which number comes first, and what does it mean?',
             'How do you get x and y out of a tuple?',
             'What does immutable mean, and why is it good for coordinates?',
             'Why is `(2, 3) == (3, 2)` False?',
         ],
         'next': 'a whole path, many tuples, in a list',
         'notes': 'Answers: x, how far across to the right. The x coordinate is position[0] and '
                  'the y coordinate is position[1], or unpack both. It can\'t change; a position '
                  'should stay fixed. The elements must match in order. Formative: name '
                  'coordinates from pointed positions, always x first; correct tuple syntax, the '
                  'right index for x versus y, and reading ==. Exit ticket: "Write the tuple for '
                  'the spot 3 across and 1 up, then the line that gets its y" (spot = (3, 1), '
                  'spot[1]).'},
    ],
}
