import struct
import serial
from Constants import *
from time import sleep


offset = 128

class Arduino_Stepper:

    FULL_STEP = 1
    HALF_STEP = 2

    # Initialize communication
    def __init__(self, baudrate=9600, port=STEPPER_PORT):
        self.ser = serial.Serial()
        self.ser.baudrate = baudrate
        self.ser.port = port
        self.ser.open()
    
    # Rotate servo 
    def move(self, angle, step_mode=FULL_STEP, limit_angle=True):
        # Convension: send angle + 128
        if limit_angle:
            angle = int(self.crop(int(angle), STEPPER_MIN_STEP_DEG, STEPPER_MAX_STEP_DEG))
        angle += offset
        if DEBUG_MODE or STEPPER_DEBUG_MODE:
            print("Stepper move", angle-offset, "degrees")
        self.ser.write(struct.pack('>B', angle))
 
     # Get an angle (0<=angle<=180)
    @staticmethod
    def crop(val, min_val=-128, max_val=127):
        if val > max_val:
            val = max_val
        if val < min_val:
            val = min_val
        return val
    
    #Close serial
    def cleanup(self):
        self.move(0)
        self.ser.close()
