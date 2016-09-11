import math
import sys
from Adafruit_IO import Client

import RPi.GPIO as GPIO
import time

Motor1F = 7
Motor1P = 5
Motor1B = 3
Motor2F = 15
Motor2P = 13
Motor2B = 11

leftMotor = 0
rightMotor = 0

timeofRot = 2.425

def turnToAngleR(theta):
        turnZeroRight()
        time.sleep(2.425/360.0*theta)

def turnToAngleL(theta):
        turnZeroLeft()
        time.sleep(2.425/360.0*theta)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor1F,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1P,GPIO.OUT)
GPIO.setup(Motor2F,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2P,GPIO.OUT)
aio = Client('47bc88002f0a4117a751a1074e25fa96')
leftMotor = GPIO.PWM(Motor2P,200)
rightMotor = GPIO.PWM(Motor1P,200)
leftMotor.start(0)
rightMotor.start(0)
GPIO.output(Motor1B,True)
GPIO.output(Motor2B,True)
leftMotor.ChangeDutyCycle(float(sys.argv[1]))
rightMotor.ChangeDutyCycle(float(sys.argv[2]))
        

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
        GPIO.output(Motor2P,True)

def turnRight():
        GPIO.output(Motor1F,False)
        GPIO.output(Motor2F,True)
        GPIO.output(Motor1B,True)
        GPIO.output(Motor2B,False)
        GPIO.output(Motor1P,True)
        GPIO.output(Motor2P,True)

def stopBot():
        GPIO.output(Motor1F,False)
        GPIO.output(Motor2F,True)
        GPIO.output(Motor1B,True)
        GPIO.output(Motor2B,True)
        GPIO.output(Motor1P,False)
        GPIO.output(Motor2P,False)


def backupDemo():
        #aio.send('BackupDemo',7)
        data = aio.receive('BackupDemo')
        print('Received value: {0}'.format(data.value))

        if (data.value=='1'):
                moveForward()
                time.sleep(1)
                aio.send('BackupDemo',7)
        elif (data.value=='2'):
                moveBackward()
                time.sleep(1)
                aio.send('BackupDemo',7)
        elif (data.value=='3'):
                turnToAngleL(90.0)
                #time.sleep(1)
                aio.send('BackupDemo',7)
        elif (data.value=='4'):
                turntoAngleR(90.0)
                #time.sleep(1)
                aio.send('BackupDemo',7)
        elif (data.value=='5'):
                turnLeft()
                time.sleep(1)
                aio.send('BackupDemo',7)
        elif (data.value=='6'):
                turnRight()
                time.sleep(1)
                aio.send('BackupDemo',7)
        elif (data.value=='7'):
                stopBot()
        else:
                stopBot()


                '''
def goToToPoint(current,destination):
        if(current =='A'):
                if(destination=='B'):
                        
        
        
def realDemo():
        data = aio.receive('ReadDemo')
        print('Received value: {0}'.format(data.value))
        if(data.value =='1'):
                goToPoint('A','B')
 '''     
def calibrateAngle():
        turnZeroRight()
        raw_input()
        stopBot()

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

        '''
def alexaRun:
        while(1):
                data = aio.receive('GoTo1')
                print('Received value: {0}'.format(data.value))
                if(data.value=='1'):
                        GPIO.output(3,True)
                        GPIO.output(5,False)
                elif(data.value=='2'):
                        GPIO.output(5,True)
                        GPIO.output(3,False)
                time.sleep(1)
'''

try:
        #turnToAngleL((180.00/math.pi)*math.acos(260.00/290.00))
        #moveForward()
        #time.sleep(2.9/0.6)
        aio.send('BackupDemo',7)
        while(1):
                backupDemo()

        leftMotor.stop()
        rightMotor.stop()
        GPIO.cleanup()
        
except KeyboardInterrupt:
        leftMotor.stop()
        rightMotor.stop()
        GPIO.cleanup()  
