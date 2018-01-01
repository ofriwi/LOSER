
//Declare pin functions on Redboard
#define stp 8
#define dir 9
#define MS1 10
#define MS2 11
#define EN  12
int step_mode = 2;
int steps_per_revolution = 400;
int dt = 3;
int offset = 128;


//Declare variables for functions
int x;
int y;
int state;


void setup() {
  pinMode(stp, OUTPUT);
  pinMode(dir, OUTPUT);
  pinMode(MS1, OUTPUT);
  pinMode(MS2, OUTPUT);
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
    digitalWrite(EN, LOW); //Pull enable pin low to allow motor control
    //sSerial.print(user_input);
    Step(user_input);
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
  digitalWrite(EN, HIGH);
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

/*
//Default microstep mode function
void StepForwardDefault()
{
  Serial.println("Moving forward at default step mode.");
  digitalWrite(dir, LOW); //Pull direction pin low to move "forward"
  for(x= 1; x<400; x++)  //Loop the forward stepping enough times for motion to be visible
  {
    digitalWrite(stp,HIGH); //Trigger one step forward
    delay(3);
    digitalWrite(stp,LOW); //Pull step pin low so it can be triggered again
    delay(3);
  }
  Serial.println("Enter new option");
  Serial.println();
}

//Reverse default microstep mode function
void ReverseStepDefault()
{
  Serial.println("Moving in reverse at default step mode.");
  digitalWrite(dir, HIGH); //Pull direction pin high to move in "reverse"
  for(x= 1; x<400; x++)  //Loop the stepping enough times for motion to be visible
  {
    digitalWrite(stp,HIGH); //Trigger one step
    delay(3);
    digitalWrite(stp,LOW); //Pull step pin low so it can be triggered again
    delay(3);
  }
  Serial.println("Enter new option");
  Serial.println();
}

// 1/8th microstep foward mode function
void SmallStepMode()
{
  Serial.println("Stepping at 1/8th microstep mode.");
  digitalWrite(dir, LOW); //Pull direction pin low to move "forward"
  digitalWrite(MS1, HIGH); //Pull MS1, and MS2 high to set logic to 1/8th microstep resolution
  digitalWrite(MS2, HIGH);
  for(x= 1; x<400*8; x++)  //Loop the forward stepping enough times for motion to be visible
  {
    digitalWrite(stp,HIGH); //Trigger one step forward
    delay(2);
    digitalWrite(stp,LOW); //Pull step pin low so it can be triggered again
    delay(2);
  }
  Serial.println("Enter new option");
  Serial.println();
}

//Forward/reverse stepping function
void ForwardBackwardStep()
{
  Serial.println("Alternate between stepping forward and reverse.");
  for(x= 1; x<5; x++)  //Loop the forward stepping enough times for motion to be visible
  {
    //Read direction pin state and change it
    state=digitalRead(dir);
    if(state == HIGH)
    {
      digitalWrite(dir, LOW);
    }
    else if(state ==LOW)
    {
      digitalWrite(dir,HIGH);
    }
    
    for(y=1; y<1000; y++)
    {
      digitalWrite(stp,HIGH); //Trigger one step
      delay(1);
      digitalWrite(stp,LOW); //Pull step pin low so it can be triggered again
      delay(1);
    }
  }
  Serial.println("Enter new option:");
  Serial.println();
}*/
