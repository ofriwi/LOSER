from PID import PID
import time
from Arduino_Servo2 import Arduino_Servo

class servo_pid:
    def pid_step(self, position):
        self.pid.update(position)
        output = self.pid.output
        print("out="+str(output))
        return output

    def __init__(self, P, I, D, set_point):
        self.pid = PID(P, I, D)
        self.pid.SetPoint=set_point
        self.servo = Arduino_Servo()
        self.last_pos = 90
        
    def do_step(self, x, y):
        position = y
        pid_out = self.pid_step(position)
        motor_out = self.crop(self.last_pos + pid_out, 0, 180)
        self.last_pos = motor_out
        print(['cur = ', self.last_pos])
        self.servo.set_angle(motor_out)

    @staticmethod
    def crop(val, min_val=0, max_val=180):
        if val > max_val:
            val = max_val
        if val < min_val:
            val = min_val
        return val
'''
servo = Arduino_Servo()
poses = [100, 70, 35, 38, 40, 50, 50, 70, 50]
#ALT 1
pid = pid_init(P=0.0, I=1.0, D=0.0, set_point=50.0)
for position in poses:
    #get position from camera
    pid_out = pid_step(position)
    motor_out = crop(pid_step(position) + 50, 0, 180)
    print(motor_out)
    servo.set_angle(motor_out)
    
    

#ALT 2
pid = pid_init(P=0.5, I=0.0, D=0.0, set_point=50.0)
current_angle=0
servo.set_angle(current_angle)
for position in poses:
    #get position from camera
    current_angle = crop(current_angle+pid_step(position), 0, 180)
    print(current_angle)
    servo.set_angle(current_angle)
servo.cleanup()
'''