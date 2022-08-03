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

def when_started1():
    initialize_drawing()
    pen.move(DOWN)
    draw_J()
    pen.move(UP)
    drivetrain.stop()
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 600, MM)
    pen.move(DOWN)
    draw_O()
    pen.move(UP)
    drivetrain.drive_for(FORWARD, 100, MM)
    pen.move(DOWN)
    draw_S()
    pen.move(UP)
    drivetrain.drive_for(FORWARD, 100, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 300, MM)
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.stop()
    pen.move(DOWN)
    draw_H()
    stop_project()

vr_thread(when_started1)

def initialize_drawing():
    drivetrain.drive_for(FORWARD, 400, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 800, MM)
    drivetrain.turn_for(RIGHT, 180, DEGREES)

def draw_J():
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_drive_velocity(50, PERCENT)
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 600, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 300, MM)

def draw_O():
    drivetrain.drive_for(FORWARD, 50, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)

def draw_S():
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 100, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 100, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)

def draw_H():
    drivetrain.drive_for(FORWARD, 500, MM)
    pen.move(UP)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.stop()
    drivetrain.turn_for(LEFT, 90, DEGREES)
    pen.move(DOWN)
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.stop()
