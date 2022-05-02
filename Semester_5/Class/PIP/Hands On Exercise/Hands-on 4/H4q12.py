'''Write a python program to compute the square root of a number using Newton’s method'''

def Newton_root(n):
    x=n/2
    c=x
    while c>0.0000001:
        c=0.5*(x**2-n)/x
        x=x-c
    return x

num=int(input('enter a number '))
print('Square root is',Newton_root(num))
