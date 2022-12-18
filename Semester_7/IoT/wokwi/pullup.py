from machine import Pin
import math,utime

input1=Pin(16,mode=Pin.IN, pull=Pin.PULL_UP)	
led=Pin(1,Pin.OUT)

while True:
    if input1.value()==0:
        led.value(0)
    else:
        led.value(1)

