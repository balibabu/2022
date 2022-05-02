'''Assume that x is a positive variable of type double. Write a python code fragment that uses the
Taylor series expansion to set the value of sum to ex = 1 + x + x2/2! + x3/3! + ……'''
def epsilon(x):
    term=1
    val = 1
    for i in range(1, 1000):
        term=term*x/i
        val += term
    return val

x=float(input('enter value of x: '))
print('e^x =',epsilon(x))