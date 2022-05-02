'''. For a given x and a given n, write a python program to compute xn/n!'''
def factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

print('enter the the value of x and y')
x=int(input('x='))
n=int(input('n='))
value=(x**n)/factorial(n)
print('x^n/n!=',value)