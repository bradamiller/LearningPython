DECK = {
    'module': 1, 'lesson': 4,
    'doc': 'module-01-driving/lesson-04-parameters-and-customization',
    'title': 'Parameters & Customization',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Explain what a **parameter** is: an input that changes what a function does',
             'Add a parameter to a Blockly function with the **gear icon** and the mutator bubble',
             'Find that parameter in the **Variables** palette and use its value inside the function',
             'Call one function with different **arguments** to get different results',
         ],
         'notes': '50 to 60 minutes, still in Blockly. The gear-icon step is the one piece of '
                  'Blockly UI nobody discovers on their own, so plan to demo it live and slowly.'},

        {'kind': 'bullets', 'title': 'Same size every time',
         'bullets': [
             'Your `square` function always draws the **same size** square',
             'Want a big one, then a small one? You could write `square_big` and `square_small`...',
             '... but that\'s the copy-paste problem all over again',
         ],
         'callout': 'The fix is a **parameter**: a slot you fill in each time you call the function',
         'tone': 'teal',
         'notes': ('Quick hook. Ask how they would draw a big square and then a small one with what they '
                  'have. Someone will suggest a second function; that is the copy-paste problem from '
                  'Lesson 1-3 coming back.')},

        {'kind': 'bullets', 'title': 'One function, any size',
         'bullets': [
             'A parameter is like a blank in a recipe: not "add 1 cup of sugar" but "add **this '
             'much** sugar"',
             'For `square`, the blank is the side length. We name the parameter `side_length`',
             'The **Straight** block\'s cm slot holds the parameter instead of a fixed number',
             'The call at the bottom fills it in with `35`',
         ],
         'size': 24,
         'split': 0.52,
         'figure': '/img/blocks/programs/square-function.png',
         'notes': 'You decide how much sugar each time you cook. Point at the two places the name '
                  'appears: on the definition (with: side_length) and in the Straight block\'s cm '
                  'slot.'},

        {'kind': 'bullets', 'title': 'One function, three sizes',
         'bullets': [
             'Pass a different value each time you call it',
             'Getting there takes **two moves**:',
             ['**Add** the parameter to the function', '**Use** its value inside the body'],
             'They happen in two different places, so it\'s easy to do one and forget the other',
         ],
         'split': 0.55,
         'figure': [
             {'name': 'call_square_35', 'note': 'medium'},
             {'name': 'call_square_60', 'note': 'big'},
             {'name': 'call_square_20', 'note': 'small'},
         ],
         'callout': 'One function, three sizes. Only the number in the socket changes.',
         'tone': 'teal',
         'notes': ('The two moves are the heart of the lesson: add the parameter with the gear, then use it '
                  'from the Variables palette. Students who do only the first get three identical '
                  'squares. The next slides walk through both.')},

        {'kind': 'video', 'title': 'The whole build, start to finish',
         'video': '/videos/l4-square-parameter.mp4',
         'poster_at': 50,
         'caption': 'Name the function, add the parameter with the gear, build the body in a '
                    'Repeat 4, feed the parameter to Straight, then call it twice: 20 cm and 30 cm.',
         'notes': 'About a minute and a half, no sound, silent by design. Watch it once for the '
                  'shape of it, then work through the steps on the next slides. Project it, pause it '
                  'wherever you want to talk, and run it again. It is also the fastest way to get a '
                  'student who fell behind back to the same place as everyone else.'},

        {'kind': 'bullets', 'title': 'Adding the parameter: the gear icon',
         'lead': 'Top-left corner of your `square` definition: a small blue **gear**. It means '
                 '"this block can change shape".',
         'lead_h': 1.0,
         'size': 22,
         'bullets': [
             '**1 · Click the gear.** A bubble opens with its own tiny workspace',
             ['In the gray strip: **input name: x**. To its right: **inputs**, with an empty notch'],
             '**2 · Drag input name: x into the inputs block**',
             ['The definition behind the bubble grows a row: **with: x**'],
         ],
         'split': 0.56,
         'figure': '/img/lesson-04/mutator-bubble.jpg',
         'callout': 'That\'s your parameter. It already exists, it just has a terrible name.',
         'notes': 'Demo this live and slowly, narrating each move. Students expect a menu or an '
                  '"Add Input" button; instead they drag a block inside another block in a '
                  'floating mini-workspace. Several will drop the input next to the inputs block '
                  'rather than inside it and see nothing happen. The tell: a definition block with '
                  'no with: row.'},

        {'kind': 'bullets', 'title': 'Rename it, then close the bubble',
         'bullets': [
             '**3 · Rename it.** Click the `x`, type `side_length`, press Enter',
             ['Underscores, not spaces: the name you\'d want in Python later (Lesson 1-11)',
              'Keep it short: it rides along on the definition, every call and every variable block'],
             '**4 · Close the bubble** by clicking the gear again',
             ['Your definition now reads **to square with: side_length**'],
         ],
         'size': 26,
         'callout': 'A second parameter? Stack another **input name** underneath. Top to bottom in '
                    'the bubble is left to right in the call, so order matters.',
         'tone': 'teal',
         'notes': 'In the next lesson, polygon (sides, side_length) is not the same function as '
                  'polygon (side_length, sides). In Lesson 1-11 students write this same function '
                  'in text, which is why the name should already be Python-friendly.'},

        {'kind': 'check',
         'question': 'You click the gear on a function block and drag an \'input name\' block into '
                     'the \'inputs\' block. What happens to the function definition?',
         'options': ['Nothing until you press Run',
                     'It grows a "with:" row naming the new parameter',
                     'The blocks inside the function are deleted',
                     'A new function is created'],
         'answer': 1,
         'explanation': 'The definition block changes shape as soon as the input connects: that '
                        '"with:" row is the parameter list. Renaming the input renames what '
                        'appears there.'},

        {'kind': 'bullets', 'title': 'Using the parameter: the Variables palette',
         'bullets': [
             'The Straight block inside is still set to a hard number, so **nothing has changed yet**',
             'Open **Variables**. Past Create variable and the set and change blocks, there\'s a '
             'rounded **side_length** block',
             'Adding the parameter created it. You don\'t have to make it',
             'Grabbed the wrong one? Switch it from its **dropdown** instead of starting over',
         ],
         'size': 22,
         'split': 0.5,
         'figure': '/img/lesson-04/variables-palette.jpg',
         'callout': 'This workspace has a few half-typed leftovers too: read the name before you drag',
         'tone': 'teal',
         'notes': 'Predictable snag: students rename the input but never visit Variables, so the '
                  'body still uses a fixed number. The function ignores its argument, and every '
                  'call draws the same square.'},

        {'kind': 'bullets', 'title': 'Drop it in, then call it',
         'bullets': [
             'Drag `side_length` into Straight\'s **cm** slot, right on top of the number',
             ['The number isn\'t deleted: it\'s tucked underneath, and comes back if you pull the '
              'variable out'],
             'Use the same parameter as many times as you like inside the function',
             'In **Functions**, the call block now reads **square with: side_length**, with a socket',
             'Drag one out and type `20`, a second and type `30`, and snap them into a stack',
         ],
         'size': 21,
         'split': 0.55,
         'figure': '/img/lesson-04/two-calls.jpg',
         'callout': 'Two sizes, one function. This is the payoff.',
         'tone': 'green',
         'notes': 'Second predictable snag: a student drags the side_length block out of the '
                  'function and into the main program, where it has no value. It only means '
                  'something inside the function that declares it. If a student deletes a '
                  'parameter later, any side_length block left in the body becomes a plain '
                  'variable that is never set: clean those out with them.'},

        {'kind': 'check',
         'question': 'Inside the function body, where do you get a block that holds the '
                     'parameter\'s value?',
         'options': ['The Variables category: the parameter appears there as a rounded block',
                     'The Functions category, next to the call block',
                     'You type its name into the number slot',
                     'You have to make a new variable with the same name'],
         'answer': 0,
         'explanation': 'Adding a parameter creates a variable of the same name, and Blockly lists '
                        'it under Variables. Drag that block into any slot inside the function '
                        'where you want the value.'},

        {'kind': 'bullets', 'title': 'Parameter vs. argument',
         'lead': 'Two words that sound similar and trip everyone up:',
         'bullets': [
             '**Parameter**: the **name** in the definition',
             ['The `side_length` in `square (side_length)`. It\'s the empty slot'],
             '**Argument**: the **value** you pass in when you call it',
             ['The `50` in `square (side_length: 50)`. It\'s what fills the slot'],
         ],
         'callout': 'Parameter = the slot. Argument = what you put in it.',
         'tone': 'teal',
         'notes': ('Keep pointing at the blocks: the parameter lives on the definition, the argument sits in '
                  'the socket of a call. Exit-ticket style question: in square (side_length: 50), '
                  'which word is the parameter and which number is the argument?')},

        {'kind': 'check',
         'question': 'In the call square (side_length: 50), what is the 50?',
         'options': ['The parameter', 'The argument: the value passed in', 'The function name',
                     'The turn angle'],
         'answer': 1,
         'explanation': 'The parameter is the name (side_length) in the definition; the argument '
                        'is the value (50) you pass when calling.'},

        {'kind': 'check',
         'question': 'With square (side_length), calling square (side_length: 35) makes the robot '
                     'drive each side how long?',
         'options': ['90 cm', '35 cm', '4 cm', 'It depends on the effort'],
         'answer': 1,
         'explanation': 'The argument 35 flows into the side_length parameter, so every Straight '
                        'drives 35 cm.'},

        {'kind': 'steps', 'title': 'Activity · Make your functions flexible',
         'steps': [
             'Add a `side_length` parameter to `square` (gear icon, then the Variables palette) and '
             'call it at three sizes. All three identical? Check what\'s in the Straight block\'s cm slot.',
             'Do the same for `triangle`: one function, any size triangle',
             '**Challenge:** add a second parameter, `effort`, for the **Effort** on Straight and '
             'Turn: `square (side_length, effort)`. Does it earn its keep? Next lesson\'s polygon '
             'leaves Effort at `0.5`.',
         ],
         'notes': 'If all three squares come out identical, the student did the first half (add) '
                  'and not the second (use). More support: pair students and have one talk the '
                  'other through the gear sequence without touching the mouse; saying it out loud '
                  'is what makes it stick. More challenge: preview Lesson 1-5 by adding a sides '
                  'parameter and computing the turn as 360 ÷ sides, or add effort and compare the '
                  'robot at 0.3 and 0.8.'},

        {'kind': 'check',
         'question': 'A function is defined as draw rectangle (length, width). Are draw rectangle '
                     '(50, 30) and draw rectangle (30, 50) the same?',
         'options': ['Yes: the numbers are the same',
                     'No: order matters, so length and width are swapped',
                     'Yes: Blockly sorts them',
                     'Only if the robot is turned off'],
         'answer': 1,
         'explanation': 'Arguments fill parameters in order. (50, 30) means length 50 and width 30; '
                        '(30, 50) swaps them into a different rectangle.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Print', 'Print dialog', '"Copies," "paper size," and "color" are parameters: one '
                                       'print function, many outcomes.'),
             ('Games', 'Difficulty settings', 'Easy or hard is a parameter fed into the same game '
                                              'code to change enemy speed and health.'),
             ('Robotics', 'Motion commands', '"Drive to (x, y) at speed s": real robot commands '
                                             'are functions with parameters just like yours.'),
         ],
         'notes': 'Parameters are everywhere you customize something without rebuilding it.'},

        {'kind': 'wrapup',
         'questions': [
             'What does a parameter let one function do?',
             'Parameter vs. argument: which is which?',
             'Why does parameter order matter?',
         ],
         'next': 'one polygon function that draws any regular shape',
         'notes': 'Answers: behave differently each time, based on the value you pass. Parameter = '
                  'the name or slot; argument = the value you pass in. Arguments fill the slots in '
                  'order. Formative: can students add a parameter with the gear, use it in the '
                  'body, and call with different arguments? Exit ticket: "Given triangle '
                  '(side_length), what does triangle (40) drive per side?" (40 cm). Next lesson '
                  'combines a parameter with the 360 ÷ sides math.'},
    ],
}
