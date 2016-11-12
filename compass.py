import math
from i2clibraries import i2c_hmc5883l
import RPi.GPIO as GPIO
import time

Motor2F = 18
Motor2P = 16
Motor2B = 12
Motor1F = 15
Motor1P = 13
Motor1B = 11

leftMotor = 0
rightMotor = 0

timeofRot = 2.425

def turnToAngle(desiredTheta,currentTheta):
    error = desiredTheta - currentTheta
    print (desiredTheta,currentTheta)
    print(error)
    if(abs(error)<5.0):
        stopBot()
    if(error>5.0):
        turnZeroRight()
    elif(error< -5.0):
        turnZeroLeft()


def turnToAngleL(theta):
        turnZeroLeft()
        time.sleep(timeofRot/360.0*theta)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor1F,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1P,GPIO.OUT)
GPIO.setup(Motor2F,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2P,GPIO.OUT)


hmc5883l = i2c_hmc5883l.i2c_hmc5883l(1) 
hmc5883l.setContinuousMode()

hmc5883l.setDeclination(0,6)

def moveForward():
        GPIO.output(Motor1F,True)
        GPIO.output(Motor2F,True)
        GPIO.output(Motor1B,False)
        GPIO.output(Motor2B,False)
        GPIO.output(Motor1P,True)
        GPIO.output(Motor2P,True)

def moveBackward():
        GPIO.output(Motor1F,False)
        GPIO.output(Motor2F,False)
        GPIO.output(Motor1B,False)
        GPIO.output(Motor2B,False)
        GPIO.output(Motor1P,True)
        GPIO.output(Motor2P,True)

def turnZeroLeft():
        GPIO.output(Motor1F,True)
        GPIO.output(Motor2F,False)
        GPIO.output(Motor1B,False)
        GPIO.output(Motor2B,False)
        GPIO.output(Motor1P,True)
        GPIO.output(Motor2P,True)

def turnZeroRight():
        GPIO.output(Motor1F,False)
        GPIO.output(Motor2F,True)
        GPIO.output(Motor1B,False)
        GPIO.output(Motor2B,False)
        GPIO.output(Motor1P,True)
        GPIO.output(Motor2P,True)

def turnLeft():
        GPIO.output(Motor1F,True)
        GPIO.output(Motor2F,False)
        GPIO.output(Motor1B,False)
        GPIO.output(Motor2B,True)
        GPIO.output(Motor1P,True)
        GPIO.output(Motor2P,False)

def turnRight():
        GPIO.output(Motor1F,False)
        GPIO.output(Motor2F,True)
        GPIO.output(Motor1B,True)
        GPIO.output(Motor2B,False)
        GPIO.output(Motor1P,False)
        GPIO.output(Motor2P,True)

def stopBot():
        GPIO.output(Motor1F,False)
        GPIO.output(Motor2F,True)
        GPIO.output(Motor1B,True)
        GPIO.output(Motor2B,True)
        GPIO.output(Motor1P,False)
        GPIO.output(Motor2P,False)

def testWSAD():
        moveForward()
        time.sleep(1)
        stopBot()
        time.sleep(3)
        moveBackward()
        time.sleep(1)
        stopBot()
        time.sleep(3)
        turnZeroLeft()
        time.sleep(1)
        stopBot()
        time.sleep(3)
        turnZeroRight()
        time.sleep(1)
        stopBot()
        time.sleep(3)
        turnLeft()
        time.sleep(1)
        stopBot()
        time.sleep(3)
        turnRight()
        time.sleep(1)
        stopBot()
        GPIO.cleanup()

while(1):
    turnToAngle(90.0,hmc5883l.getHeading())

