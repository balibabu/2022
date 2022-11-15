from machine import Pin
import utime, _thread

isPressed=0

def clickListener(button):
    global isPressed
    while True:
        if button.value()==0: isPressed=0
        else: isPressed=1

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

_thread.start_new_thread(clickListener,(button,))

while True:
    for light,duration in zip(lights,durations):
        c=0
        while c<duration*10:
            c+=1
            glow(light)
            while isPressed==1:
                glow(red,duration=5)
            

