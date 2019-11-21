#Property of Gavin Burgess

import ctre
import wpilib as wpi
import wpilib.drive
from wpilib.interfaces import GenericHID
from networktables import NetworkTables

class MyRobot(wpi.TimedRobot):

    class SensorData():
        def __init__(self, table):
            self.dashboard = NetworkTables.getTable(table)

        def sendSensorData(self, tag, data):
            self.dashboard.putNumber(tag, data)

    #def sendSensorData(self, tag, data):
            #self.dashboard.putNumber(tag, data)

    def boolFromVal(self, value):
            if(value < 500):
                return True
            else:
                return False

    def robotInit(self):
        #----------Motors and Drive Control----------
        self.leftMotor = wpi.SpeedControllerGroup(ctre.WPI_TalonSRX(7))
        self.rightMotor = wpi.SpeedControllerGroup(ctre.WPI_TalonSRX(22))
        self.drive = wpi.drive.DifferentialDrive(self.leftMotor, self.rightMotor)
        #self.dashboard = NetworkTables.getTable(table)
        #def sendSensorData(self, tag, data):
            #self.dashboard.putNumber(tag, data)                
        #----------Controllers----------
        self.joystick = wpilib.XboxController(1)
        self.dashboard = NetworkTables.getTable("LIFT")
        #def sendSensorData(self, tag, data):
            #self.dashboard.putNumber(tag, data)
        #----------Arm Stuff----------
        self.arm = ctre.WPI_TalonSRX(21)
        self.armSensors = ctre.sensorcollection.SensorCollection(self.arm)
        self.armPosition = self.armSensors.getQuadraturePosition()
        #----------Lift Stuff----------
        self.lift = ctre.WPI_TalonSRX(4)
        self.liftSpeed = 0.75
        self.liftSpeedDown = -0.25
        self.sensorThreshold = 2.5
        self.aboveMid = False
        self.notMoving = False
        self.movingDown = False
        self.movingUp = False
        self.bottomHallEffect = wpilib.AnalogInput(0)
        self.middleHallEffect = wpilib.AnalogInput(1)
        self.topHallEffect = wpilib.AnalogInput(2)
        self.liftSensor = self.dashboard
        
        def boolFromVal(self, value):
            if(value < 500):
                return True
            else:
                return False
        
        #self.liftSensor.sendSensorData("Value", self.bottomHallEffect.getValue())
        #self.liftSensor.sendSensorData("bottom", self.boolFromVal(self.bottomHallEffect.getValue()))
        #self.liftSensor.sendSensorData("middle", self.boolFromVal(self.middleHallEffect.getValue()))
        #self.liftSensor.sendSensorData("top", self.boolFromVal(self.topHallEffect.getValue()))
        #self.notMoving = self.boolFromVal(self.bottomHallEffect.getValue()) or self.boolFromVal(self.middleHallEffect.getValue()) or self.boolFromVal(self.topHallEffect.getValue())
        '''
        self.liftSensor.putNumber("Value", self.bottomHallEffect.getValue())
        self.liftSensor.putNumber("bottom", self.boolFromVal(self.bottomHallEffect.getValue()))
        self.liftSensor.putNumber("middle", self.boolFromVal(self.middleHallEffect.getValue()))
        self.liftSensor.putNumber("top", self.boolFromVal(self.topHallEffect.getValue()))
        self.notMoving = self.boolFromVal(self.bottomHallEffect.getValue()) or self.boolFromVal(self.middleHallEffect.getValue()) or self.boolFromVal(self.topHallEffect.getValue())
        '''
        '''
        if(joystick.getXButton()):
            notMoving = True
            movingDown = False
            movingUp = False
    
        if(joystick.getYButton()):
                movingUp = not self.boolFromVal(self.topHallEffect.getValue())
                notMoving = False
                movingDown = False

        if(joystick.getAButton()):
                movingUp = False
                movingDown = not self.boolFromVal(self.bottomHallEffect.getValue())
                notMoving = False
        '''
    def teleopPeriodic(self):

        def sendSensorData(self, tag, data):
            self.dashboard.putNumber(tag, data)

        self.liftSensor.putNumber("Value", self.bottomHallEffect.getValue())
        self.liftSensor.putNumber("bottom", self.boolFromVal(self.bottomHallEffect.getValue()))
        self.liftSensor.putNumber("middle", self.boolFromVal(self.middleHallEffect.getValue()))
        self.liftSensor.putNumber("top", self.boolFromVal(self.topHallEffect.getValue()))
        self.notMoving = self.boolFromVal(self.bottomHallEffect.getValue()) or self.boolFromVal(self.middleHallEffect.getValue()) or self.boolFromVal(self.topHallEffect.getValue())

        self.drive.arcadeDrive(self.joystick.getY()*3/4, self.joystick.getX()*3/4)
        if(self.joystick.getBumper(GenericHID.Hand.kRight)): #Open Arm
            if(self.armPosition <= -3000):
                self.arm.stopMotor()
            elif(self.armPosition <= -150):
                self.arm.stopMotor()
            else:
                self.arm.set(0.2)
        elif(self.joystick.getBumper(GenericHID.Hand.kLeft)):
            if(self.armPosition >= 135):
                self.arm.stopMotor()
            else:
                self.arm.set(-0.4)

        if(self.joystick.getXButton()):
            self.notMoving = True
            self.movingDown = False
            self.movingUp = False
    
        if(self.joystick.getYButton()):
                self.movingUp = not self.boolFromVal(self.topHallEffect.getValue())
                self.notMoving = False
                self.movingDown = False

        if(self.joystick.getAButton()):
                self.movingUp = False
                self.movingDown = not self.boolFromVal(self.bottomHallEffect.getValue())
                self.notMoving = False

        if(self.notMoving):
            self.lift.set(.125)
        elif(self.movingUp):
            self.lift.set(self.liftSpeed)
        elif(self.movingDown):
            self.lift.set(self.liftSpeedDown)
        else:
            self.lift.stopMotor()

    def autonomusInit(self):
        self.timer.reset()
        self.timer.start()

    def autonomusPeriodic(self):
        self.teleopPeriodic()

if __name__ == '__main__':
    wpilib.run(MyRobot)

