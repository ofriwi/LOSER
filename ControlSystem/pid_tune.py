from servo_pid import *
import time

P = 0.8
I = 0.0
D = 0.05
'''
pid = PID(P, I, D)
pid.SetPoint=1
pid.setWindup(0, 180)
pid.setSampleTime(0.1)
servo = Arduino_Servo()
pos = 0
i=0
while 1:
    pid.update(pos)
    pos += pid.output
    print(i)
    print(pos)
    i+=1
    time.sleep(1)
    '''
pid_manager = servo_pid(P, I, D, 10)
pid_manager.pid.SetPoint=100
pid_manager.pid.setWindup(0, 180)
pos = 90
i=0
while 1:
    pos += pid_manager.do_step(0)
    print(i)
    print(pos)
    i+=1
    time.sleep(0.1)
    