#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
int wait = 5;  // delay after servo rotation

void setup() {
  Serial.begin(9600);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  if(Serial.available() > 0){
    int input = (int)Serial.read();
    if(input >= 200){
      wait = input - 200;
    }else{
      myservo.write(input);
    }
    delay(wait);
  }
}

