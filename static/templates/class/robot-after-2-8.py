# robot.py after Lesson 2-8 (class track): every skeleton
# through Lesson 2-8 pasted in, nothing written yet.

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
    #     pick a random whole number of degrees between 90 and
    # 270     print it, so you can see each choice     turn by
    # that many degrees
    pass


# ===== LINE TRACKING =====
# Drives the robot along the line using the LINE SENSOR
# functions above. Starts with the proportional follower: read
# the error, scale it by KP, steer with arcade(). Grows over
# the module into following to a cross, parking on it, and
# turning to the next line.
BASE_EFFORT = 0.3        # forward speed while following
KP = 0.5                 # proportional gain -- tune this!

def test_follow():
    # loop forever:
    #     error = sensor.get_error()
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
        error = sensor.get_error()
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
    # until sensor.is_at_cross():
    #     correction = sensor.get_error() * KP
    #     steer with arcade(BASE_EFFORT, -correction)
    # then stop the motors
    pass

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
    track_to_intersection()
    print("Done!")

def test_reverse():
    # follow to the cross, turn around, follow back to it
    track_to_intersection()
    drivetrain.turn(180)
    track_to_intersection()
    print("Done!")

# ===== RUN =====
board.wait_for_button()
# call ONE test function here
