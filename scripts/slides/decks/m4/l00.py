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
             'Use **problem decomposition** to break a big problem into parts: say what each '
             'part takes in and hands back, build and test each alone, then connect them',
         ],
         'notes': '20 to 25 minutes, problem decomposition, no coding yet. This is an advance '
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

        {'kind': 'bullets', 'title': 'Far-apart destinations, one-hop paths',
         'bullets': [
             '`destinations` is a **supplied list**: the places the robot must reach, in order',
             'Each destination can be **many intersections** from the one before it',
             'For each destination, the planner hands back a **list of adjacent intersections**: '
             'every entry is **one hop** from the one before',
             'So the loop turns one far-away destination into one list of single hops, and the '
             'driver drives those hops one block at a time',
         ],
         'callout': 'One destination in, one list of single hops out, once per destination',
         'tone': 'teal',
         'notes': 'This is the idea the whole module rests on. The destinations list says where to go, '
                  'not how to get there; the planner fills in every intersection in between. In the '
                  'example, (2, 0) to (2, 3) is three intersections apart, and its path is '
                  '[(2, 1), (2, 2), (2, 3)].'},

        {'kind': 'figure', 'title': 'Three destinations, three lists of hops',
         'figure': './decks/m4/fig/destinations-hops.svg',
         'caption': 'The destinations list says where to go. For each one, the planner returns the '
                    'adjacent intersections that get there.',
         'notes': 'Point at leg 2: the destination (2, 3) is three intersections from (2, 0), and the '
                  'planner returns three entries, each one block from the last. The path never '
                  'includes the starting intersection, only the ones to drive to.'},

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

        {'kind': 'bullets', 'title': 'Breaking a big problem into parts',
         'bullets': [
             'Where did the two halves come from? Nobody writes "drive to every destination, all '
             'by itself" as one big function and gets it right',
             'Too much to hold in your head, and when it goes wrong you would not know where to look',
             'So we split it: breaking a big problem into smaller parts you build one at a time '
             'is **problem decomposition**',
             'You will also hear **top-down design**: start from the whole goal, work down to the '
             'pieces',
         ],
         'size': 26},

        {'kind': 'steps', 'title': 'Four steps, for any project', 'tag': 'The method',
         'steps': [
             '**State the whole problem in one sentence.** If you can\'t, you don\'t know yet what '
             'you\'re building.',
             '**Name the parts, and say what each one takes in and hands back.** The step that '
             'matters most: it is how the parts fit together later.',
             '**Build and test each part on its own.** A part tested alone is one you can trust '
             'when something goes wrong.',
             '**Connect them.** If steps 2 and 3 were done well, this is the short one.',
         ]},

        {'kind': 'table', 'title': 'The method, applied to Module 4',
         'headers': ['Step', 'In Module 4'],
         'widths': [1, 3.4],
         'rows': [
             ['1 · The whole problem', 'Visit each destination in order, on its own'],
             ['2 · The parts', '**Planner:** position and destination in, list of intersections '
                               'out. **Driver:** that list, position and heading in; where it '
                               'ended up out'],
             ['3 · Build and test each', 'Planner in 4-4 to 4-6, on screen. Driver in 4-7 and '
                                         '4-8, one leg at a time'],
             ['4 · Connect them', 'Plan, print, drive in 4-8, then the seven lines in 4-9'],
         ],
         'size': 19},

        {'kind': 'figure', 'title': 'Parts can have parts',
         'figure': '/img/lesson-m4-00/decomposition.svg',
         'caption': 'The planner is small enough to build in one go; the driver gets split once more.',
         'notes': 'If a part is still too big to write and test in one sitting, split it again '
                  'with the same four steps. Stop when you can say what a piece does in one '
                  'sentence and test it on its own. What passes between the parts is the '
                  'agreement: the planner only ever hands the driver a list of intersections, '
                  'decided in step 2 before either half was written. That is why Module 5 can '
                  'swap in a new planner and the driver does not change at all.'},

        {'kind': 'check',
         'question': 'Your next project: the robot drives the grid and blinks its light at every '
                     'intersection with a box on it. You\'ve written the one-sentence goal. '
                     'Following the method, what comes next?',
         'options': ['Write the code for the first function',
                     'Name the parts, and what each one takes in and hands back',
                     'Run the whole program on the robot to see what happens',
                     'Pick the robot\'s top speed'],
         'answer': 1,
         'explanation': 'Step 2 comes before any code. Deciding what each part takes in and hands '
                        'back is what lets you build and test the parts separately, and then '
                        'connect them with very little work.',
         'notes': 'Put the four steps on the wall for the whole module. Lessons 4-4, 4-7 and 4-8 '
                  'each open the next step with a short callout. If there is time, have pairs '
                  'decompose something that is not a robot (a class trip, a birthday party) into '
                  'parts with what goes in and what comes out; most find step 2 is the hard one. '
                  'Students met the idea in Lesson 1-7 ("break it into functions"); new here is '
                  'naming what passes between the parts.'},

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
             'What are the four steps of problem decomposition?',
         ],
         'next': 'coordinates: a name for every spot on the grid',
         'notes': 'Answers: visit multiple destinations on its own. compute_manhattan_path '
                  'plans; drive_path drives. State the whole problem; name the parts and what '
                  'each takes in and hands back; build and test each alone; connect them. Reference this overview at the start of every lesson: "remember the '
                  'big picture? today we build this piece." That thread turns nine separate '
                  'topics into one system. Return to the seven-line program in Lesson 4-9.'},
    ],
}
