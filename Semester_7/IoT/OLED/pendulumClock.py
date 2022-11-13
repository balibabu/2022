from draw import Draw
import utime,math,_thread
class Clock:
    obj=Draw()
    obj.clear()
    centre=(63,31)
    radS=25
    radM=20
    radH=15
    def marker(forPendulum=0):
        if forPendulum:
            pass
        else:
            pass

    def move(hand,theta,visible=1):
        def pie(deg): return deg*math.pi/180 # converts degree into radian (pi)
        x,y=Clock.centre
        Clock.obj.glow=visible
        Clock.obj.line((x,y),(x+round(hand*math.cos(pie(theta))),y+round(hand*math.sin(pie(theta)))))
        
    def pendulum(swing):
        def pie(deg): return deg*math.pi/180 # converts degree into radian (pi)
        amplitude=60
        buttomAngl=180
        startAngl=buttomAngl-amplitude//2
        finishAngl=buttomAngl+amplitude//2

        def move(theta,visible=1):
            length1=Clock.radS+3
            length2=length1+40
            x,y=Clock.centre
            Clock.obj.glow=visible
            point1=(x+round(length1*math.cos(pie(theta))),y+round(length1*math.sin(pie(theta))))
            point2=(x+round(length2*math.cos(pie(theta))),y+round(length2*math.sin(pie(theta))))
            Clock.obj.line(point1,point2)
            Clock.obj.circleFill(point2,5)
            
        def leftRight():
            incre=0
            theta=startAngl
            while theta<=finishAngl:
                move(theta)
                Clock.obj.show()
                move(theta,0)
                theta+=incre
                if theta<buttomAngl:
                    incre+=1
                else:
                    incre-=1

        def rightLeft():
            decre=0
            theta=finishAngl
            while theta>=startAngl:
                move(theta)
                Clock.obj.show()
                move(theta,0)
                theta-=decre
                if theta>buttomAngl:
                    decre+=1
                else:
                    decre-=1

        if swing==-1:
            leftRight()
        else:
            rightLeft()

    def start():
        Clock.obj.circleEquationTechnique(Clock.centre,Clock.radS+2)
        while True:
            _time=utime.gmtime()
            hrs,mins,sec=_time[3],_time[4],_time[5]
            secTheta=sec*6-90
            minsTheta=mins*6-90
            hrsTheta=(hrs%12)*30-90
            Clock.move(Clock.radS,secTheta)
            Clock.move(Clock.radM,minsTheta)
            Clock.move(Clock.radH,hrsTheta)
            Clock.obj.show()
            Clock.move(Clock.radS,secTheta,0)
            Clock.move(Clock.radM,minsTheta,0)
            Clock.move(Clock.radH,hrsTheta,0)
    
    def startWithPendulum():
        Clock.centre=(100,31)
        Clock.obj.circleEquationTechnique(Clock.centre,Clock.radS+2)
        alternate=1
        while True:
            _time=utime.gmtime()
            hrs,mins,sec=_time[3],_time[4],_time[5]
            secTheta=sec*6
            minsTheta=mins*6
            hrsTheta=(hrs%12)*30
            Clock.move(Clock.radS,secTheta)
            Clock.move(Clock.radM,minsTheta)
            Clock.move(Clock.radH,hrsTheta)
            Clock.obj.show()
            alternate*=(-1)
            Clock.pendulum(alternate)
            Clock.move(Clock.radS,secTheta,0)
            Clock.move(Clock.radM,minsTheta,0)
            Clock.move(Clock.radH,hrsTheta,0)



