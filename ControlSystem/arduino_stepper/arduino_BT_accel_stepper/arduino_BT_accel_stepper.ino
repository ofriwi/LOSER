#include <MPU9250.h>
#include <SoftwareSerial.h>
#include <AccelStepper.h>


//Declare pin functions on Redboard
#define stp 8
#define dir 9
#define MS1 10
#define MS2 11
#define EN  12

int step_mode = 8;
int steps_per_revolution = 400;
int offset = 128;
bool input = false;
int angle;
int ratio = 110/90*360*step_mode/steps_per_revolution;

//For the Gyro
MPU9250 myIMU;
float gyro_val = 0.0;

//sending to pi
int btdata; // the data given from the computer
char receivedChar;
bool newData = false;

//BT
SoftwareSerial bt (5, 6);
AccelStepper stepper(AccelStepper::DRIVER, stp, dir);


void setup() {
  //stepper.setMaxSpeed(3000);
  //stepper.setAcceleration(2500);
  stepper.setMaxSpeed(200);//2000
  stepper.setAcceleration(100);//1400
  
  pinMode(MS1, OUTPUT);
  pinMode(MS2, OUTPUT);
  setStepMode();
  stepper.setEnablePin(EN);
  stepper.setPinsInverted(false, false, true);
  stepper.enableOutputs();
  
  Serial.begin(9600); //Open Serial connection for debugging
  bt.begin(9600);

  //Gyro setup
  byte c = myIMU.readByte(MPU9250_ADDRESS, WHO_AM_I_MPU9250);
  if (c == 0x71) // WHO_AM_I should always be 0x68
  {

    // Start by performing self test and reporting values
    myIMU.MPU9250SelfTest(myIMU.SelfTest);
//    Serial.print("x-axis self test: gyration trim within : ");
//    Serial.print(myIMU.SelfTest[3],1); Serial.println("% of factory value");
//    Serial.print("y-axis self test: gyration trim within : ");
//    Serial.print(myIMU.SelfTest[4],1); Serial.println("% of factory value");
//    Serial.print("z-axis self test: gyration trim within : ");
//    Serial.print(myIMU.SelfTest[5],1); Serial.println("% of factory value");

    // Calibrate gyro and accelerometers, load biases in bias registers
    myIMU.calibrateMPU9250(myIMU.gyroBias, myIMU.accelBias);


    myIMU.initMPU9250();


  } // if (c == 0x71)
  else
  {
    Serial.print("Could not connect to MPU9250: 0x");
    Serial.println(c, HEX);
    while(1) ; // Loop forever if communication doesn't happen
  }

}

//Main loop
void loop() {
  // Get data from BT
  input = false;
  if(bt.available() > 0){
    while(bt.available() > 1){
      bt.read();
    }//     WAIT FOR LAST INPUT 
    angle = (int)bt.read() - offset; //Read user input and trigger appropriate function
    input = true;
  }
  
  //Gyro reading 
  myIMU.delt_t = millis() - myIMU.count;
    if (myIMU.delt_t > 20)
    {
     gyro_val = myIMU.gz;
     myIMU.count = millis();
     bt.write(receivedChar);
     }
     
  //get a char from serial
//   if (Serial.available() > 0) { 
//     receivedChar = Serial.read();
//     newData = true;
//   }
//    if (newData) {
//     Serial.println(String(receivedChar));
//     newData = false;
//     bt.write(receivedChar);
//    }
    
  /*
  // Get data from serial (for debugging)
  if(Serial.available() > 0){
    while(Serial.available() > 1){
      Serial.read();
    }//     WAIT FOR LAST INPUT 
    angle = (int)Serial.parseInt(); //Read user input and trigger appropriate function
    input = true;
  }*/

  // Move the stepper
  if (input){
    Serial.println(angle);
    stepper.move(angle*ratio);
  }
  if (stepper.distanceToGo() != 0){
    stepper.run();
  }

   
  
}
void setStepMode(){
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
/*
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
*/
