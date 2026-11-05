DECK = {
    'module': 3, 'lesson': 0,
    'doc': 'module-03-grid-driving/lesson-00-overview',
    'title': 'Same Code, Bigger Floor',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Describe what the robot will do by the end of Module 3',
             'Explain why the module needs so little new driving code',
             'Describe a route on the grid as drives and turns, counted in intersections',
             'Say who plans the route in this module, and who will plan it in Module 4',
         ],
         'notes': '10 to 15 minutes, no coding yet. Module 3 is the lightest module, so this is '
                  'short too. Two ideas to leave on the board: reuse (say it before Lesson 3-1 '
                  'does, so students notice when it comes true) and who plans the route. Do not '
                  'explain why a grid intersection looks like the cross: Lesson 3-1 opens with '
                  'that. Tape the 4 x 4 grid before Lesson 3-1 (see Setting up in the teacher '
                  'guide); it stays down for Modules 3 to 6.'},

        {'kind': 'bullets', 'title': 'From a circle to a grid',
         'bullets': [
             'Module 2 ended with a robot that follows a line, finds a cross, parks on it and '
             'turns onto the next line',
             'That was all on **one taped circle**',
             'Now the floor becomes a **grid**: taped lines running across and up, crossing '
             'each other all over',
         ],
         'callout': 'Four short lessons, because you already wrote the hard part',
         'tone': 'teal'},

        {'kind': 'figure', 'title': 'Where this module ends up',
         'figure': '/img/lesson-m3-04/square-run.svg',
         'crop': (0.02, 0.07, 0.585, 0.875),
         'caption': 'A square: two intersections per side, a right turn at every corner, and back '
                    'where it started.',
         'notes': 'This is the Lesson 3-4 project.'},

        {'kind': 'bullets', 'title': 'Reuse is the whole idea',
         'bullets': [
             'LINE SENSOR and LINE TRACKING already follow a line, stop at a cross and turn onto '
             'the next line',
             'A grid is made of nothing else, so they come across **unchanged**',
             'New: a small third section, **GRID DRIVING**',
             ['"Drive through three intersections" in one line',
              'Tests that string drives and turns into routes',
              'None of it reads a sensor'],
         ],
         'callout': 'Write a piece well once, test it, then use it for things you hadn\'t thought of',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Routes counted in intersections',
         'bullets': [
             'A route is a list like: **drive two intersections, turn right, drive one**',
             'Every number is a count of intersections, so it means the same on any grid',
             'Every stop is on an intersection the sensors found, so the robot knows where it '
             'is after each one',
         ]},

        {'kind': 'cards', 'title': 'Who plans the route?',
         'height': 3.4,
         'cards': [
             ('Module 3', 'You plan it',
              'You work out the drives and turns on paper and write them into a test.'),
             ('Module 4', 'The robot plans it',
              'You name an intersection, like "go to (2, 3)", and the robot works out the rest.'),
         ]},

        {'kind': 'check',
         'question': 'In Module 3, how does the robot know to drive two intersections and then '
                     'turn right?',
         'options': ['It sees the corner with its sensors and decides to turn',
                     'You worked out the route and wrote the drives and turns into your test',
                     'It measures the grid with its rangefinder',
                     'It remembers the route from Module 2'],
         'answer': 1,
         'explanation': 'Every route in this module is planned by you. The sensors tell the robot '
                        'where to stop, not where to go. That\'s Module 4.'},

        {'kind': 'table', 'title': 'Your roadmap',
         'headers': ['Lesson', 'What happens'],
         'widths': [3.6, 7.8],
         'size': 18,
         'rows': [
             ['**3-1** Intro to the Grid', 'Drive to the first intersection with the functions '
              'you already have. GRID DRIVING opens.'],
             ['**3-2** Multiple Intersections', 'Drive through a chosen number of intersections '
              'with one call'],
             ['**3-3** Turning on the Grid', 'Drive, turn, drive: an L-shaped path planned on '
              'paper'],
             ['**3-4** Final Project', 'A square, two intersections per side, ending where it '
              'started'],
         ]},

        {'kind': 'wrapup',
         'questions': [
             'What will the robot do by the end of the module?',
             'Why is there so little new driving code?',
             'Who plans the route in Module 3?',
         ],
         'next': 'put the robot on the grid and reach the first intersection',
         'notes': 'Answers: drive a square on the grid and finish where it started. LINE SENSOR '
                  'and LINE TRACKING already handle lines, crosses and turns, and a grid is made '
                  'of those. You do; in Module 4, the robot will.'},
    ],
}
