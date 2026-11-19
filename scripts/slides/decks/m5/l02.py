"""Module 5, Lesson 5-2 · Finding the Path.

Both discussions ("Where's the path?" and "Teaching it to a computer") run one
slide per question, then one slide with the answer. Each question slide's notes
hold that step of the lesson's teacher note. Grids: fig/make_discuss_grids.py.
"""

FIG = './decks/m5/fig/'


def ask(n, total, question, figure=None, notes=None):
    s = {'kind': 'bullets', 'title': f'Question {n} of {total}', 'tag': 'Discuss',
         'bullets': question, 'size': 28}
    if figure:
        s.update(figure=FIG + figure + '.svg', split=0.55)
    if notes:
        s['notes'] = notes
    return s


def answer(n, total, points, rule=None, figure=None, notes=None):
    s = {'kind': 'bullets', 'title': f'Answer {n} of {total}', 'tag': 'Discuss',
         'bullets': points, 'size': 28}
    if figure:
        s.update(figure=FIG + figure + '.svg', split=0.55)
    if rule:
        s.update(callout=rule, tone='green')
    if notes:
        s['notes'] = notes
    return s


DECK = {
    'module': 5, 'lesson': 2,
    'doc': 'module-05-pathfinding/lesson-02-finding-the-path',
    'title': 'Finding the Path',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Walk downhill from the start to find a shortest path, and explain why the path '
             'leaves the start out',
             'Explain why the wave starts at the destination',
             'Explain why a computer takes intersections oldest-first, and why the numbers are '
             'all it needs',
             'Carry out the algorithm exactly as a computer would, by hand, including on a grid '
             'with no path',
         ],
         'notes': '55 to 60 minutes, no coding. Two discussions and two activities: about 10, '
                  '15, 15 and 10 minutes. If time is short, keep "Teaching it to a computer" and '
                  'the review, and shorten the trace to steps 2 to 4.'},

        {'kind': 'bullets', 'title': 'The numbers say how far',
         'bullets': [
             'The robot needs a **path**: a list of intersections to drive to',
             'Today: what\'s the path?',
             'And how would a computer find it?',
         ],
         'callout': 'It ends with the whole algorithm in plain words: Lesson 5-5 turns it into '
                    'Python',
         'tone': 'teal'},

        # --- Discuss · Where's the path? ---
        {'kind': 'bullets', 'title': 'Where\'s the path?', 'tag': 'Discuss',
         'bullets': [
             'Start from the grid you numbered in Lesson 5-1',
             'The wall at (1,0) and (1,1)',
             'D at (3,0) is 0; S at (0,0) got a **7**',
         ],
         'split': 0.55,
         'figure': FIG + 'd51-wall-full.svg',
         'notes': 'Leading the discussion, 10 minutes. Put the numbered wall grid from the end of '
                  'Lesson 5-1 back on the board.'},

        ask(1, 4, ['You\'re standing on S, a 7', 'Which way do you go first?'], 'd51-wall-full',
            notes='Let them notice that it goes away from D, and that the numbers say so with '
                  'complete confidence.'),
        answer(1, 4, ['**Up, to (0,1), the 6**',
                      'The only neighbor with a smaller number',
                      'It goes **away** from D, and that\'s right'],
               figure='d52-first-step'),

        ask(2, 4, ['Keep going', 'How do you choose each step, and when do you stop?'],
            'd52-first-step',
            notes='Ask why it can\'t fail: every intersection got its number from a neighbor one '
                  'less, so there is always a way down.'),
        answer(2, 4, ['Every number came from a neighbor one less, so there is always a way down'],
               rule='**Always step to a neighbor one less. Stop at 0, which is D.**',
               figure='d52-walk',
               notes='One walk from the 7: up the left column, along the row y = 2, down the '
                     'right column.'),

        ask(3, 4, ['Somewhere you\'ll find two neighbors with the same number',
                   'Which one do you pick?'], 'd52-walk',
            notes='Look at (2,2), the 3: its neighbors (3,2) and (2,1) are both 2.'),
        answer(3, 4, ['**Either one**',
                      'Both lead down to 0 in the same number of steps',
                      'There can be several shortest paths; the number of steps is the same'],
               figure='d52-tie'),

        ask(4, 4, ['Why did we start the wave at D, and not at S?'],
            notes='Ask what would happen had we numbered from S: you would walk downhill from D '
                  'back to S, and then have to turn the list around.'),
        answer(4, 4, ['**So the walk starts where the robot is** and goes forward to D',
                      'The path comes out in driving order',
                      'Bonus: the numbers from D give the way from **any** start']),

        # --- Walking downhill ---
        {'kind': 'code', 'title': 'Walking downhill',
         'lead': 'Each step is an intersection the robot drives **to**. In order, they are the '
                 'path:',
         'code': '[(0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (3, 1), (3, 0)]',
         'code_size': 22,
         'callout': 'The start is left out: the robot is already there. So `len(path)` is the '
                    'number of steps, 7',
         'tone': 'teal',
         'notes': 'Same as Module 4\'s compute_manhattan_path. A classmate who picked differently '
                  'at a tie might have [..., (2, 2), (2, 1), (2, 0), (3, 0)]: also 7 steps, also '
                  'right. In Lesson 5-6 students test the planner by checking what must be true '
                  'of any correct answer, not by comparing against one list.'},

        {'kind': 'check',
         'question': 'Walking downhill, you are on an intersection numbered 4. Its open neighbors '
                     'are numbered 3, 3 and 5. Where can you step?',
         'options': ['To either 3: both lead down to the destination in 3 more steps',
                     'Only to the first 3 you check',
                     'To the 5, because it is further from the destination',
                     'Nowhere: two 3s means there is no path'],
         'answer': 0,
         'explanation': 'Any neighbor with one less works. Two choices just means two different '
                        'shortest paths, both correct.'},

        # --- Discuss · Teaching it to a computer ---
        {'kind': 'bullets', 'title': 'Teaching it to a computer', 'tag': 'Discuss',
         'bullets': [
             'You numbered the grid **with your eyes**: "all the 2s" at once',
             'A computer can\'t: it sees **one intersection** and its open neighbors',
             'The same limit your own rule had in Lesson 5-1',
         ],
         'notes': 'Leading the bridge, 10 to 15 minutes: the most important ten minutes in the '
                  'module. This is where students usually get stuck: they can do it by hand, but '
                  'can\'t see what a program would do. Each answer is one piece of the program, so '
                  'write each on the board as it\'s found, in words, and leave it up for the rest '
                  'of the lesson.'},

        ask(1, 4, ['A computer looks around **one intersection at a time**',
                   'In what order should it take them, so that every 1 is looked around before '
                   'any 2?'],
            notes='Listen for "the order they were numbered". If they\'re stuck, ask: "Which got '
                  'its number first, a 1 or a 2?"'),
        answer(1, 4, ['**In the order they were numbered**',
                      'Every 1 was numbered before any 2',
                      'Oldest first: the wave front moves out one step at a time, just as on '
                      'paper']),

        ask(2, 4, ['How can it remember that order?',
                   'What does it write down, and where does each newly numbered intersection '
                   'go?']),
        answer(2, 4, ['**A list: the to-visit list**',
                      'A newly numbered intersection goes on the **end**',
                      'The next one to look around comes off the **front**'],
               rule='**Add to the end, take from the front.**',
               notes='Act it out if the room is flat: students in a line, the one at the front '
                     'sits down and sends any unnumbered neighbors to the back.'),

        ask(3, 4, ['When is the wave finished?']),
        answer(3, 4, ['**When the list is empty**',
                      'Every intersection the wave can reach has its number'],
               notes='On paper you could stop once S had a number; the computer just lets the '
                     'wave finish, which on a 4×4 grid costs nothing.'),

        ask(4, 4, ['To walk downhill, what does the computer need to know about each '
                   'intersection?', 'Does it need anything else?']),
        answer(4, 4, ['**Just its number**',
                      'The walk only looks for a neighbor one less',
                      'Nothing else needs remembering'],
               notes='Say this plainly; students expect something more complicated, and it\'s why '
                     'the code in Lesson 5-5 is short.'),

        # --- Activity · Trace it the computer's way ---
        {'kind': 'steps', 'title': 'Trace it the computer\'s way', 'tag': 'Activity',
         'lead': '3×3, center (1,1) blocked. Start (0,0), destination (2,2). Neighbors in the '
                 'order left, right, down, up.',
         'steps': [
             'Take the intersection at the **front** of the to-visit list',
             'Each open neighbor with **no number yet** gets one more, and goes on the **end**',
             'Stop when the list is **empty**',
             'Then walk downhill from (0,0). At a tie, take the first in left, right, down, up',
         ],
         'notes': 'Students copy the table on the next slide and fill it in; the first two rows '
                  'are done for them. The full trace is on the lesson page behind a reveal, and '
                  'the step-through after the table shows it.'},

        {'kind': 'table', 'title': 'Fill in the table', 'tag': 'Activity',
         'headers': ['Step', 'Take off the front', 'Newly numbered', 'To-visit afterward'],
         'rows': [
             ['start', '—', '(2,2): 0', '(2,2)'],
             ['1', '(2,2)', '(1,2): 1, (2,1): 1', '(1,2), (2,1)'],
             ['2', '', '', ''],
             ['3', '', '', ''],
             ['…', '', '', ''],
             ['8', '', '', ''],
         ],
         'widths': [1, 2, 3, 3],
         'notes': 'Answer: 2 (1,2) gives (0,2): 2. 3 (2,1) gives (2,0): 2. 4 (0,2) gives (0,1): 3. '
                  '5 (2,0) gives (1,0): 3. 6 (0,1) gives (0,0): 4. 7 (1,0): nothing new. 8 (0,0): '
                  'nothing new, the list is empty. Walking downhill from the 4: (1,0) and (0,1) '
                  'are both 3, and (1,0) comes first. The path is [(1, 0), (2, 0), (2, 1), (2, 2)]: '
                  '4 steps.'},

        {'kind': 'figure', 'title': 'Check your trace', 'tag': 'Activity',
         'figure': '/img/lesson-m5-03/bfs-downhill-steps-xy.svg',
         'caption': 'Take from the front, add to the back, until the list is empty; then walk '
                    'downhill from S.',
         'notes': 'On the lesson page students can press Step to see what the computer does next '
                  'and why. The last step says why it is the shortest: every 1 was written before '
                  'any 2 and every 2 before any 3, so S\'s 4 is the fewest steps.'},

        {'kind': 'check',
         'question': 'Why does the computer take intersections from the FRONT of the to-visit '
                     'list?',
         'options': ['The front holds the oldest, so everything 1 step away is handled before '
                     'anything 2 steps away',
                     'So the search heads toward the start',
                     'It doesn\'t matter: any order gives the right numbers',
                     'So blocked intersections are skipped'],
         'answer': 0,
         'explanation': 'New intersections go on the end, so the front is always the oldest. '
                        'Oldest-first means the wave front moves out one step at a time, which is '
                        'what makes every number a shortest distance.'},

        # --- Review: the algorithm ---
        {'kind': 'bullets', 'title': 'Review: number from D',
         'tag': 'The algorithm',
         'bullets': [
             'Write 0 on the destination and put it on a to-visit list',
             'Until the list is empty, take the intersection at the **front**',
             'Each open neighbor **with no number yet** gets one more, and joins the **end**',
             'A neighbor that already has a number is left alone',
         ],
         'callout': 'Join at the end, take from the front: everything 1 step away is numbered '
                    'before anything 2 steps away',
         'tone': 'teal',
         'notes': 'Have students explain the review back to a partner in their own words before '
                  '"Be the computer". Lesson 5-3 goes through it asking what the program has to '
                  'remember for each part, and Lesson 5-5\'s skeleton lists its steps as numbered '
                  'comments, with one line of Python under each. A student who can explain the '
                  'review can write the program; a student who skipped it is translating a '
                  'picture.'},

        {'kind': 'bullets', 'title': 'Review: walk downhill',
         'tag': 'The algorithm',
         'bullets': [
             'No number on the start? The wave never reached it: **no path**',
             'Otherwise, from the start, step to an open neighbor **one less**',
             'Write down each intersection you step onto, until you\'re on the destination',
             'Leave the start off: the robot is already there',
         ],
         'callout': 'All it needs is one number per intersection',
         'tone': 'teal',
         'notes': 'And while it numbers the grid it never looks at where the start is, which is '
                  'why walls in the way are no problem.'},

        {'kind': 'check',
         'question': 'What in the algorithm makes sure no intersection is ever numbered twice?',
         'options': ['Only a neighbor that does not have a number yet gets one and joins the list',
                     'Always taking the intersection at the front of the list',
                     'Stopping when the list is empty',
                     'Walking downhill from the start'],
         'answer': 0,
         'explanation': 'A neighbor that already has a number is left alone. That is the '
                        'numbered-once rule from Lesson 5-1.'},

        {'kind': 'check',
         'question': 'What makes sure everything 1 step from the destination is numbered before '
                     'anything 2 steps away?',
         'options': ['New intersections join the end of the list, and the next one is always '
                     'taken from the front',
                     'Stopping when the list is empty',
                     'Looking at the open neighbors only',
                     'Walking downhill from the start'],
         'answer': 0,
         'explanation': 'Joining at the end and taking from the front means the oldest is always '
                        'next, so the wave front moves out one step at a time.'},

        # --- Activity · Be the computer ---
        {'kind': 'steps', 'title': 'Be the computer', 'tag': 'Activity',
         'lead': 'Pairs. The computer sees only one intersection and its open neighbors. The '
                 'other reads the review aloud and checks. 3×3, middle column blocked, start '
                 '(0,0), destination (2,0).',
         'lead_h': 1.15,
         'steps': [
             'What ends the numbering, and which intersections got numbers?',
             'Did the start get a number? What does that mean?',
             'Swap jobs and run it again with only (1,1) blocked. What path do you get?',
         ],
         'notes': 'Answers. Middle column blocked: (2,0) gets 0, (2,1) gets 1, (2,2) gets 2, then '
                  'the list is empty. The start never got a number: there is no path, and the '
                  'program will hand back an empty list, []. Only (1,1) blocked: (1,0) and (2,1) '
                  'get 1; (0,0) and (2,2) get 2; (0,1) and (1,2) get 3; (0,2) gets 4. The start '
                  'is a 2, and the path is [(1, 0), (2, 0)]. Listen for: the numbering ends '
                  'because the list runs out, not because the start was found.'},

        # --- Check your paper against the computer ---
        {'kind': 'code', 'title': 'Check against the computer',
         'lead': 'Your teacher\'s demonstration program runs the 3×3 with (1,1) blocked, step by '
                 'step, then prints the numbers:',
         'code': ' 2 |   2  1  0\n'
                 ' 1 |   3  X  1\n'
                 ' 0 |   4  3  2\n'
                 '    ----------\n'
                 '       0  1  2',
         'code_size': 26,
         'callout': 'If your trace matches, you ran the algorithm the way the computer does',
         'tone': 'green',
         'notes': 'The program is in the Module 5 sample programs. It is plain Python, no robot '
                  'and no XRPLib, so it runs on any laptop or in XRP Code with the robot '
                  'connected. Project it rather than handing it out, since Lesson 5-5 has students '
                  'write bfs_distances() and the walk themselves. Don\'t walk through its code: '
                  'Lessons 5-3 to 5-5 get there from the review, one step at a time. Nothing goes '
                  'into robot.py yet.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Robotics', 'Wavefront planners', 'Many robots spread a wave of numbers out from '
                                                'the goal, then drive downhill from wherever '
                                                'they are.'),
             ('Graphics', 'Paint-bucket fill', 'The fill tool spreads out from where you click '
                                               'with a to-visit list, like the wave.'),
             ('Puzzles', 'Maze solvers', 'Flood the maze from the exit, then walk downhill from '
                                         'the entrance.'),
         ]},

        {'kind': 'wrapup',
         'questions': [
             'How do you get the path from the numbers?',
             'Why does the wave start at the destination?',
             'Why does the computer take the oldest intersection first?',
             'What happens when the start is walled off?',
         ],
         'next': 'what the program has to remember, and the grid as a graph',
         'notes': 'Answers: from the start, keep stepping to a neighbor one less until you reach '
                  '0. So the walk starts where the robot is and the path comes out in driving '
                  'order. So the wave front moves out one step at a time. The list empties '
                  'without reaching it; there is no path. Formative: a correct trace table, and '
                  'the "Be the computer" answers, especially that the dead-end numbering ends '
                  'because the list runs out. Exit ticket: "What would go wrong if the computer '
                  'took the newest intersection from the list instead of the oldest?" (The wave '
                  'front would no longer move out one step at a time, so the numbers might not be '
                  'shortest distances, and the walk could take a longer route.) Preview: next '
                  'lesson asks what the program has to remember for each part; that\'s where the '
                  'grid becomes a graph and Python\'s dictionary comes in.'},
    ],
}
