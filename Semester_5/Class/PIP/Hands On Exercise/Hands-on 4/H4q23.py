'''Input an integer n. Write a python program that will find the smallest exact divisor other than
one.'''
def smallestDivisor(num):
    for i in range(2,num+1):
        if num%i==0: return i

    return 1

n=int(input('enter a number '))
print(smallestDivisor(n))