'''13. Write a function which takes co-ordinates of three points as input and returns true if points are
collinear otherwise returns false.'''
def is_collinear(x1,y1,x2,y2,x3,y3):
    
    return (x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))==0

    
print(is_collinear(2,4,4,6,6,8)) #collinear
print(is_collinear(2,4,4,6,6,9)) #non collinear


