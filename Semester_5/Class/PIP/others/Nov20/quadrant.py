def quadrant(x,y):
    if x>=0 and y>=0:
        print("first quadrant")
    elif x<0 and y>=0:
        print("second quadrant")
    elif x<0 and y<0:
        print("third quadrant")
    else:
        print("fourth quadrant")

def main():
    x=int(input("enter x coordinate "))
    y=int(input("enter y coordinate "))
    quadrant(x,y)

if __name__=='__main__':
    main()
