import time
import RPi.GPIO as GPIO

pin = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

pwm = GPIO.PWM(pin, 50) #50 pulses per second
pwm.start(7.5) #Centers the servo
time.sleep(0.5) #Allowing the servo to move to the center
pwm.ChangeDutyCycle(0) #The black magic. I'll explain later

#Function that receives an angle from 0 to 180 deg
def angle(degree): 
  if degree < 0: #This 
    degree = 0 
  elif degree > 180: #and this ensures that we're not overshooting
    degree = 180

  duty = (0.05555555*degree) + 2.5 #This converts angle to dutycycle

  pwm.ChangeDutyCycle(duty)
  time.sleep(1)
  pwm.ChangeDutyCycle(0) #Again, black magic

#A simple function to return the servo to center, although it's not really needed
def center(): 
  pwm.ChangeDutyCycle(7.5)
  time.sleep(0.3)
  pwm.ChangeDutyCycle(0)

#Since this is a module, not a script, I like to call this function from another script in order to stop the whole show
def stop(): 
  pwm.ChangeDutyCycle(0)
  pwm.stop()
  GPIO.cleanup()

  print("Servo stopped")
