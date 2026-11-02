DECK = {
    'module': 1, 'lesson': 2,
    'doc': 'module-01-driving/lesson-02-drawing-shapes',
    'title': 'Drawing Shapes',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Build a program up one step at a time, running it after each change',
             'Make the robot trace a square, and explain why the program needs what it needs',
             'Find a shorter way to write a program that does the same thing many times',
             'Work out the turn angle for any regular shape (`360° ÷ number of sides`)',
         ],
         'notes': '50 to 60 minutes, Blockly. This lesson is a discovery sequence: students '
                  'figure out the square, and the shortcut, before either is explained. Resist '
                  'showing a finished program at any point. Rough budget: 10 minutes for '
                  'straight and turn, 15 for the square, 10 for the shortcut, 15 for other '
                  'shapes.'},

        {'kind': 'bullets', 'title': 'Today: a square, one block at a time',
         'bullets': [
             'In Lesson 1-1 you drove the robot forward and back',
             'Today you get it to draw a **square**',
             'You\'ll work out how, one block at a time. No recipe up front',
             'Along the way you\'ll invent a **shortcut** that programmers use constantly',
         ],
         'notes': 'The whole point is who does the discovering. Students who arrive at "repeat '
                  'the straight-and-turn four times" on their own own the idea of a loop; '
                  'students who are handed the Repeat block have merely seen one. Your job is '
                  'to ask questions, not answer them: "What did the robot do? What do you want '
                  'it to do next? What\'s one block that would get you closer?"'},

        {'kind': 'figure', 'title': 'Where you\'re headed',
         'figure': '/img/lesson-02/square-goal.svg', 'frame': 0.9,
         'crop': (0.0, 0.085, 0.61, 1.0),
         'caption': 'Four equal sides, four equal corners, back to the start facing the same '
                    'way. You\'ll get there one block at a time.',
         'notes': 'On the lesson page this is an animation: the robot carries a marker in the '
                  'hole between its wheels and draws the square as it drives. The slide shows '
                  'the finished drawing. It shows the goal, not the program.'},

        {'kind': 'steps', 'title': 'Activity · Build up to a square',
         'lead': 'Three steps, each one a small change to the program you already have.',
         'steps': [
             '**Drive straight:** 20 centimeters',
             '**Add a turn:** 90 degrees, after the drive',
             '**Make a square:** and end up back where you started',
         ],
         'callout': 'Run the robot after **every** step: watching what it actually does is the '
                    'point',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Step 1 · Drive straight',
         'bullets': [
             'Start a new project in XRP Code',
             '**Find a block that makes the robot drive straight for 20 centimeters.** Look '
             'through the palette, drag it out, set it up',
             'Put a **Wait for button press** block above it',
             'Robot on the floor, click **RUN**, press the button on the robot',
             'Did it go 20 cm? Where did it end up, and which way is it facing?',
         ],
         'size': 22, 'split': 0.5,
         'figure': '/img/lesson-02/l2-step1.svg', 'frame': 0.8,
         'crop': (0.0, 0.085, 0.61, 1.0),
         'notes': 'Let students find the Straight block themselves: say "find a block that '
                  'drives straight" rather than naming it. They are practicing searching the '
                  'palette, which they need again when they hunt for the shortcut. A few will '
                  'forget the button-press block and the robot drives off the table: a memorable '
                  'lesson in why it exists. Keep this part short; it\'s a warm-up.'},

        {'kind': 'bullets', 'title': 'Step 2 · Add a turn',
         'bullets': [
             'Change your program so that **after driving straight, the robot turns 90 '
             'degrees**',
             'Find the block that turns, add it under the Straight block, set the angle',
             '**Predict before you press the button:** where will the robot end up, and which '
             'way will it be facing?',
             'Then run it and check',
         ],
         'callout': 'Predict first, then run',
         'tone': 'orange'},

        {'kind': 'check',
         'question': 'Your program is Straight 20, then Turn 90. After it runs, how has the robot '
                     'changed from where it started?',
         'options': ['It is in the same spot, facing the same way',
                     'It moved 20 cm forward and now faces a quarter-turn from where it started',
                     'It has turned but not moved',
                     'It has driven in a full circle'],
         'answer': 1,
         'explanation': 'Blocks run in order: first the drive, then the turn. So the robot is '
                        '20 cm away AND rotated 90°. A side and a corner: the building block of '
                        'every shape.'},

        {'kind': 'frames', 'title': 'Step 2: one side and one corner',
         'figure': '/img/lesson-02/l2-step2.svg',
         'crop': (0.0, 0.085, 0.61, 1.0),
         'frames': [(0.4, '**Straight:** driving 20 cm forward'),
                    (0.8, '**Turn:** a quarter turn, in place')],
         'callout': 'Drive, then turn in place: one side and one corner',
         'notes': 'Show this after students have predicted and run their own. Ask "what shape '
                  'has the robot drawn so far?" (a single side and a corner, an L). Then ask the '
                  'question that sets up the square: "What would you have to add to draw a '
                  'second side?" Don\'t answer it.'},

        {'kind': 'bullets', 'title': 'Step 3 · Make a square',
         'lead': '**The real challenge:** change your program so the robot drives a complete '
                 'square and ends up back where it started, facing the same way.',
         'lead_h': 1.25,
         'bullets': [
             'You already know everything you need. Use the blocks you have',
             'Try something, run it, watch what happens, adjust, run it again',
             'A first try that\'s a triangle or an open box is fine: that\'s **information**',
         ],
         'callout': '**You\'ve succeeded when** the robot drives four roughly equal sides, turns '
                    'four corners, and finishes near its starting spot',
         'tone': 'green',
         'notes': 'Nearly every student will stack Straight, Turn, Straight, Turn, Straight, '
                  'Turn, Straight, Turn: eight blocks. That is the correct answer for this part. '
                  'Do not suggest a shorter way. If a student finds it in the palette on their '
                  'own, ask them to hold on to it and demonstrate later. Common stumbles: only '
                  'three sides, or a turn of 45° or 180°; they will see the wrong shape and fix '
                  'it.'},

        {'kind': 'frames', 'title': 'A wrong shape tells you what to change',
         'figure': '/img/lesson-02/l2-step3.svg',
         'crop': (0.0, 0.085, 0.61, 1.0),
         'frames': [(0.38, '**A first try:** three sides, not closed'),
                    (0.92, '**The fix:** four sides, closed')],
         'notes': 'The lesson page animates both tries. Here: the first try ends one side short, '
                  'so count again; with one more side and one more corner, the square closes and '
                  'the robot is back on its start mark, facing the way it began.'},

        {'kind': 'bullets', 'title': 'Once your square works, look at your program',
         'bullets': [
             'How many blocks did it take?',
             'Is there anything in it that\'s the same thing, over and over?',
         ],
         'callout': 'Count, then point at anything that repeats',
         'tone': 'teal',
         'notes': 'Once a student\'s square works, ask them to count their blocks and to point at '
                  'anything that\'s repeated. That question is the bridge to the shortcut. The '
                  'lesson page has a working eight-block square behind a reveal for students to '
                  'compare with after theirs runs; it stays off the slides.'},

        {'kind': 'check',
         'question': 'In the eight-block square, what is being repeated, and how many times?',
         'options': ['The Straight block, eight times',
                     'The pair Straight-then-Turn, four times',
                     'The Turn block, eight times',
                     'Nothing is repeated'],
         'answer': 1,
         'explanation': 'Look at the pattern: drive a side, turn a corner. That pair appears four '
                        'times, once per side of the square.'},

        {'kind': 'bullets', 'title': 'Activity · A shorter way to say "four times"',
         'bullets': [
             'You just wrote the same two blocks four times',
             'A shape with 12 sides would take 24 blocks. There has to be a better way',
             '**The palette has a block that repeats whatever you put inside it. Go find it.**',
             'Drag it out, set it to run **4** times, move **one** Straight and **one** Turn '
             'inside it, and delete the other six',
             'Run it. Does the robot still draw a square?',
         ],
         'size': 25,
         'notes': 'Give students a minute or two to find the block themselves (it\'s Repeat, in '
                  'the Loops category). If someone found it while building the square, this is '
                  'their moment to demonstrate. Only after most have tried it, show a finished '
                  'version and name it: a loop, one copy of the instructions run as many times as '
                  'you say. Stress dropping the blocks inside the Repeat\'s mouth: beside it '
                  'instead of inside is the classic error, and the robot drives one side and '
                  'stops. A new Repeat block starts at 10.'},

        {'kind': 'bullets', 'title': 'You just used a loop',
         'bullets': [
             'You write the instructions **once**',
             'The **Repeat** block runs them as many times as you tell it to',
             'One of the most important ideas in all of programming',
             'And you got to it by noticing your own program repeating itself',
         ],
         'callout': 'A **loop**: one copy of the instructions, run as many times as you say',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'A student\'s Repeat-4 program makes the robot drive one side and then stop. '
                     'What\'s the most likely problem?',
         'options': ['The robot is out of battery',
                     'The Straight and Turn blocks are next to the Repeat instead of inside it',
                     'Repeat only works with Turn blocks',
                     'The number 4 is too small'],
         'answer': 1,
         'explanation': 'Only blocks tucked inside the Repeat\'s mouth get repeated. Blocks '
                        'stacked beside it run once, so the robot drives a single side, and the '
                        'empty loop repeats nothing.'},

        {'kind': 'bullets', 'title': 'Activity · Now try a triangle',
         'bullets': [
             'Change your Repeat from 4 to **3**',
             'What angle should the turn be?',
             'Make your best guess, run it, and look at the result',
         ],
         'callout': 'Did it close? Which way is it facing compared to the start?',
         'tone': 'orange',
         'notes': 'Let the wrong angle happen. Most students leave the turn at 90° (three sides '
                  'of a square) or guess 60° because they remember a triangle\'s corners are 60° '
                  '(a wide, open zig-zag). Both failures are the whole point. Ask: "Did it '
                  'close? Which way is it facing compared to the start? How far did it turn in '
                  'total?"'},

        {'kind': 'bullets', 'title': 'Didn\'t close? Walk the triangle yourself',
         'bullets': [
             'Pace out a side',
             'Pivot at the corner the way the robot does',
             'Keep going until you\'re back where you began, **facing the way you started**',
             'How far did you turn **in total**, adding up all three corners?',
         ],
         'callout': 'That total is the whole answer',
         'tone': 'teal',
         'notes': 'Have a student walk the triangle at the front of the room, pivoting at each '
                  'corner, so everyone sees they have turned all the way around by the end. Let '
                  'the class work out what each corner must be before you go on; the lesson '
                  'keeps that step behind a reveal.'},

        {'kind': 'frames', 'title': 'Two tries that don\'t close',
         'figure': '/img/lesson-02/l2-triangle-tries.svg',
         'crop': (0.0, 0.085, 0.61, 1.0),
         'frames': [(0.46, '**Turn 90:** three sides of a square, 270° in total'),
                    (0.92, '**Turn 60:** an open zig-zag, only 180° in total')],
         'callout': 'Keep an eye on the running total: a closed shape has to add up to **one full '
                    'turn**',
         'tone': 'teal',
         'notes': 'Use this for students who are stuck after their first try. On the lesson page '
                  'it is an animation with a running total of the degrees turned at each '
                  'corner.'},

        {'kind': 'check',
         'question': 'A classmate\'s triangle isn\'t closing up: the robot ends facing the wrong '
                     'way. They used Turn 60°. What should it be?',
         'options': ['90°', '120°', '30°', '45°'],
         'answer': 1,
         'explanation': 'A triangle has 3 sides: 360 ÷ 3 = 120°. The turn is the OUTSIDE angle, '
                        'not the 60° inside angle: a common mix-up.',
         'notes': 'Answer: B, 120°. Ask this once students have set their own turn to the angle '
                  'they worked out and seen the triangle close.'},

        {'kind': 'table', 'title': 'Do the reasoning on paper first',
         'lead': 'Sketch a square and walk your pencil around it, writing the turn at each '
                 'corner: four 90s that add up to 360. Then fill in the table.',
         'headers': ['Shape', 'Sides', 'Repeat', 'Turn angle'],
         'rows': [
             ['Triangle', '3', '3', '____'],
             ['Square', '4', '4', '____'],
             ['Pentagon', '5', '5', '____'],
             ['Hexagon', '6', '6', '____'],
             ['Octagon', '8', '8', '____'],
         ],
         'notes': 'The completed table is in the teacher copy on the lesson page. Students who '
                  'fill it in without the rule usually get the triangle row wrong, so that one '
                  'row is the quickest check of whether the idea landed. Collect the table if '
                  'you want a paper artifact: it\'s the only written work in this lesson.'},

        {'kind': 'steps', 'title': 'Activity · Make other shapes',
         'lead': 'Change just two numbers: the repeat count and the turn angle. Predict, then run.',
         'steps': [
             '**Pentagon:** Repeat `5`, and the turn angle from your table. Shorten the sides to '
             '`15` cm so it fits',
             '**Hexagon:** Repeat `6`, and its angle from your table',
             '**Your choice:** pick a number of sides, work out `360 ÷ sides`, predict, run. What '
             'happens as the number of sides gets big?',
         ],
         'callout': 'Doesn\'t close? The angle and the repeat count disagree',
         'tone': 'orange',
         'notes': 'Give each robot a clear patch of floor, about 1 m square at 20 cm sides. '
                  'Lopsided shapes are usually wheel slip: lower Effort to 0.3 on carpet, or '
                  'nudge it to 0.7 if the robot is sluggish. Within about 10% is a success. More '
                  'support: a reference card of angles and a fill-in template "Repeat (__) · '
                  'Straight (__) · Turn (__)." More challenge: a five-point star (Repeat 5, Turn '
                  '144°: ask them to work out why 144 before running it), or two shapes '
                  'back-to-back from the same start.'},

        {'kind': 'check',
         'question': 'What turn angle do you need to draw a regular hexagon (6 sides)?',
         'options': ['90°', '60°', '120°', '45°'],
         'answer': 1,
         'explanation': '360 ÷ 6 = 60°. Split one full turn evenly across all six corners.'},

        {'kind': 'check',
         'question': 'You change a working square program from Repeat 4 to Repeat 6, and set the '
                     'turn to 60°. What does the robot draw?',
         'options': ['A bigger square', 'A hexagon (6 sides)', 'The same square, slower',
                     'An incomplete shape'],
         'answer': 1,
         'explanation': 'Six sides with 60° turns (360 ÷ 6) closes into a hexagon. The side length '
                        'sets the size, not the number of sides.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Manufacturing', 'CNC machines',
              'Cutting tools trace shapes by repeating precise move-and-turn steps, just at much '
              'finer scale.'),
             ('Making', '3D printers',
              'Each layer is a looped path the print head repeats hundreds of times to build up '
              'an object.'),
             ('Art', 'Pen plotters',
              'Drawing robots turn loops of coordinates into logos, maps, and signatures on '
              'paper.'),
         ],
         'notes': 'Repeating a move-and-turn is exactly how machines make precise, repeatable '
                  'paths.'},

        {'kind': 'wrapup',
         'questions': [
             'Why did the eight-block square work, and why is the Repeat version better?',
             'What\'s the rule for the turn angle?',
             'If a shape doesn\'t close, what\'s the first thing to check?',
         ],
         'next': 'tuck the square inside a function, so you can reuse it by name',
         'notes': 'Answers: same result, but one copy of the instructions instead of four, and '
                  'easy to change. 360 ÷ number of sides. The turn angle: did the turns add up to '
                  '360? Formative: did each student get a square working before seeing Repeat, '
                  'and can they say what Repeat does in their own words? Exit ticket: "Octagon: '
                  'what goes in the Repeat, and what\'s the turn?" (8, and 360 ÷ 8 = 45°). Next '
                  'lesson, true to form, students feel the need for a function before they meet '
                  'one.'},
    ],
}
