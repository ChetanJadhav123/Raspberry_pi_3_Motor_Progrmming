import RPi.GPIO as GPIO
from time import sleep

#GPIO.setmode(GPIO.BCM)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

while 1:
    GPIO.output(18, False)
    GPIO.output(16, True)
    sleep(10)
    GPIO.output(18, True)
    GPIO.output(16, False)
    sleep(10)


