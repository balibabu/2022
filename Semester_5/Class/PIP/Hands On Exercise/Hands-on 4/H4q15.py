'''Write a python program GCD that finds the greatest common divisor (gcd) of two integers using
Euclid’s algorithm, which is an iterative computation based on the following observation: if x is
greater than y, then if y divides x, the gcd of x and y is y; otherwise, the gcd of x and y is the same
as the gcd of x % y and y.'''

def hcf(a,b):
    if a==0:
        return b
    else:
        return hcf(b%a,a)

num1=int(input("enter 1st number "))
num2=int(input("enter 12nd number "))
print("the gcd of given numbers is",hcf(num1,num2))

