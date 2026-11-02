DECK = {
    'module': 4, 'lesson': 0,
    'doc': 'module-04-manhattan/lesson-00-overview',
    'title': 'The Big Picture',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Describe the goal of Module 4: autonomous multi-destination navigation',
             'Name the two halves, the **planner** (`compute_manhattan_path`) and the '
             '**driver** (`drive_path`), and each one\'s job',
             'Read the short main program and explain it in plain English',
             'Explain **top-down design**: start with the big picture, then build each piece',
         ],
         'notes': '15 to 20 minutes, top-down design, no coding yet. This is an advance '
                  'organizer: the point is the shape, not the detail. Resist explaining how '
                  'anything works. If students ask how compute_manhattan_path works, the answer '
                  'is "that is exactly Lessons 4-4 and 4-5". Tell them plainly they are not '
                  'meant to understand every line yet: by Lesson 4-9 they will, because they '
                  'will have built each piece.'},

        {'kind': 'bullets', 'title': 'Where we are headed',
         'bullets': [
             'By the end of this module your robot starts at one corner of the grid',
             'It visits **several destinations in order, all by itself**',
             'No remote control, no manual steering',
             'It figures out each route and drives it, intersection by intersection',
         ],
         'callout': 'Before we learn a single new piece, we look at the whole thing',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'How we compute the route',
         'lead': 'The robot plans every route the same simple way:',
         'lead_h': 0.75,
         'bullets': [
             '**Go across until x is right. Then go up or down until y is right.**',
             'That\'s the whole algorithm',
             'It always gives an L-shaped route, or a straight line if the robot is already '
             'in the right column or row',
             'It never takes a step it doesn\'t need',
         ],
         'callout': 'It\'s called the **Manhattan algorithm**, after a real place',
         'tone': 'teal'},

        {'kind': 'figure', 'title': 'Why "Manhattan"?',
         'figure': './decks/m4/fig/manhattan-grid.svg',
         'caption': 'A taxi can\'t cut through the buildings, so every trip is blocks across '
                    'plus blocks up or down.',
         'notes': 'Most of Manhattan is a rectangular grid: long avenues run north and south, '
                  'shorter numbered streets cross them east and west, and every block is packed '
                  'with buildings. New Yorkers give directions this way: "two blocks east, then '
                  'three up." The robot is in exactly the same situation, because it can only '
                  'drive along the tape. Lesson 4-4 builds the algorithm properly. For the '
                  'curious: the grid comes from the Commissioners\' Plan of 1811; it is turned '
                  'roughly 29 degrees from true north, so "Manhattan north" is a local '
                  'convention; and the same distance is called taxicab distance in mathematics. '
                  'The map is a hook, not a lesson. Lesson 4-4 opens with "Why Manhattan?" and '
                  'assumes students have seen this. (This slide uses a copy of the lesson '
                  'figure with its text halos redrawn for the slide renderer.)'},

        {'kind': 'bullets', 'title': 'The big assumption: every street is clear',
         'bullets': [
             'The Manhattan algorithm assumes **nothing is in the way**: every line of tape and '
             'every intersection can be driven',
             'That\'s why it can be so simple: it never has to look for a detour',
             'Real streets aren\'t always clear',
             ['**Module 5** puts obstacles on the grid: the robot plans around them, and even '
              'notices a new one while it\'s driving',
              '**Module 6** (optional) handles streets that are open but slow, where the '
              'shortest route in steps isn\'t the fastest'],
         ],
         'size': 26},

        {'kind': 'code', 'title': 'The whole program, really',
         'lead': 'Here\'s the **entire** main program you\'re building toward. Seven lines:',
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
         'notes': 'In plain English: start at corner (0, 0) facing North; for each destination, '
                  'compute the path from where we are, print it, drive it, and remember where '
                  'we ended up. Students do not need to understand compute_manhattan_path or '
                  'drive_path yet. Consider printing these seven lines on a card students keep '
                  'and revisit at the start of each lesson, highlighting the piece they build '
                  'that day.'},

        {'kind': 'figure', 'title': 'The seven lines, on the floor',
         'figure': '/img/lesson-m4-00/delivery-overview-xy.svg',
         'caption': 'Three destinations, three legs, each planned from where the last one ended.'},

        {'kind': 'bullets', 'title': 'Where the seven lines will live',
         'bullets': [
             'In your `robot.py` they are the body of the module\'s **last test function**',
             'The two functions they call live in two new sections above it: '
             '**MANHATTAN PLANNER** and **NAVIGATOR**',
             'Those sit on top of the **LINE TRACKING** and **GRID DRIVING** sections you '
             'already have',
             'The `RUN` block waits for the button, as always',
         ],
         'callout': 'All of that is left out of the seven lines so the shape stands out',
         'tone': 'teal'},

        {'kind': 'cards', 'title': 'Two halves, two jobs',
         'cards': [
             ('Planner', 'compute_manhattan_path',
              'Told where the robot is and where it wants to go, it computes a **list of '
              'intersections** to follow. It never touches the robot.'),
             ('Driver', 'drive_path',
              'Given that list, it **drives the robot** through each intersection, turning and '
              'line-following, and reports where it ended up. It never decides the route.'),
         ],
         'height': 3.4},

        {'kind': 'figure', 'title': 'A path goes one way',
         'figure': '/img/lesson-m4-00/two-halves.svg',
         'caption': 'A path goes from planner to driver; where the robot ended up comes back '
                    'for the next plan.'},

        {'kind': 'bullets', 'title': 'Separation of concerns',
         'bullets': [
             'The planner **produces** a path; the driver **consumes** it',
             'Each half has exactly one responsibility: that\'s called **separation of '
             'concerns**',
             'It makes bugs easy to find',
             ['A wrong **route** is a planner problem',
              'A wrong **turn** is a driver problem'],
             'The planner is **told** where the robot is rather than remembering, so the '
             'printed path is always checkable before the robot moves',
         ],
         'size': 27},

        {'kind': 'check',
         'question': 'Which half decides the route, and which one drives the robot?',
         'options': ['drive_path plans; compute_manhattan_path drives',
                     'compute_manhattan_path plans the path; drive_path drives it',
                     'They both do both jobs',
                     'track_to_intersection does everything'],
         'answer': 1,
         'explanation': 'compute_manhattan_path computes the list of intersections (planning); '
                        'drive_path drives through them (execution). One job each.'},

        {'kind': 'bullets', 'title': 'Your roadmap',
         'lead': 'Every lesson in this module builds one piece of that program:',
         'lead_h': 0.7,
         'bullets': [
             '**4-1** coordinates: the `(x, y)` system',
             '**4-2** tuples: storing a position like `(2, 3)` (scratch work)',
             '**4-3** lists: storing a path like `[(1,0), (2,0), (3,0)]` (scratch work too)',
             '**4-4** the Manhattan algorithm, on paper then in code: the MANHATTAN PLANNER '
             'section opens',
             '**4-5** the planner function: its name, its promises, and why it is told where '
             'the robot is',
             '**4-6** testing without a robot: a test harness joins the planner section',
             '**4-7** turning logic, headings as numbers: the NAVIGATOR section opens',
             '**4-8** driving the path, built on your Module 2 line-tracking functions',
             '**4-9** the final project: it all comes together in one test function',
         ],
         'size': 23,
         'notes': 'drive_path reuses the Module 2 functions for the actual driving, so students '
                  'are not starting from scratch: that is the payoff of building a toolkit. If '
                  'the class did the Module 2 class extensions, Lessons 4-5 and 4-8 each have an '
                  'optional class version too.'},

        {'kind': 'wrapup',
         'questions': [
             'What will the robot do by the end of the module?',
             'What are the two halves, and what is each one\'s job?',
             'What does top-down design mean?',
         ],
         'next': 'coordinates: a name for every spot on the grid',
         'notes': 'Answers: visit multiple destinations on its own. compute_manhattan_path '
                  'plans; drive_path drives. Start with the big goal, break it into buildable '
                  'pieces. Reference this overview at the start of every lesson: "remember the '
                  'big picture? today we build this piece." That thread turns nine separate '
                  'topics into one system. Return to the seven-line program in Lesson 4-9.'},
    ],
}
