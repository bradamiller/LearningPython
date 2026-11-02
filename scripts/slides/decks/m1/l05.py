DECK = {
    'module': 1, 'lesson': 5,
    'doc': 'module-01-driving/lesson-05-polygon-function',
    'title': 'The Polygon Function',
    'slides': [
        {'kind': 'title',
         'objectives': [
             'Combine a loop, a function and parameters to solve one bigger problem',
             'Compute the turn angle **inside** the function with `360 ÷ sides`',
             'Test one function against many shapes (triangle, square, hexagon, octagon...)',
             'Explain how one general function replaces a whole pile of specific ones',
         ],
         'notes': '50 to 60 minutes, still in Blockly. A synthesis lesson: everything from Lessons '
                  '1-2 to 1-4 (loops, functions, parameters, the angle formula) goes into one '
                  'function.'},

        {'kind': 'bullets', 'title': 'This is the big one',
         'bullets': [
             'Loops, functions, parameters and the angle formula, all in **one** function',
             'It draws **any** regular polygon',
             'Tell it how many sides and how long, and it figures out the rest',
         ],
         'callout': 'Every polygon is: repeat N times, drive a side, turn `360 ÷ N`',
         'tone': 'teal',
         'notes': ('A synthesis lesson. Ask students to say the pattern out loud for a square and a '
                  'triangle before showing the function: repeat 4, turn 90; repeat 3, turn 120.')},

        {'kind': 'bullets', 'title': 'One function to draw them all',
         'bullets': [
             'So far each shape needed its own function',
             'Only two things change from shape to shape:',
             ['the number of **sides**', 'the **side length**'],
             'Things that change are perfect for **parameters**',
             'And the angle? The function can calculate it itself',
         ],
         'callout': 'Look for the pattern: what changes becomes a parameter, what can be worked out '
                    'gets computed',
         'tone': 'teal',
         'notes': ('Lead students to name the two things that change themselves. The angle is the twist: it '
                  'changes too, but it can be worked out from sides, so it does not need to be a '
                  'parameter.')},

        {'kind': 'figure', 'title': 'The polygon function',
         'figure': '/img/blocks/programs/polygon-function.png',
         'caption': 'One function draws every regular polygon. The two parameters are `sides` and '
                    '`side_length`; the turn angle is computed from `sides`.',
         'notes': ('Walk the block from the top: the definition with two parameters, the repeat count, the '
                  'Straight cm and the Turn angle. Ask where sides shows up (twice) before the next '
                  'slide says it.')},

        {'kind': 'bullets', 'title': 'The new trick: division in the Turn slot',
         'bullets': [
             'Put a **math division block**, `360 ÷ sides`, right into the Turn block\'s angle slot',
             '`sides` now does **double duty**:',
             ['it sets how many times the loop repeats', 'and it sets the angle'],
             'Not a parameter: **Effort** stays at `0.5` in both blocks',
             ['A parameter earns its place when callers actually need to vary it. `sides` and '
              '`side_length` change with every shape, speed doesn\'t'],
         ],
         'size': 24,
         'notes': 'The one unfamiliar step is Math, then the division block. Have students drag '
                  '360 ÷ [ ] into the Turn angle slot, then drop the sides variable into the blank. '
                  'Point out that sides is used in two places, which is why this single function '
                  'generalizes. Build the square test case first and confirm it works before '
                  'turning students loose on other shapes.'},

        {'kind': 'bullets', 'title': 'Activity · Test it like an engineer', 'tag': 'Activity',
         'bullets': [
             'Real programmers test one function against **many inputs**',
             'In your main program, call `polygon` with different values',
             'Write down what you expect each call to draw **before** you click RUN',
             'Then run it and see whether the robot agrees with you',
             'The arguments fill the sockets **in order**: `sides` first, then `side_length`',
         ],
         'size': 26,
         'split': 0.55,
         'figure': [
             {'name': 'wait_for_button_press'},
             {'name': 'call_polygon_4_30'},
             {'name': 'call_polygon_3_30'},
             {'name': 'call_polygon_6_20'},
             {'name': 'call_polygon_8_15'},
         ],
         'notes': 'Insist on written predictions first. The lesson page has a "Check your '
                  'predictions" reveal with an animation of all four calls: open it only after '
                  'everyone has committed and run their robot. The side lengths shrink as the '
                  'shapes gain sides, because a shape with more sides needs more floor for the '
                  'same side length.'},

        {'kind': 'check',
         'question': 'What turn angle will polygon compute for a 12-sided shape (a dodecagon)?',
         'options': ['12°', '30°', '36°', '90°'],
         'answer': 1,
         'explanation': 'The function calculates 360 ÷ 12 = 30° on its own: no need to work it out '
                        'by hand.'},

        {'kind': 'check',
         'question': 'polygon (8, 25) traces an octagon about 2 m around. What does polygon (8, 50) do?',
         'options': ['A different shape',
                     'The same octagon shape, but about twice as big (~4 m around)',
                     'An octagon at double speed',
                     'Nothing changes'],
         'answer': 1,
         'explanation': 'Doubling side_length doubles each side, so the perimeter doubles. But the '
                        'angles, and therefore the shape, stay the same.'},

        {'kind': 'steps', 'title': 'Activity · Explore',
         'steps': [
             'Run the four test shapes and check each one roughly closes back to its start',
             'Notice what happens as sides go up (10, 12, 20): the shape gets closer and closer to '
             'a **circle**',
             '**Challenge:** draw a pentagon, `Turn 72°`, then draw the pentagon again. The two '
             'overlapping pentagons make a star or mandala.',
         ],
         'notes': 'More support: give a skeleton with the Repeat block already placed and ask only '
                  'for Straight and the 360 ÷ sides Turn. More challenge: a "spiral polygon" that '
                  'grows each side, or a star helper built on top of polygon. When a shape looks '
                  'off: first confirm the math (360 ÷ 6 = 60), then rule out wheel slip by testing '
                  'at effort 0.5. Many "bugs" here are physics, not code.'},

        {'kind': 'check',
         'question': 'Without polygon, you\'d write one function each for square, triangle, '
                     'pentagon, hexagon, and octagon. With polygon, how many functions do you need?',
         'options': ['Five', 'One', 'One per shape you draw', 'Three'],
         'answer': 1,
         'explanation': 'That\'s the power of generalizing: a single well-designed function replaces '
                        'all the special-case ones.'},

        {'kind': 'cards', 'title': 'Real-world connections',
         'cards': [
             ('Software', 'Libraries', 'A charting library draws any chart from parameters: you '
                                       'don\'t write new code for every graph.'),
             ('Design', 'Parametric CAD', 'Engineers define a part once with parameters, then '
                                          'generate every size from the same model.'),
             ('Manufacturing', 'Configurable machines', 'One programmable machine makes many '
                                                        'products by changing inputs, not by '
                                                        'rebuilding the machine.'),
         ],
         'notes': 'Writing one flexible tool instead of many rigid ones is the heart of good '
                  'engineering.'},

        {'kind': 'wrapup',
         'questions': [
             'What two parameters does `polygon` take, and what does each control?',
             'How does the function get the turn angle?',
             'Why is one general function better than many specific ones?',
         ],
         'next': 'under `straight` and `turn`, to control the left and right motors directly',
         'notes': 'Answers: sides (how many times to repeat, and the angle) and side_length (how '
                  'long each side is). 360 ÷ sides, computed inside. Less code, fewer bugs, easier '
                  'to change. Formative: can students explain why sides appears in two places, and '
                  'predict a shape from a call? Exit ticket: "Turn angle for a 9-sided polygon?" '
                  '(360 ÷ 9 = 40°).'},
    ],
}
