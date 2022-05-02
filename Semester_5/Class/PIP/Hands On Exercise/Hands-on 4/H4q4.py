'''Input a number n, write a python program to compute n factorial (written as n!) where n>=0.'''
num=int(input('enter a number '))
factorial=1
for i in range(1,num+1):
    factorial*=i

print('factorial of the number is',factorial)