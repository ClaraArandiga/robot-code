import wpilib
from commands2 import JoystickButton
from commands.drive_command import DriveCommand
from commands.elevation_command import ElevateUpCommand, ElevateDownCommand
from subsystems.drive_subsystem import DriveSubsystem
from subsystems.elevation_subsystem import ElevationSubsystem

class RobotContainer:
    def __init__(self):
        self.drive_subsystem = DriveSubsystem()
        self.elevation_subsystem = ElevationSubsystem()
        
        self.joystick = wpilib.Joystick(0)
        
        self.configure_button_bindings()

    def configure_button_bindings(self):
        move_command = DriveCommand(
            self.drive_subsystem,
            lambda: -self.joystick.getRawAxis(3),
            lambda: self.joystick.getRawAxis(0)
        )
        self.drive_subsystem.setDefaultCommand(move_command)

        JoystickButton(self.joystick, 4).whileHeld(ElevateUpCommand(self.elevation_subsystem))
        JoystickButton(self.joystick, 2).whileHeld(ElevateDownCommand(self.elevation_subsystem))
