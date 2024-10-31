import wpilib
import wpilib.drive
import rev
from commands2 import SubsystemBase

class DriveSubsystem(SubsystemBase):
    def __init__(self):
        super().__init__()
        # Inicialização dos motores
        self.left_front_motor = rev.CANSparkMax(50, rev.CANSparkLowLevel.MotorType.kBrushed)
        self.left_rear_motor = rev.CANSparkMax(51, rev.CANSparkLowLevel.MotorType.kBrushed)
        self.right_front_motor = rev.CANSparkMax(53, rev.CANSparkLowLevel.MotorType.kBrushed)
        self.right_rear_motor = rev.CANSparkMax(52, rev.CANSparkLowLevel.MotorType.kBrushed)

        # Agrupando motores da esquerda e direita
        self.left = wpilib.MotorControllerGroup(self.left_front_motor, self.left_rear_motor)
        self.right = wpilib.MotorControllerGroup(self.right_front_motor, self.right_rear_motor)
        self.right.setInverted(True)

        # Configuração do drive
        self.robot_drive = wpilib.drive.DifferentialDrive(self.left, self.right)

    def arcade_drive(self, move_value, rotate_value):
        self.robot_drive.arcadeDrive(move_value, rotate_value)

    def stop(self):
        self.robot_drive.stopMotor()
