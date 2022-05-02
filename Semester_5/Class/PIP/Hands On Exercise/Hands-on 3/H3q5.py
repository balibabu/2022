'''Write a python program that takes the x – y coordinates of a point in the Cartesian plane and
prints a message telling either an axis on which the point lies or the quadrant in which it is
found
    if x==0 and y==0:
        print('it is origin')
    if x>=0 and y>=0:
        print("first quadrant")
    elif x<0 and y>=0:
        print("second quadrant")
    elif x<0 and y<0:
        print("third quadrant")
    else:
        print("fourth quadrant")
'''

def quadrant(x,y):
    if x == 0 and y == 0:
        print('it is origin')
    elif x == 0:
        print("it's on y axis")
    elif y == 0:
        print("it's on x axis")
    elif x > 0 and y > 0:
        print("first quadrant")
    elif x < 0 and y > 0:
        print("second quadrant")
    elif x < 0 and y < 0:
        print("third quadrant")
    else:
        print("fourth quadrant")


def main():
    x=float(input("enter x coordinate "))
    y=float(input("enter y coordinate "))
    quadrant(x,y)

if __name__=='__main__':
    main()