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

