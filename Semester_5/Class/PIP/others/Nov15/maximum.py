def maximum(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c


def main():
    a=int(input("enter 1st number "))
    b=int(input("enter 2nd number "))
    c=int(input("enter 3rd number "))
    print("the maximum number is",maximum(a,b,c))


if __name__=='__main__':
    main()

