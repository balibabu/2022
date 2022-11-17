from machine import Pin 
import utime
class Distance:
    trigger=Pin(2,Pin.OUT)
    echo=Pin(3,Pin.IN)

    def setTriggerEchoPin(trig,ech): 
        Distance.trigger=trig
        Distance.echo=ech

    def calculate():
        trigger=Distance.trigger
        echo=Distance.echo

        trigger.low()   # to make silent if it is working
        utime.sleep_us(2) # silent for 2 micro second
        trigger.high()
        utime.sleep_us(5) # turn on for 5 microsecond
        trigger.low()

        while echo.value()==0:
            signalOff=utime.ticks_us()
        
        while echo.value() == 1:
            signalOn = utime.ticks_us()

        timePassed=signalOn-signalOff
        distance=timePassed*0.0343/2    # 2d=speed_of_sound(343m/s) * time, time is in microsecond(10^-6s)
        return distance