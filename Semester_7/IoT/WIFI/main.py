from machine import Pin, UART
import utime

uart=UART(0, baudrate=115200,rx=Pin(1),tx=Pin(0))

led=Pin(25,Pin.OUT)
led.value(0)

def ConnectToWifi():
    uart.write("AT+RST\r\n")
    utime.sleep(5)

    uart.write("AT+CWMODE=1\r\n")
    utime.sleep(1)

    uart.write('''AT+CWJAP="ITER BH-8",""\r\n''')
    # uart.write('''AT+CWJAP="Laptop","12345678901"\r\n''')
    # uart.write('''AT+CWJAP="Bali","12345678"\r\n''')
    utime.sleep(5)

    uart.write("AT+CPIMUX=0\r\n")
    utime.sleep(3)

    uart.write('''AT+CIPSTART="UDP","0.0.0.0",5000,5000,2\r\n''')
    utime.sleep(3)

ConnectToWifi()

while True:
    buf=uart.readline()
    dat=buf.decode('UTF-8')
    n=dat.find('LON')
    if n>0:
        led.value(1)
    
    n=dat.find('LOFF')
    if n>0:
        led.value(0)