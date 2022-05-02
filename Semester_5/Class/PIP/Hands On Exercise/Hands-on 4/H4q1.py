'''Write a python program that takes the value of N through keyboard and prints a table of the power
of 2 that are less than or equal to 2N.'''

num=int(input('enter a number\n'))
for i in range(num):
    print('{0:<5} {1:<5}'.format(i,2**i))