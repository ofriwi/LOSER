from time import sleep
from Arduino_Servo import Arduino_Servo

servo = Arduino_Servo()
dt = 1
servo.set_angle(90)
#servo.set_angle(175, dt)
#servo.set_angle(90, dt)
try:
    while 1:
        x = int(input("Set Angle"))
        servo.set_angle(x)
except KeyboardInterrupt:
    print("S")
    servo.cleanup()