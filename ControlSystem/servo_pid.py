from PID import PID
import time
from Arduino_Servo import Arduino_Servo
from Constants import *

class servo_pid:
    
    # Calculate next PID value
    def pid_step(self, position):
        self.pid.setWindup(SERVO_MIN_DEG - self.last_pos, SERVO_MAX_DEG - self.last_pos)  # Ensure output in servo's range
        self.pid.update(position)
        output = self.pid.output
        if DEBUG_MODE or SERVO_DEBUG_MODE:
            print('PID output is:'+ str(output))
        return output

    # Initialize
    def __init__(self, P, I, D, set_point):
        self.pid = PID(P, I, D)
        self.pid.SetPoint=set_point
        self.servo = Arduino_Servo()
        self.last_pos = SERVO_CENTER_DEG
        self.servo.set_angle(SERVO_CENTER_DEG)
            
    # Do the next thing
    def do_step(self, y):
        position = y
        motor_out = self.last_pos + self.pid_step(position)
        if DEBUG_MODE or SERVO_DEBUG_MODE:
            print('Last position was:' + str(self.last_pos))
            print('Before cropping, value is:' + str(motor_out))
        self.last_pos = self.servo.set_angle(motor_out)
        return motor_out
        
class servo_pid_no_last:
    
    # Calculate next PID value
    def pid_step(self, position):
        self.pid.update(position)
        output = self.pid.output
        if DEBUG_MODE or SERVO_DEBUG_MODE:
            print('PID output is:' + str(output))
        return output

    # Initialize
    def __init__(self, P, I, D, set_point=0.0):
        self.pid = PID(P, I, D)
        self.pid.SetPoint=set_point
        self.pid.setWindup(SERVO_MIN_DEG - SERVO_CENTER_DEG, SERVO_MAX_DEG - SERVO_CENTER_DEG)  # Ensure output in servo's range
        self.servo = Arduino_Servo()
        self.servo.set_angle(SERVO_CENTER_DEG)
            
    # Do the next thing
    def do_step(self, y):
        position = y
        motor_out = self.pid_step(position) + SERVO_CENTER_DEG
        if DEBUG_MODE or SERVO_DEBUG_MODE:
            print('\nNo last pos mode')
            print('Before cropping, value is:' + str(motor_out))
        self.servo.set_angle(motor_out)
        return motor_out