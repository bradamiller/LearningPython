def device(n, title, photo, lead, prompts, notes):
    """One device from the gallery: the photo, its caption and its Think about it prompt."""
    return {'kind': 'figure', 'title': title, 'tag': f'Device {n} of 8',
            'figure': photo,
            'caption': lead + '   **Think about it:** ' + ' '.join(prompts),
            'notes': notes}


DECK = {
    'module': 1, 'lesson': 0,
    'doc': 'module-01-driving/lesson-00-what-is-a-robot',
    'title': 'What Is a Robot?',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Argue whether a given device is or isn\'t a robot, and say **why**',
             'Work out, from the examples, what every robot has to be able to do, and state it '
             'as a short definition',
             'Explain why the classic "mechanical arm" definition isn\'t enough anymore',
             'Describe how the XRP, and this course, fits that definition',
         ],
         'notes': '30 to 40 minutes, a kickoff discussion with no coding. The lesson page holds '
                  'the talking points and the "answers" in teacher boxes; these notes carry '
                  'the short version. Rough budget: 15 minutes for the gallery, 10 for the '
                  'definition, 5 to 10 for the wrap-up.'},

        {'kind': 'video', 'title': 'It used to be easy to tell',
         'video': '/videos/gort.mp4', 'poster_at': 1,
         'caption': 'Gort, from The Day the Earth Stood Still (1951): the robot everyone '
                    'recognizes. Today the line is a lot blurrier.',
         'notes': 'For most of the last century a robot was easy to spot: a metal figure with '
                  'a visor, walking stiffly out of a flying saucer. Nobody argued about '
                  'whether that was a robot. The clip plays from the slide.'},

        {'kind': 'bullets', 'title': 'Where do you draw the line?',
         'lead': 'The machines around us are smarter now, and much less obvious.',
         'bullets': [
             'Is the thing in your pocket a robot?',
             'The car in the driveway?',
             'The washing machine?',
         ],
         'callout': 'You\'ll look at eight machines and argue it out until a **definition** '
                    'emerges',
         'tone': 'teal',
         'notes': 'This is a discussion, not a lecture: do not reveal answers as you go, the '
                  'value is in the disagreement. A format that works: show one device at a '
                  'time, have students vote with their feet (robot on one side, not a robot on '
                  'the other, not sure in the middle), then ask someone from each side to '
                  'defend it. Keep a running list of their reasons on the board. Listen for, '
                  'and amplify, sensors and acting on what was sensed, but do not name those '
                  'traits for them. Keep asking "what\'s your reason?"'},

        {'kind': 'steps', 'title': 'Activity · Is this a robot?',
         'lead': 'You\'re about to see eight devices. For **each one**, before the class '
                 'discusses it:',
         'steps': [
             '**Decide:** robot or not a robot. You have to pick: no "not sure."',
             '**Say why.** One sentence: what is it about this device that makes it a robot, '
             'or keeps it from being one?',
             'Record your answer in the box under the picture, or on paper. You\'ll look back '
             'over all eight at the end.',
         ],
         'callout': 'Most prompts ask the same thing: **what happens if the person walks away?**',
         'tone': 'teal',
         'notes': 'The Yes/No buttons and the Why? line under each picture on the lesson page '
                  'are live: type the class consensus there on the projector so nobody has to '
                  'scroll back.'},

        device(1, 'A radio-controlled airplane', '/img/lesson-01/RadioControlledAirplane.jpg',
               'It flies. It has motors. Somebody\'s holding a controller. Robot?',
               ['If the pilot sets the controller down, what does the '
                'plane do next?'],
               'Most say not a robot, and the reason is the key one: a person does all the '
               'deciding. The plane senses nothing and decides nothing; the pilot\'s eyes and '
               'hands do. Push back gently: "It has motors and it moves. Isn\'t that enough?" '
               'You want them to say that moving isn\'t the test.'),

        device(2, 'A camera drone', '/img/lesson-01/Drone.jpg',
               'Also flies, also has a controller in the box. Same answer as the airplane?',
               ['If the pilot lets go of the sticks, what happens?',
                'If your answer is different from the airplane\'s, what makes the difference?'],
               'The pair to the airplane, and where the room starts to split. A camera drone '
               'has GPS, obstacle sensors and a computer that holds it level, stops it hitting '
               'a wall and flies it home on low battery, even with a human nominally in '
               'control. Ask: "What can the drone do that the airplane can\'t?" It senses and '
               'makes some decisions itself.'),

        device(3, 'A vacuum cleaner', '/img/lesson-01/ManualVacuum.jpg',
               'Powerful motor, does a useful job. Robot?',
               ['Who steers it?',
                'If you walk away in the middle of cleaning, what happens?'],
               'An easy no, for the same reason as the airplane: a person pushes it everywhere. '
               'A motor and a job, but no sensing and no deciding. Keep it quick; it sets up '
               'the next one.'),

        device(4, 'A vacuum that drives itself', '/img/lesson-01/RobotVacuum.jpg',
               'Same job as the vacuum before. Different answer?',
               ['What\'s different about **how** it does the job?',
                'What happens if you walk away?'],
               'Nearly everyone says yes; it is even called a robot vacuum. Make them prove it. '
               'What does it sense (bumper, cliff sensors, dirt detection)? What does it decide '
               '(turn when it hits something, go back to the dock)? What does it do (drive, '
               'vacuum)? Put sense, decide and do on the board: they are about to become the '
               'definition.'),

        device(5, 'A car', '/img/lesson-01/RedCar.jpg',
               'A car. Is a car a robot?',
               ['Answer once with a person driving, then again with the car in self-driving mode. Did your answer change? If '
                'so, what changed about the **car**?'],
               'Expect a real split, and let it run. With a person driving, most say no. On '
               'driver assist or self-driving, cameras sense the road, a computer decides to '
               'brake or steer, and it steers: most say yes. The same machine can be a robot '
               'or not depending on what is doing the thinking. Celebrate a student who gets '
               'there alone.'),

        device(6, 'A laundry-folding machine', '/img/lesson-01/ClothesFolding.jpg',
               'A research robot folding laundry.',
               ['Most people say yes right away, so say **precisely** what makes it one.',
                'What would it have to know about the towel in order to fold it?'],
               'An easy yes, and a chance to name why it is hard: it has to sense where the '
               'cloth is, work out how to grab it, and move its arms precisely. A task trivial '
               'for a person is a research problem for a robot, which students will feel in '
               'Module 2 when line following turns out harder than it looks.'),

        device(7, 'A Mars rover', '/img/lesson-01/MarsRover.jpg',
               'A rover on Mars, hundreds of millions of km away.',
               ['A radio signal takes minutes each way. How does that change how it\'s driven? '
                'Compare the RC airplane.'],
               'Yes, and the twist is worth stating: with minutes of delay each way, nobody can '
               'drive it with a joystick. It has to look at the ground, decide whether a rock '
               'is safe, and drive around it by itself. Ask: "Why couldn\'t NASA just '
               'remote-control it like the airplane?" Distance forces autonomy.'),

        device(8, 'A washing machine', '/img/lesson-01/WashingMachine.jpg',
               'A washing machine. Think carefully before you answer.',
               ['Press start and walk away. What does it do on its own?',
                'Look at what you wrote for the vacuum that drives itself. Are you being '
                'consistent?'],
               'Save this one for last: it breaks the room. Students say "obviously not" until '
               'someone points out it senses the load and water level, decides when to spin '
               'and how long to rinse, and acts, all without a person after the button press. '
               'Don\'t resolve it. "Robot" is a spectrum, not a switch: simple and fixed here, '
               'rich and adaptable in a rover.'),

        {'kind': 'bullets', 'title': 'Look back over your eight answers',
         'bullets': [
             'What do your **yes** reasons have in common?',
             'What do your **no** reasons have in common?',
             'Try to write the rule in one sentence',
         ],
         'callout': 'A device is a robot if it ______.',
         'tone': 'orange',
         'notes': 'Harvest the board into the definition. Group the class\'s words into sense, '
                  'think and act: you are naming the definition they built, not handing one '
                  'over. The punchline: every device on the list moves or acts, so acting '
                  'can\'t be the test; the robots sense something and act on what they sensed. '
                  'If a student says "it\'s not about moving, it\'s about sensing and deciding," '
                  'write it on the board in their words.'},

        {'kind': 'bullets', 'title': 'So what is a robot? The 1979 answer',
         'lead': 'The Robot Institute of America, 1979: "a reprogrammable, multifunctional '
                 'manipulator designed to move material, parts, tools, or specialized devices '
                 'through various programmed motions for the performance of a variety of '
                 'tasks."',
         'lead_h': 1.6, 'size': 23,
         'bullets': [
             'In plain English: a **programmable mechanical arm** that does factory work: '
             'assembly, welding, painting',
             'The classic jobs are the **three Ds**: work that is **dirty, dull, or dangerous** '
             'for people',
         ],
         'callout': 'Check it against the eight: a Mars rover isn\'t a "manipulator," and '
                    'neither is a drone or a robot vacuum. Too narrow.',
         'tone': 'orange'},

        {'kind': 'check',
         'question': 'Which device from the lineup does the 1979 "reprogrammable manipulator" '
                     'definition clearly leave out, even though almost everyone agrees it\'s a '
                     'robot?',
         'options': ['The towel-folding robot: it has arms',
                     'The Mars rover: it drives and explores, but it isn\'t a manipulator arm',
                     'The RC airplane',
                     'The canister vacuum'],
         'answer': 1,
         'explanation': 'The 1979 definition describes a factory arm. A rover, a drone, or a '
                        'robot vacuum has no manipulator at all, yet they\'re clearly robots. '
                        'That\'s why we need a better definition.'},

        {'kind': 'cards', 'title': 'Try again: sense, think, act',
         'height': 3.9,
         'cards': [
             ('1 · Sense', 'Take in the world',
              'Cameras, bump sensors, distance sensors, GPS, light sensors: some way of '
              'finding out what\'s out there.'),
             ('2 · Think', 'Decide',
              'A program that turns sensor readings into a choice: turn left, stop, go home, '
              'grab here.'),
             ('3 · Act', 'Change the world',
              'Motors, wheels, arms, propellers: something that carries the decision out '
              'physically.'),
         ],
         'notes': 'These three traits come from the robotics engineering program at WPI. A robot '
                  'must sense (take in information with some kind of sensor), think (process '
                  'what it sensed and decide), and act (do something in the world based on that '
                  'decision). Point back at the class\'s own words on the board.'},

        {'kind': 'bullets', 'title': 'Miss one, and it\'s something else',
         'bullets': [
             'A machine that only **acts** is a **tool**: the vacuum cleaner',
             'A machine where a **person** does the sensing and thinking is '
             '**remote-controlled**: the airplane',
         ],
         'callout': 'A robot must **sense**, **think**, and **act**',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'Using sense, think, act, why isn\'t the RC airplane a robot?',
         'options': ['It can\'t fly high enough',
                     'The human does the sensing and thinking; the plane only acts',
                     'It has no motor',
                     'It isn\'t reprogrammable'],
         'answer': 1,
         'explanation': 'The plane acts (motor, control surfaces), but all the sensing (the '
                        'pilot\'s eyes) and deciding (the pilot\'s hands) happen in a person. '
                        'Two of the three traits are missing from the machine itself.'},

        {'kind': 'check',
         'question': 'Why can\'t NASA fly a Mars rover the way you\'d fly the RC airplane?',
         'options': ['Mars has no radio',
                     'The radio delay is minutes each way, so the rover must sense and decide '
                     'for itself',
                     'Rovers have no motors',
                     'It could; they just prefer not to'],
         'answer': 1,
         'explanation': 'A command takes minutes to arrive and the reply takes minutes to come '
                        'back. By then the rover could have driven off a ledge. Distance forces '
                        'it to do its own sensing and thinking.'},

        {'kind': 'check',
         'question': 'A washing machine senses the load, follows cycle logic, and spins on its '
                     'own. Under sense, think, act, what\'s the honest answer?',
         'options': ['Definitely not a robot: it doesn\'t move around',
                     'All three, in a simple, fixed way: the low end of a robot spectrum, and '
                     'arguing is the point',
                     'Definitely a robot, exactly like a Mars rover',
                     'It fails because it has no sensors'],
         'answer': 1,
         'explanation': 'By the letter of the definition it qualifies, just barely: simple '
                        'sensing, fixed logic, one kind of action. A good definition makes the '
                        'disagreement precise; it doesn\'t always make it go away.',
         'notes': 'Answer: B. The spectrum idea (washing machine at one end, rover at the other) '
                  'is the most important nuance here. It heads off the "is it or isn\'t it" '
                  'dead end, and it sets up the idea that this course moves the XRP along that '
                  'spectrum.'},

        {'kind': 'bullets', 'title': 'Why robots?',
         'bullets': [
             'Robots combine **many ideas at once**',
             'A competition robot built by high-school students **senses** where the balls '
             'and the goal are with a camera, **thinks** with trigonometry to aim, and '
             '**acts**: it drives into position and shoots',
             'A climbing robot needs torque, gear ratios and speed calculations just to get off '
             'the ground',
         ],
         'callout': 'Robotics is where math, physics, and programming stop being separate '
                    'subjects',
         'tone': 'teal'},

        {'kind': 'video', 'title': 'Sense, think, act in competition',
         'video': '/videos/ballshooter.mp4', 'poster_at': 10,
         'caption': 'A FIRST competition robot built by high-school students: it senses the '
                    'balls and goal with a camera, aims with trigonometry, and shoots.',
         'notes': 'While it plays, ask the class to call out each part as they see it: what is '
                  'it sensing, what is it deciding, what is it doing?'},

        {'kind': 'cards', 'title': 'The robot on your desk',
         'height': 4.3,
         'cards': [
             ('Sense', 'The XRP\'s senses',
              'Reflectance sensors that see light vs. dark, an ultrasonic rangefinder that '
              'measures distance, and encoders that count how far each wheel has turned.'),
             ('Think', 'The XRP\'s brain',
              'The controller board runs **your** program. Every decision it makes is one you '
              'wrote: in Blockly first, then in Python.'),
             ('Act', 'The XRP\'s muscles',
              'Two motors, one per wheel. That\'s enough to drive straight, turn, curve, and '
              'spin.'),
         ],
         'notes': 'Hold up an XRP and point at each part as you read the card.'},

        {'kind': 'bullets', 'title': 'The shape of this course',
         'bullets': [
             '**Module 1:** mostly **act**: driving, turning, drawing shapes',
             '**Module 2:** add **sensing**, so it can follow a line and react to what it sees',
             '**Modules 4 and 5:** the **thinking** gets serious: your robot plans its own route '
             'across a grid and re-plans around obstacles it discovers',
             'By the end, the XRP does all three: a robot by anyone\'s definition',
         ],
         'callout': 'Not a toy: the same robot is used in a college sophomore programming '
                    'course. The tools you learn here are the real ones.',
         'tone': 'teal'},

        {'kind': 'check',
         'question': 'Which of the three traits will you spend most of Module 1 on?',
         'options': ['Sense: reading sensors',
                     'Act: making the robot drive, turn, and draw shapes',
                     'Think: pathfinding algorithms',
                     'None: Module 1 is all theory'],
         'answer': 1,
         'explanation': 'Module 1 is about controlling the motors: driving, turning, shapes. '
                        'Sensing arrives in Module 2, and the heavy thinking (pathfinding) in '
                        'Modules 4 and 5.'},

        {'kind': 'cards', 'title': 'Real-world connections: the three Ds',
         'cards': [
             ('Dirty', 'Sewers & disaster sites',
              'Inspection robots crawl pipes and rubble where people can\'t or shouldn\'t go.'),
             ('Dull', 'Warehouses & factories',
              'Robots move shelves, weld seams, and paint car bodies, thousands of identical '
              'times a day.'),
             ('Dangerous', 'Bombs, reactors, deep space',
              'Bomb-disposal robots, nuclear-plant inspectors, and rovers do the jobs where a '
              'mistake costs a life.'),
         ],
         'notes': 'Robots earn their keep on work that is dirty, dull, or dangerous for people.'},

        {'kind': 'wrapup',
         'questions': [
             'What three things must a robot do?',
             'Why isn\'t a remote-controlled plane a robot?',
             'Name a device at home and argue whether it\'s a robot, using all three traits.',
         ],
         'next': 'meet the XRP: its parts, XRP Code, and your first program',
         'notes': 'Answers: sense, think, act. The person does the sensing and thinking. '
                  'Formative check: can students give a reason, not just a vote, for each '
                  'device, and map it onto sense, think, act? Exit ticket: "Pick any device in '
                  'your house. Is it a robot? Defend your answer using all three traits." Look '
                  'for the spectrum idea: "it senses and acts but doesn\'t really decide '
                  'anything."'},
    ],
}
