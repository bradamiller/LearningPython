DECK = {
    'module': 1, 'lesson': 9,
    'doc': 'module-01-driving/lesson-09-variables-and-expressions',
    'title': 'Variables & Expressions',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Explain what `=` does: work out the right side, then store the result in the '
             'named memory location on the left',
             'Reassign a variable, including using its own old value',
             'Name variables the way Python programmers do, and say why `Rangefinder` and '
             '`rangefinder` are different things',
             'Predict the value of an arithmetic expression using operator precedence, and use '
             'parentheses to change it',
         ],
         'notes': '50 to 60 minutes, and no robot needed. Everything runs in the XRP Code '
                  'terminal with print(), so this is the lesson to use when robots are '
                  'unavailable or batteries are flat. It is also the best diagnostic before '
                  'Module 2.'},

        {'kind': 'code', 'title': 'The `=` nobody explained',
         'lead': 'You\'ve already written this line without anyone explaining the `=`. That single '
                 'character is doing something specific, and once you see what, a lot of Python '
                 'stops being mysterious.',
         'lead_h': 1.3,
         'code':'drivetrain = DifferentialDrive.get_default_differential_drive()',
         'code_size': 22,
         'callout': 'Today: the **value** on the right, and the **place it gets stored** on the left',
         'tone': 'teal',
         'notes': 'That single character is doing something specific, and once students see what, '
                  'a lot of Python stops being mysterious. No robot today: everything is checked '
                  'with print() in the terminal.'},

        {'kind': 'bullets', 'title': 'A named place in the robot\'s memory',
         'bullets': [
             'The controller has **memory**: physical storage on the board',
             'Memory is a long bank of **locations**; each holds one value',
             'A **variable** is a location with a **name** you chose',
             'Like post office boxes: each has its own number on the front',
             'Only the clerk reaches in. Here the clerk is the **processor**',
         ],
         'split': 0.56,
         'figure': '/img/lesson-09/memory-post-office.png',
         'notes': 'You can look in a box, put something in it, or replace what is there. Nothing '
                  'goes into a location or comes out of one except through the processor, the '
                  'chip that runs your program.'},

        {'kind': 'code', 'title': 'Claim a location: a name, `=`, a value',
         'code': 'side_length = 30\n'
                 'robot_name = "Bolt"\n'
                 'threshold = 0.5',
         'code_size': 30, 'width': 7,
         'callout': 'After these three lines, memory has three named locations: one holding `30`, '
                    'one holding `"Bolt"`, one holding `0.5`',
         'tone': 'teal'},

        {'kind': 'figure', 'title': 'Three named locations',
         'figure': '/img/lesson-09/memory-locations.svg',
         'caption': 'Three named locations, and two that no program has claimed yet.',
         'notes': 'The numbers on the plates are real: every location has an address, whether or '
                  'not anything is stored there. Students use the name, not the address, for a '
                  'long time; addresses come back in Lesson 4-3 with lists. Leave the address '
                  'alone unless asked. If someone asks: that is how the processor finds the box, '
                  'and you get to use the name instead.'},

        {'kind': 'bullets', 'title': '`=` is an instruction, not a claim',
         'bullets': [
             'In math, `x = 5` is a **claim** that two things are the same',
             'In Python it\'s an **instruction**: store this here',
             'It runs in a specific order: **right side first**, every time',
             'In `side_length = 20 + 5`, Python works out `25`, **then** stores `25` in `side_length`',
             'The location doesn\'t hold "20 + 5". It holds `25`.',
         ],
         'callout': 'Work out whatever is on the **right**. Then store that result in the location '
                    'named on the **left**.',
         'tone': 'teal',
         'notes': 'The one sentence that prevents a month of confusion. Say it, write it on the '
                  'board, and have students say it back. Nearly every later confusion (the '
                  'accumulator in 2-7, error = setpoint - sensor_value in 2-5, the distances '
                  'updates in Module 5) dissolves if they hold onto the order. Name the '
                  'math-class collision out loud. Some teachers say "gets" or "becomes" for = '
                  'all year.'},

        {'kind': 'check',
         'question': 'What is the difference between `=` in math and `=` in Python?',
         'options': ['There is no difference',
                     'It\'s an instruction: work out the right side, then store it in the named '
                     'memory on the left',
                     'In Python it means "is approximately equal to"',
                     'In Python it only works with whole numbers'],
         'answer': 1,
         'explanation': 'Math\'s = states that two things are equal. Python\'s = does something: it '
                        'works out the right-hand side and stores that result in the variable '
                        'named on the left.'},

        {'kind': 'code', 'title': 'Storing something new overwrites what was there',
         'lead': 'A location holds exactly **one** value: a new one takes the old one\'s place. '
                 'That makes the strangest-looking line in programming straightforward:',
         'lead_h': 1.2,
         'code': 'side_length = 30\n'
                 'side_length = 45      # the 30 in that location is overwritten; it now holds 45\n'
                 '\n'
                 'count = 0\n'
                 'count = count + 1     # read count (0), add 1, store 1 back in count\n'
                 'count = count + 1     # read count (1), add 1, store 2 back in count',
         'code_size': 22,
         'callout': 'Read it as "count **becomes** count plus one". The same location is read on '
                    'the right, then written on the left.',
         'tone': 'teal',
         'notes': 'The word variable means it can vary. Draw the location: a rectangle with 2040 above it, a name card under it and a '
                  'number inside. Step through count = count + 1: read the 0 out, add 1 beside '
                  'it, rub out the 0, write the 1 in. The physical erase is the point; students '
                  'who think both values coexist are the ones who get stuck. Students will write '
                  'this exact pattern in Module 2 to count intersections.'},

        {'kind': 'check',
         'question': 'After `total = 10`, then `total = total + 5`, then `total = total + 5`, '
                     'what is `total`?',
         'options': ['10', '15', '20',
                     'It causes an error because total is used to define itself'],
         'answer': 2,
         'explanation': 'Each line reads what is currently in total, works out the right side with '
                        'it, and stores the result back: 10, then 10+5 = 15, then 15+5 = 20.',
         'notes': 'Answer: C. If someone asks about drivetrain = ...: the location holds the '
                  'address of where the drivetrain object lives, not the object itself, because '
                  'something that can grow does not fit in a fixed-size location. Lesson 4-3 '
                  'makes it precise.'},

        {'kind': 'code', 'title': 'Choosing names: `snake_case`',
         'lead': 'All lowercase, words joined by underscores. Code gets read far more often than '
                 'it gets written.',
         'code': 'side_length = 30       # yes\n'
                 'base_effort = 0.5      # yes\n'
                 'sideLength = 30        # works, but not the Python style\n'
                 'SideLength = 30        # works, but this looks like a class (see below)\n'
                 's = 30                 # works, but what is it?',
         'code_size': 20,
         'callout': 'Descriptive beats short: `threshold` says what the number means, `t` doesn\'t. '
                    'The exception is a loop counter like `i`.',
         'tone': 'teal',
         'notes': 'side_length in the Blockly function was chosen in Lesson 1-4 to be the name '
                  'they would want in Python later. The loop counter i arrives next lesson.'},

        {'kind': 'code', 'title': 'Capital letters mean something',
         'lead': 'Python cares about capitals: `Rangefinder` and `rangefinder` are two different '
                 'names. That\'s not a nuisance, it\'s a convention doing real work:',
         'lead_h': 1.2,
         'code': 'from XRPLib.rangefinder import Rangefinder            # Rangefinder -- the class\n'
                 'rangefinder = Rangefinder.get_default_rangefinder()   # rangefinder -- your variable',
         'code_size': 20,
         'callout': '**Capitalized** is the class, the "book on the shelf" from Lesson 1-8. '
                    '**lowercase** is your variable, the one actual thing you use.',
         'tone': 'orange',
         'notes': 'Once students see this pattern they can read the three-step XRPLib code for '
                  'any device and tell at a glance which name is which.'},

        {'kind': 'check',
         'question': 'In the line `reflectance = Reflectance.get_default_reflectance()` what is the '
                     'difference between the two spellings?',
         'options': ['Nothing: Python ignores capital letters',
                     '`Reflectance` (capitalized) is the class; `reflectance` is the variable '
                     'holding your sensor',
                     'The capitalized one is a typo that Python fixes',
                     'Capitalized names are for numbers, lowercase for text'],
         'answer': 1,
         'explanation': 'Python is case-sensitive, and the convention is Capitalized for classes, '
                        'lowercase snake_case for your own variables. Both names are needed and '
                        'they mean different things.'},

        {'kind': 'bullets', 'title': 'Working out the value: expressions',
         'bullets': [
             'Anything Python can work out into a **single value** is an **expression**',
             '`25` is an expression. So is `20 + 5`, and so is `side_length * 2`',
             'Expressions go wherever a value belongs:',
             [
                 'on the right of an `=`',
                 'inside the parentheses when you call something',
                 'anywhere else a value belongs',
             ],
         ],
         'callout': 'Naming a value and working out a new one is most of what any program does',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'The arithmetic operators',
         'code': '7 + 2      # 9\n'
                 '7 - 2      # 5\n'
                 '7 * 2      # 14\n'
                 '7 / 2      # 3.5\n'
                 '7 % 2      # 1   (the remainder after dividing)',
         'code_size': 24, 'width': 9,
         'callout': 'Multiply is `*` and divide is `/`: no × or ÷ on a keyboard. `%` is '
                    '**remainder**, not percent.',
         'tone': 'orange',
         'notes': '7 % 2 is what is left over when 2 goes into 7. Students won\'t need % until '
                  'Module 2, where it is the trick for doing something every 50th time around a '
                  'loop.'},

        {'kind': 'code', 'title': 'Variables in expressions',
         'lead': 'A variable can appear anywhere a number can: by the time Python does the '
                 'arithmetic, the variable has already been replaced by its value.',
         'lead_h': 1.2,
         'code': 'sides = 6\n'
                 'turn_angle = 360 / sides     # right side: 360 / 6 = 60.0',
         'code_size': 24,
         'callout': 'Why `60.0` and not `60`? Whole numbers are **integers**, decimals are '
                    '**floats**, and `/` always hands back a float, even when it comes out even.',
         'tone': 'teal',
         'notes': 'This almost never matters for driving: drivetrain.turn(60.0) turns exactly as '
                  'far as drivetrain.turn(60). It matters for reading output, so that when a '
                  'print() shows 60.0, students know nothing has gone wrong.'},

        {'kind': 'code', 'title': 'Precedence: which operator goes first',
         'lead': 'Same rule as math: `*` and `/` happen **before** `+` and `-`. Here\'s a line '
                 'you\'ll write next lesson, to make each square in a nest bigger than the last:',
         'lead_h': 1.2,
         'code': '20 + 2 * 5      # 30, not 110 -- the 2 * 5 happens first\n'
                 '\n'
                 'size = 20 + square * 5      # square counts 0, 1, 2, 3 -> size is 20, 25, 30, 35',
         'code_size': 22,
         'callout': 'It only works because `square * 5` is worked out **first**. Strictly left to '
                    'right, `20 + square` would come first and the sizes would be wrong.',
         'tone': 'orange',
         'notes': 'Resist teaching PEMDAS as a rule to memorize; they have it already. Teach it as '
                  'a thing that silently produces wrong numbers. A precedence mistake raises no '
                  'error, so the robot drives confidently and wrongly, and students hunt for the '
                  'bug in their motors.'},

        {'kind': 'code', 'title': 'Parentheses beat everything',
         'code': '(20 + 2) * 5     # 110 -- now the addition goes first\n'
                 '\n'
                 'threshold = (white_reading + black_reading) / 2',
         'code_size': 24,
         'callout': 'Drop the parentheses and only the black reading is halved. The robot still '
                    'runs; it just reads the line wrong.',
         'tone': 'orange',
         'notes': 'The threshold line is from Module 2: the value that tells line from floor is the '
                  'midpoint of two readings. A wrong number is a far more annoying mistake than a '
                  'crash. Professionals add parentheses they don\'t strictly need: '
                  '20 + (square * 5) behaves identically and reads better.'},

        {'kind': 'check',
         'question': 'What is the value of `10 + 4 * 2` ?',
         'options': ['28', '18', '80', '16'],
         'answer': 1,
         'explanation': 'Multiplication goes before addition: 4 * 2 = 8 first, then 10 + 8 = 18. '
                        'To get 28 you would need parentheses: (10 + 4) * 2.'},

        {'kind': 'check',
         'question': 'Your white reading is 0.2 and your black reading is 0.8, and you want the '
                     'midpoint (0.5). Which line gives it?',
         'options': ['`threshold = white + black / 2`', '`threshold = (white + black) / 2`',
                     '`threshold = white + black // 2`', 'Both of the first two work'],
         'answer': 1,
         'explanation': 'Without parentheses, only black is divided: 0.2 + 0.4 = 0.6, not the '
                        'midpoint. The parentheses force the addition first: (0.2 + 0.8) / 2 = 0.5.'},

        {'kind': 'code', 'title': 'Activity · Predict, then print', 'tag': 'Activity',
         'lead': 'No robot. Write your prediction next to each line **on paper first**, then type '
                 'them into XRP Code, run, and compare.',
         'lead_h': 1.2,
         'code': 'print(3 + 4 * 2)\n'
                 'print((3 + 4) * 2)\n'
                 'print(10 / 4)\n'
                 'print(10 - 2 - 3)\n'
                 'print(2 * 3 + 4 * 5)\n'
                 'print(100 / 10 / 2)',
         'code_size': 22, 'width': 6.5,
         'callout': 'Got one wrong? Work out **why** before moving on: write out the order Python '
                    'used, one step at a time.',
         'tone': 'orange',
         'notes': 'Answers for the teacher: 11, 14, 2.5, 5, 26, 5.0. The two same-precedence cases '
                  '(10 - 2 - 3 and 100 / 10 / 2) are there deliberately: students over-apply the '
                  'rule and decide some hidden precedence must reorder them. Equal operators '
                  'simply run left to right. A student who can predict these six has the mental '
                  'model for proportional control.'},

        {'kind': 'steps', 'title': 'Activity · Keep predicting', 'start': 3,
         'steps': [
             'Predict, then check the accumulator: `count = 0`, then `count = count + 3`, then '
             '`count = count * 2`, then `print(count)`',
             'Set `sides = 8` and write one line that prints the turn angle for an eight-sided '
             'shape (you did this in Lesson 1-5 with blocks)',
             '**Challenge:** `white = 0.25` and `black = 0.75`. Write one line that prints the '
             'midpoint. This is the real calculation you\'ll make in Module 2.',
         ],
         'notes': 'Step 3 of the activity on the page (the accumulator) gives 6: 0 + 3 is 3, then '
                  '3 * 2 is 6. Circle back to the challenge in Lesson 2-1, when students compute '
                  'a real threshold from their own robot\'s readings.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Games', 'Score and health', '`score = score + 100` after a pickup is the same '
                                           'accumulator you just wrote.'),
             ('Money', 'Totals and tax', 'Checkout code is a stack of expressions: subtotal, '
                                         'discount, tax, total, each named so the next line can '
                                         'use it.'),
             ('Science', 'Sensor math', 'Every instrument converts a raw reading into a real '
                                        'measurement with arithmetic like this, parentheses and '
                                        'all.'),
         ],
         'notes': 'Naming a value and working out a new one is most of what any program does.'},

        {'kind': 'wrapup',
         'questions': [
             'What are the two steps Python takes on a line like `size = 20 + 5`?',
             'How can `count = count + 1` make sense?',
             'Which happens first in `3 + 4 * 2`, and how would you change it?',
             'What\'s the difference between `Rangefinder` and `rangefinder`?',
         ],
         'next': 'Python for loops, the text version of the Repeat block',
         'notes': 'Answers: work out the right side, then store it in size. Read what is in the '
                  'location, add 1, store it back, overwriting. The multiplication; use '
                  'parentheses. Capitalized is the class, lowercase is your variable. Exit ticket: '
                  '"Write one line that sets perimeter to the distance around a square whose side '
                  'is side_length" (perimeter = side_length * 4). Next lesson\'s nested squares use '
                  'size = 20 + square * 5, straight out of today\'s precedence section.'},
    ],
}
