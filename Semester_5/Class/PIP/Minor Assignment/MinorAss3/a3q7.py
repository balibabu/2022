def series_a(n,x):
    val,term = 1,1
    for i in range(1, n):
        term = term * (-x * x) / (2 * i * (2 * i - 1))
        val += term
    return val
def series_b(n,x):
    term=1
    val = 1
    for i in range(1, n):
        term=term*x/i
        val += term
    return val

n=int(input('enter no. of terms '))
x=int(input('enter value of x '))


print('the sum of nth term is',series_a(n,x))
print('the sum of nth term of e^x is',series_b(n,x))
