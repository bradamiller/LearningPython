SQUARE_DEF = [
    {'name': 'function_def_square', 'alt': 'function definition named square', 'children': [
        {'name': 'repeat_4', 'alt': 'repeat 4 times', 'children': [
            {'name': 'straight_cm30', 'alt': 'Straight cm 30'},
            {'name': 'turn', 'alt': 'Turn Deg 90'},
        ]},
    ]},
]

SQUARE_CALLS = [
    {'name': 'call_square', 'alt': 'square call block'},
    {'name': 'call_square', 'alt': 'square call block'},
    {'name': 'call_square', 'alt': 'square call block'},
]

DECK = {
    'module': 1, 'lesson': 11,
    'doc': 'module-01-driving/lesson-11-python-functions',
    'title': 'Python Functions',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Define a function in Python with `def name(parameters):`',
             'Call a function with arguments and use its parameters, including ones with a default value',
             'Return a value from a function and use it',
             'Explain why a function\'s variables are **local**, and why it can still read `drivetrain`',
         ],
         'notes': '50 to 60 minutes. Students already built functions in Blockly with the "to do '
                  'something" block in Lessons 1-3 to 1-5. Today is the same idea in Python, plus '
                  'parameters and return values.'},

        # ---- From "to do something" to def
        {'kind': 'bullets', 'title': 'From "to do something" to `def`',
         'bullets': [
             'Lessons 1-3 to 1-5: reusable functions with the **"to do something"** block',
             'Now the same idea in Python, with the `def` keyword: **define once, call many times**',
             'Plus: pass in **parameters**, and hand back a **return** value',
         ],
         'figure': SQUARE_DEF,
         'split': 0.46,
         'callout': 'The definition doesn\'t drive anything on its own. It says what a square is.',
         'tone': 'teal',
         'notes': 'This is the reusable square from Lesson 1-3. In Blockly the definition sits off '
                  'to one side of the workspace, apart from the calls.'},

        {'kind': 'bullets', 'title': 'The calls',
         'bullets': [
             'Three squares, three call blocks',
             'In Blockly the definition and the calls are **two separate things** in the workspace',
             'In Python both halves live in the **same file**: the `def` block first, then the calls underneath it',
         ],
         'figure': SQUARE_CALLS,
         'split': 0.64},

        {'kind': 'code', 'title': 'The same square in Python',
         'code': 'def square():\n'
                 '    for i in range(4):\n'
                 '        drivetrain.straight(30)\n'
                 '        drivetrain.turn(90)\n'
                 '\n'
                 'square()\n'
                 'square()\n'
                 'square()',
         'code_size': 26, 'width': 7.5,
         'callout': 'Definition at the top, calls underneath',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'The pieces map to what you know',
         'bullets': [
             '`def`: the keyword that **defines** a function (like the "to do something" block)',
             '`square`: the name (lowercase, words joined by underscores)',
             '`()`: the parameter list (empty for now)',
             '`:` and indentation: everything indented is the function **body**',
             '`square()`: **calls** it. Define it once at the top, call it as often as you like',
         ],
         'split': 0.54,
         'code': 'def square():\n'
                 '    for i in range(4):\n'
                 '        drivetrain.straight(30)\n'
                 '        drivetrain.turn(90)\n'
                 '\n'
                 'square()',
         'code_size': 18,
         'notes': 'Order matters in Python, a difference from Blockly: Python reads top to bottom, '
                  'so a function must be defined above the line that calls it. "Called before it\'s '
                  'defined" is a common first error, and the fix is to move the def block up. '
                  'This is the text version of the same define/call idea from Lesson 1-3.'},

        {'kind': 'check',
         'question': 'Which keyword defines a function in Python?',
         'options': ['`function`', '`def`', '`define`', '`func`'],
         'answer': 1,
         'explanation': 'Python uses `def`, followed by the function name, parentheses, and a colon.'},

        # ---- Parameters
        {'kind': 'bullets', 'title': 'Parameters make it flexible',
         'lead': 'Like the gear icon added an input in Blockly, a name inside the parentheses adds a parameter.',
         'lead_h': 1.5,
         'bullets': [
             '`side_length` is the **parameter**: a local variable',
             '`30`, `50` and `20` are the **arguments**, the values you pass in',
             'Same names you used in Blockly',
         ],
         'split': 0.46,
         'code': 'def square(side_length):\n'
                 '    for i in range(4):\n'
                 '        drivetrain.straight(side_length)\n'
                 '        drivetrain.turn(90)\n'
                 '\n'
                 'square(30)\n'
                 'square(50)\n'
                 'square(20)',
         'code_size': 18,
         'callout': 'Add more parameters with commas: `def square(side_length, effort):`',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'Given `def square(side_length):`, what does calling `square(45)` make the robot do?',
         'options': ['Draw a square with 45 cm sides', 'Draw a square with 90 cm sides',
                     'Turn 45 degrees', 'Cause an error: you must pass two numbers'],
         'answer': 0,
         'explanation': 'The argument 45 fills the `side_length` parameter, so each Straight drives '
                        '45 cm. One parameter, one argument.'},

        # ---- Returning a value
        {'kind': 'bullets', 'title': 'Returning a value',
         'bullets': [
             'Some functions **do** something (draw a square)',
             'Others **calculate** something and **return** an answer',
             'The `return` keyword hands a value back to whoever called it',
             'Store it in a variable, print it, or use it in another calculation',
         ],
         'split': 0.46,
         'code': 'def calculate_angle(sides):\n'
                 '    return 360 / sides\n'
                 '\n'
                 'angle = calculate_angle(6)\n'
                 'print(f"Hexagon angle: {angle}")\n'
                 '# -> Hexagon angle: 60.0',
         'code_size': 18,
         'notes': 'In the lesson the output comment sits at the end of the print line; the slide '
                  'puts it on its own line to fit. 360 / 6 is 60.0 because / always gives a '
                  'float.'},

        {'kind': 'code', 'title': 'Bigger functions from smaller ones',
         'lead': 'A `polygon` that uses `calculate_angle`:',
         'code': 'def polygon(sides, side_length):\n'
                 '    angle = calculate_angle(sides)\n'
                 '    for i in range(sides):\n'
                 '        drivetrain.straight(side_length)\n'
                 '        drivetrain.turn(angle)\n'
                 '\n'
                 'polygon(4, 30)   # square\n'
                 'polygon(3, 25)   # triangle\n'
                 'polygon(8, 15)   # octagon',
         'code_size': 22,
         'notes': 'Same polygon idea students built in Blockly in Lesson 1-5. Point out that the '
                  'return value of one function becomes a variable inside another.'},

        # ---- Where a variable lives
        {'kind': 'code', 'title': 'Where a variable lives',
         'lead': '`angle` is created inside `polygon`, so it is **local** to it: it comes into '
                 'existence when `polygon` starts, and is gone when it finishes.',
         'lead_h': 1.2,
         'code': 'def polygon(sides, side_length):\n'
                 '    angle = calculate_angle(sides)      # angle is born here\n'
                 '    ...                                 # and dies when polygon returns\n'
                 '\n'
                 'polygon(4, 30)\n'
                 'print(angle)          # NameError -- there\'s no angle out here',
         'code_size': 20,
         'callout': 'Parameters are locals too. They just arrive already holding the values you passed in.',
         'tone': 'teal',
         'notes': 'Ask for angle from the main program and Python says it doesn\'t know the name. '
                  'sides and side_length are locals as well.'},

        {'kind': 'bullets', 'title': 'A feature, not a restriction',
         'bullets': [
             'Each call gets its **own** locals',
             'Two different functions can both use a parameter called `sides` without interfering',
             'A function\'s working names are **sealed inside it**',
             'So you can write one without checking what every other function happens to call things',
         ]},

        {'kind': 'code', 'title': 'So why does `drivetrain` work?',
         'lead': 'It breaks the pattern. `drivetrain` isn\'t a parameter, and it isn\'t created '
                 'inside `square`. It\'s defined out in the main program.',
         'lead_h': 1.2,
         'code': 'drivetrain = DifferentialDrive.get_default_differential_drive()\n'
                 '\n'
                 'def square(side_length):\n'
                 '    for i in range(4):\n'
                 '        drivetrain.straight(side_length)      # not local -- where\'s this from?',
         'code_size': 18},

        {'kind': 'bullets', 'title': 'Local first, then look outward',
         'bullets': [
             'When Python meets a name inside a function, it looks for a **local** one first',
             'If there isn\'t one, it looks **outside** the function',
             'So a function can **read** names from the surrounding program',
         ],
         'callout': 'That\'s why the three-step XRPLib pattern works: make the drivetrain once at '
                    'the top, and every function you write can reach it',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Reading is fine, assigning is different',
         'bullets': [
             '**Reading** an outside name from inside a function is fine. This course does it constantly',
             '**Assigning** to one is a different matter: Python deliberately makes it awkward',
             ['`drivetrain = something` inside a function creates a **new local** by that name',
              'It does not change the outer one'],
             'We won\'t need that in Module 1',
         ],
         'callout': 'In Module 2, `self.` is the clean answer to "how does an object remember something between calls"',
         'tone': 'orange',
         'notes': 'Don\'t over-promise the sealed box. "Functions can\'t see outside themselves" is '
                  'a simplification students will disprove at once, since every robot program '
                  'calls drivetrain from inside a function. Teach the real rule: local first, '
                  'then look outward. Keep global out of it; it isn\'t needed in this course. The '
                  'read/write asymmetry nudges toward passing values in and returning them out, '
                  'the habit Module 2\'s classes formalize. If asked about a local with the same '
                  'name as an outer one: the local wins inside the function and the outer one is '
                  'untouched. Two print() calls demonstrate it in thirty seconds.'},

        {'kind': 'check',
         'question': 'A variable created inside a function (like `angle` above) can be used...',
         'options': ['Anywhere in the program', 'Only inside that function: it is local',
                     'Only after the program ends', 'Only in other functions'],
         'answer': 1,
         'explanation': 'Variables defined in a function are local to it: they\'re created when the '
                        'function runs and gone when it returns. Code outside can\'t see `angle`.'},

        {'kind': 'check',
         'question': 'If a function\'s variables are local, how can `square()` use `drivetrain`, '
                     'which was created in the main program?',
         'options': ['Because `drivetrain` is special to XRPLib',
                     'If a name isn\'t local, Python looks outside: functions can read outer names',
                     'It does not work; that program has a bug',
                     'Because `drivetrain` is passed in automatically'],
         'answer': 1,
         'explanation': 'Python checks for a local name first, then looks outward. Reading an outer '
                        'name works, so one drivetrain made at the top serves every function. '
                        'Assigning to it from inside is what doesn\'t behave as you\'d expect.'},

        {'kind': 'check',
         'question': 'What\'s wrong with this?   `def multiply(x, y)`',
         'options': ['`multiply` should be capitalized', 'It is missing the colon: `def multiply(x, y):`',
                     '`x` and `y` need quotes', 'Nothing is wrong'],
         'answer': 1,
         'explanation': 'A `def` line, like a `for` line, must end with a colon before its indented body.'},

        # ---- Defaults
        {'kind': 'bullets', 'title': 'Giving a parameter a default',
         'bullets': [
             'Some functions have an obvious **usual** answer',
             'If nine calls out of ten are `square(30)`, typing the `30` every time is noise',
             'Python lets you write that usual value into the definition',
         ],
         'split': 0.5,
         'code': 'def square(side_length=30):\n'
                 '    for i in range(4):\n'
                 '        drivetrain.straight(side_length)\n'
                 '        drivetrain.turn(90)',
         'code_size': 18,
         'callout': 'The `=30` doesn\'t run when the function is defined. It is a **fallback** for '
                    'the calls that don\'t supply one.',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'The call wins',
         'lead': 'The same definition, called two ways:',
         'code': 'square()      # no argument given -> side_length is 30\n'
                 'square(50)    # argument given -> side_length is 50',
         'code_size': 24,
         'callout': '`side_length` is still a local name that arrives holding a value. The value now '
                    'has two places it can come from, and the call wins whenever it offers one.',
         'callout_size': 21,
         'tone': 'orange'},

        {'kind': 'code', 'title': 'One rule: defaults go last',
         'lead': 'Some parameters can have defaults and others not, but **the ones with defaults go last**.',
         'code': 'def polygon(sides, side_length=30):    # fine\n'
                 'def polygon(sides=4, side_length):     # SyntaxError',
         'code_size': 24,
         'callout': 'Python matches arguments to parameters left to right. In `polygon(6)`, an '
                    'optional one in the middle would leave no way to tell where the `6` goes.',
         'callout_size': 21,
         'tone': 'teal',
         'notes': 'Defaults come back in the planner classes: BFS(rows=4, cols=4) in Lesson 5-5\'s '
                  'class extension and again in Lesson 6-5. Nearly every grid is 4 by 4, so it is '
                  'almost always made as plain BFS(), while a different grid is one argument away. '
                  'Watch for students reading = in a def line as an assignment that runs. Settle '
                  'it by calling the function both ways and printing the parameter.'},

        {'kind': 'check',
         'question': 'Given `def polygon(sides, side_length=30):`, what does calling `polygon(6)` draw?',
         'options': ['A hexagon with 30 cm sides', 'A hexagon with 6 cm sides', 'A 30-sided shape',
                     'An error: `polygon` needs two arguments'],
         'answer': 0,
         'explanation': 'Arguments fill parameters from the left, so the 6 goes to `sides`. No second '
                        'argument was given, so `side_length` falls back to its default of 30.'},

        # ---- Activity
        {'kind': 'steps', 'title': 'Activity · Build a shape library',
         'steps': [
             'Write `polygon(sides, side_length)` and test it on three shapes: the function you built in Blockly in Lesson 1-5, now in Python',
             'Add a helper `calculate_perimeter(sides, side_length)` that **returns** `sides * side_length`, and print the perimeter after drawing',
             '**Challenge:** give `polygon` a default `side_length`, so `polygon(6)` draws a hexagon with 30 cm sides. Check that `polygon(6, 50)` still overrides it',
         ],
         'notes': 'More support: start with a no-parameter def say_hello() that prints "Hello", and '
                  'a fill-in-the-blank skeleton before robot code. More challenge: a full shape '
                  'library (star, spiral), or functions that call functions. Encourage a one-line '
                  'docstring under each def: "a sentence saying what it does, in quotes, as the '
                  'first line". Lesson 1-12 explains docstrings properly.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Everywhere', 'Standard libraries', 'Languages ship thousands of ready-made functions. '
                                                  'You call them without knowing the internals.'),
             ('Teams', 'Shared code', 'Engineers split a big system into functions so many people '
                                      'can work on it at once.'),
             ('Robotics', 'Motion & perception', '"read distance", "drive to", "plan path": real '
                                                 'robot code is functions calling functions.'),
         ],
         'notes': 'Functions with parameters and return values are the building blocks of every '
                  'program.'},

        {'kind': 'wrapup',
         'questions': [
             'What keyword defines a function, and what punctuation must end the line?',
             'What\'s the difference between a parameter and an argument?',
             'What does `return` do?',
             'What does a default do, and where must defaulted parameters go?',
         ],
         'next': 'Lesson 1-12, the Python final project',
         'notes': 'Answers: def, and a colon. Parameter = the name in the def; argument = the value '
                  'in the call. return sends a value back to whoever called the function. A '
                  'default supplies a value when the call doesn\'t; defaulted parameters go last. '
                  'Formative: correct def syntax, using parameters in the body, reading a return. '
                  'Exit ticket: "Write add(a, b) that returns a + b." Lesson 1-12 is the capstone: '
                  'students design and build their own complete Python program.'},
    ],
}
