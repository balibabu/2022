from machine import Pin
import utime, _thread

pins=[Pin(i,Pin.OUT) for i in range(1,13)]
buttonPin=Pin(16,Pin.IN)
buzzer=Pin(17,Pin.OUT)

redPins=[Pin(i,Pin.OUT) for i in range(1,13,3)]
yellowPins=[Pin(i,Pin.OUT) for i in range(2,13,3)]
greenPins=[Pin(i,Pin.OUT) for i in range(3,13,3)]
greenTime=1
redTime=1
yellowTime=1
pedestrianTime=4
isButtonPressed=False

def interruptListener(pin): # interrupt handler is different in wokwi simulator than hardware
    global interruptMetaData
    global isButtonPressed
    isButtonPressed=True
    buttonPin.irq(handler=None)
    interruptMetaData[1].value(0)
    glowOne(interruptMetaData[0],pedestrianTime)    # glowing red bulb on current side
    glowOne(interruptMetaData[1],interruptMetaData[2])

def switchOff(pins):
    for pin in pins:
        pin.value(0)

def glowAllExcept(pins,_pin=False):
    for pin in pins:
        pin.value(1)
    if _pin: _pin.value(0)

def glowOne(pin,duration=1):
    global isButtonPressed
    if isButtonPressed:
        buzzer.value(1)
        isButtonPressed=False
    pin.value(1)
    utime.sleep(duration)
    pin.value(0)
    buzzer.value(0)

def cycle(pins):
    global interruptMetaData
    for i in range(4):
        buttonPin.irq(trigger=Pin.IRQ_RISING, handler=interruptListener)
        glowAllExcept(redPins,redPins[i])
        interruptMetaData=[redPins[i],greenPins[i],greenTime]
        glowOne(greenPins[i],greenTime)
        interruptMetaData=[redPins[i],yellowPins[i],yellowTime]
        glowOne(yellowPins[i],yellowTime)

interruptMetaData=None

while True:
    cycle(pins)
