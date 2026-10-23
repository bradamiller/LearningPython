# robot.py after Lesson 5-2 (function track): every skeleton
# through Lesson 5-2 pasted in, nothing written yet.

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
# the robot is on a crossing line. Lesson 2-9 adds the
# functions that park on the cross and turn to the next line.

def track_to_intersection():
    # until is_at_cross():
    #     correction = get_error() * KP
    #     steer with arcade(BASE_EFFORT, -correction)
    # then stop the motors
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
    # follow to the cross, turn around, follow back to it
    track_to_intersection()
    drivetrain.turn(180)
    track_to_intersection()
    print("Done!")

# --- Lesson 2-9: park on the cross, turn to the next line ---
# Completes the driving toolkit begun in Lesson 2-5.
# track_to_intersection() stops with the SENSORS on the cross;
# drive_past_intersection() moves the WHEELS onto it. The two
# turns spin until a LINE SENSOR function sees the next line,
# so no turn depends on a timer. With these four, every
# program from here to Module 5 is a list of calls to this
# section.
TURN_EFFORT = 0.25       # spin speed during a turn

def drive_past_intersection():
    # drive straight forward by exactly the sensor-to-axle
    # distance
    pass

def turn_clockwise():
    # 1. blind turn, about 60 deg: get BOTH sensors off this line
    # 2. keep spinning in place (no forward speed, only turn)
    # 3. wait until a sensor sees a line
    # 4. stop
    pass

def turn_counterclockwise():
    # the mirror image: same four moves, opposite direction
    pass

def test_park():
    # follow to the cross, then put the wheels on it
    track_to_intersection()
    drive_past_intersection()

def test_turn():
    # park on the cross, then turn until a sensor finds a
    # line: on the circle, that is all the way around
    track_to_intersection()
    drive_past_intersection()
    turn_clockwise()

def test_course():
    # follow, park, turn around, follow the circle back to
    # the cross: the whole lesson in four calls
    track_to_intersection()
    drive_past_intersection()
    turn_clockwise()
    track_to_intersection()
    print("Done!")

# --- Lesson 2-10: final project ---
# The module project: lap the circle, reversing at the cross,
# four times, then stop. Nothing new is defined for it. It is
# a list of calls to the four driving functions above, which
# is the point: the sections did the work, the project
# assembles them.

def test_reversal():
    # park on the cross, turn around (one clockwise turn
    # does it here), then follow back to the cross
    pass

def test_final_project():
    # the mission: follow to the cross, park on it, reverse,
    # four times in all; then stop and print "Done!"
    # write your plan here as comments first, then the code
    pass


# ===== GRID DRIVING =====
# Drives the taped grid one intersection at a time, using only
# the LINE TRACKING functions: a grid intersection is the
# cross from Module 2. To ARRIVE at an intersection is
# track_to_intersection() then drive_past_intersection(); a
# turn happens parked on one. Nothing here touches a sensor.

def test_first_intersection():
    # from a line, arrive at the next intersection and say so
    pass

def test_arrive_and_turn():
    # arrive at the intersection, then turn right onto the
    # crossing line
    pass

# --- Lesson 3-2: a run of intersections ---
# drive_intersections(count) is the arrival pair in a loop.
# It ends parked on the count-th intersection, so Lessons 3-3
# and 3-4 build every path out of it and the two turns.

def drive_intersections(count):
    """Arrive at count intersections in a row, printing
    which one it is each time. Ends parked on the last one
    with the sensors past it, ready to turn or to go on."""
    pass

def test_two_by_hand():
    # the arrival pair written out twice, no loop: the robot
    # should end parked on the SECOND intersection
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
# drive to, across first and then up or down. Pure arithmetic --
# nothing in here touches a sensor or a motor, so every test
# in this section runs on screen with the robot sitting still.

def compute_manhattan_path(position, destination):
    """Compute a Manhattan path from position to destination.

    position:    an (x, y) tuple -- where the robot is now
    destination: an (x, y) tuple -- where it needs to go

    Returns a list of (x, y) tuples the robot should move to,
    not including position itself.
    """
    # 1. path = [] ; unpack start and end into x and y numbers
    # 2. east loop: while x is short of the end x,
    #    step x by one and append the new position
    # 3. north loop: the same for y
    # 4. return path
    pass

# --- Lesson 4-6: the test harness ---
# run_test() asks the planner for a path and compares it
# with one you traced by hand, printing PASS or FAIL. A
# planner test from here on is a list of run_test() calls.

def run_test(test_name, position, destination, expected):
    """Plan position -> destination and compare the result
    with expected; print test_name with PASS or FAIL."""
    pass


# ===== NAVIGATOR =====
# Drives a planned path. The MANHATTAN PLANNER section says
# WHERE to go (a list of intersections); this section works
# out which way to face at each one and does the driving with
# the LINE TRACKING functions. It is the only code that knows
# the robot's position and heading, and it hands both back.
HEADING_NAMES = ["N", "E", "S", "W"]    # HEADING_NAMES[2] -> "S"

def desired_heading(position, next_pos):
    """Return the heading (0-3) that points from position to
    next_pos, which must be one step away; raise if it is not."""
    # 1. x_diff and y_diff: next_pos minus position
    # 2. one if per direction, from the table above; each
    #    checks BOTH differences, because the other one is 0
    # 3. none matched: raise ValueError, naming both positions
    pass

# --- Lesson 4-8: turn to a heading, drive a path ---
# turn_to() turns a quarter turn at a time, with the LINE
# TRACKING turns, until the robot faces the heading it
# needs. drive_path() is the loop: for each
# intersection, face it, arrive with the track-then-drive-past
# pair, and record the new position. Both hand back what they
# changed, because the caller keeps the only record.

def turn_to(heading, desired):
    """Turn clockwise a quarter turn at a time until heading
    is desired; return the new heading."""
    # while heading is not desired:
    #     one turn_clockwise()
    #     heading goes up by 1, wrapping 3 back to 0
    # return heading
    pass

def drive_path(path, position, heading):
    """Turn and drive through every intersection in path, from
    position facing heading; return the final (position, heading)."""
    # for each next_pos in path:
    #     1. needed = desired_heading(position, next_pos)
    #     2. heading = turn_to(heading, needed)
    #     3. arrive: track_to_intersection(), then
    #        drive_past_intersection()
    #     4. position = next_pos -- the robot is there now
    # return position, heading
    pass

def test_drive_path():
    position = (0, 0)
    heading = 0                   # facing North
    destination = (2, 3)

    path = compute_manhattan_path(position, destination)
    print("Path:", path)

    board.wait_for_button()       # read the path, THEN press

    position, heading = drive_path(path, position, heading)
    print("Arrived at:", position, "facing", HEADING_NAMES[heading])

# --- Lesson 4-9: final project, the delivery run ---
# The module project: visit DESTINATIONS in order, planning
# each leg with the MANHATTAN PLANNER from wherever the last
# leg ended and driving it with the NAVIGATOR. Nothing new is
# defined; the two sections did the work.
DESTINATIONS = [(2, 0), (2, 3), (0, 3), (0, 0)]

def test_delivery_paper():
    # no robot: from (0, 0), plan the path to each destination
    # in turn, print it with its step count, and move
    # position on to that destination for the next leg
    pass

def test_delivery():
    # position and heading start at home, facing North
    # plan the FIRST leg and print it; wait for the button
    # for each destination:
    #     compute the path from where the robot is
    #     print it
    #     drive it
    #     ... and keep position and heading up to date
    #     print where the robot arrived
    pass


# ===== GRID GRAPH =====
# The grid as a graph, in a dictionary: every intersection is
# a key, and its value is the list of neighbors it is joined
# to. The BFS PLANNER searches this graph. Starts with the
# open grid; Lesson 5-4 adds the blocked list, so a blocked
# intersection is neither a key nor anyone's neighbor.
ROWS = 4                 # the grid is ROWS x COLS intersections
COLS = 4

def build_grid_graph(rows, cols):
    """Return the open grid as a dictionary: every (x, y)
    maps to the list of its on-grid neighbors."""
    # 1. graph = {}
    # 2. for every x, for every y:
    #       neighbors = []
    #       left, right, down, up: append each one that is
    #       still on the grid (a bounds check for each)
    #       graph[(x, y)] = neighbors
    # 3. return graph
    pass

def remove_blocked(graph, blocked_nodes):
    """Take every node in blocked_nodes out of graph: delete
    its key AND drop it from every other node's neighbors."""
    # 1. for each blocked node that is in graph: del its key
    # 2. for each node still in graph: replace its neighbor
    #    list with one that leaves the blocked nodes out
    # 3. return graph
    pass

# ===== RUN =====
board.wait_for_button()
# call ONE test function here
