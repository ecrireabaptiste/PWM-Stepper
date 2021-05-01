import ModuleStepper
import RPi.GPIO as GPIO
import threading
import time

GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)

STEPS360 = 200
RESOLUTION = {1 : (0, 0, 0),
              2 : (1, 0, 0),
              4 : (0, 1, 0),
              8 : (1, 1, 0),
              16: (0, 0, 1),
              32: (1, 0, 1)}

DIR1 = 20
STEP1 = 15
SLEEP1 = 16
MICROSTEP1 = (12, 7, 8)

DIR2 = 9
STEP2 = 11
SLEEP2 = 10
MICROSTEP2 = (22, 27, 17)

MS = 4
FREQ = 1700
DIFF = 0
DTY = 50

#Setup Stepper 
GPIO.setup(SLEEP1, GPIO.OUT)
GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(MICROSTEP1, GPIO.OUT)
GPIO.setup(STEP1, GPIO.OUT)
GPIO.output(MICROSTEP1, RESOLUTION[MS])
GPIO.output(STEP1, GPIO.LOW)
GPIO.output(SLEEP1, GPIO.HIGH)


GPIO.setup(SLEEP2, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(MICROSTEP2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)
GPIO.output(MICROSTEP2, RESOLUTION[MS])
GPIO.output(STEP2, GPIO.LOW)
GPIO.output(SLEEP2, GPIO.HIGH)

FREQ1 = FREQ+DIFF
FREQ2 = FREQ-DIFF

if FREQ1>0:
    DIRECTION1 = 1
else:
    DIRECTION1 = 0

if FREQ2>0:
    DIRECTION2 = 0
else:
    DIRECTION2 = 1



#Launch Steppers

pwm1 = GPIO.PWM(STEP1, 1)
pwm1.ChangeDutyCycle(DTY)
pwm1.ChangeFrequency(abs(FREQ1))
GPIO.output(DIR1, DIRECTION1)

pwm2 = GPIO.PWM(STEP2, 1)
pwm2.ChangeDutyCycle(DTY)
pwm2.ChangeFrequency(abs(FREQ2))
GPIO.output(DIR2, DIRECTION2)

pwm1.start(DTY)
pwm2.start(DTY)




time.sleep(5)


#Setdown All Steppers
pwm1.stop()
GPIO.output(STEP1, GPIO.LOW)
GPIO.output(SLEEP1, GPIO.HIGH)
pwm2.stop()
GPIO.output(STEP2, GPIO.LOW)
GPIO.output(SLEEP2, GPIO.HIGH)
GPIO.cleanup()

print('Done')