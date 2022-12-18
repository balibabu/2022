from machine import Pin
import utime, urandom

pushButton=Pin(16,Pin.IN)
weekName=['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
weekPins={'sunday':1, 'monday':2, 'tuesday':3, 'wednesday':4, 'thursday':5, 'friday':6, 'saturday':7}

def buttonAction(pin):
    global randomNumber
    pushButton.irq(handler=None)
    print('Your lucky day of the week is',weekName[randomNumber])
    utime.sleep(5)

def glowBulb(pinNumber):
    Pin(pinNumber,Pin.OUT).value(1)
    utime.sleep(0.01)
    Pin(pinNumber,Pin.OUT).value(0)

randomNumber=1
while True:
    randomNumber=int(urandom.uniform(0,7))
    glowBulb(weekPins[weekName[randomNumber]])
    pushButton.irq(trigger=Pin.IRQ_RISING, handler=buttonAction)
