from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import math,utime

class Draw: # x and y axis
    i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
    oled = SSD1306_I2C(128, 64, i2c)

    def show(self):
        self.oled.show()
    def clear(self):
        self.oled.fill(0)

    def point(self,x,y):
        self.oled.pixel(x,y,1)
        # self.oled.show()
    
    def line(self,p1,p2):
        xint=p1[0]-p2[0]
        yint=p1[1]-p2[1]
        if xint==0:
            start=min(p1[1],p2[1])
            for y in range(abs(yint)+1):
                self.oled.pixel(p1[0],start+y,1)
        elif yint==0:
            start=min(p1[0],p2[0])
            for x in range(abs(xint)+1):
                self.oled.pixel(start+x,p1[1],1)
        else:
            m=yint/xint     # slope
            c=p1[1]-m*p1[0]
            for x in range(p1[0],p2[0],1 if p1[0]<p2[0] else -1):
                y=m*x+c
                self.oled.pixel(x,round(y),1)
            
            for y in range(p1[1],p2[1],1 if p1[1]<p2[1] else -1):
                x=(y-c)/m
                self.oled.pixel(round(x),y,1)
        # self.oled.show()
    
    
    def rectangleFill(self,point1,point2):
        for x in range(point1[0],point2[0],1 if point1[0]<point2[0] else -1):
            self.rectangle((x,point1[1]),point2)
    
    def rectangle(self,point1,point2):
        p3=point2[0],point1[1]
        p4=point1[0],point2[1]
        self.line(point1,p3)
        self.line(point1,p4)
        self.line(point2,p3)
        self.line(point2,p4)
    
    def circle(self,centre,radius):
        a,b=centre
        r=radius
        for x in range(a-r,a+r+1):
            y=b+math.sqrt(r*r-(x-a)*(x-a))
            self.oled.pixel(x,round(y),1)
            y=b-math.sqrt(r*r-(x-a)*(x-a))
            self.oled.pixel(x,round(y),1)

        for y in range(b-r,b+r+1):
            x=a+math.sqrt(r*r-(y-b)*(y-b))
            self.oled.pixel(round(x),y,1)
            x=a-math.sqrt(r*r-(y-b)*(y-b))
            self.oled.pixel(round(x),y,1)

    def circleFill(self,centre,radius):
        for i in range(radius+1):
            self.circle(centre,i)
            # self.rectangle((centre[0]-i//2,centre[1]-i//2),(centre[0]+i//2,centre[1]+i//2))

    def triangle(self,p1,p2,p3):
        self.line(p1,p2)
        self.line(p1,p3)
        self.line(p2,p3)
