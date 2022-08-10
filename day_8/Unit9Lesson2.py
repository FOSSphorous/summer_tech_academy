#region VEXcode Generated Robot Configuration
import math
import random
from vexcode_vr_enhanced_robot import *

drivetrain = Drivetrain()
magnet = Electromagnet("magnet", 0)
pen = Pen()
brain = Brain()
left_bumper = Bumper("leftBumper", 1)
right_bumper = Bumper("rightBumper", 2)
front_eye = EyeSensor("fronteye", 3)
down_eye = EyeSensor("downeye", 4)
right_eye = EyeSensor("righteye", 5)
left_eye = EyeSensor("lefteye", 6)
rear_eye = EyeSensor("reareye", 7)
front_distance = Distance("frontdistance", 8)
rear_distance = Distance("reardistance", 9)
left_distance = Distance("leftdistance", 10)
right_distance = Distance("rightdistance", 11)
location = Location()
pen.set_pen_width(THIN)
distance = front_distance
#endregion VEXcode Generated Robot Configuration


# Drives around, clearing "Dynamic Castle crasher" playground
def main():
    # Set speeds to max to save some time in the sim
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)

    while True:

        # Does the Distance Sensor detect a castle?
        if distance.found_object():
            # Crash castle detected by Distance Sensor
            drivetrain.drive(FORWARD)

            # Don't fall off the edge
            if down_eye.detect(RED):
                drivetrain.drive_for(REVERSE, 300, MM)
                drivetrain.turn(RIGHT)

        else:
            # Turn to find a castle using the Distance Sensor
            drivetrain.turn(RIGHT)

        wait(5, MSEC)

    stop_project()

vr_thread(main)
