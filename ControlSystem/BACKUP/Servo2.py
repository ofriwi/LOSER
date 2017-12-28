import struct
import serial

class Arduino_Servo:
    
    def __init__(self, baudrate=9600, port="/dev/ttyUSB0"):
        ser = serial.Serial()
        ser.baudrate = baudrate
        ser.port = port
        ser.open()
    
    def set_angle(self, angle):
        ser.write(struct.pack('>B', angle))
            
    def cleanup(self):
        ser.close()

