import RPi.GPIO as GPIO
from time import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
while True:
    GPIO.output(25, GPIO.HIGH)
    sleep(3)
    GPIO.output(25, GPIO.LOW)
    sleep(3)
