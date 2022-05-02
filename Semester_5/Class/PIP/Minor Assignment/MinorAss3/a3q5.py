def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)

n1=int(input('enter a number '))
n2=int(input('enter 2nd number '))
print('greatest common divisor is',gcd(n1,n2))
