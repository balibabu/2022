from machine import Pin
import utime, _thread

def glow(timeperiod,led):
    while True:
        led.toggle()
        utime.sleep(timeperiod)

red=Pin(14,Pin.OUT)
blu=Pin(3,Pin.OUT)
#red.value(1)
#blu.value(1)

_thread.start_new_thread(glow,(.311,red))
#_thread.start_new_thread(glow,(250,blu))
while True:
    blu.toggle()
    utime.sleep(.311)