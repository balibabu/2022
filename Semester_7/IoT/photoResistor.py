from machine import ADC,Pin
import utime

photoResistor=ADC(28)

while True:
    brightness_level=photoResistor.read_u16()
    if brightness_level>8000:
        print(brightness_level)

    utime.sleep(.01)
