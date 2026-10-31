DECK = {
    'module': 2, 'lesson': 1,
    'doc': 'module-02-line-tracking/lesson-01-reflectance-sensor',
    'title': 'The Reflectance Sensor',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Explain how a reflectance sensor tells light surfaces from dark ones',
             'Read the left and right sensors with `get_left()` and `get_right()`',
             'Start `robot.py`, your one file for the course, and write its first two functions',
             'Interpret sensor values (roughly `0.0` on white to `1.0` on black)',
             'Pick a **threshold** and record calibration data for your own robot and tape',
         ],
         'notes': '50 to 60 minutes. First look at sensing, and the day robot.py is born. The '
                  'lesson has six objectives; the slide folds "pick a threshold" and "record '
                  'calibration data" into one line.'},

        {'kind': 'bullets', 'title': 'From doing to sensing',
         'bullets': [
             'In Module 1 the robot only did what you told it, step by step',
             'Now it gets to **sense** the world',
             'Its "eyes": two **reflectance sensors** that tell a white surface from a black line',
             'Today you record the readings you will rely on for the rest of the module',
         ],
         'callout': 'Question for the room: you can see the line. How could a robot tell?',
         'tone': 'teal',
         'notes': 'Quick hook. Take a few answers before moving on; most students guess a camera '
                  'or a color sensor, which sets up the next slide nicely.'},

        {'kind': 'figure', 'title': 'How the robot "sees" a line',
         'figure': '/img/lesson-m2-01/reflectance-sensor.svg',
         'caption': 'The **LED** shines, the **phototransistor** listens. White bounces most of '
                    'the light back: a low reading. Black tape soaks it up: a high reading.',
         'notes': 'Flip a robot over and show the two sensors underneath. Each is a pair of '
                  'parts side by side: an LED shining down, and a phototransistor right next to '
                  'it measuring how much light comes back. The real sensor uses infrared, which '
                  'is invisible; the figure draws it in red.'},

        {'kind': 'bullets', 'title': 'It measures light, not color',
         'bullets': [
             'The sensor only knows **how much light came back**',
             '**White surface**: most light bounces back, a **low** value (around `0.1–0.3`)',
             '**Black line**: light is absorbed, a **high** value (around `0.7–0.9`)',
             'Anything dark reads like a line, anything light reads like the floor',
             'A **left** and a **right** sensor, each with its own reading',
         ],
         'callout': 'Two readings let the robot tell **which side** of a line it is on',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'Your sensor reads 0.8. What is it most likely over?',
         'options': ['A white surface', 'A black line', 'The edge of the line',
                     'Nothing: that value is impossible'],
         'answer': 1,
         'explanation': 'High values (near 1.0) mean little light came back: a dark surface '
                        'absorbs it. White gives low values near 0.0.'},

        {'kind': 'code', 'title': 'Read the sensors in Python',
         'lead': 'Reading a sensor is just importing its class and calling a method:',
         'code': 'from XRPLib.reflectance import Reflectance\n'
                 'from XRPLib.board import Board\n'
                 '\n'
                 'reflectance = Reflectance.get_default_reflectance()\n'
                 'board = Board.get_default_board()\n'
                 '\n'
                 'board.wait_for_button()\n'
                 '\n'
                 'left = reflectance.get_left()\n'
                 'right = reflectance.get_right()\n'
                 'print("Left sensor:", left)\n'
                 'print("Right sensor:", right)',
         'code_size': 18,
         'notes': 'Have students run this as a scratch program before robot.py exists. They get '
                  'two numbers, then the program ends. Let them notice that sliding the robot '
                  'afterwards changes nothing: that frustration is the point of the next slide.'},

        {'kind': 'bullets', 'title': 'A snapshot, not a live feed',
         'bullets': [
             'Run it: you get two numbers, then the program ends',
             '`get_left()` and `get_right()` run **once**, the instant you press the button',
             'Python reaches the bottom of the file and the program is over',
             'Sliding the robot across the tape afterwards changes nothing on screen',
         ],
         'callout': 'To watch the readings **change**, the reading has to happen over and over: '
                    'it goes in a **loop**',
         'tone': 'orange'},

        {'kind': 'bullets', 'title': 'Pausing a program: `time.sleep()`',
         'bullets': [
             'A loop with nothing slowing it down runs **fast**: fifty readings print before '
             'you could move the robot',
             'Python comes with a built-in module called `time`. It isn\'t part of XRPLib; it '
             'ships with Python itself (and MicroPython on the XRP)',
             'Bring it in with `import time` at the top of the file',
             '`time.sleep()` means "the `sleep` function that lives in the `time` module", the '
             'same way `reflectance.get_left()` belongs to the sensor',
         ],
         'notes': 'The dot notation is the new idea here: module dot function, just like object '
                  'dot method. MicroPython is the version of Python running on the XRP.'},

        {'kind': 'code', 'title': '`time.sleep()` takes seconds',
         'lead': 'One number: **how many seconds to pause**. Whole numbers and decimals both work.',
         'code': 'import time\n'
                 '\n'
                 'time.sleep(1)      # wait one second\n'
                 'time.sleep(0.5)    # wait half a second\n'
                 'time.sleep(0.1)    # wait a tenth of a second',
         'code_size': 24,
         'callout': 'The program stops at that line, then carries on. Anything already in motion '
                    'keeps going: motors that were running are still running.',
         'tone': 'teal',
         'notes': 'The lesson lists the three sleeps as examples rather than one program. The '
                  'point about motors matters next lesson: sleeping does not stop the robot.'},

        {'kind': 'bullets', 'title': 'One file, for the rest of the course',
         'bullets': [
             'Until now, every lesson started a new program',
             'From here on you have **one file**, `robot.py`, and each lesson adds to it',
             'Sensor functions this module, then driving, grid driving in Module 3, and on to the end',
             'Lost the file or joined partway? The **robot.py templates** page has it as it '
             'stands after every lesson',
         ],
         'callout': 'The loop you are about to write is the first piece of code you **keep**',
         'tone': 'teal'},

        {'kind': 'code', 'title': 'Create `robot.py` with this start',
         'code': 'from XRPLib.reflectance import Reflectance\n'
                 'from XRPLib.differential_drive import DifferentialDrive\n'
                 'from XRPLib.board import Board\n'
                 'import time\n'
                 '\n'
                 'reflectance = Reflectance.get_default_reflectance()\n'
                 'drivetrain = DifferentialDrive.get_default_differential_drive()\n'
                 'board = Board.get_default_board()\n'
                 '\n'
                 '\n'
                 '# ===== RUN =====\n'
                 'board.wait_for_button()\n'
                 '# call ONE test function here',
         'code_size': 18,
         'notes': 'Everyone creates robot.py now and pastes this in. The templates page on the '
                  'site has the file as it stands after every lesson, skeletons pasted and '
                  'nothing written, for anyone who loses it or joins late.'},

        {'kind': 'bullets', 'title': 'Two rules that keep it working all year',
         'bullets': [
             '**New code goes above** `RUN`**, never below it.** Python runs top to bottom, so '
             'everything the run block calls has to be defined above it',
             '**One test at a time.** The one line under `RUN` calls the test you are working '
             'on: change the call, don\'t stack them',
             'Each lesson gives a **skeleton** to paste: a banner comment, what the section does, '
             'its settings, function outlines and a **test function**',
         ],
         'notes': 'Make the two file rules a ritual today: new code above RUN, one test call. '
                  'They are what keeps the Module 5 file readable.'},

        {'kind': 'figure', 'title': 'One file, one section per job',
         'figure': './decks/m2/fig/robot-py-one-file.svg',
         'caption': 'Each module adds its sections above `RUN`. In every section the functions '
                    'come first, then the tests. Today you start LINE SENSOR with three of them.',
         'notes': 'Point at the three marked "today": get_left, get_right and test_sensors. The '
                  'greyed-out ones arrive later in the module. The figure is a copy of the lesson\'s '
                  'robot-py-one-file.svg with its footer line re-anchored so the slide renderer '
                  'draws it cleanly.'},

        {'kind': 'code', 'title': 'Paste above `RUN`: the LINE SENSOR section',
         'code': '# ===== LINE SENSOR =====\n'
                 '# Reads the two reflectance sensors and answers questions\n'
                 '# about them. Starts here with the two raw readings; over this\n'
                 '# module it grows to answer "how far off the line am I?" and\n'
                 '# "am I on a line? on a cross?" Nothing in here drives.\n'
                 '# Everything that drives asks these functions instead of the\n'
                 '# hardware.\n'
                 '\n'
                 'def get_left():\n'
                 '    # return the left reflectance reading\n'
                 '    pass\n'
                 '\n'
                 'def get_right():\n'
                 '    # return the right reflectance reading\n'
                 '    pass',
         'code_size': 17,
         'notes': 'This and the next slide are one skeleton on the lesson page, pasted in one go. '
                  'It is split here so it stays readable from the back of the room.'},

        {'kind': 'code', 'title': '... and its test, still in the same paste',
         'lead': 'The test is already written. It calls your two functions.',
         'code': 'def test_sensors():\n'
                 '    # prints both readings 50 times, a tenth of a second apart\n'
                 '    for i in range(50):\n'
                 '        print("Left:", get_left(), "  Right:", get_right())\n'
                 '        time.sleep(0.1)',
         'code_size': 20,
         'callout': '`pass` means "nothing here yet": it holds the place of the body so the file '
                    'runs. Delete it when the real line goes in.',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Your first two functions',
         'bullets': [
             '`get_left()` and `get_right()` are **one line each**: they `return` the reading '
             'from `reflectance`',
             'You wrote functions with `return` in Lesson 1-11',
             'New: they use `reflectance` without being handed it',
             ['It was created at the top of the file, outside any function, so every function '
              'below can see it',
              'The same way `polygon()` used `drivetrain` in Module 1'],
         ],
         'notes': 'Do not write the two bodies on the board; students write them. The lesson '
                  'page has a reveal to check against after they run test_sensors().'},

        {'kind': 'bullets', 'title': 'Where the returned value goes',
         'bullets': [
             'A function call is a **question**, and `return` is its **answer**',
             'At the `print` line in `test_sensors()`, Python stops at `get_left()` and runs your function',
             'The value after its `return` **takes the place of the call**',
             'By the time `print` runs, it is as if you had typed the number itself, say `0.23`',
         ],
         'callout': 'You ask `get_left()`, you get a number back to print, compare or do '
                    'arithmetic with',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Two things to watch for',
         'bullets': [
             '**Two things with the same name.** Inside yours, `reflectance.get_left()` is the '
             'sensor\'s own method, not your function calling itself',
             ['The `reflectance.` in front makes the difference. Yours is a plain function that '
              'asks the sensor and passes its answer on'],
             '**If it prints** `None`**, the** `return` **is missing**',
             ['A function that ends without a `return` hands back `None`, Python\'s word for '
              '"nothing"',
              'The sensor is fine; the number just never left the function'],
         ]},

        {'kind': 'check',
         'question': '`test_sensors()` prints `Left: None  Right: None` every time, even while you '
                     'slide the robot across the tape. What is the most likely cause?',
         'options': ['The reflectance sensor is unplugged',
                     '`get_left()` and `get_right()` read the sensor but never return the reading',
                     'The robot is not over the tape',
                     '`print()` cannot show sensor readings'],
         'answer': 1,
         'explanation': 'A function that ends without a return statement gives back None. The '
                        'sensor was read inside the function, but the value never came out of '
                        'it. Put return in front of the read.'},

        {'kind': 'bullets', 'title': 'Why wrap one line in a function?',
         'bullets': [
             'From now on **every** program asks for a sensor reading by **this** name',
             'Only this one place knows how the hardware is read',
             'In six lessons these two will be the bottom of a **toolkit** of functions, and '
             'they will not have changed',
         ],
         'callout': 'Read it once → **keep reading**: the idea behind next lesson\'s `while` loop',
         'tone': 'teal',
         'notes': 'The two wrappers are trivial on purpose. Students call get_left() from here to '
                  'the end of the course, and by the time the sensor toolkit is finished in '
                  'Lesson 2-7 these two have been in use for six lessons.'},

        {'kind': 'steps', 'title': 'Write them and run `test_sensors()`',
         'tag': 'Try it',
         'steps': [
             'Write the two bodies in place of `pass`',
             'Set the run line to `test_sensors()` and run',
             'You have about **five seconds**: slide the robot across the tape and watch the '
             'numbers follow it',
         ],
         'callout': 'Seeing `None`? Check the `return`.',
         'tone': 'orange',
         'notes': 'Same two readings as the first program; they just happen fifty times now, a '
                  'tenth of a second apart. Setup that makes or breaks the readings: tape '
                  'pressed flat with no bubbles, sensors a few millimeters off the surface, no '
                  'direct sunlight or bright overhead lights. Emphasize print() as the '
                  'number-one debugging tool all module.'},

        {'kind': 'figure', 'title': 'What you should see',
         'figure': '/img/lesson-m2-01/slide-across-tape.svg',
         'frame': 0.36,
         'caption': 'About `0.2` on white, about `0.8` on the tape. The **left** sensor climbs first, '
                    'then the **right** one as the left leaves.',
         'notes': 'The figure on the lesson page is an animation of the robot slid by hand across '
                  'the tape and back while the shell scrolls; this is the moment just after the '
                  'first crossing, with the whole sweep in the shell (newest line at the bottom). '
                  'With the tape between the two sensors, both read about 0.5.'},

        {'kind': 'steps', 'title': 'Activity · Calibrate and pick a threshold',
         'lead': 'Surfaces and tape differ, so measure your own. Run `test_sensors()` and record:',
         'steps': [
             'Both sensors on **white**',
             'Both sensors on the **black line**',
             'One sensor on the **edge**',
         ],
         'callout': 'threshold = (highest white value + lowest black value) ÷ 2',
         'tone': 'teal',
         'notes': 'Have students save their calibration data: they reuse it in Lessons 2-2 '
                  'through 2-8. 0.5 is a fine starting guess, but a glossy surface, a faded '
                  'line or bright lighting can push the real edge value well off it. Students '
                  'who calibrate get line following that works in 2-5 and 2-6; students who '
                  'guess spend those lessons fighting a bad threshold. Real robots calibrate on '
                  'startup.'},

        {'kind': 'bullets', 'title': 'The threshold',
         'bullets': [
             'Halfway between your **highest white** reading and your **lowest black** reading',
             'Your programs use it to decide "on the line" vs. "off"',
             'Above it: the line. Below it: white',
             '0.5 is a fine first guess, but your surface, tape and lighting can move it',
         ],
         'callout': 'Calibrate instead of trusting a textbook number. Write your values down!',
         'tone': 'orange'},

        {'kind': 'check',
         'question': 'Your "off line" (white) values average 0.2 and your "on line" (black) '
                     'values average 0.8. What threshold should you choose?',
         'options': ['0.2', '0.5', '0.8', '1.0'],
         'answer': 1,
         'explanation': 'Halfway between 0.2 and 0.8 is 0.5. A reading above it means the line; '
                        'below it means white.'},

        {'kind': 'check',
         'question': 'Why does the XRP have two reflectance sensors instead of one?',
         'options': ['As a spare in case one breaks',
                     'So it can tell which side of the line it is on',
                     'To read the line twice as fast',
                     'One reads white, the other reads black'],
         'answer': 1,
         'explanation': 'Two independent readings let the robot tell whether it is drifting left '
                        'or right of the line: essential for following it later.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Retail', 'Barcode scanners', 'Scanners read the pattern of light and dark bars '
                                            'exactly the way your sensor reads tape.'),
             ('Warehouses', 'Line-following AGVs', 'Automated guided vehicles follow lines taped '
                                                   'or painted on warehouse floors.'),
             ('Phones', 'Ambient light', 'Your phone\'s ambient light sensor dims its screen '
                                         'using the same idea: measuring reflected or available '
                                         'light.'),
         ]},

        {'kind': 'wrapup',
         'questions': [
             'Does a higher reading mean lighter or darker?',
             'What is a threshold, and how do you pick one?',
             'Why two sensors?',
         ],
         'next': 'a `while` loop drives the robot until it finds the line',
         'notes': 'Answers: darker, less light bounced back. The cutoff between line and white, '
                  'halfway between your calibrated values. To tell which side of the line the '
                  'robot is on. Formative: can students read and interpret values and explain '
                  'how the sensor works? Exit ticket: white average 0.2, black average 0.8, '
                  'choose a threshold (0.5). Next lesson THRESHOLD goes into the LINE SENSOR '
                  'section.'},
    ],
}
