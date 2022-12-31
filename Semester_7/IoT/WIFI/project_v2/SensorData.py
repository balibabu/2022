from dht import DHT11
from bmp280 import *
from machine import Pin, I2C
class Data:
    sensor=DHT11(Pin(28))
    bus = I2C(1,scl=Pin(3),sda=Pin(2),freq=200000)
    bmp = BMP280(bus)
    bmp.use_case(BMP280_CASE_INDOOR)
    ERROR=-3

    def getAltitude(self):
        pressure_in_hectopascal =self.pressure=self.bmp.pressure * 0.01 + self.ERROR
        local_pressure = pressure_in_hectopascal    # Unit : hPa
        sea_level_pressure = 1013.25 # Unit : hPa
        pressure_ratio = local_pressure / sea_level_pressure
        altitude = 44330*(1-(pressure_ratio**(1/5.255)))
        return round(altitude,2)

    def getTemperature(self):
        return round(self.sensor.temperature,2)

    def getHumidity(self):
        return round(self.sensor.humidity,2)

    def getPressure(self): # in mm of Hg
        pressure=self.bmp.pressure
        p_mmHg=pressure/133.3224
        return round(p_mmHg,2)