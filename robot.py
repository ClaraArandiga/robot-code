import wpilib
import wpilib.drive
import rev 
from ClimbSys import ElevationSys

class TestRobot(wpilib.TimedRobot):
    def robotInit(self):
        # Initialize motors using CAN IDs
        self.left_front_motor = rev.CANSparkMax(50, rev.CANSparkLowLevel.MotorType.kBrushed)
        self.left_rear_motor = rev.CANSparkMax(51, rev.CANSparkLowLevel.MotorType.kBrushed)
        self.right_front_motor = rev.CANSparkMax(53, rev.CANSparkLowLevel.MotorType.kBrushed)
        self.right_rear_motor = rev.CANSparkMax(52, rev.CANSparkLowLevel.MotorType.kBrushed)

        # Group left and right motors
        self.left = wpilib.MotorControllerGroup(self.left_front_motor, self.left_rear_motor)
        self.right = wpilib.MotorControllerGroup(self.right_front_motor, self.right_rear_motor)

        self.right.setInverted(True)

        # Set up differential drive for arcade driving
        self.robot_drive = wpilib.drive.DifferentialDrive(self.left, self.right)

        # Initialize joystick for controlling the robot
        self.joystick = wpilib.Joystick(0)

        self.elevation = ElevationSys()

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        self.robot_drive.setExpiration(0.1)
        self.robot_drive.setSafetyEnabled(True)

    def axis(self):
        if self.joystick.getRawAxis(3) > 0:
            return -self.joystick.getRawAxis(3)
        elif self.joystick.getRawAxis(4) > 0:
            return self.joystick.getRawAxis(4)
        return 0      

    def teleopPeriodic(self):
        # Get joystick axis values for movement and rotati on
        move_value = self.axis()  # Y-axis
        rotate_value = self.joystick.getRawAxis(0)  # X-axis

        # Use arcade drive to move the robot
        self.robot_drive.arcadeDrive(move_value, rotate_value)

        self.elevation.teleop()