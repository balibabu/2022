'''Define a class ComplexNumbers. Write operations for addition, subtraction, and multiplication, using
the notion of operator overloading.
'''
class ComplexNumber:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(obj1,obj2):
        return ComplexNumber(obj1.x+obj2.x,obj1.y+obj2.y)
    def __sub__(obj1,obj2):
        return ComplexNumber(obj1.x-obj2.x,obj1.y-obj2.y)
    def __mul__(obj1,obj2):
        a,b=obj1.x,obj1.y
        c,d=obj2.x,obj2.y
        return ComplexNumber(a*c-b*d,a*d+c*b)
    def __str__(self):
        return str(self.x)+'+'+str(self.y)+'i'

n1=ComplexNumber(8,3)
n2=ComplexNumber(2,1)
print('n1 = ',n1)
print('n2 = ',n2)
print('n1+n2 =',n1+n2)
print('n1*n2 =',n1*n2)
print('n1-n2 =',n1-n2)