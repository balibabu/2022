'''Write a python program to compute the sum of the first n terms (n>=1) of the series.
S=1-3+5-7+9-'''

n=int(input('enter a number(n>=1) '))
s=0
for i in range(n):
    s=s+(i*2+1)*(-1)**i

print('sum of first n terms is:',s)