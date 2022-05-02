'''Write a python program that accepts a positive integer n and reverses the order of its digits'''
def reverse(num):
    rev=0
    while(num):
        rev=rev*10+num%10
        num//=10
    return rev

num=int(input("enter a number "))
print("the reverse number is",reverse(num))
