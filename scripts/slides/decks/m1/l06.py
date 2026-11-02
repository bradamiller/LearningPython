DECK = {
    'module': 1, 'lesson': 6,
    'doc': 'module-01-driving/lesson-06-differential-drive',
    'title': 'Differential Drive & Motor Control',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Explain **differential drive**: steering by running the two wheels at different speeds',
             'Predict the robot\'s motion from what each side\'s motor is doing',
             'Use **Set effort** to control the motors directly (`-1` to `1`), and explain how '
             '**effort** differs from **speed**',
             'Steer with **Arcade**, and say what changing its **Turn** number does to the size of the circle',
             'Decide when to use direct motor control vs. the high-level `Straight`/`Turn`',
         ],
         'notes': '60 to 75 minutes. Under the hood: every Straight and Turn so far was really '
                  'two motors. Today students drive the motors directly, meet the word effort, '
                  'and finish with two hands-on activities (circles, then Earth – Moon – Earth). '
                  'Have dry-erase markers, whiteboard panels and the printable Earth and Moon '
                  'ready.'},

        {'kind': 'bullets', 'title': 'How the robot really steers',
         'bullets': [
             'Every `Straight` and `Turn` you\'ve used is really controlling **two motors**',
             'The XRP is a **differential drive** robot: it has no steering wheel',
             'All it can control is **how fast each side turns, and in which direction**',
             'That turns out to be enough for every motion it can make',
         ],
         'callout': 'Today you take the wheel: curves, spins and smooth steering the high-level '
                    'blocks can\'t do on their own',
         'tone': 'teal',
         'notes': 'Quick hook. Ask: a car steers by turning its front wheels. The XRP\'s wheels '
                  'can\'t turn. So how does it steer? Take a few answers, then predict.'},

        {'kind': 'figure', 'title': 'Predict first: which way will the robot drive?',
         'figure': './decks/m1/fig/l06-cases-predict.png',
         'caption': 'Seen from above. Arrows show which way each side turns, and how fast (longer = '
                    'faster). Straight, curve, swing around, or spin? Decide for each case.',
         'notes': 'Have every student commit to a prediction for all four cases before you '
                  'advance (write them down, or a show of fingers 1 to 4). On the lesson page each '
                  'case is an animation with a Drive it button; you can play them there instead '
                  'of the next slide.'},

        {'kind': 'figure', 'title': 'Drive it: what each case does',
         'figure': './decks/m1/fig/l06-cases-drive.png',
         'notes': 'Blue: the path of the point midway between the wheels. Purple: the point it '
                  'turns around. Case 1 drives straight. Case 2 arcs toward the slower side (here, right): the '
                  'faster side travels farther in the same time. Case 3 swings around the stopped '
                  'left wheel. Case 4 spins on the spot, around the pen hole midway between the '
                  'wheels. Ask who predicted each one right before explaining.'},

        {'kind': 'cards', 'title': 'One idea: drive each side on its own',
         'cards': [
             ('Same', 'Both sides, same speed', 'Drives straight. Match the two sides and '
                                                'there\'s nothing to turn the robot.'),
             ('Different', 'One side faster', 'Turns. The bigger the difference, the tighter the '
                                              'curve, until one side stops and it swings about '
                                              'that wheel.'),
             ('Opposite', 'Each side opposite', 'Turns in place. The robot rotates about its own '
                                                'center without going anywhere.'),
         ],
         'notes': 'Every one of the four cases comes from this: the left and right sides of the '
                  'driveline are operated independently.'},

        {'kind': 'check',
         'question': 'Your robot is supposed to drive straight but keeps drifting to the left. '
                     'What does that tell you about the two sides?',
         'options': ['Both sides are running at exactly the same speed',
                     'The right side is running slightly faster than the left',
                     'The motors are running in opposite directions',
                     'One side is completely stopped'],
         'answer': 1,
         'explanation': 'Drifting is Case 2 in miniature: the faster side travels farther, so the '
                        'robot curves toward the slower one. Drifting left means the right side '
                        'is winning.'},

        {'kind': 'bullets', 'title': 'Commanding the motors: Set effort',
         'bullets': [
             'Effort runs from `-1` (full reverse) through `0` (stopped) to `1` (full forward)',
             'You set **each wheel separately**, so each of the four cases is just a pair of '
             'effort numbers',
             '`Straight` **finishes**: it drives its 20 cm, stops the motors, and hands the '
             'program to the next block',
             '`Set effort` **doesn\'t finish**: it switches the motors on and moves straight to '
             'the next block, leaving them running',
         ],
         'callout': 'They keep running until something stops them',
         'notes': 'This is the big idea of the lesson: blocks that finish vs. blocks that don\'t. '
                  'Say it plainly now and come back to it in every section.'},

        {'kind': 'figure', 'title': 'When should the motors stop?',
         'figure': [
             {'name': 'wait_for_button_press'},
             {'name': 'set_effort', 'note': 'left: 0.5, right: 0.5  -> straight'},
             {'name': 'sleep', 'note': '3 seconds: the motors are still running the whole time'},
         ],
         'caption': 'A question `Straight` never asks you. For a first look we answer it with a '
                    '**Sleep**, but keep an eye on how well that works.',
         'notes': 'Set effort starts both wheels, and they stay on while the program sleeps. The '
                  'Sleep is a placeholder because we have no sensors yet; don\'t let timed driving '
                  'take root as a habit. The block pictures are the generic ones from the site, so '
                  'the numbers drawn inside a block can differ from the note beside it: the note '
                  'is what this program uses.'},

        {'kind': 'check',
         'question': 'You run Set effort with left 0.5 and right 0.5. What does the robot do?',
         'options': ['Curves to the left', 'Drives straight forward', 'Spins in place',
                     'Stays still'],
         'answer': 1,
         'explanation': 'Equal effort on both wheels means both sides move at the same speed, so '
                        'the robot goes straight.'},

        {'kind': 'check',
         'question': 'What happens with left 0.5 and right -0.5 (one wheel forward, one backward)?',
         'options': ['Drives straight', 'Spins in place', 'Drives backward', 'Curves gently'],
         'answer': 1,
         'explanation': 'Opposite efforts push the two sides in opposite directions, so the robot '
                        'rotates on the spot.'},

        {'kind': 'bullets', 'title': 'Effort is not the same as speed',
         'bullets': [
             'Effort is **how hard the motors try**: electrically, how much voltage they get',
             'Like your own effort in a sport: how hard you\'re working, not how fast you go',
             'Pedal uphill at a constant effort and you slow down; the same effort on the flat '
             'carries you much faster',
             '**Effort** is your input. **Speed** is the result',
         ],
         'split': 0.5,
         'figure': '/img/lesson-06/motor-effort-analogy.jpg',
         'callout': 'Speed depends on the hill, the carpet, the battery, and how much the robot '
                    'is carrying',
         'tone': 'teal',
         'notes': 'Name this explicitly, or students read "effort 0.5" as "half speed" and are '
                  'puzzled when the same program behaves differently on carpet, a ramp or a '
                  'tired battery. The bike-uphill analogy lands fastest.'},

        {'kind': 'frames', 'title': 'Same hill, two ways to drive',
         'figure': '/img/lesson-06/effort-vs-speed-on-a-hill.svg',
         'frames': [(0.42, '**Effort control**: same effort, so the hill sets the speed'),
                    (0.8, '**Speed control**: same speed, so the hill sets the effort')],
         'callout': 'Name the speed you want, and the robot adjusts its own effort: harder uphill, '
                    'easing off on the way down',
         'notes': 'Dots are dropped at equal time steps: bunched means slow, spread out means fast. '
                  'Left: effort held, the robot crawls uphill and races down. Right: speed held, '
                  'the effort gauge drops low on the downhill. The lesson page animates both '
                  'runs with buttons; worth playing live.'},

        {'kind': 'bullets', 'title': 'Why the same numbers move differently',
         'bullets': [
             'Effort `0.5` on a smooth floor is quicker than effort `0.5` on thick carpet',
             'And quicker again with a fresh battery',
             '`Straight` and `Turn` are more repeatable than raw effort',
             'They **watch the robot\'s sensors and adjust**, instead of blindly holding one '
             'voltage',
         ],
         'notes': 'If you have a ramp or a carpet square handy, run one Set effort program on '
                  'both surfaces back to back: thirty seconds of demo and the distinction sticks. '
                  'This is also the honest answer to "why do we even have Straight and Turn?": '
                  'they close the loop with sensors; Set effort is open-loop. Module 2\'s line '
                  'following builds on adjusting effort from what the robot senses.'},

        {'kind': 'check',
         'question': 'You set both motors to effort 0.5 and drive across a smooth floor, then '
                     'across a thick carpet. What happens?',
         'options': ['The robot travels at the same speed on both: effort sets the speed',
                     'Slower on the carpet: effort is how hard the motors try, and the carpet '
                     'fights back',
                     'It goes faster on the carpet',
                     'The robot refuses to move on carpet'],
         'answer': 1,
         'explanation': 'Effort is the input (roughly, motor voltage), not the outcome. The same '
                        'effort against more resistance gives less speed, exactly like pedalling '
                        'a bike uphill.'},

        {'kind': 'check',
         'question': 'A robot is asked to hold a steady speed as it drives up and over a hill. '
                     'What does its effort do?',
         'options': ['Stays at one fixed value the whole way',
                     'Rises going uphill and drops going downhill, to keep the speed the same',
                     'Drops going uphill', 'Goes to zero at the top'],
         'answer': 1,
         'explanation': 'That\'s the trade: commanding speed means the robot changes effort by '
                        'itself to maintain what you asked for. Commanding effort means you fix '
                        'the effort and let the speed vary.'},

        {'kind': 'steps', 'title': 'Blocks that finish vs. blocks that don\'t',
         'tag': 'Try it',
         'lead': 'Run the Set effort program (effort `0.5`, Sleep 3 seconds) three times, and '
                 'measure how far the robot goes each time:',
         'steps': [
             'With a **fresh battery**',
             'On **carpet**',
             'On a **smooth floor**',
         ],
         'callout': 'Three seconds at effort `0.5` is not a distance. It\'s three seconds.',
         'tone': 'orange',
         'notes': 'The distance changes with the battery, the surface, the weight on the robot, '
                  'even whether the floor slopes. That\'s effort-isn\'t-speed showing up as a '
                  'practical problem. Having students measure it themselves is what stops timed '
                  'driving from taking root.'},

        {'kind': 'cards', 'title': 'Two kinds of block',
         'cards': [
             ('Finishes', 'Straight / Turn', 'Runs until the job is done (the distance driven, '
                                            'the angle turned), then stops the motors by itself. '
                                            'The next block doesn\'t start until it\'s finished.'),
             ('Doesn\'t finish', 'Set effort / Arcade', 'Switches the motors on and moves to the '
                                                        'next block immediately. The motors stay '
                                                        'on until something stops them.'),
         ],
         'height': 3.4,
         'notes': 'The distinction to drill: finishing vs. not finishing. It\'s also abstraction '
                  'vs. control: Straight and Turn are precise and repeatable but limited to '
                  'straight lines and pivots; Set effort is raw but can make smooth curves. '
                  'Neither is better; it\'s the right tool for the task.'},

        {'kind': 'bullets', 'title': 'What stops the motors?',
         'lead': 'Three things:',
         'lead_h': 0.7,
         'bullets': [
             'A **Stop motors** block',
             'Another `Set effort` (including effort `0`)',
             'The program ending',
             'No stop block needed at the **end** of a program: the robot stops the motors '
             'when the program is over',
         ],
         'split': 0.68,
         'figure': '/img/blocks/stop_motors.png',
         'callout': 'Any time the motors should quit while the program keeps going, that\'s what '
                    '**Stop motors** is for',
         'tone': 'teal',
         'notes': 'Head off the habit of a stop block at the end of every program: it does '
                  'nothing there. Stop motors is for stopping mid-program.'},

        {'kind': 'bullets', 'title': 'What should the robot wait for?',
         'bullets': [
             'A Sleep is the crudest possible answer, and you just measured why',
             'The answer for the rest of this course: stop on something the robot **senses**',
             [
                 'until the rangefinder says the wall is 10 cm away',
                 'until the reflectance sensor sees the line',
                 'until the encoder has counted far enough',
             ],
             'Same `Set effort`, but the robot decides when it\'s done instead of the clock',
         ],
         'callout': 'That\'s where Module 2 goes next',
         'tone': 'teal',
         'notes': 'Real programs stop on what the robot senses (Module 2), or use Straight/Turn '
                  'when a measured distance is what they want.'},

        {'kind': 'check',
         'question': 'What\'s the difference between what Straight does and what Set effort does?',
         'options': ['Straight drives its distance and stops; Set effort starts the motors and '
                     'leaves them running',
                     'They do the same thing: Set effort is just the Python version',
                     'Straight leaves the motors running; Set effort stops them when it finishes',
                     'Set effort can only drive backward'],
         'answer': 0,
         'explanation': 'Straight and Turn finish a job and stop. Set effort just sets the motors '
                        'going: deciding when they stop is now your problem.'},

        {'kind': 'check',
         'question': 'Why is "Set effort 0.5, Sleep 3 seconds" a poor way to travel a set distance?',
         'options': ['Sleep blocks are slower than Straight blocks',
                     'Effort is not speed: 3 seconds covers different distances with battery, '
                     'surface, and load',
                     'Sleep stops the motors, so the robot never gets anywhere',
                     'The robot cannot run Set effort and Sleep in the same program'],
         'answer': 1,
         'explanation': 'Timed driving is guesswork: a fresh battery on a smooth floor goes much '
                        'farther in 3 seconds than a tired one on carpet. Use Straight for a '
                        'distance, and a sensor to stop at something.'},

        {'kind': 'bullets', 'title': 'Smooth steering with Arcade',
         'lead': 'Setting two efforts by hand is fiddly. **Arcade** takes two numbers, like a game '
                 'controller, and works out the two motor efforts for you:',
         'lead_h': 1.2,
         'bullets': [
             '**Straight**: how fast it drives forward (the one people call speed)',
             '**Turn**: how hard it bends, and which way',
             [
                 '`0` is dead straight',
                 'positive and negative bend opposite ways',
             ],
         ],
         'notes': 'For more support, let students use Arcade before Set effort: it is more '
                  'intuitive. Start with symmetric efforts (0.3 on both wheels) before curves, and '
                  'give a table of effort pairs and their outcomes. For more challenge: build a '
                  'spiral by gradually increasing one side\'s effort across several Set effort '
                  'blocks.'},

        {'kind': 'figure', 'title': 'Arcade in a program',
         'figure': [
             {'name': 'wait_for_button_press'},
             {'name': 'arcade', 'note': 'Straight: 0.5, Turn: 0.3  -> forward, curving left'},
             {'name': 'sleep', 'note': '3 seconds: again, a stand-in until we have sensors'},
         ],
         'caption': 'Arcade combines forward motion and steering into one block. Like Set effort, '
                    'it doesn\'t finish: the Sleep says when to stop.',
         'notes': 'A positive Turn bends left (counterclockwise). The Arcade block picture is the '
                  'generic one from the site and shows its own default numbers; the note beside it '
                  'gives the values this program uses (Straight 0.5, Turn 0.3).'},

        {'kind': 'check',
         'question': 'When is the Arcade block a better choice than Set effort?',
         'options': ['When you need smooth, intuitive steering like a game controller',
                     'When you need to control each wheel to an exact effort',
                     'When you want precise, measured distances',
                     'Arcade and Set effort are exactly the same'],
         'answer': 0,
         'explanation': 'Arcade is easiest for smooth curves and navigation; Set effort gives '
                        'finer, per-wheel control when you need it.'},

        {'kind': 'table', 'title': 'Activity · Get a feel for circles',
         'tag': 'Step 1',
         'lead': 'Marker in the holder, on a whiteboard panel. Wait for button, Arcade, Sleep: '
                 'Straight `0.5`, a Sleep long enough to come round once. Change **only Turn**.',
         'headers': ['Straight', 'Turn', 'How big was the circle?'],
         'widths': [1.3, 1.3, 5],
         'rows': [['0.5', '0.15', ''], ['0.5', '0.3', ''], ['0.5', '0.5', ''], ['0.5', '0.8', '']],
         'callout': 'No exact measurements needed. Write one sentence: what happens to the circle '
                    'when the turn number goes up?',
         'tone': 'teal',
         'notes': 'Circles first, so students aren\'t fighting what the numbers do and a '
                  'four-part mission at the same time. No marker? Chalk a starting mark and '
                  'eyeball it. Step 1 is genuinely open: resist handing over the relationship; '
                  'it takes about four runs to see, and a student who says it owns it.'},

        {'kind': 'check',
         'question': 'You run Arcade with Straight 0.5 and Turn 0.3, then change Turn to 0.6. '
                     'What happens to the circle?',
         'options': ['It gets bigger', 'It gets smaller: more turn means a tighter circle',
                     'It stays the same size but the robot goes faster', 'The robot drives straight'],
         'answer': 1,
         'explanation': 'Turn is how hard the robot is bending. More bend for the same forward '
                        'speed means a tighter circle. Turn 0 is no bend at all: a straight line.'},

        {'kind': 'frames', 'title': 'Compare with a simulated robot',
         'tag': 'After your own runs',
         'figure': '/img/lesson-06/arcade-circles.svg',
         'crop': (0.0, 0.08, 1.0, 1.0),
         'frames': [(0.30, 'Turn **0.15**: about 50 cm across'),
                    (0.55, 'Turn **0.3**: about 25 cm across')],
         'callout': 'Watch the two wheel efforts as well as the circle',
         'notes': 'Show only after students have done their own runs. The simulated robot is '
                  'drawn to scale on a whiteboard panel. Their robots\' circles won\'t match '
                  'these numbers exactly, and that\'s expected.'},

        {'kind': 'frames', 'title': 'Compare with a simulated robot',
         'tag': 'After your own runs',
         'figure': '/img/lesson-06/arcade-circles.svg',
         'crop': (0.0, 0.08, 1.0, 1.0),
         'frames': [(0.77, 'Turn **0.5**: the left wheel stops, about 15 cm'),
                    (0.95, 'Turn **0.8**: the left wheel runs backward, about 10 cm')],
         'callout': 'The bigger the difference between the wheels, the tighter the circle',
         'notes': 'At Turn 0.5 the inside wheel stops and the robot swings around it (Case 3). '
                  'At 0.8 the inside wheel runs backward and the circle is smaller than the '
                  'robot (heading toward Case 4).'},

        {'kind': 'steps', 'title': 'Step 2 · Find a circle that fits',
         'steps': [
             'Aim for a circle roughly **12 to 18 inches** (30–45 cm) across: it fits on a '
             'whiteboard panel and on your desk space later',
             'Don\'t calculate it. Change Turn, run it, look, change it again. Three or four '
             'tries is normal',
             'Write both numbers down and don\'t lose them:  My circle: Straight ____ Turn ____',
         ],
         'callout': 'Every robot lands on slightly different numbers. The rest of this lesson uses yours.',
         'tone': 'teal',
         'notes': 'For your eyes only: at Straight 0.5, a Turn around 0.4 to 0.6 usually lands in '
                  'the 12 to 18 inch range, but don\'t publish it; it varies with battery, floor '
                  'and tyre wear, and the hunt is the point. If a group is stuck, ask which '
                  'direction to move the number, not which number to use.'},

        {'kind': 'steps', 'title': 'Step 3 · Time a half circle',
         'steps': [
             'Keep Straight and Turn exactly as they are. Change only the **Sleep**',
             'Stop when the robot faces the **opposite** direction from where it started: a half circle',
             'Start from a wall or a tape line, so you have something to judge against',
             'Write it down:  My half circle takes ____ seconds. A full circle takes twice that',
         ],
         'callout': '"Is it pointing backwards?" you can answer by looking. "Is it back where it '
                    'started?" is a guess.',
         'tone': 'orange',
         'notes': 'Insist on the point-the-opposite-way test. Students who judge a full circle are '
                  'out by a quarter turn without knowing it, and in the next activity that error '
                  'is what makes them miss the Earth. The drawn circles are worth the mess: '
                  'identical numbers on two robots give different circles, which is the '
                  'timed-driving problem arriving on its own.'},

        {'kind': 'check',
         'question': 'Your half circle takes 1.4 seconds. Roughly how long is a full circle at the '
                     'same Straight and Turn?',
         'options': ['Still 1.4 seconds', 'About 2.8 seconds: twice as far around',
                     'About 0.7 seconds', 'There is no way to tell'],
         'answer': 1,
         'explanation': 'Nothing about the robot\'s motion changed (same Straight, same Turn), so '
                        'going twice as far around the circle takes twice as long.'},

        {'kind': 'bullets', 'title': 'Activity · Earth – Moon – Earth',
         'bullets': [
             'Tape an **Earth** and a **Moon** to your whiteboard panel, about 18–24 inches '
             '(45–60 cm) apart',
             'Your robot is a spacecraft. Its mission:',
             [
                 'swing around the Moon',
                 'cross to the Earth',
                 'swing around the Earth **the other way**',
                 'come back to rejoin its own lunar orbit',
             ],
         ],
         'split': 0.47,
         'figure': '/img/lesson-06/earth-moon-mission.svg',
         'frame': 0.0,
         'crop': (0.065, 0.0, 0.935, 1.0),
         'callout': 'Printable Earth and Moon: in this lesson\'s Resources. Print, cut out, tape down.',
         'tone': 'teal',
         'notes': 'Both bodies are drawn the same size, which is not remotely true and very '
                  'convenient: both orbits are the same size, so the circle numbers from the last '
                  'activity work for each. (The real Moon is about a quarter of Earth\'s width, '
                  'and thirty Earths would fit in the gap.) The mission framing gives students a '
                  'reason to care whether the robot arrives pointing the right way, which is what '
                  'actually teaches heading. The whole path fits in roughly 1 m by 0.5 m.'},

        {'kind': 'bullets', 'title': 'Step 1 · Plan the mission on paper',
         'bullets': [
             'Before you touch a block, **draw the path**',
             'Mark where the robot starts and which way it goes round the Moon',
             'Mark where it crosses to the Earth, and which way it goes round that one',
             'You should end up with a shape you recognize',
         ],
         'callout': 'The robot bends **one way** around the Moon and **the other way** around the '
                    'Earth. That\'s why `Straight` and `Turn` blocks can\'t draw this shape at all.',
         'tone': 'orange',
         'notes': 'Step 1 is not optional. Students who skip the drawing tune four numbers at once '
                  'with no idea which one is wrong. The drawing tells them what should happen, so '
                  'a wrong run becomes information.'},

        {'kind': 'bullets', 'title': 'How far apart should the bodies go?',
         'bullets': [
             'About **one and a half times your circle\'s diameter**',
             'Any closer: the crossings are too shallow to see',
             'Any further: they get steep and the path stops looking like an infinity symbol',
             'At one and a half, the crossings meet at a tidy 45°, and each swing is '
             '**three-quarters of a turn**',
         ],
         'callout': 'A 14-inch circle wants the Earth and Moon about 21 inches apart',
         'tone': 'teal',
         'notes': 'If a group picked a big circle in the last activity, they spread the bodies out '
                  'to match, or go back and find a smaller circle. That is a fair consequence, '
                  'not a failure.'},

        {'kind': 'table', 'title': 'Step 2 · Build the mission',
         'lead': 'Four moves, and you already have the numbers for two of them:',
         'headers': ['#', 'Move', 'Block', 'The number'],
         'widths': [0.6, 3.4, 2.4, 3.8],
         'rows': [
             ['1', 'Orbit the Moon', 'Arcade + Sleep', 'your Straight and Turn'],
             ['2', 'Cross to the Earth', 'Straight', 'the gap, in cm'],
             ['3', 'Orbit the Earth, the other way', 'Arcade + Sleep', 'same, with Turn **negated**'],
             ['4', 'Cross back to the Moon', 'Straight', 'the same gap'],
         ],
         'callout': 'Orbit Sleep: about **three-quarters** of a full circle, 1.5 times your '
                    'half-circle time. Tune from there.',
         'tone': 'teal',
         'notes': 'Three-quarters is not a guess: with the bodies spaced at one and a half '
                  'diameters, three-quarters of a turn is exactly what brings the robot out of a '
                  'swing pointing at the other body.'},

        {'kind': 'frames', 'title': 'Measured vs. timed, in one program',
         'figure': '/img/lesson-06/earth-moon-mission.svg',
         'crop': (0.065, 0.0, 0.935, 1.0),
         'frames': [(0.08, 'Crossings: `Straight` **finishes**, so it\'s drawn solid'),
                    (0.25, 'Swings: Arcade needs a Sleep, so it\'s drawn dashed')],
         'callout': 'A distance lands the same way every run. A time is a much shakier thing to rely on.',
         'tone': 'teal',
         'notes': 'This is the finishes / doesn\'t-finish distinction from earlier, doing real work '
                  'in one program. The animated figure on the lesson page flies the whole '
                  'mission; the robot itself does not appear in these still frames.'},

        {'kind': 'bullets', 'title': 'Step 3 · Fly it, then fix it',
         'lead': 'It will not work first time. That\'s the job:',
         'lead_h': 0.75,
         'bullets': [
             '**Overshooting the turn round the Moon**: it leaves pointing the wrong way. '
             'Shorten that Sleep',
             '**Missing the Earth entirely**: the crossing distance is wrong, or the orbit before '
             'it left the robot off-heading. Fix the heading first',
             '**A lopsided path**: the two Turn values aren\'t true mirror images. Check the sign '
             'is the only thing that changed',
         ],
         'size': 24,
         'callout': '**You\'ve succeeded when** the marker loops the Moon, crosses to the Earth, '
                    'loops it the other way, and comes back to meet where it started',
         'tone': 'green',
         'notes': 'The first flight rarely closes, and that is the useful part. Two robots with '
                  'identical numbers fly visibly different missions; the same robot differs on a '
                  'fresh battery. Name it: the only reason we\'re timing this is that the robot '
                  'can\'t yet sense where it is. Module 2 picks that thread up.'},

        {'kind': 'bullets', 'title': 'Challenge, and no whiteboard?',
         'bullets': [
             '**Challenge**: move the two bodies further apart without changing the size of your '
             'orbits. Which of the four numbers has to change, and which don\'t?',
             '**No whiteboard panel or cutouts?** Two sticky notes on the floor work, or two '
             'chalk marks',
             'You lose the drawn path, so judge by eye: does the robot pass close to each marker, '
             'and finish where it began?',
         ],
         'notes': 'If you want the science: the Apollo missions really did fly a figure-eight. The '
                  'free-return trajectory loops behind the Moon and lets its gravity throw the '
                  'spacecraft back toward Earth, so if the engines fail the crew comes home '
                  'anyway. It\'s what saved Apollo 13. Worth ninety seconds, not a lesson.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Mobility', 'Wheelchairs & rovers', 'Powered wheelchairs and Mars rovers steer by '
                                                  'differential drive: this left/right speed trick.'),
             ('Gaming', 'Twin-stick control', 'Tank-style games map two sticks to two "tracks", '
                                              'the same idea as setting two efforts.'),
             ('Heavy equipment', 'Skid-steer loaders', 'Construction skid steers turn by driving '
                                                       'their left and right wheels at different '
                                                       'speeds.'),
             ('Spaceflight', 'Free-return trajectory', 'Apollo flew a real figure-eight: loop '
                                                       'behind the Moon, let its gravity throw '
                                                       'you back at Earth. It brought Apollo 13 '
                                                       'home.'),
         ],
         'height': 4.2,
         'notes': 'Direct motor control is how machines that don\'t drive in straight lines work.'},

        {'kind': 'wrapup',
         'questions': [
             'How does a differential-drive robot turn?',
             'What happens to the motors when Straight finishes? And after Set effort?',
             'Why is timed driving unreliable, and what should a robot stop on instead?',
             'When would you pick `Straight`/`Turn` over `Set effort`?',
             'In Arcade, which number changes the size of the circle, and which way?',
         ],
         'next': 'Lesson 1-7, Blockly challenges: the capstone of the Blockly phase',
         'notes': 'Answers: by running its wheels at different speeds. Straight stops them; Set '
                  'effort leaves them running. Effort isn\'t speed (battery and surface change '
                  'the distance); stop on a sensor reading. When you need precise, repeatable '
                  'distances and angles. Turn: bigger Turn, tighter circle. Exit ticket: "Fill in '
                  'efforts to spin the robot in place" (equal and opposite, e.g. 0.5 / -0.5).'},
    ],
}
