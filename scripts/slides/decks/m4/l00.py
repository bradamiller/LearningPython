DECK = {'module': 4,
 'lesson': 0,
 'doc': 'module-04-manhattan/lesson-00-overview',
 'title': 'The Big Picture',
 'slides': [{'kind': 'title',
             'objectives': ['Describe the problem Module 4 solves: drive to a destination on its '
                            'own, then to several in a row',
                            'Split a complex problem into simpler parts: plan the route first, '
                            'test it with no robot, then drive it',
                            'Name the **planner** (`compute_manhattan_path`), the **driver** '
                            '(`drive_path`), and the list of tuples between them'],
             'notes': '20 to 25 minutes, problem decomposition, a class discussion, no coding yet. '
                      'The lesson opens with the whole problem, leads a class discussion to the '
                      'split this module uses: plan first, test the plan with no robot, then drive '
                      'it. After that it is an advance organizer: the point is the shape, not the '
                      'detail. If students ask how compute_manhattan_path works, the answer is '
                      '"that is exactly Lessons 4-3 and 4-4". Tell them plainly they are not meant '
                      'to understand every line yet: by Lesson 4-7 they will, because they will '
                      'have built each piece.'},
            {'kind': 'figure',
             'title': 'The problem',
             'figure': './decks/m4/fig/manhattan-grid.svg',
             'caption': "A taxi can't cut through the buildings. The robot is in the same spot: it "
                        'can only drive along the tape. Where would you even start?',
             'notes': 'The problem: get the robot from where it starts to a destination on the '
                      'grid, all by itself. A taxi in Manhattan has the same problem: buildings '
                      'fill every block, so it can only drive along the streets. The robot can '
                      'only drive along the tape, and nobody steers it at the corners. One '
                      'destination for now; several in a row comes at the end of the module. New '
                      'Yorkers give directions this way: "two blocks east, then three up." Lesson '
                      '4-3 builds the algorithm properly. For the curious: the grid comes from the '
                      "Commissioners' Plan of 1811; it is turned roughly 29 degrees from true "
                      'north, so "Manhattan north" is a local convention; and the same distance is '
                      'called taxicab distance in mathematics. The map is a hook, not a lesson. '
                      'Lesson 4-3 opens with "Why Manhattan?" and assumes students have seen this. '
                      '(This slide uses a copy of the lesson figure with its text halos redrawn '
                      'for the slide renderer.)'},
            {'kind': 'bullets',
             'title': 'How to find the route',
             'bullets': ['**Go across until x is right. Then go up or down until y is right.**',
                         "That's the whole algorithm"],
             'callout': "It's called the **Manhattan algorithm**: the taxi's route, two blocks "
                        'across, then three up',
             'tone': 'teal',
             'size': 30},
            {'kind': 'bullets',
             'title': 'The big assumption: every street is clear',
             'bullets': ['The algorithm assumes **nothing is in the way**, so it never needs a '
                         'detour',
                         '**Module 5** adds obstacles; **Module 6** (optional) adds slow streets'],
             'size': 28},
            {'kind': 'bullets',
             'title': 'Harder than it sounds',
             'bullets': ['Knowing the route is only part of it',
                         '"Drive over there" sounds like one job, but it is a **somewhat complex '
                         'problem**',
                         'Too much to get right in one go',
                         'One way to tackle it: **break it into simpler sub-problems**, and solve '
                         'each one'],
             'callout': 'That is called **problem decomposition** (or **top-down design**)',
             'tone': 'teal',
             'size': 28},
            {'kind': 'steps',
             'title': 'How would you split it?',
             'tag': 'Class discussion',
             'steps': ['Before the robot moves, could you write down every intersection it will '
                       'drive through?',
                       'How could you check that list is right, **without the robot**?',
                       "Once the list is right, what's left for the robot to do?"],
             'size': 24,
             'notes': '5 to 8 minutes, teacher-led. Ask in order; draw the grid on the board. 1: '
                      'Yes. Expect "two right, then three up"; mark each intersection on the board '
                      'grid. If someone says the robot should decide as it goes, ask "Does it need '
                      'to? Nothing on the grid changes." 2: Trace it on the grid by hand, or have '
                      'the computer print it and compare. Steer to: no robot needed, so the route '
                      'can be tested on a laptop. 3: Just drive it: at each intersection, face the '
                      'next one and follow the tape there. It does not decide anything. Then name '
                      'the split: plan the route, drive the plan, with the list passed between '
                      'them. Ideas about motors, sensors or turning belong to the driving half.'},
            {'kind': 'figure',
             'title': 'Plan first, then drive',
             'figure': '/img/lesson-m4-00/plan-then-drive.svg',
             'caption': 'The plan is a list of (x, y) tuples. One function makes it; another '
                        'drives it.',
             'notes': 'That is one way to split the problem, and the one this module uses. The '
                      'planning function never moves the robot, so it can be tested with no robot: '
                      'print the route and check it against the grid. Once the plan is right, a '
                      'second function takes the plan and drives it; it decides nothing. Each '
                      'intersection is an (x, y) pair, stored as a tuple, so the plan is a list of '
                      'tuples, the one thing the two functions share. Tuples come properly in '
                      'Lesson 4-1 and lists in Lesson 4-2.'},
            {'kind': 'bullets',
             'title': 'Planner and driver',
             'bullets': ['**Planner:** `compute_manhattan_path` returns the list of tuples. Never '
                         'moves the robot.',
                         '**Driver:** `drive_path` drives the list, then reports where the robot '
                         'ended up. Never decides the route.',
                         'One job each is called **separation of concerns**',
                         ['A wrong **route** is a planner problem',
                          'A wrong **turn** is a driver problem']],
             'size': 26},
            {'kind': 'check',
             'question': 'Why plan the whole route first, as its own function, before writing the '
                         'code that drives?',
             'options': ['Because the robot can only run one function at a time',
                         'Because the plan can be checked with no robot, and the driver then '
                         'follows a route you trust',
                         'Because planning makes the robot drive faster',
                         'Because the driving function has to be written last in the file'],
             'answer': 1,
             'explanation': 'The planning function never moves the robot, so you can test it on '
                            'screen and check its list of tuples on paper. Once you trust the '
                            'plan, a wrong move on the floor can only be a driving problem.'},
            {'kind': 'code',
             'title': 'From one destination to several',
             'lead': 'Several destinations is just a loop: plan, drive, repeat. The whole program, '
                     'seven lines:',
             'code': 'position = (0, 0)\n'
                     'heading = 0                      # facing North\n'
                     'destinations = [(2, 0), (2, 3), (0, 3)]\n'
                     '\n'
                     'for dest in destinations:\n'
                     '    path = compute_manhattan_path(position, dest)\n'
                     '    print("Path:", path)\n'
                     '    position, heading = drive_path(path, position, heading)',
             'code_size': 20,
             'callout': 'It is short **because the functions do all the work**',
             'tone': 'teal',
             'notes': 'In plain English: start at corner (0, 0) facing North; for each '
                      'destination, compute the path from where we are, print it, drive it, and '
                      'remember where we ended up. Students do not need to understand '
                      'compute_manhattan_path or drive_path yet. Consider printing these seven '
                      'lines on a card students keep and revisit at the start of each lesson, '
                      'highlighting the piece they build that day.'},
            {'kind': 'figure',
             'title': 'The seven lines, on the floor',
             'figure': '/img/lesson-m4-00/delivery-overview-xy.svg',
             'caption': 'Three destinations, three legs, each planned from where the last one '
                        'ended.'},
            {'kind': 'figure',
             'title': 'The module at a glance',
             'figure': './decks/m4/fig/l05-decomp-1.svg',
             'caption': 'The whole problem. What are its parts?',
             'notes': 'Four slides, one level each, as in Lesson 4-5. Click through as the class '
                      'answers.'},
            {'kind': 'figure',
             'title': 'The module at a glance',
             'figure': './decks/m4/fig/l05-decomp-2.svg',
             'caption': 'Plan, then drive: the split you just made.',
             'notes': 'The planner is small enough to build and test in one go (4-3, 4-4); the '
                      'driver needs breaking down.'},
            {'kind': 'figure',
             'title': 'The module at a glance',
             'figure': './decks/m4/fig/l05-decomp-3.svg',
             'caption': 'Driving breaks into two steps at each intersection: turn to face the next '
                        'one, then drive to it.',
             'notes': 'Driving is Module 2 line tracking, already built.'},
            {'kind': 'figure',
             'title': 'The module at a glance',
             'figure': './decks/m4/fig/l05-decomp-4.svg',
             'caption': 'And turning breaks into two: which way to face, then turn until facing '
                        'it.',
             'notes': 'Each box names the lesson that builds it. Lesson 4-5 opens with this same '
                      'tree.'},
            {'kind': 'bullets',
             'title': "What's next",
             'bullets': ['**4-1 and 4-2:** the background: coordinates, tuples and lists',
                         '**4-3 and 4-4:** write and test the planner',
                         '**4-5 and 4-6:** write and test the driver',
                         '**4-7:** put them together'],
             'size': 30},
            {'kind': 'wrapup',
             'questions': ['What problem does Module 4 solve?',
                           'Why plan the route first, before writing the code that drives?',
                           "What are the two halves, and what is each one's job?"],
             'next': 'coordinates: a name for every spot on the grid',
             'notes': 'Answers: drive from where it starts to a destination on its own, then to '
                      'several in a row. The planner never moves the robot, so its list of tuples '
                      'can be printed and checked with no robot; then the driver only follows a '
                      'plan you trust. compute_manhattan_path plans; drive_path drives. Open each '
                      'lesson with "remember the big picture? Today we build this piece." Return '
                      'to the seven-line program in Lesson 4-7.'}]}
