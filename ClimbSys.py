import wpilib
import phoenix5 

class ElevationSys:
    def __init__(self):
        self.joystick = wpilib.Joystick(0)
        self.climb_motor_left = phoenix5.WPI_VictorSPX(9) 
        self.climb_motor_right = phoenix5.WPI_VictorSPX(8)
        self.climb_motor_left.setInverted(True)

    def teleop(self):
        if self.joystick.getRawButton(4): # While pressed -> motor up
            self.climb_motor_left.set(1.0)
            self.climb_motor_right.set(1.0) 

        elif self.joystick.getRawButton(2): # While pressed -> motor down
            self.climb_motor_left.set(-1.0) 
            self.climb_motor_right.set(-1.0) 

        else: # -> motor off
            self.climb_motor_left.set(0.0) 
            self.climb_motor_right.set(0.0)