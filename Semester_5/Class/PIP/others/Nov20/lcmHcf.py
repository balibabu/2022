def hcf(a,b):
    if a==0:
        return b
    else:
        return hcf(b%a,a)
def lcm(a,b):
    return a*b/hcf(a,b)

n1=int(input('enter a number '))
n2=int(input('enter 2nd number '))
print('hcf is',hcf(n1,n2))
print('lcm is',lcm(n1,n2))
