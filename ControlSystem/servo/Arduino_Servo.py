import struct
import serial

class Arduino_Servo:
    
    def __init__(self, baudrate=9600, port="/dev/ttyUSB0"):
        self.ser = serial.Serial()
        self.ser.baudrate = baudrate
        self.ser.port = port
        self.ser.open()
    
    def set_angle(self, angle):
        self.ser.write(struct.pack('>B', int(angle)))
            
    def cleanup(self):
        self.ser.close()