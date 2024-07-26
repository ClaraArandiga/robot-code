import wpilib
import wpilib.drive
import phoenix5 
from elevationSys import climbSys
import rev       

class TestRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.left_front_motor = phoenix5.WPI_VictorSPX(4) 
        self.left_rear_motor = phoenix5.WPI_VictorSPX(1)  
        self.right_front_motor = phoenix5.WPI_VictorSPX(8) 
        self.right_rear_motor = phoenix5.WPI_VictorSPX(12) 

        self.left = wpilib.MotorControllerGroup(self.left_front_motor, self.left_rear_motor)
        self.right = wpilib.MotorControllerGroup(self.right_front_motor, self.right_rear_motor)

        self.robot_drive = wpilib.drive.DifferentialDrive(
            self.left, self.right
        )

        climbSys.init(self)

        self.joystick = wpilib.Joystick(0)
    def teleopPeriodic(self):
        move_value = self.joystick.getRawAxis(0)
        rotate_value = self.joystick.getRawAxis(1)
        self.robot_drive.arcadeDrive(move_value, rotate_value)

        climbSys.teleop(self)

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass 

# if _name_ == "_main_":
    # wpilib.run(TestRobot)