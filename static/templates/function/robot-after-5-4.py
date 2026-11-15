# robot.py after Lesson 5-4 (function track): every skeleton
# through Lesson 5-4 pasted in, nothing written yet.

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board
import time
import random

reflectance = Reflectance.get_default_reflectance()
drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()


# ===== LINE SENSOR =====
# Reads the two reflectance sensors and answers questions
# about them. Starts here with the two raw readings; over this
# module it grows to answer "how far off the line am I?" and
# "am I on a line? on a cross?" Nothing in here drives.
# Everything that drives asks these functions instead of the
# hardware.
THRESHOLD = 0.5          # use YOUR value from Lesson 2-1

def get_left():
    # return the left reflectance reading
    pass

def get_right():
    # return the right reflectance reading
    pass

def get_error():
    # return the left reading minus the right reading
    pass

def is_either_on_line():
    # return True when AT LEAST ONE reading is above THRESHOLD
    pass

def is_at_cross():
    # return True when BOTH readings are above THRESHOLD
    pass

def set_threshold(new_value):
    global THRESHOLD
    THRESHOLD = new_value

def test_sensors():
    # prints both readings 50 times, a tenth of a second apart
    for i in range(50):
        print("Left:", get_left(), "  Right:", get_right())
        time.sleep(0.1)

def test_drive_to_line():
    # read the left sensor into a variable
    # while that reading says "white":
    #     drive forward
    #     read the sensor again
    # stop the motors
    # print the reading that ended the loop
    pass

def test_bounce():
    # loop forever:
    #     if the left sensor sees the line:
    #         stop, print a message, turn around
    #     else:
    #         drive forward
    pass

def test_random_bounce():
    # a copy of test_bounce(), with the if branch becoming:
    #     stop
    #     pick a random whole number of degrees, 90 to 270
    #     print it, so you can see each choice
    #     turn by that many degrees
    pass


# ===== LINE TRACKING =====
# Drives the robot along the line using the LINE SENSOR
# functions above. Starts with the proportional follower: read
# the error, scale it by KP, steer with arcade(). Grows over
# the module into following to a cross, parking on it, and
# turning to the next line.
BASE_EFFORT = 0.4        # forward speed while following
KP = 0.5                 # proportional gain -- tune this!

def test_follow():
    # loop forever:
    #     error = get_error()
    #     correction = error times KP
    #     steer: arcade() with BASE_EFFORT and the correction
    #     time.sleep(0.01), so the loop doesn't flood the
    # processor
    pass

def test_sweep():
    # no motors: sweep the robot across the line BY HAND while
    # this runs, and watch error and correction change sign at
    # the edge
    for i in range(500):
        error = get_error()
        correction = error * KP
        if i % 50 == 0:
            print(f"i={i}  error={error:.2f}  correction={correction:.2f}")
        time.sleep(0.02)

# --- Lesson 2-8: follow to a cross ---
# track_to_intersection() is the follower from test_follow()
# with a reason to stop: it follows until is_at_cross() says
# the sensors are on a crossing line, then drives on until
# the robot's center is on it. Lesson 2-9 adds the turns.

def track_to_intersection():
    # until is_at_cross():
    #     correction = get_error() * KP
    #     steer with arcade(BASE_EFFORT, correction)
    # then stop the motors
    # then drive straight 8.75 cm: the robot's center onto
    # the cross
    pass

def test_cross_moving():
    # robot 20-30 cm from a straight line, square on: drive
    # until the cross check fires
    while not is_at_cross():
        drivetrain.set_effort(0.3, 0.3)
    drivetrain.stop()
    print("Cross!")

def test_track():
    # robot on the circle, pointed along it: follow to the
    # cross and stop
    track_to_intersection()
    print("Done!")

def test_reverse():
    # follow to the cross, turn around on it, follow back
    track_to_intersection()
    drivetrain.turn(180)
    track_to_intersection()
    print("Done!")

# --- Lesson 2-9: turn to the next line ---
# Completes the driving toolkit begun in Lesson 2-5.
# track_to_intersection() stops with the robot's center on
# the cross. The two turns spin there until a LINE SENSOR
# function sees the next line, so no turn depends on a
# timer. With these three, every program from here to
# Module 5 is a list of calls to this section.
TURN_EFFORT = 0.25       # spin speed during a turn

def turn_clockwise():
    # 1. blind turn, about 60 deg: get BOTH sensors off this line
    # 2. keep spinning in place (no forward speed, only turn)
    # 3. wait until a sensor sees a line
    # 4. stop
    pass

def turn_counterclockwise():
    # the mirror image: same four moves, opposite direction
    pass

def test_turn():
    # follow to the cross, then turn until a sensor finds a
    # line: on the circle, that is all the way around
    track_to_intersection()
    turn_clockwise()

def test_course():
    # follow, turn around, follow the circle back to the
    # cross: the whole lesson in three calls
    track_to_intersection()
    turn_clockwise()
    track_to_intersection()
    print("Done!")

# --- Lesson 2-10: final project ---
# The module project: lap the circle, reversing at the cross,
# four times, then stop. Nothing new is defined for it. It is
# a list of calls to the three driving functions above, which
# is the point: the sections did the work, the project
# assembles them.

def test_reversal():
    # follow to the cross, turn around (one clockwise turn
    # does it here), then follow back to the cross
    pass

def test_final_project():
    # the mission: follow to the cross, reverse,
    # four times in all; then stop and print "Done!"
    # write your plan here as comments first, then the code
    pass


# ===== GRID DRIVING =====
# Drives the taped grid one intersection at a time, using only
# the LINE TRACKING functions: a grid intersection is the
# cross from Module 2. To ARRIVE at an intersection is
# track_to_intersection(), which stops with the robot's
# center on it; a turn happens parked there. Nothing here
# touches a sensor.

def test_first_intersection():
    # from a line, arrive at the next intersection and say so
    pass

def test_arrive_and_turn():
    # arrive at the intersection, then turn right onto the
    # crossing line
    pass

# --- Lesson 3-2: a run of intersections ---
# drive_intersections(count) is track_to_intersection() in a
# loop.
# It ends parked on the count-th intersection, so Lessons 3-3
# and 3-4 build every path out of it and the two turns.

def drive_intersections(count):
    """Arrive at count intersections in a row, printing
    which one it is each time. Ends parked on the last one
    with the sensors past it, ready to turn or to go on."""
    pass

def test_two_by_hand():
    # track_to_intersection() written out twice, no loop: the
    # robot should end parked on the SECOND intersection
    pass

def test_drive_run():
    # drive_intersections(3), then print that it is done
    pass

# --- Lesson 3-3: turning on the grid ---
# No new function: a path is drive_intersections(), a turn,
# drive_intersections() again. The turn works because the
# helper leaves the wheels parked on the intersection.

def test_l_shape():
    # drive 2 intersections, turn right, drive 2 more, then
    # print that the L is complete
    pass

def test_my_path():
    # the path you planned on paper, one leg per line
    pass

# --- Lesson 3-4: final project, the square ---
# The module project: four sides of SIDE intersections with a
# right turn at every corner, back to the start. Built from
# drive_intersections() and one turn; nothing new is defined.
SIDE = 2                 # intersections per side

def test_one_side():
    # one side of the square: drive SIDE intersections, then
    # turn right
    pass

def test_square():
    # the project. A for loop that runs one side per pass,
    # printing which side it is on; then the finish message
    pass


# ===== MANHATTAN PLANNER =====
# Plans a route across the grid: given where the robot is and
# where it should go, returns the list of (x, y) tuples to
# drive to. Nothing in here touches a sensor or a motor.

def compute_manhattan_path(start, destination):
    """Return the (x, y) steps from start to destination, across
    first, then up or down. The start itself is not in the list."""
    print("computing path from:", start, "to:", destination)
    path = []
    x, y = start              # where the plan is now
    dest_x, dest_y = destination   # where it is going

    # East: keep stepping right until x matches dest_x
    while x < dest_x:
        x = x + 1             # one step right
        path.append((x, y))   # record the new spot

    # West: copy east, flip < to > and + to -

    # North: copy east, but step y until it matches dest_y

    # South: copy north, flip < to > and + to -

    return path

def run_test(test_name, start, destination, expected):
    """Plan start -> destination and compare the result
    with expected; print test_name with PASS or FAIL."""
    actual = compute_manhattan_path(start, destination)
    if actual == expected:
        print(test_name, "- PASS")
    else:
        print(test_name, "- FAIL")
        print("  Expected:", expected)
        print("  Actual:  ", actual)

def test_planner():
    # expected = your answer key, traced by hand
    run_test("Leg 1",       (0, 0), (2, 3), [(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)])
    run_test("Leg 2",       (2, 3), (1, 0), [])   # your answer key
    run_test("Same column", (2, 0), (2, 3), [])   # your answer key
    run_test("Same row",    (0, 2), (3, 2), [])   # your answer key
    run_test("Same spot",   (1, 1), (1, 1), [])   # your answer key


# ===== NAVIGATOR =====
# Drives a planned path, one intersection at a time, and hands
# back where the robot ended up and which way it faces.
HEADING_NAMES = ["N", "E", "S", "W"]    # HEADING_NAMES[2] -> "S"

def get_desired_heading(position, next_pos):
    """Return the heading (0-3) that points from position to
    next_pos, which must be one step away."""
    # 1. unpack position into x, y and next_pos into
    #    next_x, next_y
    # 2. one if per row of the table, each returning its
    #    heading. North is: if next_y > y: return 0
    # 3. (optional) none matched: raise ValueError, naming
    #    both positions -- see "Catching mistakes early"
    pass

def test_headings():
    for next_pos in [(0, 1), (1, 2), (2, 1), (1, 0)]:
        heading = get_desired_heading((1, 1), next_pos)
        print("(1, 1) to", next_pos, ":", heading, HEADING_NAMES[heading])

def turn_to(current_heading, desired_heading):
    """Turn clockwise a quarter turn at a time until
    current_heading is desired_heading; return the new
    heading."""
    # while current_heading is not desired_heading:
    #     turn_clockwise()
    #     current_heading goes up by 1, wrapping 3 back to 0
    # return current_heading
    pass

def fake_track_to_intersection():
    """STUB for track_to_intersection(): print instead of
    driving. Lesson 4-6 swaps in the real one."""
    print("tracking to intersection")

def fake_turn_clockwise():
    """STUB for turn_clockwise(): print instead of
    turning. Lesson 4-6 swaps in the real one."""
    print("turning clockwise")

def drive_path(path, current_position, current_heading):
    """Turn and drive through every intersection in path;
    return the final position and heading."""
    for next_pos in path:
        # 1. desired_heading: which way to face next_pos
        # 2. print("moving: from", current_position, "to:", next_pos,
        #          "heading:", HEADING_NAMES[desired_heading])
        # 3. turn: current_heading = turn_to(...)
        # 4. drive there: track_to_intersection()
        current_position = next_pos     # the robot is there now
    return current_position, current_heading

# --- The main program: the delivery run ---
DELIVERY_STOPS = [(2, 3), (1, 0), (3, 1), (2, 2), (0, 0)]

def test_delivery():
    # 1. robot_position starts at (0, 0); robot_heading
    #    starts at 0, North
    # 2. for each delivery_destination in DELIVERY_STOPS:
    #      plan the path from robot_position, and print it
    #      drive it, and assign the pose it hands back
    #      print "new position:", robot_position,
    #            "heading:", HEADING_NAMES[robot_heading]
    pass


# ===== GRID GRAPH =====
# The grid as a graph, in a dictionary: every intersection is
# a key, and its value is the list of neighbors it is joined
# to. The BFS PLANNER searches this graph. Starts with the
# open grid; Lesson 5-4 adds the blocked list, so a blocked
# intersection is neither a key nor anyone's neighbor.
ROWS = 4                 # the grid is ROWS x COLS intersections
COLS = 4

def build_graph(rows, cols, blocked):
    """Return the grid as a dictionary, leaving out every
    intersection in blocked: not a key, not anyone's neighbor."""
    # 1. graph = {}
    # 2. for every x, for every y:
    #       neighbors = []
    #       left, right, down, up: append each one that is
    #       still on the grid (a bounds check for each)
    #       graph[(x, y)] = neighbors
    # 3. return graph
    pass

# --- Lesson 5-4: the blocked list ---
# BLOCKED is the one record of where the robot must not go.
# add_blocked() is the one way in: tests, the rangefinder and
# you all use it. build_graph() builds AROUND the list, so a
# blocked intersection is never a key and never a neighbor.
BLOCKED = []             # intersections the robot must not drive through

def add_blocked(intersection):
    """Record intersection in BLOCKED, once, even if told twice."""
    pass

def clear_blocked():
    """Empty BLOCKED in place, so a test can start fresh."""
    pass


# ===== BFS PLANNER =====
# The second planner. compute_bfs_path(start, destination)
# has the same shape as the MANHATTAN PLANNER's function and
# keeps the same two promises (told the position; the path
# leaves the start out), but it searches the GRID GRAPH ring
# by ring, so it routes AROUND whatever is in BLOCKED. Pure
# dictionary work: every test here runs with the robot still.

def compute_bfs_path(start, destination):
    """Shortest path from start to destination around
    BLOCKED, as the list of intersections to drive to."""
    graph = build_graph(ROWS, COLS, BLOCKED)      # rebuilt every call
    print("compute_bfs_path is not written yet!")
    return []

# ===== RUN =====
board.wait_for_button()
# call ONE test function here
