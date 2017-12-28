
from pid import PID
import time
from servo.Arduino_Servo import Arduino_Servo

def pid_step(position):
    pid.update(position)
    output = pid.output
    return output

def pid_init(P, I, D, set_point):
    pid = PID.PID(P, I, D)
    pid.SetPoint=set_point
    return pid
    
def crop(val, minimum, maximum):
    if (val<minimum):
        val = minimum
    if val>maximum:
        val=maximum
    return val



servo = Arduino_Servo()
poses = [100, 70, 35, 38, 40, 50, 50, 70, 50]
'''ALT 1'''
pid = pid_init(P=0.0, I=1.0, D=0.0, set_point=50.0)
for position in poses:
    '''get position from camera'''
    pid_out = pid_step(position)
    motor_out = crop(pid_step(position) + 50, 0, 180)
    print(motor_out)
    servo.set_angle(motor_out)
    
    

'''ALT 2'''
pid = pid_init(P=0.5, I=0.0, D=0.0, set_point=50.0)
current_angle=0
servo.set_angle(current_angle)
for position in poses:
    '''get position from camera'''
    current_angle = crop(current_angle+pid_step(position), 0, 180)
    print(current_angle)
    servo.set_angle(current_angle)
servo.cleanup()