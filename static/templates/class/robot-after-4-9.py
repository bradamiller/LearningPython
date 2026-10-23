# robot.py after Lesson 4-9 (class track): every skeleton
# through Lesson 4-9 pasted in, nothing written yet.

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board
import time
import random

reflectance = Reflectance.get_default_reflectance()
drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()


# ===== LINE SENSOR (Lesson 2-7, class version) =====
# One LineSensor object owns the reflectance sensor and its
# threshold, and answers questions about the line: how far off
# it we are (get_error) and whether we are on a cross or on a
# line at all. Nothing in here drives. Everything that drives,
# from the next lesson on, asks this object.

class LineSensor:
    def __init__(self):
        self.reflectance = Reflectance.get_default_reflectance()
        self.threshold = 0.5

    def get_left(self):
        pass

    def get_right(self):
        pass

    def get_error(self):
        pass

    def is_at_cross(self):
        pass

    def is_either_on_line(self):
        pass

sensor = LineSensor()

def test_sensors():
    # prints both readings 50 times, a tenth of a second apart
    for i in range(50):
        print("Left:", sensor.get_left(), "  Right:", sensor.get_right())
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


# ===== LINE TRACKING (class version) =====
# One LineTrack object drives the robot along the line. It HAS
# A LineSensor (built in __init__, so you never make one
# separately) and asks it the questions; it HAS the drivetrain
# and gives it the orders. Same four methods as the function
# version, same names, with tracker. in front.

class LineTrack:
    def __init__(self):
        self.sensor = LineSensor()           # has-a LineSensor
        self.drivetrain = DifferentialDrive.get_default_differential_drive()
        self.base_effort = 0.4
        self.kp = 0.5
        self.turn_effort = 0.25

    def track_to_intersection(self):
        # your function, with self. in front of the sensor,
        # the drivetrain and the settings
        pass

    def drive_past_intersection(self):
        pass

    def turn_clockwise(self):
        pass

    def turn_counterclockwise(self):
        pass

tracker = LineTrack()

def test_follow():
    # loop forever:
    #     error = sensor.get_error()
    #     correction = error times tracker.kp
    #     steer: arcade() with tracker.base_effort and the correction
    #     time.sleep(0.01), so the loop doesn't flood the
    # processor
    pass

def test_sweep():
    # no motors: sweep the robot across the line BY HAND while
    # this runs, and watch error and correction change sign at
    # the edge
    for i in range(500):
        error = sensor.get_error()
        correction = error * tracker.kp
        if i % 50 == 0:
            print(f"i={i}  error={error:.2f}  correction={correction:.2f}")
        time.sleep(0.02)

def test_cross_moving():
    # robot 20-30 cm from a straight line, square on: drive
    # until the cross check fires
    while not sensor.is_at_cross():
        drivetrain.set_effort(0.3, 0.3)
    drivetrain.stop()
    print("Cross!")

def test_track():
    # robot on the circle, pointed along it: follow to the
    # cross and stop
    tracker.track_to_intersection()
    print("Done!")

def test_reverse():
    # follow to the cross, turn around, follow back to it
    tracker.track_to_intersection()
    drivetrain.turn(180)
    tracker.track_to_intersection()
    print("Done!")

def test_park():
    # follow to the cross, then put the wheels on it
    tracker.track_to_intersection()
    tracker.drive_past_intersection()

def test_turn():
    # park on the cross, then turn until a sensor finds a
    # line: on the circle, that is all the way around
    tracker.track_to_intersection()
    tracker.drive_past_intersection()
    tracker.turn_clockwise()

def test_course():
    # follow, park, turn around, follow the circle back to
    # the cross: the whole lesson in four calls
    tracker.track_to_intersection()
    tracker.drive_past_intersection()
    tracker.turn_clockwise()
    tracker.track_to_intersection()
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


# ===== MANHATTAN PLANNER (class version) =====
# One Manhattan object plans routes on the grid, across
# first and then up or down. It holds NO state: compute_path()
# is told the robot's position every call. Pure arithmetic.

class Manhattan:
    """The Lesson 4-5 planner as a class.

    It holds NO state: compute_path() is told the robot's position
    every time. Manhattan is a class only so that it has the same
    shape as the Module 5 and 6 planners (BFS, Dijkstra) -- then one
    main program and one test harness work with any of them by
    changing one name.
    """

    def __init__(self):
        pass        # nothing to set up

    def compute_path(self, position, destination):
        # your compute_manhattan_path(), unchanged: nothing in
        # it needs self., because the planner holds nothing
        pass

planner = Manhattan()

# --- Lesson 4-6: the test harness ---
# run_test() asks the planner for a path and compares it
# with one you traced by hand, printing PASS or FAIL. A
# planner test from here on is a list of run_test() calls.

def run_test(test_name, position, destination, expected):
    """Plan position -> destination and compare the result
    with expected; print test_name with PASS or FAIL."""
    pass


# ===== NAVIGATOR (class version) =====
# One Navigator object owns the robot's position and heading.
# It HAS a LineTrack (built in __init__) and gives it the
# driving orders; it is told where to go and keeps its own
# record of where it got to. Same three methods as the
# function version, same names, with navigator. in front.
HEADING_NAMES = ["N", "E", "S", "W"]    # HEADING_NAMES[2] -> "S"

class Navigator:
    def __init__(self, start, heading):
        self.position = start
        self.heading = heading
        self.line_track = LineTrack()        # has-a LineTrack

    def desired_heading(self, next_pos):
        # your function; position is self.position now, so
        # it is no longer a parameter
        pass

    def turn_to(self, desired):
        # your function, with self.heading in place of the
        # parameter and self.line_track. in front of each
        # turn; it STORES the new heading, not returns it
        pass

    def drive_path(self, path):
        # your function, with self. in front of position,
        # heading and the two LINE TRACKING calls; it stores
        # the final position instead of returning it
        pass

navigator = Navigator((0, 0), 0)

def test_drive_path():
    destination = (2, 3)

    path = planner.compute_path(navigator.position, destination)
    print("Path:", path)

    board.wait_for_button()       # read the path, THEN press

    navigator.drive_path(path)
    print("Arrived at:", navigator.position, "facing", HEADING_NAMES[navigator.heading])

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
    # the navigator starts at home, facing North
    # plan the FIRST leg and print it; wait for the button
    # for each destination:
    #     compute the path from navigator.position
    #     print it
    #     navigator.drive_path(path) -- it keeps the record
    #     print where the navigator arrived
    pass

# ===== RUN =====
board.wait_for_button()
# call ONE test function here
