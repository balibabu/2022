from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import _thread,utime

def render(screen,points,color=1):
    for point in points:
        oled.pixel(point[0],point[1],color)

def move(points,x=0,y=0):
    for i in range(len(points)):
        point=points[i]
        points[i]=(point[0]+x,point[1]+y)

def removeOutlier(points):
    for point in points:
        if point[0]<0:
            points.remove(point)

def dino():
    return [(14, 45), (15, 45), (16, 45), (17, 45), (18, 45), (19, 45), (13, 46), (14, 46), (16, 46), (17, 46), (18, 46), (19, 46), (20, 46), (13, 47), (14, 47), (15, 47), (16, 47), (17, 47), (18, 47), (19, 47), (20, 47), (13, 48), (14, 48), (15, 48), (16, 48), (17, 48), (18, 48), (19, 48), (20, 48), (13, 49), (14, 49), (15, 49), (16, 49), (5, 50), (13, 50), (14, 50), (15, 50), (16, 50), (17, 50), (18, 50), (19, 50), (5, 51), (12, 51), (13, 51), (14, 51), (15, 51), (5, 52), (6, 52), (11, 52), (12, 52), (13, 52), (14, 52), (15, 52), (5, 53), (6, 53), (7, 53), (10, 53), (11, 53), (12, 53), (13, 53), (14, 53), (15, 53), (16, 53), (17, 53), (5, 54), (6, 54), (7, 54), (8, 54), (9, 54), (10, 54), (11, 54), (12, 54), (13, 54), (14, 54), (15, 54), (17, 54), (6, 55), (7, 55), (8, 55), (9, 55), (10, 55), (11, 55), (12, 55), (13, 55), (14, 55), (15, 55), (7, 56), (8, 56), (9, 56), (10, 56), (11, 56), (12, 56), (13, 56), (14, 56), (8, 57), (9, 57), (10, 57), (11, 57), (12, 57), (13, 57), (9, 58), (10, 58), (11, 58), (12, 58), (13, 58), (9, 59), (10, 59), (12, 59), (13, 59), (9, 60), (13, 60), (9, 61), (10, 61), (13, 61), (14, 61)]

def getObs():
    height=12 # some random height between 2 and 5
    obstaclePo=[(127, 49), (127, 50), (127, 51), (127, 52), (127, 53), (127, 54), (129, 47), (129, 48), (129, 49), (129, 50), (129, 51), (129, 52), (129, 53), (129, 54), (129, 55), (129, 56), (129, 57), (129, 58), (129, 59), (129, 60), (129, 61), (131, 47), (131, 48), (131, 49), (131, 50), (131, 51), (131, 52), (128, 54), (130, 52)]
    return obstaclePo

def jump(screen,obstaclePoints):
    button=Pin(16,Pin.IN, pull=Pin.PULL_DOWN)
    def up(points):
        for i in range(len(points)):
            point=points[i]
            points[i]=(point[0],point[1]-1)
    def down(points):
        for i in range(len(points)):
            point=points[i]
            points[i]=(point[0],point[1]+1)
    
    di=dino()
    c=0
    while True:
        removeOutlier(obstaclePoints)
        if button.value()==1:
            for i in range(16):
                render(screen,di+obstaclePoints)
                if condition(di,obstaclePoints): return
                screen.show()
                render(screen,di+obstaclePoints,0)
                move(di,y=-2)
                move(obstaclePoints,x=-2)

            for i in range(16):
                render(screen,di+obstaclePoints)
                if condition(di,obstaclePoints): return
                screen.show()
                render(screen,di+obstaclePoints,0)
                move(di,y=2)
                move(obstaclePoints,x=-2)
        else:
            render(screen,di+obstaclePoints)
            if condition(di,obstaclePoints): return
            screen.show()
            #utime.sleep(100)
            render(screen,di+obstaclePoints,0)
            move(obstaclePoints,x=-2)
            
        if c==0: # half screen +- random between 1 to 10
            obstaclePoints+=getObs()
        c=(c+1.5)%60

def condition(dinoPoints,obstaclePoints):
    for point in dinoPoints:
        if point in obstaclePoints:
            return True
    return False

i2c=I2C(0,sda=Pin(0), scl=Pin(1) )
oled=SSD1306_I2C(128,64,i2c)
oled.text("game starts in 3 sec",0,31)
oled.show()
utime.sleep(1)
oled.fill(0)
obstaclePoints=[]
#obstacle(oled,obstaclePoints,0)
jump(oled,obstaclePoints)
# _thread.start_new_thread(obstacle)
oled.fill(1)
oled.text("Game over",0,31,0)
oled.show()