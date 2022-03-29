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
        self.controllerMethods = MethodsRobot.Controller()
        #self.controllerMethods = MethodsRobot.Controller()

        self.timer = wpi.Timer()

        self.driverController = wpi.XboxController(ports.controllerPorts.get("driverController"))
        #self.codriverController = wpi.XboxController(ports.controllerPorts.get("codriverContoller"))

        
    def teleopPeriodic(self):
        self.driveMethods.basicDrive(self.driverController.getXButton(), self.driverController.getYButton())
        self.shooterMethods.intake(self.driverController.getBButtonPressed(), self.driverController.getAButtonPressed())
        self.shooterMethods.shooting(self.driverController.getLeftTriggerAxis())
        # print(self.controllerMethods.colorSensor.isConnected(), self.controllerMethods.colorSensor.getColor())
        #self.controllerMethods.spinner(self.driveController.getBumperPressed(GenericHID.Hand.kLeft), self.driveController.getBumperPressed(GenericHID.Hand.kRight))

    def autonomousInit(self):
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        self.teleopPeriodic()
        


if __name__ == '__main__':
    wpi.run(MyRobot)