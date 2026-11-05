DECK = {
    'module': 5, 'lesson': 0,
    'doc': 'module-05-pathfinding/lesson-00-overview',
    'title': 'When the Road Is Blocked',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Describe what the robot will do by the end of Module 5',
             'Explain why the Module 4 planner can\'t get around a blocked intersection',
             'Name the module\'s three new pieces, a map of the grid, a planner that searches '
             'it, and obstacle detection, and say what each one does',
             'Explain what it means to swap one planner for another without changing the rest '
             'of the program',
         ],
         'notes': '15 to 20 minutes, no coding yet. Keep it to the destination and the three '
                  'pieces. Do not say how the planner searches: students invent that in Lesson '
                  '5-3. The figure uses a different grid from Lesson 5-1\'s detour activity, so it '
                  'does not give that answer away. If students ask how the robot finds the way '
                  'around: "Lessons 5-1 and 5-3, with a pencil, before any code."'},

        {'kind': 'bullets', 'title': 'Module 4\'s one blind spot',
         'bullets': [
             'Module 4 ended with a robot that plans its own routes and drives them',
             'It plans every route the same way: **across, then up**',
             'And it assumes **nothing is ever in the way**',
             'Put a box on one intersection of its route and it drives straight at it',
         ],
         'callout': 'This module teaches it to go around',
         'tone': 'orange'},

        {'kind': 'figure', 'title': 'One box, two planners',
         'figure': '/img/lesson-m5-00/blocked-route-xy.svg',
         'caption': 'Module 4\'s planner has one route and it\'s blocked; this module\'s planner '
                    'finds a way around.',
         'notes': 'The box is at (2, 0). Manhattan goes across first and runs into it. The way '
                  'around is still 5 steps, the same as if the box were not there.'},

        {'kind': 'bullets', 'title': 'Where this module ends up',
         'bullets': [
             'Visit **several destinations** on a grid with obstacles on it',
             'Plan around the obstacles it knows about',
             'Spot new ones with the **rangefinder** while it drives, and re-plan on the spot',
             'Do better on its **second run**, because it remembers what the first run found',
         ],
         'callout': 'The last required module: everything you\'ve built works together',
         'tone': 'teal'},

        {'kind': 'cards', 'title': 'Three new pieces',
         'height': 3.6,
         'cards': [
             ('Map', 'The grid as a graph',
              'Every intersection, which ones it connects to, and which are blocked.'),
             ('Planner', 'Breadth-first search',
              'A shortest route from here to there, around every blocked intersection.'),
             ('Senses', 'Obstacle detection',
              'The rangefinder looks ahead; if something is there, it goes on the map and the '
              'robot plans again.'),
         ],
         'notes': 'Each piece gets its own section of robot.py: GRID GRAPH, BFS PLANNER and '
                  'OBSTACLES. The driving does not change: the NAVIGATOR section from Module 4 '
                  'comes across untouched. Like Manhattan, the new planner is tested on screen '
                  'before it drives anything.'},

        {'kind': 'bullets', 'title': 'The swap',
         'bullets': [
             'Manhattan and the new planner answer **the same request**',
             'Where the robot is and where it should go in; a list of intersections out',
             'The navigator doesn\'t care which planner made the list',
             'So once the new planner passes its tests, you swap it in by **changing one name**',
         ],
         'callout': 'The route that ran into the box now goes around it',
         'tone': 'teal',
         'notes': 'This is the payoff of four modules of reusable code, and of the decomposition '
                  'in Lesson 4-0: what passes between planner and driver was decided before '
                  'either was written, so either side can be replaced without touching the '
                  'other. Come back to the figure '
                  'in Lesson 5-6, when the swap happens on screen; from Lesson 5-7 the robot '
                  'drives it.'},

        {'kind': 'check',
         'question': 'Both planners take a position and a destination and return a list of '
                     'intersections. Why does that matter?',
         'options': ['It means they always return the same route',
                     'The code that drives the route works with either one, so swapping planners '
                     'changes one name, not the whole program',
                     'It means the new planner is just as fast as Manhattan',
                     'It means you can delete the Manhattan planner'],
         'answer': 1,
         'explanation': 'Everything that uses the list, the navigator, the tests and the main '
                        'program, works with either planner. Only the name changes.'},

        {'kind': 'table',
         'title': 'Your roadmap (1 of 2)',
         'headers': ['Lesson', 'What happens'],
         'widths': [3.6, 7.8],
         'size': 20,
         'rows': [['**5-1** Grid as a Graph',
                   'Block an intersection and find a way around by hand. No code.'],
                  ['**5-2** Dictionaries', 'Store the graph in Python. GRID GRAPH opens.'],
                  ['**5-3** BFS Concept',
                   'Turn "I just looked" into a method, traced with a pencil. No code.'],
                  ['**5-4** Pathfinding Functions', 'A shared blocked list; BFS PLANNER opens'],
                  ['**5-5** compute_bfs_path()', 'The pencil method, line for line, in Python']]},

        {'kind': 'table',
         'title': 'Your roadmap (2 of 2)',
         'headers': ['Lesson', 'What happens'],
         'widths': [3.6, 7.8],
         'size': 20,
         'rows': [['**5-6** Testing and Swapping',
                   'Test any planner on screen; swap by changing one name'],
                  ['**5-7** Obstacle Detection',
                   'Look before each block, and plan again. OBSTACLES opens.'],
                  ['**5-8** Building Experience',
                   'Re-plan until arrival; start Run 2 knowing what Run 1 found'],
                  ['**5-9** Capstone Project',
                   'Several destinations, obstacles avoided, a better second run']],
         'notes': 'Materials: the 4 x 4 grid, and from Lesson 5-7 a few flat, firm boxes the '
                  'rangefinder can see. Lessons 5-1 to 5-6 never put a robot on the floor. Pacing: '
                  'about four weeks; the course is complete at the end of this module.'},

        {'kind': 'wrapup',
         'questions': [
             'What will the robot do by the end of the module?',
             'Why can\'t the Module 4 planner handle a box on its route?',
             'What are the three new pieces?',
         ],
         'next': 'see the grid as a graph, and find a way around by hand',
         'notes': 'Answers: visit several destinations, plan around known obstacles, find new '
                  'ones while driving, and improve on its second run. It always plans across then '
                  'up, and has no idea anything is blocked. A map of the grid, a planner that '
                  'searches it, and detection with the rangefinder.'},
    ],
}
