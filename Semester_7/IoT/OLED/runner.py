from machine import Pin
from ball import Ball
push=Pin(2,mode=Pin.IN, pull=Pin.PULL_DOWN)


Ball.ball.oled.text("press button",12,24,1)
Ball.ball.oled.text("to start",22,36,1)
Ball.ball.oled.show()
while True:
    if push.value()==0:
        pass
    else:
        Ball.randomBall()
