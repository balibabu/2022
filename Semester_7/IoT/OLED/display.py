from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime

class Display:
    i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
    oled = SSD1306_I2C(128, 64, i2c)

    def setSdaSclPin(_sda,_scl):
        Display.i2c=I2C(0,sda=Pin(_sda), scl=Pin(_scl), freq=400000)
        Display.oled = SSD1306_I2C(128, 64, i2c)
    
    def display(content,color=1): 
        # 1 letter consumes 6*6 pixels with 1px padding
        # total 16 letters in a row
        Display.oled.fill(not color)
        row=0
        for i in range(0,len(content)+16,16):
            Display.oled.text(content[i:i+16],0,row,color)
            row+=8
        Display.oled.show()
    
    def formatedDisplay(content,color=1):
        words=content.split()
        toshow=''
        row=0
        for word in words:
            if (len(toshow)+len(word))>16:
                Display.oled.text(toshow,0,row,color)
                row+=8
                toshow=word+' '
            else:
                toshow+=word+' '
        Display.oled.show()
