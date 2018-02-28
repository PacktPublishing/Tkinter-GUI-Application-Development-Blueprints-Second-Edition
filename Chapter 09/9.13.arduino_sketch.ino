const int triggerPin = 8;
const int echoBackPin = 7;

void setup() {
 Serial.begin(9600);
 pinMode(triggerPin, OUTPUT);
 pinMode(echoBackPin, INPUT);
}

void loop() {
  long duration, distanceIncm;
  // trigger ultrasound ping
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(triggerPin, LOW);
  // receive input from the sensor
  duration = pulseIn(echoBackPin, HIGH);

  //calculate distance
  distanceIncm = duration / 29 / 2;

  // send data over serial port
  Serial.print('distance in cm is :');
  Serial.print(distanceIncm);
  Serial.println();
  delay(100);
}
