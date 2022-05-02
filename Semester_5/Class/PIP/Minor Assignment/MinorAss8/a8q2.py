'''2. Write a recursive function to print the sum of the digits of a given non-negative
integer.'''
def sum_of_digit(num):
    '''sum of digits using recursion'''
    if num//10==0:
        return num
    else:
        return num%10+sum_of_digit(num//10)

num=int(input("enter a number: "))
print('sum of digits is',sum_of_digit(num))
