import wpilib
import phoenix5
from commands2 import SubsystemBase

class ElevationSubsystem(SubsystemBase):
    def __init__(self):
        super().__init__()
        self.climb_motor_left = phoenix5.WPI_VictorSPX(9)
        self.climb_motor_right = phoenix5.WPI_VictorSPX(8)
        self.climb_motor_left.setInverted(True)

    def move_up(self):
        self.climb_motor_left.set(1.0)
        self.climb_motor_right.set(1.0)

    def move_down(self):
        self.climb_motor_left.set(-1.0)
        self.climb_motor_right.set(-1.0)

    def stop(self):
        self.climb_motor_left.set(0)
        self.climb_motor_right.set(0)
