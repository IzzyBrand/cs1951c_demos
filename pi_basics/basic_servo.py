'''
Demonstrates low level servo control with.a raspberry pi.

NOTE: this is not how you will want to control a servo in general! Check out

This tutorial for a more typical use
https://learn.adafruit.com/adafruits-raspberry-pi-lesson-8-using-a-servo-motor

This github to see how to use the servoblaster library
https://github.com/richardghirst/PiBits/tree/master/ServoBlaster

Example code for csci1951c Designing Humanity Centered Robots
Brown University

Izzy Brand (2018)
'''

import RPi.GPIO as GPIO # this library enables interfacing with the GPIO (pins)
from time import sleep # this library gives delay functionality
import numpy as np # the math library for python

servo_pin = 18 # declare a variable to store which pin to blink

# setup the pin
GPIO.setmode(GPIO.BCM) # say how the pins are numbered (this is the most common scheme)
GPIO.setup(servo_pin, GPIO.OUT) # set the led_pin as output

delay_between_pulses = 0.02 # 20 milliseconds
min_pulse_duration = 1000
max_pulse_duration = 2000

# blink in a loop
while True:
	pulse_duration = np.random.randint(min_pulse_duration, max_pulse_duration) # get a random servo angle
        print "Setting servo to", pulse_duration

	# send 50 pulses (corresponds to about 1 second)
	for i in range(50):
	    GPIO.output(servo_pin, GPIO.HIGH)
	    sleep(pulse_duration * 1e-6)
	    GPIO.output(servo_pin, GPIO.LOW)
	    sleep(delay_between_pulses)

