'''. Given two numbers d and e are suspected of being consecutive members of the Fibonacci
sequence. Write a python program that will refute or confirm this conjecture.'''
def consecutive_fibo(n1,n2):
    a, b = 0, 1
    while b <= n2:
        if a == n1 and b == n2:
            return 'consecutive'
        a, b = b, a + b
    return 'not consecutive'

n1=int(input('enter 1st number:'))
n2=int(input('enter 2nd number:'))
print('these numbers are:',consecutive_fibo(n1,n2))
