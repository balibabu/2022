from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import _thread,utime
class Dino:
    def __init__(self):
        self.obstaclePoints=[]
        self.jumpHeight=16
        self.obSpeed=2   # obstacle speed
        self.score=0
        self.dinoPoints=[(14, 45), (15, 45), (16, 45), (17, 45), (18, 45), (19, 45), (13, 46), (14, 46), (16, 46), (17, 46), (18, 46), (19, 46), (20, 46), (13, 47), (14, 47), (15, 47), (16, 47), (17, 47), (18, 47), (19, 47), (20, 47), (13, 48), (14, 48), (15, 48), (16, 48), (17, 48), (18, 48), (19, 48), (20, 48), (13, 49), (14, 49), (15, 49), (16, 49), (5, 50), (13, 50), (14, 50), (15, 50), (16, 50), (17, 50), (18, 50), (19, 50), (5, 51), (12, 51), (13, 51), (14, 51), (15, 51), (5, 52), (6, 52), (11, 52), (12, 52), (13, 52), (14, 52), (15, 52), (5, 53), (6, 53), (7, 53), (10, 53), (11, 53), (12, 53), (13, 53), (14, 53), (15, 53), (16, 53), (17, 53), (5, 54), (6, 54), (7, 54), (8, 54), (9, 54), (10, 54), (11, 54), (12, 54), (13, 54), (14, 54), (15, 54), (17, 54), (6, 55), (7, 55), (8, 55), (9, 55), (10, 55), (11, 55), (12, 55), (13, 55), (14, 55), (15, 55), (7, 56), (8, 56), (9, 56), (10, 56), (11, 56), (12, 56), (13, 56), (14, 56), (8, 57), (9, 57), (10, 57), (11, 57), (12, 57), (13, 57), (9, 58), (10, 58), (11, 58), (12, 58), (13, 58), (9, 59), (10, 59), (12, 59), (13, 59), (9, 60), (13, 60), (9, 61), (10, 61), (13, 61), (14, 61)]
        self.newObstaclePoints=[(127, 49), (127, 50), (127, 51), (127, 52), (127, 53), (127, 54), (129, 47), (129, 48), (129, 49), (129, 50), (129, 51), (129, 52), (129, 53), (129, 54), (129, 55), (129, 56), (129, 57), (129, 58), (129, 59), (129, 60), (129, 61), (131, 47), (131, 48), (131, 49), (131, 50), (131, 51), (131, 52), (128, 54), (130, 52)]

    def intro(self,screen):
        screen.text("Game starts",20,22)
        for i in range(3,0,-1):
            screen.text(f"in {i} seconds",15,38)
            screen.show()
            screen.text(f"in {i} seconds",15,38,0)
            utime.sleep(1)
        screen.fill(0)

    def gameOver(self,screen):
        screen.fill(1)
        screen.text("Game Over",20,22,0)
        screen.text(f"Your Score:{self.score//len(self.newObstaclePoints)}",10,38,0)
        screen.show()

    def render(self,screen,points,color=1):
        for point in points:
            screen.pixel(point[0],point[1],color)

    def move(self,points,x=0,y=0):
        for i in range(len(points)):
            point=points[i]
            points[i]=(point[0]+x,point[1]+y)
    
    def removeOutlier(self):
        points=self.obstaclePoints
        for point in points:
            if point[0]<0:
                points.remove(point)
                self.score+=1
    
    def condition(self,dinoPoints,obstaclePoints):
        for point in dinoPoints:
            if point in obstaclePoints:
                return True
        return False
 
    def play(self,up=0,down=0,left=0,right=0):
        def jump(screen,dinoPts,obsPts,y):
            for i in range(self.jumpHeight):
                self.render(screen,dinoPts+obsPts)
                if self.condition(dinoPts,obsPts):  return
                screen.show()
                self.render(screen,dinoPts+obsPts,0)
                self.move(dinoPts,y=y)
                self.move(obsPts,x=-self.obSpeed)

        i2c=I2C(0,sda=Pin(0), scl=Pin(1) )
        screen=SSD1306_I2C(128,64,i2c)
        self.intro(screen)
        button=Pin(up,Pin.IN, pull=Pin.PULL_DOWN)
        c=0
        while True:
            if c==0: # half screen +- random between 1 to 10
                self.obstaclePoints+=self.newObstaclePoints
            c=(c+self.obSpeed)%60

            if button.value()==1:
                jump(screen,self.dinoPoints,self.obstaclePoints,y=-2)
                jump(screen,self.dinoPoints,self.obstaclePoints,y=2)
            else:
                self.render(screen,self.dinoPoints+self.obstaclePoints)
                screen.show()
                self.render(screen,self.dinoPoints+self.obstaclePoints,0)
                self.move(self.obstaclePoints,x=-self.obSpeed)
            if self.condition(self.dinoPoints,self.obstaclePoints): break
            self.removeOutlier()
        self.gameOver(screen)
