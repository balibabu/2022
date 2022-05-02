'''Write a python program to generate the first n terms of the sequence without using multiplication.
1 2 4 8 16 32 ……….'''

num=int(input("enter no. of terms "))
for i in range(num):
    print(2**i,end=' ')
