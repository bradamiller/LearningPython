# robot.py after Lesson 2-5 (class track): every skeleton
# through Lesson 2-5 pasted in, nothing written yet.

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
SETPOINT = 0.5           # the reading at the edge of the line

def get_left():
    # return the left reflectance reading
    pass

def get_right():
    # return the right reflectance reading
    pass

def get_error():
    # return SETPOINT minus the left reading
    pass

def is_either_on_line():
    # return True when AT LEAST ONE reading is above THRESHOLD
    pass

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
BASE_EFFORT = 0.3        # forward speed while following
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

# ===== RUN =====
board.wait_for_button()
# call ONE test function here
