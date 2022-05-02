'''9. Write a recursive function that multiplies two positive numbers a and b, and returns
the result. Multiplication is to be achieved as a + a + a (b times).'''
def multiply(a,b):
    if b==1:
        return a
    else:
        return a+multiply(a,b-1)

num1=int(input('enter 1st number:'))
num2=int(input('enter 2nd number:'))
print('product of these numbers is',multiply(num1,num2))