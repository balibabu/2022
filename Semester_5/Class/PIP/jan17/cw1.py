class Point:
    def __init__(self,x,y):
        self.x = x
        self.y=y

    def __add__(obj1,obj2):
        x=obj1.x+obj2.x
        y=obj1.y+obj2.y
        return Point(x,y)


    def __str__(self):
        return '({},{})'.format(self.x,self.y)

p1=Point(3,6)
p2=Point(2,1)
print(p1+p2)