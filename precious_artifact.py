from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port,Direction
from pybricks.tools import multitask, run_task,wait

hub = PrimeHub()
left_motor = Motor(Port.A,Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E,Direction.CLOCKWISE)
RAM = Motor(Port.C)
LAM = Motor(Port.B)

wheel_diameter = 56
axle_track = 122
robot = DriveBase(left_motor,right_motor,wheel_diameter,axle_track)

robot.use_gyro(True)

robot.settings(straight_speed = 720,straight_acceleration= 300, turn_rate=600, turn_acceleration=400)
hub.imu.reset_heading(0)

async def main():
   if hub.imu.ready():
    await robot.straight(-1000) #robot straight
    robot.settings(straight_speed = 220,straight_acceleration= 100, turn_rate=200, turn_acceleration=100) #robot slower
    await robot.straight(25)
    await robot.turn(-90)
    await multitask(RAM.run_time(690,900),LAM.run_time(560,860)) #arm goes down (LAM+RAM)
    robot.settings(straight_speed = 220,straight_acceleration= 100, turn_rate=200, turn_acceleration=100)
    await robot.straight(70)
    await multitask(RAM.run_time(0,0),LAM.run_time(300,340)) #arm goes down (LAM+RAM)
    robot.settings(straight_speed = 190,straight_acceleration= 50, turn_rate=100, turn_acceleration=70)
    await robot.straight(54)
    robot.settings(straight_speed = 220,straight_acceleration= 100, turn_rate=200, turn_acceleration=100)
    await multitask(RAM.run_time(-690,910),LAM.run_time(-150,500))  # arm go up (LAM)
    await multitask(RAM.run_time(690,910),LAM.run_time(0,0)) #arm goes up (RAM)
    await wait(930)
    await robot.straight(-30)
    await robot.turn(5.3)
    await robot.straight(-80)
    await robot.turn(110)
    robot.settings(straight_speed = 720,straight_acceleration= 300, turn_rate=600, turn_acceleration=400)
    await robot.straight(800)
    



# Runs the main program from start to finish.
run_task(main())
