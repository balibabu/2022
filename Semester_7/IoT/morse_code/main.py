from machine import Pin
import utime
# morse code : 0 - dot and 1 - dash
coded={'A': '01', 'B': '1000', 'C': '1010', 'D': '100', 'E': '0', 'F': '0010',
 'G': '110', 'H': '0000', 'I': '00', 'J': '0111', 'K': '101', 'L': '0100', 'M': '11',
 'N': '10', 'O': '111', 'P': '0110', 'Q': '1101', 'R': '010', 'S': '000', 'T': '1', 
 'U': '001', 'V': '0001', 'W': '011', 'X': '1001', 'Y': '1011', 'Z': '1100',
 '0': '11111', '1': '01111', '2': '00111', '3': '00011', '4': '00001',
  '5': '00000', '6': '10000', '7': '11000', '8': '11100', '9': '11110'}

# 1000, 01, 0100, 00 => bali
# 0000,0,0100,0100,111,011,111,010,0100,100 => hello world

led=Pin(0,Pin.OUT)
led.value(0)



def blink_dot():
  led.toggle()
  utime.sleep(0.2)
  led.toggle()
  utime.sleep(0.4)

def blink_dash():
  led.toggle()
  utime.sleep(0.6)
  led.toggle()
  utime.sleep(0.4)

def letter(ch):
  code=coded[ch] if ch in coded else ''
  for i in code:
    blink_dot() if i=='0' else blink_dash()
  
  
def word(str1):
  str1=str1.upper()
  for i in str1:
    if i==' ':
      utime.sleep(1)
      continue
    letter(i)
    utime.sleep(0.6)

while True:
  word('hello world')