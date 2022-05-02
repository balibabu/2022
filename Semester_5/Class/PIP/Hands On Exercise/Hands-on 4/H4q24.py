
'''Amicable numbers are pair of numbers each of whose divisors add to the other number.
Example: The smallest pair of amicable numbers is (220, 284). They are amicable because the
proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110, of which the sum is 284; and
the proper divisors of 284 are 1, 2, 4, 71 and 142, of which the sum is 220.
Note: 1 is included as a divisor but the numbers are not included as their own divisors.'''
def isAmicable(a,b):
    '''is sum of all divisors(>n) of first is equal to second'''
    fac=0
    for i in range(1,a):
        if a%i==0: fac+=i

    if fac==b: return True
    fac=0
    for i in range(1,b):
        if b%i==0: fac+=i
    if fac==a: return True
    return False

print('enter a pair of number')
n1=int(input())
n2=int(input())
print(isAmicable(n1,n2))

