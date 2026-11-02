DECK = {
    'module': 5, 'lesson': 3,
    'doc': 'module-05-pathfinding/lesson-03-bfs-concept',
    'title': 'Breadth-First Search: The Concept',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Explain why "look at the grid and guess" isn\'t a method a computer can use',
             'Number every intersection with its distance from the start, one ring at a time',
             'Explain why the first number written on the destination is the shortest path length',
             'Record where each intersection was reached **from**, and walk it back to get the path',
             'Recognize that more than one path can be shortest, and that any of them is right',
         ],
         'notes': '55 minutes, no coding: a hand-trace on paper. The second objective on the lesson '
                  'page ends "around blocked intersections"; the slide shortens it. Nothing goes '
                  'into robot.py today. The whole method fits in one idea: ripples.'},

        {'kind': 'bullets', 'title': 'From "I just looked" to a method',
         'bullets': [
             'In Lesson 5-1 you found a path around blocked intersections by looking at the whole grid',
             'That works for you. It doesn\'t work for a computer',
             'A computer only ever sees **one intersection and its neighbors**',
             'Today: a method precise enough to follow with a pencil, and to type in two lessons',
         ],
         'callout': 'It\'s called **breadth-first search**, and the whole thing fits in one idea: ripples',
         'tone': 'teal'},

        {'kind': 'steps', 'title': 'Activity · Explain your method to a computer',
         'lead': 'Take the Lesson 5-1 grid with its blocked intersections and the path you found.',
         'steps': [
             'Write down your **rule**, in numbered steps, for someone who can\'t see the whole grid',
             'They can see one intersection and which of its neighbors are open. That\'s it',
             'Your rule has to get them to the destination by a shortest path, every time, on any grid',
             'Give it two minutes. Then test your rule on the next grid',
         ],
         'notes': 'Keep the timer honest: two minutes, then move on to the wall grid.'},

        {'kind': 'figure', 'title': 'Test your rule on this one', 'tag': 'Activity',
         'figure': '/img/lesson-m5-03/wall-problem-xy.svg',
         'caption': 'Start at S (0,0), destination D (3,0), straight across the bottom row. '
                    'There\'s a wall in the way at (1,0) and (1,1).',
         'notes': 'What you are fishing for: nearly every rule is Manhattan with a patch, "head '
                  'toward the goal; if it\'s blocked, go around." Going around means stepping up '
                  'to (0,1), still blocked on its right, then up to (0,2), and now "head toward '
                  'the goal" goes right, still away from the bottom row. Some rules loop; most '
                  'can\'t say how far around to go. The point is not to make them fail but to '
                  'feel that a rule which looks at the goal can\'t handle a wall that forces you '
                  'away from it. The method that follows never looks at the goal until it '
                  'arrives.'},

        {'kind': 'bullets', 'title': 'Ripples',
         'lead': 'A method that never guesses, never looks at the destination, and still always '
                 'finds a shortest path:',
         'lead_h': 1.2,
         'bullets': [
             'Write **0** on the start',
             'Every intersection you can reach in one step gets a **1**',
             'Every intersection one step from a 1 that **doesn\'t have a number yet** gets a **2**',
             'Keep going, always finishing one ring before you start the next',
             'Stop when the destination gets a number',
         ],
         'callout': 'The number on the destination is its distance from the start, in steps',
         'tone': 'teal'},

        {'kind': 'figure', 'title': 'Ripples spreading out from the start',
         'figure': '/img/lesson-m5-03/bfs-rings-xy.svg',
         'caption': 'Each ring is exactly one step further out, around the blocked intersection. '
                    'The arrows on the right record where each one was reached from.',
         'notes': 'Point at the left panel now. The right panel (came from) is the subject of a '
                  'later section; mention it is how the numbers will turn into a path.'},

        {'kind': 'bullets', 'title': 'Why it\'s always shortest',
         'bullets': [
             'Could there be a shorter path you missed? No, and the reason is the rule itself',
             'Ring 3 was only written after **every** ring-2 intersection was done',
             'So anything with a 3 on it can\'t be reached in 2 steps',
             'The first number written on the destination is the smallest one it could ever get',
         ],
         'callout': '**Breadth-first**: it goes wide (the whole ring) before it goes deep',
         'tone': 'orange'},

        {'kind': 'check',
         'question': 'An intersection already has a 2 on it. Later, while looking around an '
                     'intersection with a 3, you find it\'s a neighbor. What do you write on it?',
         'options': ['Nothing: it keeps its 2', '4, because 3 + 1', '3, the smaller of 3 and 4',
                     'Cross out the 2 and write 4'],
         'answer': 0,
         'explanation': 'An intersection is numbered once, the first time it\'s reached. Because '
                        'rings are finished in order, that first number is already the smallest '
                        'possible.'},

        {'kind': 'bullets', 'title': 'Activity · Trace it: 3×3 with (1,1) blocked', 'tag': 'Activity',
         'bullets': [
             'Start at (0,0), destination (2,2). Put an **X** on the center: it never gets a '
             'number and it\'s never anyone\'s neighbor',
             'Keep a **to-visit** list beside the grid',
             ['when an intersection gets its number, add it to the **end** of the list',
              'to decide where to look next, take the one at the **front**'],
             'Check neighbors in the order the code will use: left, right, down, up',
         ],
         'callout': 'Say it out loud: "Take the oldest one I haven\'t looked around yet. Every '
                    'neighbor with no number gets the next number."',
         'tone': 'teal',
         'notes': 'Keep the to-visit list on the board and always take from the front. Students '
                  'who skip ahead get the wall exercise wrong and usually can\'t see why; the list '
                  'makes the error visible.'},

        {'kind': 'table', 'title': 'The trace (1 of 2)', 'tag': 'Activity',
         'headers': ['Step', 'Looking around', 'New numbers written', 'To-visit afterward'],
         'widths': [1, 2, 3.2, 2.8],
         'rows': [
             ['start', '(none)', '(0,0): **0**', '(0,0)'],
             ['1', '(0,0)', '(1,0): **1**, (0,1): **1**', '(1,0), (0,1)'],
             ['2', '(1,0)', '(2,0): **2**', '(0,1), (2,0)'],
             ['3', '(0,1)', '(0,2): **2**', '(2,0), (0,2)'],
             ['4', '(2,0)', '(2,1): **3**', '(0,2), (2,1)'],
         ],
         'notes': 'Have students run the trace on paper alongside, one row at a time, before you '
                  'show each row. The lesson page shows the start row\'s "looking around" cell as '
                  'a dash.'},

        {'kind': 'table', 'title': 'The trace (2 of 2)', 'tag': 'Activity',
         'headers': ['Step', 'Looking around', 'New numbers written', 'To-visit afterward'],
         'widths': [1, 2, 3.2, 2.8],
         'rows': [
             ['5', '(0,2)', '(1,2): **3**', '(2,1), (1,2)'],
             ['6', '(2,1)', '(2,2): **4**', '(1,2), (2,2)'],
             ['7', '(1,2)', 'nothing new', '(2,2)'],
             ['8', '(2,2)', 'destination reached: stop', ''],
         ],
         'callout': 'Step 7: (1,2) finds (0,2) and (2,2), and both already have numbers. It writes '
                    'nothing.',
         'tone': 'orange',
         'notes': 'Step 7 is the knowledge-check rule in action: a number is written once, the '
                  'first time.'},

        {'kind': 'figure', 'title': 'Take from the front, add to the back', 'tag': 'Activity',
         'figure': '/img/lesson-m5-03/bfs-ripple-xy.svg',
         'frame': 0.5,
         'caption': 'The same trace, moving: take from the front, add to the back, and the rings '
                    'fill in one at a time.',
         'notes': 'The figure on the lesson page is an animation of the whole trace; this is step '
                  '6, where (2,1) is taken from the front and (2,2) gets its 4. Play the animation '
                  'on the lesson page if you can.'},

        {'kind': 'check',
         'question': 'Why does the to-visit list have to be used oldest-first?',
         'options': ['So that every ring is finished before the next one starts',
                     'So the search heads toward the destination',
                     'It doesn\'t matter: any order works',
                     'So blocked intersections are skipped'],
         'answer': 0,
         'explanation': 'Oldest-first means every ring-1 intersection is looked around before any '
                        'ring-2 one. That ordering is the whole guarantee that the first number '
                        'written is the smallest.'},

        {'kind': 'bullets', 'title': 'Where did I come from?',
         'bullets': [
             'The number tells you **how far**. It doesn\'t tell you **which way**',
             'So add one thing to the rule: every time you write a number on an intersection, '
             'also write down which intersection you were looking around at the time',
             'That is where it **came from**',
         ],
         'callout': 'The came-from record is how the numbers turn into a path',
         'tone': 'teal'},

        {'kind': 'table', 'title': 'The came-from record',
         'headers': ['Intersection', 'Ring', 'Came from'],
         'widths': [1, 1, 1],
         'size': 18,
         'rows': [
             ['(0,0)', '0', 'none'],
             ['(1,0)', '1', '(0,0)'],
             ['(0,1)', '1', '(0,0)'],
             ['(2,0)', '2', '(1,0)'],
             ['(0,2)', '2', '(0,1)'],
             ['(2,1)', '3', '(2,0)'],
             ['(1,2)', '3', '(0,2)'],
             ['(2,2)', '4', '(2,1)'],
         ],
         'notes': 'The same 3x3 trace with (1,1) blocked. Have students add a came-from column '
                  'to their own trace.'},

        {'kind': 'code', 'title': 'Walk it back',
         'lead': 'Start at the destination and follow "came from" backwards, until you reach the start:',
         'lead_h': 1.0,
         'code': '(2,2) <- (2,1) <- (2,0) <- (1,0) <- (0,0)',
         'code_size': 24, 'width': 10,
         'callout': 'Written forward, and **without** the start: `[(1, 0), (2, 0), (2, 1), (2, 2)]`',
         'tone': 'green',
         'callout_size': 24,
         'notes': 'The lesson page draws the arrows as left-pointing arrows; the slide writes them '
                  'as <-. Those are the intersections the robot drives to. The start isn\'t in the '
                  'list because the robot is already standing on it: the same rule '
                  'compute_manhattan_path followed in Module 4, so len(path) is the number of '
                  'steps, here 4.'},

        {'kind': 'check',
         'question': 'The came-from record is {(0,0): none, (0,1): (0,0), (0,2): (0,1), '
                     '(1,2): (0,2)}. What is the path from (0,0) to (1,2)?',
         'options': ['[(0,1), (0,2), (1,2)]', '[(0,0), (0,1), (0,2), (1,2)]',
                     '[(1,2), (0,2), (0,1)]', '[(1,2), (0,2), (0,1), (0,0)]'],
         'answer': 0,
         'explanation': 'Walk back from (1,2): came from (0,2), which came from (0,1), which came '
                        'from (0,0), the start, so stop. Flip it and leave the start out.'},

        {'kind': 'code', 'title': 'More than one right answer',
         'lead': '(2,2) has **two** neighbors with a 3, (2,1) and (1,2). Which one it "came from" '
                 'depends on which was looked around first. A classmate who checked neighbors in a '
                 'different order would get',
         'lead_h': 1.5,
         'code': '[(0, 1), (0, 2), (1, 2), (2, 2)]',
         'code_size': 26, 'width': 8,
         'callout': 'Four steps. Also shortest. Also right. What\'s unique is the **number of steps**',
         'tone': 'teal',
         'notes': 'On an open grid there are usually several shortest paths. Plant the seed: in '
                  'Lesson 5-6, when students test their planner, they won\'t compare against one '
                  'expected list. They\'ll check what has to be true of any correct answer.'},

        {'kind': 'bullets', 'title': 'Activity · The wall, and the dead end', 'tag': 'Activity',
         'lead': 'Back to the wall at (1,0) and (1,1). Number every intersection, starting from (0,0).',
         'lead_h': 1.2,
         'bullets': [
             'Write down the ring number on (3,0), and one shortest path to it',
             'Your first step goes **away** from the destination. In one sentence: why does this '
             'method get that right when "head toward the goal" didn\'t?',
             'Then block the whole column at x = 1 and start again',
             'What happens to the rings? What number does (3,0) get?',
         ],
         'split': 0.56,
         'code': ' 3 |   .  .  .  .\n'
                 ' 2 |   .  .  .  .\n'
                 ' 1 |   .  X  .  .\n'
                 ' 0 |   0  X  .  .\n'
                 '    -------------\n'
                 '       0  1  2  3',
         'code_size': 22,
         'notes': 'Numbering the whole grid is fine; it makes the picture clearer. The blocked '
                  'column is (1,0), (1,1), (1,2), (1,3). The answers are in the "Answers" teacher '
                  'note on the lesson page. For the blocked column, ask what the program should '
                  'return when the destination never gets a number: an empty path. Lesson 5-5 '
                  'makes it do exactly that, and Lesson 5-6 has a test for it.'},

        {'kind': 'bullets', 'title': 'Check your paper against the computer',
         'bullets': [
             'Nothing goes into `robot.py` today: that starts in Lesson 5-4',
             'Your teacher\'s demonstration program does the 3×3 trace with (1,1) blocked, step by step',
             'It prints each intersection as it\'s reached, and the to-visit list after every step',
             'Then it draws the grid of ring numbers',
             'Same ring numbers as yours? You ran the algorithm',
         ],
         'split': 0.6,
         'code': ' 2 |   2  3  4\n'
                 ' 1 |   1  X  3\n'
                 ' 0 |   0  1  2\n'
                 '    ----------\n'
                 '       0  1  2',
         'code_size': 24,
         'callout': 'A different path with the same number of steps? That\'s "more than one right '
                    'answer" for real',
         'tone': 'teal',
         'notes': 'The program is lesson-03-bfs-concept.py in the Module 5 solutions. It is plain '
                  'Python (no robot, no XRPLib), so it runs on any laptop or in XRP Code. Project '
                  'it rather than handing it out: in Lesson 5-5 students write bfs_rings() and '
                  'print_grid() themselves, and their own file draws this grid. The last ten '
                  'minutes with it matter. If time allows, show (don\'t hand out) the loop from '
                  'the teacher note on the lesson page and have students match each line to '
                  'something they did with a pencil; in 5-5 they get it as a numbered outline, not '
                  'as code.'},

        {'kind': 'frames', 'title': 'The ripple on a bigger grid',
         'figure': '/img/lesson-m5-03/fanout-bfs.svg',
         'crop': (0.0, 0.08, 0.58, 1.0),
         'frames': [(0.4, 'The rings spread evenly and bend around the wall'),
                    (0.8, 'D is reached: the walk-back is 9 steps')],
         'callout': 'It spreads evenly, even **away** from D, and stops as soon as D comes off the list',
         'tone': 'teal',
         'notes': 'Same rule as the 3x3 trace, unchanged, on a grid of 8 by 6 with a wall across '
                  'the middle: it spreads like a ripple in a pond and bends around the wall. The '
                  'search has no idea where D is until it gets there, and a few far corners never '
                  'get a number. The figure on the lesson page is an animation; play it there if '
                  'you can.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Maps', 'GPS routing', 'Turn-by-turn directions come from search algorithms that '
                                     'spread out from where you are, exactly like the rings.'),
             ('Networks', 'Internet packets', 'Routers find the fewest hops to a destination '
                                              'with breadth-first search over the network graph.'),
             ('Games', 'Enemy AI', 'Game characters find their way around walls with graph search '
                                   'like this, many times a second.'),
         ]},

        {'kind': 'wrapup',
         'questions': [
             'What does the number on an intersection mean?',
             'Why is the first number written on the destination the shortest path length?',
             'What does "came from" let you do that the number alone doesn\'t?',
             'Does the path include the start?',
         ],
         'next': 'the blocked list, and a BFS PLANNER section in robot.py',
         'notes': 'Answers: its distance from the start, in steps. Rings are finished in order, so '
                  'nothing is reached late by a short route. Walk back from the destination and '
                  'read off the path. No, the robot is already there. Resist introducing a '
                  'distances table or "infinity": BFS doesn\'t need them, and they are exactly '
                  'what Module 6 adds. If a student asks about slow roads: "good question, Module '
                  '6." Exit ticket: "An intersection already has a 2. You reach it again from a 3. '
                  'What do you write?" (Nothing.) Preview: next lesson GRID GRAPH gains the '
                  'blocked list and add_blocked(), build_grid_graph() is rewritten around it, and '
                  'a new BFS PLANNER section opens with compute_bfs_path() as a placeholder.'},
    ],
}
