from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from decoder import Decoder
import utime

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

def plot(matrix,screen):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            screen.pixel(j,i,matrix[i][j])
    screen.show()
    screen.fill(0)

images=open('file.txt').readlines()
for image in images:
    plot(Decoder.decode(image),oled)
    utime.sleep(2)