from machine import ADC,Pin
import utime

photoResistor=ADC(28)

while True:
    brightness_level=photoResistor.read_u16()
    print((65535-brightness_level)/65535*100,'%')
    utime.sleep(1)
