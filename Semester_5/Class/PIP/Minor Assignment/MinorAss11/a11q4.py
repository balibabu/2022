'''
4. Write a class Point having x and y coordinates as data members. Write another class LineSegment
that derives the class Point Also, list appropriate methods.
'''

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y=y
    def __str__(self):
        return '({},{})'.format(self.x,self.y)

class LineSegment(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def length(self,other):
        distance = pow(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2),0.5)
        return distance



ob1 = LineSegment(0, 0)
ob2 = LineSegment(8, 6)
print(LineSegment.length(ob1, ob2))