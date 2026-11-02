DECK = {
    'module': 1, 'lesson': 12,
    'doc': 'module-01-driving/lesson-12-python-final-project',
    'title': 'Python Final Project',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Design a complete program, from a problem statement to a working robot',
             'Combine loops, functions and parameters in one purposeful program',
             'Test and debug systematically, and document your code so others can read it',
             'Present your work and reflect on what you learned',
         ],
         'notes': 'Multi-day capstone and the summative assessment for Module 1. Run it as an arc: '
                  'plan, build, test, document, present.'},

        {'kind': 'bullets', 'title': 'The capstone of Module 1',
         'bullets': [
             'Design and build your **own** complete Python program for the XRP',
             'Pull together everything you\'ve learned: **loops, functions, parameters, motor '
             'control** and **geometric thinking**',
             'It\'s both a real project and your **proof of mastery**',
         ],
         'callout': 'Plan, build, test, document, present',
         'tone': 'teal',
         'notes': 'Teams of 2 to 3 with rotating roles (programmer, tester, documenter) work well. '
                  'Have teams turn in a short written plan before they code.'},

        # ---- Pick your project
        {'kind': 'cards', 'title': 'Activity · Pick your project',
         'height': 4.9,
         'cards': [
             ('Option A', 'Polygon artist', 'Use a polygon function to compose a geometric art '
                                            'piece: nested shapes, a star, a repeating pattern. '
                                            'A great fit if you liked Lesson 1-5.'),
             ('Option B', 'Precision navigation', 'Build a delivery robot: functions for each '
                                                  'course segment, hit waypoints accurately, and '
                                                  'return home.'),
             ('Option C', 'Sensor behavior', '(Stretch) Use the rangefinder or reflectance '
                                             'sensors so the robot reacts to its world: avoid an '
                                             'obstacle, follow a line.'),
             ('Option D', 'Your own idea', 'Anything that shows off Module 1 skills: a race '
                                           'timer, a robot dance, a maze runner. Clear it with '
                                           'your teacher first.'),
         ],
         'notes': 'Choose one path, or pitch your own to the teacher. Option C reaches ahead to '
                  'sensors, which Module 2 covers properly, so treat it as a stretch.'},

        # ---- Plan before you code
        {'kind': 'steps', 'title': 'Activity · Plan before you code',
         'lead': 'Professionals design before they build. On paper first:',
         'steps': [
             '**Problem statement:** one or two sentences. What will your robot do?',
             '**Function inventory:** list the functions you\'ll need, with their parameters '
             '(e.g. `polygon(sides, side_length)`, `navigate_segment(distance, angle)`)',
             '**Pseudocode:** the flow in plain English, not Python',
         ],
         'notes': 'Collect the written plan (problem, function list, pseudocode) before teams '
                  'start coding.'},

        {'kind': 'code', 'title': 'Pseudocode: plain English, not Python',
         'code': 'Program:\n'
                 '    set up the robot\n'
                 '    for each shape in my design:\n'
                 '        draw the shape\n'
                 '        move to the next spot\n'
                 '    announce "done"',
         'code_size': 26, 'width': 8.5,
         'callout': 'The flow in plain English first. The Python comes after the plan.',
         'tone': 'teal',
         'notes': 'The point is the shape of the program, not the syntax. Students who can\'t '
                  'write the pseudocode aren\'t ready to write the Python yet.'},

        {'kind': 'check',
         'question': 'You\'re about to build a 60-block-worth Python program. What\'s the smartest '
                     'way to start?',
         'options': ['Write the whole thing, then run it once at the end',
                     'Write and test one small function at a time, then combine them',
                     'Copy a classmate\'s program',
                     'Skip planning and improvise'],
         'answer': 1,
         'explanation': 'Build and test in small pieces (unit testing), then integrate. It\'s far '
                        'easier to find a bug in one small function than in a giant program.'},

        # ---- A clean program structure
        {'kind': 'bullets', 'title': 'A clean program structure',
         'lead': 'Good Python programs have a shape:',
         'lead_h': 0.75,
         'bullets': [
             'A **docstring** at the top saying what this is',
             'The **imports** and **setup**',
             'Your **functions**',
             'Finally, the handful of lines that actually **run** the show',
         ],
         'callout': 'Use the skeleton on the next two slides as your starting point',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'The skeleton, top half',
         'code': '"""\n'
                 'Module 1 Final Project: <your project name>\n'
                 'Team: <names>\n'
                 'Description: <two-sentence overview>\n'
                 '"""\n'
                 '\n'
                 'from XRPLib.differential_drive import DifferentialDrive\n'
                 'from XRPLib.board import Board\n'
                 'import time\n'
                 '\n'
                 'drivetrain = DifferentialDrive.get_default_differential_drive()\n'
                 'board = Board.get_default_board()\n'
                 '\n'
                 '# ===== HELPER FUNCTIONS =====\n'
                 'def calculate_angle(sides):\n'
                 '    """Return the exterior angle of a regular polygon."""\n'
                 '    return 360 / sides',
         'code_size': 17,
         'notes': 'This is the skeleton the lesson gives, split over two slides to fit. It is a '
                  'starting layout, not anyone\'s project: students replace the example functions '
                  'and run lines with their own.'},

        {'kind': 'code', 'title': 'The skeleton, bottom half',
         'code': '# ===== MAIN FUNCTIONS =====\n'
                 'def polygon(sides, side_length):\n'
                 '    """Draw one regular polygon."""\n'
                 '    angle = calculate_angle(sides)\n'
                 '    for i in range(sides):\n'
                 '        drivetrain.straight(side_length)\n'
                 '        drivetrain.turn(angle)\n'
                 '\n'
                 '# ===== RUN =====\n'
                 'board.wait_for_button()\n'
                 '\n'
                 'print("Starting...")\n'
                 'polygon(4, 30)\n'
                 'time.sleep(1)\n'
                 'polygon(6, 25)\n'
                 'print("Done!")',
         'code_size': 18},

        {'kind': 'bullets', 'title': 'Define above, run below',
         'bullets': [
             'Everything above `# ===== RUN =====` **defines** things',
             'Nothing happens until the lines beneath it',
             'Someone opening your file can read the last few lines to find out what the program '
             'does, then go looking for the function that does it',
             'Order still matters, as in Lesson 1-11: a function has to be defined **above** the '
             'line that calls it, so the running code sits at the bottom',
         ]},

        # ---- Two kinds of note
        {'kind': 'bullets', 'title': 'Two kinds of note: comments',
         'bullets': [
             'The `#` lines are **comments**, the kind you met in Lesson 1-8',
             'Python ignores everything after the `#`',
             'Banner lines divide a long file into **labeled regions** you can find at a glance',
         ],
         'split': 0.5,
         'code': '# ===== HELPER FUNCTIONS =====',
         'code_size': 22},

        {'kind': 'code', 'title': 'Two kinds of note: docstrings',
         'lead': 'A string in quotes, written on its own as the **first thing inside** a function, '
                 'a class or a file, is a **docstring**, short for documentation string.',
         'lead_h': 1.2,
         'code': 'def calculate_angle(sides):\n'
                 '    """Return the exterior angle of a regular polygon."""\n'
                 '    return 360 / sides',
         'code_size': 22,
         'callout': 'Triple quotes are ordinary Python quotes that can run across several lines. '
                    'That\'s why the one at the top of the file can hold a title, a team and a '
                    'description.',
         'callout_size': 21,
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'A docstring doesn\'t vanish',
         'bullets': [
             'Python **keeps** a docstring, attached to the thing it describes',
             '`help(calculate_angle)` prints that sentence, and your editor shows it when you hover over a call',
             'A `#` comment above the `def` looks almost the same, but is gone the moment the file is loaded',
             'Write one sentence, present tense, saying what the caller gets: "Return the exterior '
             'angle of a regular polygon", not "This function calculates..."',
         ],
         'callout': '**Docstring** for what a function is for. **Comment** for why a line is the way it is.',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Write for the person who opens this in six months',
         'lead': 'That person is usually you.',
         'lead_h': 0.7,
         'bullets': [
             'Worth writing: what the code **can\'t say on its own**',
             ['Why the effort is `0.5` and not `0.8`',
              'Which surface you measured the turn on',
              'What you already tried that didn\'t work'],
             'Noise: a comment that just **renames** the line beneath it',
             ['`# turn 90 degrees` above `drivetrain.turn(90)`'],
         ],
         'callout': 'Change the code and that comment quietly goes stale: a lie waiting to happen',
         'tone': 'orange',
         'notes': 'Students arrive commenting nothing, or commenting every line. A comment is a '
                  'message to a future reader; the test is whether it says something the code '
                  'cannot. Two-minute demo: put "# turn 90 degrees" above drivetrain.turn(90), '
                  'change the call to turn(120), and ask what the comment is now. Stale comments '
                  'are worse than none, because people believe them. Don\'t grade docstrings on '
                  'wording: one clear sentence per function is the whole ask. Show help() in the '
                  'shell once, so they see their own docstring come back out.'},

        {'kind': 'code', 'title': 'Two ways to describe a function',
         'lead': 'Look at both notes in this snippet, then answer the question on the next slide.',
         'code': '# Return the exterior angle\n'
                 'def calculate_angle(sides):\n'
                 '    """Return the exterior angle."""',
         'code_size': 26,
         'notes': 'The knowledge check in the lesson shows this code with the question. The '
                  'question slide can\'t hold code, so it sits here first.'},

        {'kind': 'check',
         'question': 'What is the difference between these two ways of describing a function?',
         'options': ['Python keeps the docstring for tools like `help()`; the comment is discarded',
                     'There is no difference: both are ignored by Python',
                     'The comment is kept and the docstring is discarded',
                     'Docstrings are only allowed at the top of a file'],
         'answer': 0,
         'explanation': 'Both are for humans, but only the docstring survives: Python attaches it '
                        'to the function, so `help()` and your editor can show it. A comment is '
                        'thrown away once the file is read.'},

        # ---- Build, test, polish
        {'kind': 'steps', 'title': 'Activity · Build, test, and polish',
         'lead': 'Work the same loop engineers use:',
         'steps': [
             '**Build** one function, then **test** it on its own with a few inputs',
             '**Integrate:** call it from the run section alongside the others, and test the flow',
             '**Instrument:** sprinkle `print()` messages so you can see what\'s happening',
             '**Polish:** a one-line docstring on each function, comments where a line needs a '
             '**why**, no leftover debug prints, clear names',
         ],
         'notes': 'Enforce test-in-pieces. A simple rubric weights design and planning, '
                  'implementation, testing evidence, documentation and a short reflection roughly '
                  'equally. Reward process and debugging, not just a flawless demo.'},

        {'kind': 'check',
         'question': 'Your program runs but the robot behaves differently each time on the same '
                     'code. Most likely cause?',
         'options': ['A syntax error',
                     'Physical factors: wheel slip, surface, or battery level',
                     'The function names are wrong',
                     'Python is broken'],
         'answer': 1,
         'explanation': 'If the code is unchanged and the result varies, it\'s usually physics '
                        '(grippier surface, fresher battery, or wheel slip), not a code bug.'},

        # ---- Show it and reflect
        {'kind': 'wrapup', 'title': 'Activity · Show it and reflect',
         'questions': [
             'What did you build, and what does it do?',
             'Which Module 1 concepts did you use, and why?',
             'What was the hardest bug, and how did you crack it?',
             'If you had more time, what would you add?',
         ],
         'notes': 'Demo the robot, then write a short reflection on these four questions. A '
                  'five-minute showcase at the end lets everyone see the range of solutions.'},

        {'kind': 'bullets', 'title': 'You made it',
         'bullets': [
             'You started Module 1 dragging a single Drive block',
             'You\'re finishing it designing **complete Python programs**',
             'Loops, functions and parameters are exactly the tools real robotics engineers use '
             'every day',
             'They carry straight into the next module',
         ],
         'callout': 'Next: Module 2 · Line Tracking. The robot starts reacting to the world.',
         'tone': 'green',
         'notes': 'The final project is the summative assessment for Module 1; a 50-point rubric '
                  'across design, implementation, testing, documentation and reflection works '
                  'well. Module 2 brings sensors and control loops, the first while loops, and '
                  'students\' own sensor classes.'},
    ],
}
