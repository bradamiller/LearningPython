DECK = {
    'module': 1, 'lesson': 8,
    'doc': 'module-01-driving/lesson-08-hello-python',
    'title': 'Hello, Python',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Explain why we move from Blockly to Python, and translate a block into the '
             'equivalent Python code',
             'Follow the first three of Python\'s five syntax rules: lowercase, parentheses, quotes',
             'Use the three-step XRPLib pattern (import the class, make an instance, call its '
             'methods) to drive the robot from Python',
             'Use `print()` to show messages and debug',
         ],
         'notes': '50 to 60 minutes. Blockly to text. Nothing here is a new concept: it\'s the same '
                  'thinking, typed instead of dragged. Frame it as the next level, not as harder. '
                  'The one genuinely new thing is syntax, the punctuation rules, so name that and '
                  'normalize making mistakes with it.'},

        {'kind': 'bullets', 'title': 'Why switch to Python at all?',
         'bullets': [
             'Blockly wasn\'t training wheels: loops, functions and parameters are **real '
             'programming ideas**',
             'You learned them without spending a single minute on typos. That was the point: '
             'get the thinking first',
             'But Blockly can only offer you the blocks somebody built for it',
             'Python is a **general-purpose programming language**: not tied to robots, or to '
             'any one job',
         ],
         'notes': 'Someone asks every year "why did we waste time on blocks, then?", usually a '
                  'student who has programmed a little. The honest answer lands better than a '
                  'defensive one: they learned loops, functions and parameters without losing a '
                  'single class period to missing colons, and those ideas transfer intact, as '
                  'they\'re about to see.'},

        {'kind': 'cards', 'title': 'The same Python, far beyond robots',
         'cards': [
             ('Web', 'Web development', 'The servers behind sites and apps.'),
             ('Data', 'Data science', 'Analyzing and charting real data sets.'),
             ('AI', 'Machine learning', 'Most of the field\'s everyday tools are written in or '
                                        'driven by Python.'),
             ('Scripts', 'Automation', 'Scripts that do a tedious job so a person doesn\'t have to.'),
         ],
         'height': 3.4,
         'notes': 'One of the most widely used languages in the world. And plenty more: scientific '
                  'research, finance, visual effects.'},

        {'kind': 'bullets', 'title': 'The best code is code you don\'t write',
         'bullets': [
             'As programs get bigger, what saves you isn\'t writing faster: it\'s **not having '
             'to write it at all**',
             'Python gives you an enormous body of **libraries and frameworks**: code other '
             'people already wrote, tested, and handed over',
             'Read a sensor, talk to a website, do statistics, draw a graph? Usually a single '
             'import line',
         ],
         'callout': 'Next: `XRPLib`, which makes the robot\'s motors and sensors a few words of '
                    'Python instead of a semester of electronics',
         'tone': 'teal',
         'notes': 'A concrete hook if you want one: Instagram\'s servers run on Django, a Python '
                  'web framework; Spotify leans on Python for the data and recommendation '
                  'pipelines behind its playlists; the first image of a black hole was assembled '
                  'with Python libraries. The point isn\'t the trivia: none of those teams wrote '
                  'their own math, plotting or networking code from scratch.'},

        {'kind': 'check',
         'question': 'What\'s the main advantage of a general-purpose language like Python over '
                     'Blockly?',
         'options': ['Python programs always run faster',
                     'It isn\'t limited to the blocks provided, and opens up libraries others '
                     'wrote and tested',
                     'Python makes it impossible to write a program with mistakes in it',
                     'Blockly cannot do loops or functions'],
         'answer': 1,
         'explanation': 'Blockly gave you the ideas, and it can do loops and functions perfectly '
                        'well. What it can\'t do is go beyond the blocks provided, or reach the '
                        'huge collection of ready-made Python libraries.'},

        {'kind': 'figure', 'title': 'The same program, two ways',
         'figure': [{'name': 'straight_cm30', 'note': 'the block you know'}],
         'caption': 'Here\'s the **Straight** block you\'ve used all module. Next: the Python that '
                    'does the exact same thing.',
         'notes': 'Put a Blockly program and its Python side by side and let students match them '
                  'up. (The lesson page draws the generic Straight block; the slide uses the '
                  '30 cm version so the block and the Python agree.)'},

        {'kind': 'code', 'title': '...and the same thing in Python',
         'code': 'from XRPLib.differential_drive import DifferentialDrive\n'
                 '\n'
                 'drivetrain = DifferentialDrive.get_default_differential_drive()\n'
                 'drivetrain.straight(30)',
         'code_size': 22,
         'callout': 'Three lines. Next slide: what each one does.',
         'tone': 'teal',
         'notes': 'Ask students to guess which line does the driving before you explain.'},

        {'kind': 'steps', 'title': 'Reading it line by line',
         'tag': ' ',
         'steps': [
             '`from XRPLib.differential_drive import DifferentialDrive`\n'
             'Bring in the robot-control library.',
             '`drivetrain = DifferentialDrive.get_default_differential_drive()`\n'
             'Get the robot\'s wheels as an object you can command.',
             '`drivetrain.straight(30)`\n'
             'Drive straight 30 cm. Use a negative number to go backward, just like the block.',
         ],
         'size': 22,
         'notes': 'Only the last line moves the robot. The first two are setup, which the next '
                  'few slides unpack.'},

        {'kind': 'bullets', 'title': 'What\'s a library?',
         'bullets': [
             '`XRPLib` is a **library**: code somebody else already wrote, tested, and left on '
             'the robot for you to use',
             'Turning a wheel at a steady speed means timing electrical pulses and counting '
             'encoder ticks',
             'Reading the reflectance sensor means measuring how much light bounces back and '
             'turning that into a number',
             'That work is genuinely hard, it\'s already done, and it\'s sitting in the library',
         ],
         'notes': 'Lead into the bookshelf picture: one book per piece of hardware.'},

        {'kind': 'figure', 'title': 'A shelf of books',
         'figure': '/img/lesson-08/library-shelf.svg',
         'caption': 'XRPLib is the shelf; each class is a book. An import takes one book down, and '
                    'what\'s written inside it are the commands you can use.',
         'notes': 'One book for the drivetrain, one for the reflectance sensor, one for the '
                  'rangefinder, one for the servo. You don\'t read the whole shelf: you take down '
                  'the one book you need, when you need it.'},

        {'kind': 'code', 'title': 'That\'s what `import` does',
         'lead': 'This line takes the **DifferentialDrive** book off the shelf and opens it on '
                 'your desk:',
         'code': 'from XRPLib.differential_drive import DifferentialDrive',
         'code_size': 24,
         'callout': 'Inside: `straight()`, `turn()`, `set_effort()`. Leave the book on the shelf '
                    'and Python has no idea those words mean anything.',
         'tone': 'teal',
         'notes': 'You import each device as you need it, which is why the import lines at the top '
                  'of a program are a decent table of contents for what the program touches.'},

        {'kind': 'steps', 'title': 'Three steps, and they never change',
         'tag': ' ',
         'lead': 'How you use **any** piece of hardware in XRPLib:',
         'steps': [
             '**Import the class.**  `from XRPLib.differential_drive import DifferentialDrive`\n'
             'Tells Python where the code for that hardware lives. Nothing happens to the robot yet.',
             '**Make an instance.**  `drivetrain = DifferentialDrive.get_default_differential_drive()`\n'
             'An object that stands for the real hardware. The name on the left is yours to pick.',
             '**Use it.**  `drivetrain.straight(30)`\n'
             'Instance name, a dot, then what you want it to do: `instance.method()`',
         ],
         'size': 19,
         'notes': 'The spine of Modules 2 to 5: import the class, make an instance, call methods '
                  'on the instance. Students who learn it as a pattern read the reflectance and '
                  'rangefinder lessons as variations; students who memorise these three lines '
                  'meet each new device as a fresh mystery. That instance.method() shape is most '
                  'of the Python they\'ll write from here on.'},

        {'kind': 'code', 'title': 'Steps 1 and 2 once. Step 3 all day.',
         'code': 'from XRPLib.differential_drive import DifferentialDrive    # 1 - once, at the top\n'
                 'from XRPLib.board import Board                             # 1 - once, at the top\n'
                 '\n'
                 'drivetrain = DifferentialDrive.get_default_differential_drive()   # 2 - once\n'
                 'board = Board.get_default_board()                                 # 2 - once\n'
                 '\n'
                 'board.wait_for_button()                 # 3 - use it\n'
                 'print("Driving forward...")\n'
                 'drivetrain.straight(30)                 # 3 - use it\n'
                 'drivetrain.turn(90)                     # 3 - use it\n'
                 'drivetrain.straight(30)                 # 3 - use it again, and again\n'
                 'print("Done!")',
         'code_size': 18,
         'notes': 'Numbering them 1, 2, 3 makes it look like three lines you write together. A real '
                  'program shows they aren\'t. Note that turn(90) is a positive turn: '
                  'counterclockwise, to the left.'},

        {'kind': 'bullets', 'title': 'Setup, then the program',
         'bullets': [
             '**Steps 1 and 2 are setup**: at the top of the file, they run once, and you never '
             'repeat them',
             'Importing the same class twice or making a second drivetrain gains you nothing',
             '**Step 3 is the actual program**: twenty lines later, inside a function you write '
             'in Lesson 1-11, as many times as your robot has things to do',
         ],
         'callout': 'When you see the three steps stacked together, read them as a **summary of '
                    'the shape**, not a block to copy',
         'tone': 'orange',
         'notes': 'Head this off: because the examples stack the three lines, some students copy '
                  'them as a unit and re-import or re-create the drivetrain further down the file '
                  'or inside a function. Nothing breaks loudly, which is why it survives. Say it '
                  'plainly once, and point at the Activity, where setup and use are twelve lines '
                  'apart.'},

        {'kind': 'code', 'title': 'The device changes; the three steps don\'t',
         'lead': 'The **reflectance sensor** from the next module, and the **rangefinder**, later on:',
         'code': 'from XRPLib.reflectance import Reflectance            # 1 - import the class\n'
                 'reflectance = Reflectance.get_default_reflectance()   # 2 - make an instance\n'
                 'reflectance.get_left()                                # 3 - use it\n'
                 '\n'
                 'from XRPLib.rangefinder import Rangefinder            # 1 - import the class\n'
                 'rangefinder = Rangefinder.get_default_rangefinder()   # 2 - make an instance\n'
                 'rangefinder.distance()                                # 3 - use it',
         'code_size': 18,
         'callout': 'Only the names differ. When a new device shows up, you already know two '
                    'thirds of the code.',
         'tone': 'green',
         'notes': 'These are two separate examples, squashed into three lines each so they can be '
                  'compared. In a real program the first two lines of each go up top with the '
                  'other setup, and the third goes wherever the robot needs that reading, quite '
                  'possibly inside a loop. Board exercise: write the three rows with only the '
                  'device filled in, and have students complete the reflectance row from the '
                  'drivetrain one before they\'ve seen any sensor code. Most can.'},

        {'kind': 'bullets', 'title': 'Comments: notes for the human',
         'bullets': [
             'A `#` tells Python to **ignore the rest of that line**',
             'Everything after it is there for the human reading the code, not for the robot',
             'A comment can sit at the end of a line, or on a line of its own',
             'They cost nothing to run, so use them freely',
         ],
         'callout': 'A line explaining **why** you picked a number is worth far more later than '
                    'one restating what the code plainly does',
         'tone': 'teal',
         'notes': 'Point back at the "# 1 - import the class" notes on the previous slide: those '
                  'are comments.'},

        {'kind': 'bullets', 'title': 'Let the editor do the spelling',
         'bullets': [
             'Class names are long, and Python is fussy about capitals: `Rangefinder`, not '
             '`rangefinder`',
             'Type the first few characters, `Diff`, and the editor offers `DifferentialDrive`. '
             'Press Tab or Enter to accept it',
             'After a dot too: type `drivetrain.` and it lists everything the drivetrain can do',
             'A quick way to discover methods nobody told you about',
         ],
         'callout': 'Suggestion never appears? The name you\'re typing probably isn\'t imported yet',
         'tone': 'orange',
         'notes': 'Note the capital/lowercase convention: Rangefinder is the class, rangefinder is '
                  'their variable. Autocomplete gets the capitals right for them.'},

        {'kind': 'check',
         'question': 'A program starts with "from XRPLib.rangefinder import Rangefinder" and then '
                     'calls rangefinder.distance(). It fails with a NameError. What was skipped?',
         'options': ['Step 2: no instance was made, so the name rangefinder means nothing yet',
                     'Step 1: the import line is wrong',
                     'The program needs to import Rangefinder twice',
                     'Nothing: distance() only works in Blockly'],
         'answer': 0,
         'explanation': 'Importing the class makes Rangefinder available; it does not create '
                        'rangefinder. The middle step, rangefinder = '
                        'Rangefinder.get_default_rangefinder(), gives that name an object.'},

        {'kind': 'check',
         'question': 'Where do the three steps actually go in a real program?',
         'options': ['Steps 1 and 2 near the top, once; step 3 wherever the device is needed, '
                     'as often as you like',
                     'All three must be written together, in that order, every time',
                     'Step 2 has to be repeated before each use of the device',
                     'They can go in any order as long as all three are present'],
         'answer': 0,
         'explanation': 'Setup happens once: one import, one instance. Using the device is the '
                        'actual program: it can be twenty lines later, in a loop or a function, '
                        'as often as you need.'},

        {'kind': 'steps', 'title': 'The five syntax rules: three for today',
         'tag': ' ',
         'lead': 'Blockly never let you make a spelling mistake. Python will.',
         'steps': [
             '**Lowercase**: `print` is not `Print`. Names are case-sensitive',
             '**Parentheses** mark a **function call**: `print` names the function, `print()` '
             'runs it. Inside go the **arguments**: one, several, or none, but the parentheses '
             'go in either way',
             '**Quotes**: text goes in quotes, `print("hello")`',
         ],
         'size': 21,
         'callout': 'The other two are for code that spans several lines. You\'ll meet them in '
                    'Lesson 1-10, when you need them.',
         'tone': 'teal',
         'notes': 'The two held back are colons and indentation: they only make sense once there '
                  'is a block of code to belong to, and the first arrives with Lesson 1-10\'s for '
                  'loop. Don\'t let it read as something skipped: the lesson promises two more by '
                  'name, and Lesson 1-10 opens by collecting on that promise.'},

        {'kind': 'check',
         'question': 'Which line is written correctly?',
         'options': ['`Print("Driving...")`', '`print "Driving..."`', '`print("Driving...")`',
                     '`print(Driving...)`'],
         'answer': 2,
         'explanation': 'Lowercase print, parentheses around the call, and quotes around the text. '
                        'The others break one rule each.'},

        {'kind': 'check',
         'question': 'What do the parentheses in `board.wait_for_button()` do?',
         'options': ['They tell Python to call the function, and anything inside them is an '
                     'argument passed to it',
                     'They are decoration; Python ignores them',
                     'They mean the function returns nothing',
                     'They are only needed when there is something inside them'],
         'answer': 0,
         'explanation': 'Parentheses are what turns a name into a call. wait_for_button needs no '
                        'arguments, so they\'re empty, but leave them off and Python just names '
                        'the function without running it.'},

        {'kind': 'steps', 'title': 'Activity · Write your first Python program',
         'steps': [
             'Same tool, different file: in **XRP Code**, `File → New File`, then choose '
             '**MICROPYTHON** instead of Blockly',
             'Your robot\'s files are down the left, the editor in the middle, and the **shell** '
             'along the bottom: that\'s where `print()` output shows up',
             'Create a file called `lesson_1_8_first_drive.py`: the lesson number, then what the '
             'program does',
             'Type the program in (typing, not pasting: it builds muscle memory), then press **RUN**',
         ],
         'size': 21,
         'notes': 'Let students hit real syntax errors and practice reading the messages: that is '
                  'the skill, and the errors here are the easy kind, one line, one mistake. '
                  'Indentation is the number one stumble overall, but it can\'t happen yet: '
                  'nothing in this lesson is indented.'},

        {'kind': 'code', 'title': 'Your first program',
         'code': 'from XRPLib.differential_drive import DifferentialDrive\n'
                 'from XRPLib.board import Board\n'
                 '\n'
                 'drivetrain = DifferentialDrive.get_default_differential_drive()\n'
                 'board = Board.get_default_board()\n'
                 '\n'
                 'board.wait_for_button()\n'
                 '\n'
                 'print("Driving forward...")\n'
                 'drivetrain.straight(30)\n'
                 '\n'
                 'print("Driving backward...")\n'
                 'drivetrain.straight(-30)\n'
                 '\n'
                 'print("Done!")',
         'code_size': 17,
         'notes': 'Encourage liberal use of print(): a message before and after each action turns '
                  'an invisible program into a visible one. This is the habit that makes the '
                  'Python lessons debuggable.'},

        {'kind': 'bullets', 'title': 'Why `board.wait_for_button()` matters',
         'bullets': [
             'It\'s the **Wait for button press** block you used all through Blockly, in text',
             'Pressing RUN starts the program **immediately**',
             'Without that line the robot drives off the moment you upload it: usually off the desk',
             'Put the robot on the floor, press RUN, **then** press the button on the robot',
         ],
         'callout': 'Watch the shell: your `print()` messages show exactly where the robot is in '
                    'the program',
         'tone': 'teal',
         'notes': 'Demo it once with the robot on the floor so students see the pause.'},

        {'kind': 'frames', 'title': 'What a correct run looks like',
         'figure': '/img/lesson-08/first-drive.svg',
         'crop': (0.0, 0.07, 1.0, 1.0),
         'frames': [(0.2, 'Nothing happens until the button'),
                    (0.4, 'Each print appears just before its move')],
         'callout': 'Then the robot drives 30 cm back to its start mark, and the shell prints '
                    '`Done!`',
         'tone': 'teal',
         'notes': 'The lesson page animates the whole run: the highlighted line is the one '
                  'running. First the program waits at board.wait_for_button(); then the shell '
                  'prints Driving forward..., the robot drives 30 cm, prints Driving backward..., '
                  'drives back, and prints Done!'},

        {'kind': 'check',
         'question': 'Why does `drivetrain.straight(-30)` drive the robot backward?',
         'options': ['Negative numbers reverse the direction, same as a negative cm in the '
                     'Straight block',
                     'It drives forward 30 cm, then stops',
                     'It turns instead of driving', 'It causes an error'],
         'answer': 0,
         'explanation': 'A negative distance means backward, exactly like typing a negative cm '
                        'value into the block.'},

        {'kind': 'code', 'title': 'Activity · Read it, then fix it',
         'lead': 'Spotting mistakes is half of programming. What\'s wrong here?',
         'code': 'drivetrain.straight(30)\n'
                 'Print("Backing up")\n'
                 'drivetrain.straight(-30)',
         'code_size': 28, 'width': 8,
         'notes': 'Give students a moment to find it on their own before the check.'},

        {'kind': 'check',
         'question': 'Find the bug in the code: `drivetrain.straight(30)`, then '
                     '`Print("Backing up")`, then `drivetrain.straight(-30)`',
         'options': ['straight should be capitalized', 'Print should be lowercase: print',
                     'The distances should be positive', 'There is no bug'],
         'answer': 1,
         'explanation': 'Python is case-sensitive. Print with a capital P isn\'t the same as the '
                        'built-in print.'},

        {'kind': 'bullets', 'title': 'Try it: drive an L-shape',
         'tag': 'Activity',
         'bullets': [
             'Rewrite your forward/backward program to drive an **L-shape**',
             '`straight`, `turn(90)`, `straight`',
             'Put a `print()` before each step',
         ],
         'callout': 'Watch the shell: does each message appear just before its move?',
         'tone': 'teal',
         'notes': 'turn(90) is a positive turn, so the robot turns counterclockwise (left). '
                  'Assessment: the program runs, the robot moves as intended, and the print '
                  'messages appear.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('AI', 'Machine learning', 'Most AI research and tools, including large language '
                                        'models, are built in Python.'),
             ('Science', 'Data & discovery', 'Scientists analyze experiments, genomes, and '
                                             'telescopes\' data with Python every day.'),
             ('Robotics', 'Real robots', 'From classroom bots to industrial arms, Python is a '
                                         'standard language for robot control.'),
         ],
         'notes': 'Python is one of the most-used languages in the world, well beyond robots.'},

        {'kind': 'wrapup',
         'questions': [
             'Why learn Python if Blockly works?',
             'Name a job Python does outside robotics.',
             'Name the three syntax rules from this lesson.',
             'What do the parentheses in `print()` tell Python?',
             'What is `print()` good for?',
         ],
         'next': 'Lesson 1-9, variables and expressions',
         'notes': 'Answers: general-purpose rather than limited to the blocks provided, used '
                  'everywhere, and it lets you build on libraries others wrote and tested. Web '
                  'development, data science, machine learning, automation. Lowercase, '
                  'parentheses, quotes (colons and indentation still to come). That the name is a '
                  'function call: run it; anything inside is an argument. Showing messages and '
                  'debugging. Formative: can students translate a block to Python and spot a '
                  'syntax error? Next lesson slows down on drivetrain = ...: what the = does, how '
                  'to name things, how Python works out the right side. Loops follow in Lesson '
                  '1-10.'},
    ],
}
