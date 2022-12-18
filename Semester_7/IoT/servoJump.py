from time import sleep
from machine import Pin, PWM

pwm = PWM(Pin(1))
pwm.freq(50)

def rotateBy(deg):
    #1000    0
    #4500	 90
    #7500	 180
    duty_cycle=1000+int(((7500-900)/180)*deg)
    pwm.duty_u16(duty_cycle)
    sleep(0.01)

def jump():
    rotateBy(90)
    sleep(1)
    rotateBy(63)
    sleep(.2)
    rotateBy(90)

jump()