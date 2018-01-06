
//Declare pin functions on Redboard
#define stp 8
#define dir 9
#define MS1 10
#define MS2 11
#define MS3 4
#define EN  12
int step_mode = 1;
int steps_per_revolution = 400;
int dt = 1;
int offset = 128;

int i = 0;
int step_modes[] = {1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8};
int dts[] = {1, 3, 5, 7, 10, 1, 3, 5, 7, 10, 1, 3, 5, 7, 10, 1, 3, 5, 7, 10, 1, 3, 5, 7, 10};

//Declare variables for functions
int x;
int y;
int state;


void setup() {
  pinMode(stp, OUTPUT);
  pinMode(dir, OUTPUT);
  pinMode(MS1, OUTPUT);
  pinMode(MS2, OUTPUT);
  pinMode(MS3, OUTPUT);
  pinMode(EN, OUTPUT);
  resetEDPins(); //Set step, direction, microstep and enable pins to default states
  Serial.begin(9600); //Open Serial connection for debugging
}

//Main loop
void loop() {
  if(Serial.available() > 0){
    while(Serial.available() > 1){
      Serial.read();
    }//     WAIT FOR LAST INPUT*/
    int user_input = (int)Serial.read(); //Read user input and trigger appropriate function
    if (user_input == -1){
      i++;
      dt = dts[i];
      step_mode = step_modes[i];
      Serial.print(dt + ", " + step_mode);
    }else{
      digitalWrite(EN, LOW); //Pull enable pin low to allow motor control
      //sSerial.print(user_input);
      Step(user_input);
      resetEDPins();
    }
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
  //digitalWrite(MS3, LOW);
  //digitalWrite(EN, HIGH);
}

void Step(int angle){
  angle -= offset;
  int steps = int(angle/360.0*steps_per_revolution * step_mode);
  //Serial.print(steps);
  if (steps > 0){
    digitalWrite(dir, LOW);
  }else{
    digitalWrite(dir, HIGH);
  }
  for(x = 0; x<abs(steps); x++)  //Loop the forward stepping enough times for motion to be visible
  {
    //Serial.print("s");
    digitalWrite(stp,HIGH); //Trigger one step forward
    delay(dt);
    digitalWrite(stp,LOW); //Pull step pin low so it can be triggered again
    delay(dt);
  }
}
