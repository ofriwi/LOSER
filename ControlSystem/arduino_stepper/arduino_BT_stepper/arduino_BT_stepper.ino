#include <SoftwareSerial.h>
//Declare pin functions on Redboard
#define stp 8
#define dir 9
#define MS1 10
#define MS2 11
#define EN  12
int step_mode = 2;
int steps_per_revolution = 400;
int dt = 7;
int offset = 128;

//Declare variables for functions
int x;
int y;
int state;

//BT
SoftwareSerial bt (5, 6);

void setup() {
  pinMode(stp, OUTPUT);
  pinMode(dir, OUTPUT);
  pinMode(MS1, OUTPUT);
  pinMode(MS2, OUTPUT);
  pinMode(EN, OUTPUT);
  digitalWrite(EN, LOW);
  resetEDPins(); //Set step, direction, microstep and enable pins to default states
  Serial.begin(9600); //Open Serial connection for debugging
  bt.begin(9600);
}

//Main loop
void loop() {
  if(bt.available() > 0){
    while(bt.available() > 1){
      bt.read();
    }//     WAIT FOR LAST INPUT */
    int user_input = (int)bt.read(); //Read user input and trigger appropriate function
    int angle = user_input - offset;
    Serial.println(angle);
    Step(angle);
    resetEDPins();
  }
}

//Reset Easy Driver pins to default states
void resetEDPins()
{
  digitalWrite(stp, LOW);
  digitalWrite(dir, LOW);
  if (step_mode == 1){
    digitalWrite(MS1, LOW);
    digitalWrite(MS2, LOW);
  }else if (step_mode == 2){
    digitalWrite(MS1, HIGH);
    digitalWrite(MS2, LOW);
  }else if (step_mode == 4){
    digitalWrite(MS1, LOW);
    digitalWrite(MS2, HIGH);
  }else if (step_mode == 8){
    digitalWrite(MS1, HIGH);
    digitalWrite(MS2, HIGH);
  }
}

void Step(int angle){
  int steps = int(angle/360.0*steps_per_revolution * step_mode);
  //Serial.print(steps);
  if (steps > 0){
    digitalWrite(dir, LOW);
  }else{
    digitalWrite(dir, HIGH);
  }
  for(x = 0; x<abs(steps); x++)  //Loop the forward stepping enough times for motion to be visible
  {
    digitalWrite(stp,HIGH); //Trigger one step forward
    delay(dt);
    digitalWrite(stp,LOW); //Pull step pin low so it can be triggered again
    delay(dt);
  }
  Serial.println("Ready");
}
