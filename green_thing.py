from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port,Direction

hub = PrimeHub()
left_motor = Motor(Port.B,Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E,Direction.CLOCKWISE)
RAM = Motor(Port.F)
LAM = Motor(Port.D)

wheel_diameter = 56
axle_track = 122
robot = DriveBase(left_motor,right_motor,wheel_diameter,axle_track)

robot.use_gyro(True)

robot.settings(straight_speed = 720,straight_acceleration= 300, turn_rate=600, turn_acceleration=400)
hub.imu.reset_heading(0)

if hub.imu.ready():
    robot.straight(650)
    robot.straight(-200)
    robot.straight(63)
    LAM.run_time(-6000,1200)
    LAM.run_time(6000,1000)
    robot.straight(200)
    robot.turn(-47)
    robot.straight(140)
    robot.straight(-20)
    RAM.run_time(-6000,900)
    robot.straight(-200)
    robot.turn(50)
    robot.straight(-1500)