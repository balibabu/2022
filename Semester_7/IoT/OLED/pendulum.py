from draw import Draw
import math
def pie(deg): return deg*math.pi/180 # converts degree into radian (pi)

def pendulum():
    obj=Draw()
    centre=(63,10)
    length=40
    theta=60
    displac=1
    while True:
        point2=(centre[0]+round(length*math.cos(pie(theta))),centre[1]+round(length*math.sin(pie(theta))))
        obj.line(centre,point2)
        obj.circleFill(point2,5)
        obj.show()
        obj.clear()
        theta+=displac
        if theta>=135: displac=-1
        elif theta<=45: displac=1
        if theta<90: displac+=1
        elif theta>90: displac-=1
        
pendulum()

        
