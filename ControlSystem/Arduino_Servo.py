import struct
import serial
from Constants import *

class Arduino_Servo:
    
    # Initialize communication
    def __init__(self, baudrate=9600, port=SERVO_PORT):
        self.ser = serial.Serial()
        self.ser.baudrate = baudrate
        self.ser.port = port
        self.ser.open()
    
    # Rotate servo 
    def set_angle(self, angle, limit_angle=True):
        if limit_angle:
            angle = int(self.crop(int(angle), SERVO_MIN_DEG, SERVO_MAX_DEG))
        if DEBUG_MODE or SERVO_DEBUG_MODE:
            print("Servo set to", angle)
        self.ser.write(struct.pack('>B', angle))
        return angle

    # Change dt of the servo
    def set_dt(self, dt):
        if DEBUG_MODE or SERVO_DEBUG_MODE:
            print("Servo set dt to", dt)
        self.ser.write(struct.pack('>B', int(dt)+200))
        
    
    # Get an angle (0<=angle<=180)
    @staticmethod
    def crop(val, min_val=0, max_val=180):
        if val > max_val:
            val = max_val
        if val < min_val:
            val = min_val
        return val
    
    #Close serial
    def cleanup(self):
        self.ser.close()
