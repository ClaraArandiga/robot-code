import wpilib
import wpilib.drive
import phoenix5 
import rev       

class TestRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.left_front_motor = phoenix5.WPI_TalonSRX(1) 
        self.left_rear_motor = rev.CANSparkMax(2, rev.MotorType.kBrushless)  
        self.right_front_motor = phoenix5.WPI_TalonSRX(3) 
        self.right_rear_motor = rev.CANSparkMax(4, rev.MotorType.kBrushless) 

        self.left = wpilib.MotorControllerGroup(self.left_front_motor, self.left_rear_motor),
        self.right = wpilib.MotorControllerGroup(self.right_front_motor, self.right_rear_motor)


        self.climb_motor = phoenix5.WPI_VictorSPX(5) 

        self.robot_drive = wpilib.drive.DifferentialDrive(
            self.left, self.right
        )

        self.joystick = wpilib.Joystick(0)
    
    def teleopPeriodic(self):
        self.robot_drive.arcadeDrive(self.joystick.getY(), self.joystick.getX())

        if self.joystick.getRawButtonPressed(1):
            self.climb_motor.set(1.0) 
        elif self.joystick.getRawButtonReleased(1):
            self.climb_motor.set(0.0) 

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass 
        # self.left.set(1)
        # self.right.set(-1)

if __name__ == "__main__":
    wpilib.run(TestRobot)
