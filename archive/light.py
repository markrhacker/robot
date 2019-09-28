import CHIP_IO.GPIO as GPIO
from time import sleep

RLED = "GPIO1"
BLED = "GPIO2"

#LED Set-up
GPIO.setup(RLED, GPIO.OUT)
GPIO.setup(BLED, GPIO.OUT)

#LED on/off
GPIO.output(RLED, GPIO.HIGH)
GPIO.output(BLED, GPIO.HIGH)

GPIO.output(RLED, GPIO.LOW)
GPIO.output(BLED, GPIO.LOW)

sleep(1)

GPIO.output(RLED, GPIO.HIGH)
GPIO.output(BLED, GPIO.HIGH)




