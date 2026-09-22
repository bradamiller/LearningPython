#!/usr/bin/env python3
"""
One-shot: insert the TODO markers recorded in REVIEW-2026-09-21.md into the
lessons they belong to. Kept in the repo as the record of what was placed and
where, and as a template if a later review pass wants to do the same thing.

A TODO is an MDX comment, so it is invisible in the rendered page and never
reaches a student. `npm run todos` lists them. Format:

    TODO(category): what is wrong — what to do about it. [REVIEW §N]

Categories: bug, blocked, answers, convention, media.
Keep braces and backticks out of the comment body — a bare brace inside MDX is
parsed as a JSX expression and breaks the build.
"""
import pathlib
import sys

D = pathlib.Path('docs')

# (file, anchor, todo-text, before/after)
TODOS = [
    # ---------------------------------------------------------------- Module 1
    ('module-01-driving/lesson-08-hello-python.mdx',
     '## The same program, two ways',
     'TODO(convention): none of this lesson\'s Python examples call board.wait_for_button(), '
     'so a student uploading one gets a robot that drives immediately. Add it to every '
     'runnable program here and in L1-10 through L1-12. [REVIEW §4]', 'before'),

    ('module-01-driving/lesson-07-blockly-challenges.mdx',
     '## Real-world connections',
     'TODO(convention): this lesson has no Real-world connections section. Every '
     'non-capstone lesson has one. [REVIEW §4]', 'before'),

    ('module-01-driving/lesson-10-python-loops.mdx',
     '## The Repeat block, in text',
     'TODO(convention): the Python programs in this lesson do not call '
     'board.wait_for_button(). Same fix as L1-8. [REVIEW §4]', 'before'),

    ('module-01-driving/lesson-11-python-functions.mdx',
     '## From "to do something" to `def`',
     'TODO(convention): the programs here do not call board.wait_for_button(). [REVIEW §4]',
     'before'),

    ('module-01-driving/lesson-12-python-final-project.mdx',
     '## The mission',
     'TODO(convention): the project skeleton does not call board.wait_for_button(). [REVIEW §4]',
     'before'),

    ('module-01-driving/lesson-06-differential-drive.mdx',
     '## Real-world connections',
     'TODO(media): the motor photos in this lesson show a VEX-style robot, not an XRP. '
     'Re-shoot with an XRP when convenient.', 'before'),

    # ---------------------------------------------------------------- Module 2
    ('module-02-line-tracking/lesson-05-proportional-control.mdx',
     '## From error to steering: the gain `Kp`',
     'TODO(blocked): Kp is capitalized here and in L2-6 and L2-7, but L2-9 and L2-10 use '
     'self.kp. L1-9 now teaches snake_case for variables and Capitalized for classes, so '
     'the bare Kp breaks the course\'s own rule. Brad to decide: rename to kp throughout, '
     'or keep Kp and add a line saying control gains are conventionally capitalized in '
     'engineering. Either way the split has to go. [REVIEW §4]', 'before'),

    ('module-02-line-tracking/lesson-05-proportional-control.mdx',
     'if loop_count % 50 == 0:',
     'TODO(bug): loop_count is defined nowhere in this module, so a student who pastes '
     'this in as instructed gets a NameError on the first pass. Either add a counter to '
     'the control loop above or print every pass. [REVIEW §1.7]', 'before'),

    ('module-02-line-tracking/lesson-05-proportional-control.mdx',
     '## Activity · Tuning Kp',
     'TODO(answers): the tuning outcomes are stated right under this heading, before '
     'students touch the robot, and the check below then asks exactly that. Move the '
     'too-high / too-low results into a Reveal with a hint. [REVIEW §3]', 'after'),

    ('module-02-line-tracking/lesson-06-two-sensor-following.mdx',
     '  placeholderLabel="Diagram — two sensors straddling a line, centered vs. drifted left vs. drifted right"',
     'TODO(media): still a placeholder. This diagram matters more than most — the drift '
     'direction was taught backwards here until 2026-09-22, and a picture is what stops it '
     'being re-introduced. Show the line off to one side and the robot on the other.', 'before'),

    ('module-02-line-tracking/lesson-07-detecting-intersections.mdx',
     '## Activity · Follow, reverse, and count',
     'TODO(answers): the challenge below prints its own complete 19-line solution '
     'immediately under the words that pose it. Move the program into a TeacherNote — it '
     'is work students hand in. [REVIEW §3]', 'after'),

    ('module-02-line-tracking/lesson-08-introduction-to-classes.mdx',
     '## What a class is',
     'TODO(convention): this is the only lesson in the whole course with no Activity '
     'section, so it has no hand-in work and contributes nothing to the pacing guide\'s '
     'activity count. The nearest thing is a sentence buried in the prose about testing '
     'with a loop that prints the error. [REVIEW §4]', 'before'),

    ('module-02-line-tracking/lesson-09-object-composition.mdx',
     '        self.kp = 0.5',
     'TODO(convention): base_effort is 0.4 here and in L2-10, but 0.3 in L2-5 through L2-7, '
     'with no comment on the change — and L2-5\'s teacher note tells teachers to start '
     'everyone at 0.3. Pick one value or explain the jump. [REVIEW §4]', 'before'),

    ('module-02-line-tracking/lesson-09-object-composition.mdx',
     'board = Board.get_default_board()',
     'TODO(bug): Board is never imported in this lesson, so this main program does not run '
     'as printed. Every other lesson in the module imports it. [REVIEW §1.7]', 'before'),

    # ---------------------------------------------------------------- Module 3
    ('module-03-grid-driving/lesson-01-introduction-to-the-grid.mdx',
     'the same tape as the circle, the Lesson 3-1 threshold from Module 2 still applies; if',
     'TODO(bug): "the Lesson 3-1 threshold from Module 2" is self-contradictory — L3-1 is '
     'this lesson, and the threshold was taught in Module 2. Looks like a bad renumber; '
     'should point at Lesson 2-1. [REVIEW §1.7]', 'before'),

    ('module-03-grid-driving/lesson-03-turning-on-the-grid.mdx',
     '## No clearing after a turn',
     'TODO(blocked): this whole section rests on a claim that is false in the source — '
     'LineTrack.turn_right() is set_effort(0.3, -0.3), a spin in place with no forward '
     'travel, so it does NOT drive the robot off the intersection. Whether that actually '
     'breaks the path programs depends on sensor spacing and cross geometry, which needs a '
     'robot on a real grid to settle. Do not reword this until it has been tested; the same '
     'claim is repeated in L3-4 and M4 L8. [REVIEW §1.2]', 'before'),

    ('module-03-grid-driving/lesson-04-final-project.mdx',
     'Notice there\'s no separate clear before `turn_right()` — the turn clears the corner',
     'TODO(blocked): repeats the turn_right clearing claim — see the TODO in L3-3. Settle it '
     'on a robot first. [REVIEW §1.2]', 'before'),

    ('module-03-grid-driving/lesson-04-final-project.mdx',
     '<Reveal title="Compare with a working version" hint="write yours first">',
     'TODO(answers): this Reveal holds the module\'s graded final project. Project code is '
     'tier-b — it belongs in a TeacherNote, where students cannot open it. [REVIEW §3]',
     'before'),

    ('module-03-grid-driving/lesson-02-driving-multiple-intersections.mdx',
     '## Activity · Package it as a helper',
     'TODO(answers): the activity prints the finished helper function immediately after '
     'asking students to write it. [REVIEW §3]', 'after'),

    # ---------------------------------------------------------------- Module 4
    ('module-04-manhattan/lesson-00-overview.mdx',
     '## Two classes, two jobs',
     'TODO(convention): this lesson has no Activity and no Real-world connections section. '
     'It is an overview, so that may be deliberate — but it is the only non-capstone lesson '
     'without either. [REVIEW §4]', 'before'),

    ('module-04-manhattan/lesson-01-coordinates.mdx',
     '## Activity · Map it',
     'TODO(answers): three problems here have no answers anywhere in the lesson, the line '
     'above hands one of them over in prose, and the knowledge check directly below is the '
     'same question as the second bullet with the rule spelled out in its explanation. Give '
     'the activity a Reveal and move the check, or reword it. [REVIEW §3]', 'after'),

    ('module-04-manhattan/lesson-02-tuples.mdx',
     'gives a *negative* distance — acknowledge it\'s real and say Lesson 4-4 fixes it with',
     'TODO(bug): L4-4 never uses abs() — it solves negative distances with four while loops '
     'and explicitly rejects the abs approach. This tells teachers to promise something the '
     'next lesson does not deliver. [REVIEW §1.7]', 'before'),

    ('module-04-manhattan/lesson-04-the-manhattan-algorithm.mdx',
     '## Activity · The edge cases',
     'TODO(answers): all three edge-case answers are printed as inline comments in the code '
     'students are asked to trace. [REVIEW §3]', 'after'),

    ('module-04-manhattan/lesson-07-the-challenge-of-turning.mdx',
     '## Turning with a while loop',
     'TODO(bug): desired_heading above has no final return, so any pair of positions that is '
     'not orthogonally adjacent silently yields None — and turn_to then loops forever, since '
     'self.heading never equals None. Add a fallback, or state that the planner guarantees '
     'adjacency. Same gap in the L4-8 version. [REVIEW §1.7]', 'before'),

    ('module-04-manhattan/lesson-08-navigator-class.mdx',
     'When the robot needs to **turn**, `turn_right()` already drives it off the current',
     'TODO(blocked): same turn_right clearing claim as M3 L3 — and drive_path above is built '
     'on it, clearing only in the straight-ahead case. If the premise is wrong, every turn '
     'leg needs clearing too. Needs a robot on a grid. [REVIEW §1.2]', 'before'),

    ('module-04-manhattan/lesson-08-navigator-class.mdx',
     '        self.line_track.drivetrain.straight(8)   # clear the intersection',
     'TODO(convention): this reaches two levels into another object (Navigator to LineTrack '
     'to DifferentialDrive), which contradicts the delegation point this same lesson makes '
     'sixty lines earlier. The 8 is also a bare magic number, and grid spacing is never '
     'specified anywhere in M3 or M4.', 'before'),

    # ---------------------------------------------------------------- Module 5
    ('module-05-dijkstra/lesson-04-dijkstra-class.mdx',
     '## The shared interface',
     'TODO(blocked): the interchangeability claim overstates what the code does. Manhattan '
     'takes one constructor argument and Dijkstra takes two, so this is not a drop-in '
     'replacement; L5-6 calls it a two-line swap but its "before" code uses a variable name '
     'students never wrote; and the position-sync line M4 L9 calls the one everyone misses '
     'appears nowhere in this module. Decide how honest to make the claim. [REVIEW §2]',
     'before'),

    ('module-05-dijkstra/lesson-06-testing-and-swapping.mdx',
     '## Activity · The two-line swap',
     'TODO(bug): the "before" snippet names the planner pathfinder, but the program students '
     'actually wrote in M4 L9 names it manhattan throughout — so this is not a two-line '
     'change against their own code. It also drops manhattan.position = navigator.position, '
     'which M4 L9 flags as the line nearly everyone misses. [REVIEW §2]', 'after'),

    ('module-05-dijkstra/lesson-09-capstone-project.mdx',
     '            if distance < THRESHOLD:',
     'TODO(bug): THRESHOLD is undefined — L5-7 defines OBSTACLE_THRESHOLD. The loop also '
     'reads the rangefinder BEFORE turning toward next_stop and then blames next_stop for '
     'the reading, so if the next stop is left or right the wrong node gets blocked. And '
     'there is no drive call anywhere in this loop, so the robot never moves. [REVIEW §1.7]',
     'before'),

    ('module-05-dijkstra/lesson-09-capstone-project.mdx',
     '            print("No path to", dest); break',
     'TODO(bug): compute_path returns an empty list both for "already there" and for '
     '"unreachable", so a round trip that ends where it started reports "No path" and skips '
     'its last leg. [REVIEW §1.7]', 'before'),

    ('module-05-dijkstra/lesson-09-capstone-project.mdx',
     '## Activity · Test in simulation, then drive',
     'TODO(answers): the capstone\'s core loop is printed on the student page, and the rubric '
     'below grades the part it hands over. M4 L9 is the model: skeleton for students, working '
     'program in a TeacherNote. [REVIEW §3]', 'after'),

    ('module-05-dijkstra/lesson-09-capstone-project.mdx',
     '## Wrap-up',
     'TODO(convention): the duration chip is 90+ min, and extract_pacing matches digits only, '
     'so the plus is silently dropped and the pacing guide records 90 minutes for a project '
     'this lesson\'s own teacher note says spans 2 to 3 days. Use Multi-day, as M2 L10 does. '
     '[REVIEW §4]', 'before'),

    ('module-05-dijkstra/lesson-07-obstacle-detection.mdx',
     'def get_next_intersection(current_pos, heading):',
     'TODO(bug): no fallback return, so a heading outside 0 to 3 yields None, which then goes '
     'into blocked_list and corrupts it silently. [REVIEW §1.7]', 'before'),
]


def main():
    inserted = missed = 0
    for rel, anchor, todo, where in TODOS:
        path = D / rel
        if not path.exists():
            print(f'MISSING FILE {rel}')
            missed += 1
            continue
        src = path.read_text()
        if anchor not in src:
            print(f'ANCHOR NOT FOUND in {rel}: {anchor[:60]}')
            missed += 1
            continue
        comment = '{/* ' + todo + ' */}'
        if comment in src:
            continue                                   # already placed
        repl = f'{comment}\n\n{anchor}' if where == 'before' else f'{anchor}\n\n{comment}'
        src = src.replace(anchor, repl, 1)
        path.write_text(src)
        inserted += 1
    print(f'inserted {inserted}, missed {missed}')
    return 1 if missed else 0


if __name__ == '__main__':
    sys.exit(main())
