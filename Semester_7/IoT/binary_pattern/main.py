from machine import Pin
import utime

def nextBinary(arr):
    n=len(arr)
    for i in range(n-1,-1,-1):
        if arr[i]==0:
            arr[i]=1
            return arr
        else:
            arr[i]=0
    return arr
    
def glow(leds):
  n=len(leds)
  stats=[0 for _ in range(n)]
  while True:
    for led,stat in zip(leds,stats):
      led.value(stat)
    utime.sleep(1)
    nextBinary(stats)
  

led_list=[
  Pin(0,Pin.OUT),
  Pin(1,Pin.OUT),
  Pin(2,Pin.OUT),
  Pin(3,Pin.OUT),
  Pin(4,Pin.OUT),
  Pin(5,Pin.OUT)
  ]
  
glow(led_list)