import ctre
import wpilib as wpi
from wpilib.drive import DifferentialDrive
from wpilib.interfaces import GenericHID
import ports

class Drive():
    def __init__(self):
        
        self.leftMotor = wpi.SpeedControllerGroup(ctre.WPI_TalonSRX(ports.talonPorts.get("leftChassisMotor")))
        self.rightMotor = wpi.SpeedControllerGroup(ctre.WPI_TalonSRX(ports.talonPorts.get("rightChassisMotor")))
        self.drive = wpi.drive.DifferentialDrive(self.leftMotor, self.rightMotor)

    def basicDrive(self, x, y):
        if self.drive is None:
            self.drive = wpi.drive.DifferentialDrive(self.leftMotor, self.rightMotor)

        self.controllerXValue = x
        self.controllerYValue = y
        self.drive.arcadeDrive(self.controllerYValue, self.controllerXValue)
    

class Shooter():
    def __init__(self):
    
        #Intake Components and Variables
        self.intakeMotor = ctre.WPI_TalonSRX(ports.talonPorts.get("intakeMotor"))
        self.bToggle = False
        self.aToggle = False

        #Shooting Components and Variables
        self.shootingMotor1 = ctre.WPI_TalonSRX(ports.talonPorts.get("shootingMotor1"))
        self.shootingMotor2 = ctre.WPI_TalonSRX(ports.talonPorts.get("shootingMotor2"))

    def intake(self, bPress, aPress):
        if(bPress):
            self.bToggle = not self.bToggle
            self.aToggle = False

        if(bPress):
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

    def shooting(self, triggerPress):
        if(triggerPress):
            self.shootingMotor1.set(.9)
            self.shootingMotor2.set(.9)
