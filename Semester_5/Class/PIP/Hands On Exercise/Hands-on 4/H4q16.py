'''Write a python program to check a number n is prime or not. The number to be inputted through
keyboard'''
def isPrime(n):
    for i in range(2,n//2+1):
        if n%i==0: return False
    return True

num=int(input("enter a number "))
print("is this prime number?",isPrime(num))
