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

robot.settings(straight_speed = 720,straight_acceleration= 300, turn_rate=600, turn_acceleration=300)
hub.imu.reset_heading(0)

if hub.imu.ready():
    robot.straight(730)
    robot.turn(25)
    robot.straight(30)
    robot.turn(-50)
    robot.turn(30)
    robot.straight(10)
    robot.turn(55)
    

  
  
  
    # LAM.run_time(-993,1090)
    # robot.straight(50)
    # LAM.run_time(500,2000)
    # LAM.run_time(-1000,1000)
    # RAM.run_time(-1000,1000)
    #robot.straight(670)
    #robot.turn(-35)
    # robot.straight(30)
    # LAM.run_time(-1000,500)
    # robot.straight(-20)
    # #robot.turn(5)
    # robot.straight(-15)
    # RAM.run_time(2000,1000)#arm goes down
    # robot.straight(45)
    # RAM.run_time(-2000,1000) #arm goes up
    # robot.straight(-100)
    # robot.turn(45)
    # robot.straight(-10)
    # LAM.run_time(1500,1000)
    # robot.straight(150)    
    # LAM.run_time(-1000,700)
    # robot.straight(-120)
    # robot.turn(40)
    # robot.straight(-650)