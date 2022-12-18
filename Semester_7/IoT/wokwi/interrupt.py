from machine import Pin
import utime

leds=[Pin(i+1,Pin.OUT) for i in range(4)]
button=Pin(16,Pin.IN)

def glow(bulb,duration=.5):
    bulb.value(1)
    utime.sleep(duration)
    bulb.value(0)

def buttonListener(pin):
    global currentLed
    button.irq(handler=None)
    print(pin,currentLed)
    glow(Pin(15,Pin.OUT),5)
    glow(currentLed)


# test=Pin(4,Pin.OUT)
currentLed=None
while True:
    for led in leds:
        button.irq(trigger=Pin.IRQ_RISING, handler=buttonListener)
        # test.irq(trigger=Pin.IRQ_RISING, handler=buttonListener) # when turn of pin test will come, interrupt would be called
        currentLed=led
        glow(led)

