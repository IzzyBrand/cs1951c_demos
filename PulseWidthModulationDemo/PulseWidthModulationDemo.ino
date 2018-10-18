/*
 * Demonstrates Pulse Width Modulation (PWM) by using two
 * potentiometers to set the frequency and ratio
 * 
 * Example code for csci1951c Designing Humanity Centered Robots
 * Brown University
 * 
 * Izzy Brand (2018)
 */

#define FREQ_PIN A0
#define RATIO_PIN A1
#define LED_PIN 4

void setup() {
  // put your setup code here, to run once:
  pinMode(FREQ_PIN, INPUT);
  pinMode(RATIO_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  // read in the data
  int frequency = analogRead(FREQ_PIN)/1025.0 * 70;  // frequency in Hz (ranges from 0 to 70)
  float ratio = analogRead(RATIO_PIN)/1023.0;        // ratio ranges from 0 to 1

  // calculate how long to keep the LED on
  int onTime = 1000.0/frequency * ratio;             // milliseconds to keep the LED on
  int offTime = 1000.0/frequency * (1.0 - ratio);    // milliseconds to keep the LED off

  // Print everything!
  Serial.print(frequency);
  Serial.print("\t");
  Serial.print(ratio);
  Serial.print("\t");
  Serial.print(onTime);
  Serial.print("\t");
  Serial.println(offTime);

  // and turn the LED on and off
  digitalWrite(LED_PIN, HIGH);
  delay(onTime);
  digitalWrite(LED_PIN, LOW);
  delay(offTime);
}

