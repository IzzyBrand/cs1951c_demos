/*
 * Demonstrates using the L298N motor controller with mixed speeds and
 * directions.
 * 
 * See this example for help setting upt the L298N motor controller
 * https://howtomechatronics.com/tutorials/arduino/arduino-dc-motor-control-tutorial-l298n-pwm-h-bridge/
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


void setup () {
  // set up the motor pins
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
}

void loop() {
  // pick a random speed for each motor 
  int m1 = random(-255, 255);
  int m2 = random(-255, 255);

  // decide which direction the motors will spin (negative is backwards)
  int m1Direction = m1 > 0;
  int m2Direction = m2 > 0;

  // send out the command to motor 1
  digitalWrite(IN1,  m1Direction); // set one pin high
  digitalWrite(IN2, !m1Direction); // and the other low
  analogWrite(ENA, abs(m1));       // and use the third to control speed
  
  // send out the command to motor 2
  digitalWrite(IN3,  m2Direction);
  digitalWrite(IN4, !m2Direction);
  analogWrite(ENB, abs(m2));

  delay(1000);
}

