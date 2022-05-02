'''A perfect number is one whose divisors add up to the number.
Example: The first perfect number is 6. because 1, 2, and 3 are its proper divisors, and 1+2+3=6
Write a python program that prints all perfect numbers in between 1 and 500.'''
def isPerfect(num):
    if num==1: return True
    sum1=0
    for i in range(1,num//2+1):
        if(num%i==0): sum1+=i
    return sum1==num

num=int(input('enter a number '))
print('Is it perfect number?',isPerfect(num))