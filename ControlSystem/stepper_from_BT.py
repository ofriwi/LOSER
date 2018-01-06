from time import sleep
from Arduino_Stepper import Arduino_BT_Stepper

stepper = Arduino_BT_Stepper()

try:
    while 1:
        x = int(input("Move:"))
        stepper.move(x)
except KeyboardInterrupt:
    print("S")
    stepper.cleanup()