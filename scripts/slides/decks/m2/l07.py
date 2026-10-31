DECK = {
    'module': 2, 'lesson': 7,
    'doc': 'module-02-line-tracking/lesson-07-sensor-functions',
    'title': 'Finishing the Sensor Toolkit',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Write `is_at_cross()`, completing the five-function sensor toolkit',
             'Explain how the functions share `reflectance` and `THRESHOLD` through **global variables**',
             'Say why one function calls another instead of repeating its logic',
             'Say when a function needs the `global` keyword, and when it doesn\'t',
             'Test the whole toolkit by sliding the robot over the line and reading the printout',
         ],
         'notes': '60 minutes. Four of the five functions already exist, written one at a time in '
                  'Lessons 2-1, 2-3, 2-5 and 2-6. This lesson adds the fifth and mostly names what '
                  'has been going on: two shared globals, and the global keyword for the one case '
                  'where a function assigns. Keep the focus on the sharing.'},

        {'kind': 'bullets', 'title': 'You\'ve already built a toolkit',
         'bullets': [
             '`get_left()` and `get_right()` since Lesson 2-1',
             '`is_either_on_line()` since the bounce',
             'A `get_error()` you\'ve already rewritten once',
             'Each written when a program needed it, and tested before that program ran',
         ],
         'callout': 'Today: add the last function, name how they **share**, and test all five',
         'tone': 'teal',
         'notes': 'Open robot.py on the projector and scroll the LINE SENSOR section. From next '
                  'lesson on the robot drives on this toolkit, so this is the lesson to be sure '
                  'of it.'},

        {'kind': 'code', 'title': 'The goal: code that reads like English',
         'lead': 'Next lesson the robot follows the line **until it reaches a crossing line**. '
                 'With the sensor logic in functions, that loop reads as a sentence:',
         'lead_h': 1.2,
         'code': 'while not is_at_cross():\n'
                 '    correction = get_error() * KP\n'
                 '    drivetrain.arcade(BASE_EFFORT, correction)',
         'code_size': 24,
         'callout': '`is_at_cross()` is far clearer than `left > 0.5 and right > 0.5` in the '
                    'middle of a loop, and `get_error()` says what the subtraction **means**',
         'tone': 'teal',
         'notes': 'Every driving function in Lessons 2-8 and 2-9 is built on these five functions.'},

        {'kind': 'bullets', 'title': 'Shared, not passed: global variables',
         'bullets': [
             'The functions need the same two things: the reflectance sensor, and the threshold',
             'You could have passed both into every function as parameters',
             'Instead they were created **once, at the top of the file**, outside any function',
             [
                 '`reflectance` in the start block',
                 '`THRESHOLD` at the top of the section',
             ],
             'Every function just used them',
         ],
         'callout': 'A variable created outside every function is a **global variable**: every '
                    'function below it can read it without being handed it',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Nothing new: globals since Module 1',
         'bullets': [
             '`drivetrain` is a global that `polygon()` used without a parameter',
             'Lesson 2-1 said so in passing; now it has a name',
             '`THRESHOLD` is in **capitals** by convention',
             'That spelling says: **a setting**, not a value that changes as the program runs',
         ],
         'callout': 'Python doesn\'t enforce the capitals. Readers rely on them.',
         'tone': 'orange'},

        {'kind': 'check',
         'question': 'Why can `get_left()` use `reflectance` when it was never passed in as a '
                     'parameter?',
         'options': ['Python passes the first variable in the file automatically',
                     '`reflectance` is a global variable: created outside every function, so '
                     'every function below it can read it',
                     '`get_left()` creates its own `reflectance` each call',
                     'It cannot; this is a bug'],
         'answer': 1,
         'explanation': 'A name created at the top level of the file is visible inside every '
                        'function. `drivetrain` has worked this way since Module 1; `reflectance` '
                        'and `THRESHOLD` work the same way here.'},

        {'kind': 'code', 'title': 'The last function: `is_at_cross()`',
         'lead': 'Your LINE SENSOR section has four functions. Add the fifth under '
                 '`is_either_on_line()`:',
         'code': 'def is_at_cross():\n'
                 '    # return True when BOTH readings are above THRESHOLD\n'
                 '    pass',
         'code_size': 24,
         'callout': 'Where a second taped line **crosses** the one you\'re following, **both** '
                    'sensors sit on black at once',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'The two `is_` functions are a pair',
         'bullets': [
             '`is_either_on_line()`: **at least one** sensor dark, so `or`',
             '`is_at_cross()`: **both** sensors dark, so `and`',
             'The first ends a **turn** in Lesson 2-9',
             'The second ends a **follow** in Lesson 2-8',
         ],
         'callout': 'With `or`, a cross check would fire every time one sensor touched the line',
         'tone': 'orange',
         'notes': 'Insist on the is_ prefix for functions that return True or False. '
                  'is_at_cross() and is_either_on_line() are used unchanged through the end of '
                  'the course.'},

        {'kind': 'figure', 'title': 'Four positions, two answers',
         'figure': '/img/lesson-m2-07/four-positions.svg',
         'caption': 'Only the cross makes both True. That\'s why `is_at_cross()` needs `and`.',
         'notes': 'Have students predict the two Booleans for each position before you reveal the '
                  'bottom rows.'},

        {'kind': 'figure', 'title': 'The whole toolkit',
         'figure': '/img/lesson-m2-07/sensor-toolkit-layers.svg',
         'caption': 'One place knows how to read the hardware; everything else goes through it.',
         'notes': 'Only get_left() and get_right() touch reflectance. The other three call those '
                  'two. These five names are the vocabulary of the rest of the course, used '
                  'unchanged through Module 5.'},

        {'kind': 'check',
         'question': 'Which condition detects an intersection (both sensors on the line)?',
         'options': ['`left > 0.5 or right > 0.5`', '`left > 0.5 and right > 0.5`',
                     '`left > 0.5`', '`not (left > 0.5)`'],
         'answer': 1,
         'explanation': 'A cross means BOTH sensors are on black at once, so both comparisons must '
                        'be true: that\'s `and`. `or` would fire during normal following too.'},

        {'kind': 'check',
         'question': 'Both sensors read 0.2 with `THRESHOLD = 0.5`. What do `is_at_cross()` and '
                     '`is_either_on_line()` return?',
         'options': ['True and True',
                     'False and False: neither reading is above the threshold, so neither the '
                     '`and` nor the `or` is satisfied',
                     'False and True', 'True and False'],
         'answer': 1,
         'explanation': '`0.2 > 0.5` is False for both sensors. `and` needs both True; `or` needs '
                        'at least one. Both come out False: the robot is off the line entirely.'},

        {'kind': 'check',
         'question': 'Why does `get_error()` call `get_left()` instead of `reflectance.get_left()`?',
         'options': ['`reflectance.get_left()` is slower',
                     'So only one function knows how the hardware is read: if the sensor '
                     'changes, you fix `get_left()` and everything else keeps working',
                     'Functions cannot use global variables twice',
                     'It makes no difference either way'],
         'answer': 1,
         'explanation': 'Functions calling functions keeps each job in one place. `get_error()` '
                        'means left minus right; how a reading is taken is `get_left()`\'s '
                        'business.'},

        {'kind': 'code', 'title': 'When `global` is needed',
         'lead': 'Every function so far **reads** `THRESHOLD`. Reading a global is free. '
                 '**Assigning** to one is different:',
         'code': 'def set_threshold(new_value):\n'
                 '    THRESHOLD = new_value        # looks right; does nothing useful',
         'code_size': 22,
         'callout': 'Call `set_threshold(0.3)`, then print `THRESHOLD`: still `0.5`',
         'tone': 'orange',
         'notes': 'Inside a function, assigning to a name creates a new local variable with that '
                  'name, which vanishes when the function returns. The global was never touched, '
                  'and Python gives no error.'},

        {'kind': 'code', 'title': 'Declare it `global` first',
         'lead': 'Inside a function, assigning creates a **new local variable** that vanishes '
                 'when the function returns. To mean the one at the top of the file:',
         'lead_h': 1.2,
         'code': 'def set_threshold(new_value):\n'
                 '    global THRESHOLD\n'
                 '    THRESHOLD = new_value',
         'code_size': 24,
         'callout': 'Read a global freely; to **assign** to it, declare `global` first',
         'tone': 'green',
         'notes': 'You will need this rarely, since settings in capitals are not supposed to '
                  'change. But the silent failure without it is the kind of bug that costs an '
                  'afternoon. Ask the class why the course avoids needing global at all. Name '
                  'the limit out loud: one THRESHOLD for the whole program means one sensor '
                  'setting. The optional class extension solves that.'},

        {'kind': 'check',
         'question': 'Why does `set_threshold()` need the `global` keyword when `is_at_cross()` '
                     'does not?',
         'options': ['Because `set_threshold` takes a parameter',
                     '`is_at_cross()` only reads `THRESHOLD`; `set_threshold()` assigns to it, and '
                     'without `global` the assignment makes a throwaway local',
                     'Every function that mentions `THRESHOLD` needs `global`',
                     'Because `THRESHOLD` is in capitals'],
         'answer': 1,
         'explanation': 'Reading a global needs nothing. Assigning inside a function creates a '
                        'local unless you declare `global` first, and the real `THRESHOLD` stays '
                        '0.5, with no error to tell you.'},

        {'kind': 'bullets', 'title': 'Before you start: tape the cross',
         'tag': 'Activity',
         'bullets': [
             'Add one short, straight strip of tape **across** your circle\'s line at a single spot',
             'About **10 cm (4 inches)**: long enough that both sensors sit on it at once',
             'Short enough to swing clear when the robot spins in place there (Lesson 2-9)',
             'The robot meets it once per lap',
         ],
         'callout': 'The cross stays on the floor for the rest of the module',
         'tone': 'teal',
         'notes': 'The cross is introduced now, with the function that detects it, so the '
                  'function can be tested on real tape the moment it is written.'},

        {'kind': 'frames', 'title': 'Testing by hand · on the line, off to one side',
         'tag': 'Activity',
         'figure': '/img/lesson-m2-07/toolkit-by-hand.svg',
         'crop': (0.025, 0.09, 1.0, 0.98),
         'frames': [(0.08, '**On the line**: each sensor on an edge of the tape'),
                    (0.28, '**Off to one side**: only the left sensor on the tape')],
         'callout': 'Motors off: slide the robot by hand and read what `test_sensors()` prints',
         'tone': 'teal',
         'notes': 'The figure on the lesson page is one animation of steps 1 and 2; this slide '
                  'and the next show its four stops. Ask for a prediction of both Booleans '
                  'before each one.'},

        {'kind': 'frames', 'title': 'Testing by hand · completely off, on the cross',
         'tag': 'Activity',
         'figure': '/img/lesson-m2-07/toolkit-by-hand.svg',
         'crop': (0.025, 0.09, 1.0, 0.98),
         'frames': [(0.47, '**Completely off**: both sensors on white'),
                    (0.82, '**On the cross**: both sensors on the strip')],
         'callout': 'Only the cross puts both sensors on tape at once',
         'tone': 'teal',
         'notes': 'Sliding along the line toward the cross, Cross stays False until both '
                  'sensors are on the strip.'},

        {'kind': 'steps', 'title': 'Step 1 · is_at_cross()',
         'steps': [
             'Write the body of `is_at_cross()`',
             'Add `" Cross:", is_at_cross()` to the print in `test_sensors()`, and set the run '
             'line to `test_sensors()`',
             'Slide the robot along the circle: `False` all the way around, `True` only when '
             'both sensors sit on the crossing strip',
         ],
         'callout': '`True` on the plain circle? The threshold is too low. Never `True` on the '
                    'cross? Too high.',
         'tone': 'orange'},

        {'kind': 'table', 'title': 'Step 2 · The whole toolkit',
         'tag': 'Activity',
         'lead': '`test_sensors()` should now print all five: left, right, error, on-line, cross. '
                 'Check four positions and write down what you see.',
         'headers': ['Position', 'error', '`is_at_cross()`', '`is_either_on_line()`'],
         'widths': [3.0, 2.4, 2.6, 3.6],
         'rows': [
             ['Centered on the line', '', '`False`', '`True`'],
             ['Off to one side', 'positive or negative', '`False`', '`True`'],
             ['Completely off the line', '', '`False`', '`False`'],
             ['On the cross', '', '`True`', '`True`'],
         ],
         'callout': 'Predict the two Booleans **before** each slide of the robot',
         'tone': 'teal',
         'notes': 'Have students predict both Booleans before each slide of the robot. The '
                  'figure on the previous slide shows the same four positions with sample '
                  'numbers.'},

        {'kind': 'steps', 'title': 'Step 3 · set_threshold()',
         'steps': [
             'Add `set_threshold()` to the section **without** `global`, and call '
             '`set_threshold(0.9)` as the first line of `test_sensors()`',
             'Slide over the cross: `is_at_cross()` still fires, because the real `THRESHOLD` '
             'never changed',
             'Add the `global` line and run again: now nothing reads as tape',
             'Take the call out again when you\'re done; the function can stay',
         ],
         'notes': 'Do this one live if you can: the silent no-op is more convincing than any '
                  'rule.'},

        {'kind': 'steps', 'title': 'Step 4 · Nothing broke',
         'steps': [
             'Set the run line to `test_follow()` and run it once',
             'The toolkit changed under it this lesson, and the follower should not care',
         ],
         'callout': 'From here on this section is finished: the next lessons **use** it and '
                    'don\'t touch it',
         'tone': 'teal'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Hardware', 'Device drivers', 'A sensor library is a handful of functions around '
                                            'one shared device handle: exactly this shape.'),
             ('Libraries', 'What you import', 'XRPLib\'s own reflectance module is '
                                                    'functions and settings bundled the same way.'),
             ('Teams', 'One place to fix', 'When the hardware changes, one function changes. '
                                           'Everyone who called it is unaffected.'),
         ]},

        {'kind': 'wrapup',
         'questions': [
             'Where do `reflectance` and `THRESHOLD` live, and why can every function see them?',
             'Why does `get_error()` call `get_left()` rather than the hardware?',
             'When do you need `global`?',
         ],
         'next': 'the robot drives on these five, until `is_at_cross()` says stop',
         'notes': 'Answers: at the top of the file, outside any function, so they are globals. '
                  'One place knows how to read the sensor. Only to assign to a global inside a '
                  'function. Formative: write is_at_cross() from its description; explain why '
                  'get_error() needs no parameters; predict the two Booleans for a robot '
                  'position. Exit ticket: "Why does set_threshold() need global and '
                  'is_at_cross() not?" Lesson 2-9 then adds the functions that park on the '
                  'cross and turn until a sensor finds the next line.'},

        {'kind': 'figure', 'title': 'Optional extension · The LineSensor class',
         'tag': 'Optional',
         'figure': '/img/lesson-m2-07/class-and-objects.svg',
         'caption': 'A **class** is a blueprint grouping **data** and **actions**. Each object '
                    'built from it, an **instance**, can be a little different.',
         'notes': 'Only for students who finish early. The five functions work, but their parts '
                  'are spread out: two globals at the top and five functions below that depend '
                  'on both. A class keeps the data and the functions that use it together. The '
                  'class is just a definition: you cannot call get_error() on the LineSensor '
                  'class itself. LineSensor() builds one object, an instance; the parentheses '
                  'build it. Each can differ depending on what you pass the constructor. '
                  'Students have used classes all along: DifferentialDrive, Reflectance, Board.'},

        {'kind': 'code', 'title': 'Optional extension · `__init__` and `self`',
         'tag': 'Optional',
         'lead': '`__init__` is the **constructor**: Python runs it when you write `LineSensor()`. '
                 '`self` is the object itself.',
         'lead_h': 1.2,
         'code': 'class LineSensor:\n'
                 '    def __init__(self):\n'
                 '        self.reflectance = Reflectance.get_default_reflectance()\n'
                 '        self.threshold = 0.5\n'
                 '\n'
                 'sensor = LineSensor()     # __init__ runs now\n'
                 'print(sensor.threshold)   # 0.5',
         'code_size': 18,
         'callout': 'Each function becomes a **method** with `self` first, the globals become '
                    '`self.` data, and calls go through the object: `sensor.get_error()`',
         'tone': 'teal',
         'callout_size': 20,
         'notes': 'The four changes from function to method: functions move inside the class with '
                  'self as the first parameter; reflectance and THRESHOLD become self.reflectance '
                  'and self.threshold, set in __init__; inside methods, those values and sibling '
                  'calls get self. in front; outside calls go through the object, and Python '
                  'supplies self. The payoff: copy the class and nothing is forgotten, two objects '
                  'can have two thresholds, and no global keyword. Students paste the lesson\'s '
                  'class skeleton in place of the LINE SENSOR functions, translate the five '
                  'bodies, and add sensor. to calls in their tests. Classic slips: missing self '
                  'in a parameter list, missing self. in front of an attribute or method, a '
                  'method indented out of the class. The file is '
                  'lesson-07-linesensor-class-addon.py in the Module 2 solutions.'},
    ],
}
