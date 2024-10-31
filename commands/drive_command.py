from commands2 import CommandBase

class DriveCommand(CommandBase):
    def __init__(self, drive_subsystem, get_move_value, get_rotate_value):
        super().__init__()
        self.drive_subsystem = drive_subsystem
        self.get_move_value = get_move_value
        self.get_rotate_value = get_rotate_value
        self.addRequirements(drive_subsystem)

    def execute(self):
        move_value = self.get_move_value()
        rotate_value = self.get_rotate_value()
        self.drive_subsystem.arcade_drive(move_value, rotate_value)

    def end(self, interrupted):
        self.drive_subsystem.stop()
