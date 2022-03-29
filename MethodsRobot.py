import ctre
import wpilib as wpi
from wpilib.drive import DifferentialDrive
from wpilib.interfaces import GenericHID
import ports
from rev._rev import ColorSensorV3

class Drive():
    def __init__(self):
        
        self.leftMotor = wpi.SpeedControllerGroup(ctre.WPI_TalonSRX(ports.talonPorts.get("leftChassisMotor")))
        self.rightMotor = wpi.SpeedControllerGroup(ctre.WPI_TalonSRX(ports.talonPorts.get("rightChassisMotor")))
        self.drive = wpi.drive.DifferentialDrive(self.leftMotor, self.rightMotor)
        self.colorSensor = ColorSensorV3(wpi.I2C.Port.kOnboard)


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

        if(aPress):
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
        if(triggerPress == 1.0):
            self.shootingMotor1.set(.9)
            self.shootingMotor2.set(.9)
        else:
            self.shootingMotor1.stopMotor()
            self.shootingMotor2.stopMotor()


class Controller():
    def __init__(self):
        self.colorSensor = ColorSensorV3(wpi.I2C.Port.kOnboard)
        self.controllerMotor = ctre.WPI_TalonSRX(ports.talonPorts.get("controllerMotor"))
        self.lToggle = False
        self.rToggle = False
        self.currentColor = self.colorSensor.getColor() #Variable to determine what the current color sensed by the sensor is
        self.ir = self.colorSensor.getIR()
        wpi.SmartDashboard.putNumber("Red", self.currentColor.red)
        wpi.SmartDashboard.putNumber("Green", self.currentColor.green)
        wpi.SmartDashboard.putNumber("Blue", self.currentColor.blue)
        wpi.SmartDashboard.putNumber("IR", self.ir)
        self.colorProximity = self.colorSensor.getProximity()
        wpi.SmartDashboard.putNumber("Proximity", self.colorProximity)
        self.colorCount = None #Variable to count how many times the color has changed, may also be used to count how many times the wheel has been spun
        self.controllerCheck = False #False: # of spins or on certian color reqs not met, keep going True: conditions met, stop
        

    def spinner(self, lPress, rPress):
        if(lPress):
            self.lToggle = not self.lToggle
            self.rToggle = False

        if(rPress):
            self.rToggle = not self.rToggle
            self.lToggle = False

        #Rotate backwards for a short time and stop. Acts as a way to quickly reverse slightly
        if(self.lToggle):
            pass

        #Keep spinning CW until toggled off by pressing the same bumper a second time
        if(self.rToggle and self.controllerCheck):
            self.controllerMotor.set(.1)
        else:
            self.controllerMotor.stopMotor()
