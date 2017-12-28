from Servo import *
from time import sleep
import Servo3

servo = Servo(3)
dt = 1
servo.set_angle(90, dt)
#servo.set_angle(175, dt)
#servo.set_angle(90, dt)
servo.cleanup(True)
'''
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass

'''