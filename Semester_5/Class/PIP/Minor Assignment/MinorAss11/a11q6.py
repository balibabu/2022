class Shape:
    def __init__(self,shapeType,x,y):
        self.shapeType=shapeType
        self.x=x
        self.y=y
    def computeArea(self):
        pass

class Triangl(Shape):
    def __init__(self,x,y):
        super().__init__('Triangle',x,y)
    def computeArea(self):
        return (self.x*self.y)/2

class Rectangle(Shape):
    def __init__(self,x,y):
        super().__init__('Rectangle',x,y)
    def computeArea(self):
        return self.x*self.y


t1=Triangl(6,5)
print(t1.computeArea())

r1=Rectangle(6,7)
print(r1.computeArea())