from commands2 import CommandBase

class ElevateUpCommand(CommandBase):
    def __init__(self, elevation_subsystem):
        super().__init__()
        self.elevation_subsystem = elevation_subsystem
        self.addRequirements(elevation_subsystem)

    def execute(self):
        self.elevation_subsystem.move_up()

    def end(self, interrupted):
        self.elevation_subsystem.stop()

class ElevateDownCommand(CommandBase):
    def __init__(self, elevation_subsystem):
        super().__init__()
        self.elevation_subsystem = elevation_subsystem
        self.addRequirements(elevation_subsystem)

    def execute(self):
        self.elevation_subsystem.move_down()

    def end(self, interrupted):
        self.elevation_subsystem.stop()
