from machine import Pin,PWM
import utime
red=Pin(3,Pin.OUT)
blue=Pin(2,Pin.OUT)
green=Pin(1,Pin.OUT)
redPwm=PWM(red)
redPwm.freq(1000)
bluePwm=PWM(blue)
bluePwm.freq(1000)
greenPwm=PWM(green)
greenPwm.freq(1000)

def glow(_red,_blu,_gre): # red, blue, green  combination  max(255,255,255)
    if _blu>255 or _red>255 or _gre>255:
        return
    redPwm.duty_u16(int(_red/255*65535))
    bluePwm.duty_u16(int(_blu/255*65535))
    greenPwm.duty_u16(int(_gre/255*65535))
    utime.sleep(0.1)

for i in range(0,255,25):
    for j in range(0,255,25):
        for k in range(0,255,25):
            glow(i,j,k)
            
print('done')
