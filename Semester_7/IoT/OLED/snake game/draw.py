from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import math,utime

class Draw: # x and y axis
    i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
    oled = SSD1306_I2C(128, 64, i2c)
    glow=1

    def show(self):
        self.oled.show()
    def clear(self):
        self.oled.fill(0 if self.glow==1 else 1)

    def point(self,x,y):
        self.oled.pixel(x,y,self.glow)
        # self.oled.show()
    
    def line(self,p1,p2):
        xint=p1[0]-p2[0]
        yint=p1[1]-p2[1]
        if xint==0:
            start=min(p1[1],p2[1])
            for y in range(abs(yint)+1):
                self.oled.pixel(p1[0],start+y,self.glow)
        elif yint==0:
            start=min(p1[0],p2[0])
            for x in range(abs(xint)+1):
                self.oled.pixel(start+x,p1[1],self.glow)
        else:
            m=yint/xint     # slope
            c=p1[1]-m*p1[0]
            for x in range(p1[0],p2[0],1 if p1[0]<p2[0] else -1):
                y=m*x+c
                self.oled.pixel(x,round(y),self.glow)
            
            for y in range(p1[1],p2[1],1 if p1[1]<p2[1] else -1):
                x=(y-c)/m
                self.oled.pixel(round(x),y,self.glow)
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
            self.oled.pixel(x,round(y),self.glow)
            y=b-math.sqrt(r*r-(x-a)*(x-a))
            self.oled.pixel(x,round(y),self.glow)

        for y in range(b-r,b+r+1):
            x=a+math.sqrt(r*r-(y-b)*(y-b))
            self.oled.pixel(round(x),y,self.glow)
            x=a-math.sqrt(r*r-(y-b)*(y-b))
            self.oled.pixel(round(x),y,self.glow)

    def circleFill(self,centre,radius):
        for i in range(radius+1):
            self.circle(centre,i)
            # self.rectangle((centre[0]-i//2,centre[1]-i//2),(centre[0]+i//2,centre[1]+i//2))

    def triangle(self,p1,p2,p3):
        self.line(p1,p2)
        self.line(p1,p3)
        self.line(p2,p3)



'''
# face()
style()
# face()
# liveFace()

obj=Draw()

# obj.rectangle
# obj.rectangle((12,12),(20,20))
# obj.show()
# obj.clear()
# obj.rectangle((12,16),(20,16))


# obj.point(0,0)
# obj.point(127,63)   # 128*64
# # obj.rectangle((35,30),(65,0))
# obj.rectangleFill((12,12),(20,20))
# obj.circle((64,32),20)
# obj.line((20,20),(50,60))
# obj.line((50,60),(20,20))
# obj.line((0,20),(2,50))
# obj.line((40,10),(50,20))
# obj.line((100,10),(50,30))
# obj.triangle((0,0),(30,0),(30,30))

# obj.circleFill((64,32),15)

# obj.rectangleFill((35,30),(65,0))

# c=60
# while True:
#     # obj.line((0,c),(130,c))
#     obj.show()
#     obj.point(0,c)
#     print(c)
#     # obj.rectangle((c,c),(c+15,c+15))
#     c+=1
#     utime.sleep(1)
#     # obj.clear()
    

obj.show()

'''