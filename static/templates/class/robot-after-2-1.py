# robot.py after Lesson 2-1 (class track): every skeleton
# through Lesson 2-1 pasted in, nothing written yet.

from XRPLib.reflectance import Reflectance
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.board import Board
import time

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

def get_left():
    # return the left reflectance reading
    pass

def get_right():
    # return the right reflectance reading
    pass

def test_sensors():
    # prints both readings 50 times, a tenth of a second apart
    for i in range(50):
        print("Left:", get_left(), "  Right:", get_right())
        time.sleep(0.1)

# ===== RUN =====
board.wait_for_button()
# call ONE test function here
