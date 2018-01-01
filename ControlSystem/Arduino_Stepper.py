import struct
import serial
from Constants import *
from time import sleep


offset = 128

class Arduino_Stepper:

    FULL_STEP = 1
    HALF_STEP = 2

    # Initialize communication
    def __init__(self, baudrate=9600, port="/dev/ttyUSB0"):
        self.ser = serial.Serial()
        self.ser.baudrate = baudrate
        self.ser.port = port
        self.ser.open()
    
    # Rotate servo 
    def move(self, angle, step_mode=FULL_STEP):
        # Convension: send angle + 128
        angle += offset
        if DEBUG_MODE or SERVO_DEBUG_MODE:
            print("Stepper move", angle-offset, "degrees")
        self.ser.write(struct.pack('>B', angle))
 
    #Close serial
    def cleanup(self):
        self.ser.close()
