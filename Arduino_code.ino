
/*
 * 
 Created 4/12/2021 By Michael
 
 Controls an RC quadrotor via PC serial port

 Pins PWM 6, 9, 10, and 11 are used to control the quadrotor


 The circuit:
 * The quadrotor remote controller is connected to Arduino PWM pins PWM 6, 9, 10, and 11 via low pass filter
 * Arduino UNO is used
 * The remote takes its vcc and GND from an external adapter
 * Note: on most Arduinos there is already an LED on the board
 attached to pin 13.
 */



// constants won't change. They're used here to set pin numbers:
const int HeightPin =  11;      // The pin used to control the height
const int XPin =  10;      // The pin used to control the move along x-axis
const int YPin =  9;      // The pin used to control the move along y-axis
const int YawPin =  6;      // The pin used to control the heading

int CommandByte = 0;   // Command received via serial port
int HeightValue = 0; // The height value, between 0-200
int XValue = 0; // The X value, between 0-200
int YValue = 0; // The Y value, between 0-200
int YawValue = 0; // The Yaw value, between 0-200

int Startflag = 0; // A flag showing the first loop

// Initialize pins
void setup() {
// sets the PWM pins as output  
pinMode(HeightPin, OUTPUT); 
pinMode(XPin, OUTPUT); 
pinMode(YPin, OUTPUT); 
pinMode(YawPin, OUTPUT);      

// Initialize serial port
Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
}

// Repeat
void loop() {
// At the start, HeightValue = 0, XValue = 1.7v, YValue = 1.7v, and YawValue = 1.7v (1.7v is the middle value => position is zero)
// This means that no motion is required
if (Startflag = 0) 
    {
     HeightValue = 0; // Height is zero
     // Send this data to the remote control as PWM signal via Low Pass Filter
     analogWrite(HeightPin, HeightValue);  // no motion along z-axis     
     XValue = 85; // 0 value for X position
     // Send this data to the remote control as PWM signal via Low Pass Filter
     analogWrite(XPin, XValue);  // Do not move along the x-axis
     //////////
     YValue = 85; // 0 value for Y position
     // Send this data to the remote control as PWM signal via Low Pass Filter
     analogWrite(YPin, YValue);  // Do not move along the y-axis
     //////////
     YawValue = 85; // 0 value for the yaw angle
     // Send this data to the remote control as PWM signal via Low Pass Filter
     analogWrite(YawPin, YawValue);  // Do not turn 
     //////////    
      Startflag = 1; // So that the code does not enter to this function anymore
    }

// ============================================================================
    
// Now control the quadrotor using the serial port commands    
// Whenever a byte is received via serial port
if (Serial.available() > 0) 
    {
      // Read the incoming byte:
      CommandByte = Serial.read();
      // Perform the commands
      
      // Stop is received
      if (CommandByte == 'S') 
    {
     HeightValue = 0; // Height is zero
     // Send this data to the remote control as PWM signal via Low Pass Filter
     analogWrite(HeightPin, HeightValue);  // no motion along z-axis     
     XValue = 85; // 0 value for X position
     // Send this data to the remote control as PWM signal via Low Pass Filter
     analogWrite(XPin, XValue);  // Do not move along the x-axis
     //////////
     YValue = 85; // 0 value for Y position
     // Send this data to the remote control as PWM signal via Low Pass Filter
     analogWrite(YPin, YValue);  // Do not move along the y-axis
     //////////
     YawValue = 85; // 0 value for the yaw angle
     // Send this data to the remote control as PWM signal via Low Pass Filter
     analogWrite(YawPin, YawValue);  // Do not turn 
    } 
    
      // UP command is received, and max height command is not reached
      // if (CommandByte == 'U' && HeightValue < 200) 
        if (CommandByte == 'U' && HeightValue < 170) // we put 170 because at this value we have the max voltage allowed = 3.71
        {
          HeightValue = HeightValue + 10; // Increase the quadrotor's height
          // Send this data to the remote control as PWM signal via Low Pass Filter
          analogWrite(HeightPin, HeightValue);  // Go Up
        }
        
       // DOWN command is received, and min height command is not reached
      if (CommandByte == 'D' && HeightValue > 10) 
        {
          HeightValue = HeightValue - 10; // Decrease the quadrotor's height
          // Send this data to the remote control as PWM signal via Low Pass Filter
          analogWrite(HeightPin, HeightValue);  // Go Down
        }     

// ============================================================================
         

      // Go forward command is received, and max forward command is not reached
      if (CommandByte == 'F' && XValue < 170) // we put 170 because at this value we have the max voltage allowed = 3.71 
        {
          XValue = XValue + 10; // Increase the quadrotor's forward command
          // Send this data to the remote control as PWM signal via Low Pass Filter
          analogWrite(XPin, XValue);  // Go Forward
        }
        
       // Go backward is received, and min forward command is not reached
      if (CommandByte == 'B' && XValue > 10) 
        {
          XValue = XValue - 10; // Decrease the quadrotor's forward command
          // Send this data to the remote control as PWM signal via Low Pass Filter
          analogWrite(XPin, XValue);  // Go Backward
        }      


// ============================================================================
         

      // Go right command is received, and max right command is not reached
      if (CommandByte == 'R' && YValue < 170) // we put 170 because at this value we have the max voltage allowed = 3.71 
        {
          YValue = YValue + 10; // Decrease the quadrotor's right command
          // Send this data to the remote control as PWM signal via Low Pass Filter
          analogWrite(YPin, YValue);  // Go Right
        }
        
       // Go left is received, and max left command is not reached
      if (CommandByte == 'L' && YValue > 10) 
        {
          YValue = YValue - 10; // Increase the quadrotor's left command
          // Send this data to the remote control as PWM signal via Low Pass Filter
          analogWrite(YPin, YValue);  // Go Left
        }      



// ============================================================================
         

      // Turn heading right command is received, and max right command is not reached
      if (CommandByte == 'C' && YawValue < 170) // we put 170 because at this value we have the max voltage allowed = 3.71 
        {
          YawValue = YawValue + 10; // Decrease the quadrotor's yaw right command
          // Send this data to the remote control as PWM signal via Low Pass Filter
          analogWrite(YawPin, YawValue);  // Turn Clock-wise
        }
        
       // Turn heading left is received, and max left command is not reached
      if (CommandByte == 'W' && YawValue > 10) 
        {
          YawValue = YawValue - 10; // Increase the quadrotor's yaw left command
          // Send this data to the remote control as PWM signal via Low Pass Filter
          analogWrite(YawPin, YawValue);  // Turn Counter clock-wise
        }      

      // delay(1000);                  // waits for a second
    }
}
