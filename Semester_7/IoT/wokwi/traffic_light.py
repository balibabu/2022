from machine import Pin
import utime

def glow(bulb,duration=0.1):
    bulb.value(1)
    utime.sleep(duration)
    bulb.value(0)

red=Pin(1,Pin.OUT)
yellow=Pin(2,Pin.OUT)
green=Pin(3,Pin.OUT)
durations=[5,2,7]
button=Pin(4,mode=Pin.IN, pull=Pin.PULL_DOWN)

lights=[red,yellow,green]

while True:
    for light,duration in zip(lights,durations):
        c=0
        while c<duration*10:
            c+=1
            glow(light)
            while button.value()==1:
                glow(red,duration=5)
                


