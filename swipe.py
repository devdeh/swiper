import RPi.GPIO as g
import time

#SETUP#
g.setmode(g.BOARD)
g.setup(32, g.OUT)
g.setup(33, g.OUT)
g.setwarnings(False)
servo1 = g.PWM(32, 50)
servo2 = g.PWM(33, 50)

rgt = 100
lft = 60
tapdown = 110
tapup = 160
tapup2 = 60
sleep_short = 0.1
sleep_long = 0.3
swipe_sleep = 0.008

#INIT#
servo1.start(0)
servo2.start(0)

#FUNCTIONS
def degree(deg):
    pwm = 2+(deg/18)
    if pwm > 2 and pwm < 13: # Range in PWM must be between 0 - 12
        return pwm # Returns correct PWM for degree pos
    else:
        print(" Not a valid angle")
        return 0

def swipe_left(): #up
    # Start position
    servo2.ChangeDutyCycle(degree(lft))
    time.sleep(sleep_short)
    servo1.ChangeDutyCycle(degree(tapup))
    time.sleep(sleep_short)
    
    # Tap down
    servo1.ChangeDutyCycle(degree(tapdown))
    time.sleep(sleep_short/2)
    servo1.ChangeDutyCycle(0)
    
    # Swipe
    i= lft
    while i < rgt:
        servo2.ChangeDutyCycle(degree(i))
        i += 2
        time.sleep(swipe_sleep)
        
    # Tap up
    servo1.ChangeDutyCycle(degree(tapup))
    time.sleep(sleep_short)
    servo1.ChangeDutyCycle(0)
    servo2.ChangeDutyCycle(0)
    
def swipe_right(): #down
    servo2.ChangeDutyCycle(degree(rgt))
    time.sleep(sleep_long)
    servo1.ChangeDutyCycle(degree(tapup))
    time.sleep(sleep_long)        

    # Tap down
    servo1.ChangeDutyCycle(degree(tapdown))
    time.sleep(sleep_short/2)
    servo1.ChangeDutyCycle(0)

   # Swipe
    i= rgt
    while i > lft:
        servo2.ChangeDutyCycle(degree(i))
        i -= 2
        time.sleep(swipe_sleep)
    
    # Tap up
    servo1.ChangeDutyCycle(degree(tapup2))
    time.sleep(sleep_short)
    servo1.ChangeDutyCycle(0)
    servo2.ChangeDutyCycle(0)

def tap_up():
    servo1.ChangeDutyCycle(degree(tapup))
    time.sleep(sleep_long) 
    servo1.ChangeDutyCycle(0)

def tap_down():
    servo1.ChangeDutyCycle(degree(tapdown))
    time.sleep(sleep_long)
    servo1.ChangeDutyCycle(0)
    
def main():
    
    while True:
        use = input("Do you want to go left 'l', right 'r', tap down 'd' or tap up 'u'? ")
        if use == "l":
            swipe_left()
        elif use == "r":
            swipe_right()
        elif use == "d":
            tap_down()
        elif use == "u":
            tap_up()
        else:
            servo1.stop()
            servo2.stop()
            g.cleanup()
            break
main()
