from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import math,utime
from draw import Draw

#i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=40000000)
#oled = SSD1306_I2C(128, 64, i2c)
obj=Draw()
obj.line((0,43),(128,43))

def ball(x=0,y=0,visible=1):
    obj.glow=visible
    obj.circle((x+63,y+31),10)
    # obj.show()

def bounce():
    ball(visible=0)
    for i in range(0,30,4):
        ball(y=-i)
        obj.show()
        ball(y=-i,visible=0)
    for i in range(30,0,-4):
        ball(y=-i)
        obj.show()
        ball(y=-i,visible=0)
    

obj.show()
push=Pin(17,mode=Pin.IN, pull=Pin.PULL_DOWN)
led=Pin(25,Pin.OUT)

while True:
    if push.value()==0:
        ball()
        obj.show()
    else:
        bounce()
