def isInsideCircle(x,y,r,x1,y1):
    d=pow((x-x1)**2+(y-y1)**2,0.5)
    if d<=r: return True
    return False

print("enter a point")
x1=int(input('enter x coordinate '))
y1=int(input('enter y coordinate '))
print('Is the enter point inside circle?',isInsideCircle(0,0,10,x1,y1))
