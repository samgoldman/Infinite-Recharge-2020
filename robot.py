import ctre
import wpilib as wpi
import wpilib.drive
from wpilib.interfaces import GenericHID


class MyRobot(wpi.TimedRobot):

    def robotInit(self):

        self.bToggle = False
        self.aToggle = False

        self.leftMotor = wpi.SpeedControllerGroup(ctre.WPI_TalonSRX(7))
        self.rightMotor = wpi.SpeedControllerGroup(ctre.WPI_TalonSRX(15))

        self.intakeMotor = ctre.WPI_TalonSRX(18)

        self.drive = wpi.drive.DifferentialDrive(self.leftMotor, self.rightMotor)

        #self.panelMotor = wpi.SpeedControllerGroup([ctre.WPI_TalonSRX([INSERT MOTOR NUM]))

        #self.liftMotor = wpi.SpeedControllerGroup([ctre.WPI_TalonSRX([INSERT MOTOR NUM]))

        #self.shooterMotorOne = wpi.SpeedControllerGroup([ctre.WPI_TalonSRX([INSERT MOTOR NUM]))
        #self.shooterMotorTwo = wpi.SpeedControllerGroup([ctre.WPI_TalonSRX([INSERT MOTOR NUM]))

        self.timer = wpilib.Timer()

        self.joystick = wpi.XboxController(1)
        
    def teleopPeriodic(self):
        self.drive.arcadeDrive(self.joystick.getY()*3/4, self.joystick.getX()*3/4)

        if(self.joystick.getBButtonPressed()):
            self.bToggle = not self.bToggle
            self.aToggle = False

        if(self.joystick.getAButtonPressed()):
            self.aToggle = not self.aToggle
            self.bToggle = False

        if(self.aToggle):
            self.intakeMotor.set(.1)
        else:
            self.intakeMotor.stopMotor()

        if(self.bToggle):
            self.intakeMotor.set(-.1)
        else:
            self.intakeMotor.stopMotor()
        

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