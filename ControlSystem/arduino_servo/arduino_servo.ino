#include <Servo.h>
#define enb 2

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
int wait = 2;  // delay after servo rotation

void setup() {
  Serial.begin(9600);
  myservo.attach(7);  // attaches the servo on pin 9 to the servo object
  //pinMode(enb, OUTPUT);
  //digitalWrite(enb, LOW);
}

void loop() {
  if(Serial.available() > 0){
    /*while(Serial.available() > 1){
      Serial.read();
    }     WAIT FOR LAST INPUT*/
    int input = (int)Serial.read();
    Serial.print(input);
    if(input >= 200){
      wait = input - 200;
    }else{
      //digitalWrite(enb, LOW);
      //Serial.print(input);
      myservo.write(input);
    Serial.print(input);
    }
    delay(wait);
    //digitalWrite(enb, HIGH);
  }
}

