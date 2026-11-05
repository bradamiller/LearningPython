DECK = {
    'module': 4, 'lesson': 1,
    'doc': 'module-04-manhattan/lesson-01-coordinates',
    'title': 'Coordinates on the Grid',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Explain what a coordinate system is and why a robot needs one',
             'Name any intersection with an `(x, y)` pair',
             'Tell x (across) from y (away from you), and remember order matters',
             'Count the steps between two positions (the Manhattan distance)',
         ],
         'notes': '40 to 50 minutes, no coding: mental model first. When students ask "when do '
                  'we code?", answer "next lesson; today you are building the map the code will '
                  'use."'},

        {'kind': 'bullets', 'title': 'A name for every spot',
         'bullets': [
             'To tell the robot **where to go**, you need a way to name every spot on the grid',
             'Today: that system, **(x, y) coordinates**',
             'With paper and the physical grid, no code yet',
         ],
         'callout': 'A solid mental model here makes tuples, lists and the Manhattan algorithm '
                    'click later',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Two numbers name any spot',
         'lead': 'You already know coordinate systems:',
         'lead_h': 0.75,
         'bullets': [
             'Battleship ("B4"), chess ("e5"), a spreadsheet cell ("A1")',
             'GPS latitude and longitude',
             'Two numbers are enough to pinpoint any spot on a flat surface',
             'Our grid uses **(x, y)**, the same order as a graph in math class',
         ],
         'callout': '`(0, 0)` is the **bottom-left corner, the one nearest you** as the grid '
                    'lies in front of you',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'x is across, y is away from you',
         'bullets': [
             '**x** (first number): how far **across to the right** from the left edge',
             ['The left column is x = `0`'],
             '**y** (second number): how far **away from you** from the near edge',
             ['The bottom row, nearest you, is y = `0`'],
             'North is away from you, up the page',
         ],
         'callout': 'So x counts **east** and y counts **north**',
         'tone': 'teal'},

        {'kind': 'frames', 'title': 'How every intersection gets its name',
         'figure': './decks/m4/fig/naming-intersections.svg',
         'crop': (0.0, 0.0, 0.62, 1.0),
         'frames': [(0.375, 'x counts across, y counts away'),
                    (0.71, '`(2, 3)` and `(3, 2)` differ'),
                    (0.96, 'Every intersection has a name')],
         'callout': 'Start at the corner nearest you, count across for x, then away for y',
         'tone': 'teal',
         'notes': 'The lesson figure is an animation that walks through six ideas; these are '
                  'three of its moments, with its side panel cropped off. If you can, have '
                  'students stand at the near edge, physically walk the grid and call out their '
                  'coordinates: kinesthetic beats diagrams here.'},

        {'kind': 'figure', 'title': 'Across first, then away',
         'figure': './decks/m4/fig/coordinates-xy.svg',
         'caption': 'Bottom-left is (0, 0): we count from zero.',
         'notes': 'This slide uses a copy of the lesson figure with its text halos redrawn for '
                  'the slide renderer.'},

        {'kind': 'bullets', 'title': 'Two things to burn in',
         'bullets': [
             'We **count from zero**: the bottom-left is `(0, 0)`, not `(1, 1)`',
             '**Order matters**: `(2, 3)` and `(3, 2)` are **different** spots',
         ],
         'callout': 'x first, y second; x is across, y is away from you',
         'tone': 'orange',
         'notes': 'Getting x and y in the right order is the number one stumble. Repeat the '
                  'convention constantly and consider posting it. Students who have graphed in '
                  'math class know the order; what is new is counting from zero and that (0, 0) '
                  'is the corner nearest them. Zero-indexing trips most of them because they '
                  'count from 1 by habit, so name why: Python indexes from 0, and matching now '
                  'avoids pain later.'},

        {'kind': 'check',
         'question': 'In the coordinate (2, 3), what does the 2 mean?',
         'options': ['The y: 2 steps away from you',
                     'The x: 2 steps right from the left edge',
                     'The total number of steps',
                     'Nothing: the order is flexible'],
         'answer': 1,
         'explanation': 'x comes first. (2, 3) means x = 2 (two right), y = 3 (three away from '
                        'you, up the page).'},

        {'kind': 'check',
         'question': 'Are (2, 3) and (3, 2) the same position?',
         'options': ['Yes: same two numbers',
                     'No: (2,3) is x 2, y 3; (3,2) is x 3, y 2, different spots',
                     'Only on a square grid',
                     'Yes, if the robot is facing north'],
         'answer': 1,
         'explanation': 'Order matters. Swapping the numbers names a completely different '
                        'intersection.'},

        {'kind': 'bullets', 'title': 'Counting steps: Manhattan distance',
         'bullets': [
             'The robot follows lines: **no diagonals**',
             'So the distance between two spots is the steps across plus the steps up or down',
             'From `(0, 0)` to `(2, 3)`: 2 right + 3 up = **5 steps**',
             'This "blocks you\'d walk" total is the **Manhattan distance**, named for walking '
             'a city grid where you can\'t cut through buildings',
         ],
         'callout': 'steps = (x difference) + (y difference)',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'How many steps from (0, 0) to (3, 2), moving only along grid lines?',
         'options': ['5', '6', '1', '3'],
         'answer': 0,
         'explanation': '3 right + 2 up = 5 steps. That sum is the Manhattan distance.'},

        {'kind': 'steps', 'title': 'Activity · Map it',
         'lead': 'Grab a blank grid and label every intersection with its `(x, y)`. Check '
                 'yourself: the top-right of a 4×4 grid, the far corner, should be `(3, 3)`. '
                 'Then answer:',
         'lead_h': 1.2,
         'steps': [
             'What\'s the bottom-right corner\'s coordinate?',
             'If the robot is at `(2, 1)`, what\'s directly to its left? Directly below it, '
             'toward you?',
             'From `(1, 1)` to `(3, 0)`: how many steps across, how many up or down, how many '
             'total steps?',
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

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Navigation', 'GPS & maps',
              'Latitude and longitude are just two numbers naming any spot on Earth.'),
             ('Cities', 'Street grids',
              '"5th Ave and 42nd St" is a coordinate: the reason this is called Manhattan '
              'distance.'),
             ('Computers', 'Screens & spreadsheets',
              'Every pixel and every cell is addressed by a row/column pair, counted from '
              'zero.'),
         ]},

        {'kind': 'wrapup',
         'questions': [
             'Which number comes first, and what does it mean?',
             'Why start counting at 0?',
             'How do you find the number of steps between two spots?',
         ],
         'next': 'storing a coordinate like (2, 3) in Python: a tuple',
         'notes': 'Answers: x, how far across to the right. To match how Python indexes, '
                  'avoiding confusion later. x difference + y difference. Formative: name '
                  'coordinates from pointed positions and vice versa, always x first, and '
                  'compute a distance. Exit ticket: "Manhattan distance from (0,0) to (3,3)?" '
                  '(6).'},
    ],
}
