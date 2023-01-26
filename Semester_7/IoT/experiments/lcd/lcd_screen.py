from machine import I2C, Pin
import utime
from pico_i2c_lcd import I2cLcd

class Screen:

    def __init__(self,scl=3,sda=2):
        scl_no=1
        if sda%4==0: scl_no=0
        i2c = I2C(scl_no, sda=Pin(sda), scl=Pin(scl), freq=400000)
        I2C_ADDR = i2c.scan()[0]
        self.lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

    def display(self,string):
        self.lcd.putstr(string)

    def clear(self):
        self.lcd.clear()