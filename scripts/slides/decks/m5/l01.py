"""Module 5, Lesson 5-1 · Finding a Way Around.

The discussion "How far away is everything?" runs one slide per question, then
one slide with the answer. Each question slide's notes hold that step of the
lesson's "Leading the discussion" teacher note. Grids: fig/make_discuss_grids.py.
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
    'module': 5, 'lesson': 1,
    'doc': 'module-05-pathfinding/lesson-01-finding-a-way-around',
    'title': 'Finding a Way Around',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Explain why the Manhattan algorithm can\'t handle a blocked intersection',
             'Explain why "look at the grid and guess" isn\'t a method a computer can use',
             'Number every intersection with its distance to the destination, one step '
             'further out at a time, around blocked intersections',
             'Explain why the number on the start is the shortest path length',
         ],
         'notes': '50 to 55 minutes, no coding: paper and the board. This lesson is the why for '
                  'the whole module. Spend real time on the hook, then let students struggle to '
                  'state a rule; that struggle is what makes the wave worth having. "Intersection" '
                  'and "neighbor" are enough today: graph, node and dictionary wait for Lesson '
                  '5-3.'},

        # --- Why Manhattan isn't enough ---
        {'kind': 'bullets', 'title': 'Why Manhattan isn\'t enough',
         'bullets': [
             'Your usual route is closed? Your GPS finds a detour',
             'Manhattan knows one strategy: **across, then up or down**',
             'It has no idea of an obstacle, so it drives right into one',
         ],
         'callout': 'Today: a method that finds a way around, and never guesses',
         'tone': 'teal',
         'notes': 'Show a blocked intersection sitting on Manhattan\'s route and let students '
                  'feel that the old algorithm is stuck before you offer anything new.'},

        {'kind': 'bullets', 'title': 'Your phone solves this too',
         'bullets': [
             '**This module, breadth-first search**: a route around blocked intersections',
             '**Module 6, Dijkstra\'s algorithm**: the **fastest** route when some streets are '
             'slow',
         ],
         'split': 0.5,
         'figure': '/img/lesson-m5-01/phone-route.svg',
         'crop': (0.22, 0.0, 0.94, 1.0),
         'notes': 'A maps app going around a closed road (this module\'s problem) and avoiding a '
                  'slow street (the next module\'s). Real apps use faster descendants of '
                  'Dijkstra (A* is the best known), but the core idea is the one students write. '
                  'If a student asks about slow roads: "good question, Module 6."'},

        {'kind': 'check',
         'question': 'Why can\'t the Manhattan algorithm route around a blocked intersection?',
         'options': ['It runs too slowly',
                     'It only knows one fixed strategy (across, then up or down) and has no '
                     'concept of obstacles',
                     'It can, if you turn it off and on again',
                     'The robot has no wheels'],
         'answer': 1,
         'explanation': 'Manhattan always follows the same L-shaped route. It never checks whether '
                        'an intersection is blocked, so it can\'t detour.'},

        # --- Activity · Finding a path around ---
        {'kind': 'figure', 'title': 'Activity · Finding a path around', 'tag': 'Activity',
         'figure': '/img/lesson-m5-01/detour-xy.svg',
         'caption': '(1,0) is blocked. Find the shortest path from (0,0) to (2,0): trace it with '
                    'your finger and count the steps.',
         'notes': 'A blocked intersection is out of play: the robot can\'t stop on it or drive '
                  'through it. Manhattan\'s straight line goes through (1,0), so it fails. Take '
                  'answers from the room before the next slide.'},

        {'kind': 'bullets', 'title': 'Check your route',
         'bullets': [
             '(0,0) → (0,1) → (1,1) → (2,1) → (2,0): **4 steps**',
             'Without the obstacle: 2 steps, the **Manhattan distance**',
             '**Obstacles make paths longer**, so the Manhattan distance is only a lower bound',
         ],
         'notes': 'Any other 4-step route around (1,0) is just as correct; there\'s usually more '
                  'than one shortest path. The Manhattan distance is the steps across plus the '
                  'steps up or down.'},

        {'kind': 'check',
         'question': 'With (1,0) blocked, the shortest path from (0,0) to (2,0) is 4 steps, but '
                     'the Manhattan distance is 2. What does that tell you?',
         'options': ['The Manhattan distance is wrong',
                     'With obstacles, the real shortest path can be longer than the Manhattan '
                     'distance',
                     'Obstacles always add exactly 2 steps',
                     'The destination is unreachable'],
         'answer': 1,
         'explanation': 'Manhattan distance is the shortest path with NO obstacles. Blocked '
                        'intersections can force a longer detour, so it becomes a lower bound.'},

        # --- Activity · Explain your method to a computer ---
        {'kind': 'bullets', 'title': 'Explain your method to a computer',
         'tag': 'Activity',
         'bullets': [
             'A computer sees **one intersection** and its open neighbors, never the whole grid',
             'Write your **rule**, in numbered steps, for someone who sees only that much',
             'It must reach D by a shortest path, every time, on any grid',
             'Two minutes, then test it here',
         ],
         'split': 0.5,
         'figure': '/img/lesson-m5-03/wall-problem-xy.svg',
         'notes': 'What you\'re fishing for. Nearly every rule students write is Manhattan with a '
                  'patch: "head toward the goal; if it\'s blocked, go around." Let them apply it '
                  'here. "Go around" means stepping up to (0,1), still blocked on its right, so '
                  'up to (0,2); now "head toward the goal" goes right to (1,2), still away from '
                  'the bottom row. Some rules loop here; most can\'t say how far "around" to go. '
                  'The point isn\'t to make them fail: it\'s for them to feel that a rule which '
                  'looks at the goal can\'t handle a wall that forces you away from it. The '
                  'discussion that follows builds a method that never looks at the goal at all.'},

        # --- Discuss · How far away is everything? ---
        {'kind': 'bullets', 'title': 'How far away is everything?', 'tag': 'Discuss',
         'bullets': [
             'Draw a 4×4 grid: S at (0,0), D at (3,3), no obstacles',
             'This time, work **from the destination**',
             'Answer each question before you go on to the next',
         ],
         'split': 0.55,
         'figure': FIG + 'd51-grid.svg',
         'notes': 'Leading the discussion, 15 to 20 minutes. Draw the grid big on the board and '
                  'write the numbers there as the class gives them. The goal is that they say '
                  'the rule; your job is to ask the next question. If someone asks why we start '
                  'from D, say it\'s a fair question and Lesson 5-2 answers it.'},

        ask(1, 5, ['On our grid, what does **"shortest"** mean?'], 'd51-grid',
            notes='Listen for "fewest blocks". If anyone says "the straightest", ask: "Is a path '
                  'with 5 steps ever shorter than one with 4?"'),
        answer(1, 5, ['The **fewest blocks** driven', 'Every block is one step']),

        ask(2, 5, ['Forget S for a moment',
                   'Which intersections are exactly **1** step from D? Write a 1 on each'],
            'd51-zero',
            notes='Easy on purpose. The real move is that the question is about distance from D, '
                  'not about getting from S. Don\'t mention S again until question 4.'),
        answer(2, 5, ['**(2,3) and (3,2)**', 'D itself is 0'], figure='d51-ones'),

        ask(3, 5, ['Which are exactly **2** steps from D? Write a 2 on each',
                   'How did you find them?'], 'd51-ones-q',
            notes='Someone will say D, by going out and back. Ask: "Do we learn anything by '
                  'writing a 2 on D? We already know it\'s 0." That is the first discovery: only '
                  'number an intersection that has no number yet. Then press on "How did you find '
                  'them?" until someone says you looked at the neighbors of the 1s. Generalize out '
                  'loud and write it on the board: "Every unnumbered neighbor of a 2 gets a 3." '
                  'That sentence is the whole method; underline it.'),
        answer(3, 5, ['**(1,3), (2,2) and (3,1)**',
                      'Look at the neighbors of the 1s',
                      'Only number an intersection with **no number yet**: D stays 0'],
               rule='**Every unnumbered neighbor of a 2 gets a 3.**', figure='d51-twos'),

        ask(4, 5, ['Keep going until S gets a number',
                   'Could there be a shorter way from S to D than S\'s number says?'], 'd51-twos-q',
            notes='Let them argue. The convincing reason: every intersection 2 steps from D was '
                  'numbered before any 3 was written, so if S were fewer steps away, it would '
                  'already have a smaller number.'),
        answer(4, 5, ['**S gets a 6. No shorter way.**',
                      'Everything closer to D was numbered first'],
               rule='**The number on an intersection is its shortest distance to D.**',
               figure='d51-full'),

        ask(5, 5, ['Put back the wall: (1,0) and (1,1) blocked, D at (3,0)',
                   'Number the grid again from D',
                   'Do you need a new rule for the blocked intersections?'], 'd51-wall',
            notes='Give them a couple of minutes to number it on paper while you draw it on the '
                  'board.'),
        answer(5, 5, ['**No new rule**',
                      'A blocked intersection never gets a number',
                      'The numbers flow around it: S gets a **7**'],
               figure='d51-wall-full',
               notes='Point at the numbers next to S: the smaller one is up, away from D. Ask: '
                     '"This method never looked at where S is. Is that a weakness or a strength?" '
                     'It is why it works where the head-toward-the-goal rules from the last '
                     'activity didn\'t. Keep this numbered grid on the board; Lesson 5-2 starts '
                     'from it.'),

        # --- What you found: a wave ---
        {'kind': 'steps', 'title': 'What you found: a wave',
         'steps': [
             'Write **0** on the destination',
             'Every intersection one step away gets a **1**',
             'Every intersection one step from a 1 that **doesn\'t have a number yet** gets a **2**',
             'Keep going, finishing one distance before you start the next, until the start has '
             'a number',
         ],
         'tag': 'The method',
         'notes': 'The method the class just worked out, written as steps. The one habit that '
                  'matters: number everything at one distance before anything further out. Don\'t '
                  'bring in a distances table, "infinity" or the to-visit list today: BFS doesn\'t '
                  'need the first two, Module 6 adds them for a reason, and Lesson 5-2\'s bridge '
                  'to the computer starts from noticing that a computer can\'t number "all the '
                  '2s" at once.'},

        {'kind': 'bullets', 'title': 'Like a stone in a pond',
         'bullets': [
             'The wave spreads out from D, the same in every direction',
             'It flows **around** a blocked intersection',
             'Everything closer is reached first',
             'It goes wide before it goes deep: **breadth-first search**',
         ],
         'split': 0.5,
         'figure': '/img/lesson-m5-03/bfs-wave-from-d-xy.svg',
         'crop': (0.0, 0.0, 0.53, 1.0),
         'notes': 'The wave front is the intersections just numbered; it moves out one step at a '
                  'time, so each number is the shortest distance to D. On a grid this is also '
                  'called a wavefront algorithm. It never looks at where the start is, so a wall '
                  'that forces you away from D is no problem. The walk in red on the lesson\'s '
                  'figure is next lesson\'s idea.'},

        {'kind': 'check',
         'question': 'An intersection already has a 2 on it. Later, while looking around an '
                     'intersection with a 3, you find it\'s a neighbor. What do you write on it?',
         'options': ['Nothing — it keeps its 2', '4, because 3 + 1',
                     '3, the smaller of 3 and 4', 'Cross out the 2 and write 4'],
         'answer': 0,
         'explanation': 'An intersection is numbered once, the first time it\'s reached. The wave '
                        'reaches everything at one distance before anything further out, so that '
                        'first number is already the smallest possible.'},

        {'kind': 'check',
         'question': 'The start has just been given a 5. Could a shorter way from the start to the '
                     'destination still turn up?',
         'options': ['No: every intersection 4 or fewer steps away is already numbered, so 5 '
                     'is the shortest',
                     'Yes: finish the whole grid, then look for a smaller number on the start',
                     'Yes: a path that heads straight toward the destination might be shorter',
                     'It depends on how many intersections are blocked'],
         'answer': 0,
         'explanation': 'The wave reaches everything closer first, so the first number written on '
                        'the start can\'t be beaten.'},

        # --- The wave on a bigger grid ---
        {'kind': 'figure', 'title': 'The wave on a bigger grid',
         'figure': '/img/lesson-m5-03/fanout-bfs-from-d.svg',
         'caption': 'Same rule on an 8 by 6 grid with a wall. The wave spreads evenly, even away '
                    'from S.',
         'notes': 'Every intersection one step from D is numbered before any two steps away, and '
                  'the wave bends around both ends of the wall. It never looks at where the start '
                  'is, so here it fills the whole grid. The red line at the end is next lesson\'s '
                  'idea. On the lesson page students can step through it.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Maps', 'GPS routing', 'Rerouting around a closed road is this problem. Route '
                                     'planners spread a wave of distances through the street '
                                     'map.'),
             ('Social', 'Degrees of separation', '"Friends of friends" are the people two steps '
                                                 'out in a breadth-first search.'),
             ('Games', 'Enemy AI', 'Game characters find their way around walls with graph '
                                   'search, many times a second.'),
         ]},

        {'kind': 'wrapup',
         'questions': [
             'Why can\'t Manhattan handle a blocked intersection?',
             'What does the number on an intersection mean?',
             'Do blocked intersections need a special rule?',
             'Why is the number on the start the shortest distance?',
         ],
         'next': 'find the path, and teach the method to a computer',
         'notes': 'Answers: one fixed route, no idea of obstacles. Its distance to the '
                  'destination, in steps. No: they never get a number, and the wave flows around '
                  'them. Everything closer to the destination was numbered first. Formative: can '
                  'students say the rule in their own words, and explain why the start\'s number '
                  'is the shortest length? Exit ticket: "An intersection already has a 2. You '
                  'reach it again from a 3. What do you write?" (Nothing.) Preview: the numbers '
                  'say how far. Next lesson finds the path itself, why numbering from the '
                  'destination makes that easy, and how a computer would do it all.'},
    ],
}
