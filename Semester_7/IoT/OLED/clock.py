from draw import Draw
import utime,math
class Clock:
    obj=Draw()
    obj.clear()
    centre=(63,31)
    radS=25
    radM=20
    radH=15
    def move(hand,theta,visible=1):
        def pie(deg): return deg*math.pi/180 # converts degree into radian (pi)
        x,y=Clock.centre
        Clock.obj.glow=visible
        Clock.obj.line((x,y),(x+round(hand*math.cos(pie(theta))),y+round(hand*math.sin(pie(theta)))))
        # Clock.obj.line(x+round(hand*math.cos(pie(theta))),y+round(hand*math.sin(pie(theta))))
    
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

