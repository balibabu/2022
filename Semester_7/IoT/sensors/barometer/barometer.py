from bmp280 import *
from machine import Pin, I2C
class Sensor:
    def __init__(self,scl=3,sda=2):
        scl_no=1
        if sda%4==0: scl_no=0
        self.bus=I2C(scl_no,scl=Pin(scl),sda=Pin(sda),freq=200000)
        self.bmp=BMP280(self.bus)
        self.bmp.use_case(BMP280_CASE_INDOOR)
        self.ERROR=-3
        
    def getAltitude(self):
        pressure_in_hectopascal =self.pressure=self.bmp.pressure * 0.01 + self.ERROR
        local_pressure = pressure_in_hectopascal    # Unit : hPa
        sea_level_pressure = 1013.25 # Unit : hPa
        pressure_ratio = local_pressure / sea_level_pressure
        altitude = 44330*(1-(pressure_ratio**(1/5.255)))
        return round(altitude,2)

    def getTemperature(self):
        return round(self.bmp.temperature,2)

    def getPressure(self): # in mm of Hg
        pressure=self.bmp.pressure
        p_mmHg=pressure/133.3224
        return round(p_mmHg,2)