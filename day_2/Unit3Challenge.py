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


def move_in_square(millimeters, rotation_direction):
  for LOOP in range(4):
    drivetrain.turn_for(rotation_direction, 90, DEGREES)
    drivetrain.drive_for(FORWARD, millimeters, MM)
    wait(5, MSEC)


def main():
  # Set speeds to max to save some time in the sim
  drivetrain.set_drive_velocity(100, PERCENT)
  drivetrain.set_turn_velocity(100, PERCENT)

  # Get in position before drawing
  drivetrain.drive_for(FORWARD, 200, MM)

  # Draw house's body
  pen.set_pen_color(BLACK)
  pen.move(DOWN)
  
  drivetrain.turn_for(LEFT, 90, DEGREES)
  drivetrain.drive_for(FORWARD, 500, MM)  # First line is half-sized
  
  move_in_square(1000, LEFT) # A complete square brings the bot back to position
  drivetrain.stop()

  pen.move(UP)

  # Prepare to draw roof
  drivetrain.turn_for(LEFT, 225, DEGREES)
  pen.set_pen_color(BLUE)
  
  # Draw roof
  pen.move(DOWN)
  drivetrain.drive_for(FORWARD, 750, MM)
  drivetrain.turn_for(RIGHT, 92, DEGREES)
  drivetrain.drive_for(FORWARD, 750, MM)
  drivetrain.stop()

  stop_project()
  
vr_thread(main)
