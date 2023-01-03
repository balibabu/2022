from machine import Pin,I2C
from bmp280 import *
import time

bus = I2C(1,scl=Pin(3),sda=Pin(2),freq=200000)
bmp = BMP280(bus)

bmp.use_case(BMP280_CASE_INDOOR)
ERROR=-3

def findAltitude(pressure_in_hectopascal):
    local_pressure = pressure_in_hectopascal    # Unit : hPa
    sea_level_pressure = 1013.25 # Unit : hPa
    pressure_ratio = local_pressure / sea_level_pressure
    altitude = 44330*(1-(pressure_ratio**(1/5.255)))
    return altitude

while True:
    pressure=bmp.pressure
    pressure_hPa = ( pressure * 0.01 ) + ERROR #hectopascal
    p_bar=pressure/100000
    p_mmHg=pressure/133.3224
    temperature=bmp.temperature
    altitude=findAltitude(pressure_hPa)
    print("Temperature: {} C".format(temperature))
    print("Pressure: {} Pa, {} bar, {} mmHg".format(pressure,p_bar,p_mmHg))
    print("Altitude:%f"%(round(altitude,2)))
    time.sleep(5)