from machine import Pin
from draw import Draw
import random, utime, math
class Ball:
    ball=Draw()
    ball.clear()

    def createBall(canva,centre,radius,visible=1):
        canva.glow=visible
        canva.circle(centre,radius)

    def randomBall():
        Ball.ball.clear()
        radius=random.randrange(1,30)
        centre=random.randrange(radius,128-radius),random.randrange(radius,64-radius)
        Ball.ball.circle(centre, radius)
        Ball.ball.show()
        
    def game(buttonPin):
        push=Pin(buttonPin,mode=Pin.IN, pull=Pin.PULL_DOWN)
        Ball.ball.oled.text("press button",12,24,1)
        Ball.ball.oled.text("to start",22,36,1)
        Ball.ball.oled.show()
        while True:
            if push.value()==0:
                pass
            else:
                Ball.randomBall()

    def wallpaper(times=1,changeTime=.5):
        for i in range(times):
            Ball.randomBall()
            utime.sleep(changeTime)

    def bounceBall(buttonPin):
        def bounce():
            radius=10
            centre=(63,60-radius)
            canva=Draw()
            line=centre[1]+radius+2
            canva.line((0,line),(128,line))
            Ball.createBall(canva, centre, radius)
            canva.show()
            # using realistic approach (i.e. gravity)
            g=-10 # for upward direction (against gravity)
            h=2 # 2 pixel up
            u=5 # initial velocity 100px per second
            total_heigth=40 # pixels to travel in upward direction
            constant=total_heigth/1.25 # reasons for time 1 sec up down
            tim=0
            heightList=[]
            t=0.03
            while total_heigth>0:
                heightList.append(centre)
                h=u*t+0.5*g*t*t
                # heightList.append(h)
                try:
                    v=math.sqrt(u*u+2*g*h)
                except:
                    break
                Ball.createBall(canva, centre, radius,0)
                centre=(centre[0],round(centre[1]-h*constant))
                # heightList.append(centre)
                Ball.createBall(canva, centre, radius)
                canva.show()
                utime.sleep(t)
                u=v
                total_heigth-=round(h*constant)
            Ball.createBall(canva, centre, radius,0)
            for i in range(len(heightList)):
                centre=heightList.pop()
                Ball.createBall(canva, centre, radius)
                canva.show()
                Ball.createBall(canva, centre, radius,0)
                utime.sleep(t)



        push=Pin(buttonPin,mode=Pin.IN, pull=Pin.PULL_DOWN)
        bounce()
        while True:
            if push.value()==0:
                pass
            else:
                bounce()


    def withOutGravity(buttonPin):
        def bounce():
            ball(visible=0)
            for i in range(0,30,4):
                ball(y=-i)
                obj.show()
                ball(y=-i,visible=0)
            for i in range(30,0,-4):
                ball(y=-i)
                obj.show()
                ball(y=-i,visible=0)
                
        push=Pin(buttonPin,mode=Pin.IN, pull=Pin.PULL_DOWN)
        bounce()
        while True:
            if push.value()==0:
                pass
            else:
                bounce()
        

    
            