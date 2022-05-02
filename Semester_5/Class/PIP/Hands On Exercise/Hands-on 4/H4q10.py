'''Write a python program to generate and print the first n terms of the Fibonacci numbers using an
efficient algorithm'''
def fibonacci(n):
    a,b=0,1
    print('Fibonacci series is:',end='')
    for i in range(n):
        print(a,',',b,end='')
        b,a=a+b,b

num=int(input("enter no. of term "))
fibonacci(num)