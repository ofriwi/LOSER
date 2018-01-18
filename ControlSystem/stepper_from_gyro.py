from time import sleep
from Arduino_Stepper import Arduino_BT_Stepper
import select
import threading

from Constants import *
from stepper_pid import *

looping = True
gyro_input = None

P = 13
I = 0.003
D = 0.02
stepper = stepper_pid(P, I, D, 0) #motor

class StepperThread(threading.Thread):
    def run(self):
        while looping:
            x = int(input("Move:"))
            stepper.move(x)
            print("Moving: " + str(x))
    
class BTReaderThread(threading.Thread):
    def run(self):
        while looping:
            ready = select.select([stepper.stepper.sock], [], [], 0.01)
            if ready[0]:
                if (str)((stepper.stepper.sock.recv(1024))) == 'g':
                    data = (stepper.stepper.sock.recv(1024))
                    gyro_input = (float)(data)
                    stepper.do_step(-gyro_input)
                    print("gyro: " + str(data))


try:
    reader_th = BTReaderThread().start()
    while 1:
        sleep(1)
except KeyboardInterrupt:
    looping = False
    print("Ending")
    stepper.stepper.cleanup()

