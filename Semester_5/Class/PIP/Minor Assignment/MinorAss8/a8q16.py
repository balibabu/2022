'''16. Write a recursive function that takes two numbers as input parameters and computes
their greatest common divisor'''
def hcf(a,b):
    if a==0:
        return b
    else:
        return hcf(b%a,a)

num1=int(input("enter 1st number "))
num2=int(input("enter 12nd number "))
print("the gcd of given numbers is",hcf(num1,num2))