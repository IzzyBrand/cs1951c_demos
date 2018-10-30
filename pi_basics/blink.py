'''
Demonstrates how to blink an LED using the RPi.GPIO library.

See this tutorial for more details
https://learn.sparkfun.com/tutorials/raspberry-gpio/python-rpigpio-api

Example code for csci1951c Designing Humanity Centered Robots
Brown University

Izzy Brand (2018)
'''

import RPi.GPIO as GPIO # this library enables interfacing with the GPIO (pins)
from time import sleep # this library gives delay functionality

led_pin = 18 # declare a variable to store which pin to blink

# setup the pin
GPIO.setmode(GPIO.BCM) # say how the pins are numbered (this is the most common scheme)
GPIO.setup(led_pin, GPIO.OUT) # set the led_pin as output

# blink in a loop
while True:
    GPIO.output(18, GPIO.HIGH)
    print "Pin", led_pin, "ON"
    sleep(1)
    GPIO.output(18, GPIO.LOW)
    print "Pin", led_pin, "OFF"
    sleep(1)

