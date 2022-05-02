def sum_of_digit(num):
    '''sum of digits using recursion'''
    if num//10==0:
        return num
    else:
        return num%10+sum_of_digit(num//10)

num=int(input("enter no. of term "))
print('sum of digits is',sum_of_digit(num))
