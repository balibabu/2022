import math

a=5
b=6
c=3
root1=-b+pow(b**2-4*a*c,0.5)
root2=-b-pow(b**2-4*a*c,0.5)
print('root1=',root1,'root2=',root2)

x=5
y=8
result=(2*x*y-9*y)/(2*x*pow(y,3))-(4*y*x**2)/(2*y)
print('result=',result)

v=100
result=2*math.cos((x+y)/2)*math.cos((x-y)/2)+math.e**x-1-x/4+math.tan(x)-math.log10(v)
print('result=',result)
