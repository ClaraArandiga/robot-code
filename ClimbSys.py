import wpilib
import wpilib.drive
import phoenix5 
import rev    

class ClimbSys:

    def init(self):
        self.joystick = wpilib.Joystick(0)
        self.climb_motor_left = phoenix5.WPI_VictorSPX(2) 
        self.climb_motor_right = phoenix5.WPI_VictorSPX(3) 

    def teleop(self):
        if self.joystick.getRawButton(4):
            self.climb_motor_left.set(1.0) 
            self.climb_motor_right.set(1.0) 

        elif self.joystick.getRawButton(2): 
            self.climb_motor_left.set(-1.0) 
            self.climb_motor_right.set(-1.0) 

        else:
            self.climb_motor_left.set(0.0) 
            self.climb_motor_right.set(0.0)