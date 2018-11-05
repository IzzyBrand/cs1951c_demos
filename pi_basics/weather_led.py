'''
Showcases the capabilities of the Pi controlling an LED based on the weather

Uses this library: https://pypi.org/project/weather-api/

Requires `pip3 install weather-api` 

Example code for csci1951c Designing Humanity Centered Robots
Brown University

Izzy Brand (2018)
'''


from weather import Weather, Unit # this library enables to access yahoo weather
import RPi.GPIO as GPIO # this library enables interfacing with the GPIO (pins)

weather = Weather(unit=Unit.CELSIUS) # initalize the weather library

# setup the led
led_pin = 18 # declare a variable to store which pin to blink
GPIO.setmode(GPIO.BCM) # say how the pins are numbered (this is the most common scheme)
GPIO.setup(led_pin, GPIO.OUT) # set the led_pin as output

while True:
	user_input = input('Enter a city: ')
	location = weather.lookup_by_location(user_input)
	condition = location.condition.text

	print("Got {}. It\'s currently {}".format(location.title, condition))

	if 'cloudy' in condition.lower():
		GPIO.output(led_pin, GPIO.HIGH)
		print('Yep, it\'s cloudy')
	else:
		GPIO.output(led_pin, GPIO.LOW)
		print('No clouds here!')