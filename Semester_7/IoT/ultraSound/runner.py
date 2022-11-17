from machine import Pin
from display import Display
from distance import Distance
import utime

calulateBtn = Pin(16, Pin.IN, pull=Pin.PULL_DOWN)
Display.display("Press the button to calculate distance")
while True:
    if calulateBtn.value()==1:
        dis=Distance.calculate()
        Display.display(f"the distance from the object is {dis} cm")
        utime.sleep(1)
