'''
Demonstrates low level servo control with.a raspberry pi.

See this page for more details
https://rpi.science.uoit.ca/lab/servo/

This github to see how to use the servoblaster library
https://github.com/richardghirst/PiBits/tree/master/ServoBlaster

Example code for csci1951c Designing Humanity Centered Robots
Brown University

Izzy Brand (2018)
'''

import numpy as np
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # the pin numbering scheme

servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT) # configure out desired pin as output

# we want to pulse pin servo_pin at 50hz
# We need 50hz because servos PWM has a period of 20 milliseconds
p = GPIO.PWM(servo_pin, 50)

# define a function that takes in the servo angle and returns
# the percentage of the time that we should pulse the pin HIGH.
def angle_to_duty_cycle(angle):
	# duration of the pulse in milliseconds (between 1 and 2)
    pulse_duration = angle/180.0 + 1.0
    # the total length of the period is 20 milliseconds. We multiply by 100 to get percent
    return pulse_duration/20.0 * 100.0

dc = angle_to_duty_cycle(90)
p.start(dc) # turn on the PWM and set the angle to 90

try:
    while True:
        angle = np.random.randint(180) # select a random number in [0,180]
        print("Setting the servo to {} degrees".format(angle))

        dc = angle_to_duty_cycle(angle)
        p.ChangeDutyCycle(dc) # set the servo to that angle

        time.sleep(1) # sleep 1 second


# when the script stops, turn off the PWM so the servo turns off
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()