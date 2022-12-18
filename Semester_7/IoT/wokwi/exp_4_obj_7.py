from machine import Pin
import utime

button=Pin(14,Pin.IN)
signal=Pin(15,Pin.OUT)

while True:
    if button.value()==1:
        signal.value(1)
        utime.sleep(0.1)
    else:
        signal.value(0)
        utime.sleep(0.1)
