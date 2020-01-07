import ctre
import wpilib as wpi
import wpilib.drive
from wpilib.interfaces import GenericHID


class MyRobot(wpi.TimedRobot):

    def robotInit(self):
        self.leftMotor = wpi.SpeedControllerGroup(ctre.WPI_TalonSRX(7))
        self.rightMotor = wpi.SpeedControllerGroup(ctre.WPI_TalonSRX(22))
        self.drive = wpi.drive.DifferentialDrive(self.leftMotor, self.rightMotor)
        self.timer = wpilib.Timer()

        self.joystick = wpi.XboxController(1)
        
    def teleopPeriodic(self):
        self.drive.arcadeDrive(self.joystick.getY()*3/4, self.joystick.getX()*3/4)

    def autonomousInit(self):
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        #self.teleopPeriodic()
        
        if self.timer.get() < 2.0:
            self.drive.arcadeDrive(-0.5, 0)  # Drive forwards at half speed
        else:
            self.drive.arcadeDrive(0, 0)  # Stop robot
        


if __name__ == '__main__':
    wpi.run(MyRobot)