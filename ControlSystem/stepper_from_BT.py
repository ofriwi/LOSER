from time import sleep
from Arduino_Stepper import Arduino_BT_Stepper
import select
import threading

looping = True

class StepperThread(threading.Thread):
    def run(self):
        while looping:
            x = int(input("Move:"))
            stepper.move(x)
            print("Moving: " + str(x))
    
class BTReaderThread(threading.Thread):
    def run(self):
        while looping:
            ready = select.select([stepper.sock], [], [], 0.01)
            if ready[0]:
                if (str)((stepper.sock.recv(1024))) == 'g':
                    data = (stepper.sock.recv(1024))
                    print("gyro: " + str(data))


stepper = Arduino_BT_Stepper()
try:
    stepper_th = StepperThread().start()
    reader_th = BTReaderThread().start()
    while 1:
        sleep(1)
except KeyboardInterrupt:
    looping = False
    print("Ending")
    stepper.cleanup()
