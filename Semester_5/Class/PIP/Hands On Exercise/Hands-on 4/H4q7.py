'''Write a python program to evaluate the function cos(x) as defined by the infinite series expansion.
cos (x) =1- x2/2! + x4/4! - x6/6! +….
The acceptable error for computation is 10-6
.'''
import math
def cosine(x):
    term=1
    cosx=1
    c=2
    while math.fabs(term)>0.0000001:
        term*=-x*x/((c-1)*c)
        c+=2
        cosx+=term
    return cosx

x=float(input('enter value in radians: '))
print('cosx=',cosine(x))

