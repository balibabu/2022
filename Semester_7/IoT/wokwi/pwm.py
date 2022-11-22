<<<<<<< HEAD
from machine import Pin,PWM
import utime

led=Pin(1,Pin.OUT)
pwm=PWM(led)
pwm.freq(1000)

brightness=0
increment=2
while True:
    brightness+=increment
    if brightness>68718:
        increment*=-1
    if brightness<0:
        increment*=-1
    pwm.duty_u16(brightness)
    utime.sleep(0.0001)


#68718  is the max value, greater than this start from 0 again

=======
from machine import Pin,PWM
import utime

led=Pin(1,Pin.OUT)
pwm=PWM(led)
pwm.freq(1000)

brightness=0
increment=2
while True:
    brightness+=increment
    if brightness>68718:
        increment*=-1
    if brightness<0:
        increment*=-1
    pwm.duty_u16(brightness)
    utime.sleep(0.0001)


#68718  is the max value, greater than this start from 0 again

>>>>>>> 909cd7b68f3944ae7d9852f3fe00e99581b331fb
