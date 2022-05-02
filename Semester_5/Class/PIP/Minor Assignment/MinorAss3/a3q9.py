def sum_of_digits(n):
    sumd=0
    while(n):
        sumd+=n%10
        n//=10
    return sumd
num=int(input('enter a number '))
print('sum of digits is',sum_of_digits(num))