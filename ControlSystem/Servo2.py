import RPi.GPIO as GPIO
from time import sleep


class Servo2:
    
    def __init__(self, pin, dt=0.5):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm=GPIO.PWM(self.pin, 50)
        self.pwm.start(7.5)
        time.sleep(dt)
        self.pwm.ChangeDutyCycle(0) 
    
    def set_angle(self, angle, dt=1):
        duty = angle / 18.0 + 2.5
        self.pwm.ChangeDutyCycle(duty)
        GPIO.output(self.pin, True)
        sleep(dt)
        GPIO.output(self.pin, False)
        self.pwm.ChangeDutyCycle(0)
        
    def set_duty(self, duty, dt=1):
        self.pwm.ChangeDutyCycle(duty)
        GPIO.output(self.pin, True)
        sleep(dt)
        GPIO.output(self.pin, False)
        self.pwm.ChangeDutyCycle(0)
            
    def cleanup(self, gpio=False):
        self.pwm.stop()
        if gpio:
            self.GPIO_cleanup()
    
    def GPIO_cleanup(self):
        GPIO.cleanup()

