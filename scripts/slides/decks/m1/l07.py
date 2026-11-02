DECK = {
    'module': 1, 'lesson': 7,
    'doc': 'module-01-driving/lesson-07-blockly-challenges',
    'title': 'Blockly Challenges & Synthesis',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Combine loops, functions, parameters, and motor control in one program',
             'Plan a program\'s structure **before** you start dragging blocks',
             'Debug with a repeatable process: predict → test → observe → adjust',
             'Judge trade-offs (precision vs. speed, simple vs. flexible)',
         ],
         'notes': '60+ minutes. The Blockly capstone: nothing new to learn, two open-ended '
                  'challenges. Have a taped course ready on the floor for Challenge 1 (the map '
                  'gives the distances), tape measures, and a marked parking box and LED-capable '
                  'robots for Challenge 2 options.'},

        {'kind': 'bullets', 'title': 'Your Blockly capstone',
         'bullets': [
             'There\'s **nothing new to learn** today',
             'You put **everything** together: loops, functions, parameters, motor control',
             'Two open-ended challenges: precision navigation, then a creative design',
             'Like real engineering problems, these have **many right answers**',
         ],
         'callout': 'Plan first, then build. Predict → test → observe → adjust.',
         'tone': 'teal',
         'notes': 'Set expectations: value the process (planning, iterating, documenting) over a '
                  'flawless result.'},

        {'kind': 'bullets', 'title': 'Challenge 1 · Precision navigation',
         'bullets': [
             'Your robot is a **delivery vehicle**',
             'It has to follow a marked course',
             'Stop on a target within **±30 cm**',
             'Then **signal** that it arrived',
         ],
         'callout': 'Everything you need you already have: Straight, Turn, a function to wrap the '
                    'route, and the debugging loop',
         'tone': 'teal',
         'notes': 'Target: finish within ±30 cm; ±15 cm as a stretch goal.'},

        {'kind': 'figure', 'title': 'The delivery course',
         'figure': '/img/lesson-07/course-map.svg',
         'caption': 'Measure it, then translate it into blocks.',
         'notes': 'Seen from above, drawn to scale (each faint square is 10 cm). The robot starts '
                  'facing up the page with its center of rotation on the start mark. Each turn is '
                  'measured from the way the robot is already facing (the dashed line). The '
                  'dashed red circle is the 30 cm stop zone. Make sure students read turn '
                  'directions off the map rather than guessing: in XRPLib a positive turn is '
                  'counterclockwise (left).'},

        {'kind': 'steps', 'title': 'Plan it, build it, test it in pieces',
         'steps': [
             '**Measure** the course',
             '**Plan** the moves on paper: sketch the segments, label the distances and angles',
             '**Build** it: Straight and Turn blocks, wrapped in a function',
             '**Test it in pieces**: get the first straight-and-turn landing correctly before '
             'you add the next',
         ],
         'callout': 'Far easier than running all five moves and guessing which one is off',
         'tone': 'orange',
         'notes': 'Have teams measure and plan on paper first, before any coding. Push the '
                  'test-in-pieces habit hard: students who build all five moves at once and then '
                  'debug struggle the most. A consistent over- or undershoot is a distance to '
                  'trim; erratic results point to wheel slip or the surface, not the code.'},

        {'kind': 'bullets', 'title': 'Stuck on how to organize it?',
         'tag': 'Only if stuck',
         'bullets': [
             'One clean structure: a **single function** that sequences the whole route',
             [
                 'first leg, first corner, second leg, second corner, final leg',
             ],
             'Call it from a **short main program**',
             'The main program reads as one instruction, and the route lives in **one place** '
             'you can tune',
         ],
         'callout': 'The distances and angles are yours to measure',
         'tone': 'teal',
         'notes': 'The lesson keeps this hint behind a reveal: show it only to teams that are '
                  'stuck on structure after planning on paper. The lesson page draws it as a '
                  'block program; the slide gives it in words, because the generic Straight and '
                  'Turn block pictures show placeholder numbers (20 cm, 90 degrees) that would '
                  'read as course values, and the first corner on this course is a right turn.'},

        {'kind': 'check',
         'question': 'Your robot overshoots the target by about 15 cm every run. What\'s the most '
                     'sensible fix?',
         'options': ['Give up and start over',
                     'Shorten the final Straight distance by roughly 15 cm and re-test',
                     'Increase the effort to 1.0', 'Add more turns'],
         'answer': 1,
         'explanation': 'Consistent overshoot is a measurement to adjust, not a mystery. Trim the '
                        'distance a bit and re-test: predict, test, observe, adjust.'},

        {'kind': 'cards', 'title': 'Challenge 2 · Creative design',
         'cards': [
             ('Option A', 'Multi-shape artist', 'Use your polygon function to lay out a design: '
                                                'pentagon, hexagon, octagon arranged into a '
                                                'pattern.'),
             ('Option B', 'Precision parking', 'Drive in, then use Set effort for a slow, careful '
                                               'final nudge to park centered in a marked box.'),
             ('Option C', 'Robot choreography', 'Combine curves, spins, and the LED into a '
                                                '30-second performance that tells a little story.'),
         ],
         'notes': 'Design your own robotic performance: pick one, or invent your own, and bring '
                  'the whole toolkit. Encourage descriptive function names and a one-line "story" '
                  'describing what the robot does.'},

        {'kind': 'steps', 'title': 'The workflow professionals use',
         'steps': [
             '**Brainstorm**, then **break it into functions**',
             'Write **pseudocode**',
             '**Build the core functions** and **test each** one',
             '**Assemble**, then **refine**',
         ],
         'size': 24,
         'callout': 'Brainstorm → functions → pseudocode → build → test each → assemble → refine',
         'tone': 'teal',
         'notes': 'Give a hard "stop coding" time five minutes early so there\'s room for a '
                  'showcase. Have two or three teams present (what was your goal, which functions '
                  'did you use, what was hardest?) and run quick peer feedback.'},

        {'kind': 'check',
         'question': 'Your creative program is one giant stack of 40 blocks and it\'s hard to '
                     'debug. What\'s the best move?',
         'options': ['Delete it and pick an easier project',
                     'Break it into small named functions and test each one on its own',
                     'Add more blocks until it works', 'Run it faster'],
         'answer': 1,
         'explanation': 'Splitting a big program into small, testable functions is exactly what '
                        'functions are for: it makes bugs easy to isolate.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Space', 'Driving a Mars rover', 'Rover drivers plan each day\'s moves on Earth, send '
                                               'the whole sequence at once, then check where the '
                                               'rover actually stopped before planning the next '
                                               'drive.'),
             ('Warehouses', 'Shelf-carrying robots', 'Warehouse robots drive set routes across the '
                                                     'floor and have to stop on exactly the right '
                                                     'spot to pick up a shelf.'),
             ('Navigation', 'Dead reckoning', 'Before GPS, navigators worked out where they were '
                                              'from heading, speed and time, then corrected at a '
                                              'landmark. Your robot drives the same way.'),
         ],
         'height': 4.2,
         'notes': 'Planning a route, running it, and trimming it until it lands is how real '
                  'machines get where they\'re going.'},

        {'kind': 'bullets', 'title': 'Looking ahead: why Python next?',
         'bullets': [
             'You may have hit Blockly\'s limits today: big programs get unwieldy',
             'Some ideas are just faster to **type** than to drag',
             'That\'s why the next phase moves to **Python**',
             'The good news: the **same concepts** you already know (loops, functions, '
             'parameters), written as text',
         ],
         'callout': 'Same ideas, new way to write them',
         'tone': 'teal',
         'notes': 'Ask who felt the stack getting unwieldy today; that frustration is the '
                  'motivation for Python.'},

        {'kind': 'check',
         'question': 'Moving from Blockly to Python next lesson mostly means…',
         'options': ['Learning brand-new concepts from scratch',
                     'Writing the same ideas (loops, functions, parameters) as typed text',
                     'Giving up on the robot', 'Only drawing shapes'],
         'answer': 1,
         'explanation': 'The logic carries straight over. Python is a new way to write the ideas '
                        'you already understand, not a new set of ideas.'},

        {'kind': 'wrapup',
         'questions': [
             'What\'s the debugging loop?',
             'Why break a big program into functions?',
             'Which Module 1 concept will you lean on most in Python?',
         ],
         'next': 'Lesson 1-8, Hello, Python',
         'notes': 'Answers: predict → test → observe → adjust. Easier to build, test, and fix. '
                  'Their call: loops, functions, and parameters all carry over. Assessment is '
                  'two-part: Challenge 1 within ±30 cm, and a working, creative Challenge 2 with a '
                  'short written reflection (what did you build, which concepts did you use and '
                  'why, what was hardest, what would you improve?). Rubric: planning, '
                  'implementation, debugging evidence, reflection.'},
    ],
}
