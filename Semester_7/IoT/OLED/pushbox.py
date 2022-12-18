from draw import Draw
from machine import Pin
class PushBox:

    def cursor(x=0,y=0,visible=1):
        obj=Draw()
        obj.clear()
        p1=((54+x)%128,(26+y)%64)
        p2=((54+x)%128,(42+y)%64)
        p3=((69+x)%128,(37+y)%64)
        p4=((59+x)%128,(38+y)%64)
        p5=((64+x)%128,(37+y)%64)
        p6=((61+x)%128,(43+y)%64)
        p7=((65+x)%128,(42+y)%64)
        
        obj.line(p1,p2)
        obj.line(p1,p3)
        obj.line(p2,p4)
        obj.line(p3,p5)
        obj.line(p4,p6)
        obj.line(p5,p7)
        obj.line(p6,p7)
        
        return obj

    def box(x=0,y=0,visible=1):
        obj=Draw()
        obj.clear()
        p1=((54+x)%128,(22+y)%64)
        p2=((74+x)%128,(42+y)%64)
        obj.line(p1,p2)
        obj.line((p1[0],(p1[1]+20)%64),(p2[0],(p2[1]-20)%64))
        obj.rectangle(p1,p2)
        return obj
        
    def controller(up,down,left,right):
        upBtn=Pin(up,mode=Pin.IN, pull=Pin.PULL_DOWN)
        downBtn=Pin(down,mode=Pin.IN,pull=Pin.PULL_DOWN)
        leftBtn=Pin(left,mode=Pin.IN,pull=Pin.PULL_DOWN)
        right=Pin(right,mode=Pin.IN,pull=Pin.PULL_DOWN)

        x,y=0,0
        PushBox.box().show()
        while True:
            if upBtn.value()==1:
                PushBox.box(x,y,0)
                y-=1
                PushBox.box(x,y,1).show()
            elif downBtn.value()==1:
                PushBox.box(x,y,0)
                y+=1
                PushBox.box(x,y,1).show()
            elif leftBtn.value()==1:
                PushBox.box(x,y,0)
                x-=1
                PushBox.box(x,y,1).show()
            elif right.value()==1:
                PushBox.box(x,y,0)
                x+=1
                PushBox.box(x,y,1).show()

    def cursor(up,down,left,right):
        upBtn=Pin(up,mode=Pin.IN, pull=Pin.PULL_DOWN)
        downBtn=Pin(down,mode=Pin.IN,pull=Pin.PULL_DOWN)
        leftBtn=Pin(left,mode=Pin.IN,pull=Pin.PULL_DOWN)
        right=Pin(right,mode=Pin.IN,pull=Pin.PULL_DOWN)

        x,y=0,0
        PushBox.cursor().show()
        while True:
            if upBtn.value()==1:
                PushBox.cursor(x,y,0)
                y-=1
                PushBox.cursor(x,y,1).show()
            elif downBtn.value()==1:
                PushBox.cursor(x,y,0)
                y+=1
                PushBox.cursor(x,y,1).show()
            elif leftBtn.value()==1:
                PushBox.cursor(x,y,0)
                x-=1
                PushBox.cursor(x,y,1).show()
            elif right.value()==1:
                PushBox.cursor(x,y,0)
                x+=1
                PushBox.cursor(x,y,1).show()
            



