# robot.py after Lesson 5-9 (class track): every skeleton
# through Lesson 5-9 pasted in, nothing written yet.

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board
from XRPLib.rangefinder import Rangefinder
import time
import random

reflectance = Reflectance.get_default_reflectance()
drivetrain = DifferentialDrive.get_default_differential_drive()
board = Board.get_default_board()
rangefinder = Rangefinder.get_default_rangefinder()


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
    #     pick a random whole number of degrees between 90 and
    # 270     print it, so you can see each choice     turn by
    # that many degrees
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
    # park on the cross, then turn to the cross street
    tracker.track_to_intersection()
    tracker.drive_past_intersection()
    tracker.turn_clockwise()

def test_course():
    # follow, park, turn, follow: the whole lesson in four
    # calls
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
    # park on the cross, turn around (two clockwise turns),
    # then follow back to the cross
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

    def add_blocked(self, intersection):
        # Manhattan cannot route around obstacles. This exists
        # so every planner can be tested the same way. It
        # deliberately does nothing.
        pass

    def clear_blocked(self):
        pass

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

    def navigate_with_detection(self, destination, rangefinder, obstacle_cm):
        """Drive from self.position (facing self.heading) to
        destination, re-planning around every obstacle the
        rangefinder finds; return (step_count, reroute_count)."""
        # the 5-8 function as a method: self.position and
        # self.heading replace the parameters; the driving
        # goes through self.line_track, self.desired_heading()
        # and self.turn_to(); planner calls stay on planner
        # step_count = 0 ; reroute_count = 0
        # arrived = False
        # while not arrived:
        #     plan from self.position; print the path
        #     if the path is empty: say "No path"; return both
        #     rerouted = False
        #     for each next_pos in path:      -- Lesson 5-7
        #         face it
        #         look ahead with rangefinder.distance()
        #         if closer than obstacle_cm:
        #             planner.add_blocked(next_pos); count it
        #             rerouted = True ; break
        #         else:
        #             arrive; self.position = next_pos; count
        #     if not rerouted: arrived = True
        # return step_count, reroute_count
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


# ===== BFS PLANNER (class version) =====
# One BFS object holds the grid size and ITS OWN blocked list
# and plans around it: compute_path() builds the graph from
# self.blocked on every call. It holds NO position (Rule 1).
# Same names as the function version, with planner. in front.

class BFS:
    def __init__(self, rows=4, cols=4):
        self.rows = rows
        self.cols = cols
        self.blocked = []

    def add_blocked(self, intersection):
        # your function, with self.blocked for BLOCKED
        pass

    def clear_blocked(self):
        # self.blocked = []  -- a method assigns to an
        # attribute freely; no global, no pop loop
        pass

    def compute_path(self, position, destination):
        # your compute_bfs_path(), with
        # build_graph(self.rows, self.cols, self.blocked)
        pass

planner = BFS()

def bfs_rings(position):
    """Ring number of every intersection reachable from
    position, as a dictionary -- the search with no break."""
    # the SETUP and SEARCH of planner.compute_path, with two
    # changes: never stop early, and instead of came-from,
    # write the ring number: one more than current's
    pass

def print_grid(rows, cols, blocked, numbers):
    """Draw the grid the way it lies in front of you: the top
    line is the far row, y = 0 is the bottom line. Each
    intersection shows its entry in numbers, X if it is
    blocked, . if it has no entry."""
    for i in range(rows):
        y = rows - 1 - i
        line = " " + str(y) + " | "
        for x in range(cols):
            if (x, y) in blocked:
                cell = "X"
            elif (x, y) in numbers:
                cell = numbers[(x, y)]
            else:
                cell = "."
            line = line + "{:>3}".format(cell)
        print(line)
    print("    " + "-" * (3 * cols + 1))
    footer = "     "
    for x in range(cols):
        footer = footer + "{:>3}".format(x)
    print(footer)

# --- Lesson 5-6: the property harness ---
# Tests any planner by what must be true of its path, not by
# one expected list, because BFS has many right answers.
# run_all_tests() is handed a planner FUNCTION and runs the
# six cases through it: one program tests Manhattan and BFS.
# Module 4's run_test() stays; exact match is right there.
HARNESS_BLOCKED = []

def block(planner, intersection):
    """Tell planner about intersection AND note it in
    HARNESS_BLOCKED, so check_path() can see it."""
    pass

def clear(planner):
    """Tell planner to forget its blocks, and forget ours."""
    pass

def manhattan_distance(a, b):
    """Steps between a and b with nothing in the way."""
    pass

def is_neighbor(a, b):
    """True when a and b are one step apart."""
    pass

def check_path(path, position, destination):
    """Return a list of everything wrong with path as a route
    from position to destination; [] means it is good."""
    # problems = []
    # an empty path is fine only if already there; return
    # 1. first step next to the start?
    # 2. last step the destination?
    # 3. every step next to the one before it?
    # 4. no step in HARNESS_BLOCKED?
    # return problems
    pass

def run_path_test(test_name, planner, position, destination, expected_steps):
    """Ask planner for a path, check the five properties, print
    PASS or FAIL with the path; return True on a pass."""
    # path = planner.compute_path(position, destination)
    # problems from check_path(), plus 5. the step count
    # no problems: print "  PASS ", test_name, "", path
    # otherwise: print "  FAIL " the same way, then each
    # problem on its own line, "          - " in front
    pass

def run_no_path_test(test_name, planner, position, destination):
    """For a walled-off destination the only right answer is
    []; print PASS or FAIL and return True on a pass."""
    pass

def run_all_tests(name, planner):
    """The six cases, through whichever planner is handed in:
    four on the open grid, the wall, and walled off."""
    print("==========", name, "==========")
    passed = 0
    clear(planner)
    if run_path_test("open (0, 0) to (3, 3)", planner, (0, 0), (3, 3), 6):
        passed = passed + 1
    if run_path_test("open (0, 0) to (0, 3)", planner, (0, 0), (0, 3), 3):
        passed = passed + 1
    if run_path_test("open (2, 1) to (0, 3)", planner, (2, 1), (0, 3), 4):
        passed = passed + 1
    if run_path_test("open (1, 1) to (1, 1)", planner, (1, 1), (1, 1), 0):
        passed = passed + 1
    block(planner, (1, 0))
    block(planner, (1, 1))
    if run_path_test("wall at (1,0),(1,1): (0,0) to (3,0)", planner, (0, 0), (3, 0), 7):
        passed = passed + 1
    block(planner, (1, 2))
    block(planner, (1, 3))
    if run_no_path_test("walled off: (0,0) to (3,0)", planner, (0, 0), (3, 0)):
        passed = passed + 1
    clear(planner)
    print(name + ":", passed, "of 6 passed")

def navigate(planner, position, destination):
    """Plan with planner and print the path; return
    destination, where the robot would be after driving it."""
    path = planner.compute_path(position, destination)
    print("  Path from", position, "to", destination, ":", path, " Steps:", len(path))
    return destination


# ===== OBSTACLES =====
# The robot fills BLOCKED itself. Before each step of a path
# the rangefinder looks at the intersection ahead; if there is
# something, add_blocked() tells the BFS PLANNER (the call the
# 5-6 harness made) and a new path is planned from where the
# robot stands. Facing and driving are the NAVIGATOR's job.
OBSTACLE_CM = 15                         # closer than this = blocked
SIMULATED_OBSTACLES = [(2, 0), (2, 2)]   # pretend boxes, for a dry run

def simulate_rangefinder(next_pos):
    """Stand-in for rangefinder.distance(): 8.0 if next_pos is
    in SIMULATED_OBSTACLES, otherwise 50.0."""
    pass

def test_detect_once():
    # the navigator at (0, 0) facing North; destination (3, 3)
    # plan the path, print it, wait for the button
    # for each next_pos in path:
    #     face it: navigator.desired_heading(), then
    #         navigator.turn_to()
    #     NEW: look ahead -- distance = simulate_rangefinder(
    #          next_pos) for now; rangefinder.distance() later
    #     print navigator.position, its heading, the distance
    #     if distance < OBSTACLE_CM:
    #         tell the planner: planner.add_blocked(next_pos)
    #         new path from HERE: planner.compute_path(
    #             navigator.position, destination); print it;
    #             then break
    #     else:
    #         arrive: navigator.line_track.
    #             track_to_intersection(), then
    #             drive_past_intersection()
    #         navigator.position = next_pos
    # print the blocked list, planner.blocked
    pass

# --- Lesson 5-8: re-plan until you arrive ---
# navigate_with_detection() is the 5-7 loop inside a while:
# plan, follow, and if something got in the way, plan again
# from here, until a whole path is driven with no reroute. It
# hands back position and heading, as drive_path() does, plus
# the step and reroute counts. KNOWN_OBSTACLES is what the
# last run found, typed in by you: memory between runs.
KNOWN_OBSTACLES = []     # what the last run printed; empty on Run 1

# --- Lesson 5-9: capstone, the delivery run ---
# The module project: visit CAPSTONE_DESTINATIONS in order,
# each leg with navigate_with_detection(), starting from what
# the last run found (KNOWN_OBSTACLES) and printing what this
# run found for the next one. Nothing new is defined; the
# sections above did the work, and this test connects them.
CAPSTONE_DESTINATIONS = [(1, 3), (3, 3), (3, 0), (0, 0)]

def test_capstone_paper():
    # no robot: hand KNOWN_OBSTACLES to planner.add_blocked(), then
    # from (0, 0) plan each leg with the BFS planner, print it
    # with its step count, and move position on to that
    # destination for the next leg
    pass

def test_capstone():
    # 1. hand KNOWN_OBSTACLES to planner.add_blocked()
    #    (empty on Run 1, last run's list on Run 2)
    # 2. the navigator starts at (0, 0) heading 0; totals at 0
    # 3. print the plan for leg 1; wait for the button
    # 4. for each destination, with its leg number:
    #        navigator.navigate_with_detection() -- plan,
    #        follow, re-plan until arrived (Lesson 5-8); the
    #        navigator keeps position and heading itself
    #        add its steps and reroutes to the totals
    # 5. print planner.blocked -- what you type in next run
    # 6. print the totals: steps, reroutes
    pass

# ===== RUN =====
board.wait_for_button()
# call ONE test function here
