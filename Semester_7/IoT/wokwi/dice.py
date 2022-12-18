from machine import Pin
import utime,urandom

button=Pin(16,Pin.IN)
leds=[Pin(i,Pin.OUT) for i in range(1,8)]
number={1:'4',2:'35',3:'345',4:'1267',5:'12467',6:'123567'}

def glowBulb(strPin,duration=0.1):
    for i in strPin:
        Pin(int(i),Pin.OUT).value(1)
    utime.sleep(duration)
    for i in strPin:
        Pin(int(i),Pin.OUT).value(0)

def button_press(pin):
    button.irq(handler=None)
    utime.sleep(2)
    for i in range(1,8):
        Pin(i,Pin.OUT).value(0)
 
while True:
    button.irq(trigger=Pin.IRQ_RISING, handler=button_press)
    glowBulb(number[int(urandom.uniform(1,7))])
