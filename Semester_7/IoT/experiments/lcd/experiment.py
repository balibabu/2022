from lcd_screen import Screen
from barometer import Sensor
import utime

sensor=Sensor(sda=18,scl=19)
screen=Screen(sda=0,scl=1)

while True:
    screen.clear()
    screen.display('Room Temperature is '+str(sensor.getTemperature())+' celcius')
    utime.sleep(2)
