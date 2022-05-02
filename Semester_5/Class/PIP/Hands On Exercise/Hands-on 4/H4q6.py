'''Write a python program to evaluate the function sin(x) as defined by the infinite series expansion.
sin (x) = x- x3/3! + x5/5! - x7/7! +…
The acceptable error for computation is 10-6
.'''
import math


def sine(x):
    term=x
    sinx=x
    c=3
    while math.fabs(term)>0.0000001:
        term=-term*x*x/(c*(c-1))
        c+=2
        sinx+=term
    return sinx

x=float(input('enter value in radians: '))
print('sinx=',sine(x))