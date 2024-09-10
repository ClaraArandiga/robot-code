import wpilib
import wpilib.drive
import phoenix5 
from ClimbSys import elevationSys
import rev

class TestRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.left_front_motor = rev.CANSparkMax(51, rev.MotorType.kBrushless)
        self.left_rear_motor = rev.CANSparkMax(52, rev.MotorType.kBrushless)
        self.right_front_motor = rev.CANSparkMax(54, rev.MotorType.kBrushless)
        self.right_rear_motor = rev.CANSparkMax(53, rev.MotorType.kBrushless)

        self.left = wpilib.MotorControllerGroup(self.left_front_motor, self.left_rear_motor)
        self.right = wpilib.MotorControllerGroup(self.right_front_motor, self.right_rear_motor)

        self.motors = wpilib.SpeedControllerGroup(self.left, self.right)

        self.robot_drive = wpilib.drive.DifferentialDrive(
            self.left, self.right
        )

        elevationSys.init(self)

        self.joystick = wpilib.Joystick(0)
    
    def teleopPeriodic(self):
        move_value = self.joystick.getRawAxis(5)
        rotate_value = self.joystick.getRawAxis(2)
        self.robot_drive.arcadeDrive(move_value, rotate_value)

        elevationSys.teleop(self)

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass 

# if _name_ == "_main_":
    # wpilib.run(TestRobot)
