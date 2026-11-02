DECK = {
    'module': 1, 'lesson': 3,
    'doc': 'module-01-driving/lesson-03-introduction-to-functions',
    'title': 'Introduction to Functions',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Explain what a **function** is: a named, reusable block of code',
             'Define a function with the **to do something** block, and say why the **return** '
             'version is not the one you want here',
             'Call your function from the main program',
             'Recognize when a function will make your code shorter and easier to change',
         ],
         'notes': '50 to 60 minutes, still in Blockly. The big idea is reuse: write the square '
                  'code once, give it a name, use it as many times as you like. The whole lesson '
                  'hangs on keeping define and call apart.'},

        {'kind': 'bullets', 'title': 'The copy-paste problem',
         'bullets': [
             'Your square program works. But what if you want **three** squares?',
             'Copying the whole loop again and again gets long and messy fast',
             'Want bigger squares? Change the number in **every** copy, and hope you don\'t miss one',
         ],
         'split': 0.52,
         'figure': [
             {'name': 'repeat', 'note': 'square #1', 'children': [
                 {'name': 'straight', 'note': 'cm: 30'},
                 {'name': 'turn', 'note': 'Deg: 90'},
             ]},
             {'name': 'repeat', 'note': 'square #2, same thing again', 'children': [
                 {'name': 'straight', 'note': 'cm: 30'},
                 {'name': 'turn', 'note': 'Deg: 90'},
             ]},
         ],
         'callout': 'Repetition like this is a signal you want a **function**',
         'tone': 'teal',
         'notes': 'Hook: put the copy-pasted version on the board and ask "what\'s annoying about '
                  'this?" Students land on "it\'s long" and "it\'s hard to change" on their own, '
                  'and that felt need is why functions exist. Recipe-card analogy: write the '
                  'recipe once, cook from it as many times as you want.'},

        {'kind': 'figure', 'title': 'One change of plan, two programs',
         'figure': '/img/lesson-03/copy-paste-vs-function.svg',
         'frame': 0.9,
         'caption': 'Make the squares 40 cm. In the copy-paste version every copy has to be found '
                    'and fixed. In the function version there is only **one place** to look.',
         'notes': 'On the lesson page this is an animation. It opens with both programs drawing '
                  'three 30 cm squares. Then the plan changes to 40 cm: on the left the 30 is '
                  'changed in the first and second loops and the third is missed; on the right it '
                  'is changed once, in the definition, and all three calls pick it up. The slide '
                  'shows the end. Ask what each robot draws now before pointing at the bottom row.'},

        {'kind': 'bullets', 'title': 'Define once, call many times',
         'lead': 'A function has two parts. Keeping them straight is the whole lesson.',
         'bullets': [
             '**Define**: where you **write** what the function does',
             ['The **to do something** block: rename it to `square`, drop your Repeat loop inside'],
             '**Call**: where you **use** it',
             ['A new **square** block appears in the Functions palette. Drag it into your main '
              'program wherever you want a square'],
         ],
         'split': 0.5,
         'figure': [
             {'name': 'function_def', 'note': 'rename to "square"', 'children': [
                 {'name': 'repeat', 'note': 'repeat 4 times', 'children': [
                     {'name': 'straight', 'note': 'cm: 30'},
                     {'name': 'turn', 'note': 'Deg: 90'},
                 ]},
             ]},
         ],
         'callout': 'The definition: the square loop now lives inside a function named `square`',
         'tone': 'teal',
         'notes': 'Recipe card again: the definition is writing the recipe card, the call is '
                  'cooking from it. Writing the card does not make dinner.'},

        {'kind': 'bullets', 'title': 'Two function blocks: take the first one',
         'bullets': [
             'The **Functions** category has two definition blocks that look almost the same',
             'Take the one that says **to do something** and nothing else',
             'The other has a **return** socket on its bottom row. Leave it alone for this whole module',
             ['Its call block is **rounded**: it stands for a **value**, not an action',
              'It only fits a slot where a number or a word belongs, like the cm box on Straight'],
             'Call block rounded and won\'t click into place? Delete it and rebuild with the plain block',
         ],
         'size': 22,
         'split': 0.6,
         'figure': [{'name': 'funct_def_with_return', 'note': 'not this one'}],
         'callout': 'You\'ll use `return` in Lesson 1-11. `square` drives the robot: there\'s '
                    'nothing to hand back, so no return.',
         'notes': 'Name the two blocks out loud when you demo. A handful of students grab the '
                  'return version every year. Everything looks fine until the call block comes '
                  'out rounded and won\'t connect, and they assume they broke something. The blocks '
                  'inside can be dragged out and reused, so rebuilding is quick.'},

        {'kind': 'bullets', 'title': 'The main program gets short',
         'bullets': [
             'Wait for the button, then call `square` as many times as you want',
             'The call block carries no extra wording: it\'s labeled **square**, the name you gave it',
             'Your own functions sit in the palette alongside the built-in ones',
         ],
         'split': 0.5,
         'figure': [
             {'name': 'wait_for_button_press'},
             {'name': 'call_square', 'note': 'the call block is just the function\'s name'},
             {'name': 'call_square'},
             {'name': 'call_square'},
         ],
         'callout': 'Everything about **how** a square gets drawn lives in the definition. The main '
                    'program only says **when**.',
         'tone': 'teal',
         'notes': ('Point out that the call block is labeled square because that is the name students gave '
                  'the function. If a student\'s call block says do something, they never renamed '
                  'the definition.')},

        {'kind': 'check',
         'question': 'What\'s the difference between defining a function and calling it?',
         'options': ['Defining runs the code; calling just names it',
                     'Defining writes what it does; calling runs it in your program',
                     'They are two words for the same thing',
                     'You can only call a function once'],
         'answer': 1,
         'explanation': 'Defining is setup: it doesn\'t move the robot. The function only runs when '
                        'you call it.'},

        {'kind': 'check',
         'question': 'Your program calls square (a 4-sided loop) four times. How many sides does '
                     'the robot drive in total?',
         'options': ['4', '8', '16', '1'],
         'answer': 2,
         'explanation': 'Each call draws 4 sides, and you called it 4 times: 4 × 4 = 16.'},

        {'kind': 'check',
         'question': 'You built your square function, but the call block that appeared is rounded '
                     'and won\'t snap into your main program. What went wrong?',
         'options': ['You used the definition block with a return value instead of the plain one',
                     'The function is empty, so there is nothing to call',
                     'You have to press Run before the block will connect',
                     'Function calls always go inside a Repeat block'],
         'answer': 0,
         'explanation': 'A function with a return value stands for a value, so its call block is '
                        'rounded and only fits where a number belongs. Rebuild the definition with '
                        'the plain "to do something" block.'},

        {'kind': 'bullets', 'title': 'Say it in English first',
         'bullets': [
             'Before you build anything, write one or two plain sentences on paper about what '
             'your function should do',
             'If you can\'t describe it in words, you\'re not ready to build it in blocks',
             'Do the same for `triangle` before step 3',
         ],
         'callout': '"square: repeat 4 times, drive 30 cm, then turn 90°"',
         'tone': 'teal',
         'notes': 'Hold the line on this: no blocks until the sentence is on paper. It is the habit '
                  'that makes the Python lessons later much easier.'},

        {'kind': 'steps', 'title': 'Activity · Build reusable shapes',
         'steps': [
             'Take your square loop from Lesson 1-2 and move it inside a new function named `square`',
             'In the main program, call `square` a few times and watch the robot retrace the same '
             'square each time',
             'Make a second function, `triangle`: Repeat 3, and work the turn angle out with the '
             'rule from Lesson 1-2 rather than looking it up. Call both in a sequence.',
         ],
         'notes': 'More support: give a program with the function already made and ask students '
                  'just to add call blocks. More challenge: a pattern of square, triangle, square, '
                  'triangle from four calls. Watch for students who re-define the function '
                  'instead of calling it; point them to the ready-made square block in the '
                  'Functions palette. A rounded call block that won\'t snap means the return '
                  'version: that is the first thing to check.'},

        {'kind': 'check',
         'question': 'You want bigger squares everywhere in your program. With a square function, '
                     'how many places do you change the size?',
         'options': ['One: just inside the function', 'One for every time you called it',
                     'You have to rewrite the function', 'Two'],
         'answer': 0,
         'explanation': 'That\'s the payoff of a function: fix or change it in one place, and every '
                        'call updates automatically.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Apps', 'Buttons & menus', 'An app defines a "button" once, then reuses it '
                                         'thousands of times across every screen.'),
             ('Games', 'Spawning enemies', 'One "make an enemy" function, called over and over, '
                                           'fills a whole level.'),
             ('Robotics', 'Skill libraries', 'Big robots are built from reusable skills, like '
                                             '"pick up" and "drive to", called in different orders.'),
         ],
         'notes': '"Write it once, use it everywhere" is how all real software is built.'},

        {'kind': 'wrapup',
         'questions': [
             'Why put repeated code in a function?',
             'What are the two parts of using a function?',
             'Does defining a function make the robot move?',
         ],
         'next': 'one function, any size square, with a parameter',
         'notes': 'Answers: write once, reuse, and change it in one place. Define it, then call '
                  'it. No, only calling it does. Formative: can students point at which code '
                  'belongs in the function and which in the main program? Exit ticket: "If square '
                  'draws 4 sides and you call it 3 times, how many sides total?" (12).'},
    ],
}
