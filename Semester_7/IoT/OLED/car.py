from draw import Draw
import utime
import random

class Car:
    running=True
    def stop(pin):
        Pin(pin,Pin.IN).irq(handler=None)
        Car.running=False

    def road(canva):
        for i in range(128):
            rough=random.randrange(2)
            canva.point(i,50+rough)

    def grass(canva,x=0,y=0,visible=1):
        x%=128
        y%=64
        canva.glow=visible
        canva.line((x+5,y+5),(x+1,y+0)) # \
        canva.line((x+5,y+5),(x+9,y+0)) # /
        canva.line((x+5,y+1),(x+5,y+6)) # |
    def movingGrasses(canva,amount=5,level=0):
        gap=128//amount
        c=128
        while Car.running:
            c-=2
            randomness=0#random.randrange(5)
            for i in range(amount):
                Car.grass(canva,x=gap*i+c+randomness,y=level)
            canva.show()
            for i in range(amount):
                Car.grass(canva,x=gap*i+c+randomness,y=level,visible=0)
        
    def tyers(canva,tpoint1,tpoint2,tsize):
        tsize=int(tsize*3/4)
        def plus(tpoint,visible=0):
            canva.glow=visible
            canva.line((tpoint[0],tpoint[1]-tsize),(tpoint[0],tpoint[1]+tsize))
            canva.line((tpoint[0]-tsize,tpoint[1]),(tpoint[0]+tsize,tpoint[1]))
            
        def cross(tpoint,visible=0):
            canva.glow=visible
            canva.line((tpoint[0]-tsize+1,tpoint[1]-tsize+1),(tpoint[0]+tsize-1,tpoint[1]+tsize-1))
            canva.line((tpoint[0]-tsize+1,tpoint[1]+tsize-1),(tpoint[0]+tsize-1,tpoint[1]-tsize+1))
            canva.line((tpoint[0]-tsize+1,tpoint[1]-tsize),(tpoint[0]+tsize,tpoint[1]+tsize-1))
            canva.line((tpoint[0]-tsize,tpoint[1]+tsize-1),(tpoint[0]+tsize-1,tpoint[1]-tsize))
        
        # while True:
        #     plus(tpoint1)
        #     plus(tpoint2)
        #     canva.show()
        #     plus(tpoint1,visible=1)
        #     plus(tpoint2,visible=1)
        #     cross(tpoint1)
        #     cross(tpoint2)
        #     canva.show()
        #     cross(tpoint1,visible=1)
        #     cross(tpoint2,visible=1)

    def garssAndTyer(canva,tpoint1,tpoint2,tsize,amount=5,level=0):
        tsize=int(tsize*3/4)
        def plus(tpoint,visible=0):
            canva.glow=visible
            canva.line((tpoint[0],tpoint[1]-tsize),(tpoint[0],tpoint[1]+tsize))
            canva.line((tpoint[0]-tsize,tpoint[1]),(tpoint[0]+tsize,tpoint[1]))
            
        def cross(tpoint,visible=0):
            canva.glow=visible
            canva.line((tpoint[0]-tsize+1,tpoint[1]-tsize+1),(tpoint[0]+tsize-1,tpoint[1]+tsize-1))
            canva.line((tpoint[0]-tsize+1,tpoint[1]+tsize-1),(tpoint[0]+tsize,tpoint[1]-tsize))
            canva.line((tpoint[0]-tsize+1,tpoint[1]-tsize),(tpoint[0]+tsize,tpoint[1]+tsize-1))
            canva.line((tpoint[0]-tsize,tpoint[1]+tsize-1),(tpoint[0]+tsize-1,tpoint[1]-tsize))
        
        btnStop=Pin(15,Pin.IN,pull=Pin.PULL_DOWN)
        btnStop.irq(Car.stop,trigger=Pin.IRQ_RISING)
        gap=128//amount
        c=128
        while True:
            c-=2
            randomness=0#random.randrange(5)
            for i in range(amount):
                Car.grass(canva,x=gap*i+c+randomness,y=level)
            plus(tpoint1)
            plus(tpoint2)
            canva.show()
            plus(tpoint1,visible=1)
            plus(tpoint2,visible=1)
            cross(tpoint1)
            cross(tpoint2)
            canva.show()
            cross(tpoint1,visible=1)
            cross(tpoint2,visible=1)
            # canva.show()
            for i in range(amount):
                Car.grass(canva,x=gap*i+c+randomness,y=level,visible=0)
            


    def staticCar():
        # point or corner 1,2,..
        # roof points
        p1=(40,8)
        p2=(80,8)
        # windows and body meeting corners
        p3=(24,24)
        p4=(96,24)
        # back and front upper
        p5=(14,24)
        p6=(112,24)
        #back and front lower   for height -> change y axis
        p7=(p5[0],36)
        p8=(p6[0],36)
        # tyers
        tsize=6
        p9=(p1[0],p7[1])
        p10=(p2[0],p7[1])
        # 2 windows rectangular
        p11=(p1[0]+4,p1[1]+4)
        p12=(p1[0]+(p2[0]-p1[0])//2-1,p3[1])
        p13=(p12[0]+4,p12[1])
        p14=(p2[0]-4,p2[1]+4)
        # 2 windows triangula
        p15=(p1[0],p1[1]+4)
        p16=(p15[0],p3[1])
        p17=(p3[0]+4,p3[1])

        p18=(p2[0],p2[1]+4)
        p19=(p18[0],p3[1])
        p20=(p4[0]-4,p4[1])
        # exhaust pipe
        esize=8
        p21=(p7[0]-esize,p7[1]-esize//4)



        canva=Draw()
        canva.line(p1,p2) #   --------
        canva.line(p3,p1) #  /
        canva.line(p2,p4) #   \
        canva.line(p3,p5)
        canva.line(p4,p6)
        canva.line(p7,p5)
        canva.line(p8,p6)
        canva.line(p8,p7)
        canva.circleFill(p9,tsize)
        canva.circleFill(p10,tsize)
        # windows
        canva.rectangle(p11,p12)
        canva.rectangle(p13,p14)
        # triangular
        canva.triangle(p15,p16,p17)
        canva.triangle(p18,p19,p20)
        # exhaust pipe
        # canva.rectangle(p7,p21)
        Car.road(canva)
        canva.show()

    def dynamicCar():
        # point or corner 1,2,..
        # roof points
        p1=(40,8)
        p2=(80,8)
        # windows and body meeting corners
        p3=(24,24)
        p4=(96,24)
        # back and front upper
        p5=(14,24)
        p6=(112,24)
        #back and front lower   for height -> change y axis
        p7=(p5[0],36)
        p8=(p6[0],36)
        # tyers
        tsize=6
        p9=(p1[0],p7[1])
        p10=(p2[0],p7[1])
        # 2 windows rectangular
        p11=(p1[0]+4,p1[1]+4)
        p12=(p1[0]+(p2[0]-p1[0])//2-1,p3[1])
        p13=(p12[0]+4,p12[1])
        p14=(p2[0]-4,p2[1]+4)
        # 2 windows triangula
        p15=(p1[0],p1[1]+4)
        p16=(p15[0],p3[1])
        p17=(p3[0]+4,p3[1])

        p18=(p2[0],p2[1]+4)
        p19=(p18[0],p3[1])
        p20=(p4[0]-4,p4[1])
        # exhaust pipe
        esize=8
        p21=(p7[0]-esize,p7[1]-esize//4)

        canva=Draw()
        canva.line(p1,p2) #   --------
        canva.line(p3,p1) #  /
        canva.line(p2,p4) #   \
        canva.line(p3,p5)
        canva.line(p4,p6)
        canva.line(p7,p5)
        canva.line(p8,p6)
        canva.line(p8,p7)
        canva.circleFill(p9,tsize)
        canva.circleFill(p10,tsize)
        # windows
        canva.rectangle(p11,p12)
        canva.rectangle(p13,p14)
        # triangular
        canva.triangle(p15,p16,p17)
        canva.triangle(p18,p19,p20)
        # exhaust pipe
        # canva.rectangle(p7,p21)
        # Car.road(canva)
        canva.show()
        # Car.movingGrasses(canva,amount=6,level=45)
        # Car.tyers(canva,p9,p10,tsize)
        Car.garssAndTyer(canva,p9,p10,tsize,amount=6,level=45)
            
