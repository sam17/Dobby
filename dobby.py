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


GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor1F,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1P,GPIO.OUT)
GPIO.setup(Motor2F,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2P,GPIO.OUT)
aio = Client('47bc88002f0a4117a751a1074e25fa96')
leftMotor = GPIO.PWM(Motor2P,100)
rightMotor = GPIO.PWM(Motor1P,100)
leftMotor.start(0)
rightMotor.start(0)
GPIO.output(Motor1B,True)
GPIO.output(Motor2B,True)
leftMotor.ChangeDutyCycle(10.0)
rightMotor.ChangeDutyCycle(20.0)
        

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
        data = aio.receive('BackupDemo')
        if (data.value=='1'):
                moveForward()
        elif (data.value=='2'):
                moveBackward()
        elif (data.value=='3'):
                turnZeroLeft()
        elif (data.value=='4'):
                turnZeroRight()
        elif (data.value=='5'):
                turnLeft()
        elif (data.value=='6'):
                turnRight()
        elif (data.value=='7'):
                stopBot()

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
        moveForward()
        time.sleep(3)
        #calibrateAngle()
        #time.sleep(3)
        #testWSAD()
        
except KeyboardInterrupt:
        leftMotor.stop()
        rightMotor.stop()
        GPIO.cleanup()  
