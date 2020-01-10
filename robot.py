import ctre
import wpilib as wpi
import wpilib.drive
from wpilib.interfaces import GenericHID

from networktables import NetworkTables
from wpilib import PowerDistributionPanel


class MyRobot(wpi.TimedRobot):

    def robotInit(self):
        self.leftMotor = wpi.SpeedControllerGroup(ports.talonPorts.get("liftMotor"))
        self.rightMotor = wpi.SpeedControllerGroup(ctre.WPI_TalonSRX(22))
        self.drive = wpi.drive.DifferentialDrive(self.leftMotor, self.rightMotor)

        #self.panelMotor = wpi.SpeedControllerGroup([ctre.WPI_TalonSRX([INSERT MOTOR NUM]))

        #self.liftMotor = wpi.SpeedControllerGroup([ctre.WPI_TalonSRX([INSERT MOTOR NUM]))

        #self.shooterMotorOne = wpi.SpeedControllerGroup([ctre.WPI_TalonSRX([INSERT MOTOR NUM]))
        #self.shooterMotorTwo = wpi.SpeedControllerGroup([ctre.WPI_TalonSRX([INSERT MOTOR NUM]))

        #self.intakeMotorOne = wpi.SpeedControllerGroup([ctre.WPI_TalonSRX([INSERT MOTOR NUM]))
        #self.intakeMotorTwo = wpi.SpeedControllerGroup([ctre.WPI_TalonSRX([INSERT MOTOR NUM]))


        #self.dashboard = NetworkTables.getTable("Dashboard")
        #self.pdp = PowerDistributionPanel([PORT NUMBERS]) <----Research PDP class



        self.timer = wpilib.Timer()

        self.joystick = wpi.XboxController(1)
        
    def teleopPeriodic(self):
        self.drive.arcadeDrive(self.joystick.getY()*3/4, self.joystick.getX()*3/4)

        #self.dashboard.putNumber("RobotSpeed", speed)
        #self.dashboard.putNumber("RobotRotation", rotation)
        #self.dashboard.putNumber("PDPCurrent", self.pdp.getTotalCurrent())
        #self.dashboard.putNumber("PDPTemperature", self.pdp.getTemperature())
        #self.dashboard.putNumber("PDPVoltage", self.pdp.getVoltage())

    def autonomousInit(self):
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        #self.teleopPeriodic()
        
        #self.dashboard.putNumber("RobotSpeed", speed)
        #self.dashboard.putNumber("RobotRotation", rotation)
        #self.dashboard.putNumber("PDPCurrent", self.pdp.getTotalCurrent())
        #self.dashboard.putNumber("PDPTemperature", self.pdp.getTemperature())
        #self.dashboard.putNumber("PDPVoltage", self.pdp.getVoltage())
        
        if self.timer.get() < 2.0:
            self.drive.arcadeDrive(-0.5, 0)  # Drive forwards at half speed
        else:
            self.drive.arcadeDrive(0, 0)  # Stop robot
        


if __name__ == '__main__':
    wpi.run(MyRobot)