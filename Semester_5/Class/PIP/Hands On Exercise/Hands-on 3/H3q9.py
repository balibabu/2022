'''Write a python program that prompts the user to enter a point (x, y) and checks whether the
point is within the circle centered at (0, 0) with radius 10. For example, (4, 5) is inside the
circle and (9, 9) is outside the circle,
Enter a point with two coordinates: 4 5
Point (4.0, 5.0) is in the circle'''

def isInsideCircle(x,y,r,x1,y1):
    d=pow((x-x1)**2+(y-y1)**2,0.5)
    if d<r: return True
    return False

print("enter a point")
x1=float(input('enter x coordinate '))
y1=float(input('enter y coordinate '))
if isInsideCircle(0,0,10,x1,y1):
    print('Point ({},{}) is inside the circle'.format(x1,y1))
else:
    print('Point ({},{}) is not in the circle'.format(x1,y1))
