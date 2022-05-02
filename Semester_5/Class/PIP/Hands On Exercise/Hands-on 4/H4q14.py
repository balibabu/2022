'''Write a python program that reads an integer and displays all its smallest factors in increasing
order. For example, if the input integer is 120, the output should be as follows: 2, 2, 2, 3, 5.'''
def smallest_factors(num):
    a=2;
    while(num>1):
        if(num%a==0):
            print(a,end=',')
            num//=a
        else:
            a+=1

num=int(input("enter a number "))
smallest_factors(num)

