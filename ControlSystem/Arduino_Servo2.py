import struct
import serial

class Arduino_Servo:
    
    # Initialize communication
    def __init__(self, baudrate=9600, port="/dev/ttyUSB0"):
        self.ser = serial.Serial()
        self.ser.baudrate = baudrate
        self.ser.port = port
        self.ser.open()
    
    # Rotate servo 
    def set_angle(self, angle, limit_angle=True):
        if limit_angle:
            angle = int(self.crop(int(angle), 0, 180))
        print("angle=" + str(angle))
        self.ser.write(struct.pack('>B', int(angle)))
    
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