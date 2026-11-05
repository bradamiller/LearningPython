DECK = {
    'module': 2, 'lesson': 0,
    'doc': 'module-02-line-tracking/lesson-00-overview',
    'title': 'The Robot Starts to Sense',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Describe what the robot will do by the end of Module 2',
             'Explain the difference between a move that ends after a set distance and a move '
             'that ends when a sensor sees something',
             'Name the one program file you\'ll start in Lesson 2-1 and keep for the rest of '
             'the course',
             'Say what each lesson in the module adds to the robot',
         ],
         'notes': '15 to 20 minutes, no coding yet. This is an advance organizer: the destination '
                  'and the shape of the file, not any one technique. Do not name or explain the '
                  'constructs the lessons are built to make students need (the while loop in 2-2, '
                  'if/else in 2-3, the error and gain in 2-5). If students ask how the robot will '
                  'follow the line, "that is Lesson 2-5" is the whole answer.'},

        {'kind': 'bullets', 'title': 'Module 1: told in advance',
         'bullets': [
             'In Module 1 your robot did exactly what it was told: drive 20 cm, turn 90°, repeat',
             'It never found out where it actually was',
             'Nudge it, or put it on a slippery floor, and it carries on with the plan anyway',
             'And ends up somewhere else',
         ],
         'callout': 'This module changes that',
         'tone': 'orange'},

        {'kind': 'figure', 'title': 'Where this module ends up',
         'figure': '/img/lesson-m2-10/final-project-reverse.svg',
         'crop': (0.0, 0.08, 0.6, 1.0),
         'caption': 'Follow the circle, turn around at the cross, four times, then stop. Nothing '
                    'is measured in centimeters or seconds.',
         'notes': 'This is the Lesson 2-10 project. Every stop and every turn ends because the robot '
                  'saw something. Show it now, and come back to it at the start of Lesson 2-10.'},

        {'kind': 'bullets', 'title': 'Sense, think, act',
         'bullets': [
             'In Lesson 1-0 you decided a robot has to **sense**, **think** and **act**',
             'In Module 1 your XRP mostly **acted**: every decision was yours, made in advance',
             'Module 2 adds the first sense: two **reflectance sensors** at the front, facing '
             'the floor',
             'They tell a white floor from a strip of black tape',
         ],
         'callout': 'Over and over: **what do my sensors see right now, and what should I do '
                    'about it?**',
         'tone': 'teal'},

        {'kind': 'cards', 'title': 'Two ways to end a move',
         'height': 3.4,
         'cards': [
             ('Module 1', 'Told in advance',
              'Drive 20 cm, then turn 90°. The robot finishes the move whatever happens.'),
             ('Module 2', 'Ended by a sensor',
              'Drive **until the sensors see the tape**. The move ends where the tape is.'),
         ],
         'notes': 'The rule for the rest of the course: the robot stops on something it senses, '
                  'not on a clock or a distance. It is why the same program still works with low '
                  'batteries or on a different floor. Students who watched the timed program '
                  'misbehave on two surfaces in Lesson 1-6 already know why.'},

        {'kind': 'check',
         'question': 'Your Module 1 program drives 50 cm to reach a line of tape. Someone moves '
                     'the tape 10 cm further away. What happens, and what would a Module 2 '
                     'program do instead?',
         'options': ['Both programs stop at the tape, because the robot can see it',
                     'The Module 1 program stops 10 cm short; a program that drives until the '
                     'sensors see the tape still stops on it',
                     'Both programs stop 10 cm short',
                     'The Module 2 program needs the new distance typed in'],
         'answer': 1,
         'explanation': 'A move measured in centimeters ends where the numbers say. A move that '
                        'ends on a sensor reading ends where the tape actually is.'},

        {'kind': 'cards', 'title': 'One file, all year: robot.py',
         'height': 3.4,
         'cards': [
             ('Section 1', 'LINE SENSOR',
              'Small functions that **read the tape**: what each sensor sees, on the line or '
              'at a cross.'),
             ('Section 2', 'LINE TRACKING',
              'Functions that **drive on the tape**: follow to the next cross, park, turn onto '
              'the next line.'),
         ],
         'notes': 'From Lesson 2-1 every student keeps one file, robot.py, and every lesson adds '
                  'to it. These two sections drive the robot for the rest of the course: around '
                  'the grid in Module 3, and along the routes it plans itself in Modules 4 and 5.'},

        {'kind': 'table',
         'title': 'Your roadmap (1 of 2)',
         'headers': ['Lesson', 'What the robot learns to do'],
         'widths': [3.6, 7.8],
         'size': 20,
         'rows': [['**2-1** Reflectance Sensor',
                   'Read its two sensors; tell the tape from the floor. `robot.py` is born.'],
                  ['**2-2** Drive to the Edge',
                   'Drive forward and stop the moment it reaches the line'],
                  ['**2-3** Bounce Driving', 'Turn back every time it meets the line'],
                  ['**2-4** Random Turns', 'Turn a different amount each bounce, and explore'],
                  ['**2-5** Proportional Control',
                   'Actually follow the line, steering a little all the time']]},

        {'kind': 'table',
         'title': 'Your roadmap (2 of 2)',
         'headers': ['Lesson', 'What the robot learns to do'],
         'widths': [3.6, 7.8],
         'size': 20,
         'rows': [['**2-6** Two-Sensor Following', 'Follow the center of the line with both sensors'],
                  ['**2-7** Sensor Toolkit', 'Finish LINE SENSOR, and test it all by hand'],
                  ['**2-8** Intersections', 'Notice a cross in the tape, and stop there'],
                  ['**2-9** Line-Tracking Functions', 'Park on the cross and turn onto the next line'],
                  ['**2-10** Final Project', 'Lap the circle, reversing at the cross, four times']],
         'notes': 'The final project needs almost no new code: by then it is a short list of calls to '
                  'functions written and tested earlier. The optional class extensions are in Lessons '
                  '2-7 and 2-9.'},

        {'kind': 'wrapup',
         'questions': [
             'What will the robot do by the end of the module?',
             'What ends each move in this module?',
             'What is robot.py, and what are its first two sections?',
         ],
         'next': 'meet the reflectance sensors, and start robot.py',
         'notes': 'Answers: follow the circle, reverse at the cross four times, and stop. '
                  'Something the sensors see, never a distance or a timer. The one file kept all '
                  'year; LINE SENSOR reads the tape, LINE TRACKING drives on it. Materials: Lesson '
                  '2-1 needs a strip of black tape on a white surface; from 2-2 a taped circle; '
                  'from 2-7 the short strip across it that makes the cross.'},
    ],
}
