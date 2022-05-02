def max3(a,b,c):
    def max2(a,b):
        if a>b: return a
        return b
    return max2(max2(a,b),c)


def main():
    a=int(input("enter 1st number "))
    b=int(input("enter 2nd number "))
    c=int(input("enter 3rd number "))
    print("the maximum number is",max3(a,b,c))


if __name__=='__main__':
    main()

