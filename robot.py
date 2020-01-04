import ctre
import wpilib as wpi
import wpilib.drive
from wpilib.interfaces import GenericHID


class MyRobot(wpi.TimedRobot):

    def robotInit(self):
        self.leftMotor = wpi.SpeedControllerGroup(ctre.WPI_TalonSRX(7))
        self.rightMotor = wpi.SpeedControllerGroup(ctre.WPI_TalonSRX(22))
        self.drive = wpi.drive.DifferentialDrive(self.leftMotor, self.rightMotor)

        self.joystick = wpi.XboxController(1)
        
    def teleopPeriodic(self):
        self.drive.arcadeDrive(self.joystick.getY()*3/4, self.joystick.getX()*3/4)

    def autonomusInit(self):
        self.timer.reset()
        self.timer.start()

    def autonomusPeriodic(self):
        self.teleopPeriodic()

if __name__ == '__main__':
    wpi.run(MyRobot)