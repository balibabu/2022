def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
num=int(input("enter no. of term "))
for i in range(num):
    print(fib(i),end=' ')
