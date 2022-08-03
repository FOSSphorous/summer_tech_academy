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

def main():
  # Set speeds to max to save some time in the sim
  drivetrain.set_drive_velocity(100, PERCENT)
  drivetrain.set_turn_velocity(100, PERCENT)

  # Start 600MM sq
  pen.move(DOWN)
  drivetrain.drive_for(FORWARD, 600, MM)
  drivetrain.turn_for(RIGHT, 90, DEGREES)
  drivetrain.drive_for(FORWARD, 600, MM)
  drivetrain.turn_for(RIGHT, 90, DEGREES)
  drivetrain.drive_for(FORWARD, 580, MM) # Why is this line a few pixels too long?
  drivetrain.turn_for(RIGHT, 90, DEGREES)
  drivetrain.drive_for(FORWARD, 600, MM)
  drivetrain.turn_for(RIGHT, 90, DEGREES)
  drivetrain.stop()
  pen.move(UP)

  # Ended 600MM sq. Giving it some space
  drivetrain.turn_for(LEFT, 90, DEGREES)
  drivetrain.drive_for(FORWARD, 100, MM)
  
  # Start 300MM sq
  pen.move(DOWN)
  drivetrain.drive_for(FORWARD, 300, MM)
  drivetrain.turn_for(LEFT, 90, DEGREES)
  drivetrain.drive_for(FORWARD, 300, MM)
  drivetrain.turn_for(LEFT, 90, DEGREES)
  drivetrain.drive_for(FORWARD, 300, MM)
  drivetrain.turn_for(LEFT, 90, DEGREES)
  drivetrain.drive_for(FORWARD, 300, MM)
  stop_project()
  pen.move(UP)

vr_thread(main)
