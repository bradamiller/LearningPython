DECK = {
    'module': 1, 'lesson': 1,
    'doc': 'module-01-driving/lesson-01-meet-the-xrp',
    'title': 'Meet the XRP',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Identify the key hardware parts of the XRP robot and say what each one does',
             'Find your way around the XRP Code (Blockly) programming environment',
             'Write, upload, and run a block program that drives the robot forward and backward',
             'Debug the most common first-day problems',
         ],
         'notes': '50 to 60 minutes, Blockly, no experience needed. Students meet the robot, '
                  'learn what each part does, and get their first program running on real '
                  'hardware.'},

        {'kind': 'bullets', 'title': 'Today: your first program on a real robot',
         'bullets': [
             'Meet your robot and learn what each part does',
             'Write your very first program to make it drive',
             'By the end, you\'ll have code running on real hardware',
             'No experience required',
         ],
         'callout': 'What makes a robot move? How does it know what to do?',
         'tone': 'teal',
         'notes': 'Opening hook, 5 to 10 minutes. The lesson\'s hook clip of an XRP driving '
                  'around is still to come, so demo a live robot instead. Ask the two questions '
                  'in the callout and let students guess before you explain: it surfaces their '
                  'mental models. Then set the goal: learn the hardware and write a first '
                  'program to make it move.'},

        {'kind': 'figure', 'title': 'The parts of the robot',
         'figure': '/img/lesson-01/xrp-parts.png',
         'caption': 'Everything in the XRP kit. Find each labeled part in front of you as it '
                    'comes up.',
         'notes': 'Hardware tour, 15 to 20 minutes. Hold up a real robot and point to each part '
                  'as you go. Every part has one job, and knowing them makes debugging much '
                  'easier later.'},

        {'kind': 'bullets', 'title': 'Every part has one job',
         'bullets': [
             '**Wheels & motors:** two motors, one per side, each spinning one wheel. The sides '
             'move independently, so the robot can steer',
             '**Controller board:** the robot\'s "brain." It receives your program over USB and '
             'tells the motors what to do',
             '**Battery:** powers everything. A low battery makes the robot sluggish',
             '**Sensors:** the **Reflectance** sensor sees light vs. dark; the **Rangefinder** '
             'measures distance. You\'ll use these in later modules',
             '**Caster wheel:** the little rear wheel that keeps the robot balanced',
         ],
         'size': 24,
         'notes': 'Quick checks while you tour: point out the left and right motors and ask which '
                  'one spins to turn the robot left. Show where the USB plugs in: that is how '
                  'programs get onto the robot. Only name the sensors for now; they come into '
                  'play in Modules 2 to 5.'},

        {'kind': 'check',
         'question': 'Why does the XRP have two motors instead of just one?',
         'options': ['So it can carry heavier loads',
                     'So each side can move at a different speed, which lets the robot steer',
                     'So there is a spare motor in case one fails',
                     'One motor drives, the other only brakes'],
         'answer': 1,
         'explanation': 'Two independently driven wheels are what let a differential-drive robot '
                        'turn: speed up one side to curve toward the other.'},

        {'kind': 'check',
         'question': 'Which part is the "brain" that runs your program and tells the motors what '
                     'to do?',
         'options': ['The battery', 'The reflectance sensor', 'The controller board',
                     'The caster wheel'],
         'answer': 2,
         'explanation': 'The controller board receives your uploaded program and drives '
                        'everything else.'},

        {'kind': 'steps', 'title': 'How the robot gets instructions',
         'tag': 'Always the same',
         'lead': 'A robot only does what you tell it. The workflow is always the same:',
         'steps': [
             '**Write** a program (we\'ll use Blockly)',
             '**Connect** your computer to the robot, by USB cable or over Bluetooth',
             '**Upload** the program to the robot',
             'The robot **runs** the program, each command in order',
         ],
         'callout': 'Writing isn\'t enough: it has to be uploaded. In XRP Code, the green **RUN** '
                    'button uploads the program **and** starts it.',
         'tone': 'teal'},

        {'kind': 'bullets', 'title': 'Two ways to connect',
         'bullets': [
             '**USB cable:** how you connect today',
             ['Every robot needs it the **first** time: XRP Code uses it to install and update '
              'the software that lives on the robot'],
             '**Bluetooth:** once a robot has been set up over USB',
             ['Unplug, turn the robot on, click **CONNECT**, choose **Bluetooth**, pick your '
              'robot from the list',
              'Works exactly like USB, but you\'re not tethered to the table'],
         ],
         'callout': 'Every XRP has its own **ID**, shown under the RUN button. Write yours on the '
                    'robot, and don\'t pair with somebody else\'s.',
         'tone': 'orange',
         'notes': 'Bluetooth in a classroom: do the USB pass first, let XRP Code finish its '
                  'update, and label every robot with its ID, or the pairing list is chaos. Low '
                  'batteries kill Bluetooth before anything else. A running program can block '
                  'the connection: press reset so it restarts without running. Chrome or Edge '
                  'only. On Windows, give it up to about 20 seconds after a dropped connection. '
                  'Keep known-good USB cables at the demo station as the fallback.'},

        {'kind': 'check',
         'question': 'Your robot is brand new. Why can\'t you just connect to it over Bluetooth '
                     'right away?',
         'options': ['Bluetooth only works with Python, not Blockly',
                     'It needs one USB connection first, so XRP Code can set up the software on '
                     'the robot',
                     'Bluetooth is slower, so uploads would fail',
                     'You can: Bluetooth always works out of the box'],
         'answer': 1,
         'explanation': 'The first USB connection is what lets XRP Code install and update the '
                        'robot\'s MicroPython software. After that, the same robot can connect '
                        'wirelessly.'},

        {'kind': 'bullets', 'title': 'Your first program in XRP Code',
         'bullets': [
             'XRP Code runs in a web browser: nothing to install, nothing to log into',
             'Open `xrpcode.wpi.edu/staging` and build programs by dragging blocks',
             '**Use Google Chrome or Microsoft Edge.** Talking to the robot needs serial and '
             'Bluetooth features only those browsers have',
             'Safari and Firefox let you build a program, then your robot never appears in the '
             'CONNECT list',
         ],
         'size': 24,
         'callout': 'Robot not in the list? Switch browsers before you troubleshoot anything else',
         'tone': 'orange',
         'notes': 'The XRP User Guide has a whole chapter on XRP Code: a tour of the three '
                  'panels, connecting over USB step by step, and troubleshooting for a robot '
                  'that won\'t show up. Have students keep it open in a tab. The lesson\'s '
                  'screen recording of creating a project and the three key blocks is still to '
                  'come; do a live tour on the projector instead.'},

        {'kind': 'check',
         'question': 'A classmate built a program in XRP Code on Safari, but when they click '
                     'CONNECT their robot never appears in the list. What is the most likely '
                     'reason?',
         'options': ['The robot is broken',
                     'Safari cannot connect to the robot: XRP Code needs Chrome or Edge for that',
                     'The program has too many blocks',
                     'They need to create an account first'],
         'answer': 1,
         'explanation': 'Building a program works in any browser; connecting to the robot does '
                        'not. The serial and Bluetooth features XRP Code uses exist only in '
                        'Chrome and Edge.'},

        {'kind': 'bullets', 'title': 'Block 1: Wait for button press',
         'bullets': [
             'Goes at the **very top** of the program',
             'A program starts running the moment you click **RUN**',
             'This block makes the robot sit still until you press **its** button',
             'So it doesn\'t drive off the table while you\'re still holding it',
         ],
         'split': 0.52,
         'figure': [{'name': 'wait_for_button_press'}],
         'notes': 'A few blocks do everything students need today. Have them drag each one out '
                  'of the block palette as you introduce it.'},

        {'kind': 'bullets', 'title': 'Block 2: Straight',
         'bullets': [
             'Drives in a straight line',
             '**cm** is how far to go',
             ['A **negative** number drives **backward**'],
             '**Effort** is how hard the motors push, from `0` to `1`',
             ['`0.5` is a good starting speed'],
         ],
         'split': 0.45,
         'figure': [{'name': 'straight'}]},

        {'kind': 'bullets', 'title': 'Block 3: Turn',
         'bullets': [
             'Turns the robot in place',
             '**Deg** is the angle: `90` is a quarter turn',
             '**Effort** works the same way as in Straight',
         ],
         'split': 0.45,
         'figure': [{'name': 'turn'}],
         'callout': 'No block needed to stop at the end: when the program finishes, the robot '
                    'stops the motors for you',
         'tone': 'teal'},

        {'kind': 'figure', 'title': 'The program we\'ll build together',
         'caption': 'Wait for the button, drive out 20 cm, then back 20 cm (a **negative** cm '
                    'reverses). **Predict:** what will the robot do? Will it end up where it '
                    'started?',
         'figure': [
             {'name': 'wait_for_button_press'},
             {'name': 'straight', 'note': 'forward — cm: 20, Effort: 0.5'},
             {'name': 'straight', 'note': 'back — change cm to -20'},
         ],
         'notes': 'This is the worked example on the lesson page. Take a few predictions before '
                  'anyone runs it.'},

        {'kind': 'check',
         'question': 'You place two Straight blocks one above the other. When you run the '
                     'program, what happens?',
         'options': ['Both blocks run at the same time',
                     'The blocks run in order: the first finishes, then the second starts',
                     'Only the top block runs',
                     'The robot picks one block at random'],
         'answer': 1,
         'explanation': 'Blocks execute in sequence, top to bottom: one command finishes before '
                        'the next begins.'},

        {'kind': 'bullets', 'title': 'Put the robot down before you switch it on',
         'bullets': [
             'At power-on, or after **reset**, the XRP spends a few seconds **calibrating its '
             'IMU**: the sensor that measures how far it has turned',
             'That calibration assumes the robot is **perfectly still**, and it can\'t tell if '
             'it isn\'t',
             'Held in your hand while it starts up, it calibrates from a moving robot',
             'No error message: it just turns the **wrong amount**, differently each time',
         ],
         'size': 24,
         'callout': 'Give the robot a few seconds of stillness',
         'tone': 'orange'},

        {'kind': 'steps', 'title': 'Every run, in this order',
         'tag': 'The habit',
         'steps': [
             '**Put the robot down** on the floor or table, where it will actually drive',
             '**Power it on**, or press **reset** if it\'s already on',
             '**Wait a few seconds**, hands off, while it calibrates',
             '**Then press the User button** to release your **Wait for button press** block',
         ],
         'callout': 'That gap between "calibrated" and "driving" is why the Wait for button press '
                    'block is so useful',
         'tone': 'teal',
         'notes': 'Establish this habit now, before turns matter. A robot held in the air '
                  'calibrates wrong, which shows up later as turns that are off by a different '
                  'amount each run: a bug students will blame on their code. When a turn '
                  'misbehaves in any lesson, "put it down and press reset" is the first thing to '
                  'try.'},

        {'kind': 'check',
         'question': 'Your program tells the robot to turn 90°, but every run it turns a '
                     'different, unpredictable amount. What is the most likely cause?',
         'options': ['The robot was moving or held when it powered on, so its IMU calibration '
                     'is bad',
                     'The Turn block only works in Python programs',
                     'The battery is fully charged',
                     'A program can only contain one Turn block'],
         'answer': 0,
         'explanation': 'The IMU calibrates in the first seconds after power-on or reset, and '
                        'assumes the robot is still. Put the robot down, power on or reset, wait '
                        'a few seconds, then press the button.'},

        {'kind': 'steps', 'title': 'Activity · Upload and run it',
         'size': 20,
         'steps': [
             'Create a new project called **Lesson_1_First_Drive**',
             'Build the forward/backward program from before',
             'Plug in the USB cable: your robot needs one USB connection before it can go '
             'wireless',
             'Click **CONNECT**, choose **USB**, and pick your robot from the list',
             'Set the robot down where it will drive (held it while it started? press **reset** '
             'and wait)',
             'Click the green **RUN** button: it uploads and starts. **Wait for button press** '
             'holds the robot still',
             'Press the User button on the robot: the program is released and it drives',
         ],
         'notes': 'Guided practice, 10 to 15 minutes. Expect it to drive about 20 cm out and back '
                  'to roughly where it started. Keep everyone on the cable for this first '
                  'upload: it is also the USB pass that makes Bluetooth possible later.'},

        {'kind': 'bullets', 'title': 'You\'ve succeeded when',
         'bullets': [
             'The program runs without errors',
             'The robot drives forward about 20 cm',
             'The robot drives back about 20 cm',
             'It stops near where it started',
         ],
         'callout': 'Not exactly 20 cm? Floor friction and battery level affect distance. Close is '
                    'fine for now.',
         'tone': 'green'},

        {'kind': 'bullets', 'title': 'If something goes wrong',
         'bullets': [
             '**Robot won\'t move:** check the battery is charged and the USB is seated, then '
             'click **RUN** again',
             '**Turns wildly off, or different every run:** it was moving while it powered on. '
             'Set it down, press reset, wait a few seconds hands off, try again',
             '**Drives the wrong way:** motor directions can be reversed; that\'s normal and '
             'fixable later',
             '**Not in the CONNECT list:** try another USB port or cable (some cables are '
             'charge-only), then reload the page',
             '**Not there over Bluetooth:** charge the battery, press reset, use Chrome or Edge. '
             'Still stuck? Plug in the cable and keep going',
         ],
         'size': 25,
         'notes': 'USB not detected is almost always a charge-only cable or a flaky port: keep a '
                  'couple of known-good data cables at the demo station. If RUN fails, have '
                  'students wait ten seconds and try once more before troubleshooting further.'},

        {'kind': 'steps', 'title': 'Activity · Make it your own',
         'lead': 'Now experiment. Try these in order:',
         'steps': [
             '**Go farther:** change the cm on both **Straight** blocks to `30` and re-run',
             '**Change the effort:** try `0.3`, then `0.8`. What changes: how **far** it goes, how '
             '**fast** it gets there, or both? Measure before you decide',
             '**Add a turn:** drop a **Turn** block between the two Straight blocks. What shape '
             'does the path make now?',
             '**Challenge:** make the robot drive a square and end up back where it started. No '
             'hints: try, run, watch, adjust',
         ],
         'notes': 'Lesson 1-2 picks up right where the challenge leaves off, so whatever they '
                  'figure out now is a head start. More challenge: measure the distance at Effort '
                  '0.3, 0.5, 0.7 and 1.0 and report what changes. More support: a starter '
                  'project with the blocks already placed, changing only the cm number, and '
                  'pair programming with Driver and Navigator roles.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Warehouses', 'Delivery robots',
              'Differential-drive robots shuttle shelves around fulfillment centers: the same '
              'two-motor steering as your XRP.'),
             ('Homes', 'Robot vacuums',
              'They drive, turn, and sense obstacles using exactly the sequence-of-commands idea '
              'from this lesson.'),
             ('Space', 'Planetary rovers',
              'Rovers upload a program, then run it on their own, because they\'re too far away '
              'to control live.'),
         ],
         'notes': 'The same ideas students just used run much bigger machines.'},

        {'kind': 'check',
         'question': 'True or false: you can run a program on the robot without uploading it.',
         'options': ['True',
                     'False: it has to be sent to the robot first (clicking RUN does that, over '
                     'USB or Bluetooth)'],
         'answer': 1,
         'explanation': 'Blockly is just the editor. Clicking RUN is what uploads the program to '
                        'the robot and starts it.'},

        {'kind': 'check',
         'question': 'True or false: the reflectance sensors detect color.',
         'options': ['True',
                     'False: they detect light vs. dark (white floor vs. black line), not color'],
         'answer': 1,
         'explanation': 'Reflectance sensors measure how much light bounces back, so they read '
                        'light and dark, not specific colors.'},

        {'kind': 'wrapup',
         'questions': [
             'What are the main parts of the robot, and what does each do?',
             'What does a block program actually do?',
             'How does a program get from your screen onto the robot?',
         ],
         'next': 'the Turn block and some geometry to draw shapes',
         'notes': 'Answer in your head or with a partner. The two true-or-false checks before '
                  'this slide are the lesson\'s wrap-up checks. Formative: can students navigate '
                  'XRP Code, drag blocks, and explain what each block does? Summative: a '
                  'successful first upload plus a plain-language explanation of the hardware and '
                  'of command sequencing. Next lesson: squares and triangles.'},
    ],
}
