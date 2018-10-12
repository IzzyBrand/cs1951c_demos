/*
 * Controls a robot using the L298N motor controller and an HC-SR04 ultasonic
 * sensor. The vehicle should drive forward until it sees an obstacle and then turn
 * before continuing to drive forward.
 * 
 * Example code for csci1951c Designing Humanity Centered Robots
 * Brown University
 * 
 * Izzy Brand (2018)
 */

#define IN1 7
#define IN2 8
#define IN3 12
#define IN4 13
#define ENA 5
#define ENB 6
#define trigPin 9
#define echoPin 10

void setup () {
  // set up the motor pins
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  setMotors(0, 0); // and stop the motors if they are already spinning
  
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  Serial.begin(9600); // Starts the serial communication
}

void loop() {
  float distance = readUltrasonicSensor();
  if (distance > 100) {
    // drive forwards at full speed if there is no obstacle
    setMotors(1, 1);
  } else {
    // slow down and turn if there is an obstacle
    setMotors(distance/100.0, distance/50.0 - 1);
  }
}

/*
 * Reads a distance in centimeters from the ultrasonic sensor
 * 
 * Returns
 *  distance (float): the distance in centimeters
 */
float readUltrasonicSensor() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  long duration = pulseIn(echoPin, HIGH);
  return duration*0.034/2; // Calculating the distance
}

/*
 * Set the motors using the L298N HBridge motor controller
 * 
 * Arguments
 *  m1 (float): the speed to set motor 1. Ranges -1 to 1
 *  m2 (float): the speed to set motor 2. Ranges -1 to 1
 */
void setMotors(float m1, float m2) {
  digitalWrite(IN1, m1 <= 0);
  digitalWrite(IN2, m1 > 0);
  digitalWrite(IN3, m2 <= 0);
  digitalWrite(IN4, m2 > 0);
  analogWrite(ENA, abs(m1) * 255);
  analogWrite(ENB, abs(m2) * 255);
}



