from machine import Pin, I2C, UART
import time

    
WiFi_SSID='Bali'              # Wifi_SSID
WiFi_password = '12345678'      # WiFi Password
TCP_ServerIP = "184.106.153.149"   # Thingspeak IP address
Port = '80'                        # Thingspeak port
API_KEY = "HBXPTW1EQ3LM5IGH"       # API Key
REFRESH_RATE=3

uart = UART(0, 115200)           # Default Baud rate

trigger = Pin(4, Pin.OUT)
echo = Pin(5, Pin.IN)

def sendAT(cmd,ack,timeout=2000):
    uart.write(cmd+'\r\n')
    t = time.ticks_ms()
    while (time.ticks_ms() - t) < timeout:
        s=uart.read()
        if(s != None):
            s=s.decode("utf-8")
            print(s)
            if(s.find(ack) >= 0):
                return True
    return False


def send_data(temperature,humidity,pressure,altitude):    
    data="GET /update?key="+API_KEY+"&field1=%s&field2=%s&field3=%s&field4=%f"%(temperature,humidity,pressure,altitude)+"\r\n"
    final=len(data)
    reading=0
    sendAT("AT+CIPSTART=\"TCP\",\""+TCP_ServerIP+"\","+Port,"OK",5000)
    sendAT("AT+CIPSEND="+str(final)+"\r\n","OK")
    time.sleep(0.5)
    uart.write(data)
    print(data)
    sendAT('AT+CIPCLOSE'+'\r\n',"OK")
    
 
sendAT("AT","OK")
sendAT("AT+CWMODE=1","OK")
sendAT("AT+CWJAP=\""+WiFi_SSID+"\",\""+WiFi_password+"\"","OK",20000)
sendAT("AT+CIFSR","OK")

############ BMP280 Sensor ##################
from bmp280 import *
bus = I2C(1,scl=Pin(3),sda=Pin(2),freq=200000)
bmp = BMP280(bus)
bmp.use_case(BMP280_CASE_INDOOR)
def findAltitude(pressure_in_hectopascal):
    local_pressure = pressure_in_hectopascal    # Unit : hPa
    sea_level_pressure = 1013.25 # Unit : hPa
    pressure_ratio = local_pressure / sea_level_pressure
    altitude = 44330*(1-(pressure_ratio**(1/5.255)))
    return altitude

############ DHT11 Sensor ##################
from dht import DHT11
sensor=DHT11(Pin(28))

while True:
    pressure=bmp.pressure
    p_mmHg=pressure/133.3224
    pressure_hPa = ( pressure * 0.01 )
    altitude=findAltitude(pressure_hPa)
    humi, temp = sensor.humidity, sensor.temperature

    send_data(temp,humi,p_mmHg,round(altitude,2))
    time.sleep(REFRESH_RATE)
        