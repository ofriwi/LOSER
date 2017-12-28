from Servo import *
from time import sleep
import Servo3

servo = Servo(3)
dt = 1
servo.set_angle(90, dt)
#servo.set_angle(175, dt)
#servo.set_angle(90, dt)
try:
    while 1:
        x = int(input("Set Angle"))
        servo.set_angle(x)
except KeyboardInterrupt:
    servo.cleanup(True)