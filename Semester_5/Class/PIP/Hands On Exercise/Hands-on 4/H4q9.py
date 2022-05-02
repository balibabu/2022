'''Write a python program to generate and print the first n terms of the Fibonacci sequence where n>=1.
The first few terms are:
 0, 1, 1, 2, 3, 5, 8, 13, ....'''
def fibonacci(n):
    a,b=0,1
    print('Fibonacci series is:',a,end='')
    for i in range(n-1):
        print(',',b,end='')
        b,a=a+b,b

    
num=int(input("enter no. of term "))
fibonacci(num)