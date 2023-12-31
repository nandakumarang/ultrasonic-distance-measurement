const int trigPin = 9;  // Trigger pin of ultrasonic sensor
const int echoPin = 10; // Echo pin of ultrasonic sensor

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // Triggering the ultrasonic sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Reading the echo pin
  long duration = pulseIn(echoPin, HIGH);

  // Calculating distance in centimeters
  int distance = duration * 0.034 / 2;

  // Sending distance data to the serial port
  Serial.print(distance);
  Serial.print(",");
  Serial.println(duration);

  delay(1000); // Wait for a second before the next measurement
}
