
import RPi.GPIO as GPIO
import time

Motor1F = 18
Motor1P = 16
Motor1B = 12
Motor2F = 15
Motor2P = 13
Motor2B = 11

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Motor1F,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1P,GPIO.OUT)
    GPIO.setup(Motor2F,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(Motor2P,GPIO.OUT)
    GPIO.output(Motor1B,True)
    GPIO.output(Motor2B,True)

def stopBot():
    #GPIO.output(Motor1F,False)
    #GPIO.output(Motor2F,True)
    GPIO.output(Motor1B,True)
    GPIO.output(Motor2B,True)
    GPIO.output(Motor1P,False)
    GPIO.output(Motor2P,False)

try:
    setup()
    stopBot()
    GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanup()
            

