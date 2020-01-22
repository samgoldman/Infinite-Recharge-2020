import ctre
import wpilib as wpi
import wpilib.drive
import ports
from wpilib.interfaces import GenericHID
import MethodsRobot

class MyRobot(wpi.TimedRobot):

    def robotInit(self):

        self.driveMethods = MethodsRobot.Drive()
        self.shooterMethods = MethodsRobot.Shooter()

        self.timer = wpilib.Timer()

        self.driverController = wpi.XboxController(ports.controllerPorts.get("driverController"))
        #self.codriverController = wpi.XboxController(ports.controllerPorts.get("codriverContoller"))

        
    def teleopPeriodic(self):
        self.driveMethods.basicDrive(self.driverController.getX(), self.driverController.getY())
        self.shooterMethods.intake(self.driverController.getBButtonPressed(), self.driverController.getAButtonPressed())
        self.shooterMethods.shooting(self.driverController.getTriggerAxis())


    def autonomousInit(self):
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        self.teleopPeriodic()
        '''
        if self.timer.get() < 2.0:
            self.drive.arcadeDrive(-0.5, 0)  # Drive forwards at half speed
        else:
            self.drive.arcadeDrive(0, 0)  # Stop robot
        '''


if __name__ == '__main__':
    wpi.run(MyRobot)