from math import sqrt
x1,y1=[float(x) for x in input('enter x1,y1').split()]
x2,y2=[float(x) for x in input('enter x2,y2').split()]
x3,y3=[float(x) for x in input('enter x3,y3').split()]
side1=sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
side2=sqrt((x3-x1)*(x3-x1)+(y3-y1)*(y3-y1))
side3=sqrt((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3))
s=(side1+side2+side3)/2
area=sqrt(s*(s-side1)*(s-side2)*(s-side3))
print(area)

