'''Write a python program called PrimeCounter that takes a command line argument N and finds 
the number of primes less than or equal to N.'''
import sys
def isPrime(n):
    if n<=1:
        return False
    for i in range(2,n//2+1):
        if n%i==0: return False
    return True
def primeCounter(n):
    count=0
    for i in range(n+1):
        if isPrime(i): count+=1
    return count

a=int(sys.argv[1])
print('No. of prime less than or equal to {} is {}'.format(a,primeCounter(a)))