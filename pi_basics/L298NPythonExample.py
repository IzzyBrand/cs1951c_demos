
'''
Demonstrates interfacing with the L298N motor driver on the raspberry Pi.

Thanks to Reet and Justin for the code!

Example code for csci1951c Designing Humanity Centered Robots
Brown University
Izzy Brand (2018)
'''

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

# dc = 50

# p7 = GPIO.PWM(7, 100)
# p13 = GPIO.PWM(13, 100)
# p11 = GPIO.PWM(11, 100)
# p15 = GPIO.PWM(15, 100)

# p11.start(dc)
# p15.start(dc)


dc = 50
p12 = GPIO.PWM(12, 300)
p23 = GPIO.PWM(23, 300)
p12.start(dc)
p23.start(dc)


GPIO.output(7,False)
GPIO.output(11,False)
GPIO.output(13,False)
GPIO.output(15,False)

print 'Forward'
GPIO.output(7,True)
GPIO.output(13, True)
time.sleep(2)

print 'Stop'

GPIO.output(7,False)
GPIO.output(13,False)
time.sleep(2)

print 'Backward'

GPIO.output(11,True)
GPIO.output(15,True)
time.sleep(2)

print 'Stop'

GPIO.output(11,False)
GPIO.output(15,False)
GPIO.cleanup()
