'''8. Write a recursive function to check whether a given number is prime or not'''
def isPrime(num,temp=2):
    if num == temp:
        return True
    elif num%temp==0:
        return False
    elif num<temp:
        return False
    else:
        return isPrime(num,temp+1)

num=int(input('enter a number:'))
print('is it prime?',isPrime(num))