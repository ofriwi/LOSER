from PID import PID
import time
from Arduino_Stepper import Arduino_Stepper
from Constants import *

class stepper_pid:
    
    # Calculate next PID value
    def pid_step(self, position):
        self.pid.update(position)
        output = self.pid.output
        if DEBUG_MODE or STEPPER_DEBUG_MODE:
            print('PID output is:', output)
        return output

    # Initialize
    def __init__(self, P, I, D, set_point=0.0):
        self.pid = PID(P, I, D)
        self.pid.SetPoint=set_point
        self.pid.setWindup(STEPPER_MIN_STEP_DEG, STEPPER_MAX_STEP_DEG)  # Ensure output in servo's range
        self.stepper = Arduino_Stepper()
            
    # Do the next thing
    def do_step(self, x):
        position = x
        motor_out = self.pid_step(position)
        if DEBUG_MODE or STEPPER_DEBUG_MODE:
            print('Before cropping, stepper output is:', motor_out, 'deg')
        self.stepper.move(motor_out)
