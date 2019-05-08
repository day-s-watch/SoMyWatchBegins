import RPi.GPIO as GPIO
import time


def gpiosetout(value, pin):
    GPIO.setmode(GPIO.BOARD)  # using BOARD Num, and also GPIO.BCM
    GPIO.setup(pin, GPIO.OUT)  # set pin Num as output
    if value:
        GPIO.output(pin, GPIO.HIGH)  # open GPIO as HIGH
    else:
        GPIO.output(pin, GPIO.LOW)  # close GPIO as LOW
